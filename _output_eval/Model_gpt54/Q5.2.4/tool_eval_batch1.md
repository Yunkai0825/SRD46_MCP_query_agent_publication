# Q5.2.4 — Tool Results (batch 1)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Plutonium(IV)",
  "limit": 10
}
```

[summary]
## search_metals — 4 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_148 | Pu^[3+] | Pu | 3 | ✓ | [Pu+3] | InChI=1S/Pu/q+3 | beta_totN_7 | ligand_totN_12 | vlm_totN_28 |
| metal_149 | Pu^[4+] | Pu | 4 | ✓ | [Pu+4] | InChI=1S/Pu/q+4 | beta_totN_6 | ligand_totN_11 | vlm_totN_36 |
| metal_150 | PuO_[2]^[2+] | Pu | 2 |  | *** | *** | beta_totN_10 | ligand_totN_22 | vlm_totN_76 |
| metal_151 | PuO_[2]^[+] | Pu | 1 |  | *** | *** | beta_totN_2 | ligand_totN_6 | vlm_totN_6 |

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "Aspirin, Acetylsalicylic acid, Acetylsalicylate, Salicylic acid, Salicylate",
  "limit": 20
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
  "name": "salicyl",
  "limit": 20
}
```

[summary]
## search_ligands — 20 result(s)

