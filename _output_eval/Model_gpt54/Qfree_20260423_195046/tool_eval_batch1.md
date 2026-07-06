# Qfree_20260423_195046 — Tool Results (batch 1)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Fe(II), Fe(III), H+",
  "limit": 10
}
```

[summary]
## search_metals

*(no results)*

---

### Step 4: `search_metals`
**Args:**
```json
{
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

### Step 5: `db_count_records`
**Args:**
```json
{
  "table": "metal_card",
  "where": "metal_name_SRD LIKE '%Fe%'"
}
```

[summary]
## db_count_records

| table | where | count |
|-------|-------|-------|
| metal_card | metal_name_SRD LIKE '%Fe%' | 2 |

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

### Step 7: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_62"
}
```

[summary]
[CATALOG]
## build_system_catalog — 20 pair(s), 88 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_156 | [M] + [H2L]^2 <=> [M(H2L)2] |  |
| beta_def_171 | [MH3L2] + [H] <=> [M(H2L)2] |  |
| beta_def_204 | [MHL2] + [H] <=> [M(HL)2] |  |
| beta_def_238 | [M(OH)2L] + [H] <=> [M(OH)L] + [H2O] |  |
| beta_def_249 | [M(OH)2L2] + [H] <=> [M(OH)L2] + [H2O] |  |
| beta_def_334 | [ML2(s)] <=> [M] + [L]^2 | solid |
| beta_def_374 | [M]^2 + [L]^2 <=> [M2(H-1L)2] + [H]^2 |  |
| beta_def_493 | [M2L] + [H] <=> [M2HL] |  |
| beta_def_515 | [M2(OH)L] + [H] <=> [M2L] + [H2O] |  |
| beta_def_516 | [ML] + [M] <=> [M2L] |  |
| beta_def_623 | [M3L2(H2O)8(s,vivianite)] <=> [M]^3 + [L]^2 + [H2O]^8 | solid |
| beta_def_732 | [M] + [H2L] <=> [MH2L] |  |
| beta_def_739 | [MHL] + [H] <=> [MH2L] |  |
| beta_def_751 | [MH2L] + [H] <=> [MH3L] |  |
| beta_def_756 | [M(HL)2] + [H] <=> [MH3L2] |  |
| beta_def_765 | [MH3L] + [H] <=> [MH4L] |  |
| beta_def_779 | [M] + [HL] <=> [MHL] |  |
| beta_def_788 | [ML] + [H] <=> [MHL] |  |
| beta_def_792 | [ML2] + [H] <=> [MHL2] |  |
| beta_def_800 | [MHL] + [L] <=> [MHL2] |  |
| beta_def_812 | [M] + [L] <=> [ML] |  |
| beta_def_839 | [M(OH)L] + [H] <=> [ML] + [H2O] |  |
| beta_def_840 | [M] + [L]^2 <=> [ML2] |  |
| beta_def_872 | [M] + [L]^3 <=> [ML3] |  |
| beta_def_894 | [M] + [L]^4 <=> [ML4] |  |
| beta_def_966 | [M(OH)L] + [H] <=> [ML] + [H2O] |  |
| beta_def_984 | [M(OH)L2] + [H] <=> [ML2] + [H2O] |  |

*(all species aqueous unless noted)*

**1. Fe^[2+] + Ammonia** (metal_62 + ligand_10103) — ligand_def_HxL: L | 32 ent, 4 sp, 32 vlms (vlm_173131…vlm_173162)
   - species: beta_def_812(8) beta_def_840(8) beta_def_872(8) beta_def_894(8)
   - eq:6 nets T:19~30°C I:-0.05~6.15M max 4n/6e
**2. Fe^[2+] + Aminoacetic acid (Glycine)** (metal_62 + ligand_5760) — ligand_def_HxL: HL | 14 ent, 3 sp, 14 vlms (vlm_93747…vlm_93760)
   - species: beta_def_812(11) beta_def_840(2) beta_def_872(1)
   - eq:7 nets T:5~45°C I:-0.15~3.15M max 3n/3e
**3. Fe^[2+] + Hydroxide ion** (metal_62 + ligand_10076) — ligand_def_HxL: *** | 13 ent, 5 sp, 13 vlms (vlm_170672…vlm_170684)
   - species: beta_def_334(1) beta_def_812(5) beta_def_840(3) beta_def_872(3) beta_def_894(1)
   - eq:3 nets T:19~30°C I:-0.15~1.15M max 5n/10e
**4. Fe^[2+] + L-2-Amino-3-hydroxypropanoic acid (Serine)** (metal_62 + ligand_5828) — ligand_def_HxL: HL | 12 ent, 3 sp, 12 vlms (vlm_96539…vlm_96550)
   - species: beta_def_812(6) beta_def_840(5) beta_def_872(1)
   - eq:4 nets T:15~41°C I:-0.05~3.15M max 3n/3e
**5. Fe^[2+] + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid)** (metal_62 + ligand_9058) — ligand_def_HxL: H3L | 11 ent, 5 sp, 11 vlms (vlm_157619…vlm_157629)
   - species: beta_def_374(1) beta_def_732(1) beta_def_779(4) beta_def_800(1) beta_def_812(4)
   - eq:5 nets T:15~41°C I:-0.05~3.15M max 5n/9e
**6. Fe^[2+] + Pyridine-2,6-diphosphonic acid (2,6-PDPA)** (metal_62 + ligand_8434) — ligand_def_HxL: H4L | 10 ent, 10 sp, 10 vlms (vlm_143982…vlm_143991)
   - species: beta_def_171(1) beta_def_204(1) beta_def_238(1) beta_def_739(1) beta_def_756(1) beta_def_788(1) beta_def_792(1) beta_def_812(1) beta_def_840(1) beta_def_966(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 10n/32e
**7. Fe^[2+] + 2-(2-Pyridylmethylenehydrazino)pyridine (Pyridine-2-aldehyde 2'-pyridylhydrazone)** (metal_62 + ligand_8176) — ligand_def_HxL: L | 10 ent, 3 sp, 10 vlms (vlm_138956…vlm_138965)
   - species: beta_def_249(3) beta_def_840(4) beta_def_984(3)
   - eq:2 nets T:15~30°C I:-0.05~0.25M max 3n/2e
**8. Fe^[2+] + 2,2'-Bipyridyl** (metal_62 + ligand_8156) — ligand_def_HxL: L | 10 ent, 3 sp, 10 vlms (vlm_138563…vlm_138572)
   - species: beta_def_812(2) beta_def_840(1) beta_def_872(7)
   - eq:3 nets T:19~35°C I:-0.15~1.15M max 3n/3e
**9. Fe^[2+] + Ethylenediamine** (metal_62 + ligand_7029) — ligand_def_HxL: L | 9 ent, 3 sp, 9 vlms (vlm_122341…vlm_122349)
   - species: beta_def_812(3) beta_def_840(3) beta_def_872(3)
   - eq:1 nets T:16.5~31.5°C I:0.775~1.225M max 3n/3e
**10. Fe^[2+] + 1,4-Bis[2,5,5-tris(carboxymethyl)-2,5-diazapentyl]benzene (PXED3A)** (metal_62 + ligand_6371) — ligand_def_HxL: H6L | 9 ent, 9 sp, 9 vlms (vlm_113386…vlm_113394)
   - species: beta_def_493(1) beta_def_515(1) beta_def_516(1) beta_def_739(1) beta_def_751(1) beta_def_765(1) beta_def_788(1) beta_def_812(1) beta_def_839(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 9n/28e
**11. Fe^[2+] + L-2-Amino-3-hydroxybutanoic acid (Threonine)** (metal_62 + ligand_5829) — ligand_def_HxL: HL | 9 ent, 2 sp, 9 vlms (vlm_96713…vlm_96721)
   - species: beta_def_812(5) beta_def_840(4)
   - eq:3 nets T:15~41°C I:-0.05~1.15M max 2n/1e
**12. Fe^[2+] + Diethylenetrinitrilopentaacetic acid (DTPA)** (metal_62 + ligand_6356) — ligand_def_HxL: H5L | 8 ent, 5 sp, 8 vlms (vlm_112678…vlm_112685)
   - species: beta_def_238(1) beta_def_516(1) beta_def_788(2) beta_def_812(3) beta_def_966(1)
   - eq:2 nets T:15~30°C I:-0.05~0.25M max 5n/8e
**13. Fe^[2+] + L-2-Amino-3-(3-indolyl)propanoic acid (Tryptophan)** (metal_62 + ligand_5907) — ligand_def_HxL: HL | 8 ent, 3 sp, 8 vlms (vlm_99130…vlm_99137)
   - species: beta_def_812(4) beta_def_840(3) beta_def_872(1)
   - eq:2 nets T:12.5~31.5°C I:0.775~3.225M max 3n/3e
**14. Fe^[2+] + Hydrogen phosphate (Phosphoric acid)** (metal_62 + ligand_10113) — ligand_def_HxL: H3L | 7 ent, 5 sp, 7 vlms (vlm_174445…vlm_174451)
   - species: beta_def_156(1) beta_def_171(1) beta_def_623(3) beta_def_732(1) beta_def_779(1)
   - eq:2 nets T:19~30°C I:-0.05~3.15M max 4n/4e
**15. Fe^[2+] + 5-Methyl-1,10-phenanthroline** (metal_62 + ligand_8193) — ligand_def_HxL: L | 7 ent, 3 sp, 7 vlms (vlm_139442…vlm_139448)
   - species: beta_def_812(2) beta_def_840(1) beta_def_872(4)
   - eq:2 nets T:17~30°C I:-0.15~0.25M max 3n/3e
**16. Fe^[2+] + 1,10-Phenanthroline (Dipyridino[a,c]benzene)** (metal_62 + ligand_8191) — ligand_def_HxL: L | 7 ent, 3 sp, 7 vlms (vlm_139266…vlm_139272)
   - species: beta_def_812(2) beta_def_840(1) beta_def_872(4)
   - eq:2 nets T:19~30°C I:-0.15~0.25M max 3n/3e
**17. Fe^[2+] + 3,7,11,15-Tetraaza-5,13(2)-dihydroxy-5,13(5)-dimethyl-1,9(2,6)-dipyridina-5,13(1,3)-dibenzenacyclohexadecaphane ([24]RBPyBC)** (metal_62 + ligand_7673) — ligand_def_HxL: H2L | 7 ent, 7 sp, 7 vlms (vlm_132581…vlm_132587)
   - species: beta_def_493(1) beta_def_515(1) beta_def_516(1) beta_def_739(1) beta_def_751(1) beta_def_788(1) beta_def_812(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 7n/15e
**18. Fe^[2+] + Pyridine-2-phosphonic-6-carboxylic acid (2PP6C)** (metal_62 + ligand_6770) — ligand_def_HxL: H3L | 7 ent, 7 sp, 7 vlms (vlm_119188…vlm_119194)
   - species: beta_def_204(1) beta_def_238(1) beta_def_788(1) beta_def_792(1) beta_def_812(1) beta_def_840(1) beta_def_966(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 7n/14e
**19. Fe^[2+] + Nitrilotriacetic acid (NTA)** (metal_62 + ligand_6165) — ligand_def_HxL: H3L | 7 ent, 3 sp, 7 vlms (vlm_105495…vlm_105501)
   - species: beta_def_812(3) beta_def_840(2) beta_def_966(2)
   - eq:3 nets T:15~30°C I:-0.05~1.15M max 3n/2e
**20. Fe^[2+] + Iminobis(methylene-2-pyridine) (Di-2-picolylamine)(DPA)** (metal_62 + ligand_8174) — ligand_def_HxL: L | 6 ent, 2 sp, 6 vlms (vlm_138896…vlm_138901)
   - species: beta_def_812(3) beta_def_840(3)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 2n/1e

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_62)",
  "order_by": "c.ligand_name_SRD ASC, s.constant_type ASC, s.constant_value DESC",
  "limit": 300
}
```

