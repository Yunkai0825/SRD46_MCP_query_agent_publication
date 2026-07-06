# Q5.1.4 — Tool Results (batch 5)

### Step 2: `search_metals`
**Args:**
```json
{
  "symbol": "Zn",
  "limit": 10
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_208 | Zn^[2+] | Zn | 2 | ✓ | [Zn+2] | InChI=1S/Zn/q+2 | beta_totN_122 | ligand_totN_1169 | vlm_totN_4095 |

---

### Step 4: `db_count_records`
**Args:**
```json
{
  "table": "vlm",
  "where": "metal_id = metal_208"
}
```

[summary]
**db_count_records:** Error - Table 'vlm' not allowed. Choose from: ['ligand_card', 'ligand_pka_bracket', 'ligand_pka_measured', 'ligandmetal_card', 'ligandmetal_stability_estimated', 'ligandmetal_stability_measured', 'metal_card', 'ref_author', 'ref_literature_alt', 'ref_vlm_author', 'ref_vlm_literature_alt']

---

### Step 5: `db_distribution`
**Args:**
```json
{
  "table": "vlm",
  "group_column": "ligand_class_name",
  "where": "metal_id = metal_208",
  "limit": 15
}
```

[summary]
**db_distribution:** Error - Table 'vlm' not allowed.

---

### Step 6: `db_distribution`
**Args:**
```json
{
  "table": "vlm",
  "group_column": "solvent_name",
  "where": "metal_id = metal_208",
  "limit": 10
}
```

[summary]
**db_distribution:** Error - Table 'vlm' not allowed.

---

### Step 7: `db_distribution`
**Args:**
```json
{
  "table": "vlm",
  "group_column": "electrolyte_composition",
  "where": "metal_id = metal_208",
  "limit": 10
}
```

[summary]
**db_distribution:** Error - Table 'vlm' not allowed.

---

### Step 8: `db_distribution`
**Args:**
```json
{
  "table": "vlm",
  "group_column": "temperature_c",
  "where": "metal_id = metal_208",
  "limit": 10
}
```

[summary]
**db_distribution:** Error - Table 'vlm' not allowed.

---

### Step 9: `db_ranked_pairs`
**Args:**
```json
{
  "where": "lc.metal_id = metal_208",
  "limit": 15
}
```

[summary]
## db_ranked_pairs - ligands_per_metal

| metal_id | name | count |
|----------|------|-------|
| metal_208 | Zn^[2+] | 1169 |

---

### Step 10: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208)",
  "order_by": "n.node_count DESC",
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
