# Q5.1.3 — Tool Results (batch 5)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "iron"
}
```

[summary]
## search_metals — 2 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_61 | Fe^[3+] | Fe | 3 | ✓ | [Fe+3] | InChI=1S/Fe/q+3 | beta_totN_128 | ligand_totN_406 | vlm_totN_1473 |
| metal_62 | Fe^[2+] | Fe | 2 | ✓ | [Fe+2] | InChI=1S/Fe/q+2 | beta_totN_57 | ligand_totN_217 | vlm_totN_667 |

---

### Step 3: `search_metals`
**Args:**
```json
{
  "name": "copper"
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

### Step 5: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_card",
  "group_column": "ligand_class_name",
  "where": "metal_id = 61",
  "limit": 10
}
```

[summary]
## db_distribution - ligandmetal_card by ligand_class_name

**total_rows:** 1473

| value | count | pct |
|-------|-------|-----|
| Inorganic ligands | 198 | 13.44% |
| Catechols | 140 | 9.5% |
| miscellaneous hydroxamic acids | 124 | 8.42% |
| Amino Acids | 116 | 7.88% |
| EDTA and derivatives | 106 | 7.2% |
| Aliphatic amines | 102 | 6.92% |
| Phenols salicylic acids | 99 | 6.72% |
| Phenols | 67 | 4.55% |
| Carboxylic acids | 61 | 4.14% |
| Pyridines (azines) | 49 | 3.33% |

---

### Step 6: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_card",
  "group_column": "ligand_class_name",
  "where": "metal_id = 62",
  "limit": 10
}
```

[summary]
## db_distribution - ligandmetal_card by ligand_class_name

**total_rows:** 667

| value | count | pct |
|-------|-------|-----|
| Amino Acids | 101 | 15.14% |
| EDTA and derivatives | 78 | 11.69% |
| Inorganic ligands | 75 | 11.24% |
| Phenanthrolines | 33 | 4.95% |
| Aminophosphorus acids | 31 | 4.65% |
| Bipyridines | 30 | 4.5% |
| NTA and derivatives | 29 | 4.35% |
| Pyridines (azines) | 28 | 4.2% |
| Pyridine carboxylic acids | 24 | 3.6% |
| Carboxylic acids polyacids | 23 | 3.45% |

---

### Step 7: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_card",
  "group_column": "ligand_class_name",
  "where": "metal_id = 41",
  "limit": 10
}
```

[summary]
## db_distribution - ligandmetal_card by ligand_class_name

**total_rows:** 8963

| value | count | pct |
|-------|-------|-----|
| Amino Acids | 1190 | 13.28% |
| Peptides | 862 | 9.62% |
| Aliphatic amines | 731 | 8.16% |
| Aliphatic amines secondary N | 558 | 6.23% |
| Aminophosphorus acids | 389 | 4.34% |
| Pyrroles (azoles) | 377 | 4.21% |
| polypeptides | 369 | 4.12% |
| Aza-macrocycles | 367 | 4.09% |
| Pyridines (azines) | 335 | 3.74% |
| Inorganic ligands | 324 | 3.61% |

---

### Step 8: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_card",
  "group_column": "ligand_class_name",
  "where": "metal_id = 42",
  "limit": 10
}
```

[summary]
## db_distribution - ligandmetal_card by ligand_class_name

**total_rows:** 285

| value | count | pct |
|-------|-------|-----|
| Inorganic ligands | 73 | 25.61% |
| miscellaneous ureas, hadrazides, amidines | 51 | 17.89% |
| Pyridines (azines) | 30 | 10.53% |
| miscellaneous alcohols and sugar | 11 | 3.86% |
| Carboxylic acids diacids S-Se-Te-P-As | 11 | 3.86% |
| Aza-thia-macrocycles | 11 | 3.86% |
| Aza-macrocycles | 11 | 3.86% |
| Carboxylic acids polyacids | 9 | 3.16% |
| Amino Acids | 9 | 3.16% |
| Aliphatic amines | 9 | 3.16% |

---

### Step 9: `db_ranked_pairs`
**Args:**
```json
{
  "rank_by": "measurements",
  "limit": 15,
  "where": "lc.metal_id = 61"
}
```

