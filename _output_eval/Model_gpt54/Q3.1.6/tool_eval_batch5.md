# Q3.1.6 — Tool Results (batch 5)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Lanthanum",
  "limit": 10
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_79 | La^[3+] | La | 3 | ✓ | [La+3] | InChI=1S/La/q+3 | beta_totN_30 | ligand_totN_297 | vlm_totN_931 |

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "DTPA, EDTA, EGTA, NTA, citrate, oxalate, tartrate, malonate, succinate, acetate, lactate, benzoate",
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

### Step 5: `search_ligands`
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

### Step 6: `search_ligands`
**Args:**
```json
{
  "name": "DTPA",
  "limit": 10
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 5 SQL matches · showing 5 · limit 10

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

### Step 7: `search_ligands`
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

### Step 8: `search_ligands`
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

### Step 9: `search_ligands`
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

### Step 10: `search_ligands`
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

### Step 11: `search_ligands`
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

### Step 12: `search_ligands`
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
  "name": "lactate",
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
  "name": "benzoate",
  "limit": 10
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_9854 | Benzoic acid ethyl ester (Ethyl benzoate) | *** | miscellaneous hydrocarbo… | 1 | *** | *** |

---

### Step 16: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_79",
  "ligand_id": "ligand_6356"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 2 species

### La^[3+] + Diethylenetrinitrilopentaacetic acid (DTPA)
**metal_id:** metal_79 | **ligand_id:** ligand_6356 | **ligand_def_HxL:** H5L  
**entries:** 5 | **species:** 2 | **vlm_count:** 5

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_788 | [MHL]/[ML][H] | [ML] + [H] <=> [MHL] | [MHL](aqueous), [ML](aqueous), [H](aqueous) | 1 |
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 4 |

**vlm_ids:** vlm_112568, vlm_112569, vlm_112570, vlm_112571, vlm_112572

**equilibrium_maps:** 2 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_6673 | 2 | 1 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_6674 | 1 | 0 | 19~29 °C | 0.35~0.65 M |

---

### Step 18: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_79 AND s.constant_type = 'log_beta' AND c.beta_definition_name = '[ML]/[M][L]' AND (s.temperature_c BETWEEN 20 AND 30 OR s.temperature_c IS NULL) AND (s.ionic_strength_mol_l <= 0.2 OR s.ionic_strength_mol_l IS NULL) AND (s.solvent_name LIKE '%water%' OR s.solvent_name IS NULL))",
  "order_by": "s.constant_value DESC",
  "limit": 50,
  "include_groups": [
    "carboxyl"
  ]
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
  "where": "(c.metal_id = metal_79 AND s.constant_type = 'log_beta' AND c.beta_definition_name = '[ML]/[M][L]' AND c.ligand_id IN (ligand_6356, ligand_6277, ligand_6342, ligand_8873) AND (s.temperature_c BETWEEN 20 AND 30 OR s.temperature_c IS NULL) AND (s.ionic_strength_mol_l <= 0.2 OR s.ionic_strength_mol_l IS NULL) AND (s.solvent_name LIKE '%water%' OR s.solvent_name IS NULL))",
  "order_by": "s.constant_value DESC",
  "limit": 50
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
  "where": "(c.metal_id = metal_79 AND c.ligand_id IN (ligand_6356, ligand_6277, ligand_6342, ligand_8873) AND c.beta_definition_name = '[ML]/[M][L]')",
  "order_by": "s.constant_value DESC",
  "limit": 50
}
```

[summary]
## search_stability — 25 row(s)

### `La^[3+]` + Diethylenetrinitrilopentaacetic acid (DTPA) — 4 measurement(s)
metal_id: metal_79 | ligand_id: ligand_6356
ligand_HxL_def: H5L | ligand_SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_112571 | *** | beta_def_812 | ΔS | 298.7 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (-9.9, L, +inf) |
| vlm_112568 | ref_eq_map_6657 | beta_def_812 | logK | 19.49 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (-9.9, L, +inf) |
| vlm_112569 | ref_eq_map_6658 | beta_def_812 | logK | -18.23 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (-9.9, L, +inf) |
| vlm_112570 | *** | beta_def_812 | ΔH | -22.2 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (-9.9, L, +inf) |

