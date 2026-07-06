# Q2.1.6 — Tool Results (batch 1)

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
  "name": "Thiocyanate, Thiocyanic acid",
  "limit": 10,
  "include_groups": [
    "thiocyanate"
  ]
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
  "name": "cadmium, lead, mercury",
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
  "name": "thiocyanate, thiocyanic acid, rhodanide, SCN",
  "formula": "HSCN, SCN",
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

### Step 9: `search_stability`
**Args:**
```json
{
  "where": "((c.metal_name_SRD LIKE '%cadmium%' OR c.metal_name_SRD LIKE '%lead%' OR c.metal_name_SRD LIKE '%mercur%') AND (c.ligand_name_SRD LIKE '%thiocyan%' OR c.ligand_name_SRD LIKE '%rhodan%' OR c.ligand_name_SRD LIKE '%SCN%'))",
  "order_by": "c.metal_name_SRD ASC, c.ligand_name_SRD ASC, s.temperature_c ASC",
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
| metal_2 | Ag^[+] | ligand_10106 | Hydrogen azide (Hydrazoic a… | HL | [N-]=[N+]=N | 6 | 5 | 25 | 0~4 | solid | 2 |
| metal_21 | Bi^[3+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 5 | 1 | 25 | 0~4 | *** | 5 |
| metal_6 | Am^[3+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 3 | 1 | 25 | 0~5 | *** | 3 |
| metal_13 | Au^[+] | ligand_10004 | Thiocarbamide (Thiourea) | L | NC(N)=S | 3 | 3 | 25 | 0.5 | *** | 1 |
| metal_2 | Ag^[+] | ligand_9825 | Cyanomethane (Acetonitrile) | L | CC#N | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_2 | Ag^[+] | ligand_10091 | Hydrogen cyanate (Cyanic ac… | HL | N=C=O | 2 | 2 | 20~30 | 0 | solid | 1 |
| metal_2 | Ag^[+] | ligand_10093 | Selenocyanate ion | L | N#C[Se-] | 2 | 2 | 20~25 | 0~0.5 | solid | 2 |
| metal_6 | Am^[3+] | ligand_10106 | Hydrogen azide (Hydrazoic a… | HL | [N-]=[N+]=N | 2 | 1 | 25 | 0~0.5 | *** | 2 |
| metal_13 | Au^[+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 2 | 2 | 25 | 3 | *** | 1 |
| metal_19 | Be^[2+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 2 | 2 | 25 | 4 | *** | 1 |
| metal_1 | Ac^[3+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 1 | 1 | 25 | 1 | *** | 1 |
| metal_2 | Ag^[+] | ligand_10095 | Dicyanimide ion | L | N#C[N-]C#N | 1 | 1 | 20 | 0 | solid | 1 |
| metal_5 | Al^[3+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 1 | 1 | 22 | 0 | *** | 1 |

### ΔH — 6 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_2 | Ag^[+] | ligand_10004 | Thiocarbamide (Thiourea) | L | NC(N)=S | 11 | 5 | 25 | 0.02~1 | *** | 0 |
| metal_13 | Au^[+] | ligand_10004 | Thiocarbamide (Thiourea) | L | NC(N)=S | 3 | 3 | 25 | 0.5 | *** | 0 |
| metal_2 | Ag^[+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 2 | 2 | 25 | 0 | solid | 0 |
| metal_6 | Am^[3+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 2 | 1 | 25 | 1~5 | *** | 0 |
| metal_2 | Ag^[+] | ligand_10106 | Hydrogen azide (Hydrazoic a… | HL | [N-]=[N+]=N | 1 | 1 | 25 | 0 | solid | 0 |
| metal_21 | Bi^[3+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 1 | 1 | 25 | 3 | *** | 0 |

### ΔS — 6 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_2 | Ag^[+] | ligand_10004 | Thiocarbamide (Thiourea) | L | NC(N)=S | 11 | 5 | 25 | 0.02~1 | *** | 0 |
| metal_13 | Au^[+] | ligand_10004 | Thiocarbamide (Thiourea) | L | NC(N)=S | 3 | 3 | 25 | 0.5 | *** | 0 |
| metal_2 | Ag^[+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 2 | 2 | 25 | 0 | solid | 0 |
| metal_6 | Am^[3+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 2 | 1 | 25 | 1~5 | *** | 0 |
| metal_2 | Ag^[+] | ligand_10106 | Hydrogen azide (Hydrazoic a… | HL | [N-]=[N+]=N | 1 | 1 | 25 | 0 | solid | 0 |
| metal_21 | Bi^[3+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 1 | 1 | 25 | 3 | *** | 0 |

---

### Step 10: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_10092 AND (c.metal_id = metal_41 OR c.metal_id = metal_62 OR c.metal_id = metal_80))",
  "order_by": "c.metal_name_SRD ASC, s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability — 23 row(s)

### `Cu^[2+]` + Hydrogen thiocyanate (Thiocyanic acid) — 21 measurement(s)
metal_id: metal_41 | ligand_id: ligand_10092
ligand_HxL_def: HL | ligand_SMILES: N=C=S

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_172270 | ref_eq_map_27842 | beta_def_840 | logK | 3.65 | 25 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172267 | ref_eq_map_27835 | beta_def_840 | logK | 3 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172269 | ref_eq_map_27838 | beta_def_840 | logK | 2.72 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172268 | ref_eq_map_27837 | beta_def_840 | logK | 2.54 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172265 | *** | beta_def_812 | ΔS | 2.5 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172261 | ref_eq_map_27845 | beta_def_812 | logK | 2.42 | 25 | 4 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172262 | ref_eq_map_27842 | beta_def_812 | logK | 2.33 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172259 | ref_eq_map_27844 | beta_def_812 | logK | 2.05 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172260 | ref_eq_map_27841 | beta_def_812 | logK | 2 | 25 | 4 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172258 | ref_eq_map_27840 | beta_def_812 | logK | 1.91 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172252 | ref_eq_map_27835 | beta_def_812 | logK | 1.88 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172256 | ref_eq_map_27843 | beta_def_812 | logK | 1.86 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172257 | ref_eq_map_27836 | beta_def_812 | logK | 1.86 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172255 | ref_eq_map_27839 | beta_def_812 | logK | 1.81 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172253 | ref_eq_map_27837 | beta_def_812 | logK | 1.78 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172254 | ref_eq_map_27838 | beta_def_812 | logK | 1.75 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172266 | *** | beta_def_812 | ΔS | -10 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172263 | *** | beta_def_812 | ΔH | -12.6 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172264 | *** | beta_def_812 | ΔH | -13 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172271 | *** | beta_def_840 | ΔH | -25.9 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172272 | *** | beta_def_840 | ΔS | -35.1 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (-1.1, L, +inf) |

### `Fe^[2+]` + Hydrogen thiocyanate (Thiocyanic acid) — 2 measurement(s)
metal_id: metal_62 | ligand_id: ligand_10092
ligand_HxL_def: HL | ligand_SMILES: N=C=S

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_172218 | ref_eq_map_27821 | beta_def_812 | logK | 1.31 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172217 | ref_eq_map_27822 | beta_def_812 | logK | 0.81 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |

---

### Step 11: `search_metals`
**Args:**
```json
{
  "metal_id": "metal_41",
  "limit": 10
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_41 | Cu^[2+] | Cu | 2 | ✓ | [Cu+2] | InChI=1S/Cu/q+2 | beta_totN_264 | ligand_totN_1951 | vlm_totN_8963 |

---
