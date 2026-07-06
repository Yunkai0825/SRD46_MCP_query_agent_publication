# Q5.1.4 — Tool Results (batch 3)

### Step 2: `search_metals`
**Args:**
```json
{
  "symbol": "Zn"
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_208 | Zn^[2+] | Zn | 2 | ✓ | [Zn+2] | InChI=1S/Zn/q+2 | beta_totN_122 | ligand_totN_1169 | vlm_totN_4095 |

---

### Step 4: `db_ranked_pairs`
**Args:**
```json
{
  "rank_by": "vlm_count",
  "limit": 10,
  "where": "lc.metal_id = metal_208"
}
```

[summary]
**db_ranked_pairs:** Error - Unknown rank_by='vlm_count'. Choose from: ['ligands_per_metal', 'measurements_per_ligand', 'measurements_per_metal', 'metals_per_ligand', 'pka_per_ligand']

---

### Step 5: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208)",
  "order_by": "n.node_count DESC",
  "limit": 3
}
```

[summary]
## search_networks — 10 row(s)

> **Reference equilibrium networks** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### `Zn^[2+]` + Aminoacetic acid (Glycine) — 3 network(s)
metal_id: metal_208 | ligand_id: ligand_5760 | ligand_def_HxL: HL | ligand_SMILES: NCC(=O)O

| beta_def | equation |
|----------|----------|
| beta_def_966 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_872 | ``[M] + [L]^3 <=> [ML3]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_113 | 4 | 4 | 31~41 | 0~0.3 | 4 | 4 diff beta_def | logK | 4.87~11.3 |
| ref_eq_net_112 | 3 | 3 | 20~30 | -0.05~0.25 | 3 | beta_def_812; beta_def_840; beta_def_872 | logK | 4.96~11.6 |
| ref_eq_net_114 | 3 | 3 | 19~29 | 0.35~0.65 | 3 | beta_def_812; beta_def_840; beta_def_872 | logK | 4.85~11.5 |

#### Reference-state network: ref_eq_net_113 (4 nodes)
> First network — reference conditions (T 31~41 °C, I 0~0.3 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 4.87 |
| beta_def_966 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` | logK | 8.9 |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` | logK | 8.97 |
| beta_def_872 | ``[M] + [L]^3 <=> [ML3]`` | logK | 11.3 |

---

### Step 6: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND c.ligand_name_SRD LIKE '%EDTA%')",
  "order_by": "s.constant_value DESC",
  "limit": 5
}
```

[summary]
## search_stability — 5 row(s)

### `Zn^[2+]` + Ethylenedinitrilotetraacetic acid (EDTA) — 1 measurement(s)
metal_id: metal_208 | ligand_id: ligand_6277
ligand_HxL_def: H4L | ligand_SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_108712 | *** | beta_def_812 | ΔS | 250.2 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |

### `Zn^[2+]` + Oxybis(ethylenenitrilo)tetraacetic acid (EEDTA) — 2 measurement(s)
metal_id: metal_208 | ligand_id: ligand_6335
ligand_HxL_def: H4L | ligand_SMILES: O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_111809 | *** | beta_def_812 | ΔS | 207.5 | 20 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.39, L, +inf) |
| vlm_111808 | *** | beta_def_812 | ΔS | 184.5 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.39, L, +inf) |

### `Zn^[2+]` + Thiobis(ethylenenitrilo)tetraacetic acid (TEDTA) — 1 measurement(s)
metal_id: metal_208 | ligand_id: ligand_6348
ligand_HxL_def: H4L | ligand_SMILES: O=C(O)CN(CCSCCN(CC(=O)O)CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_112304 | *** | beta_def_812 | ΔS | 204.6 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.31, L, +inf) |

### `Zn^[2+]` + N-(2-Hydroxyethyl)ethylenedinitrilotriacetic acid (HEDTA) — 1 measurement(s)
metal_id: metal_208 | ligand_id: ligand_6275
ligand_HxL_def: H3L | ligand_SMILES: O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_108152 | *** | beta_def_812 | ΔS | 161.5 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.7, L, +inf) |

---

### Step 7: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND c.ligand_name_SRD LIKE '%citrate%')",
  "order_by": "s.constant_value DESC",
  "limit": 5
}
```

