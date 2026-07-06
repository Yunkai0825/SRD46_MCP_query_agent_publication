# Q1.1.6 — Tool Results (batch 3)

### Step 2: `search_ligands`
**Args:**
```json
{
  "ligand_class": "Amino Acids",
  "limit": 1
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 297 SQL matches · showing 1 · limit 1

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5760 | Aminoacetic acid (Glycine) | HL | Amino Acids | 428 | `NCC(=O)O` | (-inf, H2L, 2.33, HL, 9.57, L, +inf) |

### Functional groups across all SQL matches (294 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 294 | 100% |
| primary_amine | 167 | 57% |
| aromatic_ring | 99 | 34% |
| hydroxyl | 79 | 27% |
| secondary_amine | 68 | 23% |
| tertiary_amine | 48 | 16% |
| amide | 40 | 14% |
| thioether | 26 | 9% |
| phenol | 22 | 7% |
| pyridine | 17 | 6% |
| halide | 13 | 4% |
| thiol | 11 | 4% |
| imine | 9 | 3% |
| ester | 6 | 2% |
| ether | 6 | 2% |
| phosphonate | 6 | 2% |
| phosphate | 5 | 2% |
| sulfonate | 4 | 1% |
| nitrile | 1 | 0% |

---

### Step 4: `get_table_schema`
**Args:**
```json
{
  "table_name": "ligand_card"
}
```

[summary]
## get_table_schema - 13 column(s)

| cid | name | type | notnull | pk |
|-----|------|------|---------|----|
| 0 | ligand_id | INTEGER | False | True |
| 1 | ligand_name_SRD | TEXT | True | False |
| 2 | ligand_class_id | INTEGER | False | False |
| 3 | ligand_class_name | TEXT | False | False |
| 4 | ligand_SMILES | TEXT | False | False |
| 5 | ligand_InChi | TEXT | False | False |
| 6 | formula | TEXT | False | False |
| 7 | composition | TEXT | False | False |
| 8 | figure_definition | TEXT | False | False |
| 9 | definition_HxL | TEXT | False | False |
| 10 | synonym_iupac_name | TEXT | False | False |
| 11 | synonym_common_name | TEXT | False | False |
| 12 | created_at | TIMESTAMP | False | False |

---

### Step 5: `db_count_records`
**Args:**
```json
{
  "table": "ligand_card",
  "where": "ligand_class_name = 'Amino Acids'"
}
```

[summary]
## db_count_records

| table | where | count |
|-------|-------|-------|
| ligand_card | ligand_class_name = 'Amino Acids' | 297 |

---

### Step 6: `db_distribution`
**Args:**
```json
{
  "table": "ligand_card",
  "group_column": "ligand_class_name",
  "where": "ligand_class_name LIKE '%Amino%Acid%'",
  "limit": 20
}
```

[summary]
## db_distribution - ligand_card by ligand_class_name

**total_rows:** 429

| value | count | pct |
|-------|-------|-----|
| Amino Acids | 297 | 69.23% |
| Aminophosphorus acids | 132 | 30.77% |

---
