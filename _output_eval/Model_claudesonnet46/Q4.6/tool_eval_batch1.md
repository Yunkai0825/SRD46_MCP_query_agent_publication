# Q4.6 — Tool Results (batch 1)

### Step 2: `search_metals`
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

### Step 5: `search_metals`
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

### Step 8: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_94"
}
```

[summary]
[CATALOG]
## build_system_catalog — 20 pair(s), 57 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_194 | [M] + [HL]^2 <=> [M(HL)2] |  |
| beta_def_204 | [MHL2] + [H] <=> [M(HL)2] |  |
| beta_def_311 | [ML(s)] <=> [M] + [L] | solid |
| beta_def_321 | [ML(s,rhodochrosite)] <=> [M] + [L] | solid |
| beta_def_334 | [ML2(s)] <=> [M] + [L]^2 | solid |
| beta_def_374 | [M]^2 + [L]^2 <=> [M2(H-1L)2] + [H]^2 |  |
| beta_def_502 | [M]^2 + [L] <=> [M2L] |  |
| beta_def_540 | [M]^2 + [L]^3 <=> [M2L3] |  |
| beta_def_732 | [M] + [H2L] <=> [MH2L] |  |
| beta_def_779 | [M] + [HL] <=> [MHL] |  |
| beta_def_788 | [ML] + [H] <=> [MHL] |  |
| beta_def_792 | [ML2] + [H] <=> [MHL2] |  |
| beta_def_812 | [M] + [L] <=> [ML] |  |
| beta_def_823 | [M] + [H2L] <=> [ML] + [H]^2 |  |
| beta_def_840 | [M] + [L]^2 <=> [ML2] |  |
| beta_def_853 | [ML] + [H2L] <=> [ML2] + [H]^2 |  |
| beta_def_872 | [M] + [L]^3 <=> [ML3] |  |
| beta_def_876 | [ML2] + [H2L] <=> [ML3] + [H]^2 |  |
| beta_def_894 | [M] + [L]^4 <=> [ML4] |  |

*(all species aqueous unless noted)*

**1. Mn^[2+] + Ammonia** (metal_94 + ligand_10103) — ligand_def_HxL: L | 32 ent, 4 sp, 32 vlms (vlm_173099…vlm_173130)
   - species: beta_def_812(8) beta_def_840(8) beta_def_872(8) beta_def_894(8)
   - eq:6 nets T:19~30°C I:-0.05~5.15M max 4n/6e
**2. Mn^[2+] + Aminoacetic acid (Glycine)** (metal_94 + ligand_5760) — ligand_def_HxL: HL | 14 ent, 2 sp, 14 vlms (vlm_93733…vlm_93746)
   - species: beta_def_812(11) beta_def_840(3)
   - eq:6 nets T:5~45°C I:-0.15~0.65M max 2n/1e
**3. Mn^[2+] + Nitrate ion** (metal_94 + ligand_10109) — ligand_def_HxL: *** | 12 ent, 2 sp, 12 vlms (vlm_173955…vlm_173966)
   - species: beta_def_812(6) beta_def_840(6)
   - eq:6 nets T:19~30°C I:-0.05~4.15M max 2n/1e
**4. Mn^[2+] + Hydroxide ion** (metal_94 + ligand_10076) — ligand_def_HxL: *** | 12 ent, 5 sp, 12 vlms (vlm_170660…vlm_170671)
   - species: beta_def_334(1) beta_def_502(2) beta_def_540(2) beta_def_812(6) beta_def_894(1)
   - eq:4 nets T:19~30°C I:-0.15~2.15M max 5n/10e
**5. Mn^[2+] + L-2-Amino-3-(4-hydroxyphenyl)propanoic acid (Tyrosine)** (metal_94 + ligand_5819) — ligand_def_HxL: H2L | 12 ent, 4 sp, 12 vlms (vlm_96246…vlm_96257)
   - species: beta_def_194(3) beta_def_204(3) beta_def_779(3) beta_def_792(3)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 4n/3e
**6. Mn^[2+] + DL-2-Amino-3-(3-hydroxyphenyl)propanoic acid (m-Tyrosine)** (metal_94 + ligand_5818) — ligand_def_HxL: H2L | 12 ent, 4 sp, 12 vlms (vlm_96152…vlm_96163)
   - species: beta_def_194(3) beta_def_204(3) beta_def_779(3) beta_def_792(3)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 4n/3e
**7. Mn^[2+] + 5-Hydroxy-2-hydroxymethyl-4-pyrone (Kojic acid)** (metal_94 + ligand_9593) — ligand_def_HxL: HL | 11 ent, 3 sp, 11 vlms (vlm_166471…vlm_166481)
   - species: beta_def_812(4) beta_def_840(4) beta_def_872(3)
   - eq:2 nets T:19~30°C I:-0.05~2.15M max 3n/3e
**8. Mn^[2+] + Ethylenediamine** (metal_94 + ligand_7029) — ligand_def_HxL: L | 11 ent, 3 sp, 11 vlms (vlm_122330…vlm_122340)
   - species: beta_def_812(4) beta_def_840(4) beta_def_872(3)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 3n/3e
**9. Mn^[2+] + Hydrogen fluoride (Hydrofluoric acid)** (metal_94 + ligand_10162) — ligand_def_HxL: HL | 10 ent, 1 sp, 10 vlms (vlm_176944…vlm_176953)
   - species: beta_def_812(10)
   - eq:6 nets T:19~30°C I:-0.15~3.15M max 1n/0e
**10. Mn^[2+] + Hydrogen sulfate ion (Sulfuric acid)** (metal_94 + ligand_10148) — ligand_def_HxL: HL | 10 ent, 1 sp, 10 vlms (vlm_176001…vlm_176010)
   - species: beta_def_812(10)
   - eq:6 nets T:19~30°C I:-0.05~4.15M max 1n/0e
**11. Mn^[2+] + Hydrogen carbonate (Carbonic acid)** (metal_94 + ligand_10096) — ligand_def_HxL: H2L | 10 ent, 4 sp, 10 vlms (vlm_172852…vlm_172861)
   - species: beta_def_311(3) beta_def_321(1) beta_def_779(4) beta_def_812(2)
   - eq:3 nets T:19~30°C I:-0.05~3.15M max 4n/6e
**12. Mn^[2+] + Pentane-2,4-dione (Acetylacetone)** (metal_94 + ligand_9526) — ligand_def_HxL: *** | 10 ent, 2 sp, 10 vlms (vlm_165373…vlm_165382)
   - species: beta_def_812(5) beta_def_840(5)
   - eq:3 nets T:19~30°C I:-0.15~1.15M max 2n/1e
**13. Mn^[2+] + 1,2-Dihydroxybenzene-3,5-disulfonic acid (Tiron)** (metal_94 + ligand_9358) — ligand_def_HxL: H4L | 10 ent, 4 sp, 10 vlms (vlm_162048…vlm_162057)
   - species: beta_def_788(3) beta_def_823(3) beta_def_853(2) beta_def_876(2)
   - eq:3 nets T:19~30°C I:-0.15~1.15M max 4n/6e
**14. Mn^[2+] + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid)** (metal_94 + ligand_9058) — ligand_def_HxL: H3L | 10 ent, 4 sp, 10 vlms (vlm_157609…vlm_157618)
   - species: beta_def_374(2) beta_def_732(1) beta_def_779(2) beta_def_812(5)
   - eq:5 nets T:19~41°C I:-0.05~0.3M max 4n/6e
**15. Mn^[2+] + L-2-Amino-3-(4-imidazolyl)propanoic acid (Histidine)** (metal_94 + ligand_5898) — ligand_def_HxL: HL | 10 ent, 2 sp, 10 vlms (vlm_98771…vlm_98780)
   - species: beta_def_812(5) beta_def_840(5)
   - eq:3 nets T:19~41°C I:-0.05~3.15M max 2n/1e
**16. Mn^[2+] + L-2-Amino-3-hydroxypropanoic acid (Serine)** (metal_94 + ligand_5828) — ligand_def_HxL: HL | 10 ent, 2 sp, 10 vlms (vlm_96529…vlm_96538)
   - species: beta_def_812(5) beta_def_840(5)
   - eq:3 nets T:19~41°C I:-0.05~3.15M max 2n/1e
**17. Mn^[2+] + 3-Hydroxy-2-methyl-4-pyrone (Maltol)** (metal_94 + ligand_9586) — ligand_def_HxL: HL | 9 ent, 3 sp, 9 vlms (vlm_166200…vlm_166208)
   - species: beta_def_812(3) beta_def_840(3) beta_def_872(3)
   - eq:1 nets T:16.5~31.5°C I:1.775~2.225M max 3n/3e
**18. Mn^[2+] + Adenosine-5'-(trihydrogendiphosphate) (ADP)** (metal_94 + ligand_8318) — ligand_def_HxL: H3L | 9 ent, 2 sp, 9 vlms (vlm_141334…vlm_141342)
   - species: beta_def_779(1) beta_def_812(8)
   - eq:4 nets T:19~41°C I:-0.05~0.3M max 2n/1e
**19. Mn^[2+] + 1,10-Phenanthroline (Dipyridino[a,c]benzene)** (metal_94 + ligand_8191) — ligand_def_HxL: L | 9 ent, 3 sp, 9 vlms (vlm_139257…vlm_139265)
   - species: beta_def_812(3) beta_def_840(3) beta_def_872(3)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 3n/3e
**20. Mn^[2+] + Nitrilotriacetic acid (NTA)** (metal_94 + ligand_6165) — ligand_def_HxL: H3L | 9 ent, 2 sp, 9 vlms (vlm_105486…vlm_105494)
   - species: beta_def_812(5) beta_def_840(4)
   - eq:3 nets T:15~30°C I:-0.15~0.25M max 2n/1e

---

### Step 9: `build_system_catalog`
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

### Step 10: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_33"
}
```