[summary]
## search_stability — 5 row(s)

### `W^[6+]` + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) — 3 measurement(s)
metal_id: metal_204 | ligand_id: ligand_9058
ligand_HxL_def: H3L | ligand_SMILES: O=C(O)CC(O)(CC(=O)O)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_157728 | *** | beta_def_554 | ΔS | 338.9 | 25 | 1 | * | *** |  |  |
| vlm_157725 | *** | beta_def_937 | ΔS | 213.4 | 25 | 1 | `[MO2(OH)4] + [L]^2 + [H]^4 <=> [MO2H2(H-1L)2] + [H2O]^4` | *** | [L] | (5.65, L, +inf) |
| vlm_157716 | *** | beta_def_934 | ΔS | 128 | 25 | 1 | `[MO2(OH)2(H-1L)] + [H] <=> [MO2(OH)(H-1L)] + [H2O]` | *** |  |  |

### `H^[+]` + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) — 1 measurement(s)
metal_id: metal_68 | ligand_id: ligand_9058
ligand_HxL_def: H3L | ligand_SMILES: O=C(O)CC(O)(CC(=O)O)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_157456 | *** | beta_def_79 | ΔS | 133.9 | 25 | 0 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (4.35, HL, 5.65, L, +inf) |

### `Fe^[3+]` + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) — 1 measurement(s)
metal_id: metal_61 | ligand_id: ligand_9058
ligand_HxL_def: H3L | ligand_SMILES: O=C(O)CC(O)(CC(=O)O)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_157686 | *** | beta_def_812 | ΔS | 117.6 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (5.65, L, +inf) |

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND (c.ligand_name_SRD LIKE '%ammonia%' OR c.ligand_name_SRD LIKE '%ammine%'))",
  "order_by": "s.constant_value DESC",
  "limit": 5
}
```

[summary]
## search_stability — 5 row(s)

### `Zn^[2+]` + Ammonia — 5 measurement(s)
metal_id: metal_208 | ligand_id: ligand_10103
ligand_HxL_def: L | ligand_SMILES: N

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_173404 | *** | beta_def_840 | ΔS | 14.6 | 25 | 2 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.26, L, +inf) |
| vlm_173411 | ref_eq_map_28174 | beta_def_894 | logK | 9.73 | 25 | 2 | `[M] + [L]^4 <=> [ML4]` | *** | [L] | (9.26, L, +inf) |
| vlm_173399 | *** | beta_def_812 | ΔS | 9.6 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173410 | ref_eq_map_28173 | beta_def_894 | logK | 9.34 | 25 | 1 | `[M] + [L]^4 <=> [ML4]` | *** | [L] | (9.26, L, +inf) |
| vlm_173412 | ref_eq_map_28172 | beta_def_894 | logK | 8.89 | 25 | 0 | `[M] + [L]^4 <=> [ML4]` | *** | [L] | (9.26, L, +inf) |

---

### Step 9: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND c.ligand_name_SRD LIKE '%carbonate%' AND c.ligand_name_SRD NOT LIKE '%hydrogen%')",
  "order_by": "s.constant_value DESC",
  "limit": 5
}
```

[summary]
## search_stability — 5 row(s)

### `UO_[2]^[2+]` + Hydrogen carbonate (Carbonic acid) — 2 measurement(s)
metal_id: metal_195 | ligand_id: ligand_10096
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_172827 | *** | beta_def_653 | ΔS | 870.3 | 25 | 3 | `[M]^3 + [L]^6 <=> [M3L6]` | *** | [L] | (9.91, L, +inf) |
| vlm_172826 | *** | beta_def_653 | ΔS | 828.4 | 25 | 0 | `[M]^3 + [L]^6 <=> [M3L6]` | *** | [L] | (9.91, L, +inf) |

