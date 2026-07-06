# Q4.6 — Tool Results (batch 2)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Mn(II), Fe(II), Co(II), Ni(II), Cu(II), Zn(II)",
  "limit": 20
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
  "name": "EDTA, NTA, IDA, citrate, oxalate, glycine, histidine, ammonia, cyanide, acetate, phosphate, carbonate, sulfate, 1,10-phenanthroline, 2,2'-bipyridine, thiocyanate, thiosulfate, cysteine, glutathione, imidazole",
  "limit": 50
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 5: `build_system_catalog`
**Args:**
```json
{}
```

[summary]
[CATALOG]
## build_system_catalog

**Error:** Provide at least one of metal_id, ligand_id, or beta_definition_id.

---

### Step 6: `search_metals`
**Args:**
```json
{
  "symbol": "Mn, Fe, Co, Ni, Cu, Zn",
  "limit": 20
}
```

[summary]
## search_metals

*(no results)*

---

### Step 7: `search_ligands`
**Args:**
```json
{
  "name": "ethylenediaminetetraacetic acid, nitrilotriacetic acid, iminodiacetic acid, citric acid, oxalic acid, glycine, histidine, ammonia, cyanide, acetic acid, phosphoric acid, carbonic acid, sulfuric acid, phenanthroline, bipyridine, thiocyanate, thiosulfate, cysteine, glutathione, imidazole",
  "limit": 100
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 9: `get_table_schema`
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

### Step 10: `get_table_schema`
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

### Step 11: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_name_SRD IN ('manganese','iron','cobalt','nickel','copper','zinc'))",
  "order_by": "c.ligand_name_SRD ASC",
  "limit": 20
}
```

[summary]
## search_stability

*(no results)*

---

### Step 12: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT DISTINCT metal_name_SRD, metal_id FROM ligandmetal_card ORDER BY metal_name_SRD LIMIT 100",
  "attach_equilibrium": false,
  "attach_literature": false
}
```

[summary]
## execute_srd46_sql - 50 row(s)

| metal_name_SRD | metal_id |
|----------------|----------|
| Ac^[3+] | metal_1 |
| Ag^[+] | metal_2 |
| Ag^[2+] | metal_3 |
| Al^[3+] | metal_5 |
| Am^[3+] | metal_6 |
| As^[3+] | metal_10 |
| As^[5+] | metal_11 |
| Au^[+] | metal_13 |
| Au^[3+] | metal_14 |
| B^[3+] | metal_15 |
| Ba^[2+] | metal_18 |
| Be^[2+] | metal_19 |
| Bi^[3+] | metal_21 |
| Bk^[3+] | metal_22 |
| BuNH_[3]^[+] | metal_23 |
| Bu_[3]Pb^[+] | metal_16 |
| Bu_[4]N^[+] | metal_17 |
| Ca^[2+] | metal_25 |
| Cd^[2+] | metal_26 |
| Ce^[3+] | metal_27 |
| Ce^[4+] | metal_28 |
| Cf^[3+] | metal_29 |
| Cm^[3+] | metal_31 |
| Co^[2+] | metal_33 |
| Co^[3+] | metal_34 |

... 25 more row(s) omitted

---

### Step 13: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT DISTINCT metal_name_SRD, metal_id FROM ligandmetal_card WHERE metal_name_SRD IN ('Mn^[2+]','Fe^[2+]','Co^[2+]','Ni^[2+]','Cu^[2+]','Zn^[2+]') ORDER BY metal_name_SRD",
  "attach_equilibrium": false,
  "attach_literature": false
}
```

[summary]
## execute_srd46_sql - 6 row(s)

| metal_name_SRD | metal_id |
|----------------|----------|
| Co^[2+] | metal_33 |
| Cu^[2+] | metal_41 |
| Fe^[2+] | metal_62 |
| Mn^[2+] | metal_94 |
| Ni^[2+] | metal_112 |
| Zn^[2+] | metal_208 |

---

