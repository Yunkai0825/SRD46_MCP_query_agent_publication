"""
Debug examples: trace which SRD-46 databases each tool actually touches
and which fields show up in the final compacted markdown.

For each tool we record:
  * primary_dbs       — DB(s) the tool's MAIN result rows come from
  * secondary_dbs     — DB(s) joined / queried for enrichment
  * raw_keys          — keys present in raw tool result (per row / top-level)
  * compactor_added   — strings that appear only after compaction

The script writes a JSON report and a per-tool markdown sample beside it.
Run from repo root:

    python -m SRD46_tools.Search_tools._tools_results_compactors._Debug_examples.tool_db_audit
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

# Make repo root importable
_HERE = Path(__file__).resolve()
_REPO = _HERE.parents[4]
sys.path.insert(0, str(_REPO))

from SRD46_tools.Search_tools.entity_search import search_metals, search_ligands
from SRD46_tools.Search_tools.stability_search import search_stability
from SRD46_tools.Search_tools.pka_search import search_pka_values, search_pka_ligands
from SRD46_tools.Search_tools.network_search import search_networks
from SRD46_tools.Search_tools.citation_search import search_citations
from SRD46_tools.Search_tools.similarity_search import search_similar_ligands
from SRD46_tools.Search_tools.system_catalog import build_system_catalog
from SRD46_tools.Search_tools.card_inspect import inspect_card, inspect_literature

from SRD46_tools.Search_tools._tools_results_compactors.entity_search_compactors import (
    compact_search_metals, compact_search_ligands,
)
from SRD46_tools.Search_tools._tools_results_compactors.stability_compactor import compact_search_stability
from SRD46_tools.Search_tools._tools_results_compactors.pka_values_compactor import compact_search_pka_values
from SRD46_tools.Search_tools._tools_results_compactors.pka_ligands_compactor import compact_search_pka_ligands
from SRD46_tools.Search_tools._tools_results_compactors.network_compactor import compact_search_networks
from SRD46_tools.Search_tools._tools_results_compactors.citation_compactor import compact_search_citations
from SRD46_tools.Search_tools._tools_results_compactors.similar_ligand_compactor import compact_search_similar_ligands
from SRD46_tools.Search_tools._tools_results_compactors.system_catalog_compactor import compact_system_catalog
from SRD46_tools.Search_tools._tools_results_compactors.inspect_card_compactor import compact_inspect_card
from SRD46_tools.Search_tools._tools_results_compactors.inspect_literature_compactor import compact_inspect_literature


CU = "metal_id = 41"           # Cu2+
GLY = 5760                      # Glycine ligand_id


def _row_keys(rows):
    if isinstance(rows, dict):
        rows = rows.get("results", rows.get("similar_ligands", [rows]))
    if rows and isinstance(rows, list) and isinstance(rows[0], dict):
        return sorted(rows[0].keys())
    return []


def _audit():
    cases = []

    # search_metals -----------------------------------------------------
    out = search_metals(metal_id=41, limit=3)
    cases.append({
        "tool": "search_metals",
        "primary_db_table": "cards.metal_card",
        "secondary_db_tables": ["cards.ligandmetal_card (counts)"],
        "raw_keys_first_row": _row_keys(out),
        "compacted": compact_search_metals(out)[:600],
    })

    # search_ligands ----------------------------------------------------
    out = search_ligands(ligand_id=GLY, limit=3)
    cases.append({
        "tool": "search_ligands",
        "primary_db_table": "cards.ligand_card",
        "secondary_db_tables": [
            "cards.ligand_pka_bracket  (-> pka_brackets enrichment)",
            "cards.ligandmetal_card    (-> vlm_count enrichment)",
        ],
        "raw_keys_first_row": _row_keys(out),
        "compacted": compact_search_ligands(out)[:600],
    })

    # search_stability --------------------------------------------------
    out = search_stability(where=f"c.metal_id=41 AND c.ligand_id={GLY}", limit=5)
    cases.append({
        "tool": "search_stability",
        "primary_db_table": "cards.ligandmetal_card JOIN cards.ligandmetal_stability_measured",
        "secondary_db_tables": [
            "cards.ligand_pka_bracket  (-> pKa_bracket_involved enrichment)",
            "equilibrium.eq_node JOIN equilibrium.eq_network  (-> map_id enrichment)",
        ],
        "raw_keys_first_row": _row_keys(out),
        "compacted": compact_search_stability(out)[:600],
    })

    # search_pka_values -------------------------------------------------
    out = search_pka_values(where=f"lc.ligand_id={GLY}", limit=5)
    cases.append({
        "tool": "search_pka_values",
        "primary_db_table": "cards.ligand_card JOIN cards.ligand_pka_measured",
        "secondary_db_tables": [
            "cards.ligandmetal_card + cards.ligandmetal_stability_measured "
            "(-> M_tot, M_above, M_below per protonation form)",
        ],
        "raw_keys_first_row": _row_keys(out),
        "compacted": compact_search_pka_values(out)[:600],
    })

    # search_pka_ligands ------------------------------------------------
    out = search_pka_ligands(where=f"lc.ligand_id={GLY}", limit=5)
    cases.append({
        "tool": "search_pka_ligands",
        "primary_db_table": "cards.ligand_card JOIN cards.ligand_pka_measured",
        "secondary_db_tables": [
            "cards.ligandmetal_card + cards.ligandmetal_stability_measured "
            "(-> M_tot, M_above, M_below)",
        ],
        "raw_keys_first_row": _row_keys(out),
        "compacted": compact_search_pka_ligands(out)[:600],
    })

    # search_networks ---------------------------------------------------
    out = search_networks(where=f"c.metal_id=41 AND c.ligand_id={GLY}", limit=3)
    cases.append({
        "tool": "search_networks",
        "primary_db_table": "equilibrium.eq_map_collection JOIN eq_map JOIN eq_network JOIN eq_node",
        "secondary_db_tables": [
            "ATTACH cards.ligand_card  (-> ligand_HxL_definition, ligand_SMILES per row)",
        ],
        "raw_keys_first_row": _row_keys(out),
        "compacted": compact_search_networks(out)[:600],
    })

    # search_citations --------------------------------------------------
    out = search_citations(where="la.shortcut LIKE '%64MA%'", limit=3)
    cases.append({
        "tool": "search_citations",
        "primary_db_table": "cards.ref_vlm_literature_alt JOIN cards.ref_literature_alt "
                            "(*** NOTE: NOT srd46_literature.db ***)",
        "secondary_db_tables": [
            "(none — single GROUP BY for vlm_count aggregation)",
        ],
        "raw_keys_first_row": _row_keys(out),
        "compacted": compact_search_citations(out)[:600],
    })

    # search_similar_ligands -------------------------------------------
    out = search_similar_ligands(ligand_id=GLY, top_k=3)
    cases.append({
        "tool": "search_similar_ligands",
        "primary_db_table": "fingerprints.ligand_similarity",
        "secondary_db_tables": [
            "cards.ligand_card  (-> ligand_name, smiles, HxL_canonical)",
            "equilibrium.eq_map_collection + eq_node (-> eq_richness: metals_covered, "
            "top_maps, n_beta_defs)",
        ],
        "raw_keys_first_row": _row_keys(out),
        "compacted": compact_search_similar_ligands(out)[:600],
    })

    # build_system_catalog ---------------------------------------------
    out = build_system_catalog(metal_id=41, ligand_id=GLY)
    cases.append({
        "tool": "build_system_catalog",
        "primary_db_table": "cards.ligandmetal_card JOIN cards.ligandmetal_stability_measured "
                            "(species_catalog, vlm_ids)",
        "secondary_db_tables": [
            "equilibrium.eq_map_collection JOIN eq_map JOIN eq_network "
            "(-> eq_maps per pair: networks, condition ranges)",
        ],
        "raw_keys_first_row": list(out.keys()) if isinstance(out, dict) else [],
        "compacted": compact_system_catalog(out)[:600],
    })

    # inspect_card (vlm) -----------------------------------------------
    vlm_id = None
    try:
        vlm_id = int(str(out["pairs"][0]["vlm_ids"][0]).split("_")[-1])
    except Exception:
        pass
    if vlm_id:
        ic = inspect_card(f"vlm_{vlm_id}")
        cases.append({
            "tool": f"inspect_card(vlm_{vlm_id})",
            "primary_db_table": "cards.ligandmetal_card JOIN cards.ligandmetal_stability_measured",
            "secondary_db_tables": [
                "ATTACH equilibrium  (eq_node JOIN eq_network -> networks)",
                "ATTACH literature   (vlm_literature_sic JOIN literature_alt -> citations)",
                "cards.ligand_pka_bracket  (-> pKa_bracket_involved)",
            ],
            "raw_top_keys": sorted(ic.keys()),
            "compacted": compact_inspect_card(ic)[:600],
        })

    # inspect_literature -----------------------------------------------
    if vlm_id:
        il = inspect_literature(f"vlm_{vlm_id}")
        cases.append({
            "tool": f"inspect_literature(vlm_{vlm_id})",
            "primary_db_table": "literature.vlm_literature_sic JOIN literature.literature_alt",
            "secondary_db_tables": ["(none)"],
            "raw_top_keys": sorted(il.keys()),
            "compacted": compact_inspect_literature(il)[:600],
        })

    return cases


def main():
    out_dir = _HERE.parent
    cases = _audit()
    (out_dir / "tool_db_audit.json").write_text(
        json.dumps(cases, indent=2, default=str), encoding="utf-8"
    )
    # Also dump a flat markdown summary
    md_lines = ["# Tool ↔ DB audit", ""]
    for c in cases:
        md_lines.append(f"## {c['tool']}")
        md_lines.append(f"- **primary**: `{c['primary_db_table']}`")
        md_lines.append("- **secondary**:")
        for s in c["secondary_db_tables"]:
            md_lines.append(f"  - {s}")
        keys = c.get("raw_keys_first_row") or c.get("raw_top_keys") or []
        if keys:
            md_lines.append(f"- **raw keys** ({len(keys)}): `{', '.join(keys)}`")
        md_lines.append("")
        md_lines.append("```markdown")
        md_lines.append(c["compacted"].rstrip())
        md_lines.append("```")
        md_lines.append("")
    (out_dir / "tool_db_audit.md").write_text("\n".join(md_lines), encoding="utf-8")
    print(f"wrote {out_dir/'tool_db_audit.json'}")
    print(f"wrote {out_dir/'tool_db_audit.md'}")


if __name__ == "__main__":
    main()
