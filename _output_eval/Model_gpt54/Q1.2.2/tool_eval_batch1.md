# Q1.2.2 — Tool Results (batch 1)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Cd(II)",
  "limit": 10
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_26 | Cd^[2+] | Cd | 2 | ✓ | [Cd+2] | InChI=1S/Cd/q+2 | beta_totN_95 | ligand_totN_818 | vlm_totN_2828 |

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "chloride",
  "limit": 10
}
```

[summary]
## search_ligands — 10 result(s)

**stats:** 12 SQL matches · showing 10 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5923 | L-[1-Carboxy-2-(4-hydroxypheny… (Tyrosine betaine) | H2L | Amino Acids | 1 | `C[N+](C)(C)C(Cc1ccc(O)cc1)C(=O)O.[Cl-]` | (-inf, HL, 9.63, L, +inf) |
| ligand_5947 | DL-[1-Carboxy-2-(2-mercapto-4-imi… (Ergothioneine) | H2L | Amino Acids | 4 | `C[N+](C)(C)C(Cc1cnc(S)[nH]1)C(=O)O.[Cl-]` | (-inf, HL, 10.44, L, +inf) |
| ligand_6769 | 3-Carboxy-N-methylpyridi… (Nicotinic acid betaine) | HL | Pyridine carboxylic acids | 1 | `C[n+]1cccc(C(=O)O)c1` | (-inf, HL, 2.04, L, +inf) |
| ligand_7954 | 3-Hydroxy-N-methylpyridinium (chloride) | HL | Pyridines (azines) | 3 | `C[n+]1cccc(O)c1` | (-inf, HL, 4.81, L, +inf) |
| ligand_7968 | 3-Hydroxy-N,2,5-… (Deoxypyridoxal N-methochloride) | HL | Pyridines (azines) | 2 | `Cc1c[n+](C)c(C)c(O)c1C=O` | (-inf, HL, 4.34, L, 4.34, H-1L, +inf) |
| ligand_8251 | 3-[(4-Amino-2-methyl-5-pyrimidinyl)met… (Thiamine) | L | Pyrimidines | 1 | `Cc1ncc(C[n+]2csc(CCO)c2C)c(N)n1` | (-inf, HL, 4.79, L, +inf) |
| ligand_9333 | 3-Hydroxyphenyltrimethylammonium (chloride) | HL | Phenols | 3 | `C[N+](C)(C)c1cccc(O)c1` | (-inf, HL, 8.06, L, +inf) |
| ligand_9334 | 4-Hydroxyphenyltrimethylammonium (chloride) | HL | Phenols | 3 | `C[N+](C)(C)c1ccc(O)cc1` | (-inf, HL, 8.35, L, +inf) |
| ligand_10163 | Chloride ion | *** | Inorganic ligands | 546 | *** | *** |
| ligand_10207 | DL-(3-Amino-3-carbo… (S-Methylmethionine chloride) | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (8 parseable SMILES)

| group | count | % |
|-------|-------|---|
| aromatic_ring | 8 | 100% |
| hydroxyl | 6 | 75% |
| carboxyl | 3 | 38% |
| phenol | 3 | 38% |
| pyridine | 3 | 38% |
| halide | 2 | 25% |
| aldehyde | 1 | 12% |
| primary_amine | 1 | 12% |
| thiazole | 1 | 12% |
| thioether | 1 | 12% |
| thiol | 1 | 12% |

---

### Step 4: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_26",
  "ligand_id": "ligand_10163"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 3 species

### Cd^[2+] + Chloride ion
**metal_id:** metal_26 | **ligand_id:** ligand_10163 | **ligand_def_HxL:** ***  
**entries:** 30 | **species:** 3 | **vlm_count:** 30

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 11 |
| beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | [M] + [L]^2 <=> [ML2] | [ML2](aqueous), [M](aqueous), [L](aqueous) | 10 |
| beta_def_872 | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | [M] + [L]^3 <=> [ML3] | [ML3](aqueous), [M](aqueous), [L](aqueous) | 9 |

**vlm_ids:** vlm_177542, vlm_177543, vlm_177544, vlm_177545, vlm_177546, … vlm_177569, vlm_177570, vlm_177571 (30 listed)

**equilibrium_maps:** 7 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_29910 | 3 | 3 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_29911 | 3 | 3 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_29912 | 3 | 3 | 19~29 °C | 1.85~2.15 M |
| ref_eq_net_29913 | 3 | 3 | 19~29 °C | 2.85~3.15 M |
| ref_eq_net_29914 | 3 | 3 | 19~29 °C | 3.85~4.15 M |
| ref_eq_net_29915 | 2 | 1 | 19~29 °C | 0.35~0.65 M |
| ref_eq_net_29916 | 1 | 0 | 19~29 °C | -0.15~0.15 M |

---

### Step 6: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_26 AND c.ligand_id = ligand_10163)",
  "order_by": "c.beta_definition_id ASC, s.constant_value ASC",
  "limit": 100
}
```

