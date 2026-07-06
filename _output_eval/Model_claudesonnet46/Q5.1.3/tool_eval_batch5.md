# Q5.1.3 — Tool Results (batch 5)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "iron",
  "limit": 10
}
```

[summary]
## search_metals — 2 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_61 | Fe^[3+] | Fe | 3 | ✓ | [Fe+3] | InChI=1S/Fe/q+3 | beta_totN_128 | ligand_totN_406 | vlm_totN_1473 |
| metal_62 | Fe^[2+] | Fe | 2 | ✓ | [Fe+2] | InChI=1S/Fe/q+2 | beta_totN_57 | ligand_totN_217 | vlm_totN_667 |

---

### Step 3: `search_metals`
**Args:**
```json
{
  "name": "copper",
  "limit": 10
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

### Step 5: `build_system_catalog`
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

### Step 6: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_41"
}
```

[summary]
[CATALOG]
## build_system_catalog — 20 pair(s), 102 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_107 | [M(H-1L)] + [H] <=> [ML] |  |
| beta_def_117 | [M(OH)(H-1L)] + [H] <=> [M(H-1L)] + [H2O] |  |
| beta_def_136 | [M(H-1L)] + [L] <=> [M(H-1L)L] |  |
| beta_def_137 | [M(H-1L)2] + [H] <=> [M(H-1L)L] |  |
| beta_def_194 | [M] + [HL]^2 <=> [M(HL)2] |  |
| beta_def_204 | [MHL2] + [H] <=> [M(HL)2] |  |
| beta_def_238 | [M(OH)2L] + [H] <=> [M(OH)L] + [H2O] |  |
| beta_def_249 | [M(OH)2L2] + [H] <=> [M(OH)L2] + [H2O] |  |
| beta_def_334 | [ML2(s)] <=> [M] + [L]^2 | solid |
| beta_def_347 | [MO(s)] + [H2O] <=> [M] + [OH]^2 | solid |
| beta_def_423 | [ML]^2 + [H2O]^2 <=> [M2(OH)2L2] + [H]^2 |  |
| beta_def_424 | [M]^2 + [L]^2 + [H2O]^2 <=> [M2(OH)2L2] + [H]^2 |  |
| beta_def_427 | [M(OH)L]^2 <=> [M2(OH)2L2] |  |
| beta_def_434 | [M]^2 + [L]^4 + [H2O]^2 <=> [M2(OH)2L4] + [H]^2 |  |
| beta_def_463 | [M2H-2L2] + [H] <=> [M2H-1L2] |  |
| beta_def_477 | [M]^2 + [L]^2 <=> [M2H-2L2] + [H]^2 |  |
| beta_def_502 | [M]^2 + [L] <=> [M2L] |  |
| beta_def_519 | [M]^2 + [L]^2 <=> [M2L2] |  |
| beta_def_567 | [M(H-1L)] + [M(OH)(H-1L)] <=> [M2(OH)(H-1L)2] |  |
| beta_def_630 | [M2H-2L2] + [M] <=> [M3H-2L2] |  |
| beta_def_649 | [M]^3 + [L]^4 <=> [M3L4] |  |
| beta_def_779 | [M] + [HL] <=> [MHL] |  |
| beta_def_788 | [ML] + [H] <=> [MHL] |  |
| beta_def_792 | [ML2] + [H] <=> [MHL2] |  |
| beta_def_798 | [M] + [HL] + [L] <=> [MHL2] |  |
| beta_def_812 | [M] + [L] <=> [ML] |  |
| beta_def_834 | [M(OH)2L] + [H]^2 <=> [ML] + [H2O]^2 |  |
| beta_def_840 | [M] + [L]^2 <=> [ML2] |  |
| beta_def_871 | [M(OH)L2] + [H] <=> [ML2] + [H2O] |  |
| beta_def_872 | [M] + [L]^3 <=> [ML3] |  |
| beta_def_894 | [M] + [L]^4 <=> [ML4] |  |
| beta_def_966 | [M(OH)L] + [H] <=> [ML] + [H2O] |  |
| beta_def_981 | [ML] + [OH] <=> [M(OH)L] |  |
| beta_def_984 | [M(OH)L2] + [H] <=> [ML2] + [H2O] |  |

*(all species aqueous unless noted)*

**1. Cu^[2+] + L-2-Amino-3-(4-imidazolyl)propanoic acid (Histidine)** (metal_41 + ligand_5898) — ligand_def_HxL: HL | 50 ent, 8 sp, 50 vlms (vlm_98835…vlm_98884)
   - species: beta_def_204(8) beta_def_424(4) beta_def_788(7) beta_def_792(8) beta_def_812(8) beta_def_840(7) beta_def_966(3) beta_def_984(5)
   - eq:6 nets T:19~41°C I:-0.05~3.15M max 8n/22e
**2. Cu^[2+] + Ammonia** (metal_41 + ligand_10103) — ligand_def_HxL: L | 49 ent, 4 sp, 49 vlms (vlm_173242…vlm_173290)
   - species: beta_def_812(13) beta_def_840(12) beta_def_872(12) beta_def_894(12)
   - eq:5 nets T:19~30°C I:-0.15~3.15M max 4n/6e
**3. Cu^[2+] + 1,3-Diazole (Imidazole)** (metal_41 + ligand_7795) — ligand_def_HxL: L | 42 ent, 7 sp, 42 vlms (vlm_133893…vlm_133934)
   - species: beta_def_424(1) beta_def_434(2) beta_def_812(10) beta_def_840(10) beta_def_872(10) beta_def_894(7) beta_def_966(2)
   - eq:8 nets T:19~41°C I:-0.15~3.15M max 7n/18e
**4. Cu^[2+] + N,N'-Dimethylethylenediamine** (metal_41 + ligand_7172) — ligand_def_HxL: L | 39 ent, 5 sp, 39 vlms (vlm_125004…vlm_125042)
   - species: beta_def_424(7) beta_def_812(9) beta_def_834(7) beta_def_840(9) beta_def_966(7)
   - eq:5 nets T:19~30°C I:-0.15~2.15M max 5n/8e
**5. Cu^[2+] + Ethanoic acid (Acetic acid)** (metal_41 + ligand_8465) — ligand_def_HxL: HL | 37 ent, 3 sp, 37 vlms (vlm_144741…vlm_144777)
   - species: beta_def_812(16) beta_def_840(16) beta_def_872(5)
   - eq:6 nets T:19~41°C I:-0.15~3.15M max 3n/3e
**6. Cu^[2+] + Glycylglycine (Diglycine)** (metal_41 + ligand_6372) — ligand_def_HxL: HL | 36 ent, 6 sp, 36 vlms (vlm_113537…vlm_113572)
   - species: beta_def_107(7) beta_def_117(6) beta_def_136(7) beta_def_137(1) beta_def_567(5) beta_def_812(10)
   - eq:6 nets T:19~41°C I:-0.15~5.15M max 6n/11e
**7. Cu^[2+] + Hydroxide ion** (metal_41 + ligand_10076) — ligand_def_HxL: *** | 34 ent, 9 sp, 34 vlms (vlm_170713…vlm_170746)
   - species: beta_def_334(5) beta_def_347(2) beta_def_502(3) beta_def_519(9) beta_def_649(4) beta_def_812(7) beta_def_840(2) beta_def_872(1) beta_def_894(1)
   - eq:6 nets T:19~41°C I:-0.15~3.15M max 6n/15e
**8. Cu^[2+] + Ethylenediamine** (metal_41 + ligand_7029) — ligand_def_HxL: L | 34 ent, 2 sp, 34 vlms (vlm_122410…vlm_122443)
   - species: beta_def_812(17) beta_def_840(17)
   - eq:9 nets T:19~41°C I:-0.15~3.15M max 2n/1e
**9. Cu^[2+] + 2,2'-Bipyridyl** (metal_41 + ligand_8156) — ligand_def_HxL: L | 33 ent, 6 sp, 33 vlms (vlm_138609…vlm_138641)
   - species: beta_def_238(3) beta_def_423(3) beta_def_812(8) beta_def_840(8) beta_def_872(8) beta_def_966(3)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 6n/8e
**10. Cu^[2+] + L-2-Amino-3-phenylpropanoic acid (Phenylalanine)** (metal_41 + ligand_5777) — ligand_def_HxL: HL | 33 ent, 3 sp, 33 vlms (vlm_95053…vlm_95085)
   - species: beta_def_788(1) beta_def_812(15) beta_def_840(17)
   - eq:7 nets T:5~45°C I:-0.15~3.15M max 3n/2e
**11. Cu^[2+] + Iminodiacetic acid (IDA)** (metal_41 + ligand_6127) — ligand_def_HxL: H2L | 32 ent, 4 sp, 32 vlms (vlm_104366…vlm_104397)
   - species: beta_def_788(3) beta_def_812(13) beta_def_840(14) beta_def_966(2)
   - eq:6 nets T:19~41°C I:-0.15~1.15M max 4n/4e
**12. Cu^[2+] + L-2-Amino-3-hydroxybutanoic acid (Threonine)** (metal_41 + ligand_5829) — ligand_def_HxL: HL | 32 ent, 5 sp, 32 vlms (vlm_96743…vlm_96774)
   - species: beta_def_249(3) beta_def_812(12) beta_def_840(12) beta_def_966(1) beta_def_984(4)
   - eq:6 nets T:19~41°C I:-0.15~3.15M max 4n/4e
**13. Cu^[2+] + Aminoacetic acid (Glycine)** (metal_41 + ligand_5760) — ligand_def_HxL: HL | 30 ent, 2 sp, 30 vlms (vlm_93847…vlm_93876)
   - species: beta_def_812(15) beta_def_840(15)
   - eq:9 nets T:5~45°C I:-0.15~2.65M max 2n/1e
**14. Cu^[2+] + N-(2-Hydroxyethyl)iminodiacetic acid (HIDA)** (metal_41 + ligand_6204) — ligand_def_HxL: H2L | 29 ent, 4 sp, 29 vlms (vlm_106728…vlm_106756)
   - species: beta_def_812(13) beta_def_840(13) beta_def_966(1) beta_def_984(2)
   - eq:4 nets T:19~30°C I:-0.15~1.15M max 4n/4e
**15. Cu^[2+] + Pyridine (Azine)** (metal_41 + ligand_7890) — ligand_def_HxL: L | 28 ent, 5 sp, 28 vlms (vlm_135256…vlm_135283)
   - species: beta_def_812(7) beta_def_840(7) beta_def_872(7) beta_def_894(6) beta_def_966(1)
   - eq:5 nets T:19~30°C I:-0.15~1.15M max 5n/7e
**16. Cu^[2+] + 1,4,9-Triazanonane (2,4-tri)** (metal_41 + ligand_7214) — ligand_def_HxL: L | 28 ent, 6 sp, 28 vlms (vlm_125799…vlm_125826)
   - species: beta_def_194(4) beta_def_779(6) beta_def_798(3) beta_def_812(6) beta_def_840(3) beta_def_981(6)
   - eq:2 nets T:19~30°C I:-0.05~0.65M max 6n/11e
**17. Cu^[2+] + DL-2,6-Diamino-5-hydroxyhexanoic acid** (metal_41 + ligand_5889) — ligand_def_HxL: HL | 28 ent, 7 sp, 28 vlms (vlm_98553…vlm_98580)
   - species: beta_def_194(4) beta_def_204(4) beta_def_463(4) beta_def_477(4) beta_def_630(4) beta_def_779(4) beta_def_788(4)
   - eq:2 nets T:20~41°C I:-0.05~0.3M max 7n/15e
**18. Cu^[2+] + 4-(2-Aminoethyl)imidazole (Histamine)** (metal_41 + ligand_7849) — ligand_def_HxL: L | 27 ent, 6 sp, 27 vlms (vlm_134661…vlm_134687)
   - species: beta_def_424(4) beta_def_788(3) beta_def_792(4) beta_def_812(6) beta_def_840(6) beta_def_871(4)
   - eq:4 nets T:19~41°C I:-0.15~1.15M max 6n/12e
**19. Cu^[2+] + 2-(2-Aminoethylamino)ethanol [N-(2-Hydroxyethyl)ethylenediamine]** (metal_41 + ligand_7181) — ligand_def_HxL: L | 27 ent, 5 sp, 27 vlms (vlm_125163…vlm_125189)
   - species: beta_def_427(4) beta_def_812(7) beta_def_834(5) beta_def_840(7) beta_def_966(4)
   - eq:5 nets T:19~30°C I:-0.15~2.15M max 5n/5e
**20. Cu^[2+] + Glycyl-L-alanine** (metal_41 + ligand_6375) — ligand_def_HxL: HL | 27 ent, 5 sp, 27 vlms (vlm_113707…vlm_113733)
   - species: beta_def_107(6) beta_def_117(6) beta_def_136(6) beta_def_567(3) beta_def_812(6)
   - eq:2 nets T:19~30°C I:-0.05~0.65M max 5n/8e

---
