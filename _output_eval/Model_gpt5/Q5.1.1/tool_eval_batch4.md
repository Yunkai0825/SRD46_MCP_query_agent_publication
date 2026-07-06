# Q5.1.1 — Tool Results (batch 4)

### Step 2: `search_metals`
**Args:**
```json
{
  "symbol": "Hg",
  "limit": 20
}
```

[summary]
## search_metals — 8 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_20 | BuHg^[+] | B | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_53 | EtHg^[+] | EHg | 1 |  | *** | *** | beta_totN_4 | ligand_totN_3 | vlm_totN_6 |
| metal_71 | Hg^[2+] | Hg | 2 | ✓ | [Hg+2] | InChI=1S/Hg/q+2 | beta_totN_68 | ligand_totN_310 | vlm_totN_1097 |
| metal_72 | Hg^[+] | Hg | 1 | ✓ | [Hg+] | InChI=1S/Hg/q+1 | beta_totN_12 | ligand_totN_31 | vlm_totN_83 |
| metal_93 | MeHg^[+] | MHg | 1 |  | *** | *** | beta_totN_18 | ligand_totN_79 | vlm_totN_148 |
| metal_136 | PhHg^[+] | PhHg | 1 |  | *** | *** | beta_totN_2 | ligand_totN_8 | vlm_totN_8 |
| metal_145 | PrHg^[+] | Pr | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_176 | O_[3]SPhHg | S | 0 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |

---

### Step 4: `search_ligands`
**Args:**
```json
{
  "name": "chloride",
  "limit": 10
}
```

[summary]
## search_ligands — 10 result(s)