[summary]
## search_stability — 30 row(s)

### `Cd^[2+]` + Chloride ion — 30 measurement(s)
metal_id: metal_26 | ligand_id: ligand_10163
ligand_HxL_def: *** | ligand_SMILES: ***

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_177550 | *** | beta_def_812 | ΔH | -0.4 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177549 | *** | beta_def_812 | ΔH | 1.3 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177543 | ref_eq_map_29796 | beta_def_812 | logK | 1.35 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177544 | ref_eq_map_29792 | beta_def_812 | logK | 1.35 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177545 | ref_eq_map_29793 | beta_def_812 | logK | 1.44 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177542 | ref_eq_map_29791 | beta_def_812 | logK | 1.52 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177546 | ref_eq_map_29794 | beta_def_812 | logK | 1.54 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177547 | ref_eq_map_29795 | beta_def_812 | logK | 1.66 | 25 | 4 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177548 | ref_eq_map_29797 | beta_def_812 | logK | 1.98 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177552 | *** | beta_def_812 | ΔS | 28 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177551 | *** | beta_def_812 | ΔS | 30.1 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177560 | *** | beta_def_840 | ΔH | 0 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_177553 | ref_eq_map_29796 | beta_def_840 | logK | 1.7 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_177554 | ref_eq_map_29792 | beta_def_840 | logK | 1.7 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_177555 | ref_eq_map_29793 | beta_def_840 | logK | 1.9 | 25 | 2 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_177556 | ref_eq_map_29794 | beta_def_840 | logK | 2.2 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_177557 | ref_eq_map_29795 | beta_def_840 | logK | 2.4 | 25 | 4 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_177558 | ref_eq_map_29791 | beta_def_840 | logK | 2.6 | 25 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_177559 | *** | beta_def_840 | ΔH | 3.8 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_177562 | *** | beta_def_840 | ΔS | 42.3 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_177561 | *** | beta_def_840 | ΔS | 45.2 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_177563 | ref_eq_map_29792 | beta_def_872 | logK | 1.5 | 25 | 1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_177564 | ref_eq_map_29793 | beta_def_872 | logK | 1.9 | 25 | 2 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_177565 | ref_eq_map_29794 | beta_def_872 | logK | 2.3 | 25 | 3 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_177567 | ref_eq_map_29791 | beta_def_872 | logK | 2.4 | 25 | 0 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_177566 | ref_eq_map_29795 | beta_def_872 | logK | 2.8 | 25 | 4 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_177569 | *** | beta_def_872 | ΔH | 7.9 | 25 | 3 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_177568 | *** | beta_def_872 | ΔH | 10 | 25 | 1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_177570 | *** | beta_def_872 | ΔS | 62.3 | 25 | 1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_177571 | *** | beta_def_872 | ΔS | 70.7 | 25 | 3 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |

---

### Step 7: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id = metal_26 AND c.ligand_id = ligand_10163)",
  "order_by": "m.condition_ionic_min ASC",
  "limit": 20
}
```

[summary]
## search_networks — 18 row(s)

> **Reference equilibrium networks** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### `Cd^[2+]` + Chloride ion — 7 network(s)
metal_id: metal_26 | ligand_id: ligand_10163 | ligand_def_HxL: *** | ligand_SMILES: ***

| beta_def | equation |
|----------|----------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |
| beta_def_872 | ``[M] + [L]^3 <=> [ML3]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_29916 | 1 | 0 | 19~29 | -0.15~0.15 | 1 | beta_def_812 | logK | 1.98 |
| ref_eq_net_29910 | 3 | 3 | 20~30 | -0.05~0.25 | 3 | beta_def_812; beta_def_872; beta_def_840 | logK | 1.52~2.6 |
| ref_eq_net_29915 | 2 | 1 | 19~29 | 0.35~0.65 | 2 | beta_def_812; beta_def_840 | logK | 1.35~1.7 |
| ref_eq_net_29911 | 3 | 3 | 19~29 | 0.85~1.15 | 3 | beta_def_812; beta_def_872; beta_def_840 | logK | 1.35~1.7 |
| ref_eq_net_29912 | 3 | 3 | 19~29 | 1.85~2.15 | 3 | beta_def_812; beta_def_840; beta_def_872 | logK | 1.44~1.9 |
| ref_eq_net_29913 | 3 | 3 | 19~29 | 2.85~3.15 | 3 | beta_def_812; beta_def_840; beta_def_872 | logK | 1.54~2.3 |
| ref_eq_net_29914 | 3 | 3 | 19~29 | 3.85~4.15 | 3 | beta_def_812; beta_def_840; beta_def_872 | logK | 1.66~2.8 |

#### Reference-state network: ref_eq_net_29916 (1 nodes)
> First network — reference conditions (T 19~29 °C, I -0.15~0.15 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 1.98 |

---
