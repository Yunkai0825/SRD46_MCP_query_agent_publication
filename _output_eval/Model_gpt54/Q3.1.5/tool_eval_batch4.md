# Q3.1.5 — Tool Results (batch 4)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Ca(II), Cu(II)",
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
  "name": "EGTA, citrate, tartrate, oxalate, carbonate, phosphate, sulfate, gluconate, lactate, acetate, malonate, NTA, EDTA, HEDP",
  "limit": 50
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
  "symbol": "Ca, Cu",
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
  "name": "ethyleneglycol-bis(2-aminoethylether)-N,N,N',N'-tetraacetic acid, ethylenediaminetetraacetic acid, nitrilotriacetic acid, citric acid, tartaric acid, oxalic acid, carbonic acid, phosphoric acid, sulfuric acid, gluconic acid, lactic acid, acetic acid, malonic acid, 1-hydroxyethylidene-1,1-diphosphonic acid",
  "limit": 50
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

### Step 9: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_name_SRD IN ('Ca(II)','Cu(II)'))",
  "order_by": "c.ligand_name_SRD ASC",
  "limit": 200
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

### Step 11: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_name = 'Ca' OR c.metal_name = 'Cu')",
  "order_by": "c.ligand_name ASC",
  "limit": 100
}
```

[summary]
## search_networks

*(no results)*

---

### Step 12: `db_distribution`
**Args:**
```json
{
  "table": "eq_collection_unassigned",
  "group_column": "ligand_name",
  "where": "metal_name IN ('Ca','Cu')",
  "limit": 100
}
```

[summary]
**db_distribution:** Error - Table 'eq_collection_unassigned' not allowed.

---

### Step 13: `get_table_schema`
**Args:**
```json
{
  "table_name": "eq_collection_unassigned",
  "database": "equilibrium"
}
```

[summary]
## get_table_schema - 2 column(s)

| cid | name | type | notnull | pk |
|-----|------|------|---------|----|
| 0 | collection_id | INTEGER | True | True |
| 1 | vlm_id | INTEGER | True | True |

---

### Step 14: `get_table_schema`
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

### Step 15: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT ligand_name, metal_name, total_entries, total_networks, metal_id, ligand_id FROM eq_map_collection WHERE metal_name IN ('Ca','Cu') ORDER BY ligand_name, metal_name LIMIT 300;",
  "attach_equilibrium": false,
  "attach_literature": false
}
```

[TOOL ERROR] execute_srd46_sql: Error executing tool execute_srd46_sql: no such table: eq_map_collection

---