### `U^[4+]` + Hydrogen carbonate (Carbonic acid) — 1 measurement(s)
metal_id: metal_193 | ligand_id: ligand_10096
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_172789 | *** | beta_def_903 | ΔS | 640.2 | 25 | 3 | `[M] + [L]^5 <=> [ML5]` | *** | [L] | (9.91, L, +inf) |

### `Fe^[3+]` + Ethanoic acid (Acetic acid) — 1 measurement(s)
metal_id: metal_61 | ligand_id: ligand_8465
ligand_HxL_def: HL | ligand_SMILES: CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_144796 | *** | beta_def_597 | ΔS | 619.2 | 25 | 1 | `[M]^3 + [L]^6 + [H2O]^2 <=> [M3(OH)2L6] + [H]^2` | *** | [L] | (4.56, L, +inf) |

### `Th^[4+]` + Propanedioic acid (Malonic acid) — 1 measurement(s)
metal_id: metal_185 | ligand_id: ligand_8873
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_152275 | *** | beta_def_872 | ΔS | 376.6 | 25 | 1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (5.27, L, +inf) |

---

### Step 10: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND c.ligand_name_SRD LIKE '%phosphate%' AND c.ligand_name_SRD NOT LIKE '%hydrogen%')",
  "order_by": "s.constant_value DESC",
  "limit": 5
}
```

[summary]
## search_stability — 5 row(s)

### `Zn^[2+]` + Phosphoric acid methyl ester (Methyl phosphate) — 1 measurement(s)
metal_id: metal_208 | ligand_id: ligand_9150
ligand_HxL_def: H2L | ligand_SMILES: COP(=O)(O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_159408 | ref_eq_map_22670 | beta_def_966 | logK | 7.29 | 25 | 0.1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |

### `Zn^[2+]` + Phosphoric acid 1-naphthyl ester (alpha-Naphthyl phosphate) — 1 measurement(s)
metal_id: metal_208 | ligand_id: ligand_9154
ligand_HxL_def: H2L | ligand_SMILES: O=P(O)(O)Oc1cccc2ccccc12

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_159468 | ref_eq_map_22711 | beta_def_966 | logK | 6.74 | 25 | 0.1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |

### `Zn^[2+]` + Diphosphoric acid butyl ester (Butyl diphosphate) — 1 measurement(s)
metal_id: metal_208 | ligand_id: ligand_9166
ligand_HxL_def: H3L | ligand_SMILES: CCCCOP(=O)(O)OP(=O)(O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_159624 | ref_eq_map_22803 | beta_def_812 | logK | 4.4 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (6.65, L, +inf) |

### `Zn^[2+]` + Diphosphoric acid phenyl ester (Phenyl diphosphate) — 1 measurement(s)
metal_id: metal_208 | ligand_id: ligand_9167
ligand_HxL_def: H3L | ligand_SMILES: O=P(O)(O)OP(=O)(O)Oc1ccccc1

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_159636 | ref_eq_map_22814 | beta_def_812 | logK | 4.06 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (6.32, L, +inf) |

### `Zn^[2+]` + Phosphoric acid butyl ester (Butyl phosphate) — 1 measurement(s)
metal_id: metal_208 | ligand_id: ligand_9151
ligand_HxL_def: H2L | ligand_SMILES: CCCCOP(=O)(O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_159421 | ref_eq_map_22680 | beta_def_812 | logK | 2.3 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (6.72, L, +inf) |

---

### Step 11: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND c.ligand_name_SRD LIKE '%hydroxide%')",
  "order_by": "s.constant_value DESC",
  "limit": 5
}
```

[summary]
## search_stability — 5 row(s)