[summary]
## search_stability — 200 row(s)

### logK — 74 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_62 | Fe^[2+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 11 | 5 | 20~37 | 0.1~3 | *** | 5 |
| metal_62 | Fe^[2+] | ligand_6371 | 1,4-Bis[2,5,5-tris(carboxym… | H6L | O=C(O)CN(CCN(CC(=O)O)Cc1ccc(CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O)cc1)CC(=O)O | 9 | 9 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7673 | 3,7,11,15-Tetraaza-5,13(2)-… | H2L | Cc1cc2c(O)c(c1)CNCc1cccc(n1)CNCc1cc(C)cc(c1O)CNCc1cccc(n1)CNC2 | 7 | 7 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8156 | 2,2'-Bipyridyl | L | c1ccc(-c2ccccn2)nc1 | 6 | 3 | 25~30 | 0~1 | *** | 3 |
| metal_62 | Fe^[2+] | ligand_8191 | 1,10-Phenanthroline (Dipyri… | L | c1cnc2c(c1)ccc1cccnc12 | 5 | 3 | 25 | 0~0.1 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_9083 | (Ethanediylidenetetrathio)t… | H4L | O=C(O)CSC(SCC(=O)O)C(SCC(=O)O)SCC(=O)O | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7645 | 1,13-Dioxa-4,7,10,16,19,22-… | L | C1CNCCOCCNCCNCCNCCOCCNCCN1 | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7771 | 1,2-Diazole (Pyrazole) | L | c1cn[nH]c1 | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_9337 | 1,2-Dihydroxybenzene (Catec… | H2L | Oc1ccccc1O | 4 | 3 | 25 | 0.1~1 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_8176 | 2-(2-Pyridylmethylenehydraz… | L | C(=N/Nc1ccccn1)\c1ccccn1 | 4 | 3 | 20~25 | 0~0.1 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_6109 | 1,4,8,11-Tetraazacyclotetra… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCCN(CC(=O)O)CC1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6760 | 1,4-Diazine-2-carboxylic ac… | HL | O=C(O)c1cnccn1 | 3 | 3 | 25 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_9759 | 2,3-Dimercaptopropanol (BAL) | H2L | OCC(S)CS | 3 | 3 | 30 | 0.1 | solid | 1 |
| metal_62 | Fe^[2+] | ligand_8204 | 2,6-Di(2-pyridyl)pyridine (… | L | c1ccc(-c2cccc(-c3ccccn3)n2)nc1 | 3 | 2 | 25 | 0.1~0.5 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_8071 | 2-(2-Pyridyl)-1,3-thiazole | L | c1ccc(-c2nccs2)nc1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7862 | 2-(2-Pyridyl)imidazole | L | c1ccc(-c2ncc[nH]2)nc1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8341 | 2-Amino-2-propylphosphonic … | H2L | CC(C)(N)P(=O)(O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8192 | 2-Methyl-1,10-phenanthroline | L | Cc1ccc2ccc3cccnc3c2n1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8072 | 4-(2-Pyridyl)-1,3-thiazole | L | c1ccc(-c2cscn2)nc1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7863 | 4-(2-Pyridyl)imidazole | L | c1ccc(-c2c[nH]cn2)nc1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6333 | (2-Hydroxytrimethylene)dini… | H4L | O=C(O)CN(CC(=O)O)CC(O)CN(CC(=O)O)CC(=O)O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_9064 | (Carboxymethoxy)propanedioi… | H3L | O=C(O)COC(C(=O)O)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_9015 | (Ethylenedithio)diacetic ac… | H2L | O=C(O)CSCCSCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_9467 | 1,2-Dihydroxynaphthalene-4-… | H3L | O=S(=O)(O)c1cc(O)c(O)c2ccccc12 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6751 | 1,2-Phenylenedinitrilotetra… | H4L | O=C(O)CN(CC(=O)O)c1ccccc1N(CC(=O)O)CC(=O)O | 2 | 2 | 25 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7795 | 1,3-Diazole (Imidazole) | L | c1c[nH]cn1 | 2 | 2 | 30 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7530 | 1,4,7,10,13,16,19-Heptaazac… | L | C1CNCCNCCNCCNCCNCCNCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6102 | 1,4,7,10-Tetraazacyclododec… | H4L | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6104 | 1,4,7,10-Tetraazacyclotride… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 2 | 1 | 25 | 0.1~1 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_7212 | 1,4,7-Triazaheptane (Diethy… | L | NCCNCCN | 2 | 2 | 25 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7614 | 1,4-Dioxa-7,10,13-triazacyc… | L | C1CNCCOCCOCCNCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7616 | 1,4-Dioxa-7,10,14-triazacyc… | L | C1CNCCNCCOCCOCCNC1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6068 | 1,4-Dioxa-7,11-diazacyclotr… | H2L | O=C(O)CN1CCCN(CC(=O)O)CCOCCOCC1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_10035 | 1-(4-Sulfobenzo[1,2-d]-2,3-… | HL | NC(=S)N/N=C1\Nc2ccc(S(=O)(=O)O)cc2C1=O | 2 | 2 | 37 | 0.15 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_10036 | 1-(N-Methyl-4-sulfobenzo[1,… | HL | CN1/C(=N\NC(N)=S)C(=O)c2cc(S(=O)(=O)O)ccc21 | 2 | 2 | 37 | 0.15 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6082 | 1-Oxa-4,7,10-triazacyclodod… | H2L | O=C(O)CN1CCNCCN(CC(=O)O)CCOCC1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6084 | 1-Oxa-4,7,10-triazacyclodod… | H3L | O=C(O)CN1CCOCCN(CC(=O)O)CCN(CC(=O)O)CC1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7739 | 1-Thia-4,7-diazacyclononane… | L | C1CNCCSCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8208 | 2,4,6-Tri(2-pyridyl)-1,3,5-… | L | c1ccc(-c2nc(-c3ccccn3)nc(-c3ccccn3)n2)nc1 | 2 | 1 | 22~25 | 0.1~0.5 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_8081 | 2-(Aminomethyl)pyridine (2-… | L | NCc1ccccn1 | 2 | 2 | 30 | 0 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8112 | 2-(Methylaminomethyl)pyridi… | L | CNCc1ccccn1 | 2 | 2 | 30 | 0 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_9946 | 2-Mercapto-4,5,6-trioxoperh… | H3L | O=C1NC(=S)NC(=O)C1=NO | 2 | 1 | 25 | 0.1~0.5 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_9384 | 3,4,5-Trihydroxybenzoic aci… | H4L | O=C(O)c1cc(O)c(O)c(O)c1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7491 | 3,7,11-Triaza-1(2,6)-pyridi… | L | c1cc2nc(c1)CNCCCNCCCNC2 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8217 | 3-Hydrazinobenzo[d]-1,2-dia… | L | NNc1nncc2ccccc12 | 2 | 2 | 37 | 0.15 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6780 | 4-Aminopyridine-2,6-dicarbo… | H2L | Nc1cc(C(=O)O)nc(C(=O)O)c1 | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8196 | 5,6-Dimethyl-1,10-phenanthr… | L | Cc1c(C)c2cccnc2c2ncccc12 | 2 | 2 | 25 | 0~0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_9945 | 1,3-Dimethyl-2,4,5,6-tetrao… | HL | CN1C(=O)C(=NO)C(=O)N(C)C1=O | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6071 | 1,4,10,13-Tetraoxa-7,16-dia… | H2L | O=C(O)CN1CCOCCOCCN(CC(=O)O)CCOCCOCC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6070 | 1,4,10-Trioxa-7,13-diazacyc… | H2L | O=C(O)CN1CCOCCOCCN(CC(=O)O)CCOCC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7500 | 1,4,7,10,13-Pentaazacyclohe… | L | C1CNCCNCCNCCNCCNC1 | 1 | 1 | 35 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6067 | 1,4-Dioxa-7,10-diazacyclodo… | H2L | O=C(O)CN1CCOCCOCCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6069 | 1,7-Dioxa-4,10-diazacyclodo… | H2L | O=C(O)CN1CCOCCN(CC(=O)O)CCOCC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_9943 | 1-Methyl-2,4,5,6-tetraoxope… | H2L | CN1C(=O)NC(=O)/C(=N/O)C1=O | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7618 | 1-Oxa-4,7,10,13-tetraazacyc… | L | C1CNCCNCCOCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7569 | 1-Oxa-4,7-diazacyclononane … | L | C1CNCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6064 | 1-Oxa-4,7-diazacyclononane-… | H2L | O=C(O)CN1CCOCCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7751 | 1-Thia-4,7,10-triazacyclodo… | L | C1CNCCSCCNCCN1 | 1 | 1 | 35 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7755 | 1-Thia-4,7,11,14-tetraazacy… | L | C1CNCCNCCSCCNCCNC1 | 1 | 1 | 35 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_9942 | 2,4,5,6-Tetraoxoperhydro-1,… | H3L | O=C1NC(=O)C(=NO)C(=O)N1 | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5769 | 2-Amino-2-methylpropanoic a… | HL | CC(C)(N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8198 | 2-Chloro-1,10-phenanthroline | L | Clc1ccc2ccc3cccnc3c2n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_9284 | 2-Hydroxy-5-sulfobenzoic ac… | H3L | O=C(O)c1cc(S(=O)(=O)O)ccc1O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8693 | 2-Oxopropanoic acid (Pyruvi… | HL | CC(=O)C(=O)O | 1 | 1 | 25 | 3 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7508 | 3,6,10,13-Tetraaza-1(2,6)-p… | L | c1cc2nc(c1)CNCCNCCCNCCNC2 | 1 | 1 | 35 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7489 | 3,6,9-Triaza-1(2,6)-pyridin… | L | c1cc2nc(c1)CNCCNCCNC2 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5788 | 3-Aminopropanoic acid (beta… | HL | NCCC(=O)O | 1 | 1 | 25 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8216 | 3-Hydrazino-6{2-[3-(1,1-dim… | L | CC(C)(C)NCC(O)COc1ccccc1-c1ccc(NN)nn1 | 1 | 1 | 37 | 0.15 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7490 | 4,7,11-Triaza-1(2,6)-pyrini… | L | c1cc2nc(c1)CNCCNCCCNC2 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8195 | 4,7-Dimethyl-1,10-phenanthr… | L | Cc1ccnc2c1ccc1c(C)ccnc12 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7661 | 5-(2-Hydroxyphenyl)-1,4,8,1… | HL | Oc1ccccc1C1CCNCCNCCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |

### ΔH — 10 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_62 | Fe^[2+] | ligand_8176 | 2-(2-Pyridylmethylenehydraz… | L | C(=N/Nc1ccccn1)\c1ccccn1 | 3 | 3 | 25 | 0 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7212 | 1,4,7-Triazaheptane (Diethy… | L | NCCNCCN | 2 | 2 | 25 | 0.1~1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_8156 | 2,2'-Bipyridyl | L | c1ccc(-c2ccccn2)nc1 | 2 | 1 | 20~30 | 0.1~1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_8191 | 1,10-Phenanthroline (Dipyri… | L | c1cnc2c(c1)ccc1cccnc12 | 1 | 1 | 20 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_8204 | 2,6-Di(2-pyridyl)pyridine (… | L | c1ccc(-c2cccc(-c3ccccn3)n2)nc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7862 | 2-(2-Pyridyl)imidazole | L | c1ccc(-c2ncc[nH]2)nc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7863 | 4-(2-Pyridyl)imidazole | L | c1ccc(-c2c[nH]cn2)nc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_8196 | 5,6-Dimethyl-1,10-phenanthr… | L | Cc1c(C)c2cccnc2c2ncccc12 | 1 | 1 | 25 | 0 | *** | 0 |

### ΔS — 10 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_62 | Fe^[2+] | ligand_8176 | 2-(2-Pyridylmethylenehydraz… | L | C(=N/Nc1ccccn1)\c1ccccn1 | 3 | 3 | 25 | 0 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7212 | 1,4,7-Triazaheptane (Diethy… | L | NCCNCCN | 2 | 2 | 25 | 1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_8156 | 2,2'-Bipyridyl | L | c1ccc(-c2ccccn2)nc1 | 2 | 1 | 25 | 0.1~1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_8191 | 1,10-Phenanthroline (Dipyri… | L | c1cnc2c(c1)ccc1cccnc12 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_8204 | 2,6-Di(2-pyridyl)pyridine (… | L | c1ccc(-c2cccc(-c3ccccn3)n2)nc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7862 | 2-(2-Pyridyl)imidazole | L | c1ccc(-c2ncc[nH]2)nc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7863 | 4-(2-Pyridyl)imidazole | L | c1ccc(-c2c[nH]cn2)nc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_8196 | 5,6-Dimethyl-1,10-phenanthr… | L | Cc1c(C)c2cccnc2c2ncccc12 | 1 | 1 | 25 | 0 | *** | 0 |

---

### Step 9: `search_pka_ligands`
**Args:**
```json
{
  "where": "(lc.ligand_id IN (ligand_6165, ligand_6277, ligand_6301, ligand_8872, ligand_8873, ligand_8465, ligand_9257, ligand_9358, ligand_9873, ligand_8126))",
  "order_by": "lc.ligand_name_SRD ASC, p.pKa ASC",
  "limit": 200
}
```

[summary]
## search_pka_ligands — 25 row(s)

| ligand_id | ligand_name | HxL_def | formula | smiles | pH_ladder | T°C_range | I(M)_range | similarity_score |
|-----------|-------------|---------|---------|--------|-----------|-----------|------------|------------------|
| ligand_9358 | 1,2-Dihydroxybenzene-3,5-disulfonic acid (Tiron) | H4L | C6H6O8S2 | O=S(=O)(O)c1cc(O)c(O)c(S(=O)(=O)O)c1 | −∞; HL (M_tot_18); (-12.5, vlm_161952); L (M_tot_1); (7.62, vlm_161957); HL (M_tot_18); +∞ | 25 | 0.1 | *** |
| ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | H2L | C7H6O3 | O=C(O)c1ccccc1O | −∞; HL (M_tot_37); (-13.4, vlm_160211); L (M_tot_3); (2.8, vlm_160226); HL (M_tot_37); +∞ | 25 | 0.1 | *** |
| ligand_8126 | 8-Hydroxyquinoline (8-Quinolinol)(Oxine) | HL | C9H7N1O1 | Oc1cccc2cccnc12 | −∞; H2L (M_tot_1); (4.97, vlm_137922); HL (M_tot_2); (9.65, vlm_137913); L (M_tot_24); +∞ | 25 | 0.1 | *** |
| ligand_9873 | Acetohydroxamic acid | HL | C2H5N1O2 | CC(=O)NO | −∞; HL (M_tot_1); (9.29, vlm_168403); L (M_tot_19); +∞ | 25 | 0.1 | *** |
| ligand_8872 | Ethanedioic acid (Oxalic acid) | H2L | C2H2O4 | O=C(O)C(=O)O | −∞; H2L (M_tot_1); (-1.2, vlm_151532); HL (M_tot_7); (3.8, vlm_151494); L (M_tot_56); +∞ | 25 | 0.1 | *** |
| ligand_8465 | Ethanoic acid (Acetic acid) | HL | C2H4O2 | CC(=O)O | −∞; HL (M_tot_2); (4.56, vlm_144406); L (M_tot_69); +∞ | 25 | 0.1 | *** |
| ligand_6277 | Ethylenedinitrilotetraacetic acid (EDTA) | H4L | C10H16N2O8 | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | −∞; H5L (M_tot_1); (-1.5, vlm_108289); H4L (M_tot_2); (2, vlm_108282); H3L (M_tot_2); (2.69, vlm_108272); H2L (M_tot_1); (6.13, vlm_108254); HL (M_tot_7); (9.52, vlm_108224); L (M_tot_70); +∞ | 25 | 0.1 | *** |
| ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | C6H9N1O6 | O=C(O)CN(CC(=O)O)CC(=O)O | −∞; H3L (M_tot_1); (-1.81, vlm_105204); H2L (M_tot_2); (-1, vlm_105223); H3L (M_tot_1); (2.52, vlm_105186); HL (M_tot_2); (9.46, vlm_105158); L (M_tot_68); +∞ | 25 | 0.1 | *** |
| ligand_8873 | Propanedioic acid (Malonic acid) | H2L | C3H4O4 | O=C(O)CC(=O)O | −∞; H2L (M_tot_2); (2.65, vlm_151949); HL (M_tot_26); (5.27, vlm_151918); L (M_tot_50); +∞ | 25 | 0.1 | *** |
| ligand_6301 | trans-1,2-Cyclohexylenedinitrilotetraacetic acid (CDTA) | H4L | C14H22N2O8 | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | −∞; HL (M_tot_5); (-12.3, vlm_109614); L (M_tot_56); (2.4, vlm_109637); H3L (M_tot_1); (3.49, vlm_109632); H2L (M_tot_1); (6.07, vlm_109623); HL (M_tot_5); +∞ | 25 | 0.1 | *** |

---

### Step 10: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND c.ligand_id IN (ligand_6165, ligand_6277, ligand_6301, ligand_9358, ligand_9257, ligand_8872, ligand_8873, ligand_8465, ligand_9873, ligand_8126))",
  "order_by": "c.ligand_name_SRD ASC, s.constant_type ASC, s.constant_value DESC",
  "limit": 300
}
```

[summary]
## search_stability — 139 row(s)

### logK — 10 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_9358 | 1,2-Dihydroxybenzene-3,5-di… | H4L | O=S(=O)(O)c1cc(O)c(O)c(S(=O)(=O)O)c1 | 16 | 4 | 20~25 | 0.1~1 | *** | 4 |
| metal_61 | Fe^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 14 | 8 | 20~25 | 0.1~1 | *** | 4 |
| metal_61 | Fe^[3+] | ligand_8126 | 8-Hydroxyquinoline (8-Quino… | HL | Oc1cccc2cccnc12 | 13 | 4 | 25 | 0~1 | solid | 4 |
| metal_61 | Fe^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 12 | 5 | 20~25 | 0.1~3 | *** | 5 |
| metal_61 | Fe^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 11 | 3 | 20~25 | 0~3 | *** | 7 |
| metal_61 | Fe^[3+] | ligand_9873 | Acetohydroxamic acid | HL | CC(=O)NO | 8 | 3 | 20~25 | 0.1~2 | *** | 4 |
| metal_61 | Fe^[3+] | ligand_8873 | Propanedioic acid (Malonic … | H2L | O=C(O)CC(=O)O | 8 | 3 | 25 | 0.1~1 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 6 | 4 | 25 | 0.1~1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 6 | 4 | 20~25 | 0.1~1 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 5 | 3 | 25 | 0.5~3 | *** | 3 |

### ΔH — 8 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 4 | 4 | 25 | 0.1~1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 4 | 4 | 25 | 0.1~1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 3 | 3 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8873 | Propanedioic acid (Malonic … | H2L | O=C(O)CC(=O)O | 3 | 3 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 1 | 25 | 1~3 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 2 | 2 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9873 | Acetohydroxamic acid | HL | CC(=O)NO | 1 | 1 | 25 | 2 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 0 |

### ΔS — 8 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 4 | 4 | 20~25 | 0.1~1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 4 | 4 | 25 | 0.1~1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 3 | 3 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8873 | Propanedioic acid (Malonic … | H2L | O=C(O)CC(=O)O | 3 | 3 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 1 | 25 | 1~3 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 2 | 2 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9873 | Acetohydroxamic acid | HL | CC(=O)NO | 1 | 1 | 25 | 2 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |

---

### Step 11: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_62 AND c.ligand_id IN (ligand_6165, ligand_6277, ligand_6301, ligand_9358, ligand_9257, ligand_8872, ligand_8873, ligand_8465, ligand_9873, ligand_8126))",
  "order_by": "c.ligand_name_SRD ASC, s.constant_type ASC, s.constant_value DESC",
  "limit": 300
}
```

[summary]
## search_stability — 29 row(s)

### logK — 8 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_62 | Fe^[2+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 7 | 3 | 20~25 | 0.1~1 | *** | 3 |
| metal_62 | Fe^[2+] | ligand_8873 | Propanedioic acid (Malonic … | H2L | O=C(O)CC(=O)O | 3 | 2 | 25 | 1 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_9873 | Acetohydroxamic acid | HL | CC(=O)NO | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 2 | 2 | 25 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 1 | 1 | 25 | 3 | *** | 1 |

### ΔH — 2 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_62 | Fe^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |

### ΔS — 2 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_62 | Fe^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |

---

### Step 12: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_61, metal_62) AND c.ligand_id IN (ligand_6165, ligand_8873, ligand_9257, ligand_9873, ligand_8465, ligand_8872, ligand_8126, ligand_9358))",
  "order_by": "c.ligand_name ASC, n.network_db_id ASC",
  "limit": 50
}
```

[summary]
## search_networks — 104 row(s)

> **Reference equilibrium networks (compact)** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### Beta-definition legend
| beta_def | equation |
|----------|----------|
| beta_def_823 | ``[M] + [H2L] <=> [ML] + [H]^2`` |
| beta_def_876 | ``[ML2] + [H2L] <=> [ML3] + [H]^2`` |
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` |
| beta_def_853 | ``[ML] + [H2L] <=> [ML2] + [H]^2`` |
| beta_def_821 | ``[M] + [HL] <=> [ML] + [H]`` |
| beta_def_846 | ``[ML] + [HL] <=> [ML2] + [H]`` |
| beta_def_779 | ``[M] + [HL] <=> [MHL]`` |
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_872 | ``[M] + [L]^3 <=> [ML3]`` |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |
| beta_def_352 | ``[ML3(s)] <=> [M] + [L]^3`` |
| beta_def_597 | ``[M]^3 + [L]^6 + [H2O]^2 <=> [M3(OH)2L6] + [H]^2`` |
| beta_def_601 | ``[M]^3 + [L]^2 + [H2O]^3 <=> [M3(OH)3L2] + [H]^3`` |
| beta_def_708 | ``[M]^7 + [L]^6 + [H2O]^9 <=> [M7(OH)9L6] + [H]^9`` |
| beta_def_966 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` |
| beta_def_238 | ``[M(OH)2L] + [H] <=> [M(OH)L] + [H2O]`` |
| beta_def_263 | ``[M(OH)3L] + [H] <=> [M(OH)2L] + [H2O]`` |
| beta_def_423 | ``[ML]^2 + [H2O]^2 <=> [M2(OH)2L2] + [H]^2`` |
| beta_def_427 | ``[M(OH)L]^2 <=> [M2(OH)2L2]`` |

### Metal-ligand pair summary
| metal | metal_id | ligand | ligand_id | HxL | T_range | I_range | net_count | max_nodes | max_net_id | ligand_SMILES |
|-------|----------|--------|-----------|-----|---------|---------|-----------|----------|------------|---------------|
| `Fe^[3+]` | metal_61 | 1,2-Dihydroxybenzene-3,5-disulfonic aci… | ligand_9358 | H4L | 15~30 | -0.05~1.15 | 4 | 4 | ref_eq_net_23905 | O=S(=O)(O)c1cc(O)c(O)c(S(=O)(=O)O)c1 |
| `Fe^[2+]` | metal_62 | 2-Hydroxybenzoic acid (Salicylic acid) | ligand_9257 | H2L | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_23158 | O=C(O)c1ccccc1O |
| `Fe^[3+]` | metal_61 | 2-Hydroxybenzoic acid (Salicylic acid) | ligand_9257 | H2L | 15~30 | -0.15~3.15 | 7 | 3 | ref_eq_net_23169 | O=C(O)c1ccccc1O |
| `Fe^[3+]` | metal_61 | 8-Hydroxyquinoline (8-Quinolinol)(Oxine) | ligand_8126 | HL | 19~30 | -0.15~1.15 | 4 | 4 | ref_eq_net_14783 | Oc1cccc2cccnc12 |
| `Fe^[2+]` | metal_62 | Acetohydroxamic acid | ligand_9873 | HL | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_26603 | CC(=O)NO |
| `Fe^[3+]` | metal_61 | Acetohydroxamic acid | ligand_9873 | HL | 15~30 | -0.05~2.15 | 4 | 3 | ref_eq_net_26610 | CC(=O)NO |
| `Fe^[2+]` | metal_62 | Ethanedioic acid (Oxalic acid) | ligand_8872 | H2L | 16.5~31.5 | 0.775~1.225 | 1 | 2 | ref_eq_net_20019 | O=C(O)C(=O)O |
| `Fe^[3+]` | metal_61 | Ethanedioic acid (Oxalic acid) | ligand_8872 | H2L | 16.5~31.5 | 0.275~3.225 | 3 | 3 | ref_eq_net_20031 | O=C(O)C(=O)O |
| `Fe^[2+]` | metal_62 | Ethanoic acid (Acetic acid) | ligand_8465 | HL | 16.5~31.5 | 2.775~3.225 | 1 | 1 | ref_eq_net_17129 | CC(=O)O |
| `Fe^[3+]` | metal_61 | Ethanoic acid (Acetic acid) | ligand_8465 | HL | 15~30 | -0.05~3.15 | 5 | 5 | ref_eq_net_17149 | CC(=O)O |
| `Fe^[2+]` | metal_62 | Nitrilotriacetic acid (NTA) | ligand_6165 | H3L | 15~30 | -0.05~1.15 | 3 | 3 | ref_eq_net_3746 | O=C(O)CN(CC(=O)O)CC(=O)O |
| `Fe^[3+]` | metal_61 | Nitrilotriacetic acid (NTA) | ligand_6165 | H3L | 15~30 | -0.05~1.15 | 5 | 5 | ref_eq_net_3758 | O=C(O)CN(CC(=O)O)CC(=O)O |
| `Fe^[2+]` | metal_62 | Propanedioic acid (Malonic acid) | ligand_8873 | H2L | 16.5~31.5 | 0.775~1.225 | 2 | 2 | ref_eq_net_20152 | O=C(O)CC(=O)O |
| `Fe^[3+]` | metal_61 | Propanedioic acid (Malonic acid) | ligand_8873 | H2L | 19~30 | -0.05~1.15 | 3 | 3 | ref_eq_net_20167 | O=C(O)CC(=O)O |

### Global max-node network: `Fe^[3+]` + Ethanoic acid (Acetic acid)
network_id: ref_eq_net_17149 | metal_id: metal_61 | ligand_id: ligand_8465 | ligand_def_HxL: HL | nodes: 5

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 3.23 |
| beta_def_601 | ``[M]^3 + [L]^2 + [H2O]^3 <=> [M3(OH)3L2] + [H]^3`` | logK | 5.87 |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` | logK | 6.22 |
| beta_def_708 | ``[M]^7 + [L]^6 + [H2O]^9 <=> [M7(OH)9L6] + [H]^9`` | logK | 17.26 |
| beta_def_597 | ``[M]^3 + [L]^6 + [H2O]^2 <=> [M3(OH)2L6] + [H]^2`` | logK | 22.05 |

---

### Step 13: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_61, metal_62) AND c.ligand_id IN (ligand_6165, ligand_8873, ligand_9257, ligand_9873, ligand_8465, ligand_8872, ligand_8126, ligand_9358) AND s.constant_type = 'logK')",
  "order_by": "c.ligand_name_SRD ASC, c.metal_name_SRD ASC, s.constant_value DESC",
  "limit": 300
}
```

[summary]
## search_stability

*(no results)*

---

### Step 14: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_9358"
}
```

[summary]
## inspect_card — Ligand | ligand_9358

**Name:** 1,2-Dihydroxybenzene-3,5-disulfonic acid (Tiron)  
**Formula:** C6H6O8S2 | **Class:** Catechols  
**SMILES:** `O=S(=O)(O)c1cc(O)c(O)c(S(=O)(=O)O)c1`  
**InChI:** `InChI=1S/C6H6O8S2/c7-4-1-3(15(9,10)11)2-5(6(4)8)16(12,13)14/h1-2,7-8H,(H,9,10,11)(H,12,13,14)`  
**HxL definition:** H4L  

**pKa values:** 2

| source_vlm | pKa | T (°C) | I (M) | From → To | Solvent | Method | Quality |
|------------|-----|--------|-------|-----------|---------|--------|---------|
| vlm_161952 | -12.50 | 25.0 | 0.1 | L → HL | *** | *** | *** |
| vlm_161957 | 7.62 | 25.0 | 0.1 | HL → H2L | *** | *** | *** |

**Partners:** 42 metal(s), 225 measurement(s) total

| metal_id | Metal | # meas |
|----------|-------|--------|
| metal_61 | Fe^[3+] | 16 |
| metal_68 | H^[+] | 12 |
| metal_5 | Al^[3+] | 12 |
| metal_208 | Zn^[2+] | 11 |
| metal_41 | Cu^[2+] | 11 |
| … | *(showing top 5 of 42)* | |

---

### Step 15: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_9257"
}
```

[summary]
## inspect_card — Ligand | ligand_9257

**Name:** 2-Hydroxybenzoic acid (Salicylic acid)  
**Formula:** C7H6O3 | **Class:** Phenols salicylic acids  
**SMILES:** `O=C(O)c1ccccc1O`  
**InChI:** `InChI=1S/C7H6O3/c8-6-4-2-1-3-5(6)7(9)10/h1-4,8H,(H,9,10)`  
**HxL definition:** H2L  

**pKa values:** 2

| source_vlm | pKa | T (°C) | I (M) | From → To | Solvent | Method | Quality |
|------------|-----|--------|-------|-----------|---------|--------|---------|
| vlm_160211 | -13.40 | 25.0 | 0.1 | L → HL | *** | *** | *** |
| vlm_160226 | 2.80 | 25.0 | 0.1 | HL → H2L | *** | *** | *** |

**Partners:** 40 metal(s), 227 measurement(s) total

| metal_id | Metal | # meas |
|----------|-------|--------|
| metal_68 | H^[+] | 36 |
| metal_61 | Fe^[3+] | 15 |
| metal_19 | Be^[2+] | 11 |
| metal_195 | UO_[2]^[2+] | 10 |
| metal_41 | Cu^[2+] | 10 |
| … | *(showing top 5 of 40)* | |

---

### Step 16: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_9873"
}
```

[summary]
## inspect_card — Ligand | ligand_9873

**Name:** Acetohydroxamic acid  
**Formula:** C2H5N1O2 | **Class:** miscellaneous hydroxamic acids  
**SMILES:** `CC(=O)NO`  
**InChI:** `InChI=1S/C2H5NO2/c1-2(4)3-5/h5H,1H3,(H,3,4)`  
**HxL definition:** HL  

**pKa values:** 1

| source_vlm | pKa | T (°C) | I (M) | From → To | Solvent | Method | Quality |
|------------|-----|--------|-------|-----------|---------|--------|---------|
| vlm_168403 | 9.29 | 25.0 | 0.1 | L → HL | *** | *** | *** |

**Partners:** 19 metal(s), 66 measurement(s) total

| metal_id | Metal | # meas |
|----------|-------|--------|
| metal_61 | Fe^[3+] | 10 |
| metal_68 | H^[+] | 6 |
| metal_208 | Zn^[2+] | 5 |
| metal_112 | Ni^[2+] | 5 |
| metal_33 | Co^[2+] | 5 |
| … | *(showing top 5 of 19)* | |

---

### Step 17: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_8873"
}
```

[summary]
## inspect_card — Ligand | ligand_8873

**Name:** Propanedioic acid (Malonic acid)  
**Formula:** C3H4O4 | **Class:** Carboxylic acids diacids  
**SMILES:** `O=C(O)CC(=O)O`  
**InChI:** `InChI=1S/C3H4O4/c4-2(5)1-3(6)7/h1H2,(H,4,5)(H,6,7)`  
**HxL definition:** H2L  

**pKa values:** 2

| source_vlm | pKa | T (°C) | I (M) | From → To | Solvent | Method | Quality |
|------------|-----|--------|-------|-----------|---------|--------|---------|
| vlm_151949 | 2.65 | 25.0 | 0.1 | HL → H2L | *** | *** | *** |
| vlm_151918 | 5.27 | 25.0 | 0.1 | L → HL | *** | *** | *** |

**Partners:** 51 metal(s), 505 measurement(s) total

| metal_id | Metal | # meas |
|----------|-------|--------|
| metal_68 | H^[+] | 59 |
| metal_79 | La^[3+] | 20 |
| metal_206 | Yb^[3+] | 19 |
| metal_192 | Tm^[3+] | 17 |
| metal_81 | Lu^[3+] | 17 |
| … | *(showing top 5 of 51)* | |

---

### Step 18: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_8465"
}
```

[summary]
## inspect_card — Ligand | ligand_8465

**Name:** Ethanoic acid (Acetic acid)  
**Formula:** C2H4O2 | **Class:** Carboxylic acids  
**SMILES:** `CC(=O)O`  
**InChI:** `InChI=1S/C2H4O2/c1-2(3)4/h1H3,(H,3,4)`  
**HxL definition:** HL  

**pKa values:** 1

| source_vlm | pKa | T (°C) | I (M) | From → To | Solvent | Method | Quality |
|------------|-----|--------|-------|-----------|---------|--------|---------|
| vlm_144406 | 4.56 | 25.0 | 0.1 | L → HL | *** | *** | *** |

**Partners:** 69 metal(s), 562 measurement(s) total

| metal_id | Metal | # meas |
|----------|-------|--------|
| metal_26 | Cd^[2+] | 40 |
| metal_41 | Cu^[2+] | 37 |
| metal_68 | H^[+] | 29 |
| metal_185 | Th^[4+] | 25 |
| metal_112 | Ni^[2+] | 22 |
| … | *(showing top 5 of 69)* | |

---

### Step 19: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_8872"
}
```

[summary]
## inspect_card — Ligand | ligand_8872

**Name:** Ethanedioic acid (Oxalic acid)  
**Formula:** C2H2O4 | **Class:** Carboxylic acids diacids  
**SMILES:** `O=C(O)C(=O)O`  
**InChI:** `InChI=1S/C2H2O4/c3-1(4)2(5)6/h(H,3,4)(H,5,6)`  
**HxL definition:** H2L  

**pKa values:** 2

| source_vlm | pKa | T (°C) | I (M) | From → To | Solvent | Method | Quality |
|------------|-----|--------|-------|-----------|---------|--------|---------|
| vlm_151532 | -1.20 | 25.0 | 0.1 | HL → H2L | *** | *** | *** |
| vlm_151494 | 3.80 | 25.0 | 0.1 | L → HL | *** | *** | *** |

**Partners:** 59 metal(s), 394 measurement(s) total

| metal_id | Metal | # meas |
|----------|-------|--------|
| metal_68 | H^[+] | 56 |
| metal_195 | UO_[2]^[2+] | 21 |
| metal_5 | Al^[3+] | 18 |
| metal_25 | Ca^[2+] | 17 |
| metal_19 | Be^[2+] | 16 |
| … | *(showing top 5 of 59)* | |

---

### Step 20: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_8126"
}
```

[summary]
## inspect_card — Ligand | ligand_8126

**Name:** 8-Hydroxyquinoline (8-Quinolinol)(Oxine)  
**Formula:** C9H7N1O1 | **Class:** Quinolines  
**SMILES:** `Oc1cccc2cccnc12`  
**InChI:** `InChI=1S/C9H7NO/c11-8-5-1-3-7-4-2-6-10-9(7)8/h1-6,11H`  
**HxL definition:** HL  

**pKa values:** 2

| source_vlm | pKa | T (°C) | I (M) | From → To | Solvent | Method | Quality |
|------------|-----|--------|-------|-----------|---------|--------|---------|
| vlm_137922 | 4.97 | 25.0 | 0.1 | HL → H2L | *** | *** | *** |
| vlm_137913 | 9.65 | 25.0 | 0.1 | L → HL | *** | *** | *** |

**Partners:** 25 metal(s), 109 measurement(s) total

| metal_id | Metal | # meas |
|----------|-------|--------|
| metal_68 | H^[+] | 18 |
| metal_61 | Fe^[3+] | 13 |
| metal_185 | Th^[4+] | 6 |
| metal_26 | Cd^[2+] | 6 |
| metal_208 | Zn^[2+] | 5 |
| … | *(showing top 5 of 25)* | |

---

### Step 21: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_6165"
}
```

[summary]
## inspect_card — Ligand | ligand_6165

**Name:** Nitrilotriacetic acid (NTA)  
**Formula:** C6H9N1O6 | **Class:** NTA and derivatives  
**SMILES:** `O=C(O)CN(CC(=O)O)CC(=O)O`  
**InChI:** `InChI=1S/C6H9NO6/c8-4(9)1-7(2-5(10)11)3-6(12)13/h1-3H2,(H,8,9)(H,10,11)(H,12,13)`  
**HxL definition:** H3L  

**pKa values:** 4

| source_vlm | pKa | T (°C) | I (M) | From → To | Solvent | Method | Quality |
|------------|-----|--------|-------|-----------|---------|--------|---------|
| vlm_105204 | -1.81 | 25.0 | 0.1 | H2L → H3L | *** | *** | *** |
| vlm_105223 | -1.00 | 25.0 | 0.1 | H3L → H4L | *** | *** | *** |
| vlm_105186 | 2.52 | 25.0 | 0.1 | HL → H2L | *** | *** | *** |
| vlm_105158 | 9.46 | 25.0 | 0.1 | L → HL | *** | *** | *** |

**Partners:** 71 metal(s), 534 measurement(s) total

| metal_id | Metal | # meas |
|----------|-------|--------|
| metal_68 | H^[+] | 72 |
| metal_103 | Mo^[6+] | 20 |
| metal_112 | Ni^[2+] | 19 |
| metal_208 | Zn^[2+] | 16 |
| metal_61 | Fe^[3+] | 16 |
| … | *(showing top 5 of 71)* | |

---

### Step 22: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND c.ligand_id IN (ligand_8872, ligand_8873, ligand_9257, ligand_9873, ligand_8465, ligand_6165, ligand_8126, ligand_9358))",
  "order_by": "c.ligand_id ASC, s.constant_value DESC",
  "limit": 200
}
```

[summary]
## search_stability — 111 row(s)

### ΔS — 6 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 3 | 3 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8873 | Propanedioic acid (Malonic … | H2L | O=C(O)CC(=O)O | 3 | 3 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 2 | 2 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 1 | 25 | 1~3 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9873 | Acetohydroxamic acid | HL | CC(=O)NO | 1 | 1 | 25 | 2 | *** | 0 |

### logK — 8 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_9358 | 1,2-Dihydroxybenzene-3,5-di… | H4L | O=S(=O)(O)c1cc(O)c(O)c(S(=O)(=O)O)c1 | 16 | 4 | 20~25 | 0.1~1 | *** | 4 |
| metal_61 | Fe^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 14 | 8 | 20~25 | 0.1~1 | *** | 4 |
| metal_61 | Fe^[3+] | ligand_8126 | 8-Hydroxyquinoline (8-Quino… | HL | Oc1cccc2cccnc12 | 13 | 4 | 25 | 0~1 | solid | 4 |
| metal_61 | Fe^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 12 | 5 | 20~25 | 0.1~3 | *** | 5 |
| metal_61 | Fe^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 11 | 3 | 20~25 | 0~3 | *** | 7 |
| metal_61 | Fe^[3+] | ligand_8873 | Propanedioic acid (Malonic … | H2L | O=C(O)CC(=O)O | 8 | 3 | 25 | 0.1~1 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_9873 | Acetohydroxamic acid | HL | CC(=O)NO | 8 | 3 | 20~25 | 0.1~2 | *** | 4 |
| metal_61 | Fe^[3+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 5 | 3 | 25 | 0.5~3 | *** | 3 |

### ΔH — 6 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 3 | 3 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8873 | Propanedioic acid (Malonic … | H2L | O=C(O)CC(=O)O | 3 | 3 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 2 | 2 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 1 | 25 | 1~3 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9873 | Acetohydroxamic acid | HL | CC(=O)NO | 1 | 1 | 25 | 2 | *** | 0 |

---

### Step 23: `search_pka_values`
**Args:**
```json
{
  "where": "(lc.ligand_id IN (ligand_8872, ligand_8873, ligand_9257, ligand_9873, ligand_8465, ligand_6165, ligand_8126, ligand_9358))",
  "order_by": "lc.ligand_name_SRD ASC, p.pKa ASC",
  "limit": 200
}
```

[summary]
## search_pka_values — 16 row(s)

### pKa -13.5–-13.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_160211 | ligand_9257 | 2-Hydroxybenzoic acid (Salicylic a… | H2L | O=C(O)c1ccccc1O | -13.4 | 25 | 0.1 | L→HL | M_tot_37 | M_tot_3 |

### pKa -12.5–-12.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_161952 | ligand_9358 | 1,2-Dihydroxybenzene-3,5-disulfoni… | H4L | O=S(=O)(O)c1cc(O)c(O)c(S(=O)(=O)O)c1 | -12.5 | 25 | 0.1 | L→HL | M_tot_18 | M_tot_1 |

### pKa -2.0–-1.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_105204 | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | -1.81 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_2 |

### pKa -1.5–-1.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_151532 | ligand_8872 | Ethanedioic acid (Oxalic acid) | H2L | O=C(O)C(=O)O | -1.2 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_7 |

### pKa -1.0–-0.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_105223 | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | -1 | 25 | 0.1 | H3L→H4L | M_tot_1 | M_tot_1 |

### pKa 2.5–3.0 (3 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_105186 | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 2.52 | 25 | 0.1 | HL→H2L | M_tot_2 | M_tot_2 |
| vlm_151949 | ligand_8873 | Propanedioic acid (Malonic acid) | H2L | O=C(O)CC(=O)O | 2.65 | 25 | 0.1 | HL→H2L | M_tot_2 | M_tot_26 |
| vlm_160226 | ligand_9257 | 2-Hydroxybenzoic acid (Salicylic a… | H2L | O=C(O)c1ccccc1O | 2.8 | 25 | 0.1 | HL→H2L | M_tot_4 | M_tot_37 |

### pKa 3.5–4.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_151494 | ligand_8872 | Ethanedioic acid (Oxalic acid) | H2L | O=C(O)C(=O)O | 3.8 | 25 | 0.1 | L→HL | M_tot_7 | M_tot_56 |

### pKa 4.5–5.0 (2 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_144406 | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 4.56 | 25 | 0.1 | L→HL | M_tot_2 | M_tot_69 |
| vlm_137922 | ligand_8126 | 8-Hydroxyquinoline (8-Quinolinol)(… | HL | Oc1cccc2cccnc12 | 4.97 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_2 |

### pKa 5.0–5.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_151918 | ligand_8873 | Propanedioic acid (Malonic acid) | H2L | O=C(O)CC(=O)O | 5.27 | 25 | 0.1 | L→HL | M_tot_26 | M_tot_50 |

### pKa 7.5–8.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_161957 | ligand_9358 | 1,2-Dihydroxybenzene-3,5-disulfoni… | H4L | O=S(=O)(O)c1cc(O)c(O)c(S(=O)(=O)O)c1 | 7.62 | 25 | 0.1 | HL→H2L | M_tot_42 | M_tot_18 |

### pKa 9.0–9.5 (2 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_168403 | ligand_9873 | Acetohydroxamic acid | HL | CC(=O)NO | 9.29 | 25 | 0.1 | L→HL | M_tot_1 | M_tot_19 |
| vlm_105158 | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 9.46 | 25 | 0.1 | L→HL | M_tot_2 | M_tot_68 |

### pKa 9.5–10.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_137913 | ligand_8126 | 8-Hydroxyquinoline (8-Quinolinol)(… | HL | Oc1cccc2cccnc12 | 9.65 | 25 | 0.1 | L→HL | M_tot_2 | M_tot_24 |

---
