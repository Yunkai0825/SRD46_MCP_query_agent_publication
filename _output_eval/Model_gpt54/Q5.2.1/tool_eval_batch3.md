# Q5.2.1 — Tool Results (batch 3)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Uranium(VI), Uranyl",
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
  "name": "18-crown-6, 15-crown-5, 12-crown-4, dibenzo-18-crown-6, benzo-15-crown-5, dicyclohexano-18-crown-6, 21-crown-7, 24-crown-8",
  "limit": 20
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

### Step 5: `search_ligands`
**Args:**
```json
{
  "name": "crown, 18-crown, 15-crown, 12-crown, dibenzo, benzo, cyclohexano",
  "limit": 50
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
  "exclude": "Au, B, Cu, Eu, Lu, Pu, Ru",
  "limit": 50
}
```

[summary]
## search_metals — 50 result(s)

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

---

### Step 9: `search_metals`
**Args:**
```json
{
  "exclude": "Ac, Ag, Al, Am, As, At, Au, B, Ba, Be, Bi, Bk, C, Ca, Cd, Ce, Cf, Cl, Cm, Co, Cr, Cs, Cu, Dy, E",
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

### Step 10: `search_metals`
**Args:**
```json
{
  "symbol": "U",
  "exclude": "Ac,Ag,Al,Am,As,At,Au,B,Ba,Be,Bi,Bk,C,Ca,Cd,Ce,Cf,Cl,Cm,Co,Cr,Cs,Cu,Dy,E,Er,Es,Eu,Fe,Fm,Ga,Gd,Ge,H,Hf,Hg,Ho,In,Ir,K,La,Li,Lu,M,Mg,Mn,Mo",
  "limit": 50
}
```

[summary]
## search_metals — 26 result(s)

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
| metal_165 | Ru^[4+] | Ru | 4 | ✓ | [Ru+4] | InChI=1S/Ru/q+4 | beta_totN_1 | ligand_totN_1 | vlm_totN_6 |
| metal_166 | Ru^[6+] | Ru | 6 | ✓ | [Ru+6] | InChI=1S/Ru/q+6 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_193 | U^[4+] | U | 4 | ✓ | [U+4] | InChI=1S/U/q+4 | beta_totN_13 | ligand_totN_18 | vlm_totN_102 |
| metal_194 | U^[3+] | U | 3 | ✓ | [U+3] | InChI=1S/U/q+3 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_195 | UO_[2]^[2+] | U | 2 |  | *** | *** | beta_totN_75 | ligand_totN_163 | vlm_totN_748 |
| metal_196 | UO_[2]^[+] | U | 1 |  | *** | *** | beta_totN_1 | ligand_totN_1 | vlm_totN_1 |

---

### Step 11: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_195"
}
```

