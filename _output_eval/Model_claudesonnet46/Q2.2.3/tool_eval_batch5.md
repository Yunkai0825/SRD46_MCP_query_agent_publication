# Q2.2.3 — Tool Results (batch 5)

### Step 3: `search_metals`
**Args:**
```json
{
  "name": "hydrogen",
  "limit": 5
}
```

[summary]
## search_metals — 5 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_20 | BuHg^[+] | B | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_23 | BuNH_[3]^[+] | B | 1 |  | *** | *** | beta_totN_1 | ligand_totN_2 | vlm_totN_2 |
| metal_24 | C(NH_[2])_[3]^[+] | C | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_45 | Et_[2]NH_[2]^[+] | E2NH2 | 1 |  | *** | *** | beta_totN_1 | ligand_totN_1 | vlm_totN_1 |
| metal_48 | Et_[3]NH^[+] | E3NH | 1 |  | *** | *** | beta_totN_1 | ligand_totN_1 | vlm_totN_1 |

---

### Step 4: `search_ligands`
**Args:**
```json
{
  "name": "DTPA",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 5 SQL matches · showing 5 · limit 5

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

### Step 6: `build_system_catalog`
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

### Step 8: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT lc.ligand_id, lc.ligand_name_SRD, lc.formula, lc.ligand_class_name, COUNT(*) as pka_count, GROUP_CONCAT(ROUND(p.pKa, 2) ORDER BY p.pKa DESC) as pka_values FROM ligand_card lc JOIN ligand_pka_measured p ON lc.ligand_id = p.ligand_id GROUP BY lc.ligand_id, lc.ligand_name_SRD, lc.formula, lc.ligand_class_name HAVING COUNT(*) > 6 ORDER BY pka_count DESC"
}
```

[summary]
## execute_srd46_sql - 33 row(s)

