# Q4.7 — Tool Results (batch 3)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Co(II), Co(III)",
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
  "name": "ammonia, ethylenediamine, diethylenetriamine, triethylenetetramine, EDTA, NTA, tris(2-aminoethyl)amine, cyclam",
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
  "symbol": "Co",
  "limit": 20
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

### Step 5: `search_ligands`
**Args:**
```json
{
  "name": "ammine, ammonia, ethylenediamine, en, diethylenetriamine, dien, triethylenetetramine, trien, edta, nta, tris(2-aminoethyl)amine, tren, cyclam",
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

### Step 7: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_33",
  "order_by": "c.ligand_name_SRD ASC, s.constant_value DESC",
  "limit": 400
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. You must call 0_plan_search_strategy first (PHASE 2) before using the execution tools.

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_34",
  "order_by": "c.ligand_name_SRD ASC, s.constant_value DESC",
  "limit": 400
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. You must call 0_plan_search_strategy first (PHASE 2) before using the execution tools.

---

### Step 10: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_33, metal_34) AND c.ligand_id IN (ligand_10103, ligand_7029, ligand_6277, ligand_6165, ligand_7795, ligand_5898, ligand_5760))",
  "order_by": "c.ligand_name_SRD ASC, c.metal_id ASC, c.beta_definition_id ASC, s.temperature_c ASC, s.ionic_strength_mol_l ASC",
  "limit": 400
}
```

[summary]
## search_stability — 167 row(s)

### logK — 11 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_33 | Co^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 22 | 4 | 10~40 | 0~1 | *** | 7 |
| metal_33 | Co^[2+] | ligand_10103 | Ammonia | L | N | 17 | 5 | 25~30 | 0~5 | *** | 5 |
| metal_33 | Co^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 15 | 5 | 25~37 | 0.1~3 | *** | 6 |
| metal_33 | Co^[2+] | ligand_7795 | 1,3-Diazole (Imidazole) | L | c1c[nH]cn1 | 13 | 4 | 25~37 | 0.1~3 | *** | 4 |
| metal_34 | Co^[3+] | ligand_10103 | Ammonia | L | N | 10 | 8 | 20~30 | 0.1~2 | *** | 5 |
| metal_33 | Co^[2+] | ligand_7029 | Ethylenediamine | L | NCCN | 9 | 3 | 25~37 | 0.1~1 | *** | 3 |
| metal_34 | Co^[3+] | ligand_7029 | Ethylenediamine | L | NCCN | 8 | 4 | 25~30 | 1 | *** | 3 |
| metal_33 | Co^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 4 | 3 | 25 | 0.1~1 | *** | 2 |
| metal_33 | Co^[2+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_34 | Co^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 2 | 20~25 | 0.1 | *** | 1 |
| metal_34 | Co^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 2 | 2 | 20 | 0.1 | *** | 1 |

### ΔH — 8 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_33 | Co^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 9 | 3 | 10~40 | 0 | *** | 0 |
| metal_33 | Co^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 7 | 2 | 15~35 | 0~1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 7 | 3 | 20~25 | 0.1~1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7795 | 1,3-Diazole (Imidazole) | L | c1c[nH]cn1 | 4 | 4 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 4 | 2 | 25 | 0.1~3 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7029 | Ethylenediamine | L | NCCN | 3 | 3 | 25 | 1 | *** | 0 |
| metal_34 | Co^[3+] | ligand_10103 | Ammonia | L | N | 2 | 2 | 25 | 0 | *** | 0 |
| metal_33 | Co^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 2 | *** | 0 |

### ΔS — 8 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_33 | Co^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 6 | 3 | 25 | 0~0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7795 | 1,3-Diazole (Imidazole) | L | c1c[nH]cn1 | 4 | 4 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 4 | 2 | 25 | 0.1~3 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7029 | Ethylenediamine | L | NCCN | 3 | 3 | 25 | 1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 3 | 3 | 25 | 0.1 | *** | 0 |
| metal_34 | Co^[3+] | ligand_10103 | Ammonia | L | N | 2 | 2 | 25 | 2 | *** | 0 |
| metal_33 | Co^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 2 | *** | 0 |

---

### Step 11: `search_similar_ligands`
**Args:**
```json
{
  "ligand_id": "ligand_7029",
  "top_k": 12,
  "metal_ids": [
    "metal_33",
    "metal_34"
  ]
}
```

[TOOL ERROR] search_similar_ligands: Error executing tool search_similar_ligands: 3 validation errors for search_similar_ligandsArguments
metal_ids.str
  Input should be a valid string [type=string_type, input_value=['metal_33', 'metal_34'], input_type=list]
    For further information visit https://errors.pydantic.dev/2.11/v/string_type
metal_ids.list[int].0
  Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='metal_33', input_type=str]
    For further information visit https://errors.pydantic.dev/2.11/v/int_parsing
