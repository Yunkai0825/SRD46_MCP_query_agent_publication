# =============================================================
#  Agent API and agentic loop
# =============================================================

import asyncio
import contextvars
import json
import logging
import threading
import time
import uuid
from dataclasses import dataclass
from typing import Callable, Dict, List, Optional


log = logging.getLogger("SRD46-UI")


_compactor_run_id_var: contextvars.ContextVar[str | None] = contextvars.ContextVar(
    "compactor_run_id",
    default=None,
)

_COMPACTOR_EXTRA_FIELDS = (
    "for_tool",
    "event_kind",
    "round_kind",
    "outcome",
    "candidate_idx",
    "candidate_tool",
    "attempts_used",
    "candidates_selected",
    "candidate_count",
    "tasks_run",
    "context_chars_before",
    "context_chars_after",
    "context_turns_before",
    "context_turns_after",
    "selection_duration_s",
    "round_duration_s",
    "duration_s",
    "original_chars",
    "final_chars",
)


class _CompactorCapture(logging.Handler):
    """Capture compactor events per run context, falling back to per thread."""

    def __init__(self):
        super().__init__(level=logging.DEBUG)
        self._events_by_scope: dict[tuple[str, str | int], list[dict]] = {}
        self._lock = threading.Lock()

    def _scope_key(self, *, run_id: Optional[str] = None, thread_id: Optional[int] = None) -> tuple[str, str | int]:
        resolved_run_id = _compactor_run_id_var.get() if run_id is None else run_id
        if resolved_run_id is not None:
            return ("run", resolved_run_id)
        resolved_thread_id = threading.get_ident() if thread_id is None else thread_id
        return ("thread", resolved_thread_id)

    def emit(self, record: logging.LogRecord) -> None:
        event = {
            "time": record.created,
            "level": record.levelname,
            "message": record.getMessage(),
        }
        for field in _COMPACTOR_EXTRA_FIELDS:
            if hasattr(record, field):
                event[field] = getattr(record, field)
        with self._lock:
            scope_key = self._scope_key(thread_id=record.thread)
            self._events_by_scope.setdefault(scope_key, []).append(event)

    def drain(self, *, run_id: Optional[str] = None, thread_id: Optional[int] = None) -> list[dict]:
        scope_key = self._scope_key(run_id=run_id, thread_id=thread_id)
        with self._lock:
            return list(self._events_by_scope.pop(scope_key, []))


_compactor_capture = _CompactorCapture()
_compactor_logger = logging.getLogger("SRD46-compactor")
if not any(isinstance(h, _CompactorCapture) for h in _compactor_logger.handlers):
    _compactor_logger.addHandler(_compactor_capture)


@dataclass
class AgentRunResult:
    answer: str
    memory: List[Dict[str, str]]
    tool_history: List[dict]
    compactor_events: List[dict]
    elapsed: float


def _build_flat_prompt(memory: List[Dict[str, str]]) -> str:
    parts = []
    for turn in memory:
        tag = "User" if turn["role"] == "user" else "Assistant"
        parts.append(f"## {tag}\n{turn['content']}")
    return "\n\n".join(parts)


def _compact_response_with_tool_call(
    response: str,
    tool_payload: dict,
    tool_call_match,
    reasoning_cap: int,
) -> str:
    if not tool_call_match:
        return response
    tc_xml = f"<tool_call>{json.dumps(tool_payload)}</tool_call>"
    prefix = response[: tool_call_match.start()]
    if len(prefix) > reasoning_cap:
        prefix = prefix[:reasoning_cap] + "\n...[reasoning trimmed]...\n"
    return prefix + tc_xml


def _parse_l0_compression_hints(preplan_result: str) -> dict:
    """Extract l0_compression_hints from a preplan JSON result."""
    try:
        body = preplan_result
        if body.startswith("[PREPLAN]"):
            body = body[body.index("\n") + 1:]
        data = json.loads(body)
        hints = data.get("l0_compression_hints", {})
        return hints if isinstance(hints, dict) else {}
    except Exception:
        return {}


