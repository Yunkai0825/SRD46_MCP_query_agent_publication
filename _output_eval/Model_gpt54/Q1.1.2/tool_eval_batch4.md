# Q1.1.2 — Tool Results (batch 4)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "H+",
  "limit": 10
}
```

[summary]
## search_metals — 10 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_20 | BuHg^[+] | B | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_23 | BuNH_[3]^[+] | B | 1 |  | *** | *** | beta_totN_1 | ligand_totN_2 | vlm_totN_2 |
| metal_24 | C(NH_[2])_[3]^[+] | C | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_45 | Et_[2]NH_[2]^[+] | E2NH2 | 1 |  | *** | *** | beta_totN_1 | ligand_totN_1 | vlm_totN_1 |
| metal_48 | Et_[3]NH^[+] | E3NH | 1 |  | *** | *** | beta_totN_1 | ligand_totN_1 | vlm_totN_1 |
| metal_53 | EtHg^[+] | EHg | 1 |  | *** | *** | beta_totN_4 | ligand_totN_3 | vlm_totN_6 |
| metal_54 | EtNH_[3]^[+] | ENH3 | 1 |  | *** | *** | beta_totN_1 | ligand_totN_3 | vlm_totN_3 |
| metal_68 | H^[+] | H | 1 | ✓ | [H+] | InChI=1S/p+1 | beta_totN_82 | ligand_totN_4081 | vlm_totN_20720 |
| metal_69 | H_[5]TeO_[6]^[-] | H | -1 |  | *** | *** | beta_totN_1 | ligand_totN_1 | vlm_totN_2 |
| metal_70 | Hf^[4+] | Hf | 4 | ✓ | [Hf+4] | InChI=1S/Hf/q+4 | beta_totN_10 | ligand_totN_14 | vlm_totN_49 |

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "citric acid, citrate",
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
  "name": "citric",
  "limit": 50
}
```

[summary]
## search_ligands — 8 result(s)

**stats:** 8 SQL matches · showing 8 · limit 50

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_9057 | DL-1-Hydroxypropane-1,2,3-tricar… (Isocitric acid) | H3L | Carboxylic acids polyaci… | 24 | `O=C(O)CC(C(=O)O)C(O)C(=O)O` | (-inf, H3L, 3.05, H2L, 4.3, HL, 5.73, L, +inf) |
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxyli… (Citric acid) | H3L | Carboxylic acids polyaci… | 384 | `O=C(O)CC(O)(CC(=O)O)C(=O)O` | (-inf, H3L, 2.9, H2L, 4.35, HL, 5.65, L, +inf) |
| ligand_10950 | DL-Methylcitric acid | *** | Ligands not selected | 0 | *** | *** |
| ligand_10951 | DL-Homocitric acid | *** | Ligands not selected | 0 | *** | *** |
| ligand_10952 | DL-threo-2-Methylisocitric acid | *** | Ligands not selected | 0 | *** | *** |
| ligand_10953 | DL-erytho-2-Methylisocitric acid | *** | Ligands not selected | 0 | *** | *** |
| ligand_10954 | DL-threo-Homoisocitric acid | *** | Ligands not selected | 0 | *** | *** |
| ligand_10955 | DL-erythro-Fluorocitric acid | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (2 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 2 | 100% |
| hydroxyl | 2 | 100% |

---

### Step 5: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_68",
  "ligand_id": "ligand_9058"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 3 species

### H^[+] + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid)
**metal_id:** metal_68 | **ligand_id:** ligand_9058 | **ligand_def_HxL:** H3L  
**entries:** 48 | **species:** 3 | **vlm_count:** 48

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_32 | [H<sub>2</sub>L]/[HL][H] | [HL] + [H] <=> [H2L] | [H2L](aqueous), [HL](aqueous), [H](aqueous) | 14 |
| beta_def_53 | [H<sub>3</sub>L]/[H<sub>2</sub>L][H] | [H2L] + [H] <=> [H3L] | [H3L](aqueous), [H2L](aqueous), [H](aqueous) | 14 |
| beta_def_79 | [HL]/[L][H] | [L] + [H] <=> [HL] | [HL](aqueous), [L](aqueous), [H](aqueous) | 20 |

**vlm_ids:** vlm_157439, vlm_157440, vlm_157441, vlm_157442, vlm_157443, … vlm_157484, vlm_157485, vlm_157486 (48 listed)

**equilibrium_maps:** 14 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_22067 | 3 | 3 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_22068 | 3 | 3 | 31~41 °C | 0~0.3 M |
| ref_eq_net_22069 | 3 | 3 | 19~29 °C | 0.35~0.65 M |
| ref_eq_net_22070 | 3 | 3 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_22071 | 3 | 3 | 13~23 °C | 1.85~2.15 M |
| ref_eq_net_22072 | 3 | 3 | 19~29 °C | 1.85~2.15 M |
| ref_eq_net_22073 | 3 | 3 | 13~23 °C | 2.85~3.15 M |
| ref_eq_net_22074 | 3 | 3 | 19~29 °C | -0.15~0.15 M |
| ref_eq_net_22075 | 1 | 0 | 19~29 °C | -0.05~0.25 M |
| ref_eq_net_22076 | 1 | 0 | 31~41 °C | 0~0.3 M |
| ref_eq_net_22077 | 1 | 0 | 19~29 °C | -0.05~0.25 M |
| ref_eq_net_22078 | 1 | 0 | 31~41 °C | 0~0.3 M |
| ref_eq_net_22079 | 1 | 0 | 19~29 °C | 0.35~0.65 M |
| ref_eq_net_22080 | 1 | 0 | 19~29 °C | 0.85~1.15 M |

---

### Step 7: `search_pka_values`
**Args:**
```json
{
  "where": "(lc.ligand_id = ligand_9058)",
  "order_by": "p.pKa ASC, p.temperature_c ASC, p.ionic_strength_mol_l ASC",
  "limit": 200
}
```

[summary]
## search_pka_values — 3 row(s)

### pKa 2.5–3.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_157473 | ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxyl… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 2.9 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_12 |

### pKa 4.0–4.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_157459 | ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxyl… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 4.35 | 25 | 0.1 | HL→H2L | M_tot_12 | M_tot_18 |

### pKa 5.5–6.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_157439 | ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxyl… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 5.65 | 25 | 0.1 | L→HL | M_tot_18 | M_tot_57 |

---