[summary]
[CATALOG]
## build_system_catalog — 20 pair(s), 95 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_194 | [M] + [HL]^2 <=> [M(HL)2] |  |
| beta_def_204 | [MHL2] + [H] <=> [M(HL)2] |  |
| beta_def_258 | [M] + [L]^4 + [H2O]^2 <=> [M(OH)2L4] + [H]^2 |  |
| beta_def_298 | [MHL(s)] <=> [M] + [HL] | solid |
| beta_def_311 | [ML(s)] <=> [M] + [L] | solid |
| beta_def_346 | * |  |
| beta_def_365 | [M]^11 + [L]^6 + [H2O]^12 <=> [M11(OH)12L6] + [H]^12 |  |
| beta_def_436 | [M]^2 + [L] + [H2O]^3 <=> [M2(OH)3L] + [H]^3 |  |
| beta_def_440 | [M]^2 + [L]^3 + [H2O]^3 <=> [M2(OH)3L3] + [H]^3 |  |
| beta_def_445 | [M]^2 + [L] + [H2O]^5 <=> [M2(OH)5L] + [H]^5 |  |
| beta_def_502 | [M]^2 + [L] <=> [M2L] |  |
| beta_def_519 | [M]^2 + [L]^2 <=> [M2L2] |  |
| beta_def_536 | [M2L] + [L] <=> [M2L2] |  |
| beta_def_570 | [M2(OH)L] + [H] <=> [M2L] + [H2O] |  |
| beta_def_598 | [M]^3 + [L] + [H2O]^3 <=> [M3(OH)3L] + [H]^3 |  |
| beta_def_624 | [M3L2(s)] <=> [M]^3 + [L]^2 | solid |
| beta_def_649 | [M]^3 + [L]^4 <=> [M3L4] |  |
| beta_def_652 | [M]^3 + [L]^5 <=> [M3L5] |  |
| beta_def_653 | [M]^3 + [L]^6 <=> [M3L6] |  |
| beta_def_662 | [M]^4 + [L]^2 + [H2O]^4 <=> [M4(OH)4L2] + [H]^4 |  |
| beta_def_671 | * |  |
| beta_def_672 | * |  |
| beta_def_676 | [M]^4 + [L]^6 <=> [M4L6] |  |
| beta_def_677 | [M]^4 + [L]^7 <=> [M4L7] |  |
| beta_def_699 | [M]^6 + [L]^3 + [H2O]^4 <=> [M6(OH)4L3] + [H]^4 |  |
| beta_def_701 | * |  |
| beta_def_732 | [M] + [H2L] <=> [MH2L] |  |
| beta_def_751 | [MH2L] + [H] <=> [MH3L] |  |
| beta_def_779 | [M] + [HL] <=> [MHL] |  |
| beta_def_788 | [ML] + [H] <=> [MHL] |  |
| beta_def_792 | [ML2] + [H] <=> [MHL2] |  |
| beta_def_801 | [ML] + [HL] <=> [MHL2] |  |
| beta_def_806 | [ML3] + [H] <=> [MHL3] |  |
| beta_def_812 | [M] + [L] <=> [ML] |  |
| beta_def_821 | [M] + [HL] <=> [ML] + [H] |  |
| beta_def_834 | [M(OH)2L] + [H]^2 <=> [ML] + [H2O]^2 |  |
| beta_def_840 | [M] + [L]^2 <=> [ML2] |  |
| beta_def_846 | [ML] + [HL] <=> [ML2] + [H] |  |
| beta_def_872 | [M] + [L]^3 <=> [ML3] |  |
| beta_def_894 | [M] + [L]^4 <=> [ML4] |  |

*(all species aqueous unless noted)*

**1. UO_[2]^[2+] + Hydroxide ion** (metal_195 + ligand_10076) — ligand_def_HxL: *** | 37 ent, 7 sp, 37 vlms (vlm_170604…vlm_170640)
   - species: beta_def_346(1) beta_def_519(9) beta_def_649(7) beta_def_652(8) beta_def_676(4) beta_def_677(1) beta_def_812(7)
   - eq:8 nets T:19~30°C I:-0.15~3.15M max 5n/10e
**2. UO_[2]^[2+] + Hydrogen carbonate (Carbonic acid)** (metal_195 + ligand_10096) — ligand_def_HxL: H2L | 33 ent, 8 sp, 33 vlms (vlm_172802…vlm_172834)
   - species: beta_def_311(3) beta_def_365(1) beta_def_436(2) beta_def_598(1) beta_def_653(7) beta_def_812(5) beta_def_840(6) beta_def_872(8)
   - eq:4 nets T:19~30°C I:-0.15~3.15M max 8n/28e
**3. UO_[2]^[2+] + Hydrogen fluoride (Hydrofluoric acid)** (metal_195 + ligand_10162) — ligand_def_HxL: HL | 23 ent, 4 sp, 23 vlms (vlm_176904…vlm_176926)
   - species: beta_def_812(8) beta_def_840(5) beta_def_872(5) beta_def_894(5)
   - eq:6 nets T:19~30°C I:-0.05~4.15M max 4n/6e
**4. UO_[2]^[2+] + Ethanedioic acid (Oxalic acid)** (metal_195 + ligand_8872) — ligand_def_HxL: H2L | 21 ent, 5 sp, 21 vlms (vlm_151717…vlm_151737)
   - species: beta_def_194(3) beta_def_779(4) beta_def_812(7) beta_def_840(6) beta_def_872(1)
   - eq:7 nets T:15~30°C I:-0.05~9.15M max 4n/6e
**5. UO_[2]^[2+] + Hydrogen sulfate ion (Sulfuric acid)** (metal_195 + ligand_10148) — ligand_def_HxL: HL | 16 ent, 2 sp, 16 vlms (vlm_175964…vlm_175979)
   - species: beta_def_812(9) beta_def_840(7)
   - eq:5 nets T:19~30°C I:-0.15~3.15M max 2n/1e
