# Q1.2.1 — Tool Results (batch 3)

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
  "name": "EDTA",
  "limit": 10
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 5 SQL matches · showing 5 · limit 10

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
  "metal_id": "metal_41",
  "ligand_id": "ligand_6277"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 4 species

### Cu^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)
**metal_id:** metal_41 | **ligand_id:** ligand_6277 | **ligand_def_HxL:** H4L  
**entries:** 20 | **species:** 4 | **vlm_count:** 20

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_739 | [MH<sub>2</sub>L]/[MHL][H] | [MHL] + [H] <=> [MH2L] | [MH2L](aqueous), [MHL](aqueous), [H](aqueous) | 2 |
| beta_def_788 | [MHL]/[ML][H] | [ML] + [H] <=> [MHL] | [MHL](aqueous), [ML](aqueous), [H](aqueous) | 4 |
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 8 |
| beta_def_966 | [ML]/[M(OH)L][H] | [M(OH)L] + [H] <=> [ML] + [H2O] | [ML](aqueous), [H2O](aqueous), [M(OH)L](aqueous), [H](aqueous) | 6 |

**vlm_ids:** vlm_108604, vlm_108605, vlm_108606, vlm_108607, vlm_108608, … vlm_108621, vlm_108622, vlm_108623 (20 listed)

**equilibrium_maps:** 2 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_5025 | 4 | 5 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_5026 | 3 | 3 | 19~29 °C | 0.85~1.15 M |

---

### Step 6: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_41 AND c.ligand_id = ligand_6277 AND c.beta_definition_id = beta_def_812)",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[summary]
## search_stability — 8 row(s)

### `Cu^[2+]` + Ethylenedinitrilotetraacetic acid (EDTA) — 8 measurement(s)
metal_id: metal_41 | ligand_id: ligand_6277
ligand_HxL_def: H4L | ligand_SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_108611 | *** | beta_def_812 | ΔS | 244.8 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108604 | ref_eq_map_5019 | beta_def_812 | logK | 18.78 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108605 | *** | beta_def_812 | ΔH | -33.1 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108606 | *** | beta_def_812 | ΔH | -34.3 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108609 | *** | beta_def_812 | ΔH | -37.2 | 35 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108608 | *** | beta_def_812 | ΔH | -38.1 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108607 | *** | beta_def_812 | ΔH | -38.5 | 15 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108610 | *** | beta_def_812 | ΔH | -39.7 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |

---

### Step 7: `inspect_card`
**Args:**
```json
{
  "prefix_id": "vlm_108604"
}
```

[summary]
## inspect_card — VLM | vlm_108604

### Metal
**metal_id:** metal_41 | **metal_name:** Cu^[2+]  
**metal_SMILES:** `[Cu+2]`  
**metal_InChi:** `InChI=1S/Cu/q+2`  

### Ligand
**ligand_id:** ligand_6277 | **ligand_name:** Ethylenedinitrilotetraacetic acid (EDTA)  
**ligand_HxL_definition:** H4L  
**ligand_SMILES:** `O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O`  
**ligand_InChi:** `InChI=1S/C10H16N2O8/c13-7(14)3-11(4-8(15)16)1-2-12(5-9(17)18)6-10(19)20/h1-6H2,(H,13,14)(H,15,16)(H,17,18)(H,19,20)`  

### Stability
**vlm_id:** vlm_108604  
**beta_definition_id:** beta_def_812 | **beta_definition_name:** [ML]/[M][L]  
**data_type:** log_K | **log_K:** 18.78  
**temperature:** 25.0 °C | **ionic_strength:** 0.1 M  
**uncertainty:** +/-8  
**solvent:** H_[2]O | **reaction_type:** homogeneous_aqueous  
**equation:** [M] + [L] <=> [ML]  
**Ligand_HxL_involved:** [L] | **pKa_bracket_involved:** (9.52, L, +inf)  
**LHS_species:** [M], [L] | **RHS_species:** [ML]  
**notes:** ['48']  

### Networks
1 network(s)

| network_id | Nodes | Edges | node_id | dup? |
|------------|-------|-------|---------|------|
| ref_eq_net_5025 | 4 | 5 | eq_node_10648 |  |

**total_citations:** 49

---