**stats:** 12 SQL matches · showing 10 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5923 | L-[1-Carboxy-2-(4-hydroxypheny… (Tyrosine betaine) | H2L | Amino Acids | 1 | `C[N+](C)(C)C(Cc1ccc(O)cc1)C(=O)O.[Cl-]` | (-inf, HL, 9.63, L, +inf) |
| ligand_5947 | DL-[1-Carboxy-2-(2-mercapto-4-imi… (Ergothioneine) | H2L | Amino Acids | 4 | `C[N+](C)(C)C(Cc1cnc(S)[nH]1)C(=O)O.[Cl-]` | (-inf, HL, 10.44, L, +inf) |
| ligand_6769 | 3-Carboxy-N-methylpyridi… (Nicotinic acid betaine) | HL | Pyridine carboxylic acids | 1 | `C[n+]1cccc(C(=O)O)c1` | (-inf, HL, 2.04, L, +inf) |
| ligand_7954 | 3-Hydroxy-N-methylpyridinium (chloride) | HL | Pyridines (azines) | 3 | `C[n+]1cccc(O)c1` | (-inf, HL, 4.81, L, +inf) |
| ligand_7968 | 3-Hydroxy-N,2,5-… (Deoxypyridoxal N-methochloride) | HL | Pyridines (azines) | 2 | `Cc1c[n+](C)c(C)c(O)c1C=O` | (-inf, HL, 4.34, L, 4.34, H-1L, +inf) |
| ligand_8251 | 3-[(4-Amino-2-methyl-5-pyrimidinyl)met… (Thiamine) | L | Pyrimidines | 1 | `Cc1ncc(C[n+]2csc(CCO)c2C)c(N)n1` | (-inf, HL, 4.79, L, +inf) |
| ligand_9333 | 3-Hydroxyphenyltrimethylammonium (chloride) | HL | Phenols | 3 | `C[N+](C)(C)c1cccc(O)c1` | (-inf, HL, 8.06, L, +inf) |
| ligand_9334 | 4-Hydroxyphenyltrimethylammonium (chloride) | HL | Phenols | 3 | `C[N+](C)(C)c1ccc(O)cc1` | (-inf, HL, 8.35, L, +inf) |
| ligand_10163 | Chloride ion | *** | Inorganic ligands | 546 | *** | *** |
| ligand_10207 | DL-(3-Amino-3-carbo… (S-Methylmethionine chloride) | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (8 parseable SMILES)

| group | count | % |
|-------|-------|---|
| aromatic_ring | 8 | 100% |
| hydroxyl | 6 | 75% |
| carboxyl | 3 | 38% |
| phenol | 3 | 38% |
| pyridine | 3 | 38% |
| halide | 2 | 25% |
| aldehyde | 1 | 12% |
| primary_amine | 1 | 12% |
| thiazole | 1 | 12% |
| thioether | 1 | 12% |
| thiol | 1 | 12% |

---

### Step 5: `search_ligands`
**Args:**
```json
{
  "name": "bromide",
  "limit": 10
}
```

[summary]
## search_ligands — 2 result(s)

**stats:** 2 SQL matches · showing 2 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_9871 | Dibromomethane (Methylene bromide) | *** | miscellaneous hydrocarbo… | 1 | *** | *** |
| ligand_10168 | Bromide ion | *** | Inorganic ligands | 391 | *** | *** |

---

### Step 6: `search_ligands`
**Args:**
```json
{
  "name": "iodide",
  "limit": 10
}
```

[summary]
## search_ligands — 6 result(s)

**stats:** 6 SQL matches · showing 6 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8435 | Trimethyl(phosphonomethyl)ammonium (iodide) | H2L | Aminophosphorus acids | 4 | `C[N+](C)(C)CP(=O)(O)O` | (-inf, HL, 5.1, L, +inf) |
| ligand_8436 | Dimethyl(phosphonoethyl)(N-methyl-N-phos… (iodide) | H4L | Aminophosphorus acids | 3 | `CN(CC[N+](C)(C)CCP(=O)(O)O)CCP(=O)(O)O` | (-inf, H4L, -1.5, H3L, 5.45, H2L, 6.46, HL, +inf) |
| ligand_9518 | 4-N-Methyltetracycline (iodide) | H2L | Naphtols | 11 | `CC1(O)c2cccc(O)c2C(=O)C2=C(O)C3(O)C(=O)C(C(N)=O)=C(O)C([N+](C)(C)C)C3CC21` | (-inf, H2L, 3.64, HL, 7.5, L, +inf) |
| ligand_9872 | Diiodomethane (Methylene iodide) | *** | miscellaneous hydrocarbo… | 1 | *** | *** |
| ligand_10171 | Iodide ion | *** | Inorganic ligands | 191 | *** | *** |
| ligand_10583 | 2-Hydroxy-N,N,N-trimethylanilinium (iodide) | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (3 parseable SMILES)

| group | count | % |
|-------|-------|---|
| hydroxyl | 3 | 100% |
| phosphonate | 2 | 67% |
| amide | 1 | 33% |
| aromatic_ring | 1 | 33% |
| ketone | 1 | 33% |
| phenol | 1 | 33% |
| tertiary_amine | 1 | 33% |

---

### Step 7: `search_ligands`
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

### Step 8: `search_ligands`
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

### Step 9: `search_ligands`
**Args:**
```json
{
  "name": "bisulfide",
  "limit": 10
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 10: `search_ligands`
**Args:**
```json
{
  "name": "cyanide",
  "limit": 10
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_10090 | Hydrogen cyanide (Hydrocyanic acid) | HL | Inorganic ligands | 194 | `C#N` | (-inf, HL, 9.04, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| nitrile | 1 | 100% |

---

### Step 11: `search_ligands`
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

### Step 12: `search_ligands`
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

### Step 13: `search_ligands`
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

### Step 14: `search_ligands`
**Args:**
```json
{
  "name": "edta",
  "limit": 10
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 5 SQL matches · showing 5 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6118 | 6,11,18,23-Tetraoxo-1,4,7,10,13,16,19,… (24edtaen) | *** | Aza macrocycles with car… | 15 | *** | (-inf, H4L, 3.3, H3L, 4.18, H2L, 7.26, HL, 7.78, L, +inf) |
| ligand_6275 | N-(2-Hydroxyethyl)ethylenedinitrilotriace… (HEDTA) | H3L | EDTA and derivatives | 237 | `O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O` | (-inf, H3L, 2.62, H2L, 5.38, HL, 9.7, L, +inf) |
| ligand_6277 | Ethylenedinitrilotetraacetic acid (EDTA) | H4L | EDTA and derivatives | 596 | `O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O` | (-inf, H5L, -1.5, H4L, 2, H3L, 2.69, H2L, 6.13, HL, 9.52, L, +inf) |
| ligand_6335 | Oxybis(ethylenenitrilo)tetraacetic acid (EEDTA) | H4L | EDTA and derivatives | 124 | `O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O` | (-inf, H4L, -1.8, H3L, 2.76, H2L, 8.75, HL, 9.39, L, +inf) |
| ligand_6348 | Thiobis(ethylenenitrilo)tetraacetic acid (TEDTA) | H4L | EDTA and derivatives | 101 | `O=C(O)CN(CCSCCN(CC(=O)O)CC(=O)O)CC(=O)O` | (-inf, H4L, 2, H3L, 2.68, H2L, 8.37, HL, 9.31, L, +inf) |

### Functional groups across all SQL matches (4 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 4 | 100% |
| tertiary_amine | 4 | 100% |
| ether | 1 | 25% |
| hydroxyl | 1 | 25% |
| thioether | 1 | 25% |

---

### Step 15: `search_ligands`
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

### Step 16: `search_ligands`
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

### Step 17: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.ligand_id = ligand_10163 AND s.solvent_name LIKE '%water%' AND s.temperature_c BETWEEN 23 AND 27 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l BETWEEN 0 AND 1))",
  "order_by": "s.temperature_c ASC, s.constant_value DESC",
  "limit": 30
}
```

[summary]
## search_stability

*(no results)*

---

### Step 18: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.ligand_id = ligand_10168 AND s.solvent_name LIKE '%water%' AND s.temperature_c BETWEEN 23 AND 27 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l BETWEEN 0 AND 1))",
  "order_by": "s.temperature_c ASC, s.constant_value DESC",
  "limit": 30
}
```

[summary]
## search_stability

*(no results)*

---

### Step 19: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.ligand_id = ligand_10171 AND s.solvent_name LIKE '%water%' AND s.temperature_c BETWEEN 23 AND 27 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l BETWEEN 0 AND 1))",
  "order_by": "s.temperature_c ASC, s.constant_value DESC",
  "limit": 30
}
```

[summary]
## search_stability

*(no results)*

---

### Step 20: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.ligand_id = ligand_10076 AND s.solvent_name LIKE '%water%' AND s.temperature_c BETWEEN 23 AND 27 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l BETWEEN 0 AND 1))",
  "order_by": "s.temperature_c ASC, s.constant_value DESC",
  "limit": 30
}
```

[summary]
## search_stability

*(no results)*

---

### Step 21: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.ligand_id = ligand_10144 AND s.solvent_name LIKE '%water%' AND s.temperature_c BETWEEN 23 AND 27 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l BETWEEN 0 AND 1))",
  "order_by": "s.temperature_c ASC, s.constant_value DESC",
  "limit": 30
}
```

[summary]
## search_stability

*(no results)*

---

### Step 22: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.ligand_id = ligand_10090 AND s.solvent_name LIKE '%water%' AND s.temperature_c BETWEEN 23 AND 27 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l BETWEEN 0 AND 1))",
  "order_by": "s.temperature_c ASC, s.constant_value DESC",
  "limit": 30
}
```

[summary]
## search_stability

*(no results)*

---

### Step 23: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.ligand_id = ligand_10103 AND s.solvent_name LIKE '%water%' AND s.temperature_c BETWEEN 23 AND 27 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l BETWEEN 0 AND 1))",
  "order_by": "s.temperature_c ASC, s.constant_value DESC",
  "limit": 30
}
```

[summary]
## search_stability

*(no results)*

---

### Step 24: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.ligand_id = ligand_7029 AND s.solvent_name LIKE '%water%' AND s.temperature_c BETWEEN 23 AND 27 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l BETWEEN 0 AND 1))",
  "order_by": "s.temperature_c ASC, s.constant_value DESC",
  "limit": 30
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
  "where": "(c.metal_id = metal_71 AND c.ligand_id = ligand_6277 AND s.solvent_name LIKE '%water%' AND s.temperature_c BETWEEN 23 AND 27 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l BETWEEN 0 AND 1))",
  "order_by": "s.temperature_c ASC, s.constant_value DESC",
  "limit": 30
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
  "where": "(c.metal_id = metal_71 AND c.ligand_id = ligand_5856 AND s.solvent_name LIKE '%water%' AND s.temperature_c BETWEEN 23 AND 27 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l BETWEEN 0 AND 1))",
  "order_by": "s.temperature_c ASC, s.constant_value DESC",
  "limit": 30
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
  "where": "(c.metal_id = metal_71 AND c.ligand_id = ligand_6592 AND s.solvent_name LIKE '%water%' AND s.temperature_c BETWEEN 23 AND 27 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l BETWEEN 0 AND 1))",
  "order_by": "s.temperature_c ASC, s.constant_value DESC",
  "limit": 30
}
```

[summary]
## search_stability

*(no results)*

---

### Step 28: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_72 AND c.ligand_id IN (ligand_10163, ligand_10168, ligand_10171) AND s.solvent_name LIKE '%water%' AND s.temperature_c BETWEEN 23 AND 27 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l BETWEEN 0 AND 1))",
  "order_by": "c.ligand_id ASC, s.temperature_c ASC, s.constant_value DESC",
  "limit": 60
}
```

[summary]
## search_stability

*(no results)*

---

### Step 29: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_72 AND c.ligand_id IN (ligand_5856, ligand_6592, ligand_10090) AND s.solvent_name LIKE '%water%' AND s.temperature_c BETWEEN 23 AND 27 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l BETWEEN 0 AND 1))",
  "order_by": "c.ligand_id ASC, s.temperature_c ASC, s.constant_value DESC",
  "limit": 60
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
  "where": "(c.metal_id = metal_93 AND c.ligand_id IN (ligand_10163, ligand_5856, ligand_6592) AND s.solvent_name LIKE '%water%' AND s.temperature_c BETWEEN 23 AND 27 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l BETWEEN 0 AND 1))",
  "order_by": "c.ligand_id ASC, s.temperature_c ASC, s.constant_value DESC",
  "limit": 60
}
```

[summary]
## search_stability

*(no results)*

---

### Step 31: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_53 AND c.ligand_id IN (ligand_10163, ligand_5856) AND s.solvent_name LIKE '%water%' AND s.temperature_c BETWEEN 23 AND 27 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l BETWEEN 0 AND 1))",
  "order_by": "c.ligand_id ASC, s.temperature_c ASC, s.constant_value DESC",
  "limit": 40
}
```

[summary]
## search_stability

*(no results)*

---

### Step 32: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.ligand_id = ligand_10163 AND m.condition_temp_min <= 25 AND m.condition_temp_max >= 25 AND (m.condition_ionic_min IS NULL OR m.condition_ionic_min >= 0) AND (m.condition_ionic_max IS NULL OR m.condition_ionic_max <= 1))",
  "order_by": "n.node_count DESC",
  "limit": 3
}
```

[summary]
## search_networks — 4 row(s)

> **Reference equilibrium networks** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### `Hg^[2+]` + Chloride ion — 1 network(s)
metal_id: metal_71 | ligand_id: ligand_10163 | ligand_def_HxL: *** | ligand_SMILES: ***

| beta_def | equation |
|----------|----------|
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |
| beta_def_872 | ``[M] + [L]^3 <=> [ML3]`` |
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_894 | ``[M] + [L]^4 <=> [ML4]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_29920 | 4 | 6 | 19~29 | 0.35~0.65 | 4 | 4 diff beta_def | logK | 6.74~15.2 |

#### Reference-state network: ref_eq_net_29920 (4 nodes)
> First network — reference conditions (T 19~29 °C, I 0.35~0.65 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 6.74 |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` | logK | 13.22 |
| beta_def_872 | ``[M] + [L]^3 <=> [ML3]`` | logK | 14.2 |
| beta_def_894 | ``[M] + [L]^4 <=> [ML4]`` | logK | 15.2 |

---

### Step 33: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.ligand_id = ligand_10144 AND m.condition_temp_min <= 25 AND m.condition_temp_max >= 25 AND (m.condition_ionic_min IS NULL OR m.condition_ionic_min >= 0) AND (m.condition_ionic_max IS NULL OR m.condition_ionic_max <= 1))",
  "order_by": "n.node_count DESC",
  "limit": 3
}
```

[summary]
## search_networks

*(no results)*

---

### Step 34: `search_pka_ligands`
**Args:**
```json
{
  "where": "(lc.ligand_id = ligand_5856 AND p.temperature_c BETWEEN 23 AND 27 AND p.solvent_name LIKE '%water%')",
  "order_by": "p.temperature_c ASC",
  "limit": 10
}
```

[summary]
## search_pka_ligands

*(no results)*

---

### Step 35: `search_pka_ligands`
**Args:**
```json
{
  "where": "(lc.ligand_id = ligand_6592 AND p.temperature_c BETWEEN 23 AND 27 AND p.solvent_name LIKE '%water%')",
  "order_by": "p.temperature_c ASC",
  "limit": 10
}
```

[summary]
## search_pka_ligands

*(no results)*

---

### Step 36: `search_pka_ligands`
**Args:**
```json
{
  "where": "(lc.ligand_id = ligand_10103 AND p.temperature_c BETWEEN 23 AND 27 AND p.solvent_name LIKE '%water%')",
  "order_by": "p.temperature_c ASC",
  "limit": 10
}
```

[summary]
## search_pka_ligands

*(no results)*

---

### Step 37: `search_pka_ligands`
**Args:**
```json
{
  "where": "(lc.ligand_id = ligand_10090 AND p.temperature_c BETWEEN 23 AND 27 AND p.solvent_name LIKE '%water%')",
  "order_by": "p.temperature_c ASC",
  "limit": 10
}
```

[summary]
## search_pka_ligands

*(no results)*

---

### Step 38: `search_pka_ligands`
**Args:**
```json
{
  "where": "(lc.ligand_id = ligand_6277 AND p.temperature_c BETWEEN 23 AND 27 AND p.solvent_name LIKE '%water%')",
  "order_by": "p.temperature_c ASC",
  "limit": 10
}
```

[summary]
## search_pka_ligands

*(no results)*

---
