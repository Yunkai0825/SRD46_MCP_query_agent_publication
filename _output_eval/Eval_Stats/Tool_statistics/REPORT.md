# Tool statistics report

## Corpus

- Runs analysed: **1,131**
- Tool calls analysed: **11,345**
- Workflow groups analysed: **7,383**
- Load issues: **0**
- Tool-usage tables exclude planning tools prefixed with `0_`.
- Step-header tool-duration metrics exclude failed tool calls and use the history header `[Xs @ Ys]` duration as mean seconds per successful call.
- Wall-time plot/export metrics use the difference between consecutive tool-group end timestamps and exclude the final pre-answer workflow group in each run.
- Argo analysis metrics use summed `_meta` elapsed timings per successful tool call when present; tools without recorded `_meta` timings are omitted from the Argo timing chart/export.
- Session-compactor metrics are parsed from each history file's final `Compactor Activity` log; they cover context pressure, selection outcomes, task fan-out, and any retry/validator events that were actually emitted.

## Top 10 most-used tools

| tool | calls | run_presence | mean_sec | error_rate |
|---|---|---|---|---|
| search_ligands | 2450 | 74.4% | 1.83 | 1.3% |
| search_stability | 1915 | 66.0% | 2.18 | 27.5% |
| search_metals | 1776 | 84.7% | 1.87 | 1.1% |
| build_system_catalog | 1017 | 66.9% | 0.73 | 0.2% |
| get_table_schema | 269 | 11.4% | 0.49 | 4.5% |
| execute_srd46_sql | 249 | 10.4% | 2.14 | 18.9% |
| search_pka_values | 220 | 12.6% | 0.89 | 40.9% |
| db_distribution | 202 | 12.6% | 1.88 | 22.8% |
| search_citations | 195 | 11.9% | 3.27 | 4.1% |
| search_networks | 186 | 12.6% | 2.76 | 14.0% |

## Top 10 slowest tools

| tool | step_header_mean_sec | step_header_p95_sec | calls |
|---|---|---|---|
| search_similar_ligands | 3.80 | 5.34 | 23 |
| search_citations | 3.27 | 8.31 | 195 |
| search_pka_ligands | 2.88 | 10.90 | 59 |
| search_networks | 2.76 | 8.80 | 186 |
| search_stability | 2.18 | 10.90 | 1915 |
| execute_srd46_sql | 2.14 | 6.19 | 249 |
| db_distribution | 1.88 | 5.83 | 202 |
| search_metals | 1.87 | 4.50 | 1776 |
| search_ligands | 1.83 | 5.32 | 2450 |
| db_ranked_pairs | 1.67 | 6.15 | 121 |

## Top 10 slowest tools by deduced wall time

| tool | wall_mean_sec | wall_p95_sec | wall_timed_calls | coverage |
|---|---|---|---|---|
| search_ligands | 99.98 | 250.00 | 2397 | 99.1% |
| execute_srd46_sql | 95.46 | 182.60 | 104 | 51.5% |
| search_metals | 93.29 | 249.35 | 1734 | 98.7% |
| search_stability | 91.20 | 255.60 | 483 | 34.8% |
| search_networks | 82.31 | 220.50 | 51 | 31.9% |
| search_citations | 78.70 | 273.10 | 83 | 44.4% |
| db_distribution | 78.01 | 249.00 | 79 | 50.6% |
| db_count_records | 72.89 | 284.60 | 35 | 36.5% |
| db_ranked_pairs | 70.57 | 178.20 | 54 | 59.3% |
| search_pka_values | 69.00 | 223.50 | 31 | 23.8% |

## Top 10 slowest tools by Argo analysis time

| tool | argo_mean_sec | argo_p95_sec | timed_calls | coverage |
|---|---|---|---|---|
| 0_plan_search_strategy | 37.25 | 68.10 | 947 | 100.0% |

## Compactor turn summary by model

| model | triggered_rounds | triggered_success_normal | none_rounds | l0_no_match_rounds | runs_with_triggered | run_trigger_rate | runs_with_triggered_success | triggered_success_run_rate |
|---|---|---|---|---|---|---|---|---|
| claudeopus46 | 209 | 128 | 168 | 230 | 130 | 45.6% | 52 | 18.2% |
| claudesonnet46 | 198 | 123 | 129 | 219 | 174 | 62.1% | 102 | 36.4% |
| gpt5 | 244 | 126 | 130 | 236 | 201 | 71.8% | 100 | 35.7% |
| gpt54 | 382 | 165 | 351 | 253 | 189 | 66.1% | 96 | 33.6% |

## Session compactor by model

