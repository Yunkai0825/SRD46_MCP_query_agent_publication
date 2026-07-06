# Q5.1.1 — Tool Results (batch 5)

### Step 2: `search_metals`
**Args:**
```json
{
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

### Step 4: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71)",
  "order_by": "s.constant_value DESC",
  "limit": 12
}
```

[summary]
## search_stability — 12 row(s)

### ΔS — 9 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_71 | Hg^[2+] | ligand_10076 | Hydroxide ion | *** | *** | 2 | 1 | 25 | 1~3 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6335 | Oxybis(ethylenenitrilo)tetr… | H4L | O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_10147 | Hydrogen sulfite (Sulfurous… | H2L | O=[SH](=O)O | 1 | 1 | 25 | 0.5 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6751 | 1,2-Phenylenedinitrilotetra… | H4L | O=C(O)CN(CC(=O)O)c1ccccc1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6316 | Octamethylenedinitrilotetra… | H4L | O=C(O)CN(CCCCCCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6348 | Thiobis(ethylenenitrilo)tet… | H4L | O=C(O)CN(CCSCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |

### ΔH — 1 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_71 | Hg^[2+] | ligand_10171 | Iodide ion | *** | *** | 1 | 1 | 25 | 0.5 | solid | 0 |

---

### Step 5: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_72)",
  "order_by": "s.constant_value DESC",
  "limit": 8
}
```

[summary]
## search_stability — 8 row(s)

### `Hg^[+]` + Hydrogen azide (Hydrazoic acid) — 2 measurement(s)
metal_id: metal_72 | ligand_id: ligand_10106
ligand_HxL_def: HL | ligand_SMILES: [N-]=[N+]=N

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_173658 | *** | beta_def_458 | ΔS | 245.2 | 25 | 0 | `[M2L2(s)] <=> [M]^2 + [L]^2` | solid | [L] | (4.45, L, +inf) |
| vlm_173657 | *** | beta_def_458 | ΔH | 125.1 | 25 | 0 | `[M2L2(s)] <=> [M]^2 + [L]^2` | solid | [L] | (4.45, L, +inf) |

### `Hg^[+]` + cis-syn-cis-2,5,8,15,18,21-Hexaoxatricyclo[20.4.0.0(9,14)]h… — 2 measurement(s)
metal_id: metal_72 | ligand_id: ligand_9677
ligand_HxL_def: *** | ligand_SMILES: ***

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_167594 | *** | beta_def_840 | ΔS | 114.2 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_167593 | *** | beta_def_840 | ΔH | 16.3 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |

### `Hg^[+]` + Hydroxide ion — 1 measurement(s)
metal_id: metal_72 | ligand_id: ligand_10076
ligand_HxL_def: *** | ligand_SMILES: ***

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_170889 | ref_eq_map_27426 | beta_def_692 | logK | 48.24 | 25 | 3 | `[M]^5 + [L]^4 <=> [M5L4]` | *** | [L] | (13.78, L, +inf) |

### `Hg^[+]` + Hydrogen diphosphate (Pyrophosphoric acid) — 1 measurement(s)
metal_id: metal_72 | ligand_id: ligand_10114
ligand_HxL_def: H4L | ligand_SMILES: O=P(O)(O)OP(=O)(O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_174741 | ref_eq_map_28673 | beta_def_978 | logK | 15.64 | 27 | 0.7 | `[M] + [L] + [OH] <=> [M(OH)L]` | *** | [L] | (8.25, L, +inf) |

### `Hg^[+]` + Hydrogen triphosphate (Triphosphoric acid) — 1 measurement(s)
metal_id: metal_72 | ligand_id: ligand_10117
ligand_HxL_def: H5L | ligand_SMILES: O=P(O)(O)OP(=O)(O)OP(=O)(O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_174959 | ref_eq_map_28744 | beta_def_978 | logK | 15 | 27 | 0.7 | `[M] + [L] + [OH] <=> [M(OH)L]` | *** | [L] | (7.77, L, +inf) |

### `Hg^[+]` + Propane-2,2-dicarboxylic acid (Dimethylmalonic acid) — 1 measurement(s)
metal_id: metal_72 | ligand_id: ligand_8887
ligand_HxL_def: H2L | ligand_SMILES: CC(C)(C(=O)O)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_152897 | ref_eq_map_20340 | beta_def_978 | logK | 13.58 | 27 | 0.7 | `[M] + [L] + [OH] <=> [M(OH)L]` | *** | [L] | (5.68, L, +inf) |

---

### Step 6: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_93)",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[summary]
## search_stability — 10 row(s)

### `MeHg^[+]` + Hydroxide ion — 1 measurement(s)
metal_id: metal_93 | ligand_id: ligand_10076
ligand_HxL_def: *** | ligand_SMILES: ***

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_170893 | *** | beta_def_812 | ΔS | 58.6 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (13.78, L, +inf) |

### `MeHg^[+]` + Hydrogen thiosulfate (Thiosulfuric acid) — 1 measurement(s)
metal_id: metal_93 | ligand_id: ligand_10149
ligand_HxL_def: H2L | ligand_SMILES: O=S(O)(O)=S

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_176274 | *** | beta_def_812 | ΔS | 41.4 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.3, L, +inf) |

### `MeHg^[+]` + 2,3-Dimercaptopropanol (BAL) — 2 measurement(s)
metal_id: metal_93 | ligand_id: ligand_9759
ligand_HxL_def: H2L | ligand_SMILES: OCC(S)CS

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_168081 | ref_eq_map_26361 | beta_def_840 | logK | 30.02 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (10.65, L, +inf) |
| vlm_168080 | ref_eq_map_26361 | beta_def_812 | logK | 19.56 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (10.65, L, +inf) |

### `MeHg^[+]` + 2-Mercaptoethanol — 2 measurement(s)
metal_id: metal_93 | ligand_id: ligand_9747
ligand_HxL_def: HL | ligand_SMILES: OCCS

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_167952 | *** | beta_def_812 | ΔS | 26.4 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.4, L, +inf) |
| vlm_167953 | ref_eq_map_26320 | beta_def_502 | logK | 22.39 | 20 | 0.1 | `[M]^2 + [L] <=> [M2L]` | *** | [L] | (9.4, L, +inf) |

### `MeHg^[+]` + DL-Mercaptobutanedioic acid (Thiomalic acid) — 1 measurement(s)
metal_id: metal_93 | ligand_id: ligand_8995
ligand_HxL_def: H3L | ligand_SMILES: O=C(O)CC(S)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_156094 | ref_eq_map_21518 | beta_def_812 | logK | 17.2 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (10.38, L, +inf) |

### `MeHg^[+]` + erythro-1,4-Dimercaptobutane-2,3-diol (Dithioerythritol) — 1 measurement(s)
metal_id: metal_93 | ligand_id: ligand_9761
ligand_HxL_def: H2L | ligand_SMILES: OC(CS)C(O)CS

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_168110 | ref_eq_map_26371 | beta_def_812 | logK | 17 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.99, L, +inf) |

### `MeHg^[+]` + Mercaptoacetic acid (Thioglycolic acid) — 1 measurement(s)
metal_id: metal_93 | ligand_id: ligand_8766
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)CS

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_150610 | ref_eq_map_19476 | beta_def_812 | logK | 16.9 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (10.11, L, +inf) |

### `MeHg^[+]` + D-2-Amino-3-mercapto-3-methylbutanoic acid (Penicillamine) — 1 measurement(s)
metal_id: metal_93 | ligand_id: ligand_5857
ligand_HxL_def: H2L | ligand_SMILES: CC(C)(S)[C@H](N)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_97584 | ref_eq_map_1044 | beta_def_812 | logK | 16.8 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (10.67, L, +inf) |

---

### Step 7: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_53)",
  "order_by": "s.constant_value DESC",
  "limit": 8
}
```

