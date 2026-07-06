Short answer: SRD‑46 does not index macromolecular proteins (e.g., transferrin, albumin, metallothionein, ceruloplasmin). It focuses on metal–small‑molecule equilibria measured in solution.

What I checked in SRD‑46
- Ligand searches for protein names and for a “protein” class returned zero matches.
- Metals of biological interest are well covered, and we can retrieve many metal–small‑ligand systems that serve as proxies for protein binding environments.

Protein ligand lookups (all returned 0 matches)
| Search term | Matches |
|-------------|---------|
| transferrin | 0 |
| lactoferrin | 0 |
| ovotransferrin / conalbumin | 0 |
| human serum albumin (HSA) | 0 |
| bovine serum albumin (BSA) | 0 |
| metallothionein | 0 |
| ceruloplasmin | 0 |
| ligand_class = protein | 0 |

Coverage of bio‑relevant metals (examples)
| Metal ion (ID) | Ligand partners (count) | VLM measurements (count) |
|---|---:|---:|
| Fe3+ (metal_61) | 406 | 1473 |
| Ga3+ (metal_64) | 146 | 428 |
| Al3+ (metal_5) | 187 | 792 |
| Cu2+ (metal_41) | 1951 | 8963 |
| Zn2+ (metal_208) | 1169 | 4095 |

Examples of Fe3+ small‑ligand systems present (proxy models)
| System (metal_61 + ligand) | Ligand ID | VLM measurements | Temp range (°C) | Ionic strength range (M) | Stoichiometries reported (from equations) |
|---|---|---:|---|---|---|
| Hydroxide | ligand_10076 | 38 | 19–30 | −0.15 to 3.15 | ML, ML2, ML4; hydroxo/polynuclear species present |
| Chloride | ligand_10163 | 13 | 19–30 | −0.15 to 4.15 | ML, ML2 |
| Hydrogen fluoride | ligand_10162 | 13 | 19–30 | −0.05 to 1.15 | ML, ML2, ML3 |
| Ethanoic acid (acetate) | ligand_8465 | 16 | 15–30 | −0.05 to 3.15 | ML, ML2, ML3; hydroxo‑bridged higher species present |
| Ethanedioic acid (oxalate) | ligand_8872 | 11 | 16.5–31.5 | 0.275 to 3.225 | ML, ML2, ML3 |
| Nitrilotriacetic acid (NTA) | ligand_6165 | 16 | 15–30 | −0.05 to 1.15 | ML and hydroxo variants; dimeric hydroxo species present |
| Ethylenediaminetetraacetic acid (EDTA) | ligand_6277 | 14 | 19–30 | −0.05 to 1.15 | ML and hydroxo variants; dimeric hydroxo species present |
| 2‑Hydroxybenzoic acid (salicylate) | ligand_9257 | 15 | 15–30 | −0.15 to 3.15 | ML; acid–base coupled formation observed |
| 8‑Hydroxyquinoline (oxine) | ligand_8126 | 13 | 19–30 | −0.15 to 1.15 | ML, ML2, ML3 |
| 1,2‑Dihydroxybenzene‑3,5‑disulfonic acid (tiron) | ligand_9358 | 16 | 15–30 | −0.05 to 1.15 | Multidentate complexes; stepwise proton‑coupled equilibria |

Notes and context
- SRD‑46 provides many Fe3+–small‑ligand equilibria (examples above) across typical lab conditions (near room temperature; ionic strength spanning dilute to moderately high electrolyte). These systems capture functional donor types relevant to proteins (e.g., phenolate/catecholate with salicylate/tiron; N/O chelation with 8‑hydroxyquinoline; carboxylate donors with acetate/oxalate; aminopolycarboxylates like NTA/EDTA for baseline comparisons).
- Transferrin specifically uses tyrosinate donors with a synergistic anion; SRD‑46 does not include the protein itself, but we can assemble a protein‑environment picture from such small‑ligand proxies.

If you’d like, I can next pull the actual stability constants and conditions for specific proxy systems (e.g., Fe3+–salicylate, Fe3+–oxalate, Fe3+–EDTA/NTA, Fe3+–8‑hydroxyquinoline) or look up analogous data for Ga3+, Al3+, Cu2+, or Zn2+.

Source: NIST Standard Reference Database 46 (SRD‑46). Evidence includes search_ligands (no protein matches), search_metals (coverage counts; e.g., Fe3+ = metal_61), and build_system_catalog for Fe3+ showing the small‑ligand systems and measurement ranges listed above.

---