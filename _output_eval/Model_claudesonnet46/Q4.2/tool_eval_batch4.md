# Q4.2 — Tool Results (batch 4)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "mercury",
  "limit": 5
}
```

[summary]
## search_metals — 5 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_20 | BuHg^[+] | B | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_53 | EtHg^[+] | EHg | 1 |  | *** | *** | beta_totN_4 | ligand_totN_3 | vlm_totN_6 |
| metal_71 | Hg^[2+] | Hg | 2 | ✓ | [Hg+2] | InChI=1S/Hg/q+2 | beta_totN_68 | ligand_totN_310 | vlm_totN_1097 |
| metal_72 | Hg^[+] | Hg | 1 | ✓ | [Hg+] | InChI=1S/Hg/q+1 | beta_totN_12 | ligand_totN_31 | vlm_totN_83 |
| metal_93 | MeHg^[+] | MHg | 1 |  | *** | *** | beta_totN_18 | ligand_totN_79 | vlm_totN_148 |

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "thiourea",
  "limit": 3
}
```

[summary]
## search_ligands — 3 result(s)

**stats:** 22 SQL matches · showing 3 · limit 3

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_7007 | 1-(2-Aminoethyl)-1,3-diazolidine-2-thione (N-(2-A… | L | Aliphatic amines | 3 | `NCCN1CCNC1=S` | *** |
| ligand_10004 | Thiocarbamide (Thiourea) | L | miscellaneous ureas, had… | 175 | `NC(N)=S` | (-inf, HL, -1.18, L, +inf) |
| ligand_10005 | N-Methylthiourea | L | miscellaneous ureas, had… | 33 | `CNC(N)=S` | *** |

### Functional groups across all SQL matches (16 parseable SMILES)

| group | count | % |
|-------|-------|---|
| secondary_amine | 14 | 88% |
| primary_amine | 8 | 50% |
| tertiary_amine | 3 | 19% |
| aromatic_ring | 2 | 12% |
| amide | 1 | 6% |

---

### Step 4: `search_ligands`
**Args:**
```json
{
  "name": "cysteine",
  "limit": 3
}
```

[summary]
## search_ligands — 3 result(s)

**stats:** 26 SQL matches · showing 3 · limit 3

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5856 | L-2-Amino-3-mercaptopropanoic acid (Cysteine) | H2L | Amino Acids | 134 | `N[C@@H](CS)C(=O)O` | (-inf, H3L, -1.9, H2L, 8.18, HL, 10.3, L, +inf) |
| ligand_5859 | DL-2-Amino-4-mercaptobutanoic acid (Homocysteine) | H2L | Amino Acids | 3 | `NC(CCS)C(=O)O` | (-inf, H3L, 2.15, H2L, 8.57, HL, 10.38, L, +inf) |
| ligand_5861 | L-2-Amino-3-(methylthio)propan… (S-Methylcysteine) | HL | Amino Acids | 39 | `CSC[C@H](N)C(=O)O` | (-inf, H2L, 2, HL, 8.74, L, +inf) |

### Functional groups across all SQL matches (22 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 19 | 86% |
| primary_amine | 19 | 86% |
| thiol | 12 | 55% |
| amide | 11 | 50% |
| thioether | 10 | 45% |
| ester | 4 | 18% |
| aromatic_ring | 1 | 5% |
| nitrile | 1 | 5% |
| secondary_amine | 1 | 5% |

---

### Step 5: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_71"
}
```

[summary]
[CATALOG]
## build_system_catalog — 20 pair(s), 92 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_194 | [M] + [HL]^2 <=> [M(HL)2] |  |
| beta_def_204 | [MHL2] + [H] <=> [M(HL)2] |  |
| beta_def_288 | [H]^2 + [ML(s,black)] <=> [M] + [H2L] | solid |
| beta_def_292 | [H]^2 + [ML(s,red)] <=> [M] + [H2L] | solid |
| beta_def_334 | [ML2(s)] <=> [M] + [L]^2 | solid |
| beta_def_348 | [MO(s,red)] + [H2O] <=> [M] + [OH]^2 | solid |
| beta_def_438 | [M2(OH)5L] + [H]^2 <=> [M2(OH)3L] + [H2O]^2 |  |
| beta_def_502 | [M]^2 + [L] <=> [M2L] |  |
| beta_def_540 | [M]^2 + [L]^3 <=> [M2L3] |  |
| beta_def_571 | [M]^2 + [L] + [H2O] <=> [M2(OH)L] + [H] |  |
| beta_def_575 | [M2(OH)3L] + [H]^2 <=> [M2(OH)L] + [H2O]^2 |  |
| beta_def_620 | [H]^4 + [M3O2L(s)] <=> [M]^3 + [L] + [H2O]^2 | solid |
| beta_def_645 | [M]^3 + [L]^3 <=> [M3L3] |  |
| beta_def_713 | [MCl2] + [L] <=> [MClL] + [Cl] |  |
| beta_def_739 | [MHL] + [H] <=> [MH2L] |  |
| beta_def_751 | [MH2L] + [H] <=> [MH3L] |  |
| beta_def_779 | [M] + [HL] <=> [MHL] |  |
| beta_def_788 | [ML] + [H] <=> [MHL] |  |
| beta_def_792 | [ML2] + [H] <=> [MHL2] |  |
| beta_def_812 | [M] + [L] <=> [ML] |  |
| beta_def_840 | [M] + [L]^2 <=> [ML2] |  |
| beta_def_845 | [MCl2] + [L]^2 <=> [ML2] + [Cl]^2 |  |
| beta_def_872 | [M] + [L]^3 <=> [ML3] |  |
| beta_def_894 | [M] + [L]^4 <=> [ML4] |  |
| beta_def_966 | [M(OH)L] + [H] <=> [ML] + [H2O] |  |
| beta_def_978 | [M] + [L] + [OH] <=> [M(OH)L] |  |

*(all species aqueous unless noted)*

**1. Hg^[2+] + Chloride ion** (metal_71 + ligand_10163) — ligand_def_HxL: *** | 38 ent, 5 sp, 38 vlms (vlm_177572…vlm_177609)
   - species: beta_def_812(8) beta_def_840(8) beta_def_872(9) beta_def_894(9) beta_def_966(4)
   - eq:5 nets T:19~30°C I:-0.05~3.15M max 5n/7e
**2. Hg^[2+] + Hydrogen cyanide (Hydrocyanic acid)** (metal_71 + ligand_10090) — ligand_def_HxL: HL | 37 ent, 5 sp, 37 vlms (vlm_172054…vlm_172090)
   - species: beta_def_812(8) beta_def_840(10) beta_def_872(9) beta_def_894(9) beta_def_978(1)
   - eq:6 nets T:5~45°C I:-0.15~2.15M max 4n/6e
**3. Hg^[2+] + Hydroxide ion** (metal_71 + ligand_10076) — ligand_def_HxL: *** | 29 ent, 6 sp, 29 vlms (vlm_170985…vlm_171013)
   - species: beta_def_348(4) beta_def_502(4) beta_def_645(2) beta_def_812(8) beta_def_840(10) beta_def_872(1)
   - eq:6 nets T:19~30°C I:-0.15~3.15M max 6n/15e
**4. Hg^[2+] + Bromide ion** (metal_71 + ligand_10168) — ligand_def_HxL: *** | 28 ent, 5 sp, 28 vlms (vlm_178151…vlm_178178)
   - species: beta_def_812(8) beta_def_840(6) beta_def_872(6) beta_def_894(6) beta_def_966(2)
   - eq:2 nets T:16.5~31.5°C I:0.275~3.225M max 5n/7e
**5. Hg^[2+] + Thiocarbamide (Thiourea)** (metal_71 + ligand_10004) — ligand_def_HxL: L | 27 ent, 5 sp, 27 vlms (vlm_169530…vlm_169556)
   - species: beta_def_540(3) beta_def_812(3) beta_def_840(7) beta_def_872(7) beta_def_894(7)
   - eq:3 nets T:19~30°C I:-0.05~1.15M max 5n/10e
**6. Hg^[2+] + Hydrogen thiocyanate (Thiocyanic acid)** (metal_71 + ligand_10092) — ligand_def_HxL: HL | 20 ent, 6 sp, 20 vlms (vlm_172456…vlm_172475)
   - species: beta_def_334(1) beta_def_812(6) beta_def_840(4) beta_def_872(3) beta_def_894(3) beta_def_966(3)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 6n/11e
**7. Hg^[2+] + Iodide ion** (metal_71 + ligand_10171) — ligand_def_HxL: *** | 16 ent, 6 sp, 16 vlms (vlm_178529…vlm_178544)
   - species: beta_def_334(3) beta_def_812(4) beta_def_840(3) beta_def_872(1) beta_def_894(4) beta_def_966(1)
   - eq:1 nets T:16.5~31.5°C I:0.275~0.725M max 6n/11e
**8. Hg^[2+] + Ethylenediamine** (metal_71 + ligand_7029) — ligand_def_HxL: L | 13 ent, 3 sp, 13 vlms (vlm_122573…vlm_122585)
   - species: beta_def_792(3) beta_def_812(5) beta_def_840(5)
   - eq:3 nets T:19~30°C I:-0.05~3.15M max 3n/2e
**9. Hg^[2+] + Ammonia** (metal_71 + ligand_10103) — ligand_def_HxL: L | 12 ent, 4 sp, 12 vlms (vlm_173464…vlm_173475)
   - species: beta_def_812(1) beta_def_840(4) beta_def_872(3) beta_def_894(4)
   - eq:3 nets T:19~30°C I:-0.05~2.15M max 4n/6e
**10. Hg^[2+] + 2,2'-Thiodiethanol (beta-Thiodiglycol)** (metal_71 + ligand_9697) — ligand_def_HxL: *** | 12 ent, 4 sp, 12 vlms (vlm_167724…vlm_167735)
   - species: beta_def_812(3) beta_def_840(3) beta_def_872(3) beta_def_894(3)
   - eq:1 nets T:16.5~31.5°C I:0.275~0.725M max 4n/6e
**11. Hg^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_71 + ligand_6277) — ligand_def_HxL: H4L | 11 ent, 4 sp, 11 vlms (vlm_108748…vlm_108758)
   - species: beta_def_739(1) beta_def_788(4) beta_def_812(5) beta_def_966(1)
   - eq:3 nets T:19~30°C I:-0.05~1.15M max 3n/3e
**12. Hg^[2+] + Hydrogen azide (Hydrazoic acid)** (metal_71 + ligand_10106) — ligand_def_HxL: HL | 10 ent, 2 sp, 10 vlms (vlm_173697…vlm_173706)
   - species: beta_def_812(5) beta_def_840(5)
   - eq:3 nets T:19~30°C I:-0.15~1.15M max 2n/1e
**13. Hg^[2+] + Hydrogen carbonate (Carbonic acid)** (metal_71 + ligand_10096) — ligand_def_HxL: H2L | 10 ent, 5 sp, 10 vlms (vlm_172918…vlm_172927)
   - species: beta_def_620(3) beta_def_779(2) beta_def_812(2) beta_def_840(1) beta_def_966(2)
   - eq:3 nets T:19~30°C I:-0.05~3.15M max 5n/8e
**14. Hg^[2+] + 1,3-Diazole (Imidazole)** (metal_71 + ligand_7795) — ligand_def_HxL: L | 10 ent, 3 sp, 10 vlms (vlm_134017…vlm_134026)
   - species: beta_def_812(3) beta_def_840(4) beta_def_966(3)
   - eq:2 nets T:19~30°C I:-0.05~3.15M max 3n/2e
**15. Hg^[2+] + Methylamine** (metal_71 + ligand_6797) — ligand_def_HxL: L | 10 ent, 6 sp, 10 vlms (vlm_119991…vlm_120000)
   - species: beta_def_713(3) beta_def_812(1) beta_def_840(1) beta_def_845(3) beta_def_872(1) beta_def_894(1)
   - eq:2 nets T:19~30°C I:-0.05~0.65M max 4n/6e
**16. Hg^[2+] + Thiosemicarbazide** (metal_71 + ligand_10025) — ligand_def_HxL: L | 9 ent, 3 sp, 9 vlms (vlm_169888…vlm_169896)
   - species: beta_def_840(3) beta_def_872(3) beta_def_894(3)
   - eq:2 nets T:19~30°C I:-0.05~0.85M max 2n/1e
**17. Hg^[2+] + Selenocarbamide (Selenourea)** (metal_71 + ligand_10022) — ligand_def_HxL: L | 9 ent, 3 sp, 9 vlms (vlm_169776…vlm_169784)
   - species: beta_def_840(3) beta_def_872(3) beta_def_894(3)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 3n/3e
**18. Hg^[2+] + Hydrogen sulfide (Hydrosulfuric acid)** (metal_71 + ligand_10144) — ligand_def_HxL: H2L | 8 ent, 5 sp, 8 vlms (vlm_175475…vlm_175482)
   - species: beta_def_194(1) beta_def_204(1) beta_def_288(4) beta_def_292(1) beta_def_792(1)
   - eq:2 nets T:15~30°C I:-0.05~1.15M max 4n/5e
**19. Hg^[2+] + rac-3,6-Dioxaoctane-1,2,4,5,7,8-hexacarboxylic acid (TDS)** (metal_71 + ligand_9096) — ligand_def_HxL: H6L | 8 ent, 8 sp, 8 vlms (vlm_158606…vlm_158613)
   - species: beta_def_438(1) beta_def_571(1) beta_def_575(1) beta_def_739(1) beta_def_751(1) beta_def_788(1) beta_def_812(1) beta_def_966(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 8n/24e
**20. Hg^[2+] + Pyridine (Azine)** (metal_71 + ligand_7890) — ligand_def_HxL: L | 8 ent, 4 sp, 8 vlms (vlm_135327…vlm_135334)
   - species: beta_def_812(3) beta_def_840(3) beta_def_872(1) beta_def_894(1)
   - eq:1 nets T:16.5~31.5°C I:0.275~0.725M max 4n/6e

---

### Step 7: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.beta_definition_id = beta_def_812 AND c.ligand_id IN (ligand_10004, ligand_10092, ligand_10144, ligand_9697, ligand_10025))",
  "order_by": "s.constant_value DESC",
  "limit": 30
}
```

[summary]
## search_stability — 12 row(s)

### `Hg^[2+]` + Hydrogen thiocyanate (Thiocyanic acid) — 6 measurement(s)
metal_id: metal_71 | ligand_id: ligand_10092
ligand_HxL_def: HL | ligand_SMILES: N=C=S

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_172460 | *** | beta_def_812 | ΔS | 20.1 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172457 | ref_eq_map_27901 | beta_def_812 | logK | 9.64 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172456 | ref_eq_map_27902 | beta_def_812 | logK | 9.08 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172461 | *** | beta_def_812 | ΔS | 5.4 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172458 | *** | beta_def_812 | ΔH | -49 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172459 | *** | beta_def_812 | ΔH | -50.2 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |

### `Hg^[2+]` + Thiocarbamide (Thiourea) — 3 measurement(s)
metal_id: metal_71 | ligand_id: ligand_10004
ligand_HxL_def: L | ligand_SMILES: NC(N)=S

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_169530 | ref_eq_map_26959 | beta_def_812 | logK | 11.4 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.18, L, +inf) |
| vlm_169532 | *** | beta_def_812 | ΔS | -20.9 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.18, L, +inf) |
| vlm_169531 | *** | beta_def_812 | ΔH | -71.1 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.18, L, +inf) |

