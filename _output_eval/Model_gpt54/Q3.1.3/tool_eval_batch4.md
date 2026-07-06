# Q3.1.3 — Tool Results (batch 4)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Zn(II)",
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
  "name": "histidine, L-histidine",
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
  "name": "hist",
  "limit": 50
}
```

[summary]
## search_ligands — 50 result(s)

**stats:** 95 SQL matches · showing 50 · limit 50

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5860 | DL-2-Amino-3-(2-mercaptoimidazo-4… (Thiohistidine) | H2L | Amino Acids | 20 | `NC(Cc1cnc(S)[nH]1)C(=O)O` | (-inf, H2L, 8.59, HL, 8.59, L, +inf) |
| ligand_5898 | L-2-Amino-3-(4-imidazolyl)propanoic a… (Histidine) | HL | Amino Acids | 250 | `N[C@@H](Cc1c[nH]cn1)C(=O)O` | (-inf, H3L, -1.7, H2L, 6.05, HL, 9.1, L, +inf) |
| ligand_5899 | L-2-Amino-3-(N(1)-methyl-4-imidazolyl)propanoic a… | HL | Amino Acids | 14 | `Cn1cnc(C[C@H](N)C(=O)O)c1` | (-inf, H3L, -1.72, H2L, 5.87, HL, 9.16, L, +inf) |
| ligand_5900 | L-2-Amino-3-(N(3)-methyl-4-imidazolyl)propanoic a… | HL | Amino Acids | 16 | `Cn1cncc1C[C@H](N)C(=O)O` | (-inf, H3L, -1.65, H2L, 6.48, HL, 8.61, L, +inf) |
| ligand_5901 | L-4-(2-Amino-3-carboxypropyl)-1,3-dimethylimidazo… | HL | Amino Acids | 6 | `Cn1c[n+](C)cc1C[C@H](N)C(=O)O` | (-inf, H2L, -1.98, HL, 7.85, L, +inf) |
| ligand_5902 | L-1-Carboxy-2-(4-imidazolyl)ethyl(dimethyl)ammoni… | HL | Amino Acids | 9 | `C[NH+](C)C(Cc1cnc[nH]1)C(=O)O` | (-inf, H3L, -1.03, H2L, 6.03, HL, 8.86, L, +inf) |
| ligand_5903 | L-1-Carboxy-2-(4-imidazolyl)ethyl(trimethyl)ammon… | HL | Amino Acids | 6 | `C[N+](C)(C)C(Cc1c[nH]cn1)C(=O)O` | (-inf, H2L, -0.98, HL, 6, L, +inf) |
| ligand_5904 | L-2-Amino-3-(N(3)-benzyl-4-imidazolyl)propanoic a… | HL | Amino Acids | 18 | `NC(Cc1cncn1Cc1ccccc1)C(=O)O` | (-inf, H3L, 1.94, H2L, 5.53, HL, 9.21, L, +inf) |
| ligand_5905 | L-2-Amino-3-(5-iodo-4-imidazol… (5-Iodo-Histidine) | HL | Amino Acids | 23 | `N[C@@H](Cc1nc[nH]c1I)C(=O)O` | (-inf, H3L, -1.47, H2L, 4.21, HL, 8.6, L, +inf) |
| ligand_5906 | L-2-Amino-3-(2,5-diiodo-4-… (2,5-Diiodo-Histidine) | HL | Amino Acids | 27 | `N[C@@H](Cc1nc(I)[nH]c1I)C(=O)O` | (-inf, H4L, -1.55, H3L, 2.74, H2L, 8.12, HL, 9.57, L, +inf) |
| ligand_5960 | L-2-(Methylamino)-3-(4-imidazolyl)propanoic acid … | HL | Amino Acids | 17 | `CNC(Cc1cnc[nH]1)C(=O)O` | (-inf, H3L, -1.4, H2L, 5.93, HL, 9.32, L, +inf) |
| ligand_5961 | L-2-(Benzylamino)-3-(4-imidazolyl)propanoic acid … | HL | Amino Acids | 18 | `O=C(O)C(Cc1cnc[nH]1)NCc1ccccc1` | (-inf, H3L, -1.3, H2L, 5.94, HL, 8.32, L, +inf) |
| ligand_5962 | L-2-(Benzylamino)-3-(3-benzyl-5-imidazolyl)propan… | HL | Amino Acids | 14 | `O=C(O)C(Cc1cn(Cc2ccccc2)cn1)NCc1ccccc1` | (-inf, H3L, 2, H2L, 5.5, HL, 8.47, L, +inf) |
| ligand_5967 | N-Acetyl-L-histidine | HL | Amino Acids | 23 | `CC(=O)N[C@@H](Cc1c[nH]cn1)C(=O)O` | (-inf, H2L, 2.84, HL, 7.02, L, +inf) |
| ligand_5968 | N-(2-Methyl-2-propoxycarbonyl)-L-histidine | HL | Amino Acids | 6 | `CC(C)OC(=O)NC(Cc1c[nH]cn1)C(=O)O` | (-inf, H2L, 2.98, HL, 7.06, L, +inf) |
| ligand_5969 | N-Acetylglycyl-L-histidine | HL | Amino Acids | 6 | `CC(=O)NCC(=O)N[C@@H](CC1C=NC=N1)C(=O)O` | (-inf, H2L, 2.87, HL, 6.99, L, +inf) |
| ligand_5970 | N-Acetylglycylglycyl-L-histidine | HL | Amino Acids | 12 | `CC(=O)NCC(=O)NCC(=O)N[C@@H](CC1C=NC=N1)C(=O)O` | (-inf, H2L, 2.96, HL, 7.06, L, +inf) |
| ligand_5971 | N-Acetylglycyl-L-histidylglycine | HL | Amino Acids | 7 | `CC(=O)NCC(=O)N[C@@H](CC1C=NC=N1)C(=O)NCC(=O)O` | (-inf, H2L, 3.13, HL, 6.74, L, +inf) |
| ligand_5972 | N-Acetylglycyl(N(3)-benzyl-L-histidyl)glycine | HL | Amino Acids | 7 | `CC(=O)NCC(=O)NC(Cc1cncn1Cc1ccccc1)C(=O)NCC(=O)O` | (-inf, H2L, 3.18, HL, 6.25, L, +inf) |
| ligand_5973 | N-Acetylglycylglycylglycyl-L-histidine | HL | Amino Acids | 7 | `CC(=O)NCC(=O)NCC(=O)NCC(=O)N[C@@H](CC1C=NC=N1)C(=O)O` | (-inf, H2L, 3.04, HL, 7.09, L, +inf) |
| ligand_5974 | N-Acetylglycylglycyl-L-histidylglycine | HL | Amino Acids | 11 | `CC(=O)NCC(=O)NCC(=O)N[C@@H](CC1C=NC=N1)C(=O)NCC(=O)O` | (-inf, H2L, 3.17, HL, 6.78, L, +inf) |
| ligand_6027 | L-2-(Dimethylamino)-3-(4-imidazolyl)propanoic aci… | HL | Amino Acids | 20 | `CN(C)C(Cc1cnc[nH]1)C(=O)O` | (-inf, H3L, -1.1, H2L, 6.01, HL, 8.88, L, +inf) |
| ligand_6401 | Glycyl-L-histidine | HL | Peptides | 59 | `NCC(=O)N[C@@H](Cc1c[nH]cn1)C(=O)O` | (-inf, H3L, 2.52, H2L, 6.7, HL, 8.14, L, +inf) |
| ligand_6420 | L-Histidylglycine | HL | Peptides | 46 | `N[C@@H](Cc1c[nH]cn1)C(=O)NCC(=O)O` | (-inf, H3L, 2.72, H2L, 5.88, HL, 7.6, L, +inf) |
| ligand_6422 | beta-Alanyl-L-histidine (L-Carnosine) | HL | Peptides | 55 | `NCCC(=O)N[C@@H](CC1C=NC=N1)C(=O)O` | (-inf, H3L, 2.54, H2L, 6.79, HL, 9.35, L, +inf) |
| ligand_6423 | beta-Alanyl-L-1-methylhistidine (L-Anserine) | HL | Peptides | 4 | `Cn1cncc1CC(NC(=O)CCN)C(=O)O` | (-inf, H2L, 7.03, HL, 9.33, L, +inf) |
| ligand_6434 | L-Alanyl-L-histidine | HL | Peptides | 25 | `C[C@H](N)C(=O)N[C@@H](CC1C=NC=N1)C(=O)O` | (-inf, H3L, -2.68, H2L, 6.74, HL, 8.06, L, +inf) |
| ligand_6463 | L-Leucyl-L-histidine | HL | Peptides | 11 | `CC(C)C[C@H](N)C(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O` | (-inf, H3L, 2.4, H2L, 6.44, HL, 7.72, L, +inf) |
| ligand_6482 | L-Histidyl-L-phenylalanine | HL | Peptides | 18 | `N[C@@H](Cc1cnc[nH]1)C(=O)N[C@@H](Cc1ccccc1)C(=O)O` | (-inf, H3L, 2.57, H2L, 6, HL, 7.56, L, +inf) |
| ligand_6491 | L-Tyrosyl-L-histidine | H2L | Peptides | 11 | `N[C@@H](Cc1ccc(O)cc1)C(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O` | (-inf, H4L, 2.68, H3L, 6.65, H2L, 7.63, HL, 10, L, +inf) |
| ligand_6492 | L-Tyrosyl-D-histidine | H2L | Peptides | 9 | `N[C@@H](Cc1ccc(O)cc1)C(=O)N[C@H](Cc1cnc[nH]1)C(=O)O` | (-inf, H4L, 2.35, H3L, 6.64, H2L, 7.77, HL, 9.84, L, +inf) |
| ligand_6494 | L-Histidyl-L-tyrosine | H2L | Peptides | 23 | `N[C@@H](Cc1cnc[nH]1)C(=O)N[C@@H](Cc1ccc(O)cc1)C(=O)O` | (-inf, H4L, 2.55, H3L, 5.91, H2L, 7.44, HL, 9.83, L, +inf) |
| ligand_6511 | L-Histidyl-L-lysine | HL | Peptides | 13 | `NCCCC[C@H](NC(=O)[C@@H](N)Cc1cnc[nH]1)C(=O)O` | (-inf, H4L, 2, H3L, 5.65, H2L, 7.29, HL, 10.09, L, +inf) |
| ligand_6512 | L-Pyroglutamyl-L-histidine | HL | Peptides | 7 | `O=C1CC[C@@H](C(=O)N[C@@H](Cc2cnc[nH]2)C(=O)O)N1` | (-inf, H2L, 2.7, HL, 7.18, L, +inf) |
| ligand_6513 | L-Picolyl-L-histidine | HL | Peptides | 9 | `O=C(N[C@@H](Cc1cnc[nH]1)C(=O)O)c1ccccn1` | (-inf, H2L, 3.05, HL, 7.72, L, +inf) |
| ligand_6514 | L-Histidyl-L-histidine | HL | Peptides | 12 | `N[C@@H](Cc1c[nH]cn1)C(=O)N[C@@H](Cc1c[nH]cn1)C(=O)O` | (-inf, H4L, 2.6, H3L, 5.66, H2L, 6.7, HL, 7.52, L, +inf) |
| ligand_6515 | D-Histidyl-L-histidine | HL | Peptides | 13 | `N[C@H](Cc1c[nH]cn1)C(=O)N[C@@H](Cc1c[nH]cn1)C(=O)O` | (-inf, H4L, 2.18, H3L, 5.32, H2L, 6.73, HL, 7.82, L, +inf) |
| ligand_6516 | N-(Mercaptoacetyl)-L-histidine | H2L | Peptides | 3 | `O=C(CS)N[C@@H](Cc1cnc[nH]1)C(=O)O` | (-inf, H3L, 3.43, H2L, 7.14, HL, 8.7, L, +inf) |
| ligand_6517 | N-(3-Mercaptopropionyl)-L-histidine | H2L | Peptides | 3 | `O=C(CCS)N[C@@H](Cc1cnc[nH]1)C(=O)O` | (-inf, H3L, 3.48, H2L, 7.25, HL, 9.86, L, +inf) |
| ligand_6525 | L-Methionyl-L-histidine | HL | Peptides | 7 | `CSCC[C@H](N)C(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O` | (-inf, H3L, 2.96, H2L, 6.57, HL, 7.59, L, +inf) |
| ligand_6526 | L-Histidyl-L-methionine | HL | Peptides | 7 | `CSCC[C@H](NC(=O)[C@@H](N)Cc1c[nH]cn1)C(=O)O` | (-inf, H3L, 2.58, H2L, 6, HL, 7.5, L, +inf) |
| ligand_6527 | L-Prolyl-L-histidine | HL | Peptides | 7 | `O=C(O)[C@H](Cc1cnc[nH]1)NC(=O)[C@@H]1CCCN1` | (-inf, H3L, 3.02, H2L, 3.02, HL, -6.84, L, +inf) |
| ligand_6528 | D-Prolyl-L-histidine | HL | Peptides | 7 | `O=C(O)[C@H](Cc1cnc[nH]1)NC(=O)[C@H]1CCCN1` | (-inf, H3L, 2.91, H2L, 2.91, HL, -6.77, L, +inf) |
| ligand_6575 | Glycylglycyl-L-histidine | HL | tripeptides | 28 | `NCC(=O)NCC(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O` | (-inf, H3L, 2.82, H2L, 6.72, HL, 8.02, L, +inf) |
| ligand_6576 | Glycyl-L-histidylglycine | HL | tripeptides | 49 | `NCC(=O)N[C@@H](CC1C=NC=N1)C(=O)NCC(=O)O` | (-inf, H3L, 3.1, H2L, 6.56, HL, 8, L, +inf) |
| ligand_6577 | L-Histidyl-L-prolyl-L-phenylalanine | HL | tripeptides | 10 | `N[C@@H](Cc1cnc[nH]1)C(=O)N1CCC[C@H]1C(=O)N[C@@H](Cc1ccccc1)C(=O)O` | (-inf, H3L, 3.26, H2L, 5.54, HL, 5.54, L, +inf) |
| ligand_6578 | L-Aspartyl-L-alanyl-L-histidine methylamide | HL | tripeptides | 32 | `CNC(=O)[C@H](Cc1cnc[nH]1)NC(=O)[C@H](C)NC(=O)[C@@H](N)CC(=O)O` | (-inf, H3L, 3, H2L, 6.38, HL, 7.7, L, +inf) |
| ligand_6579 | N-Acetyl-L-tyrosyl-L-isoleucyl-L-histidine | *** | tripeptides | 12 | *** | (-inf, H3L, 2.95, H2L, 7.02, HL, 9.78, L, +inf) |
| ligand_6580 | N-Benzoylglycyl-L-histdyl-L-leucine | *** | tripeptides | 6 | *** | (-inf, H2L, 3.15, HL, 6.6, L, +inf) |
| ligand_6581 | Glycyl-L-histidyl-L-lysine | HL | tripeptides | 29 | `NCCCC[C@H](NC(=O)[C@H](Cc1cnc[nH]1)NC(=O)CN)C(=O)O` | (-inf, H4L, 2.9, H3L, 6.5, H2L, 7.91, HL, 10.51, L, +inf) |

### Functional groups across all SQL matches (71 parseable SMILES)

| group | count | % |
|-------|-------|---|
| aromatic_ring | 56 | 79% |
| carboxyl | 53 | 75% |
| amide | 52 | 73% |
| primary_amine | 43 | 61% |
| imine | 17 | 24% |
| ester | 7 | 10% |
| hydroxyl | 5 | 7% |
| secondary_amine | 5 | 7% |
| thiol | 5 | 7% |
| phenol | 3 | 4% |
| halide | 2 | 3% |
| pyridine | 2 | 3% |
| thioether | 2 | 3% |
| tertiary_amine | 1 | 1% |

---

### Step 5: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_208",
  "ligand_id": "ligand_5898"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 6 species

### Zn^[2+] + L-2-Amino-3-(4-imidazolyl)propanoic acid (Histidine)
**metal_id:** metal_208 | **ligand_id:** ligand_5898 | **ligand_def_HxL:** HL  
**entries:** 29 | **species:** 6 | **vlm_count:** 29

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_204 | [M(HL)<sub>2</sub>]/[MHL<sub>2</sub>][H] | [MHL2] + [H] <=> [M(HL)2] | [M(HL)2](aqueous), [MHL2](aqueous), [H](aqueous) | 1 |
| beta_def_788 | [MHL]/[ML][H] | [ML] + [H] <=> [MHL] | [MHL](aqueous), [ML](aqueous), [H](aqueous) | 4 |
| beta_def_792 | [MHL<sub>2</sub>]/[ML<sub>2</sub>][H] | [ML2] + [H] <=> [MHL2] | [MHL2](aqueous), [ML2](aqueous), [H](aqueous) | 3 |
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 8 |
| beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | [M] + [L]^2 <=> [ML2] | [ML2](aqueous), [M](aqueous), [L](aqueous) | 12 |
| beta_def_984 | [ML<sub>2</sub>]/[M(OH)L<sub>2</sub>][H] | [M(OH)L2] + [H] <=> [ML2] + [H2O] | [ML2](aqueous), [H2O](aqueous), [M(OH)L2](aqueous), [H](aqueous) | 1 |

**vlm_ids:** vlm_98899, vlm_98900, vlm_98901, vlm_98902, vlm_98903, … vlm_98925, vlm_98926, vlm_98927 (29 listed)

**equilibrium_maps:** 6 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_1354 | 5 | 6 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_1355 | 4 | 4 | 31~41 °C | 0~0.3 M |
| ref_eq_net_1356 | 3 | 2 | 19~29 °C | 0.35~0.65 M |
| ref_eq_net_1357 | 2 | 1 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_1358 | 2 | 1 | 19~29 °C | 2.85~3.15 M |
| ref_eq_net_1359 | 2 | 1 | 19~29 °C | -0.05~0.25 M |

---

### Step 7: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND c.ligand_id = ligand_5898)",
  "order_by": "s.temperature_c ASC, s.ionic_strength_mol_l ASC, s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability — 29 row(s)

### `Zn^[2+]` + L-2-Amino-3-(4-imidazolyl)propanoic acid (Histidine) — 29 measurement(s)
metal_id: metal_208 | ligand_id: ligand_5898
ligand_HxL_def: HL | ligand_SMILES: N[C@@H](Cc1c[nH]cn1)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_98916 | *** | beta_def_840 | ΔS | 72 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.1, L, +inf) |
| vlm_98906 | *** | beta_def_812 | ΔS | 57.3 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.1, L, +inf) |
| vlm_98907 | ref_eq_map_1353 | beta_def_840 | logK | 12.04 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.1, L, +inf) |
| vlm_98899 | ref_eq_map_1353 | beta_def_812 | logK | 6.51 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.1, L, +inf) |
| vlm_98924 | ref_eq_map_1353 | beta_def_792 | logK | 5.8 | 25 | 0.1 | `[ML2] + [H] <=> [MHL2]` | *** |  |  |
| vlm_98923 | ref_eq_map_1353 | beta_def_204 | logK | 5.67 | 25 | 0.1 | `[MHL2] + [H] <=> [M(HL)2]` | *** |  |  |
| vlm_98919 | ref_eq_map_1353 | beta_def_788 | logK | 4.86 | 25 | 0.1 | `[ML] + [H] <=> [MHL]` | *** |  |  |
| vlm_98922 | *** | beta_def_788 | ΔS | 0.4 | 25 | 0.1 | `[ML] + [H] <=> [MHL]` | *** |  |  |
| vlm_98914 | *** | beta_def_840 | ΔH | 0 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.1, L, +inf) |
| vlm_98925 | ref_eq_map_1358 | beta_def_792 | logK | -5.54 | 25 | 0.1 | `[ML2] + [H] <=> [MHL2]` | *** |  |  |
| vlm_98908 | ref_eq_map_1358 | beta_def_840 | logK | -12.18 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.1, L, +inf) |
| vlm_98904 | *** | beta_def_812 | ΔH | -20.1 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.1, L, +inf) |
| vlm_98921 | *** | beta_def_788 | ΔH | -27.6 | 25 | 0.1 | `[ML] + [H] <=> [MHL]` | *** |  |  |
| vlm_98913 | *** | beta_def_840 | ΔH | -47.3 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.1, L, +inf) |
| vlm_98917 | *** | beta_def_840 | ΔS | -67.4 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.1, L, +inf) |
| vlm_98910 | ref_eq_map_1355 | beta_def_840 | logK | 11.91 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.1, L, +inf) |
| vlm_98927 | ref_eq_map_1355 | beta_def_984 | logK | 9.95 | 25 | 0.5 | `[M(OH)L2] + [H] <=> [ML2] + [H2O]` | *** |  |  |
| vlm_98901 | ref_eq_map_1355 | beta_def_812 | logK | 6.48 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.1, L, +inf) |
| vlm_98911 | ref_eq_map_1356 | beta_def_840 | logK | 12.29 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.1, L, +inf) |
| vlm_98902 | ref_eq_map_1356 | beta_def_812 | logK | 6.58 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.1, L, +inf) |
| vlm_98918 | *** | beta_def_840 | ΔS | 58.2 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.1, L, +inf) |
| vlm_98912 | ref_eq_map_1357 | beta_def_840 | logK | 12.74 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.1, L, +inf) |
| vlm_98903 | ref_eq_map_1357 | beta_def_812 | logK | 7.07 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (9.1, L, +inf) |
| vlm_98905 | *** | beta_def_812 | ΔH | -23 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (9.1, L, +inf) |
| vlm_98915 | *** | beta_def_840 | ΔH | -49.4 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.1, L, +inf) |
| vlm_98909 | ref_eq_map_1354 | beta_def_840 | logK | 11.67 | 37 | 0.15 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.1, L, +inf) |
| vlm_98900 | ref_eq_map_1354 | beta_def_812 | logK | 6.35 | 37 | 0.15 | `[M] + [L] <=> [ML]` | *** | [L] | (9.1, L, +inf) |
| vlm_98926 | ref_eq_map_1354 | beta_def_792 | logK | 5.5 | 37 | 0.15 | `[ML2] + [H] <=> [MHL2]` | *** |  |  |
| vlm_98920 | ref_eq_map_1354 | beta_def_788 | logK | 4.61 | 37 | 0.15 | `[ML] + [H] <=> [MHL]` | *** |  |  |

---

### Step 8: `search_citations`
**Args:**
```json
{
  "where": "(rv.vlm_id IN (98899,98900,98901,98902,98903,98904,98905,98906,98907,98908,98909,98910,98911,98912,98913,98914,98915,98916,98917,98918,98919,98920,98921,98922,98923,98924,98925,98926,98927) AND (la.citation LIKE '%2005%' OR la.citation LIKE '%2004%' OR la.citation LIKE '%2006%'))",
  "order_by": "la.citation ASC",
  "limit": 50
}
```

[summary]
## search_citations

*(no results)*

---

### Step 9: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND c.ligand_id = ligand_5898)",
  "order_by": "m.condition_temp_min ASC, m.condition_ionic_min ASC",
  "limit": 20
}
```

[summary]
## search_networks — 18 row(s)

> **Reference equilibrium networks** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### `Zn^[2+]` + L-2-Amino-3-(4-imidazolyl)propanoic acid (Histidine) — 6 network(s)
metal_id: metal_208 | ligand_id: ligand_5898 | ligand_def_HxL: HL | ligand_SMILES: N[C@@H](Cc1c[nH]cn1)C(=O)O

| beta_def | equation |
|----------|----------|
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |
| beta_def_792 | ``[ML2] + [H] <=> [MHL2]`` |
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_984 | ``[M(OH)L2] + [H] <=> [ML2] + [H2O]`` |
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` |
| beta_def_204 | ``[MHL2] + [H] <=> [M(HL)2]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_1359 | 2 | 1 | 19~29 | -0.05~0.25 | 2 | beta_def_840; beta_def_792 | logK | -12.18~-5.54 |
| ref_eq_net_1356 | 3 | 2 | 19~29 | 0.35~0.65 | 3 | beta_def_812; beta_def_984; beta_def_840 | logK | 6.48~11.91 |
| ref_eq_net_1357 | 2 | 1 | 19~29 | 0.85~1.15 | 2 | beta_def_812; beta_def_840 | logK | 6.58~12.29 |
| ref_eq_net_1358 | 2 | 1 | 19~29 | 2.85~3.15 | 2 | beta_def_812; beta_def_840 | logK | 7.07~12.74 |
| ref_eq_net_1354 | 5 | 6 | 20~30 | -0.05~0.25 | 5 | 5 diff beta_def | logK | 4.86~12.04 |
| ref_eq_net_1355 | 4 | 4 | 31~41 | 0~0.3 | 4 | 4 diff beta_def | logK | 4.61~11.67 |

#### Reference-state network: ref_eq_net_1359 (2 nodes)
> First network — reference conditions (T 19~29 °C, I -0.05~0.25 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` | logK | -12.18 |
| beta_def_792 | ``[ML2] + [H] <=> [MHL2]`` | logK | -5.54 |

---
