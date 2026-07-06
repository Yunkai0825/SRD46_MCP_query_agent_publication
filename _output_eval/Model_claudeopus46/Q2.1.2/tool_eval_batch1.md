# Q2.1.2 — Tool Results (batch 1)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "manganese, iron, cobalt, nickel, copper, zinc"
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

### Step 4: `search_metals`
**Args:**
```json
{
  "name": "manganese"
}
```

[summary]
## search_metals — 4 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_94 | Mn^[2+] | Mn | 2 | ✓ | [Mn+2] | InChI=1S/Mn/q+2 | beta_totN_44 | ligand_totN_486 | vlm_totN_1273 |
| metal_95 | Mn^[3+] | Mn | 3 | ✓ | [Mn+3] | InChI=1S/Mn/q+3 | beta_totN_8 | ligand_totN_12 | vlm_totN_26 |
| metal_96 | Mn^[4+] | Mn | 4 | ✓ | [Mn+4] | InChI=1S/Mn/q+4 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_97 | MeNH_[3]^[+] | MNH3 | 1 |  | *** | *** | beta_totN_1 | ligand_totN_5 | vlm_totN_9 |

---

### Step 5: `search_metals`
**Args:**
```json
{
  "name": "iron"
}
```

[summary]
## search_metals — 2 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_61 | Fe^[3+] | Fe | 3 | ✓ | [Fe+3] | InChI=1S/Fe/q+3 | beta_totN_128 | ligand_totN_406 | vlm_totN_1473 |
| metal_62 | Fe^[2+] | Fe | 2 | ✓ | [Fe+2] | InChI=1S/Fe/q+2 | beta_totN_57 | ligand_totN_217 | vlm_totN_667 |

---

### Step 6: `search_metals`
**Args:**
```json
{
  "name": "cobalt"
}
```

[summary]
## search_metals — 3 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_33 | Co^[2+] | Co | 2 | ✓ | [Co+2] | InChI=1S/Co/q+2 | beta_totN_92 | ligand_totN_977 | vlm_totN_2977 |
| metal_34 | Co^[3+] | Co | 3 | ✓ | [Co+3] | InChI=1S/Co/q+3 | beta_totN_20 | ligand_totN_19 | vlm_totN_55 |
| metal_181 | TcO^[2+] | Tc | 2 |  | *** | *** | beta_totN_2 | ligand_totN_1 | vlm_totN_2 |

---

### Step 7: `search_metals`
**Args:**
```json
{
  "name": "nickel"
}
```

[summary]
## search_metals — 2 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_112 | Ni^[2+] | Ni | 2 | ✓ | [Ni+2] | InChI=1S/Ni/q+2 | beta_totN_149 | ligand_totN_1369 | vlm_totN_5325 |
| metal_113 | Ni^[3+] | Ni | 3 | ✓ | [Ni+3] | InChI=1S/Ni/q+3 | beta_totN_5 | ligand_totN_4 | vlm_totN_7 |

---

