# Q5.2.4 — Tool Results (batch 3)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Pu(IV)",
  "limit": 10
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
  "name": "aspirin, acetylsalicylic acid, acetylsalicylate",
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
  "name": "salicylate, salicylic acid",
  "limit": 20
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 5: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_149"
}
```

[summary]
[CATALOG]
## build_system_catalog — 11 pair(s), 19 species *(compact)*

### Pu^[4+] + Nitrate ion
**metal_id:** metal_149 | **ligand_id:** ligand_10109 | **ligand_def_HxL:** ***  
**entries:** 9 | **species:** 3 | **vlm_count:** 9

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 6 |
| beta_def_840 | [M] + [L]^2 <=> [ML2] | 2 |
| beta_def_872 | [M] + [L]^3 <=> [ML3] | 1 |

**vlm_ids:** 9 (vlm_173938…vlm_173946)

**eq_maps:** 4 ref nets (ref_eq_net_28485, ref_eq_net_28486, ref_eq_net_28487…ref_eq_net_28488) | T: 15~30 °C | I: -0.05~4.15 M | max 3 nodes, 3 edges

---

### Pu^[4+] + Hydroxide ion
**metal_id:** metal_149 | **ligand_id:** ligand_10076 | **ligand_def_HxL:** ***  
**entries:** 5 | **species:** 1 | **vlm_count:** 5

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 5 |

**vlm_ids:** 5 (vlm_170588…vlm_170592)

**eq_maps:** 3 ref nets (ref_eq_net_27406, ref_eq_net_27407, ref_eq_net_27408) | T: 16.5~31.5 °C | I: 0.275~2.225 M | max 1 nodes, 0 edges

---

### Pu^[4+] + Hydrogen fluoride (Hydrofluoric acid)
**metal_id:** metal_149 | **ligand_id:** ligand_10162 | **ligand_def_HxL:** HL  
**entries:** 4 | **species:** 1 | **vlm_count:** 4

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 4 |

**vlm_ids:** 4 (vlm_176898…vlm_176901)

**eq_maps:** 2 ref nets (ref_eq_net_29637, ref_eq_net_29638) | T: 16.5~31.5 °C | I: 1.775~2.225 M | max 1 nodes, 0 edges

---

### Pu^[4+] + Hydrogen sulfate ion (Sulfuric acid)
**metal_id:** metal_149 | **ligand_id:** ligand_10148 | **ligand_def_HxL:** HL  
**entries:** 4 | **species:** 2 | **vlm_count:** 4

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 3 |
| beta_def_840 | [M] + [L]^2 <=> [ML2] | 1 |

**vlm_ids:** 4 (vlm_175959…vlm_175962)

**eq_maps:** 1 ref nets (ref_eq_net_29258) | T: 16.5~31.5 °C | I: 1.775~2.225 M | max 2 nodes, 1 edges

---

### Pu^[4+] + Pentane-2,4-dione (Acetylacetone)
**metal_id:** metal_149 | **ligand_id:** ligand_9526 | **ligand_def_HxL:** ***  
**entries:** 4 | **species:** 4 | **vlm_count:** 4

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 1 |
| beta_def_840 | [M] + [L]^2 <=> [ML2] | 1 |
| beta_def_872 | [M] + [L]^3 <=> [ML3] | 1 |
| beta_def_894 | [M] + [L]^4 <=> [ML4] | 1 |

**vlm_ids:** 4 (vlm_165352…vlm_165355)

**eq_maps:** 1 ref nets (ref_eq_net_25226) | T: 20~30 °C | I: -0.05~0.25 M | max 4 nodes, 6 edges

---

### Pu^[4+] + Chloride ion
**metal_id:** metal_149 | **ligand_id:** ligand_10163 | **ligand_def_HxL:** ***  
**entries:** 3 | **species:** 1 | **vlm_count:** 3

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 3 |

**vlm_ids:** vlm_177329, vlm_177330, vlm_177331

**eq_maps:** 3 ref nets (ref_eq_net_29818, ref_eq_net_29819, ref_eq_net_29820) | T: 12.5~31.5 °C | I: 0.775~4.225 M | max 1 nodes, 0 edges

---

### Pu^[4+] + Hydrogen peroxide
**metal_id:** metal_149 | **ligand_id:** ligand_10143 | **ligand_def_HxL:** H2L  
**entries:** 2 | **species:** 2 | **vlm_count:** 2

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_527 | [M]^2 + [H2L]^2 <=> [M2L2] + [H]^4 | 1 |
| beta_def_572 | [M]^2 + [H2L] + [H2O] <=> [M2(OH)L] + [H]^3 | 1 |

**vlm_ids:** vlm_175363, vlm_175364

**eq_maps:** 1 ref nets (ref_eq_net_29035) | T: 16.5~31.5 °C | I: 0.275~0.725 M | max 2 nodes, 1 edges

---

### Pu^[4+] + Ethanedioic acid (Oxalic acid)
**metal_id:** metal_149 | **ligand_id:** ligand_8872 | **ligand_def_HxL:** H2L  
**entries:** 2 | **species:** 2 | **vlm_count:** 2

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 1 |
| beta_def_840 | [M] + [L]^2 <=> [ML2] | 1 |

**vlm_ids:** vlm_151713, vlm_151714

**eq_maps:** 1 ref nets (ref_eq_net_20006) | T: 16.5~31.5 °C | I: 3.775~4.225 M | max 2 nodes, 1 edges

---

### Pu^[4+] + Bromide ion
**metal_id:** metal_149 | **ligand_id:** ligand_10168 | **ligand_def_HxL:** ***  
**entries:** 1 | **species:** 1 | **vlm_count:** 1

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 1 |

**vlm_ids:** vlm_177973

**eq_maps:** 1 ref nets (ref_eq_net_30048) | T: 16.5~31.5 °C | I: 1.775~2.225 M | max 1 nodes, 0 edges

---

### Pu^[4+] + Hydrogen amidosulfate (Sulfamic acid)
**metal_id:** metal_149 | **ligand_id:** ligand_10151 | **ligand_def_HxL:** HL  
**entries:** 1 | **species:** 1 | **vlm_count:** 1

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 1 |

**vlm_ids:** vlm_176333

**eq_maps:** 1 ref nets (ref_eq_net_29413) | T: 16.5~31.5 °C | I: 1.775~2.225 M | max 1 nodes, 0 edges

---

### Pu^[4+] + Diethylenetrinitrilopentaacetic acid (DTPA)
**metal_id:** metal_149 | **ligand_id:** ligand_6356 | **ligand_def_HxL:** H5L  
**entries:** 1 | **species:** 1 | **vlm_count:** 1

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 1 |

**vlm_ids:** vlm_112670

**eq_maps:** 1 ref nets (ref_eq_net_6721) | T: 12.5~27.5 °C | I: 0.275~0.725 M | max 1 nodes, 0 edges

---

### Step 7: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_149 AND (c.ligand_name_SRD LIKE '%aspirin%' OR c.ligand_name_SRD LIKE '%acetylsalicylic%' OR c.ligand_name_SRD LIKE '%acetylsalicylate%' OR c.ligand_name_SRD LIKE '%2-acetoxybenzoate%' OR c.ligand_name_SRD LIKE '%ASA%'))",
  "limit": 20
}
```

