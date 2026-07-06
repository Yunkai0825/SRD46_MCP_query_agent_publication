# Q3.2.4 — Tool Results (batch 3)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "iron(II), iron(III)",
  "limit": 20
}
```

[summary]
## search_metals

*(no results)*

---

### Step 3: `search_metals`
**Args:**
```json
{
  "name": "iron",
  "symbol": "Fe",
  "limit": 20
}
```

[summary]
## search_metals — 2 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_61 | Fe^[3+] | Fe | 3 | ✓ | [Fe+3] | InChI=1S/Fe/q+3 | beta_totN_128 | ligand_totN_406 | vlm_totN_1473 |
| metal_62 | Fe^[2+] | Fe | 2 | ✓ | [Fe+2] | InChI=1S/Fe/q+2 | beta_totN_57 | ligand_totN_217 | vlm_totN_667 |

---

### Step 4: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_61"
}
```

[summary]
[CATALOG]
## build_system_catalog — 20 pair(s), 113 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_194 | [M] + [HL]^2 <=> [M(HL)2] |  |
| beta_def_204 | [MHL2] + [H] <=> [M(HL)2] |  |
| beta_def_207 | [MHL3] + [H] <=> [M(HL)2L] |  |
| beta_def_208 | [M] + [HL]^3 <=> [M(HL)3] |  |
| beta_def_213 | [M(HL)2L] + [H] <=> [M(HL)3] |  |
| beta_def_214 | [MH2L3] + [H] <=> [M(HL)3] |  |
| beta_def_238 | [M(OH)2L] + [H] <=> [M(OH)L] + [H2O] |  |
| beta_def_263 | [M(OH)3L] + [H] <=> [M(OH)2L] + [H2O] |  |
| beta_def_351 | [(M2O3)0.5(s,alpha)] + [H2O]^1.5 <=> [M] + [OH]^3 | solid |
| beta_def_352 | [ML3(s)] <=> [M] + [L]^3 | solid |
| beta_def_357 | [MOOH(s,alpha)] + [H2O] <=> [M] + [OH]^3 | solid |
| beta_def_423 | [ML]^2 + [H2O]^2 <=> [M2(OH)2L2] + [H]^2 |  |
| beta_def_424 | [M]^2 + [L]^2 + [H2O]^2 <=> [M2(OH)2L2] + [H]^2 |  |
| beta_def_427 | [M(OH)L]^2 <=> [M2(OH)2L2] |  |
| beta_def_502 | [M]^2 + [L] <=> [M2L] |  |
| beta_def_519 | [M]^2 + [L]^2 <=> [M2L2] |  |
| beta_def_585 | [M]^2 + [L]^3 + [H2O] <=> [M2(OH)L3] + [H] |  |
| beta_def_597 | [M]^3 + [L]^6 + [H2O]^2 <=> [M3(OH)2L6] + [H]^2 |  |
| beta_def_601 | [M]^3 + [L]^2 + [H2O]^3 <=> [M3(OH)3L2] + [H]^3 |  |
| beta_def_649 | [M]^3 + [L]^4 <=> [M3L4] |  |
| beta_def_708 | [M]^7 + [L]^6 + [H2O]^9 <=> [M7(OH)9L6] + [H]^9 |  |
| beta_def_748 | [ML3] + [H]^2 <=> [MH2L3] |  |
| beta_def_779 | [M] + [HL] <=> [MHL] |  |
| beta_def_788 | [ML] + [H] <=> [MHL] |  |
| beta_def_792 | [ML2] + [H] <=> [MHL2] |  |
| beta_def_803 | [ML3] + [H] <=> [MHL3] |  |
| beta_def_812 | [M] + [L] <=> [ML] |  |
| beta_def_821 | [M] + [HL] <=> [ML] + [H] |  |
| beta_def_823 | [M] + [H2L] <=> [ML] + [H]^2 |  |
| beta_def_840 | [M] + [L]^2 <=> [ML2] |  |
| beta_def_846 | [ML] + [HL] <=> [ML2] + [H] |  |
| beta_def_853 | [ML] + [H2L] <=> [ML2] + [H]^2 |  |
| beta_def_864 | [M(OH)2L2] + [H]^2 <=> [ML2] + [H2O]^2 |  |
| beta_def_872 | [M] + [L]^3 <=> [ML3] |  |
| beta_def_873 | [ML2] + [HL] <=> [ML3] + [H] |  |
| beta_def_876 | [ML2] + [H2L] <=> [ML3] + [H]^2 |  |
| beta_def_892 | [M(OH)L3] + [H] <=> [ML3] + [H2O] |  |
| beta_def_894 | [M] + [L]^4 <=> [ML4] |  |
| beta_def_903 | [M] + [L]^5 <=> [ML5] |  |
| beta_def_966 | [M(OH)L] + [H] <=> [ML] + [H2O] |  |
| beta_def_981 | [ML] + [OH] <=> [M(OH)L] |  |
| beta_def_984 | [M(OH)L2] + [H] <=> [ML2] + [H2O] |  |

