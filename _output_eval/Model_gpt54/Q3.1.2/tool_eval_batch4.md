# Q3.1.2 — Tool Results (batch 4)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "copper(II), nickel(II)",
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
  "name": "histidine, glycine, cysteine, aspartic acid, glutamic acid, proline, alanine, serine",
  "limit": 20
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
  "name": "copper, nickel",
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
  "name": "histidine, glycine, cysteine, aspartic, glutamic, proline, alanine, serine",
  "limit": 50
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 6: `search_metals`
**Args:**
```json
{
  "symbol": "Cu, Ni",
  "limit": 10
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
  "formula": "C2H5NO2, C3H7NO2, C3H7NO2S, C4H7NO4, C5H9NO4, C5H9NO2, C3H7NO3, C6H9N3O2",
  "limit": 50
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 9: `build_system_catalog`
**Args:**
```json
{}
```

[summary]
[CATALOG]
## build_system_catalog

**Error:** Provide at least one of metal_id, ligand_id, or beta_definition_id.

---

### Step 10: `search_stability`
**Args:**
```json
{
  "where": "c.metal_name_SRD LIKE '%copper%' AND c.ligand_class_name LIKE '%amino%acid%'",
  "order_by": "c.ligand_name_SRD ASC",
  "limit": 200
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. You must call 0_plan_search_strategy first (PHASE 2) before using the execution tools.

---

### Step 11: `search_stability`
**Args:**
```json
{
  "where": "c.metal_name_SRD LIKE '%nickel%' AND c.ligand_class_name LIKE '%amino%acid%'",
  "order_by": "c.ligand_name_SRD ASC",
  "limit": 200
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. You must call 0_plan_search_strategy first (PHASE 2) before using the execution tools.

---

### Step 13: `get_table_schema`
**Args:**
```json
{
  "table_name": "ligandmetal_card",
  "database": "equilibrium"
}
```

[summary]
**get_table_schema:** Error - Table 'ligandmetal_card' not found.
Available tables: eq_collection_unassigned, eq_edge, eq_edge_species, eq_export_metadata, eq_map, eq_map_collection, eq_map_stray, eq_network, eq_network_species, eq_node, eq_node_species, sqlite_sequence

---

### Step 14: `get_table_schema`
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

### Step 15: `get_table_schema`
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

### Step 16: `get_table_schema`
**Args:**
```json
{
  "table_name": "ligand_pka_measured",
  "database": "equilibrium"
}
```

[summary]
**get_table_schema:** Error - Table 'ligand_pka_measured' not found.
Available tables: eq_collection_unassigned, eq_edge, eq_edge_species, eq_export_metadata, eq_map, eq_map_collection, eq_map_stray, eq_network, eq_network_species, eq_node, eq_node_species, sqlite_sequence

---

### Step 17: `search_pka_ligands`
**Args:**
```json
{
  "where": "((lc.ligand_name_SRD LIKE '%histidine%' OR lc.ligand_name_SRD LIKE '%glycine%' OR lc.ligand_name_SRD LIKE '%cysteine%' OR lc.ligand_name_SRD LIKE '%aspartic%' OR lc.ligand_name_SRD LIKE '%glutamic%' OR lc.ligand_name_SRD LIKE '%proline%' OR lc.ligand_name_SRD LIKE '%alanine%' OR lc.ligand_name_SRD LIKE '%serine%'))",
  "order_by": "lc.ligand_name_SRD ASC, p.pKa ASC",
  "limit": 200
}
```

[summary]
## search_pka_ligands — 200 row(s)

| ligand_id | ligand_name | HxL_def | formula | smiles | pH_ladder | T°C_range | I(M)_range | similarity_score |
|-----------|-------------|---------|---------|--------|-----------|-----------|------------|------------------|
| ligand_6729 | (4-Aminophenylamino)butanedioic acid (N-(4-Aminophenyl)aspa… | H2L | C10H12N2O4 | Nc1ccc(NC(CC(=O)O)C(=O)O)cc1 | −∞; H4L (M_tot_1); (2.39, vlm_117775); H3L (M_tot_1); (3.08, vlm_117774); H2L (M_tot_1); (4.03, vlm_117773); HL (M_tot_1); (6.36, vlm_117772); L (M_tot_7); +∞ | 25 | 0.5 | *** |
| ligand_6126 | (Carboxymethyl)trimethylammonium (nitrate) (N,N,N,-Trimethy… | HL | C5H12N1O2/+ | C[N+](C)(C)CC(=O)O.O=[N+]([O-])[O-] | −∞; HL (M_tot_1); (-1.7, vlm_104099); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_8968 | 2-(Acetylamino)butanedioic acid (N-Acetylaspartic acid) | H2L | C6H9N1O5 | CC(=O)NC(CC(=O)O)C(=O)O | −∞; H2L (M_tot_1); (3.04, vlm_155335); HL (M_tot_1); (4.49, vlm_155334); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_8969 | 2-(Acetylamino)pentanedioic acid (N-Acetylglutamic acid) | H2L | C7H11N1O5 | CC(=O)NC(CCC(=O)O)C(=O)O | −∞; H2L (M_tot_1); (3.29, vlm_155340); HL (M_tot_1); (4.6, vlm_155339); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_6724 | 2-(Carboxymethylamino)benzoic acid (N-(2-Carboxyphenyl)glyc… | H2L | C9H9N1O4 | O=C(O)CNc1ccccc1C(=O)O | −∞; H2L (M_tot_1); (3.33, vlm_117728); HL (M_tot_1); (4.9, vlm_117727); L (M_tot_6); +∞ | 25 | 0.1 | *** |
| ligand_5959 | 2-(Carboxymethylaminomethyl)azole-4-sulfonic acid (N-(4-Sul… | H2L | C7H10N2O5S1 | O=C(O)CNCc1cc(S(=O)(=O)O)c[nH]1 | −∞; H2L (M_tot_1); (2.25, vlm_100094); HL (M_tot_1); (8.71, vlm_100093); L (M_tot_2); +∞ | 25 | 1 | *** |
| ligand_8458 | 2-Amino-2-(methoxycarboxy)ethyl(dihydrogenphosphate) (O-Pho… | H2L | C3H10N1O6P1 | COC(=O)C(N)COP(=O)(O)O | −∞; H2L (M_tot_1); (5.33, vlm_144212); HL (M_tot_1); (7.83, vlm_144211); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6471 | 2-Methylalanyl-2-methylalanine | HL | C8H16N2O3 | CC(C)(N)C(=O)NC(C)(C)C(=O)O | −∞; H2L (M_tot_1); (3.67, vlm_115368); HL (M_tot_1); (8.26, vlm_115367); L (M_tot_3); +∞ | 25 | 0.1 | *** |
| ligand_6559 | 2-Methylalanyl-2-methylalanyl-2-methylalanine | HL | C12H23N3O4 | CC(C)(N)C(=O)NC(C)(C)C(=O)NC(C)(C)C(=O)O | −∞; H2L (M_tot_1); (3.82, vlm_116228); HL (M_tot_1); (8.11, vlm_116227); L (M_tot_3); +∞ | 25 | 0.1 | *** |
| ligand_6603 | 2-Methylalanyl-2-methylalanyl-2-methylalanyl-2-methylalanine | HL | C16H30N4O5 | CC(C)(N)C(=O)NC(C)(C)C(=O)NC(C)(C)C(=O)NC(C)(C)C(=O)O | −∞; H2L (M_tot_1); (3.8, vlm_116806); HL (M_tot_1); (7.78, vlm_116805); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_6602 | 2-Methylalanyl-2-methylalanyl-2-methylalanylglycine | HL | C14H26N4O5 | CC(C)(N)C(=O)NC(C)(C)C(=O)NC(C)(C)C(=O)NCC(=O)O | −∞; H2L (M_tot_1); (3.46, vlm_116800); HL (M_tot_1); (8.33, vlm_116799); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_8971 | 3-(4-Nitrobenzoylamino)butane-1,3-dicarboxylic acid (N-(4-N… | H2L | C13H10N2O7 | CC(CCC(=O)O)(NC(=O)c1ccc([N+](=O)[O-])cc1)C(=O)O | −∞; H2L (M_tot_1); (3.23, vlm_155346); HL (M_tot_1); (4.57, vlm_155345); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_8970 | 3-(Benzoylamino)butane-1,3-dicarboxylic acid (N-Benzoyl-2-m… | H2L | C13H11N1O5 | CC(CCC(=O)O)(NC(=O)c1ccccc1)C(=O)O | −∞; H2L (M_tot_1); (3.51, vlm_155343); HL (M_tot_1); (4.63, vlm_155342); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_6990 | 3-Aminopropanohydroxamic acid (beta-Alaninehydroxamic acid) | HL | C3H8N2O2 | NCCC(=O)NO | −∞; H2L (M_tot_1); (8.32, vlm_121640); HL (M_tot_4); (9.59, vlm_121638); L (M_tot_4); +∞ | 25 | 0.1 | *** |
| ligand_5788 | 3-Aminopropanoic acid (beta-Alanine) | HL | C3H7N1O2 | NCCC(=O)O | −∞; H2L (M_tot_1); (3.51, vlm_95222); HL (M_tot_3); (10.08, vlm_95204); L (M_tot_11); +∞ | 25 | 0.1 | *** |
| ligand_6941 | 3-Aminopropanoic acid ethyl ester (beta-Alanine ethyl ester) | L | C5H11N1O2 | CCOC(=O)CCN | −∞; HL (M_tot_1); (9.18, vlm_121216); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5760 | Aminoacetic acid (Glycine) | HL | C2H5N1O2 | NCC(=O)O | −∞; H2L (M_tot_1); (2.33, vlm_93627); HL (M_tot_20); (9.57, vlm_93606); L (M_tot_43); +∞ | 25 | 0.1 | *** |
| ligand_6982 | Aminoacetohydroxamic acid (Glycinehydroxamic acid) | HL | C2H6N2O2 | NCC(=O)NO | −∞; H2L (M_tot_1); (7.45, vlm_121429); HL (M_tot_2); (9.18, vlm_121426); L (M_tot_9); +∞ | 25 | 0.1 | *** |
| ligand_6962 | D-4-Amino-1,2-oxazolidin-3-one (D-Cycloserine) | L | C6H6N2O2 | NC1CONC1=O | −∞; H2L (M_tot_1); (4.39, vlm_121319); HL (M_tot_6); (7.35, vlm_121315); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_6542 | D-Alanyl-D-alanyl-D-alanine | HL | C9H17N3O4 | C[C@@H](N)C(=O)N[C@H](C)C(=O)N[C@H](C)C(=O)O | −∞; H2L (M_tot_1); (3.28, vlm_116112); HL (M_tot_1); (7.95, vlm_116111); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6541 | D-Alanyl-L-alanyl-L-alanine | HL | C9H17N3O4 | C[C@H](NC(=O)[C@H](C)NC(=O)[C@@H](C)N)C(=O)O | −∞; H2L (M_tot_1); (3.26, vlm_116110); HL (M_tot_1); (7.95, vlm_116109); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6600 | D-Alanyl-L-alanyl-L-alanyl-L-alanine | HL | C12H22N4O5 | C[C@H](NC(=O)[C@H](C)NC(=O)[C@H](C)NC(=O)[C@@H](C)N)C(=O)O | −∞; H2L (M_tot_1); (3.31, vlm_116792); HL (M_tot_1); (7.83, vlm_116791); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6586 | D-Arginyl-L-lysyl-L-aspartic acid | *** | C16H31N7O6 | *** | −∞; H4L (M_tot_1); (2.76, vlm_116564); H3L (M_tot_1); (4.2, vlm_116563); H2L (M_tot_1); (7.5, vlm_116562); HL (M_tot_2); (10.29, vlm_116561); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6515 | D-Histidyl-L-histidine | HL | C12H16N6O3 | N[C@H](Cc1c[nH]cn1)C(=O)N[C@@H](Cc1c[nH]cn1)C(=O)O | −∞; H4L (M_tot_1); (2.18, vlm_115820); H3L (M_tot_1); (5.32, vlm_115818); H2L (M_tot_1); (6.73, vlm_115816); HL (M_tot_1); (7.82, vlm_115814); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_6555 | D-Leucyl-L-leucylglycine | HL | C14H27N3O4 | CC(C)C[C@@H](N)C(=O)N[C@@H](CC(C)C)C(=O)NCC(=O)O | −∞; H2L (M_tot_1); (3.33, vlm_116206); HL (M_tot_1); (7.87, vlm_116205); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_6522 | D-Methionyl-L-S-methylcysteine | HL | C9H18N2O3S2 | CSCC[C@@H](N)C(=O)N[C@@H](CSC)C(=O)O | −∞; H2L (M_tot_1); (2.72, vlm_115882); HL (M_tot_1); (7.62, vlm_115881); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_6528 | D-Prolyl-L-histidine | HL | C10H18N4O3 | O=C(O)[C@H](Cc1cnc[nH]1)NC(=O)[C@H]1CCCN1 | −∞; HL (M_tot_1); (-9.16, vlm_115947); L (M_tot_2); (-6.77, vlm_115948); HL (M_tot_1); (2.91, vlm_115949); H2L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_8784 | DL-(2,3-Dimercaptopropionyl)glycine | H3L | C5H9N1O3S2 | O=C(O)CNC(=O)C(S)CS | −∞; H3L (M_tot_1); (3.63, vlm_150900); H2L (M_tot_1); (7.63, vlm_150899); HL (M_tot_1); (10.66, vlm_150898); L (M_tot_3); +∞ | 20 | 0.1 | *** |
| ligand_8781 | DL-(2-Mercapto-2-phenylacetyl)glycine | H2L | C10H10N1O3S1 | O=C(O)CNC(=O)C(S)c1ccccc1 | −∞; H2L (M_tot_1); (3.2, vlm_150888); HL (M_tot_1); (7.8, vlm_150887); L (M_tot_1); +∞ | 20 | 0.1 | *** |
| ligand_8779 | DL-(2-Mercapto-3-methylbutanonyl)glycine | H2L | C7H13N1O3S1 | CC(C)C(S)C(=O)NCC(=O)O | −∞; H2L (M_tot_1); (3.77, vlm_150884); HL (M_tot_1); (9.07, vlm_150883); L (M_tot_1); +∞ | 20 | 0.1 | *** |
| ligand_8782 | DL-(2-Mercapto-3-phenylpropionyl)glycine | H2L | C11H12N1O3S1 | O=C(O)CNC(=O)C(S)Cc1ccccc1 | −∞; H2L (M_tot_1); (3.47, vlm_150890); HL (M_tot_1); (8.41, vlm_150889); L (M_tot_1); +∞ | 20 | 0.1 | *** |
| ligand_8783 | DL-(2-Mercaptopropionyl)-L-cysteine | H3L | C6H11N1O3S2 | CC(S)C(=O)N[C@@H](CS)C(=O)O | −∞; H3L (M_tot_1); (3.26, vlm_150893); H2L (M_tot_1); (8.46, vlm_150892); HL (M_tot_1); (10.17, vlm_150891); L (M_tot_2); +∞ | 20 | 0.1 | *** |
| ligand_8776 | DL-(2-Mercaptopropionyl)-beta-alanine | H2L | C6H11N1O3S1 | CC(S)C(=O)NCCC(=O)O | −∞; H2L (M_tot_1); (3.77, vlm_150878); HL (M_tot_1); (8.81, vlm_150877); L (M_tot_1); +∞ | 20 | 0.1 | *** |
| ligand_8775 | DL-(2-Mercaptopropionyl)glycine | H2L | C5H9N1O3S1 | CC(S)C(=O)NCC(=O)O | −∞; H2L (M_tot_1); (3.4, vlm_150847); HL (M_tot_1); (8.37, vlm_150843); L (M_tot_6); +∞ | 25 | 0.1 | *** |
| ligand_8780 | DL-(2-Mercaptopropionyl)phenylglycine | H2L | C11H12N1O3S1 | CC(S)C(=O)NC(C(=O)O)c1ccccc1 | −∞; H2L (M_tot_1); (3.08, vlm_150886); HL (M_tot_1); (8.66, vlm_150885); L (M_tot_1); +∞ | 20 | 0.1 | *** |
| ligand_8778 | DL-(3-Mercaptopropionyl)-beta-alanine | H2L | C6H11N1O3S1 | O=C(O)CCNC(=O)CCS | −∞; H2L (M_tot_1); (3.82, vlm_150882); HL (M_tot_1); (9.69, vlm_150881); L (M_tot_1); +∞ | 20 | 0.1 | *** |
| ligand_8777 | DL-(3-Mercaptopropionyl)glycine | H2L | C5H9N1O3S1 | O=C(O)CNC(=O)CCS | −∞; H2L (M_tot_1); (3.71, vlm_150880); HL (M_tot_1); (9.6, vlm_150879); L (M_tot_1); +∞ | 20 | 0.1 | *** |
| ligand_5942 | DL-1,3-Thiazolidine-4-carboxylic acid (DL-Thiaproline) | HL | C4H7N1O2S1 | O=C(O)C1CSCN1 | −∞; HL (M_tot_1); (-6.11, vlm_99933); L (M_tot_8); (-1.5, vlm_99935); HL (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5805 | DL-2-Amino-2-methylpentanedioic acid (2-Methylglutamic acid) | H2L | C6H11N1O4 | C[C@](N)(CCC(=O)O)C(=O)O | −∞; H2L (M_tot_1); (4.05, vlm_95867); HL (M_tot_1); (9.72, vlm_95866); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_5783 | DL-2-Amino-3-(2-chlorophenyl)propanoic acid (DL-3-(2-Chloro… | HL | C9H10Cl1N1O2 | N[C@@H](Cc1ccccc1Cl)C(=O)O | −∞; H2L (M_tot_1); (2.23, vlm_95183); HL (M_tot_1); (8.94, vlm_95182); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5780 | DL-2-Amino-3-(2-fluorophenyl)propanoic acid (DL-3-(2-Fluoro… | HL | C9H10F1N1O2 | N[C@@H](Cc1ccccc1F)C(=O)O | −∞; H2L (M_tot_1); (2.12, vlm_95166); HL (M_tot_1); (9.01, vlm_95163); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5860 | DL-2-Amino-3-(2-mercaptoimidazo-4-yl)propanoic acid (Thiohi… | H2L | C6H9N3O2S1 | NC(Cc1cnc(S)[nH]1)C(=O)O | −∞; HL (M_tot_1); (-11.77, vlm_97676); L (M_tot_9); (8.59, vlm_97679); HL (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5855 | DL-2-Amino-3-(3,4-dimethoxyphenyl)propanoic acid (3,4-Dimet… | HL | C11H15N1O4 | COc1ccc(C[C@H](N)C(=O)O)cc1OC | −∞; H2L (M_tot_1); (2.37, vlm_97370); HL (M_tot_1); (9.02, vlm_97369); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5784 | DL-2-Amino-3-(3-chlorophenyl)propanoic acid (DL-3-(3-Chloro… | HL | C9H10Cl1N1O2 | N[C@@H](Cc1cccc(Cl)c1)C(=O)O | −∞; H2L (M_tot_1); (2.17, vlm_95185); HL (M_tot_1); (8.91, vlm_95184); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5781 | DL-2-Amino-3-(3-fluorophenyl)propanoic acid (DL-3-(3-Fluoro… | HL | C9H10F1N1O2 | N[C@@H](Cc1cccc(F)c1)C(=O)O | −∞; H2L (M_tot_1); (2.1, vlm_95172); HL (M_tot_1); (8.98, vlm_95169); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5785 | DL-2-Amino-3-(4-chlorophenyl)propanoic acid (DL-3-(4-Chloro… | HL | C9H10Cl1N1O2 | N[C@@H](Cc1ccc(Cl)cc1)C(=O)O | −∞; H2L (M_tot_1); (2.08, vlm_95187); HL (M_tot_1); (8.96, vlm_95186); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5782 | DL-2-Amino-3-(4-fluorophenyl)propanoic acid (DL-3-(4-Fluoro… | HL | C9H10F1N1O2 | N[C@@H](Cc1ccc(F)cc1)C(=O)O | −∞; H2L (M_tot_1); (2.13, vlm_95178); HL (M_tot_1); (9.05, vlm_95175); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5778 | DL-2-Amino-3-chloropropanoic acid (3-Chloroalanine) | HL | C3H6Cl1N1O2 | N[C@@H](CCl)C(=O)O | −∞; H2L (M_tot_1); (2, vlm_95146); HL (M_tot_1); (8.18, vlm_95145); L (M_tot_4); +∞ | 25 | 0.1 | *** |
| ligand_5807 | DL-2-Amino-3-hydroxypentanedioic acid (3-Hydroxyglutamic ac… | H2L | C5H9N1O5 | N[C@H](C(=O)O)C(O)CC(=O)O | −∞; H3L (M_tot_1); (2.09, vlm_95876); H2L (M_tot_1); (4.08, vlm_95875); HL (M_tot_1); (9.06, vlm_95874); L (M_tot_4); +∞ | 25 | 0.1 | *** |
| ligand_6994 | DL-2-Amino-3-hydroxypropanohydroxamic acid (Serinehydroxami… | HL | C3H8N2O3 | N[C@@H](CO)C(=O)NO | −∞; H2L (M_tot_1); (6.8, vlm_121685); HL (M_tot_2); (9.04, vlm_121683); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_11519 | DL-2-Amino-3-methoxypropanoic acid (3-Methoxyalanine) | HL | C4H9N1O3 | COC[C@H](N)C(=O)O | −∞; H2L (M_tot_1); (2.037, vlm_97356); HL (M_tot_1); (9.176, vlm_97351); L (M_tot_1); +∞ | 25 | 0 | *** |
| ligand_5803 | DL-2-Amino-3-methylbutanedioic acid (3-Methylaspartic acid) | H2L | C5H9N1O4 | CC(C(=O)O)[C@H](N)C(=O)O | −∞; H3L (M_tot_1); (1.99, vlm_95735); H2L (M_tot_1); (3.59, vlm_95734); HL (M_tot_2); (9.48, vlm_95733); L (M_tot_2); +∞ | 25 | 0.5 | *** |
| ligand_6989 | DL-2-Amino-3-phenylpropanohydroxamic acid (Phenylalaninehyd… | HL | C9H12N2O2 | N[C@@H](Cc1ccccc1)C(=O)NO | −∞; H2L (M_tot_1); (6.89, vlm_121635); HL (M_tot_1); (9.01, vlm_121634); L (M_tot_2); +∞ | 25 | 0.5 | *** |
| ligand_5859 | DL-2-Amino-4-mercaptobutanoic acid (Homocysteine) | H2L | C4H9N1O2S1 | NC(CCS)C(=O)O | −∞; H3L (M_tot_1); (2.15, vlm_97673); H2L (M_tot_1); (8.57, vlm_97672); HL (M_tot_1); (10.38, vlm_97671); L (M_tot_1); +∞ | 25~30 | 0.1 | *** |
| ligand_8712 | DL-2-Methyl-5-pyrrolidone-2-carboxylic acid (2-Methylpyrogl… | HL | C6H9N1O3 | CC1(C(=O)O)CCC(=O)N1 | −∞; HL (M_tot_1); (3.14, vlm_149991); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_8713 | DL-2-Phenyl-5-pyrrolidone-2-carboxylic acid (2-Phenylpyrogl… | HL | C11H11N1O3 | O=C1CCC(C(=O)O)(c2ccccc2)N1 | −∞; HL (M_tot_1); (2.69, vlm_149992); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5834 | DL-3-Amino-2-hydroxypropanoic acid (Isoserine) | HL | C3H7N1O3 | NCC(O)C(=O)O | −∞; H2L (M_tot_1); (2.66, vlm_96924); HL (M_tot_5); (9.13, vlm_96921); L (M_tot_6); +∞ | 25 | 0.1 | *** |
| ligand_5796 | DL-3-Amino-3-phenylpropanoic acid (Phenyl-beta-Alanine) | HL | C9H11N1O2 | NC(CC(=O)O)c1ccccc1 | −∞; H2L (M_tot_1); (3.4, vlm_95403); HL (M_tot_1); (9, vlm_95402); L (M_tot_1); +∞ | 25 | 0.5 | *** |
| ligand_6926 | DL-Alanine ethyl ester | L | C5H11N1O2 | CCOC(=O)C(C)N | −∞; HL (M_tot_1); (7.91, vlm_121189); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6925 | DL-Alanine methyl ester | L | C4H9N1O2 | COC(=O)C(C)N | −∞; HL (M_tot_1); (7.76, vlm_121186); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6558 | DL-Alanyl-2-methylalanyl-2-methylalanine | HL | C11H21N3O4 | CC(N)C(=O)NC(C)(C)C(=O)NC(C)(C)C(=O)O | −∞; H2L (M_tot_1); (3.95, vlm_116223); HL (M_tot_1); (8.29, vlm_116222); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_5838 | DL-Amino-4-Methoxyphenylacetic acid (4-Methoxyphenylglycine) | HL | C9H11N1O3 | COc1ccc(C(N)C(=O)O)cc1 | −∞; H2L (M_tot_1); (2, vlm_97021); HL (M_tot_1); (9.07, vlm_97020); L (M_tot_6); +∞ | 25 | 0.1 | *** |
| ligand_5786 | DL-Amino-4-sulfophenylacetic acid (4-Sulfophenylglycine) | H2L | C8H9N1O5S1 | NC(C(=O)O)c1ccc(S(=O)(=O)O)cc1 | −∞; H2L (M_tot_1); (-1.8, vlm_95189); HL (M_tot_1); (8.66, vlm_95188); L (M_tot_6); +∞ | 25 | 0.1 | *** |
| ligand_5776 | DL-Aminophenylacetic acid (Phenylglycine) | HL | C8H9N1O2 | NC(C(=O)O)c1ccccc1 | −∞; H2L (M_tot_1); (-1.9, vlm_94963); HL (M_tot_1); (8.92, vlm_94962); L (M_tot_6); +∞ | 25 | 0.1 | *** |
| ligand_6939 | DL-Glutamic acid diethyl ester | L | C9H17N1O4 | CCOC(=O)CCC(N)C(=O)OCC | −∞; HL (M_tot_1); (7.035, vlm_121212); L (M_tot_1); +∞ | 25 | 0 | *** |
| ligand_6938 | DL-Glutamic acid dimethyl ester | L | C7H13N1O4 | COC(=O)CCC(N)C(=O)OC | −∞; HL (M_tot_1); (7.03, vlm_121211); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6022 | DL-N,N-Bis(2-hydroxyethyl)alanine | HL | C7H15N1O4 | CC(C(=O)O)N(CCO)CCO | −∞; H2L (M_tot_1); (-1.7, vlm_101637); HL (M_tot_1); (8.47, vlm_101636); L (M_tot_21); +∞ | 20 | 0.1 | *** |
| ligand_6725 | DL-N-(2-Carboxyphenyl)alanine | H2L | C10H11N1O4 | CC(Nc1ccccc1C(=O)O)C(=O)O | −∞; H2L (M_tot_1); (3.12, vlm_117737); HL (M_tot_1); (5.01, vlm_117736); L (M_tot_3); +∞ | 20 | 0.1 | *** |
| ligand_6936 | DL-Phenylalanine ethyl ester | L | C11H15N1O2 | CCOC(=O)C(N)Cc1ccccc1 | −∞; HL (M_tot_1); (7.12, vlm_121209); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6412 | DL-Phosphoserylglycine (DL-Serylglycine dihydrogenphosphate) | H3L | C5H11N2O7P1 | NC(COP(=O)(O)O)C(=O)NCC(=O)O | −∞; H3L (M_tot_1); (3.16, vlm_114515); H2L (M_tot_1); (5.42, vlm_114514); HL (M_tot_1); (8.01, vlm_114513); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_6896 | DL-Serine methyl ester | L | C4H9N1O3 | COC(=O)C(N)CO | −∞; HL (M_tot_1); (7.07, vlm_120943); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_6924 | Glycine butyl ester | L | C6H13N1O2 | CCCCOC(=O)CN | −∞; HL (M_tot_1); (7.78, vlm_121185); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6953 | Glycine diethylamide | L | C6H14N2O1 | CCN(CC)C(=O)CN | −∞; HL (M_tot_1); (8.45, vlm_121271); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_6923 | Glycine ethyl ester | L | C4H9N1O2 | CCOC(=O)CN | −∞; HL (M_tot_1); (7.69, vlm_121166); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_6952 | Glycine ethylamide | L | C4H10N2O1 | CCNC(=O)CN | −∞; HL (M_tot_1); (8.19, vlm_121264); L (M_tot_2); +∞ | 25 | 0.5 | *** |
| ligand_6922 | Glycine methyl ester | L | C3H7N1O2 | COC(=O)CN | −∞; HL (M_tot_1); (7.66, vlm_121161); L (M_tot_3); +∞ | 25 | 0.1 | *** |
| ligand_6557 | Glycyl-2-methylalanylglycine | HL | C8H15N3O4 | CC(C)(NC(=O)CN)C(=O)NCC(=O)O | −∞; H2L (M_tot_1); (3.33, vlm_116217); HL (M_tot_1); (8.2, vlm_116216); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_6391 | Glycyl-DL-phosphoserine (Glycyl-DL-serine dihydrogenphospha… | H3L | C5H11N2O7P1 | NCC(=O)N[C@@H](COP(=O)(O)O)C(=O)O | −∞; H3L (M_tot_1); (2.91, vlm_114064); H2L (M_tot_1); (6.03, vlm_114063); HL (M_tot_1); (8.42, vlm_114062); L (M_tot_3); +∞ | 25 | 0.1 | *** |
| ligand_6572 | Glycyl-DL-phosphoserylglycine (Glycyl-DL-serylglycine dihyd… | H3L | C7H13N3O8P1 | NCC(=O)NC(COP(=O)(O)O)C(=O)NCC(=O)O | −∞; H3L (M_tot_1); (3.29, vlm_116358); H2L (M_tot_1); (5.77, vlm_116357); HL (M_tot_2); (8.22, vlm_116356); L (M_tot_3); +∞ | 25 | 0.1 | *** |
| ligand_6574 | Glycyl-DL-serylglycine | HL | C7H13N3O5 | NCC(=O)NC(CO)C(=O)NCC(=O)O | −∞; H2L (M_tot_1); (3.23, vlm_116373); HL (M_tot_1); (7.99, vlm_116372); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6398 | Glycyl-L-S-methylcysteine | HL | C6H12N2O3S1 | CSC[C@H](NC(=O)CN)C(=O)O | −∞; H2L (M_tot_1); (2.9, vlm_114225); HL (M_tot_1); (8.12, vlm_114224); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_6375 | Glycyl-L-alanine | HL | C5H10N2O3 | C[C@H](NC(=O)CN)C(=O)O | −∞; H2L (M_tot_1); (3.12, vlm_113683); HL (M_tot_1); (8.15, vlm_113672); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_6537 | Glycyl-L-alanyl-D-alanine | HL | C8H15N3O4 | C[C@H](NC(=O)CN)C(=O)N[C@H](C)C(=O)O | −∞; H2L (M_tot_1); (3.19, vlm_116101); HL (M_tot_1); (8.06, vlm_116100); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6536 | Glycyl-L-alanyl-L-alanine | HL | C8H15N3O4 | C[C@H](NC(=O)[C@H](C)NC(=O)CN)C(=O)O | −∞; H2L (M_tot_1); (3.27, vlm_116099); HL (M_tot_1); (7.99, vlm_116098); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6534 | Glycyl-L-alanylglycine | HL | C7H13N3O4 | C[C@H](NC(=O)CN)C(=O)NCC(=O)O | −∞; H2L (M_tot_1); (3.34, vlm_116081); HL (M_tot_1); (7.96, vlm_116080); L (M_tot_3); +∞ | 25 | 0.1 | *** |
| ligand_6389 | Glycyl-L-aspartic acid | H2L | C6H10N2O5 | NCC(=O)N[C@@H](CC(=O)O)C(=O)O | −∞; H3L (M_tot_1); (2.8, vlm_114008); H2L (M_tot_1); (4.3, vlm_114005); HL (M_tot_1); (8.34, vlm_114002); L (M_tot_4); +∞ | 25 | 0.1 | *** |
| ligand_6397 | Glycyl-L-cysteine | H2L | C5H10N2O3S1 | NCC(=O)N[C@@H](CS)C(=O)O | −∞; H3L (M_tot_1); (2.73, vlm_114214); H2L (M_tot_1); (8.04, vlm_114213); HL (M_tot_1); (9.48, vlm_114212); L (M_tot_4); +∞ | 25 | 0.1 | *** |
| ligand_6390 | Glycyl-L-glutamic acid | H2L | C7H12N2O5 | NCC(=O)N[C@@H](CCC(=O)O)C(=O)O | −∞; H3L (M_tot_1); (2.83, vlm_114043); H2L (M_tot_1); (4.34, vlm_114040); HL (M_tot_1); (8.3, vlm_114037); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_6401 | Glycyl-L-histidine | HL | C8H12N4O3 | NCC(=O)N[C@@H](Cc1c[nH]cn1)C(=O)O | −∞; H3L (M_tot_1); (2.52, vlm_114278); H2L (M_tot_1); (6.7, vlm_114276); HL (M_tot_2); (8.14, vlm_114274); L (M_tot_7); +∞ | 25 | 0.1 | *** |
| ligand_6576 | Glycyl-L-histidylglycine | HL | C10H15N5O4 | NCC(=O)N[C@@H](CC1C=NC=N1)C(=O)NCC(=O)O | −∞; H3L (M_tot_1); (3.1, vlm_116415); H2L (M_tot_1); (6.56, vlm_116409); HL (M_tot_1); (8, vlm_116403); L (M_tot_4); +∞ | 25 | 0.1 | *** |
| ligand_6651 | Glycyl-L-histidylglycyl-L-histidine | *** | C16H23N8O5 | *** | −∞; H4L (M_tot_1); (2.57, vlm_117147); H3L (M_tot_1); (6, vlm_117146); H2L (M_tot_1); (6.95, vlm_117145); HL (M_tot_1); (8, vlm_117144); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_6395 | Glycyl-L-hydroxyproline | HL | C7H12N2O4 | NCC(=O)N1CC(O)C[C@H]1C(=O)O | −∞; H2L (M_tot_1); (2.8, vlm_114170); HL (M_tot_1); (8.37, vlm_114169); L (M_tot_1); +∞ | 25 | 0.5~0.7 | *** |
| ligand_6545 | Glycyl-L-leucylglycine | HL | C10H19N3O4 | CC(C)C[C@H](NC(=O)CN)C(=O)NCC(=O)O | −∞; HL (M_tot_1); (7.95, vlm_116126); L (M_tot_3); +∞ | 25 | 0.1 | *** |
| ligand_6385 | Glycyl-L-phenylalanine | HL | C11H14N2O3 | NCC(=O)N[C@@H](Cc1ccccc1)C(=O)O | −∞; H2L (M_tot_1); (2.99, vlm_113890); HL (M_tot_1); (8.09, vlm_113887); L (M_tot_4); +∞ | 25 | 0.1 | *** |
| ligand_6388 | Glycyl-L-proline | HL | C7H12N2O3 | NCC(=O)N1CCC[C@H]1C(=O)O | −∞; H2L (M_tot_1); (2.82, vlm_113971); HL (M_tot_1); (8.46, vlm_113967); L (M_tot_4); +∞ | 25 | 0.1 | *** |
| ligand_6618 | Glycyl-L-prolyl-D-phenylalanylglycine | HL | C18H24N4O5 | NCC(=O)N1CCC[C@H]1C(=O)N[C@H](Cc1ccccc1)C(=O)NCC(=O)O | −∞; HL (M_tot_1); (8.64, vlm_116893); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_6667 | Glycyl-L-prolyl-L-lysyl-L-prolylglycine | HL | C20H34N6O6 | NCCCC[C@H](NC(=O)[C@@H]1CCCN1C(=O)CN)C(=O)N1CCC[C@H]1C(=O)NCC(=O)O | −∞; H3L (M_tot_1); (3.41, vlm_117262); H2L (M_tot_1); (8.12, vlm_117261); HL (M_tot_2); (10.24, vlm_117260); L (M_tot_2); +∞ | 25 | 0.1 | *** |

---

### Step 18: `search_stability`
**Args:**
```json
{
  "where": "((c.metal_name_SRD LIKE '%Copper(II)%' OR c.metal_name_SRD LIKE '%copper(II)%' OR c.metal_name_SRD LIKE '%Cu(II)%') AND (c.ligand_name_SRD LIKE '%histidine%' OR c.ligand_name_SRD LIKE '%glycine%' OR c.ligand_name_SRD LIKE '%cysteine%' OR c.ligand_name_SRD LIKE '%aspartic%' OR c.ligand_name_SRD LIKE '%glutamic%' OR c.ligand_name_SRD LIKE '%proline%' OR c.ligand_name_SRD LIKE '%alanine%' OR c.ligand_name_SRD LIKE '%serine%'))",
  "order_by": "c.ligand_name_SRD ASC, s.constant_value DESC",
  "limit": 300
}
```

[summary]
## search_stability — 200 row(s)

### logK — 44 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_41 | Cu^[2+] | ligand_5913 | DL-2-Amino-3-(5-hydroxo-6-o… | HL | NC(Cc1ccc(O)c(=O)[nH]1)C(=O)O | 10 | 10 | 37 | 0.15 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5913 | DL-2-Amino-3-(5-hydroxo-6-o… | HL | NC(Cc1ccc(O)c(=O)[nH]1)C(=O)O | 10 | 10 | 37 | 0.15 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 8 | 3 | 25~37 | 0.1~3 | *** | 4 |
| metal_92 | Mg^[2+] | ligand_5912 | DL-2-Amino-3-(5-hydroxo-4-o… | HL | NC(Cc1cc(=O)c(O)c[nH]1)C(=O)O | 7 | 7 | 37 | 0.15 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_5910 | DL-2-Amino-3-(6-oxo-1,6-dih… | HL | NC(Cc1cccc(=O)[nH]1)C(=O)O | 7 | 7 | 37 | 0.15 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5910 | DL-2-Amino-3-(6-oxo-1,6-dih… | HL | NC(Cc1cccc(=O)[nH]1)C(=O)O | 7 | 7 | 37 | 0.15 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5912 | DL-2-Amino-3-(5-hydroxo-4-o… | HL | NC(Cc1cc(=O)c(O)c[nH]1)C(=O)O | 6 | 6 | 37 | 0.15 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 6 | 2 | 25~37 | 0.1~3 | *** | 5 |
| metal_208 | Zn^[2+] | ligand_5906 | L-2-Amino-3-(2,5-diiodo-4-i… | HL | N[C@@H](Cc1nc(I)[nH]c1I)C(=O)O | 5 | 5 | 25 | 0.5 | *** | 1 |
| metal_33 | Co^[2+] | ligand_5906 | L-2-Amino-3-(2,5-diiodo-4-i… | HL | N[C@@H](Cc1nc(I)[nH]c1I)C(=O)O | 5 | 5 | 25 | 0.5 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_5906 | L-2-Amino-3-(2,5-diiodo-4-i… | HL | N[C@@H](Cc1nc(I)[nH]c1I)C(=O)O | 5 | 5 | 25 | 0.5 | *** | 1 |
| metal_33 | Co^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 5 | 2 | 25~37 | 0.1~1 | *** | 4 |
| metal_68 | H^[+] | ligand_5912 | DL-2-Amino-3-(5-hydroxo-4-o… | HL | NC(Cc1cc(=O)c(O)c[nH]1)C(=O)O | 4 | 4 | 37 | 0.15 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_5912 | DL-2-Amino-3-(5-hydroxo-4-o… | HL | NC(Cc1cc(=O)c(O)c[nH]1)C(=O)O | 4 | 4 | 37 | 0.15 | *** | 1 |
| metal_92 | Mg^[2+] | ligand_5913 | DL-2-Amino-3-(5-hydroxo-6-o… | HL | NC(Cc1ccc(O)c(=O)[nH]1)C(=O)O | 4 | 4 | 37 | 0.15 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_5906 | L-2-Amino-3-(2,5-diiodo-4-i… | HL | N[C@@H](Cc1nc(I)[nH]c1I)C(=O)O | 4 | 4 | 25 | 0.5 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_5906 | L-2-Amino-3-(2,5-diiodo-4-i… | HL | N[C@@H](Cc1nc(I)[nH]c1I)C(=O)O | 4 | 4 | 25 | 0.5 | *** | 1 |
| metal_68 | H^[+] | ligand_5906 | L-2-Amino-3-(2,5-diiodo-4-i… | HL | N[C@@H](Cc1nc(I)[nH]c1I)C(=O)O | 4 | 4 | 25 | 0.5 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 4 | 2 | 25~37 | 0.1~1 | *** | 4 |
| metal_68 | H^[+] | ligand_5913 | DL-2-Amino-3-(5-hydroxo-6-o… | HL | NC(Cc1ccc(O)c(=O)[nH]1)C(=O)O | 3 | 3 | 37 | 0.15 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_5913 | DL-2-Amino-3-(5-hydroxo-6-o… | HL | NC(Cc1ccc(O)c(=O)[nH]1)C(=O)O | 3 | 3 | 37 | 0.15 | *** | 1 |
| metal_68 | H^[+] | ligand_5910 | DL-2-Amino-3-(6-oxo-1,6-dih… | HL | NC(Cc1cccc(=O)[nH]1)C(=O)O | 3 | 3 | 37 | 0.15 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_5915 | L-2-Amino-3-(2-pyridyl)prop… | HL | N[C@@H](Cc1ccccn1)C(=O)O | 3 | 2 | 25 | 0.1 | *** | 2 |
| metal_112 | Ni^[2+] | ligand_5915 | L-2-Amino-3-(2-pyridyl)prop… | HL | N[C@@H](Cc1ccccn1)C(=O)O | 3 | 2 | 25 | 0.1 | *** | 2 |
| metal_33 | Co^[2+] | ligand_5915 | L-2-Amino-3-(2-pyridyl)prop… | HL | N[C@@H](Cc1ccccn1)C(=O)O | 3 | 2 | 25 | 0.1 | *** | 2 |
| metal_208 | Zn^[2+] | ligand_5915 | L-2-Amino-3-(2-pyridyl)prop… | HL | N[C@@H](Cc1ccccn1)C(=O)O | 3 | 2 | 25 | 0.1 | *** | 2 |
| metal_112 | Ni^[2+] | ligand_5860 | DL-2-Amino-3-(2-mercaptoimi… | H2L | NC(Cc1cnc(S)[nH]1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5860 | DL-2-Amino-3-(2-mercaptoimi… | H2L | NC(Cc1cnc(S)[nH]1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_5860 | DL-2-Amino-3-(2-mercaptoimi… | H2L | NC(Cc1cnc(S)[nH]1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_5860 | DL-2-Amino-3-(2-mercaptoimi… | H2L | NC(Cc1cnc(S)[nH]1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_5860 | DL-2-Amino-3-(2-mercaptoimi… | H2L | NC(Cc1cnc(S)[nH]1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5860 | DL-2-Amino-3-(2-mercaptoimi… | H2L | NC(Cc1cnc(S)[nH]1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_94 | Mn^[2+] | ligand_5860 | DL-2-Amino-3-(2-mercaptoimi… | H2L | NC(Cc1cnc(S)[nH]1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_5915 | L-2-Amino-3-(2-pyridyl)prop… | HL | N[C@@H](Cc1ccccn1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 2 | 1 | 25 | 0.1~3 | *** | 2 |
| metal_71 | Hg^[2+] | ligand_5860 | DL-2-Amino-3-(2-mercaptoimi… | H2L | NC(Cc1cnc(S)[nH]1)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_5860 | DL-2-Amino-3-(2-mercaptoimi… | H2L | NC(Cc1cnc(S)[nH]1)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_93 | MeHg^[+] | ligand_5947 | DL-[1-Carboxy-2-(2-mercapto… | H2L | C[N+](C)(C)C(Cc1cnc(S)[nH]1)C(=O)O.[Cl-] | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_68 | H^[+] | ligand_5947 | DL-[1-Carboxy-2-(2-mercapto… | H2L | C[N+](C)(C)C(Cc1cnc(S)[nH]1)C(=O)O.[Cl-] | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 1 | 1 | 25 | 3 | *** | 1 |
| metal_2 | Ag^[+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_201 | VO^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_64 | Ga^[3+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 1 | 1 | 25 | 3 | *** | 1 |
| metal_19 | Be^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |

### ΔH — 2 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_5860 | DL-2-Amino-3-(2-mercaptoimi… | H2L | NC(Cc1cnc(S)[nH]1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_5947 | DL-[1-Carboxy-2-(2-mercapto… | H2L | C[N+](C)(C)C(Cc1cnc(S)[nH]1)C(=O)O.[Cl-] | 1 | 1 | 25 | 0.1 | *** | 0 |

### ΔS — 10 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_41 | Cu^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 11 | 7 | 25 | 0.1~3 | *** | 0 |
| metal_68 | H^[+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 11 | 3 | 25 | 0~3 | *** | 0 |
| metal_33 | Co^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 3 | 2 | 25 | 0.1~3 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 3 | 2 | 25 | 0.1~3 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 3 | 2 | 25 | 0.1~3 | *** | 0 |
| metal_68 | H^[+] | ligand_5860 | DL-2-Amino-3-(2-mercaptoimi… | H2L | NC(Cc1cnc(S)[nH]1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 2 | 2 | 25 | 3 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 2 | 2 | 25 | 3 | *** | 0 |
| metal_26 | Cd^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_5947 | DL-[1-Carboxy-2-(2-mercapto… | H2L | C[N+](C)(C)C(Cc1cnc(S)[nH]1)C(=O)O.[Cl-] | 1 | 1 | 25 | 0.1 | *** | 0 |

---

### Step 19: `search_stability`
**Args:**
```json
{
  "where": "((c.metal_name_SRD LIKE '%Nickel(II)%' OR c.metal_name_SRD LIKE '%nickel(II)%' OR c.metal_name_SRD LIKE '%Ni(II)%') AND (c.ligand_name_SRD LIKE '%histidine%' OR c.ligand_name_SRD LIKE '%glycine%' OR c.ligand_name_SRD LIKE '%cysteine%' OR c.ligand_name_SRD LIKE '%aspartic%' OR c.ligand_name_SRD LIKE '%glutamic%' OR c.ligand_name_SRD LIKE '%proline%' OR c.ligand_name_SRD LIKE '%alanine%' OR c.ligand_name_SRD LIKE '%serine%'))",
  "order_by": "c.ligand_name_SRD ASC, s.constant_value DESC",
  "limit": 300
}
```

[summary]
## search_stability — 200 row(s)

### logK — 44 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_41 | Cu^[2+] | ligand_5913 | DL-2-Amino-3-(5-hydroxo-6-o… | HL | NC(Cc1ccc(O)c(=O)[nH]1)C(=O)O | 10 | 10 | 37 | 0.15 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5913 | DL-2-Amino-3-(5-hydroxo-6-o… | HL | NC(Cc1ccc(O)c(=O)[nH]1)C(=O)O | 10 | 10 | 37 | 0.15 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 8 | 3 | 25~37 | 0.1~3 | *** | 4 |
| metal_92 | Mg^[2+] | ligand_5912 | DL-2-Amino-3-(5-hydroxo-4-o… | HL | NC(Cc1cc(=O)c(O)c[nH]1)C(=O)O | 7 | 7 | 37 | 0.15 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_5910 | DL-2-Amino-3-(6-oxo-1,6-dih… | HL | NC(Cc1cccc(=O)[nH]1)C(=O)O | 7 | 7 | 37 | 0.15 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5910 | DL-2-Amino-3-(6-oxo-1,6-dih… | HL | NC(Cc1cccc(=O)[nH]1)C(=O)O | 7 | 7 | 37 | 0.15 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5912 | DL-2-Amino-3-(5-hydroxo-4-o… | HL | NC(Cc1cc(=O)c(O)c[nH]1)C(=O)O | 6 | 6 | 37 | 0.15 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 6 | 2 | 25~37 | 0.1~3 | *** | 5 |
| metal_208 | Zn^[2+] | ligand_5906 | L-2-Amino-3-(2,5-diiodo-4-i… | HL | N[C@@H](Cc1nc(I)[nH]c1I)C(=O)O | 5 | 5 | 25 | 0.5 | *** | 1 |
| metal_33 | Co^[2+] | ligand_5906 | L-2-Amino-3-(2,5-diiodo-4-i… | HL | N[C@@H](Cc1nc(I)[nH]c1I)C(=O)O | 5 | 5 | 25 | 0.5 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_5906 | L-2-Amino-3-(2,5-diiodo-4-i… | HL | N[C@@H](Cc1nc(I)[nH]c1I)C(=O)O | 5 | 5 | 25 | 0.5 | *** | 1 |
| metal_33 | Co^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 5 | 2 | 25~37 | 0.1~1 | *** | 4 |
| metal_68 | H^[+] | ligand_5912 | DL-2-Amino-3-(5-hydroxo-4-o… | HL | NC(Cc1cc(=O)c(O)c[nH]1)C(=O)O | 4 | 4 | 37 | 0.15 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_5912 | DL-2-Amino-3-(5-hydroxo-4-o… | HL | NC(Cc1cc(=O)c(O)c[nH]1)C(=O)O | 4 | 4 | 37 | 0.15 | *** | 1 |
| metal_92 | Mg^[2+] | ligand_5913 | DL-2-Amino-3-(5-hydroxo-6-o… | HL | NC(Cc1ccc(O)c(=O)[nH]1)C(=O)O | 4 | 4 | 37 | 0.15 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_5906 | L-2-Amino-3-(2,5-diiodo-4-i… | HL | N[C@@H](Cc1nc(I)[nH]c1I)C(=O)O | 4 | 4 | 25 | 0.5 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_5906 | L-2-Amino-3-(2,5-diiodo-4-i… | HL | N[C@@H](Cc1nc(I)[nH]c1I)C(=O)O | 4 | 4 | 25 | 0.5 | *** | 1 |
| metal_68 | H^[+] | ligand_5906 | L-2-Amino-3-(2,5-diiodo-4-i… | HL | N[C@@H](Cc1nc(I)[nH]c1I)C(=O)O | 4 | 4 | 25 | 0.5 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 4 | 2 | 25~37 | 0.1~1 | *** | 4 |
| metal_68 | H^[+] | ligand_5913 | DL-2-Amino-3-(5-hydroxo-6-o… | HL | NC(Cc1ccc(O)c(=O)[nH]1)C(=O)O | 3 | 3 | 37 | 0.15 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_5913 | DL-2-Amino-3-(5-hydroxo-6-o… | HL | NC(Cc1ccc(O)c(=O)[nH]1)C(=O)O | 3 | 3 | 37 | 0.15 | *** | 1 |
| metal_68 | H^[+] | ligand_5910 | DL-2-Amino-3-(6-oxo-1,6-dih… | HL | NC(Cc1cccc(=O)[nH]1)C(=O)O | 3 | 3 | 37 | 0.15 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_5915 | L-2-Amino-3-(2-pyridyl)prop… | HL | N[C@@H](Cc1ccccn1)C(=O)O | 3 | 2 | 25 | 0.1 | *** | 2 |
| metal_112 | Ni^[2+] | ligand_5915 | L-2-Amino-3-(2-pyridyl)prop… | HL | N[C@@H](Cc1ccccn1)C(=O)O | 3 | 2 | 25 | 0.1 | *** | 2 |
| metal_33 | Co^[2+] | ligand_5915 | L-2-Amino-3-(2-pyridyl)prop… | HL | N[C@@H](Cc1ccccn1)C(=O)O | 3 | 2 | 25 | 0.1 | *** | 2 |
| metal_208 | Zn^[2+] | ligand_5915 | L-2-Amino-3-(2-pyridyl)prop… | HL | N[C@@H](Cc1ccccn1)C(=O)O | 3 | 2 | 25 | 0.1 | *** | 2 |
| metal_112 | Ni^[2+] | ligand_5860 | DL-2-Amino-3-(2-mercaptoimi… | H2L | NC(Cc1cnc(S)[nH]1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5860 | DL-2-Amino-3-(2-mercaptoimi… | H2L | NC(Cc1cnc(S)[nH]1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_5860 | DL-2-Amino-3-(2-mercaptoimi… | H2L | NC(Cc1cnc(S)[nH]1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_5860 | DL-2-Amino-3-(2-mercaptoimi… | H2L | NC(Cc1cnc(S)[nH]1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_5860 | DL-2-Amino-3-(2-mercaptoimi… | H2L | NC(Cc1cnc(S)[nH]1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5860 | DL-2-Amino-3-(2-mercaptoimi… | H2L | NC(Cc1cnc(S)[nH]1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_94 | Mn^[2+] | ligand_5860 | DL-2-Amino-3-(2-mercaptoimi… | H2L | NC(Cc1cnc(S)[nH]1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_5915 | L-2-Amino-3-(2-pyridyl)prop… | HL | N[C@@H](Cc1ccccn1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 2 | 1 | 25 | 0.1~3 | *** | 2 |
| metal_71 | Hg^[2+] | ligand_5860 | DL-2-Amino-3-(2-mercaptoimi… | H2L | NC(Cc1cnc(S)[nH]1)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_5860 | DL-2-Amino-3-(2-mercaptoimi… | H2L | NC(Cc1cnc(S)[nH]1)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_93 | MeHg^[+] | ligand_5947 | DL-[1-Carboxy-2-(2-mercapto… | H2L | C[N+](C)(C)C(Cc1cnc(S)[nH]1)C(=O)O.[Cl-] | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_68 | H^[+] | ligand_5947 | DL-[1-Carboxy-2-(2-mercapto… | H2L | C[N+](C)(C)C(Cc1cnc(S)[nH]1)C(=O)O.[Cl-] | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 1 | 1 | 25 | 3 | *** | 1 |
| metal_2 | Ag^[+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_201 | VO^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_64 | Ga^[3+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 1 | 1 | 25 | 3 | *** | 1 |
| metal_19 | Be^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |

### ΔH — 2 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_5860 | DL-2-Amino-3-(2-mercaptoimi… | H2L | NC(Cc1cnc(S)[nH]1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_5947 | DL-[1-Carboxy-2-(2-mercapto… | H2L | C[N+](C)(C)C(Cc1cnc(S)[nH]1)C(=O)O.[Cl-] | 1 | 1 | 25 | 0.1 | *** | 0 |

### ΔS — 10 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_41 | Cu^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 11 | 7 | 25 | 0.1~3 | *** | 0 |
| metal_68 | H^[+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 11 | 3 | 25 | 0~3 | *** | 0 |
| metal_33 | Co^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 3 | 2 | 25 | 0.1~3 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 3 | 2 | 25 | 0.1~3 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 3 | 2 | 25 | 0.1~3 | *** | 0 |
| metal_68 | H^[+] | ligand_5860 | DL-2-Amino-3-(2-mercaptoimi… | H2L | NC(Cc1cnc(S)[nH]1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 2 | 2 | 25 | 3 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 2 | 2 | 25 | 3 | *** | 0 |
| metal_26 | Cd^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_5947 | DL-[1-Carboxy-2-(2-mercapto… | H2L | C[N+](C)(C)C(Cc1cnc(S)[nH]1)C(=O)O.[Cl-] | 1 | 1 | 25 | 0.1 | *** | 0 |

---
