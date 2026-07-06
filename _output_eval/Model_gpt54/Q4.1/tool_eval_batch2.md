# Q4.1 — Tool Results (batch 2)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Fe(II), Fe(III)",
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
  "name": "DMF, acetonitrile, THF, ethylene glycol, N,N-dimethylformamide, MeCN, tetrahydrofuran, 1,2-ethanediol",
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
  "name": "iron",
  "symbol": "Fe",
  "limit": 20
}
```

[summary]
## search_metals — 2 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_61 | Fe^[3+] | Fe | 3 | ✓ | [Fe+3] | InChI=1S/Fe/q+3 | beta_totN_128 | ligand_totN_406 | vlm_totN_1473 |
| metal_62 | Fe^[2+] | Fe | 2 | ✓ | [Fe+2] | InChI=1S/Fe/q+2 | beta_totN_57 | ligand_totN_217 | vlm_totN_667 |

---

### Step 5: `search_ligands`
**Args:**
```json
{
  "name": "dimethylformamide, formamide, acetonitrile, methyl cyanide, tetrahydrofuran, glycol, ethylene glycol, ethanediol",
  "limit": 50
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 6: `build_system_catalog`
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

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_61, metal_62) AND (c.ligand_name_SRD LIKE '%dimethylformamide%' OR c.ligand_name_SRD LIKE '%DMF%' OR c.ligand_name_SRD LIKE '%acetonitrile%' OR c.ligand_name_SRD LIKE '%MeCN%' OR c.ligand_name_SRD LIKE '%tetrahydrofuran%' OR c.ligand_name_SRD LIKE '%THF%' OR c.ligand_name_SRD LIKE '%ethylene glycol%' OR c.ligand_name_SRD LIKE '%ethanediol%' OR c.ligand_name_SRD LIKE '%ethane-1,2-diol%'))",
  "order_by": "c.metal_name_SRD, c.ligand_name_SRD, s.constant_value DESC",
  "limit": 50
}
```

[summary]
## search_stability

*(no results)*

---

### Step 9: `search_citations`
**Args:**
```json
{
  "where": "(la.citation LIKE '%dimethylformamide%' OR la.citation LIKE '%DMF%' OR la.citation LIKE '%acetonitrile%' OR la.citation LIKE '%MeCN%' OR la.citation LIKE '%tetrahydrofuran%' OR la.citation LIKE '%THF%' OR la.citation LIKE '%ethylene glycol%' OR la.citation LIKE '%ethanediol%')",
  "order_by": "la.shortcut",
  "limit": 50
}
```

[summary]
## search_citations

*(no results)*

---

### Step 10: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_61, metal_62) AND (c.ligand_name_SRD LIKE '%formamide%' OR c.ligand_name_SRD LIKE '%acetamide%' OR c.ligand_name_SRD LIKE '%urea%' OR c.ligand_name_SRD LIKE '%nitrile%' OR c.ligand_name_SRD LIKE '%dioxane%' OR c.ligand_name_SRD LIKE '%glyme%' OR c.ligand_name_SRD LIKE '%glycol%' OR c.ligand_name_SRD LIKE '%glycerol%'))",
  "order_by": "c.ligand_name_SRD, s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability — 10 row(s)

### `Fe^[3+]` + Hydroxyacetic acid (Glycolic acid) — 4 measurement(s)
metal_id: metal_61 | ligand_id: ligand_8640
ligand_HxL_def: HL | ligand_SMILES: O=C(O)CO

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_147409 | ref_eq_map_18185 | beta_def_812 | logK | 2.9 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (3.62, L, +inf) |
| vlm_147411 | ref_eq_map_18185 | beta_def_136 | logK | 2.41 | 25 | 1 | `[M(H-1L)] + [L] <=> [M(H-1L)L]` | *** | [L] | (3.62, L, +inf) |
| vlm_147412 | ref_eq_map_18185 | beta_def_140 | logK | 1.5 | 25 | 1 | `[M(H-1L)L] + [L] <=> [M(H-1L)L2]` | *** | [L] | (3.62, L, +inf) |
| vlm_147410 | ref_eq_map_18185 | beta_def_107 | logK | 1.31 | 25 | 1 | `[M(H-1L)] + [H] <=> [ML]` | *** |  |  |

### `Fe^[2+]` + Hydroxyacetic acid (Glycolic acid) — 1 measurement(s)
metal_id: metal_62 | ligand_id: ligand_8640
ligand_HxL_def: HL | ligand_SMILES: O=C(O)CO

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_147386 | ref_eq_map_18174 | beta_def_812 | logK | 1.33 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (3.62, L, +inf) |

### `Fe^[2+]` + Mercaptoacetic acid (Thioglycolic acid) — 2 measurement(s)
metal_id: metal_62 | ligand_id: ligand_8766
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)CS

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_150592 | ref_eq_map_19472 | beta_def_840 | logK | 10.92 | 25 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (10.11, L, +inf) |
| vlm_150593 | ref_eq_map_19472 | beta_def_966 | logK | 1.62 | 25 | 0 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |

### `Fe^[3+]` + Oxydiacetic acid (Diglycolic acid) — 1 measurement(s)
metal_id: metal_61 | ligand_id: ligand_8974
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)COCC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_155690 | ref_eq_map_21371 | beta_def_812 | logK | 5.04 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (3.94, L, +inf) |

### `Fe^[2+]` + Oxydiacetic acid (Diglycolic acid) — 2 measurement(s)
metal_id: metal_62 | ligand_id: ligand_8974
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)COCC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_155667 | ref_eq_map_21364 | beta_def_812 | logK | 2.56 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (3.94, L, +inf) |
| vlm_155668 | ref_eq_map_21364 | beta_def_779 | logK | 0.64 | 25 | 0.1 | `[M] + [HL] <=> [MHL]` | *** | [HL] | (2.82, HL, 3.94) |

---

### Step 11: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_61, metal_62) AND (c.ligand_name_SRD LIKE '%glycine%' OR c.ligand_name_SRD LIKE '%acetate%' OR c.ligand_name_SRD LIKE '%oxalate%' OR c.ligand_name_SRD LIKE '%malonate%' OR c.ligand_name_SRD LIKE '%propionate%' OR c.ligand_name_SRD LIKE '%formate%' OR c.ligand_name_SRD LIKE '%urea%' OR c.ligand_name_SRD LIKE '%acetamide%' OR c.ligand_name_SRD LIKE '%formamide%' OR c.ligand_name_SRD LIKE '%pyridine%' OR c.ligand_name_SRD LIKE '%imidazole%' OR c.ligand_name_SRD LIKE '%thiocyanate%' OR c.ligand_name_SRD LIKE '%azide%' OR c.ligand_name_SRD LIKE '%chloride%'))",
  "order_by": "c.ligand_name_SRD, s.constant_value DESC",
  "limit": 120
}
```