| model | run_presence | rounds/run | ctx_chars_mean | ctx_turns_mean | selected_rate | selected_candidates_mean | parallel_tasks_mean | retry_events |
|---|---|---|---|---|---|---|---|---|
| claudeopus46 | 98.9% | 4.76 | 24687 | 31.8 | 55.4% | 9.85 | 9.85 | 364 |
| claudesonnet46 | 100.0% | 4.69 | 11368 | 15.0 | 60.6% | 2.29 | 2.29 | 0 |
| gpt5 | 99.6% | 4.60 | 14151 | 18.4 | 65.2% | 3.97 | 3.97 | 0 |
| gpt54 | 99.3% | 5.79 | 16161 | 19.8 | 52.1% | 2.65 | 2.65 | 40 |

- Overall triggered compaction turns: **1033**; triggered-success turns on normal runs: **542**; NONE turns: **778**; L0 no-match turns: **938**; runs with >=1 triggered turn: **694 / 1131** (61.4%); runs with >=1 triggered-success turn: **350 / 1131** (30.9%).

## Top 10 compactor event types

| event_type | events | run_presence | content_chars_mean | context_chars_mean | attempt_mean |
|---|---|---|---|---|---|
| hardcoded_compactor | 8983 | 99.5% | 1755.1 | nan | nan |
| other | 3048 | 0.5% | nan | nan | nan |
| summary_subagent_produced | 2186 | 0.5% | nan | nan | nan |
| context_window | 1811 | 77.9% | nan | 16655.3 | nan |
| validator_accepted | 1780 | 0.5% | nan | nan | 1.09 |
| running_tasks | 1033 | 61.4% | nan | nan | nan |
| selected_candidates | 1033 | 61.4% | nan | nan | nan |
| l0_no_match | 938 | 82.9% | nan | nan | nan |
| chose_none | 778 | 40.5% | nan | nan | nan |
| validator_retry | 404 | 0.5% | nan | nan | 1.69 |

## Top 10 tools by model

### claudeopus46

| tool | call_share | mean_calls/run | mean_sec |
|---|---|---|---|
| search_ligands | 30.7% | 2.60 | 1.54 |
| search_stability | 22.4% | 1.89 | 1.53 |
| search_metals | 20.5% | 1.73 | 2.25 |
| build_system_catalog | 9.8% | 0.83 | 0.67 |
| execute_srd46_sql | 2.9% | 0.24 | 1.74 |
| db_distribution | 2.7% | 0.22 | 1.85 |
| search_pka_values | 2.6% | 0.22 | 0.70 |
| db_ranked_pairs | 2.1% | 0.18 | 1.59 |
| get_table_schema | 1.4% | 0.12 | 0.79 |
| search_citations | 1.3% | 0.11 | 2.20 |

### claudesonnet46

| tool | call_share | mean_calls/run | mean_sec |
|---|---|---|---|
| search_metals | 24.6% | 1.68 | 1.99 |
| search_ligands | 22.5% | 1.54 | 1.48 |
| search_stability | 20.0% | 1.37 | 0.83 |
| build_system_catalog | 13.0% | 0.89 | 1.01 |
| execute_srd46_sql | 3.3% | 0.23 | 1.59 |
| search_pka_values | 3.3% | 0.23 | 0.49 |
| get_table_schema | 3.2% | 0.22 | 0.89 |
| search_networks | 1.9% | 0.13 | 3.24 |
| db_distribution | 1.7% | 0.12 | 2.07 |
| search_citations | 1.7% | 0.11 | 3.15 |

### gpt5

| tool | call_share | mean_calls/run | mean_sec |
|---|---|---|---|
| search_ligands | 35.3% | 3.17 | 2.58 |
| search_stability | 21.5% | 1.93 | 4.28 |
| search_metals | 17.8% | 1.60 | 2.06 |
| build_system_catalog | 11.2% | 1.00 | 0.75 |
| search_citations | 3.1% | 0.28 | 3.07 |
| get_table_schema | 2.4% | 0.21 | 0.21 |
| execute_srd46_sql | 1.8% | 0.16 | 2.53 |
| search_networks | 1.6% | 0.14 | 3.36 |
| search_pka_values | 1.6% | 0.14 | 1.59 |
| db_distribution | 1.4% | 0.12 | 2.05 |

### gpt54

| tool | call_share | mean_calls/run | mean_sec |
|---|---|---|---|
| search_stability | 21.1% | 1.58 | 1.49 |
| search_ligands | 18.3% | 1.37 | 1.10 |
| search_metals | 17.1% | 1.28 | 0.96 |
| build_system_catalog | 11.7% | 0.88 | 0.51 |
| get_table_schema | 5.3% | 0.40 | 0.35 |
| inspect_card | 3.9% | 0.29 | 0.86 |
| search_networks | 3.7% | 0.28 | 2.33 |
| execute_srd46_sql | 3.4% | 0.25 | 2.84 |
| db_distribution | 3.3% | 0.24 | 1.68 |
| search_pka_values | 2.5% | 0.19 | 0.76 |

## Run timing by model

