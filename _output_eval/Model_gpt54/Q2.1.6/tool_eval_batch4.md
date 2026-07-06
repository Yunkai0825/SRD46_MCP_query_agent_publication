# Q2.1.6 — Tool Results (batch 4)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Cadmium, Lead, Mercury",
  "limit": 10
}
```

[summary]
## search_metals

*(no results)*

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "Thiocyanate, Thiocyanic acid",
  "limit": 10
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 4: `search_metals`
**Args:**
```json
{
  "symbol": "Cd, Pb, Hg",
  "limit": 10
}
```

[summary]
## search_metals

*(no results)*

---

### Step 5: `search_ligands`
**Args:**
```json
{
  "formula": "SCN, HSCN",
  "limit": 10
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 6: `search_metals`
**Args:**
```json
{
  "exclude": [],
  "limit": 20
}
```

[TOOL ERROR] search_metals: Error executing tool search_metals: 1 validation error for search_metalsArguments
exclude
  Input should be a valid string [type=string_type, input_value=[], input_type=list]
    For further information visit https://errors.pydantic.dev/2.11/v/string_type

---

### Step 7: `search_ligands`
**Args:**
```json
{
  "exclude": [],
  "limit": 20
}
```

[TOOL ERROR] search_ligands: Error executing tool search_ligands: 1 validation error for search_ligandsArguments
exclude
  Input should be a valid string [type=string_type, input_value=[], input_type=list]
    For further information visit https://errors.pydantic.dev/2.11/v/string_type

---

### Step 8: `db_distribution`
**Args:**
```json
{
  "table": "metal_card",
  "group_column": "metal_name_SRD",
  "limit": 20
}
```

[PHASE ERROR] Tool 'db_distribution' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 9: `db_distribution`
**Args:**
```json
{
  "table": "ligand_card",
  "group_column": "ligand_name_SRD",
  "limit": 50
}
```

[PHASE ERROR] Tool 'db_distribution' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 10: `build_system_catalog`
**Args:**
```json
{}
```

[summary]
[CATALOG]
## build_system_catalog

**Error:** Provide at least one of metal_id, ligand_id, or beta_definition_id.

---

### Step 12: `search_networks`
**Args:**
```json
{
  "where": "((c.metal_name LIKE '%cadmium%' OR c.metal_name LIKE '%lead%' OR c.metal_name LIKE '%mercury%') AND (c.ligand_name LIKE '%thiocyan%' OR c.ligand_name LIKE '%rhodan%'))",
  "order_by": "c.metal_name, c.ligand_name",
  "limit": 20
}
```

[summary]
## search_networks — 44 row(s)

> **Reference equilibrium networks (compact)** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### Beta-definition legend
| beta_def | equation |
|----------|----------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |
| beta_def_540 | ``[M]^2 + [L]^3 <=> [M2L3]`` |
| beta_def_872 | ``[M] + [L]^3 <=> [ML3]`` |
| beta_def_894 | ``[M] + [L]^4 <=> [ML4]`` |
| beta_def_79 | ``[L] + [H] <=> [HL]`` |

### Metal-ligand pair summary
| metal | metal_id | ligand | ligand_id | HxL | T_range | I_range | net_count | max_nodes | ligand_SMILES |
|-------|----------|--------|-----------|-----|---------|---------|-----------|----------|---------------|
| `Ag^[+]` | metal_2 | Cyanomethane (Acetonitrile) | ligand_9825 | L | 20~30 | -0.05~0.25 | 1 | 2 | CC#N |
| `Ag^[+]` | metal_2 | Thiocarbamide (Thiourea) | ligand_10004 | L | 19~30 | -0.05~1.15 | 3 | 4 | NC(N)=S |
| `Au^[+]` | metal_13 | Thiocarbamide (Thiourea) | ligand_10004 | L | 16.5~31.5 | 0.275~0.725 | 1 | 3 | NC(N)=S |
| `Cd^[2+]` | metal_26 | Thiocarbamide (Thiourea) | ligand_10004 | L | 19~30 | -0.05~0.65 | 2 | 4 | NC(N)=S |
| `Co^[2+]` | metal_33 | Thiocarbamide (Thiourea) | ligand_10004 | L | 20~30 | -0.05~0.25 | 1 | 3 | NC(N)=S |
| `Cu^[+]` | metal_42 | Cyanomethane (Acetonitrile) | ligand_9825 | L | 20~30 | -0.05~0.25 | 1 | 1 | CC#N |
| `Cu^[+]` | metal_42 | Thiocarbamide (Thiourea) | ligand_10004 | L | 20~30 | -0.05~0.25 | 1 | 3 | NC(N)=S |
| `H^[+]` | metal_68 | Thiocarbamide (Thiourea) | ligand_10004 | L | 19~30 | -0.15~4.15 | 6 | 1 | NC(N)=S |
| `Pd^[2+]` | metal_127 | Cyanomethane (Acetonitrile) | ligand_9825 | L | 16.5~31.5 | 0.775~1.225 | 1 | 2 | CC#N |
| `Pd^[2+]` | metal_127 | Thiocarbamide (Thiourea) | ligand_10004 | L | 16.5~31.5 | 0.275~0.725 | 1 | 1 | NC(N)=S |
| `Pt^[2+]` | metal_146 | Thiocarbamide (Thiourea) | ligand_10004 | L | 16.5~31.5 | 0.275~0.725 | 1 | 1 | NC(N)=S |
| `Zn^[2+]` | metal_208 | Thiocarbamide (Thiourea) | ligand_10004 | L | 16.5~31.5 | 1.775~2.225 | 1 | 3 | NC(N)=S |

### Max-node network per pair
| metal | metal_id | ligand | ligand_id | max_net_id | max_nodes | max_edge_counts | max_T_range | max_I_range | max_vlm_counts | max_beta_def_ids | max_type | max_values |
|-------|----------|--------|----------|------------|-----------|------------------|-------------|-------------|----------------|------------------|----------|------------|
| `Ag^[+]` | metal_2 | Cyanomethane (Acetonitrile) | ligand_9825 | ref_eq_net_26527 | 2 | 1 | 20~30 | -0.05~0.25 | 2 | beta_def_812; beta_def_840 | logK | 0.42~0.78 |
| `Ag^[+]` | metal_2 | Thiocarbamide (Thiourea) | ligand_10004 | ref_eq_net_27020 | 4 | 6 | 20~30 | -0.05~0.25 | 4 | 4 diff beta_def | logK | 6.46~20.7 |
| `Au^[+]` | metal_13 | Thiocarbamide (Thiourea) | ligand_10004 | ref_eq_net_27023 | 3 | 3 | 16.5~31.5 | 0.275~0.725 | 3 | beta_def_812; beta_def_840; beta_def_872 | logK | 4.52~6.1 |
| `Cd^[2+]` | metal_26 | Thiocarbamide (Thiourea) | ligand_10004 | ref_eq_net_27027 | 4 | 6 | 20~30 | -0.05~0.25 | 4 | 4 diff beta_def | logK | 1.3~3.2 |
| `Co^[2+]` | metal_33 | Thiocarbamide (Thiourea) | ligand_10004 | ref_eq_net_27018 | 3 | 3 | 20~30 | -0.05~0.25 | 3 | beta_def_812; beta_def_840; beta_def_872 | logK | 0.7~1.5 |
| `Cu^[+]` | metal_42 | Cyanomethane (Acetonitrile) | ligand_9825 | ref_eq_net_26526 | 1 | 0 | 20~30 | -0.05~0.25 | 1 | beta_def_840 | logK | 4.35 |
| `Cu^[+]` | metal_42 | Thiocarbamide (Thiourea) | ligand_10004 | ref_eq_net_27019 | 3 | 3 | 20~30 | -0.05~0.25 | 3 | beta_def_840; beta_def_872; beta_def_894 | logK | 12.3~15.5 |
| `H^[+]` | metal_68 | Thiocarbamide (Thiourea) | ligand_10004 | ref_eq_net_27012 | 1 | 0 | 20~30 | -0.05~0.25 | 1 | beta_def_79 | logK | -1.18 |
| `Pd^[2+]` | metal_127 | Cyanomethane (Acetonitrile) | ligand_9825 | ref_eq_net_26528 | 2 | 1 | 16.5~31.5 | 0.775~1.225 | 2 | beta_def_812; beta_def_840 | logK | 1.19~1.53 |
| `Pd^[2+]` | metal_127 | Thiocarbamide (Thiourea) | ligand_10004 | ref_eq_net_27024 | 1 | 0 | 16.5~31.5 | 0.275~0.725 | 1 | beta_def_894 | logK | 30.3 |
| `Pt^[2+]` | metal_146 | Thiocarbamide (Thiourea) | ligand_10004 | ref_eq_net_27025 | 1 | 0 | 16.5~31.5 | 0.275~0.725 | 1 | beta_def_894 | logK | 38.6 |
| `Zn^[2+]` | metal_208 | Thiocarbamide (Thiourea) | ligand_10004 | ref_eq_net_27026 | 3 | 3 | 16.5~31.5 | 1.775~2.225 | 3 | beta_def_812; beta_def_840; beta_def_872 | logK | 0.5~0.9 |

### Global max-node network: `Ag^[+]` + Thiocarbamide (Thiourea)
network_id: ref_eq_net_27020 | metal_id: metal_2 | ligand_id: ligand_10004 | ligand_def_HxL: L | nodes: 4

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 6.46 |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` | logK | 10.9 |
| beta_def_872 | ``[M] + [L]^3 <=> [ML3]`` | logK | 12.88 |
| beta_def_540 | ``[M]^2 + [L]^3 <=> [M2L3]`` | logK | 20.7 |

---

### Step 13: `search_pka_ligands`
**Args:**
```json
{
  "where": "(lc.ligand_name_SRD LIKE '%thiocyan%' OR lc.ligand_name_SRD LIKE '%rhodan%')",
  "order_by": "lc.ligand_name_SRD",
  "limit": 20
}
```

[summary]
## search_pka_ligands — 5 row(s)

| ligand_id | ligand_name | HxL_def | formula | smiles | pH_ladder | T°C_range | I(M)_range | similarity_score |
|-----------|-------------|---------|---------|--------|-----------|-----------|------------|------------------|
| ligand_9966 | 1,3-Thiazolidine-2-thione-4-one (Rhodanine) | *** | C3H3N1O1S2 | *** | −∞; HL (M_tot_1); (5.18, vlm_169276); L (M_tot_2); +∞ | 20 | 0.1 | *** |
| ligand_9967 | 5-(3-Phenylallylidene)-1,3-thiazolidine-2-thione-4-one (5-C… | *** | C12H9N1O1S2 | *** | −∞; HL (M_tot_1); (7.68, vlm_169279); L (M_tot_2); +∞ | 20 | 0.1 | *** |
| ligand_9968 | 5-Benzylidene-1,3-thiazolidine-2-thione-4-one (5-Benzyliden… | *** | C10H7N1O1S2 | *** | −∞; HL (M_tot_1); (7.58, vlm_169281); L (M_tot_2); +∞ | 20 | 0.1 | *** |
| ligand_9971 | 5-Oxolidine-1,3-thiazolidine-2-thione-4-one (5-Furylidine r… | *** | C7H5N1O2S2 | *** | −∞; HL (M_tot_1); (6.37, vlm_169290); L (M_tot_2); +∞ | 20 | 0.1 | *** |
| ligand_10092 | Hydrogen thiocyanate (Thiocyanic acid) | HL | C1H1N1S1 | N=C=S | −∞; HL (M_tot_1); (-1.1, vlm_172116); L (M_tot_65); +∞ | 20 | 0 | *** |

---