| ligand_id | ligand_name_SRD | formula | ligand_class_name | pka_count | pka_values |
|-----------|-----------------|---------|-------------------|-----------|------------|
| ligand_7540 | 1,4,7,10,13,16,19,22,25,28,31-Undecaazacyclotritriacontane ([33]aneN11) | C22H55N11 | Aza-macrocycles | 11 | 9.79,9.48,9.02,8.64,8.06,6.44,4.49,3.58,2.76,2.26,-1.7 |
| ligand_7541 | 1,4,7,10,13,16,19,22,25,28,31,34-Dodecaazacyclohexatriacontane ([36]aneN12) | C24H60N12 | Aza-macrocycles | 11 | 9.75,9.65,8.12,7.82,5.66,4.27,3.58,2.62,2.3,-8.88,-8.96 |
| ligand_6368 | Pentaethylenehexanitrilooctaacetic acid (PHOA) | C26H44N6O16 | EDTA and derivatives | 10 | 10.85,9.96,8.85,6.2,4.48,3.57,2.52,2.02,-1.4,-1.7 |
| ligand_7253 | 2,5,8,11,14,17,20,23,26,29-Decaazatriacontane (Me2nonaen) | C20H52N10 | Aliphatic amines secondary N | 10 | 10.27,9.72,9.27,8.72,8.24,6.58,4.54,3.5,2.71,-1.5 |
| ligand_7539 | 1,4,7,10,13,16,19,22,25,28-Decaazacyclotriacontane ([30]aneN10) | C20H50N10 | Aza-macrocycles | 10 | 9.85,9.44,8.95,8.56,7.79,5.24,3.84,3.02,2.0,-1.8 |
| ligand_6367 | Tetraethylenepentanitriloheptaacetic acid (TPHA) | C22H37N5O14 | EDTA and derivatives | 9 | 10.48,9.78,8.19,4.69,3.75,2.66,2.07,-1.4,-1.7 |
| ligand_7252 | 2,5,8,11,14,17,20,23,26-Nonaazaheptacosane (Me2octaen) | C18H47N9 | Aliphatic amines secondary N | 9 | 10.58,9.72,9.35,8.7,7.93,5.1,3.88,2.94,2.74 |
| ligand_7538 | 1,4,7,10,13,16,19,22,25-Nonaazacycloheptacosane ([27]aneN9) | C18H45N9 | Aza-macrocycles | 9 | 9.59,9.4,8.77,8.27,6.37,4.22,3.24,2.31,-1.8 |
| ligand_6041 | N,N'-Bis(3-hydroxy-5-phosphomethyl-2-methyl-4-pyridylmethyl)ethylenedinitrilodi... | C22H32N4O14P2 | Amino Acids | 8 | 8.17,6.92,6.14,5.35,3.34,2.1,-11.2,-11.6 |
| ligand_6047 | N,N''-Bis(3-hydroxy-6-methyl-2-pyridinylmethyl)diethylenetrinitrilotriacetic ac... | C24H33N5O8 | Amino Acids | 8 | 10.95,8.9,6.21,5.19,3.49,2.25,-1.5,-12.1 |
| ligand_6356 | Diethylenetrinitrilopentaacetic acid (DTPA) | C14H23N3O10 | EDTA and derivatives | 8 | 4.28,2.7,2.0,-0.1,-0.7,-1.6,-8.4,-9.9 |
| ligand_6366 | Triethylenetetranitrilohexaacetic acid (TTHA) | C18H30N4O12 | EDTA and derivatives | 8 | 10.62,9.52,6.14,4.08,2.76,2.3,-1.5,-1.8 |
| ligand_7251 | 2,5,8,11,14,17,20,23-Octaazatetracosane (Me2heptaen) | C16H42N8 | Aliphatic amines secondary N | 8 | 10.39,9.77,9.28,8.61,6.68,4.44,3.31,2.93 |
| ligand_7254 | 1,3-Bis(2,5,8,11-tetraazaundecyl)benzene (MXTRIEN) | C20H42N8 | Aliphatic amines secondary N | 8 | 9.96,9.46,8.86,8.2,6.53,5.73,3.55,2.86 |
| ligand_7534 | 1,4,7,10,13,16,19,22-Octaazacyclotetracosane ([24]aneN8) | C16H40N8 | Aza-macrocycles | 8 | 9.65,9.33,8.76,7.87,4.55,3.42,2.71,-1.9 |
| ligand_7535 | 1,5,9,13,17,21,25,32-Octaazacyclodotriacontane ([32]aneN8) | C24H56N8 | Aza-macrocycles | 8 | 10.5,9.68,9.1,8.12,7.52,6.9,6.48,-10.68 |
| ligand_7543 | 1,5,9,13,17,21,28,32-Octaazabicyclo[11.11.11]pentatriacontane | C27H60N8 | Aza-macrocycles | 8 | 10.45,10.3,9.55,8.6,7.45,7.3,5.4,4.6 |
| ligand_8431 | Oxybis[ethylenenitrilobis(methylenephosphonic acid)] | C8H24N2O13P4 | Aminophosphorus acids | 8 | 10.72,10.1,7.52,6.41,5.66,4.73,2.72,-1.5 |
| ligand_8433 | Diethylenetrinitrilopentakis(methylenephosphonic acid) (DTPP) | C9H28N3O15P5 | Aminophosphorus acids | 8 | 10.1,8.15,7.17,6.38,5.5,4.45,2.8,-12.0 |
| ligand_9171 | myo-Inositol-hexa(dihydrogenphosphate) (Phytic acid) | C6H18O36P6 | Organophosphorus and arsenic acids | 8 | 10.53,9.02,7.82,6.13,4.88,2.49,2.0,-8.59 |
| ligand_6046 | N,N'-Bis(3-hydroxy-6-methyl-2-pyridinylmethyl)ethylenedinitrilodiacetic acid (E... | C20H26N4O6 | Amino Acids | 7 | 7.5,5.61,3.53,2.27,-1.1,-11.03,-11.79 |
| ligand_6125 | 7,19-Bis(carboxymethyl)-1,13(2,3)-tetrahydroxy-2,12,14,24-tetraoxo-3,7,11,15,19... | C32H42N6O12 | Aza macrocycles with carboxylic acids | 7 | 9.94,9.57,8.87,6.51,5.88,2.4,-11.2 |
| ligand_6359 | Diethylenetrinitrilopentapropanoic acid (DTPP) | C19H33N3O10 | EDTA and derivatives | 7 | 9.61,8.78,4.94,4.23,3.79,3.24,2.79 |
| ligand_6371 | 1,4-Bis[2,5,5-tris(carboxymethyl)-2,5-diazapentyl]benzene (PXED3A) | C24H34N4O12 | EDTA and derivatives | 7 | 10.5,9.83,5.74,4.77,3.0,2.29,-1.7 |
| ligand_7250 | 2,5,8,11,14,17,20-Heptaazaheneicosane (Me2hexaen) | C14H37N7 | Aliphatic amines secondary N | 7 | 10.22,9.6,8.94,8.05,4.75,3.37,2.45 |

... 8 more row(s) omitted

---
