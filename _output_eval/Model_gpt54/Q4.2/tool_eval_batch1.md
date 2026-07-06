# Q4.2 — Tool Results (batch 1)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "mercury(II)",
  "limit": 10
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

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "cysteine, glutathione, thiourea, diethyldithiocarbamate, thiocyanate, thiosulfate, sulfide, mercaptoacetate, ammonia, ethylenediamine, imidazole, pyridine, acetate, oxalate, citrate, phosphate, carbonate",
  "limit": 50
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 4: `search_ligands`
**Args:**
```json
{
  "name": "cysteine, glutathione, thiourea, thiocyanate, thiosulfate, sulfide, ammonia, imidazole, pyridine, acetate, oxalate, citrate, phosphate, carbonate",
  "limit": 100
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

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.beta_definition_id = beta_def_812 AND c.ligand_id IN (ligand_10004, ligand_10092, ligand_9697) AND s.solvent_name = 'water' AND s.temperature_c >= 19 AND s.temperature_c <= 30 AND s.ionic_strength_mol_l >= 0 AND s.ionic_strength_mol_l <= 0.5)",
  "order_by": "c.ligand_name_SRD ASC, ABS(s.temperature_c - 25) ASC, ABS(COALESCE(s.ionic_strength_mol_l,0) - 0.1) ASC",
  "limit": 50
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
  "where": "(c.metal_id = metal_71 AND c.beta_definition_id = beta_def_812 AND c.ligand_id IN (ligand_7029, ligand_10103, ligand_7795, ligand_7890) AND s.solvent_name = 'water' AND s.temperature_c >= 19 AND s.temperature_c <= 30 AND s.ionic_strength_mol_l >= 0 AND s.ionic_strength_mol_l <= 0.5)",
  "order_by": "c.ligand_name_SRD ASC, ABS(s.temperature_c - 25) ASC, ABS(COALESCE(s.ionic_strength_mol_l,0) - 0.1) ASC",
  "limit": 50
}
```

[summary]
## search_stability

*(no results)*

---

### Step 10: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.beta_definition_id = beta_def_812 AND c.ligand_id IN (ligand_10096, ligand_10076, ligand_6277) AND s.solvent_name = 'water' AND s.temperature_c >= 19 AND s.temperature_c <= 30 AND s.ionic_strength_mol_l >= 0 AND s.ionic_strength_mol_l <= 0.5)",
  "order_by": "c.ligand_name_SRD ASC, ABS(s.temperature_c - 25) ASC, ABS(COALESCE(s.ionic_strength_mol_l,0) - 0.1) ASC",
  "limit": 50
}
```

[summary]
## search_stability

*(no results)*

---

### Step 11: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.ligand_id IN (ligand_10004, ligand_10092, ligand_9697, ligand_7029, ligand_10103, ligand_7795, ligand_7890, ligand_10096, ligand_10076, ligand_6277))",
  "order_by": "c.ligand_name_SRD ASC, s.constant_value DESC",
  "limit": 200
}
```

[summary]
## search_stability — 152 row(s)

