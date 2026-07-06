# Q3.2.1 — Tool Results (batch 3)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Cu(II)",
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
  "name": "glycine",
  "limit": 10
}
```

[summary]
## search_ligands — 10 result(s)

**stats:** 170 SQL matches · showing 10 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5760 | Aminoacetic acid (Glycine) | HL | Amino Acids | 428 | `NCC(=O)O` | (-inf, H2L, 2.33, HL, 9.57, L, +inf) |
| ligand_5776 | DL-Aminophenylacetic acid (Phenylglycine) | HL | Amino Acids | 12 | `NC(C(=O)O)c1ccccc1` | (-inf, H2L, -1.9, HL, 8.92, L, +inf) |
| ligand_5786 | DL-Amino-4-sulfophenylacet… (4-Sulfophenylglycine) | H2L | Amino Acids | 12 | `NC(C(=O)O)c1ccc(S(=O)(=O)O)cc1` | (-inf, H2L, -1.8, HL, 8.66, L, +inf) |
| ligand_5838 | DL-Amino-4-Methoxyphenyl… (4-Methoxyphenylglycine) | HL | Amino Acids | 12 | `COc1ccc(C(N)C(=O)O)cc1` | (-inf, H2L, 2, HL, 9.07, L, +inf) |
| ligand_5925 | N-Methylglycine (Sarcosine) | HL | Amino Acids | 39 | `CNCC(=O)O` | (-inf, H2L, 2.18, HL, 9.98, L, +inf) |
| ligand_5926 | N-Ethylglycine | HL | Amino Acids | 6 | `CCNCC(=O)O` | (-inf, H2L, 2.3, HL, 10.1, L, +inf) |
| ligand_5927 | N-Propylglycine | HL | Amino Acids | 6 | `CCCNCC(=O)O` | (-inf, H2L, 2.28, HL, 10.03, L, +inf) |
| ligand_5928 | N-Butylglycine | HL | Amino Acids | 6 | `CCCCNCC(=O)O` | (-inf, H2L, 2.29, HL, 10.07, L, +inf) |
| ligand_5929 | N-(2-Propyl)glycine | HL | Amino Acids | 5 | `CC(C)NCC(=O)O` | (-inf, H2L, 2.36, HL, 10.06, L, +inf) |
| ligand_5937 | N-(Phosphonomethyl)glycine (Glyphosate) | H3L | Amino Acids | 146 | `O=C(O)CNCP(=O)(O)O` | (-inf, H4L, -0.5, H3L, 2.2, H2L, 5.45, HL, 10.1, L, +inf) |

### Functional groups across all SQL matches (129 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 114 | 88% |
| amide | 96 | 74% |
| primary_amine | 78 | 60% |
| aromatic_ring | 26 | 20% |
| hydroxyl | 25 | 19% |
| secondary_amine | 22 | 17% |
| tertiary_amine | 14 | 11% |
| ester | 9 | 7% |
| thiol | 9 | 7% |
| phenol | 7 | 5% |
| imine | 5 | 4% |
| phosphonate | 3 | 2% |
| thioether | 3 | 2% |
| phosphate | 2 | 2% |
| pyridine | 2 | 2% |
| sulfonate | 2 | 2% |
| ether | 1 | 1% |

---

### Step 4: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_41",
  "ligand_id": "ligand_5760"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 2 species

### Cu^[2+] + Aminoacetic acid (Glycine)
**metal_id:** metal_41 | **ligand_id:** ligand_5760 | **ligand_def_HxL:** HL  
**entries:** 30 | **species:** 2 | **vlm_count:** 30

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 15 |
| beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | [M] + [L]^2 <=> [ML2] | [ML2](aqueous), [M](aqueous), [L](aqueous) | 15 |

**vlm_ids:** vlm_93847, vlm_93848, vlm_93849, vlm_93850, vlm_93851, … vlm_93874, vlm_93875, vlm_93876 (30 listed)

**equilibrium_maps:** 9 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_86 | 2 | 1 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_87 | 2 | 1 | 31~41 °C | 0~0.3 M |
| ref_eq_net_88 | 2 | 1 | 19~29 °C | 0.35~0.65 M |
| ref_eq_net_89 | 2 | 1 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_90 | 2 | 1 | 19~29 °C | 1.85~2.15 M |
| ref_eq_net_91 | 2 | 1 | 19~29 °C | 2.35~2.65 M |
| ref_eq_net_92 | 2 | 1 | 5~15 °C | -0.15~0.15 M |
| ref_eq_net_93 | 2 | 1 | 19~29 °C | -0.15~0.15 M |
| ref_eq_net_94 | 2 | 1 | 35~45 °C | -0.15~0.15 M |

---

### Step 6: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_41 AND c.ligand_id = ligand_5760 AND (c.beta_definition_id = beta_def_812 OR c.beta_definition_id = beta_def_840))",
  "order_by": "s.temperature_c ASC, s.ionic_strength_mol_l ASC",
  "limit": 100
}
```

[summary]
## search_stability — 30 row(s)

