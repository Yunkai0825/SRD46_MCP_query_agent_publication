# Q5.2.2 — Tool Results (batch 4)

### Step 2: `search_ligands`
**Args:**
```json
{
  "name": "transferrin",
  "limit": 50
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "apotransferrin",
  "limit": 50
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 4: `search_ligands`
**Args:**
```json
{
  "name": "lactoferrin",
  "limit": 50
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 5: `search_ligands`
**Args:**
```json
{
  "name": "ovotransferrin",
  "limit": 50
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 6: `search_ligands`
**Args:**
```json
{
  "name": "albumin",
  "limit": 50
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 7: `search_ligands`
**Args:**
```json
{
  "name": "metallothionein",
  "limit": 50
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 9: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_name_SRD LIKE '%transferrin%' OR c.ligand_name_SRD LIKE '%apotransferrin%' OR c.ligand_name_SRD LIKE '%lactoferrin%' OR c.ligand_name_SRD LIKE '%ovotransferrin%' OR c.ligand_name_SRD LIKE '%albumin%' OR c.ligand_name_SRD LIKE '%serum albumin%' OR c.ligand_name_SRD LIKE '%metallothionein%' OR c.ligand_name_SRD LIKE '%ferritin%' OR c.ligand_class_name LIKE '%protein%')",
  "order_by": "c.ligand_name_SRD ASC",
  "limit": 300
}
```

[summary]
## search_stability

*(no results)*

---

### Step 10: `search_citations`
**Args:**
```json
{
  "where": "(la.citation LIKE '%transferrin%' OR la.citation LIKE '%albumin%' OR la.citation LIKE '%metallothionein%' OR la.citation LIKE '%ferritin%' OR la.citation LIKE '%lactoferrin%' OR la.citation LIKE '%ovotransferrin%' OR la.citation LIKE '%human serum albumin%' OR la.citation LIKE '%bovine serum albumin%' OR la.citation LIKE '%HSA%' OR la.citation LIKE '%BSA%')",
  "order_by": "la.shortcut ASC",
  "limit": 200
}
```

[summary]
## search_citations — 2 row(s)

| example_vlm_id | vlm_count | lit_id | shortcut | citation |
|----------------|-----------|--------|----------|----------|
| vlm_99994 | 100 | lit_1716 | 80OO | T. Ohsaka, N. Oyama, and H. Matsuda, Bull. Chem. Soc. Japan, 1980, 53, 3601 |
| vlm_138105 | 22 | lit_12764 | 83HOO | K. Hayashi, T. Ohsawa, K. Okamoto, J. Hidaka, and H. Einaga, J. Coord. Chem., 1… |

---

### Step 11: `search_stability`
**Args:**
```json
{
  "where": "((c.ligand_name_SRD LIKE '%histidine%' OR c.ligand_name_SRD LIKE '%imidazole%') AND (c.metal_name_SRD LIKE '%Copper%' OR c.metal_name_SRD LIKE '%Zinc%'))",
  "order_by": "s.temperature_c ASC, c.ligand_name_SRD ASC",
  "limit": 200
}
```

[summary]
## search_stability — 200 row(s)

### logK — 39 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 15 | 3 | 25 | 0~3 | *** | 5 |
| metal_33 | Co^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 13 | 5 | 25 | 0.1~3 | *** | 5 |
| metal_112 | Ni^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 13 | 5 | 25 | 0.1~3 | *** | 5 |
| metal_33 | Co^[2+] | ligand_5906 | L-2-Amino-3-(2,5-diiodo-4-i… | HL | N[C@@H](Cc1nc(I)[nH]c1I)C(=O)O | 5 | 5 | 25 | 0.5 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_5906 | L-2-Amino-3-(2,5-diiodo-4-i… | HL | N[C@@H](Cc1nc(I)[nH]c1I)C(=O)O | 5 | 5 | 25 | 0.5 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5906 | L-2-Amino-3-(2,5-diiodo-4-i… | HL | N[C@@H](Cc1nc(I)[nH]c1I)C(=O)O | 5 | 5 | 25 | 0.5 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 5 | 2 | 25 | 0.1~3 | *** | 3 |
| metal_68 | H^[+] | ligand_5906 | L-2-Amino-3-(2,5-diiodo-4-i… | HL | N[C@@H](Cc1nc(I)[nH]c1I)C(=O)O | 4 | 4 | 25 | 0.5 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_5906 | L-2-Amino-3-(2,5-diiodo-4-i… | HL | N[C@@H](Cc1nc(I)[nH]c1I)C(=O)O | 4 | 4 | 25 | 0.5 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_5906 | L-2-Amino-3-(2,5-diiodo-4-i… | HL | N[C@@H](Cc1nc(I)[nH]c1I)C(=O)O | 4 | 4 | 25 | 0.5 | *** | 1 |
| metal_94 | Mn^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 4 | 2 | 25 | 0.1~3 | *** | 2 |
| metal_42 | Cu^[+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_5915 | L-2-Amino-3-(2-pyridyl)prop… | HL | N[C@@H](Cc1ccccn1)C(=O)O | 3 | 2 | 25 | 0.1 | *** | 2 |
| metal_112 | Ni^[2+] | ligand_5915 | L-2-Amino-3-(2-pyridyl)prop… | HL | N[C@@H](Cc1ccccn1)C(=O)O | 3 | 2 | 25 | 0.1 | *** | 2 |
| metal_41 | Cu^[2+] | ligand_5915 | L-2-Amino-3-(2-pyridyl)prop… | HL | N[C@@H](Cc1ccccn1)C(=O)O | 3 | 2 | 25 | 0.1 | *** | 2 |
| metal_208 | Zn^[2+] | ligand_5915 | L-2-Amino-3-(2-pyridyl)prop… | HL | N[C@@H](Cc1ccccn1)C(=O)O | 3 | 2 | 25 | 0.1 | *** | 2 |
| metal_112 | Ni^[2+] | ligand_5777 | L-2-Amino-3-phenylpropanoic… | HL | N[C@@H](Cc1ccccc1)C(=O)O | 2 | 2 | 10 | 0 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_5777 | L-2-Amino-3-phenylpropanoic… | HL | N[C@@H](Cc1ccccc1)C(=O)O | 2 | 2 | 10 | 0 | *** | 1 |
| metal_68 | H^[+] | ligand_5860 | DL-2-Amino-3-(2-mercaptoimi… | H2L | NC(Cc1cnc(S)[nH]1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_94 | Mn^[2+] | ligand_5860 | DL-2-Amino-3-(2-mercaptoimi… | H2L | NC(Cc1cnc(S)[nH]1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5860 | DL-2-Amino-3-(2-mercaptoimi… | H2L | NC(Cc1cnc(S)[nH]1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_5860 | DL-2-Amino-3-(2-mercaptoimi… | H2L | NC(Cc1cnc(S)[nH]1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_5860 | DL-2-Amino-3-(2-mercaptoimi… | H2L | NC(Cc1cnc(S)[nH]1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5860 | DL-2-Amino-3-(2-mercaptoimi… | H2L | NC(Cc1cnc(S)[nH]1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_5860 | DL-2-Amino-3-(2-mercaptoimi… | H2L | NC(Cc1cnc(S)[nH]1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_5915 | L-2-Amino-3-(2-pyridyl)prop… | HL | N[C@@H](Cc1ccccn1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_106 | Na^[+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 2 | 1 | 25 | 0~0.1 | *** | 2 |
| metal_19 | Be^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_110 | Nd^[3+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 2 | 2 | 25 | 3 | *** | 1 |
| metal_68 | H^[+] | ligand_5777 | L-2-Amino-3-phenylpropanoic… | HL | N[C@@H](Cc1ccccc1)C(=O)O | 1 | 1 | 10 | 0 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5777 | L-2-Amino-3-phenylpropanoic… | HL | N[C@@H](Cc1ccccc1)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5777 | L-2-Amino-3-phenylpropanoic… | HL | N[C@@H](Cc1ccccc1)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_5860 | DL-2-Amino-3-(2-mercaptoimi… | H2L | NC(Cc1cnc(S)[nH]1)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_5860 | DL-2-Amino-3-(2-mercaptoimi… | H2L | NC(Cc1cnc(S)[nH]1)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_5947 | DL-[1-Carboxy-2-(2-mercapto… | H2L | C[N+](C)(C)C(Cc1cnc(S)[nH]1)C(=O)O.[Cl-] | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_93 | MeHg^[+] | ligand_5947 | DL-[1-Carboxy-2-(2-mercapto… | H2L | C[N+](C)(C)C(Cc1cnc(S)[nH]1)C(=O)O.[Cl-] | 1 | 1 | 25 | 0.5 | *** | 1 |

### ΔH — 12 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 12 | 3 | 25 | 0~3 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 5 | 2 | 25 | 0.1~3 | *** | 0 |
| metal_33 | Co^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 4 | 2 | 25 | 0.1~3 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 3 | 2 | 25 | 0.1~3 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_5777 | L-2-Amino-3-phenylpropanoic… | HL | N[C@@H](Cc1ccccc1)C(=O)O | 2 | 2 | 10 | 0 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5777 | L-2-Amino-3-phenylpropanoic… | HL | N[C@@H](Cc1ccccc1)C(=O)O | 2 | 2 | 10 | 0 | *** | 0 |
| metal_68 | H^[+] | ligand_5860 | DL-2-Amino-3-(2-mercaptoimi… | H2L | NC(Cc1cnc(S)[nH]1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 2 | 2 | 25 | 3 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 2 | 2 | 25 | 3 | *** | 0 |
| metal_68 | H^[+] | ligand_5777 | L-2-Amino-3-phenylpropanoic… | HL | N[C@@H](Cc1ccccc1)C(=O)O | 1 | 1 | 10 | 0 | *** | 0 |
| metal_68 | H^[+] | ligand_5947 | DL-[1-Carboxy-2-(2-mercapto… | H2L | C[N+](C)(C)C(Cc1cnc(S)[nH]1)C(=O)O.[Cl-] | 1 | 1 | 25 | 0.1 | *** | 0 |

### ΔS — 9 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 12 | 3 | 25 | 0~3 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 5 | 2 | 25 | 0.1~3 | *** | 0 |
| metal_33 | Co^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 4 | 2 | 25 | 0.1~3 | *** | 0 |
| metal_68 | H^[+] | ligand_5860 | DL-2-Amino-3-(2-mercaptoimi… | H2L | NC(Cc1cnc(S)[nH]1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 2 | 2 | 25 | 3 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 2 | 2 | 25 | 3 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 2 | 1 | 25 | 0.1~3 | *** | 0 |
| metal_68 | H^[+] | ligand_5947 | DL-[1-Carboxy-2-(2-mercapto… | H2L | C[N+](C)(C)C(Cc1cnc(S)[nH]1)C(=O)O.[Cl-] | 1 | 1 | 25 | 0.1 | *** | 0 |

---

### Step 12: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_name_SRD LIKE '%cysteine%' AND (c.metal_name_SRD LIKE '%Copper%' OR c.metal_name_SRD LIKE '%Zinc%'))",
  "order_by": "s.temperature_c ASC, c.ligand_name_SRD ASC",
  "limit": 200
}
```

[summary]
## search_stability — 200 row(s)

### logK — 40 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 12 | 2 | 10~25 | 0~5 | *** | 6 |
| metal_112 | Ni^[2+] | ligand_5885 | L-2,4-Diaminobutanoic acid | HL | NCCC(N)C(=O)O | 12 | 10 | 25 | 0.1 | *** | 2 |
| metal_33 | Co^[2+] | ligand_5883 | L-2,3-Diaminopropanoic acid | HL | NCC(N)C(=O)O | 7 | 5 | 25 | 0.1~0.5 | *** | 2 |
| metal_41 | Cu^[2+] | ligand_5888 | DL-2,7-Diaminooctanedioic a… | HL | NC(CCCCC(N)C(=O)O)C(=O)O | 6 | 6 | 20 | 0.1 | *** | 1 |
| metal_74 | In^[3+] | ligand_5856 | L-2-Amino-3-mercaptopropano… | H2L | N[C@@H](CS)C(=O)O | 6 | 6 | 22 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_5883 | L-2,3-Diaminopropanoic acid | HL | NCC(N)C(=O)O | 6 | 6 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_5883 | L-2,3-Diaminopropanoic acid | HL | NCC(N)C(=O)O | 6 | 6 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5883 | L-2,3-Diaminopropanoic acid | HL | NCC(N)C(=O)O | 6 | 6 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_5885 | L-2,4-Diaminobutanoic acid | HL | NCCC(N)C(=O)O | 6 | 5 | 25 | 0.1 | *** | 2 |
| metal_112 | Ni^[2+] | ligand_5856 | L-2-Amino-3-mercaptopropano… | H2L | N[C@@H](CS)C(=O)O | 5 | 5 | 20 | 0.1 | *** | 2 |
| metal_41 | Cu^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 5 | 3 | 25 | 0.1~5 | *** | 2 |
| metal_68 | H^[+] | ligand_5883 | L-2,3-Diaminopropanoic acid | HL | NCC(N)C(=O)O | 5 | 3 | 25 | 0.1~0.5 | *** | 2 |
| metal_71 | Hg^[2+] | ligand_5883 | L-2,3-Diaminopropanoic acid | HL | NCC(N)C(=O)O | 5 | 5 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_5888 | DL-2,7-Diaminooctanedioic a… | HL | NC(CCCCC(N)C(=O)O)C(=O)O | 4 | 4 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5856 | L-2-Amino-3-mercaptopropano… | H2L | N[C@@H](CS)C(=O)O | 4 | 4 | 20 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_5885 | L-2,4-Diaminobutanoic acid | HL | NCCC(N)C(=O)O | 4 | 3 | 25 | 0.1 | *** | 2 |
| metal_208 | Zn^[2+] | ligand_5778 | DL-2-Amino-3-chloropropanoi… | HL | N[C@@H](CCl)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_64 | Ga^[3+] | ligand_5778 | DL-2-Amino-3-chloropropanoi… | HL | N[C@@H](CCl)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_37 | Cr^[3+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_5885 | L-2,4-Diaminobutanoic acid | HL | NCCC(N)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_5828 | L-2-Amino-3-hydroxypropanoi… | HL | N[C@@H](CO)C(=O)O | 2 | 2 | 12 | 0 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_5828 | L-2-Amino-3-hydroxypropanoi… | HL | N[C@@H](CO)C(=O)O | 2 | 2 | 20 | 0.7 | *** | 1 |
| metal_68 | H^[+] | ligand_5890 | L-3,3'-Dithiobis(2-aminopro… | H2L | NC(CSSC[C@H](N)C(=O)O)C(=O)O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_5778 | DL-2-Amino-3-chloropropanoi… | HL | N[C@@H](CCl)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_5 | Al^[3+] | ligand_5778 | DL-2-Amino-3-chloropropanoi… | HL | N[C@@H](CCl)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 3 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5828 | L-2-Amino-3-hydroxypropanoi… | HL | N[C@@H](CO)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5828 | L-2-Amino-3-hydroxypropanoi… | HL | N[C@@H](CO)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_92 | Mg^[2+] | ligand_5856 | L-2-Amino-3-mercaptopropano… | H2L | N[C@@H](CS)C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_5856 | L-2-Amino-3-mercaptopropano… | H2L | N[C@@H](CS)C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_94 | Mn^[2+] | ligand_5856 | L-2-Amino-3-mercaptopropano… | H2L | N[C@@H](CS)C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5856 | L-2-Amino-3-mercaptopropano… | H2L | N[C@@H](CS)C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_5856 | L-2-Amino-3-mercaptopropano… | H2L | N[C@@H](CS)C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_68 | H^[+] | ligand_5859 | DL-2-Amino-4-mercaptobutano… | H2L | NC(CCS)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |

### ΔH — 10 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_41 | Cu^[2+] | ligand_5883 | L-2,3-Diaminopropanoic acid | HL | NCC(N)C(=O)O | 6 | 6 | 25 | 0.1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_5883 | L-2,3-Diaminopropanoic acid | HL | NCC(N)C(=O)O | 5 | 5 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 3 | 2 | 10~25 | 0 | *** | 0 |
| metal_68 | H^[+] | ligand_5883 | L-2,3-Diaminopropanoic acid | HL | NCC(N)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_5885 | L-2,4-Diaminobutanoic acid | HL | NCCC(N)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5885 | L-2,4-Diaminobutanoic acid | HL | NCCC(N)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |

### ΔS — 10 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_41 | Cu^[2+] | ligand_5883 | L-2,3-Diaminopropanoic acid | HL | NCC(N)C(=O)O | 6 | 6 | 25 | 0.1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_5883 | L-2,3-Diaminopropanoic acid | HL | NCC(N)C(=O)O | 5 | 5 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_5883 | L-2,3-Diaminopropanoic acid | HL | NCC(N)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_5885 | L-2,4-Diaminobutanoic acid | HL | NCCC(N)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0 | *** | 0 |
| metal_33 | Co^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5885 | L-2,4-Diaminobutanoic acid | HL | NCCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |

---

### Step 13: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_name_SRD LIKE '%carbonate%' AND c.metal_name_SRD LIKE '%Iron(III)%')",
  "order_by": "s.temperature_c ASC, c.ligand_name_SRD ASC",
  "limit": 200
}
```

[summary]
## search_stability — 200 row(s)

### logK — 73 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_8907 | Butanedioic acid (Succinic … | H2L | O=C(O)CCC(=O)O | 10 | 2 | 10~18 | 0~3 | *** | 5 |
| metal_65 | Gd^[3+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 10 | 4 | 20 | 0.1~3 | *** | 3 |
| metal_58 | Eu^[3+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 8 | 4 | 20 | 0.1~2 | *** | 4 |
| metal_139 | Pr^[3+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 7 | 4 | 20 | 0.1~2 | *** | 2 |
| metal_195 | UO_[2]^[2+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 5 | 3 | 20 | 0.1~1 | *** | 2 |
| metal_169 | Sc^[3+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 4 | 4 | 20 | 1 | *** | 1 |
| metal_27 | Ce^[3+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 4 | 4 | 20 | 1 | *** | 1 |
| metal_58 | Eu^[3+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 4 | 4 | 20 | 1 | *** | 1 |
| metal_179 | Tb^[3+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 4 | 4 | 20 | 1 | *** | 1 |
| metal_81 | Lu^[3+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 4 | 4 | 20 | 1 | *** | 1 |
| metal_74 | In^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 4 | 4 | 20 | 2 | *** | 1 |
| metal_79 | La^[3+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 4 | 4 | 20 | 0.1~2 | *** | 2 |
| metal_73 | Ho^[3+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 4 | 4 | 20 | 0.1~2 | *** | 2 |
| metal_68 | H^[+] | ligand_10096 | Hydrogen carbonate (Carboni… | H2L | O=C(O)O | 3 | 3 | 10 | 0 | gas | 1 |
| metal_26 | Cd^[2+] | ligand_8907 | Butanedioic acid (Succinic … | H2L | O=C(O)CCC(=O)O | 3 | 3 | 20 | 1 | *** | 2 |
| metal_64 | Ga^[3+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 3 | 3 | 20 | 1 | *** | 1 |
| metal_65 | Gd^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 3 | 3 | 20 | 1 | *** | 1 |
| metal_179 | Tb^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 3 | 3 | 20 | 2 | *** | 1 |
| metal_6 | Am^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 3 | 3 | 20 | 0.5 | *** | 1 |
| metal_117 | NpO_[2]^[2+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 3 | 3 | 20 | 1 | *** | 1 |
| metal_150 | PuO_[2]^[2+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 3 | 3 | 20 | 1 | *** | 1 |
| metal_205 | Y^[3+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_27 | Ce^[3+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_110 | Nd^[3+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_173 | Sm^[3+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_179 | Tb^[3+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_44 | Dy^[3+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_55 | Er^[3+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_192 | Tm^[3+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_206 | Yb^[3+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_81 | Lu^[3+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_6 | Am^[3+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 3 | 3 | 20 | 0.5 | *** | 1 |
| metal_117 | NpO_[2]^[2+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 3 | 3 | 20 | 1 | *** | 1 |
| metal_150 | PuO_[2]^[2+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 3 | 3 | 20 | 1 | *** | 1 |
| metal_37 | Cr^[3+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 2 | 2 | 5 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_8873 | Propanedioic acid (Malonic … | H2L | O=C(O)CC(=O)O | 2 | 2 | 10 | 0 | *** | 1 |
| metal_92 | Mg^[2+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 2 | 1 | 18~20 | 0~0.1 | *** | 2 |
| metal_25 | Ca^[2+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 2 | 2 | 18~20 | 0~0.1 | solid | 1 |
| metal_177 | Sr^[2+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 2 | 2 | 18~20 | 0~0.1 | solid | 2 |
| metal_18 | Ba^[2+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 2 | 2 | 18~20 | 0~0.1 | solid | 2 |
| metal_6 | Am^[3+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 2 | 2 | 20 | 0.7 | *** | 1 |
| metal_118 | NpO_[2]^[+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 2 | 2 | 20 | 1 | *** | 1 |
| metal_201 | VO^[2+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 2 | 2 | 20 | 1 | *** | 1 |
| metal_58 | Eu^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 2 | 2 | 20 | 0.5 | *** | 1 |
| metal_148 | Pu^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 2 | 2 | 20 | 2 | *** | 1 |
| metal_31 | Cm^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 2 | 2 | 20 | 0.5 | *** | 1 |
| metal_195 | UO_[2]^[2+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 2 | 2 | 20 | 0.1 | *** | 2 |
| metal_26 | Cd^[2+] | ligand_10096 | Hydrogen carbonate (Carboni… | H2L | O=C(O)O | 2 | 2 | 20 | 0.1 | *** | 2 |
| metal_31 | Cm^[3+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 2 | 2 | 20 | 0.5 | *** | 1 |
| metal_202 | VO_[2]^[+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 2 | 2 | 20 | 0.5 | *** | 1 |
| metal_68 | H^[+] | ligand_10143 | Hydrogen peroxide | H2L | OO | 1 | 1 | 5 | 3 | *** | 1 |
| metal_68 | H^[+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 1 | 1 | 10 | 0 | *** | 1 |
| metal_68 | H^[+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 1 | 1 | 10 | 0 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_10096 | Hydrogen carbonate (Carboni… | H2L | O=C(O)O | 1 | 1 | 10 | 0 | solid | 1 |
| metal_39 | CrO_[4]^[2-] | ligand_10143 | Hydrogen peroxide | H2L | OO | 1 | 1 | 10 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 1 | 1 | 10 | 0 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 1 | 1 | 18 | 0 | *** | 1 |
| metal_118 | NpO_[2]^[+] | ligand_8907 | Butanedioic acid (Succinic … | H2L | O=C(O)CCC(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_150 | PuO_[2]^[2+] | ligand_8907 | Butanedioic acid (Succinic … | H2L | O=C(O)CCC(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_8907 | Butanedioic acid (Succinic … | H2L | O=C(O)CCC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 1 | 1 | 20 | 0.1 | solid | 1 |
| metal_150 | PuO_[2]^[2+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_103 | Mo^[6+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_204 | W^[6+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_15 | B^[3+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_44 | Dy^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 1 | 1 | 20 | 2 | *** | 1 |
| metal_55 | Er^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 1 | 1 | 20 | 2 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_191 | Tl^[+] | ligand_10096 | Hydrogen carbonate (Carboni… | H2L | O=C(O)O | 1 | 1 | 20 | 3.5 | *** | 1 |
| metal_103 | Mo^[6+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_15 | B^[3+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_74 | In^[3+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 1 | 1 | 20 | 2 | *** | 1 |

### ΔH — 6 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_8907 | Butanedioic acid (Succinic … | H2L | O=C(O)CCC(=O)O | 2 | 2 | 15 | 0 | *** | 0 |
| metal_68 | H^[+] | ligand_8873 | Propanedioic acid (Malonic … | H2L | O=C(O)CC(=O)O | 2 | 2 | 10 | 0 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 2 | 2 | 15 | 0 | *** | 0 |
| metal_68 | H^[+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 1 | 1 | 10 | 0 | *** | 0 |
| metal_68 | H^[+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 1 | 1 | 10 | 0 | *** | 0 |
| metal_68 | H^[+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 1 | 1 | 10 | 0 | *** | 0 |

---