### logK — 10 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_71 | Hg^[2+] | ligand_10076 | Hydroxide ion | *** | *** | 17 | 6 | 25 | 0~3 | solid | 6 |
| metal_71 | Hg^[2+] | ligand_10004 | Thiocarbamide (Thiourea) | L | NC(N)=S | 11 | 5 | 25 | 0.1~1 | *** | 3 |
| metal_71 | Hg^[2+] | ligand_10096 | Hydrogen carbonate (Carboni… | H2L | O=C(O)O | 10 | 5 | 25 | 0~3 | solid | 3 |
| metal_71 | Hg^[2+] | ligand_7029 | Ethylenediamine | L | NCCN | 9 | 3 | 25 | 0.1~3 | *** | 3 |
| metal_71 | Hg^[2+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 8 | 6 | 25 | 0~1 | solid | 2 |
| metal_71 | Hg^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 7 | 4 | 20~25 | 0.1~1 | *** | 3 |
| metal_71 | Hg^[2+] | ligand_10103 | Ammonia | L | N | 6 | 4 | 22~25 | 0.1~2 | *** | 3 |
| metal_71 | Hg^[2+] | ligand_7795 | 1,3-Diazole (Imidazole) | L | c1c[nH]cn1 | 4 | 3 | 25 | 0.1~3 | *** | 2 |
| metal_71 | Hg^[2+] | ligand_9697 | 2,2'-Thiodiethanol (beta-Th… | *** | *** | 4 | 4 | 25 | 0.5 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_7890 | Pyridine (Azine) | L | c1ccncc1 | 4 | 4 | 25 | 0.5 | *** | 1 |

### ΔS — 9 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_71 | Hg^[2+] | ligand_10004 | Thiocarbamide (Thiourea) | L | NC(N)=S | 8 | 5 | 25 | 0.1~0.5 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 6 | 5 | 25 | 0~1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_10076 | Hydroxide ion | *** | *** | 6 | 4 | 25 | 1~3 | solid | 0 |
| metal_71 | Hg^[2+] | ligand_9697 | 2,2'-Thiodiethanol (beta-Th… | *** | *** | 4 | 4 | 25 | 0.5 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_7795 | 1,3-Diazole (Imidazole) | L | c1c[nH]cn1 | 3 | 3 | 25 | 3 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_10103 | Ammonia | L | N | 3 | 3 | 25 | 2 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_7029 | Ethylenediamine | L | NCCN | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_7890 | Pyridine (Azine) | L | c1ccncc1 | 2 | 2 | 25 | 0.5 | *** | 0 |

### ΔH — 9 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_71 | Hg^[2+] | ligand_10004 | Thiocarbamide (Thiourea) | L | NC(N)=S | 8 | 5 | 25~30 | 0.1~0.5 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 6 | 5 | 25 | 0~1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_10076 | Hydroxide ion | *** | *** | 6 | 4 | 25 | 1~3 | solid | 0 |
| metal_71 | Hg^[2+] | ligand_9697 | 2,2'-Thiodiethanol (beta-Th… | *** | *** | 4 | 4 | 25 | 0.5 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_7795 | 1,3-Diazole (Imidazole) | L | c1c[nH]cn1 | 3 | 3 | 25 | 0.5 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_10103 | Ammonia | L | N | 3 | 3 | 27 | 2 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_7029 | Ethylenediamine | L | NCCN | 2 | 2 | 25 | 0 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 2 | 20~25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_7890 | Pyridine (Azine) | L | c1ccncc1 | 2 | 2 | 25 | 0.5 | *** | 0 |

---

### Step 12: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_10004"
}
```

[summary]
## inspect_card — Ligand | ligand_10004

**Name:** Thiocarbamide (Thiourea)  
**Formula:** C1H4N2S1 | **Class:** miscellaneous ureas, hadrazides, amidines  
**SMILES:** `NC(N)=S`  
**InChI:** `InChI=1S/CH4N2S/c2-1(3)4/h(H4,2,3,4)`  
**HxL definition:** L  

**pKa values:** 1

| source_vlm | pKa | T (°C) | I (M) | From → To | Solvent | Method | Quality |
|------------|-----|--------|-------|-----------|---------|--------|---------|
| vlm_169435 | -1.18 | 25.0 | 0.1 | L → HL | *** | *** | *** |

**Partners:** 13 metal(s), 175 measurement(s) total

| metal_id | Metal | # meas |
|----------|-------|--------|
| metal_2 | Ag^[+] | 33 |
| metal_26 | Cd^[2+] | 32 |
| metal_125 | Pb^[2+] | 28 |
| metal_71 | Hg^[2+] | 27 |
| metal_174 | Sn^[2+] | 24 |
| … | *(showing top 5 of 13)* | |

---

### Step 13: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_7029"
}
```

[summary]
## inspect_card — Ligand | ligand_7029

**Name:** Ethylenediamine  
**Formula:** C2H8N2 | **Class:** Aliphatic amines  
**SMILES:** `NCCN`  
**InChI:** `InChI=1S/C2H8N2/c3-1-2-4/h1-4H2`  
**HxL definition:** L  

**pKa values:** 2

| source_vlm | pKa | T (°C) | I (M) | From → To | Solvent | Method | Quality |
|------------|-----|--------|-------|-----------|---------|--------|---------|
| vlm_122303 | 7.11 | 25.0 | 0.1 | HL → H2L | *** | *** | *** |
| vlm_122282 | 9.92 | 25.0 | 0.1 | L → HL | *** | *** | *** |

**Partners:** 23 metal(s), 310 measurement(s) total

| metal_id | Metal | # meas |
|----------|-------|--------|
| metal_112 | Ni^[2+] | 45 |
| metal_68 | H^[+] | 41 |
| metal_2 | Ag^[+] | 40 |
| metal_208 | Zn^[2+] | 36 |
| metal_41 | Cu^[2+] | 34 |
| … | *(showing top 5 of 23)* | |

---

### Step 14: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_10096"
}
```

[summary]
## inspect_card — Ligand | ligand_10096

**Name:** Hydrogen carbonate (Carbonic acid)  
**Formula:** C1H2O3 | **Class:** Inorganic ligands  
**SMILES:** `O=C(O)O`  
**InChI:** `InChI=1S/CH2O3/c2-1(3)4/h(H2,2,3,4)`  
**HxL definition:** H2L  

**pKa values:** 2

| source_vlm | pKa | T (°C) | I (M) | From → To | Solvent | Method | Quality |
|------------|-----|--------|-------|-----------|---------|--------|---------|
| vlm_172632 | 6.13 | 25.0 | 0.1 | HL → H2L | *** | *** | *** |
| vlm_172612 | 9.91 | 25.0 | 0.1 | L → HL | *** | *** | *** |

**Partners:** 39 metal(s), 335 measurement(s) total

| metal_id | Metal | # meas |
|----------|-------|--------|
| metal_68 | H^[+] | 48 |
| metal_195 | UO_[2]^[2+] | 33 |
| metal_25 | Ca^[2+] | 21 |
| metal_41 | Cu^[2+] | 20 |
| metal_92 | Mg^[2+] | 16 |
| … | *(showing top 5 of 39)* | |

---

### Step 15: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.ligand_id = ligand_10004)",
  "order_by": "s.constant_type ASC, s.constant_value DESC",
  "limit": 50
}
```

