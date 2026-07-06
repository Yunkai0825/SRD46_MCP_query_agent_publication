# Qfree_20260423_134926 — Tool Results (batch 1)

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

### Step 4: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61)",
  "order_by": "s.constant_value DESC",
  "limit": 2000
}
```

[TOOL ERROR] search_stability: Error executing tool search_stability: SQL parse error: Invalid expression / Unexpected token. Line 1, Col: 47.
  SELECT 1 FROM _stub WHERE s.constant_value [4mDESC[0m

---

### Step 5: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_62)",
  "order_by": "s.constant_value DESC",
  "limit": 2000
}
```

[TOOL ERROR] search_stability: Error executing tool search_stability: SQL parse error: Invalid expression / Unexpected token. Line 1, Col: 47.
  SELECT 1 FROM _stub WHERE s.constant_value [4mDESC[0m

---

### Step 6: `get_table_schema`
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

### Step 7: `get_table_schema`
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

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND s.reaction_type = 'ML')",
  "limit": 50
}
```

[summary]
## search_stability

*(no results)*

---

### Step 9: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_62 AND s.reaction_type = 'ML')",
  "limit": 50
}
```

[summary]
## search_stability

*(no results)*

---

### Step 10: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_stability_measured",
  "group_column": "reaction_type",
  "limit": 30
}
```

[summary]
## db_distribution - ligandmetal_stability_measured by reaction_type

**total_rows:** 79063

| value | count | pct |
|-------|-------|-----|
| homogeneous_aqueous | 77969 | 98.62% |
| dissolution | 1067 | 1.35% |
| gas_absorption | 22 | 0.03% |
| *** | 4 | 0.01% |
| unknown | 1 | 0.0% |

---

### Step 11: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_stability_measured",
  "group_column": "constant_type",
  "limit": 30
}
```

[summary]
## db_distribution - ligandmetal_stability_measured by constant_type

**total_rows:** 79063

| value | count | pct |
|-------|-------|-----|
| K | 60540 | 76.57% |
| H | 9693 | 12.26% |
| S | 8830 | 11.17% |

---

### Step 12: `get_table_schema`
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

### Step 13: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_card",
  "group_column": "beta_definition_name",
  "where": "metal_id = 61",
  "limit": 50
}
```

[summary]
## db_distribution - ligandmetal_card by beta_definition_name

**total_rows:** 1473

| value | count | pct |
|-------|-------|-----|
| [ML]/[M][L] | 487 | 33.06% |
| [ML<sub>2</sub>]/[M][L]<sup>2</sup> | 100 | 6.79% |
| [MHL]/[ML][H] | 85 | 5.77% |
| [ML][H]/[M][HL] | 72 | 4.89% |
| [ML]/[M(OH)L][H] | 68 | 4.62% |
| [MHL]/[M][HL] | 68 | 4.62% |
| [ML<sub>3</sub>]/[M][L]<sup>3</sup> | 65 | 4.41% |
| [ML][H]<sup>2</sup>/[M][H<sub>2</sub>L] | 28 | 1.9% |
| [MH<sub>2</sub>L]/[MHL][H] | 28 | 1.9% |
| [M(OH)L]/[M(OH)<sub>2</sub>L][H] | 24 | 1.63% |
| [ML][H]<sup>3</sup>/[M][H<sub>3</sub>L] | 23 | 1.56% |
| [M<sub>3</sub>(OH)<sub>2</sub>L<sub>6</sub>][H]<sup>2</sup>/[M]<sup>3</sup>[L]<… | 23 | 1.56% |
| [ML<sub>2</sub>][H]/[ML][HL] | 20 | 1.36% |
| [MH<sub>3</sub>L]/[MH<sub>2</sub>L][H] | 20 | 1.36% |
| [MHL<sub>2</sub>]/[ML<sub>2</sub>][H] | 19 | 1.29% |
| [ML<sub>2</sub>][H]<sup>2</sup>/[ML][H<sub>2</sub>L] | 18 | 1.22% |
| [ML<sub>3</sub>][H]<sup>2</sup>/[ML<sub>2</sub>][H<sub>2</sub>L] | 14 | 0.95% |
| [ML<sub>3</sub>][H]/[ML<sub>2</sub>][HL] | 13 | 0.88% |
| [M(HL)<sub>2</sub>]/[M][HL]<sup>2</sup> | 13 | 0.88% |
| [M<sub>2</sub>(OH)<sub>2</sub>L<sub>2</sub>]/[M(OH)L]<sup>2</sup> | 11 | 0.75% |
| [MH<sub>2</sub>L]/[M][H<sub>2</sub>L] | 10 | 0.68% |
| [M<sub>2</sub>L<sub>2</sub>]/[M]<sup>2</sup>[L]<sup>2</sup> | 10 | 0.68% |
| [M(OH)L]/[ML][OH] | 9 | 0.61% |
| [ML<sub>2</sub>]/[M(OH)L<sub>2</sub>][H] | 8 | 0.54% |
| [MHL<sub>3</sub>]/[ML<sub>3</sub>][H] | 8 | 0.54% |
| [M(OH)<sub>2</sub>L]/[M(OH)L][OH] | 8 | 0.54% |
| [ML<sub>3</sub>]/[M(OH)L<sub>3</sub>][H] | 7 | 0.48% |
| [MHL][H]/[M][H<sub>2</sub>L] | 7 | 0.48% |
| [MH<sub>4</sub>L]/[MH<sub>3</sub>L][H] | 7 | 0.48% |
| [MH<sub>2</sub>L]/[ML][H]<sup>2</sup> | 7 | 0.48% |
| [M<sub>2</sub>L]/[M]<sup>2</sup>[L] | 7 | 0.48% |
| [ML<sub>4</sub>]/[M][L]<sup>4</sup> | 6 | 0.41% |
| [ML<sub>2</sub>]/[ML][L] | 6 | 0.41% |
| [M<sub>2</sub>L<sub>3</sub>]/[M]<sup>2</sup>[L]<sup>3</sup> | 6 | 0.41% |
| [M<sub>2</sub>(OH)<sub>2</sub>L<sub>2</sub>][H]<sup>2</sup>/[M]<sup>2</sup>[L]<… | 6 | 0.41% |
| [M<sub>2</sub>(OH)<sub>2</sub>L<sub>2</sub>][H]<sup>2</sup>/[ML]<sup>2</sup> | 6 | 0.41% |
| [M(HL)<sub>2</sub>][H]/[M(HL)][H<sub>2</sub>L] | 6 | 0.41% |
| [M(HL)<sub>2</sub>]/[MHL<sub>2</sub>][H] | 6 | 0.41% |
| [M<sub>3</sub>L<sub>4</sub>]/[M]<sup>3</sup>[L]<sup>4</sup> | 5 | 0.34% |
| [ML]/[M(H<sub>-1</sub>L)][H] | 4 | 0.27% |
| [ML<sub>5</sub>]/[M][L]<sup>5</sup> | 4 | 0.27% |
| [MH<sub>2</sub>L<sub>3</sub>]/[MHL<sub>3</sub>][H] | 4 | 0.27% |
| [M(HL)<sub>3</sub>][H]/[M(HL)<sub>2</sub>][H<sub>2</sub>L] | 4 | 0.27% |
| [M][L]<sup>3</sup>/[ML<sub>3</sub>(s)] | 3 | 0.2% |
| [ML<sub>6</sub>]/[M][L]<sup>6</sup> | 3 | 0.2% |
| [ML<sub>3</sub>]/[ML<sub>2</sub>][L] | 3 | 0.2% |
| [MHL][H]<sup>2</sup>/[M][H<sub>3</sub>L] | 3 | 0.2% |
| [M<sub>2</sub>L]/[ML][M] | 3 | 0.2% |
| [M<sub>2</sub>L]/[M<sub>2</sub>(OH)<sub>2</sub>L][H]<sup>2</sup> | 3 | 0.2% |
| [M<sub>2</sub>(OH)L]/[M<sub>2</sub>(OH)<sub>2</sub>L][H] | 3 | 0.2% |

---

### Step 14: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_card",
  "group_column": "beta_definition_name",
  "where": "metal_id = 62",
  "limit": 50
}
```

[summary]
## db_distribution - ligandmetal_card by beta_definition_name

**total_rows:** 667

