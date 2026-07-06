# Q5.1.2 — Tool Results (batch 2)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Calcium, Zinc, Copper(II), Iron(III), Iron(II), Gadolinium, Aluminum, Lead, Cobalt(II), Cobalt(III), Nickel, Manganese(II), Magnesium",
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
  "name": "DTPA, diethylenetriaminepentaacetic acid",
  "limit": 10
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

### Step 7: `search_ligands`
**Args:**
```json
{
  "name": "pentetic acid, diethylenetriaminepentaacetate, H5DTPA, pentetate",
  "limit": 20
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 8: `search_similar_ligands`
**Args:**
```json
{
  "ligand_name": "pentetic acid",
  "top_k": 10
}
```

[summary]
## search_similar_ligands — 10 row(s)

**Query:** Diethylenetrinitrilopentaacetic acid (DTPA)

| ligand_id | ligand_name | smiles | HxL_canonical | family_score | similarity_score | tversky_query_in_target | tversky_target_in_query | diff_catalog_fun_group |
|---|---|---|---|---|---|---|---|---|
| ligand_6356 | Diethylenetrinitrilopentaacetic acid (DTPA) | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | H5L | — | — | — | — | *(query)* |
| ligand_6366 | Triethylenetetranitrilohexaacetic acid (TTHA) | O=C(O)CN(CCN(CCN(CC(=O)O)CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | H6L | 1 | 1 | 1 | 1 | carboxyl(+1); tertiary_amine(+1) |
| ligand_6367 | Tetraethylenepentanitriloheptaacetic acid (TPHA) | O=C(O)CN(CCN(CCN(CC(=O)O)CC(=O)O)CC(=O)O)CCN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | H7L | 1 | 1 | 1 | 1 | carboxyl(+2); tertiary_amine(+2) |
| ligand_6368 | Pentaethylenehexanitrilooctaacetic acid (PHOA) | O=C(O)CN(CCN(CCN(CCN(CC(=O)O)CC(=O)O)CC(=O)O)CC(=O)O)CCN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | H8L | 1 | 1 | 1 | 1 | carboxyl(+3); tertiary_amine(+3) |
| ligand_6277 | Ethylenedinitrilotetraacetic acid (EDTA) | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | H4L | 0.9677 | 0.9333 | 0.9396 | 0.9929 | carboxyl(-1); tertiary_amine(-1) |
| ligand_6370 | Nitrilotris(ethylenenitrilo)hexaacetic acid | O=C(O)CN(CCN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O)CC(=O)O | H6L | 1 | 0.875 | 0.9333 | 0.9333 | carboxyl(+1); tertiary_amine(+1) |
| ligand_6358 | Diethylenetrinitrilotetraacetic-N''-propanoic acid (DTTAP) | O=C(O)CCN(CCN(CCN(CC(=O)O)CC(=O)O)CC(=O)O)CC(=O)O | H5L | 0.9394 | 0.7895 | 0.974 | 0.8065 | no_diff_catalog_fun |
| ligand_6264 | N-(2-Hydroxyethyl)diethylenetrinitrilotetraacetic acid | O=C(O)CN(CCO)CCN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | H4L | 0.9394 | 0.7895 | 0.974 | 0.8065 | carboxyl(-1); hydroxyl(+1) |
| ligand_6275 | N-(2-Hydroxyethyl)ethylenedinitrilotriacetic acid (HEDTA) | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | H3L | 0.9394 | 0.7895 | 0.974 | 0.8065 | carboxyl(-2); hydroxyl(+1); tertiary_amine(-1) |
| ligand_6048 | N,N'-Bis(2-hydroxyethyl)ethylenedinitrilodiacetic acid | O=C(O)CN(CCO)CCN(CCO)CC(=O)O | H2L | 0.9394 | 0.7368 | 0.915 | 0.791 | carboxyl(-3); hydroxyl(+2); tertiary_amine(-1) |
| ligand_6309 | Ethylenedinitrilo-N,N'-di(3-propanoic)-N,N'-diacetic acid | O=C(O)CCN(CCN(CCC(=O)O)CC(=O)O)CC(=O)O | H4L | 0.9394 | 0.7368 | 0.915 | 0.791 | carboxyl(-1); tertiary_amine(-1) |

### Diff signature summary (89 ligand(s) with similarity > 0.5)
| group | <-2 | -2 | -1 | 0 | +1 | +2 | >+2 | avg_beta_counts_per_ligand |
|---|---|---|---|---|---|---|---|---|
| no_diff_catalog_fun | *** | *** | *** | 1 | *** | *** | *** | 33.0 |
| carboxyl | 38 | 16 | 29 | 1 | 3 | 1 | 1 | 37.4 |
| tertiary_amine | *** | 35 | 41 | 7 | 4 | 1 | 1 | 37.4 |
| hydroxyl | *** | *** | *** | *** | 8 | 7 | 1 | 29.3 |
| amide | *** | *** | *** | *** | 3 | 6 | *** | 18.6 |
| ether | *** | *** | *** | *** | 6 | 1 | *** | 51.1 |
| thioether | *** | *** | *** | *** | 3 | 1 | *** | 38.0 |
| thiol | *** | *** | *** | *** | 1 | 2 | *** | 20.0 |
| primary_amine | *** | *** | *** | *** | 1 | 2 | *** | 23.3 |
| aromatic_ring | *** | *** | *** | *** | *** | *** | 3 | 33.3 |
| phosphonate | *** | *** | *** | *** | 1 | 1 | *** | 11.5 |
| sulfonate | *** | *** | *** | *** | 1 | *** | *** | 8.0 |
| secondary_amine | *** | *** | *** | *** | 1 | *** | *** | 1.0 |
| ketone | *** | *** | *** | *** | 1 | *** | *** | 16.0 |

---

### Step 9: `build_system_catalog`
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

### Step 10: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_6356 AND s.constant_type LIKE '%log%')",
  "order_by": "s.constant_value DESC",
  "limit": 50
}
```