| model | mean_total_sec | mean_planning_sec | mean_execution_sec | error_run_rate |
|---|---|---|---|---|
| gpt5 | 1290.9 | 422.1 | 795.8 | 52.9% |
| claudeopus46 | 1043.7 | 585.2 | 405.2 | 62.8% |
| claudesonnet46 | 992.3 | 519.0 | 413.2 | 51.1% |
| gpt54 | 268.8 | 127.8 | 129.1 | 37.4% |

## Top 10 tool failures

| tool | category | reason | failures |
|---|---|---|---|
| search_stability | phase_tool_unavailable | tool unavailable before planning phase | 509 |
| 0_plan_search_strategy | planner_gate | planner called before required l0 tools | 290 |
| search_pka_values | phase_tool_unavailable | tool unavailable before planning phase | 88 |
| db_ranked_pairs | phase_tool_unavailable | tool unavailable before planning phase | 26 |
| db_distribution | phase_tool_unavailable | tool unavailable before planning phase | 24 |
| search_networks | phase_tool_unavailable | tool unavailable before planning phase | 23 |
| search_ligands | phase_error | [PHASE ERROR] Call 0_preplan_decision first to triage the question before L0 searches. | 22 |
| db_distribution | not_found | [TOOL ERROR] db_distribution: Error executing tool db_distribution: no such column: metal_id | 16 |
| search_metals | phase_error | [PHASE ERROR] Call 0_preplan_decision first to triage the question before L0 searches. | 15 |
| execute_srd46_sql | other_error | [TOOL ERROR] execute_srd46_sql: Error executing tool execute_srd46_sql: Sub-SELECT clauses are not allowed in WHERE clauses. | 14 |

## Top 10 parallel batches

| signature | occurrences | mean_wall_sec | error_rate |
|---|---|---|---|
| search_ligands || search_metals | 610 | 72.47 | 0.8% |
| search_stability || search_stability | 167 | 223.56 | 3.0% |
| search_ligands || search_ligands || search_metals | 109 | 76.55 | 0.0% |
| search_metals || search_metals | 58 | 132.66 | 0.0% |
| search_pka_values || search_stability | 56 | 233.46 | 0.0% |
| get_table_schema || get_table_schema | 50 | 62.88 | 0.0% |
| search_networks || search_stability | 48 | 71.08 | 2.1% |
| search_citations || search_stability | 47 | 123.21 | 4.3% |
| search_ligands || search_ligands | 40 | 91.95 | 0.0% |
| search_ligands || search_ligands || search_ligands | 33 | 105.03 | 0.0% |

## Top 10 workflow snippets

| len | snippet | occurrences | runs |
|---|---|---|---|
| 2 | build_system_catalog -> 0_plan_search_strategy | 583 | 583 |
| 2 | 0_preplan_decision -> [search_ligands || search_metals] | 511 | 509 |
| 2 | search_stability -> search_stability | 359 | 140 |
| 2 | [search_ligands || search_metals] -> build_system_catalog | 256 | 256 |
| 3 | 0_preplan_decision -> [search_ligands || search_metals] -> build_system_catalog | 232 | 232 |
| 2 | 0_plan_search_strategy -> search_stability | 226 | 225 |
| 2 | build_system_catalog -> build_system_catalog | 221 | 123 |
| 3 | search_stability -> search_stability -> search_stability | 214 | 56 |
| 3 | [search_ligands || search_metals] -> build_system_catalog -> 0_plan_search_strategy | 199 | 199 |
| 2 | 0_plan_search_strategy -> build_system_catalog | 196 | 196 |

## Figures emitted

- `compactor_context_by_model.png`
- `compactor_retry_by_model.png`
- `compactor_selection_by_model.png`
- `compactor_trigger_summary_by_model.png`
- `overall_usage_latency_top10.png`
- `parallel_batch_patterns_top10.png`
- `prompt_tool_affinity_heatmap_top10.png`
- `run_timing_by_model.png`
- `run_timing_by_model_section.png`
- `tool_argo_duration_by_model.png`
- `tool_chain_second_order_top15.png`
- `tool_duration_by_model.png`
- `tool_failures_top10.png`
- `tool_preferences_by_model_top10.png`
- `tool_wall_time_by_model.png`
- `workflow_snippets_top10.png`

## Files emitted

- Data tables: `\\Sheldon.cse.anl.gov\yunkai.sun$\_temp_codespace\_output_eval\Eval_Stats\Tool_statistics\_data`
- Aggregated CSVs: `\\Sheldon.cse.anl.gov\yunkai.sun$\_temp_codespace\_output_eval\Eval_Stats\Tool_statistics\csv`
- JSON mirrors: `\\Sheldon.cse.anl.gov\yunkai.sun$\_temp_codespace\_output_eval\Eval_Stats\Tool_statistics\json`
- Figures: `\\Sheldon.cse.anl.gov\yunkai.sun$\_temp_codespace\_output_eval\Eval_Stats\Tool_statistics\figures`
- OriginPro import bundle: `\\Sheldon.cse.anl.gov\yunkai.sun$\_temp_codespace\_output_eval\Eval_Stats\Tool_statistics\origin_import`
