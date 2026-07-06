# Q4.2 — Tool Results (batch 3)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "mercury",
  "symbol": "Hg"
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

### Step 4: `search_ligands`
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

### Step 5: `search_ligands`
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

### Step 6: `search_ligands`
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

### Step 7: `search_ligands`
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

### Step 8: `search_ligands`
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

### Step 9: `search_ligands`
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

### Step 10: `search_ligands`
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

### Step 11: `search_ligands`
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

### Step 12: `search_ligands`
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

### Step 13: `search_ligands`
**Args:**
```json
{
  "name": "citric acid",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 8 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_9057 | DL-1-Hydroxypropane-1,2,3-tricar… (Isocitric acid) | H3L | Carboxylic acids polyaci… | 24 | `O=C(O)CC(C(=O)O)C(O)C(=O)O` | (-inf, H3L, 3.05, H2L, 4.3, HL, 5.73, L, +inf) |
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxyli… (Citric acid) | H3L | Carboxylic acids polyaci… | 384 | `O=C(O)CC(O)(CC(=O)O)C(=O)O` | (-inf, H3L, 2.9, H2L, 4.35, HL, 5.65, L, +inf) |
| ligand_10950 | DL-Methylcitric acid | *** | Ligands not selected | 0 | *** | *** |
| ligand_10951 | DL-Homocitric acid | *** | Ligands not selected | 0 | *** | *** |
| ligand_10952 | DL-threo-2-Methylisocitric acid | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (2 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 2 | 100% |
| hydroxyl | 2 | 100% |

---

### Step 14: `search_ligands`
**Args:**
```json
{
  "name": "imidazole",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 50 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_7795 | 1,3-Diazole (Imidazole) | L | Pyrroles (azoles) | 237 | `c1c[nH]cn1` | (-inf, HL, 7, L, 7, H-1L, +inf) |
| ligand_7796 | 1-Methylimidazole | L | Pyrroles (azoles) | 52 | `Cn1ccnc1` | (-inf, HL, 7.1, L, +inf) |
| ligand_7797 | 1-Ethylimidazole | L | Pyrroles (azoles) | 17 | `CCn1ccnc1` | (-inf, HL, 7.21, L, +inf) |
| ligand_7798 | 1-Propylimidazole | L | Pyrroles (azoles) | 17 | `CCCn1ccnc1` | (-inf, HL, 7.22, L, +inf) |
| ligand_7799 | 1-Butylimidazole | L | Pyrroles (azoles) | 16 | `CCCCn1ccnc1` | (-inf, HL, 7.22, L, +inf) |

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

### Step 15: `search_ligands`
**Args:**
```json
{
  "name": "hydrogen sulfide",
  "limit": 5
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_10144 | Hydrogen sulfide (Hydrosulfuric acid) | H2L | Inorganic ligands | 93 | `S` | (-inf, H2L, 6.82, HL, +inf) |

---

### Step 16: `search_ligands`
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

### Step 17: `search_ligands`
**Args:**
```json
{
  "name": "thioglycol",
  "limit": 5
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8766 | Mercaptoacetic acid (Thioglycolic acid) | H2L | Carboxylic acids thio | 148 | `O=C(O)CS` | (-inf, H2L, 3.48, HL, 10.11, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 1 | 100% |
| thiol | 1 | 100% |

---

### Step 18: `search_ligands`
**Args:**
```json
{
  "name": "mercaptoacetic",
  "limit": 5
}
```

[summary]
## search_ligands — 4 result(s)

**stats:** 4 SQL matches · showing 4 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5875 | 5-Amino-3-thi… (S-2-Aminoethylmercaptoacetic acid) | HL | Amino Acids | 32 | `NCCSCC(=O)O` | (-inf, H2L, 3.18, HL, 9.53, L, +inf) |
| ligand_5876 | 6-Amino-3-th… (S-3-Aminopropylmercaptoacetic acid) | HL | Amino Acids | 21 | `NCCCSCC(=O)O` | (-inf, H2L, 3.35, HL, 10.19, L, +inf) |
| ligand_8766 | Mercaptoacetic acid (Thioglycolic acid) | H2L | Carboxylic acids thio | 148 | `O=C(O)CS` | (-inf, H2L, 3.48, HL, 10.11, L, +inf) |
| ligand_9750 | Mercaptoacetic acid methyl ester | HL | miscellaneous mercaptans | 2 | `COC(=O)CS` | (-inf, HL, 7.99, L, +inf) |

### Functional groups across all SQL matches (4 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 3 | 75% |
| primary_amine | 2 | 50% |
| thioether | 2 | 50% |
| thiol | 2 | 50% |
| ester | 1 | 25% |

---

### Step 20: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_71 AND c.ligand_id = ligand_10004",
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
  "where": "c.metal_id = metal_71 AND c.ligand_id = ligand_10144",
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
  "where": "c.metal_id = metal_71 AND c.ligand_id = ligand_5856",
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
  "where": "c.metal_id = metal_71 AND c.ligand_id = ligand_10103",
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
  "where": "c.metal_id = metal_71 AND c.ligand_id = ligand_7029",
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
  "where": "c.metal_id = metal_71 AND c.ligand_id = ligand_7795",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 26: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_71 AND c.ligand_id = ligand_8872",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 27: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_71 AND c.ligand_id = ligand_9058",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 28: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_71 AND c.ligand_id = ligand_8766",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 29: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_71 AND c.ligand_id = ligand_10149",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 30: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_71 AND c.ligand_id = ligand_5760",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---
