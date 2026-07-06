# Q4.6 — Tool Results (batch 4)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Mn(II), Fe(II), Co(II), Ni(II), Cu(II), Zn(II)",
  "limit": 20
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
  "name": "EDTA, NTA, citrate, oxalate, acetate, glycine, ammonia, ethylenediamine, 2,2'-bipyridine, 1,10-phenanthroline, imidazole, histidine, salicylate",
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
  "symbol": "Mn, Fe, Co, Ni, Cu, Zn",
  "limit": 20
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
  "name": "ethylenediaminetetraacetic acid, nitrilotriacetic acid, citric acid, oxalic acid, acetic acid, glycine, ammonia, ethylenediamine, 2,2'-bipyridine, 1,10-phenanthroline, imidazole, histidine, salicylic acid",
  "limit": 100
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 7: `build_system_catalog`
**Args:**
```json
{}
```

[summary]
[CATALOG]
## build_system_catalog

**Error:** Provide at least one of metal_id, ligand_id, or beta_definition_id.

---

### Step 8: `search_metals`
**Args:**
```json
{
  "limit": 20
}
```

[summary]
## search_metals — 20 result(s)

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

---

### Step 9: `search_metals`
**Args:**
```json
{
  "exclude": "metal_1, metal_2, metal_3, metal_4, metal_5, metal_6, metal_7, metal_8, metal_9, metal_10, metal_11, metal_12, metal_13, metal_14, metal_15, metal_16, metal_17, metal_18, metal_19, metal_20",
  "limit": 100
}
```

[summary]
## search_metals — 100 result(s)

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

---

### Step 10: `search_ligands`
**Args:**
```json
{
  "limit": 50
}
```

[summary]
## search_ligands — 50 result(s)