### `La^[3+]` + Ethylenedinitrilotetraacetic acid (EDTA) — 9 measurement(s)
metal_id: metal_79 | ligand_id: ligand_6277
ligand_HxL_def: H4L | ligand_SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_108396 | *** | beta_def_812 | ΔS | 253.6 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108397 | *** | beta_def_812 | ΔS | 222.6 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108389 | ref_eq_map_4946 | beta_def_812 | logK | 15.36 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108390 | ref_eq_map_4947 | beta_def_812 | logK | 14.48 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108391 | *** | beta_def_812 | ΔH | -12.1 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108392 | *** | beta_def_812 | ΔH | -16.3 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108395 | *** | beta_def_812 | ΔH | -18.8 | 40 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108394 | *** | beta_def_812 | ΔH | -20.5 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108393 | *** | beta_def_812 | ΔH | -22.2 | 10 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |

### `La^[3+]` + Ethylenebis(oxyethylenenitrilo)tetraacetic acid (EGTA) — 4 measurement(s)
metal_id: metal_79 | ligand_id: ligand_6342
ligand_HxL_def: H4L | ligand_SMILES: O=C(O)CN(CCOCCOCCN(CC(=O)O)CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_112018 | *** | beta_def_812 | ΔS | 223 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.32, L, +inf) |
| vlm_112016 | ref_eq_map_6451 | beta_def_812 | logK | 15.74 | 20 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.32, L, +inf) |
| vlm_112015 | ref_eq_map_6450 | beta_def_812 | logK | 15.67 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.32, L, +inf) |
| vlm_112017 | *** | beta_def_812 | ΔH | -23 | 20 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.32, L, +inf) |

### `La^[3+]` + Propanedioic acid (Malonic acid) — 8 measurement(s)
metal_id: metal_79 | ligand_id: ligand_8873
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_152044 | *** | beta_def_812 | ΔS | 122.6 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (5.27, L, +inf) |
| vlm_152045 | *** | beta_def_812 | ΔS | 99.6 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (5.27, L, +inf) |
| vlm_152042 | *** | beta_def_812 | ΔH | 15.5 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (5.27, L, +inf) |
| vlm_152043 | *** | beta_def_812 | ΔH | 12.1 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (5.27, L, +inf) |
| vlm_152041 | ref_eq_map_20060 | beta_def_812 | logK | 4.94 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (5.27, L, +inf) |
| vlm_152039 | ref_eq_map_20059 | beta_def_812 | logK | 3.99 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (5.27, L, +inf) |
| vlm_152038 | ref_eq_map_20057 | beta_def_812 | logK | 3.69 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (5.27, L, +inf) |
| vlm_152040 | ref_eq_map_20058 | beta_def_812 | logK | 3.06 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (5.27, L, +inf) |

---

### Step 21: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_79 AND c.beta_definition_name = '[ML]/[M][L]')",
  "order_by": "s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability — 100 row(s)

