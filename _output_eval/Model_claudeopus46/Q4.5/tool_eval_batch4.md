# Q4.5 — Tool Results (batch 4)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "calcium"
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_25 | Ca^[2+] | Ca | 2 | ✓ | [Ca+2] | InChI=1S/Ca/q+2 | beta_totN_68 | ligand_totN_644 | vlm_totN_1761 |

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "acetate, formate, lactate, glycolate, oxalate, malonate, succinate, citrate, tartrate, EDTA, NTA, iminodiacetate, glycine, aspartate, glutamate, salicylate, phosphate, carbonate",
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

### Step 5: `search_ligands`
**Args:**
```json
{
  "name": "formate",
  "limit": 5
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
  "name": "oxalate",
  "limit": 5
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
  "name": "malonate",
  "limit": 5
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8873 | Propanedioic acid (Malonic acid) | H2L | Carboxylic acids diacids | 505 | `O=C(O)CC(=O)O` | (-inf, H2L, 2.65, HL, 5.27, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 1 | 100% |

---

### Step 8: `search_ligands`
**Args:**
```json
{
  "name": "succinate",
  "limit": 5
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
  "name": "citrate",
  "limit": 5
}
```

[summary]
## search_ligands — 4 result(s)

**stats:** 4 SQL matches · showing 4 · limit 5

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
  "name": "EDTA",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 5 SQL matches · showing 5 · limit 5

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

### Step 12: `search_ligands`
**Args:**
```json
{
  "name": "NTA",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 298 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5763 | DL-2-Aminopentanoic acid (Norvaline) | HL | Amino Acids | 35 | `CCC[C@H](N)C(=O)O` | (-inf, H2L, 2.31, HL, 9.65, L, +inf) |
| ligand_5766 | L-2-Amino-4-methylpentanoic acid (Leucine) | HL | Amino Acids | 49 | `CC(C)C[C@H](N)C(=O)O` | (-inf, H2L, 2.32, HL, 9.58, L, +inf) |
| ligand_5767 | L-2-Amino-3-methylpentanoic acid (Isoleucine) | HL | Amino Acids | 51 | `CC[C@H](C)[C@H](N)C(=O)O` | (-inf, H2L, 2.26, HL, 9.6, L, +inf) |
| ligand_5768 | D-allo-2-Amino-3-methylpentan… (D-allo-Isoleucine) | HL | Amino Acids | 16 | `CC[C@H](C)[C@@H](N)C(=O)O` | (-inf, H2L, 2.2, HL, 9.62, L, +inf) |
| ligand_5773 | 1-Aminocyclopentanecarboxylic acid (Cycloleucine) | HL | Amino Acids | 11 | `NC1(C(=O)O)CCCC1` | (-inf, H2L, 2.4, HL, 10.31, L, +inf) |

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

### Step 13: `search_ligands`
**Args:**
```json
{
  "name": "tartrate",
  "limit": 5
}
```

[summary]
## search_ligands

*(no results)*

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
  "name": "formic acid",
  "limit": 5
}
```

[summary]
## search_ligands — 4 result(s)

**stats:** 4 SQL matches · showing 4 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8464 | Methanoic acid (Formic acid) | HL | Carboxylic acids | 128 | `O=CO` | (-inf, HL, 3.57, L, +inf) |
| ligand_8628 | Phosphinoformic acid | H2L | Carboxylic acids | 2 | `O=C(O)[PH](=O)O` | (-inf, H2L, -1.7, HL, 3.19, L, +inf) |
| ligand_8629 | Phosphonoformic acid | H3L | Carboxylic acids | 23 | `O=C(O)P(=O)(O)O` | (-inf, H3L, -1.7, H2L, 3.6, HL, 7.57, L, +inf) |
| ligand_11435 | Phenylazoformic acid 2-ph… (1,5-Diphenylcarbazone) | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (3 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 3 | 100% |
| hydroxyl | 2 | 67% |
| aldehyde | 1 | 33% |
| phosphonate | 1 | 33% |

---

### Step 16: `search_ligands`
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

### Step 17: `search_ligands`
**Args:**
```json
{
  "name": "succinic acid",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 13 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6138 | 2,2'-Bis(2-Carboxymethyl)iminodiacetic acid (Imin… | H4L | Iminodiacetic acid and d… | 26 | `O=C(O)CC(NC(CC(=O)O)C(=O)O)C(=O)O` | (-inf, H4L, -1.97, H3L, 3.24, H2L, 4.24, HL, 10, L, +inf) |
| ligand_8907 | Butanedioic acid (Succinic acid) | H2L | Carboxylic acids diacids | 253 | `O=C(O)CCC(=O)O` | (-inf, H2L, 3.99, HL, 5.24, L, +inf) |
| ligand_8908 | DL-Propane-1,2-dicarboxylic… (Methylsuccinic acid) | H2L | Carboxylic acids diacids | 38 | `CC(CC(=O)O)C(=O)O` | (-inf, H2L, 3.88, HL, 5.35, L, +inf) |
| ligand_8909 | 2-Methylpropane-1,2-d… (2,2-Dimethylsuccinic acid) | H2L | Carboxylic acids diacids | 11 | `CC(C)(CC(=O)O)C(=O)O` | (-inf, HL, 5.86, L, +inf) |
| ligand_8910 | meso-Butane-2,3-… (meso-2,3-Dimethylsuccinic acid) | H2L | Carboxylic acids diacids | 10 | `C[C@H](C(=O)O)[C@@H](C)C(=O)O` | (-inf, H2L, 3.67, HL, 5.3, L, +inf) |

### Functional groups across all SQL matches (11 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 11 | 100% |
| hydroxyl | 2 | 18% |
| secondary_amine | 1 | 9% |

---

### Step 18: `search_ligands`
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

### Step 19: `search_ligands`
**Args:**
```json
{
  "name": "tartaric acid",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 9 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8955 | D-2,3-Dihydroxybutanedioic acid (D-Tartaric acid) | H2L | Carboxylic acids diacids… | 214 | `O=C(O)C(O)C(O)C(=O)O` | (-inf, H2L, 2.82, HL, 3.97, L, +inf) |
| ligand_8956 | meso-2,3-Dihydroxybutanedioi… (meso-Tartaric acid) | H2L | Carboxylic acids diacids… | 43 | `O=C(O)[C@@H](O)[C@@H](O)C(=O)O` | (-inf, H2L, 2.97, HL, 4.49, L, +inf) |
| ligand_8996 | DL-2,3-Dimercaptobutaned… (DL-Dithiotartaric acid) | H4L | Carboxylic acids diacids… | 9 | `O=C(O)C(S)C(S)C(=O)O` | (-inf, H4L, 2.25, H3L, 3.96, H2L, 9.61, HL, +inf) |
| ligand_8997 | meso-2,3-Dimercaptobut… (meso-Dithiotartaric acid) | H4L | Carboxylic acids diacids… | 41 | `O=C(O)[C@@H](S)[C@@H](S)C(=O)O` | (-inf, H4L, 2.4, H3L, 3.46, H2L, 9.64, HL, 9.64, L, +inf) |
| ligand_10941 | erthro-2-Methyltartaric acid | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (4 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 4 | 100% |
| hydroxyl | 2 | 50% |
| thiol | 2 | 50% |

---

### Step 20: `search_ligands`
**Args:**
```json
{
  "name": "nitrilotriacetic",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 35 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6047 | N,N''-Bis(3-hydroxy-6-methyl-2-pyridiny… (DTTA-HP) | H5L | Amino Acids | 24 | `Cc1ccc(O)c(CN(CCN(CCN(CC(=O)O)Cc2nc(C)ccc2O)CC(=O)O)CC(=O)O)n1` | (-inf, H8L, -1.5, H7L, 2.25, H6L, 3.49, H5L, 5.19, H4L, 6.21, H3L, 8.9, H2L, 10.95, HL, 10.95, L, +inf) |
| ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | NTA and derivatives | 534 | `O=C(O)CN(CC(=O)O)CC(=O)O` | (-inf, H4L, -1, H3L, -1, H2L, 2.52, HL, 9.46, L, +inf) |
| ligand_6166 | Nitrilotriacetic acid N-oxide | H3L | NTA and derivatives | 4 | `O=C(O)C[N+]([O-])(CC(=O)O)CC(=O)O` | (-inf, H2L, 2.57, HL, 7.89, L, +inf) |
| ligand_6172 | DL-2-Methylnitrilotriacetic acid | H3L | NTA and derivatives | 50 | `CC(C(=O)O)N(CC(=O)O)CC(=O)O` | (-inf, H3L, -1.5, H2L, -1.5, HL, -2.58, L, +inf) |
| ligand_6173 | DL-2-Ethylnitrilotriacetic acid | H3L | NTA and derivatives | 43 | `CCC(C(=O)O)N(CC(=O)O)CC(=O)O` | (-inf, H3L, -1.9, H2L, -1.9, HL, 9.81, L, +inf) |

### Functional groups across all SQL matches (34 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 34 | 100% |
| tertiary_amine | 33 | 97% |
| aromatic_ring | 12 | 35% |
| hydroxyl | 4 | 12% |
| amide | 2 | 6% |
| halide | 2 | 6% |
| phenol | 1 | 3% |
| pyridine | 1 | 3% |
| secondary_amine | 1 | 3% |
| sulfonate | 1 | 3% |
| thioether | 1 | 3% |

---

### Step 21: `search_ligands`
**Args:**
```json
{
  "name": "salicylic acid",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 43 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8701 | 2-Acetoxybenzoic acid (Acetylsalicylic acid) | HL | Carboxylic acids keto | 5 | `CC(=O)Oc1ccccc1C(=O)O` | (-inf, HL, 3.45, L, +inf) |
| ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | H2L | Phenols salicylic acids | 227 | `O=C(O)c1ccccc1O` | (-inf, H2L, 2.8, HL, 2.8, L, +inf) |
| ligand_9265 | 2-Hydroxy-3-methylbenzoic acid (3-Methylsalicylic… | H2L | Phenols salicylic acids | 9 | `Cc1cccc(C(=O)O)c1O` | (-inf, H2L, 2.83, HL, 2.83, L, +inf) |
| ligand_9266 | 2-Hydroxy-4-methylbenzoic acid (4-Methylsalicylic… | H2L | Phenols salicylic acids | 8 | `Cc1ccc(C(=O)O)c(O)c1` | (-inf, H2L, 2.96, HL, 2.96, L, +inf) |
| ligand_9267 | 2-Hydroxy-5-methylbenzoic acid (5-Methylsalicylic… | H2L | Phenols salicylic acids | 6 | `Cc1ccc(O)c(C(=O)O)c1` | (-inf, H2L, 2.88, HL, 2.88, L, +inf) |

### Functional groups across all SQL matches (25 parseable SMILES)

| group | count | % |
|-------|-------|---|
| aromatic_ring | 25 | 100% |
| carboxyl | 25 | 100% |
| hydroxyl | 24 | 96% |
| phenol | 24 | 96% |
| halide | 6 | 24% |
| tertiary_amine | 5 | 20% |
| sulfonate | 3 | 12% |
| primary_amine | 2 | 8% |
| ester | 1 | 4% |
| nitrile | 1 | 4% |

---

### Step 22: `search_ligands`
**Args:**
```json
{
  "name": "phosphoric acid",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 43 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_9150 | Phosphoric acid methyl ester (Methyl phosphate) | H2L | Organophosphorus and ars… | 12 | `COP(=O)(O)O` | (-inf, HL, 6.25, L, +inf) |
| ligand_9151 | Phosphoric acid butyl ester (Butyl phosphate) | H2L | Organophosphorus and ars… | 11 | `CCCCOP(=O)(O)O` | (-inf, HL, 6.72, L, +inf) |
| ligand_9152 | Phosphoric acid phenyl ester (Phenyl phosphate) | H2L | Organophosphorus and ars… | 24 | `O=P(O)(O)Oc1ccccc1` | (-inf, H2L, -0.9, HL, 5.78, L, +inf) |
| ligand_9153 | Phosphoric acid 4-nitro… (4-Nitrophenyl phosphate) | H2L | Organophosphorus and ars… | 4 | `O=[N+]([O-])c1ccc(OP(=O)(O)O)cc1` | (-inf, HL, 5.01, L, +inf) |
| ligand_9154 | Phosphoric acid 1-naph… (alpha-Naphthyl phosphate) | H2L | Organophosphorus and ars… | 18 | `O=P(O)(O)Oc1cccc2ccccc12` | (-inf, H2L, -0.9, HL, 5.74, L, +inf) |

### Functional groups across all SQL matches (28 parseable SMILES)

| group | count | % |
|-------|-------|---|
| hydroxyl | 26 | 93% |
| phosphate | 23 | 82% |
| aromatic_ring | 6 | 21% |
| secondary_amine | 2 | 7% |
| tertiary_amine | 2 | 7% |
| thiol | 2 | 7% |

---

### Step 23: `search_ligands`
**Args:**
```json
{
  "name": "carbonate",
  "limit": 5
}
```

[summary]
## search_ligands — 4 result(s)

**stats:** 4 SQL matches · showing 4 · limit 5

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

### Step 24: `search_ligands`
**Args:**
```json
{
  "name": "iminodiacetic",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 140 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5975 | Ethylenediiminodiacetic acid (EDDA) | H2L | Amino Acids | 198 | `O=C(O)CNCCNCC(=O)O` | (-inf, H4L, -1.3, H3L, 2.12, H2L, 6.55, HL, 9.61, L, +inf) |
| ligand_5994 | N,N'-Bis(2-hydroxyphenyl)ethylenediiminodi… (HPED) | H4L | Amino Acids | 37 | `O=C(O)CN(CCN(CC(=O)O)c1ccccc1O)c1ccccc1O` | (-inf, H5L, -1.9, H4L, 3.58, H3L, 6.15, H2L, 10.44, HL, 10.44, L, +inf) |
| ligand_6013 | N-(4-Methylphenylsulfonyl)ethylenediiminodiacetic… | H2L | Amino Acids | 2 | `Cc1ccc(S(=O)(=O)N(CCNCC(=O)O)CC(=O)O)cc1` | (-inf, H2L, 2, HL, 7.83, L, +inf) |
| ligand_6127 | Iminodiacetic acid (IDA) | H2L | Iminodiacetic acid and d… | 375 | `O=C(O)CNCC(=O)O` | (-inf, H3L, -1.77, H2L, 2.62, HL, 9.34, L, +inf) |
| ligand_6129 | L-2-(2-Propyl)iminodiacetic acid | H2L | Iminodiacetic acid and d… | 5 | `CC(C)C(NCC(=O)O)C(=O)O` | (-inf, H3L, -1.5, H2L, 2.42, HL, 9.23, L, +inf) |

### Functional groups across all SQL matches (117 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 117 | 100% |
| tertiary_amine | 106 | 91% |
| aromatic_ring | 51 | 44% |
| hydroxyl | 38 | 32% |
| secondary_amine | 17 | 15% |
| amide | 13 | 11% |
| phenol | 11 | 9% |
| sulfonate | 9 | 8% |
| ether | 3 | 3% |
| halide | 3 | 3% |
| ketone | 3 | 3% |
| primary_amine | 3 | 3% |
| pyridine | 3 | 3% |
| thioether | 3 | 3% |
| phosphonate | 2 | 2% |
| thiol | 2 | 2% |
| ester | 1 | 1% |
| nitrile | 1 | 1% |

---

### Step 25: `search_ligands`
**Args:**
```json
{
  "name": "lactic acid",
  "limit": 5
}
```

[summary]
## search_ligands — 4 result(s)

**stats:** 4 SQL matches · showing 4 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8641 | D-2-Hydroxypropanoic acid (Lactic acid) | HL | Carboxylic acids hydroxy | 349 | `CC(O)C(=O)O` | (-inf, HL, 3.67, L, +inf) |
| ligand_8660 | DL-2-Phenyl-2-hydroxypropanoic … (Atrolactic acid) | HL | Carboxylic acids hydroxy | 34 | `CC(O)(C(=O)O)c1ccccc1` | (-inf, HL, 3.53, L, +inf) |
| ligand_8767 | DL-2-Mercaptopropanoic acid (Thiolactic acid) | H2L | Carboxylic acids thio | 71 | `CC(S)C(=O)O` | (-inf, H2L, 3.48, HL, 10.08, L, +inf) |
| ligand_8976 | DL-2,2'-Oxydipropanoic acid (Dilactic acid) | H2L | Carboxylic acids diacids | 30 | `CC(OC(C)C(=O)O)C(=O)O` | *** |

### Functional groups across all SQL matches (4 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 4 | 100% |
| hydroxyl | 2 | 50% |
| aromatic_ring | 1 | 25% |
| ether | 1 | 25% |
| thiol | 1 | 25% |

---

### Step 26: `search_ligands`
**Args:**
```json
{
  "name": "glycolic acid",
  "limit": 5
}
```

[summary]
## search_ligands — 4 result(s)

**stats:** 4 SQL matches · showing 4 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8640 | Hydroxyacetic acid (Glycolic acid) | HL | Carboxylic acids hydroxy | 402 | `O=C(O)CO` | (-inf, HL, 3.62, L, +inf) |
| ligand_8766 | Mercaptoacetic acid (Thioglycolic acid) | H2L | Carboxylic acids thio | 148 | `O=C(O)CS` | (-inf, H2L, 3.48, HL, 10.11, L, +inf) |
| ligand_8974 | Oxydiacetic acid (Diglycolic acid) | H2L | Carboxylic acids diacids | 363 | `O=C(O)COCC(=O)O` | (-inf, H2L, 2.82, HL, 3.94, L, +inf) |
| ligand_10907 | Acrylamidoglycolic acid | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (3 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 3 | 100% |
| ether | 1 | 33% |
| hydroxyl | 1 | 33% |
| thiol | 1 | 33% |

---

### Step 27: `search_ligands`
**Args:**
```json
{
  "name": "acetic acid",
  "limit": 3,
  "exclude_groups": [
    "aromatic_ring",
    "primary_amine",
    "secondary_amine",
    "tertiary_amine"
  ]
}
```

[summary]
## search_ligands — 3 result(s)

**stats:** 683 SQL matches · 470 excluded by group filter · showing 3 · limit 3

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6039 | N,N"-Bis(2-hydroxybenzyl)diethylenetrinitr… (HBDT) | *** | Amino Acids | 49 | *** | (-inf, H6L, -1.7, H5L, 3.95, H4L, 7.17, H3L, 9.32, H2L, 10.98, HL, 10.98, L, +inf) |
| ligand_6092 | 9,16-Dioxo-1,4,7,10,15-pentaaza-cis-cycloheptadec… | *** | Aza macrocycles with car… | 6 | *** | (-inf, H4L, 2, H3L, 3.32, H2L, 4.67, HL, 9.68, L, +inf) |
| ligand_6118 | 6,11,18,23-Tetraoxo-1,4,7,10,13,16,19,… (24edtaen) | *** | Aza macrocycles with car… | 15 | *** | (-inf, H4L, 3.3, H3L, 4.18, H2L, 7.26, HL, 7.78, L, +inf) |

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

### Step 28: `search_ligands`
**Args:**
```json
{
  "name": "propionic acid",
  "limit": 3
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 3

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8467 | Propanoic acid (Propionic acid) | HL | Carboxylic acids | 236 | `CCC(=O)O` | (-inf, HL, 4.69, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 1 | 100% |

---

### Step 29: `search_ligands`
**Args:**
```json
{
  "formula": "C2H4O2",
  "limit": 5
}
```

[summary]
## search_ligands — 3 result(s)

**stats:** 3 SQL matches · showing 3 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8465 | Ethanoic acid (Acetic acid) | HL | Carboxylic acids | 562 | `CC(=O)O` | (-inf, HL, 4.56, L, +inf) |
| ligand_8466 | Ethanoic acid trideuterated (Acetic acid-d3) | *** | Carboxylic acids | 5 | *** | (-inf, HL, 4.772, L, +inf) |
| ligand_8766 | Mercaptoacetic acid (Thioglycolic acid) | H2L | Carboxylic acids thio | 148 | `O=C(O)CS` | (-inf, H2L, 3.48, HL, 10.11, L, +inf) |

### Functional groups across all SQL matches (2 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 2 | 100% |
| thiol | 1 | 50% |

---

### Step 30: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_25 AND c.ligand_id = ligand_8464 AND s.constant_type = 'log_beta'",
  "order_by": "s.constant_value DESC",
  "limit": 5
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 31: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_25 AND c.ligand_id = ligand_8465 AND s.constant_type = 'log_beta'",
  "order_by": "s.constant_value DESC",
  "limit": 5
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 32: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_25 AND c.ligand_id = ligand_8640 AND s.constant_type = 'log_beta'",
  "order_by": "s.constant_value DESC",
  "limit": 5
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 33: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_25 AND c.ligand_id = ligand_8641 AND s.constant_type = 'log_beta'",
  "order_by": "s.constant_value DESC",
  "limit": 5
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 34: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_25 AND c.ligand_id = ligand_8872 AND s.constant_type = 'log_beta'",
  "order_by": "s.constant_value DESC",
  "limit": 5
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 35: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_25 AND c.ligand_id = ligand_8873 AND s.constant_type = 'log_beta'",
  "order_by": "s.constant_value DESC",
  "limit": 5
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 36: `build_system_catalog`
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
