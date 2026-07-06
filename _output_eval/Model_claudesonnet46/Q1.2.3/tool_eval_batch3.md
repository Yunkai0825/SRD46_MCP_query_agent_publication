# Q1.2.3 — Tool Results (batch 3)

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

### Step 5: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_5856"
}
```

[summary]
## inspect_card — Ligand | ligand_5856

**Name:** L-2-Amino-3-mercaptopropanoic acid (Cysteine)  
**Formula:** C3H7N1O2S1 | **Class:** Amino Acids  
**SMILES:** `N[C@@H](CS)C(=O)O`  
**InChI:** `InChI=1S/C3H7NO2S/c4-2(1-7)3(5)6/h2,7H,1,4H2,(H,5,6)/t2-/m0/s1`  
**HxL definition:** H2L  

**pKa values:** 3

| source_vlm | pKa | T (°C) | I (M) | From → To | Solvent | Method | Quality |
|------------|-----|--------|-------|-----------|---------|--------|---------|
| vlm_97397 | -1.90 | 25.0 | 0.1 | H2L → H3L | *** | *** | *** |
| vlm_97384 | 8.18 | 25.0 | 0.1 | HL → H2L | *** | *** | *** |
| vlm_97371 | 10.30 | 25.0 | 0.1 | L → HL | *** | *** | *** |

**Partners:** 18 metal(s), 134 measurement(s) total

| metal_id | Metal | # meas |
|----------|-------|--------|
| metal_68 | H^[+] | 37 |
| metal_208 | Zn^[2+] | 23 |
| metal_125 | Pb^[2+] | 16 |
| metal_112 | Ni^[2+] | 15 |
| metal_26 | Cd^[2+] | 8 |
| … | *(showing top 5 of 18)* | |

---

### Step 6: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND c.ligand_id = ligand_5856)",
  "order_by": "s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability — 20 row(s)

### `Zn^[2+]` + L-2-Amino-3-mercaptopropanoic acid (Cysteine) — 20 measurement(s)
metal_id: metal_208 | ligand_id: ligand_5856
ligand_HxL_def: H2L | ligand_SMILES: N[C@@H](CS)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_97464 | ref_eq_map_1019 | beta_def_636 | logK | 52.5 | 25 | 3 | `[M]^3 + [H] + [L]^4 <=> [M3HL4]` | *** | [L] | (10.3, L, +inf) |
| vlm_97462 | ref_eq_map_1020 | beta_def_636 | logK | 49.5 | 20 | 0.1 | `[M]^3 + [H] + [L]^4 <=> [M3HL4]` | *** | [L] | (10.3, L, +inf) |
| vlm_97461 | ref_eq_map_1017 | beta_def_636 | logK | 49 | 25 | 0.1 | `[M]^3 + [H] + [L]^4 <=> [M3HL4]` | *** | [L] | (10.3, L, +inf) |
| vlm_97463 | ref_eq_map_1018 | beta_def_636 | logK | 48.3 | 37 | 0.15 | `[M]^3 + [H] + [L]^4 <=> [M3HL4]` | *** | [L] | (10.3, L, +inf) |
| vlm_97450 | ref_eq_map_1019 | beta_def_840 | logK | 19.39 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (10.3, L, +inf) |
| vlm_97448 | ref_eq_map_1020 | beta_def_840 | logK | 18.21 | 20 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (10.3, L, +inf) |
| vlm_97447 | ref_eq_map_1017 | beta_def_840 | logK | 18.12 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (10.3, L, +inf) |
| vlm_97449 | ref_eq_map_1018 | beta_def_840 | logK | 17.9 | 37 | 0.15 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (10.3, L, +inf) |
| vlm_97446 | ref_eq_map_1017 | beta_def_812 | logK | 9.11 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (10.3, L, +inf) |
| vlm_97465 | ref_eq_map_1017 | beta_def_637 | logK | 6.9 | 25 | 0.1 | `[M3L4] + [H] <=> [M3HL4]` | *** |  |  |
| vlm_97456 | ref_eq_map_1019 | beta_def_792 | logK | 6.47 | 25 | 3 | `[ML2] + [H] <=> [MHL2]` | *** |  |  |
| vlm_97453 | ref_eq_map_1017 | beta_def_792 | logK | 6.3 | 25 | 0.1 | `[ML2] + [H] <=> [MHL2]` | *** |  |  |
| vlm_97467 | ref_eq_map_1019 | beta_def_637 | logK | 6.3 | 25 | 3 | `[M3L4] + [H] <=> [M3HL4]` | *** |  |  |
| vlm_97455 | ref_eq_map_1018 | beta_def_792 | logK | 6.25 | 37 | 0.15 | `[ML2] + [H] <=> [MHL2]` | *** |  |  |
| vlm_97460 | ref_eq_map_1019 | beta_def_204 | logK | 6.03 | 25 | 3 | `[MHL2] + [H] <=> [M(HL)2]` | *** |  |  |
| vlm_97468 | ref_eq_map_1018 | beta_def_651 | logK | 6.03 | 37 | 0.15 | `[M3(OH)L4] + [H] <=> [M3L4] + [H2O]` | *** |  |  |
| vlm_97458 | ref_eq_map_1020 | beta_def_204 | logK | 5.8 | 20 | 0.1 | `[MHL2] + [H] <=> [M(HL)2]` | *** |  |  |
| vlm_97466 | ref_eq_map_1018 | beta_def_637 | logK | 5.77 | 37 | 0.15 | `[M3L4] + [H] <=> [M3HL4]` | *** |  |  |
| vlm_97459 | ref_eq_map_1018 | beta_def_204 | logK | 5.6 | 37 | 0.15 | `[MHL2] + [H] <=> [M(HL)2]` | *** |  |  |
| vlm_97457 | ref_eq_map_1017 | beta_def_204 | logK | 5.5 | 25 | 0.1 | `[MHL2] + [H] <=> [M(HL)2]` | *** |  |  |

---

### Step 7: `search_pka_values`
**Args:**
```json
{
  "where": "(lc.ligand_id = ligand_5856)",
  "order_by": "p.pKa ASC"
}
```

[summary]
## search_pka_values — 3 row(s)

### pKa -2.0–-1.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_97397 | ligand_5856 | L-2-Amino-3-mercaptopropanoic acid… | H2L | N[C@@H](CS)C(=O)O | -1.9 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_2 |

### pKa 8.0–8.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_97384 | ligand_5856 | L-2-Amino-3-mercaptopropanoic acid… | H2L | N[C@@H](CS)C(=O)O | 8.18 | 25 | 0.1 | HL→H2L | M_tot_2 | M_tot_9 |

### pKa 10.0–10.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_97371 | ligand_5856 | L-2-Amino-3-mercaptopropanoic acid… | H2L | N[C@@H](CS)C(=O)O | 10.3 | 25 | 0.1 | L→HL | M_tot_9 | M_tot_17 |

---
