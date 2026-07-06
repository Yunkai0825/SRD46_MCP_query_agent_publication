# Q4.3 — Tool Results (batch 3)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "copper(II), nickel(II), zinc(II)",
  "limit": 10
}
```

[summary]
## search_metals

*(no results)*

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "ethylenediamine, ammonia",
  "limit": 10
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 4: `search_metals`
**Args:**
```json
{
  "symbol": "Cu, Ni, Zn",
  "limit": 10
}
```

[summary]
## search_metals

*(no results)*

---

### Step 5: `search_ligands`
**Args:**
```json
{
  "name": "ethylenediamine, 1,2-diaminoethane, ammonia, azane",
  "limit": 20
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 7: `build_system_catalog`
**Args:**
```json
{}
```

[summary]
[CATALOG]
## build_system_catalog

**Error:** Provide at least one of metal_id, ligand_id, or beta_definition_id.

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "c.metal_name_SRD LIKE '%copper%' AND c.ligand_name_SRD LIKE '%amm%'",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. You must call 0_plan_search_strategy first (PHASE 2) before using the execution tools.

---

### Step 9: `search_stability`
**Args:**
```json
{
  "where": "c.metal_name_SRD LIKE '%nickel%' AND c.ligand_name_SRD LIKE '%amm%'",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. You must call 0_plan_search_strategy first (PHASE 2) before using the execution tools.

---

### Step 10: `search_stability`
**Args:**
```json
{
  "where": "c.metal_name_SRD LIKE '%zinc%' AND c.ligand_name_SRD LIKE '%amm%'",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. You must call 0_plan_search_strategy first (PHASE 2) before using the execution tools.

---

### Step 11: `search_stability`
**Args:**
```json
{
  "where": "c.metal_name_SRD LIKE '%copper%' AND (c.ligand_name_SRD LIKE '%ethylenediamine%' OR c.ligand_name_SRD LIKE '%diaminoethane%' OR c.ligand_name_SRD LIKE '%en%')",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. You must call 0_plan_search_strategy first (PHASE 2) before using the execution tools.

---

### Step 12: `search_stability`
**Args:**
```json
{
  "where": "c.metal_name_SRD LIKE '%nickel%' AND (c.ligand_name_SRD LIKE '%ethylenediamine%' OR c.ligand_name_SRD LIKE '%diaminoethane%' OR c.ligand_name_SRD LIKE '%en%')",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. You must call 0_plan_search_strategy first (PHASE 2) before using the execution tools.

---

### Step 13: `search_stability`
**Args:**
```json
{
  "where": "c.metal_name_SRD LIKE '%zinc%' AND (c.ligand_name_SRD LIKE '%ethylenediamine%' OR c.ligand_name_SRD LIKE '%diaminoethane%' OR c.ligand_name_SRD LIKE '%en%')",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. You must call 0_plan_search_strategy first (PHASE 2) before using the execution tools.

---

### Step 14: `search_metals`
**Args:**
```json
{
  "name": "copper, nickel, zinc",
  "limit": 20
}
```

[summary]
## search_metals

*(no results)*

---

### Step 15: `search_ligands`
**Args:**
```json
{
  "name": "ethylenediamine, ammonia",
  "limit": 20,
  "exclude_groups": []
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 17: `get_table_schema`
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

### Step 18: `get_table_schema`
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

### Step 19: `get_table_schema`
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

### Step 20: `get_table_schema`
**Args:**
```json
{
  "table_name": "ligand_card",
  "database": "cards"
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

### Step 21: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT metal_id, metal_name_SRD, symbol_pure, charge, charge_str FROM metal_card WHERE (symbol_pure IN ('Cu','Ni','Zn') OR metal_name_SRD LIKE '%copper%' OR metal_name_SRD LIKE '%nickel%' OR metal_name_SRD LIKE '%zinc%') AND charge = 2 ORDER BY symbol_pure, metal_name_SRD;"
}
```

[summary]
## execute_srd46_sql - 3 row(s)

| metal_id | metal_name_SRD | symbol_pure | charge | charge_str |
|----------|----------------|-------------|--------|------------|
| metal_41 | Cu^[2+] | Cu | 2 | 2+ |
| metal_112 | Ni^[2+] | Ni | 2 | 2+ |
| metal_208 | Zn^[2+] | Zn | 2 | 2+ |

---

### Step 22: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT ligand_id, ligand_name_SRD, synonym_iupac_name, synonym_common_name, formula, definition_HxL FROM ligand_card WHERE ligand_name_SRD LIKE '%ethylenediamine%' OR synonym_iupac_name LIKE '%ethylenediamine%' OR synonym_common_name LIKE '%ethylenediamine%' OR ligand_name_SRD LIKE '%diaminoethane%' OR synonym_iupac_name LIKE '%diaminoethane%' OR synonym_common_name LIKE '%diaminoethane%' OR ligand_name_SRD LIKE '%ammonia%' OR synonym_iupac_name LIKE '%ammonia%' OR synonym_common_name LIKE '%ammonia%' OR formula LIKE '%NH3%' ORDER BY ligand_name_SRD;"
}
```

[summary]
## execute_srd46_sql - 50 row(s)

| ligand_id | ligand_name_SRD | synonym_iupac_name | synonym_common_name | formula | definition_HxL |
|-----------|-----------------|--------------------|---------------------|---------|----------------|
| ligand_7036 | 1,1,2,2-Tetramethylethylenediamine | *** | *** | C6H16N2 | L |
| ligand_10480 | 1,1-Diethylethylenediamine | *** | *** | ******** | *** |
| ligand_7033 | 1,1-Dimethylethylenediamine | *** | *** | C4H12N2 | L |
| ligand_7059 | 1,3-Diamino-2-propanol (2-Hydroxytrimethylenediamine) | *** | *** | C3H10N2O1 | L |
| ligand_7395 | 1,4-Diazabicyclo[2.2.2]octane (Triethylenediamine) | *** | *** | C6H8N2 | L |
| ligand_10501 | 2,2-Diethyltrimethylenediamine | *** | *** | ******** | *** |
| ligand_7039 | 2,2-Dimethyltrimethylenediamine (2,2-Dimethyl-1,3-propylenediamine) | *** | *** | C5H14N2 | L |
| ligand_7181 | 2-(2-Aminoethylamino)ethanol [N-(2-Hydroxyethyl)ethylenediamine] | *** | *** | C4H12N2O1 | L |
| ligand_8117 | 2-(2-Aminoethylaminomethyl)pyridine (N-2-Picolylethylenediamine) | *** | *** | C8H12N3 | L |
| ligand_7166 | 2-(2-Propylaminomethyl)-2-propylamine (N-2-Propyl-2,2-dimethylethylenediamine) | *** | *** | C7H18N2 | L |
| ligand_7183 | 2-(3-Aminopropylamino)ethanol [N-(2-Hydroxyethyl)trimethylenediamine] | *** | *** | C5H14N2O1 | L |
| ligand_7168 | 2-(Cyclohexylaminomethyl)-2-propylamine (N-Cyclohexyl-2,2-dimethylethylenediami... | *** | *** | C10H22N2 | L |
| ligand_8383 | 2-Aminoethylaminomethylphosphonic acid (Ethylenediamine-N-methylenephosphonic a... | *** | *** | C3H11N2O3P1 | H2L |
| ligand_7040 | 2-Methylenetrimethylenediamine (2-Methylene-1,3-propylenediamine) | *** | *** | C4H10N2 | L |
| ligand_8118 | 2-[2-(2-Aminoethylamino)ethyl]pyridine (N-[2-(2-Picolyl)ethyl]ethylenediamine) | *** | *** | C9H14N3 | L |
| ligand_10533 | 3-(2-Aminoethylamino)propanol (N-(3-hydroxypropyl)ethylenediamine) | *** | *** | ******** | *** |
| ligand_7311 | 3-Aminopropylnitrilodi-2-ethanol [N,N-Bis(2-hydroxyethyl)trimethylenediamine] | *** | *** | C7H18N2O2 | L |
| ligand_7194 | 7-Thia-1,4-diazanonane [N-(2-Ethylthioethyl)ethylenediamine] | *** | *** | C6H16N2S1 | L |
| ligand_7193 | 7-Thia-1,4-diazaoctane [N-(2-Methylthioethyl)ethylenediamine] | *** | *** | C5H14N2S1 | L |
| ligand_7195 | 8,8-Dimethyl-7-thia-1,4-diazanonane [N-(2-(2-Methyl-2-propylthio)ethyl)ethylene... | *** | *** | C8H20N2S1 | L |
| ligand_7196 | 8-Thia-1,5-diazanonane [N-(2-Methylthioethyl)trimethylenediamine] | *** | *** | C6H16N2S1 | L |
| ligand_10103 | Ammonia | *** | *** | H3N1 | L |
| ligand_7032 | DL-(2-Methyl-2-propyl)ethylenediamine (t-Butylethylenediamine) | *** | *** | C6H16N2 | L |
| ligand_7034 | DL-1,2-Dimethylethylenediamine (DL-2,3-Butylenediamine) | *** | *** | C4H12N2 | L |
| ligand_7182 | DL-1-(2-Aminoethylamino)-2-propanol [N-(2-Hydroxypropyl)ethylenediamine] | *** | *** | C5H14N2O1 | L |

... 25 more row(s) omitted

---

### Step 23: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT ligand_id, ligand_name_SRD, synonym_iupac_name, synonym_common_name, formula, definition_HxL FROM ligand_card WHERE ligand_name_SRD = 'Ethylenediamine' OR synonym_iupac_name = 'Ethylenediamine' OR synonym_common_name = 'Ethylenediamine' OR ligand_name_SRD = '1,2-Diaminoethane' OR synonym_iupac_name = '1,2-Diaminoethane' OR synonym_common_name = '1,2-Diaminoethane' OR ligand_name_SRD = '1,2-diaminoethane' OR synonym_iupac_name = '1,2-diaminoethane' OR synonym_common_name = '1,2-diaminoethane' OR ligand_name_SRD LIKE '%Ethylenediamine%' OR synonym_iupac_name LIKE '%Ethylenediamine%' OR synonym_common_name LIKE '%Ethylenediamine%' ORDER BY ligand_name_SRD;"
}
```

[summary]
## execute_srd46_sql - 50 row(s)

| ligand_id | ligand_name_SRD | synonym_iupac_name | synonym_common_name | formula | definition_HxL |
|-----------|-----------------|--------------------|---------------------|---------|----------------|
| ligand_7036 | 1,1,2,2-Tetramethylethylenediamine | *** | *** | C6H16N2 | L |
| ligand_10480 | 1,1-Diethylethylenediamine | *** | *** | ******** | *** |
| ligand_7033 | 1,1-Dimethylethylenediamine | *** | *** | C4H12N2 | L |
| ligand_7059 | 1,3-Diamino-2-propanol (2-Hydroxytrimethylenediamine) | *** | *** | C3H10N2O1 | L |
| ligand_7395 | 1,4-Diazabicyclo[2.2.2]octane (Triethylenediamine) | *** | *** | C6H8N2 | L |
| ligand_10501 | 2,2-Diethyltrimethylenediamine | *** | *** | ******** | *** |
| ligand_7039 | 2,2-Dimethyltrimethylenediamine (2,2-Dimethyl-1,3-propylenediamine) | *** | *** | C5H14N2 | L |
| ligand_7181 | 2-(2-Aminoethylamino)ethanol [N-(2-Hydroxyethyl)ethylenediamine] | *** | *** | C4H12N2O1 | L |
| ligand_8117 | 2-(2-Aminoethylaminomethyl)pyridine (N-2-Picolylethylenediamine) | *** | *** | C8H12N3 | L |
| ligand_7166 | 2-(2-Propylaminomethyl)-2-propylamine (N-2-Propyl-2,2-dimethylethylenediamine) | *** | *** | C7H18N2 | L |
| ligand_7183 | 2-(3-Aminopropylamino)ethanol [N-(2-Hydroxyethyl)trimethylenediamine] | *** | *** | C5H14N2O1 | L |
| ligand_7168 | 2-(Cyclohexylaminomethyl)-2-propylamine (N-Cyclohexyl-2,2-dimethylethylenediami... | *** | *** | C10H22N2 | L |
| ligand_8383 | 2-Aminoethylaminomethylphosphonic acid (Ethylenediamine-N-methylenephosphonic a... | *** | *** | C3H11N2O3P1 | H2L |
| ligand_7040 | 2-Methylenetrimethylenediamine (2-Methylene-1,3-propylenediamine) | *** | *** | C4H10N2 | L |
| ligand_8118 | 2-[2-(2-Aminoethylamino)ethyl]pyridine (N-[2-(2-Picolyl)ethyl]ethylenediamine) | *** | *** | C9H14N3 | L |
| ligand_10533 | 3-(2-Aminoethylamino)propanol (N-(3-hydroxypropyl)ethylenediamine) | *** | *** | ******** | *** |
| ligand_7311 | 3-Aminopropylnitrilodi-2-ethanol [N,N-Bis(2-hydroxyethyl)trimethylenediamine] | *** | *** | C7H18N2O2 | L |
| ligand_7194 | 7-Thia-1,4-diazanonane [N-(2-Ethylthioethyl)ethylenediamine] | *** | *** | C6H16N2S1 | L |
| ligand_7193 | 7-Thia-1,4-diazaoctane [N-(2-Methylthioethyl)ethylenediamine] | *** | *** | C5H14N2S1 | L |
| ligand_7195 | 8,8-Dimethyl-7-thia-1,4-diazanonane [N-(2-(2-Methyl-2-propylthio)ethyl)ethylene... | *** | *** | C8H20N2S1 | L |
| ligand_7196 | 8-Thia-1,5-diazanonane [N-(2-Methylthioethyl)trimethylenediamine] | *** | *** | C6H16N2S1 | L |
| ligand_7032 | DL-(2-Methyl-2-propyl)ethylenediamine (t-Butylethylenediamine) | *** | *** | C6H16N2 | L |
| ligand_7034 | DL-1,2-Dimethylethylenediamine (DL-2,3-Butylenediamine) | *** | *** | C4H12N2 | L |
| ligand_7182 | DL-1-(2-Aminoethylamino)-2-propanol [N-(2-Hydroxypropyl)ethylenediamine] | *** | *** | C5H14N2O1 | L |
| ligand_7038 | DL-1-Methyltrimethylenediamine (1,3-Butylenediamine) | *** | *** | C4H12N2 | L |

... 25 more row(s) omitted

---

### Step 24: `search_stability`
**Args:**
```json
{
  "where": "((c.metal_id = metal_41 OR c.metal_id = metal_112 OR c.metal_id = metal_208) AND (c.ligand_id = ligand_10103) AND s.temperature_c >= 24.9 AND s.temperature_c <= 25.1 AND (s.solvent_name IS NULL OR s.solvent_name LIKE '%water%' OR s.solvent_name LIKE '%aque%') AND s.constant_type IN ('logK','log β','logβ','K1','β1'))",
  "order_by": "c.metal_name_SRD, s.ionic_strength_mol_l, s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability

*(no results)*

---

### Step 25: `search_stability`
**Args:**
```json
{
  "where": "((c.metal_id = metal_41 OR c.metal_id = metal_112 OR c.metal_id = metal_208) AND s.temperature_c >= 24.9 AND s.temperature_c <= 25.1 AND (s.solvent_name IS NULL OR s.solvent_name LIKE '%water%' OR s.solvent_name LIKE '%aque%') AND s.constant_type IN ('logK','log β','logβ','K1','β1') AND (c.ligand_name_SRD LIKE '%Ethylenediamine%' OR c.ligand_name_SRD LIKE '%diaminoethane%'))",
  "order_by": "c.metal_name_SRD, s.ionic_strength_mol_l, s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability — 100 row(s)

### logK — 22 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_26 | Cd^[2+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 8 | 2 | 25 | 0.1~2 | *** | 4 |
| metal_2 | Ag^[+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 5 | 3 | 25 | 0.1~1 | *** | 2 |
| metal_25 | Ca^[2+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 4 | 2 | 25 | 0~1 | *** | 3 |
| metal_26 | Cd^[2+] | ligand_5948 | N-(2-Aminoethyl)glycine (Et… | HL | NCCNCC(=O)O | 4 | 2 | 25 | 0.1~1 | *** | 2 |
| metal_33 | Co^[2+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 4 | 2 | 25 | 0.1~1 | *** | 2 |
| metal_33 | Co^[2+] | ligand_5948 | N-(2-Aminoethyl)glycine (Et… | HL | NCCNCC(=O)O | 4 | 2 | 25 | 0.5~1 | *** | 2 |
| metal_6 | Am^[3+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 3 | 2 | 25 | 0.1~1 | *** | 2 |
| metal_33 | Co^[2+] | ligand_5975 | Ethylenediiminodiacetic aci… | H2L | O=C(O)CNCCNCC(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_5958 | Diethylenetriamine-N(1)-ace… | HL | NCCNCCNCC(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_2 | Ag^[+] | ligand_5797 | 4-Aminobutanoic acid | HL | NCCCC(=O)O | 2 | 2 | 25 | 0.5 | *** | 1 |
| metal_5 | Al^[3+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 2 | 2 | 25 | 0.5 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_6132 | N-(2-Carboxyethyl)glycine | H2L | O=C(O)CCNCC(=O)O | 2 | 2 | 30 | 0.1 | *** | 1 |
| metal_27 | Ce^[3+] | ligand_5975 | Ethylenediiminodiacetic aci… | H2L | O=C(O)CNCCNCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_27 | Ce^[3+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_6132 | N-(2-Carboxyethyl)glycine | H2L | O=C(O)CCNCC(=O)O | 2 | 2 | 30 | 0.1 | *** | 1 |
| metal_18 | Ba^[2+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_19 | Be^[2+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_5975 | Ethylenediiminodiacetic aci… | H2L | O=C(O)CNCCNCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_6003 | 6-Oxa-3,9-diazaundecanedioi… | H2L | O=C(O)CNCCOCCNCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_34 | Co^[3+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_36 | Cr^[2+] | ligand_5975 | Ethylenediiminodiacetic aci… | H2L | O=C(O)CNCCNCC(=O)O | 1 | 1 | 25 | 1 | *** | 1 |
| metal_36 | Cr^[2+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 1 | 1 | 25 | 1 | *** | 1 |

### ΔH — 10 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_33 | Co^[2+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 11 | 2 | 15~35 | 0~1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 4 | 1 | 15~35 | 0~0.1 | *** | 0 |
| metal_2 | Ag^[+] | ligand_5797 | 4-Aminobutanoic acid | HL | NCCCC(=O)O | 2 | 2 | 25 | 0.5 | *** | 0 |
| metal_26 | Cd^[2+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 2 | 2 | 20 | 0.1 | *** | 0 |
| metal_27 | Ce^[3+] | ligand_5975 | Ethylenediiminodiacetic aci… | H2L | O=C(O)CNCCNCC(=O)O | 2 | 2 | 25 | 1 | *** | 0 |
| metal_2 | Ag^[+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_6 | Am^[3+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 1 | 1 | 25 | 0.5 | *** | 0 |
| metal_18 | Ba^[2+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 1 | 1 | 20 | 0.1 | *** | 0 |
| metal_26 | Cd^[2+] | ligand_5975 | Ethylenediiminodiacetic aci… | H2L | O=C(O)CNCCNCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_5975 | Ethylenediiminodiacetic aci… | H2L | O=C(O)CNCCNCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |

### ΔS — 10 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_33 | Co^[2+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 4 | 2 | 25 | 0.1~1 | *** | 0 |
| metal_2 | Ag^[+] | ligand_5797 | 4-Aminobutanoic acid | HL | NCCCC(=O)O | 2 | 2 | 25 | 0.5 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 2 | 1 | 25 | 0~0.1 | *** | 0 |
| metal_26 | Cd^[2+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_27 | Ce^[3+] | ligand_5975 | Ethylenediiminodiacetic aci… | H2L | O=C(O)CNCCNCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_2 | Ag^[+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_6 | Am^[3+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_18 | Ba^[2+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_26 | Cd^[2+] | ligand_5975 | Ethylenediiminodiacetic aci… | H2L | O=C(O)CNCCNCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_5975 | Ethylenediiminodiacetic aci… | H2L | O=C(O)CNCCNCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |

---
