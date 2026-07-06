# Q1.2.4 — Tool Results (batch 1)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Nickel(II)",
  "limit": 10
}
```

[summary]
## search_metals — 2 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_112 | Ni^[2+] | Ni | 2 | ✓ | [Ni+2] | InChI=1S/Ni/q+2 | beta_totN_149 | ligand_totN_1369 | vlm_totN_5325 |
| metal_113 | Ni^[3+] | Ni | 3 | ✓ | [Ni+3] | InChI=1S/Ni/q+3 | beta_totN_5 | ligand_totN_4 | vlm_totN_7 |

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "EDTA, ethylenediaminetetraacetic acid",
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
  "name": "ethylenediaminetetraacetate",
  "limit": 20
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
  "name": "edetic acid",
  "limit": 20
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 20

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6277 | Ethylenedinitrilotetraacetic acid (EDTA) | H4L | EDTA and derivatives | 596 | `O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O` | (-inf, H5L, -1.5, H4L, 2, H3L, 2.69, H2L, 6.13, HL, 9.52, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 1 | 100% |
| tertiary_amine | 1 | 100% |

---

### Step 6: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_112",
  "ligand_id": "ligand_6277"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 4 species

### Ni^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)
**metal_id:** metal_112 | **ligand_id:** ligand_6277 | **ligand_def_HxL:** H4L  
**entries:** 19 | **species:** 4 | **vlm_count:** 19

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_739 | [MH<sub>2</sub>L]/[MHL][H] | [MHL] + [H] <=> [MH2L] | [MH2L](aqueous), [MHL](aqueous), [H](aqueous) | 1 |
| beta_def_788 | [MHL]/[ML][H] | [ML] + [H] <=> [MHL] | [MHL](aqueous), [ML](aqueous), [H](aqueous) | 4 |
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 8 |
| beta_def_966 | [ML]/[M(OH)L][H] | [M(OH)L] + [H] <=> [ML] + [H2O] | [ML](aqueous), [H2O](aqueous), [M(OH)L](aqueous), [H](aqueous) | 6 |

**vlm_ids:** vlm_108585, vlm_108586, vlm_108587, vlm_108588, vlm_108589, … vlm_108601, vlm_108602, vlm_108603 (19 listed)

**equilibrium_maps:** 2 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_5023 | 3 | 3 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_5024 | 3 | 3 | 19~29 °C | 0.85~1.15 M |

---

### Step 8: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id = metal_112 AND c.ligand_id = ligand_6277)",
  "order_by": "n.node_count DESC, n.network_db_id ASC",
  "limit": 20
}
```

[summary]
## search_networks — 6 row(s)

> **Reference equilibrium networks** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### `Ni^[2+]` + Ethylenedinitrilotetraacetic acid (EDTA) — 2 network(s)
metal_id: metal_112 | ligand_id: ligand_6277 | ligand_def_HxL: H4L | ligand_SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O

| beta_def | equation |
|----------|----------|
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` |
| beta_def_966 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` |
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_739 | ``[MHL] + [H] <=> [MH2L]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_5023 | 3 | 3 | 20~30 | -0.05~0.25 | 3 | beta_def_966; beta_def_788; beta_def_812 | logK | -11.9~18.4 |
| ref_eq_net_5024 | 3 | 3 | 19~29 | 0.85~1.15 | 3 | beta_def_966; beta_def_739; beta_def_788 | logK | -12.9~3 |

#### Reference-state network: ref_eq_net_5023 (3 nodes)
> First network — reference conditions (T 20~30 °C, I -0.05~0.25 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_966 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` | logK | -11.9 |
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` | logK | 3.1 |
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 18.4 |

---
