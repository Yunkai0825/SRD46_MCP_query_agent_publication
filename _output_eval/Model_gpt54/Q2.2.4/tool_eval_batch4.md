# Q2.2.4 — Tool Results (batch 4)

### Step 2: `search_ligands`
**Args:**
```json
{
  "limit": 1
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 5750 SQL matches · showing 1 · limit 1

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5760 | Aminoacetic acid (Glycine) | HL | Amino Acids | 428 | `NCC(=O)O` | (-inf, H2L, 2.33, HL, 9.57, L, +inf) |

### Functional groups across all SQL matches (4054 parseable SMILES)

| group | count | % |
|-------|-------|---|
| aromatic_ring | 1903 | 47% |
| carboxyl | 1693 | 42% |
| hydroxyl | 1430 | 35% |
| primary_amine | 1101 | 27% |
| tertiary_amine | 820 | 20% |
| amide | 756 | 19% |
| secondary_amine | 724 | 18% |
| phenol | 462 | 11% |
| pyridine | 428 | 11% |
| ether | 291 | 7% |
| halide | 268 | 7% |
| thioether | 261 | 6% |
| sulfonate | 203 | 5% |
| phosphonate | 181 | 4% |
| thiol | 119 | 3% |
| imine | 109 | 3% |
| phosphate | 99 | 2% |
| ester | 92 | 2% |
| ketone | 90 | 2% |
| oxime | 48 | 1% |
| aldehyde | 44 | 1% |
| nitrile | 39 | 1% |
| thiazole | 10 | 0% |
| imidazole | 8 | 0% |
| pyrazole | 8 | 0% |
| carboxylate | 1 | 0% |

---

### Step 4: `db_distribution`
**Args:**
```json
{
  "table": "ligand_card",
  "group_column": "ligand_class_name",
  "where": "ligand_class_name = '{''$ne'': None}'",
  "limit": 500
}
```

[summary]
## db_distribution - ligand_card by ligand_class_name

**total_rows:** 0

| value | count | pct |
|-------|-------|-----|

---

### Step 5: `db_count_records`
**Args:**
```json
{
  "table": "ligand_card",
  "where": "ligand_class_name = '{''$ne'': None}'"
}
```

[summary]
## db_count_records

| table | where | count |
|-------|-------|-------|
| ligand_card | ligand_class_name = '{''$ne'': None}' | 0 |

---