def _phase_error_message(
    tool_name: str,
    *,
    preplan_called: bool,
    plan_called: bool,
    l0_called: set,
    l0_required: set,
    preplan_tool: str,
    plan_tool: str,
    l0_discovery_tools: set,
) -> Optional[str]:
    if tool_name == preplan_tool:
        return None
    if tool_name in l0_discovery_tools:
        if not preplan_called:
            return (
                "[PHASE ERROR] Call 0_preplan_decision first "
                "to triage the question before L0 searches."
            )
        return None
    if tool_name == plan_tool:
        missing = l0_required - l0_called
        if missing:
            return (
                "[PHASE ERROR] Cannot call planner yet. "
                f"You must first call these L0 tools: {', '.join(sorted(missing))}."
            )
        return None
    if not plan_called:
        missing = l0_required - l0_called
        if missing:
            return (
                f"[PHASE ERROR] Tool '{tool_name}' is not available yet. "
                f"Complete PHASE 1 first: call {', '.join(sorted(missing))}, "
                "then call 0_plan_search_strategy."
            )
        if not l0_required and preplan_called:
            return None
        return (
            f"[PHASE ERROR] Tool '{tool_name}' is not available yet. "
            "You must call 0_plan_search_strategy first (PHASE 2) before "
            "using the execution tools."
        )
    return None