### `Hg^[2+]` + 2,2'-Thiodiethanol (beta-Thiodiglycol) — 3 measurement(s)
metal_id: metal_71 | ligand_id: ligand_9697
ligand_HxL_def: *** | ligand_SMILES: ***

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_167726 | *** | beta_def_812 | ΔS | 10 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_167724 | ref_eq_map_26223 | beta_def_812 | logK | 6.4 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_167725 | *** | beta_def_812 | ΔH | -33.5 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] |  |

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.beta_definition_id = beta_def_812 AND c.ligand_id IN (ligand_7029, ligand_10103, ligand_7795, ligand_6797, ligand_7890))",
  "order_by": "s.constant_value DESC",
  "limit": 30
}
```

[summary]
## search_stability — 13 row(s)

### `Hg^[2+]` + Ethylenediamine — 5 measurement(s)
metal_id: metal_71 | ligand_id: ligand_7029
ligand_HxL_def: L | ligand_SMILES: NCCN

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_122573 | ref_eq_map_9615 | beta_def_812 | logK | 14.3 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122574 | ref_eq_map_9616 | beta_def_812 | logK | 14.3 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122576 | *** | beta_def_812 | ΔH | 0 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122575 | ref_eq_map_9617 | beta_def_812 | logK | -16.75 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122577 | *** | beta_def_812 | ΔS | -74.5 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |

### `Hg^[2+]` + 1,3-Diazole (Imidazole) — 3 measurement(s)
metal_id: metal_71 | ligand_id: ligand_7795
ligand_HxL_def: L | ligand_SMILES: c1c[nH]cn1

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_134017 | ref_eq_map_13325 | beta_def_812 | logK | 9.18 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (-14.5, L, 7) |
| vlm_134019 | *** | beta_def_812 | ΔS | 0 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (-14.5, L, 7) |
| vlm_134018 | *** | beta_def_812 | ΔH | -75.3 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (-14.5, L, 7) |

### `Hg^[2+]` + Ammonia — 1 measurement(s)
metal_id: metal_71 | ligand_id: ligand_10103
ligand_HxL_def: L | ligand_SMILES: N

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_173464 | ref_eq_map_28182 | beta_def_812 | logK | 8.8 | 22 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |

### `Hg^[2+]` + Methylamine — 1 measurement(s)
metal_id: metal_71 | ligand_id: ligand_6797
ligand_HxL_def: L | ligand_SMILES: CN

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_119991 | ref_eq_map_8733 | beta_def_812 | logK | 8.66 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (10.65, L, +inf) |

### `Hg^[2+]` + Pyridine (Azine) — 3 measurement(s)
metal_id: metal_71 | ligand_id: ligand_7890
ligand_HxL_def: L | ligand_SMILES: c1ccncc1

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_135327 | ref_eq_map_13747 | beta_def_812 | logK | 5.2 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (5.24, L, +inf) |
| vlm_135329 | *** | beta_def_812 | ΔS | -25.1 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (5.24, L, +inf) |
| vlm_135328 | *** | beta_def_812 | ΔH | -37.7 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (5.24, L, +inf) |

---

### Step 9: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.beta_definition_id = beta_def_812 AND c.ligand_id IN (ligand_10096, ligand_6277))",
  "order_by": "s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability — 7 row(s)

### `Hg^[2+]` + Ethylenedinitrilotetraacetic acid (EDTA) — 5 measurement(s)
metal_id: metal_71 | ligand_id: ligand_6277
ligand_HxL_def: H4L | ligand_SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_108752 | *** | beta_def_812 | ΔS | 146.4 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108748 | ref_eq_map_5060 | beta_def_812 | logK | 21.5 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108749 | ref_eq_map_5062 | beta_def_812 | logK | 20.8 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108750 | ref_eq_map_5061 | beta_def_812 | logK | 20.6 | 20 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108751 | *** | beta_def_812 | ΔH | -79.1 | 20 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |

### `Hg^[2+]` + Hydrogen carbonate (Carbonic acid) — 2 measurement(s)
metal_id: metal_71 | ligand_id: ligand_10096
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_172919 | ref_eq_map_28035 | beta_def_812 | logK | -10.7 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (9.91, L, +inf) |
| vlm_172918 | ref_eq_map_28034 | beta_def_812 | logK | -11 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.91, L, +inf) |

---