[summary]
**db_ranked_pairs:** Error - Unknown rank_by='measurements'. Choose from: ['ligands_per_metal', 'measurements_per_ligand', 'measurements_per_metal', 'metals_per_ligand', 'pka_per_ligand']

---

### Step 10: `db_ranked_pairs`
**Args:**
```json
{
  "rank_by": "measurements",
  "limit": 15,
  "where": "lc.metal_id = 62"
}
```

[summary]
**db_ranked_pairs:** Error - Unknown rank_by='measurements'. Choose from: ['ligands_per_metal', 'measurements_per_ligand', 'measurements_per_metal', 'metals_per_ligand', 'pka_per_ligand']

---

### Step 11: `db_ranked_pairs`
**Args:**
```json
{
  "rank_by": "measurements",
  "limit": 15,
  "where": "lc.metal_id = 41"
}
```

[summary]
**db_ranked_pairs:** Error - Unknown rank_by='measurements'. Choose from: ['ligands_per_metal', 'measurements_per_ligand', 'measurements_per_metal', 'metals_per_ligand', 'pka_per_ligand']

---

### Step 12: `db_ranked_pairs`
**Args:**
```json
{
  "rank_by": "measurements",
  "limit": 15,
  "where": "lc.metal_id = 42"
}
```

[summary]
**db_ranked_pairs:** Error - Unknown rank_by='measurements'. Choose from: ['ligands_per_metal', 'measurements_per_ligand', 'measurements_per_metal', 'metals_per_ligand', 'pka_per_ligand']

---