### Step 16: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_name LIKE 'Ca%')",
  "order_by": "c.ligand_name ASC",
  "limit": 100
}
```

[summary]
## search_networks — 174 row(s)

> **Reference equilibrium networks (compact)** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### Beta-definition legend
| beta_def | equation |
|----------|----------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` |
| beta_def_739 | ``[MHL] + [H] <=> [MH2L]`` |
| beta_def_516 | ``[ML] + [M] <=> [M2L]`` |
| beta_def_966 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` |
| beta_def_779 | ``[M] + [HL] <=> [MHL]`` |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |
| beta_def_792 | ``[ML2] + [H] <=> [MHL2]`` |
| beta_def_751 | ``[MH2L] + [H] <=> [MH3L]`` |
| beta_def_765 | ``[MH3L] + [H] <=> [MH4L]`` |
| beta_def_298 | ``[MHL(s)] <=> [M] + [HL]`` |
| beta_def_502 | ``[M]^2 + [L] <=> [M2L]`` |

### Metal-ligand pair summary
| metal | metal_id | ligand | ligand_id | HxL | T_range | I_range | net_count | max_nodes | max_net_id | ligand_SMILES |
|-------|----------|--------|-----------|-----|---------|---------|-----------|----------|------------|---------------|
| `Ca^[2+]` | metal_25 | 1,2,3-Triazole-4,5-dicarboxylic acid | ligand_5956 | H2L | 20~30 | -0.05~0.25 | 1 | 3 | ref_eq_net_1671 | O=C(O)c1nn[nH]c1C(=O)O |
| `Ca^[2+]` | metal_25 | 1,4,10,13-Tetraoxa-7,16-diazacyclooctad… | ligand_6071 | H2L | 19~30 | -0.05~0.25 | 3 | 1 | ref_eq_net_2712 | O=C(O)CN1CCOCCOCCN(CC(=O)O)CCOCCOCC1 |
| `Ca^[2+]` | metal_25 | 1,4,10-Trioxa-7,13-diazacyclopentadecan… | ligand_6070 | H2L | 19~30 | -0.05~0.25 | 2 | 2 | ref_eq_net_2677 | O=C(O)CN1CCOCCOCCN(CC(=O)O)CCOCC1 |
| `Ca^[2+]` | metal_25 | 1,4,7,10-Tetraazacyclododecane-N,N',N''… | ligand_6102 | H4L | 20~30 | -0.05~0.25 | 1 | 3 | ref_eq_net_3021 | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 |
| `Ca^[2+]` | metal_25 | 1,4,7,10-Tetraazacyclododecane-N,N',N''… | ligand_6098 | H3L | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_2987 | CC(C(=O)O)N1CCNCCN(C(C)C(=O)O)CCN(C(C)C(=O)O)CC1 |
| `Ca^[2+]` | metal_25 | 1,4,7,10-Tetraazacyclododecane-N,N',N''… | ligand_6097 | H3L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_2974 | O=C(O)CN1CCNCCN(CC(=O)O)CCN(CC(=O)O)CC1 |
| `Ca^[2+]` | metal_25 | 1,4,7-Triazacyclononane-N,N',N''-triace… | ligand_6076 | H3L | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_2777 | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CC1 |
| `Ca^[2+]` | metal_25 | 1,4-Diazacyclohexane-N,N'-diacetic acid… | ligand_6058 | H2L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_2557 | O=C(O)CN1CCN(CC(=O)O)CC1 |
| `Ca^[2+]` | metal_25 | 1,4-Dioxa-7,10-diazacyclododecane-N,N'-… | ligand_6067 | H2L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_2632 | O=C(O)CN1CCOCCOCCN(CC(=O)O)CC1 |
| `Ca^[2+]` | metal_25 | 1,4-Dioxa-7,11-diazacyclotridecane-7,11… | ligand_6068 | H2L | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_2645 | O=C(O)CN1CCCN(CC(=O)O)CCOCCOCC1 |
| `Ca^[2+]` | metal_25 | 1,5,9-Triazacyclododecane-N,N',N''-tria… | ligand_6081 | H3L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_2797 | O=C(O)CN1CCCN(CC(=O)O)CCCN(CC(=O)O)CCC1 |
| `Ca^[2+]` | metal_25 | 1,7-Dioxa-4,10-diazacyclododecane-N,N'-… | ligand_6069 | H2L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_2659 | O=C(O)CN1CCOCCN(CC(=O)O)CCOCC1 |
| `Ca^[2+]` | metal_25 | 1-Aminocyclohexanecarboxylic acid | ligand_5774 | HL | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_371 | NC1(C(=O)O)CCCCC1 |
| `Ca^[2+]` | metal_25 | 1-Oxa-4,7,10-triazacyclododecane-4,10-d… | ligand_6082 | H2L | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_2804 | O=C(O)CN1CCNCCN(CC(=O)O)CCOCC1 |
| `Ca^[2+]` | metal_25 | 1-Oxa-4,7,10-triazacyclododecane-4,7,10… | ligand_6084 | H3L | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_2829 | O=C(O)CN1CCOCCN(CC(=O)O)CCN(CC(=O)O)CC1 |
| `Ca^[2+]` | metal_25 | 1-Oxa-4,7,11-triazacyclotridecane-4,7,1… | ligand_6085 | H3L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_2845 | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCOCC1 |
| `Ca^[2+]` | metal_25 | 1-Oxa-4,7-diazacyclononane-N,N'-diaceti… | ligand_6064 | H2L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_2595 | O=C(O)CN1CCOCCN(CC(=O)O)CC1 |
| `Ca^[2+]` | metal_25 | 1-Oxa-4,8,12-triazacyclotetradecane-4,1… | ligand_6083 | H2L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_2816 | O=C(O)CN1CCCNCCCN(CC(=O)O)CCOCC1 |
| `Ca^[2+]` | metal_25 | 1-Oxa-4,8,12-triazacyclotetradecane-4,8… | ligand_6086 | H3L | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_2855 | O=C(O)CN1CCCN(CC(=O)O)CCOCCN(CC(=O)O)CCC1 |
| `Ca^[2+]` | metal_25 | 1-Thia-4,7-diazacyclononane-N,N'-diacet… | ligand_6065 | H2L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_2607 | O=C(O)CN1CCSCCN(CC(=O)O)CC1 |
| `Ca^[2+]` | metal_25 | 13,16,21,24-Tetramethyl-4,7-dioxa-1,10,… | ligand_7655 | L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_179 | CN1CCN(C)CCN2CCOCCOCCN(CC1)CCN(C)CCN(C)CC2 |
| `Ca^[2+]` | metal_25 | 2-Hydroxy-1,3-propylenediiminodibutaned… | ligand_6002 | H4L | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_2141 | O=C(O)CC(NCC(O)CNC(CC(=O)O)C(=O)O)C(=O)O |
| `Ca^[2+]` | metal_25 | 2-Hydroxy-1,3-propylenediiminodipropane… | ligand_6001 | H4L | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_2133 | O=C(O)C(NCC(O)CNC(C(=O)O)C(=O)O)C(=O)O |
| `Ca^[2+]` | metal_25 | 2-Indolecarboxylic acid | ligand_5932 | HL | 16.5~31.5 | 0.775~1.225 | 1 | 1 | ref_eq_net_1551 | O=C(O)c1cc2ccccc2[nH]1 |
| `Ca^[2+]` | metal_25 | 5-Thia-2,8-diazanonane-N,N'-diacetic ac… | ligand_6031 | H2L | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_2364 | CN(CCSCCN(C)CC(=O)O)CC(=O)O |
| `Ca^[2+]` | metal_25 | 6,11-Dioxo-1,4,7,10-tetraazacyclododeca… | ligand_6073 | H2L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_2752 | O=C(O)CN1CCN(CC(=O)O)CC(=O)NCCNC(=O)C1 |
| `Ca^[2+]` | metal_25 | 6,12-Dioxo-1,4,7,11-tetraazacyclotridec… | ligand_6074 | H2L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_2760 | O=C(O)CN1CCN(CC(=O)O)CC(=O)NCCCNC(=O)C1 |
| `Ca^[2+]` | metal_25 | 9,14-Dioxo-1,4,7,10,13-pentaazacyclopen… | ligand_6089 | H3L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_2897 | O=C(O)CN1CCN(CC(=O)O)CC(=O)NCCNC(=O)CN(CC(=O)O)CC1 |
| `Ca^[2+]` | metal_25 | 9,15-Dioxo-1,4,7,10,14-pentaazacyclohex… | ligand_6090 | H3L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_2919 | O=C(O)CN1CCN(CC(=O)O)CC(=O)NCCCNC(=O)CN(CC(=O)O)CC1 |
| `Ca^[2+]` | metal_25 | 9,16-Dioxo-1,4,7,10,15-pentaazacyclohep… | ligand_6091 | H3L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_2928 | O=C(O)CN1CCN(CC(=O)O)CC(=O)NCCCCNC(=O)CN(CC(=O)O)CC1 |
| `Ca^[2+]` | metal_25 | Aminoacetic acid (Glycine) | ligand_5760 | HL | 15~41 | -0.15~3.15 | 6 | 2 | ref_eq_net_24 | NCC(=O)O |
| `Ca^[2+]` | metal_25 | Aminopropanedioic acid (Aminomalonic ac… | ligand_5801 | H2L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_546 | NC(C(=O)O)C(=O)O |
| `Ca^[2+]` | metal_25 | DL-1,3-Thiazolidine-4-carboxylic acid (… | ligand_5942 | HL | 28.5~43.5 | -0.075~0.375 | 1 | 1 | ref_eq_net_1626 | O=C(O)C1CSCN1 |
| `Ca^[2+]` | metal_25 | DL-1-Ethylethylenedinitrilotetraacetic … | ligand_6051 | H2L | 28.5~43.5 | -0.075~0.375 | 1 | 1 | ref_eq_net_2512 | CCC(CN(CC(N)=O)CC(=O)O)N(CC(N)=O)CC(=O)O |
| `Ca^[2+]` | metal_25 | DL-1-Methylethylenedinitrilotetraacetic… | ligand_6050 | H2L | 28.5~43.5 | -0.075~0.375 | 1 | 3 | ref_eq_net_2502 | CC(CN(CC(N)=O)CC(=O)O)N(CC(N)=O)CC(=O)O |
| `Ca^[2+]` | metal_25 | DL-2,3-Diaminopropanoic-N,N'-dipropaned… | ligand_5993 | H4L | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_2048 | O=C(O)C(CNC(C(=O)O)C(=O)O)NC(C(=O)O)C(=O)O |
| `Ca^[2+]` | metal_25 | DL-2-Amino-3-(5-hydroxo-4-oxo-1,4-dihyd… | ligand_5912 | HL | 28.5~43.5 | -0.075~0.375 | 1 | 4 | ref_eq_net_1438 | NC(Cc1cc(=O)c(O)c[nH]1)C(=O)O |
| `Ca^[2+]` | metal_25 | DL-2-Amino-3-(5-hydroxo-6-oxo-1,6-dihyd… | ligand_5913 | HL | 28.5~43.5 | -0.075~0.375 | 1 | 3 | ref_eq_net_1442 | NC(Cc1ccc(O)c(=O)[nH]1)C(=O)O |
| `Ca^[2+]` | metal_25 | DL-N,N-Bis(2-hydroxyethyl)alanine | ligand_6022 | HL | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_2288 | CC(C(=O)O)N(CCO)CCO |
| `Ca^[2+]` | metal_25 | Ethylenediiminobis(3-hydroxy-2-propanoi… | ligand_5999 | H2L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_2109 | O=C(O)C(CO)NCCNC(CO)C(=O)O |
| `Ca^[2+]` | metal_25 | Ethylenediiminobis(4-hydroxy-2-butanoic… | ligand_6000 | H2L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_2121 | O=C(O)C(CCO)NCCNC(CCO)C(=O)O |
| `Ca^[2+]` | metal_25 | Ethylenediiminodi-2-pentanedioic acid (… | ligand_5985 | H4L | 15~30 | -0.05~0.25 | 2 | 2 | ref_eq_net_1925 | O=C(O)CCC(NCCNC(CCC(=O)O)C(=O)O)C(=O)O |
| `Ca^[2+]` | metal_25 | Ethylenediiminodi-2-propanoic acid | ligand_5977 | H2L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_1792 | CC(NCCNC(C)C(=O)O)C(=O)O |
| `Ca^[2+]` | metal_25 | Ethylenediiminodibutanedioic acid (EDDS) | ligand_5984 | H4L | 15~30 | -0.05~0.65 | 3 | 2 | ref_eq_net_1870 | O=C(O)CC(NCCNC(CC(=O)O)C(=O)O)C(=O)O |
| `Ca^[2+]` | metal_25 | Ethylenediiminodipropanedioic acid (EDD… | ligand_5983 | H4L | 15~30 | -0.05~0.25 | 2 | 2 | ref_eq_net_1832 | O=C(O)C(NCCNC(C(=O)O)C(=O)O)C(=O)O |
| `Ca^[2+]` | metal_25 | L-2,5-Diaminopentanoic acid (Ornithine) | ligand_5886 | HL | 16.5~31.5 | 0.775~1.225 | 1 | 1 | ref_eq_net_1221 | NCCC[C@H](N)C(=O)O |
| `Ca^[2+]` | metal_25 | L-2,6-Diaminohexanoic acid (Lysine) | ligand_5887 | HL | 19~30 | -0.15~1.15 | 4 | 2 | ref_eq_net_1245 | NCCCC[C@H](N)C(=O)O |
| `Ca^[2+]` | metal_25 | L-2-Amino-3-(3-hydroxo-4-oxo-1,4-dihydr… | ligand_5911 | HL | 28.5~43.5 | -0.075~0.375 | 1 | 4 | ref_eq_net_1434 | N[C@@H](Cn1ccc(=O)c(O)c1)C(=O)O |
| `Ca^[2+]` | metal_25 | L-2-Amino-3-(4-hydroxy-3,5-diiodophenyl… | ligand_5821 | H2L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_740 | N[C@@H](Cc1cc(I)c(O)c(I)c1)C(=O)O |
| `Ca^[2+]` | metal_25 | L-2-Amino-3-(4-hydroxyphenyl)propanoic … | ligand_5819 | H2L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_727 | N[C@@H](Cc1ccc(O)cc1)C(=O)O |
| `Ca^[2+]` | metal_25 | L-2-Amino-3-(4-imidazolyl)propanoic aci… | ligand_5898 | HL | 20~41 | -0.05~0.3 | 2 | 2 | ref_eq_net_1324 | N[C@@H](Cc1c[nH]cn1)C(=O)O |
| `Ca^[2+]` | metal_25 | L-2-Amino-3-hydroxypropanoic acid (Seri… | ligand_5828 | HL | 19~30 | -0.05~3.15 | 2 | 1 | ref_eq_net_785 | N[C@@H](CO)C(=O)O |
| `Ca^[2+]` | metal_25 | L-2-Amino-3-mercaptopropanoic acid (Cys… | ligand_5856 | H2L | 20~41 | -0.05~0.3 | 2 | 1 | ref_eq_net_1001 | N[C@@H](CS)C(=O)O |
| `Ca^[2+]` | metal_25 | L-2-Amino-3-phosphopropanoic acid (Phos… | ligand_5809 | H3L | 20~41 | -0.05~0.3 | 2 | 3 | ref_eq_net_672 | N[C@@H](COP(=O)(O)O)C(=O)O |
| `Ca^[2+]` | metal_25 | L-2-Amino-5-ureidopentanoic acid (Citru… | ligand_5852 | HL | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_977 | NC(=O)NCCC[C@H](N)C(=O)O |
| `Ca^[2+]` | metal_25 | L-2-Aminopentanedioic acid (Glutamic ac… | ligand_5804 | H2L | 19~41 | -0.15~1.15 | 4 | 2 | ref_eq_net_624 | N[C@@H](CCC(=O)O)C(=O)O |
| `Ca^[2+]` | metal_25 | L-2-Aminopropanoic acid (Alanine) | ligand_5761 | HL | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_148 | C[C@H](N)C(=O)O |
| `Ca^[2+]` | metal_25 | L-Aminobutanedioic acid (Aspartic acid) | ligand_5802 | H2L | 19~41 | -0.15~0.3 | 3 | 2 | ref_eq_net_560 | N[C@@H](CC(=O)O)C(=O)O |
| `Ca^[2+]` | metal_25 | N'''-2-Hydroxypropyl-1,4,7,10-Tetraazac… | ligand_6100 | H3L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_2999 | CC(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 |
| `Ca^[2+]` | metal_25 | N,N"-Bis(2-hydroxybenzyl)diethylenetrin… | ligand_6039 | *** | 20~30 | -0.05~0.25 | 1 | 5 | ref_eq_net_2440 | *** |
| `Ca^[2+]` | metal_25 | N,N'-Bis(2-hydroxybenzyl)ethylenedinitr… | ligand_6037 | H4L | 20~30 | -0.05~0.25 | 1 | 3 | ref_eq_net_2407 | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)Cc1ccccc1O |
| `Ca^[2+]` | metal_25 | N,N'-Bis(2-hydroxyethyl)ethylenedinitri… | ligand_6049 | H4L | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_2496 | O=C(O)C(C(=O)O)N(CCO)CCN(CCO)C(C(=O)O)C(=O)O |
| `Ca^[2+]` | metal_25 | N,N'-Bis(2-hydroxyphenyl)ethylenediimin… | ligand_5994 | H4L | 20~30 | -0.05~0.25 | 1 | 3 | ref_eq_net_2073 | O=C(O)CN(CCN(CC(=O)O)c1ccccc1O)c1ccccc1O |
| `Ca^[2+]` | metal_25 | N,N'-Bis(2-pyridylmethyl)ethylenedinitr… | ligand_6056 | H2L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_2542 | O=C(O)CN(CCN(CC(=O)O)Cc1ccccn1)Cc1ccccn1 |
| `Ca^[2+]` | metal_25 | N,N'-Dimethylethylenedinitrilodiacetic … | ligand_6030 | H2L | 20~30 | -0.05~0.25 | 1 | 3 | ref_eq_net_2350 | CN(CCN(C)CC(=O)O)CC(=O)O |
| `Ca^[2+]` | metal_25 | N,N-Bis(2-hydroxypropyl)glycine | ligand_6023 | HL | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_2309 | CC(O)CN(CC(=O)O)CC(C)O |
| `Ca^[2+]` | metal_25 | N,N-Bis(phosphonomethyl)glycine | ligand_6019 | H5L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_2235 | O=C(O)CN(CP(=O)(O)O)CP(=O)(O)O |
| `Ca^[2+]` | metal_25 | N-(Phosphonomethyl)glycine (Glyphosate) | ligand_5937 | H3L | 19~30 | -0.05~0.65 | 2 | 7 | ref_eq_net_1588 | O=C(O)CNCP(=O)(O)O |
| `Ca^[2+]` | metal_25 | Oxybis(ethyleneiminopropanedioic acid) | ligand_6005 | H4L | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_2171 | O=C(O)C(NCCOCCNC(C(=O)O)C(=O)O)C(=O)O |
| `Ca^[2+]` | metal_25 | cis-1,4-Cyclohexylenediiminodipropanedi… | ligand_5991 | H4L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_2038 | O=C(O)C(N[C@H]1CC[C@@H](NC(C(=O)O)C(=O)O)CC1)C(=O)O |
| `Ca^[2+]` | metal_25 | meso-(1,2-Dimethylethylene)diiminodibut… | ligand_5987 | H4L | 20~30 | -0.05~0.25 | 1 | 3 | ref_eq_net_1978 | CC(NC(CC(=O)O)C(=O)O)C(C)NC(CC(=O)O)C(=O)O |
| `Ca^[2+]` | metal_25 | meso-(1,2-Dimethylethylene)diiminodipro… | ligand_5986 | H4L | 20~30 | -0.05~0.25 | 1 | 3 | ref_eq_net_1971 | C[C@H](NC(C(=O)O)C(=O)O)[C@@H](C)NC(C(=O)O)C(=O)O |
| `Ca^[2+]` | metal_25 | meso-1,2-Dimethylethylenedinitrilotetra… | ligand_6053 | H2L | 28.5~43.5 | -0.075~0.375 | 1 | 1 | ref_eq_net_2529 | CC(C(C)N(CC(N)=O)CC(=O)O)N(CC(N)=O)CC(=O)O |
| `Ca^[2+]` | metal_25 | rac-1,2-Dimethylethylenedinitrilotetraa… | ligand_6052 | H2L | 28.5~43.5 | -0.075~0.375 | 1 | 1 | ref_eq_net_2522 | CC(C(C)N(CC(N)=O)CC(=O)O)N(CC(N)=O)CC(=O)O |
| `Ca^[2+]` | metal_25 | trans-1,4-Cyclohexylenediiminodipropane… | ligand_5992 | H4L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_2043 | O=C(O)C(N[C@H]1CC[C@H](NC(C(=O)O)C(=O)O)CC1)C(=O)O |

### Global max-node network: `Ca^[2+]` + N-(Phosphonomethyl)glycine (Glyphosate)
network_id: ref_eq_net_1588 | metal_id: metal_25 | ligand_id: ligand_5937 | ligand_def_HxL: H3L | nodes: 7

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_298 | ``[MHL(s)] <=> [M] + [HL]`` | logK | -5.3 |
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 3.29 |
| beta_def_502 | ``[M]^2 + [L] <=> [M2L]`` | logK | 4.32 |
| beta_def_739 | ``[MHL] + [H] <=> [MH2L]`` | logK | 4.5 |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` | logK | 5.87 |
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` | logK | 8.3 |
| beta_def_792 | ``[ML2] + [H] <=> [MHL2]`` | logK | 8.74 |

---

### Step 17: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_name LIKE 'Cu%')",
  "order_by": "c.ligand_name ASC",
  "limit": 100
}
```

