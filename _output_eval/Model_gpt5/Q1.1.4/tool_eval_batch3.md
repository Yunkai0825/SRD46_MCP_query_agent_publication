# Q1.1.4 — Tool Results (batch 3)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "silver",
  "symbol": "Ag",
  "limit": 25
}
```

[summary]
## search_metals — 3 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_2 | Ag^[+] | Ag | 1 | ✓ | [Ag+] | InChI=1S/Ag/q+1 | beta_totN_68 | ligand_totN_649 | vlm_totN_2885 |
| metal_3 | Ag^[2+] | Ag | 2 | ✓ | [Ag+2] | InChI=1S/Ag/q+2 | beta_totN_1 | ligand_totN_5 | vlm_totN_5 |
| metal_4 | Ag^[3+] | Ag | 3 | ✓ | [Ag+3] | InChI=1S/Ag/q+3 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "ammonia",
  "limit": 50
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 50

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_10103 | Ammonia | L | Inorganic ligands | 447 | `N` | (-inf, HL, 9.26, L, +inf) |

---

### Step 4: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_2",
  "ligand_id": "ligand_10103"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 2 species

### Ag^[+] + Ammonia
**metal_id:** metal_2 | **ligand_id:** ligand_10103 | **ligand_def_HxL:** L  
**entries:** 47 | **species:** 2 | **vlm_count:** 47

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 22 |
| beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | [M] + [L]^2 <=> [ML2] | [ML2](aqueous), [M](aqueous), [L](aqueous) | 25 |

**vlm_ids:** vlm_173338, vlm_173339, vlm_173340, vlm_173341, vlm_173342, … vlm_173382, vlm_173383, vlm_173384 (47 listed)

**equilibrium_maps:** 16 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_28262 | 2 | 1 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_28263 | 2 | 1 | 19~29 °C | 1.85~2.15 M |
| ref_eq_net_28264 | 2 | 1 | 19~29 °C | 2.85~3.15 M |
| ref_eq_net_28265 | 2 | 1 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_28266 | 2 | 1 | 19~29 °C | 1.85~2.15 M |
| ref_eq_net_28267 | 2 | 1 | 19~29 °C | 2.85~3.15 M |
| ref_eq_net_28268 | 2 | 1 | 19~29 °C | 3.85~4.15 M |
| ref_eq_net_28269 | 2 | 1 | 19~29 °C | 4.85~5.15 M |
| ref_eq_net_28270 | 1 | 0 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_28271 | 2 | 1 | 19~29 °C | 0.35~0.65 M |
| ref_eq_net_28272 | 2 | 1 | 19~29 °C | 1.85~2.15 M |
| ref_eq_net_28273 | 2 | 1 | 19~29 °C | 2.85~3.15 M |
| ref_eq_net_28274 | 2 | 1 | 19~29 °C | 3.85~4.15 M |
| ref_eq_net_28275 | 2 | 1 | 19~29 °C | 4.85~5.15 M |
| ref_eq_net_28276 | 1 | 0 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_28277 | 1 | 0 | 19~29 °C | 0.85~1.15 M |

---

### Step 5: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_2 AND c.ligand_id = ligand_10103 AND (c.beta_definition_id = beta_def_812 OR c.beta_definition_id = beta_def_840)",
  "order_by": "c.beta_definition_id, s.temperature_c, s.ionic_strength_mol_l, s.constant_type",
  "limit": 200
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. You must call 0_plan_search_strategy first (PHASE 2) before using the execution tools.

---

### Step 7: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_2 AND c.ligand_id = ligand_10103)",
  "order_by": "c.beta_definition_id, s.temperature_c, s.ionic_strength_mol_l, s.solvent_name, s.constant_type",
  "limit": 500
}
```

[summary]
## search_stability — 47 row(s)

### `Ag^[+]` + Ammonia — 47 measurement(s)
metal_id: metal_2 | ligand_id: ligand_10103
ligand_HxL_def: L | ligand_SMILES: N

| equation | type | vlm_counts | ref_eq_map | value_range | T°C_range | I(M)_range | beta_defs | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|----------|------|------------|------------|-------------|-----------|------------|-----------|--------------------|--------------|-------------|
| `[M] + [L] <=> [ML]` | ΔH | 5 | *** | -25.9~-20.5 | 25 | 0~3 | beta_def_812 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L] <=> [ML]` | logK | 13 | 13 diff ref_eq_map | 3.2~3.8 | 25 | 0~5 | beta_def_812 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L] <=> [ML]` | ΔS | 4 | *** | -12.1~-5.4 | 25 | 0~3 | beta_def_812 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^2 <=> [ML2]` | ΔH | 5 | *** | -61.9~-56.1 | 25 | 0~3 | beta_def_840 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^2 <=> [ML2]` | logK | 16 | 16 diff ref_eq_map | 7.14~8.18 | 25 | 0~5 | beta_def_840 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^2 <=> [ML2]` | ΔS | 4 | *** | -55.6~-46.4 | 25 | 0~3 | beta_def_840 | *** | [L] | (9.26, L, +inf) |

Summary stats
| type | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|------|------------|-------------|-----------|------------|--------------------|-------------------|
| ΔH | 10 | 2 | 25 | 0~3 | *** | 0 |
| logK | 29 | 2 | 25 | 0~5 | *** | 16 |
| ΔS | 8 | 2 | 25 | 0~3 | *** | 0 |

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_2 AND c.ligand_id = ligand_10103 AND s.constant_type = 'logK')",
  "order_by": "c.beta_definition_id, s.temperature_c, s.ionic_strength_mol_l, s.solvent_name, s.electrolyte_composition",
  "limit": 500
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
  "where": "(c.metal_id = metal_2 AND c.ligand_id = ligand_10103 AND c.beta_definition_id = beta_def_812)",
  "order_by": "s.temperature_c, s.ionic_strength_mol_l, s.solvent_name, s.electrolyte_composition, s.constant_value",
  "limit": 200
}
```