### Step 13: `search_ligands`
**Args:**
```json
{
  "name": "EDTA"
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 5 SQL matches · showing 5 · limit 25

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

### Step 14: `search_ligands`
**Args:**
```json
{
  "name": "glycine"
}
```

[summary]
## search_ligands — 25 result(s)

**stats:** 170 SQL matches · showing 25 · limit 25

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
| ligand_5948 | N-(2-Aminoethyl)glycine (Ethylenediamine m… (EDMA) | HL | Amino Acids | 30 | `NCCNCC(=O)O` | (-inf, H3L, -1.9, H2L, 6.67, HL, 9.84, L, +inf) |
| ligand_5949 | N-[Tris(hydroxymethyl)methyl]glycine (Tricine) | HL | Amino Acids | 10 | `O=C(O)CNC(CO)(CO)CO` | (-inf, H2L, 2.023, HL, 8.135, L, +inf) |
| ligand_5959 | 2-(Carboxymethylaminomethyl)azole-4-sulfonic acid… | H2L | Amino Acids | 9 | `O=C(O)CNCc1cc(S(=O)(=O)O)c[nH]1` | (-inf, H2L, 2.25, HL, 8.71, L, +inf) |
| ligand_5971 | N-Acetylglycyl-L-histidylglycine | HL | Amino Acids | 7 | `CC(=O)NCC(=O)N[C@@H](CC1C=NC=N1)C(=O)NCC(=O)O` | (-inf, H2L, 3.13, HL, 6.74, L, +inf) |
| ligand_5972 | N-Acetylglycyl(N(3)-benzyl-L-histidyl)glycine | HL | Amino Acids | 7 | `CC(=O)NCC(=O)NC(Cc1cncn1Cc1ccccc1)C(=O)NCC(=O)O` | (-inf, H2L, 3.18, HL, 6.25, L, +inf) |
| ligand_5974 | N-Acetylglycylglycyl-L-histidylglycine | HL | Amino Acids | 11 | `CC(=O)NCC(=O)NCC(=O)N[C@@H](CC1C=NC=N1)C(=O)NCC(=O)O` | (-inf, H2L, 3.17, HL, 6.78, L, +inf) |
| ligand_5997 | rac-Trimethylenebis[2-(2-hydroxy-3,5… (rac-TMPHPG) | *** | Amino Acids | 13 | *** | (-inf, H6L, 2.42, H5L, 2.49, H4L, 7.33, H3L, 8.94, H2L, 8.94, HL, -11.65, L, +inf) |
| ligand_5998 | meso-Trimethylenebis[2-(2-hydroxy-3… (meso-TMPHPG) | H4L | Amino Acids | 13 | `Cc1cc(C)c(O)c([C@H](NCCCN[C@@H](C(=O)O)c2cc(C)cc(C)c2O)C(=O)O)c1` | (-inf, H6L, -1.8, H5L, 2.29, H4L, 7.33, H3L, 9.14, H2L, 9.14, HL, -12.08, L, +inf) |
| ligand_6015 | N,N-Dimethylglycine | HL | Amino Acids | 25 | `CN(C)CC(=O)O` | (-inf, H2L, 2, HL, 9.77, L, +inf) |
| ligand_6016 | N,N-Diethylglycine | HL | Amino Acids | 5 | `CCN(CC)CC(=O)O` | (-inf, H2L, 2.04, HL, 10.47, L, +inf) |
| ligand_6017 | N,N-Pentamethyleneglyc… (Piperidine-N-acetic acid) | HL | Amino Acids | 6 | `O=C(O)CN1CCCCC1` | (-inf, H2L, 2.13, HL, 10.25, L, +inf) |
| ligand_6019 | N,N-Bis(phosphonomethyl)glycine | H5L | Amino Acids | 55 | `O=C(O)CN(CP(=O)(O)O)CP(=O)(O)O` | (-inf, H5L, -1.7, H4L, 2.1, H3L, 5.04, H2L, 6.4, HL, 6.4, L, +inf) |
| ligand_6021 | N,N-Bis(2-hydroxyethyl)glycine (Bicine) | HL | Amino Acids | 82 | `O=C(O)CN(CCO)CCO` | (-inf, H2L, -1.7, HL, 8.11, L, +inf) |
| ligand_6023 | N,N-Bis(2-hydroxypropyl)glycine | HL | Amino Acids | 14 | `CC(O)CN(CC(=O)O)CC(C)O` | (-inf, HL, 8.13, L, +inf) |
| ligand_6024 | N,N-Bis(3-oxo-3-(4-oxa-1-azacyclohexyl)propyl)gly… | HL | Amino Acids | 9 | `O=C(O)CN(CCC(=O)N1CCOCC1)CCC(=O)N1CCOCC1` | (-inf, H2L, -1.9, HL, 8.2, L, +inf) |

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

### Step 15: `search_ligands`
**Args:**
```json
{
  "name": "oxalate"
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 16: `search_ligands`
**Args:**
```json
{
  "name": "citrate"
}
```

[summary]
## search_ligands — 4 result(s)

**stats:** 4 SQL matches · showing 4 · limit 25

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

### Step 17: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_6277 AND c.metal_id IN (metal_61, metal_62, metal_41, metal_42))",
  "order_by": "c.metal_id, s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability — 20 row(s)

### `Cu^[2+]` + Ethylenedinitrilotetraacetic acid (EDTA) — 20 measurement(s)
metal_id: metal_41 | ligand_id: ligand_6277
ligand_HxL_def: H4L | ligand_SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_108611 | *** | beta_def_812 | ΔS | 244.8 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108615 | *** | beta_def_788 | ΔS | 31.4 | 25 | 0.1 | `[ML] + [H] <=> [MHL]` | *** |  |  |
| vlm_108604 | ref_eq_map_5019 | beta_def_812 | logK | 18.78 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108612 | ref_eq_map_5019 | beta_def_788 | logK | 3.1 | 25 | 0.1 | `[ML] + [H] <=> [MHL]` | *** |  |  |
| vlm_108613 | ref_eq_map_5020 | beta_def_788 | logK | 2.9 | 25 | 1 | `[ML] + [H] <=> [MHL]` | *** |  |  |
| vlm_108616 | ref_eq_map_5019 | beta_def_739 | logK | 2 | 25 | 0.1 | `[MHL] + [H] <=> [MH2L]` | *** |  |  |
| vlm_108620 | *** | beta_def_966 | ΔH | 0 | 20 | 0.1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |
| vlm_108617 | ref_eq_map_5020 | beta_def_739 | logK | -1.9 | 25 | 1 | `[MHL] + [H] <=> [MH2L]` | *** |  |  |
| vlm_108614 | *** | beta_def_788 | ΔH | -8.4 | 25 | 0.1 | `[ML] + [H] <=> [MHL]` | *** |  |  |
| vlm_108618 | ref_eq_map_5019 | beta_def_966 | logK | -11.4 | 25 | 0.1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |
| vlm_108619 | ref_eq_map_5020 | beta_def_966 | logK | -11.5 | 25 | 1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |
| vlm_108621 | *** | beta_def_966 | ΔH | -31 | 25 | 1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |
| vlm_108605 | *** | beta_def_812 | ΔH | -33.1 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108606 | *** | beta_def_812 | ΔH | -34.3 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108609 | *** | beta_def_812 | ΔH | -37.2 | 35 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108608 | *** | beta_def_812 | ΔH | -38.1 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108607 | *** | beta_def_812 | ΔH | -38.5 | 15 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108610 | *** | beta_def_812 | ΔH | -39.7 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108622 | *** | beta_def_966 | ΔS | -63.6 | 25 | 0.1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |
| vlm_108623 | *** | beta_def_966 | ΔS | -116.3 | 25 | 1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |

---

### Step 18: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_5760 AND c.metal_id IN (metal_61, metal_62, metal_41, metal_42))",
  "order_by": "c.metal_id, s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability — 20 row(s)

### `Cu^[2+]` + Aminoacetic acid (Glycine) — 20 measurement(s)
metal_id: metal_41 | ligand_id: ligand_5760
ligand_HxL_def: HL | ligand_SMILES: NCC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_93875 | *** | beta_def_840 | ΔS | 118 | 25 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.57, L, +inf) |
| vlm_93876 | *** | beta_def_840 | ΔS | 106.7 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.57, L, +inf) |
| vlm_93860 | *** | beta_def_812 | ΔS | 79.5 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.57, L, +inf) |
| vlm_93861 | *** | beta_def_812 | ΔS | 72.4 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.57, L, +inf) |
| vlm_93868 | ref_eq_map_92 | beta_def_840 | logK | 16.3 | 10 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.57, L, +inf) |
| vlm_93869 | ref_eq_map_93 | beta_def_840 | logK | 15.7 | 25 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.57, L, +inf) |
| vlm_93866 | ref_eq_map_90 | beta_def_840 | logK | 15.4 | 25 | 2 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.57, L, +inf) |
| vlm_93867 | ref_eq_map_91 | beta_def_840 | logK | 15.4 | 25 | 2.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.57, L, +inf) |
| vlm_93870 | ref_eq_map_94 | beta_def_840 | logK | 15.3 | 40 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.57, L, +inf) |
| vlm_93862 | ref_eq_map_86 | beta_def_840 | logK | 15.1 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.57, L, +inf) |
| vlm_93865 | ref_eq_map_89 | beta_def_840 | logK | 15.1 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.57, L, +inf) |
| vlm_93864 | ref_eq_map_88 | beta_def_840 | logK | 15 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.57, L, +inf) |
| vlm_93863 | ref_eq_map_87 | beta_def_840 | logK | 14.69 | 37 | 0.15 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.57, L, +inf) |
| vlm_93853 | ref_eq_map_92 | beta_def_812 | logK | 8.8 | 10 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.57, L, +inf) |
| vlm_93854 | ref_eq_map_93 | beta_def_812 | logK | 8.56 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.57, L, +inf) |
| vlm_93851 | ref_eq_map_90 | beta_def_812 | logK | 8.38 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.57, L, +inf) |
| vlm_93855 | ref_eq_map_94 | beta_def_812 | logK | 8.37 | 40 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.57, L, +inf) |
| vlm_93852 | ref_eq_map_91 | beta_def_812 | logK | 8.34 | 25 | 2.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.57, L, +inf) |
| vlm_93850 | ref_eq_map_89 | beta_def_812 | logK | 8.2 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.57, L, +inf) |
| vlm_93847 | ref_eq_map_86 | beta_def_812 | logK | 8.19 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.57, L, +inf) |

---
