# Q5.1.4 — Tool Results (batch 2)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "zinc",
  "symbol": "Zn",
  "limit": 10
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_208 | Zn^[2+] | Zn | 2 | ✓ | [Zn+2] | InChI=1S/Zn/q+2 | beta_totN_122 | ligand_totN_1169 | vlm_totN_4095 |

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

### Step 6: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT c.ligand_id, c.ligand_name_SRD, COUNT(s.stability_id) AS n_measurements\nFROM ligandmetal_card c\nJOIN ligandmetal_stability_measured s ON s.card_id = c.card_id\nWHERE c.metal_id = 208\nGROUP BY c.ligand_id, c.ligand_name_SRD\nORDER BY n_measurements DESC\nLIMIT 15;"
}
```

[summary]
## execute_srd46_sql - 15 row(s)

| ligand_id | ligand_name_SRD | n_measurements |
|-----------|-----------------|----------------|
| ligand_5760 | Aminoacetic acid (Glycine) | 37 |
| ligand_7029 | Ethylenediamine | 36 |
| ligand_10076 | Hydroxide ion | 33 |
| ligand_7795 | 1,3-Diazole (Imidazole) | 30 |
| ligand_10090 | Hydrogen cyanide (Hydrocyanic acid) | 30 |
| ligand_5898 | L-2-Amino-3-(4-imidazolyl)propanoic acid (Histidine) | 29 |
| ligand_10092 | Hydrogen thiocyanate (Thiocyanic acid) | 24 |
| ligand_5856 | L-2-Amino-3-mercaptopropanoic acid (Cysteine) | 23 |
| ligand_8412 | Nitrilotris(methylenephosphonic acid) (NTP) | 21 |
| ligand_10103 | Ammonia | 21 |
| ligand_6127 | Iminodiacetic acid (IDA) | 20 |
| ligand_5761 | L-2-Aminopropanoic acid (Alanine) | 19 |
| ligand_8191 | 1,10-Phenanthroline (Dipyridino[a,c]benzene) | 19 |
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) | 19 |
| ligand_5857 | D-2-Amino-3-mercapto-3-methylbutanoic acid (Penicillamine) | 18 |

---

### Step 7: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT s.solvent_name, COUNT(*) AS n\nFROM ligandmetal_stability_measured s\nJOIN ligandmetal_card c ON c.card_id = s.card_id\nWHERE c.metal_id = 208\nGROUP BY s.solvent_name\nORDER BY n DESC\nLIMIT 10;"
}
```

[summary]
## execute_srd46_sql - 1 row(s)

| solvent_name | n |
|--------------|---|
| H_[2]O | 4095 |

---

### Step 8: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT s.ionic_strength_mol_l, COUNT(*) AS n\nFROM ligandmetal_stability_measured s\nJOIN ligandmetal_card c ON c.card_id = s.card_id\nWHERE c.metal_id = 208\nGROUP BY s.ionic_strength_mol_l\nORDER BY n DESC\nLIMIT 10;"
}
```

[summary]
## execute_srd46_sql - 10 row(s)

| ionic_strength_mol_l | n |
|----------------------|---|
| 0.1 | 2457 |
| 0.5 | 498 |
| 1.0 | 338 |
| 0.15 | 294 |
| 0.0 | 244 |
| 3.0 | 131 |
| 2.0 | 110 |
| 4.0 | 10 |
| 0.7 | 8 |
| 6.0 | 3 |

---

### Step 9: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT s.constant_type, COUNT(*) AS n\nFROM ligandmetal_stability_measured s\nJOIN ligandmetal_card c ON c.card_id = s.card_id\nWHERE c.metal_id = 208\nGROUP BY s.constant_type\nORDER BY n DESC;"
}
```

[summary]
## execute_srd46_sql - 3 row(s)

| constant_type | n |
|---------------|---|
| K | 3351 |
| H | 395 |
| S | 349 |