[summary]
[CATALOG]
## build_system_catalog — 20 pair(s), 75 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_194 | [M] + [HL]^2 <=> [M(HL)2] |  |
| beta_def_204 | [MHL2] + [H] <=> [M(HL)2] |  |
| beta_def_208 | [M] + [HL]^3 <=> [M(HL)3] |  |
| beta_def_214 | [MH2L3] + [H] <=> [M(HL)3] |  |
| beta_def_334 | [ML2(s)] <=> [M] + [L]^2 | solid |
| beta_def_502 | [M]^2 + [L] <=> [M2L] |  |
| beta_def_674 | [M]^4 + [L]^4 <=> [M4L4] |  |
| beta_def_739 | [MHL] + [H] <=> [MH2L] |  |
| beta_def_744 | [MHL3] + [H] <=> [MH2L3] |  |
| beta_def_779 | [M] + [HL] <=> [MHL] |  |
| beta_def_788 | [ML] + [H] <=> [MHL] |  |
| beta_def_792 | [ML2] + [H] <=> [MHL2] |  |
| beta_def_803 | [ML3] + [H] <=> [MHL3] |  |
| beta_def_812 | [M] + [L] <=> [ML] |  |
| beta_def_840 | [M] + [L]^2 <=> [ML2] |  |
| beta_def_872 | [M] + [L]^3 <=> [ML3] |  |
| beta_def_894 | [M] + [L]^4 <=> [ML4] |  |
| beta_def_903 | [M] + [L]^5 <=> [ML5] |  |
| beta_def_966 | [M(OH)L] + [H] <=> [ML] + [H2O] |  |
| beta_def_984 | [M(OH)L2] + [H] <=> [ML2] + [H2O] |  |

