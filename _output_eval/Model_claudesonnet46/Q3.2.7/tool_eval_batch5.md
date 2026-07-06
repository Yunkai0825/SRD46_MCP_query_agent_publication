# Q3.2.7 — Tool Results (batch 5)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "copper",
  "symbol": "Cu"
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
  "name": "ammonia"
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

### Step 6: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_41 AND c.ligand_id = ligand_10103 AND s.temperature_c BETWEEN 20 AND 30 AND s.ionic_strength_mol_l BETWEEN 0 AND 0.3)",
  "order_by": "c.beta_definition_id ASC, s.constant_value DESC",
  "limit": 40
}
```

[summary]
## search_stability — 13 row(s)

### `Cu^[2+]` + Ammonia — 13 measurement(s)
metal_id: metal_41 | ligand_id: ligand_10103
ligand_HxL_def: L | ligand_SMILES: N

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_173251 | *** | beta_def_812 | ΔS | 9.6 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173242 | ref_eq_map_28132 | beta_def_812 | logK | 4.1 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173246 | ref_eq_map_28136 | beta_def_812 | logK | 4.02 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173247 | *** | beta_def_812 | ΔH | -20.1 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173258 | ref_eq_map_28132 | beta_def_840 | logK | 7.4 | 25 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.26, L, +inf) |
| vlm_173263 | *** | beta_def_840 | ΔS | 0 | 25 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.26, L, +inf) |
| vlm_173259 | *** | beta_def_840 | ΔH | -42.3 | 25 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.26, L, +inf) |
| vlm_173270 | ref_eq_map_28132 | beta_def_872 | logK | 10.2 | 25 | 0 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (9.26, L, +inf) |
| vlm_173275 | *** | beta_def_872 | ΔS | -14.2 | 25 | 0 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (9.26, L, +inf) |
| vlm_173271 | *** | beta_def_872 | ΔH | -62.3 | 25 | 0 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (9.26, L, +inf) |
| vlm_173282 | ref_eq_map_28132 | beta_def_894 | logK | 12.3 | 25 | 0 | `[M] + [L]^4 <=> [ML4]` | *** | [L] | (9.26, L, +inf) |
| vlm_173287 | *** | beta_def_894 | ΔS | -55.2 | 25 | 0 | `[M] + [L]^4 <=> [ML4]` | *** | [L] | (9.26, L, +inf) |
| vlm_173283 | *** | beta_def_894 | ΔH | -86.6 | 25 | 0 | `[M] + [L]^4 <=> [ML4]` | *** | [L] | (9.26, L, +inf) |

---
