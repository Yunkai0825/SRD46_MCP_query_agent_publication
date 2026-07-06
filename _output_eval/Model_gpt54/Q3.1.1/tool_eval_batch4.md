# Q3.1.1 — Tool Results (batch 4)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Lead(II)",
  "limit": 10
}
```

[summary]
## search_metals — 10 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_16 | Bu_[3]Pb^[+] | B | 1 |  | *** | *** | beta_totN_2 | ligand_totN_1 | vlm_totN_2 |
| metal_46 | Et_[2]Pb^[2+] | E2Pb | 2 |  | *** | *** | beta_totN_2 | ligand_totN_3 | vlm_totN_5 |
| metal_49 | Et_[3]Pb^[+] | E3Pb | 1 |  | *** | *** | beta_totN_2 | ligand_totN_3 | vlm_totN_5 |
| metal_84 | Me_[2]Pb^[2+] | M2Pb | 2 |  | *** | *** | beta_totN_5 | ligand_totN_4 | vlm_totN_9 |
| metal_87 | Me_[3]Pb^[+] | M3Pb | 1 |  | *** | *** | beta_totN_7 | ligand_totN_23 | vlm_totN_33 |
| metal_125 | Pb^[2+] | Pb | 2 | ✓ | [Pb+2] | InChI=1S/Pb/q+2 | beta_totN_80 | ligand_totN_470 | vlm_totN_1585 |
| metal_126 | Pb^[4+] | Pb | 4 | ✓ | [Pb+4] | InChI=1S/Pb/q+4 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_129 | Ph_[2]Pb^[2+] | Ph2Pb | 2 |  | *** | *** | beta_totN_2 | ligand_totN_1 | vlm_totN_2 |
| metal_130 | Ph_[3]Pb^[+] | Ph3Pb | 1 |  | *** | *** | beta_totN_1 | ligand_totN_2 | vlm_totN_2 |
| metal_140 | Pr_[2]Pb^[2+] | Pr | 2 |  | *** | *** | beta_totN_2 | ligand_totN_3 | vlm_totN_5 |

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "EDTA, DTPA, EGTA, CDTA, dimercaptosuccinic acid, DMSA, dimercaprol, BAL, D-penicillamine, citrate",
  "limit": 20
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
  "name": "ethylenediaminetetraacetic acid, diethylenetriaminepentaacetic acid, ethyleneglycol-bis(2-aminoethylether)-N,N,N',N'-tetraacetic acid, trans-1,2-diaminocyclohexane-N,N,N',N'-tetraacetic acid, meso-2,3-dimercaptosuccinic acid, 2,3-dimercaptopropan-1-ol, penicillamine, citric acid",
  "limit": 30
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 5: `db_ranked_pairs`
**Args:**
```json
{
  "rank_by": "measurement_count",
  "limit": 20,
  "where": {
    "metal_id": "metal_125"
  }
}
```

[PHASE ERROR] Tool 'db_ranked_pairs' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 6: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_125"
}
```