*(all species aqueous unless noted)*

**1. Co^[2+] + Aminoacetic acid (Glycine)** (metal_33 + ligand_5760) — ligand_def_HxL: HL | 37 ent, 4 sp, 37 vlms (vlm_93761…vlm_93797)
   - species: beta_def_812(12) beta_def_840(12) beta_def_872(12) beta_def_966(1)
   - eq:7 nets T:5~45°C I:-0.15~1.15M max 4n/4e
**2. Co^[2+] + L-2-Amino-3-(4-imidazolyl)propanoic acid (Histidine)** (metal_33 + ligand_5898) — ligand_def_HxL: HL | 23 ent, 5 sp, 23 vlms (vlm_98787…vlm_98809)
   - species: beta_def_788(1) beta_def_792(2) beta_def_812(7) beta_def_840(12) beta_def_984(1)
   - eq:6 nets T:19~41°C I:-0.05~3.15M max 4n/4e
**3. Co^[2+] + 1,3-Diazole (Imidazole)** (metal_33 + ligand_7795) — ligand_def_HxL: L | 21 ent, 4 sp, 21 vlms (vlm_133831…vlm_133851)
   - species: beta_def_812(6) beta_def_840(5) beta_def_872(5) beta_def_894(5)
   - eq:4 nets T:19~41°C I:-0.05~3.15M max 4n/6e