---

### Step 10: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT s.temperature_c, COUNT(*) AS n\nFROM ligandmetal_stability_measured s\nJOIN ligandmetal_card c ON c.card_id = s.card_id\nWHERE c.metal_id = 208\nGROUP BY s.temperature_c\nORDER BY n DESC\nLIMIT 10;"
}
```

[summary]
## execute_srd46_sql - 10 row(s)

| temperature_c | n |
|---------------|---|
| 25.0 | 3363 |
| 37.0 | 307 |
| 20.0 | 274 |
| 30.0 | 86 |
| 35.0 | 15 |
| 10.0 | 14 |
| 40.0 | 12 |
| 15.0 | 8 |
| 45.0 | 7 |
| 27.0 | 4 |

---

### Step 11: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND c.ligand_name_SRD LIKE '%EDTA%')",
  "order_by": "s.temperature_c ASC",
  "limit": 5
}
```

[summary]
## search_stability — 5 row(s)

### `Zn^[2+]` + Ethylenedinitrilotetraacetic acid (EDTA) — 1 measurement(s)
metal_id: metal_208 | ligand_id: ligand_6277
ligand_HxL_def: H4L | ligand_SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_108721 | *** | beta_def_966 | ΔH | 0 | 20 | 0.1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |

### `Zn^[2+]` + Oxybis(ethylenenitrilo)tetraacetic acid (EEDTA) — 3 measurement(s)
metal_id: metal_208 | ligand_id: ligand_6335
ligand_HxL_def: H4L | ligand_SMILES: O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_111807 | *** | beta_def_812 | ΔH | -25.1 | 20 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.39, L, +inf) |
| vlm_111809 | *** | beta_def_812 | ΔS | 207.5 | 20 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.39, L, +inf) |
| vlm_111810 | ref_eq_map_6373 | beta_def_788 | logK | 2.75 | 20 | 0.1 | `[ML] + [H] <=> [MHL]` | *** |  |  |

### `Zn^[2+]` + Thiobis(ethylenenitrilo)tetraacetic acid (TEDTA) — 1 measurement(s)
metal_id: metal_208 | ligand_id: ligand_6348
ligand_HxL_def: H4L | ligand_SMILES: O=C(O)CN(CCSCCN(CC(=O)O)CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_112303 | *** | beta_def_812 | ΔH | -15.5 | 20 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.31, L, +inf) |

---

### Step 12: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND c.ligand_name_SRD LIKE '%citrate%')",
  "order_by": "s.temperature_c ASC",
  "limit": 5
}
```

[summary]
## search_stability — 5 row(s)

### `H^[+]` + 2-Hydroxy-2-ethylbutanoic acid — 1 measurement(s)
metal_id: metal_68 | ligand_id: ligand_8653
ligand_HxL_def: HL | ligand_SMILES: CCC(O)(CC)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_148501 | ref_eq_map_18563 | beta_def_79 | logK | 3.8 | 18 | 0 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (-inf, HL, 3.62, L, +inf) |

### `H^[+]` + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) — 4 measurement(s)
metal_id: metal_68 | ligand_id: ligand_9058
ligand_HxL_def: H3L | ligand_SMILES: O=C(O)CC(O)(CC(=O)O)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_157449 | ref_eq_map_22012 | beta_def_79 | logK | 5.08 | 18 | 2 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (4.35, HL, 5.65, L, +inf) |
| vlm_157451 | ref_eq_map_22014 | beta_def_79 | logK | 5.12 | 18 | 3 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (4.35, HL, 5.65, L, +inf) |
| vlm_157463 | ref_eq_map_22012 | beta_def_32 | logK | 4.09 | 18 | 2 | `[HL] + [H] <=> [H2L]` | *** | [HL]; [H2L] | (2.9, H2L, 4.35, HL, 5.65) |
| vlm_157465 | ref_eq_map_22014 | beta_def_32 | logK | 4.18 | 18 | 3 | `[HL] + [H] <=> [H2L]` | *** | [HL]; [H2L] | (2.9, H2L, 4.35, HL, 5.65) |

---

### Step 13: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND c.ligand_name_SRD LIKE '%chloride%')",
  "order_by": "s.temperature_c ASC",
  "limit": 5
}
```

