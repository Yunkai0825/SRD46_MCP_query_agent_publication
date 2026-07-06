# Q2.1.6 — Tool Results (batch 5)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Cadmium(II), Lead(II), Mercury(II)",
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
  "name": "Thiocyanate, Thiocyanic acid",
  "limit": 10
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
  "name": "cadmium, lead, mercury",
  "symbol": "Cd, Pb, Hg",
  "limit": 10
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
  "name": "thiocyanate, thiocyanic",
  "formula": "SCN, HSCN",
  "limit": 20
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

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_name_SRD LIKE '%cadmium%' OR c.metal_name_SRD LIKE '%lead%' OR c.metal_name_SRD LIKE '%mercury%') AND (c.ligand_name_SRD LIKE '%thiocyan%' OR c.ligand_name_SRD LIKE '%rhodan%')",
  "order_by": "c.metal_name_SRD ASC, s.constant_value DESC",
  "limit": 100
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. You must call 0_plan_search_strategy first (PHASE 2) before using the execution tools.

---

### Step 9: `search_ligands`
**Args:**
```json
{
  "include_groups": [
    "SCN"
  ],
  "name": "thiocyan",
  "limit": 20
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 10: `search_metals`
**Args:**
```json
{
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

### Step 11: `search_ligands`
**Args:**
```json
{
  "limit": 100
}
```

[summary]
## search_ligands — 100 result(s)

**stats:** 5750 SQL matches · showing 100 · limit 100

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
| ligand_5810 | L-2-Amino-2-methyl-3-phosphopropanoic acid | H4L | Amino Acids | 3 | `CC(N)(COP(=O)(O)O)C(=O)O` | (-inf, H3L, 2.07, H2L, 5.68, HL, 10.07, L, +inf) |
| ligand_5811 | L-2-Amino-3-phosphobutanoic ac… (Phosphothreonine) | H4L | Amino Acids | 3 | `C[C@@H](OP(=O)(O)O)[C@H](N)C(=O)O` | (-inf, H3L, 2.25, H2L, 5.83, HL, 9.67, L, +inf) |
| ligand_5812 | DL-2-Amino-3-(phenylphospho)propanoic acid | H3L | Amino Acids | 2 | `NC(COP(=O)(O)Oc1ccccc1)C(=O)O` | (-inf, H2L, 2.13, HL, 8.79, L, +inf) |
| ligand_5813 | DL-2-Amino-3-phosphonopropanoic acid | H4L | Amino Acids | 31 | `NC(CP(=O)(O)O)C(=O)O` | (-inf, H3L, 2.37, H2L, 6.06, HL, 10.74, L, +inf) |
| ligand_5814 | DL-2-Amino-4-phosphonobutanoic acid | H4L | Amino Acids | 16 | `NC(CCP(=O)(O)O)C(=O)O` | (-inf, H3L, 2.51, H2L, 6.9, HL, 10.21, L, +inf) |
| ligand_5815 | DL-3-Amino-2-phosphonopropanoic acid | H4L | Amino Acids | 20 | `NCC(C(=O)O)P(=O)(O)O` | (-inf, H3L, 3.44, H2L, 5.52, HL, 10.07, L, +inf) |
| ligand_5816 | D-3-Amino-3-carboxyp… (Asparagine hydroxamic acid) | H2L | Amino Acids | 17 | `NC(CC(=O)NO)C(=O)O` | (-inf, H3L, 2.18, H2L, 8.15, HL, 9.37, L, +inf) |
| ligand_5817 | DL-2-Amino-3-(2-hydroxyphenyl)propan… (o-Tyrosine) | H2L | Amino Acids | 71 | `NC(Cc1ccccc1O)C(=O)O` | (-inf, H3L, 2.41, H2L, 8.67, HL, 11.01, L, +inf) |
| ligand_5818 | DL-2-Amino-3-(3-hydroxyphenyl)propan… (m-Tyrosine) | H2L | Amino Acids | 86 | `N[C@@H](Cc1cccc(O)c1)C(=O)O` | (-inf, H3L, 2.22, H2L, 8.95, HL, 10.04, L, +inf) |
| ligand_5819 | L-2-Amino-3-(4-hydroxyphenyl)propanoic… (Tyrosine) | H2L | Amino Acids | 107 | `N[C@@H](Cc1ccc(O)cc1)C(=O)O` | (-inf, H3L, 2.24, H2L, 9.04, HL, 10.1, L, +inf) |
| ligand_5820 | L-2-Amino-2-methyl-3-(4-hydrox… (L-Methyltyrosine) | H2L | Amino Acids | 7 | `CC(N)(Cc1ccc(O)cc1)C(=O)O` | (-inf, H3L, 2.16, H2L, 9.14, HL, 10.24, L, +inf) |
| ligand_5821 | L-2-Amino-3-(4-hydroxy-3,5… (L-3,5-Diiodotyrosine) | H2L | Amino Acids | 3 | `N[C@@H](Cc1cc(I)c(O)c(I)c1)C(=O)O` | (-inf, H2L, 6.16, HL, 9.1, L, +inf) |
| ligand_5822 | DL-2-Amino-3-(3-hydroxy-4-methoxyphenyl)propanoic… | H2L | Amino Acids | 3 | `COc1ccc(CC(N)C(=O)O)cc1O` | (-inf, H3L, 2.23, H2L, 8.84, HL, 10.12, L, +inf) |
| ligand_5823 | DL-2-Amino-3-(4-hydroxy-3-methoxyphenyl)propanoic… | H2L | Amino Acids | 3 | `COc1cc(CC(N)C(=O)O)ccc1O` | (-inf, H3L, 2.13, H2L, 8.78, HL, 10.14, L, +inf) |
| ligand_5824 | L-2-Amino-3-(3-amino-4-hydroxyp… (m-Aminotyrosine) | H2L | Amino Acids | 9 | `Nc1cc(C[C@H](N)C(=O)O)ccc1O` | (-inf, H4L, 2, H3L, 4.48, H2L, 9.09, HL, 10.19, L, +inf) |
| ligand_5825 | DL-2-Amino-2-(3,4-dihydroxyphenyl)acetic a… (DOPG) | H3L | Amino Acids | 6 | `NC(C(=O)O)c1ccc(O)c(O)c1` | (-inf, H4L, 2, H3L, 8.56, H2L, 9.75, HL, 9.75, L, +inf) |
| ligand_5826 | L-2-Amino-3-(3,4-dihydroxyphenyl)propanoic… (DOPA) | H3L | Amino Acids | 91 | `NC(Cc1ccc(O)c(O)c1)C(=O)O` | (-inf, H4L, 2.2, H3L, 8.75, H2L, 9.81, HL, 9.81, L, +inf) |
| ligand_5827 | L-2-Amino-2-methyl-3-(3,4-dihydr… (L-2-MethylDOPA) | H3L | Amino Acids | 13 | `CC(N)(Cc1ccc(O)c(O)c1)C(=O)O` | (-inf, H4L, 2.24, H3L, 8.88, H2L, 9.99, HL, +inf) |
| ligand_5828 | L-2-Amino-3-hydroxypropanoic acid (Serine) | HL | Amino Acids | 139 | `N[C@@H](CO)C(=O)O` | (-inf, H2L, 2.16, HL, 9.05, L, +inf) |
| ligand_5829 | L-2-Amino-3-hydroxybutanoic acid (Threonine) | HL | Amino Acids | 117 | `C[C@@H](O)[C@H](N)C(=O)O` | (-inf, H2L, 2.2, HL, 8.94, L, +inf) |
| ligand_5830 | allo-L-2-Amino-3-hydroxybutano… (L-allo-Threonine) | HL | Amino Acids | 31 | `C[C@H](O)[C@H](N)C(=O)O` | (-inf, H2L, 2.11, HL, 8.92, L, +inf) |
| ligand_5831 | erythro-2-Amino-3-hydroxy-… (erythro-Phenylserine) | HL | Amino Acids | 22 | `NC(C(=O)O)C(O)c1ccccc1` | (-inf, H2L, -1.9, HL, 8.7, L, +inf) |
| ligand_5832 | threo-2-Amino-3-hydroxy-3-ph… (threo-Phenylserine) | HL | Amino Acids | 13 | `NC(C(=O)O)C(O)c1ccccc1` | (-inf, H2L, -1.9, HL, 8.87, L, +inf) |
| ligand_5833 | L-2-Amino-4-hydroxybutanoic acid (Homoserine) | HL | Amino Acids | 31 | `N[C@@H](CCO)C(=O)O` | (-inf, H2L, 2.24, HL, 9.28, L, +inf) |
| ligand_5834 | DL-3-Amino-2-hydroxypropanoic acid (Isoserine) | HL | Amino Acids | 36 | `NCC(O)C(=O)O` | (-inf, H2L, 2.66, HL, 9.13, L, +inf) |
| ligand_5835 | DL-4-Amino-3-hydroxybutanoic acid | HL | Amino Acids | 21 | `NCC(O)CC(=O)O` | (-inf, H2L, 3.9, HL, 9.46, L, +inf) |
| ligand_5836 | L-trans-2-Amino-3-hydroxy-2,3-dihydrobenzoic acid | HL | Amino Acids | 6 | `N[C@H]1C(C(=O)O)=CC=C[C@@H]1O` | (-inf, H2L, 3.36, HL, 8.56, L, +inf) |
| ligand_5837 | D-gluco-2-Amino-3,4,5,6-tet… (D-Glucosaminic acid) | HL | Amino Acids | 30 | `N[C@@H](C(=O)O)[C@@H](O)[C@H](O)[C@H](O)CO` | (-inf, H2L, 2.2, HL, 9.08, L, +inf) |
| ligand_5838 | DL-Amino-4-Methoxyphenyl… (4-Methoxyphenylglycine) | HL | Amino Acids | 12 | `COc1ccc(C(N)C(=O)O)cc1` | (-inf, H2L, 2, HL, 9.07, L, +inf) |
| ligand_5839 | L-2-Aminobutanedioic acid 4-… (4-Methyl aspartate) | HL | Amino Acids | 1 | `COC(=O)CC(N)C(=O)O` | (-inf, HL, 8.5, L, +inf) |
| ligand_5840 | DL-2-Aminopentanedioic acid 5… (5-Ethyl glutamate) | HL | Amino Acids | 2 | `CCOC(=O)CC[C@H](N)C(=O)O` | (-inf, H2L, 2.15, HL, 9.19, L, +inf) |
| ligand_5841 | L-2-Aminopentanedioic acid 5… (5-Benzyl glutamate) | HL | Amino Acids | 2 | `N[C@@H](CCC(=O)OCc1ccccc1)C(=O)O` | (-inf, H2L, 2.06, HL, 8.89, L, +inf) |
| ligand_5842 | DL-2-Aminopentanedioic acid 1… (1-Ethyl glutamate) | HL | Amino Acids | 2 | `CCOC(=O)[C@@H](N)CCC(=O)O` | (-inf, H2L, 3.85, HL, 7.84, L, +inf) |
| ligand_5843 | L-2-Aminobutanedioic acid 4-amide (Asparagine) | HL | Amino Acids | 92 | `NC(=O)C[C@H](N)C(=O)O` | (-inf, H2L, 2.16, HL, 8.73, L, +inf) |
| ligand_5844 | L-2-Aminopentanedioic acid 5-amide (Glutamine) | HL | Amino Acids | 71 | `NC(=O)CC[C@H](N)C(=O)O` | (-inf, H2L, 2.19, HL, 9, L, +inf) |
| ligand_5845 | L-2-Amino-6-(2-methylpropamido)hexanoic acid (N(6… | HL | Amino Acids | 30 | `CC(C)C(=O)NCCCCC(N)C(=O)O` | (-inf, H2L, 2.4, HL, 9.42, L, +inf) |
| ligand_5846 | L-6-Amino-2-acetamidohexanoic acid (N(2)-Acetyl-L… | HL | Amino Acids | 1 | `CC(=O)N[C@@H](CCCCN)C(=O)O` | *** |
| ligand_5847 | L-2-Amino-6-acetamidohexanoic acid (N(6)-Acetyl-L… | HL | Amino Acids | 7 | `CC(=O)NCCCCC(N)C(=O)O` | (-inf, H2L, 2.13, HL, 9.52, L, +inf) |
| ligand_5848 | L-2-Amino-3-(oxalylamido)propanoic acid | HL | Amino Acids | 10 | `NC(CNC(=O)C(=O)O)C(=O)O` | (-inf, H3L, -1.2, H2L, 2.44, HL, 8.95, L, +inf) |
| ligand_5849 | N(6)-d-Biotinyl-L-lysine (d-Biocytin) | HL | Amino Acids | 7 | `NC(CCCCNC(=O)CCCCC1SCC2NC(=O)NC21)C(=O)O` | (-inf, H2L, 2.26, HL, 9.29, L, +inf) |
| ligand_5850 | d-Biocytin sulfoxide | HL | Amino Acids | 4 | `NC(CCCCNC(=O)CCCCC1C2NC(=O)NC2CS1=O)C(=O)O` | (-inf, HL, 9.3, L, +inf) |
| ligand_5851 | d-Biocytin sulfone | HL | Amino Acids | 4 | `NC(CCCCNC(=O)CCCCC1C2NC(=O)NC2CS1(=O)=O)C(=O)O` | (-inf, HL, 9.31, L, +inf) |
| ligand_5852 | L-2-Amino-5-ureidopentanoic acid (Citrulline) | HL | Amino Acids | 16 | `NC(=O)NCCC[C@H](N)C(=O)O` | (-inf, H2L, 2.3, HL, 9.33, L, +inf) |
| ligand_5853 | L-2-Amino-3-(phenylmethoxy)propa… (O-Benzylserine) | HL | Amino Acids | 4 | `N[C@@H](COCc1ccccc1)C(=O)O` | (-inf, H2L, -1.9, HL, 9.03, L, +inf) |
| ligand_5854 | L-2-Amino-3-(4-methoxyph… (4-Methoxyphenylalanine) | HL | Amino Acids | 5 | `COc1ccc(C[C@H](N)C(=O)O)cc1` | (-inf, HL, -9.15, L, +inf) |
| ligand_5855 | DL-2-Amino-3-(3,4-di… (3,4-Dimethoxyphenylalanine) | HL | Amino Acids | 2 | `COc1ccc(C[C@H](N)C(=O)O)cc1OC` | (-inf, H2L, 2.37, HL, 9.02, L, +inf) |
| ligand_5856 | L-2-Amino-3-mercaptopropanoic acid (Cysteine) | H2L | Amino Acids | 134 | `N[C@@H](CS)C(=O)O` | (-inf, H3L, -1.9, H2L, 8.18, HL, 10.3, L, +inf) |
| ligand_5857 | D-2-Amino-3-mercapto-3-methylbuta… (Penicillamine) | H2L | Amino Acids | 91 | `CC(C)(S)[C@H](N)C(=O)O` | (-inf, H3L, -1.9, H2L, 7.96, HL, 10.67, L, +inf) |
| ligand_5858 | DL-2-Amino-3-mercapto-3-methylpentanoic acid | H2L | Amino Acids | 2 | `CCC(C)(S)C(N)C(=O)O` | (-inf, H2L, 7.96, HL, 10.5, L, +inf) |
| ligand_5859 | DL-2-Amino-4-mercaptobutanoic acid (Homocysteine) | H2L | Amino Acids | 3 | `NC(CCS)C(=O)O` | (-inf, H3L, 2.15, H2L, 8.57, HL, 10.38, L, +inf) |

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

### Step 12: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_26",
  "ligand_id": "ligand_5760"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 3 species

### Cd^[2+] + Aminoacetic acid (Glycine)
**metal_id:** metal_26 | **ligand_id:** ligand_5760 | **ligand_def_HxL:** HL  
**entries:** 32 | **species:** 3 | **vlm_count:** 32

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 11 |
| beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | [M] + [L]^2 <=> [ML2] | [ML2](aqueous), [M](aqueous), [L](aqueous) | 11 |
| beta_def_872 | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | [M] + [L]^3 <=> [ML3] | [ML3](aqueous), [M](aqueous), [L](aqueous) | 10 |

**vlm_ids:** vlm_93961, vlm_93962, vlm_93963, vlm_93964, vlm_93965, … vlm_93990, vlm_93991, vlm_93992 (32 listed)

**equilibrium_maps:** 7 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_119 | 3 | 3 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_120 | 3 | 3 | 19~29 °C | 0.35~0.65 M |
| ref_eq_net_121 | 3 | 3 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_122 | 3 | 3 | 5~15 °C | -0.15~0.15 M |
| ref_eq_net_123 | 3 | 3 | 19~29 °C | -0.15~0.15 M |
| ref_eq_net_124 | 3 | 3 | 35~45 °C | -0.15~0.15 M |
| ref_eq_net_125 | 2 | 1 | 31~41 °C | 0~0.3 M |

---

### Step 14: `search_stability`
**Args:**
```json
{
  "where": "((c.metal_id = metal_26 OR c.metal_name_SRD LIKE '%Lead(II)%' OR c.metal_name_SRD LIKE '%Pb^[2+]%' OR c.metal_name_SRD LIKE '%Mercury(II)%' OR c.metal_name_SRD LIKE '%Hg^[2+]%') AND (c.ligand_name_SRD LIKE '%thiocyan%' OR c.ligand_name_SRD LIKE '%rhodan%' OR c.ligand_name_SRD LIKE '%isothiocyan%') AND s.solvent_name LIKE '%water%' AND s.reaction_type LIKE '%ML%')",
  "order_by": "c.metal_name_SRD ASC, c.ligand_name_SRD ASC, s.temperature_c ASC, s.ionic_strength_mol_l ASC, s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability — 100 row(s)

### logK — 15 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_2 | Ag^[+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 17 | 5 | 25 | 0~4 | solid | 4 |
| metal_2 | Ag^[+] | ligand_10004 | Thiocarbamide (Thiourea) | L | NC(N)=S | 11 | 5 | 25 | 0.02~1 | *** | 3 |
| metal_21 | Bi^[3+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 7 | 6 | 25 | 0~1 | *** | 2 |
| metal_2 | Ag^[+] | ligand_10106 | Hydrogen azide (Hydrazoic a… | HL | [N-]=[N+]=N | 6 | 5 | 25 | 0~4 | solid | 2 |
| metal_6 | Am^[3+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 3 | 1 | 25 | 0~5 | *** | 3 |
| metal_13 | Au^[+] | ligand_10004 | Thiocarbamide (Thiourea) | L | NC(N)=S | 3 | 3 | 25 | 0.5 | *** | 1 |
| metal_2 | Ag^[+] | ligand_9825 | Cyanomethane (Acetonitrile) | L | CC#N | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_2 | Ag^[+] | ligand_10091 | Hydrogen cyanate (Cyanic ac… | HL | N=C=O | 2 | 2 | 20~30 | 0 | solid | 1 |
| metal_2 | Ag^[+] | ligand_10093 | Selenocyanate ion | L | N#C[Se-] | 2 | 2 | 20~25 | 0~0.5 | solid | 2 |
| metal_6 | Am^[3+] | ligand_10106 | Hydrogen azide (Hydrazoic a… | HL | [N-]=[N+]=N | 2 | 1 | 25 | 0~0.5 | *** | 2 |
| metal_13 | Au^[+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 2 | 2 | 25 | 3 | *** | 1 |
| metal_19 | Be^[2+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 2 | 2 | 25 | 4 | *** | 1 |
| metal_1 | Ac^[3+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 1 | 1 | 25 | 1 | *** | 1 |
| metal_2 | Ag^[+] | ligand_10095 | Dicyanimide ion | L | N#C[N-]C#N | 1 | 1 | 20 | 0 | solid | 1 |
| metal_5 | Al^[3+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 1 | 1 | 22 | 0 | *** | 1 |

### ΔS — 5 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_2 | Ag^[+] | ligand_10004 | Thiocarbamide (Thiourea) | L | NC(N)=S | 11 | 5 | 25 | 0.02~1 | *** | 0 |
| metal_13 | Au^[+] | ligand_10004 | Thiocarbamide (Thiourea) | L | NC(N)=S | 3 | 3 | 25 | 0.5 | *** | 0 |
| metal_2 | Ag^[+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 2 | 2 | 25 | 0 | solid | 0 |
| metal_6 | Am^[3+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 2 | 1 | 25 | 1~5 | *** | 0 |
| metal_2 | Ag^[+] | ligand_10106 | Hydrogen azide (Hydrazoic a… | HL | [N-]=[N+]=N | 1 | 1 | 25 | 0 | solid | 0 |

### ΔH — 5 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_2 | Ag^[+] | ligand_10004 | Thiocarbamide (Thiourea) | L | NC(N)=S | 11 | 5 | 25 | 0.02~1 | *** | 0 |
| metal_13 | Au^[+] | ligand_10004 | Thiocarbamide (Thiourea) | L | NC(N)=S | 3 | 3 | 25 | 0.5 | *** | 0 |
| metal_2 | Ag^[+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 2 | 2 | 25 | 0 | solid | 0 |
| metal_6 | Am^[3+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 2 | 1 | 25 | 1~5 | *** | 0 |
| metal_2 | Ag^[+] | ligand_10106 | Hydrogen azide (Hydrazoic a… | HL | [N-]=[N+]=N | 1 | 1 | 25 | 0 | solid | 0 |

---

### Step 15: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_10092 AND (c.metal_name_SRD LIKE '%Cd%' OR c.metal_name_SRD LIKE '%cadmium%' OR c.metal_name_SRD LIKE '%Pb%' OR c.metal_name_SRD LIKE '%lead%' OR c.metal_name_SRD LIKE '%Hg%' OR c.metal_name_SRD LIKE '%mercury%'))",
  "order_by": "c.metal_name_SRD ASC, s.temperature_c ASC, s.ionic_strength_mol_l ASC, s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability — 89 row(s)

### logK — 8 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_26 | Cd^[2+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 23 | 4 | 25 | 0~3 | *** | 7 |
| metal_71 | Hg^[2+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 8 | 6 | 25 | 0~1 | solid | 2 |
| metal_125 | Pb^[2+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 8 | 3 | 25 | 1~4 | *** | 4 |
| metal_53 | EtHg^[+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 2 | 2 | 25 | 1 | *** | 1 |
| metal_72 | Hg^[+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 2 | 1 | 25 | 0~1 | solid | 2 |
| metal_93 | MeHg^[+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_87 | Me_[3]Pb^[+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 1 | 1 | 25 | 1.5 | *** | 1 |
| metal_136 | PhHg^[+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 1 | 1 | 25 | 1 | *** | 1 |

### ΔS — 3 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_26 | Cd^[2+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 14 | 4 | 25 | 0~3 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 6 | 5 | 25 | 0~1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 1 | 1 | 25 | 2 | *** | 0 |

### ΔH — 3 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_26 | Cd^[2+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 14 | 4 | 25 | 0~3 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 6 | 5 | 25 | 0~1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 1 | 1 | 25 | 0 | *** | 0 |

---

### Step 16: `search_metals`
**Args:**
```json
{
  "name": "lead, mercury",
  "symbol": "Pb, Hg",
  "limit": 200
}
```

[summary]
## search_metals

*(no results)*

---

### Step 17: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_10092 AND c.metal_id IN (metal_26, metal_71, metal_125) AND s.constant_type = 'logK' AND s.temperature_c = 25 AND s.ionic_strength_mol_l = 1)",
  "order_by": "c.metal_id ASC, s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability

*(no results)*

---