[summary]
## search_stability — 120 row(s)

### logK — 29 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 10 | 3 | 10~40 | 0~3 | *** | 7 |
| metal_61 | Fe^[3+] | ligand_6982 | Aminoacetohydroxamic acid (… | HL | NCC(=O)NO | 9 | 8 | 20~25 | 0.1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_10163 | Chloride ion | *** | *** | 9 | 2 | 25 | 0~4 | *** | 7 |
| metal_61 | Fe^[3+] | ligand_7944 | 2,3-Dihydroxypyridine (3-Hy… | HL | Oc1cccnc1O | 7 | 6 | 25 | 0.1~1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 6 | 3 | 25 | 0.5~3 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_6999 | Glycylglycinehydroxamic acid | HL | NCC(=O)NCC(=O)NO | 6 | 6 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7946 | 1-Butyl-2,3-dihydroxypyridi… | HL | CCCCn1cccc(O)c1=O | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8176 | 2-(2-Pyridylmethylenehydraz… | L | C(=N/Nc1ccccn1)\c1ccccn1 | 4 | 3 | 20~25 | 0~0.1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_7950 | 1,2-Diethyl-3,4-dihydroxypy… | HL | CCc1c(O)c(=O)ccn1CC | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7949 | 1,2-Dimethyl-3,4-dihydroxyp… | HL | Cc1c(O)c(=O)ccn1C | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8204 | 2,6-Di(2-pyridyl)pyridine (… | L | c1ccc(-c2cccc(-c3ccccn3)n2)nc1 | 3 | 2 | 25 | 0.1~0.5 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_7862 | 2-(2-Pyridyl)imidazole | L | c1ccc(-c2ncc[nH]2)nc1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7947 | 3,4-Dihydroxypyridine (3-Hy… | HL | Oc1ccncc1O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7863 | 4-(2-Pyridyl)imidazole | L | c1ccc(-c2c[nH]cn2)nc1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6763 | 6-Methylpyridine-2-carboxyl… | HL | Cc1cccc(C(=O)O)n1 | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7795 | 1,3-Diazole (Imidazole) | L | c1c[nH]cn1 | 2 | 2 | 30 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8081 | 2-(Aminomethyl)pyridine (2-… | L | NCc1ccccn1 | 2 | 2 | 30 | 0 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8112 | 2-(Methylaminomethyl)pyridi… | L | CNCc1ccccn1 | 2 | 2 | 30 | 0 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8054 | 2-(Methylsulfonamidomethyl)… | HL | CS(=O)(=O)NCc1ccccn1 | 2 | 2 | 30 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6780 | 4-Aminopyridine-2,6-dicarbo… | H2L | Nc1cc(C(=O)O)nc(C(=O)O)c1 | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6780 | 4-Aminopyridine-2,6-dicarbo… | H2L | Nc1cc(C(=O)O)nc(C(=O)O)c1 | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7000 | Glycylglycylglycinehydroxam… | HL | NCC(=O)NCC(=O)NCC(=O)NO | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7939 | 2-Hydroxypyridine (1,2-Dihy… | *** | *** | 1 | 1 | 25 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7941 | 3-Hydroxypyridine | HL | Oc1cccnc1 | 1 | 1 | 25 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7942 | 4-Hydroxypyridine (1,4-Dihy… | HL | Oc1ccncc1 | 1 | 1 | 25 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_10163 | Chloride ion | *** | *** | 1 | 1 | 25 | 0 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8209 | Ethylenedinitrilotetrakis(m… | L | c1ccc(CN(CCN(Cc2ccccn2)Cc2ccccn2)Cc2ccccn2)nc1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6372 | Glycylglycine (Diglycine) | HL | NCC(=O)NCC(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6372 | Glycylglycine (Diglycine) | HL | NCC(=O)NCC(=O)O | 1 | 1 | 20 | 1 | *** | 1 |

### ΔS — 7 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_62 | Fe^[2+] | ligand_8176 | 2-(2-Pyridylmethylenehydraz… | L | C(=N/Nc1ccccn1)\c1ccccn1 | 3 | 3 | 25 | 0 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_10163 | Chloride ion | *** | *** | 2 | 1 | 25 | 0~1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_8204 | 2,6-Di(2-pyridyl)pyridine (… | L | c1ccc(-c2cccc(-c3ccccn3)n2)nc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7862 | 2-(2-Pyridyl)imidazole | L | c1ccc(-c2ncc[nH]2)nc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7863 | 4-(2-Pyridyl)imidazole | L | c1ccc(-c2c[nH]cn2)nc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_8209 | Ethylenedinitrilotetrakis(m… | L | c1ccc(CN(CCN(Cc2ccccn2)Cc2ccccn2)Cc2ccccn2)nc1 | 1 | 1 | 25 | 0.1 | *** | 0 |

### ΔH — 8 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_62 | Fe^[2+] | ligand_8176 | 2-(2-Pyridylmethylenehydraz… | L | C(=N/Nc1ccccn1)\c1ccccn1 | 3 | 3 | 25 | 0 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 3 | 1 | 10~40 | 0 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_10163 | Chloride ion | *** | *** | 2 | 1 | 25 | 0~1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_8204 | 2,6-Di(2-pyridyl)pyridine (… | L | c1ccc(-c2cccc(-c3ccccn3)n2)nc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7862 | 2-(2-Pyridyl)imidazole | L | c1ccc(-c2ncc[nH]2)nc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7863 | 4-(2-Pyridyl)imidazole | L | c1ccc(-c2c[nH]cn2)nc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_10163 | Chloride ion | *** | *** | 1 | 1 | 25 | 0 | solid | 0 |
| metal_62 | Fe^[2+] | ligand_8209 | Ethylenedinitrilotetrakis(m… | L | c1ccc(CN(CCN(Cc2ccccn2)Cc2ccccn2)Cc2ccccn2)nc1 | 1 | 1 | 20 | 0.1 | *** | 0 |

---

### Step 12: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_61, metal_62) AND (c.ligand_name LIKE '%glycolic%' OR c.ligand_name LIKE '%diglycolic%'))",
  "order_by": "c.metal_name, c.ligand_name",
  "limit": 20
}
```

[summary]
## search_networks — 10 row(s)

> **Reference equilibrium networks** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### `Fe^[2+]` + Hydroxyacetic acid (Glycolic acid) — 1 network(s)
metal_id: metal_62 | ligand_id: ligand_8640 | ligand_def_HxL: HL | ligand_SMILES: O=C(O)CO

| beta_def | equation |
|----------|----------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_18224 | 1 | 0 | 16.5~31.5 | 0.775~1.225 | 1 | beta_def_812 | logK | 1.33 |

#### Reference-state network: ref_eq_net_18224 (1 nodes)
> First network — reference conditions (T 16.5~31.5 °C, I 0.775~1.225 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 1.33 |

### `Fe^[2+]` + Mercaptoacetic acid (Thioglycolic acid) — 2 network(s)
metal_id: metal_62 | ligand_id: ligand_8766 | ligand_def_HxL: H2L | ligand_SMILES: O=C(O)CS

| beta_def | equation |
|----------|----------|
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |
| beta_def_966 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_19525 | 1 | 0 | 20~30 | -0.05~0.25 | 1 | beta_def_840 | logK | 10.92 |
| ref_eq_net_19526 | 1 | 0 | 20~30 | -0.05~0.25 | 1 | beta_def_966 | logK | 1.62 |

#### Reference-state network: ref_eq_net_19525 (1 nodes)
> First network — reference conditions (T 20~30 °C, I -0.05~0.25 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` | logK | 10.92 |

### `Fe^[2+]` + Oxydiacetic acid (Diglycolic acid) — 1 network(s)
metal_id: metal_62 | ligand_id: ligand_8974 | ligand_def_HxL: H2L | ligand_SMILES: O=C(O)COCC(=O)O

| beta_def | equation |
|----------|----------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_779 | ``[M] + [HL] <=> [MHL]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_21422 | 2 | 1 | 20~30 | -0.05~0.25 | 2 | beta_def_779; beta_def_812 | logK | 0.64~2.56 |

#### Reference-state network: ref_eq_net_21422 (2 nodes)
> First network — reference conditions (T 20~30 °C, I -0.05~0.25 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_779 | ``[M] + [HL] <=> [MHL]`` | logK | 0.64 |
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 2.56 |

### `Fe^[3+]` + Hydroxyacetic acid (Glycolic acid) — 1 network(s)
metal_id: metal_61 | ligand_id: ligand_8640 | ligand_def_HxL: HL | ligand_SMILES: O=C(O)CO

| beta_def | equation |
|----------|----------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_107 | ``[M(H-1L)] + [H] <=> [ML]`` |
| beta_def_136 | ``[M(H-1L)] + [L] <=> [M(H-1L)L]`` |
| beta_def_140 | ``[M(H-1L)L] + [L] <=> [M(H-1L)L2]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_18235 | 4 | 5 | 16.5~31.5 | 0.775~1.225 | 4 | 4 diff beta_def | logK | 1.31~2.9 |

#### Reference-state network: ref_eq_net_18235 (4 nodes)
> First network — reference conditions (T 16.5~31.5 °C, I 0.775~1.225 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_107 | ``[M(H-1L)] + [H] <=> [ML]`` | logK | 1.31 |
| beta_def_140 | ``[M(H-1L)L] + [L] <=> [M(H-1L)L2]`` | logK | 1.5 |
| beta_def_136 | ``[M(H-1L)] + [L] <=> [M(H-1L)L]`` | logK | 2.41 |
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 2.9 |

### `Fe^[3+]` + Oxydiacetic acid (Diglycolic acid) — 1 network(s)
metal_id: metal_61 | ligand_id: ligand_8974 | ligand_def_HxL: H2L | ligand_SMILES: O=C(O)COCC(=O)O

| beta_def | equation |
|----------|----------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_21429 | 1 | 0 | 16.5~31.5 | 0.275~0.725 | 1 | beta_def_812 | logK | 5.04 |

#### Reference-state network: ref_eq_net_21429 (1 nodes)
> First network — reference conditions (T 16.5~31.5 °C, I 0.275~0.725 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 5.04 |

---