[summary]
## search_networks — 267 row(s)

> **Reference equilibrium networks (compact)** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### Beta-definition legend
| beta_def | equation |
|----------|----------|
| beta_def_800 | ``[MHL] + [L] <=> [MHL2]`` |
| beta_def_779 | ``[M] + [HL] <=> [MHL]`` |
| beta_def_194 | ``[M] + [HL]^2 <=> [M(HL)2]`` |
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` |
| beta_def_839 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` |
| beta_def_739 | ``[MHL] + [H] <=> [MH2L]`` |
| beta_def_751 | ``[MH2L] + [H] <=> [MH3L]`` |
| beta_def_516 | ``[ML] + [M] <=> [M2L]`` |
| beta_def_515 | ``[M2(OH)L] + [H] <=> [M2L] + [H2O]`` |
| beta_def_574 | ``[M2(OH)2L] + [H] <=> [M2(OH)L] + [H2O]`` |
| beta_def_418 | ``[M2(OH)3L] + [H] <=> [M2(OH)2L] + [H2O]`` |
| beta_def_493 | ``[M2L] + [H] <=> [M2HL]`` |
| beta_def_674 | ``[M]^4 + [L]^4 <=> [M4L4]`` |
| beta_def_871 | ``[M(OH)L2] + [H] <=> [ML2] + [H2O]`` |
| beta_def_540 | ``[M]^2 + [L]^3 <=> [M2L3]`` |
| beta_def_649 | ``[M]^3 + [L]^4 <=> [M3L4]`` |
| beta_def_156 | ``[M] + [H2L]^2 <=> [M(H2L)2]`` |
| beta_def_732 | ``[M] + [H2L] <=> [MH2L]`` |
| beta_def_204 | ``[MHL2] + [H] <=> [M(HL)2]`` |
| beta_def_792 | ``[ML2] + [H] <=> [MHL2]`` |
| beta_def_163 | ``[M(H2L)(HL)] + [H] <=> [M(H2L)2]`` |
| beta_def_756 | ``[M(HL)2] + [H] <=> [MH3L2]`` |
| beta_def_476 | ``[M]^2 + [H]^2 + [L]^2 <=> [M2H2L2]`` |
| beta_def_631 | ``[M]^3 + [H]^2 + [L]^3 <=> [M3H2L3]`` |
| beta_def_669 | ``[M]^4 + [H]^2 + [L]^4 <=> [M4H2L4]`` |
| beta_def_519 | ``[M]^2 + [L]^2 <=> [M2L2]`` |
| beta_def_499 | ``[M2L2] + [H] <=> [M2HL2]`` |
| beta_def_984 | ``[M(OH)L2] + [H] <=> [ML2] + [H2O]`` |
| beta_def_249 | ``[M(OH)2L2] + [H] <=> [M(OH)L2] + [H2O]`` |
| beta_def_966 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` |

### Metal-ligand pair summary
| metal | metal_id | ligand | ligand_id | HxL | T_range | I_range | net_count | max_nodes | max_net_id | ligand_SMILES |
|-------|----------|--------|-----------|-----|---------|---------|-----------|----------|------------|---------------|
| `Cu^[2+]` | metal_41 | (3-Aminopropyl)malonic acid | ligand_5808 | H2L | 20~30 | -0.05~0.25 | 1 | 3 | ref_eq_net_660 | NCCCC(C(=O)O)C(=O)O |
| `Cu^[2+]` | metal_41 | 1-Aminocycloheptanecarboxylic acid | ligand_5775 | HL | 20~30 | -0.05~0.25 | 1 | 3 | ref_eq_net_379 | NC1(C(=O)O)CCCCCC1 |
| `Cu^[2+]` | metal_41 | 1-Aminocyclohexanecarboxylic acid | ligand_5774 | HL | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_374 | NC1(C(=O)O)CCCCC1 |
| `Cu^[2+]` | metal_41 | 1-Aminocyclopentanecarboxylic acid (Cyc… | ligand_5773 | HL | 20~30 | -0.05~0.25 | 1 | 3 | ref_eq_net_368 | NC1(C(=O)O)CCCC1 |
| `Cu^[2+]` | metal_41 | 13,16,21,24-Tetramethyl-4,7-dioxa-1,10,… | ligand_7655 | L | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_184 | CN1CCN(C)CCN2CCOCCOCCN(CC1)CCN(C)CCN(C)CC2 |
| `Cu^[2+]` | metal_41 | 2-Amino-2-methylpropanoic acid (2-Amino… | ligand_5769 | HL | 19~30 | -0.15~0.25 | 2 | 2 | ref_eq_net_338 | CC(C)(N)C(=O)O |
| `Cu^[2+]` | metal_41 | 3,6,9,13,16,19-Hexaaza-1,11(2,5)-difura… | ligand_7652 | L | 20~30 | -0.05~0.25 | 1 | 8 | ref_eq_net_165 | c1cc2oc1CNCCNCCNCc1ccc(o1)CNCCNCCNC2 |
| `Cu^[2+]` | metal_41 | 3-Aminopropanoic acid (beta-Alanine) | ligand_5788 | HL | 19~30 | -0.05~5.15 | 4 | 3 | ref_eq_net_466 | NCCC(=O)O |
| `Cu^[2+]` | metal_41 | 4-Aminobutanoic acid | ligand_5797 | HL | 19~30 | -0.05~5.15 | 2 | 1 | ref_eq_net_524 | NCCCC(=O)O |
| `Cu^[2+]` | metal_41 | 6,16-Dioxa-3,9,13,19-tetraaza-1,11(2,6)… | ligand_7653 | L | 20~30 | -0.05~0.25 | 1 | 7 | ref_eq_net_170 | c1cc2nc(c1)CNCCOCCNCc1cccc(n1)CNCCOCCNC2 |
| `Cu^[2+]` | metal_41 | 6,9,19,22-Tetraoxa-3,12,16,25-tetraaza-… | ligand_7654 | L | 20~30 | -0.05~0.25 | 1 | 9 | ref_eq_net_175 | c1cc2nc(c1)CNCCOCCOCCNCc1cccc(n1)CNCCOCCOCCNC2 |
| `Cu^[2+]` | metal_41 | 6-Aminohexanoic acid | ligand_5799 | HL | 16.5~31.5 | 2.775~3.225 | 1 | 2 | ref_eq_net_539 | NCCCCCC(=O)O |
| `Cu^[+]` | metal_42 | 6-Aminohexanoic acid | ligand_5799 | HL | 16.5~31.5 | 2.775~3.225 | 1 | 1 | ref_eq_net_540 | NCCCCCC(=O)O |
| `Cu^[2+]` | metal_41 | Aminoacetic acid (Glycine) | ligand_5760 | HL | 5~45 | -0.15~2.65 | 9 | 2 | ref_eq_net_86 | NCC(=O)O |
| `Cu^[+]` | metal_42 | Aminoacetic acid (Glycine) | ligand_5760 | HL | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_100 | NCC(=O)O |
| `Cu^[2+]` | metal_41 | Aminopropanedioic acid (Aminomalonic ac… | ligand_5801 | H2L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_547 | NC(C(=O)O)C(=O)O |
| `Cu^[2+]` | metal_41 | D-3-Amino-3-carboxypropanohydroxamic ac… | ligand_5816 | H2L | 16.5~31.5 | 0.275~0.725 | 1 | 5 | ref_eq_net_707 | NC(CC(=O)NO)C(=O)O |
| `Cu^[2+]` | metal_41 | D-allo-2-Amino-3-methylpentanoic acid (… | ligand_5768 | HL | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_326 | CC[C@H](C)[C@@H](N)C(=O)O |
| `Cu^[2+]` | metal_41 | DL-2-Amino-2-(3,4-dihydroxyphenyl)aceti… | ligand_5825 | H3L | 16.5~31.5 | 0.775~1.225 | 1 | 2 | ref_eq_net_746 | NC(C(=O)O)c1ccc(O)c(O)c1 |
| `Cu^[2+]` | metal_41 | DL-2-Amino-2-methylpentanedioic acid (2… | ligand_5805 | H2L | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_653 | C[C@](N)(CCC(=O)O)C(=O)O |
| `Cu^[2+]` | metal_41 | DL-2-Amino-3-(2-hydroxyphenyl)propanoic… | ligand_5817 | H2L | 20~30 | -0.05~0.25 | 1 | 4 | ref_eq_net_713 | NC(Cc1ccccc1O)C(=O)O |
| `Cu^[2+]` | metal_41 | DL-2-Amino-3-(3-hydroxyphenyl)propanoic… | ligand_5818 | H2L | 20~30 | -0.05~0.25 | 1 | 4 | ref_eq_net_720 | N[C@@H](Cc1cccc(O)c1)C(=O)O |
| `Cu^[2+]` | metal_41 | DL-2-Amino-3-methylbutanedioic acid (3-… | ligand_5803 | H2L | 16.5~31.5 | 0.275~0.725 | 1 | 3 | ref_eq_net_614 | CC(C(=O)O)[C@H](N)C(=O)O |
| `Cu^[2+]` | metal_41 | DL-2-Amino-3-phosphonopropanoic acid | ligand_5813 | H4L | 20~30 | -0.05~0.25 | 1 | 5 | ref_eq_net_689 | NC(CP(=O)(O)O)C(=O)O |
| `Cu^[2+]` | metal_41 | DL-2-Amino-4-pentenoic acid | ligand_5770 | HL | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_346 | C=CCC(N)C(=O)O |
| `Cu^[2+]` | metal_41 | DL-2-Amino-4-phosphonobutanoic acid | ligand_5814 | H4L | 20~30 | -0.05~0.25 | 1 | 4 | ref_eq_net_697 | NC(CCP(=O)(O)O)C(=O)O |
| `Cu^[2+]` | metal_41 | DL-2-Amino-4-sulfobutanoic acid (Homocy… | ligand_5787 | H2L | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_443 | N[C@@H](CCS(=O)(=O)O)C(=O)O |
| `Cu^[2+]` | metal_41 | DL-2-Amino-5-hexenoic acid | ligand_5771 | HL | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_354 | C=CCCC(N)C(=O)O |
| `Cu^[2+]` | metal_41 | DL-2-Amino-6-heptenoic acid | ligand_5772 | HL | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_361 | C=CCCCC(N)C(=O)O |
| `Cu^[2+]` | metal_41 | DL-2-Aminobutanoic acid | ligand_5762 | HL | 19~30 | -0.05~5.15 | 2 | 3 | ref_eq_net_238 | CCC(N)C(=O)O |
| `Cu^[2+]` | metal_41 | DL-2-Aminohexanoic acid (Norleucine) | ligand_5764 | HL | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_258 | CCCC[C@H](N)C(=O)O |
| `Cu^[2+]` | metal_41 | DL-2-Aminopentanoic acid (Norvaline) | ligand_5763 | HL | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_248 | CCC[C@H](N)C(=O)O |
| `Cu^[2+]` | metal_41 | DL-3-Amino-2-phosphonopropanoic acid | ligand_5815 | H4L | 20~30 | -0.05~0.25 | 1 | 4 | ref_eq_net_702 | NCC(C(=O)O)P(=O)(O)O |
| `Cu^[2+]` | metal_41 | DL-3-Aminobutanoic acid | ligand_5789 | HL | 19~30 | -0.05~5.15 | 2 | 3 | ref_eq_net_484 | CC(N)CC(=O)O |
| `Cu^[2+]` | metal_41 | DL-Amino-4-sulfophenylacetic acid (4-Su… | ligand_5786 | H2L | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_440 | NC(C(=O)O)c1ccc(S(=O)(=O)O)cc1 |
| `Cu^[2+]` | metal_41 | DL-Aminophenylacetic acid (Phenylglycin… | ligand_5776 | HL | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_385 | NC(C(=O)O)c1ccccc1 |
| `Cu^[2+]` | metal_41 | L-2-Amino-2-methyl-3-(3,4-dihydroxyphen… | ligand_5827 | H3L | 20~30 | -0.05~0.25 | 1 | 10 | ref_eq_net_772 | CC(N)(Cc1ccc(O)c(O)c1)C(=O)O |
| `Cu^[2+]` | metal_41 | L-2-Amino-2-methyl-3-(4-hydroxyphenyl)p… | ligand_5820 | H2L | 20~30 | -0.05~0.25 | 1 | 4 | ref_eq_net_738 | CC(N)(Cc1ccc(O)cc1)C(=O)O |
| `Cu^[2+]` | metal_41 | L-2-Amino-3-(3,4-dihydroxyphenyl)propan… | ligand_5826 | H3L | 15~30 | -0.05~1.15 | 4 | 6 | ref_eq_net_757 | NC(Cc1ccc(O)c(O)c1)C(=O)O |
| `Cu^[2+]` | metal_41 | L-2-Amino-3-(3-amino-4-hydroxyphenyl)pr… | ligand_5824 | H2L | 20~30 | -0.05~0.25 | 1 | 5 | ref_eq_net_744 | Nc1cc(C[C@H](N)C(=O)O)ccc1O |
| `Cu^[2+]` | metal_41 | L-2-Amino-3-(4-hydroxyphenyl)propanoic … | ligand_5819 | H2L | 19~30 | -0.05~0.65 | 2 | 5 | ref_eq_net_731 | N[C@@H](Cc1ccc(O)cc1)C(=O)O |
| `Cu^[2+]` | metal_41 | L-2-Amino-3-hydroxypropanoic acid (Seri… | ligand_5828 | HL | 19~30 | -0.05~1.15 | 3 | 4 | ref_eq_net_802 | N[C@@H](CO)C(=O)O |
| `Cu^[2+]` | metal_41 | L-2-Amino-3-methylbutanoic acid (Valine) | ligand_5765 | HL | 19~41 | -0.05~0.65 | 3 | 4 | ref_eq_net_278 | CC(C)[C@H](N)C(=O)O |
| `Cu^[2+]` | metal_41 | L-2-Amino-3-methylpentanoic acid (Isole… | ligand_5767 | HL | 20~41 | -0.05~0.3 | 2 | 3 | ref_eq_net_319 | CC[C@H](C)[C@H](N)C(=O)O |
| `Cu^[2+]` | metal_41 | L-2-Amino-3-phenylpropanoic acid (Pheny… | ligand_5777 | HL | 5~45 | -0.15~3.15 | 7 | 3 | ref_eq_net_406 | N[C@@H](Cc1ccccc1)C(=O)O |
| `Cu^[2+]` | metal_41 | L-2-Amino-3-phosphopropanoic acid (Phos… | ligand_5809 | H3L | 19~30 | -0.05~1.15 | 2 | 3 | ref_eq_net_676 | N[C@@H](COP(=O)(O)O)C(=O)O |
| `Cu^[2+]` | metal_41 | L-2-Amino-4-methylpentanoic acid (Leuci… | ligand_5766 | HL | 20~41 | -0.05~0.3 | 2 | 4 | ref_eq_net_303 | CC(C)C[C@H](N)C(=O)O |
| `Cu^[2+]` | metal_41 | L-2-Aminopentanedioic acid (Glutamic ac… | ligand_5804 | H2L | 20~41 | -0.05~0.3 | 2 | 3 | ref_eq_net_638 | N[C@@H](CCC(=O)O)C(=O)O |
| `Cu^[2+]` | metal_41 | L-2-Aminopropanoic acid (Alanine) | ligand_5761 | HL | 19~41 | -0.15~5.15 | 7 | 3 | ref_eq_net_201 | C[C@H](N)C(=O)O |
| `Cu^[+]` | metal_42 | L-2-Aminopropanoic acid (Alanine) | ligand_5761 | HL | 16.5~31.5 | 0.275~0.725 | 1 | 1 | ref_eq_net_208 | C[C@H](N)C(=O)O |
| `Cu^[2+]` | metal_41 | L-Aminobutanedioic acid (Aspartic acid) | ligand_5802 | H2L | 19~41 | -0.05~2.15 | 5 | 3 | ref_eq_net_595 | N[C@@H](CC(=O)O)C(=O)O |
| `Cu^[2+]` | metal_41 | cis-2-Amino-4-cyclohexene-1-carboxylic … | ligand_5794 | HL | 16.5~31.5 | 0.275~0.725 | 1 | 1 | ref_eq_net_504 | N[C@H]1CC=CC[C@H]1C(=O)O |
| `Cu^[2+]` | metal_41 | cis-2-Aminocyclohexane-1-carboxylic acid | ligand_5792 | HL | 16.5~31.5 | 0.275~0.725 | 1 | 1 | ref_eq_net_494 | N[C@H]1CCCC[C@H]1C(=O)O |
| `Cu^[2+]` | metal_41 | cis-2-Aminocyclopentane-1-carboxylic ac… | ligand_5790 | HL | 16.5~31.5 | 0.275~0.725 | 1 | 1 | ref_eq_net_487 | N[C@H]1CCC[C@H]1C(=O)O |
| `Cu^[2+]` | metal_41 | trans-2-Amino-4-cyclohexene-1-carboxyli… | ligand_5795 | HL | 16.5~31.5 | 0.275~0.725 | 1 | 1 | ref_eq_net_509 | N[C@@H]1CC=CC[C@H]1C(=O)O |
| `Cu^[2+]` | metal_41 | trans-2-Aminocyclohexane-1-carboxylic a… | ligand_5793 | HL | 16.5~31.5 | 0.275~0.725 | 1 | 1 | ref_eq_net_499 | N[C@@H]1CCCC[C@H]1C(=O)O |
| `Cu^[2+]` | metal_41 | trans-2-Aminocyclopentane-1-carboxylic … | ligand_5791 | HL | 16.5~31.5 | 0.275~0.725 | 1 | 1 | ref_eq_net_491 | N[C@@H]1CCC[C@H]1C(=O)O |

### Global max-node network: `Cu^[2+]` + L-2-Amino-2-methyl-3-(3,4-dihydroxyphenyl)propanoic acid (L…
network_id: ref_eq_net_772 | metal_id: metal_41 | ligand_id: ligand_5827 | ligand_def_HxL: H3L | nodes: 10

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_669 | ``[M]^4 + [H]^2 + [L]^4 <=> [M4H2L4]`` | logK | -46.6 |
| beta_def_631 | ``[M]^3 + [H]^2 + [L]^3 <=> [M3H2L3]`` | logK | -36.9 |
| beta_def_476 | ``[M]^2 + [H]^2 + [L]^2 <=> [M2H2L2]`` | logK | -27.29 |
| beta_def_204 | ``[MHL2] + [H] <=> [M(HL)2]`` | logK | -11.1 |
| beta_def_792 | ``[ML2] + [H] <=> [MHL2]`` | logK | -9.9 |
| beta_def_751 | ``[MH2L] + [H] <=> [MH3L]`` | logK | -1.96 |
| beta_def_163 | ``[M(H2L)(HL)] + [H] <=> [M(H2L)2]`` | logK | 5.77 |
| beta_def_732 | ``[M] + [H2L] <=> [MH2L]`` | logK | 7.63 |
| beta_def_756 | ``[M(HL)2] + [H] <=> [MH3L2]`` | logK | 8.74 |
| beta_def_156 | ``[M] + [H2L]^2 <=> [M(H2L)2]`` | logK | 14.04 |

---

### Step 18: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_name LIKE 'Ca%' AND c.ligand_id IN (ligand_5760, ligand_5761, ligand_5764, ligand_5765, ligand_5766, ligand_5767, ligand_5768, ligand_5769, ligand_5777, ligand_5788, ligand_5799, ligand_5802, ligand_5804, ligand_5809, ligand_5813, ligand_5814, ligand_5815, ligand_5828))",
  "order_by": "c.ligand_name ASC",
  "limit": 100
}
```

