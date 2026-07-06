# Q3.1.1 — Tool Results (batch 1)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "lead",
  "symbol": "Pb"
}
```

[summary]
## search_metals — 11 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_16 | Bu_[3]Pb^[+] | B | 1 |  | *** | *** | beta_totN_2 | ligand_totN_1 | vlm_totN_2 |
| metal_46 | Et_[2]Pb^[2+] | E2Pb | 2 |  | *** | *** | beta_totN_2 | ligand_totN_3 | vlm_totN_5 |
| metal_49 | Et_[3]Pb^[+] | E3Pb | 1 |  | *** | *** | beta_totN_2 | ligand_totN_3 | vlm_totN_5 |
| metal_84 | Me_[2]Pb^[2+] | M2Pb | 2 |  | *** | *** | beta_totN_5 | ligand_totN_4 | vlm_totN_9 |
| metal_87 | Me_[3]Pb^[+] | M3Pb | 1 |  | *** | *** | beta_totN_7 | ligand_totN_23 | vlm_totN_33 |
| metal_125 | Pb^[2+] | Pb | 2 | ✓ | [Pb+2] | InChI=1S/Pb/q+2 | beta_totN_80 | ligand_totN_470 | vlm_totN_1585 |
| metal_126 | Pb^[4+] | Pb | 4 | ✓ | [Pb+4] | InChI=1S/Pb/q+4 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_129 | Ph_[2]Pb^[2+] | Ph2Pb | 2 |  | *** | *** | beta_totN_2 | ligand_totN_1 | vlm_totN_2 |
| metal_130 | Ph_[3]Pb^[+] | Ph3Pb | 1 |  | *** | *** | beta_totN_1 | ligand_totN_2 | vlm_totN_2 |
| metal_140 | Pr_[2]Pb^[2+] | Pr | 2 |  | *** | *** | beta_totN_2 | ligand_totN_3 | vlm_totN_5 |
| metal_142 | Pr_[3]Pb^[+] | Pr | 1 |  | *** | *** | beta_totN_2 | ligand_totN_1 | vlm_totN_2 |

---

### Step 3: `search_ligands`
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

### Step 4: `search_ligands`
**Args:**
```json
{
  "name": "DTPA",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 5 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6117 | 9,17-Dioxo-1,4,7,10,13,16-hexaazacycl… (DTPA-dien) | H3L | Aza macrocycles with car… | 6 | `O=C(O)CN1CCN(CC(=O)O)CC(=O)NCCNCCNC(=O)CN(CC(=O)O)CC1` | (-inf, H5L, -1.8, H4L, 2.62, H3L, 4.1, H2L, 8.87, HL, 10.02, L, +inf) |
| ligand_6356 | Diethylenetrinitrilopentaacetic acid (DTPA) | H5L | EDTA and derivatives | 322 | `O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O` | (-inf, H8L, -0.1, H7L, -0.1, H6L, -0.7, H5L, 2, H4L, 2.7, H3L, 4.28, H2L, 4.28, HL, -8.4, L, +inf) |
| ligand_6362 | Diethylenetrinitrilopentaacetic acid N… (DTPA-BMA) | *** | EDTA and derivatives | 43 | *** | (-inf, H4L, -1.4, H3L, 3.31, H2L, 4.38, HL, 9.37, L, +inf) |
| ligand_6363 | Diethylenetrinitrilopentaacetic acid N… (DTPA-BBA) | *** | EDTA and derivatives | 9 | *** | (-inf, H3L, 3.31, H2L, 4.44, HL, 9.36, L, +inf) |
| ligand_6364 | N,N"-Bis(2-pyridylmethyl)diethylenetrin… (DTPA-BP) | *** | EDTA and derivatives | 14 | *** | (-inf, H5L, 2.28, H4L, 3.41, H3L, 4.76, H2L, 6.46, HL, 9.5, L, +inf) |

### Functional groups across all SQL matches (2 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 2 | 100% |
| tertiary_amine | 2 | 100% |
| amide | 1 | 50% |
| secondary_amine | 1 | 50% |

---

### Step 5: `search_ligands`
**Args:**
```json
{
  "name": "DMSA",
  "limit": 5
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8997 | meso-2,3-Dimercaptobut… (meso-Dithiotartaric acid) | H4L | Carboxylic acids diacids… | 41 | `O=C(O)[C@@H](S)[C@@H](S)C(=O)O` | (-inf, H4L, 2.4, H3L, 3.46, H2L, 9.64, HL, 9.64, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 1 | 100% |
| thiol | 1 | 100% |

---

### Step 6: `search_ligands`
**Args:**
```json
{
  "name": "penicillamine",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 6 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5857 | D-2-Amino-3-mercapto-3-methylbuta… (Penicillamine) | H2L | Amino Acids | 91 | `CC(C)(S)[C@H](N)C(=O)O` | (-inf, H3L, -1.9, H2L, 7.96, HL, 10.67, L, +inf) |
| ligand_5891 | D-3,3'-Dithiobis(2-amin… (Penicillamine disulfide) | H2L | Amino Acids | 23 | `CC(C)(SSC(C)(C)C(N)C(=O)O)C(N)C(=O)O` | (-inf, H4L, -1.3, H3L, 2.04, H2L, 7.77, HL, 8.74, L, +inf) |
| ligand_6657 | L-5-Glutamyl… (Penicillamine-glutatione disulfide) | H3L | polypeptides | 2 | `CC(C)(SSCC(NC(=O)CCC(N)C(=O)O)C(=O)NCC(=O)O)C(N)C(=O)O` | (-inf, H2L, 7.99, HL, 9.1, L, +inf) |
| ligand_8773 | N-Acetyl-D-penicillamine | H2L | Carboxylic acids thio | 19 | `CC(=O)N[C@@H](C(=O)O)C(C)(C)S` | (-inf, H2L, 3.29, HL, 10.1, L, +inf) |
| ligand_10214 | DL-3,3-Di… (D-Penicillamine-DL-cysteine disulfide) | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (4 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 4 | 100% |
| primary_amine | 3 | 75% |
| amide | 2 | 50% |
| thiol | 2 | 50% |

---

### Step 7: `search_ligands`
**Args:**
```json
{
  "name": "dimercaprol",
  "limit": 5
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_9759 | 2,3-Dimercaptopropanol (BAL) | H2L | miscellaneous mercaptans | 25 | `OCC(S)CS` | (-inf, H2L, 8.63, HL, 10.65, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| hydroxyl | 1 | 100% |
| thiol | 1 | 100% |

---

### Step 8: `search_ligands`
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

### Step 9: `search_ligands`
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

### Step 10: `search_ligands`
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

### Step 11: `search_ligands`
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

### Step 12: `search_ligands`
**Args:**
```json
{
  "name": "succimer",
  "limit": 5
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8997 | meso-2,3-Dimercaptobut… (meso-Dithiotartaric acid) | H4L | Carboxylic acids diacids… | 41 | `O=C(O)[C@@H](S)[C@@H](S)C(=O)O` | (-inf, H4L, 2.4, H3L, 3.46, H2L, 9.64, HL, 9.64, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 1 | 100% |
| thiol | 1 | 100% |

---

### Step 13: `search_ligands`
**Args:**
```json
{
  "name": "dimercaptopropane",
  "limit": 5
}
```

[summary]
## search_ligands — 2 result(s)

**stats:** 2 SQL matches · showing 2 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_9758 | 2,3-Dimercaptopropanesulfonic acid (Unithiol) | H3L | miscellaneous mercaptans | 28 | `O=S(=O)(O)CC(S)CS` | (-inf, H3L, -1.1, H2L, 8.67, HL, 8.67, L, +inf) |
| ligand_11271 | 1,3-Dimercaptopropane-2-sulfonic acid | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| hydroxyl | 1 | 100% |
| sulfonate | 1 | 100% |
| thiol | 1 | 100% |

---

### Step 15: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_125"
}
```

[summary]
[CATALOG]
## build_system_catalog — 20 pair(s), 126 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_194 | [M] + [HL]^2 <=> [M(HL)2] |  |
| beta_def_204 | [MHL2] + [H] <=> [M(HL)2] |  |
| beta_def_208 | [M] + [HL]^3 <=> [M(HL)3] |  |
| beta_def_317 | [ML(s,cerussite)] <=> [M] + [L] | solid |
| beta_def_328 | [(M2OL2)0.5(s)] + [H2O]^0.5 <=> [M] + [L] + [OH] | solid |
| beta_def_334 | [ML2(s)] <=> [M] + [L]^2 | solid |
| beta_def_348 | [MO(s,red)] + [H2O] <=> [M] + [OH]^2 | solid |
| beta_def_349 | [MO(s,yellow)] + [H2O] <=> [M] + [OH]^2 | solid |
| beta_def_363 | [H]^8 + [M10(OH)6OL6(s)] <=> [M]^10 + [L]^6 + [H2O]^7 | solid |
| beta_def_433 | [M2(OH)L2] + [OH] <=> [M2(OH)2L2] |  |
| beta_def_473 | [M2HL] + [H] <=> [M2H2L] |  |
| beta_def_483 | [M2H2L] + [H] <=> [M2H3L] |  |
| beta_def_486 | [M2H3L] + [H] <=> [M2H4L] |  |
| beta_def_493 | [M2L] + [H] <=> [M2HL] |  |
| beta_def_502 | [M]^2 + [L] <=> [M2L] |  |
| beta_def_515 | [M2(OH)L] + [H] <=> [M2L] + [H2O] |  |
| beta_def_519 | [M]^2 + [L]^2 <=> [M2L2] |  |
| beta_def_574 | [M2(OH)2L] + [H] <=> [M2(OH)L] + [H2O] |  |
| beta_def_584 | [M2L2] + [OH] <=> [M2(OH)L2] |  |
| beta_def_596 | [M3(OH)3L] + [H] <=> [M3(OH)2L] + [H2O] |  |
| beta_def_616 | [M3(OH)2L2(s)] <=> [M]^3 + [OH]^2 + [L]^2 | solid |
| beta_def_635 | [M3L] + [H] <=> [M3HL] |  |
| beta_def_638 | [M]^3 + [L] <=> [M3L] |  |
| beta_def_640 | [M3(OH)L] + [H] <=> [M3L] + [H2O] |  |
| beta_def_649 | [M]^3 + [L]^4 <=> [M3L4] |  |
| beta_def_656 | [M3(OH)2L] + [H] <=> [M3OHL] + [H2O] |  |
| beta_def_674 | [M]^4 + [L]^4 <=> [M4L4] |  |
| beta_def_706 | [M]^6 + [L]^8 <=> [M6L8] |  |
| beta_def_732 | [M] + [H2L] <=> [MH2L] |  |
| beta_def_739 | [MHL] + [H] <=> [MH2L] |  |
| beta_def_744 | [MHL3] + [H] <=> [MH2L3] |  |
| beta_def_779 | [M] + [HL] <=> [MHL] |  |
| beta_def_788 | [ML] + [H] <=> [MHL] |  |
| beta_def_792 | [ML2] + [H] <=> [MHL2] |  |
| beta_def_797 | [M] + [H] + [L]^2 <=> [MHL2] |  |
| beta_def_803 | [ML3] + [H] <=> [MHL3] |  |
| beta_def_812 | [M] + [L] <=> [ML] |  |
| beta_def_840 | [M] + [L]^2 <=> [ML2] |  |
| beta_def_872 | [M] + [L]^3 <=> [ML3] |  |
| beta_def_894 | [M] + [L]^4 <=> [ML4] |  |
| beta_def_966 | [M(OH)L] + [H] <=> [ML] + [H2O] |  |
| beta_def_978 | [M] + [L] + [OH] <=> [M(OH)L] |  |
| beta_def_984 | [M(OH)L2] + [H] <=> [ML2] + [H2O] |  |

*(all species aqueous unless noted)*

**1. Pb^[2+] + Bromide ion** (metal_125 + ligand_10168) — ligand_def_HxL: *** | 45 ent, 5 sp, 45 vlms (vlm_178198…vlm_178242)
   - species: beta_def_334(8) beta_def_812(11) beta_def_840(10) beta_def_872(9) beta_def_894(7)
   - eq:9 nets T:19~30°C I:-0.15~4.15M max 5n/10e
**2. Pb^[2+] + Hydroxide ion** (metal_125 + ligand_10076) — ligand_def_HxL: *** | 34 ent, 10 sp, 34 vlms (vlm_171068…vlm_171101)
   - species: beta_def_328(1) beta_def_348(1) beta_def_349(1) beta_def_502(2) beta_def_649(5) beta_def_674(7) beta_def_706(5) beta_def_812(5) beta_def_840(3) beta_def_872(4)
   - eq:6 nets T:19~30°C I:-0.15~5.15M max 10n/45e
**3. Pb^[2+] + Chloride ion** (metal_125 + ligand_10163) — ligand_def_HxL: *** | 32 ent, 4 sp, 32 vlms (vlm_177638…vlm_177669)
   - species: beta_def_334(2) beta_def_812(10) beta_def_840(10) beta_def_872(10)
   - eq:8 nets T:19~30°C I:-0.15~4.15M max 4n/6e
**4. Pb^[2+] + Iodide ion** (metal_125 + ligand_10171) — ligand_def_HxL: *** | 28 ent, 5 sp, 28 vlms (vlm_178552…vlm_178579)
   - species: beta_def_334(4) beta_def_812(6) beta_def_840(6) beta_def_872(6) beta_def_894(6)
   - eq:6 nets T:19~30°C I:-0.05~4.15M max 5n/10e
**5. Pb^[2+] + Thiocarbamide (Thiourea)** (metal_125 + ligand_10004) — ligand_def_HxL: L | 28 ent, 4 sp, 28 vlms (vlm_169581…vlm_169608)
   - species: beta_def_812(7) beta_def_840(7) beta_def_872(7) beta_def_894(7)
   - eq:5 nets T:19~30°C I:-0.05~3.15M max 4n/6e
**6. Pb^[2+] + Aminoacetic acid (Glycine)** (metal_125 + ligand_5760) — ligand_def_HxL: HL | 25 ent, 8 sp, 25 vlms (vlm_94001…vlm_94025)
   - species: beta_def_194(2) beta_def_204(1) beta_def_208(1) beta_def_779(5) beta_def_792(1) beta_def_812(8) beta_def_840(4) beta_def_966(3)
   - eq:4 nets T:19~30°C I:-0.05~3.15M max 6n/11e
**7. Pb^[2+] + Nitrate ion** (metal_125 + ligand_10109) — ligand_def_HxL: *** | 23 ent, 4 sp, 23 vlms (vlm_174057…vlm_174079)
   - species: beta_def_812(9) beta_def_840(7) beta_def_872(4) beta_def_894(3)
   - eq:5 nets T:19~30°C I:-0.05~3.15M max 4n/6e
**8. Pb^[2+] + Ethanoic acid (Acetic acid)** (metal_125 + ligand_8465) — ligand_def_HxL: HL | 20 ent, 3 sp, 20 vlms (vlm_144913…vlm_144932)
   - species: beta_def_812(8) beta_def_840(7) beta_def_872(5)
   - eq:6 nets T:19~35°C I:-0.15~3.15M max 3n/3e
**9. Pb^[2+] + Butanedioic acid (Succinic acid)** (metal_125 + ligand_8907) — ligand_def_HxL: H2L | 16 ent, 8 sp, 16 vlms (vlm_153489…vlm_153504)
   - species: beta_def_194(2) beta_def_744(1) beta_def_779(2) beta_def_792(2) beta_def_803(2) beta_def_812(3) beta_def_840(2) beta_def_872(2)
   - eq:3 nets T:19~30°C I:-0.05~3.15M max 8n/15e
**10. Pb^[2+] + L-2-Amino-3-mercaptopropanoic acid (Cysteine)** (metal_125 + ligand_5856) — ligand_def_HxL: H2L | 16 ent, 5 sp, 16 vlms (vlm_97478…vlm_97493)
   - species: beta_def_779(4) beta_def_797(3) beta_def_812(6) beta_def_840(2) beta_def_984(1)
   - eq:4 nets T:19~30°C I:-0.05~3.15M max 5n/8e
**11. Pb^[2+] + L-5-Glutamyl-L-cysteinylglycine (Glutathione)** (metal_125 + ligand_6592) — ligand_def_HxL: H3L | 14 ent, 6 sp, 14 vlms (vlm_116692…vlm_116705)
   - species: beta_def_204(3) beta_def_739(3) beta_def_788(3) beta_def_812(3) beta_def_840(1) beta_def_984(1)
   - eq:1 nets T:16.5~31.5°C I:2.775~3.225M max 6n/9e
**12. Pb^[2+] + Hydrogen carbonate (Carbonic acid)** (metal_125 + ligand_10096) — ligand_def_HxL: H2L | 13 ent, 9 sp, 13 vlms (vlm_172928…vlm_172940)
   - species: beta_def_317(4) beta_def_363(1) beta_def_502(1) beta_def_616(1) beta_def_638(1) beta_def_779(1) beta_def_812(1) beta_def_840(2) beta_def_978(1)
   - eq:6 nets T:19~30°C I:-0.15~3.15M max 5n/10e
**13. Pb^[2+] + N-Ethylthiourea** (metal_125 + ligand_10006) — ligand_def_HxL: L | 13 ent, 4 sp, 13 vlms (vlm_169663…vlm_169675)
   - species: beta_def_812(4) beta_def_840(3) beta_def_872(3) beta_def_894(3)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 4n/6e
**14. Pb^[2+] + D-2-Amino-3-mercapto-3-methylbutanoic acid (Penicillamine)** (metal_125 + ligand_5857) — ligand_def_HxL: H2L | 13 ent, 7 sp, 13 vlms (vlm_97622…vlm_97634)
   - species: beta_def_204(1) beta_def_779(3) beta_def_792(2) beta_def_812(3) beta_def_840(2) beta_def_966(1) beta_def_984(1)
   - eq:3 nets T:19~41°C I:-0.05~3.15M max 6n/8e
**15. Pb^[2+] + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid)** (metal_125 + ligand_9058) — ligand_def_HxL: H3L | 12 ent, 8 sp, 12 vlms (vlm_157788…vlm_157799)
   - species: beta_def_433(1) beta_def_519(1) beta_def_584(1) beta_def_732(2) beta_def_779(2) beta_def_792(1) beta_def_812(2) beta_def_840(2)
   - eq:2 nets T:16.5~31.5°C I:0.775~2.225M max 8n/13e
**16. Pb^[2+] + D-2-Hydroxypropanoic acid (Lactic acid)** (metal_125 + ligand_8641) — ligand_def_HxL: HL | 12 ent, 3 sp, 12 vlms (vlm_147786…vlm_147797)
   - species: beta_def_812(6) beta_def_840(5) beta_def_872(1)
   - eq:4 nets T:19~30°C I:-0.05~3.15M max 3n/3e
**17. Pb^[2+] + 1,4,7,10,13,16,19,22,25,28,31,34-Dodecaazacyclohexatriacontane ([36]aneN12)** (metal_125 + ligand_7541) — ligand_def_HxL: L | 12 ent, 12 sp, 12 vlms (vlm_130878…vlm_130889)
   - species: beta_def_473(1) beta_def_483(1) beta_def_486(1) beta_def_493(1) beta_def_502(1) beta_def_515(1) beta_def_574(1) beta_def_596(1) beta_def_635(1) beta_def_638(1) beta_def_640(1) beta_def_656(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 12n/50e
**18. Pb^[2+] + Hydrogen nitrite (Nitrous acid)** (metal_125 + ligand_10108) — ligand_def_HxL: HL | 11 ent, 3 sp, 11 vlms (vlm_173824…vlm_173834)
   - species: beta_def_812(6) beta_def_840(3) beta_def_872(2)
   - eq:8 nets T:15~35°C I:-0.15~4.15M max 3n/3e
**19. Pb^[2+] + Propanedioic acid (Malonic acid)** (metal_125 + ligand_8873) — ligand_def_HxL: H2L | 11 ent, 7 sp, 11 vlms (vlm_152381…vlm_152391)
   - species: beta_def_194(1) beta_def_779(1) beta_def_792(1) beta_def_803(1) beta_def_812(4) beta_def_840(2) beta_def_872(1)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 7n/13e
**20. Pb^[2+] + 1,4,7,10,13,16,19,22,25,28,31-Undecaazacyclotritriacontane ([33]aneN11)** (metal_125 + ligand_7540) — ligand_def_HxL: L | 11 ent, 11 sp, 11 vlms (vlm_130831…vlm_130841)
   - species: beta_def_473(1) beta_def_483(1) beta_def_486(1) beta_def_493(1) beta_def_502(1) beta_def_515(1) beta_def_574(1) beta_def_635(1) beta_def_638(1) beta_def_640(1) beta_def_656(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 11n/41e

---

### Step 16: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_125 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 20 AND 30",
  "order_by": "s.constant_value DESC",
  "limit": 50
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. You must call 0_plan_search_strategy first (PHASE 2) before using the execution tools.

---
