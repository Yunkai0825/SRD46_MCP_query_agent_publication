# Q3.2.4 — Tool Results (batch 2)

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

### Step 3: `search_metals`
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

### Step 4: `build_system_catalog`
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

### Step 6: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND s.constant_type = 'log_beta' AND s.temperature_c >= 20 AND s.temperature_c <= 25 AND (s.reaction_type IS NULL OR (s.reaction_type NOT LIKE '%OH%' AND s.reaction_type NOT LIKE '%hydro%')))",
  "order_by": "s.constant_value DESC",
  "limit": 120,
  "exclude_groups": [
    "hydroxide"
  ]
}
```

[summary]
## search_stability

*(no results)*

---

### Step 7: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_62 AND s.constant_type = 'log_beta' AND s.temperature_c >= 20 AND s.temperature_c <= 25 AND (s.reaction_type IS NULL OR (s.reaction_type NOT LIKE '%OH%' AND s.reaction_type NOT LIKE '%hydro%')))",
  "order_by": "s.constant_value DESC",
  "limit": 120,
  "exclude_groups": [
    "hydroxide"
  ]
}
```

[summary]
## search_stability

*(no results)*

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61)",
  "order_by": "s.constant_value DESC",
  "limit": 80,
  "exclude_groups": [
    "hydroxide"
  ]
}
```

[summary]
## search_stability — 80 row(s)

### ΔS — 31 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_10076 | Hydroxide ion | *** | *** | 4 | 3 | 25 | 0.1~3 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_10106 | Hydrogen azide (Hydrazoic a… | HL | [N-]=[N+]=N | 4 | 4 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 3 | 3 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8873 | Propanedioic acid (Malonic … | H2L | O=C(O)CC(=O)O | 3 | 3 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 3 | 3 | 25 | 0.5 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 2 | 2 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8467 | Propanoic acid (Propionic a… | HL | CCC(=O)O | 2 | 2 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8479 | 3-Methylbutanoic acid (Isov… | HL | CC(C)CC(=O)O | 2 | 2 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8469 | Pentanoic acid (Valeric aci… | HL | CCCCC(=O)O | 2 | 2 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8473 | 2-Methylpropanoic acid (Iso… | HL | CC(C)C(=O)O | 2 | 2 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8464 | Methanoic acid (Formic acid) | HL | O=CO | 2 | 2 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8468 | Butanoic acid (Butyric acid) | HL | CCCC(=O)O | 2 | 2 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_10163 | Chloride ion | *** | *** | 2 | 1 | 25 | 0~1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9300 | 2-Hydroxybenzaldehyde (Sali… | HL | O=Cc1ccccc1O | 1 | 1 | 25 | 3 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9414 | N,N',N''-Tris(2,3-dihydroxy… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9192 | Hydroxybenzene (Phenol) | HL | Oc1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9251 | 3-Cyanophenol | HL | N#Cc1cccc(O)c1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9218 | 3-Chlorophenol | HL | Oc1cccc(Cl)c1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9237 | 3-Nitrophenol | HL | O=[N+]([O-])c1cccc(O)c1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9217 | 2-Chlorophenol | HL | Oc1ccccc1Cl | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9219 | 4-Chlorophenol | HL | Oc1ccc(Cl)cc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9250 | 2-Cyanophenol | HL | N#Cc1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9302 | 4-Hydroxybenzaldehyde | HL | O=Cc1ccc(O)cc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9252 | 4-Cyanophenol | HL | N#Cc1ccc(O)cc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9238 | 4-Nitrophenol | HL | O=[N+]([O-])c1ccc(O)cc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9402 | N,N',N''-Tris(2,3-dihydroxy… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9410 | 1,3,5-Tris(2,3-dihydroxy-5-… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 1 | 1 | 25 | 0 | *** | 0 |

### ΔH — 4 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8467 | Propanoic acid (Propionic a… | HL | CCC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8479 | 3-Methylbutanoic acid (Isov… | HL | CC(C)CC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8464 | Methanoic acid (Formic acid) | HL | O=CO | 1 | 1 | 25 | 1 | *** | 0 |

### logK — 18 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_10076 | Hydroxide ion | *** | *** | 3 | 1 | 25 | 0~3 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_8126 | 8-Hydroxyquinoline (8-Quino… | HL | Oc1cccc2cccnc12 | 3 | 1 | 25 | 0~1 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_9894 | Trimethylenedihydroxamic ac… | H2L | O=C(CCCC(=O)NO)NO | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9906 | Rhodotorulic acid | H2L | CC(=O)N(O)CCCC1NC(=O)C(CCCN(O)C(C)=O)NC1=O | 2 | 2 | 25 | 0.1~1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_7391 | Piperazine-N,N'-diacetohydr… | H2L | O=C(CN1CCN(C(=O)NO)CC1)NO | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9901 | N,N'-Di-2-propylpentamethyl… | H2L | CC(C)N(O)C(=O)CCCCCC(=O)N(O)C(C)C | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9902 | N,N'-Di-2-propylhexamethyle… | H2L | CC(C)N(O)C(=O)CCCCCCC(=O)N(O)C(C)C | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9900 | N,N'-Di-2-propyltetramethyl… | H2L | CC(C)N(O)C(=O)CCCCC(=O)N(O)C(C)C | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9899 | N,N'-Di-2-propyltrimethylen… | H2L | CC(C)N(O)C(=O)CCCC(=O)N(O)C(C)C | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9905 | Trimethylenebis[aminocarbon… | H2L | O=C(NCCCNC(=O)c1cccc(=O)n1O)c1cccc(=O)n1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7422 | 1,4,7-Tris(3-hydroxy-6-meth… | H3L | Cc1ccc(O)c(CN2CCN(Cc3nc(C)ccc3O)CCN(Cc3nc(C)ccc3O)CC2)n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7154 | Iminodiacetohydroxamic acid | H2L | O=C(CNCC(=O)NO)NO | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_10090 | Hydrogen cyanide (Hydrocyan… | HL | C#N | 1 | 1 | 25 | 0 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6037 | N,N'-Bis(2-hydroxybenzyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)Cc1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6371 | 1,4-Bis[2,5,5-tris(carboxym… | H6L | O=C(O)CN(CCN(CC(=O)O)Cc1ccc(CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O)cc1)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6021 | N,N-Bis(2-hydroxyethyl)glyc… | HL | O=C(O)CN(CCO)CCO | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6124 | 6,16-Bis(carboxymethyl)-1,1… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7340 | 1,3,5-Tris(dimethylamino)-1… | L | CN(C)[C@H]1[C@@H](O)[C@@H](N(C)C)[C@@H](O)[C@@H](N(C)C)[C@H]1O | 1 | 1 | 25 | 0.1 | *** | 1 |

---

### Step 9: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_62)",
  "order_by": "s.constant_value DESC",
  "limit": 80,
  "exclude_groups": [
    "hydroxide"
  ]
}
```

