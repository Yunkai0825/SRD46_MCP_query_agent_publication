# Q1.2.3 — Tool Results (batch 1)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "zinc",
  "limit": 5
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_208 | Zn^[2+] | Zn | 2 | ✓ | [Zn+2] | InChI=1S/Zn/q+2 | beta_totN_122 | ligand_totN_1169 | vlm_totN_4095 |

---

### Step 4: `search_networks`
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

### Step 5: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND n.node_count > 5)",
  "order_by": "n.node_count DESC",
  "limit": 5
}
```

[summary]
## search_networks — 32 row(s)

> **Reference equilibrium networks (compact)** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### Beta-definition legend
| beta_def | equation |
|----------|----------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |
| beta_def_779 | ``[M] + [HL] <=> [MHL]`` |
| beta_def_792 | ``[ML2] + [H] <=> [MHL2]`` |
| beta_def_204 | ``[MHL2] + [H] <=> [M(HL)2]`` |
| beta_def_636 | ``[M]^3 + [H] + [L]^4 <=> [M3HL4]`` |
| beta_def_637 | ``[M3L4] + [H] <=> [M3HL4]`` |
| beta_def_651 | ``[M3(OH)L4] + [H] <=> [M3L4] + [H2O]`` |
| beta_def_839 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` |
| beta_def_975 | ``[M(OH)2L] + [H] <=> [M(OH)L] + [H2O]`` |
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` |
| beta_def_516 | ``[ML] + [M] <=> [M2L]`` |
| beta_def_515 | ``[M2(OH)L] + [H] <=> [M2L] + [H2O]`` |
| beta_def_739 | ``[MHL] + [H] <=> [MH2L]`` |
| beta_def_984 | ``[M(OH)L2] + [H] <=> [ML2] + [H2O]`` |

### Metal-ligand pair summary
| metal | metal_id | ligand | ligand_id | HxL | T_range | I_range | net_count | max_nodes | ligand_SMILES |
|-------|----------|--------|-----------|-----|---------|---------|-----------|----------|---------------|
| `Zn^[2+]` | metal_208 | L-2-Amino-3-mercaptopropanoic acid (Cys… | ligand_5856 | H2L | 20~41 | -0.05~0.3 | 2 | 7 | N[C@@H](CS)C(=O)O |
| `Zn^[2+]` | metal_208 | 6,16-Dioxa-3,9,13,19-tetraaza-1,11(2,6)… | ligand_7653 | L | 20~30 | -0.05~0.25 | 1 | 6 | c1cc2nc(c1)CNCCOCCNCc1cccc(n1)CNCCOCCNC2 |
| `Zn^[2+]` | metal_208 | 6,9,19,22-Tetraoxa-3,12,16,25-tetraaza-… | ligand_7654 | L | 20~30 | -0.05~0.25 | 1 | 6 | c1cc2nc(c1)CNCCOCCOCCNCc1cccc(n1)CNCCOCCOCCNC2 |
| `Zn^[2+]` | metal_208 | D-2-Amino-3-mercapto-3-methylbutanoic a… | ligand_5857 | H2L | 19~29 | 2.85~3.15 | 1 | 6 | CC(C)(S)[C@H](N)C(=O)O |

### Max-node network per pair
| metal | metal_id | ligand | ligand_id | max_net_id | max_nodes | max_edge_counts | max_T_range | max_I_range | max_vlm_counts | max_beta_def_ids | max_type | max_values |
|-------|----------|--------|----------|------------|-----------|------------------|-------------|-------------|----------------|------------------|----------|------------|
| `Zn^[2+]` | metal_208 | L-2-Amino-3-mercaptopropanoic acid (Cys… | ligand_5856 | ref_eq_net_1017 | 7 | 13 | 20~30 | -0.05~0.25 | 7 | 7 diff beta_def | logK | 4.6~49 |
| `Zn^[2+]` | metal_208 | 6,16-Dioxa-3,9,13,19-tetraaza-1,11(2,6)… | ligand_7653 | ref_eq_net_171 | 6 | 12 | 20~30 | -0.05~0.25 | 6 | 6 diff beta_def | logK | 3.8~11 |
| `Zn^[2+]` | metal_208 | 6,9,19,22-Tetraoxa-3,12,16,25-tetraaza-… | ligand_7654 | ref_eq_net_176 | 6 | 12 | 20~30 | -0.05~0.25 | 6 | 6 diff beta_def | logK | 3.9~9.7 |
| `Zn^[2+]` | metal_208 | D-2-Amino-3-mercapto-3-methylbutanoic a… | ligand_5857 | ref_eq_net_1050 | 6 | 13 | 19~29 | 2.85~3.15 | 6 | 6 diff beta_def | logK | -12~47.6 |

### Global max-node network: `Zn^[2+]` + L-2-Amino-3-mercaptopropanoic acid (Cysteine)
network_id: ref_eq_net_1017 | metal_id: metal_208 | ligand_id: ligand_5856 | ligand_def_HxL: H2L | nodes: 7

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_779 | ``[M] + [HL] <=> [MHL]`` | logK | 4.6 |
| beta_def_204 | ``[MHL2] + [H] <=> [M(HL)2]`` | logK | 5.5 |
| beta_def_792 | ``[ML2] + [H] <=> [MHL2]`` | logK | 6.3 |
| beta_def_637 | ``[M3L4] + [H] <=> [M3HL4]`` | logK | 6.9 |
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 9.11 |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` | logK | 18.12 |
| beta_def_636 | ``[M]^3 + [H] + [L]^4 <=> [M3HL4]`` | logK | 49 |

---
