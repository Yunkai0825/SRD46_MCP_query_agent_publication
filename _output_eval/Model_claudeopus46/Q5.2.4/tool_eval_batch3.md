# Q5.2.4 — Tool Results (batch 3)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "plutonium"
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
  "name": "aspirin"
}
```

[summary]
## search_ligands — 2 result(s)

**stats:** 2 SQL matches · showing 2 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_10895 | 2-(Acetylthio)benzoic acid (thioaspirin) | *** | Ligands not selected | 0 | *** | *** |
| ligand_10913 | Acetylsalicylic acid (Aspirin) | *** | Ligands not selected | 0 | *** | *** |

---

### Step 4: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_149",
  "ligand_id": "ligand_10913"
}
```

[summary]
[CATALOG]
## build_system_catalog

*(no pairs found)*

**summary:** {'n_metals': 0, 'n_ligands': 0, 'n_pairs': 0, 'total_species': 0}

---

### Step 6: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_149 AND c.ligand_id = ligand_10913)"
}
```

[summary]
## search_stability

*(no results)*

---

### Step 7: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_10913"
}
```

[summary]
## inspect_card — Ligand | ligand_10913

**Name:** Acetylsalicylic acid (Aspirin)  
**Formula:** ******** | **Class:** Ligands not selected  

**pKa values:** none

**Partners:** 0 metal(s), 0 measurement(s) total

*(no metal partners)*

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_149 AND c.ligand_name_SRD LIKE '%salicyl%')",
  "limit": 10
}
```

[summary]
## search_stability — 10 row(s)

### `H^[+]` + 2-Hydroxybenzoic acid 2-(dihydrogenphosphate) (Salicyl phos… — 6 measurement(s)
metal_id: metal_68 | ligand_id: ligand_8636
ligand_HxL_def: H4L | ligand_SMILES: O=C(O)c1ccccc1OP(=O)(O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_147030 | ref_eq_map_18078 | beta_def_79 | logK | 6.61 | 25 | 0.1 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (3.69, HL, 6.61, L, +inf) |
| vlm_147031 | *** | beta_def_79 | ΔH | 0 | 25 | 0.1 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (3.69, HL, 6.61, L, +inf) |
| vlm_147032 | *** | beta_def_79 | ΔS | -41.8 | 25 | 0.1 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (3.69, HL, 6.61, L, +inf) |
| vlm_147033 | ref_eq_map_18078 | beta_def_32 | logK | 3.69 | 25 | 0.1 | `[HL] + [H] <=> [H2L]` | *** | [HL]; [H2L] | (-inf, H2L, 3.69, HL, 6.61) |
| vlm_147034 | *** | beta_def_32 | ΔH | 0 | 25 | 0.1 | `[HL] + [H] <=> [H2L]` | *** | [HL]; [H2L] | (-inf, H2L, 3.69, HL, 6.61) |
| vlm_147035 | *** | beta_def_32 | ΔS | -12.6 | 25 | 0.1 | `[HL] + [H] <=> [H2L]` | *** | [HL]; [H2L] | (-inf, H2L, 3.69, HL, 6.61) |

### `VO^[2+]` + 2-Hydroxybenzoic acid 2-(dihydrogenphosphate) (Salicyl phos… — 3 measurement(s)
metal_id: metal_201 | ligand_id: ligand_8636
ligand_HxL_def: H4L | ligand_SMILES: O=C(O)c1ccccc1OP(=O)(O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_147036 | ref_eq_map_18079 | beta_def_812 | logK | 5.81 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (6.61, L, +inf) |
| vlm_147037 | ref_eq_map_18079 | beta_def_966 | logK | 5.7 | 25 | 0.1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |
| vlm_147038 | ref_eq_map_18079 | beta_def_553 | logK | 2.3 | 25 | 0.1 | `[MOL]^2 <=> [M2O2L2]` | *** |  |  |

### `H^[+]` + 2-Carboxy-6-(methoxycarbonyl)phenol 1-(dihydrogenphosphate) — 1 measurement(s)
metal_id: metal_68 | ligand_id: ligand_8637
ligand_HxL_def: H3L | ligand_SMILES: COC(=O)c1cccc(C(=O)O)c1OP(=O)(O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_147040 | ref_eq_map_18080 | beta_def_79 | logK | 7.63 | 35 | 0.1 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (3.38, HL, 7.63, L, +inf) |

---
