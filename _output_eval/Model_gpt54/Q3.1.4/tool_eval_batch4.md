# Q3.1.4 — Tool Results (batch 4)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Fe(II), Fe(III)",
  "limit": 10
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
  "name": "iron(II), iron(III), ferrous, ferric, iron",
  "symbol": "Fe",
  "limit": 20
}
```

[summary]
## search_metals

*(no results)*

---

### Step 5: `get_table_schema`
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

### Step 6: `get_table_schema`
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

### Step 7: `get_table_schema`
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

### Step 8: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT metal_id, metal_name_SRD, symbol_pure, charge FROM metal_card WHERE primary_metal = 'Fe' OR symbol_pure = 'Fe' ORDER BY charge, metal_id"
}
```

[summary]
## execute_srd46_sql - 2 row(s)

| metal_id | metal_name_SRD | symbol_pure | charge |
|----------|----------------|-------------|--------|
| metal_62 | Fe^[2+] | Fe | 2 |
| metal_61 | Fe^[3+] | Fe | 3 |

---

### Step 9: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_name_SRD LIKE '%Fe%' OR c.metal_name_SRD LIKE '%iron%')",
  "order_by": "c.metal_id, c.ligand_id",
  "limit": 2000
}
```

[summary]
## search_stability — 200 row(s)

### logK — 74 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 14 | 8 | 20~25 | 0.1~1 | *** | 4 |
| metal_61 | Fe^[3+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 6 | 3 | 25 | 0.5~3 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_6204 | N-(2-Hydroxyethyl)iminodiac… | H2L | O=C(O)CN(CCO)CC(=O)O | 6 | 5 | 20~25 | 0.1~1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_5937 | N-(Phosphonomethyl)glycine … | H3L | O=C(O)CNCP(=O)(O)O | 5 | 5 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6041 | N,N'-Bis(3-hydroxy-5-phosph… | H6L | Cc1ncc(COP(=O)(O)O)c(CN(CCN(CC(=O)O)Cc2c(COP(=O)(O)O)cnc(C)c2O)CC(=O)O)c1O | 5 | 5 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6047 | N,N''-Bis(3-hydroxy-6-methy… | H5L | Cc1ccc(O)c(CN(CCN(CCN(CC(=O)O)Cc2nc(C)ccc2O)CC(=O)O)CC(=O)O)n1 | 5 | 5 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 5 | 4 | 25 | 0.1~1 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_5777 | L-2-Amino-3-phenylpropanoic… | HL | N[C@@H](Cc1ccccc1)C(=O)O | 4 | 3 | 20~25 | 1~3 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_5938 | (Carboxymethylamino)acetohy… | H2L | O=C(O)CNCC(=O)NO | 4 | 4 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6036 | N,N'-Bis(carboxymethyl)ethy… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)NO)CC(=O)NO | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6039 | N,N"-Bis(2-hydroxybenzyl)di… | *** | *** | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6054 | N,N'-Bis(carboxymethyl)ethy… | H4L | CC(C)N(O)C(=O)CN(CCN(CC(=O)O)CC(=O)N(O)C(C)C)CC(=O)O | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6057 | N,N',N''-Tris(carboxymethyl… | H5L | CC(C)N(O)C(=O)CN(CCN(CCN(CC(=O)O)CC(=O)N(O)C(C)C)CC(=O)O)CC(=O)O | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6113 | 1-Oxa-4,7,10,13-tetraazacyc… | H4L | O=C(O)CN1CCOCCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6123 | 7,24-Dihydroxy-8,23-dioxo-1… | H2L | O=C(O)CN1CCOCCOCCN(CC(=O)O)CCC(=O)N(O)CCOCCOCCN(O)C(=O)CC1 | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6124 | 6,16-Bis(carboxymethyl)-1,1… | *** | *** | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6125 | 7,19-Bis(carboxymethyl)-1,1… | *** | *** | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6203 | N,N-Bis(carboxymethyl)amino… | H3L | O=C(O)CN(CC(=O)O)CC(=O)NO | 4 | 4 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5809 | L-2-Amino-3-phosphopropanoi… | H3L | N[C@@H](COP(=O)(O)O)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5976 | Ethylenediiminodi-3-propano… | H2L | O=C(O)CCNCCNCCC(=O)O | 3 | 3 | 30 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5977 | Ethylenediiminodi-2-propano… | H2L | CC(NCCNC(C)C(=O)O)C(=O)O | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5996 | meso-Ethylenediiminobis[(2-… | H4L | O=C(O)C(Cc1ccccc1O)NCCNC(Cc1ccccc1O)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5997 | rac-Trimethylenebis[2-(2-hy… | *** | *** | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5998 | meso-Trimethylenebis[2-(2-h… | H4L | Cc1cc(C)c(O)c([C@H](NCCCN[C@@H](C(=O)O)c2cc(C)cc(C)c2O)C(=O)O)c1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6019 | N,N-Bis(phosphonomethyl)gly… | H5L | O=C(O)CN(CP(=O)(O)O)CP(=O)(O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6020 | N-(Carboxymethyl)-N-(2-hydr… | H2L | O=C(O)CN(CCO)CC(=O)NO | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6042 | N,N'-Bis(3-hydroxy-5-hydrox… | H4L | Cc1ncc(CO)c(CN(CCN(CC(=O)O)Cc2c(CO)cnc(C)c2O)CC(=O)O)c1O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6044 | N-(2-Hydroxybenzyl)-N'-(3-h… | H4L | Cc1ncc(CO)c(CN(CCN(CC(=O)O)Cc2ccccc2O)CC(=O)O)c1O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6046 | N,N'-Bis(3-hydroxy-6-methyl… | H4L | Cc1ccc(O)c(CN(CCN(CC(=O)O)Cc2nc(C)ccc2O)CC(=O)O)n1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6084 | 1-Oxa-4,7,10-triazacyclodod… | H3L | O=C(O)CN1CCOCCN(CC(=O)O)CCN(CC(=O)O)CC1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6086 | 1-Oxa-4,8,12-triazacyclotet… | H3L | O=C(O)CN1CCCN(CC(=O)O)CCOCCN(CC(=O)O)CCC1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6087 | 1,7-Dioxa-4,10,13-triazacyc… | H3L | O=C(O)CN1CCOCCN(CC(=O)O)CCN(CC(=O)O)CCOCC1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6121 | 3,6,9-Tris(carboxymethyl)-3… | H3L | O=C(O)CN1CCN(CC(=O)O)Cc2cccc(n2)CN(CC(=O)O)CC1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6135 | L-2-(Carboxymethyl)iminodia… | H3L | O=C(O)CNC(CC(=O)O)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6188 | DL-2-(2-Methylthioethyl)nit… | H3L | CSCCC(C(=O)O)N(CC(=O)O)CC(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6197 | N-(2-Hydroxybenzyl)iminodia… | H3L | O=C(O)CN(CC(=O)O)Cc1ccccc1O | 3 | 3 | 25 | 0.1~1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_5761 | L-2-Aminopropanoic acid (Al… | HL | C[C@H](N)C(=O)O | 2 | 2 | 25 | 0.5 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5994 | N,N'-Bis(2-hydroxyphenyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)c1ccccc1O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5995 | rac-Ethylenediiminobis[(2-h… | H4L | O=C(O)C(Cc1ccccc1O)NCCNC(Cc1ccccc1O)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5999 | Ethylenediiminobis(3-hydrox… | H2L | O=C(O)C(CO)NCCNC(CO)C(=O)O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6000 | Ethylenediiminobis(4-hydrox… | H2L | O=C(O)C(CCO)NCCNC(CCO)C(=O)O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6021 | N,N-Bis(2-hydroxyethyl)glyc… | HL | O=C(O)CN(CCO)CCO | 2 | 2 | 20~25 | 0.1~0.5 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_6035 | N,N'-Bis(carboxymethylamino… | H4L | O=C(O)CNC(=O)CN(CCN(CC(=O)O)CC(=O)NCC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6037 | N,N'-Bis(2-hydroxybenzyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)Cc1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6038 | N,N'-Bis(2-hydroxy-5-sulfob… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1cc(S(=O)(=O)O)ccc1O)Cc1cc(S(=O)(=O)O)ccc1O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6048 | N,N'-Bis(2-hydroxyethyl)eth… | H2L | O=C(O)CN(CCO)CCN(CCO)CC(=O)O | 2 | 2 | 30 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6085 | 1-Oxa-4,7,11-triazacyclotri… | H3L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCOCC1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6088 | 1,7,13-Trioxa-4,10,16-triaz… | H3L | O=C(O)CN1CCOCCN(CC(=O)O)CCOCCN(CC(=O)O)CCOCC1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6102 | 1,4,7,10-Tetraazacyclododec… | H4L | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6104 | 1,4,7,10-Tetraazacyclotride… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6109 | 1,4,8,11-Tetraazacyclotetra… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCCN(CC(=O)O)CC1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6120 | 3,11-Bis(carboxymethyl)-7-m… | H2L | CN1CCCN(CC(=O)O)Cc2cccc(n2)CN(CC(=O)O)CCC1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5804 | L-2-Aminopentanedioic acid … | H2L | N[C@@H](CCC(=O)O)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5826 | L-2-Amino-3-(3,4-dihydroxyp… | H3L | NC(Cc1ccc(O)c(O)c1)C(=O)O | 1 | 1 | 25 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5828 | L-2-Amino-3-hydroxypropanoi… | HL | N[C@@H](CO)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5829 | L-2-Amino-3-hydroxybutanoic… | HL | C[C@@H](O)[C@H](N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5843 | L-2-Aminobutanedioic acid 4… | HL | NC(=O)C[C@H](N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5863 | L-2-Amino-4-(methylthio)but… | HL | CSCC[C@H](N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5886 | L-2,5-Diaminopentanoic acid… | HL | NCCC[C@H](N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5907 | L-2-Amino-3-(3-indolyl)prop… | HL | N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5911 | L-2-Amino-3-(3-hydroxo-4-ox… | HL | N[C@@H](Cn1ccc(=O)c(O)c1)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5917 | L-2-Amino-5-guanidopentanoi… | H2L | N=C(N)NCCC[C@H](N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5925 | N-Methylglycine (Sarcosine) | HL | CNCC(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5930 | L-Pyrrolidine-2-carboxylic … | HL | O=C(O)C1CCCN1 | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5941 | L-4-Hydroxypyrrolidine-2-ca… | HL | O=C(O)C1CC(O)CN1 | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5984 | Ethylenediiminodibutanedioi… | H4L | O=C(O)CC(NCCNC(CC(=O)O)C(=O)O)C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6043 | N,N'-Bis(3-hydroxy-5-hydrox… | H4L | Cc1c([O-])c(CN(CCN(CC(=O)O)Cc2c(CO)c[n+](C)c(C)c2[O-])CC(=O)O)c(CO)c[n+]1C | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6045 | N-(2-Hydroxy-3,5-dimethylbe… | H4L | Cc1cc(C)c(O)c(CN(CCN(CC(=O)O)Cc2c(C)c[n+](C)c(C)c2[O-])CC(=O)O)c1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6063 | 1,5-Diazacyclooctane-N,N'-d… | H2L | O=C(O)CN1CCCN(CC(=O)O)CCC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6076 | 1,4,7-Triazacyclononane-N,N… | H3L | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6195 | N-(2-Carboxyethyl)-N-(phosp… | H4L | O=C(O)CCN(CC(=O)O)CP(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6200 | N-(3-Carboxy-2-hydroxy-5-su… | H4L | O=C(O)CN(CC(=O)O)Cc1cc(S(=O)(=O)O)cc(C(=O)O)c1O | 1 | 1 | 25 | 0.1 | *** | 1 |

### ΔH — 1 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 0 |

### ΔS — 1 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |

---

### Step 10: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_61, metal_62))",
  "order_by": "c.metal_id, c.ligand_id",
  "limit": 2000
}
```

