# Q2.1.6 — Tool Results (batch 3)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Cadmium(II), Lead(II), Mercury(II)",
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
  "name": "thiocyanate, thiocyanic acid, rhodanide, isothiocyanate",
  "limit": 20
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
  "limit": 20
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 7: `build_system_catalog`
**Args:**
```json
{}
```

[summary]
[CATALOG]
## build_system_catalog

**Error:** Provide at least one of metal_id, ligand_id, or beta_definition_id.

---

### Step 8: `search_metals`
**Args:**
```json
{
  "name": "cadmium, lead, mercury",
  "limit": 20
}
```

[summary]
## search_metals

*(no results)*

---

### Step 9: `search_ligands`
**Args:**
```json
{
  "name": "thiocyanic, thiocyanate, rhodanide, isothiocyanate, thiocyanato",
  "limit": 50
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 10: `search_stability`
**Args:**
```json
{
  "where": "c.metal_name_SRD IN ('cadmium','lead','mercury') AND (c.ligand_name_SRD LIKE '%thiocyan%' OR c.ligand_name_SRD LIKE '%rhodan%' OR c.ligand_name_SRD LIKE '%isothiocyan%')",
  "order_by": "c.metal_name_SRD ASC, s.constant_value DESC",
  "limit": 100
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. You must call 0_plan_search_strategy first (PHASE 2) before using the execution tools.

---

### Step 12: `search_stability`
**Args:**
```json
{
  "where": "((c.metal_name_SRD LIKE '%cadmium%' OR c.metal_name_SRD LIKE '%lead%' OR c.metal_name_SRD LIKE '%mercury%') AND (c.ligand_name_SRD LIKE '%thiocyan%' OR c.ligand_name_SRD LIKE '%rhodan%' OR c.ligand_name_SRD LIKE '%isothiocyan%') AND s.solvent_name LIKE '%water%')",
  "order_by": "c.metal_name_SRD ASC, s.temperature_c ASC, s.ionic_strength_mol_l ASC, s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability — 100 row(s)

### logK — 15 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_2 | Ag^[+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 17 | 5 | 25 | 0~4 | solid | 4 |
| metal_2 | Ag^[+] | ligand_10004 | Thiocarbamide (Thiourea) | L | NC(N)=S | 11 | 5 | 25 | 0.02~1 | *** | 3 |
| metal_21 | Bi^[3+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 7 | 6 | 25 | 0~1 | *** | 2 |
| metal_2 | Ag^[+] | ligand_10106 | Hydrogen azide (Hydrazoic a… | HL | [N-]=[N+]=N | 6 | 5 | 25 | 0~4 | solid | 2 |
| metal_6 | Am^[3+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 3 | 1 | 25 | 0~5 | *** | 3 |
| metal_13 | Au^[+] | ligand_10004 | Thiocarbamide (Thiourea) | L | NC(N)=S | 3 | 3 | 25 | 0.5 | *** | 1 |
| metal_2 | Ag^[+] | ligand_10091 | Hydrogen cyanate (Cyanic ac… | HL | N=C=O | 2 | 2 | 20~30 | 0 | solid | 1 |
| metal_2 | Ag^[+] | ligand_10093 | Selenocyanate ion | L | N#C[Se-] | 2 | 2 | 20~25 | 0~0.5 | solid | 2 |
| metal_2 | Ag^[+] | ligand_9825 | Cyanomethane (Acetonitrile) | L | CC#N | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_6 | Am^[3+] | ligand_10106 | Hydrogen azide (Hydrazoic a… | HL | [N-]=[N+]=N | 2 | 1 | 25 | 0~0.5 | *** | 2 |
| metal_13 | Au^[+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 2 | 2 | 25 | 3 | *** | 1 |
| metal_19 | Be^[2+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 2 | 2 | 25 | 4 | *** | 1 |
| metal_1 | Ac^[3+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 1 | 1 | 25 | 1 | *** | 1 |
| metal_2 | Ag^[+] | ligand_10095 | Dicyanimide ion | L | N#C[N-]C#N | 1 | 1 | 20 | 0 | solid | 1 |
| metal_5 | Al^[3+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 1 | 1 | 22 | 0 | *** | 1 |

### ΔH — 5 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_2 | Ag^[+] | ligand_10004 | Thiocarbamide (Thiourea) | L | NC(N)=S | 11 | 5 | 25 | 0.02~1 | *** | 0 |
| metal_13 | Au^[+] | ligand_10004 | Thiocarbamide (Thiourea) | L | NC(N)=S | 3 | 3 | 25 | 0.5 | *** | 0 |
| metal_2 | Ag^[+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 2 | 2 | 25 | 0 | solid | 0 |
| metal_6 | Am^[3+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 2 | 1 | 25 | 1~5 | *** | 0 |
| metal_2 | Ag^[+] | ligand_10106 | Hydrogen azide (Hydrazoic a… | HL | [N-]=[N+]=N | 1 | 1 | 25 | 0 | solid | 0 |

### ΔS — 5 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_2 | Ag^[+] | ligand_10004 | Thiocarbamide (Thiourea) | L | NC(N)=S | 11 | 5 | 25 | 0.02~1 | *** | 0 |
| metal_13 | Au^[+] | ligand_10004 | Thiocarbamide (Thiourea) | L | NC(N)=S | 3 | 3 | 25 | 0.5 | *** | 0 |
| metal_2 | Ag^[+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 2 | 2 | 25 | 0 | solid | 0 |
| metal_6 | Am^[3+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 2 | 1 | 25 | 1~5 | *** | 0 |
| metal_2 | Ag^[+] | ligand_10106 | Hydrogen azide (Hydrazoic a… | HL | [N-]=[N+]=N | 1 | 1 | 25 | 0 | solid | 0 |

---

### Step 13: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_10092 AND (c.metal_name_SRD LIKE '%Cd%' OR c.metal_name_SRD LIKE '%cadm%' OR c.metal_name_SRD LIKE '%Pb%' OR c.metal_name_SRD LIKE '%lead%' OR c.metal_name_SRD LIKE '%Hg%' OR c.metal_name_SRD LIKE '%mercur%'))",
  "order_by": "c.metal_name_SRD ASC, s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability — 89 row(s)

### logK — 8 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_26 | Cd^[2+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 23 | 4 | 25 | 0~3 | *** | 7 |
| metal_71 | Hg^[2+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 8 | 6 | 25 | 0~1 | solid | 2 |
| metal_125 | Pb^[2+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 8 | 3 | 25 | 1~4 | *** | 4 |
| metal_53 | EtHg^[+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 2 | 2 | 25 | 1 | *** | 1 |
| metal_72 | Hg^[+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 2 | 1 | 25 | 0~1 | solid | 2 |
| metal_93 | MeHg^[+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_87 | Me_[3]Pb^[+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 1 | 1 | 25 | 1.5 | *** | 1 |
| metal_136 | PhHg^[+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 1 | 1 | 25 | 1 | *** | 1 |

### ΔS — 3 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_26 | Cd^[2+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 14 | 4 | 25 | 0~3 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 6 | 5 | 25 | 0~1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 1 | 1 | 25 | 2 | *** | 0 |

### ΔH — 3 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_26 | Cd^[2+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 14 | 4 | 25 | 0~3 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 6 | 5 | 25 | 0~1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 1 | 1 | 25 | 0 | *** | 0 |

---

### Step 14: `search_networks`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_10092 AND c.metal_id IN (metal_26, metal_71, metal_125))",
  "order_by": "c.metal_name ASC, m.condition_temp_min ASC, m.condition_ionic_min ASC",
  "limit": 50
}
```

[summary]
## search_networks — 39 row(s)

> **Reference equilibrium networks** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### `Cd^[2+]` + Hydrogen thiocyanate (Thiocyanic acid) — 7 network(s)
metal_id: metal_26 | ligand_id: ligand_10092 | ligand_def_HxL: HL | ligand_SMILES: N=C=S

| beta_def | equation |
|----------|----------|
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_894 | ``[M] + [L]^4 <=> [ML4]`` |
| beta_def_872 | ``[M] + [L]^3 <=> [ML3]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_28001 | 2 | 1 | 19~29 | -0.15~0.15 | 2 | beta_def_812; beta_def_840 | logK | 1.93~2.72 |
| ref_eq_net_27998 | 4 | 6 | 19~29 | 0.35~0.65 | 4 | 4 diff beta_def | logK | 1.35~2.08 |
| ref_eq_net_27999 | 4 | 6 | 19~29 | 0.85~1.15 | 4 | 4 diff beta_def | logK | 1.31~2.03 |
| ref_eq_net_27997 | 4 | 6 | 19~29 | 1.85~2.15 | 4 | 4 diff beta_def | logK | 1.09~2.18 |
| ref_eq_net_28002 | 1 | 0 | 19~29 | 1.85~2.15 | 1 | beta_def_812 | logK | 1.33 |
| ref_eq_net_28000 | 4 | 6 | 19~29 | 2.85~3.15 | 4 | 4 diff beta_def | logK | 1.39~2.5 |
| ref_eq_net_27996 | 4 | 6 | 20~30 | -0.05~0.25 | 4 | 4 diff beta_def | logK | 1.68~2.85 |

#### Reference-state network: ref_eq_net_28001 (2 nodes)
> First network — reference conditions (T 19~29 °C, I -0.15~0.15 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 1.93 |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` | logK | 2.72 |

### `Hg^[2+]` + Hydrogen thiocyanate (Thiocyanic acid) — 2 network(s)
metal_id: metal_71 | ligand_id: ligand_10092 | ligand_def_HxL: HL | ligand_SMILES: N=C=S

| beta_def | equation |
|----------|----------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |
| beta_def_872 | ``[M] + [L]^3 <=> [ML3]`` |
| beta_def_894 | ``[M] + [L]^4 <=> [ML4]`` |
| beta_def_966 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` |
| beta_def_334 | ``[ML2(s)] <=> [M] + [L]^2`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_28004 | 6 | 11 | 19~29 | 0.85~1.15 | 6 | 6 diff beta_def | logK | -19.56~21.7 |
| ref_eq_net_28003 | 2 | 1 | 20~30 | -0.05~0.25 | 2 | beta_def_812; beta_def_840 | logK | 9.64~17.5 |

#### Reference-state network: ref_eq_net_28004 (6 nodes)
> First network — reference conditions (T 19~29 °C, I 0.85~1.15 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_334 | ``[ML2(s)] <=> [M] + [L]^2`` | logK | -19.56 |
| beta_def_966 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` | logK | 3.4 |
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 9.08 |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` | logK | 16.86 |
| beta_def_872 | ``[M] + [L]^3 <=> [ML3]`` | logK | 19.7 |
| beta_def_894 | ``[M] + [L]^4 <=> [ML4]`` | logK | 21.7 |

### `Pb^[2+]` + Hydrogen thiocyanate (Thiocyanic acid) — 4 network(s)
metal_id: metal_125 | ligand_id: ligand_10092 | ligand_def_HxL: HL | ligand_SMILES: N=C=S

| beta_def | equation |
|----------|----------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |
| beta_def_872 | ``[M] + [L]^3 <=> [ML3]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_28011 | 1 | 0 | 16.5~31.5 | 0.775~1.225 | 1 | beta_def_812 | logK | 0.49 |
| ref_eq_net_28009 | 2 | 1 | 16.5~31.5 | 1.775~2.225 | 2 | beta_def_812; beta_def_840 | logK | 0.54~0.87 |
| ref_eq_net_28008 | 3 | 3 | 16.5~31.5 | 2.775~3.225 | 3 | beta_def_812; beta_def_872; beta_def_840 | logK | 0.78~0.99 |
| ref_eq_net_28010 | 2 | 1 | 16.5~31.5 | 3.775~4.225 | 2 | beta_def_812; beta_def_840 | logK | 1.08~1.48 |

#### Reference-state network: ref_eq_net_28011 (1 nodes)
> First network — reference conditions (T 16.5~31.5 °C, I 0.775~1.225 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 0.49 |

---