[summary]
## search_stability — 22 row(s)

### `Ag^[+]` + Ammonia — 22 measurement(s)
metal_id: metal_2 | ligand_id: ligand_10103
ligand_HxL_def: L | ligand_SMILES: N

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_173351 | *** | beta_def_812 | ΔH | -20.5 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173356 | *** | beta_def_812 | ΔS | -5.4 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173350 | ref_eq_map_28152 | beta_def_812 | logK | 3.31 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173338 | ref_eq_map_28161 | beta_def_812 | logK | 3.31 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173352 | *** | beta_def_812 | ΔH | -21.3 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173357 | *** | beta_def_812 | ΔS | -7.5 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173339 | ref_eq_map_28155 | beta_def_812 | logK | 3.35 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173340 | ref_eq_map_28153 | beta_def_812 | logK | 3.26 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173341 | ref_eq_map_28156 | beta_def_812 | logK | 3.27 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173342 | ref_eq_map_28162 | beta_def_812 | logK | 3.53 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173355 | *** | beta_def_812 | ΔH | -25.9 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173354 | *** | beta_def_812 | ΔH | -23.8 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173353 | *** | beta_def_812 | ΔH | -22.2 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173358 | *** | beta_def_812 | ΔS | -12.1 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173359 | *** | beta_def_812 | ΔS | -10.5 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173343 | ref_eq_map_28154 | beta_def_812 | logK | 3.2 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173344 | ref_eq_map_28157 | beta_def_812 | logK | 3.25 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173345 | ref_eq_map_28163 | beta_def_812 | logK | 3.63 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173346 | ref_eq_map_28158 | beta_def_812 | logK | 3.25 | 25 | 4 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173347 | ref_eq_map_28164 | beta_def_812 | logK | 3.8 | 25 | 4 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173348 | ref_eq_map_28159 | beta_def_812 | logK | 3.21 | 25 | 5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173349 | ref_eq_map_28165 | beta_def_812 | logK | 3.28 | 25 | 5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |

---

### Step 10: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_2 AND c.ligand_id = ligand_10103 AND c.beta_definition_id = beta_def_840)",
  "order_by": "s.temperature_c, s.ionic_strength_mol_l, s.solvent_name, s.electrolyte_composition, s.constant_value",
  "limit": 200
}
```

[summary]
## search_stability — 25 row(s)

### `Ag^[+]` + Ammonia — 25 measurement(s)
metal_id: metal_2 | ligand_id: ligand_10103
ligand_HxL_def: L | ligand_SMILES: N

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_173376 | *** | beta_def_840 | ΔH | -56.1 | 25 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.26, L, +inf) |
| vlm_173381 | *** | beta_def_840 | ΔS | -48.5 | 25 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.26, L, +inf) |
| vlm_173375 | ref_eq_map_28152 | beta_def_840 | logK | 7.22 | 25 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.26, L, +inf) |
| vlm_173360 | ref_eq_map_28161 | beta_def_840 | logK | 7.31 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.26, L, +inf) |
| vlm_173377 | *** | beta_def_840 | ΔH | -56.5 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.26, L, +inf) |
| vlm_173382 | *** | beta_def_840 | ΔS | -51 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.26, L, +inf) |
| vlm_173361 | ref_eq_map_28155 | beta_def_840 | logK | 7.24 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.26, L, +inf) |
| vlm_173362 | ref_eq_map_28160 | beta_def_840 | logK | 7.24 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.26, L, +inf) |
| vlm_173363 | ref_eq_map_28166 | beta_def_840 | logK | 7.34 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.26, L, +inf) |
| vlm_173364 | ref_eq_map_28167 | beta_def_840 | logK | 7.54 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.26, L, +inf) |
| vlm_173365 | ref_eq_map_28153 | beta_def_840 | logK | 7.22 | 25 | 2 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.26, L, +inf) |
| vlm_173366 | ref_eq_map_28156 | beta_def_840 | logK | 7.28 | 25 | 2 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.26, L, +inf) |
| vlm_173367 | ref_eq_map_28162 | beta_def_840 | logK | 7.78 | 25 | 2 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.26, L, +inf) |
| vlm_173380 | *** | beta_def_840 | ΔH | -61.9 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.26, L, +inf) |
| vlm_173379 | *** | beta_def_840 | ΔH | -59 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.26, L, +inf) |
| vlm_173378 | *** | beta_def_840 | ΔH | -58.2 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.26, L, +inf) |
| vlm_173383 | *** | beta_def_840 | ΔS | -55.6 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.26, L, +inf) |
| vlm_173384 | *** | beta_def_840 | ΔS | -46.4 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.26, L, +inf) |
| vlm_173368 | ref_eq_map_28154 | beta_def_840 | logK | 7.14 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.26, L, +inf) |
| vlm_173369 | ref_eq_map_28157 | beta_def_840 | logK | 7.3 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.26, L, +inf) |
| vlm_173370 | ref_eq_map_28163 | beta_def_840 | logK | 7.92 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.26, L, +inf) |
| vlm_173371 | ref_eq_map_28158 | beta_def_840 | logK | 7.34 | 25 | 4 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.26, L, +inf) |
| vlm_173372 | ref_eq_map_28164 | beta_def_840 | logK | 8.18 | 25 | 4 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.26, L, +inf) |
| vlm_173373 | ref_eq_map_28159 | beta_def_840 | logK | 7.14 | 25 | 5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.26, L, +inf) |
| vlm_173374 | ref_eq_map_28165 | beta_def_840 | logK | 7.38 | 25 | 5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.26, L, +inf) |

---
