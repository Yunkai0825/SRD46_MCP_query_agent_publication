# Q3.1.5 — Tool Results (batch 4)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Calcium",
  "symbol": "Ca",
  "limit": 5
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_25 | Ca^[2+] | Ca | 2 | ✓ | [Ca+2] | InChI=1S/Ca/q+2 | beta_totN_68 | ligand_totN_644 | vlm_totN_1761 |

---

### Step 3: `search_metals`
**Args:**
```json
{
  "name": "Copper",
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

### Step 4: `search_ligands`
**Args:**
```json
{
  "name": "18-crown-6",
  "limit": 10
}
```

[summary]
## search_ligands — 8 result(s)

**stats:** 8 SQL matches · showing 8 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclooctadecane (18-Crown-6) | *** | miscellaneous crown ether | 76 | *** | *** |
| ligand_9677 | cis-syn-cis-2,5,8,15,… (A-Dicyclohexyl-18-Crown-6) | *** | miscellaneous crown ether | 42 | *** | *** |
| ligand_9678 | cis-anti-cis-2,5,8,15… (B-Dicyclohexyl-18-Crown-6) | *** | miscellaneous crown ether | 39 | *** | *** |
| ligand_9679 | Benzo-1,4,7,10,13,16-hexaoxacy… (Benzo-18-crown-6) | *** | miscellaneous crown ether | 2 | *** | *** |
| ligand_9680 | 2,3,11,12-Dibenzo-1,4,7,10,1… (Dibenzo-18-crown-6) | *** | miscellaneous crown ether | 13 | *** | *** |
| ligand_9681 | 3'-Hydroxymethy… (3-Hydroxymethylbenzo-18-crown-6) | *** | miscellaneous crown ether | 3 | *** | *** |
| ligand_11253 | Cyclohexyl-18-crown-6 | *** | Ligands not selected | 0 | *** | *** |
| ligand_11254 | Bis(t-butylcyclohexyl)-18-crown-6 | *** | Ligands not selected | 0 | *** | *** |

---

### Step 5: `search_ligands`
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

### Step 6: `search_ligands`
**Args:**
```json
{
  "name": "tartrate",
  "limit": 10
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
  "name": "gluconate",
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
  "name": "lactate",
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
  "name": "phosphate",
  "limit": 10
}
```

[summary]
## search_ligands — 10 result(s)

**stats:** 128 SQL matches · showing 10 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6391 | Glycyl-DL-… (Glycyl-DL-serine dihydrogenphosphate) | H3L | Peptides | 7 | `NCC(=O)N[C@@H](COP(=O)(O)O)C(=O)O` | (-inf, H3L, 2.91, H2L, 6.03, HL, 8.42, L, +inf) |
| ligand_6412 | DL-Phosphos… (DL-Serylglycine dihydrogenphosphate) | H3L | Peptides | 16 | `NC(COP(=O)(O)O)C(=O)NCC(=O)O` | (-inf, H3L, 3.16, H2L, 5.42, HL, 8.01, L, +inf) |
| ligand_6469 | L-Phosph… (L-Seryl-L-leucine dihydrogen phosphate) | H3L | Peptides | 3 | `CC(C)CC(NC(=O)C(N)COP(=O)(O)O)C(=O)O` | (-inf, H3L, 3.11, H2L, 5.47, HL, 8.26, L, +inf) |
| ligand_6470 | L… (L-O-Phenylseryl-L-leucine dihydrogenphosphate) | H2L | Peptides | 2 | `CC(C)CC(NC(=O)C(N)COP(=O)(O)Oc1ccccc1)C(=O)O` | (-inf, H2L, 3.16, HL, 7.12, L, +inf) |
| ligand_6504 | L-P… (L-Seryl-L-glutamic acid dihydrogenphosphate) | H4L | Peptides | 25 | `NC(COP(=O)(O)O)C(=O)NC(CCC(=O)O)C(=O)O` | (-inf, H4L, 3.04, H3L, 4.4, H2L, 5.69, HL, 8.22, L, +inf) |
| ligand_6506 | L-Phosphos… (L-Seryl-L-lysine dihydrogenphosphate) | H3L | Peptides | 10 | `NCCCCC(NC(=O)C(N)COP(=O)(O)O)C(=O)O` | (-inf, H4L, 2.99, H3L, 5.34, H2L, 5.59, HL, 11.05, L, +inf) |
| ligand_6572 | Glyc… (Glycyl-DL-serylglycine dihydrogenphosphate) | H3L | tripeptides | 9 | `NCC(=O)NC(COP(=O)(O)O)C(=O)NCC(=O)O` | (-inf, H3L, 3.29, H2L, 5.77, HL, 8.22, L, +inf) |
| ligand_7977 | Pyridoxal-5'-(dihydrogenphosphate) | H3L | Pyridines (azines) | 51 | `Cc1ncc(COP(=O)(O)O)c(C=O)c1O` | (-inf, H4L, -1.4, H3L, 3.51, H2L, 6.04, HL, 8.25, L, +inf) |
| ligand_7980 | Pyridoxamine-5'-(dihydrogenphosphate) | H3L | Pyridines (azines) | 16 | `Cc1ncc(COP(=O)(O)O)c(CN)c1O` | (-inf, H4L, 3.4, H3L, 5.64, H2L, 8.42, HL, 10.8, L, +inf) |
| ligand_7981 | 5-Aminomethyl-3-hydrox… (Isopyridoxaminephosphate) | H3L | Pyridines (azines) | 4 | `Cc1ncc(CN)c(COP(=O)(O)O)c1O` | (-inf, H4L, 3.64, H3L, 5.55, H2L, 8.44, HL, 10.69, L, +inf) |

### Functional groups across all SQL matches (103 parseable SMILES)

| group | count | % |
|-------|-------|---|
| hydroxyl | 101 | 98% |
| phosphate | 93 | 90% |
| aromatic_ring | 51 | 50% |
| ether | 38 | 37% |
| primary_amine | 34 | 33% |
| carboxyl | 14 | 14% |
| amide | 7 | 7% |
| pyridine | 7 | 7% |
| ester | 2 | 2% |
| secondary_amine | 2 | 2% |
| tertiary_amine | 2 | 2% |
| aldehyde | 1 | 1% |
| halide | 1 | 1% |
| phosphonate | 1 | 1% |
| thiol | 1 | 1% |

---

### Step 10: `search_ligands`
**Args:**
```json
{
  "name": "pyrophosphate",
  "limit": 10
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

### Step 12: `search_ligands`
**Args:**
```json
{
  "name": "sulfate",
  "limit": 10
}
```

[summary]
## search_ligands — 10 result(s)

**stats:** 11 SQL matches · showing 10 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6852 | 2-Aminoethyl(hydrogensulfate) | HL | Aliphatic amines | 5 | `NCCOS(=O)(=O)O` | (-inf, HL, 9.182, L, +inf) |
| ligand_9382 | 2,3,4-Trihydroxybenzenesulfon… (Pyrogallolsulfate) | H4L | Catechols | 4 | `O=S(=O)(O)c1ccc(O)c(O)c1O` | (-inf, H3L, 8.28, H2L, 11.3, HL, +inf) |
| ligand_10148 | Hydrogen sulfate ion (Sulfuric acid) | HL | Inorganic ligands | 581 | `O=S(=O)([O-])O` | (-inf, HL, 1.54, L, +inf) |
| ligand_10149 | Hydrogen thiosulfate (Thiosulfuric acid) | H2L | Inorganic ligands | 117 | `O=S(O)(O)=S` | (-inf, H2L, -0.6, HL, -0.6, L, +inf) |
| ligand_10150 | Selenosulfate ion | *** | Inorganic ligands | 1 | *** | *** |
| ligand_10151 | Hydrogen amidosulfate (Sulfamic acid) | HL | Inorganic ligands | 22 | `NS(=O)(=O)O` | (-inf, HL, 0.034, L, +inf) |
| ligand_10152 | Hydrogen hydroxyl… (Hydroxylamine-O-sulfonic acid) | HL | Inorganic ligands | 1 | `NOS(=O)(=O)O` | (-inf, HL, 1.48, L, +inf) |
| ligand_10153 | Hydrogen amidodisulfate (Aminodisulfonic acid) | H2L | Inorganic ligands | 1 | `O=S(=O)(O)NS(=O)(=O)O` | (-inf, HL, 8.5, L, +inf) |
| ligand_10154 | Hydrogen peroxosulfate | H2L | Inorganic ligands | 1 | `O=S(=O)(O)OO` | (-inf, HL, 9.86, L, +inf) |
| ligand_10155 | Hydrogen peroxydisulfate (Peroxydisulfuric acid) | H2L | Inorganic ligands | 27 | `O=S(=O)(O)OOS(=O)(=O)O` | *** |

### Functional groups across all SQL matches (9 parseable SMILES)

| group | count | % |
|-------|-------|---|
| hydroxyl | 9 | 100% |
| sulfonate | 8 | 89% |
| primary_amine | 3 | 33% |
| aromatic_ring | 1 | 11% |
| phenol | 1 | 11% |
| secondary_amine | 1 | 11% |

---

### Step 13: `search_ligands`
**Args:**
```json
{
  "name": "malonate",
  "limit": 10
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8873 | Propanedioic acid (Malonic acid) | H2L | Carboxylic acids diacids | 505 | `O=C(O)CC(=O)O` | (-inf, H2L, 2.65, HL, 5.27, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 1 | 100% |

---

### Step 14: `search_ligands`
**Args:**
```json
{
  "name": "succinate",
  "limit": 10
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 15: `search_ligands`
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

### Step 16: `search_ligands`
**Args:**
```json
{
  "name": "aspartate",
  "limit": 10
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5839 | L-2-Aminobutanedioic acid 4-… (4-Methyl aspartate) | HL | Amino Acids | 1 | `COC(=O)CC(N)C(=O)O` | (-inf, HL, 8.5, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 1 | 100% |
| ester | 1 | 100% |
| primary_amine | 1 | 100% |

---

### Step 17: `search_ligands`
**Args:**
```json
{
  "name": "glutamate",
  "limit": 10
}
```

[summary]
## search_ligands — 3 result(s)

**stats:** 3 SQL matches · showing 3 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5840 | DL-2-Aminopentanedioic acid 5… (5-Ethyl glutamate) | HL | Amino Acids | 2 | `CCOC(=O)CC[C@H](N)C(=O)O` | (-inf, H2L, 2.15, HL, 9.19, L, +inf) |
| ligand_5841 | L-2-Aminopentanedioic acid 5… (5-Benzyl glutamate) | HL | Amino Acids | 2 | `N[C@@H](CCC(=O)OCc1ccccc1)C(=O)O` | (-inf, H2L, 2.06, HL, 8.89, L, +inf) |
| ligand_5842 | DL-2-Aminopentanedioic acid 1… (1-Ethyl glutamate) | HL | Amino Acids | 2 | `CCOC(=O)[C@@H](N)CCC(=O)O` | (-inf, H2L, 3.85, HL, 7.84, L, +inf) |

### Functional groups across all SQL matches (3 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 3 | 100% |
| ester | 3 | 100% |
| primary_amine | 3 | 100% |
| aromatic_ring | 1 | 33% |

---

### Step 18: `search_ligands`
**Args:**
```json
{
  "name": "EDTA",
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

### Step 19: `search_ligands`
**Args:**
```json
{
  "name": "EGTA",
  "limit": 10
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6342 | Ethylenebis(oxyethylenenitrilo)tetraacetic… (EGTA) | H4L | EDTA and derivatives | 169 | `O=C(O)CN(CCOCCOCCN(CC(=O)O)CC(=O)O)CC(=O)O` | (-inf, H4L, -1.9, H3L, 2.7, H2L, 8.71, HL, 9.32, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 1 | 100% |
| ether | 1 | 100% |
| tertiary_amine | 1 | 100% |

---

### Step 20: `search_ligands`
**Args:**
```json
{
  "name": "NTA",
  "limit": 10
}
```

[summary]
## search_ligands — 10 result(s)

**stats:** 298 SQL matches · showing 10 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5763 | DL-2-Aminopentanoic acid (Norvaline) | HL | Amino Acids | 35 | `CCC[C@H](N)C(=O)O` | (-inf, H2L, 2.31, HL, 9.65, L, +inf) |
| ligand_5766 | L-2-Amino-4-methylpentanoic acid (Leucine) | HL | Amino Acids | 49 | `CC(C)C[C@H](N)C(=O)O` | (-inf, H2L, 2.32, HL, 9.58, L, +inf) |
| ligand_5767 | L-2-Amino-3-methylpentanoic acid (Isoleucine) | HL | Amino Acids | 51 | `CC[C@H](C)[C@H](N)C(=O)O` | (-inf, H2L, 2.26, HL, 9.6, L, +inf) |
| ligand_5768 | D-allo-2-Amino-3-methylpentan… (D-allo-Isoleucine) | HL | Amino Acids | 16 | `CC[C@H](C)[C@@H](N)C(=O)O` | (-inf, H2L, 2.2, HL, 9.62, L, +inf) |
| ligand_5773 | 1-Aminocyclopentanecarboxylic acid (Cycloleucine) | HL | Amino Acids | 11 | `NC1(C(=O)O)CCCC1` | (-inf, H2L, 2.4, HL, 10.31, L, +inf) |
| ligand_5790 | cis-2-Aminocyclopentane-1-carboxylic acid | HL | Amino Acids | 6 | `N[C@H]1CCC[C@H]1C(=O)O` | (-inf, H2L, 3.54, HL, 10.1, L, +inf) |
| ligand_5791 | trans-2-Aminocyclopentane-1-carboxylic acid | HL | Amino Acids | 3 | `N[C@@H]1CCC[C@H]1C(=O)O` | (-inf, H2L, 3.75, HL, 9.91, L, +inf) |
| ligand_5798 | 5-Aminopentanoic acid | HL | Amino Acids | 20 | `NCCCCC(=O)O` | (-inf, H2L, 4.27, HL, 10.766, L, +inf) |
| ligand_5804 | L-2-Aminopentanedioic acid (Glutamic acid) | H2L | Amino Acids | 94 | `N[C@@H](CCC(=O)O)C(=O)O` | (-inf, H3L, 2.16, H2L, 4.15, HL, 9.58, L, +inf) |
| ligand_5805 | DL-2-Amino-2-methylpentan… (2-Methylglutamic acid) | H2L | Amino Acids | 4 | `C[C@](N)(CCC(=O)O)C(=O)O` | (-inf, H2L, 4.05, HL, 9.72, L, +inf) |

### Functional groups across all SQL matches (223 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 88 | 39% |
| secondary_amine | 81 | 36% |
| tertiary_amine | 60 | 27% |
| amide | 46 | 21% |
| primary_amine | 45 | 20% |
| hydroxyl | 38 | 17% |
| ether | 37 | 17% |
| aromatic_ring | 31 | 14% |
| thioether | 13 | 6% |
| phosphonate | 10 | 4% |
| pyridine | 9 | 4% |
| imine | 7 | 3% |
| ketone | 7 | 3% |
| ester | 6 | 3% |
| halide | 6 | 3% |
| thiol | 5 | 2% |
| oxime | 3 | 1% |
| phenol | 2 | 1% |
| phosphate | 2 | 1% |
| sulfonate | 1 | 0% |

---

### Step 22: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_25"
}
```

[summary]
[CATALOG]
## build_system_catalog — 20 pair(s), 74 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_156 | [M] + [H2L]^2 <=> [M(H2L)2] |  |
| beta_def_283 | [MHL(s)] <=> [M] + [H] + [L] | solid |
| beta_def_296 | [MHL(H2O)2(s)] <=> [M] + [HL] + [H2O]^2 | solid |
| beta_def_298 | [MHL(s)] <=> [M] + [HL] | solid |
| beta_def_306 | [ML(H2O)2(s,gypsum)] <=> [M] + [L] + [H2O]^2 | solid |
| beta_def_307 | [ML(H2O)3(s)] <=> [M] + [L] + [H2O]^3 | solid |
| beta_def_310 | [ML(H2O)6(s)] <=> [M] + [L] + [H2O]^6 | solid |
| beta_def_313 | [ML(s,aragonite)] <=> [M] + [L] | solid |
| beta_def_316 | [ML(s,calcite)] <=> [M] + [L] | solid |
| beta_def_319 | [ML(s,monohydrocalcite)] <=> [M] + [L] | solid |
| beta_def_324 | [ML(s,vaterite)] <=> [M] + [L] | solid |
| beta_def_327 | [ML(H2O)(s)] <=> [M] + [L] + [H2O] | solid |
| beta_def_332 | [ML2(H2O)6(s)] <=> [M] + [L]^2 + [H2O]^6 | solid |
| beta_def_502 | [M]^2 + [L] <=> [M2L] |  |
| beta_def_516 | [ML] + [M] <=> [M2L] |  |
| beta_def_624 | [M3L2(s)] <=> [M]^3 + [L]^2 | solid |
| beta_def_625 | [M3L2(s,beta)] <=> [M]^3 + [L]^2 | solid |
| beta_def_665 | [M4HL3(H2O)2.5(s)] <=> [M]^4 + [H] + [L]^3 + [H2O]^2.5 | solid |
| beta_def_666 | [M4HL3(H2O)3(s)] <=> [M]^4 + [H] + [L]^3 + [H2O]^3 | solid |
| beta_def_689 | [M5(OH)L3(H2O)(s)] <=> [M]^5 + [OH] + [L]^3 + [H2O] | solid |
| beta_def_732 | [M] + [H2L] <=> [MH2L] |  |
| beta_def_739 | [MHL] + [H] <=> [MH2L] |  |
| beta_def_751 | [MH2L] + [H] <=> [MH3L] |  |
| beta_def_765 | [MH3L] + [H] <=> [MH4L] |  |
| beta_def_779 | [M] + [HL] <=> [MHL] |  |
| beta_def_788 | [ML] + [H] <=> [MHL] |  |
| beta_def_792 | [ML2] + [H] <=> [MHL2] |  |
| beta_def_812 | [M] + [L] <=> [ML] |  |
| beta_def_840 | [M] + [L]^2 <=> [ML2] |  |
| beta_def_966 | [M(OH)L] + [H] <=> [ML] + [H2O] |  |

*(all species aqueous unless noted)*

**1. Ca^[2+] + Hydrogen phosphate (Phosphoric acid)** (metal_25 + ligand_10113) — ligand_def_HxL: H3L | 40 ent, 9 sp, 40 vlms (vlm_174342…vlm_174381)
   - species: beta_def_156(1) beta_def_296(7) beta_def_298(4) beta_def_625(4) beta_def_665(1) beta_def_666(2) beta_def_689(2) beta_def_732(9) beta_def_779(10)
   - eq:10 nets T:13~41°C I:-0.15~3.15M max 8n/28e
**2. Ca^[2+] + Nitrilotris(methylenephosphonic acid) (NTP)** (metal_25 + ligand_8412) — ligand_def_HxL: H6L | 30 ent, 4 sp, 30 vlms (vlm_143294…vlm_143323)
   - species: beta_def_739(4) beta_def_751(2) beta_def_788(12) beta_def_812(12)
   - eq:3 nets T:19~30°C I:-0.15~1.15M max 4n/4e
**3. Ca^[2+] + 1-Hydroxyethane-1,1-diphosphonic acid (Etidronic acid)** (metal_25 + ligand_9142) — ligand_def_HxL: H4L | 22 ent, 3 sp, 22 vlms (vlm_159220…vlm_159241)
   - species: beta_def_502(6) beta_def_779(6) beta_def_812(10)
   - eq:4 nets T:19~30°C I:-0.15~0.65M max 3n/3e
**4. Ca^[2+] + Hydrogen carbonate (Carbonic acid)** (metal_25 + ligand_10096) — ligand_def_HxL: H2L | 21 ent, 7 sp, 21 vlms (vlm_172687…vlm_172707)
   - species: beta_def_310(3) beta_def_313(4) beta_def_316(4) beta_def_319(1) beta_def_324(3) beta_def_779(3) beta_def_812(3)
   - eq:4 nets T:5~45°C I:-0.15~0.85M max 7n/21e
**5. Ca^[2+] + Hydrogen sulfate ion (Sulfuric acid)** (metal_25 + ligand_10148) — ligand_def_HxL: HL | 19 ent, 2 sp, 19 vlms (vlm_175657…vlm_175675)
   - species: beta_def_306(10) beta_def_812(9)
   - eq:9 nets T:19~41°C I:-0.15~6.15M max 2n/1e
**6. Ca^[2+] + N-(Phosphonomethyl)glycine (Glyphosate)** (metal_25 + ligand_5937) — ligand_def_HxL: H3L | 19 ent, 7 sp, 19 vlms (vlm_99765…vlm_99783)
   - species: beta_def_298(1) beta_def_502(4) beta_def_739(4) beta_def_788(4) beta_def_792(1) beta_def_812(4) beta_def_840(1)
   - eq:2 nets T:19~30°C I:-0.05~0.65M max 7n/11e
**7. Ca^[2+] + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid)** (metal_25 + ligand_9058) — ligand_def_HxL: H3L | 18 ent, 5 sp, 18 vlms (vlm_157530…vlm_157547)
   - species: beta_def_283(1) beta_def_624(1) beta_def_732(1) beta_def_779(5) beta_def_812(10)
   - eq:8 nets T:19~41°C I:-0.15~0.3M max 5n/10e
**8. Ca^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_25 + ligand_6277) — ligand_def_HxL: H4L | 18 ent, 2 sp, 18 vlms (vlm_108344…vlm_108361)
   - species: beta_def_788(2) beta_def_812(16)
   - eq:6 nets T:19~41°C I:-0.05~1.15M max 2n/1e
**9. Ca^[2+] + Ethanedioic acid (Oxalic acid)** (metal_25 + ligand_8872) — ligand_def_HxL: H2L | 17 ent, 3 sp, 17 vlms (vlm_151595…vlm_151611)
   - species: beta_def_307(2) beta_def_327(9) beta_def_812(6)
   - eq:9 nets T:13~41°C I:-0.15~1.15M max 3n/3e
**10. Ca^[2+] + Hydrogen triphosphate (Triphosphoric acid)** (metal_25 + ligand_10117) — ligand_def_HxL: H5L | 15 ent, 3 sp, 15 vlms (vlm_174890…vlm_174904)
   - species: beta_def_779(6) beta_def_812(8) beta_def_966(1)
   - eq:5 nets T:19~30°C I:-0.15~1.15M max 3n/2e
**11. Ca^[2+] + Ethylenedinitrilotetrakis(methylenephosphonic acid) (EDTP)** (metal_25 + ligand_8428) — ligand_def_HxL: H8L | 15 ent, 5 sp, 15 vlms (vlm_143717…vlm_143731)
   - species: beta_def_739(3) beta_def_751(3) beta_def_765(3) beta_def_788(3) beta_def_812(3)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 5n/7e
**12. Ca^[2+] + Nitrilotriacetic acid (NTA)** (metal_25 + ligand_6165) — ligand_def_HxL: H3L | 15 ent, 2 sp, 15 vlms (vlm_105256…vlm_105270)
   - species: beta_def_812(9) beta_def_840(6)
   - eq:7 nets T:15~41°C I:-0.15~1.15M max 2n/1e
**13. Ca^[2+] + Hydrogen iodate (Iodic acid)** (metal_25 + ligand_10173) — ligand_def_HxL: HL | 14 ent, 2 sp, 14 vlms (vlm_178632…vlm_178645)
   - species: beta_def_332(9) beta_def_812(5)
   - eq:7 nets T:19~30°C I:-0.05~4.15M max 2n/1e
**14. Ca^[2+] + Propane-1,2,3-tricarboxylic acid (Tricarballylic acid)** (metal_25 + ligand_9048) — ligand_def_HxL: H3L | 13 ent, 4 sp, 13 vlms (vlm_157144…vlm_157156)
   - species: beta_def_502(2) beta_def_732(3) beta_def_779(3) beta_def_812(5)
   - eq:5 nets T:15~30°C I:-0.15~0.25M max 4n/6e
**15. Ca^[2+] + Adenosine-5'-(tetrahydrogentriphosphate) (ATP)** (metal_25 + ligand_8321) — ligand_def_HxL: H4L | 12 ent, 2 sp, 12 vlms (vlm_141536…vlm_141547)
   - species: beta_def_779(5) beta_def_812(7)
   - eq:5 nets T:19~41°C I:-0.05~0.65M max 2n/1e
**16. Ca^[2+] + Triethylenetetranitrilohexaacetic acid (TTHA)** (metal_25 + ligand_6366) — ligand_def_HxL: H6L | 12 ent, 4 sp, 12 vlms (vlm_113057…vlm_113068)
   - species: beta_def_516(3) beta_def_739(3) beta_def_788(3) beta_def_812(3)
   - eq:3 nets T:15~35°C I:-0.05~0.25M max 4n/4e
**17. Ca^[2+] + Tetramethylenedinitrilotetraacetic acid** (metal_25 + ligand_6313) — ligand_def_HxL: H4L | 12 ent, 3 sp, 12 vlms (vlm_110650…vlm_110661)
   - species: beta_def_516(1) beta_def_788(4) beta_def_812(7)
   - eq:3 nets T:15~30°C I:-0.05~0.65M max 3n/3e
**18. Ca^[2+] + Aminoacetic acid (Glycine)** (metal_25 + ligand_5760) — ligand_def_HxL: HL | 12 ent, 2 sp, 12 vlms (vlm_93666…vlm_93677)
   - species: beta_def_779(4) beta_def_812(8)
   - eq:6 nets T:15~41°C I:-0.15~3.15M max 2n/1e
**19. Ca^[2+] + D-2,3-Dihydroxybutanedioic acid (D-Tartaric acid)** (metal_25 + ligand_8955) — ligand_def_HxL: H2L | 11 ent, 2 sp, 11 vlms (vlm_154938…vlm_154948)
   - species: beta_def_779(5) beta_def_812(6)
   - eq:3 nets T:19~30°C I:-0.15~0.25M max 2n/1e
**20. Ca^[2+] + Diethylenetrinitrilopentaacetic acid (DTPA)** (metal_25 + ligand_6356) — ligand_def_HxL: H5L | 11 ent, 3 sp, 11 vlms (vlm_112538…vlm_112548)
   - species: beta_def_516(3) beta_def_788(3) beta_def_812(5)
   - eq:3 nets T:15~41°C I:-0.05~0.3M max 3n/3e

---

### Step 23: `build_system_catalog`
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

### Step 25: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_25 AND c.ligand_id IN (ligand_9676, ligand_10096, ligand_10148, ligand_8873, ligand_6342, ligand_6277, ligand_8465) AND c.beta_definition_id IN (beta_def_812, beta_def_840) AND (s.solvent_name LIKE '%water%') AND s.temperature_c BETWEEN 20 AND 30 AND s.ionic_strength_mol_l BETWEEN 0.05 AND 0.20)",
  "order_by": "s.temperature_c ASC, s.ionic_strength_mol_l ASC",
  "limit": 400
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
  "where": "(c.metal_id = metal_41 AND c.ligand_id IN (ligand_9676, ligand_10096, ligand_10148, ligand_8873, ligand_6342, ligand_6277, ligand_8465) AND c.beta_definition_id IN (beta_def_812, beta_def_840) AND (s.solvent_name LIKE '%water%') AND s.temperature_c BETWEEN 20 AND 30 AND s.ionic_strength_mol_l BETWEEN 0.05 AND 0.20)",
  "order_by": "s.temperature_c ASC, s.ionic_strength_mol_l ASC",
  "limit": 400
}
```

[summary]
## search_stability

*(no results)*

---
