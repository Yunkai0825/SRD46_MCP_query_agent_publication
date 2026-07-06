# Q4.2 — Tool Results (batch 4)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "mercury",
  "symbol": "Hg",
  "limit": 5
}
```

[summary]
## search_metals — 5 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_20 | BuHg^[+] | B | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_53 | EtHg^[+] | EHg | 1 |  | *** | *** | beta_totN_4 | ligand_totN_3 | vlm_totN_6 |
| metal_71 | Hg^[2+] | Hg | 2 | ✓ | [Hg+2] | InChI=1S/Hg/q+2 | beta_totN_68 | ligand_totN_310 | vlm_totN_1097 |
| metal_72 | Hg^[+] | Hg | 1 | ✓ | [Hg+] | InChI=1S/Hg/q+1 | beta_totN_12 | ligand_totN_31 | vlm_totN_83 |
| metal_93 | MeHg^[+] | MHg | 1 |  | *** | *** | beta_totN_18 | ligand_totN_79 | vlm_totN_148 |

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "cysteine",
  "limit": 10
}
```

[summary]
## search_ligands — 10 result(s)

**stats:** 26 SQL matches · showing 10 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5856 | L-2-Amino-3-mercaptopropanoic acid (Cysteine) | H2L | Amino Acids | 134 | `N[C@@H](CS)C(=O)O` | (-inf, H3L, -1.9, H2L, 8.18, HL, 10.3, L, +inf) |
| ligand_5859 | DL-2-Amino-4-mercaptobutanoic acid (Homocysteine) | H2L | Amino Acids | 3 | `NC(CCS)C(=O)O` | (-inf, H3L, 2.15, H2L, 8.57, HL, 10.38, L, +inf) |
| ligand_5861 | L-2-Amino-3-(methylthio)propan… (S-Methylcysteine) | HL | Amino Acids | 39 | `CSC[C@H](N)C(=O)O` | (-inf, H2L, 2, HL, 8.74, L, +inf) |
| ligand_5862 | L-2-Amino-3-(ethylthio)propanoi… (S-Ethylcysteine) | HL | Amino Acids | 46 | `CCSC[C@H](N)C(=O)O` | (-inf, H2L, -1.9, HL, 8.65, L, +inf) |
| ligand_5871 | L-2-Amino-3-(2-Cyanoethylthio)propanoic acid (L-5… | HL | Amino Acids | 1 | `N#CCCSCC(N)C(=O)O` | (-inf, HL, 8.46, L, +inf) |
| ligand_5872 | L-2-Amino-3-(Ethoxy-3-oxopropylthio)propanoic aci… | HL | Amino Acids | 1 | `CCOC(=O)CCSCC(N)C(=O)O` | (-inf, HL, 8.51, L, +inf) |
| ligand_5879 | L-2-Amino-3-(2-aminoethylthio)propanoic acid (S-(… | HL | Amino Acids | 22 | `NCCSC[C@H](N)C(=O)O` | (-inf, H3L, -1.7, H2L, 8.32, HL, 9.67, L, +inf) |
| ligand_6007 | L,L-Ethylenediimino-… (N,N'-Ethylenedi-L-cysteine) | H4L | Amino Acids | 32 | `O=C(O)C(CS)NCCNC(CS)C(=O)O` | (-inf, H5L, -1.7, H4L, 5.4, H3L, 7.91, H2L, 9.88, HL, 9.88, L, +inf) |
| ligand_6397 | Glycyl-L-cysteine | H2L | Peptides | 12 | `NCC(=O)N[C@@H](CS)C(=O)O` | (-inf, H3L, 2.73, H2L, 8.04, HL, 9.48, L, +inf) |
| ligand_6398 | Glycyl-L-S-methylcysteine | HL | Peptides | 4 | `CSC[C@H](NC(=O)CN)C(=O)O` | (-inf, H2L, 2.9, HL, 8.12, L, +inf) |

### Functional groups across all SQL matches (22 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 19 | 86% |
| primary_amine | 19 | 86% |
| thiol | 12 | 55% |
| amide | 11 | 50% |
| thioether | 10 | 45% |
| ester | 4 | 18% |
| aromatic_ring | 1 | 5% |
| nitrile | 1 | 5% |
| secondary_amine | 1 | 5% |

---

### Step 4: `search_ligands`
**Args:**
```json
{
  "name": "glutathione",
  "limit": 10
}
```

[summary]
## search_ligands — 4 result(s)

**stats:** 4 SQL matches · showing 4 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6592 | L-5-Glutamyl-L-cysteinylglycine (Glutathione) | H3L | tripeptides | 106 | `N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O` | (-inf, H4L, 2.08, H3L, 3.49, H2L, 8.64, HL, 9.51, L, +inf) |
| ligand_6593 | L-5-Glutamyl-(S-methyl-L-cy… (S-methylglutathione) | H2L | tripeptides | 5 | `CSC[C@H](NC(=O)CC[C@H](N)C(=O)O)C(=O)NCC(=O)O` | (-inf, HL, 9.08, L, +inf) |
| ligand_6682 | N,N-[N'',N''''-Di(L-5-glu… (Glutathione disulfide) | *** | polypeptides | 53 | *** | (-inf, H6L, -1.5, H5L, 2.35, H4L, 3.16, H3L, 3.83, H2L, 8.85, HL, 9.81, L, +inf) |
| ligand_10422 | L-5-Glutamyl-… (DL-Cysteine-glutathione disulfide) | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (2 parseable SMILES)

| group | count | % |
|-------|-------|---|
| amide | 2 | 100% |
| carboxyl | 2 | 100% |
| primary_amine | 2 | 100% |
| thioether | 1 | 50% |
| thiol | 1 | 50% |

---

### Step 5: `search_ligands`
**Args:**
```json
{
  "name": "thiourea",
  "limit": 10
}
```

[summary]
## search_ligands — 10 result(s)

**stats:** 22 SQL matches · showing 10 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_7007 | 1-(2-Aminoethyl)-1,3-diazolidine-2-thione (N-(2-A… | L | Aliphatic amines | 3 | `NCCN1CCNC1=S` | *** |
| ligand_10004 | Thiocarbamide (Thiourea) | L | miscellaneous ureas, had… | 175 | `NC(N)=S` | (-inf, HL, -1.18, L, +inf) |
| ligand_10005 | N-Methylthiourea | L | miscellaneous ureas, had… | 33 | `CNC(N)=S` | *** |
| ligand_10006 | N-Ethylthiourea | L | miscellaneous ureas, had… | 21 | `CCNC(N)=S` | *** |
| ligand_10007 | N-Butylthiourea | L | miscellaneous ureas, had… | 2 | `CCCCNC(N)=S` | *** |
| ligand_10008 | N,N'-Dimethylthiourea | L | miscellaneous ureas, had… | 16 | `CNC(=S)NC` | *** |
| ligand_10009 | N,N'-Diethylthiourea | L | miscellaneous ureas, had… | 15 | `CCNC(=S)NCC` | *** |
| ligand_10010 | 1,3-Diazolidine-2-thione (Ethylenethiourea) | L | miscellaneous ureas, had… | 10 | `S=C1NCCN1` | *** |
| ligand_10011 | 4-Methyl-1,3-diazolidi… (4-Methylethylenethiourea) | L | miscellaneous ureas, had… | 3 | `CC1CNC(=S)N1` | *** |
| ligand_10012 | 4,4-Dimethyl-1,3-d… (4,4-Dimethylethylenethiourea) | L | miscellaneous ureas, had… | 3 | `CC1(C)CNC(=S)N1` | *** |

### Functional groups across all SQL matches (16 parseable SMILES)

| group | count | % |
|-------|-------|---|
| secondary_amine | 14 | 88% |
| primary_amine | 8 | 50% |
| tertiary_amine | 3 | 19% |
| aromatic_ring | 2 | 12% |
| amide | 1 | 6% |

---

### Step 6: `search_ligands`
**Args:**
```json
{
  "name": "thiosulfate",
  "limit": 10
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_10149 | Hydrogen thiosulfate (Thiosulfuric acid) | H2L | Inorganic ligands | 117 | `O=S(O)(O)=S` | (-inf, H2L, -0.6, HL, -0.6, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| hydroxyl | 1 | 100% |

---

### Step 7: `search_ligands`
**Args:**
```json
{
  "name": "thioglycolate",
  "limit": 10
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 8: `search_ligands`
**Args:**
```json
{
  "name": "mercaptoacetate",
  "limit": 10
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 9: `search_ligands`
**Args:**
```json
{
  "name": "2-mercaptoethanol",
  "limit": 10
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_9747 | 2-Mercaptoethanol | HL | miscellaneous mercaptans | 41 | `OCCS` | (-inf, HL, 9.4, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| hydroxyl | 1 | 100% |
| thiol | 1 | 100% |

---

### Step 10: `search_ligands`
**Args:**
```json
{
  "name": "mercaptoethanol",
  "limit": 10
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_9747 | 2-Mercaptoethanol | HL | miscellaneous mercaptans | 41 | `OCCS` | (-inf, HL, 9.4, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| hydroxyl | 1 | 100% |
| thiol | 1 | 100% |

---

### Step 11: `search_ligands`
**Args:**
```json
{
  "name": "sulfide",
  "limit": 10
}
```

[summary]
## search_ligands — 10 result(s)

**stats:** 10 SQL matches · showing 10 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5891 | D-3,3'-Dithiobis(2-amin… (Penicillamine disulfide) | H2L | Amino Acids | 23 | `CC(C)(SSC(C)(C)C(N)C(=O)O)C(N)C(=O)O` | (-inf, H4L, -1.3, H3L, 2.04, H2L, 7.77, HL, 8.74, L, +inf) |
| ligand_6656 | L-3,3'-Dithiobis(a… (L-Cysteinylglycine disulfide) | H2L | polypeptides | 20 | `N[C@@H](CSSC[C@H](N)C(=O)NCC(=O)O)C(=O)NCC(=O)O` | (-inf, H4L, 2.65, H3L, 3.39, H2L, 6.3, HL, 7.28, L, +inf) |
| ligand_6657 | L-5-Glutamyl… (Penicillamine-glutatione disulfide) | H3L | polypeptides | 2 | `CC(C)(SSCC(NC(=O)CCC(N)C(=O)O)C(=O)NCC(=O)O)C(N)C(=O)O` | (-inf, H2L, 7.99, HL, 9.1, L, +inf) |
| ligand_6682 | N,N-[N'',N''''-Di(L-5-glu… (Glutathione disulfide) | *** | polypeptides | 53 | *** | (-inf, H6L, -1.5, H5L, 2.35, H4L, 3.16, H3L, 3.83, H2L, 8.85, HL, 9.81, L, +inf) |
| ligand_9696 | Dimethylsulfide | *** | miscellaneous sulfides | 1 | *** | *** |
| ligand_10144 | Hydrogen sulfide (Hydrosulfuric acid) | H2L | Inorganic ligands | 93 | `S` | (-inf, H2L, 6.82, HL, +inf) |
| ligand_10145 | Hydrogen tetrasulfide | H2L | Inorganic ligands | 2 | `SSSS` | (-inf, H2L, 3.8, HL, 6.3, L, +inf) |
| ligand_10146 | Hydrogen pentasulfide | H2L | Inorganic ligands | 2 | `SSSSS` | (-inf, H2L, 3.5, HL, 5.7, L, +inf) |
| ligand_10214 | DL-3,3-Di… (D-Penicillamine-DL-cysteine disulfide) | *** | Ligands not selected | 0 | *** | *** |
| ligand_10422 | L-5-Glutamyl-… (DL-Cysteine-glutathione disulfide) | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (6 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 3 | 50% |
| primary_amine | 3 | 50% |
| amide | 2 | 33% |
| thiol | 2 | 33% |

---

### Step 12: `search_ligands`
**Args:**
```json
{
  "name": "hydrosulfide",
  "limit": 10
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 13: `search_ligands`
**Args:**
```json
{
  "name": "ammonia",
  "limit": 10
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_10103 | Ammonia | L | Inorganic ligands | 447 | `N` | (-inf, HL, 9.26, L, +inf) |

---

### Step 14: `search_ligands`
**Args:**
```json
{
  "name": "ethylenediamine",
  "limit": 10
}
```

[summary]
## search_ligands — 10 result(s)

**stats:** 105 SQL matches · showing 10 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5948 | N-(2-Aminoethyl)glycine (Ethylenediamine m… (EDMA) | HL | Amino Acids | 30 | `NCCNCC(=O)O` | (-inf, H3L, -1.9, H2L, 6.67, HL, 9.84, L, +inf) |
| ligand_6253 | N-(2-Aminoeth… (Ethylenediamine-N,N-diacetic acid) | H2L | NTA and derivatives | 39 | `NCCN(CC(=O)O)CC(=O)O` | (-inf, H2L, 5.53, HL, 10.87, L, +inf) |
| ligand_7029 | Ethylenediamine | L | Aliphatic amines | 310 | `NCCN` | (-inf, H2L, 7.11, HL, 9.92, L, +inf) |
| ligand_7030 | DL-Methylethylenediamine (1,2-Propylenediami… (pn) | L | Aliphatic amines | 86 | `CC(N)CN` | (-inf, H2L, 6.85, HL, 9.81, L, +inf) |
| ligand_7031 | DL-Ethylethylenediamine (1,2-Butylenediamine) | L | Aliphatic amines | 19 | `CCC(N)CN` | (-inf, H2L, 6.65, HL, 9.66, L, +inf) |
| ligand_7032 | DL-(2-Methyl-2-propyl)et… (t-Butylethylenediamine) | L | Aliphatic amines | 2 | `CC(C)(C)C(N)CN` | (-inf, H2L, 6.26, HL, 9.78, L, +inf) |
| ligand_7033 | 1,1-Dimethylethylenediamine | L | Aliphatic amines | 37 | `CC(C)(N)CN` | (-inf, H2L, 6.46, HL, 9.75, L, +inf) |
| ligand_7034 | DL-1,2-Dimethylethylened… (DL-2,3-Butylenediamine) | L | Aliphatic amines | 46 | `CC(N)C(C)N` | (-inf, H2L, 6.6, HL, 9.7, L, +inf) |
| ligand_7035 | meso-1,2-Dimethylethyl… (meso-2,3-Butylenediamine) | L | Aliphatic amines | 53 | `C[C@H](N)[C@@H](C)N` | (-inf, H2L, 6.63, HL, 9.76, L, +inf) |
| ligand_7036 | 1,1,2,2-Tetramethylethylenediamine | L | Aliphatic amines | 15 | `CC(C)(N)C(C)(C)N` | (-inf, H2L, 6.35, HL, 9.93, L, +inf) |

### Functional groups across all SQL matches (85 parseable SMILES)

| group | count | % |
|-------|-------|---|
| primary_amine | 58 | 68% |
| secondary_amine | 43 | 51% |
| tertiary_amine | 23 | 27% |
| hydroxyl | 14 | 16% |
| aromatic_ring | 13 | 15% |
| amide | 7 | 8% |
| phosphonate | 4 | 5% |
| thioether | 4 | 5% |
| phenol | 3 | 4% |
| pyridine | 3 | 4% |
| carboxyl | 2 | 2% |
| sulfonate | 1 | 1% |
| thiol | 1 | 1% |

---

### Step 15: `search_ligands`
**Args:**
```json
{
  "name": "imidazole",
  "limit": 10
}
```

[summary]
## search_ligands — 10 result(s)

**stats:** 50 SQL matches · showing 10 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_7795 | 1,3-Diazole (Imidazole) | L | Pyrroles (azoles) | 237 | `c1c[nH]cn1` | (-inf, HL, 7, L, 7, H-1L, +inf) |
| ligand_7796 | 1-Methylimidazole | L | Pyrroles (azoles) | 52 | `Cn1ccnc1` | (-inf, HL, 7.1, L, +inf) |
| ligand_7797 | 1-Ethylimidazole | L | Pyrroles (azoles) | 17 | `CCn1ccnc1` | (-inf, HL, 7.21, L, +inf) |
| ligand_7798 | 1-Propylimidazole | L | Pyrroles (azoles) | 17 | `CCCn1ccnc1` | (-inf, HL, 7.22, L, +inf) |
| ligand_7799 | 1-Butylimidazole | L | Pyrroles (azoles) | 16 | `CCCCn1ccnc1` | (-inf, HL, 7.22, L, +inf) |
| ligand_7800 | 2-Methylimidazole | L | Pyrroles (azoles) | 18 | `Cc1ncc[nH]1` | (-inf, HL, 7.9, L, +inf) |
| ligand_7801 | 2-Ethylimidazole | L | Pyrroles (azoles) | 20 | `CCc1ncc[nH]1` | (-inf, HL, 7.87, L, +inf) |
| ligand_7802 | 2-(2-Propyl)imidazole | L | Pyrroles (azoles) | 1 | `CC(C)c1ncc[nH]1` | (-inf, HL, 7.77, L, +inf) |
| ligand_7803 | 4-Methylimidazole | L | Pyrroles (azoles) | 26 | `Cc1c[nH]cn1` | (-inf, HL, 7.55, L, +inf) |
| ligand_7804 | 1,2-Dimethylimidazole | L | Pyrroles (azoles) | 10 | `Cc1nccn1C` | (-inf, HL, 8.21, L, +inf) |

### Functional groups across all SQL matches (44 parseable SMILES)

| group | count | % |
|-------|-------|---|
| aromatic_ring | 44 | 100% |
| hydroxyl | 7 | 16% |
| primary_amine | 6 | 14% |
| pyridine | 3 | 7% |
| thiol | 3 | 7% |
| ester | 1 | 2% |
| secondary_amine | 1 | 2% |
| tertiary_amine | 1 | 2% |

---

### Step 16: `search_ligands`
**Args:**
```json
{
  "name": "pyridine",
  "limit": 10
}
```

[summary]
## search_ligands — 10 result(s)

**stats:** 304 SQL matches · showing 10 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5963 | L-4,5,6,7-Tetrahydro-1H-imidazo[4,5-c… (Spinacine) | HL | Amino Acids | 14 | `O=C(O)C1Cc2[nH]cnc2CN1` | (-inf, H3L, -1.5, H2L, 4.9, HL, 8.59, L, +inf) |
| ligand_6762 | Pyridine-2-carboxylic acid (Picolinic acid) | HL | Pyridine carboxylic acids | 316 | `O=C(O)c1ccccn1` | (-inf, H2L, -0.95, HL, 5.21, L, +inf) |
| ligand_6763 | 6-Methylpyridine-2-carboxylic acid | HL | Pyridine carboxylic acids | 27 | `Cc1cccc(C(=O)O)n1` | (-inf, H2L, -1.2, HL, 5.86, L, +inf) |
| ligand_6765 | Pyridine-2-carboxylic acid N-oxide | HL | Pyridine carboxylic acids | 20 | `O=C(O)c1cccc[n+]1[O-]` | (-inf, HL, 3.31, L, +inf) |
| ligand_6766 | Pyridine-3-carboxylic acid (Nicotinic acid) | HL | Pyridine carboxylic acids | 28 | `O=C(O)c1cccnc1` | (-inf, H2L, 2.08, HL, 4.69, L, +inf) |
| ligand_6767 | Pyridine-4-carboxylic acid (Isonicotinic acid) | HL | Pyridine carboxylic acids | 16 | `O=C(O)c1ccncc1` | (-inf, H2L, 1.77, HL, 4.84, L, +inf) |
| ligand_6770 | Pyridine-2-phosphonic-6-carboxylic acid (2PP6C) | H3L | Pyridine carboxylic acids | 14 | `O=C(O)c1cccc(P(=O)(O)O)n1` | (-inf, H2L, 3.66, HL, 7.11, L, +inf) |
| ligand_6771 | Pyridine-2,3-dicarboxylic acid (Quinolinic acid) | H2L | Pyridine carboxylic acids | 47 | `O=C(O)c1cccnc1C(=O)O` | (-inf, H2L, 2.36, HL, 4.72, L, +inf) |
| ligand_6772 | Pyridine-2,4-dicarboxylic acid (Lutidinic acid) | H2L | Pyridine carboxylic acids | 16 | `O=C(O)c1ccnc(C(=O)O)c1` | (-inf, H2L, 2.23, HL, 4.79, L, +inf) |
| ligand_6773 | Pyridine-2,5-dicarboxylic… (Isocinchomeronic acid) | H2L | Pyridine carboxylic acids | 12 | `O=C(O)c1ccc(C(=O)O)nc1` | (-inf, H2L, 2.38, HL, 5.02, L, +inf) |

### Functional groups across all SQL matches (260 parseable SMILES)

| group | count | % |
|-------|-------|---|
| aromatic_ring | 260 | 100% |
| pyridine | 258 | 99% |
| hydroxyl | 67 | 26% |
| primary_amine | 49 | 19% |
| secondary_amine | 33 | 13% |
| carboxyl | 27 | 10% |
| tertiary_amine | 19 | 7% |
| thioether | 17 | 7% |
| amide | 16 | 6% |
| aldehyde | 14 | 5% |
| halide | 11 | 4% |
| imine | 6 | 2% |
| ether | 5 | 2% |
| ketone | 5 | 2% |
| oxime | 5 | 2% |
| ester | 4 | 2% |
| nitrile | 4 | 2% |
| sulfonate | 3 | 1% |
| phosphonate | 2 | 1% |
| phosphate | 1 | 0% |
| thiol | 1 | 0% |

---

### Step 17: `search_ligands`
**Args:**
```json
{
  "name": "acetate",
  "limit": 10
}
```

[summary]
## search_ligands — 3 result(s)

**stats:** 3 SQL matches · showing 3 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6365 | {Bis[3-(bis(carboxymethyl)amino)propyl]methylammo… | H4L | EDTA and derivatives | 32 | `C[N+](CCCN(CC(=O)O)CC(=O)O)(CCCN(CC(=O)O)CC(=O)O)CC(=O)[O-]` | (-inf, H4L, 2.14, H3L, 2.82, H2L, 7.95, HL, 8.84, L, +inf) |
| ligand_8698 | 2-Oxobutanedioic acid 4-et… (4-Ethyl oxaloacetate) | HL | Carboxylic acids keto | 5 | `CCOC(=O)CC(=O)C(=O)O` | (-inf, HL, 9.3, L, +inf) |
| ligand_9801 | Acetic acid vinyl ester (Vinyl acetate) | *** | miscellaneous hydrocarbo… | 2 | *** | *** |

### Functional groups across all SQL matches (2 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 2 | 100% |
| carboxylate | 1 | 50% |
| ester | 1 | 50% |
| ketone | 1 | 50% |
| tertiary_amine | 1 | 50% |

---

### Step 18: `search_ligands`
**Args:**
```json
{
  "name": "oxalate",
  "limit": 10
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 19: `search_ligands`
**Args:**
```json
{
  "name": "citrate",
  "limit": 10
}
```

[summary]
## search_ligands — 4 result(s)

**stats:** 4 SQL matches · showing 4 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8672 | 2-Hydroxypropane-1,2,3-tri… (sym-Dimethyl citrate) | HL | Carboxylic acids hydroxy | 2 | `COC(=O)CC(O)(CC(=O)OC)C(=O)O` | (-inf, HL, 3.02, L, +inf) |
| ligand_8682 | DL-2-Hydroxypropane-1,2,3-t… (as-Dimethyl citrate) | HL | Carboxylic acids hydroxy | 2 | `COC(=O)CC(O)(CC(=O)O)C(=O)OC` | (-inf, HL, 3.78, L, +inf) |
| ligand_8965 | 2-Hydroxypropane-1,2,3-tri… (as-Monomethylcitrate) | H2L | Carboxylic acids diacids… | 4 | `COC(=O)CC(O)(CC(=O)O)C(=O)O` | (-inf, H2L, 2.7, HL, 4.66, L, +inf) |
| ligand_8966 | 2-Hydroxypropane-1,2,3-tr… (sym-Monomethylcitrate) | H2L | Carboxylic acids diacids… | 4 | `COC(=O)C(O)(CC(=O)O)CC(=O)O` | (-inf, H2L, 3.39, HL, 4.63, L, +inf) |

### Functional groups across all SQL matches (4 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 4 | 100% |
| ester | 4 | 100% |
| hydroxyl | 4 | 100% |

---

### Step 20: `search_ligands`
**Args:**
```json
{
  "name": "carbonate",
  "limit": 10
}
```

[summary]
## search_ligands — 4 result(s)

**stats:** 4 SQL matches · showing 4 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_10096 | Hydrogen carbonate (Carbonic acid) | H2L | Inorganic ligands | 335 | `O=C(O)O` | (-inf, H2L, 6.13, HL, 9.91, L, +inf) |
| ligand_10097 | Hydrogen trithiocarbonate | H2L | Inorganic ligands | 4 | `S=C(S)S` | (-inf, H2L, 2.68, HL, 8.22, L, +inf) |
| ligand_10098 | Hydrogen perthiocarbonate | H2L | Inorganic ligands | 3 | `S=C(S)SS` | (-inf, HL, 7.24, L, +inf) |
| ligand_10099 | Hydrogen triselenocarbonate | H2L | Inorganic ligands | 4 | `[Se]=C([SeH])[SeH]` | (-inf, HL, 7.13, L, +inf) |

### Functional groups across all SQL matches (4 parseable SMILES)

| group | count | % |
|-------|-------|---|
| thiol | 2 | 50% |
| carboxyl | 1 | 25% |

---

### Step 21: `search_ligands`
**Args:**
```json
{
  "name": "hydroxide",
  "limit": 10
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_10076 | Hydroxide ion | *** | Inorganic ligands | 953 | *** | (-inf, HL, 13.78, L, +inf) |

---

### Step 22: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_71"
}
```

[summary]
[CATALOG]
## build_system_catalog — 20 pair(s), 92 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_194 | [M] + [HL]^2 <=> [M(HL)2] |  |
| beta_def_204 | [MHL2] + [H] <=> [M(HL)2] |  |
| beta_def_288 | [H]^2 + [ML(s,black)] <=> [M] + [H2L] | solid |
| beta_def_292 | [H]^2 + [ML(s,red)] <=> [M] + [H2L] | solid |
| beta_def_334 | [ML2(s)] <=> [M] + [L]^2 | solid |
| beta_def_348 | [MO(s,red)] + [H2O] <=> [M] + [OH]^2 | solid |
| beta_def_438 | [M2(OH)5L] + [H]^2 <=> [M2(OH)3L] + [H2O]^2 |  |
| beta_def_502 | [M]^2 + [L] <=> [M2L] |  |
| beta_def_540 | [M]^2 + [L]^3 <=> [M2L3] |  |
| beta_def_571 | [M]^2 + [L] + [H2O] <=> [M2(OH)L] + [H] |  |
| beta_def_575 | [M2(OH)3L] + [H]^2 <=> [M2(OH)L] + [H2O]^2 |  |
| beta_def_620 | [H]^4 + [M3O2L(s)] <=> [M]^3 + [L] + [H2O]^2 | solid |
| beta_def_645 | [M]^3 + [L]^3 <=> [M3L3] |  |
| beta_def_713 | [MCl2] + [L] <=> [MClL] + [Cl] |  |
| beta_def_739 | [MHL] + [H] <=> [MH2L] |  |
| beta_def_751 | [MH2L] + [H] <=> [MH3L] |  |
| beta_def_779 | [M] + [HL] <=> [MHL] |  |
| beta_def_788 | [ML] + [H] <=> [MHL] |  |
| beta_def_792 | [ML2] + [H] <=> [MHL2] |  |
| beta_def_812 | [M] + [L] <=> [ML] |  |
| beta_def_840 | [M] + [L]^2 <=> [ML2] |  |
| beta_def_845 | [MCl2] + [L]^2 <=> [ML2] + [Cl]^2 |  |
| beta_def_872 | [M] + [L]^3 <=> [ML3] |  |
| beta_def_894 | [M] + [L]^4 <=> [ML4] |  |
| beta_def_966 | [M(OH)L] + [H] <=> [ML] + [H2O] |  |
| beta_def_978 | [M] + [L] + [OH] <=> [M(OH)L] |  |

*(all species aqueous unless noted)*

**1. Hg^[2+] + Chloride ion** (metal_71 + ligand_10163) — ligand_def_HxL: *** | 38 ent, 5 sp, 38 vlms (vlm_177572…vlm_177609)
   - species: beta_def_812(8) beta_def_840(8) beta_def_872(9) beta_def_894(9) beta_def_966(4)
   - eq:5 nets T:19~30°C I:-0.05~3.15M max 5n/7e
**2. Hg^[2+] + Hydrogen cyanide (Hydrocyanic acid)** (metal_71 + ligand_10090) — ligand_def_HxL: HL | 37 ent, 5 sp, 37 vlms (vlm_172054…vlm_172090)
   - species: beta_def_812(8) beta_def_840(10) beta_def_872(9) beta_def_894(9) beta_def_978(1)
   - eq:6 nets T:5~45°C I:-0.15~2.15M max 4n/6e
**3. Hg^[2+] + Hydroxide ion** (metal_71 + ligand_10076) — ligand_def_HxL: *** | 29 ent, 6 sp, 29 vlms (vlm_170985…vlm_171013)
   - species: beta_def_348(4) beta_def_502(4) beta_def_645(2) beta_def_812(8) beta_def_840(10) beta_def_872(1)
   - eq:6 nets T:19~30°C I:-0.15~3.15M max 6n/15e
**4. Hg^[2+] + Bromide ion** (metal_71 + ligand_10168) — ligand_def_HxL: *** | 28 ent, 5 sp, 28 vlms (vlm_178151…vlm_178178)
   - species: beta_def_812(8) beta_def_840(6) beta_def_872(6) beta_def_894(6) beta_def_966(2)
   - eq:2 nets T:16.5~31.5°C I:0.275~3.225M max 5n/7e
**5. Hg^[2+] + Thiocarbamide (Thiourea)** (metal_71 + ligand_10004) — ligand_def_HxL: L | 27 ent, 5 sp, 27 vlms (vlm_169530…vlm_169556)
   - species: beta_def_540(3) beta_def_812(3) beta_def_840(7) beta_def_872(7) beta_def_894(7)
   - eq:3 nets T:19~30°C I:-0.05~1.15M max 5n/10e
**6. Hg^[2+] + Hydrogen thiocyanate (Thiocyanic acid)** (metal_71 + ligand_10092) — ligand_def_HxL: HL | 20 ent, 6 sp, 20 vlms (vlm_172456…vlm_172475)
   - species: beta_def_334(1) beta_def_812(6) beta_def_840(4) beta_def_872(3) beta_def_894(3) beta_def_966(3)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 6n/11e
**7. Hg^[2+] + Iodide ion** (metal_71 + ligand_10171) — ligand_def_HxL: *** | 16 ent, 6 sp, 16 vlms (vlm_178529…vlm_178544)
   - species: beta_def_334(3) beta_def_812(4) beta_def_840(3) beta_def_872(1) beta_def_894(4) beta_def_966(1)
   - eq:1 nets T:16.5~31.5°C I:0.275~0.725M max 6n/11e
**8. Hg^[2+] + Ethylenediamine** (metal_71 + ligand_7029) — ligand_def_HxL: L | 13 ent, 3 sp, 13 vlms (vlm_122573…vlm_122585)
   - species: beta_def_792(3) beta_def_812(5) beta_def_840(5)
   - eq:3 nets T:19~30°C I:-0.05~3.15M max 3n/2e
**9. Hg^[2+] + Ammonia** (metal_71 + ligand_10103) — ligand_def_HxL: L | 12 ent, 4 sp, 12 vlms (vlm_173464…vlm_173475)
   - species: beta_def_812(1) beta_def_840(4) beta_def_872(3) beta_def_894(4)
   - eq:3 nets T:19~30°C I:-0.05~2.15M max 4n/6e
**10. Hg^[2+] + 2,2'-Thiodiethanol (beta-Thiodiglycol)** (metal_71 + ligand_9697) — ligand_def_HxL: *** | 12 ent, 4 sp, 12 vlms (vlm_167724…vlm_167735)
   - species: beta_def_812(3) beta_def_840(3) beta_def_872(3) beta_def_894(3)
   - eq:1 nets T:16.5~31.5°C I:0.275~0.725M max 4n/6e
**11. Hg^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_71 + ligand_6277) — ligand_def_HxL: H4L | 11 ent, 4 sp, 11 vlms (vlm_108748…vlm_108758)
   - species: beta_def_739(1) beta_def_788(4) beta_def_812(5) beta_def_966(1)
   - eq:3 nets T:19~30°C I:-0.05~1.15M max 3n/3e
**12. Hg^[2+] + Hydrogen azide (Hydrazoic acid)** (metal_71 + ligand_10106) — ligand_def_HxL: HL | 10 ent, 2 sp, 10 vlms (vlm_173697…vlm_173706)
   - species: beta_def_812(5) beta_def_840(5)
   - eq:3 nets T:19~30°C I:-0.15~1.15M max 2n/1e
**13. Hg^[2+] + Hydrogen carbonate (Carbonic acid)** (metal_71 + ligand_10096) — ligand_def_HxL: H2L | 10 ent, 5 sp, 10 vlms (vlm_172918…vlm_172927)
   - species: beta_def_620(3) beta_def_779(2) beta_def_812(2) beta_def_840(1) beta_def_966(2)
   - eq:3 nets T:19~30°C I:-0.05~3.15M max 5n/8e
**14. Hg^[2+] + 1,3-Diazole (Imidazole)** (metal_71 + ligand_7795) — ligand_def_HxL: L | 10 ent, 3 sp, 10 vlms (vlm_134017…vlm_134026)
   - species: beta_def_812(3) beta_def_840(4) beta_def_966(3)
   - eq:2 nets T:19~30°C I:-0.05~3.15M max 3n/2e
**15. Hg^[2+] + Methylamine** (metal_71 + ligand_6797) — ligand_def_HxL: L | 10 ent, 6 sp, 10 vlms (vlm_119991…vlm_120000)
   - species: beta_def_713(3) beta_def_812(1) beta_def_840(1) beta_def_845(3) beta_def_872(1) beta_def_894(1)
   - eq:2 nets T:19~30°C I:-0.05~0.65M max 4n/6e
**16. Hg^[2+] + Thiosemicarbazide** (metal_71 + ligand_10025) — ligand_def_HxL: L | 9 ent, 3 sp, 9 vlms (vlm_169888…vlm_169896)
   - species: beta_def_840(3) beta_def_872(3) beta_def_894(3)
   - eq:2 nets T:19~30°C I:-0.05~0.85M max 2n/1e
**17. Hg^[2+] + Selenocarbamide (Selenourea)** (metal_71 + ligand_10022) — ligand_def_HxL: L | 9 ent, 3 sp, 9 vlms (vlm_169776…vlm_169784)
   - species: beta_def_840(3) beta_def_872(3) beta_def_894(3)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 3n/3e
**18. Hg^[2+] + Hydrogen sulfide (Hydrosulfuric acid)** (metal_71 + ligand_10144) — ligand_def_HxL: H2L | 8 ent, 5 sp, 8 vlms (vlm_175475…vlm_175482)
   - species: beta_def_194(1) beta_def_204(1) beta_def_288(4) beta_def_292(1) beta_def_792(1)
   - eq:2 nets T:15~30°C I:-0.05~1.15M max 4n/5e
**19. Hg^[2+] + rac-3,6-Dioxaoctane-1,2,4,5,7,8-hexacarboxylic acid (TDS)** (metal_71 + ligand_9096) — ligand_def_HxL: H6L | 8 ent, 8 sp, 8 vlms (vlm_158606…vlm_158613)
   - species: beta_def_438(1) beta_def_571(1) beta_def_575(1) beta_def_739(1) beta_def_751(1) beta_def_788(1) beta_def_812(1) beta_def_966(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 8n/24e
**20. Hg^[2+] + Pyridine (Azine)** (metal_71 + ligand_7890) — ligand_def_HxL: L | 8 ent, 4 sp, 8 vlms (vlm_135327…vlm_135334)
   - species: beta_def_812(3) beta_def_840(3) beta_def_872(1) beta_def_894(1)
   - eq:1 nets T:16.5~31.5°C I:0.275~0.725M max 4n/6e

---

### Step 24: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.ligand_id = ligand_9747 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 20 AND 30 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2))",
  "order_by": "s.constant_value DESC",
  "limit": 3
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
  "where": "(c.metal_id = metal_71 AND c.ligand_id = ligand_10004 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 20 AND 30 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2))",
  "order_by": "s.constant_value DESC",
  "limit": 3
}
```

[summary]
## search_stability

*(no results)*

---

### Step 26: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.ligand_id = ligand_10149 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 20 AND 30 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2))",
  "order_by": "s.constant_value DESC",
  "limit": 3
}
```

[summary]
## search_stability

*(no results)*

---

### Step 27: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.ligand_id = ligand_5856 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 20 AND 30 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2))",
  "order_by": "s.constant_value DESC",
  "limit": 3
}
```

[summary]
## search_stability — 1 row(s)

### `Hg^[2+]` + L-2-Amino-3-mercaptopropanoic acid (Cysteine) — 1 measurement(s)
metal_id: metal_71 | ligand_id: ligand_5856
ligand_HxL_def: H2L | ligand_SMILES: N[C@@H](CS)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_97477 | ref_eq_map_1023 | beta_def_812 | logK | 14.4 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (10.3, L, +inf) |

---

### Step 28: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.ligand_id = ligand_6592 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 20 AND 30 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2))",
  "order_by": "s.constant_value DESC",
  "limit": 3
}
```

[summary]
## search_stability — 1 row(s)

### `Hg^[2+]` + L-5-Glutamyl-L-cysteinylglycine (Glutathione) — 1 measurement(s)
metal_id: metal_71 | ligand_id: ligand_6592
ligand_HxL_def: H3L | ligand_SMILES: N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_116684 | ref_eq_map_7679 | beta_def_812 | logK | 26 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.51, L, +inf) |

---

### Step 29: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.ligand_id = ligand_10103 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 20 AND 30 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2))",
  "order_by": "s.constant_value DESC",
  "limit": 3
}
```

[summary]
## search_stability

*(no results)*

---

### Step 30: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.ligand_id = ligand_7029 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 20 AND 30 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2))",
  "order_by": "s.constant_value DESC",
  "limit": 3
}
```

[summary]
## search_stability — 3 row(s)

### `Hg^[2+]` + Ethylenediamine — 3 measurement(s)
metal_id: metal_71 | ligand_id: ligand_7029
ligand_HxL_def: L | ligand_SMILES: NCCN

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_122573 | ref_eq_map_9615 | beta_def_812 | logK | 14.3 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122576 | *** | beta_def_812 | ΔH | 0 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122577 | *** | beta_def_812 | ΔS | -74.5 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |

---

### Step 31: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.ligand_id = ligand_7795 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 20 AND 30 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2))",
  "order_by": "s.constant_value DESC",
  "limit": 3
}
```

[summary]
## search_stability

*(no results)*

---

### Step 32: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.ligand_id = ligand_7890 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 20 AND 30 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2))",
  "order_by": "s.constant_value DESC",
  "limit": 3
}
```

[summary]
## search_stability

*(no results)*

---

### Step 33: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.ligand_id = ligand_10096 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 20 AND 30 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2))",
  "order_by": "s.constant_value DESC",
  "limit": 3
}
```

[summary]
## search_stability

*(no results)*

---

### Step 34: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.ligand_id = ligand_10076 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 20 AND 30 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2))",
  "order_by": "s.constant_value DESC",
  "limit": 3
}
```

[summary]
## search_stability — 1 row(s)

### `Hg^[2+]` + Hydroxide ion — 1 measurement(s)
metal_id: metal_71 | ligand_id: ligand_10076
ligand_HxL_def: *** | ligand_SMILES: ***

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_170988 | ref_eq_map_27454 | beta_def_812 | logK | 10.6 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (13.78, L, +inf) |

---
