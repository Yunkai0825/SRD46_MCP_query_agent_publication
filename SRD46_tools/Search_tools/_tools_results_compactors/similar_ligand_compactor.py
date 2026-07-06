"""Markdown compactor for ``search_similar_ligands()`` results.

Renders a table of structurally similar ligands ranked by Tanimoto
similarity (Morgan-2048 fingerprints), with the query ligand shown as a
reference row at the top.

Features
--------
- Full SMILES display (no truncation).
- Query ligand shown as first reference row with ``similarity = 1.000``.
- RDKit-based functional-group diff column: for each similar ligand,
  shows groups gained / lost relative to the query
  (e.g. ``+thiol, −carboxyl``).
- Diff-signature histogram appended for ligands with similarity > 0.5,
  summarising the most common structural changes across the result set.

Public API
----------
``compact_similar_ligand(rows)``
    Returns ``list[str]`` of markdown lines (no heading).
``compact_search_similar_ligands(data)``
    Returns a complete markdown string with ``## search_similar_ligands``
    heading and row count.  Accepts raw ``dict`` or ``list[dict]``.
"""
from __future__ import annotations

from ._compactor_helpers import _cell, _esc, _num


# ── DB query: all ligands above similarity threshold ─────────────────

def _fetch_all_similar_above(
    query_ligand: dict, threshold: float
) -> list[dict]:
    """Return all ligands from the fingerprint DB with tanimoto_morgan > *threshold*.

    Each returned dict has ``ligand_id``, ``ligand_name``, ``smiles``,
    ``similarity_score``, ``n_beta_defs``.
    """
    import re, sqlite3
    from .._db_connection import FINGERPRINT_DB, CARDS_DB, EQUILIBRIUM_DB

    qid_raw = query_ligand.get("ligand_id", "")
    m = re.search(r"(\d+)", str(qid_raw))
    if not m:
        return []
    qid = int(m.group(1))

    fp_path = str(FINGERPRINT_DB)
    cards_path = str(CARDS_DB)
    if not FINGERPRINT_DB.exists() or not CARDS_DB.exists():
        return []

    conn = sqlite3.connect(f"file:{fp_path}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    try:
        sql = """
            SELECT ligand_id_2 AS similar_id, tanimoto_morgan AS sim
            FROM   ligand_similarity
            WHERE  ligand_id_1 = ? AND ligand_id_2 != ?
              AND  tanimoto_morgan > ?
            UNION ALL
            SELECT ligand_id_1 AS similar_id, tanimoto_morgan AS sim
            FROM   ligand_similarity
            WHERE  ligand_id_2 = ? AND ligand_id_1 != ?
              AND  tanimoto_morgan > ?
            ORDER BY sim DESC
        """
        rows = [dict(r) for r in conn.execute(
            sql, (qid, qid, threshold, qid, qid, threshold)
        ).fetchall()]
    finally:
        conn.close()

    if not rows:
        return []

    # Enrich with ligand_name + smiles from cards DB
    all_ids = [r["similar_id"] for r in rows]
    placeholders = ",".join("?" * len(all_ids))
    cards_conn = sqlite3.connect(f"file:{cards_path}?mode=ro", uri=True)
    cards_conn.row_factory = sqlite3.Row
    try:
        info_rows = cards_conn.execute(
            f"SELECT ligand_id, ligand_name_SRD AS ligand_name, "
            f"       ligand_SMILES AS smiles "
            f"FROM   ligand_card WHERE ligand_id IN ({placeholders})",
            all_ids,
        ).fetchall()
    finally:
        cards_conn.close()
    info_map = {r["ligand_id"]: dict(r) for r in info_rows}

    # Enrich with beta_def count from equilibrium DB
    beta_map: dict[int, int] = {}
    eq_path = str(EQUILIBRIUM_DB)
    if EQUILIBRIUM_DB.exists():
        eq_conn = sqlite3.connect(f"file:{eq_path}?mode=ro", uri=True)
        eq_conn.row_factory = sqlite3.Row
        try:
            beta_rows = eq_conn.execute(
                f"SELECT ligand_id, SUM(total_entries) AS n_beta "
                f"FROM   eq_map_collection "
                f"WHERE  ligand_id IN ({placeholders}) "
                f"GROUP BY ligand_id",
                all_ids,
            ).fetchall()
            beta_map = {r["ligand_id"]: r["n_beta"] for r in beta_rows}
        finally:
            eq_conn.close()

    result = []
    for r in rows:
        sid = r["similar_id"]
        info = info_map.get(sid, {})
        result.append({
            "ligand_id": f"ligand_{sid}",
            "ligand_name": info.get("ligand_name"),
            "smiles": info.get("smiles"),
            "similarity_score": r["sim"],
            "n_beta_defs": beta_map.get(sid, 0),
        })
    return result


# ── functional-group helpers ─────────────────────────────────────────

def _detect_functional_groups(smiles: str | None) -> dict[str, int]:
    """Return ``{group_name: count}`` for all catalog groups found in *smiles*."""
    if not smiles:
        return {}
    try:
        from rdkit import Chem
        from .._normalization_helpers.functional_group_catalog import FUNCTIONAL_GROUP_CATALOG
    except ImportError:
        return {}
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return {}
    result: dict[str, int] = {}
    for name, smarts in FUNCTIONAL_GROUP_CATALOG.items():
        pat = Chem.MolFromSmarts(smarts)
        if pat is None:
            continue
        n = len(mol.GetSubstructMatches(pat))
        if n:
            result[name] = n
    return result


def _diff_catalog_fun_groups(query_groups: dict[str, int], target_groups: dict[str, int]) -> str:
    """Compact string showing functional-group differences (target vs query)."""
    all_names = sorted(set(query_groups) | set(target_groups))
    diffs: list[str] = []
    for g in all_names:
        qc = query_groups.get(g, 0)
        tc = target_groups.get(g, 0)
        if qc != tc:
            diffs.append(f"{g}({tc - qc:+d})")
    return "; ".join(diffs) if diffs else "no_diff_catalog_fun"


# ═════════════════════════════════════════════════════════════════════
#  Public entry point
# ═════════════════════════════════════════════════════════════════════

def compact_similar_ligand(rows: list[dict]) -> list[str]:
    """Render similar_ligand results.

    ``search_cards("similar_ligand")`` returns a wrapper list like::

        [{"query_ligand": {...}, "query_eq_richness": [...],
          "metal_filter": ..., "similar_ligands": [...]}]

    Extract the inner ``similar_ligands`` list and render it.
    """
    if not rows:
        return ["*(no results)*"]

    # Unwrap: list may be [wrapper_dict] with similar_ligands inside
    first = rows[0]
    inner = first.get("similar_ligands") if isinstance(first, dict) else None
    if inner is not None and isinstance(inner, list):
        # Header with query context
        q = first.get("query_ligand", {})
        q_name = q.get("ligand_name", q.get("ligand_id", "?")) if isinstance(q, dict) else str(q)
        lines: list[str] = [f"**Query:** {q_name}"]

        # Eq-richness summary if present
        richness = first.get("query_eq_richness", [])
        if richness and isinstance(richness, list):
            lines.append(f"**Eq-map coverage:** {len(richness)} metal partner(s)")
        lines.append("")

        if not inner:
            lines.append("*(no similar ligands found)*")
            return lines

        # Pre-compute functional-group diff for each similar ligand
        q_smi = q.get("smiles") if isinstance(q, dict) else None
        q_groups = _detect_functional_groups(q_smi)

        # Render similar_ligands table
        # Pick display columns — skip large/nested keys
        _SKIP = {"smiles_canonical", "inchi", "eq_richness"}
        keys = [k for k in inner[0].keys() if k not in _SKIP]
        keys.append("diff_catalog_fun_group")
        lines.append("| " + " | ".join(keys) + " |")
        lines.append("|" + "|".join("---" for _ in keys) + "|")

        # Insert query ligand as the first row (reference)
        if isinstance(q, dict) and q.get("ligand_id"):
            q_vals = []
            for k in keys:
                if k == "diff_catalog_fun_group":
                    q_vals.append("*(query)*")
                elif k in ("family_score", "similarity_score",
                           "tversky_query_in_target", "tversky_target_in_query"):
                    q_vals.append("—")
                elif k == "smiles":
                    q_vals.append(str(q.get(k, "")) if q.get(k) else "***")
                else:
                    v = q.get(k, "")
                    q_vals.append(_esc(v) if k.endswith("_name") else _cell(v, 50))
            lines.append("| " + " | ".join(q_vals) + " |")
        for s in inner:
            vals = []
            for k in keys:
                if k == "diff_catalog_fun_group":
                    t_groups = _detect_functional_groups(s.get("smiles"))
                    vals.append(_diff_catalog_fun_groups(q_groups, t_groups))
                    continue
                v = s.get(k, "")
                if isinstance(v, float):
                    vals.append(_num(v))
                elif k == "smiles":
                    vals.append(str(v) if v else "***")  # full SMILES, no truncation
                else:
                    vals.append(_esc(v) if k.endswith("_name") else _cell(v, 50))
            lines.append("| " + " | ".join(vals) + " |")

        # -- diff signature pivot: ALL ligands in DB with similarity > 0.5 --
        # Also include search results (inner) that pass the threshold.
        _SIM_THRESHOLD = 0.5
        all_above = _fetch_all_similar_above(q, _SIM_THRESHOLD)

        # Merge search results that pass threshold but might be absent
        # from the DB query (defensive dedup by ligand_id).
        seen_ids = {s.get("ligand_id") for s in all_above}
        for s in inner:
            sim = s.get("similarity_score")
            if sim is not None and float(sim) > _SIM_THRESHOLD:
                lid = s.get("ligand_id")
                if lid and lid not in seen_ids:
                    all_above.append({
                        "ligand_id": lid,
                        "ligand_name": s.get("ligand_name"),
                        "smiles": s.get("smiles"),
                        "similarity_score": float(sim),
                        "n_beta_defs": 0,
                    })
                    seen_ids.add(lid)

        if all_above:
            from collections import defaultdict

            # Decompose per-group diffs for every similar ligand
            group_bucket: dict[str, dict[str, int]] = defaultdict(
                lambda: defaultdict(int)
            )
            # Track how many ligands have 0-diff per group
            group_zero: dict[str, int] = defaultdict(int)
            # Track beta_defs per bucket for avg computation
            group_beta: dict[str, dict[str, list[int]]] = defaultdict(
                lambda: defaultdict(list)
            )
            no_diff_count = 0
            no_diff_betas: list[int] = []
            n_total = len(all_above)
            _COLS = ["<-2", "-2", "-1", "0", "+1", "+2", ">+2"]

            def _bucket(v: int) -> str:
                if v < -2:
                    return "<-2"
                if v > 2:
                    return ">+2"
                return f"{v:+d}"

            for s in all_above:
                t_groups = _detect_functional_groups(s.get("smiles"))
                all_names = sorted(set(q_groups) | set(t_groups))
                n_beta = s.get("n_beta_defs", 0)
                has_diff = False
                for g in all_names:
                    qc = q_groups.get(g, 0)
                    tc = t_groups.get(g, 0)
                    if qc != tc:
                        has_diff = True
                        b = _bucket(tc - qc)
                        group_bucket[g][b] += 1
                        group_beta[g][b].append(n_beta)
                    else:
                        group_zero[g] += 1
                        group_beta[g]["0"].append(n_beta)
                if not has_diff:
                    no_diff_count += 1
                    no_diff_betas.append(n_beta)

            def _avg(betas: list[int]) -> str:
                if not betas:
                    return "***"
                return f"{sum(betas) / len(betas):.1f}"

            lines.append("")
            lines.append(
                f"### Diff signature summary "
                f"({n_total} ligand(s) with similarity > {_SIM_THRESHOLD})"
            )
            hdr = "| group | " + " | ".join(_COLS) + " | avg_beta_counts_per_ligand |"
            sep = "|" + "|".join("---" for _ in range(len(_COLS) + 2)) + "|"
            lines.append(hdr)
            lines.append(sep)
            # "no_diff_catalog_fun" row: ligands with identical functional-group profile
            dash_row = ["no_diff_catalog_fun"] + ["***"] * len(_COLS)
            dash_row[_COLS.index("0") + 1] = str(no_diff_count) if no_diff_count else "***"
            dash_row.append(_avg(no_diff_betas))
            lines.append("| " + " | ".join(dash_row) + " |")
            # Sort groups by total occurrences descending
            for g in sorted(
                group_bucket,
                key=lambda x: sum(group_bucket[x].values()),
                reverse=True,
            ):
                row = [g]
                all_betas: list[int] = []
                for col in _COLS:
                    if col == "0":
                        v = group_zero.get(g, 0)
                        row.append(str(v) if v else "***")
                    else:
                        v = group_bucket[g].get(col, 0)
                        row.append(str(v) if v else "***")
                    all_betas.extend(group_beta[g].get(col, []))
                row.append(_avg(all_betas))
                lines.append("| " + " | ".join(row) + " |")

        return lines

    # Fallback: flat list of dicts — auto-detect columns
    keys = list(first.keys())
    header = "| " + " | ".join(keys) + " |"
    sep = "|" + "|".join("---" for _ in keys) + "|"
    lines = [header, sep]
    for r in rows:
        vals = [_cell(r.get(k, ""), 50) for k in keys]
        lines.append("| " + " | ".join(vals) + " |")
    return lines


def compact_search_similar_ligands(data) -> str:
    """Compact markdown for ``search_similar_ligands()`` results.

    Accepts either the raw dict returned by ``search_similar_ligands()``
    or a list wrapping that dict.
    """
    if isinstance(data, dict):
        data = [data]
    if not isinstance(data, list):
        return f"**search_similar_ligands:** unexpected data type {type(data).__name__}\n"
    if not data:
        return "## search_similar_ligands\n\n*(no results)*\n"
    n = len(data)
    if isinstance(data[0], dict):
        inner = data[0].get("similar_ligands")
        if isinstance(inner, list):
            n = len(inner)
    lines = [f"## search_similar_ligands \u2014 {n} row(s)", ""]
    lines.extend(compact_similar_ligand(data))
    lines.append("")
    return "\n".join(lines) + "\n"
