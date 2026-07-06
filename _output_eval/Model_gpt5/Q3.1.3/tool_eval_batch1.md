# Q3.1.3 — Tool Results (batch 1)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "zinc",
  "limit": 20
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
  "name": "histidine",
  "limit": 50
}
```

[summary]
## search_ligands — 50 result(s)

**stats:** 57 SQL matches · showing 50 · limit 50

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
| ligand_5973 | N-Acetylglycylglycylglycyl-L-histidine | HL | Amino Acids | 7 | `CC(=O)NCC(=O)NCC(=O)NCC(=O)N[C@@H](CC1C=NC=N1)C(=O)O` | (-inf, H2L, 3.04, HL, 7.09, L, +inf) |
| ligand_6027 | L-2-(Dimethylamino)-3-(4-imidazolyl)propanoic aci… | HL | Amino Acids | 20 | `CN(C)C(Cc1cnc[nH]1)C(=O)O` | (-inf, H3L, -1.1, H2L, 6.01, HL, 8.88, L, +inf) |
| ligand_6401 | Glycyl-L-histidine | HL | Peptides | 59 | `NCC(=O)N[C@@H](Cc1c[nH]cn1)C(=O)O` | (-inf, H3L, 2.52, H2L, 6.7, HL, 8.14, L, +inf) |
| ligand_6422 | beta-Alanyl-L-histidine (L-Carnosine) | HL | Peptides | 55 | `NCCC(=O)N[C@@H](CC1C=NC=N1)C(=O)O` | (-inf, H3L, 2.54, H2L, 6.79, HL, 9.35, L, +inf) |
| ligand_6423 | beta-Alanyl-L-1-methylhistidine (L-Anserine) | HL | Peptides | 4 | `Cn1cncc1CC(NC(=O)CCN)C(=O)O` | (-inf, H2L, 7.03, HL, 9.33, L, +inf) |
| ligand_6434 | L-Alanyl-L-histidine | HL | Peptides | 25 | `C[C@H](N)C(=O)N[C@@H](CC1C=NC=N1)C(=O)O` | (-inf, H3L, -2.68, H2L, 6.74, HL, 8.06, L, +inf) |
| ligand_6463 | L-Leucyl-L-histidine | HL | Peptides | 11 | `CC(C)C[C@H](N)C(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O` | (-inf, H3L, 2.4, H2L, 6.44, HL, 7.72, L, +inf) |
| ligand_6491 | L-Tyrosyl-L-histidine | H2L | Peptides | 11 | `N[C@@H](Cc1ccc(O)cc1)C(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O` | (-inf, H4L, 2.68, H3L, 6.65, H2L, 7.63, HL, 10, L, +inf) |
| ligand_6492 | L-Tyrosyl-D-histidine | H2L | Peptides | 9 | `N[C@@H](Cc1ccc(O)cc1)C(=O)N[C@H](Cc1cnc[nH]1)C(=O)O` | (-inf, H4L, 2.35, H3L, 6.64, H2L, 7.77, HL, 9.84, L, +inf) |
| ligand_6512 | L-Pyroglutamyl-L-histidine | HL | Peptides | 7 | `O=C1CC[C@@H](C(=O)N[C@@H](Cc2cnc[nH]2)C(=O)O)N1` | (-inf, H2L, 2.7, HL, 7.18, L, +inf) |
| ligand_6513 | L-Picolyl-L-histidine | HL | Peptides | 9 | `O=C(N[C@@H](Cc1cnc[nH]1)C(=O)O)c1ccccn1` | (-inf, H2L, 3.05, HL, 7.72, L, +inf) |
| ligand_6514 | L-Histidyl-L-histidine | HL | Peptides | 12 | `N[C@@H](Cc1c[nH]cn1)C(=O)N[C@@H](Cc1c[nH]cn1)C(=O)O` | (-inf, H4L, 2.6, H3L, 5.66, H2L, 6.7, HL, 7.52, L, +inf) |
| ligand_6515 | D-Histidyl-L-histidine | HL | Peptides | 13 | `N[C@H](Cc1c[nH]cn1)C(=O)N[C@@H](Cc1c[nH]cn1)C(=O)O` | (-inf, H4L, 2.18, H3L, 5.32, H2L, 6.73, HL, 7.82, L, +inf) |
| ligand_6516 | N-(Mercaptoacetyl)-L-histidine | H2L | Peptides | 3 | `O=C(CS)N[C@@H](Cc1cnc[nH]1)C(=O)O` | (-inf, H3L, 3.43, H2L, 7.14, HL, 8.7, L, +inf) |
| ligand_6517 | N-(3-Mercaptopropionyl)-L-histidine | H2L | Peptides | 3 | `O=C(CCS)N[C@@H](Cc1cnc[nH]1)C(=O)O` | (-inf, H3L, 3.48, H2L, 7.25, HL, 9.86, L, +inf) |
| ligand_6525 | L-Methionyl-L-histidine | HL | Peptides | 7 | `CSCC[C@H](N)C(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O` | (-inf, H3L, 2.96, H2L, 6.57, HL, 7.59, L, +inf) |
| ligand_6527 | L-Prolyl-L-histidine | HL | Peptides | 7 | `O=C(O)[C@H](Cc1cnc[nH]1)NC(=O)[C@@H]1CCCN1` | (-inf, H3L, 3.02, H2L, 3.02, HL, -6.84, L, +inf) |
| ligand_6528 | D-Prolyl-L-histidine | HL | Peptides | 7 | `O=C(O)[C@H](Cc1cnc[nH]1)NC(=O)[C@H]1CCCN1` | (-inf, H3L, 2.91, H2L, 2.91, HL, -6.77, L, +inf) |
| ligand_6575 | Glycylglycyl-L-histidine | HL | tripeptides | 28 | `NCC(=O)NCC(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O` | (-inf, H3L, 2.82, H2L, 6.72, HL, 8.02, L, +inf) |
| ligand_6578 | L-Aspartyl-L-alanyl-L-histidine methylamide | HL | tripeptides | 32 | `CNC(=O)[C@H](Cc1cnc[nH]1)NC(=O)[C@H](C)NC(=O)[C@@H](N)CC(=O)O` | (-inf, H3L, 3, H2L, 6.38, HL, 7.7, L, +inf) |
| ligand_6579 | N-Acetyl-L-tyrosyl-L-isoleucyl-L-histidine | *** | tripeptides | 12 | *** | (-inf, H3L, 2.95, H2L, 7.02, HL, 9.78, L, +inf) |
| ligand_6594 | N-(Mercaptoacetyl)glycyl-L-histidine | H2L | tripeptides | 3 | `O=C(CS)NCC(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O` | (-inf, H3L, 3.47, H2L, 7.1, HL, 8.65, L, +inf) |
| ligand_6648 | Glycylglycylglycyl-L-histidine | HL | polypeptides | 9 | `NCC(=O)NCC(=O)NCC(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O` | (-inf, H3L, 2.9, H2L, 6.73, HL, 7.99, L, +inf) |
| ligand_6649 | L-Alanylglycylglycyl-L-histidine | *** | polypeptides | 12 | *** | (-inf, H3L, 2.62, H2L, 6.89, HL, 8.14, L, +inf) |
| ligand_6651 | Glycyl-L-histidylglycyl-L-histidine | *** | polypeptides | 8 | *** | (-inf, H4L, 2.57, H3L, 6, H2L, 6.95, HL, 8, L, +inf) |
| ligand_6652 | L-Alanylglycylglycyl-L-(N(Im)-benzoxymethyl)histi… | *** | polypeptides | 8 | *** | (-inf, H3L, 2.57, H2L, 6.05, HL, 8.15, L, +inf) |
| ligand_6653 | N-(2-Methyl-2-propyloxycarbonyl)-L-alanylglycylgl… | *** | polypeptides | 8 | *** | (-inf, H2L, 2.83, HL, 7.19, L, +inf) |
| ligand_6654 | L-Alanylglycylglycyl-L-histidine methylester | *** | polypeptides | 5 | *** | (-inf, H2L, 6.62, HL, 8.05, L, +inf) |
| ligand_6655 | L-Alanylglycyl-L-prolyl-L-histidine | HL | polypeptides | 10 | `C[C@H](N)C(=O)NCC(=O)N1CCC[C@H]1C(=O)N[C@@H](Cc1cnc[nH]1)C(=O)O` | (-inf, H3L, 2.63, H2L, 6.8, HL, 8.16, L, +inf) |
| ligand_6996 | L-2-Amino-3-(4-imidazo… (Histidinehydroxamic acid) | HL | Aliphatic amines | 48 | `N[C@@H](Cc1c[nH]cn1)C(=O)NO` | (-inf, H3L, 5.34, H2L, 7.18, HL, 9.12, L, +inf) |
| ligand_7838 | L-Pyroglutamyl-L-histidine methyl ester | L | Pyrroles (azoles) | 4 | `COC(=O)[C@H](CC1C=NC=N1)NC(=O)[C@@H]1CCC(=O)N1` | (-inf, HL, 6.34, L, +inf) |
| ligand_7842 | Phenylmethyloxycarbonylglycylglycyl-L-histidine m… | L | Pyrroles (azoles) | 5 | `COC(=O)[C@H](CC1C=NC=N1)NC(=O)CNC(=O)CNC(=O)OCc1ccccc1` | (-inf, HL, 6.11, L, +inf) |
| ligand_7853 | L-Histidine methyl ester | L | Pyrroles (azoles) | 27 | `COC(=O)[C@@H](N)Cc1c[nH]cn1` | (-inf, H2L, 5.27, HL, 7.22, L, +inf) |

### Functional groups across all SQL matches (46 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 40 | 87% |
| aromatic_ring | 38 | 83% |
| amide | 31 | 67% |
| primary_amine | 26 | 57% |
| imine | 9 | 20% |
| ester | 5 | 11% |
| secondary_amine | 5 | 11% |
| thiol | 4 | 9% |
| hydroxyl | 3 | 7% |
| halide | 2 | 4% |
| phenol | 2 | 4% |
| pyridine | 1 | 2% |
| tertiary_amine | 1 | 2% |
| thioether | 1 | 2% |

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

### Step 7: `get_table_schema`
**Args:**
```json
{
  "table_name": "ligandmetal_stability_measured",
  "database": "equilibrium"
}
```

[summary]
**get_table_schema:** Error - Table 'ligandmetal_stability_measured' not found.
Available tables: eq_collection_unassigned, eq_edge, eq_edge_species, eq_export_metadata, eq_map, eq_map_collection, eq_map_stray, eq_network, eq_network_species, eq_node, eq_node_species, sqlite_sequence

---

### Step 8: `get_table_schema`
**Args:**
```json
{
  "table_name": "ligandmetal_card",
  "database": "cards"
}
```

[summary]
## get_table_schema - 17 column(s)

| cid | name | type | notnull | pk |
|-----|------|------|---------|----|
| 0 | card_id | INTEGER | False | True |
| 1 | complex_system_id | INTEGER | True | False |
| 2 | metal_id | INTEGER | True | False |
| 3 | ligand_id | INTEGER | True | False |
| 4 | beta_definition_id | INTEGER | True | False |
| 5 | complex_id | TEXT | False | False |
| 6 | ligand_class_id | INTEGER | False | False |
| 7 | ligand_class_name | TEXT | False | False |
| 8 | metal_name_SRD | TEXT | False | False |
| 9 | metal_SMILES | TEXT | False | False |
| 10 | metal_InChi | TEXT | False | False |
| 11 | ligand_name_SRD | TEXT | False | False |
| 12 | ligand_SMILES | TEXT | False | False |
| 13 | ligand_InChi | TEXT | False | False |
| 14 | ligand_HxL_definition_SRD | TEXT | False | False |
| 15 | beta_definition_name | TEXT | False | False |
| 16 | created_at | TIMESTAMP | False | False |

---

### Step 9: `get_table_schema`
**Args:**
```json
{
  "table_name": "beta_definition",
  "database": "equilibrium"
}
```

[summary]
**get_table_schema:** Error - Table 'beta_definition' not found.
Available tables: eq_collection_unassigned, eq_edge, eq_edge_species, eq_export_metadata, eq_map, eq_map_collection, eq_map_stray, eq_network, eq_network_species, eq_node, eq_node_species, sqlite_sequence

---

### Step 10: `get_table_schema`
**Args:**
```json
{
  "table_name": "literature",
  "database": "literature"
}
```

[summary]
## get_table_schema - 6 column(s)

| cid | name | type | notnull | pk |
|-----|------|------|---------|----|
| 0 | literature_id | INTEGER | False | True |
| 1 | paper_id | INTEGER | False | False |
| 2 | year | INTEGER | False | False |
| 3 | issue | INTEGER | False | False |
| 4 | page | INTEGER | False | False |
| 5 | comment | TEXT | False | False |

---

### Step 11: `get_table_schema`
**Args:**
```json
{
  "table_name": "rv_literature_vlm",
  "database": "literature"
}
```

[summary]
**get_table_schema:** Error - Table 'rv_literature_vlm' not found.
Available tables: author, footnote, literature, literature_alt, paper, verk_literature_author, vlm_literature, vlm_literature_sic

---

### Step 12: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND c.ligand_id = ligand_5898)",
  "order_by": "c.beta_definition_id ASC, s.constant_type ASC, s.constant_value DESC",
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
| vlm_98923 | ref_eq_map_1353 | beta_def_204 | logK | 5.67 | 25 | 0.1 | `[MHL2] + [H] <=> [M(HL)2]` | *** |  |  |
| vlm_98921 | *** | beta_def_788 | ΔH | -27.6 | 25 | 0.1 | `[ML] + [H] <=> [MHL]` | *** |  |  |
| vlm_98919 | ref_eq_map_1353 | beta_def_788 | logK | 4.86 | 25 | 0.1 | `[ML] + [H] <=> [MHL]` | *** |  |  |
| vlm_98920 | ref_eq_map_1354 | beta_def_788 | logK | 4.61 | 37 | 0.15 | `[ML] + [H] <=> [MHL]` | *** |  |  |
| vlm_98922 | *** | beta_def_788 | ΔS | 0.4 | 25 | 0.1 | `[ML] + [H] <=> [MHL]` | *** |  |  |
| vlm_98924 | ref_eq_map_1353 | beta_def_792 | logK | 5.8 | 25 | 0.1 | `[ML2] + [H] <=> [MHL2]` | *** |  |  |
| vlm_98926 | ref_eq_map_1354 | beta_def_792 | logK | 5.5 | 37 | 0.15 | `[ML2] + [H] <=> [MHL2]` | *** |  |  |
| vlm_98925 | ref_eq_map_1358 | beta_def_792 | logK | -5.54 | 25 | 0.1 | `[ML2] + [H] <=> [MHL2]` | *** |  |  |
| vlm_98904 | *** | beta_def_812 | ΔH | -20.1 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.1, L, +inf) |
| vlm_98905 | *** | beta_def_812 | ΔH | -23 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (9.1, L, +inf) |
| vlm_98903 | ref_eq_map_1357 | beta_def_812 | logK | 7.07 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (9.1, L, +inf) |
| vlm_98902 | ref_eq_map_1356 | beta_def_812 | logK | 6.58 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.1, L, +inf) |
| vlm_98899 | ref_eq_map_1353 | beta_def_812 | logK | 6.51 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.1, L, +inf) |
| vlm_98901 | ref_eq_map_1355 | beta_def_812 | logK | 6.48 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.1, L, +inf) |
| vlm_98900 | ref_eq_map_1354 | beta_def_812 | logK | 6.35 | 37 | 0.15 | `[M] + [L] <=> [ML]` | *** | [L] | (9.1, L, +inf) |
| vlm_98906 | *** | beta_def_812 | ΔS | 57.3 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.1, L, +inf) |
| vlm_98914 | *** | beta_def_840 | ΔH | 0 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.1, L, +inf) |
| vlm_98913 | *** | beta_def_840 | ΔH | -47.3 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.1, L, +inf) |
| vlm_98915 | *** | beta_def_840 | ΔH | -49.4 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.1, L, +inf) |
| vlm_98912 | ref_eq_map_1357 | beta_def_840 | logK | 12.74 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.1, L, +inf) |
| vlm_98911 | ref_eq_map_1356 | beta_def_840 | logK | 12.29 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.1, L, +inf) |
| vlm_98907 | ref_eq_map_1353 | beta_def_840 | logK | 12.04 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.1, L, +inf) |
| vlm_98910 | ref_eq_map_1355 | beta_def_840 | logK | 11.91 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.1, L, +inf) |
| vlm_98909 | ref_eq_map_1354 | beta_def_840 | logK | 11.67 | 37 | 0.15 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.1, L, +inf) |
| vlm_98908 | ref_eq_map_1358 | beta_def_840 | logK | -12.18 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.1, L, +inf) |
| vlm_98916 | *** | beta_def_840 | ΔS | 72 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.1, L, +inf) |
| vlm_98918 | *** | beta_def_840 | ΔS | 58.2 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.1, L, +inf) |
| vlm_98917 | *** | beta_def_840 | ΔS | -67.4 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.1, L, +inf) |
| vlm_98927 | ref_eq_map_1355 | beta_def_984 | logK | 9.95 | 25 | 0.5 | `[M(OH)L2] + [H] <=> [ML2] + [H2O]` | *** |  |  |

---