**stats:** 60 SQL matches · showing 20 · limit 20

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8636 | 2-Hydroxybenzoic acid 2-(dihy… (Salicyl phosphate) | H4L | Carboxylic acids | 9 | `O=C(O)c1ccccc1OP(=O)(O)O` | (-inf, H2L, 3.69, HL, 6.61, L, +inf) |
| ligand_8701 | 2-Acetoxybenzoic acid (Acetylsalicylic acid) | HL | Carboxylic acids keto | 5 | `CC(=O)Oc1ccccc1C(=O)O` | (-inf, HL, 3.45, L, +inf) |
| ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | H2L | Phenols salicylic acids | 227 | `O=C(O)c1ccccc1O` | (-inf, H2L, 2.8, HL, 2.8, L, +inf) |
| ligand_9265 | 2-Hydroxy-3-methylbenzoic acid (3-Methylsalicylic… | H2L | Phenols salicylic acids | 9 | `Cc1cccc(C(=O)O)c1O` | (-inf, H2L, 2.83, HL, 2.83, L, +inf) |
| ligand_9266 | 2-Hydroxy-4-methylbenzoic acid (4-Methylsalicylic… | H2L | Phenols salicylic acids | 8 | `Cc1ccc(C(=O)O)c(O)c1` | (-inf, H2L, 2.96, HL, 2.96, L, +inf) |
| ligand_9267 | 2-Hydroxy-5-methylbenzoic acid (5-Methylsalicylic… | H2L | Phenols salicylic acids | 6 | `Cc1ccc(O)c(C(=O)O)c1` | (-inf, H2L, 2.88, HL, 2.88, L, +inf) |
| ligand_9268 | 2-Hydroxy-6-methylbenzoi… (6-Methylsalicylic acid) | H2L | Phenols salicylic acids | 5 | `Cc1cccc(O)c1C(=O)O` | (-inf, H2L, 3.16, HL, +inf) |
| ligand_9269 | 2-Hydroxy-3-(2-propyl… (3-Isopropylsalicylic acid) | H2L | Phenols salicylic acids | 2 | `CC(C)c1cccc(C(=O)O)c1O` | (-inf, H2L, 2.76, HL, +inf) |
| ligand_9274 | 5-Fluoro-2-hydroxybenzoi… (5-Fluorosalicylic acid) | H2L | Phenols salicylic acids | 3 | `O=C(O)c1cc(F)ccc1O` | (-inf, H2L, 2.56, HL, 2.56, L, +inf) |
| ligand_9275 | 5-Chloro-2-hydroxybenzoi… (5-Chlorosalicylic acid) | H2L | Phenols salicylic acids | 19 | `O=C(O)c1cc(Cl)ccc1O` | (-inf, H2L, 2.46, HL, 2.46, L, +inf) |
| ligand_9276 | 6-Chloro-2-hydroxybenzoi… (6-Chlorosalicylic acid) | H2L | Phenols salicylic acids | 1 | `O=C(O)c1c(O)cccc1Cl` | (-inf, H2L, 2.63, HL, +inf) |
| ligand_9277 | 5-Bromo-2-hydroxybenzoic … (5-Bromosalicylic acid) | H2L | Phenols salicylic acids | 11 | `O=C(O)c1cc(Br)ccc1O` | (-inf, H2L, 2.44, HL, 2.44, L, +inf) |
| ligand_9278 | 2-Hydroxy-5-iodobenzoic ac… (5-Iodosalicylic acid) | H2L | Phenols salicylic acids | 10 | `O=C(O)c1cc(I)ccc1O` | (-inf, H2L, -2.54, HL, -2.54, L, +inf) |
| ligand_9279 | 2-Hydroxy-3-nitrobenzoic … (3-Nitrosalicylic acid) | H2L | Phenols salicylic acids | 14 | `O=C(O)c1cccc([N+](=O)[O-])c1O` | (-inf, H2L, -1.73, HL, 9.87, L, +inf) |
| ligand_9280 | 2-Hydroxy-4-nitrobenzoic … (4-Nitrosalicylic acid) | H2L | Phenols salicylic acids | 4 | `O=C(O)c1ccc([N+](=O)[O-])cc1O` | (-inf, H2L, 2.05, HL, 10.91, L, +inf) |
| ligand_9281 | 2-Hydroxy-5-nitrobenzoic … (5-Nitrosalicylic acid) | H2L | Phenols salicylic acids | 36 | `O=C(O)c1cc([N+](=O)[O-])ccc1O` | (-inf, H2L, -1.94, HL, 9.9, L, +inf) |
| ligand_9282 | 2-Hydroxy-6-nitrobenzoic … (6-Nitrosalicylic acid) | H2L | Phenols salicylic acids | 4 | `O=C(O)c1c(O)cccc1[N+](=O)[O-]` | (-inf, H2L, 1.99, HL, 9.04, L, +inf) |
| ligand_9283 | 2-Hydroxy-3,5-dinitro… (3,5-Dinitrosalicylic acid) | H2L | Phenols salicylic acids | 35 | `O=C(O)c1cc([N+](=O)[O-])cc([N+](=O)[O-])c1O` | (-inf, H2L, -0.3, HL, 7.07, L, +inf) |
| ligand_9284 | 2-Hydroxy-5-sulfobenzoic … (5-Sulfosalicylic acid) | H3L | Phenols salicylic acids | 127 | `O=C(O)c1cc(S(=O)(=O)O)ccc1O` | (-inf, H2L, 2.48, HL, 11.85, L, +inf) |
| ligand_9285 | 3-Bromo-2-hydroxy… (3-Bromo-5-sulfosalicylic acid) | H3L | Phenols salicylic acids | 89 | `O=C(O)c1cc(S(=O)(=O)O)cc(Br)c1O` | (-inf, H2L, 2.02, HL, 10.52, L, +inf) |

### Functional groups across all SQL matches (41 parseable SMILES)

| group | count | % |
|-------|-------|---|
| aromatic_ring | 41 | 100% |
| hydroxyl | 40 | 98% |
| phenol | 39 | 95% |
| carboxyl | 27 | 66% |
| halide | 10 | 24% |
| aldehyde | 9 | 22% |
| tertiary_amine | 8 | 20% |
| sulfonate | 5 | 12% |
| amide | 3 | 7% |
| primary_amine | 3 | 7% |
| ester | 2 | 5% |
| imine | 2 | 5% |
| oxime | 2 | 5% |
| nitrile | 1 | 2% |
| phosphate | 1 | 2% |

---

### Step 5: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_149",
  "ligand_id": "ligand_8701"
}
```

[summary]
[CATALOG]
## build_system_catalog

*(no pairs found)*

**summary:** {'n_metals': 0, 'n_ligands': 0, 'n_pairs': 0, 'total_species': 0}

---

### Step 7: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_149 AND c.ligand_id = ligand_8701)",
  "order_by": "s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability

*(no results)*

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_149 AND c.ligand_id = ligand_9257)",
  "order_by": "s.constant_value DESC",
  "limit": 20
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
  "where": "(c.metal_id = metal_149)",
  "order_by": "c.ligand_name_SRD ASC, s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability — 36 row(s)

### logK — 11 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_149 | Pu^[4+] | ligand_10109 | Nitrate ion | *** | *** | 7 | 3 | 20~25 | 0~4 | *** | 4 |
| metal_149 | Pu^[4+] | ligand_9526 | Pentane-2,4-dione (Acetylac… | *** | *** | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_149 | Pu^[4+] | ligand_10163 | Chloride ion | *** | *** | 3 | 1 | 20~25 | 1~4 | *** | 3 |
| metal_149 | Pu^[4+] | ligand_10076 | Hydroxide ion | *** | *** | 3 | 1 | 25 | 0.5~2 | *** | 3 |
| metal_149 | Pu^[4+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 2 | 2 | 25 | 4 | *** | 1 |
| metal_149 | Pu^[4+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 2 | 1 | 25 | 2 | *** | 2 |
| metal_149 | Pu^[4+] | ligand_10143 | Hydrogen peroxide | H2L | OO | 2 | 2 | 25 | 0.5 | *** | 1 |
| metal_149 | Pu^[4+] | ligand_10148 | Hydrogen sulfate ion (Sulfu… | HL | O=S(=O)([O-])O | 2 | 2 | 25 | 2 | *** | 1 |
| metal_149 | Pu^[4+] | ligand_10168 | Bromide ion | *** | *** | 1 | 1 | 25 | 2 | *** | 1 |
| metal_149 | Pu^[4+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.5 | *** | 1 |
| metal_149 | Pu^[4+] | ligand_10151 | Hydrogen amidosulfate (Sulf… | HL | NS(=O)(=O)O | 1 | 1 | 25 | 2 | *** | 1 |

### ΔH — 4 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_149 | Pu^[4+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 1 | 1 | 25 | 2 | *** | 0 |
| metal_149 | Pu^[4+] | ligand_10148 | Hydrogen sulfate ion (Sulfu… | HL | O=S(=O)([O-])O | 1 | 1 | 25 | 2 | *** | 0 |
| metal_149 | Pu^[4+] | ligand_10076 | Hydroxide ion | *** | *** | 1 | 1 | 25 | 2 | *** | 0 |
| metal_149 | Pu^[4+] | ligand_10109 | Nitrate ion | *** | *** | 1 | 1 | 25 | 2 | *** | 0 |

### ΔS — 4 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_149 | Pu^[4+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 1 | 1 | 25 | 2 | *** | 0 |
| metal_149 | Pu^[4+] | ligand_10148 | Hydrogen sulfate ion (Sulfu… | HL | O=S(=O)([O-])O | 1 | 1 | 25 | 2 | *** | 0 |
| metal_149 | Pu^[4+] | ligand_10076 | Hydroxide ion | *** | *** | 1 | 1 | 25 | 2 | *** | 0 |
| metal_149 | Pu^[4+] | ligand_10109 | Nitrate ion | *** | *** | 1 | 1 | 25 | 2 | *** | 0 |

---

### Step 10: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id = 149)",
  "order_by": "c.ligand_name ASC",
  "limit": 100
}
```

[summary]
## search_networks — 28 row(s)

> **Reference equilibrium networks (compact)** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### Beta-definition legend
| beta_def | equation |
|----------|----------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |
| beta_def_572 | ``[M]^2 + [H2L] + [H2O] <=> [M2(OH)L] + [H]^3`` |
| beta_def_527 | ``[M]^2 + [H2L]^2 <=> [M2L2] + [H]^4`` |
| beta_def_872 | ``[M] + [L]^3 <=> [ML3]`` |
| beta_def_894 | ``[M] + [L]^4 <=> [ML4]`` |

### Metal-ligand pair summary
| metal | metal_id | ligand | ligand_id | HxL | T_range | I_range | net_count | max_nodes | ligand_SMILES |
|-------|----------|--------|-----------|-----|---------|---------|-----------|----------|---------------|
| `Pu^[4+]` | metal_149 | Bromide ion | ligand_10168 | *** | 16.5~31.5 | 1.775~2.225 | 1 | 1 | *** |
| `Pu^[4+]` | metal_149 | Chloride ion | ligand_10163 | *** | 12.5~31.5 | 0.775~4.225 | 3 | 1 | *** |
| `Pu^[4+]` | metal_149 | Diethylenetrinitrilopentaacetic acid (D… | ligand_6356 | H5L | 12.5~27.5 | 0.275~0.725 | 1 | 1 | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O |
| `Pu^[4+]` | metal_149 | Ethanedioic acid (Oxalic acid) | ligand_8872 | H2L | 16.5~31.5 | 3.775~4.225 | 1 | 2 | O=C(O)C(=O)O |
| `Pu^[4+]` | metal_149 | Hydrogen amidosulfate (Sulfamic acid) | ligand_10151 | HL | 16.5~31.5 | 1.775~2.225 | 1 | 1 | NS(=O)(=O)O |
| `Pu^[4+]` | metal_149 | Hydrogen fluoride (Hydrofluoric acid) | ligand_10162 | HL | 16.5~31.5 | 1.775~2.225 | 2 | 1 | F |
| `Pu^[4+]` | metal_149 | Hydrogen peroxide | ligand_10143 | H2L | 16.5~31.5 | 0.275~0.725 | 1 | 2 | OO |
| `Pu^[4+]` | metal_149 | Hydrogen sulfate ion (Sulfuric acid) | ligand_10148 | HL | 16.5~31.5 | 1.775~2.225 | 1 | 2 | O=S(=O)([O-])O |
| `Pu^[4+]` | metal_149 | Hydroxide ion | ligand_10076 | *** | 16.5~31.5 | 0.275~2.225 | 3 | 1 | *** |
| `Pu^[4+]` | metal_149 | Nitrate ion | ligand_10109 | *** | 15~30 | -0.05~4.15 | 4 | 3 | *** |
| `Pu^[4+]` | metal_149 | Pentane-2,4-dione (Acetylacetone) | ligand_9526 | *** | 20~30 | -0.05~0.25 | 1 | 4 | *** |

### Max-node network per pair
| metal | metal_id | ligand | ligand_id | max_net_id | max_nodes | max_edge_counts | max_T_range | max_I_range | max_vlm_counts | max_beta_def_ids | max_type | max_values |
|-------|----------|--------|----------|------------|-----------|------------------|-------------|-------------|----------------|------------------|----------|------------|
| `Pu^[4+]` | metal_149 | Bromide ion | ligand_10168 | ref_eq_net_30048 | 1 | 0 | 16.5~31.5 | 1.775~2.225 | 1 | beta_def_812 | logK | 0.33 |
| `Pu^[4+]` | metal_149 | Chloride ion | ligand_10163 | ref_eq_net_29818 | 1 | 0 | 16.5~31.5 | 0.775~1.225 | 1 | beta_def_812 | logK | 0.14 |
| `Pu^[4+]` | metal_149 | Diethylenetrinitrilopentaacetic acid (D… | ligand_6356 | ref_eq_net_6721 | 1 | 0 | 12.5~27.5 | 0.275~0.725 | 1 | beta_def_812 | logK | -29.5 |
| `Pu^[4+]` | metal_149 | Ethanedioic acid (Oxalic acid) | ligand_8872 | ref_eq_net_20006 | 2 | 1 | 16.5~31.5 | 3.775~4.225 | 2 | beta_def_812; beta_def_840 | logK | 8.3~14.9 |
| `Pu^[4+]` | metal_149 | Hydrogen amidosulfate (Sulfamic acid) | ligand_10151 | ref_eq_net_29413 | 1 | 0 | 16.5~31.5 | 1.775~2.225 | 1 | beta_def_812 | logK | 0.11 |
| `Pu^[4+]` | metal_149 | Hydrogen fluoride (Hydrofluoric acid) | ligand_10162 | ref_eq_net_29637 | 1 | 0 | 16.5~31.5 | 1.775~2.225 | 1 | beta_def_812 | logK | 7.49 |
| `Pu^[4+]` | metal_149 | Hydrogen peroxide | ligand_10143 | ref_eq_net_29035 | 2 | 1 | 16.5~31.5 | 0.275~0.725 | 2 | beta_def_572; beta_def_527 | logK | 6.94~8.8 |
| `Pu^[4+]` | metal_149 | Hydrogen sulfate ion (Sulfuric acid) | ligand_10148 | ref_eq_net_29258 | 2 | 1 | 16.5~31.5 | 1.775~2.225 | 2 | beta_def_812; beta_def_840 | logK | 3.8~6.6 |
| `Pu^[4+]` | metal_149 | Hydroxide ion | ligand_10076 | ref_eq_net_27406 | 1 | 0 | 16.5~31.5 | 0.275~0.725 | 1 | beta_def_812 | logK | 12.1 |
| `Pu^[4+]` | metal_149 | Nitrate ion | ligand_10109 | ref_eq_net_28486 | 3 | 3 | 15~25 | 3.85~4.15 | 3 | beta_def_812; beta_def_872; beta_def_840 | logK | 0.74~1.37 |
| `Pu^[4+]` | metal_149 | Pentane-2,4-dione (Acetylacetone) | ligand_9526 | ref_eq_net_25226 | 4 | 6 | 20~30 | -0.05~0.25 | 4 | 4 diff beta_def | logK | 10.5~34.1 |

### Global max-node network: `Pu^[4+]` + Pentane-2,4-dione (Acetylacetone)
network_id: ref_eq_net_25226 | metal_id: metal_149 | ligand_id: ligand_9526 | ligand_def_HxL: *** | nodes: 4

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 10.5 |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` | logK | 19.7 |
| beta_def_872 | ``[M] + [L]^3 <=> [ML3]`` | logK | 28.1 |
| beta_def_894 | ``[M] + [L]^4 <=> [ML4]`` | logK | 34.1 |

---

### Step 11: `search_similar_ligands`
**Args:**
```json
{
  "ligand_id": "ligand_8701",
  "top_k": 10,
  "metal_ids": [
    "metal_149"
  ]
}
```

[TOOL ERROR] search_similar_ligands: Error executing tool search_similar_ligands: 2 validation errors for search_similar_ligandsArguments
metal_ids.str
  Input should be a valid string [type=string_type, input_value=['metal_149'], input_type=list]
    For further information visit https://errors.pydantic.dev/2.11/v/string_type
metal_ids.list[int].0
  Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='metal_149', input_type=str]
    For further information visit https://errors.pydantic.dev/2.11/v/int_parsing

---
