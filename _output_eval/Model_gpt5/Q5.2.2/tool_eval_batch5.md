# Q5.2.2 — Tool Results (batch 5)

### Step 2: `search_metals`
**Args:**
```json
{
  "symbol": "Fe, Al, Ga, Ti, Cu, Zn, Mn",
  "limit": 200
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
  "name": "transferrin, lactoferrin, ovotransferrin, conalbumin, human serum albumin, bovine serum albumin, serum albumin, albumin, metallothionein, ceruloplasmin",
  "limit": 200
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 5: `db_distribution`
**Args:**
```json
{
  "table": "ligand_card",
  "group_column": "ligand_class_name",
  "limit": 50
}
```

[PHASE ERROR] Tool 'db_distribution' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 6: `search_stability`
**Args:**
```json
{
  "where": "c.ligand_name_SRD LIKE '%transferrin%' OR c.ligand_name_SRD LIKE '%lactoferrin%' OR c.ligand_name_SRD LIKE '%ovotransferrin%' OR c.ligand_name_SRD LIKE '%conalbumin%' OR c.ligand_name_SRD LIKE '%albumin%' OR c.ligand_name_SRD LIKE '%metallothionein%' OR c.ligand_name_SRD LIKE '%ceruloplasmin%'",
  "limit": 5
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 7: `search_metals`
**Args:**
```json
{
  "name": "iron, aluminum, aluminium, gallium, titanium, copper, zinc, manganese",
  "symbol": "Fe, Al, Ga, Ti, Cu, Zn, Mn",
  "limit": 200
}
```

[summary]
## search_metals

*(no results)*

---

### Step 8: `search_ligands`
**Args:**
```json
{
  "name": "transferrin, serotransferrin, apotransferrin, holotransferrin, lactoferrin, ovotransferrin, conalbumin, ferritin, human serum albumin, bovine serum albumin, serum albumin, albumin, HSA, BSA, metallothionein, ceruloplasmin",
  "limit": 200
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 9: `build_system_catalog`
**Args:**
```json
{}
```

[summary]
[CATALOG]
## build_system_catalog

**Error:** Provide at least one of metal_id, ligand_id, or beta_definition_id.

---

### Step 10: `search_metals`
**Args:**
```json
{
  "limit": 25
}
```

[summary]
## search_metals — 25 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_1 | Ac^[3+] | Ac | 3 | ✓ | [Ac+3] | InChI=1S/Ac/q+3 | beta_totN_4 | ligand_totN_9 | vlm_totN_23 |
| metal_2 | Ag^[+] | Ag | 1 | ✓ | [Ag+] | InChI=1S/Ag/q+1 | beta_totN_68 | ligand_totN_649 | vlm_totN_2885 |
| metal_3 | Ag^[2+] | Ag | 2 | ✓ | [Ag+2] | InChI=1S/Ag/q+2 | beta_totN_1 | ligand_totN_5 | vlm_totN_5 |
| metal_4 | Ag^[3+] | Ag | 3 | ✓ | [Ag+3] | InChI=1S/Ag/q+3 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_5 | Al^[3+] | Al | 3 | ✓ | [Al+3] | InChI=1S/Al/q+3 | beta_totN_108 | ligand_totN_187 | vlm_totN_792 |
| metal_6 | Am^[3+] | Am | 3 | ✓ | [Am+3] | InChI=1S/Am/q+3 | beta_totN_13 | ligand_totN_46 | vlm_totN_190 |
| metal_7 | Am^[4+] | Am | 4 | ✓ | [Am+4] | InChI=1S/Am/q+4 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_8 | AmO_[2]^[2+] | Am | 2 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_9 | AmO_[2]^[+] | Am | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_10 | As^[3+] | As | 3 | ✓ | [As+3] | InChI=1S/As/q+3 | beta_totN_17 | ligand_totN_42 | vlm_totN_62 |
| metal_11 | As^[5+] | As | 5 | ✓ | [As+5] | InChI=1S/As/q+5 | beta_totN_5 | ligand_totN_6 | vlm_totN_8 |
| metal_12 | At^[+] | At | 1 | ✓ | [At+] | InChI=1S/At/q+1 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_13 | Au^[+] | Au | 1 | ✓ | [Au+] | InChI=1S/Au/q+1 | beta_totN_5 | ligand_totN_3 | vlm_totN_13 |
| metal_14 | Au^[3+] | Au | 3 | ✓ | [Au+3] | InChI=1S/Au/q+3 | beta_totN_11 | ligand_totN_10 | vlm_totN_22 |
| metal_15 | B^[3+] | B | 3 | ✓ | [B+3] | InChI=1S/B/q+3 | beta_totN_23 | ligand_totN_86 | vlm_totN_195 |
| metal_16 | Bu_[3]Pb^[+] | B | 1 |  | *** | *** | beta_totN_2 | ligand_totN_1 | vlm_totN_2 |
| metal_17 | Bu_[4]N^[+] | B | 1 |  | *** | *** | beta_totN_1 | ligand_totN_2 | vlm_totN_2 |
| metal_18 | Ba^[2+] | Ba | 2 | ✓ | [Ba+2] | InChI=1S/Ba/q+2 | beta_totN_36 | ligand_totN_344 | vlm_totN_749 |
| metal_19 | Be^[2+] | Be | 2 | ✓ | [Be+2] | InChI=1S/Be/q+2 | beta_totN_69 | ligand_totN_107 | vlm_totN_443 |
| metal_20 | BuHg^[+] | B | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_21 | Bi^[3+] | Bi | 3 | ✓ | [Bi+3] | InChI=1S/Bi/q+3 | beta_totN_30 | ligand_totN_44 | vlm_totN_283 |
| metal_22 | Bk^[3+] | Bk | 3 | ✓ | [Bk+3] | InChI=1S/Bk/q+3 | beta_totN_2 | ligand_totN_15 | vlm_totN_28 |
| metal_23 | BuNH_[3]^[+] | B | 1 |  | *** | *** | beta_totN_1 | ligand_totN_2 | vlm_totN_2 |
| metal_24 | C(NH_[2])_[3]^[+] | C | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_25 | Ca^[2+] | Ca | 2 | ✓ | [Ca+2] | InChI=1S/Ca/q+2 | beta_totN_68 | ligand_totN_644 | vlm_totN_1761 |

---

### Step 11: `search_ligands`
**Args:**
```json
{
  "name": "transferrin, lactoferrin, ovotransferrin, conalbumin, ferritin, human serum albumin, bovine serum albumin, serum albumin, albumin, metallothionein, ceruloplasmin",
  "limit": 200
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 12: `search_ligands`
**Args:**
```json
{
  "ligand_class": "protein",
  "limit": 50
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 13: `search_metals`
**Args:**
```json
{
  "limit": 500
}
```

[summary]
## search_metals — 230 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_1 | Ac^[3+] | Ac | 3 | ✓ | [Ac+3] | InChI=1S/Ac/q+3 | beta_totN_4 | ligand_totN_9 | vlm_totN_23 |
| metal_2 | Ag^[+] | Ag | 1 | ✓ | [Ag+] | InChI=1S/Ag/q+1 | beta_totN_68 | ligand_totN_649 | vlm_totN_2885 |
| metal_3 | Ag^[2+] | Ag | 2 | ✓ | [Ag+2] | InChI=1S/Ag/q+2 | beta_totN_1 | ligand_totN_5 | vlm_totN_5 |
| metal_4 | Ag^[3+] | Ag | 3 | ✓ | [Ag+3] | InChI=1S/Ag/q+3 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_5 | Al^[3+] | Al | 3 | ✓ | [Al+3] | InChI=1S/Al/q+3 | beta_totN_108 | ligand_totN_187 | vlm_totN_792 |
| metal_6 | Am^[3+] | Am | 3 | ✓ | [Am+3] | InChI=1S/Am/q+3 | beta_totN_13 | ligand_totN_46 | vlm_totN_190 |
| metal_7 | Am^[4+] | Am | 4 | ✓ | [Am+4] | InChI=1S/Am/q+4 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_8 | AmO_[2]^[2+] | Am | 2 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_9 | AmO_[2]^[+] | Am | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_10 | As^[3+] | As | 3 | ✓ | [As+3] | InChI=1S/As/q+3 | beta_totN_17 | ligand_totN_42 | vlm_totN_62 |
| metal_11 | As^[5+] | As | 5 | ✓ | [As+5] | InChI=1S/As/q+5 | beta_totN_5 | ligand_totN_6 | vlm_totN_8 |
| metal_12 | At^[+] | At | 1 | ✓ | [At+] | InChI=1S/At/q+1 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_13 | Au^[+] | Au | 1 | ✓ | [Au+] | InChI=1S/Au/q+1 | beta_totN_5 | ligand_totN_3 | vlm_totN_13 |
| metal_14 | Au^[3+] | Au | 3 | ✓ | [Au+3] | InChI=1S/Au/q+3 | beta_totN_11 | ligand_totN_10 | vlm_totN_22 |
| metal_15 | B^[3+] | B | 3 | ✓ | [B+3] | InChI=1S/B/q+3 | beta_totN_23 | ligand_totN_86 | vlm_totN_195 |
| metal_16 | Bu_[3]Pb^[+] | B | 1 |  | *** | *** | beta_totN_2 | ligand_totN_1 | vlm_totN_2 |
| metal_17 | Bu_[4]N^[+] | B | 1 |  | *** | *** | beta_totN_1 | ligand_totN_2 | vlm_totN_2 |
| metal_18 | Ba^[2+] | Ba | 2 | ✓ | [Ba+2] | InChI=1S/Ba/q+2 | beta_totN_36 | ligand_totN_344 | vlm_totN_749 |
| metal_19 | Be^[2+] | Be | 2 | ✓ | [Be+2] | InChI=1S/Be/q+2 | beta_totN_69 | ligand_totN_107 | vlm_totN_443 |
| metal_20 | BuHg^[+] | B | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_21 | Bi^[3+] | Bi | 3 | ✓ | [Bi+3] | InChI=1S/Bi/q+3 | beta_totN_30 | ligand_totN_44 | vlm_totN_283 |
| metal_22 | Bk^[3+] | Bk | 3 | ✓ | [Bk+3] | InChI=1S/Bk/q+3 | beta_totN_2 | ligand_totN_15 | vlm_totN_28 |
| metal_23 | BuNH_[3]^[+] | B | 1 |  | *** | *** | beta_totN_1 | ligand_totN_2 | vlm_totN_2 |
| metal_24 | C(NH_[2])_[3]^[+] | C | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_25 | Ca^[2+] | Ca | 2 | ✓ | [Ca+2] | InChI=1S/Ca/q+2 | beta_totN_68 | ligand_totN_644 | vlm_totN_1761 |
| metal_26 | Cd^[2+] | Cd | 2 | ✓ | [Cd+2] | InChI=1S/Cd/q+2 | beta_totN_95 | ligand_totN_818 | vlm_totN_2828 |
| metal_27 | Ce^[3+] | Ce | 3 | ✓ | [Ce+3] | InChI=1S/Ce/q+3 | beta_totN_22 | ligand_totN_188 | vlm_totN_567 |
| metal_28 | Ce^[4+] | Ce | 4 | ✓ | [Ce+4] | InChI=1S/Ce/q+4 | beta_totN_5 | ligand_totN_3 | vlm_totN_9 |
| metal_29 | Cf^[3+] | Cf | 3 | ✓ | [Cf+3] | InChI=1S/Cf/q+3 | beta_totN_4 | ligand_totN_23 | vlm_totN_42 |
| metal_30 | ClMe_[2]Sn^[+] | Cl | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_31 | Cm^[3+] | Cm | 3 | ✓ | [Cm+3] | InChI=1S/Cm/q+3 | beta_totN_6 | ligand_totN_31 | vlm_totN_84 |
| metal_32 | CetMe_[3]N^[+] | C | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_33 | Co^[2+] | Co | 2 | ✓ | [Co+2] | InChI=1S/Co/q+2 | beta_totN_92 | ligand_totN_977 | vlm_totN_2977 |
| metal_34 | Co^[3+] | Co | 3 | ✓ | [Co+3] | InChI=1S/Co/q+3 | beta_totN_20 | ligand_totN_19 | vlm_totN_55 |
| metal_35 | Cr^[+] | Cr | 1 | ✓ | [Cr+] | InChI=1S/Cr/q+1 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_36 | Cr^[2+] | Cr | 2 | ✓ | [Cr+2] | InChI=1S/Cr/q+2 | beta_totN_7 | ligand_totN_32 | vlm_totN_66 |
| metal_37 | Cr^[3+] | Cr | 3 | ✓ | [Cr+3] | InChI=1S/Cr/q+3 | beta_totN_35 | ligand_totN_37 | vlm_totN_130 |
| metal_38 | Cr^[4+] | Cr | 4 | ✓ | [Cr+4] | InChI=1S/Cr/q+4 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_39 | CrO_[4]^[2-] | Cr | -2 |  | *** | *** | beta_totN_1 | ligand_totN_1 | vlm_totN_1 |
| metal_40 | Cs^[+] | Cs | 1 | ✓ | [Cs+] | InChI=1S/Cs/q+1 | beta_totN_10 | ligand_totN_47 | vlm_totN_86 |
| metal_41 | Cu^[2+] | Cu | 2 | ✓ | [Cu+2] | InChI=1S/Cu/q+2 | beta_totN_264 | ligand_totN_1951 | vlm_totN_8963 |
| metal_42 | Cu^[+] | Cu | 1 | ✓ | [Cu+] | InChI=1S/Cu/q+1 | beta_totN_32 | ligand_totN_117 | vlm_totN_285 |
| metal_43 | Cu^[3+] | Cu | 3 | ✓ | [Cu+3] | InChI=1S/Cu/q+3 | beta_totN_4 | ligand_totN_8 | vlm_totN_10 |
| metal_44 | Dy^[3+] | Dy | 3 | ✓ | [Dy+3] | InChI=1S/Dy/q+3 | beta_totN_23 | ligand_totN_252 | vlm_totN_758 |
| metal_45 | Et_[2]NH_[2]^[+] | E2NH2 | 1 |  | *** | *** | beta_totN_1 | ligand_totN_1 | vlm_totN_1 |
| metal_46 | Et_[2]Pb^[2+] | E2Pb | 2 |  | *** | *** | beta_totN_2 | ligand_totN_3 | vlm_totN_5 |
| metal_47 | Et_[2]Sn^[2+] | E2Sn | 2 |  | *** | *** | beta_totN_4 | ligand_totN_1 | vlm_totN_12 |
| metal_48 | Et_[3]NH^[+] | E3NH | 1 |  | *** | *** | beta_totN_1 | ligand_totN_1 | vlm_totN_1 |
| metal_49 | Et_[3]Pb^[+] | E3Pb | 1 |  | *** | *** | beta_totN_2 | ligand_totN_3 | vlm_totN_5 |
| metal_50 | Et_[3]Sn^[+] | E3Sn | 1 |  | *** | *** | beta_totN_1 | ligand_totN_1 | vlm_totN_1 |
| metal_51 | Et_[4]N^[+] | E4N | 1 |  | *** | *** | beta_totN_1 | ligand_totN_3 | vlm_totN_5 |
| metal_52 | Vy_[2]Sn^[2+] | Eene2Sn | 2 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_53 | EtHg^[+] | EHg | 1 |  | *** | *** | beta_totN_4 | ligand_totN_3 | vlm_totN_6 |
| metal_54 | EtNH_[3]^[+] | ENH3 | 1 |  | *** | *** | beta_totN_1 | ligand_totN_3 | vlm_totN_3 |
| metal_55 | Er^[3+] | Er | 3 | ✓ | [Er+3] | InChI=1S/Er/q+3 | beta_totN_29 | ligand_totN_241 | vlm_totN_792 |
| metal_56 | Es^[3+] | Es | 3 | ✓ | [Es+3] | InChI=1S/Es/q+3 | beta_totN_2 | ligand_totN_6 | vlm_totN_7 |
| metal_57 | EtSn^[3+] | ESn | 3 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_58 | Eu^[3+] | Eu | 3 | ✓ | [Eu+3] | InChI=1S/Eu/q+3 | beta_totN_30 | ligand_totN_267 | vlm_totN_870 |
| metal_59 | Eu^[2+] | Eu | 2 | ✓ | [Eu+2] | InChI=1S/Eu/q+2 | beta_totN_1 | ligand_totN_2 | vlm_totN_2 |
| metal_60 | Eu^[4+] | Eu | 4 | ✓ | [Eu+4] | InChI=1S/Eu/q+4 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_61 | Fe^[3+] | Fe | 3 | ✓ | [Fe+3] | InChI=1S/Fe/q+3 | beta_totN_128 | ligand_totN_406 | vlm_totN_1473 |
| metal_62 | Fe^[2+] | Fe | 2 | ✓ | [Fe+2] | InChI=1S/Fe/q+2 | beta_totN_57 | ligand_totN_217 | vlm_totN_667 |
| metal_63 | Fm^[3+] | Fm | 3 | ✓ | [Fm+3] | InChI=1S/Fm/q+3 | beta_totN_2 | ligand_totN_3 | vlm_totN_3 |
| metal_64 | Ga^[3+] | Ga | 3 | ✓ | [Ga+3] | InChI=1S/Ga/q+3 | beta_totN_38 | ligand_totN_146 | vlm_totN_428 |
| metal_65 | Gd^[3+] | Gd | 3 | ✓ | [Gd+3] | InChI=1S/Gd/q+3 | beta_totN_28 | ligand_totN_288 | vlm_totN_897 |
| metal_66 | Ge^[4+] | Ge | 4 | ✓ | [Ge+4] | InChI=1S/Ge/q+4 | beta_totN_32 | ligand_totN_80 | vlm_totN_132 |
| metal_67 | Ge^[2+] | Ge | 2 | ✓ | [Ge+2] | InChI=1S/Ge/q+2 | beta_totN_1 | ligand_totN_1 | vlm_totN_1 |
| metal_68 | H^[+] | H | 1 | ✓ | [H+] | InChI=1S/p+1 | beta_totN_82 | ligand_totN_4081 | vlm_totN_20720 |
| metal_69 | H_[5]TeO_[6]^[-] | H | -1 |  | *** | *** | beta_totN_1 | ligand_totN_1 | vlm_totN_2 |
| metal_70 | Hf^[4+] | Hf | 4 | ✓ | [Hf+4] | InChI=1S/Hf/q+4 | beta_totN_10 | ligand_totN_14 | vlm_totN_49 |
| metal_71 | Hg^[2+] | Hg | 2 | ✓ | [Hg+2] | InChI=1S/Hg/q+2 | beta_totN_68 | ligand_totN_310 | vlm_totN_1097 |
| metal_72 | Hg^[+] | Hg | 1 | ✓ | [Hg+] | InChI=1S/Hg/q+1 | beta_totN_12 | ligand_totN_31 | vlm_totN_83 |
| metal_73 | Ho^[3+] | Ho | 3 | ✓ | [Ho+3] | InChI=1S/Ho/q+3 | beta_totN_24 | ligand_totN_230 | vlm_totN_705 |
| metal_74 | In^[3+] | In | 3 | ✓ | [In+3] | InChI=1S/In/q+3 | beta_totN_41 | ligand_totN_109 | vlm_totN_433 |
| metal_75 | In^[+] | In | 1 | ✓ | [In+] | InChI=1S/In/q+1 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_76 | Ir^[3+] | Ir | 3 | ✓ | [Ir+3] | InChI=1S/Ir/q+3 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_77 | Ir^[4+] | Ir | 4 | ✓ | [Ir+4] | InChI=1S/Ir/q+4 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_78 | K^[+] | K | 1 | ✓ | [K+] | InChI=1S/K/q+1 | beta_totN_19 | ligand_totN_134 | vlm_totN_335 |
| metal_79 | La^[3+] | La | 3 | ✓ | [La+3] | InChI=1S/La/q+3 | beta_totN_30 | ligand_totN_297 | vlm_totN_931 |
| metal_80 | Li^[+] | Li | 1 | ✓ | [Li+] | InChI=1S/Li/q+1 | beta_totN_11 | ligand_totN_92 | vlm_totN_216 |
| metal_81 | Lu^[3+] | Lu | 3 | ✓ | [Lu+3] | InChI=1S/Lu/q+3 | beta_totN_25 | ligand_totN_234 | vlm_totN_671 |
| metal_82 | Me_[2]Au^[+] | M2Au | 1 |  | *** | *** | beta_totN_1 | ligand_totN_1 | vlm_totN_1 |
| metal_83 | Me_[2]Ga^[+] | M2Ga | 1 |  | *** | *** | beta_totN_2 | ligand_totN_1 | vlm_totN_2 |
| metal_84 | Me_[2]Pb^[2+] | M2Pb | 2 |  | *** | *** | beta_totN_5 | ligand_totN_4 | vlm_totN_9 |
| metal_85 | Me_[2]Sn^[2+] | M2Sn | 2 |  | *** | *** | beta_totN_19 | ligand_totN_26 | vlm_totN_165 |
| metal_86 | Me_[2]Tl^[+] | M2Tl | 1 |  | *** | *** | beta_totN_4 | ligand_totN_6 | vlm_totN_11 |
| metal_87 | Me_[3]Pb^[+] | M3Pb | 1 |  | *** | *** | beta_totN_7 | ligand_totN_23 | vlm_totN_33 |
| metal_88 | Me_[3]Sn^[+] | M3Sn | 1 |  | *** | *** | beta_totN_5 | ligand_totN_10 | vlm_totN_17 |
| metal_89 | Me_[4]N^[+] | M4N | 1 |  | *** | *** | beta_totN_1 | ligand_totN_4 | vlm_totN_6 |
| metal_90 | MeB(OH)_[2] | MB | 0 |  | *** | *** | beta_totN_2 | ligand_totN_4 | vlm_totN_4 |
| metal_91 | Md^[3+] | Md | 3 | ✓ | [Md+3] | InChI=1S/Md/q+3 | beta_totN_1 | ligand_totN_1 | vlm_totN_1 |
| metal_92 | Mg^[2+] | Mg | 2 | ✓ | [Mg+2] | InChI=1S/Mg/q+2 | beta_totN_53 | ligand_totN_508 | vlm_totN_1422 |
| metal_93 | MeHg^[+] | MHg | 1 |  | *** | *** | beta_totN_18 | ligand_totN_79 | vlm_totN_148 |
| metal_94 | Mn^[2+] | Mn | 2 | ✓ | [Mn+2] | InChI=1S/Mn/q+2 | beta_totN_44 | ligand_totN_486 | vlm_totN_1273 |
| metal_95 | Mn^[3+] | Mn | 3 | ✓ | [Mn+3] | InChI=1S/Mn/q+3 | beta_totN_8 | ligand_totN_12 | vlm_totN_26 |
| metal_96 | Mn^[4+] | Mn | 4 | ✓ | [Mn+4] | InChI=1S/Mn/q+4 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_97 | MeNH_[3]^[+] | MNH3 | 1 |  | *** | *** | beta_totN_1 | ligand_totN_5 | vlm_totN_9 |
| metal_98 | m-NO_[2]PhB(OH)_[2] | m-NOPhB(OH) | 0 |  | *** | *** | beta_totN_2 | ligand_totN_4 | vlm_totN_4 |
| metal_99 | Mo_[2]O_[7]^[2-] | Mo | -2 |  | *** | *** | beta_totN_2 | ligand_totN_1 | vlm_totN_2 |
| metal_100 | Mo^[3+] | Mo | 3 | ✓ | [Mo+3] | InChI=1S/Mo/q+3 | beta_totN_1 | ligand_totN_1 | vlm_totN_1 |
| metal_101 | Mo^[4+] | Mo | 4 | ✓ | [Mo+4] | InChI=1S/Mo/q+4 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_102 | Mo^[5+] | Mo | 5 | ✓ | [Mo+5] | InChI=1S/Mo/q+5 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_103 | Mo^[6+] | Mo | 6 | ✓ | [Mo+6] | InChI=1S/Mo/q+6 | beta_totN_33 | ligand_totN_29 | vlm_totN_108 |
| metal_104 | MeReO_[3] | MReO3 | 0 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_105 | MeSn^[3+] | MSn | 3 |  | *** | *** | beta_totN_5 | ligand_totN_2 | vlm_totN_8 |
| metal_106 | Na^[+] | Na | 1 | ✓ | [Na+] | InChI=1S/Na/q+1 | beta_totN_16 | ligand_totN_134 | vlm_totN_335 |
| metal_107 | Nb(OH)_[2]^[+] | Nb | 1 |  | *** | *** | beta_totN_1 | ligand_totN_1 | vlm_totN_1 |
| metal_108 | Nb^[5+] | Nb | 5 | ✓ | [Nb+5] | InChI=1S/Nb/q+5 | beta_totN_5 | ligand_totN_2 | vlm_totN_5 |
| metal_109 | Nb^[3+] | Nb | 3 | ✓ | [Nb+3] | InChI=1S/Nb/q+3 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_110 | Nd^[3+] | Nd | 3 | ✓ | [Nd+3] | InChI=1S/Nd/q+3 | beta_totN_29 | ligand_totN_263 | vlm_totN_794 |
| metal_111 | NH_[4]^[+] | N | 1 |  | *** | *** | beta_totN_8 | ligand_totN_35 | vlm_totN_72 |
| metal_112 | Ni^[2+] | Ni | 2 | ✓ | [Ni+2] | InChI=1S/Ni/q+2 | beta_totN_149 | ligand_totN_1369 | vlm_totN_5325 |
| metal_113 | Ni^[3+] | Ni | 3 | ✓ | [Ni+3] | InChI=1S/Ni/q+3 | beta_totN_5 | ligand_totN_4 | vlm_totN_7 |
| metal_114 | No^[2+] | No | 2 | ✓ | [No+2] | InChI=1S/No/q+2 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_115 | Np^[3+] | Np | 3 | ✓ | [Np+3] | InChI=1S/Np/q+3 | beta_totN_1 | ligand_totN_1 | vlm_totN_1 |
| metal_116 | Np^[4+] | Np | 4 | ✓ | [Np+4] | InChI=1S/Np/q+4 | beta_totN_7 | ligand_totN_15 | vlm_totN_51 |
| metal_117 | NpO_[2]^[2+] | Np | 2 |  | *** | *** | beta_totN_7 | ligand_totN_15 | vlm_totN_64 |
| metal_118 | NpO_[2]^[+] | Np | 1 |  | *** | *** | beta_totN_8 | ligand_totN_55 | vlm_totN_129 |
| metal_119 | NpO_[3]^[+] | Np | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_120 | OsO_[2] | Os | 0 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_121 | OsO_[3] | Os | 0 |  | *** | *** | beta_totN_2 | ligand_totN_1 | vlm_totN_2 |
| metal_122 | OsO_[4] | Os | 0 |  | *** | *** | beta_totN_1 | ligand_totN_1 | vlm_totN_2 |
| metal_123 | Pa^[4+] | Pa | 4 | ✓ | [Pa+4] | InChI=1S/Pa/q+4 | beta_totN_4 | ligand_totN_2 | vlm_totN_7 |
| metal_124 | Pa^[5+] | Pa | 5 | ✓ | [Pa+5] | InChI=1S/Pa/q+5 | beta_totN_2 | ligand_totN_1 | vlm_totN_4 |
| metal_125 | Pb^[2+] | Pb | 2 | ✓ | [Pb+2] | InChI=1S/Pb/q+2 | beta_totN_80 | ligand_totN_470 | vlm_totN_1585 |
| metal_126 | Pb^[4+] | Pb | 4 | ✓ | [Pb+4] | InChI=1S/Pb/q+4 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_127 | Pd^[2+] | Pd | 2 | ✓ | [Pd+2] | InChI=1S/Pd/q+2 | beta_totN_43 | ligand_totN_86 | vlm_totN_245 |
| metal_128 | Pd^[4+] | Pd | 4 | ✓ | [Pd+4] | InChI=1S/Pd/q+4 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_129 | Ph_[2]Pb^[2+] | Ph2Pb | 2 |  | *** | *** | beta_totN_2 | ligand_totN_1 | vlm_totN_2 |
| metal_130 | Ph_[3]Pb^[+] | Ph3Pb | 1 |  | *** | *** | beta_totN_1 | ligand_totN_2 | vlm_totN_2 |
| metal_131 | Ph_[3]Sn^[+] | Ph3Sn | 1 |  | *** | *** | beta_totN_1 | ligand_totN_1 | vlm_totN_1 |
| metal_132 | Ph_[4]As^[+] | Ph4As | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_133 | Ph_[4]P^[+] | Ph4P | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_134 | Ph_[4]Sb^[+] | Ph4Sb | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_135 | PhB(OH)_[2] | PhB | 0 |  | *** | *** | beta_totN_6 | ligand_totN_16 | vlm_totN_16 |
| metal_136 | PhHg^[+] | PhHg | 1 |  | *** | *** | beta_totN_2 | ligand_totN_8 | vlm_totN_8 |
| metal_137 | Pm^[3+] | Pm | 3 | ✓ | [Pm+3] | InChI=1S/Pm/q+3 | beta_totN_4 | ligand_totN_14 | vlm_totN_24 |
| metal_138 | Po | Po | 0 | ✓ | [Po] | InChI=1S/Po | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_139 | Pr^[3+] | Pr | 3 | ✓ | [Pr+3] | InChI=1S/Pr/q+3 | beta_totN_24 | ligand_totN_231 | vlm_totN_723 |
| metal_140 | Pr_[2]Pb^[2+] | Pr | 2 |  | *** | *** | beta_totN_2 | ligand_totN_3 | vlm_totN_5 |
| metal_141 | Pr_[2]Sn^[2+] | Pr | 2 |  | *** | *** | beta_totN_2 | ligand_totN_1 | vlm_totN_2 |
| metal_142 | Pr_[3]Pb^[+] | Pr | 1 |  | *** | *** | beta_totN_2 | ligand_totN_1 | vlm_totN_2 |
| metal_143 | Pr_[3]Sn^[+] | Pr | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_144 | Pr_[4]N^[+] | Pr | 1 |  | *** | *** | beta_totN_1 | ligand_totN_3 | vlm_totN_5 |
| metal_145 | PrHg^[+] | Pr | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_146 | Pt^[2+] | Pt | 2 | ✓ | [Pt+2] | InChI=1S/Pt/q+2 | beta_totN_12 | ligand_totN_19 | vlm_totN_36 |
| metal_147 | Pt^[4+] | Pt | 4 | ✓ | [Pt+4] | InChI=1S/Pt/q+4 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_148 | Pu^[3+] | Pu | 3 | ✓ | [Pu+3] | InChI=1S/Pu/q+3 | beta_totN_7 | ligand_totN_12 | vlm_totN_28 |
| metal_149 | Pu^[4+] | Pu | 4 | ✓ | [Pu+4] | InChI=1S/Pu/q+4 | beta_totN_6 | ligand_totN_11 | vlm_totN_36 |
| metal_150 | PuO_[2]^[2+] | Pu | 2 |  | *** | *** | beta_totN_10 | ligand_totN_22 | vlm_totN_76 |
| metal_151 | PuO_[2]^[+] | Pu | 1 |  | *** | *** | beta_totN_2 | ligand_totN_6 | vlm_totN_6 |
| metal_152 | R_[4]N^[+] | R4N | 1 | ✓ | [N+] | InChI=1S/N/q+1 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_153 | Ra^[2+] | Ra | 2 | ✓ | [Ra+2] | InChI=1S/Ra/q+2 | beta_totN_2 | ligand_totN_10 | vlm_totN_11 |
| metal_154 | Rb^[+] | Rb | 1 | ✓ | [Rb+] | InChI=1S/Rb/q+1 | beta_totN_9 | ligand_totN_43 | vlm_totN_74 |
| metal_155 | Re^[2+] | Re | 2 | ✓ | [Re+2] | InChI=1S/Re/q+2 | beta_totN_1 | ligand_totN_1 | vlm_totN_1 |
| metal_156 | Re^[4+] | Re | 4 | ✓ | [Re+4] | InChI=1S/Re/q+4 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_157 | Re^[5+] | Re | 5 | ✓ | [Re+5] | InChI=1S/Re/q+5 | beta_totN_2 | ligand_totN_2 | vlm_totN_2 |
| metal_158 | Re^[7+] | Re | 7 | ✓ | [Re+7] | InChI=1S/Re/q+7 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_159 | Rh^[+] | Rh | 1 | ✓ | [Rh+] | InChI=1S/Rh/q+1 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_160 | Rh^[3+] | Rh | 3 | ✓ | [Rh+3] | InChI=1S/Rh/q+3 | beta_totN_6 | ligand_totN_2 | vlm_totN_16 |
| metal_161 | Rh^[4+] | Rh | 4 | ✓ | [Rh+4] | InChI=1S/Rh/q+4 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_162 | Rh^[5+] | Rh | 5 | ✓ | [Rh+5] | InChI=1S/Rh/q+5 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_163 | Ru^[2+] | Ru | 2 | ✓ | [Ru+2] | InChI=1S/Ru/q+2 | beta_totN_1 | ligand_totN_1 | vlm_totN_6 |
| metal_164 | Ru^[3+] | Ru | 3 | ✓ | [Ru+3] | InChI=1S/Ru/q+3 | beta_totN_2 | ligand_totN_1 | vlm_totN_2 |
| metal_165 | Ru^[4+] | Ru | 4 | ✓ | [Ru+4] | InChI=1S/Ru/q+4 | beta_totN_1 | ligand_totN_1 | vlm_totN_6 |
| metal_166 | Ru^[6+] | Ru | 6 | ✓ | [Ru+6] | InChI=1S/Ru/q+6 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_167 | Sb^[3+] | Sb | 3 | ✓ | [Sb+3] | InChI=1S/Sb/q+3 | beta_totN_32 | ligand_totN_17 | vlm_totN_57 |
| metal_168 | Sb^[5+] | Sb | 5 | ✓ | [Sb+5] | InChI=1S/Sb/q+5 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_169 | Sc^[3+] | Sc | 3 | ✓ | [Sc+3] | InChI=1S/Sc/q+3 | beta_totN_16 | ligand_totN_44 | vlm_totN_156 |
| metal_170 | Se^[4+] | Se | 4 | ✓ | [Se+4] | InChI=1S/Se/q+4 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_171 | Se^[6+] | Se | 6 | ✓ | [Se+6] | InChI=1S/Se/q+6 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_172 | Si^[4+] | Si | 4 | ✓ | [Si+4] | InChI=1S/Si/q+4 | beta_totN_8 | ligand_totN_13 | vlm_totN_24 |
| metal_173 | Sm^[3+] | Sm | 3 | ✓ | [Sm+3] | InChI=1S/Sm/q+3 | beta_totN_28 | ligand_totN_265 | vlm_totN_844 |
| metal_174 | Sn^[2+] | Sn | 2 | ✓ | [Sn+2] | InChI=1S/Sn/q+2 | beta_totN_22 | ligand_totN_27 | vlm_totN_145 |
| metal_175 | Sn^[4+] | Sn | 4 | ✓ | [Sn+4] | InChI=1S/Sn/q+4 | beta_totN_5 | ligand_totN_1 | vlm_totN_5 |
| metal_176 | O_[3]SPhHg | S | 0 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_177 | Sr^[2+] | Sr | 2 | ✓ | [Sr+2] | InChI=1S/Sr/q+2 | beta_totN_34 | ligand_totN_362 | vlm_totN_784 |
| metal_178 | Ta^[5+] | Ta | 5 | ✓ | [Ta+5] | InChI=1S/Ta/q+5 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_179 | Tb^[3+] | Tb | 3 | ✓ | [Tb+3] | InChI=1S/Tb/q+3 | beta_totN_24 | ligand_totN_235 | vlm_totN_709 |
| metal_180 | Tc^[7+] | Tc | 7 | ✓ | [Tc+7] | InChI=1S/Tc/q+7 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_181 | TcO^[2+] | Tc | 2 |  | *** | *** | beta_totN_2 | ligand_totN_1 | vlm_totN_2 |
| metal_182 | Te^[4+] | Te | 4 | ✓ | [Te+4] | InChI=1S/Te/q+4 | beta_totN_2 | ligand_totN_19 | vlm_totN_21 |
| metal_183 | Te^[6+] | Te | 6 | ✓ | [Te+6] | InChI=1S/Te/q+6 | beta_totN_2 | ligand_totN_2 | vlm_totN_3 |
| metal_185 | Th^[4+] | Th | 4 | ✓ | [Th+4] | InChI=1S/Th/q+4 | beta_totN_44 | ligand_totN_99 | vlm_totN_476 |
| metal_186 | Ti | Ti | 0 | ✓ | [Ti] | InChI=1S/Ti | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_187 | Ti^[3+] | Ti | 3 | ✓ | [Ti+3] | InChI=1S/Ti/q+3 | beta_totN_21 | ligand_totN_11 | vlm_totN_39 |
| metal_188 | Ti^[4+] | Ti | 4 | ✓ | [Ti+4] | InChI=1S/Ti/q+4 | beta_totN_6 | ligand_totN_3 | vlm_totN_10 |
| metal_189 | TiO^[2+] | Ti | 2 |  | *** | *** | beta_totN_1 | ligand_totN_2 | vlm_totN_6 |
| metal_190 | Tl^[3+] | Tl | 3 | ✓ | [Tl+3] | InChI=1S/Tl/q+3 | beta_totN_13 | ligand_totN_23 | vlm_totN_130 |
| metal_191 | Tl^[+] | Tl | 1 | ✓ | [Tl+] | InChI=1S/Tl/q+1 | beta_totN_14 | ligand_totN_87 | vlm_totN_272 |
| metal_192 | Tm^[3+] | Tm | 3 | ✓ | [Tm+3] | InChI=1S/Tm/q+3 | beta_totN_22 | ligand_totN_223 | vlm_totN_633 |
| metal_193 | U^[4+] | U | 4 | ✓ | [U+4] | InChI=1S/U/q+4 | beta_totN_13 | ligand_totN_18 | vlm_totN_102 |
| metal_194 | U^[3+] | U | 3 | ✓ | [U+3] | InChI=1S/U/q+3 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_195 | UO_[2]^[2+] | U | 2 |  | *** | *** | beta_totN_75 | ligand_totN_163 | vlm_totN_748 |
| metal_196 | UO_[2]^[+] | U | 1 |  | *** | *** | beta_totN_1 | ligand_totN_1 | vlm_totN_1 |
| metal_197 | V^[5+] | V | 5 | ✓ | [V+5] | InChI=1S/V/q+5 | beta_totN_8 | ligand_totN_2 | vlm_totN_8 |
| metal_198 | V^[2+] | V | 2 | ✓ | [V+2] | InChI=1S/V/q+2 | beta_totN_5 | ligand_totN_8 | vlm_totN_17 |
| metal_199 | V^[3+] | V | 3 | ✓ | [V+3] | InChI=1S/V/q+3 | beta_totN_21 | ligand_totN_13 | vlm_totN_53 |
| metal_200 | V^[4+] | V | 4 | ✓ | [V+4] | InChI=1S/V/q+4 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_201 | VO^[2+] | V | 2 |  | *** | *** | beta_totN_58 | ligand_totN_96 | vlm_totN_364 |
| metal_202 | VO_[2]^[+] | V | 1 |  | *** | *** | beta_totN_22 | ligand_totN_24 | vlm_totN_64 |
| metal_203 | W^[4+] | W | 4 | ✓ | [W+4] | InChI=1S/W/q+4 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_204 | W^[6+] | W | 6 | ✓ | [W+6] | InChI=1S/W/q+6 | beta_totN_18 | ligand_totN_24 | vlm_totN_63 |
| metal_205 | Y^[3+] | Y | 3 | ✓ | [Y+3] | InChI=1S/Y/q+3 | beta_totN_26 | ligand_totN_182 | vlm_totN_533 |
| metal_206 | Yb^[3+] | Yb | 3 | ✓ | [Yb+3] | InChI=1S/Yb/q+3 | beta_totN_28 | ligand_totN_235 | vlm_totN_771 |
| metal_207 | Yb^[2+] | Yb | 2 | ✓ | [Yb+2] | InChI=1S/Yb/q+2 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_208 | Zn^[2+] | Zn | 2 | ✓ | [Zn+2] | InChI=1S/Zn/q+2 | beta_totN_122 | ligand_totN_1169 | vlm_totN_4095 |
| metal_209 | Zr^[4+] | Zr | 4 | ✓ | [Zr+4] | InChI=1S/Zr/q+4 | beta_totN_17 | ligand_totN_20 | vlm_totN_80 |
| metal_210 | W_[2]O_[4]^[2+] | W | 2 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_211 | Ph_[3]Sb^[2+] | Ph3Sb | 2 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_212 | He | He | 0 | ✓ | [He] | InChI=1S/He | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_213 | O | O | 0 | ✓ | [O] | InChI=1S/O | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_214 | F | F | 0 | ✓ | [F] | InChI=1S/F | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_215 | Ne | Ne | 0 | ✓ | [Ne] | InChI=1S/Ne | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_216 | S | S | 0 | ✓ | [S] | InChI=1S/S | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_217 | Cl | Cl | 0 | ✓ | [Cl] | InChI=1S/Cl | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_218 | Ar | Ar | 0 | ✓ | [Ar] | InChI=1S/Ar | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_219 | Br | Br | 0 | ✓ | [Br] | InChI=1S/Br | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_220 | Kr | Kr | 0 | ✓ | [Kr] | InChI=1S/Kr | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_221 | I | I | 0 | ✓ | [I] | InChI=1S/I | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_222 | Xe | Xe | 0 | ✓ | [Xe] | InChI=1S/Xe | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_223 | Rn | Rn | 0 | ✓ | [Rn] | InChI=1S/Rn | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_224 | Fr^[+] | Fr | 1 | ✓ | [Fr+] | InChI=1S/Fr/q+1 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_225 | Rf | Rf | 0 | ✓ | [Rf] | InChI=1S/Rf | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_226 | Db | Db | 0 | ✓ | [Db] | InChI=1S/Db | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_227 | Sg | Sg | 0 | ✓ | [Sg] | InChI=1S/Sg | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_228 | Bh | Bh | 0 | ✓ | [Bh] | InChI=1S/Bh | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_229 | Hs | Hs | 0 | ✓ | [Hs] | InChI=1S/Hs | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_230 | Mt | Mt | 0 | ✓ | [Mt] | InChI=1S/Mt | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_231 | Lr | Lr | 0 | ✓ | [Lr] | InChI=1S/Lr | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |

---

### Step 14: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_61"
}
```

[summary]
[CATALOG]
## build_system_catalog — 20 pair(s), 113 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_194 | [M] + [HL]^2 <=> [M(HL)2] |  |
| beta_def_204 | [MHL2] + [H] <=> [M(HL)2] |  |
| beta_def_207 | [MHL3] + [H] <=> [M(HL)2L] |  |
| beta_def_208 | [M] + [HL]^3 <=> [M(HL)3] |  |
| beta_def_213 | [M(HL)2L] + [H] <=> [M(HL)3] |  |
| beta_def_214 | [MH2L3] + [H] <=> [M(HL)3] |  |
| beta_def_238 | [M(OH)2L] + [H] <=> [M(OH)L] + [H2O] |  |
| beta_def_263 | [M(OH)3L] + [H] <=> [M(OH)2L] + [H2O] |  |
| beta_def_351 | [(M2O3)0.5(s,alpha)] + [H2O]^1.5 <=> [M] + [OH]^3 | solid |
| beta_def_352 | [ML3(s)] <=> [M] + [L]^3 | solid |
| beta_def_357 | [MOOH(s,alpha)] + [H2O] <=> [M] + [OH]^3 | solid |
| beta_def_423 | [ML]^2 + [H2O]^2 <=> [M2(OH)2L2] + [H]^2 |  |
| beta_def_424 | [M]^2 + [L]^2 + [H2O]^2 <=> [M2(OH)2L2] + [H]^2 |  |
| beta_def_427 | [M(OH)L]^2 <=> [M2(OH)2L2] |  |
| beta_def_502 | [M]^2 + [L] <=> [M2L] |  |
| beta_def_519 | [M]^2 + [L]^2 <=> [M2L2] |  |
| beta_def_585 | [M]^2 + [L]^3 + [H2O] <=> [M2(OH)L3] + [H] |  |
| beta_def_597 | [M]^3 + [L]^6 + [H2O]^2 <=> [M3(OH)2L6] + [H]^2 |  |
| beta_def_601 | [M]^3 + [L]^2 + [H2O]^3 <=> [M3(OH)3L2] + [H]^3 |  |
| beta_def_649 | [M]^3 + [L]^4 <=> [M3L4] |  |
| beta_def_708 | [M]^7 + [L]^6 + [H2O]^9 <=> [M7(OH)9L6] + [H]^9 |  |
| beta_def_748 | [ML3] + [H]^2 <=> [MH2L3] |  |
| beta_def_779 | [M] + [HL] <=> [MHL] |  |
| beta_def_788 | [ML] + [H] <=> [MHL] |  |
| beta_def_792 | [ML2] + [H] <=> [MHL2] |  |
| beta_def_803 | [ML3] + [H] <=> [MHL3] |  |
| beta_def_812 | [M] + [L] <=> [ML] |  |
| beta_def_821 | [M] + [HL] <=> [ML] + [H] |  |
| beta_def_823 | [M] + [H2L] <=> [ML] + [H]^2 |  |
| beta_def_840 | [M] + [L]^2 <=> [ML2] |  |
| beta_def_846 | [ML] + [HL] <=> [ML2] + [H] |  |
| beta_def_853 | [ML] + [H2L] <=> [ML2] + [H]^2 |  |
| beta_def_864 | [M(OH)2L2] + [H]^2 <=> [ML2] + [H2O]^2 |  |
| beta_def_872 | [M] + [L]^3 <=> [ML3] |  |
| beta_def_873 | [ML2] + [HL] <=> [ML3] + [H] |  |
| beta_def_876 | [ML2] + [H2L] <=> [ML3] + [H]^2 |  |
| beta_def_892 | [M(OH)L3] + [H] <=> [ML3] + [H2O] |  |
| beta_def_894 | [M] + [L]^4 <=> [ML4] |  |
| beta_def_903 | [M] + [L]^5 <=> [ML5] |  |
| beta_def_966 | [M(OH)L] + [H] <=> [ML] + [H2O] |  |
| beta_def_981 | [ML] + [OH] <=> [M(OH)L] |  |
| beta_def_984 | [M(OH)L2] + [H] <=> [ML2] + [H2O] |  |

*(all species aqueous unless noted)*

**1. Fe^[3+] + Hydrogen thiocyanate (Thiocyanic acid)** (metal_61 + ligand_10092) — ligand_def_HxL: HL | 39 ent, 5 sp, 39 vlms (vlm_172282…vlm_172320)
   - species: beta_def_812(21) beta_def_840(8) beta_def_872(5) beta_def_894(1) beta_def_981(4)
   - eq:13 nets T:19~30°C I:-0.15~5.15M max 4n/6e
**2. Fe^[3+] + Hydroxide ion** (metal_61 + ligand_10076) — ligand_def_HxL: *** | 38 ent, 8 sp, 38 vlms (vlm_170791…vlm_170828)
   - species: beta_def_351(1) beta_def_352(2) beta_def_357(2) beta_def_519(10) beta_def_649(5) beta_def_812(11) beta_def_840(6) beta_def_894(1)
   - eq:8 nets T:19~30°C I:-0.15~3.15M max 8n/28e
**3. Fe^[3+] + Hydrogen azide (Hydrazoic acid)** (metal_61 + ligand_10106) — ligand_def_HxL: HL | 22 ent, 5 sp, 22 vlms (vlm_173624…vlm_173645)
   - species: beta_def_812(6) beta_def_840(4) beta_def_872(4) beta_def_894(4) beta_def_903(4)
   - eq:4 nets T:19~30°C I:-0.15~3.15M max 5n/10e
**4. Fe^[3+] + 1,2-Dihydroxybenzene-3,5-disulfonic acid (Tiron)** (metal_61 + ligand_9358) — ligand_def_HxL: H4L | 16 ent, 4 sp, 16 vlms (vlm_162088…vlm_162103)
   - species: beta_def_788(4) beta_def_823(4) beta_def_853(4) beta_def_876(4)
   - eq:4 nets T:15~30°C I:-0.05~1.15M max 4n/6e
**5. Fe^[3+] + Ethanoic acid (Acetic acid)** (metal_61 + ligand_8465) — ligand_def_HxL: HL | 16 ent, 5 sp, 16 vlms (vlm_144783…vlm_144798)
   - species: beta_def_597(5) beta_def_601(1) beta_def_708(1) beta_def_812(6) beta_def_840(3)
   - eq:5 nets T:15~30°C I:-0.05~3.15M max 5n/10e
**6. Fe^[3+] + Nitrilotriacetic acid (NTA)** (metal_61 + ligand_6165) — ligand_def_HxL: H3L | 16 ent, 8 sp, 16 vlms (vlm_105553…vlm_105568)
   - species: beta_def_238(2) beta_def_263(1) beta_def_423(1) beta_def_427(1) beta_def_788(1) beta_def_812(4) beta_def_840(2) beta_def_966(4)
   - eq:5 nets T:15~30°C I:-0.05~1.15M max 5n/8e
**7. Fe^[3+] + 2-Hydroxybenzoic acid (Salicylic acid)** (metal_61 + ligand_9257) — ligand_def_HxL: H2L | 15 ent, 3 sp, 15 vlms (vlm_160398…vlm_160412)
   - species: beta_def_779(1) beta_def_821(11) beta_def_846(3)
   - eq:7 nets T:15~30°C I:-0.15~3.15M max 3n/3e
**8. Fe^[3+] + Propanedioic acid (Malonic acid)** (metal_61 + ligand_8873) — ligand_def_HxL: H2L | 14 ent, 3 sp, 14 vlms (vlm_152337…vlm_152350)
   - species: beta_def_812(5) beta_def_840(5) beta_def_872(4)
   - eq:3 nets T:19~30°C I:-0.05~1.15M max 3n/3e
**9. Fe^[3+] + trans-1,2-Cyclohexylenedinitrilotetraacetic acid (CDTA)** (metal_61 + ligand_6301) — ligand_def_HxL: H4L | 14 ent, 4 sp, 14 vlms (vlm_109793…vlm_109806)
   - species: beta_def_423(3) beta_def_427(3) beta_def_812(4) beta_def_966(4)
   - eq:3 nets T:15~30°C I:-0.05~1.15M max 3n/3e
**10. Fe^[3+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_61 + ligand_6277) — ligand_def_HxL: H4L | 14 ent, 4 sp, 14 vlms (vlm_108639…vlm_108652)
   - species: beta_def_427(3) beta_def_788(3) beta_def_812(4) beta_def_966(4)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 3n/3e
**11. Fe^[3+] + Chloride ion** (metal_61 + ligand_10163) — ligand_def_HxL: *** | 13 ent, 2 sp, 13 vlms (vlm_177390…vlm_177402)
   - species: beta_def_812(11) beta_def_840(2)
   - eq:7 nets T:19~30°C I:-0.15~4.15M max 2n/1e
**12. Fe^[3+] + Hydrogen fluoride (Hydrofluoric acid)** (metal_61 + ligand_10162) — ligand_def_HxL: HL | 13 ent, 3 sp, 13 vlms (vlm_176996…vlm_177008)
   - species: beta_def_812(5) beta_def_840(4) beta_def_872(4)
   - eq:3 nets T:19~30°C I:-0.05~1.15M max 3n/3e
**13. Fe^[3+] + 4-Amino-2-hydroxybenzoic acid (p-Aminosalicylic acid)** (metal_61 + ligand_9297) — ligand_def_HxL: H2L | 13 ent, 4 sp, 13 vlms (vlm_161165…vlm_161177)
   - species: beta_def_779(6) beta_def_821(3) beta_def_846(2) beta_def_873(2)
   - eq:4 nets T:19~30°C I:-0.05~3.15M max 4n/6e
**14. Fe^[3+] + 8-Hydroxyquinoline (8-Quinolinol)(Oxine)** (metal_61 + ligand_8126) — ligand_def_HxL: HL | 13 ent, 4 sp, 13 vlms (vlm_137976…vlm_137988)
   - species: beta_def_352(1) beta_def_812(4) beta_def_840(4) beta_def_872(4)
   - eq:4 nets T:19~30°C I:-0.15~1.15M max 4n/6e
**15. Fe^[3+] + DL-2-Amino-3-hydroxybutanohydroxamic acid (Threoninehydroxamic acid)** (metal_61 + ligand_6995) — ligand_def_HxL: HL | 12 ent, 12 sp, 12 vlms (vlm_121724…vlm_121735)
   - species: beta_def_194(1) beta_def_204(1) beta_def_207(1) beta_def_208(1) beta_def_213(1) beta_def_424(1) beta_def_779(1) beta_def_792(1) beta_def_803(1) beta_def_840(1) beta_def_872(1) beta_def_892(1)
   - eq:1 nets T:16.5~31.5°C I:0.275~0.725M max 12n/41e
**16. Fe^[3+] + Ethanedioic acid (Oxalic acid)** (metal_61 + ligand_8872) — ligand_def_HxL: H2L | 11 ent, 3 sp, 11 vlms (vlm_151793…vlm_151803)
   - species: beta_def_812(5) beta_def_840(3) beta_def_872(3)
   - eq:3 nets T:16.5~31.5°C I:0.275~3.225M max 3n/3e
**17. Fe^[3+] + Glycylglycylglycinehydroxamic acid** (metal_61 + ligand_7000) — ligand_def_HxL: HL | 11 ent, 11 sp, 11 vlms (vlm_121837…vlm_121847)
   - species: beta_def_194(1) beta_def_204(1) beta_def_208(1) beta_def_214(1) beta_def_502(1) beta_def_748(1) beta_def_792(1) beta_def_812(1) beta_def_840(1) beta_def_864(1) beta_def_872(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 11n/30e
**18. Fe^[3+] + DL-2-Amino-3-hydroxypropanohydroxamic acid (Serinehydroxamic acid)** (metal_61 + ligand_6994) — ligand_def_HxL: HL | 11 ent, 11 sp, 11 vlms (vlm_121699…vlm_121709)
   - species: beta_def_194(1) beta_def_204(1) beta_def_207(1) beta_def_208(1) beta_def_213(1) beta_def_424(1) beta_def_779(1) beta_def_792(1) beta_def_803(1) beta_def_840(1) beta_def_872(1)
   - eq:1 nets T:16.5~31.5°C I:0.275~0.725M max 11n/34e
**19. Fe^[3+] + DL-2-Aminopentanohydroxamic acid (Norvalinehydroxamic acid)** (metal_61 + ligand_6985) — ligand_def_HxL: HL | 11 ent, 11 sp, 11 vlms (vlm_121560…vlm_121570)
   - species: beta_def_194(1) beta_def_207(1) beta_def_424(1) beta_def_585(1) beta_def_779(1) beta_def_792(1) beta_def_803(1) beta_def_840(1) beta_def_872(1) beta_def_892(1) beta_def_984(1)
   - eq:1 nets T:16.5~31.5°C I:0.275~0.725M max 11n/39e
**20. Fe^[3+] + Acetohydroxamic acid** (metal_61 + ligand_9873) — ligand_def_HxL: HL | 10 ent, 3 sp, 10 vlms (vlm_168447…vlm_168456)
   - species: beta_def_812(6) beta_def_840(2) beta_def_872(2)
   - eq:4 nets T:15~30°C I:-0.05~2.15M max 3n/3e

---