[summary]
## search_stability — 27 row(s)

### `Hg^[2+]` + Thiocarbamide (Thiourea) — 27 measurement(s)
metal_id: metal_71 | ligand_id: ligand_10004
ligand_HxL_def: L | ligand_SMILES: NC(N)=S

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_169543 | *** | beta_def_872 | ΔH | 0 | 30 | 0.1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (-1.18, L, +inf) |
| vlm_169544 | *** | beta_def_872 | ΔH | 0 | 25 | 0.5 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (-1.18, L, +inf) |
| vlm_169531 | *** | beta_def_812 | ΔH | -71.1 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.18, L, +inf) |
| vlm_169536 | *** | beta_def_840 | ΔH | -138.1 | 30 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (-1.18, L, +inf) |
| vlm_169537 | *** | beta_def_840 | ΔH | -142.3 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (-1.18, L, +inf) |
| vlm_169550 | *** | beta_def_894 | ΔH | -192.5 | 30 | 0.1 | `[M] + [L]^4 <=> [ML4]` | *** | [L] | (-1.18, L, +inf) |
| vlm_169551 | *** | beta_def_894 | ΔH | -200.8 | 25 | 0.5 | `[M] + [L]^4 <=> [ML4]` | *** | [L] | (-1.18, L, +inf) |
| vlm_169555 | *** | beta_def_540 | ΔH | -209.2 | 25 | 0.5 | `[M]^2 + [L]^3 <=> [M2L3]` | *** | [L] | (-1.18, L, +inf) |
| vlm_169554 | ref_eq_map_26959 | beta_def_540 | logK | 36 | 25 | 0.5 | `[M]^2 + [L]^3 <=> [M2L3]` | *** | [L] | (-1.18, L, +inf) |
| vlm_169548 | ref_eq_map_26959 | beta_def_894 | logK | 27.1 | 25 | 0.5 | `[M] + [L]^4 <=> [ML4]` | *** | [L] | (-1.18, L, +inf) |
| vlm_169547 | ref_eq_map_26958 | beta_def_894 | logK | 26.6 | 25 | 0.1 | `[M] + [L]^4 <=> [ML4]` | *** | [L] | (-1.18, L, +inf) |
| vlm_169541 | ref_eq_map_26959 | beta_def_872 | logK | 25.1 | 25 | 0.5 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (-1.18, L, +inf) |
| vlm_169540 | ref_eq_map_26958 | beta_def_872 | logK | 24.6 | 25 | 0.1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (-1.18, L, +inf) |
| vlm_169534 | ref_eq_map_26959 | beta_def_840 | logK | 22.1 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (-1.18, L, +inf) |
| vlm_169533 | ref_eq_map_26958 | beta_def_840 | logK | 21.7 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (-1.18, L, +inf) |
| vlm_169530 | ref_eq_map_26959 | beta_def_812 | logK | 11.4 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.18, L, +inf) |
| vlm_169535 | ref_eq_map_26960 | beta_def_840 | logK | -22.1 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (-1.18, L, +inf) |
| vlm_169542 | ref_eq_map_26960 | beta_def_872 | logK | -24.7 | 25 | 1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (-1.18, L, +inf) |
| vlm_169549 | ref_eq_map_26960 | beta_def_894 | logK | -26.5 | 25 | 1 | `[M] + [L]^4 <=> [ML4]` | *** | [L] | (-1.18, L, +inf) |
| vlm_169545 | *** | beta_def_872 | ΔS | 0 | 25 | 0.1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (-1.18, L, +inf) |
| vlm_169546 | *** | beta_def_872 | ΔS | 0 | 25 | 0.5 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (-1.18, L, +inf) |
| vlm_169556 | *** | beta_def_540 | ΔS | -12.6 | 25 | 0.5 | `[M]^2 + [L]^3 <=> [M2L3]` | *** | [L] | (-1.18, L, +inf) |
| vlm_169532 | *** | beta_def_812 | ΔS | -20.9 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.18, L, +inf) |
| vlm_169538 | *** | beta_def_840 | ΔS | -46 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (-1.18, L, +inf) |
| vlm_169539 | *** | beta_def_840 | ΔS | -54.4 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (-1.18, L, +inf) |
| vlm_169552 | *** | beta_def_894 | ΔS | -142.3 | 25 | 0.1 | `[M] + [L]^4 <=> [ML4]` | *** | [L] | (-1.18, L, +inf) |
| vlm_169553 | *** | beta_def_894 | ΔS | -154.8 | 25 | 0.5 | `[M] + [L]^4 <=> [ML4]` | *** | [L] | (-1.18, L, +inf) |

