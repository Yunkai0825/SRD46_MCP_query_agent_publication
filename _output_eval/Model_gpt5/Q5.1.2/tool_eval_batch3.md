# Q5.1.2 — Tool Results (batch 3)

### Step 2: `search_ligands`
**Args:**
```json
{
  "name": "DTPA",
  "limit": 20
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 5 SQL matches · showing 5 · limit 20

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6117 | 9,17-Dioxo-1,4,7,10,13,16-hexaazacycl… (DTPA-dien) | H3L | Aza macrocycles with car… | 6 | `O=C(O)CN1CCN(CC(=O)O)CC(=O)NCCNCCNC(=O)CN(CC(=O)O)CC1` | (-inf, H5L, -1.8, H4L, 2.62, H3L, 4.1, H2L, 8.87, HL, 10.02, L, +inf) |
| ligand_6356 | Diethylenetrinitrilopentaacetic acid (DTPA) | H5L | EDTA and derivatives | 322 | `O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O` | (-inf, H8L, -0.1, H7L, -0.1, H6L, -0.7, H5L, 2, H4L, 2.7, H3L, 4.28, H2L, 4.28, HL, -8.4, L, +inf) |
| ligand_6362 | Diethylenetrinitrilopentaacetic acid N… (DTPA-BMA) | *** | EDTA and derivatives | 43 | *** | (-inf, H4L, -1.4, H3L, 3.31, H2L, 4.38, HL, 9.37, L, +inf) |
| ligand_6363 | Diethylenetrinitrilopentaacetic acid N… (DTPA-BBA) | *** | EDTA and derivatives | 9 | *** | (-inf, H3L, 3.31, H2L, 4.44, HL, 9.36, L, +inf) |
| ligand_6364 | N,N"-Bis(2-pyridylmethyl)diethylenetrin… (DTPA-BP) | *** | EDTA and derivatives | 14 | *** | (-inf, H5L, 2.28, H4L, 3.41, H3L, 4.76, H2L, 6.46, HL, 9.5, L, +inf) |

### Functional groups across all SQL matches (2 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 2 | 100% |
| tertiary_amine | 2 | 100% |
| amide | 1 | 50% |
| secondary_amine | 1 | 50% |

---

### Step 3: `search_metals`
**Args:**
```json
{
  "name": "iron",
  "limit": 5
}
```

[summary]
## search_metals — 2 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_61 | Fe^[3+] | Fe | 3 | ✓ | [Fe+3] | InChI=1S/Fe/q+3 | beta_totN_128 | ligand_totN_406 | vlm_totN_1473 |
| metal_62 | Fe^[2+] | Fe | 2 | ✓ | [Fe+2] | InChI=1S/Fe/q+2 | beta_totN_57 | ligand_totN_217 | vlm_totN_667 |

---

### Step 4: `search_metals`
**Args:**
```json
{
  "name": "calcium",
  "limit": 5
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_25 | Ca^[2+] | Ca | 2 | ✓ | [Ca+2] | InChI=1S/Ca/q+2 | beta_totN_68 | ligand_totN_644 | vlm_totN_1761 |

---

### Step 5: `search_metals`
**Args:**
```json
{
  "name": "magnesium",
  "limit": 5
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_92 | Mg^[2+] | Mg | 2 | ✓ | [Mg+2] | InChI=1S/Mg/q+2 | beta_totN_53 | ligand_totN_508 | vlm_totN_1422 |

---

### Step 6: `search_metals`
**Args:**
```json
{
  "name": "copper",
  "limit": 5
}
```

[summary]
## search_metals — 3 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_41 | Cu^[2+] | Cu | 2 | ✓ | [Cu+2] | InChI=1S/Cu/q+2 | beta_totN_264 | ligand_totN_1951 | vlm_totN_8963 |
| metal_42 | Cu^[+] | Cu | 1 | ✓ | [Cu+] | InChI=1S/Cu/q+1 | beta_totN_32 | ligand_totN_117 | vlm_totN_285 |
| metal_43 | Cu^[3+] | Cu | 3 | ✓ | [Cu+3] | InChI=1S/Cu/q+3 | beta_totN_4 | ligand_totN_8 | vlm_totN_10 |

---

### Step 7: `search_metals`
**Args:**
```json
{
  "name": "zinc",
  "limit": 5
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_208 | Zn^[2+] | Zn | 2 | ✓ | [Zn+2] | InChI=1S/Zn/q+2 | beta_totN_122 | ligand_totN_1169 | vlm_totN_4095 |

---

### Step 8: `search_metals`
**Args:**
```json
{
  "name": "nickel",
  "limit": 5
}
```

[summary]
## search_metals — 2 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_112 | Ni^[2+] | Ni | 2 | ✓ | [Ni+2] | InChI=1S/Ni/q+2 | beta_totN_149 | ligand_totN_1369 | vlm_totN_5325 |
| metal_113 | Ni^[3+] | Ni | 3 | ✓ | [Ni+3] | InChI=1S/Ni/q+3 | beta_totN_5 | ligand_totN_4 | vlm_totN_7 |

---

### Step 9: `search_metals`
**Args:**
```json
{
  "name": "cobalt",
  "limit": 5
}
```

[summary]
## search_metals — 3 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_33 | Co^[2+] | Co | 2 | ✓ | [Co+2] | InChI=1S/Co/q+2 | beta_totN_92 | ligand_totN_977 | vlm_totN_2977 |
| metal_34 | Co^[3+] | Co | 3 | ✓ | [Co+3] | InChI=1S/Co/q+3 | beta_totN_20 | ligand_totN_19 | vlm_totN_55 |
| metal_181 | TcO^[2+] | Tc | 2 |  | *** | *** | beta_totN_2 | ligand_totN_1 | vlm_totN_2 |

---

### Step 10: `search_metals`
**Args:**
```json
{
  "name": "manganese",
  "limit": 5
}
```

[summary]
## search_metals — 4 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_94 | Mn^[2+] | Mn | 2 | ✓ | [Mn+2] | InChI=1S/Mn/q+2 | beta_totN_44 | ligand_totN_486 | vlm_totN_1273 |
| metal_95 | Mn^[3+] | Mn | 3 | ✓ | [Mn+3] | InChI=1S/Mn/q+3 | beta_totN_8 | ligand_totN_12 | vlm_totN_26 |
| metal_96 | Mn^[4+] | Mn | 4 | ✓ | [Mn+4] | InChI=1S/Mn/q+4 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_97 | MeNH_[3]^[+] | MNH3 | 1 |  | *** | *** | beta_totN_1 | ligand_totN_5 | vlm_totN_9 |

---

### Step 11: `search_metals`
**Args:**
```json
{
  "name": "aluminum",
  "limit": 5
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_5 | Al^[3+] | Al | 3 | ✓ | [Al+3] | InChI=1S/Al/q+3 | beta_totN_108 | ligand_totN_187 | vlm_totN_792 |

---

### Step 12: `search_metals`
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

### Step 13: `search_metals`
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

### Step 14: `search_metals`
**Args:**
```json
{
  "name": "gadolinium",
  "limit": 5
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_65 | Gd^[3+] | Gd | 3 | ✓ | [Gd+3] | InChI=1S/Gd/q+3 | beta_totN_28 | ligand_totN_288 | vlm_totN_897 |

---

### Step 15: `build_system_catalog`
**Args:**
```json
{
  "ligand_id": "ligand_6356"
}
```

[summary]
[CATALOG]
## build_system_catalog — 20 pair(s), 68 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_32 | [HL] + [H] <=> [H2L] |  |
| beta_def_53 | [H2L] + [H] <=> [H3L] |  |
| beta_def_64 | [H3L] + [H] <=> [H4L] |  |
| beta_def_68 | [H4L] + [H] <=> [H5L] |  |
| beta_def_72 | [H5L] + [H] <=> [H6L] |  |
| beta_def_76 | [H6L] + [H] <=> [H7L] |  |
| beta_def_77 | [H7L] + [H] <=> [H8L] |  |
| beta_def_79 | [L] + [H] <=> [HL] |  |
| beta_def_238 | [M(OH)2L] + [H] <=> [M(OH)L] + [H2O] |  |
| beta_def_502 | [M]^2 + [L] <=> [M2L] |  |
| beta_def_516 | [ML] + [M] <=> [M2L] |  |
| beta_def_739 | [MHL] + [H] <=> [MH2L] |  |
| beta_def_788 | [ML] + [H] <=> [MHL] |  |
| beta_def_812 | [M] + [L] <=> [ML] |  |
| beta_def_839 | [M(OH)L] + [H] <=> [ML] + [H2O] |  |
| beta_def_966 | [M(OH)L] + [H] <=> [ML] + [H2O] |  |

*(all species aqueous)*

**1. H^[+] + Diethylenetrinitrilopentaacetic acid (DTPA)** (metal_68 + ligand_6356) — ligand_def_HxL: H5L | 57 ent, 8 sp, 57 vlms (vlm_112470…vlm_112526)
   - species: beta_def_32(14) beta_def_53(8) beta_def_64(8) beta_def_68(8) beta_def_72(2) beta_def_76(2) beta_def_77(1) beta_def_79(14)
   - eq:10 nets T:15~41°C I:-0.05~1.15M max 8n/28e
**2. Ca^[2+] + Diethylenetrinitrilopentaacetic acid (DTPA)** (metal_25 + ligand_6356) — ligand_def_HxL: H5L | 11 ent, 3 sp, 11 vlms (vlm_112538…vlm_112548)
   - species: beta_def_516(3) beta_def_788(3) beta_def_812(5)
   - eq:3 nets T:15~41°C I:-0.05~0.3M max 3n/3e
**3. Th^[4+] + Diethylenetrinitrilopentaacetic acid (DTPA)** (metal_185 + ligand_6356) — ligand_def_HxL: H5L | 9 ent, 3 sp, 9 vlms (vlm_112657…vlm_112665)
   - species: beta_def_788(3) beta_def_812(4) beta_def_839(2)
   - eq:3 nets T:15~30°C I:-0.05~0.65M max 3n/3e
**4. Mg^[2+] + Diethylenetrinitrilopentaacetic acid (DTPA)** (metal_92 + ligand_6356) — ligand_def_HxL: H5L | 9 ent, 3 sp, 9 vlms (vlm_112529…vlm_112537)
   - species: beta_def_516(1) beta_def_788(3) beta_def_812(5)
   - eq:3 nets T:15~41°C I:-0.05~0.3M max 3n/3e
**5. Cu^[2+] + Diethylenetrinitrilopentaacetic acid (DTPA)** (metal_41 + ligand_6356) — ligand_def_HxL: H5L | 9 ent, 4 sp, 9 vlms (vlm_112702…vlm_112710)
   - species: beta_def_516(2) beta_def_739(1) beta_def_788(2) beta_def_812(4)
   - eq:2 nets T:15~30°C I:-0.05~0.25M max 4n/4e
**6. Zn^[2+] + Diethylenetrinitrilopentaacetic acid (DTPA)** (metal_208 + ligand_6356) — ligand_def_HxL: H5L | 8 ent, 3 sp, 8 vlms (vlm_112736…vlm_112743)
   - species: beta_def_516(2) beta_def_788(2) beta_def_812(4)
   - eq:2 nets T:15~30°C I:-0.05~0.25M max 3n/3e
**7. Ni^[2+] + Diethylenetrinitrilopentaacetic acid (DTPA)** (metal_112 + ligand_6356) — ligand_def_HxL: H5L | 8 ent, 3 sp, 8 vlms (vlm_112694…vlm_112701)
   - species: beta_def_516(2) beta_def_788(2) beta_def_812(4)
   - eq:2 nets T:15~30°C I:-0.05~0.25M max 3n/3e
**8. Fe^[2+] + Diethylenetrinitrilopentaacetic acid (DTPA)** (metal_62 + ligand_6356) — ligand_def_HxL: H5L | 8 ent, 5 sp, 8 vlms (vlm_112678…vlm_112685)
   - species: beta_def_238(1) beta_def_516(1) beta_def_788(2) beta_def_812(3) beta_def_966(1)
   - eq:2 nets T:15~30°C I:-0.05~0.25M max 5n/8e
**9. Co^[2+] + Diethylenetrinitrilopentaacetic acid (DTPA)** (metal_33 + ligand_6356) — ligand_def_HxL: H5L | 8 ent, 3 sp, 8 vlms (vlm_112686…vlm_112693)
   - species: beta_def_516(2) beta_def_788(2) beta_def_812(4)
   - eq:2 nets T:15~30°C I:-0.05~0.25M max 3n/3e
**10. Cd^[2+] + Diethylenetrinitrilopentaacetic acid (DTPA)** (metal_26 + ligand_6356) — ligand_def_HxL: H5L | 8 ent, 3 sp, 8 vlms (vlm_112744…vlm_112751)
   - species: beta_def_516(2) beta_def_788(2) beta_def_812(4)
   - eq:2 nets T:15~30°C I:-0.05~0.25M max 3n/3e
**11. Mn^[2+] + Diethylenetrinitrilopentaacetic acid (DTPA)** (metal_94 + ligand_6356) — ligand_def_HxL: H5L | 7 ent, 3 sp, 7 vlms (vlm_112671…vlm_112677)
   - species: beta_def_516(1) beta_def_788(2) beta_def_812(4)
   - eq:2 nets T:15~30°C I:-0.05~0.25M max 3n/3e
**12. Fe^[3+] + Diethylenetrinitrilopentaacetic acid (DTPA)** (metal_61 + ligand_6356) — ligand_def_HxL: H5L | 7 ent, 3 sp, 7 vlms (vlm_112712…vlm_112718)
   - species: beta_def_788(2) beta_def_812(3) beta_def_966(2)
   - eq:3 nets T:15~30°C I:-0.05~0.25M max 3n/3e
**13. Bi^[3+] + Diethylenetrinitrilopentaacetic acid (DTPA)** (metal_21 + ligand_6356) — ligand_def_HxL: H5L | 7 ent, 4 sp, 7 vlms (vlm_112785…vlm_112791)
   - species: beta_def_739(1) beta_def_788(2) beta_def_812(3) beta_def_966(1)
   - eq:3 nets T:15~30°C I:-0.05~1.15M max 3n/3e
**14. Sm^[3+] + Diethylenetrinitrilopentaacetic acid (DTPA)** (metal_173 + ligand_6356) — ligand_def_HxL: H5L | 6 ent, 3 sp, 6 vlms (vlm_112588…vlm_112593)
   - species: beta_def_502(1) beta_def_788(1) beta_def_812(4)
   - eq:2 nets T:19~30°C I:-0.05~0.65M max 3n/2e
**15. Pb^[2+] + Diethylenetrinitrilopentaacetic acid (DTPA)** (metal_125 + ligand_6356) — ligand_def_HxL: H5L | 6 ent, 3 sp, 6 vlms (vlm_112760…vlm_112765)
   - species: beta_def_516(1) beta_def_788(1) beta_def_812(4)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 3n/3e
**16. Nd^[3+] + Diethylenetrinitrilopentaacetic acid (DTPA)** (metal_110 + ligand_6356) — ligand_def_HxL: H5L | 6 ent, 3 sp, 6 vlms (vlm_112582…vlm_112587)
   - species: beta_def_502(1) beta_def_788(1) beta_def_812(4)
   - eq:2 nets T:19~30°C I:-0.05~0.65M max 3n/2e
**17. Ga^[3+] + Diethylenetrinitrilopentaacetic acid (DTPA)** (metal_64 + ligand_6356) — ligand_def_HxL: H5L | 6 ent, 3 sp, 6 vlms (vlm_112772…vlm_112777)
   - species: beta_def_788(2) beta_def_812(2) beta_def_839(2)
   - eq:2 nets T:15~30°C I:-0.05~0.25M max 3n/3e
**18. Eu^[3+] + Diethylenetrinitrilopentaacetic acid (DTPA)** (metal_58 + ligand_6356) — ligand_def_HxL: H5L | 6 ent, 3 sp, 6 vlms (vlm_112594…vlm_112599)
   - species: beta_def_502(1) beta_def_788(1) beta_def_812(4)
   - eq:2 nets T:19~30°C I:-0.05~0.65M max 3n/2e
**19. Al^[3+] + Diethylenetrinitrilopentaacetic acid (DTPA)** (metal_5 + ligand_6356) — ligand_def_HxL: H5L | 6 ent, 3 sp, 6 vlms (vlm_112766…vlm_112771)
   - species: beta_def_788(2) beta_def_812(3) beta_def_966(1)
   - eq:2 nets T:15~30°C I:-0.05~0.25M max 3n/3e
**20. Yb^[3+] + Diethylenetrinitrilopentaacetic acid (DTPA)** (metal_206 + ligand_6356) — ligand_def_HxL: H5L | 5 ent, 2 sp, 5 vlms (vlm_112630…vlm_112634)
   - species: beta_def_788(1) beta_def_812(4)
   - eq:2 nets T:19~30°C I:-0.05~0.65M max 2n/1e

---

### Step 17: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_6356 AND c.beta_definition_id = beta_def_812 AND c.metal_id IN (metal_25, metal_92, metal_41, metal_208, metal_62, metal_61, metal_65, metal_112, metal_33, metal_94, metal_26, metal_125, metal_5, metal_64, metal_110, metal_58, metal_173, metal_206) AND s.temperature_c BETWEEN 20 AND 30 AND (s.solvent_name LIKE '%water%' OR s.solvent_name IS NULL))",
  "order_by": "c.metal_id ASC, s.temperature_c ASC, s.ionic_strength_mol_l ASC",
  "limit": 400
}
```

[summary]
## search_stability

*(no results)*

---
