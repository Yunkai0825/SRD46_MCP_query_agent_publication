# Q5.1.4 — Tool Results (batch 4)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "zinc",
  "symbol": "Zn",
  "limit": 20
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
  "where": "c.lc.metal_id = metal_208"
}
```

[summary]
**db_ranked_pairs:** Error - Unknown rank_by='vlm_count'. Choose from: ['ligands_per_metal', 'measurements_per_ligand', 'measurements_per_metal', 'metals_per_ligand', 'pka_per_ligand']

---

### Step 5: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_card",
  "group_column": "ligand_class_name",
  "where": "metal_id = metal_208",
  "limit": 20
}
```

[summary]
## db_distribution - ligandmetal_card by ligand_class_name

**total_rows:** 4095

| value | count | pct |
|-------|-------|-----|
| Amino Acids | 654 | 15.97% |
| Inorganic ligands | 285 | 6.96% |
| Aliphatic amines | 253 | 6.18% |
| EDTA and derivatives | 203 | 4.96% |
| Pyrroles (azoles) | 201 | 4.91% |
| Pyridines (azines) | 188 | 4.59% |
| Aliphatic amines secondary N | 180 | 4.4% |
| Aza-macrocycles | 167 | 4.08% |
| NTA and derivatives | 143 | 3.49% |
| Aza-oxa-macrocycles | 126 | 3.08% |
| Carboxylic acids diacids | 122 | 2.98% |
| Aminophosphorus acids | 113 | 2.76% |
| Peptides | 109 | 2.66% |
| Naphtols | 109 | 2.66% |
| Aza macrocycles with carboxylic acids | 106 | 2.59% |
| Bipyridines | 73 | 1.78% |
| Aliphatic amines tertiary N | 71 | 1.73% |
| Carboxylic acids | 61 | 1.49% |
| Carboxylic acids polyacids | 60 | 1.47% |
| Iminodiacetic acid and derivatives | 58 | 1.42% |

---

### Step 6: `db_ranked_pairs`
**Args:**
```json
{
  "rank_by": "measurements_per_ligand",
  "limit": 10,
  "where": "c.lc.metal_id = metal_208"
}
```

[TOOL ERROR] db_ranked_pairs: Error executing tool db_ranked_pairs: no such column: c.lc.metal_id

---

### Step 7: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208)",
  "order_by": "n.edge_count DESC",
  "limit": 8
}
```

[summary]
## search_networks — 28 row(s)

> **Reference equilibrium networks** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### `Zn^[2+]` + 6,16-Dioxa-3,9,13,19-tetraaza-1,11(2,6)-dipyridinacycloeico… — 1 network(s)
metal_id: metal_208 | ligand_id: ligand_7653 | ligand_def_HxL: L | ligand_SMILES: c1cc2nc(c1)CNCCOCCNCc1cccc(n1)CNCCOCCNC2

| beta_def | equation |
|----------|----------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_839 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` |
| beta_def_975 | ``[M(OH)2L] + [H] <=> [M(OH)L] + [H2O]`` |
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` |
| beta_def_516 | ``[ML] + [M] <=> [M2L]`` |
| beta_def_515 | ``[M2(OH)L] + [H] <=> [M2L] + [H2O]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_171 | 6 | 12 | 20~30 | -0.05~0.25 | 6 | 6 diff beta_def | logK | 3.8~11 |

#### Reference-state network: ref_eq_net_171 (6 nodes)
> First network — reference conditions (T 20~30 °C, I -0.05~0.25 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_516 | ``[ML] + [M] <=> [M2L]`` | logK | 3.8 |
| beta_def_515 | ``[M2(OH)L] + [H] <=> [M2L] + [H2O]`` | logK | 7.07 |
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` | logK | 7.45 |
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 8.89 |
| beta_def_839 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` | logK | 9.52 |
| beta_def_975 | ``[M(OH)2L] + [H] <=> [M(OH)L] + [H2O]`` | logK | 11 |

### `Zn^[2+]` + Aminoacetic acid (Glycine) — 7 network(s)
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
| ref_eq_net_115 | 3 | 3 | 19~29 | 0.85~1.15 | 3 | beta_def_812; beta_def_840; beta_def_872 | logK | 4.89~11.5 |
| ref_eq_net_116 | 3 | 3 | 5~15 | -0.15~0.15 | 3 | beta_def_812; beta_def_840; beta_def_872 | logK | 5.5~12.7 |
| ref_eq_net_117 | 3 | 3 | 19~29 | -0.15~0.15 | 3 | beta_def_812; beta_def_840; beta_def_872 | logK | 5.38~12.3 |
| ref_eq_net_118 | 3 | 3 | 35~45 | -0.15~0.15 | 3 | beta_def_812; beta_def_840; beta_def_872 | logK | 5.29~12 |

#### Reference-state network: ref_eq_net_113 (4 nodes)
> First network — reference conditions (T 31~41 °C, I 0~0.3 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 4.87 |
| beta_def_966 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` | logK | 8.9 |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` | logK | 8.97 |
| beta_def_872 | ``[M] + [L]^3 <=> [ML3]`` | logK | 11.3 |

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND c.ligand_name_SRD LIKE '%EDTA%' AND s.solvent_name = 'water' AND s.ionic_strength_mol_l BETWEEN 0.09 AND 0.11 AND s.temperature_c BETWEEN 23 AND 27)",
  "order_by": "s.constant_value DESC",
  "limit": 5
}
```

