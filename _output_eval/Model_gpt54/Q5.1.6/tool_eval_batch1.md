# Q5.1.6 — Tool Results (batch 1)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Lanthanum, Cerium, Neodymium, Europium, Gadolinium, Terbium, Dysprosium, Yttrium, Ytterbium, Lutetium",
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
  "name": "EDTA, DTPA, NTA, Citrate, Carbonate, Fluoride, Oxalate, Phosphate, Hydroxide",
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
{}
```

[summary]
[CATALOG]
## build_system_catalog

**Error:** Provide at least one of metal_id, ligand_id, or beta_definition_id.

---

### Step 7: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_name_SRD IN ('Yttrium','Lanthanum','Cerium','Praseodymium','Neodymium','Samarium','Europium','Gadolinium','Terbium','Dysprosium','Holmium','Erbium','Thulium','Ytterbium','Lutetium'))",
  "order_by": "c.ligand_name_SRD ASC",
  "limit": 200
}
```

[summary]
## search_stability

*(no results)*

---

### Step 8: `db_ranked_pairs`
**Args:**
```json
{
  "rank_by": "measurement_count",
  "limit": 50,
  "where": "metal_name_SRD = '[''Yttrium'', ''Lanthanum'', ''Cerium'', ''Praseodymium'', ''Neodymium'', ''Samarium'', ''Europium'', ''Gadolinium'', ''Terbium'', ''Dysprosium'', ''Holmium'', ''Erbium'', ''Thulium'', ''Ytterbium'', ''Lutetium'']'"
}
```

[summary]
**db_ranked_pairs:** Error - Unknown rank_by='measurement_count'. Choose from: ['ligands_per_metal', 'measurements_per_ligand', 'measurements_per_metal', 'metals_per_ligand', 'pka_per_ligand']

---

### Step 9: `db_ranked_pairs`
**Args:**
```json
{
  "rank_by": "measurements_per_metal",
  "limit": 50
}
```

[summary]
## db_ranked_pairs - measurements_per_metal

| metal_id | name | count |
|----------|------|-------|
| metal_68 | H^[+] | 20720 |
| metal_41 | Cu^[2+] | 8963 |
| metal_112 | Ni^[2+] | 5325 |
| metal_208 | Zn^[2+] | 4095 |
| metal_33 | Co^[2+] | 2977 |
| metal_2 | Ag^[+] | 2885 |
| metal_26 | Cd^[2+] | 2828 |
| metal_25 | Ca^[2+] | 1761 |
| metal_125 | Pb^[2+] | 1585 |
| metal_61 | Fe^[3+] | 1473 |
| metal_92 | Mg^[2+] | 1422 |
| metal_94 | Mn^[2+] | 1273 |
| metal_71 | Hg^[2+] | 1097 |
| metal_79 | La^[3+] | 931 |
| metal_65 | Gd^[3+] | 897 |
| metal_58 | Eu^[3+] | 870 |
| metal_173 | Sm^[3+] | 844 |
| metal_110 | Nd^[3+] | 794 |
| metal_5 | Al^[3+] | 792 |
| metal_55 | Er^[3+] | 792 |
| metal_177 | Sr^[2+] | 784 |
| metal_206 | Yb^[3+] | 771 |
| metal_44 | Dy^[3+] | 758 |
| metal_18 | Ba^[2+] | 749 |
| metal_195 | UO_[2]^[2+] | 748 |
| metal_139 | Pr^[3+] | 723 |
| metal_179 | Tb^[3+] | 709 |
| metal_73 | Ho^[3+] | 705 |
| metal_81 | Lu^[3+] | 671 |
| metal_62 | Fe^[2+] | 667 |
| metal_192 | Tm^[3+] | 633 |
| metal_27 | Ce^[3+] | 567 |
| metal_205 | Y^[3+] | 533 |
| metal_185 | Th^[4+] | 476 |
| metal_19 | Be^[2+] | 443 |
| metal_74 | In^[3+] | 433 |
| metal_64 | Ga^[3+] | 428 |
| metal_201 | VO^[2+] | 364 |
| metal_78 | K^[+] | 335 |
| metal_106 | Na^[+] | 335 |
| metal_42 | Cu^[+] | 285 |
| metal_21 | Bi^[3+] | 283 |
| metal_191 | Tl^[+] | 272 |
| metal_127 | Pd^[2+] | 245 |
| metal_80 | Li^[+] | 216 |
| metal_15 | B^[3+] | 195 |
| metal_6 | Am^[3+] | 190 |
| metal_85 | Me_[2]Sn^[2+] | 165 |
| metal_169 | Sc^[3+] | 156 |
| metal_93 | MeHg^[+] | 148 |

