# Q5.2.2 — Tool Results (batch 5)

### Step 2: `search_ligands`
**Args:**
```json
{
  "name": "transferrin",
  "limit": 10
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "lactoferrin",
  "limit": 10
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
  "name": "albumin",
  "limit": 10
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 5: `search_ligands`
**Args:**
```json
{
  "name": "metallothionein",
  "limit": 10
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
  "name": "ovotransferrin",
  "limit": 10
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 8: `db_distribution`
**Args:**
```json
{
  "table": "ligand_card",
  "group_column": "ligand_class_name",
  "limit": 40
}
```

[summary]
## db_distribution - ligand_card by ligand_class_name

**total_rows:** 5750

| value | count | pct |
|-------|-------|-----|
| Ligands not selected | 1339 | 23.29% |
| Amino Acids | 297 | 5.17% |
| Aliphatic amines | 250 | 4.35% |
| Pyridines (azines) | 248 | 4.31% |
| Carboxylic acids | 182 | 3.17% |
| Aza-macrocycles | 165 | 2.87% |
| Peptides | 157 | 2.73% |
| Aliphatic amines secondary N | 139 | 2.42% |
| Pyrroles (azoles) | 134 | 2.33% |
| Aminophosphorus acids | 132 | 2.3% |
| EDTA and derivatives | 115 | 2.0% |
| Aza-oxa-macrocycles | 112 | 1.95% |
| Carboxylic acids diacids | 103 | 1.79% |
| Inorganic ligands | 101 | 1.76% |
| Naphtols | 100 | 1.74% |
| polypeptides | 98 | 1.7% |
| Organophosphorus and arsenic acids | 95 | 1.65% |
| Aliphatic amines tertiary N | 95 | 1.65% |
| Phenols | 92 | 1.6% |
| NTA and derivatives | 91 | 1.58% |
| miscellaneous hydrocarbons | 84 | 1.46% |
| miscellaneous hydroxamic acids | 74 | 1.29% |
| Aniline | 72 | 1.25% |
| Carboxylic acids thio | 71 | 1.23% |
| miscellaneous ureas, hadrazides, amidines | 70 | 1.22% |
| Aza macrocycles with carboxylic acids | 70 | 1.22% |
| miscellaneous alcohols and sugar | 68 | 1.18% |
| tripeptides | 66 | 1.15% |
| Catechols | 66 | 1.15% |
| Aniline carboxylic acids | 66 | 1.15% |
| Aza-oxo-macrocycles | 58 | 1.01% |
| cyclic ketones | 57 | 0.99% |
| miscellaneous amides | 54 | 0.94% |
| Carboxylic acids diacids S-Se-Te-P-As | 53 | 0.92% |
| Purines | 52 | 0.9% |
| Carboxylic acids hydroxy | 52 | 0.9% |
| Cyclic amines  | 51 | 0.89% |
| Phenols salicylic acids | 49 | 0.85% |
| Carboxylic acids polyacids | 49 | 0.85% |
| miscellaneous mercaptans | 46 | 0.8% |

---

### Step 9: `search_ligands`
**Args:**
```json
{
  "name": "desferrioxamine",
  "limit": 10
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_9910 | Desferriferrioxamin B | H3L | miscellaneous hydroxamic… | 53 | `CC(=O)N(O)CCCCCNC(=O)CCC(=O)N(O)CCCCCNC(=O)CCC(=O)N(O)CCCCCN` | (-inf, H4L, 8.32, H3L, 8.96, H2L, 9.55, HL, 10.79, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| amide | 1 | 100% |
| hydroxyl | 1 | 100% |
| primary_amine | 1 | 100% |

---

### Step 10: `search_ligands`
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

### Step 11: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_5898 AND c.metal_name_SRD LIKE '%iron%')",
  "order_by": "s.constant_value DESC",
  "limit": 8
}
```

[summary]
## search_stability

*(no results)*

---

### Step 12: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_9910)",
  "order_by": "s.constant_value DESC",
  "limit": 8
}
```

[summary]
## search_stability — 8 row(s)

### `Fe^[3+]` + Desferriferrioxamin B — 2 measurement(s)
metal_id: metal_61 | ligand_id: ligand_9910
ligand_HxL_def: H3L | ligand_SMILES: CC(=O)N(O)CCCCCNC(=O)CCC(=O)N(O)CCCCCNC(=O)CCC(=O)N(O)CCCCCN

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_168817 | ref_eq_map_26690 | beta_def_779 | logK | 30.7 | 25 | 0.1 | `[M] + [HL] <=> [MHL]` | *** | [HL] | (9.55, HL, 10.79) |
| vlm_168818 | ref_eq_map_26691 | beta_def_779 | logK | 30.6 | 20 | 0.1 | `[M] + [HL] <=> [MHL]` | *** | [HL] | (9.55, HL, 10.79) |

### `Ga^[3+]` + Desferriferrioxamin B — 2 measurement(s)
metal_id: metal_64 | ligand_id: ligand_9910
ligand_HxL_def: H3L | ligand_SMILES: CC(=O)N(O)CCCCCNC(=O)CCC(=O)N(O)CCCCCNC(=O)CCC(=O)N(O)CCCCCN

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_168830 | ref_eq_map_26695 | beta_def_779 | logK | 28.17 | 25 | 0.1 | `[M] + [HL] <=> [MHL]` | *** | [HL] | (9.55, HL, 10.79) |
| vlm_168831 | ref_eq_map_26696 | beta_def_779 | logK | 27.56 | 25 | 1 | `[M] + [HL] <=> [MHL]` | *** | [HL] | (9.55, HL, 10.79) |

### `Al^[3+]` + Desferriferrioxamin B — 1 measurement(s)
metal_id: metal_5 | ligand_id: ligand_9910
ligand_HxL_def: H3L | ligand_SMILES: CC(=O)N(O)CCCCCNC(=O)CCC(=O)N(O)CCCCCNC(=O)CCC(=O)N(O)CCCCCN

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_168827 | ref_eq_map_26694 | beta_def_779 | logK | 24.14 | 25 | 0.1 | `[M] + [HL] <=> [MHL]` | *** | [HL] | (9.55, HL, 10.79) |

### `In^[3+]` + Desferriferrioxamin B — 1 measurement(s)
metal_id: metal_74 | ligand_id: ligand_9910
ligand_HxL_def: H3L | ligand_SMILES: CC(=O)N(O)CCCCCNC(=O)CCC(=O)N(O)CCCCCNC(=O)CCC(=O)N(O)CCCCCN

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_168836 | ref_eq_map_26697 | beta_def_779 | logK | 20.6 | 25 | 0.1 | `[M] + [HL] <=> [MHL]` | *** | [HL] | (9.55, HL, 10.79) |

### `Yb^[3+]` + Desferriferrioxamin B — 1 measurement(s)
metal_id: metal_206 | ligand_id: ligand_9910
ligand_HxL_def: H3L | ligand_SMILES: CC(=O)N(O)CCCCCNC(=O)CCC(=O)N(O)CCCCCNC(=O)CCC(=O)N(O)CCCCCN

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_168803 | ref_eq_map_26685 | beta_def_779 | logK | 16 | 20 | 0.1 | `[M] + [HL] <=> [MHL]` | *** | [HL] | (9.55, HL, 10.79) |

### `Cu^[2+]` + Desferriferrioxamin B — 1 measurement(s)
metal_id: metal_41 | ligand_id: ligand_9910
ligand_HxL_def: H3L | ligand_SMILES: CC(=O)N(O)CCCCCNC(=O)CCC(=O)N(O)CCCCCNC(=O)CCC(=O)N(O)CCCCCN

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_168814 | ref_eq_map_26689 | beta_def_779 | logK | 14.12 | 20 | 0.1 | `[M] + [HL] <=> [MHL]` | *** | [HL] | (9.55, HL, 10.79) |

---

### Step 13: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_name_SRD LIKE '%cysteine%' AND c.metal_name_SRD LIKE '%copper%')",
  "order_by": "s.constant_value DESC",
  "limit": 6
}
```

