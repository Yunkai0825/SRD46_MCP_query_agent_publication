# Q2.2.5 — Tool Results (batch 4)

### Step 3: `get_table_schema`
**Args:**
```json
{
  "table_name": "vlm",
  "database": "equilibrium"
}
```

[summary]
**get_table_schema:** Error - Table 'vlm' not found.
Available tables: eq_collection_unassigned, eq_edge, eq_edge_species, eq_export_metadata, eq_map, eq_map_collection, eq_map_stray, eq_network, eq_network_species, eq_node, eq_node_species, sqlite_sequence

---

### Step 4: `get_table_schema`
**Args:**
```json
{
  "table_name": "beta_def",
  "database": "equilibrium"
}
```

[summary]
**get_table_schema:** Error - Table 'beta_def' not found.
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

### Step 6: `get_table_schema`
**Args:**
```json
{
  "table_name": "eq_network",
  "database": "equilibrium"
}
```

[summary]
## get_table_schema - 5 column(s)

| cid | name | type | notnull | pk |
|-----|------|------|---------|----|
| 0 | network_db_id | INTEGER | False | True |
| 1 | map_id | INTEGER | True | False |
| 2 | network_id | INTEGER | True | False |
| 3 | node_count | INTEGER | False | False |
| 4 | edge_count | INTEGER | False | False |

---

### Step 7: `db_distribution`
**Args:**
```json
{
  "table": "eq_node",
  "group_column": "constant_type",
  "limit": 50
}
```

[summary]
**db_distribution:** Error - Table 'eq_node' not allowed.

---

### Step 8: `db_count_records`
**Args:**
```json
{
  "table": "eq_node"
}
```

[summary]
**db_count_records:** Error - Table 'eq_node' not allowed. Choose from: ['ligand_card', 'ligand_pka_bracket', 'ligand_pka_measured', 'ligandmetal_card', 'ligandmetal_stability_estimated', 'ligandmetal_stability_measured', 'metal_card', 'ref_author', 'ref_literature_alt', 'ref_vlm_author', 'ref_vlm_literature_alt']

---

### Step 9: `get_table_schema`
**Args:**
```json
{
  "table_name": "ligandmetal_stability_measured",
  "database": "cards"
}
```

[summary]
## get_table_schema - 25 column(s)

| cid | name | type | notnull | pk |
|-----|------|------|---------|----|
| 0 | stability_id | INTEGER | False | True |
| 1 | card_id | INTEGER | True | False |
| 2 | constant_type | TEXT | False | False |
| 3 | constant_value | REAL | False | False |
| 4 | temperature_c | REAL | False | False |
| 5 | ionic_strength_mol_l | REAL | False | False |
| 6 | solvent_id | INTEGER | False | False |
| 7 | solvent_name | TEXT | False | False |
| 8 | electrolyte_composition | TEXT | False | False |
| 9 | equation_python | TEXT | False | False |
| 10 | raw_definition | TEXT | False | False |
| 11 | normalized_definition | TEXT | False | False |
| 12 | equation_str | TEXT | False | False |
| 13 | equation_tree_json | TEXT | False | False |
| 14 | equation_sides_json | TEXT | False | False |
| 15 | LHS_species_json | TEXT | False | False |
| 16 | RHS_species_json | TEXT | False | False |
| 17 | HxL_involved_json | TEXT | False | False |
| 18 | presence_flags_json | TEXT | False | False |
| 19 | reaction_type | TEXT | False | False |
| 20 | element_conserved | INTEGER | False | False |
| 21 | citations_json | TEXT | False | False |
| 22 | audit_timestamp | TEXT | False | False |
| 23 | error | TEXT | False | False |
| 24 | notes | TEXT | False | False |

---

### Step 10: `db_count_records`
**Args:**
```json
{
  "table": "ligandmetal_stability_measured"
}
```

[summary]
## db_count_records

| table | where | count |
|-------|-------|-------|
| ligandmetal_stability_measured | (all) | 79063 |

---

### Step 11: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT constant_type, COUNT(*) AS count FROM ligandmetal_stability_measured GROUP BY constant_type ORDER BY count DESC"
}
```

[summary]
## execute_srd46_sql - 3 row(s)

| constant_type | count |
|---------------|-------|
| K | 60540 |
| H | 9693 |
| S | 8830 |

---
