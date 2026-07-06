# Q3.1.2 — Tool Results (batch 5)

### Step 2: `search_metals`
**Args:**
```json
{
  "symbol": "Cu",
  "limit": 5
}
```

[summary]
## search_metals — 3 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_41 | Cu^[2+] | Cu | 2 | ✓ | [Cu+2] | InChI=1S/Cu/q+2 | beta_totN_264 | ligand_totN_1951 | vlm_totN_8963 |
| metal_42 | Cu^[+] | Cu | 1 | ✓ | [Cu+] | InChI=1S/Cu/q+1 | beta_totN_32 | ligand_totN_117 | vlm_totN_285 |
| metal_43 | Cu^[3+] | Cu | 3 | ✓ | [Cu+3] | InChI=1S/Cu/q+3 | beta_totN_4 | ligand_totN_8 | vlm_totN_10 |

---

### Step 3: `search_metals`
**Args:**
```json
{
  "symbol": "Ni",
  "limit": 5
}
```

[summary]
## search_metals — 2 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_112 | Ni^[2+] | Ni | 2 | ✓ | [Ni+2] | InChI=1S/Ni/q+2 | beta_totN_149 | ligand_totN_1369 | vlm_totN_5325 |
| metal_113 | Ni^[3+] | Ni | 3 | ✓ | [Ni+3] | InChI=1S/Ni/q+3 | beta_totN_5 | ligand_totN_4 | vlm_totN_7 |

---

### Step 4: `search_ligands`
**Args:**
```json
{
  "name": "histidine",
  "limit": 10
}
```

[summary]
## search_ligands — 10 result(s)