[summary]
[CATALOG]
## build_system_catalog — 20 pair(s), 126 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_194 | [M] + [HL]^2 <=> [M(HL)2] |  |
| beta_def_204 | [MHL2] + [H] <=> [M(HL)2] |  |
| beta_def_208 | [M] + [HL]^3 <=> [M(HL)3] |  |
| beta_def_317 | [ML(s,cerussite)] <=> [M] + [L] | solid |
| beta_def_328 | [(M2OL2)0.5(s)] + [H2O]^0.5 <=> [M] + [L] + [OH] | solid |
| beta_def_334 | [ML2(s)] <=> [M] + [L]^2 | solid |
| beta_def_348 | [MO(s,red)] + [H2O] <=> [M] + [OH]^2 | solid |
| beta_def_349 | [MO(s,yellow)] + [H2O] <=> [M] + [OH]^2 | solid |
| beta_def_363 | [H]^8 + [M10(OH)6OL6(s)] <=> [M]^10 + [L]^6 + [H2O]^7 | solid |
| beta_def_433 | [M2(OH)L2] + [OH] <=> [M2(OH)2L2] |  |
| beta_def_473 | [M2HL] + [H] <=> [M2H2L] |  |
| beta_def_483 | [M2H2L] + [H] <=> [M2H3L] |  |
| beta_def_486 | [M2H3L] + [H] <=> [M2H4L] |  |
| beta_def_493 | [M2L] + [H] <=> [M2HL] |  |
| beta_def_502 | [M]^2 + [L] <=> [M2L] |  |
| beta_def_515 | [M2(OH)L] + [H] <=> [M2L] + [H2O] |  |
| beta_def_519 | [M]^2 + [L]^2 <=> [M2L2] |  |
| beta_def_574 | [M2(OH)2L] + [H] <=> [M2(OH)L] + [H2O] |  |
| beta_def_584 | [M2L2] + [OH] <=> [M2(OH)L2] |  |
| beta_def_596 | [M3(OH)3L] + [H] <=> [M3(OH)2L] + [H2O] |  |
| beta_def_616 | [M3(OH)2L2(s)] <=> [M]^3 + [OH]^2 + [L]^2 | solid |
| beta_def_635 | [M3L] + [H] <=> [M3HL] |  |
| beta_def_638 | [M]^3 + [L] <=> [M3L] |  |
| beta_def_640 | [M3(OH)L] + [H] <=> [M3L] + [H2O] |  |
| beta_def_649 | [M]^3 + [L]^4 <=> [M3L4] |  |
| beta_def_656 | [M3(OH)2L] + [H] <=> [M3OHL] + [H2O] |  |
| beta_def_674 | [M]^4 + [L]^4 <=> [M4L4] |  |
| beta_def_706 | [M]^6 + [L]^8 <=> [M6L8] |  |
| beta_def_732 | [M] + [H2L] <=> [MH2L] |  |
| beta_def_739 | [MHL] + [H] <=> [MH2L] |  |
| beta_def_744 | [MHL3] + [H] <=> [MH2L3] |  |
| beta_def_779 | [M] + [HL] <=> [MHL] |  |
| beta_def_788 | [ML] + [H] <=> [MHL] |  |
| beta_def_792 | [ML2] + [H] <=> [MHL2] |  |
| beta_def_797 | [M] + [H] + [L]^2 <=> [MHL2] |  |
| beta_def_803 | [ML3] + [H] <=> [MHL3] |  |
| beta_def_812 | [M] + [L] <=> [ML] |  |
| beta_def_840 | [M] + [L]^2 <=> [ML2] |  |
| beta_def_872 | [M] + [L]^3 <=> [ML3] |  |
| beta_def_894 | [M] + [L]^4 <=> [ML4] |  |
| beta_def_966 | [M(OH)L] + [H] <=> [ML] + [H2O] |  |
| beta_def_978 | [M] + [L] + [OH] <=> [M(OH)L] |  |
| beta_def_984 | [M(OH)L2] + [H] <=> [ML2] + [H2O] |  |

*(all species aqueous unless noted)*

**1. Pb^[2+] + Bromide ion** (metal_125 + ligand_10168) — ligand_def_HxL: *** | 45 ent, 5 sp, 45 vlms (vlm_178198…vlm_178242)
   - species: beta_def_334(8) beta_def_812(11) beta_def_840(10) beta_def_872(9) beta_def_894(7)
   - eq:9 nets T:19~30°C I:-0.15~4.15M max 5n/10e
**2. Pb^[2+] + Hydroxide ion** (metal_125 + ligand_10076) — ligand_def_HxL: *** | 34 ent, 10 sp, 34 vlms (vlm_171068…vlm_171101)
   - species: beta_def_328(1) beta_def_348(1) beta_def_349(1) beta_def_502(2) beta_def_649(5) beta_def_674(7) beta_def_706(5) beta_def_812(5) beta_def_840(3) beta_def_872(4)
   - eq:6 nets T:19~30°C I:-0.15~5.15M max 10n/45e
**3. Pb^[2+] + Chloride ion** (metal_125 + ligand_10163) — ligand_def_HxL: *** | 32 ent, 4 sp, 32 vlms (vlm_177638…vlm_177669)
   - species: beta_def_334(2) beta_def_812(10) beta_def_840(10) beta_def_872(10)
   - eq:8 nets T:19~30°C I:-0.15~4.15M max 4n/6e