### Step 8: `search_metals`
**Args:**
```json
{
  "name": "copper"
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

### Step 9: `search_metals`
**Args:**
```json
{
  "name": "zinc"
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_208 | Zn^[2+] | Zn | 2 | ✓ | [Zn+2] | InChI=1S/Zn/q+2 | beta_totN_122 | ligand_totN_1169 | vlm_totN_4095 |

---

### Step 10: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_94 AND c.ligand_id = ligand_10103 AND s.constant_type = 'log K' AND s.temperature_c BETWEEN 20 AND 30",
  "order_by": "s.constant_value DESC",
  "limit": 20
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 11: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_62 AND c.ligand_id = ligand_10103 AND s.constant_type = 'log K' AND s.temperature_c BETWEEN 20 AND 30",
  "order_by": "s.constant_value DESC",
  "limit": 20
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 12: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_33 AND c.ligand_id = ligand_10103 AND s.constant_type = 'log K' AND s.temperature_c BETWEEN 20 AND 30",
  "order_by": "s.constant_value DESC",
  "limit": 20
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 13: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_112 AND c.ligand_id = ligand_10103 AND s.constant_type = 'log K' AND s.temperature_c BETWEEN 20 AND 30",
  "order_by": "s.constant_value DESC",
  "limit": 20
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 14: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_41 AND c.ligand_id = ligand_10103 AND s.constant_type = 'log K' AND s.temperature_c BETWEEN 20 AND 30",
  "order_by": "s.constant_value DESC",
  "limit": 20
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 15: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_208 AND c.ligand_id = ligand_10103 AND s.constant_type = 'log K' AND s.temperature_c BETWEEN 20 AND 30",
  "order_by": "s.constant_value DESC",
  "limit": 20
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 16: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_94",
  "ligand_id": "ligand_10103"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 4 species

### Mn^[2+] + Ammonia
**metal_id:** metal_94 | **ligand_id:** ligand_10103 | **ligand_def_HxL:** L  
**entries:** 32 | **species:** 4 | **vlm_count:** 32

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 8 |
| beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | [M] + [L]^2 <=> [ML2] | [ML2](aqueous), [M](aqueous), [L](aqueous) | 8 |
| beta_def_872 | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | [M] + [L]^3 <=> [ML3] | [ML3](aqueous), [M](aqueous), [L](aqueous) | 8 |
| beta_def_894 | [ML<sub>4</sub>]/[M][L]<sup>4</sup> | [M] + [L]^4 <=> [ML4] | [ML4](aqueous), [M](aqueous), [L](aqueous) | 8 |

**vlm_ids:** vlm_173099, vlm_173100, vlm_173101, vlm_173102, vlm_173103, … vlm_173128, vlm_173129, vlm_173130 (32 listed)

**equilibrium_maps:** 6 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_28219 | 4 | 6 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_28220 | 4 | 6 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_28221 | 4 | 6 | 19~29 °C | 1.85~2.15 M |
| ref_eq_net_28222 | 4 | 6 | 19~29 °C | 2.85~3.15 M |
| ref_eq_net_28223 | 4 | 6 | 19~29 °C | 3.85~4.15 M |
| ref_eq_net_28224 | 4 | 6 | 19~29 °C | 4.85~5.15 M |

---

### Step 17: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_62",
  "ligand_id": "ligand_10103"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 4 species

### Fe^[2+] + Ammonia
**metal_id:** metal_62 | **ligand_id:** ligand_10103 | **ligand_def_HxL:** L  
**entries:** 32 | **species:** 4 | **vlm_count:** 32

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 8 |
| beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | [M] + [L]^2 <=> [ML2] | [ML2](aqueous), [M](aqueous), [L](aqueous) | 8 |
| beta_def_872 | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | [M] + [L]^3 <=> [ML3] | [ML3](aqueous), [M](aqueous), [L](aqueous) | 8 |
| beta_def_894 | [ML<sub>4</sub>]/[M][L]<sup>4</sup> | [M] + [L]^4 <=> [ML4] | [ML4](aqueous), [M](aqueous), [L](aqueous) | 8 |

**vlm_ids:** vlm_173131, vlm_173132, vlm_173133, vlm_173134, vlm_173135, … vlm_173160, vlm_173161, vlm_173162 (32 listed)

**equilibrium_maps:** 6 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_28225 | 4 | 6 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_28226 | 4 | 6 | 19~29 °C | 1.85~2.15 M |
| ref_eq_net_28227 | 4 | 6 | 19~29 °C | 2.85~3.15 M |
| ref_eq_net_28228 | 4 | 6 | 19~29 °C | 3.85~4.15 M |
| ref_eq_net_28229 | 4 | 6 | 19~29 °C | 4.85~5.15 M |
| ref_eq_net_28230 | 4 | 6 | 19~29 °C | 5.85~6.15 M |

---

### Step 18: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_33",
  "ligand_id": "ligand_10103"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 5 species

### Co^[2+] + Ammonia
**metal_id:** metal_33 | **ligand_id:** ligand_10103 | **ligand_def_HxL:** L  
**entries:** 19 | **species:** 5 | **vlm_count:** 19

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 7 |
| beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | [M] + [L]^2 <=> [ML2] | [ML2](aqueous), [M](aqueous), [L](aqueous) | 3 |
| beta_def_872 | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | [M] + [L]^3 <=> [ML3] | [ML3](aqueous), [M](aqueous), [L](aqueous) | 3 |
| beta_def_894 | [ML<sub>4</sub>]/[M][L]<sup>4</sup> | [M] + [L]^4 <=> [ML4] | [ML4](aqueous), [M](aqueous), [L](aqueous) | 3 |
| beta_def_903 | [ML<sub>5</sub>]/[M][L]<sup>5</sup> | [M] + [L]^5 <=> [ML5] | [ML5](aqueous), [M](aqueous), [L](aqueous) | 3 |

**vlm_ids:** vlm_173163, vlm_173164, vlm_173165, vlm_173166, vlm_173167, … vlm_173179, vlm_173180, vlm_173181 (19 listed)

**equilibrium_maps:** 5 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_28231 | 5 | 10 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_28232 | 5 | 10 | 19~29 °C | 4.85~5.15 M |
| ref_eq_net_28233 | 5 | 10 | 25~35 °C | 1.85~2.15 M |
| ref_eq_net_28234 | 1 | 0 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_28235 | 1 | 0 | 19~29 °C | -0.15~0.15 M |

---

### Step 19: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_112",
  "ligand_id": "ligand_10103"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 6 species

### Ni^[2+] + Ammonia
**metal_id:** metal_112 | **ligand_id:** ligand_10103 | **ligand_def_HxL:** L  
**entries:** 60 | **species:** 6 | **vlm_count:** 60

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 11 |
| beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | [M] + [L]^2 <=> [ML2] | [ML2](aqueous), [M](aqueous), [L](aqueous) | 13 |
| beta_def_872 | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | [M] + [L]^3 <=> [ML3] | [ML3](aqueous), [M](aqueous), [L](aqueous) | 10 |
| beta_def_894 | [ML<sub>4</sub>]/[M][L]<sup>4</sup> | [M] + [L]^4 <=> [ML4] | [ML4](aqueous), [M](aqueous), [L](aqueous) | 10 |
| beta_def_903 | [ML<sub>5</sub>]/[M][L]<sup>5</sup> | [M] + [L]^5 <=> [ML5] | [ML5](aqueous), [M](aqueous), [L](aqueous) | 8 |
| beta_def_907 | [ML<sub>6</sub>]/[M][L]<sup>6</sup> | [M] + [L]^6 <=> [ML6] | [ML6](aqueous), [M](aqueous), [L](aqueous) | 8 |

**vlm_ids:** vlm_173182, vlm_173183, vlm_173184, vlm_173185, vlm_173186, … vlm_173239, vlm_173240, vlm_173241 (60 listed)

**equilibrium_maps:** 5 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_28236 | 6 | 15 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_28237 | 6 | 15 | 19~29 °C | 1.85~2.15 M |
| ref_eq_net_28238 | 4 | 6 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_28239 | 2 | 1 | 19~29 °C | -0.15~0.15 M |
| ref_eq_net_28240 | 1 | 0 | 19~29 °C | 2.85~3.15 M |

---

### Step 20: `build_system_catalog`
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

### Step 21: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_208",
  "ligand_id": "ligand_10103"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 4 species

### Zn^[2+] + Ammonia
**metal_id:** metal_208 | **ligand_id:** ligand_10103 | **ligand_def_HxL:** L  
**entries:** 21 | **species:** 4 | **vlm_count:** 21

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 6 |
| beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | [M] + [L]^2 <=> [ML2] | [ML2](aqueous), [M](aqueous), [L](aqueous) | 5 |
| beta_def_872 | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | [M] + [L]^3 <=> [ML3] | [ML3](aqueous), [M](aqueous), [L](aqueous) | 5 |
| beta_def_894 | [ML<sub>4</sub>]/[M][L]<sup>4</sup> | [M] + [L]^4 <=> [ML4] | [ML4](aqueous), [M](aqueous), [L](aqueous) | 5 |

**vlm_ids:** vlm_173394, vlm_173395, vlm_173396, vlm_173397, vlm_173398, … vlm_173412, vlm_173413, vlm_173414 (21 listed)

**equilibrium_maps:** 4 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_28282 | 4 | 6 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_28283 | 4 | 6 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_28284 | 4 | 6 | 19~29 °C | 1.85~2.15 M |
| ref_eq_net_28285 | 1 | 0 | 19~29 °C | -0.15~0.15 M |

---

### Step 23: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_10103 AND c.beta_definition_id = beta_def_812 AND c.metal_id IN (metal_94, metal_62, metal_33, metal_112, metal_41, metal_208) AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 80
}
```

[summary]
## search_stability — 53 row(s)

### ΔS — 6 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_41 | Cu^[2+] | ligand_10103 | Ammonia | L | N | 4 | 1 | 25 | 0~3 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_10103 | Ammonia | L | N | 3 | 1 | 25 | 0~2 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 2 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 2 | *** | 0 |
| metal_33 | Co^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 2 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 2 | *** | 0 |

### logK — 6 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_62 | Fe^[2+] | ligand_10103 | Ammonia | L | N | 6 | 1 | 25 | 0~6 | *** | 6 |
| metal_94 | Mn^[2+] | ligand_10103 | Ammonia | L | N | 6 | 1 | 25 | 0~5 | *** | 6 |
| metal_41 | Cu^[2+] | ligand_10103 | Ammonia | L | N | 5 | 1 | 25 | 0~3 | *** | 5 |
| metal_33 | Co^[2+] | ligand_10103 | Ammonia | L | N | 5 | 1 | 25 | 0~5 | *** | 5 |
| metal_208 | Zn^[2+] | ligand_10103 | Ammonia | L | N | 4 | 1 | 25 | 0~2 | *** | 4 |
| metal_112 | Ni^[2+] | ligand_10103 | Ammonia | L | N | 4 | 1 | 25 | 0~2 | *** | 4 |

### ΔH — 6 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_41 | Cu^[2+] | ligand_10103 | Ammonia | L | N | 4 | 1 | 25 | 0~3 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_10103 | Ammonia | L | N | 4 | 1 | 25 | 0~3 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 27 | 2 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 2 | *** | 0 |
| metal_33 | Co^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 2 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 2 | *** | 0 |

---
