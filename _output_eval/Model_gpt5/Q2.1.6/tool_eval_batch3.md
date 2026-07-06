# Q2.1.6 — Tool Results (batch 3)

### Step 2: `search_metals`
**Args:**
```json
{
  "symbol": "Cd",
  "limit": 10
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_26 | Cd^[2+] | Cd | 2 | ✓ | [Cd+2] | InChI=1S/Cd/q+2 | beta_totN_95 | ligand_totN_818 | vlm_totN_2828 |

---

### Step 3: `search_metals`
**Args:**
```json
{
  "symbol": "Pb",
  "limit": 10
}
```

[summary]
## search_metals — 10 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_16 | Bu_[3]Pb^[+] | B | 1 |  | *** | *** | beta_totN_2 | ligand_totN_1 | vlm_totN_2 |
| metal_46 | Et_[2]Pb^[2+] | E2Pb | 2 |  | *** | *** | beta_totN_2 | ligand_totN_3 | vlm_totN_5 |
| metal_49 | Et_[3]Pb^[+] | E3Pb | 1 |  | *** | *** | beta_totN_2 | ligand_totN_3 | vlm_totN_5 |
| metal_84 | Me_[2]Pb^[2+] | M2Pb | 2 |  | *** | *** | beta_totN_5 | ligand_totN_4 | vlm_totN_9 |
| metal_87 | Me_[3]Pb^[+] | M3Pb | 1 |  | *** | *** | beta_totN_7 | ligand_totN_23 | vlm_totN_33 |
| metal_125 | Pb^[2+] | Pb | 2 | ✓ | [Pb+2] | InChI=1S/Pb/q+2 | beta_totN_80 | ligand_totN_470 | vlm_totN_1585 |
| metal_126 | Pb^[4+] | Pb | 4 | ✓ | [Pb+4] | InChI=1S/Pb/q+4 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_129 | Ph_[2]Pb^[2+] | Ph2Pb | 2 |  | *** | *** | beta_totN_2 | ligand_totN_1 | vlm_totN_2 |
| metal_130 | Ph_[3]Pb^[+] | Ph3Pb | 1 |  | *** | *** | beta_totN_1 | ligand_totN_2 | vlm_totN_2 |
| metal_140 | Pr_[2]Pb^[2+] | Pr | 2 |  | *** | *** | beta_totN_2 | ligand_totN_3 | vlm_totN_5 |

---

### Step 4: `search_metals`
**Args:**
```json
{
  "symbol": "Hg",
  "limit": 10
}
```

[summary]
## search_metals — 8 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_20 | BuHg^[+] | B | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_53 | EtHg^[+] | EHg | 1 |  | *** | *** | beta_totN_4 | ligand_totN_3 | vlm_totN_6 |
| metal_71 | Hg^[2+] | Hg | 2 | ✓ | [Hg+2] | InChI=1S/Hg/q+2 | beta_totN_68 | ligand_totN_310 | vlm_totN_1097 |
| metal_72 | Hg^[+] | Hg | 1 | ✓ | [Hg+] | InChI=1S/Hg/q+1 | beta_totN_12 | ligand_totN_31 | vlm_totN_83 |
| metal_93 | MeHg^[+] | MHg | 1 |  | *** | *** | beta_totN_18 | ligand_totN_79 | vlm_totN_148 |
| metal_136 | PhHg^[+] | PhHg | 1 |  | *** | *** | beta_totN_2 | ligand_totN_8 | vlm_totN_8 |
| metal_145 | PrHg^[+] | Pr | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_176 | O_[3]SPhHg | S | 0 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |

---

### Step 5: `search_ligands`
**Args:**
```json
{
  "name": "thiocyanate",
  "limit": 25
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_10092 | Hydrogen thiocyanate (Thiocyanic acid) | HL | Inorganic ligands | 434 | `N=C=S` | (-inf, HL, -1.1, L, +inf) |

---

### Step 6: `search_ligands`
**Args:**
```json
{
  "name": "thiocyanic acid",
  "limit": 25
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_10092 | Hydrogen thiocyanate (Thiocyanic acid) | HL | Inorganic ligands | 434 | `N=C=S` | (-inf, HL, -1.1, L, +inf) |

---

### Step 8: `build_system_catalog`
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

### Step 9: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_125",
  "ligand_id": "ligand_10092"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 3 species

### Pb^[2+] + Hydrogen thiocyanate (Thiocyanic acid)
**metal_id:** metal_125 | **ligand_id:** ligand_10092 | **ligand_def_HxL:** HL  
**entries:** 10 | **species:** 3 | **vlm_count:** 10

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 6 |
| beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | [M] + [L]^2 <=> [ML2] | [ML2](aqueous), [M](aqueous), [L](aqueous) | 3 |
| beta_def_872 | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | [M] + [L]^3 <=> [ML3] | [ML3](aqueous), [M](aqueous), [L](aqueous) | 1 |

**vlm_ids:** vlm_172483, vlm_172484, vlm_172485, vlm_172486, vlm_172487, vlm_172488, vlm_172489, vlm_172490, vlm_172491, vlm_172492

**equilibrium_maps:** 4 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_28008 | 3 | 3 | 16.5~31.5 °C | 2.775~3.225 M |
| ref_eq_net_28009 | 2 | 1 | 16.5~31.5 °C | 1.775~2.225 M |
| ref_eq_net_28010 | 2 | 1 | 16.5~31.5 °C | 3.775~4.225 M |
| ref_eq_net_28011 | 1 | 0 | 16.5~31.5 °C | 0.775~1.225 M |

---

### Step 10: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_71",
  "ligand_id": "ligand_10092"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 6 species

### Hg^[2+] + Hydrogen thiocyanate (Thiocyanic acid)
**metal_id:** metal_71 | **ligand_id:** ligand_10092 | **ligand_def_HxL:** HL  
**entries:** 20 | **species:** 6 | **vlm_count:** 20

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_334 | [M][L]<sup>2</sup>/[ML<sub>2</sub>(s)] | [ML2(s)] <=> [M] + [L]^2 | [M](aqueous), [L](aqueous), [ML2(s)](solid) | 1 |
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 6 |
| beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | [M] + [L]^2 <=> [ML2] | [ML2](aqueous), [M](aqueous), [L](aqueous) | 4 |
| beta_def_872 | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | [M] + [L]^3 <=> [ML3] | [ML3](aqueous), [M](aqueous), [L](aqueous) | 3 |
| beta_def_894 | [ML<sub>4</sub>]/[M][L]<sup>4</sup> | [M] + [L]^4 <=> [ML4] | [ML4](aqueous), [M](aqueous), [L](aqueous) | 3 |
| beta_def_966 | [ML]/[M(OH)L][H] | [M(OH)L] + [H] <=> [ML] + [H2O] | [ML](aqueous), [H2O](aqueous), [M(OH)L](aqueous), [H](aqueous) | 3 |

**vlm_ids:** vlm_172456, vlm_172457, vlm_172458, vlm_172459, vlm_172460, … vlm_172473, vlm_172474, vlm_172475 (20 listed)

**equilibrium_maps:** 2 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_28003 | 2 | 1 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_28004 | 6 | 11 | 19~29 °C | 0.85~1.15 M |

---

### Step 12: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_10092 AND c.metal_id IN (metal_26, metal_71, metal_125) AND c.beta_definition_id = beta_def_812 AND (s.temperature_c BETWEEN 20 AND 30) AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2) AND (s.solvent_name LIKE '%Water%'))",
  "order_by": "c.metal_id ASC, s.ionic_strength_mol_l ASC, s.temperature_c ASC",
  "limit": 60
}
```

[summary]
## search_stability

*(no results)*

---
