# Q5.2.2 — Tool Results (batch 3)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Fe(III), Fe(II), Al(III), Ga(III), Cu(II), Cu(I), Zn(II), Cd(II), Hg(II), Ca(II), Mg(II)",
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
  "name": "transferrin, albumin, metallothionein, ferritin, ceruloplasmin",
  "limit": 20
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

### Step 7: `search_citations`
**Args:**
```json
{
  "where": "(la.citation LIKE '%transferrin%' OR la.citation LIKE '%serotransferrin%' OR la.citation LIKE '%apo-transferrin%' OR la.citation LIKE '%albumin%' OR la.citation LIKE '%metallothionein%' OR la.citation LIKE '%ferritin%' OR la.citation LIKE '%ceruloplasmin%' OR la.citation LIKE '%protein binding%')",
  "order_by": "la.shortcut",
  "limit": 20
}
```

[summary]
## search_citations

*(no results)*

---

### Step 8: `search_pka_ligands`
**Args:**
```json
{
  "where": "(lc.ligand_name_SRD LIKE '%transferrin%' OR lc.ligand_name_SRD LIKE '%albumin%' OR lc.ligand_name_SRD LIKE '%metallothionein%' OR lc.ligand_name_SRD LIKE '%ferritin%' OR lc.ligand_name_SRD LIKE '%ceruloplasmin%' OR lc.ligand_name_SRD LIKE '%pept%' OR lc.ligand_class_name LIKE '%protein%' OR lc.ligand_class_name LIKE '%pept%')",
  "order_by": "lc.ligand_name_SRD",
  "limit": 50
}
```

[summary]
## search_pka_ligands — 50 row(s)

| ligand_id | ligand_name | HxL_def | formula | smiles | pH_ladder | T°C_range | I(M)_range | similarity_score |
|-----------|-------------|---------|---------|--------|-----------|-----------|------------|------------------|
| ligand_6471 | 2-Methylalanyl-2-methylalanine | HL | C8H16N2O3 | CC(C)(N)C(=O)NC(C)(C)C(=O)O | −∞; H2L (M_tot_1); (3.67, vlm_115368); HL (M_tot_1); (8.26, vlm_115367); L (M_tot_3); +∞ | 25 | 0.1 | *** |
| ligand_6559 | 2-Methylalanyl-2-methylalanyl-2-methylalanine | HL | C12H23N3O4 | CC(C)(N)C(=O)NC(C)(C)C(=O)NC(C)(C)C(=O)O | −∞; H2L (M_tot_1); (3.82, vlm_116228); HL (M_tot_1); (8.11, vlm_116227); L (M_tot_3); +∞ | 25 | 0.1 | *** |
| ligand_6603 | 2-Methylalanyl-2-methylalanyl-2-methylalanyl-2-methylalanine | HL | C16H30N4O5 | CC(C)(N)C(=O)NC(C)(C)C(=O)NC(C)(C)C(=O)NC(C)(C)C(=O)O | −∞; H2L (M_tot_1); (3.8, vlm_116806); HL (M_tot_1); (7.78, vlm_116805); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_6602 | 2-Methylalanyl-2-methylalanyl-2-methylalanylglycine | HL | C14H26N4O5 | CC(C)(N)C(=O)NC(C)(C)C(=O)NC(C)(C)C(=O)NCC(=O)O | −∞; H2L (M_tot_1); (3.46, vlm_116800); HL (M_tot_1); (8.33, vlm_116799); L (M_tot_2); +∞ | 25 | 0.1 | *** |
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
| ligand_6558 | DL-Alanyl-2-methylalanyl-2-methylalanine | HL | C11H21N3O4 | CC(N)C(=O)NC(C)(C)C(=O)NC(C)(C)C(=O)O | −∞; H2L (M_tot_1); (3.95, vlm_116223); HL (M_tot_1); (8.29, vlm_116222); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_6412 | DL-Phosphoserylglycine (DL-Serylglycine dihydrogenphosphate) | H3L | C5H11N2O7P1 | NC(COP(=O)(O)O)C(=O)NCC(=O)O | −∞; H3L (M_tot_1); (3.16, vlm_114515); H2L (M_tot_1); (5.42, vlm_114514); HL (M_tot_1); (8.01, vlm_114513); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_6557 | Glycyl-2-methylalanylglycine | HL | C8H15N3O4 | CC(C)(NC(=O)CN)C(=O)NCC(=O)O | −∞; H2L (M_tot_1); (3.33, vlm_116217); HL (M_tot_1); (8.2, vlm_116216); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_6374 | Glycyl-4-aminobutanoic acid | HL | C6H12N2O3 | NCC(=O)NCCCC(=O)O | −∞; H2L (M_tot_1); (4.22, vlm_113652); HL (M_tot_1); (8.12, vlm_113642); L (M_tot_3); +∞ | 25 | 0.1 | *** |
| ligand_6549 | Glycyl-D-leucyl-L-leucine | HL | C14H27N3O4 | CC(C)C[C@H](NC(=O)[C@@H](CC(C)C)NC(=O)CN)C(=O)O | −∞; HL (M_tot_1); (8.15, vlm_116170); L (M_tot_2); +∞ | 25 | 0.1 | *** |