[summary]
## search_networks — 29 row(s)

> **Reference equilibrium networks (compact)** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### Beta-definition legend
| beta_def | equation |
|----------|----------|
| beta_def_779 | ``[M] + [HL] <=> [MHL]`` |
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` |
| beta_def_739 | ``[MHL] + [H] <=> [MH2L]`` |

### Metal-ligand pair summary
| metal | metal_id | ligand | ligand_id | HxL | T_range | I_range | net_count | max_nodes | ligand_SMILES |
|-------|----------|--------|-----------|-----|---------|---------|-----------|----------|---------------|
| `Ca^[2+]` | metal_25 | Aminoacetic acid (Glycine) | ligand_5760 | HL | 15~41 | -0.15~3.15 | 6 | 2 | NCC(=O)O |
| `Ca^[2+]` | metal_25 | L-2-Amino-3-hydroxypropanoic acid (Seri… | ligand_5828 | HL | 19~30 | -0.05~3.15 | 2 | 1 | N[C@@H](CO)C(=O)O |
| `Ca^[2+]` | metal_25 | L-2-Amino-3-phosphopropanoic acid (Phos… | ligand_5809 | H3L | 20~41 | -0.05~0.3 | 2 | 3 | N[C@@H](COP(=O)(O)O)C(=O)O |
| `Ca^[2+]` | metal_25 | L-2-Aminopentanedioic acid (Glutamic ac… | ligand_5804 | H2L | 19~41 | -0.15~1.15 | 4 | 2 | N[C@@H](CCC(=O)O)C(=O)O |
| `Ca^[2+]` | metal_25 | L-2-Aminopropanoic acid (Alanine) | ligand_5761 | HL | 20~30 | -0.05~0.25 | 1 | 2 | C[C@H](N)C(=O)O |
| `Ca^[2+]` | metal_25 | L-Aminobutanedioic acid (Aspartic acid) | ligand_5802 | H2L | 19~41 | -0.15~0.3 | 3 | 2 | N[C@@H](CC(=O)O)C(=O)O |

### Max-node network per pair
| metal | metal_id | ligand | ligand_id | max_net_id | max_nodes | max_edge_counts | max_T_range | max_I_range | max_vlm_counts | max_beta_def_ids | max_type | max_values |
|-------|----------|--------|----------|------------|-----------|------------------|-------------|-------------|----------------|------------------|----------|------------|
| `Ca^[2+]` | metal_25 | Aminoacetic acid (Glycine) | ligand_5760 | ref_eq_net_24 | 2 | 1 | 20~30 | -0.05~0.25 | 2 | beta_def_779; beta_def_812 | logK | 0.3~1.09 |
| `Ca^[2+]` | metal_25 | L-2-Amino-3-hydroxypropanoic acid (Seri… | ligand_5828 | ref_eq_net_785 | 1 | 0 | 20~30 | -0.05~0.25 | 1 | beta_def_812 | logK | 1.43 |
| `Ca^[2+]` | metal_25 | L-2-Amino-3-phosphopropanoic acid (Phos… | ligand_5809 | ref_eq_net_672 | 3 | 2 | 31~41 | 0~0.3 | 3 | beta_def_812; beta_def_739; beta_def_788 | logK | 2.23~9.1 |
| `Ca^[2+]` | metal_25 | L-2-Aminopentanedioic acid (Glutamic ac… | ligand_5804 | ref_eq_net_624 | 2 | 1 | 20~30 | -0.05~0.25 | 2 | beta_def_779; beta_def_812 | logK | -1.17~1.43 |
| `Ca^[2+]` | metal_25 | L-2-Aminopropanoic acid (Alanine) | ligand_5761 | ref_eq_net_148 | 2 | 1 | 20~30 | -0.05~0.25 | 2 | beta_def_779; beta_def_812 | logK | 0.35~1.3 |
| `Ca^[2+]` | metal_25 | L-Aminobutanedioic acid (Aspartic acid) | ligand_5802 | ref_eq_net_560 | 2 | 1 | 20~30 | -0.05~0.25 | 2 | beta_def_779; beta_def_812 | logK | -1.1~1.7 |

### Global max-node network: `Ca^[2+]` + L-2-Amino-3-phosphopropanoic acid (Phosphoserine)
network_id: ref_eq_net_672 | metal_id: metal_25 | ligand_id: ligand_5809 | ligand_def_HxL: H3L | nodes: 3

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 2.23 |
| beta_def_739 | ``[MHL] + [H] <=> [MH2L]`` | logK | 5.5 |
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` | logK | 9.1 |