### `Zn^[2+]` + Hydroxide ion — 5 measurement(s)
metal_id: metal_208 | ligand_id: ligand_10076
ligand_HxL_def: *** | ligand_SMILES: ***

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_170946 | *** | beta_def_337 | ΔH | 31.4 | 25 | 2 | `[ML2(s,am)] <=> [M] + [L]^2` | solid | [L] | (13.78, L, +inf) |
| vlm_170943 | ref_eq_map_27449 | beta_def_674 | logK | 27.9 | 25 | 3 | `[M]^4 + [L]^4 <=> [M4L4]` | *** | [L] | (13.78, L, +inf) |
| vlm_170960 | *** | beta_def_347 | ΔH | 22.6 | 25 | 2 | `[MO(s)] + [H2O] <=> [M] + [OH]^2` | solid |  |  |
| vlm_170939 | ref_eq_map_27447 | beta_def_894 | logK | 15.5 | 25 | 0 | `[M] + [L]^4 <=> [ML4]` | *** | [L] | (13.78, L, +inf) |
| vlm_170938 | ref_eq_map_27449 | beta_def_894 | logK | 15.4 | 25 | 3 | `[M] + [L]^4 <=> [ML4]` | *** | [L] | (13.78, L, +inf) |

---

### Step 12: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_208"
}
```

[summary]
[CATALOG]
## build_system_catalog — 20 pair(s), 94 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_204 | [MHL2] + [H] <=> [M(HL)2] |  |
| beta_def_238 | [M(OH)2L] + [H] <=> [M(OH)L] + [H2O] |  |
| beta_def_334 | [ML2(s)] <=> [M] + [L]^2 | solid |
| beta_def_337 | [ML2(s,am)] <=> [M] + [L]^2 | solid |
| beta_def_340 | [ML2(s,beta1)] <=> [M] + [L]^2 | solid |
| beta_def_341 | [ML2(s,beta2)] <=> [M] + [L]^2 | solid |
| beta_def_343 | [ML2(s,delta)] <=> [M] + [L]^2 | solid |
| beta_def_344 | [ML2(s,epsilon)] <=> [M] + [L]^2 | solid |
| beta_def_345 | [ML2(s,gamma)] <=> [M] + [L]^2 | solid |
| beta_def_347 | [MO(s)] + [H2O] <=> [M] + [OH]^2 | solid |
| beta_def_374 | [M]^2 + [L]^2 <=> [M2(H-1L)2] + [H]^2 |  |
| beta_def_502 | [M]^2 + [L] <=> [M2L] |  |
| beta_def_636 | [M]^3 + [H] + [L]^4 <=> [M3HL4] |  |
| beta_def_637 | [M3L4] + [H] <=> [M3HL4] |  |
| beta_def_651 | [M3(OH)L4] + [H] <=> [M3L4] + [H2O] |  |
| beta_def_674 | [M]^4 + [L]^4 <=> [M4L4] |  |
| beta_def_739 | [MHL] + [H] <=> [MH2L] |  |
| beta_def_751 | [MH2L] + [H] <=> [MH3L] |  |
| beta_def_765 | [MH3L] + [H] <=> [MH4L] |  |
| beta_def_779 | [M] + [HL] <=> [MHL] |  |
| beta_def_788 | [ML] + [H] <=> [MHL] |  |
| beta_def_792 | [ML2] + [H] <=> [MHL2] |  |
| beta_def_812 | [M] + [L] <=> [ML] |  |
| beta_def_840 | [M] + [L]^2 <=> [ML2] |  |
| beta_def_872 | [M] + [L]^3 <=> [ML3] |  |
| beta_def_894 | [M] + [L]^4 <=> [ML4] |  |
| beta_def_966 | [M(OH)L] + [H] <=> [ML] + [H2O] |  |
| beta_def_984 | [M(OH)L2] + [H] <=> [ML2] + [H2O] |  |

*(all species aqueous unless noted)*

**1. Zn^[2+] + Aminoacetic acid (Glycine)** (metal_208 + ligand_5760) — ligand_def_HxL: HL | 37 ent, 4 sp, 37 vlms (vlm_93924…vlm_93960)
   - species: beta_def_812(12) beta_def_840(13) beta_def_872(11) beta_def_966(1)
   - eq:7 nets T:5~45°C I:-0.15~1.15M max 4n/4e
**2. Zn^[2+] + Ethylenediamine** (metal_208 + ligand_7029) — ligand_def_HxL: L | 36 ent, 3 sp, 36 vlms (vlm_122508…vlm_122543)
   - species: beta_def_812(12) beta_def_840(12) beta_def_872(12)
   - eq:8 nets T:19~41°C I:-0.15~3.15M max 3n/3e
**3. Zn^[2+] + Hydroxide ion** (metal_208 + ligand_10076) — ligand_def_HxL: *** | 33 ent, 13 sp, 33 vlms (vlm_170929…vlm_170961)
   - species: beta_def_337(4) beta_def_340(2) beta_def_341(2) beta_def_343(2) beta_def_344(2) beta_def_345(2) beta_def_347(4) beta_def_502(3) beta_def_674(1) beta_def_812(5) beta_def_840(2) beta_def_872(2) beta_def_894(2)
   - eq:4 nets T:19~30°C I:-0.15~3.15M max 11n/55e
**4. Zn^[2+] + Hydrogen cyanide (Hydrocyanic acid)** (metal_208 + ligand_10090) — ligand_def_HxL: HL | 30 ent, 5 sp, 30 vlms (vlm_171980…vlm_172009)
   - species: beta_def_334(1) beta_def_812(2) beta_def_840(9) beta_def_872(9) beta_def_894(9)
   - eq:5 nets T:5~45°C I:-0.15~3.15M max 5n/10e
**5. Zn^[2+] + 1,3-Diazole (Imidazole)** (metal_208 + ligand_7795) — ligand_def_HxL: L | 30 ent, 4 sp, 30 vlms (vlm_133954…vlm_133983)
   - species: beta_def_812(9) beta_def_840(7) beta_def_872(7) beta_def_894(7)
   - eq:7 nets T:19~41°C I:-0.05~3.15M max 4n/6e
**6. Zn^[2+] + L-2-Amino-3-(4-imidazolyl)propanoic acid (Histidine)** (metal_208 + ligand_5898) — ligand_def_HxL: HL | 29 ent, 6 sp, 29 vlms (vlm_98899…vlm_98927)
   - species: beta_def_204(1) beta_def_788(4) beta_def_792(3) beta_def_812(8) beta_def_840(12) beta_def_984(1)
   - eq:6 nets T:19~41°C I:-0.05~3.15M max 5n/6e
**7. Zn^[2+] + Hydrogen thiocyanate (Thiocyanic acid)** (metal_208 + ligand_10092) — ligand_def_HxL: HL | 24 ent, 4 sp, 24 vlms (vlm_172381…vlm_172404)
   - species: beta_def_812(8) beta_def_840(6) beta_def_872(5) beta_def_894(5)
   - eq:6 nets T:19~30°C I:-0.15~5.15M max 4n/6e
**8. Zn^[2+] + L-2-Amino-3-mercaptopropanoic acid (Cysteine)** (metal_208 + ligand_5856) — ligand_def_HxL: H2L | 23 ent, 8 sp, 23 vlms (vlm_97446…vlm_97468)
   - species: beta_def_204(4) beta_def_636(4) beta_def_637(3) beta_def_651(1) beta_def_779(2) beta_def_792(4) beta_def_812(1) beta_def_840(4)
   - eq:4 nets T:15~41°C I:-0.05~3.15M max 7n/14e
**9. Zn^[2+] + Ammonia** (metal_208 + ligand_10103) — ligand_def_HxL: L | 21 ent, 4 sp, 21 vlms (vlm_173394…vlm_173414)
   - species: beta_def_812(6) beta_def_840(5) beta_def_872(5) beta_def_894(5)
   - eq:4 nets T:19~30°C I:-0.15~2.15M max 4n/6e
**10. Zn^[2+] + Nitrilotris(methylenephosphonic acid) (NTP)** (metal_208 + ligand_8412) — ligand_def_HxL: H6L | 21 ent, 5 sp, 21 vlms (vlm_143422…vlm_143442)
   - species: beta_def_739(2) beta_def_751(2) beta_def_765(1) beta_def_788(7) beta_def_812(9)
   - eq:2 nets T:19~30°C I:-0.15~0.25M max 5n/7e
**11. Zn^[2+] + Iminodiacetic acid (IDA)** (metal_208 + ligand_6127) — ligand_def_HxL: H2L | 20 ent, 2 sp, 20 vlms (vlm_104424…vlm_104443)
   - species: beta_def_812(10) beta_def_840(10)
   - eq:3 nets T:19~41°C I:-0.05~1.15M max 2n/1e
**12. Zn^[2+] + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid)** (metal_208 + ligand_9058) — ligand_def_HxL: H3L | 19 ent, 4 sp, 19 vlms (vlm_157746…vlm_157764)
   - species: beta_def_374(3) beta_def_779(5) beta_def_812(6) beta_def_840(5)
   - eq:4 nets T:19~41°C I:-0.05~0.65M max 4n/6e
**13. Zn^[2+] + 1,10-Phenanthroline (Dipyridino[a,c]benzene)** (metal_208 + ligand_8191) — ligand_def_HxL: L | 19 ent, 3 sp, 19 vlms (vlm_139340…vlm_139358)
   - species: beta_def_812(7) beta_def_840(6) beta_def_872(6)
   - eq:3 nets T:19~30°C I:-0.15~1.15M max 3n/3e
**14. Zn^[2+] + L-2-Aminopropanoic acid (Alanine)** (metal_208 + ligand_5761) — ligand_def_HxL: HL | 19 ent, 4 sp, 19 vlms (vlm_94305…vlm_94323)
   - species: beta_def_812(7) beta_def_840(7) beta_def_872(3) beta_def_966(2)
   - eq:5 nets T:19~41°C I:-0.15~1.15M max 4n/4e
**15. Zn^[2+] + 2,2'-Bipyridyl** (metal_208 + ligand_8156) — ligand_def_HxL: L | 18 ent, 3 sp, 18 vlms (vlm_138658…vlm_138675)
   - species: beta_def_812(6) beta_def_840(6) beta_def_872(6)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 3n/3e
**16. Zn^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_208 + ligand_6277) — ligand_def_HxL: H4L | 18 ent, 4 sp, 18 vlms (vlm_108707…vlm_108724)
   - species: beta_def_739(1) beta_def_788(5) beta_def_812(6) beta_def_966(6)
   - eq:5 nets T:19~30°C I:-0.15~3.15M max 4n/5e
**17. Zn^[2+] + N-(2-Hydroxyethyl)iminodiacetic acid (HIDA)** (metal_208 + ligand_6204) — ligand_def_HxL: H2L | 18 ent, 4 sp, 18 vlms (vlm_106769…vlm_106786)
   - species: beta_def_238(1) beta_def_812(8) beta_def_840(8) beta_def_966(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 4n/3e
**18. Zn^[2+] + D-2-Amino-3-mercapto-3-methylbutanoic acid (Penicillamine)** (metal_208 + ligand_5857) — ligand_def_HxL: H2L | 18 ent, 8 sp, 18 vlms (vlm_97593…vlm_97610)
   - species: beta_def_204(4) beta_def_636(1) beta_def_637(1) beta_def_779(2) beta_def_792(4) beta_def_812(1) beta_def_840(4) beta_def_984(1)
   - eq:4 nets T:15~41°C I:-0.05~3.15M max 6n/13e
**19. Zn^[2+] + Ethanoic acid (Acetic acid)** (metal_208 + ligand_8465) — ligand_def_HxL: HL | 17 ent, 3 sp, 17 vlms (vlm_144834…vlm_144850)
   - species: beta_def_812(8) beta_def_840(6) beta_def_872(3)
   - eq:6 nets T:19~30°C I:-0.15~3.15M max 3n/3e
**20. Zn^[2+] + DL-Methylethylenediamine (1,2-Propylenediamine) (pn)** (metal_208 + ligand_7030) — ligand_def_HxL: L | 17 ent, 3 sp, 17 vlms (vlm_122671…vlm_122687)
   - species: beta_def_812(8) beta_def_840(8) beta_def_872(1)
   - eq:8 nets T:19~35°C I:-0.15~2.15M max 3n/3e

---