### ΔS — 61 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_79 | La^[3+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1~0.5 | *** | 0 |
| metal_79 | La^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_79 | La^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_79 | La^[3+] | ligand_6267 | N-Methylethylenedinitrilotr… | H3L | CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_79 | La^[3+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_79 | La^[3+] | ligand_6309 | Ethylenedinitrilo-N,N'-di(3… | H4L | O=C(O)CCN(CCN(CCC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_79 | La^[3+] | ligand_10148 | Hydrogen sulfate ion (Sulfu… | HL | O=S(=O)([O-])O | 2 | 1 | 25 | 0~2 | *** | 0 |
| metal_79 | La^[3+] | ligand_8873 | Propanedioic acid (Malonic … | H2L | O=C(O)CC(=O)O | 2 | 1 | 25 | 0.1~1 | *** | 0 |
| metal_79 | La^[3+] | ligand_9593 | 5-Hydroxy-2-hydroxymethyl-4… | HL | O=c1cc(CO)occ1O | 2 | 1 | 25 | 0.1~2 | *** | 0 |
| metal_79 | La^[3+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6298 | trans-1,2-Cyclopentylenedin… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCC[C@H]1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6311 | Trimethylenedinitrilotetraa… | H4L | O=C(O)CN(CCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6335 | Oxybis(ethylenenitrilo)tetr… | H4L | O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6751 | 1,2-Phenylenedinitrilotetra… | H4L | O=C(O)CN(CC(=O)O)c1ccccc1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6348 | Thiobis(ethylenenitrilo)tet… | H4L | O=C(O)CN(CCSCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6342 | Ethylenebis(oxyethylenenitr… | H4L | O=C(O)CN(CCOCCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6362 | Diethylenetrinitrilopentaac… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6313 | Tetramethylenedinitrilotetr… | H4L | O=C(O)CN(CCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_9054 | Benzene-1,2,3-tricarboxylic… | H3L | O=C(O)c1cccc(C(=O)O)c1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8937 | trans-Cyclohexane-1,4-dicar… | H2L | O=C(O)[C@H]1CC[C@H](C(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_5975 | Ethylenediiminodiacetic aci… | H2L | O=C(O)CNCCNCC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8915 | cis-Butenedioic acid (Malei… | H2L | O=C(O)/C=C\C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6774 | Pyridine-2,6-dicarboxylic a… | H2L | O=C(O)c1cccc(C(=O)O)n1 | 1 | 1 | 25 | 0.5 | *** | 0 |
| metal_79 | La^[3+] | ligand_8986 | Ethylenebis(oxyacetic acid) | H2L | O=C(O)COCCOCC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8933 | Hexanedioic acid (Adipic ac… | H2L | O=C(O)CCCCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8921 | Pentanedioic acid (Glutaric… | H2L | O=C(O)CCCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8907 | Butanedioic acid (Succinic … | H2L | O=C(O)CCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8974 | Oxydiacetic acid (Diglycoli… | H2L | O=C(O)COCC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_79 | La^[3+] | ligand_9526 | Pentane-2,4-dione (Acetylac… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_10086 | Hexacyanocobaltate(III) ion | *** | *** | 1 | 1 | 25 | 0 | *** | 0 |
| metal_79 | La^[3+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 1 | 1 | 25 | 1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8939 | Benzene-1,3-dicarboxylic ac… | H2L | O=C(O)c1cccc(C(=O)O)c1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8917 | trans-Butenedioic acid (Fum… | H2L | O=C(O)/C=C/C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_10085 | Hexacyanoferrate(III) ion | *** | *** | 1 | 1 | 25 | 0 | *** | 0 |
| metal_79 | La^[3+] | ligand_9568 | 1-Hydroxycyclohepta-3,5,7-t… | HL | O=c1cccccc1O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8473 | 2-Methylpropanoic acid (Iso… | HL | CC(C)C(=O)O | 1 | 1 | 25 | 2 | *** | 0 |
| metal_79 | La^[3+] | ligand_9564 | Dihydroxycyclobutenedione (… | H2L | O=c1c(O)c(O)c1=O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6771 | Pyridine-2,3-dicarboxylic a… | H2L | O=C(O)c1cccnc1C(=O)O | 1 | 1 | 25 | 0.5 | *** | 0 |
| metal_79 | La^[3+] | ligand_9566 | Dihydroxycyclopentenetrione… | H2L | O=c1c(O)c(O)c(=O)c1=O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8521 | Phenylacetic acid | HL | O=C(O)Cc1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_9601 | L-3,4-Dihydroxy-5-(1,2-dihy… | H2L | O=C1O[C@H]([C@@H](O)CO)C(O)=C1O | 1 | 1 | 25 | 2 | *** | 0 |
| metal_79 | La^[3+] | ligand_8673 | 3-Hydroxypropanoic acid | HL | O=C(O)CCO | 1 | 1 | 25 | 2 | *** | 0 |
| metal_79 | La^[3+] | ligand_8467 | Propanoic acid (Propionic a… | HL | CCC(=O)O | 1 | 1 | 25 | 2 | *** | 0 |
| metal_79 | La^[3+] | ligand_8520 | Benzenecarboxylic acid (Ben… | HL | O=C(O)c1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8583 | 4-Fluorobenzoic acid | HL | O=C(O)c1ccc(F)cc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8760 | 4-Methoxybenzoic acid (p-An… | HL | COc1ccc(C(=O)O)cc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 1 | 1 | 25 | 2 | *** | 0 |
| metal_79 | La^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8759 | 3-Methoxybenzoic acid | HL | COc1cccc(C(=O)O)c1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8582 | 3-Fluorobenzoic acid | HL | O=C(O)c1cccc(F)c1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6762 | Pyridine-2-carboxylic acid … | HL | O=C(O)c1ccccn1 | 1 | 1 | 25 | 0.5 | *** | 0 |
| metal_79 | La^[3+] | ligand_8728 | Oxole-2-carboxylic acid (2-… | HL | O=C(O)c1ccco1 | 1 | 1 | 25 | 2 | *** | 0 |
| metal_79 | La^[3+] | ligand_8614 | 3-Nitrobenzoic acid | HL | O=C(O)c1cccc([N+](=O)[O-])c1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6760 | 1,4-Diazine-2-carboxylic ac… | HL | O=C(O)c1cnccn1 | 1 | 1 | 25 | 1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 1 | 1 | 25 | 2 | *** | 0 |
| metal_79 | La^[3+] | ligand_8641 | D-2-Hydroxypropanoic acid (… | HL | CC(O)C(=O)O | 1 | 1 | 25 | 2 | *** | 0 |
| metal_79 | La^[3+] | ligand_8659 | L-Phenyl(hydroxy)acetic aci… | HL | O=C(O)C(O)c1ccccc1 | 1 | 1 | 25 | 2 | *** | 0 |
| metal_79 | La^[3+] | ligand_10163 | Chloride ion | *** | *** | 1 | 1 | 25 | 1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8647 | 2-Hydroxy-2-methylpropanoic… | HL | CC(C)(O)C(=O)O | 1 | 1 | 25 | 2 | *** | 0 |

### logK — 22 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_79 | La^[3+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1~1 | *** | 2 |
| metal_79 | La^[3+] | ligand_6335 | Oxybis(ethylenenitrilo)tetr… | H4L | O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1 | *** | 2 |
| metal_79 | La^[3+] | ligand_6342 | Ethylenebis(oxyethylenenitr… | H4L | O=C(O)CN(CCOCCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1 | *** | 2 |
| metal_79 | La^[3+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6298 | trans-1,2-Cyclopentylenedin… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCC[C@H]1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6366 | Triethylenetetranitrilohexa… | H6L | O=C(O)CN(CCN(CCN(CC(=O)O)CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6102 | 1,4,7,10-Tetraazacyclododec… | H4L | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6116 | 1,4,7,10,13,16-Hexaazacyclo… | H6L | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6358 | Diethylenetrinitrilotetraac… | H5L | O=C(O)CCN(CCN(CCN(CC(=O)O)CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6104 | 1,4,7,10-Tetraazacyclotride… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_10114 | Hydrogen diphosphate (Pyrop… | H4L | O=P(O)(O)OP(=O)(O)O | 1 | 1 | 25 | 0 | *** | 1 |
| metal_79 | La^[3+] | ligand_6287 | rac-(1,2-Dimethylethylene)d… | H4L | CC(C(C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6279 | DL-(Ethylethylene)dinitrilo… | H4L | CCC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6280 | DL-(Propylethylene)dinitril… | H4L | CCCC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6282 | DL-(Butylethylene)dinitrilo… | H4L | CCCCC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6283 | DL-(2-Methylpropylethylene)… | H4L | CC(C)CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6284 | DL-(Hexylethylene)dinitrilo… | H4L | CCCCCCC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6037 | N,N'-Bis(2-hydroxybenzyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)Cc1ccccc1O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6281 | DL-(2-Propylethylene)dinitr… | H4L | CC(C)C(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6353 | N-Ethyliminobis(ethylenenit… | H4L | CCN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6289 | DL-(Phenylethylene)dinitril… | H4L | O=C(O)CN(CC(=O)O)CC(c1ccccc1)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |

### ΔH — 4 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_79 | La^[3+] | ligand_10148 | Hydrogen sulfate ion (Sulfu… | HL | O=S(=O)([O-])O | 2 | 1 | 25 | 0~2 | *** | 0 |
| metal_79 | La^[3+] | ligand_6311 | Trimethylenedinitrilotetraa… | H4L | O=C(O)CN(CCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8873 | Propanedioic acid (Malonic … | H2L | O=C(O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |

---

### Step 22: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_79 AND c.beta_definition_name = '[ML]/[M][L]' AND s.constant_type = 'logK' AND c.ligand_id IN (ligand_6301, ligand_6335, ligand_6342, ligand_6356, ligand_6277, ligand_6165))",
  "order_by": "s.constant_value DESC",
  "limit": 30
}
```

[summary]
## search_stability

*(no results)*

---