**4. Co^[2+] + Ammonia** (metal_33 + ligand_10103) — ligand_def_HxL: L | 19 ent, 5 sp, 19 vlms (vlm_173163…vlm_173181)
   - species: beta_def_812(7) beta_def_840(3) beta_def_872(3) beta_def_894(3) beta_def_903(3)
   - eq:5 nets T:19~35°C I:-0.15~5.15M max 5n/10e
**5. Co^[2+] + Iminodiacetic acid (IDA)** (metal_33 + ligand_6127) — ligand_def_HxL: H2L | 19 ent, 2 sp, 19 vlms (vlm_104319…vlm_104337)
   - species: beta_def_812(10) beta_def_840(9)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 2n/1e
**6. Co^[2+] + 2,2'-Bipyridyl** (metal_33 + ligand_8156) — ligand_def_HxL: L | 18 ent, 3 sp, 18 vlms (vlm_138573…vlm_138590)
   - species: beta_def_812(6) beta_def_840(6) beta_def_872(6)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 3n/3e
**7. Co^[2+] + 2-(Methylaminomethyl)pyridine** (metal_33 + ligand_8112) — ligand_def_HxL: L | 17 ent, 3 sp, 17 vlms (vlm_137679…vlm_137695)
   - species: beta_def_812(7) beta_def_840(7) beta_def_872(3)
   - eq:3 nets T:19~30°C I:-0.15~0.65M max 3n/3e