### Step 14: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT ligand_id, ligand_name_SRD, ligand_HxL_definition_SRD, beta_definition_id, beta_definition_name, COUNT(DISTINCT metal_id) AS metal_count FROM ligandmetal_card WHERE metal_id IN (94,62,33,112,41,208) GROUP BY ligand_id, ligand_name_SRD, ligand_HxL_definition_SRD, beta_definition_id, beta_definition_name HAVING COUNT(DISTINCT metal_id)=6 ORDER BY ligand_name_SRD LIMIT 100",
  "attach_equilibrium": false,
  "attach_literature": false
}
```

[summary]
## execute_srd46_sql - 50 row(s)

| ligand_id | ligand_name_SRD | ligand_HxL_definition_SRD | beta_definition_id | beta_definition_name | metal_count |
|-----------|-----------------|---------------------------|--------------------|----------------------|-------------|
| ligand_6333 | (2-Hydroxytrimethylene)dinitrilotetraacetic acid | H4L | beta_def_788 | [MHL]/[ML][H] | 6 |
| ligand_6333 | (2-Hydroxytrimethylene)dinitrilotetraacetic acid | H4L | beta_def_812 | [ML]/[M][L] | 6 |
| ligand_9064 | (Carboxymethoxy)propanedioic acid | H3L | beta_def_779 | [MHL]/[M][HL] | 6 |
| ligand_9064 | (Carboxymethoxy)propanedioic acid | H3L | beta_def_812 | [ML]/[M][L] | 6 |
| ligand_8191 | 1,10-Phenanthroline (Dipyridino[a,c]benzene) | L | beta_def_812 | [ML]/[M][L] | 6 |
| ligand_8191 | 1,10-Phenanthroline (Dipyridino[a,c]benzene) | L | beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | 6 |
| ligand_8191 | 1,10-Phenanthroline (Dipyridino[a,c]benzene) | L | beta_def_872 | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | 6 |
| ligand_7771 | 1,2-Diazole (Pyrazole) | L | beta_def_812 | [ML]/[M][L] | 6 |
| ligand_9337 | 1,2-Dihydroxybenzene (Catechol) | H2L | beta_def_823 | [ML][H]<sup>2</sup>/[M][H<sub>2</sub>L] | 6 |
| ligand_9337 | 1,2-Dihydroxybenzene (Catechol) | H2L | beta_def_853 | [ML<sub>2</sub>][H]<sup>2</sup>/[ML][H<sub>2</sub>L] | 6 |
| ligand_6751 | 1,2-Phenylenedinitrilotetraacetic acid | H4L | beta_def_788 | [MHL]/[ML][H] | 6 |
| ligand_6751 | 1,2-Phenylenedinitrilotetraacetic acid | H4L | beta_def_812 | [ML]/[M][L] | 6 |
| ligand_7795 | 1,3-Diazole (Imidazole) | L | beta_def_812 | [ML]/[M][L] | 6 |
| ligand_7795 | 1,3-Diazole (Imidazole) | L | beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | 6 |
| ligand_6071 | 1,4,10,13-Tetraoxa-7,16-diazacyclooctadecane-N,N'-diacetic acid | H2L | beta_def_812 | [ML]/[M][L] | 6 |
| ligand_6070 | 1,4,10-Trioxa-7,13-diazacyclopentadecane-N,N'-diacetic acid | H2L | beta_def_812 | [ML]/[M][L] | 6 |
| ligand_7530 | 1,4,7,10,13,16,19-Heptaazacycloheneicosane ([21]aneN7) | L | beta_def_812 | [ML]/[M][L] | 6 |
| ligand_7244 | 1,4,7,10,13-Pentaazatridecane (Tetraethylenepentamine)(tetren)(2,2,2,2-pent) | L | beta_def_812 | [ML]/[M][L] | 6 |
| ligand_6102 | 1,4,7,10-Tetraazacyclododecane-N,N',N'',N'''-tetraacetic acid (DOTA) | H4L | beta_def_788 | [MHL]/[ML][H] | 6 |
| ligand_6102 | 1,4,7,10-Tetraazacyclododecane-N,N',N'',N'''-tetraacetic acid (DOTA) | H4L | beta_def_812 | [ML]/[M][L] | 6 |
| ligand_6104 | 1,4,7,10-Tetraazacyclotridecane-N,N',N'',N'''-tetraacetic acid (TRITA) | H4L | beta_def_788 | [MHL]/[ML][H] | 6 |
| ligand_6104 | 1,4,7,10-Tetraazacyclotridecane-N,N',N'',N'''-tetraacetic acid (TRITA) | H4L | beta_def_812 | [ML]/[M][L] | 6 |
| ligand_7224 | 1,4,7,10-Tetraazadecane (Triethylenetetramine)(trien)(2,2,2-tet) | L | beta_def_812 | [ML]/[M][L] | 6 |
| ligand_7212 | 1,4,7-Triazaheptane (Diethylenetriamine)(dien)(2,2-tri) | L | beta_def_812 | [ML]/[M][L] | 6 |
| ligand_7212 | 1,4,7-Triazaheptane (Diethylenetriamine)(dien)(2,2-tri) | L | beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | 6 |

... 25 more row(s) omitted

---

### Step 15: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT ligand_id, ligand_name_SRD, ligand_HxL_definition_SRD, beta_definition_id, beta_definition_name, metal_name_SRD, ROUND(AVG(CASE WHEN constant_value GLOB '*[^0-9.-]*' THEN NULL ELSE CAST(constant_value AS REAL) END), 3) AS avg_logbeta, COUNT(*) AS n_rows FROM ligandmetal_card c JOIN ligandmetal_stability_measured s ON c.complex_system_id = s.complex_system_id WHERE c.metal_id IN (94,62,33,112,41,208) AND c.beta_definition_id = 812 GROUP BY ligand_id, ligand_name_SRD, ligand_HxL_definition_SRD, beta_definition_id, beta_definition_name, metal_name_SRD HAVING COUNT(DISTINCT metal_name_SRD) >= 1 ORDER BY ligand_name_SRD, metal_name_SRD LIMIT 300",
  "attach_equilibrium": false,
  "attach_literature": false
}
```

