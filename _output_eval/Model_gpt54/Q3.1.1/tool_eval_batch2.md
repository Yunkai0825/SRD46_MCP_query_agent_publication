# Q3.1.1 — Tool Results (batch 2)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Pb(II)",
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
  "name": "EDTA, DTPA, HEDTA, EGTA, CDTA, DMSA, succimer, DMPS, dimercaprol, BAL, penicillamine, citrate, NTA",
  "limit": 30
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

### Step 6: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_125 AND s.reaction_type = 'water' AND s.solvent_name LIKE '%water%' AND s.constant_type = 'logB' AND c.ligand_id NOT IN (ligand_10076, ligand_10163, ligand_10168, ligand_10171, ligand_10109, ligand_10108, ligand_10096) AND ABS(s.temperature_c - 25) <= 1 AND ABS(s.ionic_strength_mol_l - 0.1) <= 0.05)",
  "order_by": "s.constant_value DESC",
  "limit": 40
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
  "where": "(c.metal_id = metal_125 AND s.reaction_type = 'water' AND s.solvent_name LIKE '%water%' AND s.constant_type = 'logB' AND c.ligand_id NOT IN (ligand_10076, ligand_10163, ligand_10168, ligand_10171, ligand_10109, ligand_10108, ligand_10096) AND ABS(s.temperature_c - 25) <= 1 AND (s.ionic_strength_mol_l IS NULL OR ABS(s.ionic_strength_mol_l) <= 0.05))",
  "order_by": "s.constant_value DESC",
  "limit": 40
}
```

[summary]
## search_stability

*(no results)*

---

### Step 8: `search_ligands`
**Args:**
```json
{
  "name": "ethylenediaminetetraacetic acid, EDTA, diethylenetriaminepentaacetic acid, DTPA, meso-2,3-dimercaptosuccinic acid, DMSA, succimer, 2,3-dimercapto-1-propanesulfonic acid, DMPS, dimercaprol, BAL, penicillamine",
  "limit": 50
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 9: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_125 AND s.constant_type = 'logB')",
  "order_by": "s.constant_value DESC",
  "limit": 100
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
  "where": "(c.metal_id = metal_125)",
  "order_by": "s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability — 100 row(s)

