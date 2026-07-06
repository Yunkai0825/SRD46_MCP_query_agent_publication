# Q4.2 — Tool Results (batch 2)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Mercury",
  "limit": 10
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

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "sulfide",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 10 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5891 | D-3,3'-Dithiobis(2-amin… (Penicillamine disulfide) | H2L | Amino Acids | 23 | `CC(C)(SSC(C)(C)C(N)C(=O)O)C(N)C(=O)O` | (-inf, H4L, -1.3, H3L, 2.04, H2L, 7.77, HL, 8.74, L, +inf) |
| ligand_6656 | L-3,3'-Dithiobis(a… (L-Cysteinylglycine disulfide) | H2L | polypeptides | 20 | `N[C@@H](CSSC[C@H](N)C(=O)NCC(=O)O)C(=O)NCC(=O)O` | (-inf, H4L, 2.65, H3L, 3.39, H2L, 6.3, HL, 7.28, L, +inf) |
| ligand_6657 | L-5-Glutamyl… (Penicillamine-glutatione disulfide) | H3L | polypeptides | 2 | `CC(C)(SSCC(NC(=O)CCC(N)C(=O)O)C(=O)NCC(=O)O)C(N)C(=O)O` | (-inf, H2L, 7.99, HL, 9.1, L, +inf) |
| ligand_6682 | N,N-[N'',N''''-Di(L-5-glu… (Glutathione disulfide) | *** | polypeptides | 53 | *** | (-inf, H6L, -1.5, H5L, 2.35, H4L, 3.16, H3L, 3.83, H2L, 8.85, HL, 9.81, L, +inf) |
| ligand_9696 | Dimethylsulfide | *** | miscellaneous sulfides | 1 | *** | *** |

### Functional groups across all SQL matches (6 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 3 | 50% |
| primary_amine | 3 | 50% |
| amide | 2 | 33% |
| thiol | 2 | 33% |

---

### Step 4: `search_ligands`
**Args:**
```json
{
  "name": "thiosulfate",
  "limit": 5
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_10149 | Hydrogen thiosulfate (Thiosulfuric acid) | H2L | Inorganic ligands | 117 | `O=S(O)(O)=S` | (-inf, H2L, -0.6, HL, -0.6, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| hydroxyl | 1 | 100% |

---

### Step 5: `search_ligands`
**Args:**
```json
{
  "name": "cysteine",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 26 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5856 | L-2-Amino-3-mercaptopropanoic acid (Cysteine) | H2L | Amino Acids | 134 | `N[C@@H](CS)C(=O)O` | (-inf, H3L, -1.9, H2L, 8.18, HL, 10.3, L, +inf) |
| ligand_5859 | DL-2-Amino-4-mercaptobutanoic acid (Homocysteine) | H2L | Amino Acids | 3 | `NC(CCS)C(=O)O` | (-inf, H3L, 2.15, H2L, 8.57, HL, 10.38, L, +inf) |
| ligand_5861 | L-2-Amino-3-(methylthio)propan… (S-Methylcysteine) | HL | Amino Acids | 39 | `CSC[C@H](N)C(=O)O` | (-inf, H2L, 2, HL, 8.74, L, +inf) |
| ligand_5862 | L-2-Amino-3-(ethylthio)propanoi… (S-Ethylcysteine) | HL | Amino Acids | 46 | `CCSC[C@H](N)C(=O)O` | (-inf, H2L, -1.9, HL, 8.65, L, +inf) |
| ligand_5871 | L-2-Amino-3-(2-Cyanoethylthio)propanoic acid (L-5… | HL | Amino Acids | 1 | `N#CCCSCC(N)C(=O)O` | (-inf, HL, 8.46, L, +inf) |

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
  "name": "thiourea",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 22 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_7007 | 1-(2-Aminoethyl)-1,3-diazolidine-2-thione (N-(2-A… | L | Aliphatic amines | 3 | `NCCN1CCNC1=S` | *** |
| ligand_10004 | Thiocarbamide (Thiourea) | L | miscellaneous ureas, had… | 175 | `NC(N)=S` | (-inf, HL, -1.18, L, +inf) |
| ligand_10005 | N-Methylthiourea | L | miscellaneous ureas, had… | 33 | `CNC(N)=S` | *** |
| ligand_10006 | N-Ethylthiourea | L | miscellaneous ureas, had… | 21 | `CCNC(N)=S` | *** |
| ligand_10007 | N-Butylthiourea | L | miscellaneous ureas, had… | 2 | `CCCCNC(N)=S` | *** |

### Functional groups across all SQL matches (16 parseable SMILES)

| group | count | % |
|-------|-------|---|
| secondary_amine | 14 | 88% |
| primary_amine | 8 | 50% |
| tertiary_amine | 3 | 19% |
| aromatic_ring | 2 | 12% |
| amide | 1 | 6% |

---

### Step 7: `search_ligands`
**Args:**
```json
{
  "name": "ammonia",
  "limit": 5
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_10103 | Ammonia | L | Inorganic ligands | 447 | `N` | (-inf, HL, 9.26, L, +inf) |

---

### Step 8: `search_ligands`
**Args:**
```json
{
  "name": "ethylenediamine",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 105 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5948 | N-(2-Aminoethyl)glycine (Ethylenediamine m… (EDMA) | HL | Amino Acids | 30 | `NCCNCC(=O)O` | (-inf, H3L, -1.9, H2L, 6.67, HL, 9.84, L, +inf) |
| ligand_6253 | N-(2-Aminoeth… (Ethylenediamine-N,N-diacetic acid) | H2L | NTA and derivatives | 39 | `NCCN(CC(=O)O)CC(=O)O` | (-inf, H2L, 5.53, HL, 10.87, L, +inf) |
| ligand_7029 | Ethylenediamine | L | Aliphatic amines | 310 | `NCCN` | (-inf, H2L, 7.11, HL, 9.92, L, +inf) |
| ligand_7030 | DL-Methylethylenediamine (1,2-Propylenediami… (pn) | L | Aliphatic amines | 86 | `CC(N)CN` | (-inf, H2L, 6.85, HL, 9.81, L, +inf) |
| ligand_7031 | DL-Ethylethylenediamine (1,2-Butylenediamine) | L | Aliphatic amines | 19 | `CCC(N)CN` | (-inf, H2L, 6.65, HL, 9.66, L, +inf) |

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

### Step 9: `search_ligands`
**Args:**
```json
{
  "name": "acetate",
  "limit": 5
}
```

[summary]
## search_ligands — 3 result(s)

**stats:** 3 SQL matches · showing 3 · limit 5

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

### Step 10: `search_ligands`
**Args:**
```json
{
  "name": "oxalate",
  "limit": 5
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 11: `search_ligands`
**Args:**
```json
{
  "name": "glycine",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 170 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5760 | Aminoacetic acid (Glycine) | HL | Amino Acids | 428 | `NCC(=O)O` | (-inf, H2L, 2.33, HL, 9.57, L, +inf) |
| ligand_5776 | DL-Aminophenylacetic acid (Phenylglycine) | HL | Amino Acids | 12 | `NC(C(=O)O)c1ccccc1` | (-inf, H2L, -1.9, HL, 8.92, L, +inf) |
| ligand_5786 | DL-Amino-4-sulfophenylacet… (4-Sulfophenylglycine) | H2L | Amino Acids | 12 | `NC(C(=O)O)c1ccc(S(=O)(=O)O)cc1` | (-inf, H2L, -1.8, HL, 8.66, L, +inf) |
| ligand_5838 | DL-Amino-4-Methoxyphenyl… (4-Methoxyphenylglycine) | HL | Amino Acids | 12 | `COc1ccc(C(N)C(=O)O)cc1` | (-inf, H2L, 2, HL, 9.07, L, +inf) |
| ligand_5925 | N-Methylglycine (Sarcosine) | HL | Amino Acids | 39 | `CNCC(=O)O` | (-inf, H2L, 2.18, HL, 9.98, L, +inf) |

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

### Step 12: `search_ligands`
**Args:**
```json
{
  "name": "thiocyanate",
  "limit": 5
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_10092 | Hydrogen thiocyanate (Thiocyanic acid) | HL | Inorganic ligands | 434 | `N=C=S` | (-inf, HL, -1.1, L, +inf) |

---

### Step 13: `search_ligands`
**Args:**
```json
{
  "name": "oxalic acid",
  "limit": 5
}
```

[summary]
## search_ligands — 4 result(s)

**stats:** 4 SQL matches · showing 4 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8872 | Ethanedioic acid (Oxalic acid) | H2L | Carboxylic acids diacids | 394 | `O=C(O)C(=O)O` | (-inf, H2L, -1.2, HL, 3.8, L, +inf) |
| ligand_8960 | Oxopropanedioic acid (Ketomaloni… (Mesoxalic acid) | H2L | Carboxylic acids diacids… | 3 | `O=C(O)C(=O)C(=O)O` | (-inf, H2L, -1.82, HL, 3.52, L, +inf) |
| ligand_9763 | Dithiooxalic acid | H2L | miscellaneous mercaptans | 3 | `O=C(S)C(=O)S` | *** |
| ligand_11304 | Ethanedi(dithioic acid) (Tetrathiooxalic acid) | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (3 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 2 | 67% |
| ketone | 1 | 33% |
| thiol | 1 | 33% |

---

### Step 14: `search_ligands`
**Args:**
```json
{
  "name": "acetic acid",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 683 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5760 | Aminoacetic acid (Glycine) | HL | Amino Acids | 428 | `NCC(=O)O` | (-inf, H2L, 2.33, HL, 9.57, L, +inf) |
| ligand_5776 | DL-Aminophenylacetic acid (Phenylglycine) | HL | Amino Acids | 12 | `NC(C(=O)O)c1ccccc1` | (-inf, H2L, -1.9, HL, 8.92, L, +inf) |
| ligand_5786 | DL-Amino-4-sulfophenylacet… (4-Sulfophenylglycine) | H2L | Amino Acids | 12 | `NC(C(=O)O)c1ccc(S(=O)(=O)O)cc1` | (-inf, H2L, -1.8, HL, 8.66, L, +inf) |
| ligand_5825 | DL-2-Amino-2-(3,4-dihydroxyphenyl)acetic a… (DOPG) | H3L | Amino Acids | 6 | `NC(C(=O)O)c1ccc(O)c(O)c1` | (-inf, H4L, 2, H3L, 8.56, H2L, 9.75, HL, 9.75, L, +inf) |
| ligand_5838 | DL-Amino-4-Methoxyphenyl… (4-Methoxyphenylglycine) | HL | Amino Acids | 12 | `COc1ccc(C(N)C(=O)O)cc1` | (-inf, H2L, 2, HL, 9.07, L, +inf) |

### Functional groups across all SQL matches (567 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 557 | 98% |
| tertiary_amine | 324 | 57% |
| aromatic_ring | 227 | 40% |
| hydroxyl | 88 | 16% |
| thioether | 76 | 13% |
| ether | 54 | 10% |
| halide | 49 | 9% |
| amide | 43 | 8% |
| secondary_amine | 36 | 6% |
| phenol | 27 | 5% |
| pyridine | 19 | 3% |
| primary_amine | 15 | 3% |
| sulfonate | 14 | 2% |
| thiol | 11 | 2% |
| ester | 6 | 1% |
| nitrile | 6 | 1% |
| ketone | 5 | 1% |
| phosphonate | 5 | 1% |
| phosphate | 2 | 0% |
| aldehyde | 1 | 0% |
| imine | 1 | 0% |

---

### Step 15: `search_ligands`
**Args:**
```json
{
  "name": "pyridine",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 304 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5963 | L-4,5,6,7-Tetrahydro-1H-imidazo[4,5-c… (Spinacine) | HL | Amino Acids | 14 | `O=C(O)C1Cc2[nH]cnc2CN1` | (-inf, H3L, -1.5, H2L, 4.9, HL, 8.59, L, +inf) |
| ligand_6762 | Pyridine-2-carboxylic acid (Picolinic acid) | HL | Pyridine carboxylic acids | 316 | `O=C(O)c1ccccn1` | (-inf, H2L, -0.95, HL, 5.21, L, +inf) |
| ligand_6763 | 6-Methylpyridine-2-carboxylic acid | HL | Pyridine carboxylic acids | 27 | `Cc1cccc(C(=O)O)n1` | (-inf, H2L, -1.2, HL, 5.86, L, +inf) |
| ligand_6765 | Pyridine-2-carboxylic acid N-oxide | HL | Pyridine carboxylic acids | 20 | `O=C(O)c1cccc[n+]1[O-]` | (-inf, HL, 3.31, L, +inf) |
| ligand_6766 | Pyridine-3-carboxylic acid (Nicotinic acid) | HL | Pyridine carboxylic acids | 28 | `O=C(O)c1cccnc1` | (-inf, H2L, 2.08, HL, 4.69, L, +inf) |

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

### Step 17: `build_system_catalog`
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

### Step 19: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.beta_definition_id = beta_def_812 AND c.ligand_id IN (ligand_10004, ligand_10092, ligand_5856, ligand_10149, ligand_10103, ligand_7029, ligand_7890, ligand_7795, ligand_8872, ligand_10076, ligand_10163, ligand_10168, ligand_10171))",
  "order_by": "s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability — 51 row(s)

### ΔS — 9 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_71 | Hg^[2+] | ligand_10076 | Hydroxide ion | *** | *** | 2 | 1 | 25 | 1~3 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_10163 | Chloride ion | *** | *** | 2 | 1 | 25 | 0.5~3 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_10168 | Bromide ion | *** | *** | 2 | 1 | 25 | 0.5~3 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 2 | 1 | 25 | 0~1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_7029 | Ethylenediamine | L | NCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_10171 | Iodide ion | *** | *** | 1 | 1 | 25 | 0.5 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_10004 | Thiocarbamide (Thiourea) | L | NC(N)=S | 1 | 1 | 25 | 0.5 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_7795 | 1,3-Diazole (Imidazole) | L | c1c[nH]cn1 | 1 | 1 | 25 | 3 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_7890 | Pyridine (Azine) | L | c1ccncc1 | 1 | 1 | 25 | 0.5 | *** | 0 |

### logK — 12 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_71 | Hg^[2+] | ligand_10076 | Hydroxide ion | *** | *** | 4 | 1 | 25 | 0~3 | *** | 4 |
| metal_71 | Hg^[2+] | ligand_10163 | Chloride ion | *** | *** | 4 | 1 | 25 | 0~3 | *** | 4 |
| metal_71 | Hg^[2+] | ligand_7029 | Ethylenediamine | L | NCCN | 3 | 1 | 25 | 0.1~3 | *** | 3 |
| metal_71 | Hg^[2+] | ligand_10168 | Bromide ion | *** | *** | 2 | 1 | 25 | 0.5~3 | *** | 2 |
| metal_71 | Hg^[2+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 2 | 1 | 25 | 0~1 | *** | 2 |
| metal_71 | Hg^[2+] | ligand_5856 | L-2-Amino-3-mercaptopropano… | H2L | N[C@@H](CS)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_10171 | Iodide ion | *** | *** | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_10004 | Thiocarbamide (Thiourea) | L | NC(N)=S | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_7795 | 1,3-Diazole (Imidazole) | L | c1c[nH]cn1 | 1 | 1 | 25 | 3 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 22 | 2 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_7890 | Pyridine (Azine) | L | c1ccncc1 | 1 | 1 | 25 | 0.5 | *** | 1 |

### ΔH — 9 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_71 | Hg^[2+] | ligand_10168 | Bromide ion | *** | *** | 4 | 1 | 25 | 0.5~3 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_10076 | Hydroxide ion | *** | *** | 2 | 1 | 25 | 1~3 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_10163 | Chloride ion | *** | *** | 2 | 1 | 25 | 0.5~3 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 2 | 1 | 25 | 0~1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_10171 | Iodide ion | *** | *** | 2 | 1 | 25 | 0~0.5 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_7029 | Ethylenediamine | L | NCCN | 1 | 1 | 25 | 0 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_10004 | Thiocarbamide (Thiourea) | L | NC(N)=S | 1 | 1 | 25 | 0.5 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_7795 | 1,3-Diazole (Imidazole) | L | c1c[nH]cn1 | 1 | 1 | 25 | 0.5 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_7890 | Pyridine (Azine) | L | c1ccncc1 | 1 | 1 | 25 | 0.5 | *** | 0 |

---