### `Cu^[2+]` + Aminoacetic acid (Glycine) — 30 measurement(s)
metal_id: metal_41 | ligand_id: ligand_5760
ligand_HxL_def: HL | ligand_SMILES: NCC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_93853 | ref_eq_map_92 | beta_def_812 | logK | 8.8 | 10 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.57, L, +inf) |
| vlm_93856 | *** | beta_def_812 | ΔH | -26.8 | 10 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.57, L, +inf) |
| vlm_93868 | ref_eq_map_92 | beta_def_840 | logK | 16.3 | 10 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.57, L, +inf) |
| vlm_93871 | *** | beta_def_840 | ΔH | -56.5 | 10 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.57, L, +inf) |
| vlm_93854 | ref_eq_map_93 | beta_def_812 | logK | 8.56 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.57, L, +inf) |
| vlm_93857 | *** | beta_def_812 | ΔH | -25.1 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.57, L, +inf) |
| vlm_93860 | *** | beta_def_812 | ΔS | 79.5 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.57, L, +inf) |
| vlm_93869 | ref_eq_map_93 | beta_def_840 | logK | 15.7 | 25 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.57, L, +inf) |
| vlm_93872 | *** | beta_def_840 | ΔH | -54.4 | 25 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.57, L, +inf) |
| vlm_93875 | *** | beta_def_840 | ΔS | 118 | 25 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.57, L, +inf) |
| vlm_93847 | ref_eq_map_86 | beta_def_812 | logK | 8.19 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.57, L, +inf) |
| vlm_93859 | *** | beta_def_812 | ΔH | -25.1 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.57, L, +inf) |
| vlm_93861 | *** | beta_def_812 | ΔS | 72.4 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.57, L, +inf) |
| vlm_93862 | ref_eq_map_86 | beta_def_840 | logK | 15.1 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.57, L, +inf) |
| vlm_93874 | *** | beta_def_840 | ΔH | -54.4 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.57, L, +inf) |
| vlm_93876 | *** | beta_def_840 | ΔS | 106.7 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.57, L, +inf) |
| vlm_93849 | ref_eq_map_88 | beta_def_812 | logK | 8.1 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.57, L, +inf) |
| vlm_93864 | ref_eq_map_88 | beta_def_840 | logK | 15 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.57, L, +inf) |
| vlm_93850 | ref_eq_map_89 | beta_def_812 | logK | 8.2 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.57, L, +inf) |
| vlm_93865 | ref_eq_map_89 | beta_def_840 | logK | 15.1 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.57, L, +inf) |
| vlm_93851 | ref_eq_map_90 | beta_def_812 | logK | 8.38 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.57, L, +inf) |
| vlm_93866 | ref_eq_map_90 | beta_def_840 | logK | 15.4 | 25 | 2 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.57, L, +inf) |
| vlm_93852 | ref_eq_map_91 | beta_def_812 | logK | 8.34 | 25 | 2.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.57, L, +inf) |
| vlm_93867 | ref_eq_map_91 | beta_def_840 | logK | 15.4 | 25 | 2.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.57, L, +inf) |
| vlm_93848 | ref_eq_map_87 | beta_def_812 | logK | 7.99 | 37 | 0.15 | `[M] + [L] <=> [ML]` | *** | [L] | (9.57, L, +inf) |
| vlm_93863 | ref_eq_map_87 | beta_def_840 | logK | 14.69 | 37 | 0.15 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.57, L, +inf) |
| vlm_93855 | ref_eq_map_94 | beta_def_812 | logK | 8.37 | 40 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.57, L, +inf) |
| vlm_93858 | *** | beta_def_812 | ΔH | -23.4 | 40 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.57, L, +inf) |
| vlm_93870 | ref_eq_map_94 | beta_def_840 | logK | 15.3 | 40 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.57, L, +inf) |
| vlm_93873 | *** | beta_def_840 | ΔH | -52.3 | 40 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.57, L, +inf) |

---

### Step 7: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id = metal_41 AND c.ligand_id = ligand_5760)",
  "order_by": "m.condition_temp_min ASC, m.condition_ionic_min ASC",
  "limit": 20
}
```

[summary]
## search_networks — 18 row(s)

> **Reference equilibrium networks** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### `Cu^[2+]` + Aminoacetic acid (Glycine) — 9 network(s)
metal_id: metal_41 | ligand_id: ligand_5760 | ligand_def_HxL: HL | ligand_SMILES: NCC(=O)O

| beta_def | equation |
|----------|----------|
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |
| beta_def_812 | ``[M] + [L] <=> [ML]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_92 | 2 | 1 | 5~15 | -0.15~0.15 | 2 | beta_def_812; beta_def_840 | logK | 8.8~16.3 |
| ref_eq_net_93 | 2 | 1 | 19~29 | -0.15~0.15 | 2 | beta_def_812; beta_def_840 | logK | 8.56~15.7 |
| ref_eq_net_88 | 2 | 1 | 19~29 | 0.35~0.65 | 2 | beta_def_812; beta_def_840 | logK | 8.1~15 |
| ref_eq_net_89 | 2 | 1 | 19~29 | 0.85~1.15 | 2 | beta_def_812; beta_def_840 | logK | 8.2~15.1 |
| ref_eq_net_90 | 2 | 1 | 19~29 | 1.85~2.15 | 2 | beta_def_812; beta_def_840 | logK | 8.38~15.4 |
| ref_eq_net_91 | 2 | 1 | 19~29 | 2.35~2.65 | 2 | beta_def_812; beta_def_840 | logK | 8.34~15.4 |
| ref_eq_net_86 | 2 | 1 | 20~30 | -0.05~0.25 | 2 | beta_def_812; beta_def_840 | logK | 8.19~15.1 |
| ref_eq_net_87 | 2 | 1 | 31~41 | 0~0.3 | 2 | beta_def_812; beta_def_840 | logK | 7.99~14.69 |
| ref_eq_net_94 | 2 | 1 | 35~45 | -0.15~0.15 | 2 | beta_def_812; beta_def_840 | logK | 8.37~15.3 |

#### Reference-state network: ref_eq_net_92 (2 nodes)
> First network — reference conditions (T 5~15 °C, I -0.15~0.15 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 8.8 |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` | logK | 16.3 |

---