**8. Co^[2+] + N-(2-Hydroxyethyl)iminodiacetic acid (HIDA)** (metal_33 + ligand_6204) — ligand_def_HxL: H2L | 17 ent, 3 sp, 17 vlms (vlm_106694…vlm_106710)
   - species: beta_def_812(8) beta_def_840(8) beta_def_966(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 3n/2e
**9. Co^[2+] + Hydrogen thiocyanate (Thiocyanic acid)** (metal_33 + ligand_10092) — ligand_def_HxL: HL | 16 ent, 2 sp, 16 vlms (vlm_172219…vlm_172234)
   - species: beta_def_812(10) beta_def_840(6)
   - eq:6 nets T:19~30°C I:-0.15~3.15M max 2n/1e
**10. Co^[2+] + 4-(2-Aminoethyl)imidazole (Histamine)** (metal_33 + ligand_7849) — ligand_def_HxL: L | 16 ent, 4 sp, 16 vlms (vlm_134624…vlm_134639)
   - species: beta_def_812(6) beta_def_840(6) beta_def_872(3) beta_def_966(1)
   - eq:4 nets T:19~41°C I:-0.15~1.15M max 4n/4e
**11. Co^[2+] + 2-(Aminomethyl)pyridine (2-Picolylamine)** (metal_33 + ligand_8081) — ligand_def_HxL: L | 15 ent, 3 sp, 15 vlms (vlm_137413…vlm_137427)
   - species: beta_def_812(5) beta_def_840(5) beta_def_872(5)
   - eq:3 nets T:19~30°C I:-0.15~0.65M max 3n/3e
**12. Co^[2+] + Ethylenediamine** (metal_33 + ligand_7029) — ligand_def_HxL: L | 15 ent, 3 sp, 15 vlms (vlm_122350…vlm_122364)
   - species: beta_def_812(5) beta_def_840(5) beta_def_872(5)
   - eq:3 nets T:19~41°C I:-0.05~1.15M max 3n/3e
**13. Co^[2+] + L-2-Amino-3-(4-hydroxyphenyl)propanoic acid (Tyrosine)** (metal_33 + ligand_5819) — ligand_def_HxL: H2L | 15 ent, 9 sp, 15 vlms (vlm_96258…vlm_96272)
   - species: beta_def_194(3) beta_def_204(3) beta_def_208(1) beta_def_214(1) beta_def_744(1) beta_def_779(1) beta_def_788(1) beta_def_792(3) beta_def_803(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 9n/21e
**14. Co^[2+] + Hydroxide ion** (metal_33 + ligand_10076) — ligand_def_HxL: *** | 14 ent, 7 sp, 14 vlms (vlm_170685…vlm_170698)
   - species: beta_def_334(2) beta_def_502(2) beta_def_674(2) beta_def_812(3) beta_def_840(2) beta_def_872(2) beta_def_894(1)
   - eq:3 nets T:19~30°C I:-0.05~3.15M max 7n/21e
**15. Co^[2+] + Ethanedioic acid (Oxalic acid)** (metal_33 + ligand_8872) — ligand_def_HxL: H2L | 14 ent, 4 sp, 14 vlms (vlm_151751…vlm_151764)
   - species: beta_def_194(1) beta_def_779(1) beta_def_812(6) beta_def_840(6)
   - eq:4 nets T:19~30°C I:-0.15~1.15M max 4n/6e
**16. Co^[2+] + L-2-Amino-3-phenylpropanoic acid (Phenylalanine)** (metal_33 + ligand_5777) — ligand_def_HxL: HL | 14 ent, 2 sp, 14 vlms (vlm_95013…vlm_95026)
   - species: beta_def_812(7) beta_def_840(7)
   - eq:2 nets T:19~30°C I:-0.05~3.15M max 2n/1e
**17. Co^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_33 + ligand_6277) — ligand_def_HxL: H4L | 13 ent, 3 sp, 13 vlms (vlm_108572…vlm_108584)
   - species: beta_def_739(1) beta_def_788(4) beta_def_812(8)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 2n/1e
**18. Co^[2+] + Nitrilotriacetic acid (NTA)** (metal_33 + ligand_6165) — ligand_def_HxL: H3L | 13 ent, 3 sp, 13 vlms (vlm_105502…vlm_105514)
   - species: beta_def_812(5) beta_def_840(5) beta_def_966(3)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 3n/2e
**19. Co^[2+] + D-2-Hydroxypropanoic acid (Lactic acid)** (metal_33 + ligand_8641) — ligand_def_HxL: HL | 12 ent, 3 sp, 12 vlms (vlm_147708…vlm_147719)
   - species: beta_def_812(5) beta_def_840(4) beta_def_872(3)
   - eq:4 nets T:15~30°C I:-0.05~2.15M max 3n/3e
**20. Co^[2+] + L-2-Amino-3-(3-indolyl)propanoic acid (Tryptophan)** (metal_33 + ligand_5907) — ligand_def_HxL: HL | 12 ent, 3 sp, 12 vlms (vlm_99138…vlm_99149)
   - species: beta_def_812(5) beta_def_840(4) beta_def_872(3)
   - eq:3 nets T:19~41°C I:-0.05~3.15M max 3n/3e

---

### Step 12: `search_ligands`
**Args:**
```json
{
  "name": "glycine",
  "limit": 3
}
```

[summary]
## search_ligands — 3 result(s)

**stats:** 170 SQL matches · showing 3 · limit 3

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5760 | Aminoacetic acid (Glycine) | HL | Amino Acids | 428 | `NCC(=O)O` | (-inf, H2L, 2.33, HL, 9.57, L, +inf) |
| ligand_5776 | DL-Aminophenylacetic acid (Phenylglycine) | HL | Amino Acids | 12 | `NC(C(=O)O)c1ccccc1` | (-inf, H2L, -1.9, HL, 8.92, L, +inf) |
| ligand_5786 | DL-Amino-4-sulfophenylacet… (4-Sulfophenylglycine) | H2L | Amino Acids | 12 | `NC(C(=O)O)c1ccc(S(=O)(=O)O)cc1` | (-inf, H2L, -1.8, HL, 8.66, L, +inf) |

### Functional groups across all SQL matches (129 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 114 | 88% |
| amide | 96 | 74% |
| primary_amine | 78 | 60% |
| aromatic_ring | 26 | 20% |
| hydroxyl | 25 | 19% |
| secondary_amine | 22 | 17% |
| tertiary_amine | 14 | 11% |
| ester | 9 | 7% |
| thiol | 9 | 7% |
| phenol | 7 | 5% |
| imine | 5 | 4% |
| phosphonate | 3 | 2% |
| thioether | 3 | 2% |
| phosphate | 2 | 2% |
| pyridine | 2 | 2% |
| sulfonate | 2 | 2% |
| ether | 1 | 1% |

---

### Step 13: `search_ligands`
**Args:**
```json
{
  "name": "ethylenediamine",
  "limit": 3
}
```

[summary]
## search_ligands — 3 result(s)

**stats:** 105 SQL matches · showing 3 · limit 3

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5948 | N-(2-Aminoethyl)glycine (Ethylenediamine m… (EDMA) | HL | Amino Acids | 30 | `NCCNCC(=O)O` | (-inf, H3L, -1.9, H2L, 6.67, HL, 9.84, L, +inf) |
| ligand_6253 | N-(2-Aminoeth… (Ethylenediamine-N,N-diacetic acid) | H2L | NTA and derivatives | 39 | `NCCN(CC(=O)O)CC(=O)O` | (-inf, H2L, 5.53, HL, 10.87, L, +inf) |
| ligand_7029 | Ethylenediamine | L | Aliphatic amines | 310 | `NCCN` | (-inf, H2L, 7.11, HL, 9.92, L, +inf) |

### Functional groups across all SQL matches (85 parseable SMILES)

| group | count | % |
|-------|-------|---|
| primary_amine | 58 | 68% |
| secondary_amine | 43 | 51% |
| tertiary_amine | 23 | 27% |
| hydroxyl | 14 | 16% |
| aromatic_ring | 13 | 15% |
| amide | 7 | 8% |
| phosphonate | 4 | 5% |
| thioether | 4 | 5% |
| phenol | 3 | 4% |
| pyridine | 3 | 4% |
| carboxyl | 2 | 2% |
| sulfonate | 1 | 1% |
| thiol | 1 | 1% |

---

### Step 14: `search_ligands`
**Args:**
```json
{
  "name": "1,10-phenanthroline",
  "limit": 3
}
```

[summary]
## search_ligands — 3 result(s)

**stats:** 15 SQL matches · showing 3 · limit 3

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8191 | 1,10-Phenanthroline (Dipyridino[a,c]benzene) | L | Phenanthrolines | 168 | `c1cnc2c(c1)ccc1cccnc12` | (-inf, H2L, -1.8, HL, 4.92, L, +inf) |
| ligand_8192 | 2-Methyl-1,10-phenanthroline | L | Phenanthrolines | 25 | `Cc1ccc2ccc3cccnc3c2n1` | (-inf, HL, 5.31, L, +inf) |
| ligand_8193 | 5-Methyl-1,10-phenanthroline | L | Phenanthrolines | 30 | `Cc1cc2cccnc2c2ncccc12` | (-inf, HL, 5.27, L, +inf) |

### Functional groups across all SQL matches (11 parseable SMILES)

| group | count | % |
|-------|-------|---|
| aromatic_ring | 11 | 100% |
| pyridine | 11 | 100% |
| halide | 3 | 27% |
| tertiary_amine | 1 | 9% |

---

### Step 16: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_5760 AND s.constant_type = 'log_beta' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 60
}
```

[summary]
## search_stability

*(no results)*

---

### Step 17: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_7029 AND s.constant_type = 'log_beta' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 60
}
```

[summary]
## search_stability

*(no results)*

---

### Step 18: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_8191 AND s.constant_type = 'log_beta' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 60
}
```

[summary]
## search_stability

*(no results)*

---
