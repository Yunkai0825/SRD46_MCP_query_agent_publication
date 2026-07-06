# Q3.2.7 — Tool Results (batch 3)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Copper(II)",
  "limit": 10
}
```

[summary]
## search_metals — 3 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_41 | Cu^[2+] | Cu | 2 | ✓ | [Cu+2] | InChI=1S/Cu/q+2 | beta_totN_264 | ligand_totN_1951 | vlm_totN_8963 |
| metal_42 | Cu^[+] | Cu | 1 | ✓ | [Cu+] | InChI=1S/Cu/q+1 | beta_totN_32 | ligand_totN_117 | vlm_totN_285 |
| metal_43 | Cu^[3+] | Cu | 3 | ✓ | [Cu+3] | InChI=1S/Cu/q+3 | beta_totN_4 | ligand_totN_8 | vlm_totN_10 |

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "ammonia, ammine",
  "limit": 10
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 4: `search_ligands`
**Args:**
```json
{
  "formula": "NH3",
  "limit": 10
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 5: `search_ligands`
**Args:**
```json
{
  "name": "azane",
  "limit": 10
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_10103 | Ammonia | L | Inorganic ligands | 447 | `N` | (-inf, HL, 9.26, L, +inf) |

---

### Step 6: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_41",
  "ligand_id": "ligand_10103"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 4 species

### Cu^[2+] + Ammonia
**metal_id:** metal_41 | **ligand_id:** ligand_10103 | **ligand_def_HxL:** L  
**entries:** 49 | **species:** 4 | **vlm_count:** 49

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 13 |
| beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | [M] + [L]^2 <=> [ML2] | [ML2](aqueous), [M](aqueous), [L](aqueous) | 12 |
| beta_def_872 | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | [M] + [L]^3 <=> [ML3] | [ML3](aqueous), [M](aqueous), [L](aqueous) | 12 |
| beta_def_894 | [ML<sub>4</sub>]/[M][L]<sup>4</sup> | [M] + [L]^4 <=> [ML4] | [ML4](aqueous), [M](aqueous), [L](aqueous) | 12 |

**vlm_ids:** vlm_173242, vlm_173243, vlm_173244, vlm_173245, vlm_173246, … vlm_173288, vlm_173289, vlm_173290 (49 listed)

**equilibrium_maps:** 5 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_28241 | 4 | 6 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_28242 | 4 | 6 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_28243 | 4 | 6 | 19~29 °C | 1.85~2.15 M |
| ref_eq_net_28244 | 4 | 6 | 19~29 °C | 2.85~3.15 M |
| ref_eq_net_28245 | 1 | 0 | 19~29 °C | -0.15~0.15 M |

---

### Step 8: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id = metal_41 AND c.ligand_id = ligand_10103 AND m.condition_temp_min <= 25 AND m.condition_temp_max >= 25 AND m.condition_ionic_min <= 0.15 AND m.condition_ionic_max >= 0)",
  "order_by": "n.node_count DESC",
  "limit": 10
}
```

[summary]
## search_networks — 5 row(s)

> **Reference equilibrium networks** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### `Cu^[2+]` + Ammonia — 2 network(s)
metal_id: metal_41 | ligand_id: ligand_10103 | ligand_def_HxL: L | ligand_SMILES: N

| beta_def | equation |
|----------|----------|
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_894 | ``[M] + [L]^4 <=> [ML4]`` |
| beta_def_872 | ``[M] + [L]^3 <=> [ML3]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_28241 | 4 | 6 | 20~30 | -0.05~0.25 | 4 | 4 diff beta_def | logK | 4.1~12.3 |
| ref_eq_net_28245 | 1 | 0 | 19~29 | -0.15~0.15 | 1 | beta_def_812 | logK | 4.02 |

#### Reference-state network: ref_eq_net_28241 (4 nodes)
> First network — reference conditions (T 20~30 °C, I -0.05~0.25 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 4.1 |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` | logK | 7.4 |
| beta_def_872 | ``[M] + [L]^3 <=> [ML3]`` | logK | 10.2 |
| beta_def_894 | ``[M] + [L]^4 <=> [ML4]`` | logK | 12.3 |

---

### Step 9: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_41 AND c.ligand_id = ligand_10103 AND c.beta_definition_id IN (beta_def_812, beta_def_840, beta_def_872, beta_def_894) AND s.temperature_c BETWEEN 24 AND 26 AND s.solvent_name LIKE '%water%')",
  "order_by": "c.beta_definition_id ASC, s.ionic_strength_mol_l ASC",
  "limit": 100
}
```

[summary]
## search_stability

*(no results)*

---

### Step 10: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_41 AND c.ligand_id = ligand_10103 AND c.beta_definition_id IN (beta_def_812, beta_def_840, beta_def_872, beta_def_894) AND s.temperature_c BETWEEN 19 AND 30)",
  "order_by": "s.ionic_strength_mol_l ASC, c.beta_definition_id ASC",
  "limit": 100
}
```

[summary]
## search_stability — 49 row(s)

### `Cu^[2+]` + Ammonia — 49 measurement(s)
metal_id: metal_41 | ligand_id: ligand_10103
ligand_HxL_def: L | ligand_SMILES: N

| equation | type | vlm_counts | ref_eq_map | value_range | T°C_range | I(M)_range | beta_defs | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|----------|------|------------|------------|-------------|-----------|------------|-----------|--------------------|--------------|-------------|
| `[M] + [L] <=> [ML]` | logK | 5 | 5 diff ref_eq_map | 4.02~4.3 | 25 | 0~3 | beta_def_812 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L] <=> [ML]` | ΔH | 4 | *** | -23~-20.1 | 25 | 0~3 | beta_def_812 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L] <=> [ML]` | ΔS | 4 | *** | 5~9.6 | 25 | 0~3 | beta_def_812 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^2 <=> [ML2]` | logK | 4 | 4 diff ref_eq_map | 7.4~7.91 | 25 | 0~3 | beta_def_840 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^2 <=> [ML2]` | ΔH | 4 | *** | -46.4~-42.3 | 25 | 0~3 | beta_def_840 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^2 <=> [ML2]` | ΔS | 4 | *** | -4.6~0 | 25 | 0~3 | beta_def_840 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^3 <=> [ML3]` | logK | 4 | 4 diff ref_eq_map | 10.2~10.8 | 25 | 0~3 | beta_def_872 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^3 <=> [ML3]` | ΔH | 4 | *** | -70.7~-62.3 | 25 | 0~3 | beta_def_872 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^3 <=> [ML3]` | ΔS | 4 | *** | -30.5~-14.2 | 25 | 0~3 | beta_def_872 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^4 <=> [ML4]` | logK | 4 | 4 diff ref_eq_map | 12.3~13.2 | 25 | 0~3 | beta_def_894 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^4 <=> [ML4]` | ΔH | 4 | *** | -99.2~-86.6 | 25 | 0~3 | beta_def_894 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^4 <=> [ML4]` | ΔS | 4 | *** | -80.3~-55.2 | 25 | 0~3 | beta_def_894 | *** | [L] | (9.26, L, +inf) |

Summary stats
| type | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|------|------------|-------------|-----------|------------|--------------------|-------------------|
| logK | 17 | 4 | 25 | 0~3 | *** | 5 |
| ΔH | 16 | 4 | 25 | 0~3 | *** | 0 |
| ΔS | 16 | 4 | 25 | 0~3 | *** | 0 |

---
