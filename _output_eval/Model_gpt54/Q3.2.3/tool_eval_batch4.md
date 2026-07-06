# Q3.2.3 — Tool Results (batch 4)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Calcium",
  "limit": 10
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_25 | Ca^[2+] | Ca | 2 | ✓ | [Ca+2] | InChI=1S/Ca/q+2 | beta_totN_68 | ligand_totN_644 | vlm_totN_1761 |

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "Oxalic acid",
  "limit": 10
}
```

[summary]
## search_ligands — 4 result(s)

**stats:** 4 SQL matches · showing 4 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8872 | Ethanedioic acid (Oxalic acid) | H2L | Carboxylic acids diacids | 394 | `O=C(O)C(=O)O` | (-inf, H2L, -1.2, HL, 3.8, L, +inf) |
| ligand_8960 | Oxopropanedioic acid (Ketomaloni… (Mesoxalic acid) | H2L | Carboxylic acids diacids… | 3 | `O=C(O)C(=O)C(=O)O` | (-inf, H2L, -1.82, HL, 3.52, L, +inf) |
| ligand_9763 | Dithiooxalic acid | H2L | miscellaneous mercaptans | 3 | `O=C(S)C(=O)S` | *** |
| ligand_11304 | Ethanedi(dithioic acid) (Tetrathiooxalic acid) | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (3 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 2 | 67% |
| ketone | 1 | 33% |
| thiol | 1 | 33% |

---

### Step 4: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_25",
  "ligand_id": "ligand_8872"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 3 species

### Ca^[2+] + Ethanedioic acid (Oxalic acid)
**metal_id:** metal_25 | **ligand_id:** ligand_8872 | **ligand_def_HxL:** H2L  
**entries:** 17 | **species:** 3 | **vlm_count:** 17

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_307 | [M][L]/[ML(H<sub>2</sub>O)<sub>3</sub>(… | [ML(H2O)3(s)] <=> [M] + [L] + [H2O]^3 | [M](aqueous), [L](aqueous), [H2O](aqueous), [ML(H2O)3(s)](solid) | 2 |
| beta_def_327 | [M][L]/[ML(H<sub>2</sub>O)(s)] | [ML(H2O)(s)] <=> [M] + [L] + [H2O] | [M](aqueous), [L](aqueous), [H2O](aqueous), [ML(H2O)(s)](solid) | 9 |
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 6 |

**vlm_ids:** vlm_151595, vlm_151596, vlm_151597, vlm_151598, vlm_151599, … vlm_151609, vlm_151610, vlm_151611 (17 listed)

**equilibrium_maps:** 9 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_19954 | 3 | 3 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_19955 | 2 | 1 | 31~41 °C | 0.35~0.65 M |
| ref_eq_net_19956 | 3 | 3 | 31~41 °C | -0.15~0.15 M |
| ref_eq_net_19957 | 2 | 1 | 31~41 °C | -0.05~0.25 M |
| ref_eq_net_19958 | 2 | 1 | 31~41 °C | 0~0.3 M |
| ref_eq_net_19959 | 2 | 1 | 13~23 °C | -0.15~0.15 M |
| ref_eq_net_19960 | 1 | 0 | 31~41 °C | 0.35~0.65 M |
| ref_eq_net_19961 | 1 | 0 | 31~41 °C | 0.85~1.15 M |
| ref_eq_net_19962 | 1 | 0 | 19~29 °C | -0.15~0.15 M |

---

### Step 6: `search_pka_values`
**Args:**
```json
{
  "where": "(lc.ligand_id = ligand_8872 AND p.temperature_c >= 20 AND p.temperature_c <= 30 AND (p.ionic_strength_mol_l IS NULL OR p.ionic_strength_mol_l <= 0.1))",
  "order_by": "p.pKa ASC",
  "limit": 20
}
```

[summary]
## search_pka_values — 2 row(s)

### pKa -1.5–-1.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_151532 | ligand_8872 | Ethanedioic acid (Oxalic acid) | H2L | O=C(O)C(=O)O | -1.2 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_7 |

### pKa 3.5–4.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_151494 | ligand_8872 | Ethanedioic acid (Oxalic acid) | H2L | O=C(O)C(=O)O | 3.8 | 25 | 0.1 | L→HL | M_tot_7 | M_tot_56 |

---

### Step 7: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_25 AND c.ligand_id = ligand_8872 AND s.temperature_c >= 20 AND s.temperature_c <= 30 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.1))",
  "order_by": "c.beta_definition_id, s.constant_value ASC",
  "limit": 30
}
```

[summary]
## search_stability — 5 row(s)

### `Ca^[2+]` + Ethanedioic acid (Oxalic acid) — 5 measurement(s)
metal_id: metal_25 | ligand_id: ligand_8872
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_151610 | ref_eq_map_19899 | beta_def_307 | logK | -8.32 | 25 | 0 | `[ML(H2O)3(s)] <=> [M] + [L] + [H2O]^3` | solid | [L] | (3.8, L, +inf) |
| vlm_151608 | ref_eq_map_19907 | beta_def_327 | logK | -8.75 | 25 | 0 | `[ML(H2O)(s)] <=> [M] + [L] + [H2O]` | solid | [L] | (3.8, L, +inf) |
| vlm_151602 | ref_eq_map_19904 | beta_def_327 | logK | -7.9 | 20 | 0.1 | `[ML(H2O)(s)] <=> [M] + [L] + [H2O]` | solid | [L] | (3.8, L, +inf) |
| vlm_151601 | ref_eq_map_19899 | beta_def_327 | logK | -7.86 | 25 | 0.1 | `[ML(H2O)(s)] <=> [M] + [L] + [H2O]` | solid | [L] | (3.8, L, +inf) |
| vlm_151599 | ref_eq_map_19899 | beta_def_812 | logK | 3.19 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (3.8, L, +inf) |

---
