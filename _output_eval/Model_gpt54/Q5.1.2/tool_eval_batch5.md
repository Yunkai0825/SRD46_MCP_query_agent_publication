# Q5.1.2 — Tool Results (batch 5)

### Step 2: `search_ligands`
**Args:**
```json
{
  "name": "DTPA, diethylenetriaminepentaacetic acid, pentetic acid",
  "limit": 10
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 4: `search_pka_ligands`
**Args:**
```json
{
  "where": "(lc.ligand_name_SRD LIKE '%diethylenetriaminepentaacetic%' OR lc.ligand_name_SRD LIKE '%pentetic%' OR lc.ligand_name_SRD LIKE '%pentetate%' OR lc.ligand_name_SRD LIKE '%DTPA%' OR lc.ligand_name_SRD LIKE '%DETAPAC%')",
  "limit": 20
}
```

[summary]
## search_pka_ligands — 20 row(s)

| ligand_id | ligand_name | HxL_def | formula | smiles | pH_ladder | T°C_range | I(M)_range | similarity_score |
|-----------|-------------|---------|---------|--------|-----------|-----------|------------|------------------|
| ligand_6117 | 9,17-Dioxo-1,4,7,10,13,16-hexaazacyclooctadecane-1,4,7-tria… | H3L | C18H24N6O8 | O=C(O)CN1CCN(CC(=O)O)CC(=O)NCCNCCNC(=O)CN(CC(=O)O)CC1 | −∞; H5L (M_tot_1); (-1.8, vlm_103954); H4L (M_tot_1); (2.62, vlm_103953); H3L (M_tot_1); (4.1, vlm_103952); H2L (M_tot_1); (8.87, vlm_103951); HL (M_tot_1); (10.02, vlm_103950); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_6356 | Diethylenetrinitrilopentaacetic acid (DTPA) | H5L | C14H23N3O10 | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | −∞; HL (M_tot_2); (-9.9, vlm_112470); L (M_tot_58); (-8.4, vlm_112484); HL (M_tot_2); (-1.6, vlm_112522); H5L (M_tot_1); (-0.7, vlm_112524); H6L (M_tot_1); (-0.1, vlm_112526); H7L (M_tot_1); (2, vlm_112514); H4L (M_tot_1); (2.7, vlm_112506); H3L (M_tot_1); (4.28, vlm_112498); H2L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6362 | Diethylenetrinitrilopentaacetic acid N,N"-bis(methylamide) … | *** | C16H21N5O8 | *** | −∞; H4L (M_tot_1); (-1.4, vlm_112939); H3L (M_tot_1); (3.31, vlm_112936); H2L (M_tot_1); (4.38, vlm_112933); HL (M_tot_1); (9.37, vlm_112930); L (M_tot_9); +∞ | 25 | 0.1 | *** |
| ligand_6363 | Diethylenetrinitrilopentaacetic acid N,N"-bis(butylamide) (… | *** | C22H33N5O8 | *** | −∞; H3L (M_tot_1); (3.31, vlm_112975); H2L (M_tot_1); (4.44, vlm_112974); HL (M_tot_1); (9.36, vlm_112973); L (M_tot_3); +∞ | 25 | 0.1 | *** |

---

### Step 5: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_name_SRD LIKE '%diethylenetriaminepentaacetic%' OR c.ligand_name_SRD LIKE '%pentetic%' OR c.ligand_name_SRD LIKE '%pentetate%' OR c.ligand_name_SRD LIKE '%DTPA%' OR c.ligand_name_SRD LIKE '%DETAPAC%')",
  "limit": 20
}
```

[summary]
## search_stability — 20 row(s)

