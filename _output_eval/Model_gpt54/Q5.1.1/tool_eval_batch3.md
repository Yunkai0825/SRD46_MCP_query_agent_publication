# Q5.1.1 — Tool Results (batch 3)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "mercury(I), mercury(II)",
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
  "name": "mercury",
  "limit": 20
}
```

[summary]
## search_metals — 8 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_20 | BuHg^[+] | B | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_53 | EtHg^[+] | EHg | 1 |  | *** | *** | beta_totN_4 | ligand_totN_3 | vlm_totN_6 |
| metal_71 | Hg^[2+] | Hg | 2 | ✓ | [Hg+2] | InChI=1S/Hg/q+2 | beta_totN_68 | ligand_totN_310 | vlm_totN_1097 |
| metal_72 | Hg^[+] | Hg | 1 | ✓ | [Hg+] | InChI=1S/Hg/q+1 | beta_totN_12 | ligand_totN_31 | vlm_totN_83 |
| metal_93 | MeHg^[+] | MHg | 1 |  | *** | *** | beta_totN_18 | ligand_totN_79 | vlm_totN_148 |
| metal_136 | PhHg^[+] | PhHg | 1 |  | *** | *** | beta_totN_2 | ligand_totN_8 | vlm_totN_8 |
| metal_145 | PrHg^[+] | Pr | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_176 | O_[3]SPhHg | S | 0 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |

---

### Step 4: `build_system_catalog`
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

### Step 6: `db_count_records`
**Args:**
```json
{
  "table": "ligandmetal_stability_measured",
  "where": "metal_id = '[''metal_71'', ''metal_72'']'"
}
```

[TOOL ERROR] db_count_records: Error executing tool db_count_records: no such column: metal_id

---

### Step 7: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_stability_measured",
  "group_column": "metal_id",
  "where": "metal_id = '[''metal_71'', ''metal_72'']'",
  "limit": 10
}
```

[TOOL ERROR] db_distribution: Error executing tool db_distribution: no such column: metal_id

---

### Step 8: `db_ranked_pairs`
**Args:**
```json
{
  "rank_by": "measurement_count",
  "limit": 15,
  "where": "lc.metal_id = '[''metal_71'', ''metal_72'']'"
}
```

[summary]
**db_ranked_pairs:** Error - Unknown rank_by='measurement_count'. Choose from: ['ligands_per_metal', 'measurements_per_ligand', 'measurements_per_metal', 'metals_per_ligand', 'pka_per_ligand']

---

### Step 9: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71)",
  "order_by": "s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability — 20 row(s)

### ΔS — 15 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_71 | Hg^[2+] | ligand_10076 | Hydroxide ion | *** | *** | 2 | 1 | 25 | 1~3 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6335 | Oxybis(ethylenenitrilo)tetr… | H4L | O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6794 | N-(6-Methyl-2-pyridylmethyl… | H2L | Cc1cccc(CN(CC(=O)O)CC(=O)O)n1 | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6793 | N-(2-Pyridylmethyl)iminodia… | H2L | O=C(O)CN(CC(=O)O)Cc1ccccn1 | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_10147 | Hydrogen sulfite (Sulfurous… | H2L | O=[SH](=O)O | 1 | 1 | 25 | 0.5 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6751 | 1,2-Phenylenedinitrilotetra… | H4L | O=C(O)CN(CC(=O)O)c1ccccc1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6316 | Octamethylenedinitrilotetra… | H4L | O=C(O)CN(CCCCCCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6348 | Thiobis(ethylenenitrilo)tet… | H4L | O=C(O)CN(CCSCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6313 | Tetramethylenedinitrilotetr… | H4L | O=C(O)CN(CCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_9704 | 4,7,13,16-Tetraoxa-1,10-dit… | *** | *** | 1 | 1 | 25 | 0.5 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_7601 | 4,7,13,16,21,24-Hexaoxa-1,1… | L | C1COCCN2CCOCCOCCN(CCO1)CCOCCOCC2 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6311 | Trimethylenedinitrilotetraa… | H4L | O=C(O)CN(CCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |

### ΔH — 1 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_71 | Hg^[2+] | ligand_10171 | Iodide ion | *** | *** | 1 | 1 | 25 | 0.5 | solid | 0 |

---

### Step 10: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_72)",
  "order_by": "s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability — 20 row(s)

