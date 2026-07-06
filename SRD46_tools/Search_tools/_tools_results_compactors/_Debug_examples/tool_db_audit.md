# Tool ↔ DB audit

## search_metals
- **primary**: `cards.metal_card`
- **secondary**:
  - cards.ligandmetal_card (counts)
- **raw keys** (10): `beta_def_count, charge, inchi, is_simple_ion, ligand_count, metal_id, metal_name, smiles, symbol, vlm_count`

```markdown
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_41 | Cu^[2+] | Cu | 2 | ✓ | [Cu+2] | InChI=1S/Cu/q+2 | beta_totN_264 | ligand_totN_1951 | vlm_totN_8963 |
```

## search_ligands
- **primary**: `cards.ligand_card`
- **secondary**:
  - cards.ligand_pka_bracket  (-> pka_brackets enrichment)
  - cards.ligandmetal_card    (-> vlm_count enrichment)
- **raw keys** (11): `common_name, formula, inchi, iupac_name, ligand_HxL_definition, ligand_class, ligand_id, ligand_name, pka_brackets, smiles, vlm_count`

```markdown
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 3

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5760 | Aminoacetic acid (Glycine) | HL | Amino Acids | 428 | `NCC(=O)O` | (-inf, H2L, 2.33, HL, 9.57, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 1 | 100% |
| primary_amine | 1 | 100% |
```

## search_stability
- **primary**: `cards.ligandmetal_card JOIN cards.ligandmetal_stability_measured`
- **secondary**:
  - cards.ligand_pka_bracket  (-> pKa_bracket_involved enrichment)
  - equilibrium.eq_node JOIN equilibrium.eq_network  (-> map_id enrichment)
- **raw keys** (26): `HxL_involved, HxL_involved_json, LHS_species_json, RHS_species_json, beta_definition_id, beta_definition_name, constant_type, electrolyte, equation, equation_str, equation_tree_json, ionic_strength, ligand_HxL_definition, ligand_SMILES, ligand_class_name, ligand_id, ligand_name, log_K, map_id, metal_id, metal_name, pKa_bracket_involved, reaction_type, solvent, temperature, vlm_id`

```markdown
## search_stability — 5 row(s)

### `Cu^[2+]` + Aminoacetic acid (Glycine) — 5 measurement(s)
metal_id: metal_41 | ligand_id: ligand_5760
ligand_HxL_def: HL | ligand_SMILES: NCC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_93847 | ref_eq_map_86 | beta_def_812 | logK | 8.19 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.57, L, +inf) |
| vlm_93848 | ref_eq_map_87 | beta_d
```

## search_pka_values
- **primary**: `cards.ligand_card JOIN cards.ligand_pka_measured`
- **secondary**:
  - cards.ligandmetal_card + cards.ligandmetal_stability_measured (-> M_tot, M_above, M_below per protonation form)
- **raw keys** (21): `M_above, M_below, M_tot, bracket_from, bracket_to, electrolyte, formula, ionic_strength, ligand_HxL_definition, ligand_class_name, ligand_id, ligand_name, method, pKa, pKa_type, pka_id, quality, smiles, solvent, source_vlm_id, temperature`

```markdown
## search_pka_values — 2 row(s)

### pKa 2.0–2.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_93627 | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 2.33 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_20 |

### pKa 9.5–10.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_
```

## search_pka_ligands
- **primary**: `cards.ligand_card JOIN cards.ligand_pka_measured`
- **secondary**:
  - cards.ligandmetal_card + cards.ligandmetal_stability_measured (-> M_tot, M_above, M_below)
- **raw keys** (21): `M_above, M_below, M_tot, bracket_from, bracket_to, electrolyte, formula, ionic_strength, ligand_HxL_definition, ligand_class_name, ligand_id, ligand_name, method, pKa, pKa_type, pka_id, quality, smiles, solvent, source_vlm_id, temperature`

```markdown
## search_pka_ligands — 2 row(s)

| ligand_id | ligand_name | HxL_def | formula | smiles | pH_ladder | T°C_range | I(M)_range | similarity_score |
|-----------|-------------|---------|---------|--------|-----------|-----------|------------|------------------|
| ligand_5760 | Aminoacetic acid (Glycine) | HL | C2H5N1O2 | NCC(=O)O | −∞; H2L (M_tot_1); (2.33, vlm_93627); HL (M_tot_20); (9.57, vlm_93606); L (M_tot_43); +∞ | 25 | 0.1 | *** |
```

## search_networks
- **primary**: `equilibrium.eq_map_collection JOIN eq_map JOIN eq_network JOIN eq_node`
- **secondary**:
  - ATTACH cards.ligand_card  (-> ligand_HxL_definition, ligand_SMILES per row)
- **raw keys** (20): `beta_definition_id, beta_definition_name, constant_type, edge_count, equation, ionic_max, ionic_min, ligand_HxL_definition, ligand_SMILES, ligand_id, ligand_name, log_K, metal_id, metal_name, network_db_id, node_count, node_id, temp_max, temp_min, vlm_id`

```markdown
## search_networks — 6 row(s)

> **Reference equilibrium networks** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### `Cu^[2+]` + Aminoacetic acid (Glycine) — 3 network(s)
metal_id: metal_41 | ligand_id: ligand_5760 | ligand_def_HxL: HL | ligand_SMILES: NCC(=O)O

| beta_def | equation |
|----------|----------|
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |
| beta_def_812 | ``[M] + [L] <=> [ML]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-
```

## search_citations
- **primary**: `cards.ref_vlm_literature_alt JOIN cards.ref_literature_alt (*** NOTE: NOT srd46_literature.db ***)`
- **secondary**:
  - (none — single GROUP BY for vlm_count aggregation)
