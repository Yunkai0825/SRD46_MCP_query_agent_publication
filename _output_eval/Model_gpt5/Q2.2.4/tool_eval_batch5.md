# Q2.2.4 — Tool Results (batch 5)

### Step 3: `get_table_schema`
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

### Step 4: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT COUNT(1) AS distinct_class_count\nFROM (\n  SELECT DISTINCT ligand_class_id\n  FROM ligand_card\n  WHERE ligand_class_id IS NOT NULL\n) x;",
  "attach_equilibrium": false,
  "attach_literature": false
}
```

[summary]
## execute_srd46_sql - 1 row(s)

| distinct_class_count |
|----------------------|
| 59 |

---

### Step 5: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT ligand_class_name, ligand_class_id, COUNT(*) AS ligand_count\nFROM ligand_card\nWHERE ligand_class_id IS NOT NULL\nGROUP BY ligand_class_id, ligand_class_name\nORDER BY ligand_count DESC, ligand_class_name ASC\nLIMIT 5;",
  "attach_equilibrium": false,
  "attach_literature": false
}
```

[summary]
## execute_srd46_sql - 5 row(s)

| ligand_class_name | ligand_class_id | ligand_count |
|-------------------|-----------------|--------------|
| Ligands not selected | 59 | 1339 |
| Amino Acids | 1 | 297 |
| Aliphatic amines | 11 | 250 |
| Pyridines (azines) | 20 | 248 |
| Carboxylic acids | 29 | 182 |

---
