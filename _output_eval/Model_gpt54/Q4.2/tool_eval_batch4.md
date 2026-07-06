# Q4.2 — Tool Results (batch 4)

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
  "name": "cysteine, glutathione, thiourea, thiosulfate, sulfide, mercaptoacetate, thioglycolate, diethyldithiocarbamate, ammonia, ethylenediamine, imidazole, pyridine, acetate, oxalate, citrate, phosphate, sulfate, lactate, carbonate",
  "limit": 50
}
```

[summary]
## search_ligands

*(no results)*

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

### Step 6: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.beta_definition_id = beta_def_812 AND c.ligand_id IN (ligand_10004, ligand_10144, ligand_10025, ligand_9697, ligand_7029, ligand_10103, ligand_7795, ligand_7890, ligand_10096, ligand_6277) AND s.temperature_c >= 20 AND s.temperature_c <= 30 AND (s.solvent_name IS NULL OR s.solvent_name LIKE '%water%' OR s.solvent_name LIKE '%aqueous%'))",
  "order_by": "c.ligand_name_SRD ASC, s.temperature_c ASC, s.ionic_strength_mol_l ASC, s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability

*(no results)*

---

### Step 7: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.ligand_id IN (ligand_10004, ligand_7029, ligand_10103, ligand_7795, ligand_7890, ligand_10096, ligand_6277) AND nd.beta_definition_id = beta_def_812)",
  "order_by": "c.ligand_name ASC",
  "limit": 20
}
```

[summary]
## search_networks — 41 row(s)

> **Reference equilibrium networks (compact)** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### Beta-definition legend
| beta_def | equation |
|----------|----------|
| beta_def_966 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` |
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |
| beta_def_894 | ``[M] + [L]^4 <=> [ML4]`` |
| beta_def_872 | ``[M] + [L]^3 <=> [ML3]`` |
| beta_def_792 | ``[ML2] + [H] <=> [MHL2]`` |
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` |
| beta_def_739 | ``[MHL] + [H] <=> [MH2L]`` |
| beta_def_779 | ``[M] + [HL] <=> [MHL]`` |
| beta_def_620 | ``[H]^4 + [M3O2L(s)] <=> [M]^3 + [L] + [H2O]^2`` |
| beta_def_540 | ``[M]^2 + [L]^3 <=> [M2L3]`` |

### Metal-ligand pair summary
| metal | metal_id | ligand | ligand_id | HxL | T_range | I_range | net_count | max_nodes | ligand_SMILES |
|-------|----------|--------|-----------|-----|---------|---------|-----------|----------|---------------|
| `Hg^[2+]` | metal_71 | 1,3-Diazole (Imidazole) | ligand_7795 | L | 19~29 | 2.85~3.15 | 1 | 3 | c1c[nH]cn1 |
| `Hg^[2+]` | metal_71 | Ammonia | ligand_10103 | L | 19~29 | 1.85~2.15 | 1 | 4 | N |
| `Hg^[2+]` | metal_71 | Ethylenediamine | ligand_7029 | L | 19~30 | -0.05~3.15 | 3 | 3 | NCCN |
| `Hg^[2+]` | metal_71 | Ethylenedinitrilotetraacetic acid (EDTA) | ligand_6277 | H4L | 19~30 | -0.05~1.15 | 3 | 3 | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O |
| `Hg^[2+]` | metal_71 | Hydrogen carbonate (Carbonic acid) | ligand_10096 | H2L | 19~29 | 0.35~3.15 | 2 | 5 | O=C(O)O |
| `Hg^[2+]` | metal_71 | Pyridine (Azine) | ligand_7890 | L | 16.5~31.5 | 0.275~0.725 | 1 | 4 | c1ccncc1 |
| `Hg^[2+]` | metal_71 | Thiocarbamide (Thiourea) | ligand_10004 | L | 19~29 | 0.35~0.65 | 1 | 5 | NC(N)=S |