[summary]
## search_stability — 80 row(s)

### ΔS — 17 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_62 | Fe^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 2 | 2 | 25 | 3 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6335 | Oxybis(ethylenenitrilo)tetr… | H4L | O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6342 | Ethylenebis(oxyethylenenitr… | H4L | O=C(O)CN(CCOCCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7345 | Nitrilotris(ethyleneamine) … | L | NCCN(CCN)CCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7348 | Ethylenedinitrilotetrakis(e… | L | NCCN(CCN)CCN(CCN)CCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_8205 | Nitrilotris(methylene-2-pyr… | L | c1ccc(CN(Cc2ccccn2)Cc2ccccn2)nc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_5907 | L-2-Amino-3-(3-indolyl)prop… | HL | N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O | 1 | 1 | 25 | 3 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_8174 | Iminobis(methylene-2-pyridi… | L | c1ccc(CNCc2ccccn2)nc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_8209 | Ethylenedinitrilotetrakis(m… | L | c1ccc(CN(CCN(Cc2ccccn2)Cc2ccccn2)Cc2ccccn2)nc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_8204 | 2,6-Di(2-pyridyl)pyridine (… | L | c1ccc(-c2cccc(-c3ccccn3)n2)nc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7212 | 1,4,7-Triazaheptane (Diethy… | L | NCCNCCN | 1 | 1 | 25 | 1 | *** | 0 |

