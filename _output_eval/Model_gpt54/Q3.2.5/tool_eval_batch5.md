# Q3.2.5 — Tool Results (batch 5)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Zinc",
  "limit": 10
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_208 | Zn^[2+] | Zn | 2 | ✓ | [Zn+2] | InChI=1S/Zn/q+2 | beta_totN_122 | ligand_totN_1169 | vlm_totN_4095 |

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "EDTA",
  "limit": 20
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 5 SQL matches · showing 5 · limit 20

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6118 | 6,11,18,23-Tetraoxo-1,4,7,10,13,16,19,… (24edtaen) | *** | Aza macrocycles with car… | 15 | *** | (-inf, H4L, 3.3, H3L, 4.18, H2L, 7.26, HL, 7.78, L, +inf) |
| ligand_6275 | N-(2-Hydroxyethyl)ethylenedinitrilotriace… (HEDTA) | H3L | EDTA and derivatives | 237 | `O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O` | (-inf, H3L, 2.62, H2L, 5.38, HL, 9.7, L, +inf) |
| ligand_6277 | Ethylenedinitrilotetraacetic acid (EDTA) | H4L | EDTA and derivatives | 596 | `O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O` | (-inf, H5L, -1.5, H4L, 2, H3L, 2.69, H2L, 6.13, HL, 9.52, L, +inf) |
| ligand_6335 | Oxybis(ethylenenitrilo)tetraacetic acid (EEDTA) | H4L | EDTA and derivatives | 124 | `O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O` | (-inf, H4L, -1.8, H3L, 2.76, H2L, 8.75, HL, 9.39, L, +inf) |
| ligand_6348 | Thiobis(ethylenenitrilo)tetraacetic acid (TEDTA) | H4L | EDTA and derivatives | 101 | `O=C(O)CN(CCSCCN(CC(=O)O)CC(=O)O)CC(=O)O` | (-inf, H4L, 2, H3L, 2.68, H2L, 8.37, HL, 9.31, L, +inf) |

### Functional groups across all SQL matches (4 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 4 | 100% |
| tertiary_amine | 4 | 100% |
| ether | 1 | 25% |
| hydroxyl | 1 | 25% |
| thioether | 1 | 25% |

---

### Step 4: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_208",
  "ligand_id": "ligand_6277"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 4 species

### Zn^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)
**metal_id:** metal_208 | **ligand_id:** ligand_6277 | **ligand_def_HxL:** H4L  
**entries:** 18 | **species:** 4 | **vlm_count:** 18

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_739 | [MH<sub>2</sub>L]/[MHL][H] | [MHL] + [H] <=> [MH2L] | [MH2L](aqueous), [MHL](aqueous), [H](aqueous) | 1 |
| beta_def_788 | [MHL]/[ML][H] | [ML] + [H] <=> [MHL] | [MHL](aqueous), [ML](aqueous), [H](aqueous) | 5 |
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 6 |
| beta_def_966 | [ML]/[M(OH)L][H] | [M(OH)L] + [H] <=> [ML] + [H2O] | [ML](aqueous), [H2O](aqueous), [M(OH)L](aqueous), [H](aqueous) | 6 |

**vlm_ids:** vlm_108707, vlm_108708, vlm_108709, vlm_108710, vlm_108711, … vlm_108722, vlm_108723, vlm_108724 (18 listed)

**equilibrium_maps:** 5 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_5056 | 3 | 3 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_5057 | 4 | 5 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_5058 | 1 | 0 | 19~29 °C | 0.35~0.65 M |
| ref_eq_net_5059 | 1 | 0 | 19~29 °C | -0.15~0.15 M |
| ref_eq_net_5060 | 1 | 0 | 19~29 °C | 2.85~3.15 M |

---

### Step 6: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND c.ligand_id = ligand_6277 AND c.beta_definition_id = beta_def_812 AND s.temperature_c >= 19 AND s.temperature_c <= 30)",
  "order_by": "s.ionic_strength_mol_l ASC",
  "limit": 50
}
```

[summary]
## search_stability — 6 row(s)

### `Zn^[2+]` + Ethylenedinitrilotetraacetic acid (EDTA) — 6 measurement(s)
metal_id: metal_208 | ligand_id: ligand_6277
ligand_HxL_def: H4L | ligand_SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_108710 | ref_eq_map_5053 | beta_def_812 | logK | 18 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108707 | ref_eq_map_5050 | beta_def_812 | logK | 16.5 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108711 | *** | beta_def_812 | ΔH | -19.7 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108712 | *** | beta_def_812 | ΔS | 250.2 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108708 | ref_eq_map_5052 | beta_def_812 | logK | 15.7 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108709 | ref_eq_map_5051 | beta_def_812 | logK | 15.7 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |

---

### Step 7: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND c.ligand_id = ligand_6277 AND nd.beta_definition_id = beta_def_812 AND m.condition_temp_min >= 19 AND m.condition_temp_max <= 30)",
  "order_by": "m.condition_ionic_min ASC",
  "limit": 20
}
```

[summary]
## search_networks — 9 row(s)

> **Reference equilibrium networks** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### `Zn^[2+]` + Ethylenedinitrilotetraacetic acid (EDTA) — 4 network(s)
metal_id: metal_208 | ligand_id: ligand_6277 | ligand_def_HxL: H4L | ligand_SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O

| beta_def | equation |
|----------|----------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` |
| beta_def_966 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` |
| beta_def_739 | ``[MHL] + [H] <=> [MH2L]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_5059 | 1 | 0 | 19~29 | -0.15~0.15 | 1 | beta_def_812 | logK | 18 |
| ref_eq_net_5056 | 3 | 3 | 20~30 | -0.05~0.25 | 3 | beta_def_966; beta_def_788; beta_def_812 | logK | -11.6~16.5 |
| ref_eq_net_5058 | 1 | 0 | 19~29 | 0.35~0.65 | 1 | beta_def_812 | logK | 15.7 |
| ref_eq_net_5057 | 4 | 5 | 19~29 | 0.85~1.15 | 4 | 4 diff beta_def | logK | -12~15.7 |

#### Reference-state network: ref_eq_net_5059 (1 nodes)
> First network — reference conditions (T 19~29 °C, I -0.15~0.15 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 18 |

---
