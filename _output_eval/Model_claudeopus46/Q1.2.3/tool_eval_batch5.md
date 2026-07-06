# Q1.2.3 — Tool Results (batch 5)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Zn"
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_208 | Zn^[2+] | Zn | 2 | ✓ | [Zn+2] | InChI=1S/Zn/q+2 | beta_totN_122 | ligand_totN_1169 | vlm_totN_4095 |

---

### Step 3: `search_networks`
**Args:**
```json
{
  "where": "c.metal_id = metal_208 AND n.node_count > 5",
  "order_by": "n.node_count DESC",
  "limit": 5
}
```

[PHASE ERROR] Tool 'search_networks' is not available yet. You must call 0_plan_search_strategy first (PHASE 2) before using the execution tools.

---

### Step 5: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND n.node_count > 5)",
  "order_by": "n.node_count DESC",
  "limit": 3
}
```

[summary]
## search_networks — 19 row(s)

> **Reference equilibrium networks** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### `Zn^[2+]` + L-2-Amino-3-mercaptopropanoic acid (Cysteine) — 1 network(s)
metal_id: metal_208 | ligand_id: ligand_5856 | ligand_def_HxL: H2L | ligand_SMILES: N[C@@H](CS)C(=O)O

| beta_def | equation |
|----------|----------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |
| beta_def_779 | ``[M] + [HL] <=> [MHL]`` |
| beta_def_792 | ``[ML2] + [H] <=> [MHL2]`` |
| beta_def_204 | ``[MHL2] + [H] <=> [M(HL)2]`` |
| beta_def_636 | ``[M]^3 + [H] + [L]^4 <=> [M3HL4]`` |
| beta_def_637 | ``[M3L4] + [H] <=> [M3HL4]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_1017 | 7 | 13 | 20~30 | -0.05~0.25 | 7 | 7 diff beta_def | logK | 4.6~49 |

#### Reference-state network: ref_eq_net_1017 (7 nodes)
> First network — reference conditions (T 20~30 °C, I -0.05~0.25 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_779 | ``[M] + [HL] <=> [MHL]`` | logK | 4.6 |
| beta_def_204 | ``[MHL2] + [H] <=> [M(HL)2]`` | logK | 5.5 |
| beta_def_792 | ``[ML2] + [H] <=> [MHL2]`` | logK | 6.3 |
| beta_def_637 | ``[M3L4] + [H] <=> [M3HL4]`` | logK | 6.9 |
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 9.11 |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` | logK | 18.12 |
| beta_def_636 | ``[M]^3 + [H] + [L]^4 <=> [M3HL4]`` | logK | 49 |

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

### `Zn^[2+]` + 6,9,19,22-Tetraoxa-3,12,16,25-tetraaza-1,14(2,6)-dipyridina… — 1 network(s)
metal_id: metal_208 | ligand_id: ligand_7654 | ligand_def_HxL: L | ligand_SMILES: c1cc2nc(c1)CNCCOCCOCCNCc1cccc(n1)CNCCOCCOCCNC2

| beta_def | equation |
|----------|----------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_839 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` |
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` |
| beta_def_739 | ``[MHL] + [H] <=> [MH2L]`` |
| beta_def_516 | ``[ML] + [M] <=> [M2L]`` |
| beta_def_515 | ``[M2(OH)L] + [H] <=> [M2L] + [H2O]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_176 | 6 | 12 | 20~30 | -0.05~0.25 | 6 | 6 diff beta_def | logK | 3.9~9.7 |

#### Reference-state network: ref_eq_net_176 (6 nodes)
> First network — reference conditions (T 20~30 °C, I -0.05~0.25 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_516 | ``[ML] + [M] <=> [M2L]`` | logK | 3.9 |
| beta_def_739 | ``[MHL] + [H] <=> [MH2L]`` | logK | 6.42 |
| beta_def_515 | ``[M2(OH)L] + [H] <=> [M2L] + [H2O]`` | logK | 6.8 |
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` | logK | 7.08 |
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 8.7 |
| beta_def_839 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` | logK | 9.7 |

---
