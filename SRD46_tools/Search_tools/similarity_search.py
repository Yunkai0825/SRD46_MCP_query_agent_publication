"""
Ligand structural-similarity search.

Ranks ligands by MACCS/Morgan/Tversky similarity using the pre-computed
``srd46_ligand_fingerprints.db`` and enriches results with
equilibrium-map coverage from the equilibrium and cards databases.
"""

import logging
import sqlite3
from typing import Optional

from ._db_connection import get_cards_db, get_equilibrium_db, FINGERPRINT_DB
from .entity_search import search_ligands
from ._normalization_helpers.id_prefixer import (
    prefix_ids_in_row,
    prefix_ids_in_rows,
    unprefix_id,
)

log = logging.getLogger("SRD46")


def _rows_to_dicts(cursor) -> list[dict]:
    return [dict(row) for row in cursor.fetchall()]


# ── fingerprint DB access ────────────────────────────────────────────

def _get_fp_db() -> sqlite3.Connection:
    path = str(FINGERPRINT_DB)
    if not FINGERPRINT_DB.exists():
        raise FileNotFoundError(f"Fingerprint DB not found: {path}")
    conn = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    return conn


# ── resolve query ligand ─────────────────────────────────────────────

def _resolve_ligand_id(
    ligand_id: Optional[int] = None,
    ligand_name: Optional[str] = None,
) -> int:
    if ligand_id is not None:
        return int(ligand_id)
    if not ligand_name:
        raise ValueError("Provide either ligand_id or ligand_name")
    hits = search_ligands(name=ligand_name, limit=5)
    results = hits.get("results", []) if isinstance(hits, dict) else hits
    if not results:
        raise ValueError(f"No ligand found for name={ligand_name!r}")
    return unprefix_id(results[0]["ligand_id"])


# ── similarity ranking ───────────────────────────────────────────────

def _fetch_top_similar(
    fp_db: sqlite3.Connection,
    query_id: int,
    top_k: int,
) -> list[dict]:
    sql = """
        SELECT ligand_id_2 AS similar_id,
               tanimoto_maccs,
               tanimoto_morgan,
               tversky_morgan_1to2 AS tversky_query_in_target,
               tversky_morgan_2to1 AS tversky_target_in_query
        FROM   ligand_similarity
        WHERE  ligand_id_1 = ?
          AND  ligand_id_2 != ?
          AND  tanimoto_morgan IS NOT NULL
        UNION ALL
        SELECT ligand_id_1 AS similar_id,
               tanimoto_maccs,
               tanimoto_morgan,
               tversky_morgan_2to1 AS tversky_query_in_target,
               tversky_morgan_1to2 AS tversky_target_in_query
        FROM   ligand_similarity
        WHERE  ligand_id_2 = ?
          AND  ligand_id_1 != ?
          AND  tanimoto_morgan IS NOT NULL
        ORDER BY tanimoto_morgan DESC
        LIMIT ?
    """
    rows = fp_db.execute(sql, (query_id, query_id, query_id, query_id, top_k))
    return _rows_to_dicts(rows)


# ── metadata enrichment ──────────────────────────────────────────────

def _fetch_ligand_info(cards_conn, ligand_ids: list[int]) -> dict[int, dict]:
    if not ligand_ids:
        return {}
    placeholders = ",".join("?" * len(ligand_ids))
    sql = f"""
        SELECT ligand_id, ligand_name_SRD AS ligand_name,
               ligand_SMILES AS smiles, definition_HxL AS HxL_canonical
        FROM   ligand_card
        WHERE  ligand_id IN ({placeholders})
    """
    rows = cards_conn.execute(sql, ligand_ids).fetchall()
    return {r["ligand_id"]: dict(r) for r in rows}


# ── equilibrium map richness ─────────────────────────────────────────