**4. Pb^[2+] + Iodide ion** (metal_125 + ligand_10171) — ligand_def_HxL: *** | 28 ent, 5 sp, 28 vlms (vlm_178552…vlm_178579)
   - species: beta_def_334(4) beta_def_812(6) beta_def_840(6) beta_def_872(6) beta_def_894(6)
   - eq:6 nets T:19~30°C I:-0.05~4.15M max 5n/10e
**5. Pb^[2+] + Thiocarbamide (Thiourea)** (metal_125 + ligand_10004) — ligand_def_HxL: L | 28 ent, 4 sp, 28 vlms (vlm_169581…vlm_169608)
   - species: beta_def_812(7) beta_def_840(7) beta_def_872(7) beta_def_894(7)
   - eq:5 nets T:19~30°C I:-0.05~3.15M max 4n/6e
**6. Pb^[2+] + Aminoacetic acid (Glycine)** (metal_125 + ligand_5760) — ligand_def_HxL: HL | 25 ent, 8 sp, 25 vlms (vlm_94001…vlm_94025)
   - species: beta_def_194(2) beta_def_204(1) beta_def_208(1) beta_def_779(5) beta_def_792(1) beta_def_812(8) beta_def_840(4) beta_def_966(3)
   - eq:4 nets T:19~30°C I:-0.05~3.15M max 6n/11e
**7. Pb^[2+] + Nitrate ion** (metal_125 + ligand_10109) — ligand_def_HxL: *** | 23 ent, 4 sp, 23 vlms (vlm_174057…vlm_174079)
   - species: beta_def_812(9) beta_def_840(7) beta_def_872(4) beta_def_894(3)
   - eq:5 nets T:19~30°C I:-0.05~3.15M max 4n/6e
**8. Pb^[2+] + Ethanoic acid (Acetic acid)** (metal_125 + ligand_8465) — ligand_def_HxL: HL | 20 ent, 3 sp, 20 vlms (vlm_144913…vlm_144932)
   - species: beta_def_812(8) beta_def_840(7) beta_def_872(5)
   - eq:6 nets T:19~35°C I:-0.15~3.15M max 3n/3e
**9. Pb^[2+] + Butanedioic acid (Succinic acid)** (metal_125 + ligand_8907) — ligand_def_HxL: H2L | 16 ent, 8 sp, 16 vlms (vlm_153489…vlm_153504)
   - species: beta_def_194(2) beta_def_744(1) beta_def_779(2) beta_def_792(2) beta_def_803(2) beta_def_812(3) beta_def_840(2) beta_def_872(2)
   - eq:3 nets T:19~30°C I:-0.05~3.15M max 8n/15e
**10. Pb^[2+] + L-2-Amino-3-mercaptopropanoic acid (Cysteine)** (metal_125 + ligand_5856) — ligand_def_HxL: H2L | 16 ent, 5 sp, 16 vlms (vlm_97478…vlm_97493)
   - species: beta_def_779(4) beta_def_797(3) beta_def_812(6) beta_def_840(2) beta_def_984(1)
   - eq:4 nets T:19~30°C I:-0.05~3.15M max 5n/8e
**11. Pb^[2+] + L-5-Glutamyl-L-cysteinylglycine (Glutathione)** (metal_125 + ligand_6592) — ligand_def_HxL: H3L | 14 ent, 6 sp, 14 vlms (vlm_116692…vlm_116705)
   - species: beta_def_204(3) beta_def_739(3) beta_def_788(3) beta_def_812(3) beta_def_840(1) beta_def_984(1)
   - eq:1 nets T:16.5~31.5°C I:2.775~3.225M max 6n/9e
**12. Pb^[2+] + Hydrogen carbonate (Carbonic acid)** (metal_125 + ligand_10096) — ligand_def_HxL: H2L | 13 ent, 9 sp, 13 vlms (vlm_172928…vlm_172940)
   - species: beta_def_317(4) beta_def_363(1) beta_def_502(1) beta_def_616(1) beta_def_638(1) beta_def_779(1) beta_def_812(1) beta_def_840(2) beta_def_978(1)
   - eq:6 nets T:19~30°C I:-0.15~3.15M max 5n/10e
