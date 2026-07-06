# Q2.2.4 — Tool Results (batch 1)

### Step 3: `search_ligands`
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

### Step 5: `get_table_schema`
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

### Step 6: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT COUNT(*) AS distinct_class_count\nFROM (\n  SELECT LOWER(TRIM(ligand_class_name)) AS class_norm\n  FROM ligand_card\n  WHERE ligand_class_name IS NOT NULL\n    AND TRIM(ligand_class_name) <> ''\n    AND LOWER(TRIM(ligand_class_name)) NOT IN ('unknown','—','-','n/a','na')\n  GROUP BY class_norm\n) t;"
}
```

[summary]
## execute_srd46_sql - 1 row(s)

| distinct_class_count |
|----------------------|
| 59 |

---

### Step 7: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT LOWER(TRIM(ligand_class_name)) AS ligand_class,\n       COUNT(*) AS ligand_count\nFROM ligand_card\nWHERE ligand_class_name IS NOT NULL\n  AND TRIM(ligand_class_name) <> ''\n  AND LOWER(TRIM(ligand_class_name)) NOT IN ('unknown','—','-','n/a','na')\nGROUP BY ligand_class\nORDER BY ligand_count DESC, ligand_class ASC\nLIMIT 5;"
}
```

[summary]
## execute_srd46_sql - 5 row(s)

| ligand_class | ligand_count |
|--------------|--------------|
| ligands not selected | 1339 |
| amino acids | 297 |
| aliphatic amines | 250 |
| pyridines (azines) | 248 |
| carboxylic acids | 182 |

---
