# Q3.1.2 — Tool Results (batch 2)

### Step 2: `search_metals`
**Args:**
```json
{
  "symbol": "Cu",
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

### Step 3: `search_metals`
**Args:**
```json
{
  "symbol": "Ni",
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

### Step 4: `search_metals`
**Args:**
```json
{
  "symbol": "H",
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

### Step 5: `search_ligands`
**Args:**
```json
{
  "name": "glycine, histidine, cysteine, aspartic acid, glutamic acid, alanine, serine, proline, lysine, tyrosine",
  "limit": 200,
  "include_groups": [
    "amino acid"
  ]
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 6: `search_ligands`
**Args:**
```json
{
  "name": "glycine, glycinate, histidine, L-histidine, cysteine, L-cysteine, aspartic acid, aspartate, glutamic acid, glutamate, alanine, serine, proline, lysine, tyrosine",
  "limit": 200
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 8: `build_system_catalog`
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

### Step 9: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_112"
}
```

[summary]
[CATALOG]
## build_system_catalog — 20 pair(s), 95 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_137 | [M(H-1L)2] + [H] <=> [M(H-1L)L] |  |
| beta_def_194 | [M] + [HL]^2 <=> [M(HL)2] |  |
| beta_def_204 | [MHL2] + [H] <=> [M(HL)2] |  |
| beta_def_208 | [M] + [HL]^3 <=> [M(HL)3] |  |
| beta_def_214 | [MH2L3] + [H] <=> [M(HL)3] |  |
| beta_def_374 | [M]^2 + [L]^2 <=> [M2(H-1L)2] + [H]^2 |  |
| beta_def_477 | [M]^2 + [L]^2 <=> [M2H-2L2] + [H]^2 |  |
| beta_def_535 | [M2H-2L2] + [H]^2 <=> [M2L2] |  |
| beta_def_630 | [M2H-2L2] + [M] <=> [M3H-2L2] |  |
| beta_def_732 | [M] + [H2L] <=> [MH2L] |  |
| beta_def_739 | [MHL] + [H] <=> [MH2L] |  |
| beta_def_744 | [MHL3] + [H] <=> [MH2L3] |  |
| beta_def_751 | [MH2L] + [H] <=> [MH3L] |  |
| beta_def_779 | [M] + [HL] <=> [MHL] |  |
| beta_def_788 | [ML] + [H] <=> [MHL] |  |
| beta_def_792 | [ML2] + [H] <=> [MHL2] |  |
| beta_def_800 | [MHL] + [L] <=> [MHL2] |  |
| beta_def_803 | [ML3] + [H] <=> [MHL3] |  |
| beta_def_812 | [M] + [L] <=> [ML] |  |
| beta_def_840 | [M] + [L]^2 <=> [ML2] |  |
| beta_def_860 | [M(H-1L)L] + [H] <=> [ML2] |  |
| beta_def_872 | [M] + [L]^3 <=> [ML3] |  |
| beta_def_894 | [M] + [L]^4 <=> [ML4] |  |
| beta_def_903 | [M] + [L]^5 <=> [ML5] |  |
| beta_def_907 | [M] + [L]^6 <=> [ML6] |  |
| beta_def_966 | [M(OH)L] + [H] <=> [ML] + [H2O] |  |
| beta_def_984 | [M(OH)L2] + [H] <=> [ML2] + [H2O] |  |

*(all species aqueous)*

**1. Ni^[2+] + Ammonia** (metal_112 + ligand_10103) — ligand_def_HxL: L | 60 ent, 6 sp, 60 vlms (vlm_173182…vlm_173241)
   - species: beta_def_812(11) beta_def_840(13) beta_def_872(10) beta_def_894(10) beta_def_903(8) beta_def_907(8)
   - eq:5 nets T:19~30°C I:-0.15~3.15M max 6n/15e
**2. Ni^[2+] + Aminoacetic acid (Glycine)** (metal_112 + ligand_5760) — ligand_def_HxL: HL | 49 ent, 3 sp, 49 vlms (vlm_93798…vlm_93846)
   - species: beta_def_812(17) beta_def_840(17) beta_def_872(15)
   - eq:9 nets T:5~45°C I:-0.15~3.15M max 3n/3e
**3. Ni^[2+] + Ethylenediamine** (metal_112 + ligand_7029) — ligand_def_HxL: L | 45 ent, 3 sp, 45 vlms (vlm_122365…vlm_122409)
   - species: beta_def_812(15) beta_def_840(15) beta_def_872(15)
   - eq:7 nets T:19~41°C I:-0.15~3.15M max 3n/3e
**4. Ni^[2+] + 1,3-Diazole (Imidazole)** (metal_112 + ligand_7795) — ligand_def_HxL: L | 41 ent, 5 sp, 41 vlms (vlm_133852…vlm_133892)
   - species: beta_def_812(11) beta_def_840(9) beta_def_872(10) beta_def_894(8) beta_def_966(3)
   - eq:9 nets T:19~41°C I:-0.15~4.15M max 5n/7e
**5. Ni^[2+] + DL-2,6-Diamino-5-hydroxyhexanoic acid** (metal_112 + ligand_5889) — ligand_def_HxL: HL | 32 ent, 9 sp, 32 vlms (vlm_98521…vlm_98552)
   - species: beta_def_194(4) beta_def_204(4) beta_def_477(4) beta_def_535(2) beta_def_630(2) beta_def_739(4) beta_def_779(4) beta_def_788(4) beta_def_792(4)
   - eq:2 nets T:20~41°C I:-0.05~0.3M max 9n/25e
**6. Ni^[2+] + Iminodiacetic acid (IDA)** (metal_112 + ligand_6127) — ligand_def_HxL: H2L | 28 ent, 2 sp, 28 vlms (vlm_104338…vlm_104365)
   - species: beta_def_812(14) beta_def_840(14)
   - eq:6 nets T:19~41°C I:-0.15~2.15M max 2n/1e
**7. Ni^[2+] + Glycylglycine (Diglycine)** (metal_112 + ligand_6372) — ligand_def_HxL: HL | 26 ent, 5 sp, 26 vlms (vlm_113511…vlm_113536)
   - species: beta_def_137(4) beta_def_812(7) beta_def_840(6) beta_def_860(5) beta_def_872(4)
   - eq:5 nets T:19~41°C I:-0.15~1.15M max 5n/5e
**8. Ni^[2+] + L-2-Amino-3-phenylpropanoic acid (Phenylalanine)** (metal_112 + ligand_5777) — ligand_def_HxL: HL | 26 ent, 2 sp, 26 vlms (vlm_95027…vlm_95052)
   - species: beta_def_812(13) beta_def_840(13)
   - eq:5 nets T:5~45°C I:-0.15~3.15M max 2n/1e
**9. Ni^[2+] + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid)** (metal_112 + ligand_9058) — ligand_def_HxL: H3L | 25 ent, 6 sp, 25 vlms (vlm_157638…vlm_157662)
   - species: beta_def_374(4) beta_def_732(2) beta_def_779(5) beta_def_800(4) beta_def_812(6) beta_def_840(4)
   - eq:4 nets T:19~30°C I:-0.05~1.15M max 6n/14e
**10. Ni^[2+] + Trimethylenediamine (1,3-Propylenediamine)** (metal_112 + ligand_7037) — ligand_def_HxL: L | 25 ent, 3 sp, 25 vlms (vlm_122912…vlm_122936)
   - species: beta_def_812(9) beta_def_840(9) beta_def_872(7)
   - eq:5 nets T:19~30°C I:-0.15~2.15M max 3n/3e
**11. Ni^[2+] + L-2-Amino-3-(4-imidazolyl)propanoic acid (Histidine)** (metal_112 + ligand_5898) — ligand_def_HxL: HL | 25 ent, 5 sp, 25 vlms (vlm_98810…vlm_98834)
   - species: beta_def_788(1) beta_def_792(2) beta_def_812(9) beta_def_840(12) beta_def_984(1)
   - eq:6 nets T:19~41°C I:-0.05~3.15M max 4n/4e
**12. Ni^[2+] + L-2-Amino-3-(4-hydroxyphenyl)propanoic acid (Tyrosine)** (metal_112 + ligand_5819) — ligand_def_HxL: H2L | 25 ent, 9 sp, 25 vlms (vlm_96273…vlm_96297)
   - species: beta_def_194(3) beta_def_204(3) beta_def_208(3) beta_def_214(3) beta_def_744(3) beta_def_779(3) beta_def_788(1) beta_def_792(3) beta_def_803(3)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 9n/21e
**13. Ni^[2+] + DL-2-Amino-3-(3-hydroxyphenyl)propanoic acid (m-Tyrosine)** (metal_112 + ligand_5818) — ligand_def_HxL: H2L | 24 ent, 8 sp, 24 vlms (vlm_96176…vlm_96199)
   - species: beta_def_194(3) beta_def_204(3) beta_def_208(3) beta_def_214(3) beta_def_744(3) beta_def_779(3) beta_def_792(3) beta_def_803(3)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 8n/15e
**14. Ni^[2+] + L-2-Aminopropanoic acid (Alanine)** (metal_112 + ligand_5761) — ligand_def_HxL: HL | 24 ent, 3 sp, 24 vlms (vlm_94125…vlm_94272)
   - species: beta_def_812(9) beta_def_840(9) beta_def_872(6)
   - eq:5 nets T:19~41°C I:-0.15~1.15M max 3n/3e
**15. Ni^[2+] + Ethanoic acid (Acetic acid)** (metal_112 + ligand_8465) — ligand_def_HxL: HL | 22 ent, 2 sp, 22 vlms (vlm_144719…vlm_144740)
   - species: beta_def_812(12) beta_def_840(10)
   - eq:6 nets T:19~30°C I:-0.15~2.15M max 2n/1e
**16. Ni^[2+] + L-2,6-Diaminohexanoic acid (Lysine)** (metal_112 + ligand_5887) — ligand_def_HxL: HL | 22 ent, 9 sp, 22 vlms (vlm_98405…vlm_98426)
   - species: beta_def_194(4) beta_def_204(4) beta_def_208(3) beta_def_214(1) beta_def_744(1) beta_def_779(4) beta_def_788(2) beta_def_792(2) beta_def_803(1)
   - eq:2 nets T:20~41°C I:-0.05~0.3M max 9n/21e
**17. Ni^[2+] + 4-(2-Aminoethyl)imidazole (Histamine)** (metal_112 + ligand_7849) — ligand_def_HxL: L | 21 ent, 5 sp, 21 vlms (vlm_134640…vlm_134660)
   - species: beta_def_788(2) beta_def_812(6) beta_def_840(6) beta_def_872(6) beta_def_966(1)
   - eq:4 nets T:19~41°C I:-0.15~1.15M max 5n/6e
**18. Ni^[2+] + DL-Methylethylenediamine (1,2-Propylenediamine) (pn)** (metal_112 + ligand_7030) — ligand_def_HxL: L | 21 ent, 3 sp, 21 vlms (vlm_122630…vlm_122650)
   - species: beta_def_812(7) beta_def_840(7) beta_def_872(7)
   - eq:5 nets T:19~30°C I:-0.15~2.15M max 3n/3e
**19. Ni^[2+] + 2-Aminoethanol (Ethanolamine)** (metal_112 + ligand_6887) — ligand_def_HxL: L | 21 ent, 3 sp, 21 vlms (vlm_120801…vlm_120821)
   - species: beta_def_812(7) beta_def_840(7) beta_def_872(7)
   - eq:5 nets T:19~30°C I:-0.15~2.15M max 3n/3e
**20. Ni^[2+] + Nitrilotris(methylenephosphonic acid) (NTP)** (metal_112 + ligand_8412) — ligand_def_HxL: H6L | 20 ent, 4 sp, 20 vlms (vlm_143397…vlm_143416)
   - species: beta_def_739(2) beta_def_751(2) beta_def_788(7) beta_def_812(9)
   - eq:2 nets T:19~30°C I:-0.15~0.25M max 4n/4e

---

### Step 11: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_41 AND c.beta_definition_id = beta_def_812 AND s.solvent_name LIKE '%water%' AND s.temperature_c BETWEEN 20 AND 30 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2) AND (c.ligand_id IN (ligand_5760, ligand_5777, ligand_5829, ligand_5898, ligand_5761, ligand_5887, ligand_5819) OR c.ligand_name_SRD LIKE '%Amino%butanedioic%' OR c.ligand_name_SRD LIKE '%Amino%pentanedioic%' OR c.ligand_name_SRD LIKE '%mercaptopropanoic%'))",
  "order_by": "c.ligand_name_SRD ASC, s.temperature_c ASC, s.ionic_strength_mol_l ASC",
  "limit": 800
}
```

[summary]
## search_stability — 200 row(s)

### logK — 28 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 14 | 2 | 10~40 | 0~5 | *** | 7 |
| metal_112 | Ni^[2+] | ligand_5885 | L-2,4-Diaminobutanoic acid | HL | NCCC(N)C(=O)O | 12 | 10 | 25 | 0.1 | *** | 2 |
| metal_41 | Cu^[2+] | ligand_5885 | L-2,4-Diaminobutanoic acid | HL | NCCC(N)C(=O)O | 10 | 6 | 25~37 | 0.1~0.15 | *** | 3 |
| metal_68 | H^[+] | ligand_5883 | L-2,3-Diaminopropanoic acid | HL | NCC(N)C(=O)O | 7 | 3 | 25~37 | 0.1~0.5 | *** | 3 |
| metal_33 | Co^[2+] | ligand_5883 | L-2,3-Diaminopropanoic acid | HL | NCC(N)C(=O)O | 7 | 5 | 25 | 0.1~0.5 | *** | 2 |
| metal_41 | Cu^[2+] | ligand_5883 | L-2,3-Diaminopropanoic acid | HL | NCC(N)C(=O)O | 7 | 6 | 25~37 | 0.1~0.15 | *** | 2 |
| metal_41 | Cu^[2+] | ligand_5888 | DL-2,7-Diaminooctanedioic a… | HL | NC(CCCCC(N)C(=O)O)C(=O)O | 6 | 6 | 20 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_5883 | L-2,3-Diaminopropanoic acid | HL | NCC(N)C(=O)O | 6 | 6 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5883 | L-2,3-Diaminopropanoic acid | HL | NCC(N)C(=O)O | 6 | 6 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_5885 | L-2,4-Diaminobutanoic acid | HL | NCCC(N)C(=O)O | 6 | 5 | 25 | 0.1 | *** | 2 |
| metal_208 | Zn^[2+] | ligand_5885 | L-2,4-Diaminobutanoic acid | HL | NCCC(N)C(=O)O | 6 | 6 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 5 | 3 | 25 | 0.1~5 | *** | 2 |
| metal_71 | Hg^[2+] | ligand_5883 | L-2,3-Diaminopropanoic acid | HL | NCC(N)C(=O)O | 5 | 5 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_5888 | DL-2,7-Diaminooctanedioic a… | HL | NC(CCCCC(N)C(=O)O)C(=O)O | 4 | 4 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5778 | DL-2-Amino-3-chloropropanoi… | HL | N[C@@H](CCl)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_64 | Ga^[3+] | ligand_5778 | DL-2-Amino-3-chloropropanoi… | HL | N[C@@H](CCl)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_5859 | DL-2-Amino-4-mercaptobutano… | H2L | NC(CCS)C(=O)O | 3 | 3 | 25~30 | 0.1 | *** | 1 |
| metal_37 | Cr^[3+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_5885 | L-2,4-Diaminobutanoic acid | HL | NCCC(N)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_5778 | DL-2-Amino-3-chloropropanoi… | HL | N[C@@H](CCl)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_5 | Al^[3+] | ligand_5778 | DL-2-Amino-3-chloropropanoi… | HL | N[C@@H](CCl)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 3 | *** | 1 |
| metal_68 | H^[+] | ligand_5828 | L-2-Amino-3-hydroxypropanoi… | HL | N[C@@H](CO)C(=O)O | 2 | 2 | 12 | 0 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_5828 | L-2-Amino-3-hydroxypropanoi… | HL | N[C@@H](CO)C(=O)O | 1 | 1 | 20 | 0.7 | *** | 1 |

### ΔH — 10 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_41 | Cu^[2+] | ligand_5883 | L-2,3-Diaminopropanoic acid | HL | NCC(N)C(=O)O | 6 | 6 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5885 | L-2,4-Diaminobutanoic acid | HL | NCCC(N)C(=O)O | 6 | 6 | 25 | 0.1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_5883 | L-2,3-Diaminopropanoic acid | HL | NCC(N)C(=O)O | 5 | 5 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 4 | 2 | 10~40 | 0 | *** | 0 |
| metal_68 | H^[+] | ligand_5883 | L-2,3-Diaminopropanoic acid | HL | NCC(N)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_5885 | L-2,4-Diaminobutanoic acid | HL | NCCC(N)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |

### ΔS — 10 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_41 | Cu^[2+] | ligand_5883 | L-2,3-Diaminopropanoic acid | HL | NCC(N)C(=O)O | 6 | 6 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5885 | L-2,4-Diaminobutanoic acid | HL | NCCC(N)C(=O)O | 6 | 6 | 25 | 0.1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_5883 | L-2,3-Diaminopropanoic acid | HL | NCC(N)C(=O)O | 5 | 5 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_5883 | L-2,3-Diaminopropanoic acid | HL | NCC(N)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_5885 | L-2,4-Diaminobutanoic acid | HL | NCCC(N)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0 | *** | 0 |
| metal_33 | Co^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |

---

### Step 12: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_112 AND c.beta_definition_id = beta_def_812 AND s.solvent_name LIKE '%water%' AND s.temperature_c BETWEEN 20 AND 30 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2) AND (c.ligand_id IN (ligand_5760, ligand_5777, ligand_5829, ligand_5898, ligand_5761, ligand_5887, ligand_5819) OR c.ligand_name_SRD LIKE '%Amino%butanedioic%' OR c.ligand_name_SRD LIKE '%Amino%pentanedioic%' OR c.ligand_name_SRD LIKE '%mercaptopropanoic%'))",
  "order_by": "c.ligand_name_SRD ASC, s.temperature_c ASC, s.ionic_strength_mol_l ASC",
  "limit": 800
}
```