---

### Step 19: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_name LIKE 'Cu%' AND c.ligand_id IN (ligand_5760, ligand_5761, ligand_5764, ligand_5765, ligand_5766, ligand_5767, ligand_5768, ligand_5769, ligand_5777, ligand_5788, ligand_5799, ligand_5802, ligand_5804, ligand_5809, ligand_5813, ligand_5814, ligand_5815, ligand_5828))",
  "order_by": "c.ligand_name ASC",
  "limit": 100
}
```

[summary]
## search_networks — 143 row(s)

> **Reference equilibrium networks (compact)** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### Beta-definition legend
| beta_def | equation |
|----------|----------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` |
| beta_def_779 | ``[M] + [HL] <=> [MHL]`` |
| beta_def_194 | ``[M] + [HL]^2 <=> [M(HL)2]`` |
| beta_def_674 | ``[M]^4 + [L]^4 <=> [M4L4]`` |
| beta_def_792 | ``[ML2] + [H] <=> [MHL2]`` |
| beta_def_204 | ``[MHL2] + [H] <=> [M(HL)2]`` |
| beta_def_732 | ``[M] + [H2L] <=> [MH2L]`` |
| beta_def_984 | ``[M(OH)L2] + [H] <=> [ML2] + [H2O]`` |
| beta_def_249 | ``[M(OH)2L2] + [H] <=> [M(OH)L2] + [H2O]`` |
| beta_def_966 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` |

### Metal-ligand pair summary
| metal | metal_id | ligand | ligand_id | HxL | T_range | I_range | net_count | max_nodes | max_net_id | ligand_SMILES |
|-------|----------|--------|-----------|-----|---------|---------|-----------|----------|------------|---------------|
| `Cu^[2+]` | metal_41 | 2-Amino-2-methylpropanoic acid (2-Amino… | ligand_5769 | HL | 19~30 | -0.15~0.25 | 2 | 2 | ref_eq_net_338 | CC(C)(N)C(=O)O |
| `Cu^[2+]` | metal_41 | 3-Aminopropanoic acid (beta-Alanine) | ligand_5788 | HL | 19~30 | -0.05~5.15 | 4 | 3 | ref_eq_net_466 | NCCC(=O)O |
| `Cu^[2+]` | metal_41 | 6-Aminohexanoic acid | ligand_5799 | HL | 16.5~31.5 | 2.775~3.225 | 1 | 2 | ref_eq_net_539 | NCCCCCC(=O)O |
| `Cu^[+]` | metal_42 | 6-Aminohexanoic acid | ligand_5799 | HL | 16.5~31.5 | 2.775~3.225 | 1 | 1 | ref_eq_net_540 | NCCCCCC(=O)O |
| `Cu^[2+]` | metal_41 | Aminoacetic acid (Glycine) | ligand_5760 | HL | 5~45 | -0.15~2.65 | 9 | 2 | ref_eq_net_86 | NCC(=O)O |
| `Cu^[+]` | metal_42 | Aminoacetic acid (Glycine) | ligand_5760 | HL | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_100 | NCC(=O)O |
| `Cu^[2+]` | metal_41 | D-allo-2-Amino-3-methylpentanoic acid (… | ligand_5768 | HL | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_326 | CC[C@H](C)[C@@H](N)C(=O)O |
| `Cu^[2+]` | metal_41 | DL-2-Amino-3-phosphonopropanoic acid | ligand_5813 | H4L | 20~30 | -0.05~0.25 | 1 | 5 | ref_eq_net_689 | NC(CP(=O)(O)O)C(=O)O |
| `Cu^[2+]` | metal_41 | DL-2-Amino-4-phosphonobutanoic acid | ligand_5814 | H4L | 20~30 | -0.05~0.25 | 1 | 4 | ref_eq_net_697 | NC(CCP(=O)(O)O)C(=O)O |
| `Cu^[2+]` | metal_41 | DL-2-Aminohexanoic acid (Norleucine) | ligand_5764 | HL | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_258 | CCCC[C@H](N)C(=O)O |
| `Cu^[2+]` | metal_41 | DL-3-Amino-2-phosphonopropanoic acid | ligand_5815 | H4L | 20~30 | -0.05~0.25 | 1 | 4 | ref_eq_net_702 | NCC(C(=O)O)P(=O)(O)O |
| `Cu^[2+]` | metal_41 | L-2-Amino-3-hydroxypropanoic acid (Seri… | ligand_5828 | HL | 19~41 | -0.05~3.15 | 5 | 4 | ref_eq_net_802 | N[C@@H](CO)C(=O)O |
| `Cu^[2+]` | metal_41 | L-2-Amino-3-methylbutanoic acid (Valine) | ligand_5765 | HL | 19~41 | -0.05~0.65 | 3 | 4 | ref_eq_net_278 | CC(C)[C@H](N)C(=O)O |
| `Cu^[2+]` | metal_41 | L-2-Amino-3-methylpentanoic acid (Isole… | ligand_5767 | HL | 20~41 | -0.05~0.3 | 2 | 3 | ref_eq_net_319 | CC[C@H](C)[C@H](N)C(=O)O |
| `Cu^[2+]` | metal_41 | L-2-Amino-3-phenylpropanoic acid (Pheny… | ligand_5777 | HL | 5~45 | -0.15~3.15 | 7 | 3 | ref_eq_net_406 | N[C@@H](Cc1ccccc1)C(=O)O |
| `Cu^[2+]` | metal_41 | L-2-Amino-3-phosphopropanoic acid (Phos… | ligand_5809 | H3L | 19~30 | -0.05~1.15 | 2 | 3 | ref_eq_net_676 | N[C@@H](COP(=O)(O)O)C(=O)O |
| `Cu^[2+]` | metal_41 | L-2-Amino-4-methylpentanoic acid (Leuci… | ligand_5766 | HL | 20~41 | -0.05~0.3 | 2 | 4 | ref_eq_net_303 | CC(C)C[C@H](N)C(=O)O |
| `Cu^[2+]` | metal_41 | L-2-Aminopentanedioic acid (Glutamic ac… | ligand_5804 | H2L | 20~41 | -0.05~0.3 | 2 | 3 | ref_eq_net_638 | N[C@@H](CCC(=O)O)C(=O)O |
| `Cu^[2+]` | metal_41 | L-2-Aminopropanoic acid (Alanine) | ligand_5761 | HL | 19~41 | -0.15~5.15 | 7 | 3 | ref_eq_net_201 | C[C@H](N)C(=O)O |
| `Cu^[+]` | metal_42 | L-2-Aminopropanoic acid (Alanine) | ligand_5761 | HL | 16.5~31.5 | 0.275~0.725 | 1 | 1 | ref_eq_net_208 | C[C@H](N)C(=O)O |
| `Cu^[2+]` | metal_41 | L-Aminobutanedioic acid (Aspartic acid) | ligand_5802 | H2L | 19~41 | -0.05~2.15 | 5 | 3 | ref_eq_net_595 | N[C@@H](CC(=O)O)C(=O)O |

### Global max-node network: `Cu^[2+]` + DL-2-Amino-3-phosphonopropanoic acid
network_id: ref_eq_net_689 | metal_id: metal_41 | ligand_id: ligand_5813 | ligand_def_HxL: H4L | nodes: 5

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` | logK | -15.49 |
| beta_def_792 | ``[ML2] + [H] <=> [MHL2]`` | logK | -6.9 |
| beta_def_204 | ``[MHL2] + [H] <=> [M(HL)2]`` | logK | -6.7 |
| beta_def_779 | ``[M] + [HL] <=> [MHL]`` | logK | 4.72 |
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 9.6 |

---