[TOOL ERROR] execute_srd46_sql: Error executing tool execute_srd46_sql: no such column: s.complex_system_id

---

### Step 16: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_94, metal_62, metal_33, metal_112, metal_41, metal_208) AND c.beta_definition_id = beta_def_812 AND c.ligand_id IN (ligand_8191, ligand_7795, ligand_7212, ligand_7224, ligand_7244, ligand_6102, ligand_6104, ligand_6333, ligand_6751, ligand_9064))",
  "order_by": "c.ligand_name_SRD ASC, c.metal_name_SRD ASC, s.constant_value ASC",
  "limit": 500
}
```

[summary]
## search_stability — 200 row(s)

### logK — 58 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_112 | Ni^[2+] | ligand_7795 | 1,3-Diazole (Imidazole) | L | c1c[nH]cn1 | 9 | 1 | 25~37 | 0~4 | *** | 9 |
| metal_41 | Cu^[2+] | ligand_7795 | 1,3-Diazole (Imidazole) | L | c1c[nH]cn1 | 8 | 1 | 25~37 | 0~3 | *** | 8 |
| metal_208 | Zn^[2+] | ligand_7795 | 1,3-Diazole (Imidazole) | L | c1c[nH]cn1 | 7 | 1 | 25~37 | 0.1~3 | *** | 7 |
| metal_112 | Ni^[2+] | ligand_8191 | 1,10-Phenanthroline (Dipyri… | L | c1cnc2c(c1)ccc1cccnc12 | 4 | 1 | 25 | 0~1 | *** | 4 |
| metal_33 | Co^[2+] | ligand_7795 | 1,3-Diazole (Imidazole) | L | c1c[nH]cn1 | 4 | 1 | 25~37 | 0.1~3 | *** | 4 |
| metal_41 | Cu^[2+] | ligand_7212 | 1,4,7-Triazaheptane (Diethy… | L | NCCNCCN | 4 | 1 | 25 | 0~1 | *** | 4 |
| metal_41 | Cu^[2+] | ligand_8191 | 1,10-Phenanthroline (Dipyri… | L | c1cnc2c(c1)ccc1cccnc12 | 3 | 1 | 25 | 0~0.5 | *** | 3 |
| metal_208 | Zn^[2+] | ligand_8191 | 1,10-Phenanthroline (Dipyri… | L | c1cnc2c(c1)ccc1cccnc12 | 3 | 1 | 25 | 0~1 | *** | 3 |
| metal_41 | Cu^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 3 | 1 | 25~37 | 0.1~1 | *** | 3 |
| metal_112 | Ni^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 3 | 1 | 25 | 0.1~1 | *** | 3 |
| metal_208 | Zn^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 3 | 1 | 25~37 | 0.1~1 | *** | 3 |
| metal_33 | Co^[2+] | ligand_6333 | (2-Hydroxytrimethylene)dini… | H4L | O=C(O)CN(CC(=O)O)CC(O)CN(CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1 | *** | 2 |
| metal_94 | Mn^[2+] | ligand_6333 | (2-Hydroxytrimethylene)dini… | H4L | O=C(O)CN(CC(=O)O)CC(O)CN(CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1 | *** | 2 |
| metal_208 | Zn^[2+] | ligand_6333 | (2-Hydroxytrimethylene)dini… | H4L | O=C(O)CN(CC(=O)O)CC(O)CN(CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_8191 | 1,10-Phenanthroline (Dipyri… | L | c1cnc2c(c1)ccc1cccnc12 | 2 | 1 | 25 | 0~0.1 | *** | 2 |
| metal_41 | Cu^[2+] | ligand_6751 | 1,2-Phenylenedinitrilotetra… | H4L | O=C(O)CN(CC(=O)O)c1ccccc1N(CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~1 | *** | 2 |
| metal_94 | Mn^[2+] | ligand_7795 | 1,3-Diazole (Imidazole) | L | c1c[nH]cn1 | 2 | 1 | 25 | 0.1~0.5 | *** | 2 |
| metal_33 | Co^[2+] | ligand_6102 | 1,4,7,10-Tetraazacyclododec… | H4L | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 2 | 1 | 25 | 0.1 | *** | 2 |
| metal_41 | Cu^[2+] | ligand_6102 | 1,4,7,10-Tetraazacyclododec… | H4L | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 2 | 1 | 25 | 0.1 | *** | 2 |
| metal_112 | Ni^[2+] | ligand_6102 | 1,4,7,10-Tetraazacyclododec… | H4L | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 2 | 1 | 25 | 0.1 | *** | 2 |
| metal_208 | Zn^[2+] | ligand_6102 | 1,4,7,10-Tetraazacyclododec… | H4L | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 2 | 1 | 25 | 0.1 | *** | 2 |
| metal_33 | Co^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 2 | 1 | 25 | 0.1~1 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 2 | 1 | 25 | 0.1~1 | *** | 2 |
| metal_94 | Mn^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 2 | 1 | 25 | 0.1~1 | *** | 2 |
| metal_33 | Co^[2+] | ligand_7212 | 1,4,7-Triazaheptane (Diethy… | L | NCCNCCN | 2 | 1 | 25 | 0.1~1 | *** | 2 |
| metal_41 | Cu^[2+] | ligand_6333 | (2-Hydroxytrimethylene)dini… | H4L | O=C(O)CN(CC(=O)O)CC(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6333 | (2-Hydroxytrimethylene)dini… | H4L | O=C(O)CN(CC(=O)O)CC(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_6333 | (2-Hydroxytrimethylene)dini… | H4L | O=C(O)CN(CC(=O)O)CC(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_9064 | (Carboxymethoxy)propanedioi… | H3L | O=C(O)COC(C(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_9064 | (Carboxymethoxy)propanedioi… | H3L | O=C(O)COC(C(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_9064 | (Carboxymethoxy)propanedioi… | H3L | O=C(O)COC(C(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_94 | Mn^[2+] | ligand_9064 | (Carboxymethoxy)propanedioi… | H3L | O=C(O)COC(C(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_9064 | (Carboxymethoxy)propanedioi… | H3L | O=C(O)COC(C(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_9064 | (Carboxymethoxy)propanedioi… | H3L | O=C(O)COC(C(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_8191 | 1,10-Phenanthroline (Dipyri… | L | c1cnc2c(c1)ccc1cccnc12 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_94 | Mn^[2+] | ligand_8191 | 1,10-Phenanthroline (Dipyri… | L | c1cnc2c(c1)ccc1cccnc12 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_6751 | 1,2-Phenylenedinitrilotetra… | H4L | O=C(O)CN(CC(=O)O)c1ccccc1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6751 | 1,2-Phenylenedinitrilotetra… | H4L | O=C(O)CN(CC(=O)O)c1ccccc1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 1 | *** | 1 |
| metal_94 | Mn^[2+] | ligand_6751 | 1,2-Phenylenedinitrilotetra… | H4L | O=C(O)CN(CC(=O)O)c1ccccc1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_6751 | 1,2-Phenylenedinitrilotetra… | H4L | O=C(O)CN(CC(=O)O)c1ccccc1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6751 | 1,2-Phenylenedinitrilotetra… | H4L | O=C(O)CN(CC(=O)O)c1ccccc1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7795 | 1,3-Diazole (Imidazole) | L | c1c[nH]cn1 | 1 | 1 | 30 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_94 | Mn^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6102 | 1,4,7,10-Tetraazacyclododec… | H4L | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_94 | Mn^[2+] | ligand_6102 | 1,4,7,10-Tetraazacyclododec… | H4L | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_6104 | 1,4,7,10-Tetraazacyclotride… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_6104 | 1,4,7,10-Tetraazacyclotride… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6104 | 1,4,7,10-Tetraazacyclotride… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_94 | Mn^[2+] | ligand_6104 | 1,4,7,10-Tetraazacyclotride… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_6104 | 1,4,7,10-Tetraazacyclotride… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6104 | 1,4,7,10-Tetraazacyclotride… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7212 | 1,4,7-Triazaheptane (Diethy… | L | NCCNCCN | 1 | 1 | 25 | 1 | *** | 1 |
| metal_94 | Mn^[2+] | ligand_7212 | 1,4,7-Triazaheptane (Diethy… | L | NCCNCCN | 1 | 1 | 25 | 1 | *** | 1 |

### ΔH — 38 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_41 | Cu^[2+] | ligand_8191 | 1,10-Phenanthroline (Dipyri… | L | c1cnc2c(c1)ccc1cccnc12 | 2 | 1 | 20~25 | 0~0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_8191 | 1,10-Phenanthroline (Dipyri… | L | c1cnc2c(c1)ccc1cccnc12 | 2 | 1 | 20~25 | 0~0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 2 | 1 | 25 | 0.1~1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 2 | 1 | 25 | 0.1~1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 2 | 1 | 25 | 0.1~1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 2 | 1 | 25 | 0.1~1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_8191 | 1,10-Phenanthroline (Dipyri… | L | c1cnc2c(c1)ccc1cccnc12 | 1 | 1 | 20 | 0.1 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_8191 | 1,10-Phenanthroline (Dipyri… | L | c1cnc2c(c1)ccc1cccnc12 | 1 | 1 | 20 | 0.1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_8191 | 1,10-Phenanthroline (Dipyri… | L | c1cnc2c(c1)ccc1cccnc12 | 1 | 1 | 20 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_6751 | 1,2-Phenylenedinitrilotetra… | H4L | O=C(O)CN(CC(=O)O)c1ccccc1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6751 | 1,2-Phenylenedinitrilotetra… | H4L | O=C(O)CN(CC(=O)O)c1ccccc1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_6751 | 1,2-Phenylenedinitrilotetra… | H4L | O=C(O)CN(CC(=O)O)c1ccccc1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_6751 | 1,2-Phenylenedinitrilotetra… | H4L | O=C(O)CN(CC(=O)O)c1ccccc1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6751 | 1,2-Phenylenedinitrilotetra… | H4L | O=C(O)CN(CC(=O)O)c1ccccc1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7795 | 1,3-Diazole (Imidazole) | L | c1c[nH]cn1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_7795 | 1,3-Diazole (Imidazole) | L | c1c[nH]cn1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_7795 | 1,3-Diazole (Imidazole) | L | c1c[nH]cn1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_7795 | 1,3-Diazole (Imidazole) | L | c1c[nH]cn1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_6102 | 1,4,7,10-Tetraazacyclododec… | H4L | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6102 | 1,4,7,10-Tetraazacyclododec… | H4L | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_6102 | 1,4,7,10-Tetraazacyclododec… | H4L | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6102 | 1,4,7,10-Tetraazacyclododec… | H4L | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_6104 | 1,4,7,10-Tetraazacyclotride… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6104 | 1,4,7,10-Tetraazacyclotride… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_6104 | 1,4,7,10-Tetraazacyclotride… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6104 | 1,4,7,10-Tetraazacyclotride… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7212 | 1,4,7-Triazaheptane (Diethy… | L | NCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_7212 | 1,4,7-Triazaheptane (Diethy… | L | NCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7212 | 1,4,7-Triazaheptane (Diethy… | L | NCCNCCN | 1 | 1 | 25 | 1 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_7212 | 1,4,7-Triazaheptane (Diethy… | L | NCCNCCN | 1 | 1 | 25 | 1 | *** | 0 |

### ΔS — 38 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_41 | Cu^[2+] | ligand_8191 | 1,10-Phenanthroline (Dipyri… | L | c1cnc2c(c1)ccc1cccnc12 | 2 | 1 | 25 | 0~0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_8191 | 1,10-Phenanthroline (Dipyri… | L | c1cnc2c(c1)ccc1cccnc12 | 2 | 1 | 25 | 0~0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 2 | 1 | 25 | 0.1~1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 2 | 1 | 25 | 0.1~1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 2 | 1 | 25 | 0.1~1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 2 | 1 | 25 | 0.1~1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_8191 | 1,10-Phenanthroline (Dipyri… | L | c1cnc2c(c1)ccc1cccnc12 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_8191 | 1,10-Phenanthroline (Dipyri… | L | c1cnc2c(c1)ccc1cccnc12 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_8191 | 1,10-Phenanthroline (Dipyri… | L | c1cnc2c(c1)ccc1cccnc12 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_6751 | 1,2-Phenylenedinitrilotetra… | H4L | O=C(O)CN(CC(=O)O)c1ccccc1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6751 | 1,2-Phenylenedinitrilotetra… | H4L | O=C(O)CN(CC(=O)O)c1ccccc1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_6751 | 1,2-Phenylenedinitrilotetra… | H4L | O=C(O)CN(CC(=O)O)c1ccccc1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_6751 | 1,2-Phenylenedinitrilotetra… | H4L | O=C(O)CN(CC(=O)O)c1ccccc1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6751 | 1,2-Phenylenedinitrilotetra… | H4L | O=C(O)CN(CC(=O)O)c1ccccc1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7795 | 1,3-Diazole (Imidazole) | L | c1c[nH]cn1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_7795 | 1,3-Diazole (Imidazole) | L | c1c[nH]cn1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_7795 | 1,3-Diazole (Imidazole) | L | c1c[nH]cn1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_7795 | 1,3-Diazole (Imidazole) | L | c1c[nH]cn1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_6102 | 1,4,7,10-Tetraazacyclododec… | H4L | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6102 | 1,4,7,10-Tetraazacyclododec… | H4L | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_6102 | 1,4,7,10-Tetraazacyclododec… | H4L | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6102 | 1,4,7,10-Tetraazacyclododec… | H4L | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_6104 | 1,4,7,10-Tetraazacyclotride… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6104 | 1,4,7,10-Tetraazacyclotride… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_6104 | 1,4,7,10-Tetraazacyclotride… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6104 | 1,4,7,10-Tetraazacyclotride… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7212 | 1,4,7-Triazaheptane (Diethy… | L | NCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_7212 | 1,4,7-Triazaheptane (Diethy… | L | NCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7212 | 1,4,7-Triazaheptane (Diethy… | L | NCCNCCN | 1 | 1 | 25 | 1 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_7212 | 1,4,7-Triazaheptane (Diethy… | L | NCCNCCN | 1 | 1 | 25 | 1 | *** | 0 |

---