[summary]
## search_stability — 200 row(s)

### logK — 28 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 14 | 2 | 10~40 | 0~5 | *** | 7 |
| metal_112 | Ni^[2+] | ligand_5885 | L-2,4-Diaminobutanoic acid | HL | NCCC(N)C(=O)O | 12 | 10 | 25 | 0.1 | *** | 2 |
| metal_41 | Cu^[2+] | ligand_5885 | L-2,4-Diaminobutanoic acid | HL | NCCC(N)C(=O)O | 10 | 6 | 25~37 | 0.1~0.15 | *** | 3 |
| metal_68 | H^[+] | ligand_5883 | L-2,3-Diaminopropanoic acid | HL | NCC(N)C(=O)O | 7 | 3 | 25~37 | 0.1~0.5 | *** | 3 |
| metal_33 | Co^[2+] | ligand_5883 | L-2,3-Diaminopropanoic acid | HL | NCC(N)C(=O)O | 7 | 5 | 25 | 0.1~0.5 | *** | 2 |
| metal_41 | Cu^[2+] | ligand_5883 | L-2,3-Diaminopropanoic acid | HL | NCC(N)C(=O)O | 7 | 6 | 25~37 | 0.1~0.15 | *** | 2 |
| metal_41 | Cu^[2+] | ligand_5888 | DL-2,7-Diaminooctanedioic a… | HL | NC(CCCCC(N)C(=O)O)C(=O)O | 6 | 6 | 20 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_5883 | L-2,3-Diaminopropanoic acid | HL | NCC(N)C(=O)O | 6 | 6 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5883 | L-2,3-Diaminopropanoic acid | HL | NCC(N)C(=O)O | 6 | 6 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_5885 | L-2,4-Diaminobutanoic acid | HL | NCCC(N)C(=O)O | 6 | 5 | 25 | 0.1 | *** | 2 |
| metal_208 | Zn^[2+] | ligand_5885 | L-2,4-Diaminobutanoic acid | HL | NCCC(N)C(=O)O | 6 | 6 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 5 | 3 | 25 | 0.1~5 | *** | 2 |
| metal_71 | Hg^[2+] | ligand_5883 | L-2,3-Diaminopropanoic acid | HL | NCC(N)C(=O)O | 5 | 5 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_5888 | DL-2,7-Diaminooctanedioic a… | HL | NC(CCCCC(N)C(=O)O)C(=O)O | 4 | 4 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5778 | DL-2-Amino-3-chloropropanoi… | HL | N[C@@H](CCl)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_64 | Ga^[3+] | ligand_5778 | DL-2-Amino-3-chloropropanoi… | HL | N[C@@H](CCl)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_5859 | DL-2-Amino-4-mercaptobutano… | H2L | NC(CCS)C(=O)O | 3 | 3 | 25~30 | 0.1 | *** | 1 |
| metal_37 | Cr^[3+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_5885 | L-2,4-Diaminobutanoic acid | HL | NCCC(N)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_5778 | DL-2-Amino-3-chloropropanoi… | HL | N[C@@H](CCl)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_5 | Al^[3+] | ligand_5778 | DL-2-Amino-3-chloropropanoi… | HL | N[C@@H](CCl)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 3 | *** | 1 |
| metal_68 | H^[+] | ligand_5828 | L-2-Amino-3-hydroxypropanoi… | HL | N[C@@H](CO)C(=O)O | 2 | 2 | 12 | 0 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_5828 | L-2-Amino-3-hydroxypropanoi… | HL | N[C@@H](CO)C(=O)O | 1 | 1 | 20 | 0.7 | *** | 1 |

### ΔH — 10 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_41 | Cu^[2+] | ligand_5883 | L-2,3-Diaminopropanoic acid | HL | NCC(N)C(=O)O | 6 | 6 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5885 | L-2,4-Diaminobutanoic acid | HL | NCCC(N)C(=O)O | 6 | 6 | 25 | 0.1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_5883 | L-2,3-Diaminopropanoic acid | HL | NCC(N)C(=O)O | 5 | 5 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 4 | 2 | 10~40 | 0 | *** | 0 |
| metal_68 | H^[+] | ligand_5883 | L-2,3-Diaminopropanoic acid | HL | NCC(N)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_5885 | L-2,4-Diaminobutanoic acid | HL | NCCC(N)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |

### ΔS — 10 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_41 | Cu^[2+] | ligand_5883 | L-2,3-Diaminopropanoic acid | HL | NCC(N)C(=O)O | 6 | 6 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5885 | L-2,4-Diaminobutanoic acid | HL | NCCC(N)C(=O)O | 6 | 6 | 25 | 0.1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_5883 | L-2,3-Diaminopropanoic acid | HL | NCC(N)C(=O)O | 5 | 5 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_5883 | L-2,3-Diaminopropanoic acid | HL | NCC(N)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_5885 | L-2,4-Diaminobutanoic acid | HL | NCCC(N)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0 | *** | 0 |
| metal_33 | Co^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |

---

### Step 13: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_41, metal_112) AND c.ligand_id IN (ligand_5898, ligand_5760) AND c.beta_definition_id = beta_def_812 AND s.solvent_name LIKE '%water%' AND s.temperature_c BETWEEN 24 AND 26 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2))",
  "order_by": "c.metal_id ASC, c.ligand_id ASC, s.ionic_strength_mol_l ASC, s.temperature_c ASC",
  "limit": 100
}
```

[summary]
## search_stability

*(no results)*

---