### Max-node network per pair
| metal | metal_id | ligand | ligand_id | max_net_id | max_nodes | max_edge_counts | max_T_range | max_I_range | max_vlm_counts | max_beta_def_ids | max_type | max_values |
|-------|----------|--------|----------|------------|-----------|------------------|-------------|-------------|----------------|------------------|----------|------------|
| `Hg^[2+]` | metal_71 | 1,3-Diazole (Imidazole) | ligand_7795 | ref_eq_net_13370 | 3 | 2 | 19~29 | 2.85~3.15 | 3 | beta_def_966; beta_def_812; beta_def_840 | logK | -1.54~18.19 |
| `Hg^[2+]` | metal_71 | Ammonia | ligand_10103 | ref_eq_net_28292 | 4 | 6 | 19~29 | 1.85~2.15 | 4 | 4 diff beta_def | logK | 8.8~19 |
| `Hg^[2+]` | metal_71 | Ethylenediamine | ligand_7029 | ref_eq_net_9639 | 3 | 2 | 20~30 | -0.05~0.25 | 3 | beta_def_792; beta_def_812; beta_def_840 | logK | 5.8~23.19 |
| `Hg^[2+]` | metal_71 | Ethylenedinitrilotetraacetic acid (EDTA) | ligand_6277 | ref_eq_net_5066 | 3 | 3 | 20~30 | -0.05~0.25 | 3 | beta_def_788; beta_def_966; beta_def_812 | logK | 3.2~21.5 |
| `Hg^[2+]` | metal_71 | Hydrogen carbonate (Carbonic acid) | ligand_10096 | ref_eq_net_28136 | 5 | 8 | 19~29 | 0.35~0.65 | 5 | 5 diff beta_def | logK | -11.8~14.5 |
| `Hg^[2+]` | metal_71 | Pyridine (Azine) | ligand_7890 | ref_eq_net_13792 | 4 | 6 | 16.5~31.5 | 0.275~0.725 | 4 | 4 diff beta_def | logK | 5.2~10.6 |
| `Hg^[2+]` | metal_71 | Thiocarbamide (Thiourea) | ligand_10004 | ref_eq_net_27033 | 5 | 10 | 19~29 | 0.35~0.65 | 5 | 5 diff beta_def | logK | 11.4~36 |

### Global max-node network: `Hg^[2+]` + Hydrogen carbonate (Carbonic acid)
network_id: ref_eq_net_28136 | metal_id: metal_71 | ligand_id: ligand_10096 | ligand_def_HxL: H2L | nodes: 5

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_620 | ``[H]^4 + [M3O2L(s)] <=> [M]^3 + [L] + [H2O]^2`` | logK | -11.8 |
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | -11 |
| beta_def_779 | ``[M] + [HL] <=> [MHL]`` | logK | 5.48 |
| beta_def_966 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` | logK | 6.6 |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` | logK | 14.5 |

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.beta_definition_id = beta_def_812 AND c.ligand_id IN (ligand_10004, ligand_7029, ligand_10103, ligand_7795, ligand_7890, ligand_10096, ligand_6277))",
  "order_by": "c.ligand_name_SRD ASC, s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability — 22 row(s)

### logK — 7 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_71 | Hg^[2+] | ligand_7029 | Ethylenediamine | L | NCCN | 3 | 1 | 25 | 0.1~3 | *** | 3 |
| metal_71 | Hg^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 3 | 1 | 20~25 | 0.1~1 | *** | 3 |
| metal_71 | Hg^[2+] | ligand_10096 | Hydrogen carbonate (Carboni… | H2L | O=C(O)O | 2 | 1 | 25 | 0.5~3 | *** | 2 |
| metal_71 | Hg^[2+] | ligand_7795 | 1,3-Diazole (Imidazole) | L | c1c[nH]cn1 | 1 | 1 | 25 | 3 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 22 | 2 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_7890 | Pyridine (Azine) | L | c1ccncc1 | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_10004 | Thiocarbamide (Thiourea) | L | NC(N)=S | 1 | 1 | 25 | 0.5 | *** | 1 |

### ΔS — 5 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_71 | Hg^[2+] | ligand_7795 | 1,3-Diazole (Imidazole) | L | c1c[nH]cn1 | 1 | 1 | 25 | 3 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_7029 | Ethylenediamine | L | NCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_7890 | Pyridine (Azine) | L | c1ccncc1 | 1 | 1 | 25 | 0.5 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_10004 | Thiocarbamide (Thiourea) | L | NC(N)=S | 1 | 1 | 25 | 0.5 | *** | 0 |

### ΔH — 5 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_71 | Hg^[2+] | ligand_7795 | 1,3-Diazole (Imidazole) | L | c1c[nH]cn1 | 1 | 1 | 25 | 0.5 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_7029 | Ethylenediamine | L | NCCN | 1 | 1 | 25 | 0 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_7890 | Pyridine (Azine) | L | c1ccncc1 | 1 | 1 | 25 | 0.5 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_10004 | Thiocarbamide (Thiourea) | L | NC(N)=S | 1 | 1 | 25 | 0.5 | *** | 0 |

---

### Step 9: `search_citations`
**Args:**
```json
{
  "where": "(rv.vlm_id IN (SELECT s.vlm_id FROM ligandmetal_stability_measured s JOIN ligandmetal_card c ON c.ligandmetal_id = s.ligandmetal_id WHERE c.metal_id = 71 AND c.beta_definition_id = 812 AND c.ligand_id IN (10004,7029,10103,7795,7890,10096,6277)))",
  "order_by": "rv.vlm_id ASC",
  "limit": 50
}
```

[TOOL ERROR] search_citations: Error executing tool search_citations: Sub-SELECT clauses are not allowed in WHERE/ORDER BY.

---