[summary]
## search_stability — 6 row(s)

### `Cu^[2+]` + L-2-Amino-3-hydroxypropanoic acid (Serine) — 2 measurement(s)
metal_id: metal_41 | ligand_id: ligand_5828
ligand_HxL_def: HL | ligand_SMILES: N[C@@H](CO)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_96603 | *** | beta_def_249 | ΔS | 153.1 | 25 | 0.1 | `[M(OH)2L2] + [H] <=> [M(OH)L2] + [H2O]` | *** |  |  |
| vlm_96593 | *** | beta_def_840 | ΔS | 113.4 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.05, L, +inf) |

### `Cu^[2+]` + L-Aminobutanedioic acid (Aspartic acid) — 1 measurement(s)
metal_id: metal_41 | ligand_id: ligand_5802
ligand_HxL_def: H2L | ligand_SMILES: N[C@@H](CC(=O)O)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_95672 | *** | beta_def_840 | ΔS | 130.1 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.66, L, +inf) |

### `Ni^[2+]` + L-Aminobutanedioic acid (Aspartic acid) — 1 measurement(s)
metal_id: metal_112 | ligand_id: ligand_5802
ligand_HxL_def: H2L | ligand_SMILES: N[C@@H](CC(=O)O)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_95657 | *** | beta_def_840 | ΔS | 124.3 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.66, L, +inf) |

### `Th^[4+]` + L-Aminobutanedioic acid (Aspartic acid) — 1 measurement(s)
metal_id: metal_185 | ligand_id: ligand_5802
ligand_HxL_def: H2L | ligand_SMILES: N[C@@H](CC(=O)O)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_95630 | *** | beta_def_779 | ΔS | 117.2 | 25 | 1 | `[M] + [HL] <=> [MHL]` | *** | [HL] | (3.71, HL, 9.66) |

### `UO_[2]^[2+]` + L-Aminobutanedioic acid (Aspartic acid) — 1 measurement(s)
metal_id: metal_195 | ligand_id: ligand_5802
ligand_HxL_def: H2L | ligand_SMILES: N[C@@H](CC(=O)O)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_95638 | *** | beta_def_194 | ΔS | 114.6 | 25 | 1 | `[M] + [HL]^2 <=> [M(HL)2]` | *** | [HL] | (3.71, HL, 9.66) |

---