[summary]
## search_stability — 5 row(s)

### `Zn^[2+]` + Chloride ion — 5 measurement(s)
metal_id: metal_208 | ligand_id: ligand_10163
ligand_HxL_def: *** | ligand_SMILES: ***

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_177526 | ref_eq_map_29790 | beta_def_812 | logK | -0.4 | 25 | 0.7 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177527 | ref_eq_map_29786 | beta_def_812 | logK | -0.3 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177528 | ref_eq_map_29787 | beta_def_812 | logK | -0.3 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177529 | ref_eq_map_29788 | beta_def_812 | logK | -0.2 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177530 | ref_eq_map_29789 | beta_def_812 | logK | 0.1 | 25 | 4 | `[M] + [L] <=> [ML]` | *** | [L] |  |

---

### Step 14: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND c.ligand_name_SRD LIKE '%sulfate%')",
  "limit": 5
}
```

[summary]
## search_stability — 5 row(s)

### `Zn^[2+]` + Hydrogen sulfate ion (Sulfuric acid) — 5 measurement(s)
metal_id: metal_208 | ligand_id: ligand_10148
ligand_HxL_def: HL | ligand_SMILES: O=S(=O)([O-])O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_176126 | ref_eq_map_29222 | beta_def_812 | logK | 0.93 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (1.54, L, +inf) |
| vlm_176127 | ref_eq_map_29223 | beta_def_812 | logK | 0.89 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (1.54, L, +inf) |
| vlm_176128 | ref_eq_map_29224 | beta_def_812 | logK | 0.76 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (1.54, L, +inf) |
| vlm_176129 | ref_eq_map_29225 | beta_def_812 | logK | 0.7 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (1.54, L, +inf) |
| vlm_176130 | ref_eq_map_29221 | beta_def_812 | logK | 2.34 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (1.54, L, +inf) |

---

### Step 15: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND c.ligand_name_SRD LIKE '%carbonate%')",
  "limit": 5
}
```

[summary]
## search_stability — 5 row(s)

### `Zn^[2+]` + Hydrogen carbonate (Carbonic acid) — 5 measurement(s)
metal_id: metal_208 | ligand_id: ligand_10096
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_172900 | ref_eq_map_28026 | beta_def_812 | logK | 3.9 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.91, L, +inf) |
| vlm_172901 | ref_eq_map_28027 | beta_def_812 | logK | 3.3 | 25 | 0.7 | `[M] + [L] <=> [ML]` | *** | [L] | (9.91, L, +inf) |
| vlm_172902 | ref_eq_map_28029 | beta_def_812 | logK | 4.76 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.91, L, +inf) |
| vlm_172903 | ref_eq_map_28027 | beta_def_840 | logK | 5.3 | 25 | 0.7 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.91, L, +inf) |
| vlm_172904 | ref_eq_map_28028 | beta_def_840 | logK | 6.9 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.91, L, +inf) |

---

