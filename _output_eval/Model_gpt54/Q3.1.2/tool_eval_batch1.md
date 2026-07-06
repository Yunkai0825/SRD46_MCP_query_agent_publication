# Q3.1.2 — Tool Results (batch 1)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Cu(II), Ni(II), H+",
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
  "name": "histidine, cysteine, glycine, aspartic acid, glutamic acid, proline, alanine, lysine, serine, tyrosine",
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
  "symbol": "Cu, Ni",
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
  "name": "glycine, histidine, cysteine, alanine, serine, tyrosine, proline, lysine",
  "include_groups": [
    "amino acid"
  ],
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
  "where": "((LOWER(c.ligand_name_SRD) LIKE '%glycin%' OR LOWER(c.ligand_name_SRD) LIKE '%alanin%' OR LOWER(c.ligand_name_SRD) LIKE '%histidin%' OR LOWER(c.ligand_name_SRD) LIKE '%cystein%' OR LOWER(c.ligand_name_SRD) LIKE '%aspart%' OR LOWER(c.ligand_name_SRD) LIKE '%glutam%' OR LOWER(c.ligand_name_SRD) LIKE '%serin%' OR LOWER(c.ligand_name_SRD) LIKE '%threon%' OR LOWER(c.ligand_name_SRD) LIKE '%tyros%' OR LOWER(c.ligand_name_SRD) LIKE '%lysin%' OR LOWER(c.ligand_name_SRD) LIKE '%argin%' OR LOWER(c.ligand_name_SRD) LIKE '%valin%' OR LOWER(c.ligand_name_SRD) LIKE '%leucin%' OR LOWER(c.ligand_name_SRD) LIKE '%isoleuc%' OR LOWER(c.ligand_name_SRD) LIKE '%prolin%' OR LOWER(c.ligand_name_SRD) LIKE '%methion%' OR LOWER(c.ligand_name_SRD) LIKE '%phenylalan%' OR LOWER(c.ligand_name_SRD) LIKE '%tryptophan%' OR LOWER(c.ligand_name_SRD) LIKE '%asparagin%' OR LOWER(c.ligand_name_SRD) LIKE '%glutamin%') AND (LOWER(c.metal_name_SRD) LIKE '%copper%' OR LOWER(c.metal_name_SRD) LIKE '%nickel%'))",
  "order_by": "c.ligand_name_SRD ASC, c.metal_name_SRD ASC",
  "limit": 200
}
```

[summary]
## search_stability

*(no results)*

---

### Step 10: `search_pka_ligands`
**Args:**
```json
{
  "where": "(LOWER(lc.ligand_name_SRD) LIKE '%glycin%' OR LOWER(lc.ligand_name_SRD) LIKE '%alanin%' OR LOWER(lc.ligand_name_SRD) LIKE '%histidin%' OR LOWER(lc.ligand_name_SRD) LIKE '%cystein%' OR LOWER(lc.ligand_name_SRD) LIKE '%aspart%' OR LOWER(lc.ligand_name_SRD) LIKE '%glutam%' OR LOWER(lc.ligand_name_SRD) LIKE '%serin%' OR LOWER(lc.ligand_name_SRD) LIKE '%threon%' OR LOWER(lc.ligand_name_SRD) LIKE '%tyros%' OR LOWER(lc.ligand_name_SRD) LIKE '%lysin%' OR LOWER(lc.ligand_name_SRD) LIKE '%argin%' OR LOWER(lc.ligand_name_SRD) LIKE '%valin%' OR LOWER(lc.ligand_name_SRD) LIKE '%leucin%' OR LOWER(lc.ligand_name_SRD) LIKE '%isoleuc%' OR LOWER(lc.ligand_name_SRD) LIKE '%prolin%' OR LOWER(lc.ligand_name_SRD) LIKE '%methion%' OR LOWER(lc.ligand_name_SRD) LIKE '%phenylalan%' OR LOWER(lc.ligand_name_SRD) LIKE '%tryptophan%' OR LOWER(lc.ligand_name_SRD) LIKE '%asparagin%' OR LOWER(lc.ligand_name_SRD) LIKE '%glutamin%')",
  "order_by": "lc.ligand_name_SRD ASC",
  "limit": 200
}
```

[summary]
## search_pka_ligands — 200 row(s)

| ligand_id | ligand_name | HxL_def | formula | smiles | pH_ladder | T°C_range | I(M)_range | similarity_score |
|-----------|-------------|---------|---------|--------|-----------|-----------|------------|------------------|
| ligand_6729 | (4-Aminophenylamino)butanedioic acid (N-(4-Aminophenyl)aspa… | H2L | C10H12N2O4 | Nc1ccc(NC(CC(=O)O)C(=O)O)cc1 | −∞; H4L (M_tot_1); (2.39, vlm_117775); H3L (M_tot_1); (3.08, vlm_117774); H2L (M_tot_1); (4.03, vlm_117773); HL (M_tot_1); (6.36, vlm_117772); L (M_tot_7); +∞ | 25 | 0.5 | *** |
| ligand_6126 | (Carboxymethyl)trimethylammonium (nitrate) (N,N,N,-Trimethy… | HL | C5H12N1O2/+ | C[N+](C)(C)CC(=O)O.O=[N+]([O-])[O-] | −∞; HL (M_tot_1); (-1.7, vlm_104099); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_5773 | 1-Aminocyclopentanecarboxylic acid (Cycloleucine) | HL | C6H11N1O2 | NC1(C(=O)O)CCCC1 | −∞; H2L (M_tot_1); (2.4, vlm_94930); HL (M_tot_2); (10.31, vlm_94929); L (M_tot_5); +∞ | 20 | 0.1 | *** |
| ligand_8968 | 2-(Acetylamino)butanedioic acid (N-Acetylaspartic acid) | H2L | C6H9N1O5 | CC(=O)NC(CC(=O)O)C(=O)O | −∞; H2L (M_tot_1); (3.04, vlm_155335); HL (M_tot_1); (4.49, vlm_155334); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_8969 | 2-(Acetylamino)pentanedioic acid (N-Acetylglutamic acid) | H2L | C7H11N1O5 | CC(=O)NC(CCC(=O)O)C(=O)O | −∞; H2L (M_tot_1); (3.29, vlm_155340); HL (M_tot_1); (4.6, vlm_155339); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_6724 | 2-(Carboxymethylamino)benzoic acid (N-(2-Carboxyphenyl)glyc… | H2L | C9H9N1O4 | O=C(O)CNc1ccccc1C(=O)O | −∞; H2L (M_tot_1); (3.33, vlm_117728); HL (M_tot_1); (4.9, vlm_117727); L (M_tot_6); +∞ | 25 | 0.1 | *** |
| ligand_5959 | 2-(Carboxymethylaminomethyl)azole-4-sulfonic acid (N-(4-Sul… | H2L | C7H10N2O5S1 | O=C(O)CNCc1cc(S(=O)(=O)O)c[nH]1 | −∞; H2L (M_tot_1); (2.25, vlm_100094); HL (M_tot_1); (8.71, vlm_100093); L (M_tot_2); +∞ | 25 | 1 | *** |
| ligand_8458 | 2-Amino-2-(methoxycarboxy)ethyl(dihydrogenphosphate) (O-Pho… | H2L | C3H10N1O6P1 | COC(=O)C(N)COP(=O)(O)O | −∞; H2L (M_tot_1); (5.33, vlm_144212); HL (M_tot_1); (7.83, vlm_144211); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6955 | 2-Methylalaninamide | L | C4H10N2O1 | CC(C)(N)C(N)=O | −∞; HL (M_tot_1); (8.06, vlm_121280); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_6968 | 2-Methylalanyl-2-methylalaninamide | L | C8H17N3O2 | CC(C)(N)C(=O)NC(C)(C)C(N)=O | −∞; HL (M_tot_1); (7.93, vlm_121364); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_6471 | 2-Methylalanyl-2-methylalanine | HL | C8H16N2O3 | CC(C)(N)C(=O)NC(C)(C)C(=O)O | −∞; H2L (M_tot_1); (3.67, vlm_115368); HL (M_tot_1); (8.26, vlm_115367); L (M_tot_3); +∞ | 25 | 0.1 | *** |
| ligand_6971 | 2-Methylalanyl-2-methylalanyl-2-methylalaninamide | L | C12H24N4O3 | CC(C)(N)C(=O)NC(C)(C)C(=O)NC(C)(C)C(N)=O | −∞; HL (M_tot_1); (7.76, vlm_121381); L (M_tot_2); +∞ | 25 | 0.1 | *** |
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
| ligand_5816 | D-3-Amino-3-carboxypropanohydroxamic acid (Asparagine hydro… | H2L | C4H8N2O4 | NC(CC(=O)NO)C(=O)O | −∞; H3L (M_tot_1); (2.18, vlm_96046); H2L (M_tot_1); (8.15, vlm_96045); HL (M_tot_1); (9.37, vlm_96044); L (M_tot_4); +∞ | 25 | 0.5 | *** |
| ligand_6962 | D-4-Amino-1,2-oxazolidin-3-one (D-Cycloserine) | L | C6H6N2O2 | NC1CONC1=O | −∞; H2L (M_tot_1); (4.39, vlm_121319); HL (M_tot_6); (7.35, vlm_121315); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_6542 | D-Alanyl-D-alanyl-D-alanine | HL | C9H17N3O4 | C[C@@H](N)C(=O)N[C@H](C)C(=O)N[C@H](C)C(=O)O | −∞; H2L (M_tot_1); (3.28, vlm_116112); HL (M_tot_1); (7.95, vlm_116111); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6541 | D-Alanyl-L-alanyl-L-alanine | HL | C9H17N3O4 | C[C@H](NC(=O)[C@H](C)NC(=O)[C@@H](C)N)C(=O)O | −∞; H2L (M_tot_1); (3.26, vlm_116110); HL (M_tot_1); (7.95, vlm_116109); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6600 | D-Alanyl-L-alanyl-L-alanyl-L-alanine | HL | C12H22N4O5 | C[C@H](NC(=O)[C@H](C)NC(=O)[C@H](C)NC(=O)[C@@H](C)N)C(=O)O | −∞; H2L (M_tot_1); (3.31, vlm_116792); HL (M_tot_1); (7.83, vlm_116791); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6428 | D-Alanyl-L-leucine | HL | C9H18N2O3 | CC(C)C[C@H](NC(=O)[C@@H](C)N)C(=O)O | −∞; H2L (M_tot_1); (3.14, vlm_114817); HL (M_tot_1); (8.23, vlm_114814); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_6586 | D-Arginyl-L-lysyl-L-aspartic acid | *** | C16H31N7O6 | *** | −∞; H4L (M_tot_1); (2.76, vlm_116564); H3L (M_tot_1); (4.2, vlm_116563); H2L (M_tot_1); (7.5, vlm_116562); HL (M_tot_2); (10.29, vlm_116561); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6515 | D-Histidyl-L-histidine | HL | C12H16N6O3 | N[C@H](Cc1c[nH]cn1)C(=O)N[C@@H](Cc1c[nH]cn1)C(=O)O | −∞; H4L (M_tot_1); (2.18, vlm_115820); H3L (M_tot_1); (5.32, vlm_115818); H2L (M_tot_1); (6.73, vlm_115816); HL (M_tot_1); (7.82, vlm_115814); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_6458 | D-Leucyl-L-isoleucine | HL | C12H24N2O3 | CC[C@H](C)[C@H](NC(=O)[C@H](N)CC(C)C)C(=O)O | −∞; H2L (M_tot_1); (3.06, vlm_115189); HL (M_tot_1); (8.09, vlm_115186); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_6456 | D-Leucyl-L-leucine (also L-Leucyl-D-leucine) | HL | C12H24N2O3 | CC(C)C[C@@H](N)C(=O)N[C@@H](CC(C)C)C(=O)O | −∞; H2L (M_tot_1); (3.11, vlm_115159); HL (M_tot_1); (8.24, vlm_115156); L (M_tot_4); +∞ | 25 | 0.1 | *** |
| ligand_6555 | D-Leucyl-L-leucylglycine | HL | C14H27N3O4 | CC(C)C[C@@H](N)C(=O)N[C@@H](CC(C)C)C(=O)NCC(=O)O | −∞; H2L (M_tot_1); (3.33, vlm_116206); HL (M_tot_1); (7.87, vlm_116205); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_6462 | D-Leucyl-L-tyrosine | H2L | C15H22N2O4 | CC(C)C[C@@H](N)C(=O)N[C@@H](Cc1ccc(O)cc1)C(=O)O | −∞; H3L (M_tot_1); (2.9, vlm_115266); H2L (M_tot_1); (8.34, vlm_115263); HL (M_tot_5); (10.36, vlm_115262); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6552 | D-Leucylglycyl-L-leucine | HL | C14H27N3O4 | CC(C)C[C@@H](N)C(=O)NCC(=O)N[C@@H](CC(C)C)C(=O)O | −∞; H2L (M_tot_1); (3.33, vlm_116189); HL (M_tot_1); (7.81, vlm_116188); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_6522 | D-Methionyl-L-S-methylcysteine | HL | C9H18N2O3S2 | CSCC[C@@H](N)C(=O)N[C@@H](CSC)C(=O)O | −∞; H2L (M_tot_1); (2.72, vlm_115882); HL (M_tot_1); (7.62, vlm_115881); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_6528 | D-Prolyl-L-histidine | HL | C10H18N4O3 | O=C(O)[C@H](Cc1cnc[nH]1)NC(=O)[C@H]1CCCN1 | −∞; HL (M_tot_1); (-9.16, vlm_115947); L (M_tot_2); (-6.77, vlm_115948); HL (M_tot_1); (2.91, vlm_115949); H2L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5768 | D-allo-2-Amino-3-methylpentanoic acid (D-allo-Isoleucine) | HL | C6H13N1O2 | CC[C@H](C)[C@@H](N)C(=O)O | −∞; H2L (M_tot_1); (2.2, vlm_94822); HL (M_tot_1); (9.62, vlm_94819); L (M_tot_3); +∞ | 25 | 0.1 | *** |
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
| ligand_7065 | DL-2,6-Diaminohexanoic acid methyl ester (DL-Lysine methyl … | L | C7H16N2O2 | COC(=O)C(N)CCCCN | −∞; H2L (M_tot_1); (7.19, vlm_123544); HL (M_tot_1); (10.25, vlm_123540); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5805 | DL-2-Amino-2-methylpentanedioic acid (2-Methylglutamic acid) | H2L | C6H11N1O4 | C[C@](N)(CCC(=O)O)C(=O)O | −∞; H2L (M_tot_1); (4.05, vlm_95867); HL (M_tot_1); (9.72, vlm_95866); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_5783 | DL-2-Amino-3-(2-chlorophenyl)propanoic acid (DL-3-(2-Chloro… | HL | C9H10Cl1N1O2 | N[C@@H](Cc1ccccc1Cl)C(=O)O | −∞; H2L (M_tot_1); (2.23, vlm_95183); HL (M_tot_1); (8.94, vlm_95182); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5780 | DL-2-Amino-3-(2-fluorophenyl)propanoic acid (DL-3-(2-Fluoro… | HL | C9H10F1N1O2 | N[C@@H](Cc1ccccc1F)C(=O)O | −∞; H2L (M_tot_1); (2.12, vlm_95166); HL (M_tot_1); (9.01, vlm_95163); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5817 | DL-2-Amino-3-(2-hydroxyphenyl)propanoic acid (o-Tyrosine) | H2L | C9H11N1O3 | NC(Cc1ccccc1O)C(=O)O | −∞; H3L (M_tot_1); (2.41, vlm_96078); H2L (M_tot_1); (8.67, vlm_96074); HL (M_tot_6); (11.01, vlm_96070); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_5860 | DL-2-Amino-3-(2-mercaptoimidazo-4-yl)propanoic acid (Thiohi… | H2L | C6H9N3O2S1 | NC(Cc1cnc(S)[nH]1)C(=O)O | −∞; HL (M_tot_1); (-11.77, vlm_97676); L (M_tot_9); (8.59, vlm_97679); HL (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5855 | DL-2-Amino-3-(3,4-dimethoxyphenyl)propanoic acid (3,4-Dimet… | HL | C11H15N1O4 | COc1ccc(C[C@H](N)C(=O)O)cc1OC | −∞; H2L (M_tot_1); (2.37, vlm_97370); HL (M_tot_1); (9.02, vlm_97369); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5784 | DL-2-Amino-3-(3-chlorophenyl)propanoic acid (DL-3-(3-Chloro… | HL | C9H10Cl1N1O2 | N[C@@H](Cc1cccc(Cl)c1)C(=O)O | −∞; H2L (M_tot_1); (2.17, vlm_95185); HL (M_tot_1); (8.91, vlm_95184); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5781 | DL-2-Amino-3-(3-fluorophenyl)propanoic acid (DL-3-(3-Fluoro… | HL | C9H10F1N1O2 | N[C@@H](Cc1cccc(F)c1)C(=O)O | −∞; H2L (M_tot_1); (2.1, vlm_95172); HL (M_tot_1); (8.98, vlm_95169); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5818 | DL-2-Amino-3-(3-hydroxyphenyl)propanoic acid (m-Tyrosine) | H2L | C9H11N1O3 | N[C@@H](Cc1cccc(O)c1)C(=O)O | −∞; H3L (M_tot_1); (2.22, vlm_96149); H2L (M_tot_1); (8.95, vlm_96145); HL (M_tot_6); (10.04, vlm_96141); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6997 | DL-2-Amino-3-(3-indole)propanohydroxamic acid (Tryptophanhy… | HL | C11H13N3O2 | N[C@@H](Cc1c[nH]c2ccccc12)C(=O)NO | −∞; H2L (M_tot_1); (7.04, vlm_121785); HL (M_tot_1); (9.09, vlm_121784); L (M_tot_3); +∞ | 25 | 0.5 | *** |
| ligand_5785 | DL-2-Amino-3-(4-chlorophenyl)propanoic acid (DL-3-(4-Chloro… | HL | C9H10Cl1N1O2 | N[C@@H](Cc1ccc(Cl)cc1)C(=O)O | −∞; H2L (M_tot_1); (2.08, vlm_95187); HL (M_tot_1); (8.96, vlm_95186); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5782 | DL-2-Amino-3-(4-fluorophenyl)propanoic acid (DL-3-(4-Fluoro… | HL | C9H10F1N1O2 | N[C@@H](Cc1ccc(F)cc1)C(=O)O | −∞; H2L (M_tot_1); (2.13, vlm_95178); HL (M_tot_1); (9.05, vlm_95175); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6871 | DL-2-Amino-3-(4-hydroxyphenyl)propanol (Tyrosinol) | HL | C9H13N1O2 | NC(CO)Cc1ccc(O)cc1 | −∞; H2L (M_tot_1); (8.94, vlm_120570); HL (M_tot_1); (9.98, vlm_120567); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5778 | DL-2-Amino-3-chloropropanoic acid (3-Chloroalanine) | HL | C3H6Cl1N1O2 | N[C@@H](CCl)C(=O)O | −∞; H2L (M_tot_1); (2, vlm_95146); HL (M_tot_1); (8.18, vlm_95145); L (M_tot_4); +∞ | 25 | 0.1 | *** |
| ligand_6995 | DL-2-Amino-3-hydroxybutanohydroxamic acid (Threoninehydroxa… | HL | C4H10N2O3 | C[C@@H](O)[C@H](N)C(=O)NO | −∞; H2L (M_tot_1); (6.92, vlm_121712); HL (M_tot_2); (8.89, vlm_121710); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_5807 | DL-2-Amino-3-hydroxypentanedioic acid (3-Hydroxyglutamic ac… | H2L | C5H9N1O5 | N[C@H](C(=O)O)C(O)CC(=O)O | −∞; H3L (M_tot_1); (2.09, vlm_95876); H2L (M_tot_1); (4.08, vlm_95875); HL (M_tot_1); (9.06, vlm_95874); L (M_tot_4); +∞ | 25 | 0.1 | *** |
| ligand_6994 | DL-2-Amino-3-hydroxypropanohydroxamic acid (Serinehydroxami… | HL | C3H8N2O3 | N[C@@H](CO)C(=O)NO | −∞; H2L (M_tot_1); (6.8, vlm_121685); HL (M_tot_2); (9.04, vlm_121683); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_11519 | DL-2-Amino-3-methoxypropanoic acid (3-Methoxyalanine) | HL | C4H9N1O3 | COC[C@H](N)C(=O)O | −∞; H2L (M_tot_1); (2.037, vlm_97356); HL (M_tot_1); (9.176, vlm_97351); L (M_tot_1); +∞ | 25 | 0 | *** |
| ligand_5803 | DL-2-Amino-3-methylbutanedioic acid (3-Methylaspartic acid) | H2L | C5H9N1O4 | CC(C(=O)O)[C@H](N)C(=O)O | −∞; H3L (M_tot_1); (1.99, vlm_95735); H2L (M_tot_1); (3.59, vlm_95734); HL (M_tot_2); (9.48, vlm_95733); L (M_tot_2); +∞ | 25 | 0.5 | *** |
| ligand_6989 | DL-2-Amino-3-phenylpropanohydroxamic acid (Phenylalaninehyd… | HL | C9H12N2O2 | N[C@@H](Cc1ccccc1)C(=O)NO | −∞; H2L (M_tot_1); (6.89, vlm_121635); HL (M_tot_1); (9.01, vlm_121634); L (M_tot_2); +∞ | 25 | 0.5 | *** |
| ligand_5859 | DL-2-Amino-4-mercaptobutanoic acid (Homocysteine) | H2L | C4H9N1O2S1 | NC(CCS)C(=O)O | −∞; H3L (M_tot_1); (2.15, vlm_97673); H2L (M_tot_1); (8.57, vlm_97672); HL (M_tot_1); (10.38, vlm_97671); L (M_tot_1); +∞ | 25~30 | 0.1 | *** |
| ligand_6986 | DL-2-Aminohexanohydroxamic acid (Norleucinehydroxamic acid) | HL | C6H14N2O2 | CCCC[C@H](N)C(=O)NO | −∞; H2L (M_tot_1); (7.33, vlm_121572); HL (M_tot_2); (9.14, vlm_121571); L (M_tot_5); +∞ | 25 | 0.5 | *** |
| ligand_5764 | DL-2-Aminohexanoic acid (Norleucine) | HL | C6H13N1O2 | CCCC[C@H](N)C(=O)O | −∞; H2L (M_tot_1); (2.31, vlm_94501); HL (M_tot_1); (9.68, vlm_94495); L (M_tot_7); +∞ | 25 | 0.1 | *** |
| ligand_5842 | DL-2-Aminopentanedioic acid 1-ethyl ester (1-Ethyl glutamat… | HL | C7H13N1O4 | CCOC(=O)[C@@H](N)CCC(=O)O | −∞; H2L (M_tot_1); (3.85, vlm_97038); HL (M_tot_1); (7.84, vlm_97037); L (M_tot_1); +∞ | 25 | 0 | *** |
| ligand_5840 | DL-2-Aminopentanedioic acid 5-ethyl ester (5-Ethyl glutamat… | HL | C7H13N1O4 | CCOC(=O)CC[C@H](N)C(=O)O | −∞; H2L (M_tot_1); (2.15, vlm_97034); HL (M_tot_1); (9.19, vlm_97033); L (M_tot_1); +∞ | 25 | 0 | *** |
| ligand_6985 | DL-2-Aminopentanohydroxamic acid (Norvalinehydroxamic acid) | HL | C5H12N2O2 | CCC[C@H](N)C(=O)NO | −∞; H2L (M_tot_1); (7.34, vlm_121550); HL (M_tot_2); (9.13, vlm_121549); L (M_tot_5); +∞ | 25 | 0.5 | *** |
| ligand_5763 | DL-2-Aminopentanoic acid (Norvaline) | HL | C5H11N1O2 | CCC[C@H](N)C(=O)O | −∞; H2L (M_tot_1); (2.31, vlm_94456); HL (M_tot_1); (9.65, vlm_94449); L (M_tot_7); +∞ | 25 | 0.1 | *** |
| ligand_8712 | DL-2-Methyl-5-pyrrolidone-2-carboxylic acid (2-Methylpyrogl… | HL | C6H9N1O3 | CC1(C(=O)O)CCC(=O)N1 | −∞; HL (M_tot_1); (3.14, vlm_149991); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_8713 | DL-2-Phenyl-5-pyrrolidone-2-carboxylic acid (2-Phenylpyrogl… | HL | C11H11N1O3 | O=C1CCC(C(=O)O)(c2ccccc2)N1 | −∞; HL (M_tot_1); (2.69, vlm_149992); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5834 | DL-3-Amino-2-hydroxypropanoic acid (Isoserine) | HL | C3H7N1O3 | NCC(O)C(=O)O | −∞; H2L (M_tot_1); (2.66, vlm_96924); HL (M_tot_5); (9.13, vlm_96921); L (M_tot_6); +∞ | 25 | 0.1 | *** |
| ligand_5796 | DL-3-Amino-3-phenylpropanoic acid (Phenyl-beta-Alanine) | HL | C9H11N1O2 | NC(CC(=O)O)c1ccccc1 | −∞; H2L (M_tot_1); (3.4, vlm_95403); HL (M_tot_1); (9, vlm_95402); L (M_tot_1); +∞ | 25 | 0.5 | *** |
| ligand_6926 | DL-Alanine ethyl ester | L | C5H11N1O2 | CCOC(=O)C(C)N | −∞; HL (M_tot_1); (7.91, vlm_121189); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6925 | DL-Alanine methyl ester | L | C4H9N1O2 | COC(=O)C(C)N | −∞; HL (M_tot_1); (7.76, vlm_121186); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6967 | DL-Alanyl-2-methylalaninamide | L | C7H15N3O2 | CC(N)C(=O)NC(C)(C)C(N)=O | −∞; HL (M_tot_1); (7.93, vlm_121359); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_6558 | DL-Alanyl-2-methylalanyl-2-methylalanine | HL | C11H21N3O4 | CC(N)C(=O)NC(C)(C)C(=O)NC(C)(C)C(=O)O | −∞; H2L (M_tot_1); (3.95, vlm_116223); HL (M_tot_1); (8.29, vlm_116222); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_5838 | DL-Amino-4-Methoxyphenylacetic acid (4-Methoxyphenylglycine) | HL | C9H11N1O3 | COc1ccc(C(N)C(=O)O)cc1 | −∞; H2L (M_tot_1); (2, vlm_97021); HL (M_tot_1); (9.07, vlm_97020); L (M_tot_6); +∞ | 25 | 0.1 | *** |
| ligand_5786 | DL-Amino-4-sulfophenylacetic acid (4-Sulfophenylglycine) | H2L | C8H9N1O5S1 | NC(C(=O)O)c1ccc(S(=O)(=O)O)cc1 | −∞; H2L (M_tot_1); (-1.8, vlm_95189); HL (M_tot_1); (8.66, vlm_95188); L (M_tot_6); +∞ | 25 | 0.1 | *** |
| ligand_5776 | DL-Aminophenylacetic acid (Phenylglycine) | HL | C8H9N1O2 | NC(C(=O)O)c1ccccc1 | −∞; H2L (M_tot_1); (-1.9, vlm_94963); HL (M_tot_1); (8.92, vlm_94962); L (M_tot_6); +∞ | 25 | 0.1 | *** |
| ligand_6939 | DL-Glutamic acid diethyl ester | L | C9H17N1O4 | CCOC(=O)CCC(N)C(=O)OCC | −∞; HL (M_tot_1); (7.035, vlm_121212); L (M_tot_1); +∞ | 25 | 0 | *** |
| ligand_6938 | DL-Glutamic acid dimethyl ester | L | C7H13N1O4 | COC(=O)CCC(N)C(=O)OC | −∞; HL (M_tot_1); (7.03, vlm_121211); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6934 | DL-Isoleucine methyl ester | L | C7H15N1O2 | CC[C@H](C)[C@H](N)C(=O)OC | −∞; HL (M_tot_1); (7.54, vlm_121204); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6933 | DL-Leucine ethyl ester | L | C8H17N1O2 | CCOC(=O)C(N)CC(C)C | −∞; HL (M_tot_1); (7.65, vlm_121201); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6932 | DL-Leucine methyl ester | L | C7H15N1O2 | COC(=O)C(N)CC(C)C | −∞; HL (M_tot_1); (7.63, vlm_121200); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_7022 | DL-Methionine methyl ester | L | C6H13N1O2S1 | COC(=O)C(N)CCSC | −∞; HL (M_tot_1); (7.1, vlm_122244); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6022 | DL-N,N-Bis(2-hydroxyethyl)alanine | HL | C7H15N1O4 | CC(C(=O)O)N(CCO)CCO | −∞; H2L (M_tot_1); (-1.7, vlm_101637); HL (M_tot_1); (8.47, vlm_101636); L (M_tot_21); +∞ | 20 | 0.1 | *** |
| ligand_6725 | DL-N-(2-Carboxyphenyl)alanine | H2L | C10H11N1O4 | CC(Nc1ccccc1C(=O)O)C(=O)O | −∞; H2L (M_tot_1); (3.12, vlm_117737); HL (M_tot_1); (5.01, vlm_117736); L (M_tot_3); +∞ | 20 | 0.1 | *** |
| ligand_6929 | DL-Norleucine methyl ester | L | C7H15N1O2 | CCCCC(N)C(=O)OC | −∞; HL (M_tot_1); (7.68, vlm_121195); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6928 | DL-Norvaline methyl ester | L | C6H13N1O2 | CCCC(N)C(=O)OC | −∞; HL (M_tot_1); (7.66, vlm_121194); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6937 | DL-O-Methyltyrosine ethyl ester | L | C12H17N1O3 | CCOC(=O)[C@@H](N)Cc1ccc(OC)cc1 | −∞; HL (M_tot_1); (7.19, vlm_121210); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6936 | DL-Phenylalanine ethyl ester | L | C11H15N1O2 | CCOC(=O)C(N)Cc1ccccc1 | −∞; HL (M_tot_1); (7.12, vlm_121209); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6412 | DL-Phosphoserylglycine (DL-Serylglycine dihydrogenphosphate) | H3L | C5H11N2O7P1 | NC(COP(=O)(O)O)C(=O)NCC(=O)O | −∞; H3L (M_tot_1); (3.16, vlm_114515); H2L (M_tot_1); (5.42, vlm_114514); HL (M_tot_1); (8.01, vlm_114513); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_6896 | DL-Serine methyl ester | L | C4H9N1O3 | COC(=O)C(N)CO | −∞; HL (M_tot_1); (7.07, vlm_120943); L (M_tot_2); +∞ | 25 | 0.1 | *** |

---

### Step 11: `search_stability`
**Args:**
```json
{
  "where": "((LOWER(c.ligand_name_SRD) LIKE '%glycine%' OR LOWER(c.ligand_name_SRD) LIKE '%beta-alanine%' OR LOWER(c.ligand_name_SRD) LIKE '%homocysteine%' OR LOWER(c.ligand_name_SRD) LIKE '%3-methylaspartic acid%' OR LOWER(c.ligand_name_SRD) LIKE '%3-hydroxyglutamic acid%' OR LOWER(c.ligand_name_SRD) LIKE '%o-tyrosine%' OR LOWER(c.ligand_name_SRD) LIKE '%m-tyrosine%' OR LOWER(c.ligand_name_SRD) LIKE '%3-chloroalanine%') AND (LOWER(c.metal_name_SRD) LIKE '%copper%' OR LOWER(c.metal_name_SRD) LIKE '%nickel%'))",
  "order_by": "c.ligand_name_SRD ASC, c.metal_name_SRD ASC, s.constant_value DESC",
  "limit": 200
}
```

[summary]
## search_stability

*(no results)*

---

### Step 12: `search_networks`
**Args:**
```json
{
  "where": "((LOWER(c.ligand_name) LIKE '%glycine%' OR LOWER(c.ligand_name) LIKE '%beta-alanine%' OR LOWER(c.ligand_name) LIKE '%homocysteine%' OR LOWER(c.ligand_name) LIKE '%3-methylaspartic acid%' OR LOWER(c.ligand_name) LIKE '%3-hydroxyglutamic acid%' OR LOWER(c.ligand_name) LIKE '%o-tyrosine%' OR LOWER(c.ligand_name) LIKE '%m-tyrosine%' OR LOWER(c.ligand_name) LIKE '%3-chloroalanine%') AND (LOWER(c.metal_name) LIKE '%copper%' OR LOWER(c.metal_name) LIKE '%nickel%'))",
  "order_by": "c.ligand_name ASC, c.metal_name ASC",
  "limit": 100
}
```

[summary]
## search_networks

*(no results)*

---

### Step 13: `db_distribution`
**Args:**
```json
{
  "table": "ligand_card",
  "group_column": "ligand_class_name",
  "limit": 30
}
```

[summary]
## db_distribution - ligand_card by ligand_class_name

**total_rows:** 5750

| value | count | pct |
|-------|-------|-----|
| Ligands not selected | 1339 | 23.29% |
| Amino Acids | 297 | 5.17% |
| Aliphatic amines | 250 | 4.35% |
| Pyridines (azines) | 248 | 4.31% |
| Carboxylic acids | 182 | 3.17% |
| Aza-macrocycles | 165 | 2.87% |
| Peptides | 157 | 2.73% |
| Aliphatic amines secondary N | 139 | 2.42% |
| Pyrroles (azoles) | 134 | 2.33% |
| Aminophosphorus acids | 132 | 2.3% |
| EDTA and derivatives | 115 | 2.0% |
| Aza-oxa-macrocycles | 112 | 1.95% |
| Carboxylic acids diacids | 103 | 1.79% |
| Inorganic ligands | 101 | 1.76% |
| Naphtols | 100 | 1.74% |
| polypeptides | 98 | 1.7% |
| Organophosphorus and arsenic acids | 95 | 1.65% |
| Aliphatic amines tertiary N | 95 | 1.65% |
| Phenols | 92 | 1.6% |
| NTA and derivatives | 91 | 1.58% |
| miscellaneous hydrocarbons | 84 | 1.46% |
| miscellaneous hydroxamic acids | 74 | 1.29% |
| Aniline | 72 | 1.25% |
| Carboxylic acids thio | 71 | 1.23% |
| miscellaneous ureas, hadrazides, amidines | 70 | 1.22% |
| Aza macrocycles with carboxylic acids | 70 | 1.22% |
| miscellaneous alcohols and sugar | 68 | 1.18% |
| tripeptides | 66 | 1.15% |
| Catechols | 66 | 1.15% |
| Aniline carboxylic acids | 66 | 1.15% |

---

### Step 14: `search_pka_ligands`
**Args:**
```json
{
  "where": "(lc.ligand_class_name = 'Amino Acids')",
  "order_by": "lc.ligand_name_SRD ASC",
  "limit": 300
}
```

[summary]
## search_pka_ligands — 200 row(s)

| ligand_id | ligand_name | HxL_def | formula | smiles | pH_ladder | T°C_range | I(M)_range | similarity_score |
|-----------|-------------|---------|---------|--------|-----------|-----------|------------|------------------|
| ligand_5808 | (3-Aminopropyl)malonic acid | H2L | C6H11N1O4 | NCCCC(C(=O)O)C(=O)O | −∞; H3L (M_tot_1); (2.52, vlm_95888); H2L (M_tot_1); (4.86, vlm_95885); HL (M_tot_2); (10.45, vlm_95882); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_6126 | (Carboxymethyl)trimethylammonium (nitrate) (N,N,N,-Trimethy… | HL | C5H12N1O2/+ | C[N+](C)(C)CC(=O)O.O=[N+]([O-])[O-] | −∞; HL (M_tot_1); (-1.7, vlm_104099); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_5939 | (Carboxymethylamino)aceto-N-methylhydroxamic acid | H2L | C5H10N2O4 | CN(O)C(=O)CNCC(=O)O | −∞; H3L (M_tot_1); (-1.9, vlm_99848); H2L (M_tot_1); (7.58, vlm_99847); HL (M_tot_1); (9.22, vlm_99846); L (M_tot_2); +∞ | 20 | 0.1 | *** |
| ligand_5938 | (Carboxymethylamino)acetohydroxamic acid | H2L | C4H8N2O4 | O=C(O)CNCC(=O)NO | −∞; H3L (M_tot_1); (-1.8, vlm_99837); H2L (M_tot_1); (6.99, vlm_99836); HL (M_tot_1); (9.09, vlm_99835); L (M_tot_3); +∞ | 20 | 0.1 | *** |
| ligand_5956 | 1,2,3-Triazole-4,5-dicarboxylic acid | H2L | C4H3N3O4 | O=C(O)c1nn[nH]c1C(=O)O | −∞; H3L (M_tot_1); (-1.86, vlm_100065); H2L (M_tot_1); (5.9, vlm_100062); HL (M_tot_1); (9.3, vlm_100059); L (M_tot_3); +∞ | 25 | 0 | *** |
| ligand_5953 | 1,2,3-Triazole-4-carboxylic acid | HL | C3H3N3O2 | O=C(O)c1cn[nH]n1 | −∞; H2L (M_tot_1); (3.22, vlm_100050); HL (M_tot_1); (8.7, vlm_100047); L (M_tot_1); +∞ | 25 | 0 | *** |
| ligand_6033 | 1,4,7-Trimethyl-1,7-bis(4-carboxybenzyl)-1,4,7-triazaheptane | H2L | C20H29N3O4 | CN(CCN(C)Cc1ccc(C(=O)O)cc1)CCN(C)Cc1ccc(C(=O)O)cc1 | −∞; H5L (M_tot_1); (-1.6, vlm_101869); H4L (M_tot_1); (3.19, vlm_101866); H3L (M_tot_1); (3.7, vlm_101863); H2L (M_tot_1); (6.89, vlm_101860); HL (M_tot_1); (8.25, vlm_101857); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_5980 | 1,4-Diaminobutane-N,N'-diacetic acid | H2L | C8H16N2O4 | O=C(O)CNCCCCNCC(=O)O | −∞; H4L (M_tot_1); (-1.84, vlm_100526); H3L (M_tot_1); (2.52, vlm_100525); H2L (M_tot_1); (9.04, vlm_100524); HL (M_tot_1); (10.33, vlm_100523); L (M_tot_3); +∞ | 25 | 1 | *** |
| ligand_6028 | 1,5-Diazacyclooctane-N-acetic acid | HL | C8H16N2O2 | O=C(O)CN1CCCNCCC1 | −∞; HL (M_tot_1); (-11.8, vlm_101743); L (M_tot_2); (-1.7, vlm_101745); H2L (M_tot_1); (5.18, vlm_101744); HL (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5775 | 1-Aminocycloheptanecarboxylic acid | HL | C8H15N1O2 | NC1(C(=O)O)CCCCCC1 | −∞; H2L (M_tot_1); (2.59, vlm_94952); HL (M_tot_2); (10.46, vlm_94951); L (M_tot_5); +∞ | 20 | 0.1 | *** |
| ligand_5774 | 1-Aminocyclohexanecarboxylic acid | HL | C7H13N1O2 | NC1(C(=O)O)CCCCC1 | −∞; H2L (M_tot_1); (2.41, vlm_94941); HL (M_tot_1); (10.13, vlm_94940); L (M_tot_6); +∞ | 20 | 0.1 | *** |
| ligand_5773 | 1-Aminocyclopentanecarboxylic acid (Cycloleucine) | HL | C6H11N1O2 | NC1(C(=O)O)CCCC1 | −∞; H2L (M_tot_1); (2.4, vlm_94930); HL (M_tot_2); (10.31, vlm_94929); L (M_tot_5); +∞ | 20 | 0.1 | *** |
| ligand_5957 | 1-Phenyl-1,2,3-triazole-4,5-dicarboxylic acid | H2L | C10H8N3O4 | O=C(O)c1nnn(-c2ccccc2)c1C(=O)O | −∞; H2L (M_tot_1); (2.1, vlm_100075); HL (M_tot_1); (4.93, vlm_100072); L (M_tot_1); +∞ | 25 | 0 | *** |
| ligand_5954 | 1-Phenyl-1,2,3-triazole-4-carboxylic acid | HL | C9H8N3O2 | O=C(O)c1cn(-c2ccccc2)nn1 | −∞; HL (M_tot_1); (2.88, vlm_100053); L (M_tot_1); +∞ | 25 | 0 | *** |
| ligand_5959 | 2-(Carboxymethylaminomethyl)azole-4-sulfonic acid (N-(4-Sul… | H2L | C7H10N2O5S1 | O=C(O)CNCc1cc(S(=O)(=O)O)c[nH]1 | −∞; H2L (M_tot_1); (2.25, vlm_100094); HL (M_tot_1); (8.71, vlm_100093); L (M_tot_2); +∞ | 25 | 1 | *** |
| ligand_5769 | 2-Amino-2-methylpropanoic acid (2-Aminoisobutyric acid) | HL | C4H9N1O2 | CC(C)(N)C(=O)O | −∞; H2L (M_tot_1); (2.34, vlm_94845); HL (M_tot_2); (10.1, vlm_94835); L (M_tot_7); +∞ | 25 | 0.1 | *** |
| ligand_6002 | 2-Hydroxy-1,3-propylenediiminodibutanedioic acid (rac- or m… | H4L | C11H18N2O9 | O=C(O)CC(NCC(O)CNC(CC(=O)O)C(=O)O)C(=O)O | −∞; H4L (M_tot_1); (3.16, vlm_101238); H3L (M_tot_1); (4.08, vlm_101237); H2L (M_tot_1); (8.78, vlm_101236); HL (M_tot_1); (10.02, vlm_101235); L (M_tot_23); +∞ | 25 | 0.1 | *** |
| ligand_6001 | 2-Hydroxy-1,3-propylenediiminodipropanedioic acid | H4L | C9H14N2O9 | O=C(O)C(NCC(O)CNC(C(=O)O)C(=O)O)C(=O)O | −∞; H4L (M_tot_1); (2.41, vlm_101215); H3L (M_tot_1); (3.4, vlm_101214); H2L (M_tot_1); (8.9, vlm_101213); HL (M_tot_1); (10.4, vlm_101212); L (M_tot_8); +∞ | 25 | 0.1 | *** |
| ligand_5966 | 2-Hydroxy-3-(4-imidazolyl)propanoic acid | HL | C6H8N2O3 | O=C(O)C(O)Cc1c[nH]cn1 | −∞; H2L (M_tot_1); (3, vlm_100192); HL (M_tot_1); (7.31, vlm_100189); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5932 | 2-Indolecarboxylic acid | HL | C9H7N1O2 | O=C(O)c1cc2ccccc2[nH]1 | −∞; HL (M_tot_1); (3.68, vlm_99629); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_6012 | 3,3',5,5'-Tetramethyl-2,2'-dipyrrolmethene-4,4'-dicarboxyli… | H2L | C15H14N2O4 | CC1=C(C(=O)O)C(C)/C(=C/c2[nH]c(C)c(C(=O)O)c2C)=N1 | −∞; HL (M_tot_1); (-16.1, vlm_101398); L (M_tot_3); (3.6, vlm_101401); H3L (M_tot_1); (4.2, vlm_101400); H2L (M_tot_1); (8.03, vlm_101399); HL (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5940 | 3-(2-Hydroxyethylamino)propanoic acid | HL | C5H11N1O3 | O=C(O)CCNCCO | −∞; H2L (M_tot_1); (3.4, vlm_99853); HL (M_tot_1); (9.72, vlm_99852); L (M_tot_4); +∞ | 20 | 0.1 | *** |
| ligand_6026 | 3-(3-Hydroxy-4-oxo-1,4-dihydro-1-pyridinyl)propanoic acid (… | HL | C8H9N1O4 | O=C(O)CCn1ccc(=O)c(O)c1 | −∞; H3L (M_tot_1); (2.8, vlm_101708); H2L (M_tot_1); (3.84, vlm_101707); HL (M_tot_1); (8.79, vlm_101706); L (M_tot_5); +∞ | 37 | 0.15 | *** |
| ligand_5965 | 3-(4-Imidazolyl)propanoic acid | HL | C6H8N2O2 | O=C(O)CCc1c[nH]cn1 | −∞; H2L (M_tot_1); (3.83, vlm_100178); HL (M_tot_1); (7.44, vlm_100175); L (M_tot_4); +∞ | 25 | 0.1 | *** |
| ligand_5982 | 3-(Carboxymethyl)-2-oxo-1,4-diazacyclohexane-1-butanedioic … | H3L | C12H14N2O7 | O=C(O)CC1NCCN(C(CC(=O)O)C(=O)O)C1=O | −∞; H3L (M_tot_1); (3.38, vlm_100567); H2L (M_tot_1); (4.39, vlm_100553); HL (M_tot_4); (7, vlm_100539); L (M_tot_7); +∞ | 25 | 0.1 | *** |
| ligand_5788 | 3-Aminopropanoic acid (beta-Alanine) | HL | C3H7N1O2 | NCCC(=O)O | −∞; H2L (M_tot_1); (3.51, vlm_95222); HL (M_tot_3); (10.08, vlm_95204); L (M_tot_11); +∞ | 25 | 0.1 | *** |
| ligand_6004 | 4,7,10-Triazatridecanedioic acid [Iminobis(ethyleneiminopro… | H2L | C10H21N3O4 | O=C(O)CCNCCNCCNCCC(=O)O | −∞; H5L (M_tot_1); (2.98, vlm_101287); H4L (M_tot_1); (3.55, vlm_101286); H3L (M_tot_1); (4.4, vlm_101285); H2L (M_tot_1); (9.31, vlm_101284); HL (M_tot_1); (9.99, vlm_101283); L (M_tot_2); +∞ | 25 | 0.5 | *** |
| ligand_5797 | 4-Aminobutanoic acid | HL | C4H9N1O2 | NCCCC(=O)O | −∞; H2L (M_tot_1); (4.02, vlm_95418); HL (M_tot_5); (10.35, vlm_95408); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_5964 | 4-Imidazolylacetic acid | HL | C5H6N2O2 | O=C(O)Cc1c[nH]cn1 | −∞; H2L (M_tot_1); (3.1, vlm_100166); HL (M_tot_1); (7.26, vlm_100165); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_5875 | 5-Amino-3-thiapentanoic acid (S-2-Aminoethylmercaptoacetic … | HL | C5H11N1O2S1 | NCCSCC(=O)O | −∞; H2L (M_tot_1); (3.18, vlm_98012); HL (M_tot_2); (9.53, vlm_98009); L (M_tot_4); +∞ | 25 | 0.5 | *** |
| ligand_5798 | 5-Aminopentanoic acid | HL | C5H11N1O2 | NCCCCC(=O)O | −∞; H2L (M_tot_1); (4.27, vlm_95469); HL (M_tot_1); (10.766, vlm_95464); L (M_tot_3); +∞ | 25 | 0 | *** |
| ligand_5955 | 5-Methyl-1-phenyl-1,2,3-triazole-4-carboxylic acid | HL | C10H10N3O2 | Cc1c(C(=O)O)nnn1-c1ccccc1 | −∞; HL (M_tot_1); (3.73, vlm_100056); L (M_tot_1); +∞ | 25 | 0 | *** |
| ligand_6031 | 5-Thia-2,8-diazanonane-N,N'-diacetic acid | H2L | C10H20N2O4S1 | CN(CCSCCN(C)CC(=O)O)CC(=O)O | −∞; H4L (M_tot_1); (-1.3, vlm_101822); H3L (M_tot_1); (2.2, vlm_101819); H2L (M_tot_1); (8.24, vlm_101816); HL (M_tot_1); (9.3, vlm_101813); L (M_tot_10); +∞ | 25 | 0.1 | *** |
| ligand_5876 | 6-Amino-3-thiahexanoic acid (S-3-Aminopropylmercaptoacetic … | HL | C6H13N1O2S1 | NCCCSCC(=O)O | −∞; H2L (M_tot_1); (3.35, vlm_98044); HL (M_tot_2); (10.19, vlm_98041); L (M_tot_3); +∞ | 25 | 0.5 | *** |
| ligand_5877 | 6-Amino-4-thiahexanoic acid (S-2-Aminoethyl-3-mercaptopropa… | HL | C6H13N1O2S1 | NCCSCCC(=O)O | −∞; HL (M_tot_2); (9.54, vlm_98062); L (M_tot_4); +∞ | 20 | 0.1 | *** |
| ligand_5799 | 6-Aminohexanoic acid | HL | C6H13N1O2 | NCCCCCC(=O)O | −∞; H2L (M_tot_1); (4.373, vlm_95495); HL (M_tot_2); (10.804, vlm_95486); L (M_tot_4); +∞ | 25 | 0 | *** |
| ligand_6003 | 6-Oxa-3,9-diazaundecanedioic acid [Oxybis(ethyleneiminoacet… | H2L | C8H16N2O5 | O=C(O)CNCCOCCNCC(=O)O | −∞; H4L (M_tot_1); (-1.9, vlm_101277); H3L (M_tot_1); (2.6, vlm_101276); H2L (M_tot_1); (8.65, vlm_101275); HL (M_tot_1); (9.61, vlm_101274); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_5800 | 7-Aminoheptanoic acid | HL | C7H15N1O2 | NCCCCCCC(=O)O | −∞; H2L (M_tot_1); (4.502, vlm_95520); HL (M_tot_1); +∞ | 25 | 0 | *** |
| ligand_5760 | Aminoacetic acid (Glycine) | HL | C2H5N1O2 | NCC(=O)O | −∞; H2L (M_tot_1); (2.33, vlm_93627); HL (M_tot_20); (9.57, vlm_93606); L (M_tot_43); +∞ | 25 | 0.1 | *** |
| ligand_5801 | Aminopropanedioic acid (Aminomalonic acid) | H2L | C3H5N1O4 | NC(C(=O)O)C(=O)O | −∞; H3L (M_tot_1); (-1.8, vlm_95531); H2L (M_tot_1); (2.94, vlm_95527); HL (M_tot_1); (9.22, vlm_95523); L (M_tot_4); +∞ | 25 | 0.1 | *** |
| ligand_5981 | Bis(carboxymethyliminomethyl)phosphinic acid | H3L | C6H13N2O6P1 | O=C(O)CNCP(=O)(O)CNCC(=O)O | −∞; H3L (M_tot_1); (2.1, vlm_100537); H2L (M_tot_1); (6.55, vlm_100536); HL (M_tot_1); (9, vlm_100535); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_5857 | D-2-Amino-3-mercapto-3-methylbutanoic acid (Penicillamine) | H2L | C5H11N1O2S1 | CC(C)(S)[C@H](N)C(=O)O | −∞; H3L (M_tot_1); (-1.9, vlm_97563); H2L (M_tot_1); (7.96, vlm_97556); HL (M_tot_9); (10.67, vlm_97549); L (M_tot_14); +∞ | 25 | 0.1 | *** |
| ligand_5891 | D-3,3'-Dithiobis(2-amino-3-methylbutanoic acid) (Penicillam… | H2L | C10H20N2O4S2 | CC(C)(SSC(C)(C)C(N)C(=O)O)C(N)C(=O)O | −∞; H4L (M_tot_1); (-1.3, vlm_98611); H3L (M_tot_1); (2.04, vlm_98609); H2L (M_tot_1); (7.77, vlm_98606); HL (M_tot_5); (8.74, vlm_98603); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_5816 | D-3-Amino-3-carboxypropanohydroxamic acid (Asparagine hydro… | H2L | C4H8N2O4 | NC(CC(=O)NO)C(=O)O | −∞; H3L (M_tot_1); (2.18, vlm_96046); H2L (M_tot_1); (8.15, vlm_96045); HL (M_tot_1); (9.37, vlm_96044); L (M_tot_4); +∞ | 25 | 0.5 | *** |
| ligand_5768 | D-allo-2-Amino-3-methylpentanoic acid (D-allo-Isoleucine) | HL | C6H13N1O2 | CC[C@H](C)[C@@H](N)C(=O)O | −∞; H2L (M_tot_1); (2.2, vlm_94822); HL (M_tot_1); (9.62, vlm_94819); L (M_tot_3); +∞ | 25 | 0.1 | *** |
| ligand_5837 | D-gluco-2-Amino-3,4,5,6-tetrahydroxyhexanoic acid (D-Glucos… | HL | C6H13N1O6 | N[C@@H](C(=O)O)[C@@H](O)[C@H](O)[C@H](O)CO | −∞; H2L (M_tot_1); (2.2, vlm_96988); HL (M_tot_1); (9.08, vlm_96985); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_5924 | DL-(4-Amino-4-carboxybutyl)trimethylammonium ion (N(5)-Trim… | HL | C8H19N2O2/+ | C[N+](C)(C)CCCC(N)C(=O)O | −∞; H2L (M_tot_1); (-1.8, vlm_99448); HL (M_tot_1); (8.7, vlm_99447); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_5942 | DL-1,3-Thiazolidine-4-carboxylic acid (DL-Thiaproline) | HL | C4H7N1O2S1 | O=C(O)C1CSCN1 | −∞; HL (M_tot_1); (-6.11, vlm_99933); L (M_tot_8); (-1.5, vlm_99935); HL (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6051 | DL-1-Ethylethylenedinitrilotetraacetic acid N,N'-diamide | H2L | C12H22N4O6 | CCC(CN(CC(N)=O)CC(=O)O)N(CC(N)=O)CC(=O)O | −∞; H3L (M_tot_1); (-1.7, vlm_102336); H2L (M_tot_2); (3.7, vlm_102335); HL (M_tot_2); (7.58, vlm_102334); L (M_tot_9); +∞ | 37 | 0.15 | *** |
| ligand_6050 | DL-1-Methylethylenedinitrilotetraacetic acid N,N'-diamide | H2L | C11H20N4O6 | CC(CN(CC(N)=O)CC(=O)O)N(CC(N)=O)CC(=O)O | −∞; H3L (M_tot_1); (-1.7, vlm_102305); H2L (M_tot_1); (-1.5, vlm_102306); H3L (M_tot_1); (3.8, vlm_102304); HL (M_tot_1); (7.56, vlm_102303); L (M_tot_10); +∞ | 37 | 0.15 | *** |
| ligand_5993 | DL-2,3-Diaminopropanoic-N,N'-dipropanedioic acid | H4L | C9H12N2O10 | O=C(O)C(CNC(C(=O)O)C(=O)O)NC(C(=O)O)C(=O)O | −∞; H5L (M_tot_1); (-1.6, vlm_101014); H4L (M_tot_1); (2.45, vlm_101013); H3L (M_tot_1); (2.98, vlm_101012); H2L (M_tot_1); (6.55, vlm_101011); HL (M_tot_1); (9.71, vlm_101010); L (M_tot_26); +∞ | 25 | 0.1 | *** |
| ligand_5889 | DL-2,6-Diamino-5-hydroxyhexanoic acid | HL | C6H12N2O5 | NCC(O)CCC(N)C(=O)O | −∞; H3L (M_tot_1); (2.1, vlm_98513); H2L (M_tot_1); (8.84, vlm_98509); HL (M_tot_7); (9.79, vlm_98505); L (M_tot_3); +∞ | 25 | 0.1 | *** |
| ligand_5888 | DL-2,7-Diaminooctanedioic acid | HL | C8H16N2O4 | NC(CCCCC(N)C(=O)O)C(=O)O | −∞; H4L (M_tot_1); (-1.8, vlm_98498); H3L (M_tot_1); (2.62, vlm_98497); H2L (M_tot_1); (9.23, vlm_98496); HL (M_tot_2); (9.89, vlm_98495); L (M_tot_2); +∞ | 20 | 0.1 | *** |
| ligand_5878 | DL-2-(Acetylamino)-3-(2-aminoethylthio)propanoic acid | HL | C7H14N2O3S1 | CC(=O)NC(CSCCN)C(=O)O | −∞; HL (M_tot_1); (9.39, vlm_98094); L (M_tot_1); +∞ | 20 | 0.1 | *** |
| ligand_5825 | DL-2-Amino-2-(3,4-dihydroxyphenyl)acetic acid (DOPG) | H3L | C8H9N1O4 | NC(C(=O)O)c1ccc(O)c(O)c1 | −∞; HL (M_tot_1); (-13.6, vlm_96379); L (M_tot_1); (2, vlm_96382); H3L (M_tot_1); (8.56, vlm_96381); H2L (M_tot_2); (9.75, vlm_96380); HL (M_tot_1); +∞ | 25 | 1 | *** |
| ligand_5805 | DL-2-Amino-2-methylpentanedioic acid (2-Methylglutamic acid) | H2L | C6H11N1O4 | C[C@](N)(CCC(=O)O)C(=O)O | −∞; H2L (M_tot_1); (4.05, vlm_95867); HL (M_tot_1); (9.72, vlm_95866); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_5783 | DL-2-Amino-3-(2-chlorophenyl)propanoic acid (DL-3-(2-Chloro… | HL | C9H10Cl1N1O2 | N[C@@H](Cc1ccccc1Cl)C(=O)O | −∞; H2L (M_tot_1); (2.23, vlm_95183); HL (M_tot_1); (8.94, vlm_95182); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5780 | DL-2-Amino-3-(2-fluorophenyl)propanoic acid (DL-3-(2-Fluoro… | HL | C9H10F1N1O2 | N[C@@H](Cc1ccccc1F)C(=O)O | −∞; H2L (M_tot_1); (2.12, vlm_95166); HL (M_tot_1); (9.01, vlm_95163); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5817 | DL-2-Amino-3-(2-hydroxyphenyl)propanoic acid (o-Tyrosine) | H2L | C9H11N1O3 | NC(Cc1ccccc1O)C(=O)O | −∞; H3L (M_tot_1); (2.41, vlm_96078); H2L (M_tot_1); (8.67, vlm_96074); HL (M_tot_6); (11.01, vlm_96070); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_5860 | DL-2-Amino-3-(2-mercaptoimidazo-4-yl)propanoic acid (Thiohi… | H2L | C6H9N3O2S1 | NC(Cc1cnc(S)[nH]1)C(=O)O | −∞; HL (M_tot_1); (-11.77, vlm_97676); L (M_tot_9); (8.59, vlm_97679); HL (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5855 | DL-2-Amino-3-(3,4-dimethoxyphenyl)propanoic acid (3,4-Dimet… | HL | C11H15N1O4 | COc1ccc(C[C@H](N)C(=O)O)cc1OC | −∞; H2L (M_tot_1); (2.37, vlm_97370); HL (M_tot_1); (9.02, vlm_97369); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5784 | DL-2-Amino-3-(3-chlorophenyl)propanoic acid (DL-3-(3-Chloro… | HL | C9H10Cl1N1O2 | N[C@@H](Cc1cccc(Cl)c1)C(=O)O | −∞; H2L (M_tot_1); (2.17, vlm_95185); HL (M_tot_1); (8.91, vlm_95184); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5781 | DL-2-Amino-3-(3-fluorophenyl)propanoic acid (DL-3-(3-Fluoro… | HL | C9H10F1N1O2 | N[C@@H](Cc1cccc(F)c1)C(=O)O | −∞; H2L (M_tot_1); (2.1, vlm_95172); HL (M_tot_1); (8.98, vlm_95169); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5822 | DL-2-Amino-3-(3-hydroxy-4-methoxyphenyl)propanoic acid | H2L | C10H13N1O4 | COc1ccc(CC(N)C(=O)O)cc1O | −∞; H3L (M_tot_1); (2.23, vlm_96366); H2L (M_tot_1); (8.84, vlm_96365); HL (M_tot_1); (10.12, vlm_96364); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5818 | DL-2-Amino-3-(3-hydroxyphenyl)propanoic acid (m-Tyrosine) | H2L | C9H11N1O3 | N[C@@H](Cc1cccc(O)c1)C(=O)O | −∞; H3L (M_tot_1); (2.22, vlm_96149); H2L (M_tot_1); (8.95, vlm_96145); HL (M_tot_6); (10.04, vlm_96141); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5921 | DL-2-Amino-3-(4-(aminomethyl)phenyl)propanoic acid | HL | C10H13N2O2 | NCc1ccc(CC(N)C(=O)O)cc1 | −∞; H2L (M_tot_1); (8.4, vlm_99444); HL (M_tot_1); (8.42, vlm_99443); L (M_tot_1); +∞ | 37 | 0.15 | *** |
| ligand_5922 | DL-2-Amino-3-(4-(dimethylamino)phenyl)propanoic acid | HL | C11H15N1O2 | CN(C)c1ccc(CC(N)C(=O)O)cc1 | −∞; HL (M_tot_1); (8.86, vlm_99445); L (M_tot_1); +∞ | 37 | 0.15 | *** |
| ligand_5920 | DL-2-Amino-3-(4-aminophenyl)propanoic acid | HL | C9H11N1O2 | Nc1ccc(CC(N)C(=O)O)cc1 | −∞; HL (M_tot_1); (8.93, vlm_99442); L (M_tot_1); +∞ | 37 | 0.15 | *** |
| ligand_5785 | DL-2-Amino-3-(4-chlorophenyl)propanoic acid (DL-3-(4-Chloro… | HL | C9H10Cl1N1O2 | N[C@@H](Cc1ccc(Cl)cc1)C(=O)O | −∞; H2L (M_tot_1); (2.08, vlm_95187); HL (M_tot_1); (8.96, vlm_95186); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5782 | DL-2-Amino-3-(4-fluorophenyl)propanoic acid (DL-3-(4-Fluoro… | HL | C9H10F1N1O2 | N[C@@H](Cc1ccc(F)cc1)C(=O)O | −∞; H2L (M_tot_1); (2.13, vlm_95178); HL (M_tot_1); (9.05, vlm_95175); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5919 | DL-2-Amino-3-(4-guanidinomethylphenyl)propanoic acid | HL | C12H16N4O2 | N=C(N)NCc1ccc(CC(N)C(=O)O)cc1 | −∞; H2L (M_tot_1); (8.83, vlm_99441); HL (M_tot_1); +∞ | 37 | 0.15 | *** |
| ligand_5918 | DL-2-Amino-3-(4-guanidinophenyl)propanoic acid | HL | C10H14N4O2 | N=C(N)Nc1ccc(CC(N)C(=O)O)cc1 | −∞; H2L (M_tot_1); (8.44, vlm_99440); HL (M_tot_1); (10.91, vlm_99439); L (M_tot_1); +∞ | 37 | 0.15 | *** |
| ligand_5823 | DL-2-Amino-3-(4-hydroxy-3-methoxyphenyl)propanoic acid | H2L | C10H13N1O4 | COc1cc(CC(N)C(=O)O)ccc1O | −∞; H3L (M_tot_1); (2.13, vlm_96369); H2L (M_tot_1); (8.78, vlm_96368); HL (M_tot_1); (10.14, vlm_96367); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5912 | DL-2-Amino-3-(5-hydroxo-4-oxo-1,4-dihydro-2-pyridinyl)propa… | HL | C8H10N2O4 | NC(Cc1cc(=O)c(O)c[nH]1)C(=O)O | −∞; H4L (M_tot_1); (-1.3, vlm_99290); H3L (M_tot_1); (3.01, vlm_99289); H2L (M_tot_1); (7.72, vlm_99288); HL (M_tot_2); (9.17, vlm_99287); L (M_tot_4); +∞ | 37 | 0.15 | *** |
| ligand_5913 | DL-2-Amino-3-(5-hydroxo-6-oxo-1,6-dihydro-2-pyridinyl)propa… | HL | C8H10N2O4 | NC(Cc1ccc(O)c(=O)[nH]1)C(=O)O | −∞; H3L (M_tot_1); (-1.9, vlm_99310); H2L (M_tot_1); (7.85, vlm_99309); HL (M_tot_3); (9.01, vlm_99308); L (M_tot_5); +∞ | 37 | 0.15 | *** |
| ligand_5909 | DL-2-Amino-3-(5-hydroxy-3-indolyl)propanoic acid (5-Hydroxy… | HL | C11H12N2O3 | NC(Cc1c[nH]c2ccc(O)cc12)C(=O)O | −∞; H3L (M_tot_1); (2.51, vlm_99238); H2L (M_tot_1); (9.49, vlm_99237); HL (M_tot_6); (10.54, vlm_99236); L (M_tot_1); +∞ | 20 | 0.5 | *** |
| ligand_5910 | DL-2-Amino-3-(6-oxo-1,6-dihydro-2-pyridinyl)propanoic acid | HL | C8H10N2O3 | NC(Cc1cccc(=O)[nH]1)C(=O)O | −∞; H2L (M_tot_1); (-1.8, vlm_99252); HL (M_tot_1); (7.8, vlm_99251); L (M_tot_3); (11.7, vlm_99250); H-1L (M_tot_1); +∞ | 37 | 0.15 | *** |
| ligand_5812 | DL-2-Amino-3-(phenylphospho)propanoic acid | H3L | C9H12N1O6P1 | NC(COP(=O)(O)Oc1ccccc1)C(=O)O | −∞; H2L (M_tot_1); (2.13, vlm_95973); HL (M_tot_1); (8.79, vlm_95972); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5779 | DL-2-Amino-3-chlorobutanoic acid | HL | C4H8Cl1N1O2 | CC(Cl)C(N)C(=O)O | −∞; H2L (M_tot_1); (-1.5, vlm_95156); HL (M_tot_1); (8.07, vlm_95155); L (M_tot_4); +∞ | 25 | 0.1 | *** |
| ligand_5778 | DL-2-Amino-3-chloropropanoic acid (3-Chloroalanine) | HL | C3H6Cl1N1O2 | N[C@@H](CCl)C(=O)O | −∞; HL (M_tot_1); (8.18, vlm_95145); L (M_tot_4); +∞ | 25 | 0.1 | *** |

---