### ΔS — 2 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_72 | Hg^[+] | ligand_10106 | Hydrogen azide (Hydrazoic a… | HL | [N-]=[N+]=N | 1 | 1 | 25 | 0 | solid | 0 |
| metal_72 | Hg^[+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |

### ΔH — 2 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_72 | Hg^[+] | ligand_10106 | Hydrogen azide (Hydrazoic a… | HL | [N-]=[N+]=N | 1 | 1 | 25 | 0 | solid | 0 |
| metal_72 | Hg^[+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |

### logK — 8 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_72 | Hg^[+] | ligand_10076 | Hydroxide ion | *** | *** | 4 | 3 | 25 | 0.5~3 | *** | 2 |
| metal_72 | Hg^[+] | ligand_10114 | Hydrogen diphosphate (Pyrop… | H4L | O=P(O)(O)OP(=O)(O)O | 2 | 2 | 27 | 0.7 | *** | 1 |
| metal_72 | Hg^[+] | ligand_10117 | Hydrogen triphosphate (Trip… | H5L | O=P(O)(O)OP(=O)(O)OP(=O)(O)O | 2 | 2 | 27 | 0.7 | *** | 1 |
| metal_72 | Hg^[+] | ligand_8887 | Propane-2,2-dicarboxylic ac… | H2L | CC(C)(C(=O)O)C(=O)O | 2 | 2 | 27 | 0.7 | *** | 1 |
| metal_72 | Hg^[+] | ligand_8907 | Butanedioic acid (Succinic … | H2L | O=C(O)CCC(=O)O | 2 | 2 | 27 | 2.5 | *** | 1 |
| metal_72 | Hg^[+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 2 | 2 | 27 | 2.5 | *** | 1 |
| metal_72 | Hg^[+] | ligand_8467 | Propanoic acid (Propionic a… | HL | CCC(=O)O | 1 | 1 | 25 | 3 | *** | 1 |
| metal_72 | Hg^[+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 1 | 1 | 25 | 3 | *** | 1 |

---

### Step 11: `db_ranked_pairs`
**Args:**
```json
{
  "rank_by": "measurements_per_metal",
  "limit": 20
}
```

[summary]
## db_ranked_pairs - measurements_per_metal

| metal_id | name | count |
|----------|------|-------|
| metal_68 | H^[+] | 20720 |
| metal_41 | Cu^[2+] | 8963 |
| metal_112 | Ni^[2+] | 5325 |
| metal_208 | Zn^[2+] | 4095 |
| metal_33 | Co^[2+] | 2977 |
| metal_2 | Ag^[+] | 2885 |
| metal_26 | Cd^[2+] | 2828 |
| metal_25 | Ca^[2+] | 1761 |
| metal_125 | Pb^[2+] | 1585 |
| metal_61 | Fe^[3+] | 1473 |
| metal_92 | Mg^[2+] | 1422 |
| metal_94 | Mn^[2+] | 1273 |
| metal_71 | Hg^[2+] | 1097 |
| metal_79 | La^[3+] | 931 |
| metal_65 | Gd^[3+] | 897 |
| metal_58 | Eu^[3+] | 870 |
| metal_173 | Sm^[3+] | 844 |
| metal_110 | Nd^[3+] | 794 |
| metal_5 | Al^[3+] | 792 |
| metal_55 | Er^[3+] | 792 |

---

### Step 12: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_71, metal_72))",
  "order_by": "n.node_count DESC",
  "limit": 20
}
```

[summary]
## search_networks — 34 row(s)

> **Reference equilibrium networks (compact)** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### Beta-definition legend
| beta_def | equation |
|----------|----------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |
| beta_def_779 | ``[M] + [HL] <=> [MHL]`` |
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` |
| beta_def_792 | ``[ML2] + [H] <=> [MHL2]`` |
| beta_def_713 | ``[MCl2] + [L] <=> [MClL] + [Cl]`` |
| beta_def_845 | ``[MCl2] + [L]^2 <=> [ML2] + [Cl]^2`` |
| beta_def_194 | ``[M] + [HL]^2 <=> [M(HL)2]`` |

### Metal-ligand pair summary
| metal | metal_id | ligand | ligand_id | HxL | T_range | I_range | net_count | max_nodes | max_net_id | ligand_SMILES |
|-------|----------|--------|-----------|-----|---------|---------|-----------|----------|------------|---------------|
| `Hg^[2+]` | metal_71 | L-2,3-Diaminopropanoic acid | ligand_5883 | HL | 20~30 | -0.05~0.25 | 1 | 5 | ref_eq_net_1201 | NCC(N)C(=O)O |
| `Hg^[2+]` | metal_71 | D-2-Amino-3-mercapto-3-methylbutanoic a… | ligand_5857 | H2L | 20~30 | -0.05~0.25 | 1 | 3 | ref_eq_net_1055 | CC(C)(S)[C@H](N)C(=O)O |
| `Hg^[2+]` | metal_71 | Aminoacetic acid (Glycine) | ligand_5760 | HL | 15~30 | -0.05~0.65 | 2 | 2 | ref_eq_net_126 | NCC(=O)O |
| `Hg^[2+]` | metal_71 | 13,16,21,24-Tetramethyl-4,7-dioxa-1,10,… | ligand_7655 | L | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_189 | CN1CCN(C)CCN2CCOCCOCCN(CC1)CCN(C)CCN(C)CC2 |
| `Hg^[2+]` | metal_71 | L-2-Amino-5-ureidopentanoic acid (Citru… | ligand_5852 | HL | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_983 | NC(=O)NCCC[C@H](N)C(=O)O |
| `Hg^[2+]` | metal_71 | L-2-Amino-3-(methylthio)propanoic acid … | ligand_5861 | HL | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_1082 | CSC[C@H](N)C(=O)O |
| `Hg^[2+]` | metal_71 | L-2-Amino-4-(methylthio)butanoic acid (… | ligand_5863 | HL | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_1119 | CSCC[C@H](N)C(=O)O |
| `Hg^[2+]` | metal_71 | L-2-Amino-4-(ethylthio)butanoic acid (E… | ligand_5864 | HL | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_1131 | CCSCC[C@H](N)C(=O)O |
| `Hg^[2+]` | metal_71 | L-2,5-Diaminopentanoic acid (Ornithine) | ligand_5886 | HL | 16.5~31.5 | 0.775~1.225 | 1 | 2 | ref_eq_net_1236 | NCCC[C@H](N)C(=O)O |
| `Hg^[2+]` | metal_71 | 3-Aminopropanoic acid (beta-Alanine) | ligand_5788 | HL | 16.5~31.5 | 0.275~0.725 | 1 | 1 | ref_eq_net_476 | NCCC(=O)O |
| `Hg^[2+]` | metal_71 | cis-2-Aminocyclopentane-1-carboxylic ac… | ligand_5790 | HL | 16.5~31.5 | 0.275~0.725 | 1 | 1 | ref_eq_net_489 | N[C@H]1CCC[C@H]1C(=O)O |
| `Hg^[2+]` | metal_71 | cis-2-Aminocyclohexane-1-carboxylic acid | ligand_5792 | HL | 16.5~31.5 | 0.275~0.725 | 1 | 1 | ref_eq_net_496 | N[C@H]1CCCC[C@H]1C(=O)O |
| `Hg^[2+]` | metal_71 | trans-2-Aminocyclohexane-1-carboxylic a… | ligand_5793 | HL | 16.5~31.5 | 0.275~0.725 | 1 | 1 | ref_eq_net_501 | N[C@@H]1CCCC[C@H]1C(=O)O |
| `Hg^[2+]` | metal_71 | cis-2-Amino-4-cyclohexene-1-carboxylic … | ligand_5794 | HL | 16.5~31.5 | 0.275~0.725 | 1 | 1 | ref_eq_net_506 | N[C@H]1CC=CC[C@H]1C(=O)O |
| `Hg^[2+]` | metal_71 | trans-2-Amino-4-cyclohexene-1-carboxyli… | ligand_5795 | HL | 16.5~31.5 | 0.275~0.725 | 1 | 1 | ref_eq_net_510 | N[C@@H]1CC=CC[C@H]1C(=O)O |
| `Hg^[2+]` | metal_71 | L-2-Amino-3-mercaptopropanoic acid (Cys… | ligand_5856 | H2L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_1023 | N[C@@H](CS)C(=O)O |
| `Hg^[2+]` | metal_71 | DL-2-Amino-3-(2-mercaptoimidazo-4-yl)pr… | ligand_5860 | H2L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_1069 | NC(Cc1cnc(S)[nH]1)C(=O)O |
| `Hg^[2+]` | metal_71 | L-Methylenedithio-3,3'-bis(2-aminopropa… | ligand_5893 | H2L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_1303 | NC(CSCSCC(N)C(=O)O)C(=O)O |
| `Hg^[2+]` | metal_71 | L-Ethylenedithio-3,3'-bis(2-aminopropan… | ligand_5894 | H2L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_1306 | NC(CSCCSCC(N)C(=O)O)C(=O)O |

### Global max-node network: `Hg^[2+]` + L-2,3-Diaminopropanoic acid
network_id: ref_eq_net_1201 | metal_id: metal_71 | ligand_id: ligand_5883 | ligand_def_HxL: HL | nodes: 5

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` | logK | -15.9 |
| beta_def_792 | ``[ML2] + [H] <=> [MHL2]`` | logK | -6.04 |
| beta_def_779 | ``[M] + [HL] <=> [MHL]`` | logK | 4.78 |
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` | logK | 5.81 |
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 8.37 |

---