**stats:** 57 SQL matches · showing 10 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5860 | DL-2-Amino-3-(2-mercaptoimidazo-4… (Thiohistidine) | H2L | Amino Acids | 20 | `NC(Cc1cnc(S)[nH]1)C(=O)O` | (-inf, H2L, 8.59, HL, 8.59, L, +inf) |
| ligand_5898 | L-2-Amino-3-(4-imidazolyl)propanoic a… (Histidine) | HL | Amino Acids | 250 | `N[C@@H](Cc1c[nH]cn1)C(=O)O` | (-inf, H3L, -1.7, H2L, 6.05, HL, 9.1, L, +inf) |
| ligand_5899 | L-2-Amino-3-(N(1)-methyl-4-imidazolyl)propanoic a… | HL | Amino Acids | 14 | `Cn1cnc(C[C@H](N)C(=O)O)c1` | (-inf, H3L, -1.72, H2L, 5.87, HL, 9.16, L, +inf) |
| ligand_5900 | L-2-Amino-3-(N(3)-methyl-4-imidazolyl)propanoic a… | HL | Amino Acids | 16 | `Cn1cncc1C[C@H](N)C(=O)O` | (-inf, H3L, -1.65, H2L, 6.48, HL, 8.61, L, +inf) |
| ligand_5901 | L-4-(2-Amino-3-carboxypropyl)-1,3-dimethylimidazo… | HL | Amino Acids | 6 | `Cn1c[n+](C)cc1C[C@H](N)C(=O)O` | (-inf, H2L, -1.98, HL, 7.85, L, +inf) |
| ligand_5902 | L-1-Carboxy-2-(4-imidazolyl)ethyl(dimethyl)ammoni… | HL | Amino Acids | 9 | `C[NH+](C)C(Cc1cnc[nH]1)C(=O)O` | (-inf, H3L, -1.03, H2L, 6.03, HL, 8.86, L, +inf) |
| ligand_5903 | L-1-Carboxy-2-(4-imidazolyl)ethyl(trimethyl)ammon… | HL | Amino Acids | 6 | `C[N+](C)(C)C(Cc1c[nH]cn1)C(=O)O` | (-inf, H2L, -0.98, HL, 6, L, +inf) |
| ligand_5904 | L-2-Amino-3-(N(3)-benzyl-4-imidazolyl)propanoic a… | HL | Amino Acids | 18 | `NC(Cc1cncn1Cc1ccccc1)C(=O)O` | (-inf, H3L, 1.94, H2L, 5.53, HL, 9.21, L, +inf) |
| ligand_5905 | L-2-Amino-3-(5-iodo-4-imidazol… (5-Iodo-Histidine) | HL | Amino Acids | 23 | `N[C@@H](Cc1nc[nH]c1I)C(=O)O` | (-inf, H3L, -1.47, H2L, 4.21, HL, 8.6, L, +inf) |
| ligand_5906 | L-2-Amino-3-(2,5-diiodo-4-… (2,5-Diiodo-Histidine) | HL | Amino Acids | 27 | `N[C@@H](Cc1nc(I)[nH]c1I)C(=O)O` | (-inf, H4L, -1.55, H3L, 2.74, H2L, 8.12, HL, 9.57, L, +inf) |

### Functional groups across all SQL matches (46 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 40 | 87% |
| aromatic_ring | 38 | 83% |
| amide | 31 | 67% |
| primary_amine | 26 | 57% |
| imine | 9 | 20% |
| ester | 5 | 11% |
| secondary_amine | 5 | 11% |
| thiol | 4 | 9% |
| hydroxyl | 3 | 7% |
| halide | 2 | 4% |
| phenol | 2 | 4% |
| pyridine | 1 | 2% |
| tertiary_amine | 1 | 2% |
| thioether | 1 | 2% |

---

### Step 5: `search_ligands`
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

### Step 6: `search_ligands`
**Args:**
```json
{
  "name": "aspartic acid",
  "limit": 10
}
```

[summary]
## search_ligands — 10 result(s)

**stats:** 22 SQL matches · showing 10 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5802 | L-Aminobutanedioic acid (Aspartic acid) | H2L | Amino Acids | 174 | `N[C@@H](CC(=O)O)C(=O)O` | (-inf, H3L, 1.95, H2L, 3.71, HL, 9.66, L, +inf) |
| ligand_5803 | DL-2-Amino-3-methylbutane… (3-Methylaspartic acid) | H2L | Amino Acids | 6 | `CC(C(=O)O)[C@H](N)C(=O)O` | (-inf, H3L, 1.99, H2L, 3.59, HL, 9.48, L, +inf) |
| ligand_6389 | Glycyl-L-aspartic acid | H2L | Peptides | 34 | `NCC(=O)N[C@@H](CC(=O)O)C(=O)O` | (-inf, H3L, 2.8, H2L, 4.3, HL, 8.34, L, +inf) |
| ligand_6561 | L-Aspartyl-L-aspartyl-L-aspartic acid | *** | tripeptides | 10 | *** | (-inf, H5L, -1.8, H4L, 2.04, H3L, 3.87, H2L, 4.78, HL, 8.13, L, +inf) |
| ligand_6585 | L-Arginyl-L-lysyl-L-aspartic acid | *** | tripeptides | 11 | *** | (-inf, H4L, 2.77, H3L, 4.2, H2L, 7.44, HL, 10.49, L, +inf) |
| ligand_6586 | D-Arginyl-L-lysyl-L-aspartic acid | *** | tripeptides | 8 | *** | (-inf, H4L, 2.76, H3L, 4.2, H2L, 7.5, HL, 10.29, L, +inf) |
| ligand_6587 | L-Arginyl-D-lysyl-L-aspartic acid | H2L | tripeptides | 8 | `N=C(N)NCCC[C@H](N)C(=O)N[C@H](CCCCN)C(=O)N[C@@H](CC(=O)O)C(=O)O` | (-inf, H4L, 2.78, H3L, 4.07, H2L, 7.39, HL, 10.45, L, +inf) |
| ligand_6588 | L-Arginyl-L-lysyl-D-aspartic acid | *** | tripeptides | 8 | *** | (-inf, H4L, 2.71, H3L, 4.12, H2L, 7.42, HL, 10.55, L, +inf) |
| ligand_6621 | L-Alanyl-L-alanyl-L-alanyl-L-aspartic acid | H2L | polypeptides | 7 | `C[C@H](N)C(=O)N[C@@H](C)C(=O)N[C@@H](C)C(=O)N[C@@H](CC(=O)O)C(=O)O` | (-inf, H3L, 3.15, H2L, 4.01, HL, 8.05, L, +inf) |
| ligand_6629 | L-Aspartyl-L-alanyl-L-alanyl-L-aspartic acid | *** | polypeptides | 9 | *** | (-inf, H4L, 3.12, H3L, 3.26, H2L, 4.64, HL, 8, L, +inf) |

### Functional groups across all SQL matches (8 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 8 | 100% |
| primary_amine | 7 | 88% |
| amide | 5 | 62% |
| secondary_amine | 2 | 25% |
| aromatic_ring | 1 | 12% |
| imine | 1 | 12% |

---

### Step 7: `search_ligands`
**Args:**
```json
{
  "name": "glutamic acid",
  "limit": 10
}
```

[summary]
## search_ligands — 10 result(s)

**stats:** 23 SQL matches · showing 10 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5804 | L-2-Aminopentanedioic acid (Glutamic acid) | H2L | Amino Acids | 94 | `N[C@@H](CCC(=O)O)C(=O)O` | (-inf, H3L, 2.16, H2L, 4.15, HL, 9.58, L, +inf) |
| ligand_5805 | DL-2-Amino-2-methylpentan… (2-Methylglutamic acid) | H2L | Amino Acids | 4 | `C[C@](N)(CCC(=O)O)C(=O)O` | (-inf, H2L, 4.05, HL, 9.72, L, +inf) |
| ligand_5807 | DL-2-Amino-3-hydroxypent… (3-Hydroxyglutamic acid) | H2L | Amino Acids | 8 | `N[C@H](C(=O)O)C(O)CC(=O)O` | (-inf, H3L, 2.09, H2L, 4.08, HL, 9.06, L, +inf) |
| ligand_6390 | Glycyl-L-glutamic acid | H2L | Peptides | 25 | `NCC(=O)N[C@@H](CCC(=O)O)C(=O)O` | (-inf, H3L, 2.83, H2L, 4.34, HL, 8.3, L, +inf) |
| ligand_6485 | L-Tyrosyl-L-glutamic acid | H3L | Peptides | 11 | `N[C@@H](Cc1ccc(O)cc1)C(=O)N[C@@H](CCC(=O)O)C(=O)O` | (-inf, H4L, 3.17, H3L, 4.48, H2L, 7.69, HL, 10.09, L, +inf) |
| ligand_6486 | L-Tyrosyl-D-glutamic acid | H3L | Peptides | 11 | `N[C@@H](Cc1ccc(O)cc1)C(=O)N[C@H](CCC(=O)O)C(=O)O` | (-inf, H4L, 2.85, H3L, 4.65, H2L, 7.85, HL, 10.17, L, +inf) |
| ligand_6503 | L-Seryl-L-glutamic acid | H2L | Peptides | 3 | `N[C@@H](CO)C(=O)N[C@@H](CCC(=O)O)C(=O)O` | (-inf, H3L, 2.94, H2L, 4.34, HL, 7.42, L, +inf) |
| ligand_6504 | L-P… (L-Seryl-L-glutamic acid dihydrogenphosphate) | H4L | Peptides | 25 | `NC(COP(=O)(O)O)C(=O)NC(CCC(=O)O)C(=O)O` | (-inf, H4L, 3.04, H3L, 4.4, H2L, 5.69, HL, 8.22, L, +inf) |
| ligand_6662 | Glycyl-L-prolylglycyl-L-prolylglutamic acid | H2L | polypeptides | 5 | `NCC(=O)N1CCC[C@H]1C(=O)NCC(=O)N1CCC[C@H]1C(=O)N[C@@H](CCC(=O)O)C(=O)O` | (-inf, H3L, 2.46, H2L, 4.4, HL, 8.53, L, +inf) |
| ligand_6938 | DL-Glutamic acid dimethyl ester | L | Aliphatic amines | 1 | `COC(=O)CCC(N)C(=O)OC` | (-inf, HL, 7.03, L, +inf) |

### Functional groups across all SQL matches (17 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 15 | 88% |
| amide | 12 | 71% |
| primary_amine | 11 | 65% |
| aromatic_ring | 5 | 29% |
| hydroxyl | 5 | 29% |
| ester | 2 | 12% |
| phenol | 2 | 12% |
| phosphate | 1 | 6% |
| tertiary_amine | 1 | 6% |

---

### Step 8: `search_ligands`
**Args:**
```json
{
  "name": "glycine",
  "limit": 10
}
```

[summary]
## search_ligands — 10 result(s)

**stats:** 170 SQL matches · showing 10 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5760 | Aminoacetic acid (Glycine) | HL | Amino Acids | 428 | `NCC(=O)O` | (-inf, H2L, 2.33, HL, 9.57, L, +inf) |
| ligand_5776 | DL-Aminophenylacetic acid (Phenylglycine) | HL | Amino Acids | 12 | `NC(C(=O)O)c1ccccc1` | (-inf, H2L, -1.9, HL, 8.92, L, +inf) |
| ligand_5786 | DL-Amino-4-sulfophenylacet… (4-Sulfophenylglycine) | H2L | Amino Acids | 12 | `NC(C(=O)O)c1ccc(S(=O)(=O)O)cc1` | (-inf, H2L, -1.8, HL, 8.66, L, +inf) |
| ligand_5838 | DL-Amino-4-Methoxyphenyl… (4-Methoxyphenylglycine) | HL | Amino Acids | 12 | `COc1ccc(C(N)C(=O)O)cc1` | (-inf, H2L, 2, HL, 9.07, L, +inf) |
| ligand_5925 | N-Methylglycine (Sarcosine) | HL | Amino Acids | 39 | `CNCC(=O)O` | (-inf, H2L, 2.18, HL, 9.98, L, +inf) |
| ligand_5926 | N-Ethylglycine | HL | Amino Acids | 6 | `CCNCC(=O)O` | (-inf, H2L, 2.3, HL, 10.1, L, +inf) |
| ligand_5927 | N-Propylglycine | HL | Amino Acids | 6 | `CCCNCC(=O)O` | (-inf, H2L, 2.28, HL, 10.03, L, +inf) |
| ligand_5928 | N-Butylglycine | HL | Amino Acids | 6 | `CCCCNCC(=O)O` | (-inf, H2L, 2.29, HL, 10.07, L, +inf) |
| ligand_5929 | N-(2-Propyl)glycine | HL | Amino Acids | 5 | `CC(C)NCC(=O)O` | (-inf, H2L, 2.36, HL, 10.06, L, +inf) |
| ligand_5937 | N-(Phosphonomethyl)glycine (Glyphosate) | H3L | Amino Acids | 146 | `O=C(O)CNCP(=O)(O)O` | (-inf, H4L, -0.5, H3L, 2.2, H2L, 5.45, HL, 10.1, L, +inf) |

### Functional groups across all SQL matches (129 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 114 | 88% |
| amide | 96 | 74% |
| primary_amine | 78 | 60% |
| aromatic_ring | 26 | 20% |
| hydroxyl | 25 | 19% |
| secondary_amine | 22 | 17% |
| tertiary_amine | 14 | 11% |
| ester | 9 | 7% |
| thiol | 9 | 7% |
| phenol | 7 | 5% |
| imine | 5 | 4% |
| phosphonate | 3 | 2% |
| thioether | 3 | 2% |
| phosphate | 2 | 2% |
| pyridine | 2 | 2% |
| sulfonate | 2 | 2% |
| ether | 1 | 1% |

---

### Step 9: `search_ligands`
**Args:**
```json
{
  "name": "proline",
  "limit": 10
}
```

[summary]
## search_ligands — 10 result(s)

**stats:** 28 SQL matches · showing 10 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5930 | L-Pyrrolidine-2-carboxylic acid (L-Proline) | HL | Amino Acids | 66 | `O=C(O)C1CCCN1` | (-inf, H2L, 1.89, HL, 10.46, L, +inf) |
| ligand_5935 | S-(1-Carboxy-3-phenylpropyl)-L-alan… (Enalaprilat) | H2L | Amino Acids | 15 | `C[C@H](N[C@@H](CCc1ccccc1)C(=O)O)C(=O)N1CCC[C@H]1C(=O)O` | (-inf, H3L, -1.6, H2L, 3.26, HL, 7.54, L, +inf) |
| ligand_5941 | L-4-Hydroxypyrrolidine-2-carbo… (L-Hydroxyproline) | HL | Amino Acids | 46 | `O=C(O)C1CC(O)CN1` | (-inf, H2L, 1.77, HL, 9.47, L, +inf) |
| ligand_5942 | DL-1,3-Thiazolidine-4-carboxylic… (DL-Thiaproline) | HL | Amino Acids | 22 | `O=C(O)C1CSCN1` | (-inf, H2L, -1.5, HL, -1.5, L, +inf) |
| ligand_6018 | L-N-Benzylproline | HL | Amino Acids | 15 | `O=C(O)[C@@H]1CCCN1Cc1ccccc1` | (-inf, H2L, 1.97, HL, 9.93, L, +inf) |
| ligand_6388 | Glycyl-L-proline | HL | Peptides | 20 | `NCC(=O)N1CCC[C@H]1C(=O)O` | (-inf, H2L, 2.82, HL, 8.46, L, +inf) |
| ligand_6395 | Glycyl-L-hydroxyproline | HL | Peptides | 2 | `NCC(=O)N1CC(O)C[C@H]1C(=O)O` | (-inf, H2L, 2.8, HL, 8.37, L, +inf) |
| ligand_6431 | L-Alanyl-L-proline | HL | Peptides | 8 | `C[C@H](N)C(=O)N1CCC[C@H]1C(=O)O` | (-inf, H2L, 2.9, HL, 8.4, L, +inf) |
| ligand_6489 | L-Tyrosyl-L-proline | H2L | Peptides | 6 | `N[C@@H](Cc1ccc(O)cc1)C(=O)N1CCC[C@H]1C(=O)O` | (-inf, H3L, 3.19, H2L, 7.81, HL, 9.91, L, +inf) |
| ligand_6608 | Glycylglycylglycyl-L-proline | HL | polypeptides | 6 | `NCC(=O)NCC(=O)NCC(=O)N1CCC[C@H]1C(=O)O` | (-inf, H2L, 2.91, HL, 8.04, L, +inf) |

### Functional groups across all SQL matches (15 parseable SMILES)

| group | count | % |
|-------|-------|---|
| amide | 11 | 73% |
| carboxyl | 11 | 73% |
| primary_amine | 6 | 40% |
| aromatic_ring | 5 | 33% |
| hydroxyl | 4 | 27% |
| secondary_amine | 4 | 27% |
| imine | 2 | 13% |
| phenol | 2 | 13% |
| pyridine | 1 | 7% |
| tertiary_amine | 1 | 7% |
| thioether | 1 | 7% |

---

### Step 10: `search_ligands`
**Args:**
```json
{
  "name": "methionine",
  "limit": 10
}
```

[summary]
## search_ligands — 10 result(s)

**stats:** 22 SQL matches · showing 10 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5863 | L-2-Amino-4-(methylthio)butanoic acid (Methionine) | HL | Amino Acids | 63 | `CSCC[C@H](N)C(=O)O` | (-inf, H2L, 2.18, HL, 9.08, L, +inf) |
| ligand_6192 | N,N,S-Tris(carboxymethyl)methionine | H4L | NTA and derivatives | 4 | `C[S+](CC[C@@H](C(=O)O)N(CC(=O)O)CC(=O)O)CC(=O)O` | (-inf, H4L, 2.1, H3L, 2.6, H2L, 7.49, HL, 7.49, L, +inf) |
| ligand_6399 | Glycyl-L-methionine | HL | Peptides | 26 | `CSCC[C@H](NC(=O)CN)C(=O)O` | (-inf, H2L, 3.02, HL, 8.12, L, +inf) |
| ligand_6475 | L-Phenylalanyl-L-methionine | HL | Peptides | 12 | `CSCC[C@H](NC(=O)[C@@H](N)Cc1ccccc1)C(=O)O` | (-inf, H2L, 3.24, HL, 7.27, L, +inf) |
| ligand_6519 | L-S-Methylcysteinyl-L-methionine | HL | Peptides | 9 | `CSCC[C@H](NC(=O)[C@@H](N)CSC)C(=O)O` | (-inf, H2L, 3.18, HL, 7.03, L, +inf) |
| ligand_6520 | L-S-Methylcysteinyl-D-methionine | HL | Peptides | 9 | `CSCC[C@@H](NC(=O)[C@@H](N)CSC)C(=O)O` | (-inf, H2L, 2.94, HL, 7.23, L, +inf) |
| ligand_6523 | L-Methionyl-L-methionine | HL | Peptides | 18 | `CSCC[C@H](NC(=O)[C@@H](N)CCSC)C(=O)O` | (-inf, H2L, 3.22, HL, 7.41, L, +inf) |
| ligand_6524 | L-Methionyl-D-methionine | HL | Peptides | 17 | `CSCC[C@H](N)C(=O)N[C@H](CCSC)C(=O)O` | (-inf, H2L, 2.98, HL, 7.59, L, +inf) |
| ligand_6526 | L-Histidyl-L-methionine | HL | Peptides | 7 | `CSCC[C@H](NC(=O)[C@@H](N)Cc1c[nH]cn1)C(=O)O` | (-inf, H3L, 2.58, H2L, 6, HL, 7.5, L, +inf) |
| ligand_6671 | L-Tyrosylglycylglycyl-L-p… (Methionine enkephalin) | *** | polypeptides | 8 | *** | (-inf, H3L, 3.46, H2L, 7.44, HL, 9.82, L, +inf) |

### Functional groups across all SQL matches (13 parseable SMILES)

| group | count | % |
|-------|-------|---|
| primary_amine | 12 | 92% |
| thioether | 12 | 92% |
| amide | 9 | 69% |
| carboxyl | 9 | 69% |
| aromatic_ring | 3 | 23% |
| ester | 1 | 8% |
| secondary_amine | 1 | 8% |
| tertiary_amine | 1 | 8% |

---

### Step 12: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_41 AND c.ligand_id = ligand_5760 AND s.temperature_c BETWEEN 20 AND 30 AND (s.solvent_name IS NULL OR LOWER(s.solvent_name) LIKE '%water%') AND (s.ionic_strength_mol_l IS NULL OR (s.ionic_strength_mol_l BETWEEN 0.05 AND 0.2))",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 13: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_112 AND c.ligand_id = ligand_5760 AND s.temperature_c BETWEEN 20 AND 30 AND (s.solvent_name IS NULL OR LOWER(s.solvent_name) LIKE '%water%') AND (s.ionic_strength_mol_l IS NULL OR (s.ionic_strength_mol_l BETWEEN 0.05 AND 0.2))",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 14: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_41 AND c.ligand_id = ligand_5898 AND s.temperature_c BETWEEN 20 AND 30 AND (s.solvent_name IS NULL OR LOWER(s.solvent_name) LIKE '%water%') AND (s.ionic_strength_mol_l IS NULL OR (s.ionic_strength_mol_l BETWEEN 0.05 AND 0.2))",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 15: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_112 AND c.ligand_id = ligand_5898 AND s.temperature_c BETWEEN 20 AND 30 AND (s.solvent_name IS NULL OR LOWER(s.solvent_name) LIKE '%water%') AND (s.ionic_strength_mol_l IS NULL OR (s.ionic_strength_mol_l BETWEEN 0.05 AND 0.2))",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 16: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_41 AND c.ligand_id = ligand_5856 AND s.temperature_c BETWEEN 20 AND 30 AND (s.solvent_name IS NULL OR LOWER(s.solvent_name) LIKE '%water%') AND (s.ionic_strength_mol_l IS NULL OR (s.ionic_strength_mol_l BETWEEN 0.05 AND 0.2))",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 17: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_112 AND c.ligand_id = ligand_5856 AND s.temperature_c BETWEEN 20 AND 30 AND (s.solvent_name IS NULL OR LOWER(s.solvent_name) LIKE '%water%') AND (s.ionic_strength_mol_l IS NULL OR (s.ionic_strength_mol_l BETWEEN 0.05 AND 0.2))",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 18: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_41 AND c.ligand_id = ligand_5802 AND s.temperature_c BETWEEN 20 AND 30 AND (s.solvent_name IS NULL OR LOWER(s.solvent_name) LIKE '%water%') AND (s.ionic_strength_mol_l IS NULL OR (s.ionic_strength_mol_l BETWEEN 0.05 AND 0.2))",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 19: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_112 AND c.ligand_id = ligand_5802 AND s.temperature_c BETWEEN 20 AND 30 AND (s.solvent_name IS NULL OR LOWER(s.solvent_name) LIKE '%water%') AND (s.ionic_strength_mol_l IS NULL OR (s.ionic_strength_mol_l BETWEEN 0.05 AND 0.2))",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 20: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_41 AND c.ligand_id = ligand_5804 AND s.temperature_c BETWEEN 20 AND 30 AND (s.solvent_name IS NULL OR LOWER(s.solvent_name) LIKE '%water%') AND (s.ionic_strength_mol_l IS NULL OR (s.ionic_strength_mol_l BETWEEN 0.05 AND 0.2))",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 21: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_112 AND c.ligand_id = ligand_5804 AND s.temperature_c BETWEEN 20 AND 30 AND (s.solvent_name IS NULL OR LOWER(s.solvent_name) LIKE '%water%') AND (s.ionic_strength_mol_l IS NULL OR (s.ionic_strength_mol_l BETWEEN 0.05 AND 0.2))",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 22: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_41 AND c.ligand_id = ligand_5930 AND s.temperature_c BETWEEN 20 AND 30 AND (s.solvent_name IS NULL OR LOWER(s.solvent_name) LIKE '%water%') AND (s.ionic_strength_mol_l IS NULL OR (s.ionic_strength_mol_l BETWEEN 0.05 AND 0.2))",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 23: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_112 AND c.ligand_id = ligand_5930 AND s.temperature_c BETWEEN 20 AND 30 AND (s.solvent_name IS NULL OR LOWER(s.solvent_name) LIKE '%water%') AND (s.ionic_strength_mol_l IS NULL OR (s.ionic_strength_mol_l BETWEEN 0.05 AND 0.2))",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 24: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_41 AND c.ligand_id = ligand_5863 AND s.temperature_c BETWEEN 20 AND 30 AND (s.solvent_name IS NULL OR LOWER(s.solvent_name) LIKE '%water%') AND (s.ionic_strength_mol_l IS NULL OR (s.ionic_strength_mol_l BETWEEN 0.05 AND 0.2))",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 25: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_112 AND c.ligand_id = ligand_5863 AND s.temperature_c BETWEEN 20 AND 30 AND (s.solvent_name IS NULL OR LOWER(s.solvent_name) LIKE '%water%') AND (s.ionic_strength_mol_l IS NULL OR (s.ionic_strength_mol_l BETWEEN 0.05 AND 0.2))",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 26: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_41"
}
```

[summary]
[CATALOG]
## build_system_catalog — 20 pair(s), 102 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_107 | [M(H-1L)] + [H] <=> [ML] |  |
| beta_def_117 | [M(OH)(H-1L)] + [H] <=> [M(H-1L)] + [H2O] |  |
| beta_def_136 | [M(H-1L)] + [L] <=> [M(H-1L)L] |  |
| beta_def_137 | [M(H-1L)2] + [H] <=> [M(H-1L)L] |  |
| beta_def_194 | [M] + [HL]^2 <=> [M(HL)2] |  |
| beta_def_204 | [MHL2] + [H] <=> [M(HL)2] |  |
| beta_def_238 | [M(OH)2L] + [H] <=> [M(OH)L] + [H2O] |  |
| beta_def_249 | [M(OH)2L2] + [H] <=> [M(OH)L2] + [H2O] |  |
| beta_def_334 | [ML2(s)] <=> [M] + [L]^2 | solid |
| beta_def_347 | [MO(s)] + [H2O] <=> [M] + [OH]^2 | solid |
| beta_def_423 | [ML]^2 + [H2O]^2 <=> [M2(OH)2L2] + [H]^2 |  |
| beta_def_424 | [M]^2 + [L]^2 + [H2O]^2 <=> [M2(OH)2L2] + [H]^2 |  |
| beta_def_427 | [M(OH)L]^2 <=> [M2(OH)2L2] |  |
| beta_def_434 | [M]^2 + [L]^4 + [H2O]^2 <=> [M2(OH)2L4] + [H]^2 |  |
| beta_def_463 | [M2H-2L2] + [H] <=> [M2H-1L2] |  |
| beta_def_477 | [M]^2 + [L]^2 <=> [M2H-2L2] + [H]^2 |  |
| beta_def_502 | [M]^2 + [L] <=> [M2L] |  |
| beta_def_519 | [M]^2 + [L]^2 <=> [M2L2] |  |
| beta_def_567 | [M(H-1L)] + [M(OH)(H-1L)] <=> [M2(OH)(H-1L)2] |  |
| beta_def_630 | [M2H-2L2] + [M] <=> [M3H-2L2] |  |
| beta_def_649 | [M]^3 + [L]^4 <=> [M3L4] |  |
| beta_def_779 | [M] + [HL] <=> [MHL] |  |
| beta_def_788 | [ML] + [H] <=> [MHL] |  |
| beta_def_792 | [ML2] + [H] <=> [MHL2] |  |
| beta_def_798 | [M] + [HL] + [L] <=> [MHL2] |  |
| beta_def_812 | [M] + [L] <=> [ML] |  |
| beta_def_834 | [M(OH)2L] + [H]^2 <=> [ML] + [H2O]^2 |  |
| beta_def_840 | [M] + [L]^2 <=> [ML2] |  |
| beta_def_871 | [M(OH)L2] + [H] <=> [ML2] + [H2O] |  |
| beta_def_872 | [M] + [L]^3 <=> [ML3] |  |
| beta_def_894 | [M] + [L]^4 <=> [ML4] |  |
| beta_def_966 | [M(OH)L] + [H] <=> [ML] + [H2O] |  |
| beta_def_981 | [ML] + [OH] <=> [M(OH)L] |  |
| beta_def_984 | [M(OH)L2] + [H] <=> [ML2] + [H2O] |  |

*(all species aqueous unless noted)*

**1. Cu^[2+] + L-2-Amino-3-(4-imidazolyl)propanoic acid (Histidine)** (metal_41 + ligand_5898) — ligand_def_HxL: HL | 50 ent, 8 sp, 50 vlms (vlm_98835…vlm_98884)
   - species: beta_def_204(8) beta_def_424(4) beta_def_788(7) beta_def_792(8) beta_def_812(8) beta_def_840(7) beta_def_966(3) beta_def_984(5)
   - eq:6 nets T:19~41°C I:-0.05~3.15M max 8n/22e
**2. Cu^[2+] + Ammonia** (metal_41 + ligand_10103) — ligand_def_HxL: L | 49 ent, 4 sp, 49 vlms (vlm_173242…vlm_173290)
   - species: beta_def_812(13) beta_def_840(12) beta_def_872(12) beta_def_894(12)
   - eq:5 nets T:19~30°C I:-0.15~3.15M max 4n/6e
**3. Cu^[2+] + 1,3-Diazole (Imidazole)** (metal_41 + ligand_7795) — ligand_def_HxL: L | 42 ent, 7 sp, 42 vlms (vlm_133893…vlm_133934)
   - species: beta_def_424(1) beta_def_434(2) beta_def_812(10) beta_def_840(10) beta_def_872(10) beta_def_894(7) beta_def_966(2)
   - eq:8 nets T:19~41°C I:-0.15~3.15M max 7n/18e
**4. Cu^[2+] + N,N'-Dimethylethylenediamine** (metal_41 + ligand_7172) — ligand_def_HxL: L | 39 ent, 5 sp, 39 vlms (vlm_125004…vlm_125042)
   - species: beta_def_424(7) beta_def_812(9) beta_def_834(7) beta_def_840(9) beta_def_966(7)
   - eq:5 nets T:19~30°C I:-0.15~2.15M max 5n/8e
**5. Cu^[2+] + Ethanoic acid (Acetic acid)** (metal_41 + ligand_8465) — ligand_def_HxL: HL | 37 ent, 3 sp, 37 vlms (vlm_144741…vlm_144777)
   - species: beta_def_812(16) beta_def_840(16) beta_def_872(5)
   - eq:6 nets T:19~41°C I:-0.15~3.15M max 3n/3e
**6. Cu^[2+] + Glycylglycine (Diglycine)** (metal_41 + ligand_6372) — ligand_def_HxL: HL | 36 ent, 6 sp, 36 vlms (vlm_113537…vlm_113572)
   - species: beta_def_107(7) beta_def_117(6) beta_def_136(7) beta_def_137(1) beta_def_567(5) beta_def_812(10)
   - eq:6 nets T:19~41°C I:-0.15~5.15M max 6n/11e
**7. Cu^[2+] + Hydroxide ion** (metal_41 + ligand_10076) — ligand_def_HxL: *** | 34 ent, 9 sp, 34 vlms (vlm_170713…vlm_170746)
   - species: beta_def_334(5) beta_def_347(2) beta_def_502(3) beta_def_519(9) beta_def_649(4) beta_def_812(7) beta_def_840(2) beta_def_872(1) beta_def_894(1)
   - eq:6 nets T:19~41°C I:-0.15~3.15M max 6n/15e
**8. Cu^[2+] + Ethylenediamine** (metal_41 + ligand_7029) — ligand_def_HxL: L | 34 ent, 2 sp, 34 vlms (vlm_122410…vlm_122443)
   - species: beta_def_812(17) beta_def_840(17)
   - eq:9 nets T:19~41°C I:-0.15~3.15M max 2n/1e
**9. Cu^[2+] + 2,2'-Bipyridyl** (metal_41 + ligand_8156) — ligand_def_HxL: L | 33 ent, 6 sp, 33 vlms (vlm_138609…vlm_138641)
   - species: beta_def_238(3) beta_def_423(3) beta_def_812(8) beta_def_840(8) beta_def_872(8) beta_def_966(3)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 6n/8e
**10. Cu^[2+] + L-2-Amino-3-phenylpropanoic acid (Phenylalanine)** (metal_41 + ligand_5777) — ligand_def_HxL: HL | 33 ent, 3 sp, 33 vlms (vlm_95053…vlm_95085)
   - species: beta_def_788(1) beta_def_812(15) beta_def_840(17)
   - eq:7 nets T:5~45°C I:-0.15~3.15M max 3n/2e
**11. Cu^[2+] + Iminodiacetic acid (IDA)** (metal_41 + ligand_6127) — ligand_def_HxL: H2L | 32 ent, 4 sp, 32 vlms (vlm_104366…vlm_104397)
   - species: beta_def_788(3) beta_def_812(13) beta_def_840(14) beta_def_966(2)
   - eq:6 nets T:19~41°C I:-0.15~1.15M max 4n/4e
**12. Cu^[2+] + L-2-Amino-3-hydroxybutanoic acid (Threonine)** (metal_41 + ligand_5829) — ligand_def_HxL: HL | 32 ent, 5 sp, 32 vlms (vlm_96743…vlm_96774)
   - species: beta_def_249(3) beta_def_812(12) beta_def_840(12) beta_def_966(1) beta_def_984(4)
   - eq:6 nets T:19~41°C I:-0.15~3.15M max 4n/4e
**13. Cu^[2+] + Aminoacetic acid (Glycine)** (metal_41 + ligand_5760) — ligand_def_HxL: HL | 30 ent, 2 sp, 30 vlms (vlm_93847…vlm_93876)
   - species: beta_def_812(15) beta_def_840(15)
   - eq:9 nets T:5~45°C I:-0.15~2.65M max 2n/1e
**14. Cu^[2+] + N-(2-Hydroxyethyl)iminodiacetic acid (HIDA)** (metal_41 + ligand_6204) — ligand_def_HxL: H2L | 29 ent, 4 sp, 29 vlms (vlm_106728…vlm_106756)
   - species: beta_def_812(13) beta_def_840(13) beta_def_966(1) beta_def_984(2)
   - eq:4 nets T:19~30°C I:-0.15~1.15M max 4n/4e
**15. Cu^[2+] + Pyridine (Azine)** (metal_41 + ligand_7890) — ligand_def_HxL: L | 28 ent, 5 sp, 28 vlms (vlm_135256…vlm_135283)
   - species: beta_def_812(7) beta_def_840(7) beta_def_872(7) beta_def_894(6) beta_def_966(1)
   - eq:5 nets T:19~30°C I:-0.15~1.15M max 5n/7e
**16. Cu^[2+] + 1,4,9-Triazanonane (2,4-tri)** (metal_41 + ligand_7214) — ligand_def_HxL: L | 28 ent, 6 sp, 28 vlms (vlm_125799…vlm_125826)
   - species: beta_def_194(4) beta_def_779(6) beta_def_798(3) beta_def_812(6) beta_def_840(3) beta_def_981(6)
   - eq:2 nets T:19~30°C I:-0.05~0.65M max 6n/11e
**17. Cu^[2+] + DL-2,6-Diamino-5-hydroxyhexanoic acid** (metal_41 + ligand_5889) — ligand_def_HxL: HL | 28 ent, 7 sp, 28 vlms (vlm_98553…vlm_98580)
   - species: beta_def_194(4) beta_def_204(4) beta_def_463(4) beta_def_477(4) beta_def_630(4) beta_def_779(4) beta_def_788(4)
   - eq:2 nets T:20~41°C I:-0.05~0.3M max 7n/15e
**18. Cu^[2+] + 4-(2-Aminoethyl)imidazole (Histamine)** (metal_41 + ligand_7849) — ligand_def_HxL: L | 27 ent, 6 sp, 27 vlms (vlm_134661…vlm_134687)
   - species: beta_def_424(4) beta_def_788(3) beta_def_792(4) beta_def_812(6) beta_def_840(6) beta_def_871(4)
   - eq:4 nets T:19~41°C I:-0.15~1.15M max 6n/12e
**19. Cu^[2+] + 2-(2-Aminoethylamino)ethanol [N-(2-Hydroxyethyl)ethylenediamine]** (metal_41 + ligand_7181) — ligand_def_HxL: L | 27 ent, 5 sp, 27 vlms (vlm_125163…vlm_125189)
   - species: beta_def_427(4) beta_def_812(7) beta_def_834(5) beta_def_840(7) beta_def_966(4)
   - eq:5 nets T:19~30°C I:-0.15~2.15M max 5n/5e
**20. Cu^[2+] + Glycyl-L-alanine** (metal_41 + ligand_6375) — ligand_def_HxL: HL | 27 ent, 5 sp, 27 vlms (vlm_113707…vlm_113733)
   - species: beta_def_107(6) beta_def_117(6) beta_def_136(6) beta_def_567(3) beta_def_812(6)
   - eq:2 nets T:19~30°C I:-0.05~0.65M max 5n/8e

---

### Step 27: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_112"
}
```

[summary]
[CATALOG]
## build_system_catalog — 20 pair(s), 95 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_137 | [M(H-1L)2] + [H] <=> [M(H-1L)L] |  |
| beta_def_194 | [M] + [HL]^2 <=> [M(HL)2] |  |
| beta_def_204 | [MHL2] + [H] <=> [M(HL)2] |  |
| beta_def_208 | [M] + [HL]^3 <=> [M(HL)3] |  |
| beta_def_214 | [MH2L3] + [H] <=> [M(HL)3] |  |
| beta_def_374 | [M]^2 + [L]^2 <=> [M2(H-1L)2] + [H]^2 |  |
| beta_def_477 | [M]^2 + [L]^2 <=> [M2H-2L2] + [H]^2 |  |
| beta_def_535 | [M2H-2L2] + [H]^2 <=> [M2L2] |  |
| beta_def_630 | [M2H-2L2] + [M] <=> [M3H-2L2] |  |
| beta_def_732 | [M] + [H2L] <=> [MH2L] |  |
| beta_def_739 | [MHL] + [H] <=> [MH2L] |  |
| beta_def_744 | [MHL3] + [H] <=> [MH2L3] |  |
| beta_def_751 | [MH2L] + [H] <=> [MH3L] |  |
| beta_def_779 | [M] + [HL] <=> [MHL] |  |
| beta_def_788 | [ML] + [H] <=> [MHL] |  |
| beta_def_792 | [ML2] + [H] <=> [MHL2] |  |
| beta_def_800 | [MHL] + [L] <=> [MHL2] |  |
| beta_def_803 | [ML3] + [H] <=> [MHL3] |  |
| beta_def_812 | [M] + [L] <=> [ML] |  |
| beta_def_840 | [M] + [L]^2 <=> [ML2] |  |
| beta_def_860 | [M(H-1L)L] + [H] <=> [ML2] |  |
| beta_def_872 | [M] + [L]^3 <=> [ML3] |  |
| beta_def_894 | [M] + [L]^4 <=> [ML4] |  |
| beta_def_903 | [M] + [L]^5 <=> [ML5] |  |
| beta_def_907 | [M] + [L]^6 <=> [ML6] |  |
| beta_def_966 | [M(OH)L] + [H] <=> [ML] + [H2O] |  |
| beta_def_984 | [M(OH)L2] + [H] <=> [ML2] + [H2O] |  |

*(all species aqueous)*

**1. Ni^[2+] + Ammonia** (metal_112 + ligand_10103) — ligand_def_HxL: L | 60 ent, 6 sp, 60 vlms (vlm_173182…vlm_173241)
   - species: beta_def_812(11) beta_def_840(13) beta_def_872(10) beta_def_894(10) beta_def_903(8) beta_def_907(8)
   - eq:5 nets T:19~30°C I:-0.15~3.15M max 6n/15e
**2. Ni^[2+] + Aminoacetic acid (Glycine)** (metal_112 + ligand_5760) — ligand_def_HxL: HL | 49 ent, 3 sp, 49 vlms (vlm_93798…vlm_93846)
   - species: beta_def_812(17) beta_def_840(17) beta_def_872(15)
   - eq:9 nets T:5~45°C I:-0.15~3.15M max 3n/3e
**3. Ni^[2+] + Ethylenediamine** (metal_112 + ligand_7029) — ligand_def_HxL: L | 45 ent, 3 sp, 45 vlms (vlm_122365…vlm_122409)
   - species: beta_def_812(15) beta_def_840(15) beta_def_872(15)
   - eq:7 nets T:19~41°C I:-0.15~3.15M max 3n/3e
**4. Ni^[2+] + 1,3-Diazole (Imidazole)** (metal_112 + ligand_7795) — ligand_def_HxL: L | 41 ent, 5 sp, 41 vlms (vlm_133852…vlm_133892)
   - species: beta_def_812(11) beta_def_840(9) beta_def_872(10) beta_def_894(8) beta_def_966(3)
   - eq:9 nets T:19~41°C I:-0.15~4.15M max 5n/7e
**5. Ni^[2+] + DL-2,6-Diamino-5-hydroxyhexanoic acid** (metal_112 + ligand_5889) — ligand_def_HxL: HL | 32 ent, 9 sp, 32 vlms (vlm_98521…vlm_98552)
   - species: beta_def_194(4) beta_def_204(4) beta_def_477(4) beta_def_535(2) beta_def_630(2) beta_def_739(4) beta_def_779(4) beta_def_788(4) beta_def_792(4)
   - eq:2 nets T:20~41°C I:-0.05~0.3M max 9n/25e
**6. Ni^[2+] + Iminodiacetic acid (IDA)** (metal_112 + ligand_6127) — ligand_def_HxL: H2L | 28 ent, 2 sp, 28 vlms (vlm_104338…vlm_104365)
   - species: beta_def_812(14) beta_def_840(14)
   - eq:6 nets T:19~41°C I:-0.15~2.15M max 2n/1e
**7. Ni^[2+] + Glycylglycine (Diglycine)** (metal_112 + ligand_6372) — ligand_def_HxL: HL | 26 ent, 5 sp, 26 vlms (vlm_113511…vlm_113536)
   - species: beta_def_137(4) beta_def_812(7) beta_def_840(6) beta_def_860(5) beta_def_872(4)
   - eq:5 nets T:19~41°C I:-0.15~1.15M max 5n/5e
**8. Ni^[2+] + L-2-Amino-3-phenylpropanoic acid (Phenylalanine)** (metal_112 + ligand_5777) — ligand_def_HxL: HL | 26 ent, 2 sp, 26 vlms (vlm_95027…vlm_95052)
   - species: beta_def_812(13) beta_def_840(13)
   - eq:5 nets T:5~45°C I:-0.15~3.15M max 2n/1e
**9. Ni^[2+] + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid)** (metal_112 + ligand_9058) — ligand_def_HxL: H3L | 25 ent, 6 sp, 25 vlms (vlm_157638…vlm_157662)
   - species: beta_def_374(4) beta_def_732(2) beta_def_779(5) beta_def_800(4) beta_def_812(6) beta_def_840(4)
   - eq:4 nets T:19~30°C I:-0.05~1.15M max 6n/14e
**10. Ni^[2+] + Trimethylenediamine (1,3-Propylenediamine)** (metal_112 + ligand_7037) — ligand_def_HxL: L | 25 ent, 3 sp, 25 vlms (vlm_122912…vlm_122936)
   - species: beta_def_812(9) beta_def_840(9) beta_def_872(7)
   - eq:5 nets T:19~30°C I:-0.15~2.15M max 3n/3e
**11. Ni^[2+] + L-2-Amino-3-(4-imidazolyl)propanoic acid (Histidine)** (metal_112 + ligand_5898) — ligand_def_HxL: HL | 25 ent, 5 sp, 25 vlms (vlm_98810…vlm_98834)
   - species: beta_def_788(1) beta_def_792(2) beta_def_812(9) beta_def_840(12) beta_def_984(1)
   - eq:6 nets T:19~41°C I:-0.05~3.15M max 4n/4e
**12. Ni^[2+] + L-2-Amino-3-(4-hydroxyphenyl)propanoic acid (Tyrosine)** (metal_112 + ligand_5819) — ligand_def_HxL: H2L | 25 ent, 9 sp, 25 vlms (vlm_96273…vlm_96297)
   - species: beta_def_194(3) beta_def_204(3) beta_def_208(3) beta_def_214(3) beta_def_744(3) beta_def_779(3) beta_def_788(1) beta_def_792(3) beta_def_803(3)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 9n/21e
**13. Ni^[2+] + DL-2-Amino-3-(3-hydroxyphenyl)propanoic acid (m-Tyrosine)** (metal_112 + ligand_5818) — ligand_def_HxL: H2L | 24 ent, 8 sp, 24 vlms (vlm_96176…vlm_96199)
   - species: beta_def_194(3) beta_def_204(3) beta_def_208(3) beta_def_214(3) beta_def_744(3) beta_def_779(3) beta_def_792(3) beta_def_803(3)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 8n/15e
**14. Ni^[2+] + L-2-Aminopropanoic acid (Alanine)** (metal_112 + ligand_5761) — ligand_def_HxL: HL | 24 ent, 3 sp, 24 vlms (vlm_94125…vlm_94272)
   - species: beta_def_812(9) beta_def_840(9) beta_def_872(6)
   - eq:5 nets T:19~41°C I:-0.15~1.15M max 3n/3e
**15. Ni^[2+] + Ethanoic acid (Acetic acid)** (metal_112 + ligand_8465) — ligand_def_HxL: HL | 22 ent, 2 sp, 22 vlms (vlm_144719…vlm_144740)
   - species: beta_def_812(12) beta_def_840(10)
   - eq:6 nets T:19~30°C I:-0.15~2.15M max 2n/1e
**16. Ni^[2+] + L-2,6-Diaminohexanoic acid (Lysine)** (metal_112 + ligand_5887) — ligand_def_HxL: HL | 22 ent, 9 sp, 22 vlms (vlm_98405…vlm_98426)
   - species: beta_def_194(4) beta_def_204(4) beta_def_208(3) beta_def_214(1) beta_def_744(1) beta_def_779(4) beta_def_788(2) beta_def_792(2) beta_def_803(1)
   - eq:2 nets T:20~41°C I:-0.05~0.3M max 9n/21e
**17. Ni^[2+] + 4-(2-Aminoethyl)imidazole (Histamine)** (metal_112 + ligand_7849) — ligand_def_HxL: L | 21 ent, 5 sp, 21 vlms (vlm_134640…vlm_134660)
   - species: beta_def_788(2) beta_def_812(6) beta_def_840(6) beta_def_872(6) beta_def_966(1)
   - eq:4 nets T:19~41°C I:-0.15~1.15M max 5n/6e
**18. Ni^[2+] + DL-Methylethylenediamine (1,2-Propylenediamine) (pn)** (metal_112 + ligand_7030) — ligand_def_HxL: L | 21 ent, 3 sp, 21 vlms (vlm_122630…vlm_122650)
   - species: beta_def_812(7) beta_def_840(7) beta_def_872(7)
   - eq:5 nets T:19~30°C I:-0.15~2.15M max 3n/3e
**19. Ni^[2+] + 2-Aminoethanol (Ethanolamine)** (metal_112 + ligand_6887) — ligand_def_HxL: L | 21 ent, 3 sp, 21 vlms (vlm_120801…vlm_120821)
   - species: beta_def_812(7) beta_def_840(7) beta_def_872(7)
   - eq:5 nets T:19~30°C I:-0.15~2.15M max 3n/3e
**20. Ni^[2+] + Nitrilotris(methylenephosphonic acid) (NTP)** (metal_112 + ligand_8412) — ligand_def_HxL: H6L | 20 ent, 4 sp, 20 vlms (vlm_143397…vlm_143416)
   - species: beta_def_739(2) beta_def_751(2) beta_def_788(7) beta_def_812(9)
   - eq:2 nets T:19~30°C I:-0.15~0.25M max 4n/4e

---
