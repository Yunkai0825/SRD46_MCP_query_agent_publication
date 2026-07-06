# Q5.2.3 — Tool Results (batch 4)

### Step 2: `get_table_schema`
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

### Step 3: `db_count_records`
**Args:**
```json
{
  "table": "ligandmetal_stability_measured",
  "where": "temperature_c = 200"
}
```

[summary]
## db_count_records

| table | where | count |
|-------|-------|-------|
| ligandmetal_stability_measured | temperature_c = 200 | 0 |

---

### Step 4: `search_stability`
**Args:**
```json
{
  "where": "(s.temperature_c >= 150)",
  "order_by": "s.temperature_c DESC",
  "limit": 20
}
```

[summary]
## search_stability

*(no results)*

---

### Step 5: `get_table_schema`
**Args:**
```json
{
  "table_name": "ligandmetal_stability_measured"
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

### Step 6: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_stability_measured",
  "group_column": "temperature_c",
  "limit": 20
}
```

[summary]
## db_distribution - ligandmetal_stability_measured by temperature_c

**total_rows:** 79063

| value | count | pct |
|-------|-------|-----|
| 25.0 | 67237 | 85.04% |
| 20.0 | 6845 | 8.66% |
| 37.0 | 1699 | 2.15% |
| 30.0 | 919 | 1.16% |
| 35.0 | 488 | 0.62% |
| 18.0 | 482 | 0.61% |
| 10.0 | 334 | 0.42% |
| 40.0 | 324 | 0.41% |
| 22.0 | 324 | 0.41% |
| 15.0 | 197 | 0.25% |
| 45.0 | 60 | 0.08% |
| 50.0 | 44 | 0.06% |
| 27.0 | 44 | 0.06% |
| 0.0 | 27 | 0.03% |
| 75.0 | 21 | 0.03% |
| 5.0 | 12 | 0.02% |
| 55.0 | 2 | 0.0% |
| 12.0 | 2 | 0.0% |
| 23.0 | 1 | 0.0% |
| 3.0 | 1 | 0.0% |

---

### Step 7: `search_stability`
**Args:**
```json
{
  "where": "(s.temperature_c >= 100)",
  "order_by": "s.temperature_c DESC",
  "limit": 20
}
```

[summary]
## search_stability

*(no results)*

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(s.temperature_c >= 70)",
  "order_by": "s.temperature_c DESC",
  "limit": 10
}
```

[summary]
## search_stability — 10 row(s)

### `H^[+]` + Adenosine-5'-(trihydrogendiphosphate) (ADP) — 9 measurement(s)
metal_id: metal_68 | ligand_id: ligand_8318
ligand_HxL_def: H3L | ligand_SMILES: Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]1O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_141259 | ref_eq_map_15976 | beta_def_79 | logK | 7.44 | 75 | 0 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (3.87, HL, 6.3, L, +inf) |
| vlm_141261 | *** | beta_def_79 | ΔH | 16.3 | 75 | 0 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (3.87, HL, 6.3, L, +inf) |
| vlm_141264 | *** | beta_def_79 | ΔS | 190 | 75 | 0 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (3.87, HL, 6.3, L, +inf) |
| vlm_141272 | ref_eq_map_15976 | beta_def_32 | logK | 3.79 | 75 | 0 | `[HL] + [H] <=> [H2L]` | *** | [HL]; [H2L] | (1.8, H2L, 3.87, HL, 6.3) |
| vlm_141274 | *** | beta_def_32 | ΔH | -13.8 | 75 | 0 | `[HL] + [H] <=> [H2L]` | *** | [HL]; [H2L] | (1.8, H2L, 3.87, HL, 6.3) |
| vlm_141277 | *** | beta_def_32 | ΔS | 33.9 | 75 | 0 | `[HL] + [H] <=> [H2L]` | *** | [HL]; [H2L] | (1.8, H2L, 3.87, HL, 6.3) |
| vlm_141280 | ref_eq_map_15976 | beta_def_53 | logK | 2.16 | 75 | 0 | `[H2L] + [H] <=> [H3L]` | *** | [H2L]; [H3L] | (-inf, H3L, 1.8, H2L, 3.87) |
| vlm_141282 | *** | beta_def_53 | ΔH | 18.4 | 75 | 0 | `[H2L] + [H] <=> [H3L]` | *** | [H2L]; [H3L] | (-inf, H3L, 1.8, H2L, 3.87) |
| vlm_141284 | *** | beta_def_53 | ΔS | 94.1 | 75 | 0 | `[H2L] + [H] <=> [H3L]` | *** | [H2L]; [H3L] | (-inf, H3L, 1.8, H2L, 3.87) |

### `Mg^[2+]` + Adenosine-5'-(trihydrogendiphosphate) (ADP) — 1 measurement(s)
metal_id: metal_92 | ligand_id: ligand_8318
ligand_HxL_def: H3L | ligand_SMILES: Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]1O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_141293 | ref_eq_map_15988 | beta_def_812 | logK | 4.89 | 75 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (6.3, L, +inf) |

---