---

### Step 16: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.ligand_id = ligand_7029)",
  "order_by": "s.constant_type ASC, s.constant_value DESC",
  "limit": 50
}
```

[summary]
## search_stability — 13 row(s)

### `Hg^[2+]` + Ethylenediamine — 13 measurement(s)
metal_id: metal_71 | ligand_id: ligand_7029
ligand_HxL_def: L | ligand_SMILES: NCCN

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_122576 | *** | beta_def_812 | ΔH | 0 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122581 | *** | beta_def_840 | ΔH | 0 | 25 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122579 | ref_eq_map_9616 | beta_def_840 | logK | 23.44 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122578 | ref_eq_map_9615 | beta_def_840 | logK | 23.19 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122573 | ref_eq_map_9615 | beta_def_812 | logK | 14.3 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122574 | ref_eq_map_9616 | beta_def_812 | logK | 14.3 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122583 | ref_eq_map_9615 | beta_def_792 | logK | 5.8 | 25 | 0.1 | `[ML2] + [H] <=> [MHL2]` | *** |  |  |
| vlm_122584 | ref_eq_map_9616 | beta_def_792 | logK | 5.65 | 25 | 1 | `[ML2] + [H] <=> [MHL2]` | *** |  |  |
| vlm_122585 | ref_eq_map_9617 | beta_def_792 | logK | 5.59 | 25 | 3 | `[ML2] + [H] <=> [MHL2]` | *** |  |  |
| vlm_122575 | ref_eq_map_9617 | beta_def_812 | logK | -16.75 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122580 | ref_eq_map_9617 | beta_def_840 | logK | -25.97 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122582 | *** | beta_def_840 | ΔS | -17.2 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122577 | *** | beta_def_812 | ΔS | -74.5 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |

---

### Step 17: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.ligand_id = ligand_10096)",
  "order_by": "s.constant_type ASC, s.constant_value DESC",
  "limit": 50
}
```

[summary]
## search_stability — 10 row(s)

### `Hg^[2+]` + Hydrogen carbonate (Carbonic acid) — 10 measurement(s)
metal_id: metal_71 | ligand_id: ligand_10096
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_172920 | ref_eq_map_28034 | beta_def_840 | logK | 14.5 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.91, L, +inf) |
| vlm_172924 | ref_eq_map_28035 | beta_def_966 | logK | 6.7 | 25 | 3 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |
| vlm_172923 | ref_eq_map_28034 | beta_def_966 | logK | 6.6 | 25 | 0.5 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |
| vlm_172922 | ref_eq_map_28035 | beta_def_779 | logK | 5.49 | 25 | 3 | `[M] + [HL] <=> [MHL]` | *** | [HL] | (6.13, HL, 9.91) |
| vlm_172921 | ref_eq_map_28034 | beta_def_779 | logK | 5.48 | 25 | 0.5 | `[M] + [HL] <=> [MHL]` | *** | [HL] | (6.13, HL, 9.91) |
| vlm_172926 | ref_eq_map_28035 | beta_def_620 | logK | -10.4 | 25 | 3 | `[H]^4 + [M3O2L(s)] <=> [M]^3 + [L] + [H2O]^2` | solid | [L] | (9.91, L, +inf) |
| vlm_172919 | ref_eq_map_28035 | beta_def_812 | logK | -10.7 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (9.91, L, +inf) |
| vlm_172918 | ref_eq_map_28034 | beta_def_812 | logK | -11 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.91, L, +inf) |
| vlm_172927 | ref_eq_map_28033 | beta_def_620 | logK | -11.1 | 25 | 0 | `[H]^4 + [M3O2L(s)] <=> [M]^3 + [L] + [H2O]^2` | solid | [L] | (9.91, L, +inf) |
| vlm_172925 | ref_eq_map_28034 | beta_def_620 | logK | -11.8 | 25 | 0.5 | `[H]^4 + [M3O2L(s)] <=> [M]^3 + [L] + [H2O]^2` | solid | [L] | (9.91, L, +inf) |

---
