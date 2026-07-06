# Q1.2.3 — Tool Results (batch 1)

### Step 2: `search_metals`
**Args:**
```json
{
  "symbol": "Zn",
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
  "limit": 1
}
```

[summary]
## search_networks — 6 row(s)

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

---

### Step 5: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_7653"
}
```

[summary]
## inspect_card — Ligand | ligand_7653

**Name:** 6,16-Dioxa-3,9,13,19-tetraaza-1,11(2,6)-dipyridinacycloeicosanaphane (O-BISBAMP)  
**Formula:** C22H34N6O2 | **Class:** Aza-oxa-macrocycles  
**SMILES:** `c1cc2nc(c1)CNCCOCCNCc1cccc(n1)CNCCOCCNC2`  
**InChI:** `InChI=1S/C22H34N6O2/c1-3-19-15-23-7-11-29-13-9-25-17-21-5-2-6-22(28-21)18-26-10-14-30-12-8-24-16-20(4-1)27-19/h1-6,23-26H,7-18H2`  
**HxL definition:** L  

**pKa values:** 4

| source_vlm | pKa | T (°C) | I (M) | From → To | Solvent | Method | Quality |
|------------|-----|--------|-------|-----------|---------|--------|---------|
| vlm_94163 | 6.80 | 25.0 | 0.1 | H3L → H4L | *** | *** | *** |
| vlm_94162 | 7.36 | 25.0 | 0.1 | H2L → H3L | *** | *** | *** |
| vlm_94161 | 7.96 | 25.0 | 0.1 | HL → H2L | *** | *** | *** |
| vlm_94160 | 8.79 | 25.0 | 0.1 | L → HL | *** | *** | *** |

**Partners:** 6 metal(s), 31 measurement(s) total

| metal_id | Metal | # meas |
|----------|-------|--------|
| metal_41 | Cu^[2+] | 7 |
| metal_208 | Zn^[2+] | 6 |
| metal_112 | Ni^[2+] | 6 |
| metal_33 | Co^[2+] | 5 |
| metal_68 | H^[+] | 4 |
| … | *(showing top 5 of 6)* | |

---
