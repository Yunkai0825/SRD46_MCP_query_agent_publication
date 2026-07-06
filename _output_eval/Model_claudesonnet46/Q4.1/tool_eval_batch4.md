# Q4.1 — Tool Results (batch 4)

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

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "dimethylformamide",
  "limit": 10
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_11422 | N,N-Dimethylformamide (DMF) | *** | Ligands not selected | 0 | *** | *** |

---

### Step 4: `search_ligands`
**Args:**
```json
{
  "name": "acetonitrile",
  "limit": 10
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_9825 | Cyanomethane (Acetonitrile) | L | miscellaneous hydrocarbo… | 7 | `CC#N` | *** |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| nitrile | 1 | 100% |

---

### Step 5: `search_ligands`
**Args:**
```json
{
  "name": "tetrahydrofuran",
  "limit": 10
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
  "name": "ethylene glycol",
  "limit": 10
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_9621 | Ethane-1,2-diol (Ethylene glycol) | *** | miscellaneous alcohols a… | 22 | *** | *** |

---

### Step 7: `search_stability`
**Args:**
```json
{
  "where": "c.ligand_id = ligand_9825 AND (c.metal_id = metal_61 OR c.metal_id = metal_62)",
  "limit": 20
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "c.ligand_id = ligand_9621 AND (c.metal_id = metal_61 OR c.metal_id = metal_62)",
  "limit": 20
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 9: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_61",
  "ligand_id": "ligand_9825"
}
```

[summary]
[CATALOG]
## build_system_catalog

*(no pairs found)*

**summary:** {'n_metals': 0, 'n_ligands': 0, 'n_pairs': 0, 'total_species': 0}

---

### Step 10: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_62",
  "ligand_id": "ligand_9825"
}
```

[summary]
[CATALOG]
## build_system_catalog

*(no pairs found)*

**summary:** {'n_metals': 0, 'n_ligands': 0, 'n_pairs': 0, 'total_species': 0}

---

### Step 11: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_62",
  "ligand_id": "ligand_9621"
}
```

[summary]
[CATALOG]
## build_system_catalog

*(no pairs found)*

**summary:** {'n_metals': 0, 'n_ligands': 0, 'n_pairs': 0, 'total_species': 0}

---

### Step 12: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_61",
  "ligand_id": "ligand_9621"
}
```

[summary]
[CATALOG]
## build_system_catalog

*(no pairs found)*

**summary:** {'n_metals': 0, 'n_ligands': 0, 'n_pairs': 0, 'total_species': 0}

---

### Step 13: `build_system_catalog`
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

### Step 14: `build_system_catalog`
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