*(all species aqueous unless noted)*

**1. Fe^[3+] + Hydrogen thiocyanate (Thiocyanic acid)** (metal_61 + ligand_10092) — ligand_def_HxL: HL | 39 ent, 5 sp, 39 vlms (vlm_172282…vlm_172320)
   - species: beta_def_812(21) beta_def_840(8) beta_def_872(5) beta_def_894(1) beta_def_981(4)
   - eq:13 nets T:19~30°C I:-0.15~5.15M max 4n/6e
**2. Fe^[3+] + Hydroxide ion** (metal_61 + ligand_10076) — ligand_def_HxL: *** | 38 ent, 8 sp, 38 vlms (vlm_170791…vlm_170828)
   - species: beta_def_351(1) beta_def_352(2) beta_def_357(2) beta_def_519(10) beta_def_649(5) beta_def_812(11) beta_def_840(6) beta_def_894(1)
   - eq:8 nets T:19~30°C I:-0.15~3.15M max 8n/28e
**3. Fe^[3+] + Hydrogen azide (Hydrazoic acid)** (metal_61 + ligand_10106) — ligand_def_HxL: HL | 22 ent, 5 sp, 22 vlms (vlm_173624…vlm_173645)
   - species: beta_def_812(6) beta_def_840(4) beta_def_872(4) beta_def_894(4) beta_def_903(4)
   - eq:4 nets T:19~30°C I:-0.15~3.15M max 5n/10e
**4. Fe^[3+] + 1,2-Dihydroxybenzene-3,5-disulfonic acid (Tiron)** (metal_61 + ligand_9358) — ligand_def_HxL: H4L | 16 ent, 4 sp, 16 vlms (vlm_162088…vlm_162103)
   - species: beta_def_788(4) beta_def_823(4) beta_def_853(4) beta_def_876(4)
   - eq:4 nets T:15~30°C I:-0.05~1.15M max 4n/6e
**5. Fe^[3+] + Ethanoic acid (Acetic acid)** (metal_61 + ligand_8465) — ligand_def_HxL: HL | 16 ent, 5 sp, 16 vlms (vlm_144783…vlm_144798)
   - species: beta_def_597(5) beta_def_601(1) beta_def_708(1) beta_def_812(6) beta_def_840(3)
   - eq:5 nets T:15~30°C I:-0.05~3.15M max 5n/10e
**6. Fe^[3+] + Nitrilotriacetic acid (NTA)** (metal_61 + ligand_6165) — ligand_def_HxL: H3L | 16 ent, 8 sp, 16 vlms (vlm_105553…vlm_105568)
   - species: beta_def_238(2) beta_def_263(1) beta_def_423(1) beta_def_427(1) beta_def_788(1) beta_def_812(4) beta_def_840(2) beta_def_966(4)
   - eq:5 nets T:15~30°C I:-0.05~1.15M max 5n/8e
**7. Fe^[3+] + 2-Hydroxybenzoic acid (Salicylic acid)** (metal_61 + ligand_9257) — ligand_def_HxL: H2L | 15 ent, 3 sp, 15 vlms (vlm_160398…vlm_160412)
   - species: beta_def_779(1) beta_def_821(11) beta_def_846(3)
   - eq:7 nets T:15~30°C I:-0.15~3.15M max 3n/3e