[summary]
## search_stability — 6 row(s)

### `EtHg^[+]` + Chloride ion — 1 measurement(s)
metal_id: metal_53 | ligand_id: ligand_10163
ligand_HxL_def: *** | ligand_SMILES: ***

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_177475 | ref_eq_map_29766 | beta_def_812 | logK | 5.32 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] |  |

### `EtHg^[+]` + Iodide ion — 3 measurement(s)
metal_id: metal_53 | ligand_id: ligand_10171
ligand_HxL_def: *** | ligand_SMILES: ***

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_178460 | ref_eq_map_30072 | beta_def_888 | logK | 0.75 | 25 | 1 | `[ML2] + [L] <=> [ML3]` | *** | [L] |  |
| vlm_178459 | ref_eq_map_30072 | beta_def_868 | logK | -0.67 | 25 | 1 | `[ML] + [L] <=> [ML2]` | *** | [L] |  |
| vlm_178461 | ref_eq_map_30072 | beta_def_311 | logK | -4.11 | 25 | 1 | `[ML(s)] <=> [M] + [L]` | solid | [L] |  |

### `EtHg^[+]` + Hydrogen thiocyanate (Thiocyanic acid) — 2 measurement(s)
metal_id: metal_53 | ligand_id: ligand_10092
ligand_HxL_def: HL | ligand_SMILES: N=C=S

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_172363 | ref_eq_map_27875 | beta_def_888 | logK | 0.2 | 25 | 1 | `[ML2] + [L] <=> [ML3]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172362 | ref_eq_map_27875 | beta_def_868 | logK | -0.1 | 25 | 1 | `[ML] + [L] <=> [ML2]` | *** | [L] | (-1.1, L, +inf) |

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_136)",
  "order_by": "s.constant_value DESC",
  "limit": 8
}
```