| value | count | pct |
|-------|-------|-----|
| [ML]/[M][L] | 269 | 40.33% |
| [ML<sub>2</sub>]/[M][L]<sup>2</sup> | 105 | 15.74% |
| [ML<sub>3</sub>]/[M][L]<sup>3</sup> | 61 | 9.15% |
| [MHL]/[ML][H] | 54 | 8.1% |
| [MHL]/[M][HL] | 30 | 4.5% |
| [ML]/[M(OH)L][H] | 19 | 2.85% |
| [MH<sub>2</sub>L]/[MHL][H] | 11 | 1.65% |
| [ML<sub>4</sub>]/[M][L]<sup>4</sup> | 10 | 1.5% |
| [M][L]/[ML(s)] | 7 | 1.05% |
| [MHL<sub>2</sub>]/[ML<sub>2</sub>][H] | 6 | 0.9% |
| [M<sub>2</sub>L]/[ML][M] | 6 | 0.9% |
| [MH<sub>3</sub>L]/[MH<sub>2</sub>L][H] | 5 | 0.75% |
| [MH<sub>2</sub>L]/[M][H<sub>2</sub>L] | 5 | 0.75% |
| [M][H<sub>2</sub>L]/[H]<sup>2</sup>[ML(s)] | 3 | 0.45% |
| [M]<sup>3</sup>[L]<sup>2</sup>/[M<sub>3</sub>L<sub>2</sub>(H<sub>2</sub>O)<sub>… | 3 | 0.45% |
| [ML][H]<sup>2</sup>/[M][H<sub>2</sub>L] | 3 | 0.45% |
| [ML][H]/[M][HL] | 3 | 0.45% |
| [ML]/[M(H<sub>-1</sub>L)][H] | 3 | 0.45% |
| [ML<sub>6</sub>]/[M][L]<sup>6</sup> | 3 | 0.45% |
| [ML<sub>2</sub>]/[M(OH)L<sub>2</sub>][H] | 3 | 0.45% |
| [MHL<sub>3</sub>]/[ML<sub>3</sub>][H] | 3 | 0.45% |
| [MH<sub>2</sub>L<sub>3</sub>]/[MHL<sub>3</sub>][H] | 3 | 0.45% |
| [M<sub>2</sub>L]/[M]<sup>2</sup>[L] | 3 | 0.45% |
| [M<sub>2</sub>L]/[M<sub>2</sub>(OH)L][H] | 3 | 0.45% |
| [M(OH)L]/[M(OH)<sub>2</sub>L][H] | 3 | 0.45% |
| [M(OH)L<sub>2</sub>]/[M(OH)<sub>2</sub>L<sub>2</sub>][H] | 3 | 0.45% |
| [M(HL)<sub>2</sub>]/[M][HL]<sup>2</sup> | 3 | 0.45% |
| [M(H<sub>2</sub>L)<sub>3</sub>]/[M][H<sub>2</sub>L]<sup>3</sup> | 3 | 0.45% |
| [M][L]<sup>2</sup>/[ML<sub>2</sub>(s)] | 2 | 0.3% |
| [ML<sub>2</sub>][H]<sup>2</sup>/[ML][H<sub>2</sub>L] | 2 | 0.3% |
| [M<sub>2</sub>HL]/[M<sub>2</sub>L][H] | 2 | 0.3% |
| [M<sub>2</sub>HL<sub>2</sub>][H]/[M]<sup>2</sup>[HL]<sup>2</sup> | 2 | 0.3% |
| [M(HL)<sub>2</sub>]/[ML<sub>2</sub>][H]<sup>2</sup> | 2 | 0.3% |
| [M(HL)<sub>2</sub>]/[MHL<sub>2</sub>][H] | 2 | 0.3% |
| [M(H<sub>2</sub>L)<sub>2</sub>]/[MH<sub>3</sub>L<sub>2</sub>][H] | 2 | 0.3% |
| [ML][H]<sup>6</sup>/[M][H<sub>6</sub>L] | 1 | 0.15% |
| [ML][H]<sup>3</sup>/[M][H<sub>3</sub>L] | 1 | 0.15% |
| [ML<sub>2</sub>][H]/[ML][HL] | 1 | 0.15% |
| [MHL<sub>3</sub>][H]/[MHL<sub>2</sub>][HL] | 1 | 0.15% |
| [MHL<sub>2</sub>][H]/[MHL][HL] | 1 | 0.15% |
| [MHL<sub>2</sub>]/[MHL][L] | 1 | 0.15% |
| [MH<sub>4</sub>L]/[MH<sub>3</sub>L][H] | 1 | 0.15% |
| [MH<sub>3</sub>L]/[MHL][H]<sup>2</sup> | 1 | 0.15% |
| [MH<sub>3</sub>L<sub>2</sub>]/[M(HL)<sub>2</sub>][H] | 1 | 0.15% |
| [MH<sub>2</sub>L<sub>2</sub>]/[ML][H]<sup>2</sup> | 1 | 0.15% |
| [M<sub>2</sub>L<sub>3</sub>]/[M]<sup>2</sup>[L]<sup>3</sup> | 1 | 0.15% |
| [M<sub>2</sub>L<sub>2</sub>]/[M]<sup>2</sup>[L]<sup>2</sup> | 1 | 0.15% |
| [M<sub>2</sub>HL]/[MHL][M] | 1 | 0.15% |
| [M<sub>2</sub>(OH)L][H]/[M]<sup>2</sup>[L] | 1 | 0.15% |
| [M<sub>2</sub>(H<sub>-1</sub>L)<sub>2</sub>][H]<sup>2</sup>/[M]<sup>2</sup>[L]<… | 1 | 0.15% |

---

### Step 15: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND c.beta_definition_name = '[ML]/[M][L]')",
  "limit": 500
}
```

[summary]
## search_stability — 200 row(s)

### logK — 150 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_8126 | 8-Hydroxyquinoline (8-Quino… | HL | Oc1cccc2cccnc12 | 4 | 1 | 25 | 0~1 | *** | 4 |
| metal_61 | Fe^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 4 | 1 | 25 | 0.1~3 | *** | 4 |
| metal_61 | Fe^[3+] | ligand_6287 | rac-(1,2-Dimethylethylene)d… | H4L | CC(C(C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 3 | 1 | 20~25 | 0.1~0.5 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_6288 | meso-(1,2-Dimethylethylene)… | H4L | C[C@H]([C@H](C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 3 | 1 | 20~25 | 0.1~0.5 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 3 | 1 | 20~25 | 0.1 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 3 | 1 | 25 | 0.5~3 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_8873 | Propanedioic acid (Malonic … | H2L | O=C(O)CC(=O)O | 3 | 1 | 25 | 0.1~1 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 2 | 1 | 25 | 0.5~3 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_5777 | L-2-Amino-3-phenylpropanoic… | HL | N[C@@H](Cc1ccccc1)C(=O)O | 2 | 1 | 20~25 | 1~3 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 2 | 1 | 25 | 0.5~1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_6311 | Trimethylenedinitrilotetraa… | H4L | O=C(O)CN(CCCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 20 | 0.1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_6333 | (2-Hydroxytrimethylene)dini… | H4L | O=C(O)CN(CC(=O)O)CC(O)CN(CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_7944 | 2,3-Dihydroxypyridine (3-Hy… | HL | Oc1cccnc1O | 2 | 1 | 25 | 0.1~1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_8558 | Chloroacetic acid | HL | O=C(O)CCl | 2 | 1 | 20~25 | 1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_5761 | L-2-Aminopropanoic acid (Al… | HL | C[C@H](N)C(=O)O | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5804 | L-2-Aminopentanedioic acid … | H2L | N[C@@H](CCC(=O)O)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5809 | L-2-Amino-3-phosphopropanoi… | H3L | N[C@@H](COP(=O)(O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5828 | L-2-Amino-3-hydroxypropanoi… | HL | N[C@@H](CO)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5829 | L-2-Amino-3-hydroxybutanoic… | HL | C[C@@H](O)[C@H](N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5843 | L-2-Aminobutanedioic acid 4… | HL | NC(=O)C[C@H](N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5863 | L-2-Amino-4-(methylthio)but… | HL | CSCC[C@H](N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5907 | L-2-Amino-3-(3-indolyl)prop… | HL | N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5925 | N-Methylglycine (Sarcosine) | HL | CNCC(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5930 | L-Pyrrolidine-2-carboxylic … | HL | O=C(O)C1CCCN1 | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5937 | N-(Phosphonomethyl)glycine … | H3L | O=C(O)CNCP(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5938 | (Carboxymethylamino)acetohy… | H2L | O=C(O)CNCC(=O)NO | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5941 | L-4-Hydroxypyrrolidine-2-ca… | HL | O=C(O)C1CC(O)CN1 | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5976 | Ethylenediiminodi-3-propano… | H2L | O=C(O)CCNCCNCCC(=O)O | 1 | 1 | 30 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5977 | Ethylenediiminodi-2-propano… | H2L | CC(NCCNC(C)C(=O)O)C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5984 | Ethylenediiminodibutanedioi… | H4L | O=C(O)CC(NCCNC(CC(=O)O)C(=O)O)C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5994 | N,N'-Bis(2-hydroxyphenyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)c1ccccc1O)c1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5995 | rac-Ethylenediiminobis[(2-h… | H4L | O=C(O)C(Cc1ccccc1O)NCCNC(Cc1ccccc1O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5996 | meso-Ethylenediiminobis[(2-… | H4L | O=C(O)C(Cc1ccccc1O)NCCNC(Cc1ccccc1O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5997 | rac-Trimethylenebis[2-(2-hy… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5998 | meso-Trimethylenebis[2-(2-h… | H4L | Cc1cc(C)c(O)c([C@H](NCCCN[C@@H](C(=O)O)c2cc(C)cc(C)c2O)C(=O)O)c1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6019 | N,N-Bis(phosphonomethyl)gly… | H5L | O=C(O)CN(CP(=O)(O)O)CP(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6020 | N-(Carboxymethyl)-N-(2-hydr… | H2L | O=C(O)CN(CCO)CC(=O)NO | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6036 | N,N'-Bis(carboxymethyl)ethy… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)NO)CC(=O)NO | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6037 | N,N'-Bis(2-hydroxybenzyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)Cc1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6038 | N,N'-Bis(2-hydroxy-5-sulfob… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1cc(S(=O)(=O)O)ccc1O)Cc1cc(S(=O)(=O)O)ccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6039 | N,N"-Bis(2-hydroxybenzyl)di… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6041 | N,N'-Bis(3-hydroxy-5-phosph… | H6L | Cc1ncc(COP(=O)(O)O)c(CN(CCN(CC(=O)O)Cc2c(COP(=O)(O)O)cnc(C)c2O)CC(=O)O)c1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6042 | N,N'-Bis(3-hydroxy-5-hydrox… | H4L | Cc1ncc(CO)c(CN(CCN(CC(=O)O)Cc2c(CO)cnc(C)c2O)CC(=O)O)c1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6043 | N,N'-Bis(3-hydroxy-5-hydrox… | H4L | Cc1c([O-])c(CN(CCN(CC(=O)O)Cc2c(CO)c[n+](C)c(C)c2[O-])CC(=O)O)c(CO)c[n+]1C | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6044 | N-(2-Hydroxybenzyl)-N'-(3-h… | H4L | Cc1ncc(CO)c(CN(CCN(CC(=O)O)Cc2ccccc2O)CC(=O)O)c1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6045 | N-(2-Hydroxy-3,5-dimethylbe… | H4L | Cc1cc(C)c(O)c(CN(CCN(CC(=O)O)Cc2c(C)c[n+](C)c(C)c2[O-])CC(=O)O)c1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6046 | N,N'-Bis(3-hydroxy-6-methyl… | H4L | Cc1ccc(O)c(CN(CCN(CC(=O)O)Cc2nc(C)ccc2O)CC(=O)O)n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6047 | N,N''-Bis(3-hydroxy-6-methy… | H5L | Cc1ccc(O)c(CN(CCN(CCN(CC(=O)O)Cc2nc(C)ccc2O)CC(=O)O)CC(=O)O)n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6054 | N,N'-Bis(carboxymethyl)ethy… | H4L | CC(C)N(O)C(=O)CN(CCN(CC(=O)O)CC(=O)N(O)C(C)C)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6057 | N,N',N''-Tris(carboxymethyl… | H5L | CC(C)N(O)C(=O)CN(CCN(CCN(CC(=O)O)CC(=O)N(O)C(C)C)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6063 | 1,5-Diazacyclooctane-N,N'-d… | H2L | O=C(O)CN1CCCN(CC(=O)O)CCC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6076 | 1,4,7-Triazacyclononane-N,N… | H3L | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6084 | 1-Oxa-4,7,10-triazacyclodod… | H3L | O=C(O)CN1CCOCCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6085 | 1-Oxa-4,7,11-triazacyclotri… | H3L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCOCC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6086 | 1-Oxa-4,8,12-triazacyclotet… | H3L | O=C(O)CN1CCCN(CC(=O)O)CCOCCN(CC(=O)O)CCC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6087 | 1,7-Dioxa-4,10,13-triazacyc… | H3L | O=C(O)CN1CCOCCN(CC(=O)O)CCN(CC(=O)O)CCOCC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6088 | 1,7,13-Trioxa-4,10,16-triaz… | H3L | O=C(O)CN1CCOCCN(CC(=O)O)CCOCCN(CC(=O)O)CCOCC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6102 | 1,4,7,10-Tetraazacyclododec… | H4L | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6104 | 1,4,7,10-Tetraazacyclotride… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6109 | 1,4,8,11-Tetraazacyclotetra… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6113 | 1-Oxa-4,7,10,13-tetraazacyc… | H4L | O=C(O)CN1CCOCCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6120 | 3,11-Bis(carboxymethyl)-7-m… | H2L | CN1CCCN(CC(=O)O)Cc2cccc(n2)CN(CC(=O)O)CCC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6121 | 3,6,9-Tris(carboxymethyl)-3… | H3L | O=C(O)CN1CCN(CC(=O)O)Cc2cccc(n2)CN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6123 | 7,24-Dihydroxy-8,23-dioxo-1… | H2L | O=C(O)CN1CCOCCOCCN(CC(=O)O)CCC(=O)N(O)CCOCCOCCN(O)C(=O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6124 | 6,16-Bis(carboxymethyl)-1,1… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6125 | 7,19-Bis(carboxymethyl)-1,1… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6135 | L-2-(Carboxymethyl)iminodia… | H3L | O=C(O)CNC(CC(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6195 | N-(2-Carboxyethyl)-N-(phosp… | H4L | O=C(O)CCN(CC(=O)O)CP(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6200 | N-(3-Carboxy-2-hydroxy-5-su… | H4L | O=C(O)CN(CC(=O)O)Cc1cc(S(=O)(=O)O)cc(C(=O)O)c1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6203 | N,N-Bis(carboxymethyl)amino… | H3L | O=C(O)CN(CC(=O)O)CC(=O)NO | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6204 | N-(2-Hydroxyethyl)iminodiac… | H2L | O=C(O)CN(CCO)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6239 | N,N-Bis(carboxymethyl)glycy… | H3L | O=C(O)CNC(=O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6240 | N,N-Bis(carboxymethyl)glycy… | H3L | O=C(O)CNC(=O)CNC(=O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6241 | N,N-Bis(carboxymethyl)glycy… | H3L | O=C(O)CNC(=O)CNC(=O)CNC(=O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6253 | N-(2-Aminoethyl)iminodiacet… | H2L | NCCN(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6276 | N-(2-Hydroxybenzyl)ethylene… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6292 | DL-Ethylenedinitrilo-N,N'-d… | H4L | CC(C(=O)O)N(CCN(CC(=O)O)C(C)C(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6310 | Ethylenedinitrilotetra(3-pr… | H4L | O=C(O)CCN(CCC(=O)O)CCN(CCC(=O)O)CCC(=O)O | 1 | 1 | 30 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6315 | Hexamethylenedinitrilotetra… | H4L | O=C(O)CN(CCCCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6335 | Oxybis(ethylenenitrilo)tetr… | H4L | O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6342 | Ethylenebis(oxyethylenenitr… | H4L | O=C(O)CN(CCOCCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6343 | N,N'-Diglycyl-1,2-diaminoet… | H4L | O=C(O)CN(CC(=O)O)CC(=O)NCCNC(=O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6348 | Thiobis(ethylenenitrilo)tet… | H4L | O=C(O)CN(CCSCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6366 | Triethylenetetranitrilohexa… | H6L | O=C(O)CN(CCN(CCN(CC(=O)O)CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6372 | Glycylglycine (Diglycine) | HL | NCC(=O)NCC(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6704 | 2-Amino-5-sulfobenzoic acid | HL | Nc1ccc(S(=O)(=O)O)cc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6760 | 1,4-Diazine-2-carboxylic ac… | HL | O=C(O)c1cnccn1 | 1 | 1 | 25 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6770 | Pyridine-2-phosphonic-6-car… | H3L | O=C(O)c1cccc(P(=O)(O)O)n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6774 | Pyridine-2,6-dicarboxylic a… | H2L | O=C(O)c1cccc(C(=O)O)n1 | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6780 | 4-Aminopyridine-2,6-dicarbo… | H2L | Nc1cc(C(=O)O)nc(C(=O)O)c1 | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6982 | Aminoacetohydroxamic acid (… | HL | NCC(=O)NO | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6983 | L-2-Aminopropanohydroxamic … | HL | CC(N)C(=O)NO | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6996 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)NO | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7000 | Glycylglycylglycinehydroxam… | HL | NCC(=O)NCC(=O)NCC(=O)NO | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7001 | L-Prolyl-L-leucinehydroxami… | HL | CC(C)C[C@H](NC(=O)[C@@H]1CCCN1)C(=O)NO | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7002 | L-Prolyl-L-leucylglycinehyd… | HL | CC(C)C[C@H](NC(=O)[C@@H]1CCCN1)C(=O)NCC(=O)NO | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7154 | Iminodiacetohydroxamic acid | H2L | O=C(CNCC(=O)NO)NO | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7295 | Nitrilotriacetohydroxamic a… | H3L | O=C(CN(CC(=O)NO)CC(=O)NO)NO | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7320 | Ethylenedinitrilotetraaceto… | H4L | O=C(CN(CCN(CC(=O)NO)CC(=O)NO)CC(=O)NO)NO | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7340 | 1,3,5-Tris(dimethylamino)-1… | L | CN(C)[C@H]1[C@@H](O)[C@@H](N(C)C)[C@@H](O)[C@@H](N(C)C)[C@H]1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7391 | Piperazine-N,N'-diacetohydr… | H2L | O=C(CN1CCN(C(=O)NO)CC1)NO | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7422 | 1,4,7-Tris(3-hydroxy-6-meth… | H3L | Cc1ccc(O)c(CN2CCN(Cc3nc(C)ccc3O)CCN(Cc3nc(C)ccc3O)CC2)n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7579 | 1,4,10-Trioxa-7,13-diazacyc… | L | C1COCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7596 | 4,7,13,18-Tetraoxa-1,10-dia… | L | C1COCCN2CCOCCN(CCO1)CCOCC2 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7600 | 4,7,13,16,21-Pentaoxa-1,10-… | L | C1COCCN2CCOCCOCCN(CCO1)CCOCC2 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7601 | 4,7,13,16,21,24-Hexaoxa-1,1… | L | C1COCCN2CCOCCOCCN(CCO1)CCOCCOCC2 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7673 | 3,7,11,15-Tetraaza-5,13(2)-… | H2L | Cc1cc2c(O)c(c1)CNCc1cccc(n1)CNCc1cc(C)cc(c1O)CNCc1cccc(n1)CNC2 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7943 | 1-Hydroxy-1,2-dihydropyridi… | HL | O=c1ccccn1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7945 | 1-Methyl-3-hydroxy-1,2-dihy… | HL | Cn1cccc(O)c1=O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7947 | 3,4-Dihydroxypyridine (3-Hy… | HL | Oc1ccncc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7949 | 1,2-Dimethyl-3,4-dihydroxyp… | HL | Cc1c(O)c(=O)ccn1C | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7950 | 1,2-Diethyl-3,4-dihydroxypy… | HL | CCc1c(O)c(=O)ccn1CC | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7982 | 1,3-Dihydroxy-4-(2-pyridyla… | H2L | Oc1ccc(/N=N/c2ccccn2)c(O)c1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8047 | Pyridine-2-carboxaldehyde o… | HL | O/N=C/c1ccccn1 | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8054 | 2-(Methylsulfonamidomethyl)… | HL | CS(=O)(=O)NCc1ccccn1 | 1 | 1 | 30 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8134 | 8-Hydroxyquinoline-5-sulfon… | H2L | O=S(=O)(O)c1ccc(O)c2ncccc12 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8136 | 8-Hydroxy-7-iodoquinoline-5… | H2L | O=S(=O)(O)c1cc(I)c(O)c2ncccc12 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8191 | 1,10-Phenanthroline (Dipyri… | L | c1cnc2c(c1)ccc1cccnc12 | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8201 | 5-Nitro-1,10-phenanthroline | L | O=[N+]([O-])c1cc2cccnc2c2ncccc12 | 1 | 1 | 25 | 0 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8360 | Amino(phenyl)methylenedipho… | H4L | NC(c1ccccc1)(P(=O)(O)O)P(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8388 | Ethylenebis[imino(phenyl)me… | H4L | O=P(O)(O)C(NCCNC(c1ccccc1)P(=O)(O)O)c1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8389 | Ethylenebis[imino(2-hydroxy… | H4L | O=P(O)(O)C(NCCNC(c1ccccc1O)P(=O)(O)O)c1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8400 | Perhydro-1,4-oxazine-4-ylme… | H4L | O=P(O)(O)C(N1CCOCC1)P(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8421 | N,N'-Dimethylethylenebis(ni… | H4L | CN(CCN(C)CP(=O)(O)O)CP(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8424 | N,N'-Bis(2-hydroxyethyl)eth… | H4L | O=P(O)(O)CN(CCO)CCN(CCO)CP(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8427 | N-(2-Hydroxyethyl)ethylened… | H6L | O=P(O)(O)CN(CCO)CCN(CP(=O)(O)O)CP(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8434 | Pyridine-2,6-diphosphonic a… | H4L | O=P(O)(O)c1cccc(P(=O)(O)O)n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8440 | Ethylenebis(iminomethylenep… | H2L | O=[PH](O)CNCCNC[PH](=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8442 | Ethylenebis(imino(2-hydroxy… | H4L | O=[PH](O)C(NCCNC(c1ccccc1O)[PH](=O)O)c1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8453 | Ethylenebis[imino(2-hydroxy… | H4L | CP(=O)(O)C(NCCNC(c1ccccc1O)P(C)(=O)O)c1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8454 | N,N'-Bis(2-hydroxybenzyl)et… | H4L | COP(=O)(O)C(NCCNC(c1ccccc1O)P(=O)(O)OC)c1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8455 | N,N'-Bis(2-hydroxybenzyl)et… | H4L | CCOP(=O)(O)C(NCCNC(c1ccccc1O)P(=O)(O)OCC)c1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8464 | Methanoic acid (Formic acid) | HL | O=CO | 1 | 1 | 25 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8467 | Propanoic acid (Propionic a… | HL | CCC(=O)O | 1 | 1 | 25 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8468 | Butanoic acid (Butyric acid) | HL | CCCC(=O)O | 1 | 1 | 25 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8469 | Pentanoic acid (Valeric aci… | HL | CCCCC(=O)O | 1 | 1 | 25 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8473 | 2-Methylpropanoic acid (Iso… | HL | CC(C)C(=O)O | 1 | 1 | 25 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8479 | 3-Methylbutanoic acid (Isov… | HL | CC(C)CC(=O)O | 1 | 1 | 25 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 1 | 1 | 25 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8668 | D-gluco-Pentahydroxyhexanoi… | HL | O=C(O)[C@H](O)[C@@H](O)[C@H](O)[C@H](O)CO | 1 | 1 | 25 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8874 | Ethane-1,1-dicarboxylic aci… | H2L | CC(C(=O)O)C(=O)O | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8877 | Pentane-1,1-dicarboxylic ac… | H2L | CCCCC(C(=O)O)C(=O)O | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8885 | 2-Phenylethane-1,1-dicarbox… | H2L | O=C(O)C(Cc1ccccc1)C(=O)O | 1 | 1 | 25 | 0.5 | *** | 1 |

### ΔH — 12 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8464 | Methanoic acid (Formic acid) | HL | O=CO | 1 | 1 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8467 | Propanoic acid (Propionic a… | HL | CCC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8468 | Butanoic acid (Butyric acid) | HL | CCCC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8469 | Pentanoic acid (Valeric aci… | HL | CCCCC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8473 | 2-Methylpropanoic acid (Iso… | HL | CC(C)C(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8479 | 3-Methylbutanoic acid (Isov… | HL | CC(C)CC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8873 | Propanedioic acid (Malonic … | H2L | O=C(O)CC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |

### ΔS — 12 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8464 | Methanoic acid (Formic acid) | HL | O=CO | 1 | 1 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8467 | Propanoic acid (Propionic a… | HL | CCC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8468 | Butanoic acid (Butyric acid) | HL | CCCC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8469 | Pentanoic acid (Valeric aci… | HL | CCCCC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8473 | 2-Methylpropanoic acid (Iso… | HL | CC(C)C(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8479 | 3-Methylbutanoic acid (Isov… | HL | CC(C)CC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8873 | Propanedioic acid (Malonic … | H2L | O=C(O)CC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |

---

### Step 16: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_62 AND c.beta_definition_name = '[ML]/[M][L]')",
  "limit": 500
}
```