async def run_agent_query(
    user_message: str,
    *,
    memory: Optional[List[Dict[str, str]]] = None,
    timeout: int | None = None,
    on_step: Optional[Callable[[dict], None]] = None,
    max_tool_iterations: int | None = None,
) -> AgentRunResult:
    """Run one full user query through the main agent API."""
    from argo_config import MAX_TOOL_ITERATIONS, MAX_TURN_SECONDS, REASONING_CAP
    from argo_client import call_argo
    from agent_runtime import (
        MCPManager,
        L0_DISCOVERY_TOOLS,
        PLAN_TOOL_NAME,
        PREPLAN_TOOL_NAME,
        SYSTEM_PROMPT,
        TOOL_CALL_PATTERN,
        coerce_tool_calls,
        extract_tool_call,
        infer_required_l0_tools,
        mark_plans_complete,
    )
    from SRD46_tools.tool_arg_normalizer import normalize_tool_arguments
    from SRD46_tools.compactor import compact_memory, compact_l0_with_hints, compact_tool_result_immediately

    conversation = memory if memory is not None else []
    conversation.append({"role": "user", "content": user_message})
    tool_history: list[dict] = []
    compactor_events: list[dict] = []
    response = ""
    turn_t0 = time.time()
    turn_timeout = timeout if timeout is not None else MAX_TURN_SECONDS
    max_iterations = max_tool_iterations if max_tool_iterations is not None else MAX_TOOL_ITERATIONS
    if max_iterations <= 0:
        raise ValueError("max_tool_iterations must be a positive integer")
    compactor_run_id = uuid.uuid4().hex
    compactor_run_token = _compactor_run_id_var.set(compactor_run_id)

    _compactor_capture.drain(run_id=compactor_run_id)

    wrap_up_messages = [
        ("[SYSTEM NOTE - First Notice: time budget exceeded] "
         "You have exceeded the time budget for this turn. "
         "You have 3 more chances (including this one) to respond. "
         "You may make one more critical tool call if truly needed, "
         "but start wrapping up. If your data is sufficient, produce a "
         "final answer now. If incomplete, say so and suggest a follow-up."),
        ("[SYSTEM NOTE - Second Notice: time budget exceeded] "
         "This is your second warning. You have ONE more chance after this. "
         "If you still need one critical tool call, make it now - but your "
         "NEXT response MUST be a final answer with no tool calls."),
        ("[SYSTEM NOTE - FINAL NOTICE, time budget exceeded] "
         "This is your LAST chance. You MUST produce a final answer NOW. "
         "Any tool call will be discarded."),
    ]
    wrap_up_warnings = 0

    preplan_called = False
    l0_called: set = set()
    l0_required: set = set(L0_DISCOVERY_TOOLS)
    l0_compression_hints: dict = {}
    l0_compression_done = False
    plan_called = False

    mcp_manager = MCPManager()
    await mcp_manager.setup()
    try:
        for iteration in range(1, max_iterations + 1):
            elapsed_total = time.time() - turn_t0
            if elapsed_total > turn_timeout and wrap_up_warnings == 0:
                wrap_up_warnings = 1
                log.warning("[!] Time limit reached (%.1fs > %ds), wrap-up warning %d/3.",
                            elapsed_total, turn_timeout, wrap_up_warnings)
                conversation.append({"role": "user", "content": wrap_up_messages[0]})
            elif elapsed_total > turn_timeout and wrap_up_warnings >= len(wrap_up_messages):
                log.warning("[!] All wrap-up warnings exhausted (%.1fs). Hard stop.", elapsed_total)
                break

            iter_t0 = time.time()
            flat_prompt = _build_flat_prompt(conversation)
            log.info("[>] agent iter=%d prompt_len=%d memory_turns=%d elapsed=%.1fs",
                     iteration, len(flat_prompt), len(conversation), elapsed_total)

            response = call_argo(flat_prompt, SYSTEM_PROMPT)
            tool_calls = coerce_tool_calls(extract_tool_call(response))

            if not tool_calls:
                plan_skippable = not l0_required and preplan_called
                if not plan_called and not plan_skippable and iteration < max_iterations - 1:
                    log.warning("[!] Agent answered before planner ran. Nudging to continue.")
                    conversation.append({"role": "assistant", "content": response})
                    conversation.append({
                        "role": "user",
                        "content": (
                            "[SYSTEM NOTE] You have NOT completed the mandatory workflow. "
                            "You must call 0_plan_search_strategy (Phase 2) and then use "
                            "the execution tools (Phase 3) to retrieve the actual data "
                            "before giving a final answer. Continue now."
                        ),
                    })
                    continue
                conversation.append({"role": "assistant", "content": response})
                mark_plans_complete(conversation)
                return AgentRunResult(
                    answer=response,
                    memory=conversation,
                    tool_history=tool_history,
                    compactor_events=compactor_events,
                    elapsed=time.time() - turn_t0,
                )

            if wrap_up_warnings > 0:
                wrap_up_warnings += 1
                if wrap_up_warnings > len(wrap_up_messages):
                    log.warning("[!] Tool call after final warning. Forcing final answer.")
                    conversation.append({"role": "assistant", "content": response})
                    conversation.append({
                        "role": "user",
                        "content": (
                            "[SYSTEM NOTE] All tool calls discarded — time budget exhausted. "
                            "Synthesize a COMPLETE final answer from the data you have already "
                            "gathered. Summarize all findings. Do NOT leave sentences unfinished."
                        ),
                    })
                    response = call_argo(_build_flat_prompt(conversation), SYSTEM_PROMPT)
                    conversation.append({"role": "assistant", "content": response})
                    mark_plans_complete(conversation)
                    return AgentRunResult(
                        answer=response,
                        memory=conversation,
                        tool_history=tool_history,
                        compactor_events=compactor_events,
                        elapsed=time.time() - turn_t0,
                    )

                if wrap_up_warnings >= 3:
                    # Warning 2+: block tool execution, force final answer
                    log.warning("[!] Blocking tool execution at warning %d/3. "
                                "Forcing final answer.", wrap_up_warnings - 1)
                    fake_results = "; ".join(
                        f'{c.get("name", "?")}: [DISCARDED — time budget exceeded]'
                        for c in tool_calls
                    )
                    conversation.append({"role": "assistant", "content": response})
                    conversation.append({
                        "role": "user",
                        "content": (
                            f"[SYSTEM NOTE] Tool calls blocked (time budget). "
                            f"Results: {fake_results}. "
                            "Synthesize a COMPLETE final answer from the data you "
                            "have already gathered. Summarize all findings. "
                            "Do NOT leave sentences unfinished."
                        ),
                    })
                    response = call_argo(_build_flat_prompt(conversation), SYSTEM_PROMPT)
                    conversation.append({"role": "assistant", "content": response})
                    mark_plans_complete(conversation)
                    return AgentRunResult(
                        answer=response,
                        memory=conversation,
                        tool_history=tool_history,
                        compactor_events=compactor_events,
                        elapsed=time.time() - turn_t0,
                    )

            log.info("   [iter %d] Tool call(s): %s",
                     iteration, ", ".join(call.get("name", "?") for call in tool_calls))

            tc_match = TOOL_CALL_PATTERN.search(response)
            parsed_payloads = tool_calls
            if tc_match:
                try:
                    parsed_payloads = coerce_tool_calls(json.loads(tc_match.group(1)))
                except Exception:
                    parsed_payloads = tool_calls

            # --- decide parallel vs sequential execution ---
            # Tools whose results gate subsequent phases — must run alone.
            _NEVER_PARALLEL = {
                PREPLAN_TOOL_NAME, PLAN_TOOL_NAME,
                "build_system_catalog",
            }

            tool_names_this_turn = [
                tc.get("name", "") for tc in tool_calls
            ]
            has_phase_errors = any(
                _phase_error_message(
                    n,
                    preplan_called=preplan_called,
                    plan_called=plan_called,
                    l0_called=l0_called,
                    l0_required=l0_required,
                    preplan_tool=PREPLAN_TOOL_NAME,
                    plan_tool=PLAN_TOOL_NAME,
                    l0_discovery_tools=L0_DISCOVERY_TOOLS,
                )
                for n in tool_names_this_turn
            )
            can_parallel = (
                len(tool_calls) > 1
                and not has_phase_errors
                and not any(n in _NEVER_PARALLEL for n in tool_names_this_turn)
            )

            if can_parallel:
                log.info("   [iter %d] Running %d tools in PARALLEL: %s",
                         iteration, len(tool_calls),
                         ", ".join(tool_names_this_turn))

            # --- execute (parallel or sequential) ---
            if can_parallel:
                all_args = [
                    normalize_tool_arguments(
                        tc.get("name", ""),
                        tc.get("arguments", {}),
                    )
                    for tc in tool_calls
                ]
                async def _timed_call(coro):
                    _t0 = time.time()
                    _res = await coro
                    return _res, time.time() - _t0

                timed_results = await asyncio.gather(*(
                    _timed_call(mcp_manager.call_tool_safe(name, args))
                    for name, args in zip(tool_names_this_turn, all_args)
                ))
                parallel_done_at = time.time() - turn_t0

                for tool_index, (tool_call, (mcp_result, tool_duration), tool_args) in enumerate(
                    zip(tool_calls, timed_results, all_args)
                ):
                    tool_name = tool_call.get("name", "")
                    raw_result = mcp_result.content[0].text
                    tool_errored = getattr(mcp_result, "is_error", False)
                    if tool_errored:
                        log.warning("[!] Tool error (parallel): %s — %s",
                                    tool_name, raw_result[:200])
                        memory_result = raw_result
                        immediate_compacted = False
                        compaction_kind = None
                    else:
                        memory_result, immediate_compacted, compaction_kind = (
                            compact_tool_result_immediately(tool_name, raw_result)
                        )
                    if tool_name in L0_DISCOVERY_TOOLS and not tool_errored:
                        l0_called.add(tool_name)

                    payload = (
                        parsed_payloads[tool_index]
                        if tool_index < len(parsed_payloads)
                        else tool_call
                    )
                    conversation.append({
                        "role": "assistant",
                        "content": _compact_response_with_tool_call(
                            response, payload, tc_match, REASONING_CAP,
                        ),
                    })
                    conversation.append({
                        "role": "user",
                        "content": f"<tool_result>\n{memory_result}\n</tool_result>",
                    })

                    step = {
                        "iteration": iteration,
                        "tool": tool_name or "?",
                        "arguments": tool_args,
                        "result_chars": len(raw_result),
                        "result_full": raw_result,
                        "display_result": memory_result,
                        "display_result_chars": len(memory_result),
                        "memory_result": memory_result,
                        "immediate_compacted": immediate_compacted,
                        "compaction_kind": compaction_kind,
                        "elapsed_at": parallel_done_at,
                        "duration_s": tool_duration,
                        "parallel": True,
                        "parallel_group": len(tool_calls),
                        "is_error": tool_errored,
                    }
                    tool_history.append(step)

            else:
                for tool_index, tool_call in enumerate(tool_calls):
                    tool_name = tool_call.get("name", "")
                    phase_error = _phase_error_message(
                        tool_name,
                        preplan_called=preplan_called,
                        plan_called=plan_called,
                        l0_called=l0_called,
                        l0_required=l0_required,
                        preplan_tool=PREPLAN_TOOL_NAME,
                        plan_tool=PLAN_TOOL_NAME,
                        l0_discovery_tools=L0_DISCOVERY_TOOLS,
                    )

                    tool_errored = False
                    tool_t0 = time.time()
                    if phase_error:
                        raw_result = phase_error
                        memory_result = phase_error
                        immediate_compacted = False
                        compaction_kind = None
                        tool_errored = True
                        log.warning("[!] %s", phase_error)
                    else:
                        tool_args = normalize_tool_arguments(
                            tool_name,
                            tool_call.get("arguments", {}),
                        )
                        raw_tool_result = await mcp_manager.call_tool_safe(
                            tool_name,
                            tool_args,
                        )
                        raw_result = raw_tool_result.content[0].text
                        tool_errored = getattr(raw_tool_result, "is_error", False)
                        if tool_errored:
                            log.warning("[!] Tool error: %s — %s",
                                        tool_name, raw_result[:200])
                            memory_result = raw_result
                            immediate_compacted = False
                            compaction_kind = None
                        else:
                            memory_result, immediate_compacted, compaction_kind = (
                                compact_tool_result_immediately(tool_name, raw_result)
                            )
                        if not tool_errored:
                            if tool_name == PREPLAN_TOOL_NAME:
                                preplan_called = True
                                l0_required = infer_required_l0_tools(raw_result)
                                l0_compression_hints = _parse_l0_compression_hints(raw_result)
                                log.info("[PG] Preplan set l0_required=%s, l0_hints=%s",
                                         sorted(l0_required) if l0_required else "(none)",
                                         list(l0_compression_hints.keys()) if l0_compression_hints else "(none)")
                            elif tool_name in L0_DISCOVERY_TOOLS:
                                l0_called.add(tool_name)
                            elif tool_name == PLAN_TOOL_NAME:
                                plan_called = True

                    payload = (
                        parsed_payloads[tool_index]
                        if tool_index < len(parsed_payloads)
                        else tool_call
                    )
                    conversation.append({
                        "role": "assistant",
                        "content": _compact_response_with_tool_call(
                            response, payload, tc_match, REASONING_CAP,
                        ),
                    })
                    conversation.append({
                        "role": "user",
                        "content": f"<tool_result>\n{memory_result}\n</tool_result>",
                    })

                    tool_duration = time.time() - tool_t0
                    step = {
                        "iteration": iteration,
                        "tool": tool_name or "?",
                        "arguments": tool_args if not phase_error else tool_call.get("arguments", {}),
                        "result_chars": len(raw_result),
                        "result_full": raw_result,
                        "display_result": memory_result,
                        "display_result_chars": len(memory_result),
                        "memory_result": memory_result,
                        "immediate_compacted": immediate_compacted,
                        "compaction_kind": compaction_kind,
                        "elapsed_at": time.time() - turn_t0,
                        "duration_s": tool_duration,
                        "parallel": False,
                        "is_error": tool_errored,
                    }
                    tool_history.append(step)

            if (not l0_compression_done
                    and preplan_called
                    and l0_required
                    and not (l0_required - l0_called)
                    and l0_compression_hints):
                l0_compression_done = True
                log.info("[PG] L0 complete — running hint-driven compression")
                await compact_l0_with_hints(
                    conversation, l0_compression_hints, argo_fn=call_argo,
                )

            if plan_called and wrap_up_warnings == 0:
                await compact_memory(conversation, argo_fn=call_argo)
            new_events = _compactor_capture.drain(run_id=compactor_run_id)
            for event in new_events:
                event["after_iteration"] = iteration
            compactor_events.extend(new_events)

            if on_step:
                on_step({
                    "tool_history": tool_history,
                    "compactor_events": new_events,
                    "iteration": iteration,
                    "elapsed": time.time() - turn_t0,
                })

            log.info("   [iter %d] completed in %.1fs (total %.1fs)",
                     iteration, time.time() - iter_t0, time.time() - turn_t0)

            if wrap_up_warnings > 0:
                idx = min(wrap_up_warnings - 1, len(wrap_up_messages) - 1)
                conversation.append({"role": "user", "content": wrap_up_messages[idx]})

        log.warning("[!] Reached limit (elapsed=%.1fs), returning best answer.",
                    time.time() - turn_t0)
        if tool_calls:
            conversation.append({"role": "assistant", "content": response})
            conversation.append({
                "role": "user",
                "content": (
                    "[SYSTEM NOTE] Time/iteration limit reached. Synthesize a COMPLETE "
                    "final answer from ALL data gathered. Do NOT leave sentences unfinished."
                ),
            })
            response = call_argo(_build_flat_prompt(conversation), SYSTEM_PROMPT)
            conversation.append({"role": "assistant", "content": response})
        mark_plans_complete(conversation)
        return AgentRunResult(
            answer=response,
            memory=conversation,
            tool_history=tool_history,
            compactor_events=compactor_events,
            elapsed=time.time() - turn_t0,
        )
    finally:
        _compactor_capture.drain(run_id=compactor_run_id)
        _compactor_run_id_var.reset(compactor_run_token)
        await mcp_manager.close()


def run_agent_query_sync(
    user_message: str,
    *,
    memory: Optional[List[Dict[str, str]]] = None,
    timeout: int | None = None,
    on_step: Optional[Callable[[dict], None]] = None,
    max_tool_iterations: int | None = None,
) -> AgentRunResult:
    """Synchronous wrapper around the main agent API."""
    return asyncio.run(
        run_agent_query(
            user_message,
            memory=memory,
            timeout=timeout,
            on_step=on_step,
            max_tool_iterations=max_tool_iterations,
        )
    )


async def agent_turn(
    user_message: str,
    memory: List[Dict[str, str]],
    timeout: int | None = None,
    max_tool_iterations: int | None = None,
) -> str:
    """Compatibility wrapper for the terminal UI."""
    result = await run_agent_query(
        user_message,
        memory=memory,
        timeout=timeout,
        max_tool_iterations=max_tool_iterations,
    )
    return result.answer