- **raw keys** (5): `citation, example_vlm_id, literature_alt_id, shortcut, vlm_count`

```markdown
## search_citations — 3 row(s)

| example_vlm_id | vlm_count | lit_id | shortcut | citation |
|----------------|-----------|--------|----------|----------|
| vlm_161952 | 28 | lit_4478 | 64Ma | W. A. E. McBryde, Canad. J. Chem., 1964, 42, 1917 |
| vlm_118645 | 55 | lit_4480 | 64MA | F. J. Millero, J. C. Ahluwalia, and L. G. Hepler, J. Phys. Chem., 1964, 68, 3435 |
| vlm_161401 | 10 | lit_4481 | 64MAa | F. J. Millero, J. C. Ahluwalia, and L. G. Hepler, J. Chem. Eng. Data, 1964, 9, … |
```

## search_similar_ligands
- **primary**: `fingerprints.ligand_similarity`
- **secondary**:
  - cards.ligand_card  (-> ligand_name, smiles, HxL_canonical)
  - equilibrium.eq_map_collection + eq_node (-> eq_richness: metals_covered, top_maps, n_beta_defs)
- **raw keys** (9): `HxL_canonical, eq_richness, family_score, ligand_id, ligand_name, similarity_score, smiles, tversky_query_in_target, tversky_target_in_query`

```markdown
## search_similar_ligands — 3 row(s)

**Query:** Aminoacetic acid (Glycine)

| ligand_id | ligand_name | smiles | HxL_canonical | family_score | similarity_score | tversky_query_in_target | tversky_target_in_query | diff_catalog_fun_group |
|---|---|---|---|---|---|---|---|---|
| ligand_5760 | Aminoacetic acid (Glycine) | NCC(=O)O | HL | — | — | — | — | *(query)* |
| ligand_6951 | Glycinamide | NCC(N)=O | L | 0.5769 | 0.5385 | 0.7 | 0.7 | amide(+1); carboxyl(-1) |
| ligand_5788 | 3-Aminopropanoic acid (beta-Alanine) | NCCC(=O)O | HL | 0.68 | 0.5333 | 0.7767 | 0.6299 | no_diff_catalog_fun |
| l
```

## build_system_catalog
- **primary**: `cards.ligandmetal_card JOIN cards.ligandmetal_stability_measured (species_catalog, vlm_ids)`
- **secondary**:
  - equilibrium.eq_map_collection JOIN eq_map JOIN eq_network (-> eq_maps per pair: networks, condition ranges)
- **raw keys** (2): `pairs, summary`

```markdown
## build_system_catalog — 1 pair(s), 2 species

### Cu^[2+] + Aminoacetic acid (Glycine)
**metal_id:** metal_41 | **ligand_id:** ligand_5760 | **ligand_def_HxL:** HL  
**entries:** 30 | **species:** 2 | **vlm_count:** 30

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 15 |
| beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | [M] + [L]^2 <=> [ML2] | [ML2](aqueous), [M](aqueous), [L](a
```

## inspect_card(vlm_93847)
- **primary**: `cards.ligandmetal_card JOIN cards.ligandmetal_stability_measured`
- **secondary**:
  - ATTACH equilibrium  (eq_node JOIN eq_network -> networks)
  - ATTACH literature   (vlm_literature_sic JOIN literature_alt -> citations)
  - cards.ligand_pka_bracket  (-> pKa_bracket_involved)
- **raw keys** (5): `card, citations, networks, prefix_id, total_citations`

```markdown
## inspect_card — VLM | vlm_93847

### Metal
**metal_id:** metal_41 | **metal_name:** Cu^[2+]  
**metal_SMILES:** `[Cu+2]`  
**metal_InChi:** `InChI=1S/Cu/q+2`  

### Ligand
**ligand_id:** ligand_5760 | **ligand_name:** Aminoacetic acid (Glycine)  
**ligand_HxL_definition:** HL  
**ligand_SMILES:** `NCC(=O)O`  
**ligand_InChi:** `InChI=1S/C2H5NO2/c3-1-2(4)5/h1,3H2,(H,4,5)`  

### Stability
**vlm_id:** vlm_93847  
**beta_definition_id:** beta_def_812 | **beta_definition_name:** [ML]/[M][L]  
**data_type:** log_K | **log_K:** 8.19  
**temperature:** 25.0 °C | **ionic_strength:** 0.1 M  
**uncert
```

## inspect_literature(vlm_93847)
- **primary**: `literature.vlm_literature_sic JOIN literature.literature_alt`
- **secondary**:
  - (none)
- **raw keys** (3): `citations, prefix_id, total_citations`

```markdown
## inspect_literature — vlm_93847 — 163 citation(s)

| lit_id | shortcut | citation |
|--------|----------|----------|
| lit_297 | 31RG | H. L. Riley and V. Gallafent, J. Chem. Soc., 1931, 2029 |
| lit_366 | 34FR | E. Ferrell, J. M. Ridgion, and H. L. Riley, J. Chem. Soc., 1934, 1440 |
| lit_684 | 45FL | H. V. Flood and V. Lorzs, Tidskr. Kjemi. Berg., 1945, 5, 83 |
| lit_705 | 46K | R. M. Keefer, J. Amer. Chem. Soc., 1946, 68, 2329 |
| lit_762 | 48K | R. M. Keefer, J. Amer. Chem. Soc., 1948, 70, 476 |
| lit_849 | 49LO | H. A. Laitinen, E. L. Onstott, J. C. Bailar, Jr., and S. Swann, Jr., J. Am
```