**13. Pb^[2+] + N-Ethylthiourea** (metal_125 + ligand_10006) — ligand_def_HxL: L | 13 ent, 4 sp, 13 vlms (vlm_169663…vlm_169675)
   - species: beta_def_812(4) beta_def_840(3) beta_def_872(3) beta_def_894(3)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 4n/6e
**14. Pb^[2+] + D-2-Amino-3-mercapto-3-methylbutanoic acid (Penicillamine)** (metal_125 + ligand_5857) — ligand_def_HxL: H2L | 13 ent, 7 sp, 13 vlms (vlm_97622…vlm_97634)
   - species: beta_def_204(1) beta_def_779(3) beta_def_792(2) beta_def_812(3) beta_def_840(2) beta_def_966(1) beta_def_984(1)
   - eq:3 nets T:19~41°C I:-0.05~3.15M max 6n/8e
**15. Pb^[2+] + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid)** (metal_125 + ligand_9058) — ligand_def_HxL: H3L | 12 ent, 8 sp, 12 vlms (vlm_157788…vlm_157799)
   - species: beta_def_433(1) beta_def_519(1) beta_def_584(1) beta_def_732(2) beta_def_779(2) beta_def_792(1) beta_def_812(2) beta_def_840(2)
   - eq:2 nets T:16.5~31.5°C I:0.775~2.225M max 8n/13e
**16. Pb^[2+] + D-2-Hydroxypropanoic acid (Lactic acid)** (metal_125 + ligand_8641) — ligand_def_HxL: HL | 12 ent, 3 sp, 12 vlms (vlm_147786…vlm_147797)
   - species: beta_def_812(6) beta_def_840(5) beta_def_872(1)
   - eq:4 nets T:19~30°C I:-0.05~3.15M max 3n/3e
**17. Pb^[2+] + 1,4,7,10,13,16,19,22,25,28,31,34-Dodecaazacyclohexatriacontane ([36]aneN12)** (metal_125 + ligand_7541) — ligand_def_HxL: L | 12 ent, 12 sp, 12 vlms (vlm_130878…vlm_130889)
   - species: beta_def_473(1) beta_def_483(1) beta_def_486(1) beta_def_493(1) beta_def_502(1) beta_def_515(1) beta_def_574(1) beta_def_596(1) beta_def_635(1) beta_def_638(1) beta_def_640(1) beta_def_656(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 12n/50e
**18. Pb^[2+] + Hydrogen nitrite (Nitrous acid)** (metal_125 + ligand_10108) — ligand_def_HxL: HL | 11 ent, 3 sp, 11 vlms (vlm_173824…vlm_173834)
   - species: beta_def_812(6) beta_def_840(3) beta_def_872(2)
   - eq:8 nets T:15~35°C I:-0.15~4.15M max 3n/3e
**19. Pb^[2+] + Propanedioic acid (Malonic acid)** (metal_125 + ligand_8873) — ligand_def_HxL: H2L | 11 ent, 7 sp, 11 vlms (vlm_152381…vlm_152391)
   - species: beta_def_194(1) beta_def_779(1) beta_def_792(1) beta_def_803(1) beta_def_812(4) beta_def_840(2) beta_def_872(1)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 7n/13e
**20. Pb^[2+] + 1,4,7,10,13,16,19,22,25,28,31-Undecaazacyclotritriacontane ([33]aneN11)** (metal_125 + ligand_7540) — ligand_def_HxL: L | 11 ent, 11 sp, 11 vlms (vlm_130831…vlm_130841)
   - species: beta_def_473(1) beta_def_483(1) beta_def_486(1) beta_def_493(1) beta_def_502(1) beta_def_515(1) beta_def_574(1) beta_def_635(1) beta_def_638(1) beta_def_640(1) beta_def_656(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 11n/41e

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_125 AND s.constant_type = 'ML' AND s.temperature_c BETWEEN 23 AND 27 AND s.ionic_strength_mol_l >= 0.05 AND s.ionic_strength_mol_l <= 1.0 AND (s.solvent_name IS NULL OR s.solvent_name LIKE '%water%' OR s.solvent_name LIKE '%aqueous%') AND c.ligand_id NOT IN (ligand_10076, ligand_10096, ligand_10163, ligand_10168, ligand_10171, ligand_10109, ligand_10108))",
  "order_by": "s.constant_value DESC",
  "limit": 40
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
  "where": "(c.metal_id = metal_125 AND s.constant_type = 'ML2' AND s.temperature_c BETWEEN 23 AND 27 AND s.ionic_strength_mol_l >= 0.05 AND s.ionic_strength_mol_l <= 1.0 AND (s.solvent_name IS NULL OR s.solvent_name LIKE '%water%' OR s.solvent_name LIKE '%aqueous%') AND c.ligand_id NOT IN (ligand_10076, ligand_10096, ligand_10163, ligand_10168, ligand_10171, ligand_10109, ligand_10108))",
  "order_by": "s.constant_value DESC",
  "limit": 40
}
```

[summary]
## search_stability

*(no results)*

---

### Step 10: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_5857"
}
```