---

### Step 10: `db_ranked_pairs`
**Args:**
```json
{
  "rank_by": "metals_per_ligand",
  "limit": 30,
  "where": "lc.metal_id = '[''metal_79'', ''metal_65'', ''metal_58'', ''metal_173'', ''metal_110'', ''metal_55'', ''metal_206'', ''metal_44'', ''metal_139'', ''metal_179'', ''metal_73'', ''metal_81'', ''metal_192'', ''metal_27'', ''metal_205'']'"
}
```

[summary]
## db_ranked_pairs - metals_per_ligand

| id | name | count |
|----|------|-------|

---

### Step 11: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_79, metal_65, metal_58, metal_173, metal_110, metal_55, metal_206, metal_44, metal_139, metal_179, metal_73, metal_81, metal_192, metal_27, metal_205))",
  "order_by": "c.ligand_name_SRD ASC, c.metal_name_SRD ASC",
  "limit": 200
}
```

[summary]
## search_stability — 200 row(s)

### logK — 79 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_44 | Dy^[3+] | ligand_8669 | (1R,3R,4R,5R)-(-)-1,3,4,5-T… | HL | O=C(O)C1(O)CC(O)C(O)C(O)C1 | 7 | 4 | 25 | 0.1~1 | *** | 2 |
| metal_55 | Er^[3+] | ligand_8669 | (1R,3R,4R,5R)-(-)-1,3,4,5-T… | HL | O=C(O)C1(O)CC(O)C(O)C(O)C1 | 7 | 4 | 25 | 0.1~1 | *** | 2 |
| metal_58 | Eu^[3+] | ligand_8669 | (1R,3R,4R,5R)-(-)-1,3,4,5-T… | HL | O=C(O)C1(O)CC(O)C(O)C(O)C1 | 7 | 4 | 25 | 0.1~1 | *** | 2 |
| metal_65 | Gd^[3+] | ligand_8669 | (1R,3R,4R,5R)-(-)-1,3,4,5-T… | HL | O=C(O)C1(O)CC(O)C(O)C(O)C1 | 7 | 4 | 25 | 0.1~1 | *** | 2 |
| metal_73 | Ho^[3+] | ligand_8669 | (1R,3R,4R,5R)-(-)-1,3,4,5-T… | HL | O=C(O)C1(O)CC(O)C(O)C(O)C1 | 7 | 4 | 25 | 0.1~1 | *** | 2 |
| metal_79 | La^[3+] | ligand_8669 | (1R,3R,4R,5R)-(-)-1,3,4,5-T… | HL | O=C(O)C1(O)CC(O)C(O)C(O)C1 | 7 | 4 | 25 | 0.1~1 | *** | 2 |
| metal_139 | Pr^[3+] | ligand_8669 | (1R,3R,4R,5R)-(-)-1,3,4,5-T… | HL | O=C(O)C1(O)CC(O)C(O)C(O)C1 | 7 | 4 | 25 | 0.1~1 | *** | 2 |
| metal_173 | Sm^[3+] | ligand_8669 | (1R,3R,4R,5R)-(-)-1,3,4,5-T… | HL | O=C(O)C1(O)CC(O)C(O)C(O)C1 | 7 | 4 | 25 | 0.1~1 | *** | 2 |
| metal_179 | Tb^[3+] | ligand_8669 | (1R,3R,4R,5R)-(-)-1,3,4,5-T… | HL | O=C(O)C1(O)CC(O)C(O)C(O)C1 | 7 | 4 | 25 | 0.1~1 | *** | 2 |
| metal_206 | Yb^[3+] | ligand_8669 | (1R,3R,4R,5R)-(-)-1,3,4,5-T… | HL | O=C(O)C1(O)CC(O)C(O)C(O)C1 | 7 | 4 | 25 | 0.1~1 | *** | 2 |
| metal_44 | Dy^[3+] | ligand_9358 | 1,2-Dihydroxybenzene-3,5-di… | H4L | O=S(=O)(O)c1cc(O)c(O)c(S(=O)(=O)O)c1 | 5 | 4 | 25 | 0.1~0.5 | *** | 2 |
| metal_55 | Er^[3+] | ligand_9358 | 1,2-Dihydroxybenzene-3,5-di… | H4L | O=S(=O)(O)c1cc(O)c(O)c(S(=O)(=O)O)c1 | 5 | 4 | 25 | 0.1~0.5 | *** | 2 |
| metal_65 | Gd^[3+] | ligand_9358 | 1,2-Dihydroxybenzene-3,5-di… | H4L | O=S(=O)(O)c1cc(O)c(O)c(S(=O)(=O)O)c1 | 5 | 4 | 25 | 0.1~0.5 | *** | 2 |
| metal_73 | Ho^[3+] | ligand_9358 | 1,2-Dihydroxybenzene-3,5-di… | H4L | O=S(=O)(O)c1cc(O)c(O)c(S(=O)(=O)O)c1 | 5 | 4 | 25 | 0.1~0.5 | *** | 2 |
| metal_27 | Ce^[3+] | ligand_8669 | (1R,3R,4R,5R)-(-)-1,3,4,5-T… | HL | O=C(O)C1(O)CC(O)C(O)C(O)C1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_81 | Lu^[3+] | ligand_8669 | (1R,3R,4R,5R)-(-)-1,3,4,5-T… | HL | O=C(O)C1(O)CC(O)C(O)C(O)C1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_110 | Nd^[3+] | ligand_8669 | (1R,3R,4R,5R)-(-)-1,3,4,5-T… | HL | O=C(O)C1(O)CC(O)C(O)C(O)C1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_192 | Tm^[3+] | ligand_8669 | (1R,3R,4R,5R)-(-)-1,3,4,5-T… | HL | O=C(O)C1(O)CC(O)C(O)C(O)C1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_205 | Y^[3+] | ligand_8669 | (1R,3R,4R,5R)-(-)-1,3,4,5-T… | HL | O=C(O)C1(O)CC(O)C(O)C(O)C1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_44 | Dy^[3+] | ligand_9015 | (Ethylenedithio)diacetic ac… | H2L | O=C(O)CSCCSCC(=O)O | 3 | 3 | 25 | 1 | *** | 1 |
| metal_55 | Er^[3+] | ligand_9015 | (Ethylenedithio)diacetic ac… | H2L | O=C(O)CSCCSCC(=O)O | 3 | 3 | 25 | 1 | *** | 1 |
| metal_173 | Sm^[3+] | ligand_9015 | (Ethylenedithio)diacetic ac… | H2L | O=C(O)CSCCSCC(=O)O | 3 | 3 | 25 | 1 | *** | 1 |
| metal_65 | Gd^[3+] | ligand_7950 | 1,2-Diethyl-3,4-dihydroxypy… | HL | CCc1c(O)c(=O)ccn1CC | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_58 | Eu^[3+] | ligand_9358 | 1,2-Dihydroxybenzene-3,5-di… | H4L | O=S(=O)(O)c1cc(O)c(O)c(S(=O)(=O)O)c1 | 3 | 3 | 25 | 0.5 | *** | 1 |
| metal_81 | Lu^[3+] | ligand_9358 | 1,2-Dihydroxybenzene-3,5-di… | H4L | O=S(=O)(O)c1cc(O)c(O)c(S(=O)(=O)O)c1 | 3 | 3 | 25 | 0.5 | *** | 1 |
| metal_79 | La^[3+] | ligand_6333 | (2-Hydroxytrimethylene)dini… | H4L | O=C(O)CN(CC(=O)O)CC(O)CN(CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1 | *** | 2 |
| metal_55 | Er^[3+] | ligand_8786 | (Ethylthio)acetic acid | HL | CCSCC(=O)O | 2 | 2 | 30 | 2 | *** | 1 |
| metal_58 | Eu^[3+] | ligand_8786 | (Ethylthio)acetic acid | HL | CCSCC(=O)O | 2 | 2 | 30 | 2 | *** | 1 |
| metal_65 | Gd^[3+] | ligand_8786 | (Ethylthio)acetic acid | HL | CCSCC(=O)O | 2 | 2 | 30 | 2 | *** | 1 |
| metal_73 | Ho^[3+] | ligand_8786 | (Ethylthio)acetic acid | HL | CCSCC(=O)O | 2 | 2 | 30 | 2 | *** | 1 |
| metal_79 | La^[3+] | ligand_8786 | (Ethylthio)acetic acid | HL | CCSCC(=O)O | 2 | 2 | 30 | 2 | *** | 1 |
| metal_110 | Nd^[3+] | ligand_8786 | (Ethylthio)acetic acid | HL | CCSCC(=O)O | 2 | 2 | 30 | 2 | *** | 1 |
| metal_173 | Sm^[3+] | ligand_8786 | (Ethylthio)acetic acid | HL | CCSCC(=O)O | 2 | 2 | 30 | 2 | *** | 1 |
| metal_179 | Tb^[3+] | ligand_8786 | (Ethylthio)acetic acid | HL | CCSCC(=O)O | 2 | 2 | 30 | 2 | *** | 1 |
| metal_205 | Y^[3+] | ligand_8786 | (Ethylthio)acetic acid | HL | CCSCC(=O)O | 2 | 2 | 30 | 2 | *** | 1 |
| metal_206 | Yb^[3+] | ligand_8786 | (Ethylthio)acetic acid | HL | CCSCC(=O)O | 2 | 2 | 30 | 2 | *** | 1 |
| metal_27 | Ce^[3+] | ligand_6286 | (1,1-Dimethylethylene)dinit… | H4L | CC(C)(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_44 | Dy^[3+] | ligand_6286 | (1,1-Dimethylethylene)dinit… | H4L | CC(C)(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_55 | Er^[3+] | ligand_6286 | (1,1-Dimethylethylene)dinit… | H4L | CC(C)(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_58 | Eu^[3+] | ligand_6286 | (1,1-Dimethylethylene)dinit… | H4L | CC(C)(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_65 | Gd^[3+] | ligand_6286 | (1,1-Dimethylethylene)dinit… | H4L | CC(C)(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_73 | Ho^[3+] | ligand_6286 | (1,1-Dimethylethylene)dinit… | H4L | CC(C)(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6286 | (1,1-Dimethylethylene)dinit… | H4L | CC(C)(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_81 | Lu^[3+] | ligand_6286 | (1,1-Dimethylethylene)dinit… | H4L | CC(C)(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_110 | Nd^[3+] | ligand_6286 | (1,1-Dimethylethylene)dinit… | H4L | CC(C)(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_139 | Pr^[3+] | ligand_6286 | (1,1-Dimethylethylene)dinit… | H4L | CC(C)(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_173 | Sm^[3+] | ligand_6286 | (1,1-Dimethylethylene)dinit… | H4L | CC(C)(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_179 | Tb^[3+] | ligand_6286 | (1,1-Dimethylethylene)dinit… | H4L | CC(C)(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_192 | Tm^[3+] | ligand_6286 | (1,1-Dimethylethylene)dinit… | H4L | CC(C)(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_206 | Yb^[3+] | ligand_6286 | (1,1-Dimethylethylene)dinit… | H4L | CC(C)(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_27 | Ce^[3+] | ligand_6333 | (2-Hydroxytrimethylene)dini… | H4L | O=C(O)CN(CC(=O)O)CC(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_44 | Dy^[3+] | ligand_6333 | (2-Hydroxytrimethylene)dini… | H4L | O=C(O)CN(CC(=O)O)CC(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_55 | Er^[3+] | ligand_6333 | (2-Hydroxytrimethylene)dini… | H4L | O=C(O)CN(CC(=O)O)CC(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_58 | Eu^[3+] | ligand_6333 | (2-Hydroxytrimethylene)dini… | H4L | O=C(O)CN(CC(=O)O)CC(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_65 | Gd^[3+] | ligand_6333 | (2-Hydroxytrimethylene)dini… | H4L | O=C(O)CN(CC(=O)O)CC(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_73 | Ho^[3+] | ligand_6333 | (2-Hydroxytrimethylene)dini… | H4L | O=C(O)CN(CC(=O)O)CC(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_81 | Lu^[3+] | ligand_6333 | (2-Hydroxytrimethylene)dini… | H4L | O=C(O)CN(CC(=O)O)CC(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_110 | Nd^[3+] | ligand_6333 | (2-Hydroxytrimethylene)dini… | H4L | O=C(O)CN(CC(=O)O)CC(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_139 | Pr^[3+] | ligand_6333 | (2-Hydroxytrimethylene)dini… | H4L | O=C(O)CN(CC(=O)O)CC(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_173 | Sm^[3+] | ligand_6333 | (2-Hydroxytrimethylene)dini… | H4L | O=C(O)CN(CC(=O)O)CC(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_179 | Tb^[3+] | ligand_6333 | (2-Hydroxytrimethylene)dini… | H4L | O=C(O)CN(CC(=O)O)CC(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_192 | Tm^[3+] | ligand_6333 | (2-Hydroxytrimethylene)dini… | H4L | O=C(O)CN(CC(=O)O)CC(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_205 | Y^[3+] | ligand_6333 | (2-Hydroxytrimethylene)dini… | H4L | O=C(O)CN(CC(=O)O)CC(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_206 | Yb^[3+] | ligand_6333 | (2-Hydroxytrimethylene)dini… | H4L | O=C(O)CN(CC(=O)O)CC(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_110 | Nd^[3+] | ligand_8191 | 1,10-Phenanthroline (Dipyri… | L | c1cnc2c(c1)ccc1cccnc12 | 1 | 1 | 25 | 5 | *** | 1 |
| metal_44 | Dy^[3+] | ligand_9337 | 1,2-Dihydroxybenzene (Catec… | H2L | Oc1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_55 | Er^[3+] | ligand_9337 | 1,2-Dihydroxybenzene (Catec… | H2L | Oc1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_58 | Eu^[3+] | ligand_9337 | 1,2-Dihydroxybenzene (Catec… | H2L | Oc1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_65 | Gd^[3+] | ligand_9337 | 1,2-Dihydroxybenzene (Catec… | H2L | Oc1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_73 | Ho^[3+] | ligand_9337 | 1,2-Dihydroxybenzene (Catec… | H2L | Oc1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_9337 | 1,2-Dihydroxybenzene (Catec… | H2L | Oc1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_81 | Lu^[3+] | ligand_9337 | 1,2-Dihydroxybenzene (Catec… | H2L | Oc1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_110 | Nd^[3+] | ligand_9337 | 1,2-Dihydroxybenzene (Catec… | H2L | Oc1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_139 | Pr^[3+] | ligand_9337 | 1,2-Dihydroxybenzene (Catec… | H2L | Oc1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_173 | Sm^[3+] | ligand_9337 | 1,2-Dihydroxybenzene (Catec… | H2L | Oc1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_192 | Tm^[3+] | ligand_9337 | 1,2-Dihydroxybenzene (Catec… | H2L | Oc1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_206 | Yb^[3+] | ligand_9337 | 1,2-Dihydroxybenzene (Catec… | H2L | Oc1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_9358 | 1,2-Dihydroxybenzene-3,5-di… | H4L | O=S(=O)(O)c1cc(O)c(O)c(S(=O)(=O)O)c1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_110 | Nd^[3+] | ligand_9358 | 1,2-Dihydroxybenzene-3,5-di… | H4L | O=S(=O)(O)c1cc(O)c(O)c(S(=O)(=O)O)c1 | 1 | 1 | 25 | 0.1 | *** | 1 |

### ΔH — 3 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_44 | Dy^[3+] | ligand_9015 | (Ethylenedithio)diacetic ac… | H2L | O=C(O)CSCCSCC(=O)O | 2 | 2 | 25 | 1 | *** | 0 |
| metal_55 | Er^[3+] | ligand_9015 | (Ethylenedithio)diacetic ac… | H2L | O=C(O)CSCCSCC(=O)O | 2 | 2 | 25 | 1 | *** | 0 |
| metal_173 | Sm^[3+] | ligand_9015 | (Ethylenedithio)diacetic ac… | H2L | O=C(O)CSCCSCC(=O)O | 2 | 2 | 25 | 1 | *** | 0 |

### ΔS — 3 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_44 | Dy^[3+] | ligand_9015 | (Ethylenedithio)diacetic ac… | H2L | O=C(O)CSCCSCC(=O)O | 2 | 2 | 25 | 1 | *** | 0 |
| metal_55 | Er^[3+] | ligand_9015 | (Ethylenedithio)diacetic ac… | H2L | O=C(O)CSCCSCC(=O)O | 2 | 2 | 25 | 1 | *** | 0 |
| metal_173 | Sm^[3+] | ligand_9015 | (Ethylenedithio)diacetic ac… | H2L | O=C(O)CSCCSCC(=O)O | 2 | 2 | 25 | 1 | *** | 0 |

---

### Step 12: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_6286 AND c.metal_id IN (metal_27, metal_44, metal_55, metal_58, metal_65, metal_73, metal_79, metal_81, metal_110, metal_139, metal_173, metal_179, metal_192, metal_206) AND s.constant_type = 'logK' AND s.temperature_c = 20 AND s.ionic_strength_mol_l = 0.1)",
  "order_by": "c.metal_name_SRD ASC, s.constant_value ASC",
  "limit": 100
}
```

