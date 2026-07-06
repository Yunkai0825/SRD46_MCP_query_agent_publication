# Q2.2.6 — Tool Results (batch 4)

### Step 3: `get_table_schema`
**Args:**
```json
{
  "table_name": "metal_card",
  "database": "cards"
}
```

[summary]
## get_table_schema - 16 column(s)

| cid | name | type | notnull | pk |
|-----|------|------|---------|----|
| 0 | metal_id | INTEGER | False | True |
| 1 | metal_name_SRD | TEXT | True | False |
| 2 | symbol_pure | TEXT | False | False |
| 3 | charge | INTEGER | False | False |
| 4 | charge_str | TEXT | False | False |
| 5 | SMILES | TEXT | False | False |
| 6 | InChi | TEXT | False | False |
| 7 | InChiKey | TEXT | False | False |
| 8 | parts_used_json | TEXT | False | False |
| 9 | stoichiometry_json | TEXT | False | False |
| 10 | is_simple_ion | INTEGER | False | False |
| 11 | is_organometallic | INTEGER | False | False |
| 12 | primary_metal | TEXT | False | False |
| 13 | formula_components_json | TEXT | False | False |
| 14 | parse_notes | TEXT | False | False |
| 15 | created_at | TIMESTAMP | False | False |

---

### Step 4: `get_table_schema`
**Args:**
```json
{
  "table_name": "ligandmetal_stability_measured",
  "database": "equilibrium"
}
```

[summary]
**get_table_schema:** Error - Table 'ligandmetal_stability_measured' not found.
Available tables: eq_collection_unassigned, eq_edge, eq_edge_species, eq_export_metadata, eq_map, eq_map_collection, eq_map_stray, eq_network, eq_network_species, eq_node, eq_node_species, sqlite_sequence

---

### Step 5: `get_table_schema`
**Args:**
```json
{
  "table_name": "eq_node",
  "database": "equilibrium"
}
```

[summary]
## get_table_schema - 15 column(s)

| cid | name | type | notnull | pk |
|-----|------|------|---------|----|
| 0 | node_db_id | INTEGER | False | True |
| 1 | network_db_id | INTEGER | True | False |
| 2 | vlm_id | INTEGER | True | False |
| 3 | entry_index | INTEGER | False | False |
| 4 | metal_id | INTEGER | True | False |
| 5 | ligand_id | INTEGER | True | False |
| 6 | beta_definition_id | INTEGER | True | False |
| 7 | beta_definition_name | TEXT | False | False |
| 8 | equation_python | TEXT | False | False |
| 9 | constant_type | TEXT | False | False |
| 10 | constant_value | REAL | False | False |
| 11 | temperature | REAL | False | False |
| 12 | ionic_strength | REAL | False | False |
| 13 | is_duplicate | INTEGER | False | False |
| 14 | used_in_map | INTEGER | False | False |

---

### Step 6: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT\n  COUNT(*) AS total_metals,\n  SUM(CASE WHEN vlm_count < 5 THEN 1 ELSE 0 END) AS metals_fewer_than_5,\n  ROUND(100.0 * SUM(CASE WHEN vlm_count < 5 THEN 1 ELSE 0 END) / COUNT(*), 2) AS pct\nFROM (\n  SELECT mc.metal_id, COUNT(DISTINCT en.vlm_id) AS vlm_count\n  FROM metal_card mc\n  LEFT JOIN eq_node en ON mc.metal_id = en.metal_id\n  GROUP BY mc.metal_id\n) sub",
  "attach_equilibrium": true
}
```

[summary]
## execute_srd46_sql - 1 row(s)

| total_metals | metals_fewer_than_5 | pct |
|--------------|---------------------|-----|
| 230 | 114 | 49.57 |

---