metal_ids.list[int].1
  Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='metal_34', input_type=str]
    For further information visit https://errors.pydantic.dev/2.11/v/int_parsing

---

### Step 12: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_33 AND c.ligand_id IN (ligand_10103, ligand_7029, ligand_6277, ligand_6165, ligand_7795))",
  "order_by": "c.ligand_id ASC, c.beta_definition_id ASC, s.temperature_c ASC, s.ionic_strength_mol_l ASC",
  "limit": 300
}
```

[summary]
## search_stability — 81 row(s)

### ΔH — 5 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_33 | Co^[2+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 7 | 3 | 20~25 | 0.1~1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 7 | 2 | 15~35 | 0~1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7795 | 1,3-Diazole (Imidazole) | L | c1c[nH]cn1 | 4 | 4 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7029 | Ethylenediamine | L | NCCN | 3 | 3 | 25 | 1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 2 | *** | 0 |

### logK — 5 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_33 | Co^[2+] | ligand_10103 | Ammonia | L | N | 17 | 5 | 25~30 | 0~5 | *** | 5 |
| metal_33 | Co^[2+] | ligand_7795 | 1,3-Diazole (Imidazole) | L | c1c[nH]cn1 | 13 | 4 | 25~37 | 0.1~3 | *** | 4 |
| metal_33 | Co^[2+] | ligand_7029 | Ethylenediamine | L | NCCN | 9 | 3 | 25~37 | 0.1~1 | *** | 3 |
| metal_33 | Co^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 4 | 3 | 25 | 0.1~1 | *** | 2 |
| metal_33 | Co^[2+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |

### ΔS — 5 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_33 | Co^[2+] | ligand_7795 | 1,3-Diazole (Imidazole) | L | c1c[nH]cn1 | 4 | 4 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 3 | 3 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7029 | Ethylenediamine | L | NCCN | 3 | 3 | 25 | 1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 2 | *** | 0 |

---

### Step 13: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_34 AND c.ligand_id IN (ligand_10103, ligand_7029, ligand_6277, ligand_6165, ligand_7795))",
  "order_by": "c.ligand_id ASC, c.beta_definition_id ASC, s.temperature_c ASC, s.ionic_strength_mol_l ASC",
  "limit": 300
}
```

[summary]
## search_stability — 26 row(s)