---

### Step 9: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_name_SRD LIKE '%transferrin%' OR c.ligand_name_SRD LIKE '%albumin%' OR c.ligand_name_SRD LIKE '%metallothionein%' OR c.ligand_name_SRD LIKE '%ferritin%' OR c.ligand_name_SRD LIKE '%ceruloplasmin%' OR c.ligand_name_SRD LIKE '%pept%' OR c.ligand_class_name LIKE '%protein%' OR c.ligand_class_name LIKE '%pept%')",
  "order_by": "c.ligand_name_SRD",
  "limit": 50
}
```

[summary]
## search_stability — 50 row(s)

### logK — 18 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_112 | Ni^[2+] | ligand_6471 | 2-Methylalanyl-2-methylalan… | HL | CC(C)(N)C(=O)NC(C)(C)C(=O)O | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_6603 | 2-Methylalanyl-2-methylalan… | HL | CC(C)(N)C(=O)NC(C)(C)C(=O)NC(C)(C)C(=O)NC(C)(C)C(=O)O | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_6602 | 2-Methylalanyl-2-methylalan… | HL | CC(C)(N)C(=O)NC(C)(C)C(=O)NC(C)(C)C(=O)NCC(=O)O | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_6471 | 2-Methylalanyl-2-methylalan… | HL | CC(C)(N)C(=O)NC(C)(C)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_6559 | 2-Methylalanyl-2-methylalan… | HL | CC(C)(N)C(=O)NC(C)(C)C(=O)NC(C)(C)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_6471 | 2-Methylalanyl-2-methylalan… | HL | CC(C)(N)C(=O)NC(C)(C)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_6559 | 2-Methylalanyl-2-methylalan… | HL | CC(C)(N)C(=O)NC(C)(C)C(=O)NC(C)(C)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_6559 | 2-Methylalanyl-2-methylalan… | HL | CC(C)(N)C(=O)NC(C)(C)C(=O)NC(C)(C)C(=O)O | 2 | 2 | 25 | 0.1~1 | *** | 2 |
| metal_68 | H^[+] | ligand_6603 | 2-Methylalanyl-2-methylalan… | HL | CC(C)(N)C(=O)NC(C)(C)C(=O)NC(C)(C)C(=O)NC(C)(C)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_6602 | 2-Methylalanyl-2-methylalan… | HL | CC(C)(N)C(=O)NC(C)(C)C(=O)NC(C)(C)C(=O)NCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_6542 | D-Alanyl-D-alanyl-D-alanine | HL | C[C@@H](N)C(=O)N[C@H](C)C(=O)N[C@H](C)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_6541 | D-Alanyl-L-alanyl-L-alanine | HL | C[C@H](NC(=O)[C@H](C)NC(=O)[C@@H](C)N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_6600 | D-Alanyl-L-alanyl-L-alanyl-… | HL | C[C@H](NC(=O)[C@H](C)NC(=O)[C@H](C)NC(=O)[C@@H](C)N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_6428 | D-Alanyl-L-leucine | HL | CC(C)C[C@H](NC(=O)[C@@H](C)N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_6428 | D-Alanyl-L-leucine | HL | CC(C)C[C@H](NC(=O)[C@@H](C)N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_6428 | D-Alanyl-L-leucine | HL | CC(C)C[C@H](NC(=O)[C@@H](C)N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_94 | Mn^[2+] | ligand_6428 | D-Alanyl-L-leucine | HL | CC(C)C[C@H](NC(=O)[C@@H](C)N)C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_6428 | D-Alanyl-L-leucine | HL | CC(C)C[C@H](NC(=O)[C@@H](C)N)C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |

### ΔH — 3 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_6428 | D-Alanyl-L-leucine | HL | CC(C)C[C@H](NC(=O)[C@@H](C)N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_6559 | 2-Methylalanyl-2-methylalan… | HL | CC(C)(N)C(=O)NC(C)(C)C(=O)NC(C)(C)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6559 | 2-Methylalanyl-2-methylalan… | HL | CC(C)(N)C(=O)NC(C)(C)C(=O)NC(C)(C)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |

### ΔS — 3 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_6428 | D-Alanyl-L-leucine | HL | CC(C)C[C@H](NC(=O)[C@@H](C)N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_6559 | 2-Methylalanyl-2-methylalan… | HL | CC(C)(N)C(=O)NC(C)(C)C(=O)NC(C)(C)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6559 | 2-Methylalanyl-2-methylalan… | HL | CC(C)(N)C(=O)NC(C)(C)C(=O)NC(C)(C)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |

---
