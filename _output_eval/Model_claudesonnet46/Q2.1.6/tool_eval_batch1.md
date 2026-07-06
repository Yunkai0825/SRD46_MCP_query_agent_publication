# Q2.1.6 — Tool Results (batch 1)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "cadmium, lead, mercury",
  "limit": 10
}
```

[summary]
## search_metals

*(no results)*

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "thiocyan",
  "limit": 10
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_10092 | Hydrogen thiocyanate (Thiocyanic acid) | HL | Inorganic ligands | 434 | `N=C=S` | (-inf, HL, -1.1, L, +inf) |

---

### Step 4: `search_metals`
**Args:**
```json
{
  "name": "cadmium",
  "limit": 5
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_26 | Cd^[2+] | Cd | 2 | ✓ | [Cd+2] | InChI=1S/Cd/q+2 | beta_totN_95 | ligand_totN_818 | vlm_totN_2828 |

---

### Step 5: `search_metals`
**Args:**
```json
{
  "name": "lead",
  "limit": 5
}
```

[summary]
## search_metals — 5 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_16 | Bu_[3]Pb^[+] | B | 1 |  | *** | *** | beta_totN_2 | ligand_totN_1 | vlm_totN_2 |
| metal_46 | Et_[2]Pb^[2+] | E2Pb | 2 |  | *** | *** | beta_totN_2 | ligand_totN_3 | vlm_totN_5 |
| metal_49 | Et_[3]Pb^[+] | E3Pb | 1 |  | *** | *** | beta_totN_2 | ligand_totN_3 | vlm_totN_5 |
| metal_84 | Me_[2]Pb^[2+] | M2Pb | 2 |  | *** | *** | beta_totN_5 | ligand_totN_4 | vlm_totN_9 |
| metal_87 | Me_[3]Pb^[+] | M3Pb | 1 |  | *** | *** | beta_totN_7 | ligand_totN_23 | vlm_totN_33 |

---

### Step 6: `search_metals`
**Args:**
```json
{
  "name": "mercury",
  "limit": 5
}
```

[summary]
## search_metals — 5 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_20 | BuHg^[+] | B | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_53 | EtHg^[+] | EHg | 1 |  | *** | *** | beta_totN_4 | ligand_totN_3 | vlm_totN_6 |
| metal_71 | Hg^[2+] | Hg | 2 | ✓ | [Hg+2] | InChI=1S/Hg/q+2 | beta_totN_68 | ligand_totN_310 | vlm_totN_1097 |
| metal_72 | Hg^[+] | Hg | 1 | ✓ | [Hg+] | InChI=1S/Hg/q+1 | beta_totN_12 | ligand_totN_31 | vlm_totN_83 |
| metal_93 | MeHg^[+] | MHg | 1 |  | *** | *** | beta_totN_18 | ligand_totN_79 | vlm_totN_148 |

---

### Step 7: `search_metals`
**Args:**
```json
{
  "symbol": "Pb",
  "limit": 5
}
```

[summary]
## search_metals — 5 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_16 | Bu_[3]Pb^[+] | B | 1 |  | *** | *** | beta_totN_2 | ligand_totN_1 | vlm_totN_2 |
| metal_46 | Et_[2]Pb^[2+] | E2Pb | 2 |  | *** | *** | beta_totN_2 | ligand_totN_3 | vlm_totN_5 |
| metal_49 | Et_[3]Pb^[+] | E3Pb | 1 |  | *** | *** | beta_totN_2 | ligand_totN_3 | vlm_totN_5 |
| metal_84 | Me_[2]Pb^[2+] | M2Pb | 2 |  | *** | *** | beta_totN_5 | ligand_totN_4 | vlm_totN_9 |
| metal_87 | Me_[3]Pb^[+] | M3Pb | 1 |  | *** | *** | beta_totN_7 | ligand_totN_23 | vlm_totN_33 |

---

### Step 8: `search_metals`
**Args:**
```json
{
  "smiles": "[Pb+2]",
  "limit": 5
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_125 | Pb^[2+] | Pb | 2 | ✓ | [Pb+2] | InChI=1S/Pb/q+2 | beta_totN_80 | ligand_totN_470 | vlm_totN_1585 |

---

### Step 9: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_26",
  "ligand_id": "ligand_10092"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 4 species

### Cd^[2+] + Hydrogen thiocyanate (Thiocyanic acid)
**metal_id:** metal_26 | **ligand_id:** ligand_10092 | **ligand_def_HxL:** HL  
**entries:** 51 | **species:** 4 | **vlm_count:** 51

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 15 |
| beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | [M] + [L]^2 <=> [ML2] | [ML2](aqueous), [M](aqueous), [L](aqueous) | 16 |
| beta_def_872 | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | [M] + [L]^3 <=> [ML3] | [ML3](aqueous), [M](aqueous), [L](aqueous) | 13 |
| beta_def_894 | [ML<sub>4</sub>]/[M][L]<sup>4</sup> | [M] + [L]^4 <=> [ML4] | [ML4](aqueous), [M](aqueous), [L](aqueous) | 7 |

**vlm_ids:** vlm_172405, vlm_172406, vlm_172407, vlm_172408, vlm_172409, … vlm_172453, vlm_172454, vlm_172455 (51 listed)

**equilibrium_maps:** 7 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_27996 | 4 | 6 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_27997 | 4 | 6 | 19~29 °C | 1.85~2.15 M |
| ref_eq_net_27998 | 4 | 6 | 19~29 °C | 0.35~0.65 M |
| ref_eq_net_27999 | 4 | 6 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_28000 | 4 | 6 | 19~29 °C | 2.85~3.15 M |
| ref_eq_net_28001 | 2 | 1 | 19~29 °C | -0.15~0.15 M |
| ref_eq_net_28002 | 1 | 0 | 19~29 °C | 1.85~2.15 M |

---

### Step 11: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_26 AND c.ligand_id = ligand_10092 AND s.constant_type = 'log_beta')",
  "order_by": "s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability

*(no results)*

---

### Step 12: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_125 AND c.ligand_id = ligand_10092 AND s.constant_type = 'log_beta')",
  "order_by": "s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability

*(no results)*

---

### Step 13: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.ligand_id = ligand_10092 AND s.constant_type = 'log_beta')",
  "order_by": "s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability

*(no results)*

---