def _fetch_eq_richness(
    eq_conn: sqlite3.Connection,
    ligand_id: int,
    metal_ids: Optional[list[int]] = None,
) -> dict:
    metal_sql = """
        SELECT c.metal_id, c.metal_name, c.total_entries
        FROM   eq_map_collection c
        WHERE  c.ligand_id = ?
        ORDER BY c.total_entries DESC
    """
    metal_rows = [dict(r) for r in eq_conn.execute(metal_sql, (ligand_id,)).fetchall()]

    if metal_ids:
        mid_set = set(metal_ids)
        filtered_metals = [m for m in metal_rows if m["metal_id"] in mid_set]
    else:
        filtered_metals = metal_rows

    if metal_ids:
        placeholders = ",".join("?" * len(metal_ids))
        top_sql = f"""
            SELECT c.collection_id, c.metal_id, c.metal_name,
                   c.ligand_id, c.ligand_name, c.total_entries, c.total_networks
            FROM   eq_map_collection c
            WHERE  c.ligand_id = ?
              AND  c.metal_id IN ({placeholders})
            ORDER BY c.total_entries DESC
            LIMIT 10
        """
        top_rows = eq_conn.execute(top_sql, [ligand_id] + metal_ids).fetchall()
    else:
        top_sql = """
            SELECT c.collection_id, c.metal_id, c.metal_name,
                   c.ligand_id, c.ligand_name, c.total_entries, c.total_networks
            FROM   eq_map_collection c
            WHERE  c.ligand_id = ?
            ORDER BY c.total_entries DESC
            LIMIT 10
        """
        top_rows = eq_conn.execute(top_sql, (ligand_id,)).fetchall()

    beta_sql = """
        SELECT COUNT(DISTINCT nd.beta_definition_id) AS n_beta
        FROM   eq_node nd
        JOIN   eq_network nw ON nw.network_db_id = nd.network_db_id
        JOIN   eq_map m ON m.map_id = nw.map_id
        JOIN   eq_map_collection c ON c.collection_id = m.collection_id
        WHERE  c.ligand_id = ?
    """
    try:
        n_beta = eq_conn.execute(beta_sql, (ligand_id,)).fetchone()[0]
    except Exception:
        n_beta = None

    return {
        "metals_covered": filtered_metals,
        "n_metals": len(filtered_metals),
        "n_beta_defs": n_beta,
        "top_maps": [dict(r) for r in top_rows],
    }


# ── public API ───────────────────────────────────────────────────────

def search_similar_ligands(
    ligand_id: Optional[int] = None,
    ligand_name: Optional[str] = None,
    top_k: int = 10,
    metal_ids: Optional[list[int]] = None,
    **_ignored,
) -> dict:
    """
    Find structurally similar ligands via fingerprint similarity.

    Parameters
    ----------
    ligand_id   : exact ligand_id to query (preferred)
    ligand_name : ligand name for resolution (if ligand_id is None)
    top_k       : number of most similar ligands to return
    metal_ids   : optional list of metal_ids to filter eq coverage

    Returns
    -------
    dict with query_ligand, query_eq_richness, metal_filter, similar_ligands.
    Each similar ligand includes similarity scores and eq_richness.
    """
    qid = _resolve_ligand_id(ligand_id, ligand_name)
    log.info("Similarity search: query ligand_id=%d, top_k=%d, metal_ids=%s",
             qid, top_k, metal_ids)

    fp_db = _get_fp_db()
    try:
        ranked = _fetch_top_similar(fp_db, qid, top_k)
    finally:
        fp_db.close()

    if not ranked:
        return {
            "query_ligand": {"ligand_id": f"ligand_{qid}"},
            "error": "No fingerprint data available for this ligand.",
            "similar_ligands": [],
        }

    all_ids = [qid] + [r["similar_id"] for r in ranked]

    with get_cards_db() as cards_conn:
        info_map = _fetch_ligand_info(cards_conn, all_ids)

    query_info = info_map.get(qid, {"ligand_id": qid})

    with get_equilibrium_db() as eq_conn:
        query_richness = _fetch_eq_richness(eq_conn, qid, metal_ids)

        results = []
        for r in ranked:
            sid = r["similar_id"]
            lig_info = info_map.get(sid, {"ligand_id": sid})
            eq_rich = _fetch_eq_richness(eq_conn, sid, metal_ids)

            results.append({
                "ligand_id": sid,
                "ligand_name": lig_info.get("ligand_name"),
                "smiles": lig_info.get("smiles"),
                "HxL_canonical": lig_info.get("HxL_canonical"),
                "family_score": round(r["tanimoto_maccs"], 4),
                "similarity_score": round(r["tanimoto_morgan"], 4),
                "tversky_query_in_target": round(r["tversky_query_in_target"], 4)
                    if r["tversky_query_in_target"] is not None else None,
                "tversky_target_in_query": round(r["tversky_target_in_query"], 4)
                    if r["tversky_target_in_query"] is not None else None,
                "eq_richness": eq_rich,
            })

    # ── Prefix IDs in all nested structures ──
    prefix_ids_in_row(query_info)
    prefix_ids_in_rows(query_richness.get("metals_covered", []))
    prefix_ids_in_rows(query_richness.get("top_maps", []))
    for sim in results:
        prefix_ids_in_row(sim)
        eq_r = sim.get("eq_richness", {})
        prefix_ids_in_rows(eq_r.get("metals_covered", []))
        prefix_ids_in_rows(eq_r.get("top_maps", []))

    return {
        "query_ligand": query_info,
        "query_eq_richness": query_richness,
        "metal_filter": [f"metal_{m}" for m in metal_ids] if metal_ids else metal_ids,
        "similar_ligands": results,
    }