[summary]
## search_stability — 8 row(s)

### `PhHg^[+]` + Hydroxide ion — 1 measurement(s)
metal_id: metal_136 | ligand_id: ligand_10076
ligand_HxL_def: *** | ligand_SMILES: ***

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_170897 | ref_eq_map_27430 | beta_def_812 | logK | 9.75 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (13.78, L, +inf) |

### `PhHg^[+]` + 8-Hydroxyquinoline-5-sulfonic acid (Sulfoxine) — 1 measurement(s)
metal_id: metal_136 | ligand_id: ligand_8134
ligand_HxL_def: H2L | ligand_SMILES: O=S(=O)(O)c1ccc(O)c2ncccc12

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_138188 | ref_eq_map_14806 | beta_def_812 | logK | 8.9 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (8.37, L, +inf) |

### `PhHg^[+]` + Iodide ion — 1 measurement(s)
metal_id: metal_136 | ligand_id: ligand_10171
ligand_HxL_def: *** | ligand_SMILES: ***

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_178462 | ref_eq_map_30073 | beta_def_812 | logK | 8.82 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] |  |

### `PhHg^[+]` + 8-Hydroxy-7-iodoquinoline-5-sulfonic acid (Ferron) — 1 measurement(s)
metal_id: metal_136 | ligand_id: ligand_8136
ligand_HxL_def: H2L | ligand_SMILES: O=S(=O)(O)c1cc(I)c(O)c2ncccc12

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_138284 | ref_eq_map_14833 | beta_def_812 | logK | 8.7 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (7.06, L, +inf) |

### `PhHg^[+]` + Hydrogen thiocyanate (Thiocyanic acid) — 1 measurement(s)
metal_id: metal_136 | ligand_id: ligand_10092
ligand_HxL_def: HL | ligand_SMILES: N=C=S

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_172364 | ref_eq_map_27876 | beta_def_812 | logK | 6.66 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |

### `PhHg^[+]` + Bromide ion — 1 measurement(s)
metal_id: metal_136 | ligand_id: ligand_10168
ligand_HxL_def: *** | ligand_SMILES: ***

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_178050 | ref_eq_map_29961 | beta_def_812 | logK | 6.62 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] |  |

### `PhHg^[+]` + Quinoline-2-carboxylic acid (Quinaldic acid) — 1 measurement(s)
metal_id: metal_136 | ligand_id: ligand_6764
ligand_HxL_def: HL | ligand_SMILES: O=C(O)c1ccc2ccccc2n1

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_119027 | ref_eq_map_8412 | beta_def_840 | logK | 6.35 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (4.77, L, +inf) |

### `PhHg^[+]` + Chloride ion — 1 measurement(s)
metal_id: metal_136 | ligand_id: ligand_10163
ligand_HxL_def: *** | ligand_SMILES: ***

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_177476 | ref_eq_map_29767 | beta_def_812 | logK | 5.77 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] |  |

---

### Step 9: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.ligand_name LIKE '%chlor%')",
  "order_by": "n.node_count DESC",
  "limit": 3
}
```

[summary]
## search_networks — 5 row(s)

> **Reference equilibrium networks** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### `Hg^[2+]` + 2-[Bis(carboxymethyl)aminoethyl]trimethylammonium (perchlor… — 1 network(s)
metal_id: metal_71 | ligand_id: ligand_6255 | ligand_def_HxL: H2L | ligand_SMILES: C[N+](C)(C)CCN(CC(=O)O)CC(=O)O

| beta_def | equation |
|----------|----------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_4712 | 2 | 1 | 20~30 | -0.05~0.25 | 2 | beta_def_840; beta_def_812 | logK | -5~-2.77 |

#### Reference-state network: ref_eq_net_4712 (2 nodes)
> First network — reference conditions (T 20~30 °C, I -0.05~0.25 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` | logK | -5 |
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | -2.77 |

### `Hg^[2+]` + Chloroacetic acid — 1 network(s)
metal_id: metal_71 | ligand_id: ligand_8558 | ligand_def_HxL: HL | ligand_SMILES: O=C(O)CCl

| beta_def | equation |
|----------|----------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_17827 | 2 | 1 | 16.5~31.5 | 2.775~3.225 | 2 | beta_def_812; beta_def_840 | logK | 2.95~5.61 |