**6. UO_[2]^[2+] + Hydrogen thiocyanate (Thiocyanic acid)** (metal_195 + ligand_10092) — ligand_def_HxL: HL | 16 ent, 3 sp, 16 vlms (vlm_172191…vlm_172206)
   - species: beta_def_812(7) beta_def_840(5) beta_def_872(4)
   - eq:5 nets T:15~30°C I:-0.05~4.15M max 3n/3e
**7. UO_[2]^[2+] + Iminodiacetic acid (IDA)** (metal_195 + ligand_6127) — ligand_def_HxL: H2L | 16 ent, 4 sp, 16 vlms (vlm_104293…vlm_104308)
   - species: beta_def_194(4) beta_def_204(3) beta_def_779(4) beta_def_812(5)
   - eq:4 nets T:19~30°C I:-0.05~3.15M max 4n/4e
**8. UO_[2]^[2+] + Hydrogen phosphate (Phosphoric acid)** (metal_195 + ligand_10113) — ligand_def_HxL: H3L | 14 ent, 6 sp, 14 vlms (vlm_174430…vlm_174443)
   - species: beta_def_298(3) beta_def_624(3) beta_def_732(2) beta_def_751(2) beta_def_779(2) beta_def_812(2)
   - eq:3 nets T:19~30°C I:-0.05~1.15M max 6n/11e
**9. UO_[2]^[2+] + Ethanoic acid (Acetic acid)** (metal_195 + ligand_8465) — ligand_def_HxL: HL | 14 ent, 3 sp, 14 vlms (vlm_144680…vlm_144693)
   - species: beta_def_812(6) beta_def_840(4) beta_def_872(4)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 3n/3e
**10. UO_[2]^[2+] + Ethylenebis(oxyacetic acid)** (metal_195 + ligand_8986) — ligand_def_HxL: H2L | 12 ent, 4 sp, 12 vlms (vlm_156003…vlm_156014)
   - species: beta_def_788(3) beta_def_792(3) beta_def_812(3) beta_def_840(3)
   - eq:1 nets T:16.5~31.5°C I:0.775~1.225M max 4n/4e
**11. UO_[2]^[2+] + Chloroacetic acid** (metal_195 + ligand_8558) — ligand_def_HxL: HL | 12 ent, 3 sp, 12 vlms (vlm_146280…vlm_146291)
   - species: beta_def_812(6) beta_def_840(3) beta_def_872(3)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 3n/3e
**12. UO_[2]^[2+] + Butanedioic acid (Succinic acid)** (metal_195 + ligand_8907) — ligand_def_HxL: H2L | 11 ent, 3 sp, 11 vlms (vlm_153426…vlm_153436)
   - species: beta_def_779(4) beta_def_801(3) beta_def_812(4)
   - eq:2 nets T:16.5~31.5°C I:0.275~1.225M max 3n/3e
**13. UO_[2]^[2+] + Hexamethylenedinitrilotetraacetic acid** (metal_195 + ligand_6315) — ligand_def_HxL: H4L | 11 ent, 6 sp, 11 vlms (vlm_110952…vlm_110962)
   - species: beta_def_502(2) beta_def_536(2) beta_def_570(2) beta_def_671(1) beta_def_672(2) beta_def_779(2)
   - eq:5 nets T:19~30°C I:-0.05~1.15M max 4n/4e
**14. UO_[2]^[2+] + Trimethylenedinitrilotetraacetic acid (TMDTA)** (metal_195 + ligand_6311) — ligand_def_HxL: H4L | 11 ent, 6 sp, 11 vlms (vlm_110507…vlm_110517)
   - species: beta_def_502(2) beta_def_536(2) beta_def_570(2) beta_def_672(2) beta_def_701(1) beta_def_779(2)
   - eq:5 nets T:19~30°C I:-0.05~1.15M max 4n/4e
