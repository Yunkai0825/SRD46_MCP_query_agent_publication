# Q5.2.3 — Tool Results (batch 5)

### Step 3: `get_table_schema`
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

### Step 4: `get_table_schema`
**Args:**
```json
{
  "table_name": "ligandmetal_card"
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

### Step 5: `search_stability`
**Args:**
```json
{
  "where": "(s.temperature_c BETWEEN 195 AND 205)",
  "order_by": "s.temperature_c ASC",
  "limit": 300
}
```

[summary]
## search_stability

*(no results)*

---

### Step 6: `search_stability`
**Args:**
```json
{
  "where": "(s.temperature_c BETWEEN 150 AND 250)",
  "order_by": "s.temperature_c ASC",
  "limit": 500
}
```

[summary]
## search_stability

*(no results)*

---

### Step 7: `search_stability`
**Args:**
```json
{
  "where": "(s.temperature_c IS NOT NULL)",
  "order_by": "s.temperature_c DESC",
  "limit": 50
}
```

[summary]
## search_stability — 50 row(s)

### logK — 11 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_8318 | Adenosine-5'-(trihydrogendi… | H3L | Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]1O | 3 | 3 | 75 | 0 | *** | 1 |
| metal_92 | Mg^[2+] | ligand_8318 | Adenosine-5'-(trihydrogendi… | H3L | Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]1O | 3 | 3 | 75 | 0 | *** | 1 |
| metal_68 | H^[+] | ligand_9500 | 1-(2-Hydroxy-5-sulfophenyla… | H3L | O=S(=O)(O)c1ccc(O)c(/N=N/c2c(O)ccc3ccccc23)c1 | 2 | 2 | 75 | 0 | *** | 1 |
| metal_29 | Cf^[3+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 2 | 2 | 55 | 2 | *** | 1 |
| metal_68 | H^[+] | ligand_8312 | Adenosine-5'-(dihydrogenpho… | H2L | Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)O)[C@@H](O)[C@H]1O | 2 | 2 | 50 | 0 | *** | 1 |
| metal_68 | H^[+] | ligand_8321 | Adenosine-5'-(tetrahydrogen… | H4L | Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)OP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]1O | 2 | 2 | 50 | 0 | *** | 1 |
| metal_37 | Cr^[3+] | ligand_9500 | 1-(2-Hydroxy-5-sulfophenyla… | H3L | O=S(=O)(O)c1ccc(O)c(/N=N/c2c(O)ccc3ccccc23)c1 | 1 | 1 | 75 | 0 | *** | 1 |
| metal_68 | H^[+] | ligand_7145 | 2,2'-Iminodiethanol (Dietha… | L | OCCNCCO | 1 | 1 | 50 | 0 | *** | 1 |
| metal_68 | H^[+] | ligand_7276 | N-Methyliminodi-2-ethanol (… | L | CN(CCO)CCO | 1 | 1 | 50 | 0 | *** | 1 |
| metal_68 | H^[+] | ligand_7289 | 2-[Bis(2-hydroxyethyl)amino… | L | OCCN(CCO)C(CO)(CO)CO | 1 | 1 | 50 | 0 | *** | 1 |
| metal_5 | Al^[3+] | ligand_7289 | 2-[Bis(2-hydroxyethyl)amino… | L | OCCN(CCO)C(CO)(CO)CO | 1 | 1 | 50 | 0.1 | *** | 1 |

### ΔH — 14 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_8318 | Adenosine-5'-(trihydrogendi… | H3L | Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]1O | 3 | 3 | 75 | 0 | *** | 0 |
| metal_92 | Mg^[2+] | ligand_8318 | Adenosine-5'-(trihydrogendi… | H3L | Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]1O | 3 | 3 | 75 | 0 | *** | 0 |
| metal_68 | H^[+] | ligand_8312 | Adenosine-5'-(dihydrogenpho… | H2L | Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)O)[C@@H](O)[C@H]1O | 2 | 2 | 50 | 0 | *** | 0 |
| metal_68 | H^[+] | ligand_8321 | Adenosine-5'-(tetrahydrogen… | H4L | Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)OP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]1O | 2 | 2 | 50 | 0 | *** | 0 |
| metal_68 | H^[+] | ligand_6797 | Methylamine | L | CN | 1 | 1 | 50 | 0 | *** | 0 |
| metal_68 | H^[+] | ligand_6802 | Hexylamine | L | CCCCCCN | 1 | 1 | 50 | 0 | *** | 0 |
| metal_68 | H^[+] | ligand_6811 | Cyclohexylamine | L | NC1CCCCC1 | 1 | 1 | 50 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_7109 | Dimethylamine | L | CNC | 1 | 1 | 50 | 0 | *** | 0 |
| metal_68 | H^[+] | ligand_7112 | N-Methylpentylamine | L | CCCCCNC | 1 | 1 | 50 | 0 | *** | 0 |
| metal_68 | H^[+] | ligand_7114 | Dipropylamine | L | CCCNCCC | 1 | 1 | 50 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_7145 | 2,2'-Iminodiethanol (Dietha… | L | OCCNCCO | 1 | 1 | 50 | 0 | *** | 0 |
| metal_68 | H^[+] | ligand_7255 | Trimethylamine | L | CN(C)C | 1 | 1 | 50 | 0 | *** | 0 |
| metal_68 | H^[+] | ligand_7260 | Triethylamine | L | CCN(CC)CC | 1 | 1 | 50 | 0 | *** | 0 |
| metal_68 | H^[+] | ligand_7276 | N-Methyliminodi-2-ethanol (… | L | CN(CCO)CCO | 1 | 1 | 50 | 0 | *** | 0 |

### ΔS — 6 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_8318 | Adenosine-5'-(trihydrogendi… | H3L | Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]1O | 3 | 3 | 75 | 0 | *** | 0 |
| metal_92 | Mg^[2+] | ligand_8318 | Adenosine-5'-(trihydrogendi… | H3L | Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]1O | 3 | 3 | 75 | 0 | *** | 0 |
| metal_68 | H^[+] | ligand_8312 | Adenosine-5'-(dihydrogenpho… | H2L | Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)O)[C@@H](O)[C@H]1O | 2 | 2 | 50 | 0 | *** | 0 |
| metal_68 | H^[+] | ligand_7145 | 2,2'-Iminodiethanol (Dietha… | L | OCCNCCO | 1 | 1 | 50 | 0 | *** | 0 |
| metal_68 | H^[+] | ligand_7276 | N-Methyliminodi-2-ethanol (… | L | CN(CCO)CCO | 1 | 1 | 50 | 0 | *** | 0 |
| metal_68 | H^[+] | ligand_8321 | Adenosine-5'-(tetrahydrogen… | H4L | Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)OP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]1O | 1 | 1 | 50 | 0 | *** | 0 |

---

### Step 8: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT\n  MAX(temperature_c) AS max_temperature_c,\n  SUM(CASE WHEN temperature_c BETWEEN 195 AND 205 THEN 1 ELSE 0 END) AS hits_195_205,\n  SUM(CASE WHEN temperature_c BETWEEN 150 AND 250 THEN 1 ELSE 0 END) AS hits_150_250,\n  COUNT(*) AS total_with_T\nFROM ligandmetal_stability_measured\nWHERE temperature_c IS NOT NULL;"
}
```

[summary]
## execute_srd46_sql - 1 row(s)

| max_temperature_c | hits_195_205 | hits_150_250 | total_with_T |
|-------------------|--------------|--------------|--------------|
| 75.0 | 0 | 0 | 79063 |

---