[summary]
## search_stability — 200 row(s)

### logK — 137 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 7 | 1 | 10~40 | 0~3 | *** | 7 |
| metal_62 | Fe^[2+] | ligand_5828 | L-2-Amino-3-hydroxypropanoi… | HL | N[C@@H](CO)C(=O)O | 4 | 1 | 20~37 | 0.1~3 | *** | 4 |
| metal_62 | Fe^[2+] | ligand_5829 | L-2-Amino-3-hydroxybutanoic… | HL | C[C@@H](O)[C@H](N)C(=O)O | 3 | 1 | 20~37 | 0.1~1 | *** | 3 |
| metal_62 | Fe^[2+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 3 | 1 | 20~25 | 0.1~1 | *** | 3 |
| metal_62 | Fe^[2+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 3 | 1 | 20~25 | 0.1~1 | *** | 3 |
| metal_62 | Fe^[2+] | ligand_5777 | L-2-Amino-3-phenylpropanoic… | HL | N[C@@H](Cc1ccccc1)C(=O)O | 2 | 1 | 20~25 | 1~3 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_5843 | L-2-Aminobutanedioic acid 4… | HL | NC(=O)C[C@H](N)C(=O)O | 2 | 1 | 20~25 | 1~3 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_5907 | L-2-Amino-3-(3-indolyl)prop… | HL | N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O | 2 | 1 | 20~25 | 1~3 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_6140 | N-Methyliminodiacetic acid … | H2L | CN(CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_6287 | rac-(1,2-Dimethylethylene)d… | H4L | CC(C(C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_6288 | meso-(1,2-Dimethylethylene)… | H4L | C[C@H]([C@H](C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 2 | 1 | 25 | 0.1~1 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_8156 | 2,2'-Bipyridyl | L | c1ccc(-c2ccccn2)nc1 | 2 | 1 | 25~30 | 0.1~1 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_8191 | 1,10-Phenanthroline (Dipyri… | L | c1cnc2c(c1)ccc1cccnc12 | 2 | 1 | 25 | 0~0.1 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_8193 | 5-Methyl-1,10-phenanthroline | L | Cc1cc2cccnc2c2ncccc12 | 2 | 1 | 22~25 | 0~0.1 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_5761 | L-2-Aminopropanoic acid (Al… | HL | C[C@H](N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7653 | 6,16-Dioxa-3,9,13,19-tetraa… | L | c1cc2nc(c1)CNCCOCCNCc1cccc(n1)CNCCOCCNC2 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5765 | L-2-Amino-3-methylbutanoic … | HL | CC(C)[C@H](N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5766 | L-2-Amino-4-methylpentanoic… | HL | CC(C)C[C@H](N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5769 | 2-Amino-2-methylpropanoic a… | HL | CC(C)(N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5770 | DL-2-Amino-4-pentenoic acid | HL | C=CCC(N)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5788 | 3-Aminopropanoic acid (beta… | HL | NCCC(=O)O | 1 | 1 | 25 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5804 | L-2-Aminopentanedioic acid … | H2L | N[C@@H](CCC(=O)O)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5844 | L-2-Aminopentanedioic acid … | HL | NC(=O)CC[C@H](N)C(=O)O | 1 | 1 | 25 | 3 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5856 | L-2-Amino-3-mercaptopropano… | H2L | N[C@@H](CS)C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5860 | DL-2-Amino-3-(2-mercaptoimi… | H2L | NC(Cc1cnc(S)[nH]1)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5863 | L-2-Amino-4-(methylthio)but… | HL | CSCC[C@H](N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 1 | 1 | 25 | 3 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5925 | N-Methylglycine (Sarcosine) | HL | CNCC(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5930 | L-Pyrrolidine-2-carboxylic … | HL | O=C(O)C1CCCN1 | 1 | 1 | 20 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5937 | N-(Phosphonomethyl)glycine … | H3L | O=C(O)CNCP(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5941 | L-4-Hydroxypyrrolidine-2-ca… | HL | O=C(O)C1CC(O)CN1 | 1 | 1 | 20 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5975 | Ethylenediiminodiacetic aci… | H2L | O=C(O)CNCCNCC(=O)O | 1 | 1 | 25 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5976 | Ethylenediiminodi-3-propano… | H2L | O=C(O)CCNCCNCCC(=O)O | 1 | 1 | 30 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5977 | Ethylenediiminodi-2-propano… | H2L | CC(NCCNC(C)C(=O)O)C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6021 | N,N-Bis(2-hydroxyethyl)glyc… | HL | O=C(O)CN(CCO)CCO | 1 | 1 | 30 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6050 | DL-1-Methylethylenedinitril… | H2L | CC(CN(CC(N)=O)CC(=O)O)N(CC(N)=O)CC(=O)O | 1 | 1 | 37 | 0.15 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6051 | DL-1-Ethylethylenedinitrilo… | H2L | CCC(CN(CC(N)=O)CC(=O)O)N(CC(N)=O)CC(=O)O | 1 | 1 | 37 | 0.15 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6052 | rac-1,2-Dimethylethylenedin… | H2L | CC(C(C)N(CC(N)=O)CC(=O)O)N(CC(N)=O)CC(=O)O | 1 | 1 | 37 | 0.15 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6053 | meso-1,2-Dimethylethylenedi… | H2L | CC(C(C)N(CC(N)=O)CC(=O)O)N(CC(N)=O)CC(=O)O | 1 | 1 | 37 | 0.15 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6056 | N,N'-Bis(2-pyridylmethyl)et… | H2L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccn1)Cc1ccccn1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6064 | 1-Oxa-4,7-diazacyclononane-… | H2L | O=C(O)CN1CCOCCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6067 | 1,4-Dioxa-7,10-diazacyclodo… | H2L | O=C(O)CN1CCOCCOCCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6068 | 1,4-Dioxa-7,11-diazacyclotr… | H2L | O=C(O)CN1CCCN(CC(=O)O)CCOCCOCC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6069 | 1,7-Dioxa-4,10-diazacyclodo… | H2L | O=C(O)CN1CCOCCN(CC(=O)O)CCOCC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6070 | 1,4,10-Trioxa-7,13-diazacyc… | H2L | O=C(O)CN1CCOCCOCCN(CC(=O)O)CCOCC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6071 | 1,4,10,13-Tetraoxa-7,16-dia… | H2L | O=C(O)CN1CCOCCOCCN(CC(=O)O)CCOCCOCC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6082 | 1-Oxa-4,7,10-triazacyclodod… | H2L | O=C(O)CN1CCNCCN(CC(=O)O)CCOCC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6084 | 1-Oxa-4,7,10-triazacyclodod… | H3L | O=C(O)CN1CCOCCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6102 | 1,4,7,10-Tetraazacyclododec… | H4L | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6104 | 1,4,7,10-Tetraazacyclotride… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6109 | 1,4,8,11-Tetraazacyclotetra… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6135 | L-2-(Carboxymethyl)iminodia… | H3L | O=C(O)CNC(CC(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6141 | N-Ethyliminodiacetic acid | H2L | CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6142 | N-Propyliminodiacetic acid | H2L | CCCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6193 | N-(Phosphonomethyl)iminodia… | H4L | O=C(O)CN(CC(=O)O)CP(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6204 | N-(2-Hydroxyethyl)iminodiac… | H2L | O=C(O)CN(CCO)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6222 | N-(2-Methoxyethyl)iminodiac… | H2L | COCCN(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6224 | N-(2-Tetrahydropyranylmethy… | H2L | O=C(O)CN(CC(=O)O)CC1CCCCO1 | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6243 | 5-Amino-2,4,6-trioxo-1,3-pe… | H3L | O=C(O)CN(CC(=O)O)C1C(=O)NC(=O)NC1=O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6248 | N-(2-Mercaptoethyl)iminodia… | H3L | O=C(O)CN(CCS)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6249 | N-[2-(Methylthio)ethyl]imin… | H2L | CSCCN(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6253 | N-(2-Aminoethyl)iminodiacet… | H2L | NCCN(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6292 | DL-Ethylenedinitrilo-N,N'-d… | H4L | CC(C(=O)O)N(CCN(CC(=O)O)C(C)C(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6310 | Ethylenedinitrilotetra(3-pr… | H4L | O=C(O)CCN(CCC(=O)O)CCN(CCC(=O)O)CCC(=O)O | 1 | 1 | 30 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6311 | Trimethylenedinitrilotetraa… | H4L | O=C(O)CN(CCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6313 | Tetramethylenedinitrilotetr… | H4L | O=C(O)CN(CCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6314 | Pentamethylenedinitrilotetr… | H4L | O=C(O)CN(CCCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6315 | Hexamethylenedinitrilotetra… | H4L | O=C(O)CN(CCCCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6316 | Octamethylenedinitrilotetra… | H4L | O=C(O)CN(CCCCCCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6333 | (2-Hydroxytrimethylene)dini… | H4L | O=C(O)CN(CC(=O)O)CC(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6335 | Oxybis(ethylenenitrilo)tetr… | H4L | O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6342 | Ethylenebis(oxyethylenenitr… | H4L | O=C(O)CN(CCOCCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6348 | Thiobis(ethylenenitrilo)tet… | H4L | O=C(O)CN(CCSCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6366 | Triethylenetetranitrilohexa… | H6L | O=C(O)CN(CCN(CCN(CC(=O)O)CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6371 | 1,4-Bis[2,5,5-tris(carboxym… | H6L | O=C(O)CN(CCN(CC(=O)O)Cc1ccc(CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O)cc1)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6372 | Glycylglycine (Diglycine) | HL | NCC(=O)NCC(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6731 | N-Phenyliminodiacetic acid | H2L | O=C(O)CN(CC(=O)O)c1ccccc1 | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6751 | 1,2-Phenylenedinitrilotetra… | H4L | O=C(O)CN(CC(=O)O)c1ccccc1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6760 | 1,4-Diazine-2-carboxylic ac… | HL | O=C(O)c1cnccn1 | 1 | 1 | 25 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6762 | Pyridine-2-carboxylic acid … | HL | O=C(O)c1ccccn1 | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6763 | 6-Methylpyridine-2-carboxyl… | HL | Cc1cccc(C(=O)O)n1 | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6764 | Quinoline-2-carboxylic acid… | HL | O=C(O)c1ccc2ccccc2n1 | 1 | 1 | 25 | 0 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6768 | Quinoline-8-carboxylic acid | HL | O=C(O)c1cccc2cccnc12 | 1 | 1 | 25 | 0 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6770 | Pyridine-2-phosphonic-6-car… | H3L | O=C(O)c1cccc(P(=O)(O)O)n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6774 | Pyridine-2,6-dicarboxylic a… | H2L | O=C(O)c1cccc(C(=O)O)n1 | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6780 | 4-Aminopyridine-2,6-dicarbo… | H2L | Nc1cc(C(=O)O)nc(C(=O)O)c1 | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6793 | N-(2-Pyridylmethyl)iminodia… | H2L | O=C(O)CN(CC(=O)O)Cc1ccccn1 | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6794 | N-(6-Methyl-2-pyridylmethyl… | H2L | Cc1cccc(CN(CC(=O)O)CC(=O)O)n1 | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7029 | Ethylenediamine | L | NCCN | 1 | 1 | 25 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7212 | 1,4,7-Triazaheptane (Diethy… | L | NCCNCCN | 1 | 1 | 25 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7345 | Nitrilotris(ethyleneamine) … | L | NCCN(CCN)CCN | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7348 | Ethylenedinitrilotetrakis(e… | L | NCCN(CCN)CCN(CCN)CCN | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7349 | Ethylenedinitrilotetrakis(t… | L | NCCCN(CCCN)CCN(CCCN)CCCN | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7489 | 3,6,9-Triaza-1(2,6)-pyridin… | L | c1cc2nc(c1)CNCCNCCNC2 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7490 | 4,7,11-Triaza-1(2,6)-pyrini… | L | c1cc2nc(c1)CNCCNCCCNC2 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7491 | 3,7,11-Triaza-1(2,6)-pyridi… | L | c1cc2nc(c1)CNCCCNCCCNC2 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7500 | 1,4,7,10,13-Pentaazacyclohe… | L | C1CNCCNCCNCCNCCNC1 | 1 | 1 | 35 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7508 | 3,6,10,13-Tetraaza-1(2,6)-p… | L | c1cc2nc(c1)CNCCNCCCNCCNC2 | 1 | 1 | 35 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7530 | 1,4,7,10,13,16,19-Heptaazac… | L | C1CNCCNCCNCCNCCNCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7569 | 1-Oxa-4,7-diazacyclononane … | L | C1CNCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7614 | 1,4-Dioxa-7,10,13-triazacyc… | L | C1CNCCOCCOCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7616 | 1,4-Dioxa-7,10,14-triazacyc… | L | C1CNCCNCCOCCOCCNC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7618 | 1-Oxa-4,7,10,13-tetraazacyc… | L | C1CNCCNCCOCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7645 | 1,13-Dioxa-4,7,10,16,19,22-… | L | C1CNCCOCCNCCNCCNCCOCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7661 | 5-(2-Hydroxyphenyl)-1,4,8,1… | HL | Oc1ccccc1C1CCNCCNCCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7673 | 3,7,11,15-Tetraaza-5,13(2)-… | H2L | Cc1cc2c(O)c(c1)CNCc1cccc(n1)CNCc1cc(C)cc(c1O)CNCc1cccc(n1)CNC2 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7739 | 1-Thia-4,7-diazacyclononane… | L | C1CNCCSCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7751 | 1-Thia-4,7,10-triazacyclodo… | L | C1CNCCSCCNCCN1 | 1 | 1 | 35 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7755 | 1-Thia-4,7,11,14-tetraazacy… | L | C1CNCCNCCSCCNCCNC1 | 1 | 1 | 35 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7771 | 1,2-Diazole (Pyrazole) | L | c1cn[nH]c1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7795 | 1,3-Diazole (Imidazole) | L | c1c[nH]cn1 | 1 | 1 | 30 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7862 | 2-(2-Pyridyl)imidazole | L | c1ccc(-c2ncc[nH]2)nc1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7863 | 4-(2-Pyridyl)imidazole | L | c1ccc(-c2c[nH]cn2)nc1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7890 | Pyridine (Azine) | L | c1ccncc1 | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8071 | 2-(2-Pyridyl)-1,3-thiazole | L | c1ccc(-c2nccs2)nc1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8072 | 4-(2-Pyridyl)-1,3-thiazole | L | c1ccc(-c2cscn2)nc1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8081 | 2-(Aminomethyl)pyridine (2-… | L | NCc1ccccn1 | 1 | 1 | 30 | 0 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8112 | 2-(Methylaminomethyl)pyridi… | L | CNCc1ccccn1 | 1 | 1 | 30 | 0 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8172 | 6,6'-Bis(aminomethyl)-2,2'-… | L | NCc1cccc(-c2cccc(CN)n2)n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8174 | Iminobis(methylene-2-pyridi… | L | c1ccc(CNCc2ccccn2)nc1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8192 | 2-Methyl-1,10-phenanthroline | L | Cc1ccc2ccc3cccnc3c2n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8195 | 4,7-Dimethyl-1,10-phenanthr… | L | Cc1ccnc2c1ccc1c(C)ccnc12 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8196 | 5,6-Dimethyl-1,10-phenanthr… | L | Cc1c(C)c2cccnc2c2ncccc12 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8199 | 5-Chloro-1,10-phenanthroline | L | Clc1cc2cccnc2c2ncccc12 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8200 | 5-Bromo-1,10-phenanthroline | L | Brc1cc2cccnc2c2ncccc12 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8201 | 5-Nitro-1,10-phenanthroline | L | O=[N+]([O-])c1cc2cccnc2c2ncccc12 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8204 | 2,6-Di(2-pyridyl)pyridine (… | L | c1ccc(-c2cccc(-c3ccccn3)n2)nc1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8205 | Nitrilotris(methylene-2-pyr… | L | c1ccc(CN(Cc2ccccn2)Cc2ccccn2)nc1 | 1 | 1 | 25 | 0.1 | *** | 1 |

### ΔH — 18 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 3 | 1 | 10~40 | 0 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_5828 | L-2-Amino-3-hydroxypropanoi… | HL | N[C@@H](CO)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_5829 | L-2-Amino-3-hydroxybutanoic… | HL | C[C@@H](O)[C@H](N)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 1 | 1 | 25 | 3 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_5907 | L-2-Amino-3-(3-indolyl)prop… | HL | N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O | 1 | 1 | 25 | 3 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6335 | Oxybis(ethylenenitrilo)tetr… | H4L | O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6342 | Ethylenebis(oxyethylenenitr… | H4L | O=C(O)CN(CCOCCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7029 | Ethylenediamine | L | NCCN | 1 | 1 | 25 | 1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7212 | 1,4,7-Triazaheptane (Diethy… | L | NCCNCCN | 1 | 1 | 25 | 1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7345 | Nitrilotris(ethyleneamine) … | L | NCCN(CCN)CCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7348 | Ethylenedinitrilotetrakis(e… | L | NCCN(CCN)CCN(CCN)CCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_8174 | Iminobis(methylene-2-pyridi… | L | c1ccc(CNCc2ccccn2)nc1 | 1 | 1 | 25 | 0.1 | *** | 0 |

### ΔS — 18 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_5828 | L-2-Amino-3-hydroxypropanoi… | HL | N[C@@H](CO)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_5829 | L-2-Amino-3-hydroxybutanoic… | HL | C[C@@H](O)[C@H](N)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 1 | 1 | 25 | 3 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_5907 | L-2-Amino-3-(3-indolyl)prop… | HL | N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O | 1 | 1 | 25 | 3 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6335 | Oxybis(ethylenenitrilo)tetr… | H4L | O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6342 | Ethylenebis(oxyethylenenitr… | H4L | O=C(O)CN(CCOCCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7029 | Ethylenediamine | L | NCCN | 1 | 1 | 25 | 1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7212 | 1,4,7-Triazaheptane (Diethy… | L | NCCNCCN | 1 | 1 | 25 | 1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7345 | Nitrilotris(ethyleneamine) … | L | NCCN(CCN)CCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7348 | Ethylenedinitrilotetrakis(e… | L | NCCN(CCN)CCN(CCN)CCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_8174 | Iminobis(methylene-2-pyridi… | L | c1ccc(CNCc2ccccn2)nc1 | 1 | 1 | 25 | 0.1 | *** | 0 |

---

### Step 17: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT DISTINCT c.beta_definition_id, c.beta_definition_name FROM ligandmetal_card AS c WHERE c.beta_definition_name = '[ML]/[M][L]' AND c.metal_id IN (61, 62) LIMIT 5"
}
```

[summary]
## execute_srd46_sql - 1 row(s)

| beta_definition_id | beta_definition_name |
|--------------------|----------------------|
| beta_def_812 | [ML]/[M][L] |

---

### Step 18: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT c.metal_id, c.metal_name_SRD, c.ligand_id, c.ligand_name_SRD, c.card_id, s.constant_type, s.constant_value, s.temperature_c, s.ionic_strength_mol_l, s.solvent_name, s.electrolyte_composition FROM ligandmetal_card AS c JOIN ligandmetal_stability_measured AS s ON c.card_id = s.card_id WHERE c.metal_id IN (61, 62) AND c.beta_definition_id = 812 AND s.constant_type = 'K' ORDER BY c.ligand_id, c.metal_id"
}
```

[summary]
## execute_srd46_sql - 50 row(s)

| metal_id | metal_name_SRD | ligand_id | ligand_name_SRD | card_id | constant_type | constant_value | temperature_c |
|----------|----------------|-----------|-----------------|---------|---------------|----------------|---------------|
| metal_61 | Fe^[3+] | ligand_5760 | Aminoacetic acid (Glycine) | 275 | K | -8.57 | 25.0 |
| metal_61 | Fe^[3+] | ligand_5760 | Aminoacetic acid (Glycine) | 276 | K | -9.25 | 25.0 |
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | 142 | K | -4.13 | 25.0 |
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | 143 | K | 3.83 | 20.0 |
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | 144 | K | 3.73 | 25.0 |
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | 145 | K | 4.2 | 25.0 |
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | 146 | K | 4.36 | 10.0 |
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | 147 | K | 4.31 | 25.0 |
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | 148 | K | 4.28 | 40.0 |
| metal_61 | Fe^[3+] | ligand_5761 | L-2-Aminopropanoic acid (Alanine) | 665 | K | -8.88 | 25.0 |
| metal_62 | Fe^[2+] | ligand_5761 | L-2-Aminopropanoic acid (Alanine) | 484 | K | 3.54 | 20.0 |
| metal_62 | Fe^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | 732 | K | 3.37 | 20.0 |
| metal_62 | Fe^[2+] | ligand_5765 | L-2-Amino-3-methylbutanoic acid (Valine) | 857 | K | 3.39 | 20.0 |
| metal_62 | Fe^[2+] | ligand_5766 | L-2-Amino-4-methylpentanoic acid (Leucine) | 938 | K | 3.42 | 20.0 |
| metal_62 | Fe^[2+] | ligand_5769 | 2-Amino-2-methylpropanoic acid (2-Aminoisobutyric acid) | 1051 | K | 3.48 | 20.0 |
| metal_62 | Fe^[2+] | ligand_5770 | DL-2-Amino-4-pentenoic acid | 1073 | K | 3.73 | 25.0 |
| metal_61 | Fe^[3+] | ligand_5777 | L-2-Amino-3-phenylpropanoic acid (Phenylalanine) | 1275 | K | -8.9 | 20.0 |
| metal_61 | Fe^[3+] | ligand_5777 | L-2-Amino-3-phenylpropanoic acid (Phenylalanine) | 1276 | K | -10.39 | 25.0 |
| metal_62 | Fe^[2+] | ligand_5777 | L-2-Amino-3-phenylpropanoic acid (Phenylalanine) | 1198 | K | 3.26 | 20.0 |
| metal_62 | Fe^[2+] | ligand_5777 | L-2-Amino-3-phenylpropanoic acid (Phenylalanine) | 1199 | K | 3.74 | 25.0 |
| metal_62 | Fe^[2+] | ligand_5788 | 3-Aminopropanoic acid (beta-Alanine) | 1413 | K | 2.53 | 25.0 |
| metal_61 | Fe^[3+] | ligand_5802 | L-Aminobutanedioic acid (Aspartic acid) | 1797 | K | 11.4 | 20.0 |
| metal_62 | Fe^[2+] | ligand_5802 | L-Aminobutanedioic acid (Aspartic acid) | 1761 | K | 4.34 | 20.0 |
| metal_61 | Fe^[3+] | ligand_5804 | L-2-Aminopentanedioic acid (Glutamic acid) | 1905 | K | 12.1 | 20.0 |
| metal_62 | Fe^[2+] | ligand_5804 | L-2-Aminopentanedioic acid (Glutamic acid) | 1880 | K | 3.52 | 20.0 |

... 25 more row(s) omitted

---

### Step 19: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT c.metal_id, c.metal_name_SRD, c.ligand_id, c.ligand_name_SRD, c.card_id, s.constant_type, s.constant_value, s.temperature_c, s.ionic_strength_mol_l, s.electrolyte_composition, c.ligand_HxL_definition_SRD FROM ligandmetal_card AS c JOIN ligandmetal_stability_measured AS s ON c.card_id = s.card_id WHERE c.metal_id IN (61, 62) AND c.beta_definition_id = 812 AND s.constant_type = 'K' ORDER BY c.ligand_id, c.metal_id LIMIT 600"
}
```

[summary]
## execute_srd46_sql - 50 row(s)

| metal_id | metal_name_SRD | ligand_id | ligand_name_SRD | card_id | constant_type | constant_value | temperature_c |
|----------|----------------|-----------|-----------------|---------|---------------|----------------|---------------|
| metal_61 | Fe^[3+] | ligand_5760 | Aminoacetic acid (Glycine) | 275 | K | -8.57 | 25.0 |
| metal_61 | Fe^[3+] | ligand_5760 | Aminoacetic acid (Glycine) | 276 | K | -9.25 | 25.0 |
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | 142 | K | -4.13 | 25.0 |
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | 143 | K | 3.83 | 20.0 |
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | 144 | K | 3.73 | 25.0 |
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | 145 | K | 4.2 | 25.0 |
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | 146 | K | 4.36 | 10.0 |
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | 147 | K | 4.31 | 25.0 |
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | 148 | K | 4.28 | 40.0 |
| metal_61 | Fe^[3+] | ligand_5761 | L-2-Aminopropanoic acid (Alanine) | 665 | K | -8.88 | 25.0 |
| metal_62 | Fe^[2+] | ligand_5761 | L-2-Aminopropanoic acid (Alanine) | 484 | K | 3.54 | 20.0 |
| metal_62 | Fe^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | 732 | K | 3.37 | 20.0 |
| metal_62 | Fe^[2+] | ligand_5765 | L-2-Amino-3-methylbutanoic acid (Valine) | 857 | K | 3.39 | 20.0 |
| metal_62 | Fe^[2+] | ligand_5766 | L-2-Amino-4-methylpentanoic acid (Leucine) | 938 | K | 3.42 | 20.0 |
| metal_62 | Fe^[2+] | ligand_5769 | 2-Amino-2-methylpropanoic acid (2-Aminoisobutyric acid) | 1051 | K | 3.48 | 20.0 |
| metal_62 | Fe^[2+] | ligand_5770 | DL-2-Amino-4-pentenoic acid | 1073 | K | 3.73 | 25.0 |
| metal_61 | Fe^[3+] | ligand_5777 | L-2-Amino-3-phenylpropanoic acid (Phenylalanine) | 1275 | K | -8.9 | 20.0 |
| metal_61 | Fe^[3+] | ligand_5777 | L-2-Amino-3-phenylpropanoic acid (Phenylalanine) | 1276 | K | -10.39 | 25.0 |
| metal_62 | Fe^[2+] | ligand_5777 | L-2-Amino-3-phenylpropanoic acid (Phenylalanine) | 1198 | K | 3.26 | 20.0 |
| metal_62 | Fe^[2+] | ligand_5777 | L-2-Amino-3-phenylpropanoic acid (Phenylalanine) | 1199 | K | 3.74 | 25.0 |
| metal_62 | Fe^[2+] | ligand_5788 | 3-Aminopropanoic acid (beta-Alanine) | 1413 | K | 2.53 | 25.0 |
| metal_61 | Fe^[3+] | ligand_5802 | L-Aminobutanedioic acid (Aspartic acid) | 1797 | K | 11.4 | 20.0 |
| metal_62 | Fe^[2+] | ligand_5802 | L-Aminobutanedioic acid (Aspartic acid) | 1761 | K | 4.34 | 20.0 |
| metal_61 | Fe^[3+] | ligand_5804 | L-2-Aminopentanedioic acid (Glutamic acid) | 1905 | K | 12.1 | 20.0 |
| metal_62 | Fe^[2+] | ligand_5804 | L-2-Aminopentanedioic acid (Glutamic acid) | 1880 | K | 3.52 | 20.0 |

... 25 more row(s) omitted

---

### Step 20: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT c.ligand_id, c.ligand_name_SRD, c.ligand_HxL_definition_SRD, c.card_id, s.constant_value, s.temperature_c, s.ionic_strength_mol_l FROM ligandmetal_card AS c JOIN ligandmetal_stability_measured AS s ON c.card_id = s.card_id WHERE c.metal_id = 61 AND c.beta_definition_id = 812 AND s.constant_type = 'K' ORDER BY s.constant_value DESC LIMIT 50"
}
```

[summary]
## execute_srd46_sql - 50 row(s)

| ligand_id | ligand_name_SRD | ligand_HxL_definition_SRD | card_id | constant_value | temperature_c | ionic_strength_mol_l |
|-----------|-----------------|---------------------------|---------|----------------|---------------|----------------------|
| ligand_7422 | 1,4,7-Tris(3-hydroxy-6-methyl-2-pyridylmethyl)-1,4,7-triazacyclononane | H3L | 33079 | 50.0 | 25.0 | 0.1 |
| ligand_6037 | N,N'-Bis(2-hydroxybenzyl)ethylenedinitrilodiacetic acid (HBED) | H4L | 7431 | 39.01 | 25.0 | 0.1 |
| ligand_6124 | 6,16-Bis(carboxymethyl)-1,11(2,3)-tetrahydroxy-2,10,12,20-tetraoxo-3,6,9,13,16,... | *** | 9358 | 37.6 | 25.0 | 0.1 |
| ligand_6038 | N,N'-Bis(2-hydroxy-5-sulfobenzyl)ethylenedinitrilodiacetic acid (SHBED) | H4L | 7457 | 36.87 | 25.0 | 0.1 |
| ligand_6125 | 7,19-Bis(carboxymethyl)-1,13(2,3)-tetrahydroxy-2,12,14,24-tetraoxo-3,7,11,15,19... | *** | 9369 | 36.0 | 25.0 | 0.1 |
| ligand_5995 | rac-Ethylenediiminobis[(2-hydroxyphenyl)acetic acid] (EHPG) | H4L | 6569 | 35.54 | 25.0 | 0.1 |
| ligand_6046 | N,N'-Bis(3-hydroxy-6-methyl-2-pyridinylmethyl)ethylenedinitrilodiacetic acid (E... | H4L | 7631 | 35.08 | 25.0 | 0.1 |
| ligand_5998 | meso-Trimethylenebis[2-(2-hydroxy-3,5-dimethylphenyl)glycine] (meso-TMPHPG) | H4L | 6621 | 34.83 | 25.0 | 0.1 |
| ligand_5997 | rac-Trimethylenebis[2-(2-hydroxy-3,5-dimethylphenyl)glycine] (rac-TMPHPG) | *** | 6608 | 34.22 | 25.0 | 0.1 |
| ligand_6041 | N,N'-Bis(3-hydroxy-5-phosphomethyl-2-methyl-4-pyridylmethyl)ethylenedinitrilodi... | H6L | 7553 | 33.5 | 25.0 | 0.1 |
| ligand_5996 | meso-Ethylenediiminobis[(2-hydroxyphenyl)acetic acid] (EHPG) | H4L | 6590 | 33.28 | 25.0 | 0.1 |
| ligand_6045 | N-(2-Hydroxy-3,5-dimethylbenzyl)-N'-(3-hydroxy-1,2,5-trimethyl-4-pyridiumylmeth... | H4L | 7621 | 33.0 | 25.0 | 0.1 |
| ligand_6047 | N,N''-Bis(3-hydroxy-6-methyl-2-pyridinylmethyl)diethylenetrinitrilotriacetic ac... | H5L | 7648 | 32.7 | 25.0 | 0.1 |
| ligand_9912 | Desferriferrioxamin E (Nocardamin) | H3L | 69783 | 32.49 | 20.0 | 0.1 |
| ligand_6276 | N-(2-Hydroxybenzyl)ethylenedinitrilotriacetic acid (HBET) | H4L | 13324 | 32.02 | 25.0 | 0.1 |
| ligand_7673 | 3,7,11,15-Tetraaza-5,13(2)-dihydroxy-5,13(5)-dimethyl-1,9(2,6)-dipyridina-5,13(... | H2L | 36432 | 32.0 | 25.0 | 0.1 |
| ligand_5994 | N,N'-Bis(2-hydroxyphenyl)ethylenediiminodiacetic acid (HPED) | H4L | 6542 | 31.8 | 25.0 | 0.1 |
| ligand_8453 | Ethylenebis[imino(2-hydroxyphenyl)methylene(methyl)phosphinic acid] | H4L | 46963 | 31.25 | 25.0 | 0.1 |
| ligand_6044 | N-(2-Hydroxybenzyl)-N'-(3-hydroxy-5-hydroxymethyl-2-methyl-4-pyridylmethyl)ethy... | H4L | 7607 | 31.0 | 25.0 | 0.1 |
| ligand_8442 | Ethylenebis(imino(2-hydroxyphenyl)methylenephosphonous acid) | H4L | 46889 | 31.0 | 25.0 | 0.1 |
| ligand_6042 | N,N'-Bis(3-hydroxy-5-hydroxymethyl-2-methyl-4-pyridylmethyl)ethylenedinitrilodi... | H4L | 7580 | 30.8 | 25.0 | 0.1 |
| ligand_9911 | N-Acetyldesferriferrioxamin B | H3L | 69769 | 30.76 | 20.0 | 0.1 |
| ligand_6039 | N,N"-Bis(2-hydroxybenzyl)diethylenetrinitrilo-N,N',N"-triacetic acid (HBDT) | *** | 7492 | 30.44 | 25.0 | 0.1 |
| ligand_6054 | N,N'-Bis(carboxymethyl)ethylenedinitrilobis(N-2-propylacetohydroxamic acid) | H4L | 7776 | 30.2 | 25.0 | 0.1 |
| ligand_9916 | Desferricoprogen | H3L | 69825 | 30.2 | 25.0 | 0.1 |

... 25 more row(s) omitted

---

### Step 21: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT c.ligand_id, c.ligand_name_SRD, c.ligand_HxL_definition_SRD, c.card_id, s.constant_value, s.temperature_c, s.ionic_strength_mol_l FROM ligandmetal_card AS c JOIN ligandmetal_stability_measured AS s ON c.card_id = s.card_id WHERE c.metal_id = 62 AND c.beta_definition_id = 812 AND s.constant_type = 'K' ORDER BY s.constant_value DESC LIMIT 50"
}
```

[summary]
## execute_srd46_sql - 50 row(s)

| ligand_id | ligand_name_SRD | ligand_HxL_definition_SRD | card_id | constant_value | temperature_c | ionic_strength_mol_l |
|-----------|-----------------|---------------------------|---------|----------------|---------------|----------------------|
| ligand_6102 | 1,4,7,10-Tetraazacyclododecane-N,N',N'',N'''-tetraacetic acid (DOTA) | H4L | 8814 | 19.8 | 25.0 | 0.1 |
| ligand_6301 | trans-1,2-Cyclohexylenedinitrilotetraacetic acid (CDTA) | H4L | 14842 | 18.9 | 25.0 | 0.1 |
| ligand_6104 | 1,4,7,10-Tetraazacyclotridecane-N,N',N'',N'''-tetraacetic acid (TRITA) | H4L | 8894 | 17.6 | 25.0 | 0.1 |
| ligand_6287 | rac-(1,2-Dimethylethylene)dinitrilotetraacetic acid | H4L | 14258 | 17.18 | 20.0 | 0.1 |
| ligand_6287 | rac-(1,2-Dimethylethylene)dinitrilotetraacetic acid | H4L | 14257 | 17.08 | 25.0 | 0.1 |
| ligand_6084 | 1-Oxa-4,7,10-triazacyclododecane-4,7,10-triacetic acid | H3L | 8370 | 16.55 | 25.0 | 0.1 |
| ligand_6356 | Diethylenetrinitrilopentaacetic acid (DTPA) | H5L | 17634 | 16.2 | 25.0 | 0.1 |
| ligand_6366 | Triethylenetetranitrilohexaacetic acid (TTHA) | H6L | 18079 | 15.8 | 25.0 | 0.1 |
| ligand_6278 | DL-(Methylethylene)dinitrilotetraacetic acid (PDTA) | H4L | 13978 | 15.5 | 25.0 | 0.1 |
| ligand_6288 | meso-(1,2-Dimethylethylene)dinitrilotetraacetic acid | H4L | 14312 | 15.33 | 25.0 | 0.1 |
| ligand_7673 | 3,7,11,15-Tetraaza-5,13(2)-dihydroxy-5,13(5)-dimethyl-1,9(2,6)-dipyridina-5,13(... | H2L | 36425 | 15.3 | 25.0 | 0.1 |
| ligand_7661 | 5-(2-Hydroxyphenyl)-1,4,8,11-tetraazacyclotetradecane | HL | 36336 | 14.8 | 25.0 | 0.1 |
| ligand_7500 | 1,4,7,10,13-Pentaazacyclohexadecane ([16]aneN5) | L | 33967 | 14.57 | 35.0 | 0.1 |
| ligand_6082 | 1-Oxa-4,7,10-triazacyclododecane-4,10-diacetic acid | H2L | 8313 | 14.46 | 25.0 | 0.1 |
| ligand_8209 | Ethylenedinitrilotetrakis(methylene-2-pyridine) (N,N,N',N'-Tetra-2-picolylethyl... | L | 43094 | 14.38 | 25.0 | 0.1 |
| ligand_6277 | Ethylenedinitrilotetraacetic acid (EDTA) | H4L | 13677 | 14.3 | 25.0 | 0.1 |
| ligand_6335 | Oxybis(ethylenenitrilo)tetraacetic acid (EEDTA) | H4L | 16746 | 14.2 | 25.0 | 0.1 |
| ligand_6292 | DL-Ethylenedinitrilo-N,N'-di(2-propanoic)-N,N'-diacetic acid | H4L | 14440 | 14.18 | 20.0 | 0.1 |
| ligand_6371 | 1,4-Bis[2,5,5-tris(carboxymethyl)-2,5-diazapentyl]benzene (PXED3A) | H6L | 18305 | 13.54 | 25.0 | 0.1 |
| ligand_8412 | Nitrilotris(methylenephosphonic acid) (NTP) | H6L | 46270 | 13.5 | 25.0 | 0.1 |
| ligand_6311 | Trimethylenedinitrilotetraacetic acid (TMDTA) | H4L | 15576 | 13.42 | 20.0 | 0.1 |
| ligand_6109 | 1,4,8,11-Tetraazacyclotetradecane-N,N',N'',N'''-tetraacetic acid (TETA) | H4L | 8992 | 13.32 | 25.0 | 0.1 |
| ligand_6313 | Tetramethylenedinitrilotetraacetic acid | H4L | 15782 | 13.16 | 20.0 | 0.1 |
| ligand_6070 | 1,4,10-Trioxa-7,13-diazacyclopentadecane-N,N'-diacetic acid | H2L | 8064 | 13.0 | 25.0 | 0.1 |
| ligand_8427 | N-(2-Hydroxyethyl)ethylenedinitrilotris(methylenephosphonic acid) | H6L | 46522 | 12.8 | 25.0 | 0.1 |

... 25 more row(s) omitted

---

### Step 22: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT fe3.ligand_id, fe3.ligand_name_SRD, fe3.constant_value AS logK_Fe3, fe2.constant_value AS logK_Fe2, (fe3.constant_value - fe2.constant_value) AS delta_logK, fe3.temperature_c AS T_Fe3, fe2.temperature_c AS T_Fe2, fe3.ionic_strength_mol_l AS I_Fe3, fe2.ionic_strength_mol_l AS I_Fe2, fe3.card_id AS card_Fe3, fe2.card_id AS card_Fe2 FROM (SELECT c.ligand_id, c.ligand_name_SRD, s.constant_value, s.temperature_c, s.ionic_strength_mol_l, c.card_id FROM ligandmetal_card AS c JOIN ligandmetal_stability_measured AS s ON c.card_id = s.card_id WHERE c.metal_id = 61 AND c.beta_definition_id = 812 AND s.constant_type = 'K') AS fe3 JOIN (SELECT c.ligand_id, c.ligand_name_SRD, s.constant_value, s.temperature_c, s.ionic_strength_mol_l, c.card_id FROM ligandmetal_card AS c JOIN ligandmetal_stability_measured AS s ON c.card_id = s.card_id WHERE c.metal_id = 62 AND c.beta_definition_id = 812 AND s.constant_type = 'K') AS fe2 ON fe3.ligand_id = fe2.ligand_id WHERE fe3.temperature_c = fe2.temperature_c AND fe3.ionic_strength_mol_l = fe2.ionic_strength_mol_l ORDER BY delta_logK DESC LIMIT 80"
}
```

[summary]
## execute_srd46_sql - 50 row(s)

| ligand_id | ligand_name_SRD | logK_Fe3 | logK_Fe2 | delta_logK | T_Fe3 | T_Fe2 | I_Fe3 |
|-----------|-----------------|----------|----------|------------|-------|-------|-------|
| ligand_7673 | 3,7,11,15-Tetraaza-5,13(2)-dihydroxy-5,13(5)-dimethyl-1,9(2,6)-dipyridina-5,13(... | 32.0 | 15.3 | 16.7 | 25.0 | 25.0 | 0.1 |
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) | 11.27 | -4.8 | 16.07 | 25.0 | 25.0 | 0.1 |
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) | 11.19 | -4.8 | 15.989999999999998 | 25.0 | 25.0 | 0.1 |
| ligand_6109 | 1,4,8,11-Tetraazacyclotetradecane-N,N',N'',N'''-tetraacetic acid (TETA) | 26.46 | 13.32 | 13.14 | 25.0 | 25.0 | 0.1 |
| ligand_5843 | L-2-Aminobutanedioic acid 4-amide (Asparagine) | 8.6 | -3.4 | 12.0 | 20.0 | 20.0 | 1.0 |
| ligand_6356 | Diethylenetrinitrilopentaacetic acid (DTPA) | 28.0 | 16.2 | 11.8 | 25.0 | 25.0 | 0.1 |
| ligand_6292 | DL-Ethylenedinitrilo-N,N'-di(2-propanoic)-N,N'-diacetic acid | 25.28 | 14.18 | 11.100000000000001 | 20.0 | 20.0 | 0.1 |
| ligand_6301 | trans-1,2-Cyclohexylenedinitrilotetraacetic acid (CDTA) | 30.0 | 18.9 | 11.100000000000001 | 25.0 | 25.0 | 0.1 |
| ligand_6366 | Triethylenetetranitrilohexaacetic acid (TTHA) | 26.8 | 15.8 | 11.0 | 25.0 | 25.0 | 0.1 |
| ligand_6287 | rac-(1,2-Dimethylethylene)dinitrilotetraacetic acid | 28.05 | 17.08 | 10.970000000000002 | 25.0 | 25.0 | 0.1 |
| ligand_6277 | Ethylenedinitrilotetraacetic acid (EDTA) | 25.1 | 14.3 | 10.8 | 25.0 | 25.0 | 0.1 |
| ligand_8434 | Pyridine-2,6-diphosphonic acid (2,6-PDPA) | 20.87 | 10.12 | 10.750000000000002 | 25.0 | 25.0 | 0.1 |
| ligand_6278 | DL-(Methylethylene)dinitrilotetraacetic acid (PDTA) | 26.0 | 15.5 | 10.5 | 25.0 | 25.0 | 0.1 |
| ligand_6288 | meso-(1,2-Dimethylethylene)dinitrilotetraacetic acid | 25.65 | 15.33 | 10.319999999999999 | 25.0 | 25.0 | 0.1 |
| ligand_6084 | 1-Oxa-4,7,10-triazacyclododecane-4,7,10-triacetic acid | 26.8 | 16.55 | 10.25 | 25.0 | 25.0 | 0.1 |
| ligand_6104 | 1,4,7,10-Tetraazacyclotridecane-N,N',N'',N'''-tetraacetic acid (TRITA) | 27.5 | 17.6 | 9.899999999999999 | 25.0 | 25.0 | 0.1 |
| ligand_8360 | Amino(phenyl)methylenediphosphonic acid | 20.15 | 10.4 | 9.749999999999998 | 25.0 | 25.0 | 0.1 |
| ligand_6102 | 1,4,7,10-Tetraazacyclododecane-N,N',N'',N'''-tetraacetic acid (DOTA) | 29.4 | 19.8 | 9.599999999999998 | 25.0 | 25.0 | 0.1 |
| ligand_5937 | N-(Phosphonomethyl)glycine (Glyphosate) | 16.09 | 6.87 | 9.219999999999999 | 25.0 | 25.0 | 0.1 |
| ligand_6348 | Thiobis(ethylenenitrilo)tetraacetic acid (TEDTA) | 20.41 | 11.57 | 8.84 | 20.0 | 20.0 | 0.1 |
| ligand_6342 | Ethylenebis(oxyethylenenitrilo)tetraacetic acid (EGTA) | 20.5 | 11.8 | 8.7 | 25.0 | 25.0 | 0.1 |
| ligand_5804 | L-2-Aminopentanedioic acid (Glutamic acid) | 12.1 | 3.52 | 8.58 | 20.0 | 20.0 | 1.0 |
| ligand_6310 | Ethylenedinitrilotetra(3-propanoic acid) (EDTP) | 14.4 | 6.2 | 8.2 | 30.0 | 30.0 | 0.1 |
| ligand_6333 | (2-Hydroxytrimethylene)dinitrilotetraacetic acid | 20.1 | 11.91 | 8.190000000000001 | 20.0 | 20.0 | 0.1 |
| ligand_6311 | Trimethylenedinitrilotetraacetic acid (TMDTA) | 21.61 | 13.42 | 8.19 | 20.0 | 20.0 | 0.1 |

... 25 more row(s) omitted

---

### Step 23: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT fe3.ligand_id, fe3.ligand_name_SRD, fe3.constant_value AS logK_Fe3, fe2.constant_value AS logK_Fe2, (fe3.constant_value - fe2.constant_value) AS delta_logK, fe3.temperature_c AS T_Fe3, fe2.temperature_c AS T_Fe2, fe3.ionic_strength_mol_l AS I_Fe3, fe2.ionic_strength_mol_l AS I_Fe2, fe3.card_id AS card_Fe3, fe2.card_id AS card_Fe2 FROM (SELECT c.ligand_id, c.ligand_name_SRD, s.constant_value, s.temperature_c, s.ionic_strength_mol_l, c.card_id FROM ligandmetal_card AS c JOIN ligandmetal_stability_measured AS s ON c.card_id = s.card_id WHERE c.metal_id = 61 AND c.beta_definition_id = 812 AND s.constant_type = 'K') AS fe3 JOIN (SELECT c.ligand_id, c.ligand_name_SRD, s.constant_value, s.temperature_c, s.ionic_strength_mol_l, c.card_id FROM ligandmetal_card AS c JOIN ligandmetal_stability_measured AS s ON c.card_id = s.card_id WHERE c.metal_id = 62 AND c.beta_definition_id = 812 AND s.constant_type = 'K') AS fe2 ON fe3.ligand_id = fe2.ligand_id WHERE fe3.temperature_c = fe2.temperature_c AND fe3.ionic_strength_mol_l = fe2.ionic_strength_mol_l ORDER BY delta_logK DESC LIMIT 80 OFFSET 50"
}
```

[summary]
## execute_srd46_sql - 26 row(s)

| ligand_id | ligand_name_SRD | logK_Fe3 | logK_Fe2 | delta_logK | T_Fe3 | T_Fe2 | I_Fe3 |
|-----------|-----------------|----------|----------|------------|-------|-------|-------|
| ligand_5907 | L-2-Amino-3-(3-indolyl)propanoic acid (Tryptophan) | 9.0 | 3.43 | 5.57 | 20.0 | 20.0 | 1.0 |
| ligand_8873 | Propanedioic acid (Malonic acid) | 7.5 | 2.17 | 5.33 | 25.0 | 25.0 | 1.0 |
| ligand_5829 | L-2-Amino-3-hydroxybutanoic acid (Threonine) | 8.6 | 3.3 | 5.3 | 20.0 | 20.0 | 1.0 |
| ligand_8873 | Propanedioic acid (Malonic acid) | 7.5 | 2.24 | 5.26 | 25.0 | 25.0 | 1.0 |
| ligand_6774 | Pyridine-2,6-dicarboxylic acid (Dipicolinic acid) | 10.91 | 5.71 | 5.2 | 20.0 | 20.0 | 0.1 |
| ligand_6127 | Iminodiacetic acid (IDA) | 10.72 | 5.54 | 5.180000000000001 | 25.0 | 25.0 | 0.5 |
| ligand_5941 | L-4-Hydroxypyrrolidine-2-carboxylic acid (L-Hydroxyproline) | 9.0 | 3.94 | 5.0600000000000005 | 20.0 | 20.0 | 1.0 |
| ligand_6204 | N-(2-Hydroxyethyl)iminodiacetic acid (HIDA) | 11.61 | 6.78 | 4.829999999999999 | 20.0 | 20.0 | 0.1 |
| ligand_8872 | Ethanedioic acid (Oxalic acid) | 7.58 | 3.05 | 4.53 | 25.0 | 25.0 | 1.0 |
| ligand_8953 | L-Hydroxybutanedioic acid (Hydroxysuccinic acid)(Malic acid) | 7.1 | 2.6 | 4.5 | 20.0 | 20.0 | 0.1 |
| ligand_10162 | Hydrogen fluoride (Hydrofluoric acid) | 5.15 | 0.8 | 4.3500000000000005 | 25.0 | 25.0 | 1.0 |
| ligand_8955 | D-2,3-Dihydroxybutanedioic acid (D-Tartaric acid) | 6.49 | 2.24 | 4.25 | 20.0 | 20.0 | 0.1 |
| ligand_8668 | D-gluco-Pentahydroxyhexanoic acid (D-Gluconic acid) | 3.1 | -1.0 | 4.1 | 25.0 | 25.0 | 1.0 |
| ligand_8465 | Ethanoic acid (Acetic acid) | 3.23 | -0.54 | 3.77 | 25.0 | 25.0 | 3.0 |
| ligand_6760 | 1,4-Diazine-2-carboxylic acid (Pyrazinecarboxylic acid) | 7.5 | 4.1 | 3.4000000000000004 | 25.0 | 25.0 | 1.0 |
| ligand_10092 | Hydrogen thiocyanate (Thiocyanic acid) | 3.03 | 1.31 | 1.7199999999999998 | 25.0 | 25.0 | 0.0 |
| ligand_10163 | Chloride ion | 1.48 | -0.2 | 1.68 | 25.0 | 25.0 | 0.0 |
| ligand_8640 | Hydroxyacetic acid (Glycolic acid) | 2.9 | 1.33 | 1.5699999999999998 | 25.0 | 25.0 | 1.0 |
| ligand_10092 | Hydrogen thiocyanate (Thiocyanic acid) | 2.29 | 0.81 | 1.48 | 25.0 | 25.0 | 3.0 |
| ligand_10092 | Hydrogen thiocyanate (Thiocyanic acid) | 2.19 | 0.81 | 1.38 | 25.0 | 25.0 | 3.0 |
| ligand_10092 | Hydrogen thiocyanate (Thiocyanic acid) | 2.08 | 0.81 | 1.27 | 25.0 | 25.0 | 3.0 |
| ligand_6288 | meso-(1,2-Dimethylethylene)dinitrilotetraacetic acid | -25.42 | -15.11 | -10.310000000000002 | 20.0 | 20.0 | 0.1 |
| ligand_5777 | L-2-Amino-3-phenylpropanoic acid (Phenylalanine) | -8.9 | 3.26 | -12.16 | 20.0 | 20.0 | 1.0 |
| ligand_5760 | Aminoacetic acid (Glycine) | -9.25 | 4.2 | -13.45 | 25.0 | 25.0 | 3.0 |
| ligand_5777 | L-2-Amino-3-phenylpropanoic acid (Phenylalanine) | -10.39 | 3.74 | -14.13 | 25.0 | 25.0 | 3.0 |

... 1 more row(s) omitted

---

### Step 24: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_7673"
}
```

[summary]
## inspect_card — Ligand | ligand_7673

**Name:** 3,7,11,15-Tetraaza-5,13(2)-dihydroxy-5,13(5)-dimethyl-1,9(2,6)-dipyridina-5,13(1,3)-dibenzenacyclohexadecaphane ([24]RBPyBC)  
**Formula:** C32H38N6 | **Class:** Aza-macrocycles  
**SMILES:** `Cc1cc2c(O)c(c1)CNCc1cccc(n1)CNCc1cc(C)cc(c1O)CNCc1cccc(n1)CNC2`  
**InChI:** `InChI=1S/C32H38N6O2/c1-21-9-23-13-33-17-27-5-3-7-29(37-27)19-35-15-25-11-22(2)12-26(32(25)40)16-36-20-30-8-4-6-28(38-30)18-34-14-24(10-21)31(23)39/h3-12,33-36,39-40H,13-20H2,1-2H3`  
**HxL definition:** H2L  

**pKa values:** 6

| source_vlm | pKa | T (°C) | I (M) | From → To | Solvent | Method | Quality |
|------------|-----|--------|-------|-----------|---------|--------|---------|
| vlm_132575 | -12.10 | 25.0 | 0.1 | L → HL | *** | *** | *** |
| vlm_132576 | -11.30 | 25.0 | 0.1 | HL → H2L | *** | *** | *** |
| vlm_132580 | 4.52 | 25.0 | 0.1 | H5L → H6L | *** | *** | *** |
| vlm_132579 | 6.65 | 25.0 | 0.1 | H4L → H5L | *** | *** | *** |
| vlm_132578 | 8.92 | 25.0 | 0.1 | H3L → H4L | *** | *** | *** |
| vlm_132577 | 9.18 | 25.0 | 0.1 | H2L → H3L | *** | *** | *** |

**Partners:** 3 metal(s), 22 measurement(s) total

| metal_id | Metal | # meas |
|----------|-------|--------|
| metal_61 | Fe^[3+] | 9 |
| metal_62 | Fe^[2+] | 7 |
| metal_68 | H^[+] | 6 |

---

### Step 25: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_9058"
}
```

[summary]
## inspect_card — Ligand | ligand_9058

**Name:** 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid)  
**Formula:** C6H8O7 | **Class:** Carboxylic acids polyacids  
**SMILES:** `O=C(O)CC(O)(CC(=O)O)C(=O)O`  
**InChI:** `InChI=1S/C6H8O7/c7-3(8)1-6(13,5(11)12)2-4(9)10/h13H,1-2H2,(H,7,8)(H,9,10)(H,11,12)`  
**HxL definition:** H3L  

**pKa values:** 3

| source_vlm | pKa | T (°C) | I (M) | From → To | Solvent | Method | Quality |
|------------|-----|--------|-------|-----------|---------|--------|---------|
| vlm_157473 | 2.90 | 25.0 | 0.1 | H2L → H3L | *** | *** | *** |
| vlm_157459 | 4.35 | 25.0 | 0.1 | HL → H2L | *** | *** | *** |
| vlm_157439 | 5.65 | 25.0 | 0.1 | L → HL | *** | *** | *** |

**Partners:** 57 metal(s), 384 measurement(s) total

| metal_id | Metal | # meas |
|----------|-------|--------|
| metal_68 | H^[+] | 48 |
| metal_112 | Ni^[2+] | 25 |
| metal_204 | W^[6+] | 24 |
| metal_26 | Cd^[2+] | 22 |
| metal_208 | Zn^[2+] | 19 |
| … | *(showing top 5 of 57)* | |

---

### Step 26: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT c.card_id, c.ligand_HxL_definition_SRD, c.beta_definition_name, s.constant_value, s.temperature_c, s.ionic_strength_mol_l, s.normalized_definition FROM ligandmetal_card AS c JOIN ligandmetal_stability_measured AS s ON c.card_id = s.card_id WHERE c.metal_id = 62 AND c.ligand_id = 9058 AND c.beta_definition_id = 812 AND s.constant_type = 'K'"
}
```

[summary]
## execute_srd46_sql - 4 row(s)

| card_id | ligand_HxL_definition_SRD | beta_definition_name | constant_value | temperature_c | ionic_strength_mol_l | normalized_definition |
|---------|---------------------------|----------------------|----------------|---------------|----------------------|-----------------------|
| 59694 | H3L | [ML]/[M][L] | 4.4 | 20.0 | 0.1 | [ML]/[M][L] |
| 59695 | H3L | [ML]/[M][L] | -4.8 | 25.0 | 0.1 | [ML]/[M][L] |
| 59696 | H3L | [ML]/[M][L] | 4.56 | 37.0 | 0.15 | [ML]/[M][L] |
| 59697 | H3L | [ML]/[M][L] | 4.7 | 37.0 | 0.15 | [ML]/[M][L] |

---

### Step 27: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT c.card_id, c.ligand_HxL_definition_SRD, c.beta_definition_name, s.constant_value, s.temperature_c, s.ionic_strength_mol_l FROM ligandmetal_card AS c JOIN ligandmetal_stability_measured AS s ON c.card_id = s.card_id WHERE c.metal_id = 61 AND c.ligand_id = 9058 AND c.beta_definition_id = 812 AND s.constant_type = 'K'"
}
```

[summary]
## execute_srd46_sql - 3 row(s)

| card_id | ligand_HxL_definition_SRD | beta_definition_name | constant_value | temperature_c | ionic_strength_mol_l |
|---------|---------------------------|----------------------|----------------|---------------|----------------------|
| 59757 | H3L | [ML]/[M][L] | 11.19 | 25.0 | 0.1 |
| 59758 | H3L | [ML]/[M][L] | 11.27 | 25.0 | 0.1 |
| 59759 | H3L | [ML]/[M][L] | 10.25 | 25.0 | 1.0 |

---

### Step 28: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT c.card_id, c.ligand_id, c.ligand_name_SRD, c.ligand_HxL_definition_SRD, c.beta_definition_name, s.constant_value, s.temperature_c, s.ionic_strength_mol_l FROM ligandmetal_card AS c JOIN ligandmetal_stability_measured AS s ON c.card_id = s.card_id WHERE c.metal_id = 61 AND c.ligand_id IN (5760, 5777, 5843) AND c.beta_definition_id = 812 AND s.constant_type = 'K'"
}
```

[summary]
## execute_srd46_sql - 5 row(s)

| card_id | ligand_id | ligand_name_SRD | ligand_HxL_definition_SRD | beta_definition_name | constant_value | temperature_c | ionic_strength_mol_l |
|---------|-----------|-----------------|---------------------------|----------------------|----------------|---------------|----------------------|
| 275 | ligand_5760 | Aminoacetic acid (Glycine) | HL | [ML]/[M][L] | -8.57 | 25.0 | 0.5 |
| 276 | ligand_5760 | Aminoacetic acid (Glycine) | HL | [ML]/[M][L] | -9.25 | 25.0 | 3.0 |
| 1275 | ligand_5777 | L-2-Amino-3-phenylpropanoic acid (Phenylalanine) | HL | [ML]/[M][L] | -8.9 | 20.0 | 1.0 |
| 1276 | ligand_5777 | L-2-Amino-3-phenylpropanoic acid (Phenylalanine) | HL | [ML]/[M][L] | -10.39 | 25.0 | 3.0 |
| 3034 | ligand_5843 | L-2-Aminobutanedioic acid 4-amide (Asparagine) | HL | [ML]/[M][L] | 8.6 | 20.0 | 1.0 |

---