[summary]
## inspect_card — Ligand | ligand_5857

**Name:** D-2-Amino-3-mercapto-3-methylbutanoic acid (Penicillamine)  
**Formula:** C5H11N1O2S1 | **Class:** Amino Acids  
**SMILES:** `CC(C)(S)[C@H](N)C(=O)O`  
**InChI:** `InChI=1S/C5H11NO2S/c1-5(2,9)3(6)4(7)8/h3,9H,6H2,1-2H3,(H,7,8)/t3-/m1/s1`  
**HxL definition:** H2L  

**pKa values:** 3

| source_vlm | pKa | T (°C) | I (M) | From → To | Solvent | Method | Quality |
|------------|-----|--------|-------|-----------|---------|--------|---------|
| vlm_97563 | -1.90 | 25.0 | 0.1 | H2L → H3L | *** | *** | *** |
| vlm_97556 | 7.96 | 25.0 | 0.1 | HL → H2L | *** | *** | *** |
| vlm_97549 | 10.67 | 25.0 | 0.1 | L → HL | *** | *** | *** |

**Partners:** 15 metal(s), 91 measurement(s) total

| metal_id | Metal | # meas |
|----------|-------|--------|
| metal_68 | H^[+] | 21 |
| metal_208 | Zn^[2+] | 18 |
| metal_125 | Pb^[2+] | 13 |
| metal_26 | Cd^[2+] | 8 |
| metal_112 | Ni^[2+] | 5 |
| … | *(showing top 5 of 15)* | |

---

### Step 11: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_9058"
}
```

[summary]
## inspect_card — Ligand | ligand_9058

**Name:** 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid)  
**Formula:** C6H8O7 | **Class:** Carboxylic acids polyacids  
**SMILES:** `O=C(O)CC(O)(CC(=O)O)C(=O)O`  
**InChI:** `InChI=1S/C6H8O7/c7-3(8)1-6(13,5(11)12)2-4(9)10/h13H,1-2H2,(H,7,8)(H,9,10)(H,11,12)`  
**HxL definition:** H3L  

**pKa values:** 3

| source_vlm | pKa | T (°C) | I (M) | From → To | Solvent | Method | Quality |
|------------|-----|--------|-------|-----------|---------|--------|---------|
| vlm_157473 | 2.90 | 25.0 | 0.1 | H2L → H3L | *** | *** | *** |
| vlm_157459 | 4.35 | 25.0 | 0.1 | HL → H2L | *** | *** | *** |
| vlm_157439 | 5.65 | 25.0 | 0.1 | L → HL | *** | *** | *** |

**Partners:** 57 metal(s), 384 measurement(s) total

| metal_id | Metal | # meas |
|----------|-------|--------|
| metal_68 | H^[+] | 48 |
| metal_112 | Ni^[2+] | 25 |
| metal_204 | W^[6+] | 24 |
| metal_26 | Cd^[2+] | 22 |
| metal_208 | Zn^[2+] | 19 |
| … | *(showing top 5 of 57)* | |

---