**stats:** 5750 SQL matches · showing 50 · limit 50

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5760 | Aminoacetic acid (Glycine) | HL | Amino Acids | 428 | `NCC(=O)O` | (-inf, H2L, 2.33, HL, 9.57, L, +inf) |
| ligand_5761 | L-2-Aminopropanoic acid (Alanine) | HL | Amino Acids | 159 | `C[C@H](N)C(=O)O` | (-inf, H2L, 2.33, HL, 9.71, L, +inf) |
| ligand_5762 | DL-2-Aminobutanoic acid | HL | Amino Acids | 53 | `CCC(N)C(=O)O` | (-inf, H2L, 2.3, HL, 9.63, L, +inf) |
| ligand_5763 | DL-2-Aminopentanoic acid (Norvaline) | HL | Amino Acids | 35 | `CCC[C@H](N)C(=O)O` | (-inf, H2L, 2.31, HL, 9.65, L, +inf) |
| ligand_5764 | DL-2-Aminohexanoic acid (Norleucine) | HL | Amino Acids | 33 | `CCCC[C@H](N)C(=O)O` | (-inf, H2L, 2.31, HL, 9.68, L, +inf) |
| ligand_5765 | L-2-Amino-3-methylbutanoic acid (Valine) | HL | Amino Acids | 81 | `CC(C)[C@H](N)C(=O)O` | (-inf, H2L, 2.27, HL, 9.52, L, +inf) |
| ligand_5766 | L-2-Amino-4-methylpentanoic acid (Leucine) | HL | Amino Acids | 49 | `CC(C)C[C@H](N)C(=O)O` | (-inf, H2L, 2.32, HL, 9.58, L, +inf) |
| ligand_5767 | L-2-Amino-3-methylpentanoic acid (Isoleucine) | HL | Amino Acids | 51 | `CC[C@H](C)[C@H](N)C(=O)O` | (-inf, H2L, 2.26, HL, 9.6, L, +inf) |
| ligand_5768 | D-allo-2-Amino-3-methylpentan… (D-allo-Isoleucine) | HL | Amino Acids | 16 | `CC[C@H](C)[C@@H](N)C(=O)O` | (-inf, H2L, 2.2, HL, 9.62, L, +inf) |
| ligand_5769 | 2-Amino-2-methylpropanoi… (2-Aminoisobutyric acid) | HL | Amino Acids | 41 | `CC(C)(N)C(=O)O` | (-inf, H2L, 2.34, HL, 10.1, L, +inf) |
| ligand_5770 | DL-2-Amino-4-pentenoic acid | HL | Amino Acids | 18 | `C=CCC(N)C(=O)O` | (-inf, H2L, 2.13, HL, 9.28, L, +inf) |
| ligand_5771 | DL-2-Amino-5-hexenoic acid | HL | Amino Acids | 15 | `C=CCCC(N)C(=O)O` | (-inf, H2L, 2.25, HL, 9.43, L, +inf) |
| ligand_5772 | DL-2-Amino-6-heptenoic acid | HL | Amino Acids | 15 | `C=CCCCC(N)C(=O)O` | (-inf, H2L, 2.34, HL, 9.52, L, +inf) |
| ligand_5773 | 1-Aminocyclopentanecarboxylic acid (Cycloleucine) | HL | Amino Acids | 11 | `NC1(C(=O)O)CCCC1` | (-inf, H2L, 2.4, HL, 10.31, L, +inf) |
| ligand_5774 | 1-Aminocyclohexanecarboxylic acid | HL | Amino Acids | 11 | `NC1(C(=O)O)CCCCC1` | (-inf, H2L, 2.41, HL, 10.13, L, +inf) |
| ligand_5775 | 1-Aminocycloheptanecarboxylic acid | HL | Amino Acids | 11 | `NC1(C(=O)O)CCCCCC1` | (-inf, H2L, 2.59, HL, 10.46, L, +inf) |
| ligand_5776 | DL-Aminophenylacetic acid (Phenylglycine) | HL | Amino Acids | 12 | `NC(C(=O)O)c1ccccc1` | (-inf, H2L, -1.9, HL, 8.92, L, +inf) |
| ligand_5777 | L-2-Amino-3-phenylpropanoic acid (Phenylalanine) | HL | Amino Acids | 138 | `N[C@@H](Cc1ccccc1)C(=O)O` | (-inf, H2L, 2.18, HL, 9.09, L, +inf) |
| ligand_5778 | DL-2-Amino-3-chloropropanoic ac… (3-Chloroalanine) | HL | Amino Acids | 10 | `N[C@@H](CCl)C(=O)O` | (-inf, H2L, 2, HL, 8.18, L, +inf) |
| ligand_5779 | DL-2-Amino-3-chlorobutanoic acid | HL | Amino Acids | 8 | `CC(Cl)C(N)C(=O)O` | (-inf, H2L, -1.5, HL, 8.07, L, +inf) |
| ligand_5780 | DL-2-Amino-3-(2-fluorophenyl)propanoic acid (DL-3… | HL | Amino Acids | 6 | `N[C@@H](Cc1ccccc1F)C(=O)O` | (-inf, H2L, 2.12, HL, 9.01, L, +inf) |
| ligand_5781 | DL-2-Amino-3-(3-fluorophenyl)propanoic acid (DL-3… | HL | Amino Acids | 6 | `N[C@@H](Cc1cccc(F)c1)C(=O)O` | (-inf, H2L, 2.1, HL, 8.98, L, +inf) |
| ligand_5782 | DL-2-Amino-3-(4-fluorophenyl)propanoic acid (DL-3… | HL | Amino Acids | 6 | `N[C@@H](Cc1ccc(F)cc1)C(=O)O` | (-inf, H2L, 2.13, HL, 9.05, L, +inf) |
| ligand_5783 | DL-2-Amino-3-(2-chlorophenyl)propanoic acid (DL-3… | HL | Amino Acids | 2 | `N[C@@H](Cc1ccccc1Cl)C(=O)O` | (-inf, H2L, 2.23, HL, 8.94, L, +inf) |
| ligand_5784 | DL-2-Amino-3-(3-chlorophenyl)propanoic acid (DL-3… | HL | Amino Acids | 2 | `N[C@@H](Cc1cccc(Cl)c1)C(=O)O` | (-inf, H2L, 2.17, HL, 8.91, L, +inf) |
| ligand_5785 | DL-2-Amino-3-(4-chlorophenyl)propanoic acid (DL-3… | HL | Amino Acids | 2 | `N[C@@H](Cc1ccc(Cl)cc1)C(=O)O` | (-inf, H2L, 2.08, HL, 8.96, L, +inf) |
| ligand_5786 | DL-Amino-4-sulfophenylacet… (4-Sulfophenylglycine) | H2L | Amino Acids | 12 | `NC(C(=O)O)c1ccc(S(=O)(=O)O)cc1` | (-inf, H2L, -1.8, HL, 8.66, L, +inf) |
| ligand_5787 | DL-2-Amino-4-sulfobutanoic acid (Homocysteic acid) | H2L | Amino Acids | 4 | `N[C@@H](CCS(=O)(=O)O)C(=O)O` | (-inf, H2L, 2.11, HL, 8.93, L, +inf) |
| ligand_5788 | 3-Aminopropanoic acid (beta-Alanine) | HL | Amino Acids | 111 | `NCCC(=O)O` | (-inf, H2L, 3.51, HL, 10.08, L, +inf) |
| ligand_5789 | DL-3-Aminobutanoic acid | HL | Amino Acids | 33 | `CC(N)CC(=O)O` | (-inf, H2L, 3.43, HL, 10.05, L, +inf) |
| ligand_5790 | cis-2-Aminocyclopentane-1-carboxylic acid | HL | Amino Acids | 6 | `N[C@H]1CCC[C@H]1C(=O)O` | (-inf, H2L, 3.54, HL, 10.1, L, +inf) |
| ligand_5791 | trans-2-Aminocyclopentane-1-carboxylic acid | HL | Amino Acids | 3 | `N[C@@H]1CCC[C@H]1C(=O)O` | (-inf, H2L, 3.75, HL, 9.91, L, +inf) |
| ligand_5792 | cis-2-Aminocyclohexane-1-carboxylic acid | HL | Amino Acids | 6 | `N[C@H]1CCCC[C@H]1C(=O)O` | (-inf, H2L, 3.49, HL, 10.54, L, +inf) |
| ligand_5793 | trans-2-Aminocyclohexane-1-carboxylic acid | HL | Amino Acids | 6 | `N[C@@H]1CCCC[C@H]1C(=O)O` | (-inf, H2L, 3.47, HL, 10.01, L, +inf) |
| ligand_5794 | cis-2-Amino-4-cyclohexene-1-carboxylic acid | HL | Amino Acids | 6 | `N[C@H]1CC=CC[C@H]1C(=O)O` | (-inf, H2L, 3.29, HL, 10.2, L, +inf) |
| ligand_5795 | trans-2-Amino-4-cyclohexene-1-carboxylic acid | HL | Amino Acids | 5 | `N[C@@H]1CC=CC[C@H]1C(=O)O` | (-inf, H2L, 3.33, HL, 10.29, L, +inf) |
| ligand_5796 | DL-3-Amino-3-phenylpropanoi… (Phenyl-beta-Alanine) | HL | Amino Acids | 2 | `NC(CC(=O)O)c1ccccc1` | (-inf, H2L, 3.4, HL, 9, L, +inf) |
| ligand_5797 | 4-Aminobutanoic acid | HL | Amino Acids | 51 | `NCCCC(=O)O` | (-inf, H2L, 4.02, HL, 10.35, L, +inf) |
| ligand_5798 | 5-Aminopentanoic acid | HL | Amino Acids | 20 | `NCCCCC(=O)O` | (-inf, H2L, 4.27, HL, 10.766, L, +inf) |
| ligand_5799 | 6-Aminohexanoic acid | HL | Amino Acids | 29 | `NCCCCCC(=O)O` | (-inf, H2L, 4.373, HL, 10.804, L, +inf) |
| ligand_5800 | 7-Aminoheptanoic acid | HL | Amino Acids | 3 | `NCCCCCCC(=O)O` | (-inf, H2L, 4.502, HL, +inf) |
| ligand_5801 | Aminopropanedioic acid (Aminomalonic acid) | H2L | Amino Acids | 14 | `NC(C(=O)O)C(=O)O` | (-inf, H3L, -1.8, H2L, 2.94, HL, 9.22, L, +inf) |
| ligand_5802 | L-Aminobutanedioic acid (Aspartic acid) | H2L | Amino Acids | 174 | `N[C@@H](CC(=O)O)C(=O)O` | (-inf, H3L, 1.95, H2L, 3.71, HL, 9.66, L, +inf) |
| ligand_5803 | DL-2-Amino-3-methylbutane… (3-Methylaspartic acid) | H2L | Amino Acids | 6 | `CC(C(=O)O)[C@H](N)C(=O)O` | (-inf, H3L, 1.99, H2L, 3.59, HL, 9.48, L, +inf) |
| ligand_5804 | L-2-Aminopentanedioic acid (Glutamic acid) | H2L | Amino Acids | 94 | `N[C@@H](CCC(=O)O)C(=O)O` | (-inf, H3L, 2.16, H2L, 4.15, HL, 9.58, L, +inf) |
| ligand_5805 | DL-2-Amino-2-methylpentan… (2-Methylglutamic acid) | H2L | Amino Acids | 4 | `C[C@](N)(CCC(=O)O)C(=O)O` | (-inf, H2L, 4.05, HL, 9.72, L, +inf) |
| ligand_5806 | DL-2-Aminohexanedioic acid | H2L | Amino Acids | 1 | `NC(CCCC(=O)O)C(=O)O` | (-inf, HL, 9.73, L, +inf) |
| ligand_5807 | DL-2-Amino-3-hydroxypent… (3-Hydroxyglutamic acid) | H2L | Amino Acids | 8 | `N[C@H](C(=O)O)C(O)CC(=O)O` | (-inf, H3L, 2.09, H2L, 4.08, HL, 9.06, L, +inf) |
| ligand_5808 | (3-Aminopropyl)malonic acid | H2L | Amino Acids | 18 | `NCCCC(C(=O)O)C(=O)O` | (-inf, H3L, 2.52, H2L, 4.86, HL, 10.45, L, +inf) |
| ligand_5809 | L-2-Amino-3-phosphopropanoic acid (Phosphoserine) | H3L | Amino Acids | 52 | `N[C@@H](COP(=O)(O)O)C(=O)O` | (-inf, H4L, -0.7, H3L, 2.14, H2L, 5.7, HL, 9.8, L, +inf) |

### Functional groups across all SQL matches (4054 parseable SMILES)

| group | count | % |
|-------|-------|---|
| aromatic_ring | 1903 | 47% |
| carboxyl | 1693 | 42% |
| hydroxyl | 1430 | 35% |
| primary_amine | 1101 | 27% |
| tertiary_amine | 820 | 20% |
| amide | 756 | 19% |
| secondary_amine | 724 | 18% |
| phenol | 462 | 11% |
| pyridine | 428 | 11% |
| ether | 291 | 7% |
| halide | 268 | 7% |
| thioether | 261 | 6% |
| sulfonate | 203 | 5% |
| phosphonate | 181 | 4% |
| thiol | 119 | 3% |
| imine | 109 | 3% |
| phosphate | 99 | 2% |
| ester | 92 | 2% |
| ketone | 90 | 2% |
| oxime | 48 | 1% |
| aldehyde | 44 | 1% |
| nitrile | 39 | 1% |
| thiazole | 10 | 0% |
| imidazole | 8 | 0% |
| pyrazole | 8 | 0% |
| carboxylate | 1 | 0% |

---

### Step 12: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_name_SRD LIKE 'Ni%' AND s.reaction_type LIKE '%ML%' AND s.solvent_name LIKE '%water%')",
  "order_by": "c.metal_id ASC",
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
  "where": "(c.metal_name_SRD LIKE 'Zn%' AND s.reaction_type LIKE '%ML%' AND s.solvent_name LIKE '%water%')",
  "order_by": "c.metal_id ASC",
  "limit": 20
}
```

[summary]
## search_stability

*(no results)*

---

### Step 14: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_94, metal_62, metal_33, metal_41) AND c.ligand_id = ligand_5760)",
  "order_by": "c.metal_id ASC, s.temperature_c ASC, s.ionic_strength_mol_l ASC",
  "limit": 100
}
```

[summary]
## search_stability — 95 row(s)

### logK — 4 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_33 | Co^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 22 | 4 | 10~40 | 0~1 | *** | 7 |
| metal_41 | Cu^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 18 | 2 | 10~40 | 0~2.5 | *** | 9 |
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 10 | 3 | 10~40 | 0~3 | *** | 7 |
| metal_94 | Mn^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 9 | 2 | 10~40 | 0~0.5 | *** | 6 |

### ΔH — 4 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_33 | Co^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 9 | 3 | 10~40 | 0 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 8 | 2 | 10~40 | 0~0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 3 | 1 | 10~40 | 0 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 3 | 1 | 10~40 | 0 | *** | 0 |

### ΔS — 4 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_33 | Co^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 6 | 3 | 25 | 0~0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 4 | 2 | 25 | 0~0.1 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 2 | 1 | 25 | 0~0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 0 | *** | 0 |

---

### Step 15: `search_ligands`
**Args:**
```json
{
  "ligand_id": "ligand_5760",
  "limit": 5
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5760 | Aminoacetic acid (Glycine) | HL | Amino Acids | 428 | `NCC(=O)O` | (-inf, H2L, 2.33, HL, 9.57, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 1 | 100% |
| primary_amine | 1 | 100% |

---

### Step 16: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_card",
  "group_column": "metal_id",
  "where": "ligand_id = 5760",
  "limit": 20
}
```

[summary]
## db_distribution - ligandmetal_card by metal_id

**total_rows:** 428

| value | count | pct |
|-------|-------|-----|
| 112 | 49 | 11.45% |
| 68 | 48 | 11.21% |
| 208 | 37 | 8.64% |
| 33 | 37 | 8.64% |
| 26 | 32 | 7.48% |
| 41 | 30 | 7.01% |
| 125 | 25 | 5.84% |
| 94 | 14 | 3.27% |
| 62 | 14 | 3.27% |
| 2 | 14 | 3.27% |
| 201 | 13 | 3.04% |
| 25 | 12 | 2.8% |
| 185 | 9 | 2.1% |
| 92 | 9 | 2.1% |
| 71 | 8 | 1.87% |
| 195 | 7 | 1.64% |
| 61 | 6 | 1.4% |
| 58 | 4 | 0.93% |
| 187 | 3 | 0.7% |
| 137 | 3 | 0.7% |

---

### Step 17: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_5760 AND c.metal_id IN (metal_94, metal_62, metal_33, metal_41, 68, 112) AND s.constant_type LIKE '%logK%' AND s.solvent_name LIKE '%water%')",
  "order_by": "c.metal_id ASC, s.temperature_c ASC, s.ionic_strength_mol_l ASC",
  "limit": 200
}
```

[summary]
## search_stability

*(no results)*

---

### Step 18: `inspect_card`
**Args:**
```json
{
  "prefix_id": "metal_68"
}
```

[summary]
## inspect_card — Metal | metal_68

**Name:** H^[+]  
**Symbol:** H | **Charge:** 1  
**SMILES:** `[H+]`  
**InChI:** `InChI=1S/p+1`  
**Flags:** simple-ion  

**Partners:** 4081 ligand(s), 20720 measurement(s) total

| ligand_id | Ligand | # meas |
|-----------|--------|--------|
| ligand_10077 | Hydrogen vanadate (Vanadic acid) | 92 |
| ligand_10113 | Hydrogen phosphate (Phosphoric acid) | 84 |
| ligand_6277 | Ethylenedinitrilotetraacetic acid (EDTA) | 75 |
| ligand_7246 | 1,4,7,10,13,16-Hexaazahexadecane (Pentaethy… (2,2,2,2,2-hex) | 72 |
| ligand_6165 | Nitrilotriacetic acid (NTA) | 72 |
| … | *(showing top 5 of 4081)* | |

### Functional groups across all ligand partners (3910 parseable SMILES)

| group | count | % |
|-------|-------|---|
| aromatic_ring | 1851 | 47% |
| carboxyl | 1646 | 42% |
| hydroxyl | 1390 | 36% |
| primary_amine | 1070 | 27% |
| tertiary_amine | 802 | 21% |
| amide | 738 | 19% |
| secondary_amine | 691 | 18% |
| phenol | 458 | 12% |
| pyridine | 425 | 11% |
| halide | 266 | 7% |
| ether | 262 | 7% |
| thioether | 247 | 6% |
| sulfonate | 193 | 5% |
| phosphonate | 176 | 5% |
| thiol | 111 | 3% |
| imine | 104 | 3% |
| phosphate | 97 | 2% |
| ester | 92 | 2% |
| ketone | 88 | 2% |
| oxime | 48 | 1% |
| aldehyde | 42 | 1% |
| nitrile | 30 | 1% |
| thiazole | 10 | 0% |
| imidazole | 8 | 0% |
| pyrazole | 8 | 0% |
| carboxylate | 1 | 0% |

---

### Step 19: `inspect_card`
**Args:**
```json
{
  "prefix_id": "metal_112"
}
```

[summary]
## inspect_card — Metal | metal_112

**Name:** Ni^[2+]  
**Symbol:** Ni | **Charge:** 2  
**SMILES:** `[Ni+2]`  
**InChI:** `InChI=1S/Ni/q+2`  
**Flags:** simple-ion  

**Partners:** 1369 ligand(s), 5325 measurement(s) total

| ligand_id | Ligand | # meas |
|-----------|--------|--------|
| ligand_10103 | Ammonia | 60 |
| ligand_5760 | Aminoacetic acid (Glycine) | 49 |
| ligand_7029 | Ethylenediamine | 45 |
| ligand_7795 | 1,3-Diazole (Imidazole) | 41 |
| ligand_5889 | DL-2,6-Diamino-5-hydroxyhexanoic acid | 32 |
| … | *(showing top 5 of 1369)* | |

### Functional groups across all ligand partners (1335 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 579 | 43% |
| aromatic_ring | 527 | 39% |
| hydroxyl | 423 | 32% |
| primary_amine | 408 | 31% |
| secondary_amine | 305 | 23% |
| tertiary_amine | 296 | 22% |
| amide | 256 | 19% |
| pyridine | 167 | 13% |
| ether | 127 | 10% |
| thioether | 118 | 9% |
| phenol | 91 | 7% |
| phosphonate | 61 | 5% |
| imine | 45 | 3% |
| phosphate | 44 | 3% |
| sulfonate | 41 | 3% |
| halide | 28 | 2% |
| ketone | 28 | 2% |
| oxime | 28 | 2% |
| thiol | 28 | 2% |
| ester | 16 | 1% |
| nitrile | 10 | 1% |
| thiazole | 9 | 1% |
| aldehyde | 7 | 1% |
| imidazole | 5 | 0% |
| pyrazole | 5 | 0% |

---