[summary]
## search_stability

*(no results)*

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_149 AND (c.ligand_name_SRD LIKE '%salicyl%' OR c.ligand_name_SRD LIKE '%hydroxybenzoate%' OR c.ligand_name_SRD LIKE '%2-hydroxybenzoate%'))",
  "limit": 20
}
```

[summary]
## search_stability — 20 row(s)

### logK — 8 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_201 | VO^[2+] | ligand_8636 | 2-Hydroxybenzoic acid 2-(di… | H4L | O=C(O)c1ccccc1OP(=O)(O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_8636 | 2-Hydroxybenzoic acid 2-(di… | H4L | O=C(O)c1ccccc1OP(=O)(O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_8637 | 2-Carboxy-6-(methoxycarbony… | H3L | COC(=O)c1cccc(C(=O)O)c1OP(=O)(O)O | 2 | 2 | 35 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_8701 | 2-Acetoxybenzoic acid (Acet… | HL | CC(=O)Oc1ccccc1C(=O)O | 2 | 2 | 37 | 0.15 | *** | 1 |
| metal_68 | H^[+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 2 | 1 | 25 | 0~0.1 | *** | 2 |
| metal_68 | H^[+] | ligand_8701 | 2-Acetoxybenzoic acid (Acet… | HL | CC(=O)Oc1ccccc1C(=O)O | 1 | 1 | 37 | 0.15 | *** | 1 |
| metal_92 | Mg^[2+] | ligand_8701 | 2-Acetoxybenzoic acid (Acet… | HL | CC(=O)Oc1ccccc1C(=O)O | 1 | 1 | 37 | 0.15 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_8701 | 2-Acetoxybenzoic acid (Acet… | HL | CC(=O)Oc1ccccc1C(=O)O | 1 | 1 | 37 | 0.15 | *** | 1 |

### ΔH — 2 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_8636 | 2-Hydroxybenzoic acid 2-(di… | H4L | O=C(O)c1ccccc1OP(=O)(O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 2 | 1 | 25 | 0~0.1 | *** | 0 |

### ΔS — 1 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_8636 | 2-Hydroxybenzoic acid 2-(di… | H4L | O=C(O)c1ccccc1OP(=O)(O)O | 2 | 2 | 25 | 0.1 | *** | 0 |

---

### Step 9: `search_citations`
**Args:**
```json
{
  "where": "((la.citation LIKE '%aspirin%' OR la.citation LIKE '%acetylsalicylic%' OR la.citation LIKE '%acetylsalicylate%') AND (la.citation LIKE '%plutonium%' OR la.citation LIKE '%Pu(IV)%' OR la.citation LIKE '%Pu%'))",
  "limit": 20
}
```

[summary]
## search_citations

*(no results)*

---
