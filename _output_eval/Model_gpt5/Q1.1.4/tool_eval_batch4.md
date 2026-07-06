# Q1.1.4 — Tool Results (batch 4)

### Step 2: `search_metals`
**Args:**
```json
{
  "symbol": "Ag",
  "limit": 10
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
  "limit": 25
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 25

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

### Step 6: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_2 AND c.ligand_id = ligand_10103)",
  "order_by": "c.beta_definition_id, s.temperature_c ASC, s.ionic_strength_mol_l ASC",
  "limit": 200
}
```

[summary]
## search_stability — 47 row(s)

### `Ag^[+]` + Ammonia — 47 measurement(s)
metal_id: metal_2 | ligand_id: ligand_10103
ligand_HxL_def: L | ligand_SMILES: N

| equation | type | vlm_counts | ref_eq_map | value_range | T°C_range | I(M)_range | beta_defs | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|----------|------|------------|------------|-------------|-----------|------------|-----------|--------------------|--------------|-------------|
| `[M] + [L] <=> [ML]` | logK | 13 | 13 diff ref_eq_map | 3.2~3.8 | 25 | 0~5 | beta_def_812 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L] <=> [ML]` | ΔH | 5 | *** | -25.9~-20.5 | 25 | 0~3 | beta_def_812 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L] <=> [ML]` | ΔS | 4 | *** | -12.1~-5.4 | 25 | 0~3 | beta_def_812 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^2 <=> [ML2]` | logK | 16 | 16 diff ref_eq_map | 7.14~8.18 | 25 | 0~5 | beta_def_840 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^2 <=> [ML2]` | ΔH | 5 | *** | -61.9~-56.1 | 25 | 0~3 | beta_def_840 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^2 <=> [ML2]` | ΔS | 4 | *** | -55.6~-46.4 | 25 | 0~3 | beta_def_840 | *** | [L] | (9.26, L, +inf) |

Summary stats
| type | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|------|------------|-------------|-----------|------------|--------------------|-------------------|
| logK | 29 | 2 | 25 | 0~5 | *** | 16 |
| ΔH | 10 | 2 | 25 | 0~3 | *** | 0 |
| ΔS | 8 | 2 | 25 | 0~3 | *** | 0 |

---