**8. Fe^[3+] + Propanedioic acid (Malonic acid)** (metal_61 + ligand_8873) — ligand_def_HxL: H2L | 14 ent, 3 sp, 14 vlms (vlm_152337…vlm_152350)
   - species: beta_def_812(5) beta_def_840(5) beta_def_872(4)
   - eq:3 nets T:19~30°C I:-0.05~1.15M max 3n/3e
**9. Fe^[3+] + trans-1,2-Cyclohexylenedinitrilotetraacetic acid (CDTA)** (metal_61 + ligand_6301) — ligand_def_HxL: H4L | 14 ent, 4 sp, 14 vlms (vlm_109793…vlm_109806)
   - species: beta_def_423(3) beta_def_427(3) beta_def_812(4) beta_def_966(4)
   - eq:3 nets T:15~30°C I:-0.05~1.15M max 3n/3e
**10. Fe^[3+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_61 + ligand_6277) — ligand_def_HxL: H4L | 14 ent, 4 sp, 14 vlms (vlm_108639…vlm_108652)
   - species: beta_def_427(3) beta_def_788(3) beta_def_812(4) beta_def_966(4)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 3n/3e
**11. Fe^[3+] + Chloride ion** (metal_61 + ligand_10163) — ligand_def_HxL: *** | 13 ent, 2 sp, 13 vlms (vlm_177390…vlm_177402)
   - species: beta_def_812(11) beta_def_840(2)
   - eq:7 nets T:19~30°C I:-0.15~4.15M max 2n/1e
**12. Fe^[3+] + Hydrogen fluoride (Hydrofluoric acid)** (metal_61 + ligand_10162) — ligand_def_HxL: HL | 13 ent, 3 sp, 13 vlms (vlm_176996…vlm_177008)
   - species: beta_def_812(5) beta_def_840(4) beta_def_872(4)
   - eq:3 nets T:19~30°C I:-0.05~1.15M max 3n/3e
**13. Fe^[3+] + 4-Amino-2-hydroxybenzoic acid (p-Aminosalicylic acid)** (metal_61 + ligand_9297) — ligand_def_HxL: H2L | 13 ent, 4 sp, 13 vlms (vlm_161165…vlm_161177)
   - species: beta_def_779(6) beta_def_821(3) beta_def_846(2) beta_def_873(2)
   - eq:4 nets T:19~30°C I:-0.05~3.15M max 4n/6e
**14. Fe^[3+] + 8-Hydroxyquinoline (8-Quinolinol)(Oxine)** (metal_61 + ligand_8126) — ligand_def_HxL: HL | 13 ent, 4 sp, 13 vlms (vlm_137976…vlm_137988)
   - species: beta_def_352(1) beta_def_812(4) beta_def_840(4) beta_def_872(4)
   - eq:4 nets T:19~30°C I:-0.15~1.15M max 4n/6e
**15. Fe^[3+] + DL-2-Amino-3-hydroxybutanohydroxamic acid (Threoninehydroxamic acid)** (metal_61 + ligand_6995) — ligand_def_HxL: HL | 12 ent, 12 sp, 12 vlms (vlm_121724…vlm_121735)
   - species: beta_def_194(1) beta_def_204(1) beta_def_207(1) beta_def_208(1) beta_def_213(1) beta_def_424(1) beta_def_779(1) beta_def_792(1) beta_def_803(1) beta_def_840(1) beta_def_872(1) beta_def_892(1)
   - eq:1 nets T:16.5~31.5°C I:0.275~0.725M max 12n/41e
**16. Fe^[3+] + Ethanedioic acid (Oxalic acid)** (metal_61 + ligand_8872) — ligand_def_HxL: H2L | 11 ent, 3 sp, 11 vlms (vlm_151793…vlm_151803)
   - species: beta_def_812(5) beta_def_840(3) beta_def_872(3)
   - eq:3 nets T:16.5~31.5°C I:0.275~3.225M max 3n/3e
