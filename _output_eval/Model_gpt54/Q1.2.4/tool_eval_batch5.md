# Q1.2.4 — Tool Results (batch 5)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "nickel(II)",
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
  "name": "edetate",
  "limit": 10
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 6: `search_ligands`
**Args:**
```json
{
  "name": "ethylenedinitrilotetraacetic acid",
  "limit": 10
}
```

[summary]
## search_ligands — 10 result(s)

**stats:** 16 SQL matches · showing 10 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6050 | DL-1-Methylethylenedinitrilotetraacetic acid N,N'… | H2L | Amino Acids | 31 | `CC(CN(CC(N)=O)CC(=O)O)N(CC(N)=O)CC(=O)O` | (-inf, H4L, -1.5, H3L, -1.5, H2L, 3.8, HL, 7.56, L, +inf) |
| ligand_6051 | DL-1-Ethylethylenedinitrilotetraacetic acid N,N'-… | H2L | Amino Acids | 24 | `CCC(CN(CC(N)=O)CC(=O)O)N(CC(N)=O)CC(=O)O` | (-inf, H3L, -1.7, H2L, 3.7, HL, 7.58, L, +inf) |
| ligand_6052 | rac-1,2-Dimethylethylenedinitrilotetraacetic acid… | H2L | Amino Acids | 15 | `CC(C(C)N(CC(N)=O)CC(=O)O)N(CC(N)=O)CC(=O)O` | (-inf, H3L, -1.8, H2L, 3.9, HL, 8.41, L, +inf) |
| ligand_6053 | meso-1,2-Dimethylethylenedinitrilotetraacetic aci… | H2L | Amino Acids | 14 | `CC(C(C)N(CC(N)=O)CC(=O)O)N(CC(N)=O)CC(=O)O` | (-inf, H3L, -1.5, H2L, 3.63, HL, 6.87, L, +inf) |
| ligand_6277 | Ethylenedinitrilotetraacetic acid (EDTA) | H4L | EDTA and derivatives | 596 | `O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O` | (-inf, H5L, -1.5, H4L, 2, H3L, 2.69, H2L, 6.13, HL, 9.52, L, +inf) |
| ligand_6311 | Trimethylenedinitrilotetraacetic acid (TMDTA) | H4L | EDTA and derivatives | 186 | `O=C(O)CN(CCCN(CC(=O)O)CC(=O)O)CC(=O)O` | (-inf, H4L, 2.09, H3L, 2.63, H2L, 7.9, HL, 10.3, L, +inf) |
| ligand_6313 | Tetramethylenedinitrilotetraacetic acid | H4L | EDTA and derivatives | 156 | `O=C(O)CN(CCCCN(CC(=O)O)CC(=O)O)CC(=O)O` | (-inf, H4L, 2, H3L, 2.68, H2L, 8.98, HL, 10.45, L, +inf) |
| ligand_6314 | Pentamethylenedinitrilotetraacetic acid | H4L | EDTA and derivatives | 93 | `O=C(O)CN(CCCCCN(CC(=O)O)CC(=O)O)CC(=O)O` | (-inf, H4L, 2.31, H3L, 2.7, H2L, 9.44, HL, 10.54, L, +inf) |
| ligand_6315 | Hexamethylenedinitrilotetraacetic acid | H4L | EDTA and derivatives | 135 | `O=C(O)CN(CCCCCCN(CC(=O)O)CC(=O)O)CC(=O)O` | (-inf, H4L, -2.4, H3L, 2.76, H2L, 9.7, HL, 10.64, L, +inf) |
| ligand_6316 | Octamethylenedinitrilotetraacetic acid | H4L | EDTA and derivatives | 66 | `O=C(O)CN(CCCCCCCCN(CC(=O)O)CC(=O)O)CC(=O)O` | (-inf, H4L, 2, H3L, 2.75, H2L, 9.86, HL, 10.66, L, +inf) |

### Functional groups across all SQL matches (12 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 12 | 100% |
| tertiary_amine | 12 | 100% |
| amide | 4 | 33% |

---

### Step 7: `build_system_catalog`
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

### Step 9: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id = metal_112 AND c.ligand_id = ligand_6277)",
  "order_by": "n.node_count DESC, n.network_db_id ASC",
  "limit": 10
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