### `Co^[3+]` + Nitrilotriacetic acid (NTA) — 2 measurement(s)
metal_id: metal_34 | ligand_id: ligand_6165
ligand_HxL_def: H3L | ligand_SMILES: O=C(O)CN(CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_105570 | ref_eq_map_3758 | beta_def_238 | logK | 9.66 | 20 | 0.1 | `[M(OH)2L] + [H] <=> [M(OH)L] + [H2O]` | *** |  |  |
| vlm_105569 | ref_eq_map_3758 | beta_def_966 | logK | 6.84 | 20 | 0.1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |

### `Co^[3+]` + Ethylenedinitrilotetraacetic acid (EDTA) — 2 measurement(s)
metal_id: metal_34 | ligand_id: ligand_6277
ligand_HxL_def: H4L | ligand_SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_108654 | ref_eq_map_5030 | beta_def_788 | logK | 2.98 | 20 | 0.1 | `[ML] + [H] <=> [MHL]` | *** |  |  |
| vlm_108653 | ref_eq_map_5030 | beta_def_812 | logK | 41.4 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |

### `Co^[3+]` + Ethylenediamine — 8 measurement(s)
metal_id: metal_34 | ligand_id: ligand_7029
ligand_HxL_def: L | ligand_SMILES: NCCN

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_122456 | ref_eq_map_9588 | beta_def_871 | logK | 5.8 | 25 | 1 | `[M(OH)L2] + [H] <=> [ML2] + [H2O]` | *** |  |  |
| vlm_122457 | ref_eq_map_9589 | beta_def_871 | logK | 6.06 | 25 | 1 | `[M(OH)L2] + [H] <=> [ML2] + [H2O]` | *** |  |  |
| vlm_122458 | ref_eq_map_9590 | beta_def_871 | logK | 4.45 | 25 | 1 | `[M(OH)L2] + [H] <=> [ML2] + [H2O]` | *** |  |  |
| vlm_122455 | ref_eq_map_9588 | beta_def_872 | logK | 48.69 | 30 | 1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (9.92, L, +inf) |
| vlm_122454 | ref_eq_map_9588 | beta_def_888 | logK | 13.99 | 25 | 1 | `[ML2] + [L] <=> [ML3]` | *** | [L] | (9.92, L, +inf) |
| vlm_122459 | ref_eq_map_9588 | beta_def_986 | logK | 8.1 | 25 | 1 | `[M(OH)2L2] + [H] <=> [M(OH)L2] + [H2O]` | *** |  |  |
| vlm_122460 | ref_eq_map_9589 | beta_def_986 | logK | 8.19 | 25 | 1 | `[M(OH)2L2] + [H] <=> [M(OH)L2] + [H2O]` | *** |  |  |
| vlm_122461 | ref_eq_map_9590 | beta_def_986 | logK | 7.94 | 25 | 1 | `[M(OH)2L2] + [H] <=> [M(OH)L2] + [H2O]` | *** |  |  |

### `Co^[3+]` + Ammonia — 14 measurement(s)
metal_id: metal_34 | ligand_id: ligand_10103
ligand_HxL_def: L | ligand_SMILES: N

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_173305 | ref_eq_map_28140 | beta_def_882 | logK | 5.33 | 20 | 0.1 | `[H] + [M(OH)L3(fac)] <=> [ML3] + [H2O]` | *** |  |  |
| vlm_173307 | ref_eq_map_28140 | beta_def_895 | logK | 5.69 | 20 | 0.1 | `[H] + [M(OH)L4(cis)] <=> [ML4] + [H2O]` | *** |  |  |
| vlm_173310 | *** | beta_def_905 | ΔH | 0 | 25 | 0 | `[ML4] + [L] <=> [ML5]` | *** | [L] | (9.26, L, +inf) |
| vlm_173309 | ref_eq_map_28141 | beta_def_905 | logK | 5.07 | 25 | 2 | `[ML4] + [L] <=> [ML5]` | *** | [L] | (9.26, L, +inf) |
| vlm_173311 | *** | beta_def_905 | ΔS | -75.3 | 25 | 2 | `[ML4] + [L] <=> [ML5]` | *** | [L] | (9.26, L, +inf) |
| vlm_173312 | ref_eq_map_28140 | beta_def_906 | logK | 6.33 | 25 | 0.1 | *** | *** |  |  |
| vlm_173317 | ref_eq_map_28143 | beta_def_907 | logK | 34.36 | 30 | 1 | `[M] + [L]^6 <=> [ML6]` | *** | [L] | (9.26, L, +inf) |
| vlm_173318 | ref_eq_map_28144 | beta_def_907 | logK | 35.21 | 30 | 2 | `[M] + [L]^6 <=> [ML6]` | *** | [L] | (9.26, L, +inf) |
| vlm_173315 | *** | beta_def_909 | ΔH | -28.9 | 25 | 0 | `[ML5] + [L] <=> [ML6]` | *** | [L] | (9.26, L, +inf) |
| vlm_173313 | ref_eq_map_28142 | beta_def_909 | logK | 4.33 | 25 | 1 | `[ML5] + [L] <=> [ML6]` | *** | [L] | (9.26, L, +inf) |
| vlm_173314 | ref_eq_map_28141 | beta_def_909 | logK | 4.5 | 25 | 2 | `[ML5] + [L] <=> [ML6]` | *** | [L] | (9.26, L, +inf) |
| vlm_173316 | *** | beta_def_909 | ΔS | 0 | 25 | 2 | `[ML5] + [L] <=> [ML6]` | *** | [L] | (9.26, L, +inf) |
| vlm_173306 | ref_eq_map_28140 | beta_def_991 | logK | 7.6 | 20 | 0.1 | `[H] + [M(OH)2L3(fac)] <=> [M(OH)L3] + [H2O]` | *** |  |  |
| vlm_173308 | ref_eq_map_28140 | beta_def_993 | logK | 7.99 | 20 | 0.1 | `[H] + [M(OH)2L4(cis)] <=> [M(OH)L4] + [H2O]` | *** |  |  |

---