[summary]
## search_stability

*(no results)*

---

### Step 11: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_6356 AND c.beta_definition_id = beta_def_812)",
  "order_by": "s.constant_value DESC",
  "limit": 50
}
```

[summary]
## search_stability — 50 row(s)

### ΔS — 29 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_5 | Al^[3+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_81 | Lu^[3+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_206 | Yb^[3+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_192 | Tm^[3+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_55 | Er^[3+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_73 | Ho^[3+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_44 | Dy^[3+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_205 | Y^[3+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_179 | Tb^[3+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_65 | Gd^[3+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_58 | Eu^[3+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_173 | Sm^[3+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_139 | Pr^[3+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_110 | Nd^[3+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_27 | Ce^[3+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_92 | Mg^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_26 | Cd^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_177 | Sr^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_18 | Ba^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |

### ΔH — 1 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_5 | Al^[3+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 27 | 0.1 | *** | 0 |

### logK — 16 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_21 | Bi^[3+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 3 | 1 | 20~25 | 0.1~1 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 3 | 1 | 20~25 | 0.1 | *** | 3 |
| metal_55 | Er^[3+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_73 | Ho^[3+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_44 | Dy^[3+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_190 | Tl^[3+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_209 | Zr^[4+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_70 | Hf^[4+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_95 | Mn^[3+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_127 | Pd^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_74 | In^[3+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_64 | Ga^[3+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_31 | Cm^[3+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_6 | Am^[3+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_22 | Bk^[3+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |

---

### Step 12: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_6356"
}
```

[summary]
## inspect_card — Ligand | ligand_6356

**Name:** Diethylenetrinitrilopentaacetic acid (DTPA)  
**Formula:** C14H23N3O10 | **Class:** EDTA and derivatives  
**SMILES:** `O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O`  
**InChI:** `InChI=1S/C14H23N3O10/c18-10(19)5-15(1-3-16(6-11(20)21)7-12(22)23)2-4-17(8-13(24)25)9-14(26)27/h1-9H2,(H,18,19)(H,20,21)(H,22,23)(H,24,25)(H,26,27)`  
**HxL definition:** H5L  

**pKa values:** 8

| source_vlm | pKa | T (°C) | I (M) | From → To | Solvent | Method | Quality |
|------------|-----|--------|-------|-----------|---------|--------|---------|
| vlm_112470 | -9.90 | 25.0 | 0.1 | L → HL | *** | *** | *** |
| vlm_112484 | -8.40 | 25.0 | 0.1 | HL → H2L | *** | *** | *** |
| vlm_112522 | -1.60 | 25.0 | 0.1 | H5L → H6L | *** | *** | *** |
| vlm_112524 | -0.70 | 25.0 | 0.1 | H6L → H7L | *** | *** | *** |
| vlm_112526 | -0.10 | 25.0 | 0.1 | H7L → H8L | *** | *** | *** |
| vlm_112514 | 2.00 | 25.0 | 0.1 | H4L → H5L | *** | *** | *** |
| vlm_112506 | 2.70 | 25.0 | 0.1 | H3L → H4L | *** | *** | *** |
| vlm_112498 | 4.28 | 25.0 | 0.1 | H2L → H3L | *** | *** | *** |

**Partners:** 59 metal(s), 322 measurement(s) total

| metal_id | Metal | # meas |
|----------|-------|--------|
| metal_68 | H^[+] | 57 |
| metal_25 | Ca^[2+] | 11 |
| metal_185 | Th^[4+] | 9 |
| metal_92 | Mg^[2+] | 9 |
| metal_41 | Cu^[2+] | 9 |
| … | *(showing top 5 of 59)* | |

---
