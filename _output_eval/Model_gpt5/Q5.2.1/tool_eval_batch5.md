# Q5.2.1 — Tool Results (batch 5)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "uranium",
  "limit": 10
}
```

[summary]
## search_metals — 10 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_13 | Au^[+] | Au | 1 | ✓ | [Au+] | InChI=1S/Au/q+1 | beta_totN_5 | ligand_totN_3 | vlm_totN_13 |
| metal_14 | Au^[3+] | Au | 3 | ✓ | [Au+3] | InChI=1S/Au/q+3 | beta_totN_11 | ligand_totN_10 | vlm_totN_22 |
| metal_16 | Bu_[3]Pb^[+] | B | 1 |  | *** | *** | beta_totN_2 | ligand_totN_1 | vlm_totN_2 |
| metal_17 | Bu_[4]N^[+] | B | 1 |  | *** | *** | beta_totN_1 | ligand_totN_2 | vlm_totN_2 |
| metal_20 | BuHg^[+] | B | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_23 | BuNH_[3]^[+] | B | 1 |  | *** | *** | beta_totN_1 | ligand_totN_2 | vlm_totN_2 |
| metal_41 | Cu^[2+] | Cu | 2 | ✓ | [Cu+2] | InChI=1S/Cu/q+2 | beta_totN_264 | ligand_totN_1951 | vlm_totN_8963 |
| metal_42 | Cu^[+] | Cu | 1 | ✓ | [Cu+] | InChI=1S/Cu/q+1 | beta_totN_32 | ligand_totN_117 | vlm_totN_285 |
| metal_43 | Cu^[3+] | Cu | 3 | ✓ | [Cu+3] | InChI=1S/Cu/q+3 | beta_totN_4 | ligand_totN_8 | vlm_totN_10 |
| metal_58 | Eu^[3+] | Eu | 3 | ✓ | [Eu+3] | InChI=1S/Eu/q+3 | beta_totN_30 | ligand_totN_267 | vlm_totN_870 |

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "18-crown-6, 15-crown-5, 12-crown-4, dibenzo-18-crown-6, benzo-15-crown-5",
  "limit": 50
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 4: `search_metals`
**Args:**
```json
{
  "name": "uranyl",
  "symbol": "U",
  "limit": 50
}
```

[summary]
## search_metals

*(no results)*

---

### Step 5: `search_ligands`
**Args:**
```json
{
  "ligand_class": "crown ether",
  "limit": 200
}
```

[summary]
## search_ligands — 24 result(s)

**stats:** 24 SQL matches · showing 24 · limit 200

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_9672 | 1,4,7,10-Tetraoxacyclododecane (12-Crown-4) | *** | miscellaneous crown ether | 3 | *** | *** |
| ligand_9673 | 2,5,8,11,14-Pentaoxapentadecane (Tetraglyme) | *** | miscellaneous crown ether | 6 | *** | *** |
| ligand_9674 | 1,4,7,10,13-Pentaoxacyclopentadecane (15-Crown-5) | *** | miscellaneous crown ether | 45 | *** | *** |
| ligand_9675 | Benzo-1,4,7,10,13-pentaoxacycl… (Benzo-15-crown-5) | *** | miscellaneous crown ether | 3 | *** | *** |
| ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclooctadecane (18-Crown-6) | *** | miscellaneous crown ether | 76 | *** | *** |
| ligand_9677 | cis-syn-cis-2,5,8,15,… (A-Dicyclohexyl-18-Crown-6) | *** | miscellaneous crown ether | 42 | *** | *** |
| ligand_9678 | cis-anti-cis-2,5,8,15… (B-Dicyclohexyl-18-Crown-6) | *** | miscellaneous crown ether | 39 | *** | *** |
| ligand_9679 | Benzo-1,4,7,10,13,16-hexaoxacy… (Benzo-18-crown-6) | *** | miscellaneous crown ether | 2 | *** | *** |
| ligand_9680 | 2,3,11,12-Dibenzo-1,4,7,10,1… (Dibenzo-18-crown-6) | *** | miscellaneous crown ether | 13 | *** | *** |
| ligand_9681 | 3'-Hydroxymethy… (3-Hydroxymethylbenzo-18-crown-6) | *** | miscellaneous crown ether | 3 | *** | *** |
| ligand_9682 | (2R,3R,11R,12R)-2,3,11,12-Tetrakis(N-methylcarbam… | *** | miscellaneous crown ether | 1 | *** | *** |
| ligand_9683 | (2R,3R,11R,12R)-2,3,11,12-Tetrakis(N,N-dimethylca… | *** | miscellaneous crown ether | 1 | *** | *** |
| ligand_9684 | (2R,3R,11R,12R)-2,3,11,12-Tetrakis(N-methoxycarbo… | *** | miscellaneous crown ether | 1 | *** | *** |
| ligand_9685 | (2R,3R,11R,12R)-2,3,11,12-Tetrakis[N-(6-sulfo-2-n… | H4L | miscellaneous crown ether | 2 | `O=C(Nc1ccc2cc(S(=O)(=O)O)ccc2c1)C1OCCOCCOC(C(=O)Nc2ccc3cc(S(=O)(=O)O)ccc3c2)C(C(=O)Nc2ccc3cc(S(=O)(=O)O)ccc3c2)OCCOCCOC1C(=O)Nc1ccc2cc(S(=O)(=O)O)ccc2c1` | *** |
| ligand_9686 | (2R,3R,11R,12R)-2,3,11,12-Tetracarboxy-1,4,7,10,1… | H4L | miscellaneous crown ether | 5 | `O=C(O)C1OCCOCCOC(C(=O)O)C(C(=O)O)OCCOCCOC1C(=O)O` | *** |
| ligand_9687 | (2R,3R,11R,12R)-2,3,11,12-Tetrakis[N-(carboxymeth… | *** | miscellaneous crown ether | 2 | *** | *** |
| ligand_9688 | (2R,3R,11R,12R)-2,3,11,12-Tetrakis[N-({1S}-1-carb… | *** | miscellaneous crown ether | 1 | *** | *** |
| ligand_9689 | (2R,3R,11R,12R)-2,3,11,12-Tetrakis[N-(3-carboxy-2… | H4L | miscellaneous crown ether | 1 | `O=C(O)c1cc2ccccc2cc1NC(=O)C1OCCOCCOC(C(=O)Nc2cc3ccccc3cc2C(=O)O)C(C(=O)Nc2cc3ccccc3cc2C(=O)O)OCCOCCOC1C(=O)Nc1cc2ccccc2cc1C(=O)O` | *** |
| ligand_9690 | (2R,3R,11R,12R)-2,3,11,12-Tetrakis[N-({1S}-1,3-di… | *** | miscellaneous crown ether | 2 | *** | *** |
| ligand_9691 | (2R,3R,11R,12R)-2,3,11,12-Tetrakis[N-({1S}-1-carb… | *** | miscellaneous crown ether | 1 | *** | *** |
| ligand_9692 | (2R,3R,11R,12R)-2,3,11,12-Tetrakis[N-({1S}-1-carb… | *** | miscellaneous crown ether | 4 | *** | *** |
| ligand_9693 | (2R,3R,11R,12R)-2,3,11,12-Tetrakis[N-({1S}-2-carb… | *** | miscellaneous crown ether | 1 | *** | *** |
| ligand_9694 | (2R,3R,11R,12R)-2,3,11,12-Tetrakis[N-(2-aminoethy… | L | miscellaneous crown ether | 1 | `NCCNC(=O)C1OCCOCCOC(C(=O)NCCN)C(C(=O)NCCN)OCCOCCOC1C(=O)NCCN` | *** |
| ligand_9695 | (2R,3R,11R,12R)-2,3,11,12-Tetrakis[N-(2-{3-carbam… | *** | miscellaneous crown ether | 1 | *** | *** |

### Functional groups across all SQL matches (4 parseable SMILES)

| group | count | % |
|-------|-------|---|
| ether | 4 | 100% |
| amide | 3 | 75% |
| aromatic_ring | 2 | 50% |
| carboxyl | 2 | 50% |
| hydroxyl | 1 | 25% |
| primary_amine | 1 | 25% |
| sulfonate | 1 | 25% |

---

### Step 7: `build_system_catalog`
**Args:**
```json
{
  "ligand_id": "ligand_9672"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 1 species

### Pb^[2+] + 1,4,7,10-Tetraoxacyclododecane (12-Crown-4)
**metal_id:** metal_125 | **ligand_id:** ligand_9672 | **ligand_def_HxL:** ***  
**entries:** 3 | **species:** 1 | **vlm_count:** 3

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 3 |

**vlm_ids:** vlm_167394, vlm_167395, vlm_167396

**equilibrium_maps:** 1 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_26164 | 1 | 0 | 20~30 °C | -0.05~0.25 M |

---

### Step 8: `build_system_catalog`
**Args:**
```json
{
  "ligand_id": "ligand_9674"
}
```

[summary]
[CATALOG]
## build_system_catalog — 11 pair(s), 11 species *(compact)*

### Na^[+] + 1,4,7,10,13-Pentaoxacyclopentadecane (15-Crown-5)
**metal_id:** metal_106 | **ligand_id:** ligand_9674 | **ligand_def_HxL:** ***  
**entries:** 6 | **species:** 1 | **vlm_count:** 6

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 6 |

**vlm_ids:** 6 (vlm_167414…vlm_167419)

**eq_maps:** 2 ref nets (ref_eq_net_26166, ref_eq_net_26167) | T: 19~30 °C | I: -0.15~0.25 M | max 1 nodes, 0 edges

---

### K^[+] + 1,4,7,10,13-Pentaoxacyclopentadecane (15-Crown-5)
**metal_id:** metal_78 | **ligand_id:** ligand_9674 | **ligand_def_HxL:** ***  
**entries:** 6 | **species:** 1 | **vlm_count:** 6

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 6 |

**vlm_ids:** 6 (vlm_167420…vlm_167425)

**eq_maps:** 2 ref nets (ref_eq_net_26168, ref_eq_net_26169) | T: 19~30 °C | I: -0.15~0.25 M | max 1 nodes, 0 edges

---

### Cs^[+] + 1,4,7,10,13-Pentaoxacyclopentadecane (15-Crown-5)
**metal_id:** metal_40 | **ligand_id:** ligand_9674 | **ligand_def_HxL:** ***  
**entries:** 6 | **species:** 1 | **vlm_count:** 6

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 6 |

**vlm_ids:** 6 (vlm_167430…vlm_167435)

**eq_maps:** 2 ref nets (ref_eq_net_26172, ref_eq_net_26173) | T: 19~30 °C | I: -0.15~0.25 M | max 1 nodes, 0 edges

---

### Tl^[+] + 1,4,7,10,13-Pentaoxacyclopentadecane (15-Crown-5)
**metal_id:** metal_191 | **ligand_id:** ligand_9674 | **ligand_def_HxL:** ***  
**entries:** 4 | **species:** 1 | **vlm_count:** 4

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 4 |

**vlm_ids:** 4 (vlm_167449…vlm_167452)

**eq_maps:** 2 ref nets (ref_eq_net_26179, ref_eq_net_26180) | T: 19~30 °C | I: -0.15~0.25 M | max 1 nodes, 0 edges

---

### Rb^[+] + 1,4,7,10,13-Pentaoxacyclopentadecane (15-Crown-5)
**metal_id:** metal_154 | **ligand_id:** ligand_9674 | **ligand_def_HxL:** ***  
**entries:** 4 | **species:** 1 | **vlm_count:** 4

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 4 |

**vlm_ids:** 4 (vlm_167426…vlm_167429)

**eq_maps:** 2 ref nets (ref_eq_net_26170, ref_eq_net_26171) | T: 19~30 °C | I: -0.15~0.25 M | max 1 nodes, 0 edges

---

### Ag^[+] + 1,4,7,10,13-Pentaoxacyclopentadecane (15-Crown-5)
**metal_id:** metal_2 | **ligand_id:** ligand_9674 | **ligand_def_HxL:** ***  
**entries:** 4 | **species:** 1 | **vlm_count:** 4

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 4 |

**vlm_ids:** 4 (vlm_167445…vlm_167448)

**eq_maps:** 2 ref nets (ref_eq_net_26177, ref_eq_net_26178) | T: 19~30 °C | I: -0.15~0.25 M | max 1 nodes, 0 edges

---

### Sr^[2+] + 1,4,7,10,13-Pentaoxacyclopentadecane (15-Crown-5)
**metal_id:** metal_177 | **ligand_id:** ligand_9674 | **ligand_def_HxL:** ***  
**entries:** 3 | **species:** 1 | **vlm_count:** 3

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 3 |

**vlm_ids:** vlm_167439, vlm_167440, vlm_167441

**eq_maps:** 1 ref nets (ref_eq_net_26175) | T: 20~30 °C | I: -0.05~0.25 M | max 1 nodes, 0 edges

---

### Pb^[2+] + 1,4,7,10,13-Pentaoxacyclopentadecane (15-Crown-5)
**metal_id:** metal_125 | **ligand_id:** ligand_9674 | **ligand_def_HxL:** ***  
**entries:** 3 | **species:** 1 | **vlm_count:** 3

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 3 |

**vlm_ids:** vlm_167456, vlm_167457, vlm_167458

**eq_maps:** 1 ref nets (ref_eq_net_26182) | T: 20~30 °C | I: -0.05~0.25 M | max 1 nodes, 0 edges

---

### NH_[4]^[+] + 1,4,7,10,13-Pentaoxacyclopentadecane (15-Crown-5)
**metal_id:** metal_111 | **ligand_id:** ligand_9674 | **ligand_def_HxL:** ***  
**entries:** 3 | **species:** 1 | **vlm_count:** 3

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 3 |

**vlm_ids:** vlm_167436, vlm_167437, vlm_167438

**eq_maps:** 1 ref nets (ref_eq_net_26174) | T: 20~30 °C | I: -0.05~0.25 M | max 1 nodes, 0 edges

---

### Hg^[2+] + 1,4,7,10,13-Pentaoxacyclopentadecane (15-Crown-5)
**metal_id:** metal_71 | **ligand_id:** ligand_9674 | **ligand_def_HxL:** ***  
**entries:** 3 | **species:** 1 | **vlm_count:** 3

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 3 |

**vlm_ids:** vlm_167453, vlm_167454, vlm_167455

**eq_maps:** 1 ref nets (ref_eq_net_26181) | T: 20~30 °C | I: -0.05~0.25 M | max 1 nodes, 0 edges

---

### Ba^[2+] + 1,4,7,10,13-Pentaoxacyclopentadecane (15-Crown-5)
**metal_id:** metal_18 | **ligand_id:** ligand_9674 | **ligand_def_HxL:** ***  
**entries:** 3 | **species:** 1 | **vlm_count:** 3

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 3 |

**vlm_ids:** vlm_167442, vlm_167443, vlm_167444

**eq_maps:** 1 ref nets (ref_eq_net_26176) | T: 20~30 °C | I: -0.05~0.25 M | max 1 nodes, 0 edges

---

### Step 9: `build_system_catalog`
**Args:**
```json
{
  "ligand_id": "ligand_9675"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 1 species

### K^[+] + Benzo-1,4,7,10,13-pentaoxacyclopentadecane (Benzo-15-crown-5)
**metal_id:** metal_78 | **ligand_id:** ligand_9675 | **ligand_def_HxL:** ***  
**entries:** 3 | **species:** 1 | **vlm_count:** 3

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 3 |

**vlm_ids:** vlm_167467, vlm_167468, vlm_167469

**equilibrium_maps:** 1 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_26183 | 1 | 0 | 20~30 °C | -0.05~0.25 M |

---

### Step 10: `build_system_catalog`
**Args:**
```json
{
  "ligand_id": "ligand_9676"
}
```

[summary]
[CATALOG]
## build_system_catalog — 19 pair(s), 19 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_812 | [M] + [L] <=> [ML] |  |

*(all species aqueous)*

**1. Sr^[2+] + 1,4,7,10,13,16-Hexaoxacyclooctadecane (18-Crown-6)** (metal_177 + ligand_9676) — ligand_def_HxL: *** | 8 ent, 1 sp, 8 vlms (vlm_167522…vlm_167529)
   - species: beta_def_812(8)
   - eq:2 nets T:19~30°C I:-0.15~0.25M max 1n/0e
**2. Ba^[2+] + 1,4,7,10,13,16-Hexaoxacyclooctadecane (18-Crown-6)** (metal_18 + ligand_9676) — ligand_def_HxL: *** | 8 ent, 1 sp, 8 vlms (vlm_167530…vlm_167537)
   - species: beta_def_812(8)
   - eq:2 nets T:19~30°C I:-0.15~0.25M max 1n/0e
**3. Rb^[+] + 1,4,7,10,13,16-Hexaoxacyclooctadecane (18-Crown-6)** (metal_154 + ligand_9676) — ligand_def_HxL: *** | 6 ent, 1 sp, 6 vlms (vlm_167490…vlm_167495)
   - species: beta_def_812(6)
   - eq:2 nets T:19~30°C I:-0.15~0.25M max 1n/0e
**4. NH_[4]^[+] + 1,4,7,10,13,16-Hexaoxacyclooctadecane (18-Crown-6)** (metal_111 + ligand_9676) — ligand_def_HxL: *** | 6 ent, 1 sp, 6 vlms (vlm_167502…vlm_167507)
   - species: beta_def_812(6)
   - eq:2 nets T:19~30°C I:-0.15~0.25M max 1n/0e
**5. Na^[+] + 1,4,7,10,13,16-Hexaoxacyclooctadecane (18-Crown-6)** (metal_106 + ligand_9676) — ligand_def_HxL: *** | 6 ent, 1 sp, 6 vlms (vlm_167478…vlm_167483)
   - species: beta_def_812(6)
   - eq:2 nets T:19~30°C I:-0.15~0.25M max 1n/0e
**6. K^[+] + 1,4,7,10,13,16-Hexaoxacyclooctadecane (18-Crown-6)** (metal_78 + ligand_9676) — ligand_def_HxL: *** | 6 ent, 1 sp, 6 vlms (vlm_167484…vlm_167489)
   - species: beta_def_812(6)
   - eq:2 nets T:19~30°C I:-0.15~0.25M max 1n/0e
**7. Cs^[+] + 1,4,7,10,13,16-Hexaoxacyclooctadecane (18-Crown-6)** (metal_40 + ligand_9676) — ligand_def_HxL: *** | 6 ent, 1 sp, 6 vlms (vlm_167496…vlm_167501)
   - species: beta_def_812(6)
   - eq:2 nets T:19~30°C I:-0.15~0.25M max 1n/0e
**8. Ca^[2+] + 1,4,7,10,13,16-Hexaoxacyclooctadecane (18-Crown-6)** (metal_25 + ligand_9676) — ligand_def_HxL: *** | 6 ent, 1 sp, 6 vlms (vlm_167516…vlm_167521)
   - species: beta_def_812(6)
   - eq:2 nets T:19~30°C I:-0.15~0.25M max 1n/0e
**9. Ag^[+] + 1,4,7,10,13,16-Hexaoxacyclooctadecane (18-Crown-6)** (metal_2 + ligand_9676) — ligand_def_HxL: *** | 6 ent, 1 sp, 6 vlms (vlm_167539…vlm_167544)
   - species: beta_def_812(6)
   - eq:2 nets T:19~30°C I:-0.15~0.25M max 1n/0e
**10. Tl^[+] + 1,4,7,10,13,16-Hexaoxacyclooctadecane (18-Crown-6)** (metal_191 + ligand_9676) — ligand_def_HxL: *** | 3 ent, 1 sp, 3 vlms (vlm_167545, vlm_167546, vlm_167547)
   - species: beta_def_812(3)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**11. Pb^[2+] + 1,4,7,10,13,16-Hexaoxacyclooctadecane (18-Crown-6)** (metal_125 + ligand_9676) — ligand_def_HxL: *** | 3 ent, 1 sp, 3 vlms (vlm_167551, vlm_167552, vlm_167553)
   - species: beta_def_812(3)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**12. Mg^[2+] + 1,4,7,10,13,16-Hexaoxacyclooctadecane (18-Crown-6)** (metal_92 + ligand_9676) — ligand_def_HxL: *** | 3 ent, 1 sp, 3 vlms (vlm_167513, vlm_167514, vlm_167515)
   - species: beta_def_812(3)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**13. Hg^[2+] + 1,4,7,10,13,16-Hexaoxacyclooctadecane (18-Crown-6)** (metal_71 + ligand_9676) — ligand_def_HxL: *** | 3 ent, 1 sp, 3 vlms (vlm_167548, vlm_167549, vlm_167550)
   - species: beta_def_812(3)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**14. Ra^[2+] + 1,4,7,10,13,16-Hexaoxacyclooctadecane (18-Crown-6)** (metal_153 + ligand_9676) — ligand_def_HxL: *** | 1 ent, 1 sp, 1 vlms (vlm_167538)
   - species: beta_def_812(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**15. MeNH_[3]^[+] + 1,4,7,10,13,16-Hexaoxacyclooctadecane (18-Crown-6)** (metal_97 + ligand_9676) — ligand_def_HxL: *** | 1 ent, 1 sp, 1 vlms (vlm_167508)
   - species: beta_def_812(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**16. EtNH_[3]^[+] + 1,4,7,10,13,16-Hexaoxacyclooctadecane (18-Crown-6)** (metal_54 + ligand_9676) — ligand_def_HxL: *** | 1 ent, 1 sp, 1 vlms (vlm_167509)
   - species: beta_def_812(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**17. Et_[3]NH^[+] + 1,4,7,10,13,16-Hexaoxacyclooctadecane (18-Crown-6)** (metal_48 + ligand_9676) — ligand_def_HxL: *** | 1 ent, 1 sp, 1 vlms (vlm_167512)
   - species: beta_def_812(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**18. Et_[2]NH_[2]^[+] + 1,4,7,10,13,16-Hexaoxacyclooctadecane (18-Crown-6)** (metal_45 + ligand_9676) — ligand_def_HxL: *** | 1 ent, 1 sp, 1 vlms (vlm_167511)
   - species: beta_def_812(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**19. BuNH_[3]^[+] + 1,4,7,10,13,16-Hexaoxacyclooctadecane (18-Crown-6)** (metal_23 + ligand_9676) — ligand_def_HxL: *** | 1 ent, 1 sp, 1 vlms (vlm_167510)
   - species: beta_def_812(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e

---

### Step 11: `build_system_catalog`
**Args:**
```json
{
  "ligand_id": "ligand_9679"
}
```

[summary]
[CATALOG]
## build_system_catalog — 2 pair(s), 2 species

### Na^[+] + Benzo-1,4,7,10,13,16-hexaoxacyclooctadecane (Benzo-18-crown-6)
**metal_id:** metal_106 | **ligand_id:** ligand_9679 | **ligand_def_HxL:** ***  
**entries:** 1 | **species:** 1 | **vlm_count:** 1

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 1 |

**vlm_ids:** vlm_167647

**equilibrium_maps:** 1 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_26237 | 1 | 0 | 20~30 °C | -0.05~0.25 M |

---

### Ba^[2+] + Benzo-1,4,7,10,13,16-hexaoxacyclooctadecane (Benzo-18-crown-6)
**metal_id:** metal_18 | **ligand_id:** ligand_9679 | **ligand_def_HxL:** ***  
**entries:** 1 | **species:** 1 | **vlm_count:** 1

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 1 |

**vlm_ids:** vlm_167648

**equilibrium_maps:** 1 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_26238 | 1 | 0 | 20~30 °C | -0.05~0.25 M |

---

### Step 12: `build_system_catalog`
**Args:**
```json
{
  "ligand_id": "ligand_9680"
}
```

[summary]
[CATALOG]
## build_system_catalog — 13 pair(s), 13 species *(compact)*

### Tl^[+] + 2,3,11,12-Dibenzo-1,4,7,10,13,16-hexaoxacyclooctadecane (Dibenzo-18-crown-6)
**metal_id:** metal_191 | **ligand_id:** ligand_9680 | **ligand_def_HxL:** ***  
**entries:** 1 | **species:** 1 | **vlm_count:** 1

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 1 |

**vlm_ids:** vlm_167666

**eq_maps:** 1 ref nets (ref_eq_net_26250) | T: 20~30 °C | I: -0.05~0.25 M | max 1 nodes, 0 edges

---

### Sr^[2+] + 2,3,11,12-Dibenzo-1,4,7,10,13,16-hexaoxacyclooctadecane (Dibenzo-18-crown-6)
**metal_id:** metal_177 | **ligand_id:** ligand_9680 | **ligand_def_HxL:** ***  
**entries:** 1 | **species:** 1 | **vlm_count:** 1

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 1 |

**vlm_ids:** vlm_167660

**eq_maps:** 1 ref nets (ref_eq_net_26244) | T: 20~30 °C | I: -0.05~0.25 M | max 1 nodes, 0 edges

---

### Rb^[+] + 2,3,11,12-Dibenzo-1,4,7,10,13,16-hexaoxacyclooctadecane (Dibenzo-18-crown-6)
**metal_id:** metal_154 | **ligand_id:** ligand_9680 | **ligand_def_HxL:** ***  
**entries:** 1 | **species:** 1 | **vlm_count:** 1

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 1 |

**vlm_ids:** vlm_167657

**eq_maps:** 1 ref nets (ref_eq_net_26241) | T: 20~30 °C | I: -0.05~0.25 M | max 1 nodes, 0 edges

---

### Pb^[2+] + 2,3,11,12-Dibenzo-1,4,7,10,13,16-hexaoxacyclooctadecane (Dibenzo-18-crown-6)
**metal_id:** metal_125 | **ligand_id:** ligand_9680 | **ligand_def_HxL:** ***  
**entries:** 1 | **species:** 1 | **vlm_count:** 1

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 1 |

**vlm_ids:** vlm_167667

**eq_maps:** 1 ref nets (ref_eq_net_26251) | T: 20~30 °C | I: -0.05~0.25 M | max 1 nodes, 0 edges

---

### Ni^[2+] + 2,3,11,12-Dibenzo-1,4,7,10,13,16-hexaoxacyclooctadecane (Dibenzo-18-crown-6)
**metal_id:** metal_112 | **ligand_id:** ligand_9680 | **ligand_def_HxL:** ***  
**entries:** 1 | **species:** 1 | **vlm_count:** 1

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 1 |

**vlm_ids:** vlm_167663

**eq_maps:** 1 ref nets (ref_eq_net_26247) | T: 20~30 °C | I: -0.05~0.25 M | max 1 nodes, 0 edges

---

### NH_[4]^[+] + 2,3,11,12-Dibenzo-1,4,7,10,13,16-hexaoxacyclooctadecane (Dibenzo-18-crown-6)
**metal_id:** metal_111 | **ligand_id:** ligand_9680 | **ligand_def_HxL:** ***  
**entries:** 1 | **species:** 1 | **vlm_count:** 1

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 1 |

**vlm_ids:** vlm_167659

**eq_maps:** 1 ref nets (ref_eq_net_26243) | T: 20~30 °C | I: -0.05~0.25 M | max 1 nodes, 0 edges

---

### Na^[+] + 2,3,11,12-Dibenzo-1,4,7,10,13,16-hexaoxacyclooctadecane (Dibenzo-18-crown-6)
**metal_id:** metal_106 | **ligand_id:** ligand_9680 | **ligand_def_HxL:** ***  
**entries:** 1 | **species:** 1 | **vlm_count:** 1

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 1 |

**vlm_ids:** vlm_167655

**eq_maps:** 1 ref nets (ref_eq_net_26239) | T: 20~30 °C | I: -0.05~0.25 M | max 1 nodes, 0 edges

---

### K^[+] + 2,3,11,12-Dibenzo-1,4,7,10,13,16-hexaoxacyclooctadecane (Dibenzo-18-crown-6)
**metal_id:** metal_78 | **ligand_id:** ligand_9680 | **ligand_def_HxL:** ***  
**entries:** 1 | **species:** 1 | **vlm_count:** 1

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 1 |

**vlm_ids:** vlm_167656

**eq_maps:** 1 ref nets (ref_eq_net_26240) | T: 20~30 °C | I: -0.05~0.25 M | max 1 nodes, 0 edges

---

### Cu^[2+] + 2,3,11,12-Dibenzo-1,4,7,10,13,16-hexaoxacyclooctadecane (Dibenzo-18-crown-6)
**metal_id:** metal_41 | **ligand_id:** ligand_9680 | **ligand_def_HxL:** ***  
**entries:** 1 | **species:** 1 | **vlm_count:** 1

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 1 |

**vlm_ids:** vlm_167664

**eq_maps:** 1 ref nets (ref_eq_net_26248) | T: 20~30 °C | I: -0.05~0.25 M | max 1 nodes, 0 edges

---

### Cs^[+] + 2,3,11,12-Dibenzo-1,4,7,10,13,16-hexaoxacyclooctadecane (Dibenzo-18-crown-6)
**metal_id:** metal_40 | **ligand_id:** ligand_9680 | **ligand_def_HxL:** ***  
**entries:** 1 | **species:** 1 | **vlm_count:** 1

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 1 |

**vlm_ids:** vlm_167658

**eq_maps:** 1 ref nets (ref_eq_net_26242) | T: 20~30 °C | I: -0.05~0.25 M | max 1 nodes, 0 edges

---

### Co^[2+] + 2,3,11,12-Dibenzo-1,4,7,10,13,16-hexaoxacyclooctadecane (Dibenzo-18-crown-6)
**metal_id:** metal_33 | **ligand_id:** ligand_9680 | **ligand_def_HxL:** ***  
**entries:** 1 | **species:** 1 | **vlm_count:** 1

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 1 |

**vlm_ids:** vlm_167662

**eq_maps:** 1 ref nets (ref_eq_net_26246) | T: 20~30 °C | I: -0.05~0.25 M | max 1 nodes, 0 edges

---

### Ba^[2+] + 2,3,11,12-Dibenzo-1,4,7,10,13,16-hexaoxacyclooctadecane (Dibenzo-18-crown-6)
**metal_id:** metal_18 | **ligand_id:** ligand_9680 | **ligand_def_HxL:** ***  
**entries:** 1 | **species:** 1 | **vlm_count:** 1

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 1 |

**vlm_ids:** vlm_167661

**eq_maps:** 1 ref nets (ref_eq_net_26245) | T: 20~30 °C | I: -0.05~0.25 M | max 1 nodes, 0 edges

---

### Ag^[+] + 2,3,11,12-Dibenzo-1,4,7,10,13,16-hexaoxacyclooctadecane (Dibenzo-18-crown-6)
**metal_id:** metal_2 | **ligand_id:** ligand_9680 | **ligand_def_HxL:** ***  
**entries:** 1 | **species:** 1 | **vlm_count:** 1

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 1 |

**vlm_ids:** vlm_167665

**eq_maps:** 1 ref nets (ref_eq_net_26249) | T: 20~30 °C | I: -0.05~0.25 M | max 1 nodes, 0 edges

---

### Step 14: `search_stability`
**Args:**
```json
{
  "where": "((c.ligand_class_name LIKE '%crown ether%' OR c.ligand_name_SRD LIKE '%crown%') AND (c.metal_name_SRD LIKE '%UO2%' OR c.metal_name_SRD LIKE '%uranyl%' OR c.metal_name_SRD LIKE '%uranium(VI)%' OR c.metal_name_SRD LIKE '%U(VI)%'))",
  "order_by": "s.constant_value DESC",
  "limit": 500
}
```

[summary]
## search_stability

*(no results)*

---
