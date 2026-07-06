# Q5.2.1 — Tool Results (batch 5)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "U(VI), uranyl",
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
  "name": "12-crown-4, 15-crown-5, 18-crown-6, benzo-15-crown-5, dibenzo-18-crown-6, dicyclohexano-18-crown-6, 21-crown-7",
  "limit": 50
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 5: `build_system_catalog`
**Args:**
```json
{}
```

[summary]
[CATALOG]
## build_system_catalog

**Error:** Provide at least one of metal_id, ligand_id, or beta_definition_id.

---

### Step 7: `search_metals`
**Args:**
```json
{
  "symbol": "U",
  "limit": 20
}
```

[summary]
## search_metals — 20 result(s)

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
| metal_59 | Eu^[2+] | Eu | 2 | ✓ | [Eu+2] | InChI=1S/Eu/q+2 | beta_totN_1 | ligand_totN_2 | vlm_totN_2 |
| metal_60 | Eu^[4+] | Eu | 4 | ✓ | [Eu+4] | InChI=1S/Eu/q+4 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_81 | Lu^[3+] | Lu | 3 | ✓ | [Lu+3] | InChI=1S/Lu/q+3 | beta_totN_25 | ligand_totN_234 | vlm_totN_671 |
| metal_82 | Me_[2]Au^[+] | M2Au | 1 |  | *** | *** | beta_totN_1 | ligand_totN_1 | vlm_totN_1 |
| metal_148 | Pu^[3+] | Pu | 3 | ✓ | [Pu+3] | InChI=1S/Pu/q+3 | beta_totN_7 | ligand_totN_12 | vlm_totN_28 |
| metal_149 | Pu^[4+] | Pu | 4 | ✓ | [Pu+4] | InChI=1S/Pu/q+4 | beta_totN_6 | ligand_totN_11 | vlm_totN_36 |
| metal_150 | PuO_[2]^[2+] | Pu | 2 |  | *** | *** | beta_totN_10 | ligand_totN_22 | vlm_totN_76 |
| metal_151 | PuO_[2]^[+] | Pu | 1 |  | *** | *** | beta_totN_2 | ligand_totN_6 | vlm_totN_6 |
| metal_163 | Ru^[2+] | Ru | 2 | ✓ | [Ru+2] | InChI=1S/Ru/q+2 | beta_totN_1 | ligand_totN_1 | vlm_totN_6 |
| metal_164 | Ru^[3+] | Ru | 3 | ✓ | [Ru+3] | InChI=1S/Ru/q+3 | beta_totN_2 | ligand_totN_1 | vlm_totN_2 |

---

### Step 8: `search_ligands`
**Args:**
```json
{
  "ligand_class": "crown",
  "limit": 100
}
```

[summary]
## search_ligands — 24 result(s)

**stats:** 24 SQL matches · showing 24 · limit 100

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

### Step 9: `build_system_catalog`
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

### Step 11: `get_table_schema`
**Args:**
```json
{
  "table_name": "metal_card",
  "database": "cards"
}
```

[summary]
## get_table_schema - 16 column(s)

| cid | name | type | notnull | pk |
|-----|------|------|---------|----|
| 0 | metal_id | INTEGER | False | True |
| 1 | metal_name_SRD | TEXT | True | False |
| 2 | symbol_pure | TEXT | False | False |
| 3 | charge | INTEGER | False | False |
| 4 | charge_str | TEXT | False | False |
| 5 | SMILES | TEXT | False | False |
| 6 | InChi | TEXT | False | False |
| 7 | InChiKey | TEXT | False | False |
| 8 | parts_used_json | TEXT | False | False |
| 9 | stoichiometry_json | TEXT | False | False |
| 10 | is_simple_ion | INTEGER | False | False |
| 11 | is_organometallic | INTEGER | False | False |
| 12 | primary_metal | TEXT | False | False |
| 13 | formula_components_json | TEXT | False | False |
| 14 | parse_notes | TEXT | False | False |
| 15 | created_at | TIMESTAMP | False | False |

---