#### Reference-state network: ref_eq_net_17827 (2 nodes)
> First network — reference conditions (T 16.5~31.5 °C, I 2.775~3.225 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 2.95 |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` | logK | 5.61 |

### `Hg^[2+]` + Trichloroacetic acid — 1 network(s)
metal_id: metal_71 | ligand_id: ligand_8560 | ligand_def_HxL: HL | ligand_SMILES: O=C(O)C(Cl)(Cl)Cl

| beta_def | equation |
|----------|----------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_17845 | 1 | 0 | 20~30 | -0.05~0.25 | 1 | beta_def_812 | logK | 3.08 |

#### Reference-state network: ref_eq_net_17845 (1 nodes)
> First network — reference conditions (T 20~30 °C, I -0.05~0.25 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 3.08 |

---

### Step 10: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.ligand_name LIKE '%hydrox%')",
  "order_by": "n.node_count DESC",
  "limit": 3
}
```

[summary]
## search_networks — 6 row(s)

> **Reference equilibrium networks** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### `Hg^[2+]` + 2-Hydroxy-1,3-propylenediiminodibutanedioic acid (rac- or m… — 1 network(s)
metal_id: metal_71 | ligand_id: ligand_6002 | ligand_def_HxL: H4L | ligand_SMILES: O=C(O)CC(NCC(O)CNC(CC(=O)O)C(=O)O)C(=O)O

| beta_def | equation |
|----------|----------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` |
| beta_def_981 | ``[ML] + [OH] <=> [M(OH)L]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_2161 | 3 | 3 | 20~30 | -0.05~0.25 | 3 | beta_def_788; beta_def_981; beta_def_812 | logK | 5.2~17.73 |

#### Reference-state network: ref_eq_net_2161 (3 nodes)
> First network — reference conditions (T 20~30 °C, I -0.05~0.25 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` | logK | 5.2 |
| beta_def_981 | ``[ML] + [OH] <=> [M(OH)L]`` | logK | 7.4 |
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 17.73 |

### `Hg^[2+]` + 2-Hydroxy-1,3-propylenediiminodipropanedioic acid — 1 network(s)
metal_id: metal_71 | ligand_id: ligand_6001 | ligand_def_HxL: H4L | ligand_SMILES: O=C(O)C(NCC(O)CNC(C(=O)O)C(=O)O)C(=O)O

| beta_def | equation |
|----------|----------|
| beta_def_981 | ``[ML] + [OH] <=> [M(OH)L]`` |
| beta_def_812 | ``[M] + [L] <=> [ML]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_2138 | 2 | 1 | 20~30 | -0.05~0.25 | 2 | beta_def_981; beta_def_812 | logK | 7.2~19.3 |

#### Reference-state network: ref_eq_net_2138 (2 nodes)
> First network — reference conditions (T 20~30 °C, I -0.05~0.25 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_981 | ``[ML] + [OH] <=> [M(OH)L]`` | logK | 7.2 |
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 19.3 |

### `Hg^[2+]` + 5'-Bis(carboxymethyl)aminomethyl-3,3'-dimethyl-4'-hydroxyfu… — 1 network(s)
metal_id: metal_71 | ligand_id: ligand_6201 | ligand_def_HxL: H4L | ligand_SMILES: CC1=C/C(=C(\c2cc(C)c(O)c(CN(CC(=O)O)CC(=O)O)c2)c2ccccc2S(=O)(=O)O)C=CC1=O

| beta_def | equation |
|----------|----------|
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_4214 | 1 | 0 | 20~30 | -0.05~0.25 | 1 | beta_def_788 | logK | 6.8 |

#### Reference-state network: ref_eq_net_4214 (1 nodes)
> First network — reference conditions (T 20~30 °C, I -0.05~0.25 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` | logK | 6.8 |

---

### Step 11: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id = metal_72 AND c.ligand_name LIKE '%chlor%')",
  "order_by": "n.node_count DESC",
  "limit": 3
}
```

[summary]
## search_networks — 4 row(s)

> **Reference equilibrium networks** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### `Hg^[+]` + Chloroacetic acid — 1 network(s)
metal_id: metal_72 | ligand_id: ligand_8558 | ligand_def_HxL: HL | ligand_SMILES: O=C(O)CCl

| beta_def | equation |
|----------|----------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_17820 | 2 | 1 | 16.5~31.5 | 2.775~3.225 | 2 | beta_def_812; beta_def_840 | logK | 2.4~4.4 |

#### Reference-state network: ref_eq_net_17820 (2 nodes)
> First network — reference conditions (T 16.5~31.5 °C, I 2.775~3.225 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 2.4 |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` | logK | 4.4 |

### `Hg^[+]` + Chloride ion — 2 network(s)
metal_id: metal_72 | ligand_id: ligand_10163 | ligand_def_HxL: *** | ligand_SMILES: ***

| beta_def | equation |
|----------|----------|
| beta_def_458 | ``[M2L2(s)] <=> [M]^2 + [L]^2`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_29879 | 1 | 0 | 20~30 | -0.05~0.25 | 1 | beta_def_458 | logK | -17.91 |
| ref_eq_net_29880 | 1 | 0 | 19~29 | 0.35~0.65 | 1 | beta_def_458 | logK | -16.88 |

#### Reference-state network: ref_eq_net_29879 (1 nodes)
> First network — reference conditions (T 20~30 °C, I -0.05~0.25 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_458 | ``[M2L2(s)] <=> [M]^2 + [L]^2`` | logK | -17.91 |

---
