# Q4.7 — Tool Results (batch 4)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "cobalt"
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
  "name": "ammonia",
  "limit": 5
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_10103 | Ammonia | L | Inorganic ligands | 447 | `N` | (-inf, HL, 9.26, L, +inf) |

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

### Step 6: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_34",
  "order_by": "s.constant_value DESC",
  "limit": 100
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. You must call 0_plan_search_strategy first (PHASE 2) before using the execution tools.

---