**17. Fe^[3+] + Glycylglycylglycinehydroxamic acid** (metal_61 + ligand_7000) — ligand_def_HxL: HL | 11 ent, 11 sp, 11 vlms (vlm_121837…vlm_121847)
   - species: beta_def_194(1) beta_def_204(1) beta_def_208(1) beta_def_214(1) beta_def_502(1) beta_def_748(1) beta_def_792(1) beta_def_812(1) beta_def_840(1) beta_def_864(1) beta_def_872(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 11n/30e
**18. Fe^[3+] + DL-2-Amino-3-hydroxypropanohydroxamic acid (Serinehydroxamic acid)** (metal_61 + ligand_6994) — ligand_def_HxL: HL | 11 ent, 11 sp, 11 vlms (vlm_121699…vlm_121709)
   - species: beta_def_194(1) beta_def_204(1) beta_def_207(1) beta_def_208(1) beta_def_213(1) beta_def_424(1) beta_def_779(1) beta_def_792(1) beta_def_803(1) beta_def_840(1) beta_def_872(1)
   - eq:1 nets T:16.5~31.5°C I:0.275~0.725M max 11n/34e
**19. Fe^[3+] + DL-2-Aminopentanohydroxamic acid (Norvalinehydroxamic acid)** (metal_61 + ligand_6985) — ligand_def_HxL: HL | 11 ent, 11 sp, 11 vlms (vlm_121560…vlm_121570)
   - species: beta_def_194(1) beta_def_207(1) beta_def_424(1) beta_def_585(1) beta_def_779(1) beta_def_792(1) beta_def_803(1) beta_def_840(1) beta_def_872(1) beta_def_892(1) beta_def_984(1)
   - eq:1 nets T:16.5~31.5°C I:0.275~0.725M max 11n/39e
**20. Fe^[3+] + Acetohydroxamic acid** (metal_61 + ligand_9873) — ligand_def_HxL: HL | 10 ent, 3 sp, 10 vlms (vlm_168447…vlm_168456)
   - species: beta_def_812(6) beta_def_840(2) beta_def_872(2)
   - eq:4 nets T:15~30°C I:-0.05~2.15M max 3n/3e

---

### Step 6: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND s.constant_type = 'logK1' AND s.solvent_name LIKE '%water%' AND s.temperature_c >= 293 AND s.temperature_c <= 303 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2))",
  "order_by": "c.ligand_class_name ASC, s.constant_value DESC",
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
  "where": "(c.metal_id = metal_62 AND s.constant_type = 'logK1' AND s.solvent_name LIKE '%water%' AND s.temperature_c >= 293 AND s.temperature_c <= 303 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2))",
  "order_by": "c.ligand_class_name ASC, s.constant_value DESC",
  "limit": 500
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
  "where": "(c.metal_id = metal_61 AND (s.solvent_name LIKE '%water%' OR s.solvent_name IS NULL) AND (s.temperature_c IS NULL OR (s.temperature_c >= 293 AND s.temperature_c <= 303)) AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2))",
  "order_by": "s.constant_value DESC",
  "limit": 500
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
  "where": "(c.metal_id = metal_62 AND (s.solvent_name LIKE '%water%' OR s.solvent_name IS NULL) AND (s.temperature_c IS NULL OR (s.temperature_c >= 293 AND s.temperature_c <= 303)) AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2))",
  "order_by": "s.constant_value DESC",
  "limit": 500
}
```

[summary]
## search_stability

*(no results)*

---

### Step 10: `get_table_schema`
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

### Step 11: `get_table_schema`
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

### Step 12: `get_table_schema`
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

### Step 13: `get_table_schema`
**Args:**
```json
{
  "table_name": "eq_map_collection",
  "database": "equilibrium"
}
```

[summary]
## get_table_schema - 10 column(s)

| cid | name | type | notnull | pk |
|-----|------|------|---------|----|
| 0 | collection_id | INTEGER | False | True |
| 1 | metal_id | INTEGER | True | False |
| 2 | ligand_id | INTEGER | True | False |
| 3 | metal_name | TEXT | False | False |
| 4 | ligand_name | TEXT | False | False |
| 5 | total_entries | INTEGER | False | False |
| 6 | total_networks | INTEGER | False | False |
| 7 | iterations_count | INTEGER | False | False |
| 8 | unassigned_count | INTEGER | False | False |
| 9 | created_at | TIMESTAMP | False | False |

---

### Step 14: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT c.metal_name_SRD, c.ligand_class_name, COUNT(*) AS n_meas, ROUND(AVG(n.constant_value),2) AS avg_logK, MIN(n.constant_value) AS min_logK, MAX(n.constant_value) AS max_logK FROM ligandmetal_card c JOIN eq_node n ON c.metal_id = n.metal_id AND c.ligand_id = n.ligand_id AND c.beta_definition_id = n.beta_definition_id WHERE c.metal_id IN (61,62) AND n.constant_value IS NOT NULL AND n.constant_type IN ('logK','logK1','log β','logB','logbeta','logβ','beta','β') GROUP BY c.metal_name_SRD, c.ligand_class_name ORDER BY c.metal_name_SRD, avg_logK DESC",
  "attach_equilibrium": true
}
```