### Step 16: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND c.ligand_name_SRD LIKE '%hydrox%')",
  "limit": 5
}
```

[summary]
## search_stability — 5 row(s)

### `Zn^[2+]` + DL-2-Amino-3-hydroxypentanedioic acid (3-Hydroxyglutamic ac… — 2 measurement(s)
metal_id: metal_208 | ligand_id: ligand_5807
ligand_HxL_def: H2L | ligand_SMILES: N[C@H](C(=O)O)C(O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_95877 | ref_eq_map_656 | beta_def_812 | logK | 4.65 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.06, L, +inf) |
| vlm_95878 | ref_eq_map_656 | beta_def_840 | logK | -8.36 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.06, L, +inf) |

### `Zn^[2+]` + DL-2-Amino-3-(2-hydroxyphenyl)propanoic acid (o-Tyrosine) — 3 measurement(s)
metal_id: metal_208 | ligand_id: ligand_5817
ligand_HxL_def: H2L | ligand_SMILES: NC(Cc1ccccc1O)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_96126 | ref_eq_map_714 | beta_def_779 | logK | 4.21 | 25 | 0.1 | `[M] + [HL] <=> [MHL]` | *** | [HL] | (8.67, HL, 11.01) |
| vlm_96127 | *** | beta_def_779 | ΔH | -9.2 | 25 | 0.1 | `[M] + [HL] <=> [MHL]` | *** | [HL] | (8.67, HL, 11.01) |
| vlm_96128 | *** | beta_def_779 | ΔS | 49.8 | 25 | 0.1 | `[M] + [HL] <=> [MHL]` | *** | [HL] | (8.67, HL, 11.01) |

---

### Step 17: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND c.ligand_name_SRD LIKE '%histidine%')",
  "limit": 5
}
```

[summary]
## search_stability — 5 row(s)

### `Zn^[2+]` + DL-2-Amino-3-(2-mercaptoimidazo-4-yl)propanoic acid (Thiohi… — 2 measurement(s)
metal_id: metal_208 | ligand_id: ligand_5860
ligand_HxL_def: H2L | ligand_SMILES: NC(Cc1cnc(S)[nH]1)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_97690 | ref_eq_map_1067 | beta_def_812 | logK | 9.16 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (-11.77, L, +inf) |
| vlm_97691 | ref_eq_map_1067 | beta_def_840 | logK | -17.2 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (-11.77, L, +inf) |

### `Zn^[2+]` + L-2-Amino-3-(4-imidazolyl)propanoic acid (Histidine) — 3 measurement(s)
metal_id: metal_208 | ligand_id: ligand_5898
ligand_HxL_def: HL | ligand_SMILES: N[C@@H](Cc1c[nH]cn1)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_98899 | ref_eq_map_1353 | beta_def_812 | logK | 6.51 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.1, L, +inf) |
| vlm_98900 | ref_eq_map_1354 | beta_def_812 | logK | 6.35 | 37 | 0.15 | `[M] + [L] <=> [ML]` | *** | [L] | (9.1, L, +inf) |
| vlm_98901 | ref_eq_map_1355 | beta_def_812 | logK | 6.48 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.1, L, +inf) |

---

### Step 18: `search_pka_ligands`
**Args:**
```json
{
  "where": "(lc.ligand_name_SRD LIKE '%EDTA%')",
  "order_by": "p.pKa ASC",
  "limit": 5
}
```

[summary]
## search_pka_ligands — 5 row(s)

| ligand_id | ligand_name | HxL_def | formula | smiles | pH_ladder | T°C_range | I(M)_range | similarity_score |
|-----------|-------------|---------|---------|--------|-----------|-----------|------------|------------------|
| ligand_6335 | Oxybis(ethylenenitrilo)tetraacetic acid (EEDTA) | H4L | C12H20N2O9 | O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | −∞; H4L (M_tot_1); (-1.8, vlm_111731); H3L (M_tot_1); +∞ | 20 | 0.1 | *** |
| ligand_6277 | Ethylenedinitrilotetraacetic acid (EDTA) | H4L | C10H16N2O8 | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | −∞; H5L (M_tot_1); (-1.5, vlm_108289); H4L (M_tot_2); (2, vlm_108282); H3L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_6348 | Thiobis(ethylenenitrilo)tetraacetic acid (TEDTA) | H4L | C12H20N2O8S1 | O=C(O)CN(CCSCCN(CC(=O)O)CC(=O)O)CC(=O)O | −∞; H4L (M_tot_1); (2, vlm_112242); H3L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6275 | N-(2-Hydroxyethyl)ethylenedinitrilotriacetic acid (HEDTA) | H3L | C10H18N2O7 | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | −∞; H3L (M_tot_1); (2.62, vlm_107963); H2L (M_tot_1); +∞ | 25 | 0.1 | *** |