**15. UO_[2]^[2+] + 3-Hydroxy-2-methyl-4-pyrone (Maltol)** (metal_195 + ligand_9586) — ligand_def_HxL: HL | 10 ent, 10 sp, 10 vlms (vlm_166190…vlm_166199)
   - species: beta_def_258(1) beta_def_440(1) beta_def_445(1) beta_def_788(1) beta_def_792(1) beta_def_806(1) beta_def_812(1) beta_def_834(1) beta_def_840(1) beta_def_872(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 10n/37e
**16. UO_[2]^[2+] + 2-Hydroxybenzoic acid (Salicylic acid)** (metal_195 + ligand_9257) — ligand_def_HxL: H2L | 10 ent, 3 sp, 10 vlms (vlm_160360…vlm_160369)
   - species: beta_def_779(1) beta_def_821(6) beta_def_846(3)
   - eq:6 nets T:15~35°C I:-0.15~0.85M max 3n/3e
**17. UO_[2]^[2+] + Oxydiacetic acid (Diglycolic acid)** (metal_195 + ligand_8974) — ligand_def_HxL: H2L | 10 ent, 3 sp, 10 vlms (vlm_155654…vlm_155663)
   - species: beta_def_792(3) beta_def_812(4) beta_def_840(3)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 3n/2e
**18. UO_[2]^[2+] + Hydroxyacetic acid (Glycolic acid)** (metal_195 + ligand_8640) — ligand_def_HxL: HL | 10 ent, 3 sp, 10 vlms (vlm_147366…vlm_147375)
   - species: beta_def_812(4) beta_def_840(3) beta_def_872(3)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 3n/3e
**19. UO_[2]^[2+] + Tetramethylenedinitrilotetraacetic acid** (metal_195 + ligand_6313) — ligand_def_HxL: H4L | 10 ent, 6 sp, 10 vlms (vlm_110715…vlm_110724)
   - species: beta_def_502(2) beta_def_536(1) beta_def_570(2) beta_def_671(1) beta_def_672(2) beta_def_779(2)
   - eq:5 nets T:19~30°C I:-0.05~1.15M max 4n/4e
**20. UO_[2]^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_195 + ligand_6277) — ligand_def_HxL: H4L | 10 ent, 6 sp, 10 vlms (vlm_108542…vlm_108551)
   - species: beta_def_502(2) beta_def_536(1) beta_def_570(1) beta_def_662(1) beta_def_699(1) beta_def_779(4)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 6n/13e

---

### Step 13: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_195 AND (c.ligand_name_SRD LIKE '%crown%' OR c.ligand_name_SRD LIKE '%18-crown-6%' OR c.ligand_name_SRD LIKE '%15-crown-5%' OR c.ligand_name_SRD LIKE '%12-crown-4%' OR c.ligand_name_SRD LIKE '%benzo-15-crown-5%' OR c.ligand_name_SRD LIKE '%dibenzo-18-crown-6%' OR c.ligand_name_SRD LIKE '%dicyclohexano-18-crown-6%' OR c.ligand_name_SRD LIKE '%hexaoxacyclooctadecane%' OR c.ligand_name_SRD LIKE '%pentaoxacyclopentadecane%' OR c.ligand_name_SRD LIKE '%tetraoxacyclododecane%' OR c.ligand_class_name LIKE '%crown%' OR c.ligand_class_name LIKE '%macrocyclic polyether%' OR c.ligand_class_name LIKE '%oxa%cyclo%'))",
  "limit": 50
}
```

[summary]
## search_stability

*(no results)*

---

### Step 14: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id = metal_195 AND (c.ligand_name LIKE '%crown%' OR c.ligand_name LIKE '%18-crown-6%' OR c.ligand_name LIKE '%15-crown-5%' OR c.ligand_name LIKE '%12-crown-4%' OR c.ligand_name LIKE '%benzo-15-crown-5%' OR c.ligand_name LIKE '%dibenzo-18-crown-6%' OR c.ligand_name LIKE '%dicyclohexano-18-crown-6%' OR c.ligand_name LIKE '%hexaoxacyclooctadecane%' OR c.ligand_name LIKE '%pentaoxacyclopentadecane%' OR c.ligand_name LIKE '%tetraoxacyclododecane%'))",
  "limit": 50
}
```

[summary]
## search_networks

*(no results)*

---

### Step 15: `search_citations`
**Args:**
```json
{
  "where": "(la.citation LIKE '%uranyl%crow%' OR la.citation LIKE '%UO2%crow%' OR la.citation LIKE '%uranium(VI)%crow%' OR la.citation LIKE '%macrocyclic polyether%uranyl%')",
  "limit": 20
}
```

[summary]
## search_citations

*(no results)*

---