[summary]
## search_stability

*(no results)*

---

### Step 9: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND c.ligand_name_SRD LIKE '%histidine%' AND s.solvent_name = 'water' AND s.ionic_strength_mol_l BETWEEN 0.09 AND 0.11 AND s.temperature_c BETWEEN 23 AND 27)",
  "order_by": "s.constant_value DESC",
  "limit": 5
}
```

[summary]
## search_stability — 5 row(s)

### `Cu^[2+]` + L-2-Amino-3-phenylpropanoic acid (Phenylalanine) — 3 measurement(s)
metal_id: metal_41 | ligand_id: ligand_5777
ligand_HxL_def: HL | ligand_SMILES: N[C@@H](Cc1ccccc1)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_95081 | *** | beta_def_840 | ΔS | 130.5 | 25 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.09, L, +inf) |
| vlm_95083 | *** | beta_def_840 | ΔS | 121.8 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.09, L, +inf) |
| vlm_95082 | *** | beta_def_840 | ΔS | 120.1 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.09, L, +inf) |

### `Zn^[2+]` + L-2-Amino-3-phenylpropanoic acid (Phenylalanine) — 1 measurement(s)
metal_id: metal_208 | ligand_id: ligand_5777
ligand_HxL_def: HL | ligand_SMILES: N[C@@H](Cc1ccccc1)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_95097 | *** | beta_def_840 | ΔS | 125.1 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.09, L, +inf) |

### `Ni^[2+]` + L-2-Amino-3-phenylpropanoic acid (Phenylalanine) — 1 measurement(s)
metal_id: metal_112 | ligand_id: ligand_5777
ligand_HxL_def: HL | ligand_SMILES: N[C@@H](Cc1ccccc1)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_95052 | *** | beta_def_840 | ΔS | 118 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.09, L, +inf) |

---

### Step 10: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND c.ligand_name_SRD LIKE '%imidazole%' AND s.solvent_name = 'water' AND s.ionic_strength_mol_l BETWEEN 0.09 AND 0.11 AND s.temperature_c BETWEEN 23 AND 27)",
  "order_by": "s.constant_value DESC",
  "limit": 5
}
```

[summary]
## search_stability — 5 row(s)

### `H^[+]` + 1,2,4-Triazole — 1 measurement(s)
metal_id: metal_68 | ligand_id: ligand_7876
ligand_HxL_def: HL | ligand_SMILES: c1nc[nH]n1

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_135074 | *** | beta_def_79 | ΔS | 56.5 | 25 | 0.5 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (2.38, HL, 9.82, L, +inf) |

### `H^[+]` + 1,2,3-Triazole — 1 measurement(s)
metal_id: metal_68 | ligand_id: ligand_7873
ligand_HxL_def: L | ligand_SMILES: c1c[nH]nn1

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_135051 | *** | beta_def_79 | ΔS | 52.7 | 25 | 0 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (-inf, HL, 9.26, L, +inf) |

### `H^[+]` + Pyridine (Azine) — 2 measurement(s)
metal_id: metal_68 | ligand_id: ligand_7890
ligand_HxL_def: L | ligand_SMILES: c1ccncc1

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_135226 | *** | beta_def_79 | ΔS | 31 | 25 | 0 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (-inf, HL, 5.24, L, +inf) |
| vlm_135227 | *** | beta_def_79 | ΔS | 30.5 | 25 | 0.5 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (-inf, HL, 5.24, L, +inf) |

### `Pd^[2+]` + Pyridine (Azine) — 1 measurement(s)
metal_id: metal_127 | ligand_id: ligand_7890
ligand_HxL_def: L | ligand_SMILES: c1ccncc1

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_135306 | ref_eq_map_13737 | beta_def_894 | logK | 28 | 25 | 1 | `[M] + [L]^4 <=> [ML4]` | *** | [L] | (5.24, L, +inf) |

---

### Step 11: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND c.ligand_name_SRD LIKE '%glycine%' AND s.solvent_name = 'water' AND s.ionic_strength_mol_l BETWEEN 0.09 AND 0.11 AND s.temperature_c BETWEEN 23 AND 27)",
  "order_by": "s.constant_value DESC",
  "limit": 5
}
```

[summary]
## search_stability — 5 row(s)

### `Th^[4+]` + Propanedioic acid (Malonic acid) — 2 measurement(s)
metal_id: metal_185 | ligand_id: ligand_8873
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_152275 | *** | beta_def_872 | ΔS | 376.6 | 25 | 1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (5.27, L, +inf) |
| vlm_152272 | *** | beta_def_840 | ΔS | 312.5 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (5.27, L, +inf) |

### `Sc^[3+]` + Propanedioic acid (Malonic acid) — 1 measurement(s)
metal_id: metal_169 | ligand_id: ligand_8873
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_152035 | *** | beta_def_872 | ΔS | 360.2 | 25 | 1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (5.27, L, +inf) |

### `Fe^[3+]` + Propanedioic acid (Malonic acid) — 2 measurement(s)
metal_id: metal_61 | ligand_id: ligand_8873
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_152350 | *** | beta_def_872 | ΔS | 341.8 | 25 | 1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (5.27, L, +inf) |
| vlm_152346 | *** | beta_def_840 | ΔS | 297.5 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (5.27, L, +inf) |

---