[summary]
## execute_srd46_sql

*(no results)*

---

### Step 15: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT c.metal_name_SRD, c.ligand_name_SRD, c.ligand_class_name, c.beta_definition_name, n.constant_type, n.constant_value, n.temperature, n.ionic_strength FROM ligandmetal_card c JOIN eq_node n ON c.metal_id = n.metal_id AND c.ligand_id = n.ligand_id AND c.beta_definition_id = n.beta_definition_id WHERE c.metal_id IN (61,62) AND n.constant_value IS NOT NULL ORDER BY c.metal_id, n.constant_value DESC LIMIT 80",
  "attach_equilibrium": true
}
```

[summary]
## execute_srd46_sql - 50 row(s)

| metal_name_SRD | ligand_name_SRD | ligand_class_name | beta_definition_name | constant_type | constant_value | temperature | ionic_strength |
|----------------|-----------------|-------------------|----------------------|---------------|----------------|-------------|----------------|
| Fe^[3+] | Trimethylenedihydroxamic acid (Glutarodihydroxamic acid) | miscellaneous hydroxamic acids | [M<sub>2</sub>(HL)<sub>2</sub>L<sub>2</sub>]/[M]<sup>2</sup>[HL]<sup>2</sup>[L]... | K | 66.34 | 20.0 | 0.1 |
| Fe^[3+] | N,N'-Di-2-propylpentamethylenodihydroxamic acid (N,N'-Diisopropylglutarodihydro... | miscellaneous hydroxamic acids | [M<sub>2</sub>L<sub>3</sub>]/[M]<sup>2</sup>[L]<sup>3</sup> | K | 62.4 | 25.0 | 0.1 |
| Fe^[3+] | N,N'-Di-2-propylhexamethylenodihydroxamic acid (N,N'-Diisopropylglutarodihydrox... | miscellaneous hydroxamic acids | [M<sub>2</sub>L<sub>3</sub>]/[M]<sup>2</sup>[L]<sup>3</sup> | K | 62.3 | 25.0 | 0.1 |
| Fe^[3+] | N,N'-Di-2-propyltetramethylenodihydroxamic acid (N,N'-Diisopropylglutarodihydro... | miscellaneous hydroxamic acids | [M<sub>2</sub>L<sub>3</sub>]/[M]<sup>2</sup>[L]<sup>3</sup> | K | 62.2 | 25.0 | 0.1 |
| Fe^[3+] | Rhodotorulic acid | miscellaneous hydroxamic acids | [M<sub>2</sub>L<sub>3</sub>]/[M]<sup>2</sup>[L]<sup>3</sup> | K | 62.2 | 25.0 | 0.1 |
| Fe^[3+] | N,N'-Di-2-propyltrimethylenodihydroxamic acid (N,N'-Diisopropylglutarodihydroxa... | miscellaneous hydroxamic acids | [M<sub>2</sub>L<sub>3</sub>]/[M]<sup>2</sup>[L]<sup>3</sup> | K | 62.1 | 25.0 | 0.1 |
| Fe^[3+] | Trimethylenedihydroxamic acid (Glutarodihydroxamic acid) | miscellaneous hydroxamic acids | [M<sub>2</sub>(OH)L<sub>2</sub>]/[M]<sup>2</sup>[OH][L]<sup>2</sup> | K | 56.74 | 20.0 | 0.1 |
| Fe^[3+] | Trimethylenebis[aminocarbonyl(1,6-dihydro-1-hydroxy-6-oxo-2-pyridine)] (3-HOPOC... | miscellaneous hydroxamic acids | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | K | 52.3 | 25.0 | 0.1 |
| Fe^[3+] | Hydroxide ion | Inorganic ligands | [M<sub>3</sub>L<sub>4</sub>]/[M]<sup>3</sup>[L]<sup>4</sup> | K | 51.0 | 25.0 | 3.0 |
| Fe^[3+] | Hydroxide ion | Inorganic ligands | [M<sub>3</sub>L<sub>4</sub>]/[M]<sup>3</sup>[L]<sup>4</sup> | K | 51.0 | 25.0 | 3.0 |
| Fe^[3+] | Hydroxide ion | Inorganic ligands | [M<sub>3</sub>L<sub>4</sub>]/[M]<sup>3</sup>[L]<sup>4</sup> | K | 51.0 | 25.0 | 3.0 |
| Fe^[3+] | Hydroxide ion | Inorganic ligands | [M<sub>3</sub>L<sub>4</sub>]/[M]<sup>3</sup>[L]<sup>4</sup> | K | 51.0 | 25.0 | 3.0 |
| Fe^[3+] | Hydroxide ion | Inorganic ligands | [M<sub>3</sub>L<sub>4</sub>]/[M]<sup>3</sup>[L]<sup>4</sup> | K | 51.0 | 25.0 | 3.0 |
| Fe^[3+] | Piperazine-N,N'-diacetohydroxamic acid | Cyclic amines | [M<sub>2</sub>L<sub>4</sub>]/[M]<sup>2</sup>[L]<sup>4</sup> | K | 50.9 | 20.0 | 0.1 |
| Fe^[3+] | 1,4,7-Tris(3-hydroxy-6-methyl-2-pyridylmethyl)-1,4,7-triazacyclononane | Aza-macrocycles | [ML]/[M][L] | K | 50.0 | 25.0 | 0.1 |
| Fe^[3+] | Hydroxide ion | Inorganic ligands | [M<sub>3</sub>L<sub>4</sub>]/[M]<sup>3</sup>[L]<sup>4</sup> | K | 49.7 | 25.0 | 0.0 |
| Fe^[3+] | Hydroxide ion | Inorganic ligands | [M<sub>3</sub>L<sub>4</sub>]/[M]<sup>3</sup>[L]<sup>4</sup> | K | 49.7 | 25.0 | 3.0 |
| Fe^[3+] | Hydroxide ion | Inorganic ligands | [M<sub>3</sub>L<sub>4</sub>]/[M]<sup>3</sup>[L]<sup>4</sup> | K | 49.7 | 25.0 | 0.0 |
| Fe^[3+] | Hydroxide ion | Inorganic ligands | [M<sub>3</sub>L<sub>4</sub>]/[M]<sup>3</sup>[L]<sup>4</sup> | K | 49.7 | 25.0 | 3.0 |
| Fe^[3+] | Hydroxide ion | Inorganic ligands | [M<sub>3</sub>L<sub>4</sub>]/[M]<sup>3</sup>[L]<sup>4</sup> | K | 49.7 | 25.0 | 0.0 |
| Fe^[3+] | Hydroxide ion | Inorganic ligands | [M<sub>3</sub>L<sub>4</sub>]/[M]<sup>3</sup>[L]<sup>4</sup> | K | 49.7 | 25.0 | 3.0 |
| Fe^[3+] | Hydroxide ion | Inorganic ligands | [M<sub>3</sub>L<sub>4</sub>]/[M]<sup>3</sup>[L]<sup>4</sup> | K | 49.7 | 25.0 | 0.0 |
| Fe^[3+] | Hydroxide ion | Inorganic ligands | [M<sub>3</sub>L<sub>4</sub>]/[M]<sup>3</sup>[L]<sup>4</sup> | K | 49.7 | 25.0 | 3.0 |
| Fe^[3+] | Hydroxide ion | Inorganic ligands | [M<sub>3</sub>L<sub>4</sub>]/[M]<sup>3</sup>[L]<sup>4</sup> | K | 49.7 | 25.0 | 0.0 |
| Fe^[3+] | Hydroxide ion | Inorganic ligands | [M<sub>3</sub>L<sub>4</sub>]/[M]<sup>3</sup>[L]<sup>4</sup> | K | 49.7 | 25.0 | 3.0 |

... 25 more row(s) omitted

---