[summary]
## search_stability

*(no results)*

---

### Step 13: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_6286"
}
```

[summary]
## inspect_card — Ligand | ligand_6286

**Name:** (1,1-Dimethylethylene)dinitrilotetraacetic acid  
**Formula:** C12H20N2O8 | **Class:** EDTA and derivatives  
**SMILES:** `CC(C)(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O`  
**InChI:** `InChI=1S/C12H20N2O8/c1-12(2,14(5-10(19)20)6-11(21)22)7-13(3-8(15)16)4-9(17)18/h3-7H2,1-2H3,(H,15,16)(H,17,18)(H,19,20)(H,21,22)`  
**HxL definition:** H4L  

**pKa values:** 4

| source_vlm | pKa | T (°C) | I (M) | From → To | Solvent | Method | Quality |
|------------|-----|--------|-------|-----------|---------|--------|---------|
| vlm_109108 | -11.46 | 20.0 | 0.1 | L → HL | *** | *** | *** |
| vlm_109110 | -3.25 | 20.0 | 0.1 | H2L → H3L | *** | *** | *** |
| vlm_109111 | -2.45 | 20.0 | 0.1 | H3L → H4L | *** | *** | *** |
| vlm_109109 | 5.38 | 20.0 | 0.1 | HL → H2L | *** | *** | *** |

**Partners:** 26 metal(s), 29 measurement(s) total

| metal_id | Metal | # meas |
|----------|-------|--------|
| metal_68 | H^[+] | 4 |
| metal_208 | Zn^[2+] | 1 |
| metal_206 | Yb^[3+] | 1 |
| metal_192 | Tm^[3+] | 1 |
| metal_179 | Tb^[3+] | 1 |
| … | *(showing top 5 of 26)* | |

---
