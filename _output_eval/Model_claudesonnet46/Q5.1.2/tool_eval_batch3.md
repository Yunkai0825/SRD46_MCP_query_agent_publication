# Q5.1.2 — Tool Results (batch 3)

### Step 2: `search_ligands`
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

### Step 4: `build_system_catalog`
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

### Step 5: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_6356 AND s.constant_type = 'log_beta' AND s.reaction_type LIKE '%ML%')",
  "order_by": "s.constant_value DESC",
  "limit": 40
}
```

[summary]
## search_stability

*(no results)*

---