### ΔS — 36 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_125 | Pb^[2+] | ligand_10076 | Hydroxide ion | *** | *** | 3 | 3 | 25 | 3 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 3 | 3 | 25 | 3 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_6751 | 1,2-Phenylenedinitrilotetra… | H4L | O=C(O)CN(CC(=O)O)c1ccccc1N(CC(=O)O)CC(=O)O | 2 | 2 | 25 | 1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_7532 | 3,6,9,12,15-Pentaaza-1(2,9)… | L | c1cc2ccc3ccc4nc3c2nc1CNCCNCCNCCNCCNC4 | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_6335 | Oxybis(ethylenenitrilo)tetr… | H4L | O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_7509 | 3,6,9-Triaza-1(2,9)-1,10-ph… | L | c1cc2ccc3ccc4nc3c2nc1CNCCNCCNC4 | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_5975 | Ethylenediiminodiacetic aci… | H2L | O=C(O)CNCCNCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_8673 | 3-Hydroxypropanoic acid | HL | O=C(O)CCO | 2 | 2 | 25 | 2 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_10114 | Hydrogen diphosphate (Pyrop… | H4L | O=P(O)(O)OP(=O)(O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_6311 | Trimethylenedinitrilotetraa… | H4L | O=C(O)CN(CCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_7522 | 3,6,9,12-Tetraaza-1(2,9)-1,… | L | c1cc2ccc3ccc4nc3c2nc1CNCCNCCNCCNC4 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_6794 | N-(6-Methyl-2-pyridylmethyl… | H2L | Cc1cccc(CN(CC(=O)O)CC(=O)O)n1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_6313 | Tetramethylenedinitrilotetr… | H4L | O=C(O)CN(CCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_6793 | N-(2-Pyridylmethyl)iminodia… | H2L | O=C(O)CN(CC(=O)O)Cc1ccccn1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_6342 | Ethylenebis(oxyethylenenitr… | H4L | O=C(O)CN(CCOCCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_6140 | N-Methyliminodiacetic acid … | H2L | CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_7528 | 3,6,10,13-Tetraaza-1,8(2,6)… | L | c1cc2nc(c1)CNCCNCc1cccc(n1)CNCCNC2 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_6316 | Octamethylenedinitrilotetra… | H4L | O=C(O)CN(CCCCCCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_6348 | Thiobis(ethylenenitrilo)tet… | H4L | O=C(O)CN(CCSCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_10106 | Hydrogen azide (Hydrazoic a… | HL | [N-]=[N+]=N | 1 | 1 | 25 | 0 | solid | 0 |
| metal_125 | Pb^[2+] | ligand_7588 | 7,16-Bis(2-hydroxyethyl)-1,… | L | OCCN1CCOCCOCCN(CCO)CCOCCOCC1 | 1 | 1 | 25 | 0.5 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_7529 | 3,7,11,15-Tetraaza-1,9(2,6)… | L | c1cc2nc(c1)CNCCCNCc1cccc(n1)CNCCCNC2 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_10163 | Chloride ion | *** | *** | 1 | 1 | 25 | 0 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_8206 | Nitrilotris[methylene(6-met… | L | Cc1cccc(CN(Cc2cccc(C)n2)Cc2cccc(C)n2)n1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.5 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_7601 | 4,7,13,16,21,24-Hexaoxa-1,1… | L | C1COCCN2CCOCCOCCN(CCO1)CCOCCOCC2 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_9678 | cis-anti-cis-2,5,8,15,18,21… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_8205 | Nitrilotris(methylene-2-pyr… | L | c1ccc(CN(Cc2ccccn2)Cc2ccccn2)nc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |

### logK — 32 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_125 | Pb^[2+] | ligand_10076 | Hydroxide ion | *** | *** | 11 | 3 | 25 | 0~3 | *** | 5 |
| metal_125 | Pb^[2+] | ligand_9747 | 2-Mercaptoethanol | HL | OCCS | 4 | 2 | 25 | 0.1~0.5 | *** | 2 |
| metal_125 | Pb^[2+] | ligand_9748 | 3-Mercaptopropane-1,2-diol … | HL | OCC(O)CS | 2 | 2 | 25 | 0.5 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_5856 | L-2-Amino-3-mercaptopropano… | H2L | N[C@@H](CS)C(=O)O | 2 | 2 | 25 | 3 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_7541 | 1,4,7,10,13,16,19,22,25,28,… | L | C1CNCCNCCNCCNCCNCCNCCNCCNCCNCCNCCNCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_7540 | 1,4,7,10,13,16,19,22,25,28,… | L | C1CNCCNCCNCCNCCNCCNCCNCCNCCNCCNCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_7509 | 3,6,9-Triaza-1(2,9)-1,10-ph… | L | c1cc2ccc3ccc4nc3c2nc1CNCCNCCNC4 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_6342 | Ethylenebis(oxyethylenenitr… | H4L | O=C(O)CN(CCOCCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_9760 | DL-threo-1,4-Dimercaptobuta… | H2L | OC(CS)C(O)CS | 1 | 1 | 37 | 0.15 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_7008 | L-Cysteine methyl ester | HL | COC(=O)[C@@H](N)CS | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_6102 | 1,4,7,10-Tetraazacyclododec… | H4L | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_9169 | D-myo-Inositol-1,2,6-tris(d… | H6L | O=P(O)(O)O[C@@H]1[C@@H](OP(=O)(O)O)[C@H](O)[C@@H](O)[C@H](O)[C@@H]1OP(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_8775 | DL-(2-Mercaptopropionyl)gly… | H2L | CC(S)C(=O)NCC(=O)O | 1 | 1 | 37 | 0.15 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_7539 | 1,4,7,10,13,16,19,22,25,28-… | L | C1CNCCNCCNCCNCCNCCNCCNCCNCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_6040 | N,N'-Bis(2-mercaptoethyl)et… | H4L | O=C(O)CN(CCS)CCN(CCS)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_9946 | 2-Mercapto-4,5,6-trioxoperh… | H3L | O=C1NC(=S)NC(=O)C1=NO | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_6007 | L,L-Ethylenediimino-2,2'-bi… | H4L | O=C(O)C(CS)NCCNC(CS)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_6087 | 1,7-Dioxa-4,10,13-triazacyc… | H3L | O=C(O)CN1CCOCCN(CC(=O)O)CCN(CC(=O)O)CCOCC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_6287 | rac-(1,2-Dimethylethylene)d… | H4L | CC(C(C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_5994 | N,N'-Bis(2-hydroxyphenyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)c1ccccc1O)c1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_6088 | 1,7,13-Trioxa-4,10,16-triaz… | H3L | O=C(O)CN1CCOCCN(CC(=O)O)CCOCCN(CC(=O)O)CCOCC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_6283 | DL-(2-Methylpropylethylene)… | H4L | CC(C)CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_6282 | DL-(Butylethylene)dinitrilo… | H4L | CCCCC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_6279 | DL-(Ethylethylene)dinitrilo… | H4L | CCC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_6280 | DL-(Propylethylene)dinitril… | H4L | CCCC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_6284 | DL-(Hexylethylene)dinitrilo… | H4L | CCCCCCC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_6281 | DL-(2-Propylethylene)dinitr… | H4L | CC(C)C(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_6104 | 1,4,7,10-Tetraazacyclotride… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_5857 | D-2-Amino-3-mercapto-3-meth… | H2L | CC(C)(S)[C@H](N)C(=O)O | 1 | 1 | 25 | 3 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |

### ΔH — 4 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_125 | Pb^[2+] | ligand_10106 | Hydrogen azide (Hydrazoic a… | HL | [N-]=[N+]=N | 1 | 1 | 25 | 0 | solid | 0 |
| metal_125 | Pb^[2+] | ligand_10080 | Hydrogen molybdate (Molybdi… | H2L | [O]=[Mo](=[O])([OH])[OH] | 1 | 1 | 25 | 0 | solid | 0 |
| metal_125 | Pb^[2+] | ligand_10081 | Hydrogen tungstate (Tungsti… | H2L | [O]=[W](=[O])([OH])[OH] | 1 | 1 | 25 | 0 | solid | 0 |
| metal_125 | Pb^[2+] | ligand_10079 | Hydrogen chromate (Chromic … | H2L | [O]=[Cr](=[O])([OH])[OH] | 1 | 1 | 25 | 0 | solid | 0 |

---

### Step 11: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id = metal_125 AND m.condition_temp_min <= 25 AND m.condition_temp_max >= 25 AND m.condition_ionic_min <= 0.1 AND m.condition_ionic_max >= 0.1 AND nd.constant_type = 'logK')",
  "order_by": "nd.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_networks

*(no results)*

---