### logK — 53 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_62 | Fe^[2+] | ligand_8156 | 2,2'-Bipyridyl | L | c1ccc(-c2ccccn2)nc1 | 3 | 1 | 25 | 0~1 | *** | 3 |
| metal_62 | Fe^[2+] | ligand_9759 | 2,3-Dimercaptopropanol (BAL) | H2L | OCC(S)CS | 2 | 2 | 30 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6349 | Dithiobis(ethylenenitrilo)t… | H4L | O=C(O)CN(CCSSCCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8204 | 2,6-Di(2-pyridyl)pyridine (… | L | c1ccc(-c2cccc(-c3ccccn3)n2)nc1 | 2 | 1 | 25 | 0.1~0.5 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_8191 | 1,10-Phenanthroline (Dipyri… | L | c1cnc2c(c1)ccc1cccnc12 | 2 | 1 | 25 | 0~0.1 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_8176 | 2-(2-Pyridylmethylenehydraz… | L | C(=N/Nc1ccccn1)\c1ccccn1 | 2 | 1 | 20~25 | 0~0.1 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_6287 | rac-(1,2-Dimethylethylene)d… | H4L | CC(C(C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_6193 | N-(Phosphonomethyl)iminodia… | H4L | O=C(O)CN(CC(=O)O)CP(=O)(O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6335 | Oxybis(ethylenenitrilo)tetr… | H4L | O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_10090 | Hydrogen cyanide (Hydrocyan… | HL | C#N | 1 | 1 | 25 | 0 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8174 | Iminobis(methylene-2-pyridi… | L | c1ccc(CNCc2ccccn2)nc1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8209 | Ethylenedinitrilotetrakis(m… | L | c1ccc(CN(CCN(Cc2ccccn2)Cc2ccccn2)Cc2ccccn2)nc1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8193 | 5-Methyl-1,10-phenanthroline | L | Cc1cc2cccnc2c2ncccc12 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8196 | 5,6-Dimethyl-1,10-phenanthr… | L | Cc1c(C)c2cccnc2c2ncccc12 | 1 | 1 | 25 | 0 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6102 | 1,4,7,10-Tetraazacyclododec… | H4L | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8199 | 5-Chloro-1,10-phenanthroline | L | Clc1cc2cccnc2c2ncccc12 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6104 | 1,4,7,10-Tetraazacyclotride… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8201 | 5-Nitro-1,10-phenanthroline | L | O=[N+]([O-])c1cc2cccnc2c2ncccc12 | 1 | 1 | 25 | 0 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6084 | 1-Oxa-4,7,10-triazacyclodod… | H3L | O=C(O)CN1CCOCCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6366 | Triethylenetetranitrilohexa… | H6L | O=C(O)CN(CCN(CCN(CC(=O)O)CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8360 | Amino(phenyl)methylenedipho… | H4L | NC(c1ccccc1)(P(=O)(O)O)P(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8434 | Pyridine-2,6-diphosphonic a… | H4L | O=P(O)(O)c1cccc(P(=O)(O)O)n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6288 | meso-(1,2-Dimethylethylene)… | H4L | C[C@H]([C@H](C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7673 | 3,7,11,15-Tetraaza-5,13(2)-… | H2L | Cc1cc2c(O)c(c1)CNCc1cccc(n1)CNCc1cc(C)cc(c1O)CNCc1cccc(n1)CNC2 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7661 | 5-(2-Hydroxyphenyl)-1,4,8,1… | HL | Oc1ccccc1C1CCNCCNCCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_9414 | N,N',N''-Tris(2,3-dihydroxy… | *** | *** | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7500 | 1,4,7,10,13-Pentaazacyclohe… | L | C1CNCCNCCNCCNCCNC1 | 1 | 1 | 35 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6082 | 1-Oxa-4,7,10-triazacyclodod… | H2L | O=C(O)CN1CCNCCN(CC(=O)O)CCOCC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6292 | DL-Ethylenedinitrilo-N,N'-d… | H4L | CC(C(=O)O)N(CCN(CC(=O)O)C(C)C(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6770 | Pyridine-2-phosphonic-6-car… | H3L | O=C(O)c1cccc(P(=O)(O)O)n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7863 | 4-(2-Pyridyl)imidazole | L | c1ccc(-c2c[nH]cn2)nc1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6253 | N-(2-Aminoethyl)iminodiacet… | H2L | NCCN(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6371 | 1,4-Bis[2,5,5-tris(carboxym… | H6L | O=C(O)CN(CCN(CC(=O)O)Cc1ccc(CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O)cc1)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8412 | Nitrilotris(methylenephosph… | H6L | O=P(O)(O)CN(CP(=O)(O)O)CP(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6311 | Trimethylenedinitrilotetraa… | H4L | O=C(O)CN(CCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6109 | 1,4,8,11-Tetraazacyclotetra… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6313 | Tetramethylenedinitrilotetr… | H4L | O=C(O)CN(CCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6070 | 1,4,10-Trioxa-7,13-diazacyc… | H2L | O=C(O)CN1CCOCCOCCN(CC(=O)O)CCOCC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_10076 | Hydroxide ion | *** | *** | 1 | 1 | 25 | 0 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8427 | N-(2-Hydroxyethyl)ethylened… | H6L | O=P(O)(O)CN(CCO)CCN(CP(=O)(O)O)CP(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8072 | 4-(2-Pyridyl)-1,3-thiazole | L | c1ccc(-c2cscn2)nc1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7489 | 3,6,9-Triaza-1(2,6)-pyridin… | L | c1cc2nc(c1)CNCCNCCNC2 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6780 | 4-Aminopyridine-2,6-dicarbo… | H2L | Nc1cc(C(=O)O)nc(C(=O)O)c1 | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8172 | 6,6'-Bis(aminomethyl)-2,2'-… | L | NCc1cccc(-c2cccc(CN)n2)n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6056 | N,N'-Bis(2-pyridylmethyl)et… | H2L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccn1)Cc1ccccn1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6762 | Pyridine-2-carboxylic acid … | HL | O=C(O)c1ccccn1 | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8208 | 2,4,6-Tri(2-pyridyl)-1,3,5-… | L | c1ccc(-c2nc(-c3ccccn3)nc(-c3ccccn3)n2)nc1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6751 | 1,2-Phenylenedinitrilotetra… | H4L | O=C(O)CN(CC(=O)O)c1ccccc1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 1 | *** | 1 |

---