### `H^[+]` + 9,17-Dioxo-1,4,7,10,13,16-hexaazacyclooctadecane-1,4,7-tria… — 5 measurement(s)
metal_id: metal_68 | ligand_id: ligand_6117
ligand_HxL_def: H3L | ligand_SMILES: O=C(O)CN1CCN(CC(=O)O)CC(=O)NCCNCCNC(=O)CN(CC(=O)O)CC1

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_103950 | ref_eq_map_3173 | beta_def_79 | logK | 10.02 | 25 | 0.1 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (8.87, HL, 10.02, L, +inf) |
| vlm_103951 | ref_eq_map_3173 | beta_def_32 | logK | 8.87 | 25 | 0.1 | `[HL] + [H] <=> [H2L]` | *** | [HL]; [H2L] | (4.1, H2L, 8.87, HL, 10.02) |
| vlm_103952 | ref_eq_map_3173 | beta_def_53 | logK | 4.1 | 25 | 0.1 | `[H2L] + [H] <=> [H3L]` | *** | [H2L]; [H3L] | (2.62, H3L, 4.1, H2L, 8.87) |
| vlm_103953 | ref_eq_map_3173 | beta_def_64 | logK | 2.62 | 25 | 0.1 | `[H3L] + [H] <=> [H4L]` | *** | [H3L]; [H4L] | (-1.8, H4L, 2.62, H3L, 4.1) |
| vlm_103954 | ref_eq_map_3173 | beta_def_68 | logK | -1.8 | 25 | 0.1 | `[H4L] + [H] <=> [H5L]` | *** | [H4L]; [H5L] | (-inf, H5L, -1.8, H4L, 2.62) |

### `Eu^[3+]` + 9,17-Dioxo-1,4,7,10,13,16-hexaazacyclooctadecane-1,4,7-tria… — 1 measurement(s)
metal_id: metal_58 | ligand_id: ligand_6117
ligand_HxL_def: H3L | ligand_SMILES: O=C(O)CN1CCN(CC(=O)O)CC(=O)NCCNCCNC(=O)CN(CC(=O)O)CC1

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_103955 | ref_eq_map_3174 | beta_def_812 | logK | 17.2 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (10.02, L, +inf) |

### `H^[+]` + Diethylenetrinitrilopentaacetic acid (DTPA) — 14 measurement(s)
metal_id: metal_68 | ligand_id: ligand_6356
ligand_HxL_def: H5L | ligand_SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_112470 | ref_eq_map_6631 | beta_def_79 | logK | -9.9 | 25 | 0.1 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (-9.9, HL, -8.4, L, +inf) |
| vlm_112471 | ref_eq_map_6634 | beta_def_79 | logK | -9.67 | 37 | 0.15 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (-9.9, HL, -8.4, L, +inf) |
| vlm_112472 | ref_eq_map_6636 | beta_def_79 | logK | 10.5 | 25 | 0.1 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (-9.9, HL, -8.4, L, +inf) |
| vlm_112473 | ref_eq_map_6640 | beta_def_79 | logK | 10.79 | 25 | 0.1 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (-9.9, HL, -8.4, L, +inf) |
| vlm_112474 | ref_eq_map_6632 | beta_def_79 | logK | 9.42 | 25 | 0.5 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (-9.9, HL, -8.4, L, +inf) |
| vlm_112475 | ref_eq_map_6637 | beta_def_79 | logK | 9.49 | 20 | 0.5 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (-9.9, HL, -8.4, L, +inf) |
| vlm_112476 | ref_eq_map_6638 | beta_def_79 | logK | 9.9 | 25 | 0.5 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (-9.9, HL, -8.4, L, +inf) |
| vlm_112477 | ref_eq_map_6635 | beta_def_79 | logK | 9.48 | 20 | 1 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (-9.9, HL, -8.4, L, +inf) |
| vlm_112478 | ref_eq_map_6633 | beta_def_79 | logK | 9.98 | 25 | 1 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (-9.9, HL, -8.4, L, +inf) |
| vlm_112479 | ref_eq_map_6639 | beta_def_79 | logK | 10.46 | 20 | 1 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (-9.9, HL, -8.4, L, +inf) |
| vlm_112480 | *** | beta_def_79 | ΔH | -34.3 | 10 | 0.1 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (-9.9, HL, -8.4, L, +inf) |
| vlm_112481 | *** | beta_def_79 | ΔH | -33.5 | 25 | 0.1 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (-9.9, HL, -8.4, L, +inf) |
| vlm_112482 | *** | beta_def_79 | ΔH | -32.6 | 40 | 0.1 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (-9.9, HL, -8.4, L, +inf) |
| vlm_112483 | *** | beta_def_79 | ΔS | 88.7 | 25 | 0.1 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (-9.9, HL, -8.4, L, +inf) |

---
