# Q4.7 — Tool Results (batch 1)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "cobalt",
  "limit": 10
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

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "ethylenediamine",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 105 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5948 | N-(2-Aminoethyl)glycine (Ethylenediamine m… (EDMA) | HL | Amino Acids | 30 | `NCCNCC(=O)O` | (-inf, H3L, -1.9, H2L, 6.67, HL, 9.84, L, +inf) |
| ligand_6253 | N-(2-Aminoeth… (Ethylenediamine-N,N-diacetic acid) | H2L | NTA and derivatives | 39 | `NCCN(CC(=O)O)CC(=O)O` | (-inf, H2L, 5.53, HL, 10.87, L, +inf) |
| ligand_7029 | Ethylenediamine | L | Aliphatic amines | 310 | `NCCN` | (-inf, H2L, 7.11, HL, 9.92, L, +inf) |
| ligand_7030 | DL-Methylethylenediamine (1,2-Propylenediami… (pn) | L | Aliphatic amines | 86 | `CC(N)CN` | (-inf, H2L, 6.85, HL, 9.81, L, +inf) |
| ligand_7031 | DL-Ethylethylenediamine (1,2-Butylenediamine) | L | Aliphatic amines | 19 | `CCC(N)CN` | (-inf, H2L, 6.65, HL, 9.66, L, +inf) |

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

### Step 4: `search_ligands`
**Args:**
```json
{
  "name": "EDTA",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 5 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6118 | 6,11,18,23-Tetraoxo-1,4,7,10,13,16,19,… (24edtaen) | *** | Aza macrocycles with car… | 15 | *** | (-inf, H4L, 3.3, H3L, 4.18, H2L, 7.26, HL, 7.78, L, +inf) |
| ligand_6275 | N-(2-Hydroxyethyl)ethylenedinitrilotriace… (HEDTA) | H3L | EDTA and derivatives | 237 | `O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O` | (-inf, H3L, 2.62, H2L, 5.38, HL, 9.7, L, +inf) |
| ligand_6277 | Ethylenedinitrilotetraacetic acid (EDTA) | H4L | EDTA and derivatives | 596 | `O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O` | (-inf, H5L, -1.5, H4L, 2, H3L, 2.69, H2L, 6.13, HL, 9.52, L, +inf) |
| ligand_6335 | Oxybis(ethylenenitrilo)tetraacetic acid (EEDTA) | H4L | EDTA and derivatives | 124 | `O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O` | (-inf, H4L, -1.8, H3L, 2.76, H2L, 8.75, HL, 9.39, L, +inf) |
| ligand_6348 | Thiobis(ethylenenitrilo)tetraacetic acid (TEDTA) | H4L | EDTA and derivatives | 101 | `O=C(O)CN(CCSCCN(CC(=O)O)CC(=O)O)CC(=O)O` | (-inf, H4L, 2, H3L, 2.68, H2L, 8.37, HL, 9.31, L, +inf) |

### Functional groups across all SQL matches (4 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 4 | 100% |
| tertiary_amine | 4 | 100% |
| ether | 1 | 25% |
| hydroxyl | 1 | 25% |
| thioether | 1 | 25% |

---

### Step 5: `build_system_catalog`
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

### Step 6: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_34"
}
```

[summary]
[CATALOG]
## build_system_catalog — 19 pair(s), 40 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_238 | [M(OH)2L] + [H] <=> [M(OH)L] + [H2O] |  |
| beta_def_263 | [M(OH)3L] + [H] <=> [M(OH)2L] + [H2O] |  |
| beta_def_352 | [ML3(s)] <=> [M] + [L]^3 | solid |
| beta_def_788 | [ML] + [H] <=> [MHL] |  |
| beta_def_812 | [M] + [L] <=> [ML] |  |
| beta_def_840 | [M] + [L]^2 <=> [ML2] |  |
| beta_def_871 | [M(OH)L2] + [H] <=> [ML2] + [H2O] |  |
| beta_def_872 | [M] + [L]^3 <=> [ML3] |  |
| beta_def_882 | [H] + [M(OH)L3(fac)] <=> [ML3] + [H2O] |  |
| beta_def_888 | [ML2] + [L] <=> [ML3] |  |
| beta_def_894 | [M] + [L]^4 <=> [ML4] |  |
| beta_def_895 | [H] + [M(OH)L4(cis)] <=> [ML4] + [H2O] |  |
| beta_def_905 | [ML4] + [L] <=> [ML5] |  |
| beta_def_906 | *** |  |
| beta_def_907 | [M] + [L]^6 <=> [ML6] |  |
| beta_def_909 | [ML5] + [L] <=> [ML6] |  |
| beta_def_966 | [M(OH)L] + [H] <=> [ML] + [H2O] |  |
| beta_def_986 | [M(OH)2L2] + [H] <=> [M(OH)L2] + [H2O] |  |
| beta_def_991 | [H] + [M(OH)2L3(fac)] <=> [M(OH)L3] + [H2O] |  |
| beta_def_993 | [H] + [M(OH)2L4(cis)] <=> [M(OH)L4] + [H2O] |  |

*(all species aqueous unless noted)*

**1. Co^[3+] + Ammonia** (metal_34 + ligand_10103) — ligand_def_HxL: L | 14 ent, 8 sp, 14 vlms (vlm_173305…vlm_173318)
   - species: beta_def_882(1) beta_def_895(1) beta_def_905(3) beta_def_906(1) beta_def_907(2) beta_def_909(4) beta_def_991(1) beta_def_993(1)
   - eq:6 nets T:19~35°C I:-0.05~2.15M max 4n/6e
**2. Co^[3+] + Ethylenediamine** (metal_34 + ligand_7029) — ligand_def_HxL: L | 8 ent, 4 sp, 8 vlms (vlm_122454…vlm_122461)
   - species: beta_def_871(3) beta_def_872(1) beta_def_888(1) beta_def_986(3)
   - eq:3 nets T:16.5~31.5°C I:0.775~1.225M max 4n/3e
**3. Co^[3+] + Chloride ion** (metal_34 + ligand_10163) — ligand_def_HxL: *** | 4 ent, 1 sp, 4 vlms (vlm_177403…vlm_177406)
   - species: beta_def_812(4)
   - eq:2 nets T:16.5~31.5°C I:0.275~3.225M max 1n/0e
**4. Co^[3+] + Hydrogen azide (Hydrazoic acid)** (metal_34 + ligand_10106) — ligand_def_HxL: HL | 4 ent, 4 sp, 4 vlms (vlm_173620…vlm_173623)
   - species: beta_def_812(1) beta_def_840(1) beta_def_872(1) beta_def_894(1)
   - eq:1 nets T:16.5~31.5°C I:1.775~2.225M max 4n/6e
**5. Co^[3+] + Hydroxide ion** (metal_34 + ligand_10076) — ligand_def_HxL: *** | 4 ent, 2 sp, 4 vlms (vlm_170829…vlm_170832)
   - species: beta_def_352(3) beta_def_812(1)
   - eq:2 nets T:19~30°C I:-0.05~3.15M max 1n/0e
**6. Co^[3+] + 2,6-Bis(aminomethyl)pyridine** (metal_34 + ligand_8110) — ligand_def_HxL: L | 3 ent, 3 sp, 3 vlms (vlm_137656, vlm_137657, vlm_137658)
   - species: beta_def_238(1) beta_def_263(1) beta_def_966(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 3n/3e
**7. Co^[3+] + cis,cis-1,3,5-Triaminocyclohexane** (metal_34 + ligand_7096) — ligand_def_HxL: L | 3 ent, 3 sp, 3 vlms (vlm_124184, vlm_124185, vlm_124186)
   - species: beta_def_238(1) beta_def_263(1) beta_def_966(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 3n/3e
**8. Co^[3+] + Nitrilotris(ethyleneamine) [Tris(2-aminoethyl)amine] (Tren)** (metal_34 + ligand_7345) — ligand_def_HxL: L | 2 ent, 2 sp, 2 vlms (vlm_128135, vlm_128136)
   - species: beta_def_238(1) beta_def_966(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 2n/1e
**9. Co^[3+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_34 + ligand_6277) — ligand_def_HxL: H4L | 2 ent, 2 sp, 2 vlms (vlm_108653, vlm_108654)
   - species: beta_def_788(1) beta_def_812(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 2n/1e
**10. Co^[3+] + Nitrilotriacetic acid (NTA)** (metal_34 + ligand_6165) — ligand_def_HxL: H3L | 2 ent, 2 sp, 2 vlms (vlm_105569, vlm_105570)
   - species: beta_def_238(1) beta_def_966(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 2n/1e
**11. Co^[3+] + Triethylenetetranitrilohexaacetic acid (TTHA)** (metal_34 + ligand_6366) — ligand_def_HxL: H6L | 1 ent, 1 sp, 1 vlms (vlm_113179)
   - species: beta_def_812(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**12. Co^[3+] + (2-Hydroxytrimethylene)dinitrilotetraacetic acid** (metal_34 + ligand_6333) — ligand_def_HxL: H4L | 1 ent, 1 sp, 1 vlms (vlm_111656)
   - species: beta_def_812(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**13. Co^[3+] + Tetramethylenedinitrilotetraacetic acid** (metal_34 + ligand_6313) — ligand_def_HxL: H4L | 1 ent, 1 sp, 1 vlms (vlm_110747)
   - species: beta_def_812(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**14. Co^[3+] + Trimethylenedinitrilotetraacetic acid (TMDTA)** (metal_34 + ligand_6311) — ligand_def_HxL: H4L | 1 ent, 1 sp, 1 vlms (vlm_110544)
   - species: beta_def_812(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**15. Co^[3+] + trans-1,2-Cyclohexylenedinitrilotetraacetic acid (CDTA)** (metal_34 + ligand_6301) — ligand_def_HxL: H4L | 1 ent, 1 sp, 1 vlms (vlm_109807)
   - species: beta_def_812(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**16. Co^[3+] + meso-(1,2-Dimethylethylene)dinitrilotetraacetic acid** (metal_34 + ligand_6288) — ligand_def_HxL: H4L | 1 ent, 1 sp, 1 vlms (vlm_109254)
   - species: beta_def_812(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**17. Co^[3+] + DL-(Methylethylene)dinitrilotetraacetic acid (PDTA)** (metal_34 + ligand_6278) — ligand_def_HxL: H4L | 1 ent, 1 sp, 1 vlms (vlm_108903)
   - species: beta_def_812(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**18. Co^[3+] + N-(2-Hydroxyethyl)ethylenedinitrilotriacetic acid (HEDTA)** (metal_34 + ligand_6275) — ligand_def_HxL: H3L | 1 ent, 1 sp, 1 vlms (vlm_108147)
   - species: beta_def_812(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**19. Co^[3+] + Iminodiacetic acid (IDA)** (metal_34 + ligand_6127) — ligand_def_HxL: H2L | 1 ent, 1 sp, 1 vlms (vlm_104405)
   - species: beta_def_812(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_33 AND c.ligand_id = ligand_10103 AND s.constant_type = 'log_beta')",
  "order_by": "s.constant_value ASC",
  "limit": 20
}
```

[summary]
## search_stability

*(no results)*

---

### Step 9: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_34 AND c.ligand_id = ligand_10103 AND s.constant_type = 'log_beta')",
  "order_by": "s.constant_value ASC",
  "limit": 20
}
```

[summary]
## search_stability

*(no results)*

---

### Step 10: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id = metal_33 AND c.ligand_id = ligand_10103)",
  "limit": 5
}
```

[summary]
## search_networks — 17 row(s)

> **Reference equilibrium networks** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### `Co^[2+]` + Ammonia — 5 network(s)
metal_id: metal_33 | ligand_id: ligand_10103 | ligand_def_HxL: L | ligand_SMILES: N

| beta_def | equation |
|----------|----------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |
| beta_def_872 | ``[M] + [L]^3 <=> [ML3]`` |
| beta_def_894 | ``[M] + [L]^4 <=> [ML4]`` |
| beta_def_903 | ``[M] + [L]^5 <=> [ML5]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_28231 | 5 | 10 | 20~30 | -0.05~0.25 | 5 | 5 diff beta_def | logK | 2.08~5.13 |
| ref_eq_net_28232 | 5 | 10 | 19~29 | 4.85~5.15 | 5 | 5 diff beta_def | logK | 2.31~6.68 |
| ref_eq_net_28233 | 5 | 10 | 25~35 | 1.85~2.15 | 5 | 5 diff beta_def | logK | 2.14~5.75 |
| ref_eq_net_28234 | 1 | 0 | 19~29 | 0.85~1.15 | 1 | beta_def_812 | logK | 2.1 |
| ref_eq_net_28235 | 1 | 0 | 19~29 | -0.15~0.15 | 1 | beta_def_812 | logK | 2.03 |

#### Reference-state network: ref_eq_net_28231 (5 nodes)
> First network — reference conditions (T 20~30 °C, I -0.05~0.25 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 2.08 |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` | logK | 3.5 |
| beta_def_872 | ``[M] + [L]^3 <=> [ML3]`` | logK | 4.43 |
| beta_def_894 | ``[M] + [L]^4 <=> [ML4]`` | logK | 5.07 |
| beta_def_903 | ``[M] + [L]^5 <=> [ML5]`` | logK | 5.13 |

---

### Step 11: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id = metal_34 AND c.ligand_id = ligand_10103)",
  "limit": 5
}
```

[summary]
## search_networks — 9 row(s)

> **Reference equilibrium networks** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### `Co^[3+]` + Ammonia — 5 network(s)
metal_id: metal_34 | ligand_id: ligand_10103 | ligand_def_HxL: L | ligand_SMILES: N

| beta_def | equation |
|----------|----------|
| beta_def_882 | ``[H] + [M(OH)L3(fac)] <=> [ML3] + [H2O]`` |
| beta_def_991 | ``[H] + [M(OH)2L3(fac)] <=> [M(OH)L3] + [H2O]`` |
| beta_def_895 | ``[H] + [M(OH)L4(cis)] <=> [ML4] + [H2O]`` |
| beta_def_993 | ``[H] + [M(OH)2L4(cis)] <=> [M(OH)L4] + [H2O]`` |
| beta_def_906 | — |
| beta_def_909 | ``[ML5] + [L] <=> [ML6]`` |
| beta_def_905 | ``[ML4] + [L] <=> [ML5]`` |
| beta_def_907 | ``[M] + [L]^6 <=> [ML6]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_28249 | 4 | 6 | 20~30 | -0.05~0.25 | 4 | 4 diff beta_def | logK | 5.33~7.99 |
| ref_eq_net_28250 | 1 | 0 | 20~30 | -0.05~0.25 | 1 | beta_def_906 | logK | 6.33 |
| ref_eq_net_28251 | 2 | 1 | 19~29 | 1.85~2.15 | 2 | beta_def_909; beta_def_905 | logK | 4.5~5.07 |
| ref_eq_net_28252 | 1 | 0 | 19~29 | 0.85~1.15 | 1 | beta_def_909 | logK | 4.33 |
| ref_eq_net_28253 | 1 | 0 | 25~35 | 0.85~1.15 | 1 | beta_def_907 | logK | 34.36 |

#### Reference-state network: ref_eq_net_28249 (4 nodes)
> First network — reference conditions (T 20~30 °C, I -0.05~0.25 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_882 | ``[H] + [M(OH)L3(fac)] <=> [ML3] + [H2O]`` | logK | 5.33 |
| beta_def_895 | ``[H] + [M(OH)L4(cis)] <=> [ML4] + [H2O]`` | logK | 5.69 |
| beta_def_991 | ``[H] + [M(OH)2L3(fac)] <=> [M(OH)L3] + [H2O]`` | logK | 7.6 |
| beta_def_993 | ``[H] + [M(OH)2L4(cis)] <=> [M(OH)L4] + [H2O]`` | logK | 7.99 |

---

### Step 12: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id = metal_33 AND c.ligand_id = ligand_7029)",
  "limit": 5
}
```

[summary]
## search_networks — 9 row(s)

> **Reference equilibrium networks** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### `Co^[2+]` + Ethylenediamine — 3 network(s)
metal_id: metal_33 | ligand_id: ligand_7029 | ligand_def_HxL: L | ligand_SMILES: NCCN

| beta_def | equation |
|----------|----------|
| beta_def_872 | ``[M] + [L]^3 <=> [ML3]`` |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |
| beta_def_812 | ``[M] + [L] <=> [ML]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_9588 | 3 | 3 | 20~30 | -0.05~0.25 | 3 | beta_def_812; beta_def_840; beta_def_872 | logK | 5.5~13.4 |
| ref_eq_net_9589 | 3 | 3 | 31~41 | 0~0.3 | 3 | beta_def_872; beta_def_812; beta_def_840 | logK | -12~9.57 |
| ref_eq_net_9590 | 3 | 3 | 19~29 | 0.85~1.15 | 3 | beta_def_812; beta_def_840; beta_def_872 | logK | 5.75~14 |

#### Reference-state network: ref_eq_net_9588 (3 nodes)
> First network — reference conditions (T 20~30 °C, I -0.05~0.25 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 5.5 |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` | logK | 10.1 |
| beta_def_872 | ``[M] + [L]^3 <=> [ML3]`` | logK | 13.4 |

---

### Step 13: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id = metal_34 AND c.ligand_id = ligand_7029)",
  "limit": 5
}
```

[summary]
## search_networks — 8 row(s)

> **Reference equilibrium networks** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### `Co^[3+]` + Ethylenediamine — 3 network(s)
metal_id: metal_34 | ligand_id: ligand_7029 | ligand_def_HxL: L | ligand_SMILES: NCCN

| beta_def | equation |
|----------|----------|
| beta_def_871 | ``[M(OH)L2] + [H] <=> [ML2] + [H2O]`` |
| beta_def_986 | ``[M(OH)2L2] + [H] <=> [M(OH)L2] + [H2O]`` |
| beta_def_888 | ``[ML2] + [L] <=> [ML3]`` |
| beta_def_872 | ``[M] + [L]^3 <=> [ML3]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_9611 | 4 | 3 | 16.5~31.5 | 0.775~1.225 | 4 | 4 diff beta_def | logK | 5.8~48.69 |
| ref_eq_net_9612 | 2 | 1 | 16.5~31.5 | 0.775~1.225 | 2 | beta_def_871; beta_def_986 | logK | 6.06~8.19 |
| ref_eq_net_9613 | 2 | 1 | 16.5~31.5 | 0.775~1.225 | 2 | beta_def_871; beta_def_986 | logK | 4.45~7.94 |

#### Reference-state network: ref_eq_net_9611 (4 nodes)
> First network — reference conditions (T 16.5~31.5 °C, I 0.775~1.225 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_871 | ``[M(OH)L2] + [H] <=> [ML2] + [H2O]`` | logK | 5.8 |
| beta_def_986 | ``[M(OH)2L2] + [H] <=> [M(OH)L2] + [H2O]`` | logK | 8.1 |
| beta_def_888 | ``[ML2] + [L] <=> [ML3]`` | logK | 13.99 |
| beta_def_872 | ``[M] + [L]^3 <=> [ML3]`` | logK | 48.69 |

---

### Step 14: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id = metal_33 AND c.ligand_id = ligand_6277)",
  "limit": 5
}
```

[summary]
## search_networks — 4 row(s)

> **Reference equilibrium networks** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### `Co^[2+]` + Ethylenedinitrilotetraacetic acid (EDTA) — 2 network(s)
metal_id: metal_33 | ligand_id: ligand_6277 | ligand_def_HxL: H4L | ligand_SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O

| beta_def | equation |
|----------|----------|
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` |
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_739 | ``[MHL] + [H] <=> [MH2L]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_5021 | 2 | 1 | 20~30 | -0.05~0.25 | 2 | beta_def_788; beta_def_812 | logK | 3~16.45 |
| ref_eq_net_5022 | 2 | 1 | 19~29 | 0.85~1.15 | 2 | beta_def_739; beta_def_788 | logK | -1.7~3 |

#### Reference-state network: ref_eq_net_5021 (2 nodes)
> First network — reference conditions (T 20~30 °C, I -0.05~0.25 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` | logK | 3 |
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 16.45 |

---

### Step 15: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id = metal_34 AND c.ligand_id = ligand_6277)",
  "limit": 5
}
```

[summary]
## search_networks — 2 row(s)

> **Reference equilibrium networks** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### `Co^[3+]` + Ethylenedinitrilotetraacetic acid (EDTA) — 1 network(s)
metal_id: metal_34 | ligand_id: ligand_6277 | ligand_def_HxL: H4L | ligand_SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O

| beta_def | equation |
|----------|----------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_5036 | 2 | 1 | 20~30 | -0.05~0.25 | 2 | beta_def_788; beta_def_812 | logK | 2.98~41.4 |

#### Reference-state network: ref_eq_net_5036 (2 nodes)
> First network — reference conditions (T 20~30 °C, I -0.05~0.25 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` | logK | 2.98 |
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 41.4 |

---

### Step 16: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id = metal_33 AND c.ligand_id = ligand_6165)",
  "limit": 5
}
```

[summary]
## search_networks — 3 row(s)

> **Reference equilibrium networks** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### `Co^[2+]` + Nitrilotriacetic acid (NTA) — 1 network(s)
metal_id: metal_33 | ligand_id: ligand_6165 | ligand_def_HxL: H3L | ligand_SMILES: O=C(O)CN(CC(=O)O)CC(=O)O

| beta_def | equation |
|----------|----------|
| beta_def_966 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |
| beta_def_812 | ``[M] + [L] <=> [ML]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_3749 | 3 | 2 | 20~30 | -0.05~0.25 | 3 | beta_def_812; beta_def_966; beta_def_840 | logK | 10.38~14.33 |

#### Reference-state network: ref_eq_net_3749 (3 nodes)
> First network — reference conditions (T 20~30 °C, I -0.05~0.25 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 10.38 |
| beta_def_966 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` | logK | 10.8 |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` | logK | 14.33 |

---

### Step 17: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id = metal_34 AND c.ligand_id = ligand_6165)",
  "limit": 5
}
```

[summary]
## search_networks — 2 row(s)

> **Reference equilibrium networks** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### `Co^[3+]` + Nitrilotriacetic acid (NTA) — 1 network(s)
metal_id: metal_34 | ligand_id: ligand_6165 | ligand_def_HxL: H3L | ligand_SMILES: O=C(O)CN(CC(=O)O)CC(=O)O

| beta_def | equation |
|----------|----------|
| beta_def_966 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` |
| beta_def_238 | ``[M(OH)2L] + [H] <=> [M(OH)L] + [H2O]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_3763 | 2 | 1 | 20~30 | -0.05~0.25 | 2 | beta_def_966; beta_def_238 | logK | 6.84~9.66 |

#### Reference-state network: ref_eq_net_3763 (2 nodes)
> First network — reference conditions (T 20~30 °C, I -0.05~0.25 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_966 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` | logK | 6.84 |
| beta_def_238 | ``[M(OH)2L] + [H] <=> [M(OH)L] + [H2O]`` | logK | 9.66 |

---

### Step 18: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id = metal_33 AND c.ligand_id = ligand_6127)",
  "limit": 5
}
```

[summary]
## search_networks — 4 row(s)

> **Reference equilibrium networks** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### `Co^[2+]` + Iminodiacetic acid (IDA) — 2 network(s)
metal_id: metal_33 | ligand_id: ligand_6127 | ligand_def_HxL: H2L | ligand_SMILES: O=C(O)CNCC(=O)O

| beta_def | equation |
|----------|----------|
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |
| beta_def_812 | ``[M] + [L] <=> [ML]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_3275 | 2 | 1 | 20~30 | -0.05~0.25 | 2 | beta_def_812; beta_def_840 | logK | 6.97~12.2 |
| ref_eq_net_3276 | 2 | 1 | 19~29 | 0.85~1.15 | 2 | beta_def_812; beta_def_840 | logK | 6.54~11.8 |

#### Reference-state network: ref_eq_net_3275 (2 nodes)
> First network — reference conditions (T 20~30 °C, I -0.05~0.25 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 6.97 |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` | logK | 12.2 |

---

### Step 19: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id = metal_34 AND c.ligand_id = ligand_6127)",
  "limit": 5
}
```

[summary]
## search_networks — 1 row(s)

> **Reference equilibrium networks** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### `Co^[3+]` + Iminodiacetic acid (IDA) — 1 network(s)
metal_id: metal_34 | ligand_id: ligand_6127 | ligand_def_HxL: H2L | ligand_SMILES: O=C(O)CNCC(=O)O

| beta_def | equation |
|----------|----------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_3293 | 1 | 0 | 20~30 | -0.05~0.25 | 1 | beta_def_812 | logK | 29.6 |

#### Reference-state network: ref_eq_net_3293 (1 nodes)
> First network — reference conditions (T 20~30 °C, I -0.05~0.25 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 29.6 |

---