### Step 12: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id IN (ligand_9672, ligand_9674, ligand_9675, ligand_9676, ligand_9677, ligand_9678, ligand_9679, ligand_9680))",
  "order_by": "c.metal_name_SRD ASC",
  "limit": 200
}
```

[summary]
## search_stability — 200 row(s)

### logK — 64 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_2 | Ag^[+] | ligand_9674 | 1,4,7,10,13-Pentaoxacyclope… | *** | *** | 2 | 1 | 25 | 0~0.1 | *** | 2 |
| metal_2 | Ag^[+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 2 | 1 | 25 | 0~0.1 | *** | 2 |
| metal_18 | Ba^[2+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 2 | 1 | 25 | 0~0.1 | *** | 2 |
| metal_25 | Ca^[2+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 2 | 1 | 25 | 0~0.1 | *** | 2 |
| metal_40 | Cs^[+] | ligand_9674 | 1,4,7,10,13-Pentaoxacyclope… | *** | *** | 2 | 1 | 25 | 0~0.1 | *** | 2 |
| metal_40 | Cs^[+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 2 | 1 | 25 | 0~0.1 | *** | 2 |
| metal_72 | Hg^[+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_72 | Hg^[+] | ligand_9678 | cis-anti-cis-2,5,8,15,18,21… | *** | *** | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_78 | K^[+] | ligand_9674 | 1,4,7,10,13-Pentaoxacyclope… | *** | *** | 2 | 1 | 25 | 0~0.1 | *** | 2 |
| metal_78 | K^[+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 2 | 1 | 25 | 0~0.1 | *** | 2 |
| metal_111 | NH_[4]^[+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 2 | 1 | 25 | 0~0.1 | *** | 2 |
| metal_106 | Na^[+] | ligand_9674 | 1,4,7,10,13-Pentaoxacyclope… | *** | *** | 2 | 1 | 25 | 0~0.1 | *** | 2 |
| metal_106 | Na^[+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 2 | 1 | 25 | 0~0.1 | *** | 2 |
| metal_154 | Rb^[+] | ligand_9674 | 1,4,7,10,13-Pentaoxacyclope… | *** | *** | 2 | 1 | 25 | 0~0.1 | *** | 2 |
| metal_154 | Rb^[+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 2 | 1 | 25 | 0~0.1 | *** | 2 |
| metal_177 | Sr^[2+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 2 | 1 | 25 | 0~0.1 | *** | 2 |
| metal_2 | Ag^[+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_2 | Ag^[+] | ligand_9678 | cis-anti-cis-2,5,8,15,18,21… | *** | *** | 1 | 1 | 25 | 0 | *** | 1 |
| metal_2 | Ag^[+] | ligand_9680 | 2,3,11,12-Dibenzo-1,4,7,10,… | *** | *** | 1 | 1 | 25 | 0 | *** | 1 |
| metal_18 | Ba^[2+] | ligand_9674 | 1,4,7,10,13-Pentaoxacyclope… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_18 | Ba^[2+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 1 | 1 | 25 | 0 | *** | 1 |
| metal_18 | Ba^[2+] | ligand_9678 | cis-anti-cis-2,5,8,15,18,21… | *** | *** | 1 | 1 | 25 | 0 | *** | 1 |
| metal_18 | Ba^[2+] | ligand_9679 | Benzo-1,4,7,10,13,16-hexaox… | *** | *** | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_18 | Ba^[2+] | ligand_9680 | 2,3,11,12-Dibenzo-1,4,7,10,… | *** | *** | 1 | 1 | 25 | 0 | *** | 1 |
| metal_23 | BuNH_[3]^[+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 1 | 1 | 25 | 0 | *** | 1 |
| metal_33 | Co^[2+] | ligand_9680 | 2,3,11,12-Dibenzo-1,4,7,10,… | *** | *** | 1 | 1 | 25 | 0 | *** | 1 |
| metal_40 | Cs^[+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 1 | 1 | 25 | 0 | *** | 1 |
| metal_40 | Cs^[+] | ligand_9680 | 2,3,11,12-Dibenzo-1,4,7,10,… | *** | *** | 1 | 1 | 25 | 0 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_9680 | 2,3,11,12-Dibenzo-1,4,7,10,… | *** | *** | 1 | 1 | 25 | 0 | *** | 1 |
| metal_54 | EtNH_[3]^[+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 1 | 1 | 25 | 0 | *** | 1 |
| metal_45 | Et_[2]NH_[2]^[+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 1 | 1 | 25 | 0 | *** | 1 |
| metal_48 | Et_[3]NH^[+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 1 | 1 | 25 | 0 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_9674 | 1,4,7,10,13-Pentaoxacyclope… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_9678 | cis-anti-cis-2,5,8,15,18,21… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_78 | K^[+] | ligand_9675 | Benzo-1,4,7,10,13-pentaoxac… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_78 | K^[+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 1 | 1 | 25 | 0 | *** | 1 |
| metal_78 | K^[+] | ligand_9678 | cis-anti-cis-2,5,8,15,18,21… | *** | *** | 1 | 1 | 25 | 0 | *** | 1 |
| metal_78 | K^[+] | ligand_9680 | 2,3,11,12-Dibenzo-1,4,7,10,… | *** | *** | 1 | 1 | 25 | 0 | *** | 1 |
| metal_97 | MeNH_[3]^[+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 1 | 1 | 25 | 0 | *** | 1 |
| metal_97 | MeNH_[3]^[+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_97 | MeNH_[3]^[+] | ligand_9678 | cis-anti-cis-2,5,8,15,18,21… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_92 | Mg^[2+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 1 | 1 | 25 | 0 | *** | 1 |
| metal_111 | NH_[4]^[+] | ligand_9674 | 1,4,7,10,13-Pentaoxacyclope… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_111 | NH_[4]^[+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 1 | 1 | 25 | 0 | *** | 1 |
| metal_111 | NH_[4]^[+] | ligand_9678 | cis-anti-cis-2,5,8,15,18,21… | *** | *** | 1 | 1 | 25 | 0 | *** | 1 |
| metal_111 | NH_[4]^[+] | ligand_9680 | 2,3,11,12-Dibenzo-1,4,7,10,… | *** | *** | 1 | 1 | 25 | 0 | *** | 1 |
| metal_106 | Na^[+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_106 | Na^[+] | ligand_9678 | cis-anti-cis-2,5,8,15,18,21… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_106 | Na^[+] | ligand_9679 | Benzo-1,4,7,10,13,16-hexaox… | *** | *** | 1 | 1 | 25 | 0 | *** | 1 |
| metal_106 | Na^[+] | ligand_9680 | 2,3,11,12-Dibenzo-1,4,7,10,… | *** | *** | 1 | 1 | 25 | 0 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_9680 | 2,3,11,12-Dibenzo-1,4,7,10,… | *** | *** | 1 | 1 | 25 | 0 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_9672 | 1,4,7,10-Tetraoxacyclododec… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_9674 | 1,4,7,10,13-Pentaoxacyclope… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_9678 | cis-anti-cis-2,5,8,15,18,21… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_9680 | 2,3,11,12-Dibenzo-1,4,7,10,… | *** | *** | 1 | 1 | 25 | 0 | *** | 1 |
| metal_153 | Ra^[2+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_154 | Rb^[+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 1 | 1 | 25 | 0 | *** | 1 |
| metal_154 | Rb^[+] | ligand_9678 | cis-anti-cis-2,5,8,15,18,21… | *** | *** | 1 | 1 | 25 | 0 | *** | 1 |
| metal_154 | Rb^[+] | ligand_9680 | 2,3,11,12-Dibenzo-1,4,7,10,… | *** | *** | 1 | 1 | 25 | 0 | *** | 1 |
| metal_177 | Sr^[2+] | ligand_9674 | 1,4,7,10,13-Pentaoxacyclope… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 1 |

### ΔH — 45 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_18 | Ba^[2+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 4 | 1 | 15~37 | 0~0.1 | *** | 0 |
| metal_177 | Sr^[2+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 4 | 1 | 25~45 | 0~0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 3 | 1 | 15~35 | 0 | *** | 0 |
| metal_2 | Ag^[+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 2 | 1 | 25 | 0~0.1 | *** | 0 |
| metal_40 | Cs^[+] | ligand_9674 | 1,4,7,10,13-Pentaoxacyclope… | *** | *** | 2 | 1 | 25 | 0~0.1 | *** | 0 |
| metal_40 | Cs^[+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 2 | 1 | 25 | 0~0.1 | *** | 0 |
| metal_72 | Hg^[+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_72 | Hg^[+] | ligand_9678 | cis-anti-cis-2,5,8,15,18,21… | *** | *** | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_78 | K^[+] | ligand_9674 | 1,4,7,10,13-Pentaoxacyclope… | *** | *** | 2 | 1 | 25 | 0~0.1 | *** | 0 |
| metal_78 | K^[+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 2 | 1 | 25 | 0~0.1 | *** | 0 |
| metal_111 | NH_[4]^[+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 2 | 1 | 25 | 0~0.1 | *** | 0 |
| metal_106 | Na^[+] | ligand_9674 | 1,4,7,10,13-Pentaoxacyclope… | *** | *** | 2 | 1 | 25 | 0~0.1 | *** | 0 |
| metal_106 | Na^[+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 2 | 1 | 25 | 0~0.1 | *** | 0 |
| metal_154 | Rb^[+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 2 | 1 | 25 | 0~0.1 | *** | 0 |
| metal_2 | Ag^[+] | ligand_9674 | 1,4,7,10,13-Pentaoxacyclope… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_2 | Ag^[+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_2 | Ag^[+] | ligand_9678 | cis-anti-cis-2,5,8,15,18,21… | *** | *** | 1 | 1 | 25 | 0 | *** | 0 |
| metal_18 | Ba^[2+] | ligand_9674 | 1,4,7,10,13-Pentaoxacyclope… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_18 | Ba^[2+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 1 | 1 | 25 | 0 | *** | 0 |
| metal_18 | Ba^[2+] | ligand_9678 | cis-anti-cis-2,5,8,15,18,21… | *** | *** | 1 | 1 | 25 | 0 | *** | 0 |
| metal_40 | Cs^[+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 1 | 1 | 25 | 0 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_9674 | 1,4,7,10,13-Pentaoxacyclope… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_9678 | cis-anti-cis-2,5,8,15,18,21… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_78 | K^[+] | ligand_9675 | Benzo-1,4,7,10,13-pentaoxac… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_78 | K^[+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 1 | 1 | 25 | 0 | *** | 0 |
| metal_78 | K^[+] | ligand_9678 | cis-anti-cis-2,5,8,15,18,21… | *** | *** | 1 | 1 | 25 | 0 | *** | 0 |
| metal_97 | MeNH_[3]^[+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_97 | MeNH_[3]^[+] | ligand_9678 | cis-anti-cis-2,5,8,15,18,21… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_92 | Mg^[2+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 1 | 1 | 25 | 0 | *** | 0 |
| metal_111 | NH_[4]^[+] | ligand_9674 | 1,4,7,10,13-Pentaoxacyclope… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_111 | NH_[4]^[+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 1 | 1 | 25 | 0 | *** | 0 |
| metal_111 | NH_[4]^[+] | ligand_9678 | cis-anti-cis-2,5,8,15,18,21… | *** | *** | 1 | 1 | 25 | 0 | *** | 0 |
| metal_106 | Na^[+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_106 | Na^[+] | ligand_9678 | cis-anti-cis-2,5,8,15,18,21… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_9672 | 1,4,7,10-Tetraoxacyclododec… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_9674 | 1,4,7,10,13-Pentaoxacyclope… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_9678 | cis-anti-cis-2,5,8,15,18,21… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_154 | Rb^[+] | ligand_9674 | 1,4,7,10,13-Pentaoxacyclope… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_154 | Rb^[+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 1 | 1 | 25 | 0 | *** | 0 |
| metal_154 | Rb^[+] | ligand_9678 | cis-anti-cis-2,5,8,15,18,21… | *** | *** | 1 | 1 | 25 | 0 | *** | 0 |
| metal_177 | Sr^[2+] | ligand_9674 | 1,4,7,10,13-Pentaoxacyclope… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |

### ΔS — 44 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_2 | Ag^[+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 2 | 1 | 25 | 0~0.1 | *** | 0 |
| metal_18 | Ba^[2+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 2 | 1 | 25 | 0~0.1 | *** | 0 |
| metal_40 | Cs^[+] | ligand_9674 | 1,4,7,10,13-Pentaoxacyclope… | *** | *** | 2 | 1 | 25 | 0~0.1 | *** | 0 |
| metal_40 | Cs^[+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 2 | 1 | 25 | 0~0.1 | *** | 0 |
| metal_72 | Hg^[+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_72 | Hg^[+] | ligand_9678 | cis-anti-cis-2,5,8,15,18,21… | *** | *** | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_78 | K^[+] | ligand_9674 | 1,4,7,10,13-Pentaoxacyclope… | *** | *** | 2 | 1 | 25 | 0~0.1 | *** | 0 |
| metal_78 | K^[+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 2 | 1 | 25 | 0~0.1 | *** | 0 |
| metal_111 | NH_[4]^[+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 2 | 1 | 25 | 0~0.1 | *** | 0 |
| metal_106 | Na^[+] | ligand_9674 | 1,4,7,10,13-Pentaoxacyclope… | *** | *** | 2 | 1 | 25 | 0~0.1 | *** | 0 |
| metal_106 | Na^[+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 2 | 1 | 25 | 0~0.1 | *** | 0 |
| metal_154 | Rb^[+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 2 | 1 | 25 | 0~0.1 | *** | 0 |
| metal_2 | Ag^[+] | ligand_9674 | 1,4,7,10,13-Pentaoxacyclope… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_2 | Ag^[+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_2 | Ag^[+] | ligand_9678 | cis-anti-cis-2,5,8,15,18,21… | *** | *** | 1 | 1 | 25 | 0 | *** | 0 |
| metal_18 | Ba^[2+] | ligand_9674 | 1,4,7,10,13-Pentaoxacyclope… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_18 | Ba^[2+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 1 | 1 | 25 | 0 | *** | 0 |
| metal_18 | Ba^[2+] | ligand_9678 | cis-anti-cis-2,5,8,15,18,21… | *** | *** | 1 | 1 | 25 | 0 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 1 | 1 | 25 | 0 | *** | 0 |
| metal_40 | Cs^[+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 1 | 1 | 25 | 0 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_9674 | 1,4,7,10,13-Pentaoxacyclope… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_9678 | cis-anti-cis-2,5,8,15,18,21… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_78 | K^[+] | ligand_9675 | Benzo-1,4,7,10,13-pentaoxac… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_78 | K^[+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 1 | 1 | 25 | 0 | *** | 0 |
| metal_78 | K^[+] | ligand_9678 | cis-anti-cis-2,5,8,15,18,21… | *** | *** | 1 | 1 | 25 | 0 | *** | 0 |
| metal_97 | MeNH_[3]^[+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_97 | MeNH_[3]^[+] | ligand_9678 | cis-anti-cis-2,5,8,15,18,21… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_92 | Mg^[2+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 1 | 1 | 25 | 0 | *** | 0 |
| metal_111 | NH_[4]^[+] | ligand_9674 | 1,4,7,10,13-Pentaoxacyclope… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_111 | NH_[4]^[+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 1 | 1 | 25 | 0 | *** | 0 |
| metal_111 | NH_[4]^[+] | ligand_9678 | cis-anti-cis-2,5,8,15,18,21… | *** | *** | 1 | 1 | 25 | 0 | *** | 0 |
| metal_106 | Na^[+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_106 | Na^[+] | ligand_9678 | cis-anti-cis-2,5,8,15,18,21… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_9672 | 1,4,7,10-Tetraoxacyclododec… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_9674 | 1,4,7,10,13-Pentaoxacyclope… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclo… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_9678 | cis-anti-cis-2,5,8,15,18,21… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_154 | Rb^[+] | ligand_9674 | 1,4,7,10,13-Pentaoxacyclope… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_154 | Rb^[+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 1 | 1 | 25 | 0 | *** | 0 |
| metal_154 | Rb^[+] | ligand_9678 | cis-anti-cis-2,5,8,15,18,21… | *** | *** | 1 | 1 | 25 | 0 | *** | 0 |
| metal_177 | Sr^[2+] | ligand_9674 | 1,4,7,10,13-Pentaoxacyclope… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |

---
