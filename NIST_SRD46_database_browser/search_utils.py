"""Compatibility shim — re-exports the canonical implementation from
``SRD46_tools.Search_tools._normalization_helpers.chem_query`` so the
browser and the SQL-WHERE normalizer share a single source of truth.

Falls back to a local copy if the package import path is unavailable
(browser running stand-alone from its own folder).
"""

from __future__ import annotations

try:  # preferred path — single source of truth in the tools package
    from SRD46_tools.Search_tools._normalization_helpers.chem_query import (
        normalize_chem_query,
    )
except Exception:  # pragma: no cover - fallback for stand-alone browser runs
    import re

    _SUPERSCRIPT_MAP = str.maketrans({
        "\u2070": "0", "\u00b9": "1", "\u00b2": "2", "\u00b3": "3",
        "\u2074": "4", "\u2075": "5", "\u2076": "6", "\u2077": "7",
        "\u2078": "8", "\u2079": "9",
        "\u207a": "+", "\u207b": "-",
    })
    _BARE_SYM = r"(?P<sym>(?<![A-Za-z])[A-Z][a-z]?)"
    _PATTERN_DIGIT_FIRST = re.compile(_BARE_SYM + r"\^?(?P<n>\d+)(?P<sign>[+-])(?!\])")
    _PATTERN_SIGN_FIRST = re.compile(_BARE_SYM + r"\^?(?P<sign>[+-])(?P<n>\d+)(?!\])")
    _PATTERN_BARE_SIGN = re.compile(_BARE_SYM + r"\^?(?P<sign>[+-])(?!\d)(?!\])")

    def _to_canonical(sym: str, n: str, sign: str) -> str:
        return f"{sym}^[{(n or '1')}{sign}]"

    def normalize_chem_query(q: str) -> str:  # type: ignore[no-redef]
        if not q:
            return q
        s = q.translate(_SUPERSCRIPT_MAP)
        s = _PATTERN_DIGIT_FIRST.sub(lambda m: _to_canonical(m["sym"], m["n"], m["sign"]), s)
        s = _PATTERN_SIGN_FIRST.sub(lambda m: _to_canonical(m["sym"], m["n"], m["sign"]), s)
        s = _PATTERN_BARE_SIGN.sub(lambda m: _to_canonical(m["sym"], "1", m["sign"]), s)
        return s


__all__ = ["normalize_chem_query"]