[summary]
## search_stability — 200 row(s)

### logK — 74 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 14 | 8 | 20~25 | 0.1~1 | *** | 4 |
| metal_61 | Fe^[3+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 6 | 3 | 25 | 0.5~3 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_6204 | N-(2-Hydroxyethyl)iminodiac… | H2L | O=C(O)CN(CCO)CC(=O)O | 6 | 5 | 20~25 | 0.1~1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_5937 | N-(Phosphonomethyl)glycine … | H3L | O=C(O)CNCP(=O)(O)O | 5 | 5 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6041 | N,N'-Bis(3-hydroxy-5-phosph… | H6L | Cc1ncc(COP(=O)(O)O)c(CN(CCN(CC(=O)O)Cc2c(COP(=O)(O)O)cnc(C)c2O)CC(=O)O)c1O | 5 | 5 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6047 | N,N''-Bis(3-hydroxy-6-methy… | H5L | Cc1ccc(O)c(CN(CCN(CCN(CC(=O)O)Cc2nc(C)ccc2O)CC(=O)O)CC(=O)O)n1 | 5 | 5 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 5 | 4 | 25 | 0.1~1 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_5777 | L-2-Amino-3-phenylpropanoic… | HL | N[C@@H](Cc1ccccc1)C(=O)O | 4 | 3 | 20~25 | 1~3 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_5938 | (Carboxymethylamino)acetohy… | H2L | O=C(O)CNCC(=O)NO | 4 | 4 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6036 | N,N'-Bis(carboxymethyl)ethy… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)NO)CC(=O)NO | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6039 | N,N"-Bis(2-hydroxybenzyl)di… | *** | *** | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6054 | N,N'-Bis(carboxymethyl)ethy… | H4L | CC(C)N(O)C(=O)CN(CCN(CC(=O)O)CC(=O)N(O)C(C)C)CC(=O)O | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6057 | N,N',N''-Tris(carboxymethyl… | H5L | CC(C)N(O)C(=O)CN(CCN(CCN(CC(=O)O)CC(=O)N(O)C(C)C)CC(=O)O)CC(=O)O | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6113 | 1-Oxa-4,7,10,13-tetraazacyc… | H4L | O=C(O)CN1CCOCCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6123 | 7,24-Dihydroxy-8,23-dioxo-1… | H2L | O=C(O)CN1CCOCCOCCN(CC(=O)O)CCC(=O)N(O)CCOCCOCCN(O)C(=O)CC1 | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6124 | 6,16-Bis(carboxymethyl)-1,1… | *** | *** | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6125 | 7,19-Bis(carboxymethyl)-1,1… | *** | *** | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6203 | N,N-Bis(carboxymethyl)amino… | H3L | O=C(O)CN(CC(=O)O)CC(=O)NO | 4 | 4 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5809 | L-2-Amino-3-phosphopropanoi… | H3L | N[C@@H](COP(=O)(O)O)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5976 | Ethylenediiminodi-3-propano… | H2L | O=C(O)CCNCCNCCC(=O)O | 3 | 3 | 30 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5977 | Ethylenediiminodi-2-propano… | H2L | CC(NCCNC(C)C(=O)O)C(=O)O | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5996 | meso-Ethylenediiminobis[(2-… | H4L | O=C(O)C(Cc1ccccc1O)NCCNC(Cc1ccccc1O)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5997 | rac-Trimethylenebis[2-(2-hy… | *** | *** | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5998 | meso-Trimethylenebis[2-(2-h… | H4L | Cc1cc(C)c(O)c([C@H](NCCCN[C@@H](C(=O)O)c2cc(C)cc(C)c2O)C(=O)O)c1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6019 | N,N-Bis(phosphonomethyl)gly… | H5L | O=C(O)CN(CP(=O)(O)O)CP(=O)(O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6020 | N-(Carboxymethyl)-N-(2-hydr… | H2L | O=C(O)CN(CCO)CC(=O)NO | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6042 | N,N'-Bis(3-hydroxy-5-hydrox… | H4L | Cc1ncc(CO)c(CN(CCN(CC(=O)O)Cc2c(CO)cnc(C)c2O)CC(=O)O)c1O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6044 | N-(2-Hydroxybenzyl)-N'-(3-h… | H4L | Cc1ncc(CO)c(CN(CCN(CC(=O)O)Cc2ccccc2O)CC(=O)O)c1O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6046 | N,N'-Bis(3-hydroxy-6-methyl… | H4L | Cc1ccc(O)c(CN(CCN(CC(=O)O)Cc2nc(C)ccc2O)CC(=O)O)n1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6084 | 1-Oxa-4,7,10-triazacyclodod… | H3L | O=C(O)CN1CCOCCN(CC(=O)O)CCN(CC(=O)O)CC1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6086 | 1-Oxa-4,8,12-triazacyclotet… | H3L | O=C(O)CN1CCCN(CC(=O)O)CCOCCN(CC(=O)O)CCC1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6087 | 1,7-Dioxa-4,10,13-triazacyc… | H3L | O=C(O)CN1CCOCCN(CC(=O)O)CCN(CC(=O)O)CCOCC1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6121 | 3,6,9-Tris(carboxymethyl)-3… | H3L | O=C(O)CN1CCN(CC(=O)O)Cc2cccc(n2)CN(CC(=O)O)CC1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6135 | L-2-(Carboxymethyl)iminodia… | H3L | O=C(O)CNC(CC(=O)O)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6188 | DL-2-(2-Methylthioethyl)nit… | H3L | CSCCC(C(=O)O)N(CC(=O)O)CC(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6197 | N-(2-Hydroxybenzyl)iminodia… | H3L | O=C(O)CN(CC(=O)O)Cc1ccccc1O | 3 | 3 | 25 | 0.1~1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_5761 | L-2-Aminopropanoic acid (Al… | HL | C[C@H](N)C(=O)O | 2 | 2 | 25 | 0.5 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5994 | N,N'-Bis(2-hydroxyphenyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)c1ccccc1O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5995 | rac-Ethylenediiminobis[(2-h… | H4L | O=C(O)C(Cc1ccccc1O)NCCNC(Cc1ccccc1O)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5999 | Ethylenediiminobis(3-hydrox… | H2L | O=C(O)C(CO)NCCNC(CO)C(=O)O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6000 | Ethylenediiminobis(4-hydrox… | H2L | O=C(O)C(CCO)NCCNC(CCO)C(=O)O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6021 | N,N-Bis(2-hydroxyethyl)glyc… | HL | O=C(O)CN(CCO)CCO | 2 | 2 | 20~25 | 0.1~0.5 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_6035 | N,N'-Bis(carboxymethylamino… | H4L | O=C(O)CNC(=O)CN(CCN(CC(=O)O)CC(=O)NCC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6037 | N,N'-Bis(2-hydroxybenzyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)Cc1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6038 | N,N'-Bis(2-hydroxy-5-sulfob… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1cc(S(=O)(=O)O)ccc1O)Cc1cc(S(=O)(=O)O)ccc1O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6048 | N,N'-Bis(2-hydroxyethyl)eth… | H2L | O=C(O)CN(CCO)CCN(CCO)CC(=O)O | 2 | 2 | 30 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6085 | 1-Oxa-4,7,11-triazacyclotri… | H3L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCOCC1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6088 | 1,7,13-Trioxa-4,10,16-triaz… | H3L | O=C(O)CN1CCOCCN(CC(=O)O)CCOCCN(CC(=O)O)CCOCC1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6102 | 1,4,7,10-Tetraazacyclododec… | H4L | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6104 | 1,4,7,10-Tetraazacyclotride… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6109 | 1,4,8,11-Tetraazacyclotetra… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCCN(CC(=O)O)CC1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6120 | 3,11-Bis(carboxymethyl)-7-m… | H2L | CN1CCCN(CC(=O)O)Cc2cccc(n2)CN(CC(=O)O)CCC1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5804 | L-2-Aminopentanedioic acid … | H2L | N[C@@H](CCC(=O)O)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5826 | L-2-Amino-3-(3,4-dihydroxyp… | H3L | NC(Cc1ccc(O)c(O)c1)C(=O)O | 1 | 1 | 25 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5828 | L-2-Amino-3-hydroxypropanoi… | HL | N[C@@H](CO)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5829 | L-2-Amino-3-hydroxybutanoic… | HL | C[C@@H](O)[C@H](N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5843 | L-2-Aminobutanedioic acid 4… | HL | NC(=O)C[C@H](N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5863 | L-2-Amino-4-(methylthio)but… | HL | CSCC[C@H](N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5886 | L-2,5-Diaminopentanoic acid… | HL | NCCC[C@H](N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5907 | L-2-Amino-3-(3-indolyl)prop… | HL | N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5911 | L-2-Amino-3-(3-hydroxo-4-ox… | HL | N[C@@H](Cn1ccc(=O)c(O)c1)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5917 | L-2-Amino-5-guanidopentanoi… | H2L | N=C(N)NCCC[C@H](N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5925 | N-Methylglycine (Sarcosine) | HL | CNCC(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5930 | L-Pyrrolidine-2-carboxylic … | HL | O=C(O)C1CCCN1 | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5941 | L-4-Hydroxypyrrolidine-2-ca… | HL | O=C(O)C1CC(O)CN1 | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5984 | Ethylenediiminodibutanedioi… | H4L | O=C(O)CC(NCCNC(CC(=O)O)C(=O)O)C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6043 | N,N'-Bis(3-hydroxy-5-hydrox… | H4L | Cc1c([O-])c(CN(CCN(CC(=O)O)Cc2c(CO)c[n+](C)c(C)c2[O-])CC(=O)O)c(CO)c[n+]1C | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6045 | N-(2-Hydroxy-3,5-dimethylbe… | H4L | Cc1cc(C)c(O)c(CN(CCN(CC(=O)O)Cc2c(C)c[n+](C)c(C)c2[O-])CC(=O)O)c1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6063 | 1,5-Diazacyclooctane-N,N'-d… | H2L | O=C(O)CN1CCCN(CC(=O)O)CCC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6076 | 1,4,7-Triazacyclononane-N,N… | H3L | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6195 | N-(2-Carboxyethyl)-N-(phosp… | H4L | O=C(O)CCN(CC(=O)O)CP(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6200 | N-(3-Carboxy-2-hydroxy-5-su… | H4L | O=C(O)CN(CC(=O)O)Cc1cc(S(=O)(=O)O)cc(C(=O)O)c1O | 1 | 1 | 25 | 0.1 | *** | 1 |

### ΔH — 1 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 0 |

### ΔS — 1 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |

---
