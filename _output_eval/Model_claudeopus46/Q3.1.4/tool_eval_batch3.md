# Q3.1.4 — Tool Results (batch 3)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "iron"
}
```

[summary]
## search_metals — 2 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_61 | Fe^[3+] | Fe | 3 | ✓ | [Fe+3] | InChI=1S/Fe/q+3 | beta_totN_128 | ligand_totN_406 | vlm_totN_1473 |
| metal_62 | Fe^[2+] | Fe | 2 | ✓ | [Fe+2] | InChI=1S/Fe/q+2 | beta_totN_57 | ligand_totN_217 | vlm_totN_667 |

---

### Step 4: `get_table_schema`
**Args:**
```json
{
  "table_name": "ligandmetal_card",
  "database": "cards"
}
```

[summary]
## get_table_schema - 17 column(s)

| cid | name | type | notnull | pk |
|-----|------|------|---------|----|
| 0 | card_id | INTEGER | False | True |
| 1 | complex_system_id | INTEGER | True | False |
| 2 | metal_id | INTEGER | True | False |
| 3 | ligand_id | INTEGER | True | False |
| 4 | beta_definition_id | INTEGER | True | False |
| 5 | complex_id | TEXT | False | False |
| 6 | ligand_class_id | INTEGER | False | False |
| 7 | ligand_class_name | TEXT | False | False |
| 8 | metal_name_SRD | TEXT | False | False |
| 9 | metal_SMILES | TEXT | False | False |
| 10 | metal_InChi | TEXT | False | False |
| 11 | ligand_name_SRD | TEXT | False | False |
| 12 | ligand_SMILES | TEXT | False | False |
| 13 | ligand_InChi | TEXT | False | False |
| 14 | ligand_HxL_definition_SRD | TEXT | False | False |
| 15 | beta_definition_name | TEXT | False | False |
| 16 | created_at | TIMESTAMP | False | False |

---

### Step 5: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT c.ligand_id, c.ligand_name_SRD, MAX(CASE WHEN c.metal_id = 61 THEN s.constant_value END) AS max_logB_Fe3, MAX(CASE WHEN c.metal_id = 62 THEN s.constant_value END) AS max_logB_Fe2, c.beta_definition_name FROM ligandmetal_card c JOIN ligandmetal_stability_measured s ON c.card_id = s.card_id WHERE c.metal_id IN (61, 62) AND c.ligand_id IN (SELECT ligand_id FROM ligandmetal_card WHERE metal_id IN (61, 62) GROUP BY ligand_id HAVING COUNT(DISTINCT metal_id) = 2) AND s.constant_type = 'log_beta' GROUP BY c.ligand_id, c.beta_definition_name HAVING max_logB_Fe3 IS NOT NULL AND max_logB_Fe2 IS NOT NULL ORDER BY c.ligand_id, c.beta_definition_name LIMIT 500",
  "attach_equilibrium": false,
  "attach_literature": false
}
```

[summary]
## execute_srd46_sql

*(no results)*

---
