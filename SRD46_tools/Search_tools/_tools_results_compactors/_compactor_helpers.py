"""Shared tiny helpers for markdown table rendering.

Every per-entity compactor (stability, network, citation,
similar_ligand, pka_values, pka_ligands) imports these instead of
duplicating formatting logic.

Helpers
-------
``_cell(val, max_len)``
    Stringify *val* for a markdown table cell; returns ``***`` for
    None / blank / ``\\N``; truncates with ``…`` beyond *max_len*.
``_esc(val)``
    Like ``_cell`` but wraps the result in backticks when it contains
    ``[`` or ``]`` (which would break markdown links).
``_ctype(raw)``
    Map single-char constant-type codes (``K`` → logK, ``H`` → ΔH,
    ``S`` → ΔS) to human-readable labels.
``_num(val)``
    Format a numeric value: round floats to 4 decimal places with
    trailing-zero suppression; pass-through ints; ``***`` for None.
``_range_str(lo, hi)``
    Format a lo~hi range, collapsing to a single value when equal.
"""
from __future__ import annotations

from typing import Any


def _cell(val: Any, max_len: int = 80) -> str:
    """Stringify a value for a markdown table cell, truncating if needed."""
    if val is None or str(val).strip() == "" or str(val).strip() == "\\N":
        return "***"
    s = str(val)
    if len(s) <= max_len:
        return s
    return s[: max_len - 1] + "…"


def _esc(val: Any) -> str:
    """Wrap value in backticks if it contains markdown-sensitive brackets."""
    s = _cell(val)
    if s == "***":
        return s
    if "[" in s or "]" in s:
        return f"`{s}`"
    return s


_CTYPE_MAP = {"K": "logK", "H": "ΔH", "S": "ΔS"}


def _ctype(raw: Any) -> str:
    """Map constant_type code to readable label."""
    return _CTYPE_MAP.get(str(raw), str(raw) if raw else "?")


def _num(val: Any) -> str:
    """Format a numeric value: round floats, pass-through ints."""
    if val is None:
        return "***"
    if isinstance(val, float):
        return f"{round(val, 4):g}"
    return str(val)


def _range_str(lo: Any, hi: Any) -> str:
    """Format a lo~hi range, collapsing when equal."""
    s_lo, s_hi = _num(lo), _num(hi)
    if s_lo == s_hi:
        return s_lo
    return f"{s_lo}~{s_hi}"