---

### Step 19: `search_pka_ligands`
**Args:**
```json
{
  "where": "(lc.ligand_name_SRD LIKE '%citrate%')",
  "order_by": "p.pKa ASC",
  "limit": 5
}
```

[summary]
## search_pka_ligands — 5 row(s)

| ligand_id | ligand_name | HxL_def | formula | smiles | pH_ladder | T°C_range | I(M)_range | similarity_score |
|-----------|-------------|---------|---------|--------|-----------|-----------|------------|------------------|
| ligand_8965 | 2-Hydroxypropane-1,2,3-tricarboxylic acid 1-methyl ester (a… | H2L | C7H10O7 | COC(=O)CC(O)(CC(=O)O)C(=O)O | −∞; H2L (M_tot_1); (2.7, vlm_155326); HL (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_8672 | 2-Hydroxypropane-1,2,3-tricarboxylic acid 1,3-dimethylester… | HL | C8H12O7 | COC(=O)CC(O)(CC(=O)OC)C(=O)O | −∞; HL (M_tot_1); (3.02, vlm_149461); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_8966 | 2-Hydroxypropane-1,2,3-tricarboxylic acid 2-methyl ester (s… | H2L | C7H10O7 | COC(=O)C(O)(CC(=O)O)CC(=O)O | −∞; H2L (M_tot_1); (3.39, vlm_155330); HL (M_tot_1); (4.63, vlm_155328); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_8682 | DL-2-Hydroxypropane-1,2,3-tricarboxylic acid 1,2-dimethyles… | HL | C8H12O7 | COC(=O)CC(O)(CC(=O)O)C(=O)OC | −∞; HL (M_tot_1); (3.78, vlm_149658); L (M_tot_1); +∞ | 25 | 0.1 | *** |

---

### Step 20: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208)",
  "order_by": "n.edge_count DESC",
  "limit": 5
}
```

[summary]
## search_networks — 16 row(s)

> **Reference equilibrium networks** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### `Zn^[2+]` + Aminoacetic acid (Glycine) — 5 network(s)
metal_id: metal_208 | ligand_id: ligand_5760 | ligand_def_HxL: HL | ligand_SMILES: NCC(=O)O

| beta_def | equation |
|----------|----------|
| beta_def_966 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_872 | ``[M] + [L]^3 <=> [ML3]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_113 | 4 | 4 | 31~41 | 0~0.3 | 4 | 4 diff beta_def | logK | 4.87~11.3 |
| ref_eq_net_112 | 3 | 3 | 20~30 | -0.05~0.25 | 3 | beta_def_812; beta_def_840; beta_def_872 | logK | 4.96~11.6 |
| ref_eq_net_114 | 3 | 3 | 19~29 | 0.35~0.65 | 3 | beta_def_812; beta_def_840; beta_def_872 | logK | 4.85~11.5 |
| ref_eq_net_115 | 3 | 3 | 19~29 | 0.85~1.15 | 3 | beta_def_812; beta_def_840; beta_def_872 | logK | 4.89~11.5 |
| ref_eq_net_116 | 3 | 3 | 5~15 | -0.15~0.15 | 3 | beta_def_812; beta_def_840; beta_def_872 | logK | 5.5~12.7 |

#### Reference-state network: ref_eq_net_113 (4 nodes)
> First network — reference conditions (T 31~41 °C, I 0~0.3 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 4.87 |
| beta_def_966 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` | logK | 8.9 |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` | logK | 8.97 |
| beta_def_872 | ``[M] + [L]^3 <=> [ML3]`` | logK | 11.3 |

---
