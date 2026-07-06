# Q3.1.1 — Tool Results (batch 4)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "lead",
  "symbol": "Pb",
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
  "name": "EDTA, ethylenediaminetetraacetic acid, DTPA, diethylenetriaminepentaacetic acid, DMSA, meso-2,3-dimercaptosuccinic acid, DMPS, 2,3-dimercapto-1-propanesulfonic acid, dimercaprol, BAL, penicillamine, EGTA, ethylene glycol-bis(β-aminoethyl ether)-N,N,N',N'-tetraacetic acid, NTA, nitrilotriacetic acid, citrate, citric acid",
  "limit": 200
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 5: `build_system_catalog`
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

### Step 7: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_125 AND c.beta_definition_id IN (beta_def_812, beta_def_840, beta_def_872, beta_def_894) AND (s.solvent_name LIKE '%water%' OR s.solvent_name IS NULL) AND s.temperature_c BETWEEN 20 AND 37 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2))",
  "order_by": "s.constant_value DESC",
  "limit": 200
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
  "where": "(c.metal_id = metal_125 AND (c.ligand_name_SRD LIKE '%ethylenediaminetetraacetic%' OR c.ligand_name_SRD LIKE '%ethylenediaminetetraacetate%' OR c.ligand_name_SRD LIKE '%Ethylenedinitrilotetraacetic%' OR c.ligand_name_SRD LIKE '%edetate%' OR c.ligand_name_SRD LIKE '%EDTA%') AND c.beta_definition_id IN (beta_def_812, beta_def_840, beta_def_872, beta_def_894) AND (s.solvent_name LIKE '%water%' OR s.solvent_name IS NULL) AND s.temperature_c BETWEEN 20 AND 37 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2))",
  "order_by": "s.constant_value DESC",
  "limit": 100
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
  "where": "(c.metal_id = metal_125 AND (c.ligand_name_SRD LIKE '%diethylenetriaminepentaacetic%' OR c.ligand_name_SRD LIKE '%pentetic%' OR c.ligand_name_SRD LIKE '%DTPA%') AND c.beta_definition_id IN (beta_def_812, beta_def_840, beta_def_872, beta_def_894) AND (s.solvent_name LIKE '%water%' OR s.solvent_name IS NULL) AND s.temperature_c BETWEEN 20 AND 37 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2))",
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
  "where": "(c.metal_id = metal_125 AND (c.ligand_name_SRD LIKE '%dimercaptosuccinic%' OR c.ligand_name_SRD LIKE '%2,3-dimercaptosuccinic%' OR c.ligand_name_SRD LIKE '%succimer%' OR c.ligand_name_SRD LIKE '%DMSA%') AND c.beta_definition_id IN (beta_def_812, beta_def_840, beta_def_872, beta_def_894) AND (s.solvent_name LIKE '%water%' OR s.solvent_name IS NULL) AND s.temperature_c BETWEEN 20 AND 37 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2))",
  "order_by": "s.constant_value DESC",
  "limit": 100
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
  "where": "(c.metal_id = metal_125 AND (c.ligand_name_SRD LIKE '%dimercapto-1-propanesulfonic%' OR c.ligand_name_SRD LIKE '%DMPS%') AND c.beta_definition_id IN (beta_def_812, beta_def_840, beta_def_872, beta_def_894) AND (s.solvent_name LIKE '%water%' OR s.solvent_name IS NULL) AND s.temperature_c BETWEEN 20 AND 37 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2))",
  "order_by": "s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability

*(no results)*

---

### Step 12: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_125 AND (c.ligand_name_SRD LIKE '%dimercaprol%' OR c.ligand_name_SRD LIKE '%2,3-dimercapto-1-propanol%' OR c.ligand_name_SRD LIKE '%British anti%Lewisite%' OR c.ligand_name_SRD LIKE '%BAL%') AND c.beta_definition_id IN (beta_def_812, beta_def_840, beta_def_872, beta_def_894) AND (s.solvent_name LIKE '%water%' OR s.solvent_name IS NULL) AND s.temperature_c BETWEEN 20 AND 37 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2))",
  "order_by": "s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability — 100 row(s)

### logK — 33 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_208 | Zn^[2+] | ligand_5856 | L-2-Amino-3-mercaptopropano… | H2L | N[C@@H](CS)C(=O)O | 8 | 2 | 20~37 | 0.1~3 | *** | 4 |
| metal_125 | Pb^[2+] | ligand_5856 | L-2-Amino-3-mercaptopropano… | H2L | N[C@@H](CS)C(=O)O | 6 | 3 | 25 | 0.1~3 | *** | 4 |
| metal_112 | Ni^[2+] | ligand_5856 | L-2-Amino-3-mercaptopropano… | H2L | N[C@@H](CS)C(=O)O | 5 | 3 | 20~37 | 0.1~0.15 | *** | 3 |
| metal_2 | Ag^[+] | ligand_9747 | 2-Mercaptoethanol | HL | OCCS | 5 | 3 | 20~25 | 0.1 | *** | 2 |
| metal_125 | Pb^[2+] | ligand_9747 | 2-Mercaptoethanol | HL | OCCS | 4 | 2 | 25 | 0.1~0.5 | *** | 2 |
| metal_125 | Pb^[2+] | ligand_9748 | 3-Mercaptopropane-1,2-diol … | HL | OCC(O)CS | 4 | 4 | 25 | 0.5 | *** | 1 |
| metal_93 | MeHg^[+] | ligand_5856 | L-2-Amino-3-mercaptopropano… | H2L | N[C@@H](CS)C(=O)O | 4 | 2 | 25 | 0.1~1 | *** | 2 |
| metal_2 | Ag^[+] | ligand_9749 | 2,2-Bis(hydroxymethyl)-3-me… | HL | OCC(CO)(CO)CS | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_9760 | DL-threo-1,4-Dimercaptobuta… | H2L | OC(CS)C(O)CS | 3 | 3 | 37 | 0.15 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_9747 | 2-Mercaptoethanol | HL | OCCS | 3 | 2 | 25 | 0.1~0.5 | *** | 2 |
| metal_208 | Zn^[2+] | ligand_9759 | 2,3-Dimercaptopropanol (BAL) | H2L | OCC(S)CS | 3 | 3 | 30 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_5856 | L-2-Amino-3-mercaptopropano… | H2L | N[C@@H](CS)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_21 | Bi^[3+] | ligand_9747 | 2-Mercaptoethanol | HL | OCCS | 3 | 3 | 25 | 1 | *** | 1 |
| metal_74 | In^[3+] | ligand_5856 | L-2-Amino-3-mercaptopropano… | H2L | N[C@@H](CS)C(=O)O | 3 | 3 | 22 | 0.1 | *** | 1 |
| metal_74 | In^[3+] | ligand_9747 | 2-Mercaptoethanol | HL | OCCS | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_5856 | L-2-Amino-3-mercaptopropano… | H2L | N[C@@H](CS)C(=O)O | 3 | 2 | 25~37 | 0.15~3 | *** | 2 |
| metal_68 | H^[+] | ligand_5856 | L-2-Amino-3-mercaptopropano… | H2L | N[C@@H](CS)C(=O)O | 2 | 1 | 25 | 0~3 | *** | 2 |
| metal_112 | Ni^[2+] | ligand_9759 | 2,3-Dimercaptopropanol (BAL) | H2L | OCC(S)CS | 2 | 2 | 30 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_9759 | 2,3-Dimercaptopropanol (BAL) | H2L | OCC(S)CS | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_93 | MeHg^[+] | ligand_9759 | 2,3-Dimercaptopropanol (BAL) | H2L | OCC(S)CS | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_9759 | 2,3-Dimercaptopropanol (BAL) | H2L | OCC(S)CS | 2 | 2 | 30 | 0.1 | *** | 1 |
| metal_93 | MeHg^[+] | ligand_9747 | 2-Mercaptoethanol | HL | OCCS | 2 | 2 | 20~25 | 0.1 | *** | 1 |
| metal_21 | Bi^[3+] | ligand_5856 | L-2-Amino-3-mercaptopropano… | H2L | N[C@@H](CS)C(=O)O | 2 | 2 | 25 | 0.5 | *** | 1 |
| metal_68 | H^[+] | ligand_9759 | 2,3-Dimercaptopropanol (BAL) | H2L | OCC(S)CS | 2 | 1 | 20~25 | 0.1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_9759 | 2,3-Dimercaptopropanol (BAL) | H2L | OCC(S)CS | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_74 | In^[3+] | ligand_8784 | DL-(2,3-Dimercaptopropionyl… | H3L | O=C(O)CNC(=O)C(S)CS | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_64 | Ga^[3+] | ligand_8784 | DL-(2,3-Dimercaptopropionyl… | H3L | O=C(O)CNC(=O)C(S)CS | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_74 | In^[3+] | ligand_9759 | 2,3-Dimercaptopropanol (BAL) | H2L | OCC(S)CS | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_93 | MeHg^[+] | ligand_9761 | erythro-1,4-Dimercaptobutan… | H2L | OC(CS)C(O)CS | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_74 | In^[3+] | ligand_8783 | DL-(2-Mercaptopropionyl)-L-… | H3L | CC(S)C(=O)N[C@@H](CS)C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_64 | Ga^[3+] | ligand_5856 | L-2-Amino-3-mercaptopropano… | H2L | N[C@@H](CS)C(=O)O | 1 | 1 | 25 | 3 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_5856 | L-2-Amino-3-mercaptopropano… | H2L | N[C@@H](CS)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_8784 | DL-(2,3-Dimercaptopropionyl… | H3L | O=C(O)CNC(=O)C(S)CS | 1 | 1 | 20 | 0.1 | *** | 1 |

### ΔS — 4 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_5856 | L-2-Amino-3-mercaptopropano… | H2L | N[C@@H](CS)C(=O)O | 7 | 3 | 25 | 0.1~3 | *** | 0 |
| metal_68 | H^[+] | ligand_9747 | 2-Mercaptoethanol | HL | OCCS | 2 | 1 | 25 | 0~0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_9760 | DL-threo-1,4-Dimercaptobuta… | H2L | OC(CS)C(O)CS | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_93 | MeHg^[+] | ligand_9747 | 2-Mercaptoethanol | HL | OCCS | 1 | 1 | 25 | 0.1 | *** | 0 |

---

### Step 13: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_125 AND c.ligand_name_SRD LIKE '%penicillamine%' AND c.beta_definition_id IN (beta_def_812, beta_def_840, beta_def_872, beta_def_894) AND (s.solvent_name LIKE '%water%' OR s.solvent_name IS NULL) AND s.temperature_c BETWEEN 20 AND 37 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2))",
  "order_by": "s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability — 100 row(s)

### ΔS — 11 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_5761 | L-2-Aminopropanoic acid (Al… | HL | C[C@H](N)C(=O)O | 6 | 2 | 25 | 0~1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_5761 | L-2-Aminopropanoic acid (Al… | HL | C[C@H](N)C(=O)O | 5 | 3 | 25 | 0.1~1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5761 | L-2-Aminopropanoic acid (Al… | HL | C[C@H](N)C(=O)O | 3 | 2 | 25 | 0.1~0.5 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_5765 | L-2-Amino-3-methylbutanoic … | HL | CC(C)[C@H](N)C(=O)O | 3 | 3 | 25 | 1 | *** | 0 |
| metal_68 | H^[+] | ligand_5765 | L-2-Amino-3-methylbutanoic … | HL | CC(C)[C@H](N)C(=O)O | 3 | 2 | 25 | 0~1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5765 | L-2-Amino-3-methylbutanoic … | HL | CC(C)[C@H](N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5761 | L-2-Aminopropanoic acid (Al… | HL | C[C@H](N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_5801 | Aminopropanedioic acid (Ami… | H2L | NC(C(=O)O)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_8914 | rac-2,2,5,5-Tetramethylhexa… | H2L | CC(C)(C)C(C(=O)O)C(C(=O)O)C(C)(C)C | 1 | 1 | 25 | 0 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_8881 | 2,2-Dimethylpropane-1,1-dic… | H2L | CC(C)(C)C(C(=O)O)C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_33 | Co^[2+] | ligand_5761 | L-2-Aminopropanoic acid (Al… | HL | C[C@H](N)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |

### logK — 27 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_41 | Cu^[2+] | ligand_5761 | L-2-Aminopropanoic acid (Al… | HL | C[C@H](N)C(=O)O | 7 | 1 | 25~37 | 0~5 | *** | 7 |
| metal_68 | H^[+] | ligand_5857 | D-2-Amino-3-mercapto-3-meth… | H2L | CC(C)(S)[C@H](N)C(=O)O | 6 | 1 | 20~37 | 0.1~3 | *** | 6 |
| metal_112 | Ni^[2+] | ligand_5761 | L-2-Aminopropanoic acid (Al… | HL | C[C@H](N)C(=O)O | 5 | 2 | 25~37 | 0~1 | *** | 5 |
| metal_208 | Zn^[2+] | ligand_5857 | D-2-Amino-3-mercapto-3-meth… | H2L | CC(C)(S)[C@H](N)C(=O)O | 5 | 2 | 20~37 | 0.1~3 | *** | 4 |
| metal_26 | Cd^[2+] | ligand_5857 | D-2-Amino-3-mercapto-3-meth… | H2L | CC(C)(S)[C@H](N)C(=O)O | 5 | 3 | 25 | 0.1~3 | *** | 2 |
| metal_125 | Pb^[2+] | ligand_5857 | D-2-Amino-3-mercapto-3-meth… | H2L | CC(C)(S)[C@H](N)C(=O)O | 5 | 2 | 25~37 | 0.1~3 | *** | 3 |
| metal_112 | Ni^[2+] | ligand_5857 | D-2-Amino-3-mercapto-3-meth… | H2L | CC(C)(S)[C@H](N)C(=O)O | 4 | 2 | 20~25 | 0.1 | *** | 2 |
| metal_41 | Cu^[2+] | ligand_5765 | L-2-Amino-3-methylbutanoic … | HL | CC(C)[C@H](N)C(=O)O | 3 | 1 | 25~37 | 0.1~0.5 | *** | 3 |
| metal_208 | Zn^[2+] | ligand_5761 | L-2-Aminopropanoic acid (Al… | HL | C[C@H](N)C(=O)O | 3 | 1 | 25~37 | 0.15~1 | *** | 3 |
| metal_112 | Ni^[2+] | ligand_5765 | L-2-Amino-3-methylbutanoic … | HL | CC(C)[C@H](N)C(=O)O | 3 | 1 | 25 | 0.1~1 | *** | 3 |
| metal_26 | Cd^[2+] | ligand_8773 | N-Acetyl-D-penicillamine | H2L | CC(=O)N[C@@H](C(=O)O)C(C)(C)S | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_5761 | L-2-Aminopropanoic acid (Al… | HL | C[C@H](N)C(=O)O | 2 | 1 | 25 | 3~5 | *** | 2 |
| metal_33 | Co^[2+] | ligand_5857 | D-2-Amino-3-mercapto-3-meth… | H2L | CC(C)(S)[C@H](N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_5891 | D-3,3'-Dithiobis(2-amino-3-… | H2L | CC(C)(SSC(C)(C)C(N)C(=O)O)C(N)C(=O)O | 2 | 1 | 25~37 | 0.1~0.15 | *** | 2 |
| metal_19 | Be^[2+] | ligand_5857 | D-2-Amino-3-mercapto-3-meth… | H2L | CC(C)(S)[C@H](N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_5857 | D-2-Amino-3-mercapto-3-meth… | H2L | CC(C)(S)[C@H](N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_93 | MeHg^[+] | ligand_5857 | D-2-Amino-3-mercapto-3-meth… | H2L | CC(C)(S)[C@H](N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_42 | Cu^[+] | ligand_5857 | D-2-Amino-3-mercapto-3-meth… | H2L | CC(C)(S)[C@H](N)C(=O)O | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_93 | MeHg^[+] | ligand_8773 | N-Acetyl-D-penicillamine | H2L | CC(=O)N[C@@H](C(=O)O)C(C)(C)S | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_5891 | D-3,3'-Dithiobis(2-amino-3-… | H2L | CC(C)(SSC(C)(C)C(N)C(=O)O)C(N)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_74 | In^[3+] | ligand_5857 | D-2-Amino-3-mercapto-3-meth… | H2L | CC(C)(S)[C@H](N)C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5891 | D-3,3'-Dithiobis(2-amino-3-… | H2L | CC(C)(SSC(C)(C)C(N)C(=O)O)C(N)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_8773 | N-Acetyl-D-penicillamine | H2L | CC(=O)N[C@@H](C(=O)O)C(C)(C)S | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_2 | Ag^[+] | ligand_5857 | D-2-Amino-3-mercapto-3-meth… | H2L | CC(C)(S)[C@H](N)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_5891 | D-3,3'-Dithiobis(2-amino-3-… | H2L | CC(C)(SSC(C)(C)C(N)C(=O)O)C(N)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5765 | L-2-Amino-3-methylbutanoic … | HL | CC(C)[C@H](N)C(=O)O | 1 | 1 | 37 | 0.15 | *** | 1 |
| metal_68 | H^[+] | ligand_5858 | DL-2-Amino-3-mercapto-3-met… | H2L | CCC(C)(S)C(N)C(=O)O | 1 | 1 | 30 | 0.1 | *** | 1 |

---

### Step 14: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_125 AND (c.ligand_name_SRD LIKE '%ethylene glycol-bis%' OR c.ligand_name_SRD LIKE '%bis(2-aminoethyl) ether%tetraacetic%' OR c.ligand_name_SRD LIKE '%EGTA%') AND c.beta_definition_id IN (beta_def_812, beta_def_840, beta_def_872, beta_def_894) AND (s.solvent_name LIKE '%water%' OR s.solvent_name IS NULL) AND s.temperature_c BETWEEN 20 AND 37 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2))",
  "order_by": "s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability

*(no results)*

---

### Step 15: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_125 AND (c.ligand_name_SRD LIKE '%nitrilotriacetic%' OR c.ligand_name_SRD LIKE '%NTA%') AND c.beta_definition_id IN (beta_def_812, beta_def_840, beta_def_872, beta_def_894) AND (s.solvent_name LIKE '%water%' OR s.solvent_name IS NULL) AND s.temperature_c BETWEEN 20 AND 37 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2))",
  "order_by": "s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability — 100 row(s)

### ΔS — 9 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_26 | Cd^[2+] | ligand_6794 | N-(6-Methyl-2-pyridylmethyl… | H2L | Cc1cccc(CN(CC(=O)O)CC(=O)O)n1 | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6794 | N-(6-Methyl-2-pyridylmethyl… | H2L | Cc1cccc(CN(CC(=O)O)CC(=O)O)n1 | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_6794 | N-(6-Methyl-2-pyridylmethyl… | H2L | Cc1cccc(CN(CC(=O)O)CC(=O)O)n1 | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6794 | N-(6-Methyl-2-pyridylmethyl… | H2L | Cc1cccc(CN(CC(=O)O)CC(=O)O)n1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_6794 | N-(6-Methyl-2-pyridylmethyl… | H2L | Cc1cccc(CN(CC(=O)O)CC(=O)O)n1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6794 | N-(6-Methyl-2-pyridylmethyl… | H2L | Cc1cccc(CN(CC(=O)O)CC(=O)O)n1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_6794 | N-(6-Methyl-2-pyridylmethyl… | H2L | Cc1cccc(CN(CC(=O)O)CC(=O)O)n1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_6794 | N-(6-Methyl-2-pyridylmethyl… | H2L | Cc1cccc(CN(CC(=O)O)CC(=O)O)n1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_92 | Mg^[2+] | ligand_6794 | N-(6-Methyl-2-pyridylmethyl… | H2L | Cc1cccc(CN(CC(=O)O)CC(=O)O)n1 | 1 | 1 | 25 | 0.1 | *** | 0 |

### logK — 76 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_71 | Hg^[2+] | ligand_6794 | N-(6-Methyl-2-pyridylmethyl… | H2L | Cc1cccc(CN(CC(=O)O)CC(=O)O)n1 | 4 | 2 | 20~25 | 0.1 | *** | 2 |
| metal_26 | Cd^[2+] | ligand_6794 | N-(6-Methyl-2-pyridylmethyl… | H2L | Cc1cccc(CN(CC(=O)O)CC(=O)O)n1 | 2 | 1 | 20~25 | 0.1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_6371 | 1,4-Bis[2,5,5-tris(carboxym… | H6L | O=C(O)CN(CCN(CC(=O)O)Cc1ccc(CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O)cc1)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_81 | Lu^[3+] | ligand_6037 | N,N'-Bis(2-hydroxybenzyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)Cc1ccccc1O | 2 | 1 | 20~25 | 0.1 | *** | 2 |
| metal_65 | Gd^[3+] | ligand_6037 | N,N'-Bis(2-hydroxybenzyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)Cc1ccccc1O | 2 | 1 | 20~25 | 0.1 | *** | 2 |
| metal_41 | Cu^[2+] | ligand_6371 | 1,4-Bis[2,5,5-tris(carboxym… | H6L | O=C(O)CN(CCN(CC(=O)O)Cc1ccc(CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O)cc1)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_6371 | 1,4-Bis[2,5,5-tris(carboxym… | H6L | O=C(O)CN(CCN(CC(=O)O)Cc1ccc(CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O)cc1)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6371 | 1,4-Bis[2,5,5-tris(carboxym… | H6L | O=C(O)CN(CCN(CC(=O)O)Cc1ccc(CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O)cc1)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_6371 | 1,4-Bis[2,5,5-tris(carboxym… | H6L | O=C(O)CN(CCN(CC(=O)O)Cc1ccc(CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O)cc1)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7422 | 1,4,7-Tris(3-hydroxy-6-meth… | H3L | Cc1ccc(O)c(CN2CCN(Cc3nc(C)ccc3O)CCN(Cc3nc(C)ccc3O)CC2)n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_64 | Ga^[3+] | ligand_7422 | 1,4,7-Tris(3-hydroxy-6-meth… | H3L | Cc1ccc(O)c(CN2CCN(Cc3nc(C)ccc3O)CCN(Cc3nc(C)ccc3O)CC2)n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6037 | N,N'-Bis(2-hydroxybenzyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)Cc1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_64 | Ga^[3+] | ligand_6037 | N,N'-Bis(2-hydroxybenzyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)Cc1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_64 | Ga^[3+] | ligand_6038 | N,N'-Bis(2-hydroxy-5-sulfob… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1cc(S(=O)(=O)O)ccc1O)Cc1cc(S(=O)(=O)O)ccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6038 | N,N'-Bis(2-hydroxy-5-sulfob… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1cc(S(=O)(=O)O)ccc1O)Cc1cc(S(=O)(=O)O)ccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6046 | N,N'-Bis(3-hydroxy-6-methyl… | H4L | Cc1ccc(O)c(CN(CCN(CC(=O)O)Cc2nc(C)ccc2O)CC(=O)O)n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6047 | N,N''-Bis(3-hydroxy-6-methy… | H5L | Cc1ccc(O)c(CN(CCN(CCN(CC(=O)O)Cc2nc(C)ccc2O)CC(=O)O)CC(=O)O)n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_64 | Ga^[3+] | ligand_6042 | N,N'-Bis(3-hydroxy-5-hydrox… | H4L | Cc1ncc(CO)c(CN(CCN(CC(=O)O)Cc2c(CO)cnc(C)c2O)CC(=O)O)c1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6276 | N-(2-Hydroxybenzyl)ethylene… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_64 | Ga^[3+] | ligand_6047 | N,N''-Bis(3-hydroxy-6-methy… | H5L | Cc1ccc(O)c(CN(CCN(CCN(CC(=O)O)Cc2nc(C)ccc2O)CC(=O)O)CC(=O)O)n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6042 | N,N'-Bis(3-hydroxy-5-hydrox… | H4L | Cc1ncc(CO)c(CN(CCN(CC(=O)O)Cc2c(CO)cnc(C)c2O)CC(=O)O)c1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_74 | In^[3+] | ligand_6038 | N,N'-Bis(2-hydroxy-5-sulfob… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1cc(S(=O)(=O)O)ccc1O)Cc1cc(S(=O)(=O)O)ccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_64 | Ga^[3+] | ligand_6046 | N,N'-Bis(3-hydroxy-6-methyl… | H4L | Cc1ccc(O)c(CN(CCN(CC(=O)O)Cc2nc(C)ccc2O)CC(=O)O)n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_74 | In^[3+] | ligand_6046 | N,N'-Bis(3-hydroxy-6-methyl… | H4L | Cc1ccc(O)c(CN(CCN(CC(=O)O)Cc2nc(C)ccc2O)CC(=O)O)n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_74 | In^[3+] | ligand_7422 | 1,4,7-Tris(3-hydroxy-6-meth… | H3L | Cc1ccc(O)c(CN2CCN(Cc3nc(C)ccc3O)CCN(Cc3nc(C)ccc3O)CC2)n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_74 | In^[3+] | ligand_6037 | N,N'-Bis(2-hydroxybenzyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)Cc1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_74 | In^[3+] | ligand_6276 | N-(2-Hydroxybenzyl)ethylene… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_74 | In^[3+] | ligand_6042 | N,N'-Bis(3-hydroxy-5-hydrox… | H4L | Cc1ncc(CO)c(CN(CCN(CC(=O)O)Cc2c(CO)cnc(C)c2O)CC(=O)O)c1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_74 | In^[3+] | ligand_6047 | N,N''-Bis(3-hydroxy-6-methy… | H5L | Cc1ccc(O)c(CN(CCN(CCN(CC(=O)O)Cc2nc(C)ccc2O)CC(=O)O)CC(=O)O)n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_64 | Ga^[3+] | ligand_6276 | N-(2-Hydroxybenzyl)ethylene… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_65 | Gd^[3+] | ligand_6038 | N,N'-Bis(2-hydroxy-5-sulfob… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1cc(S(=O)(=O)O)ccc1O)Cc1cc(S(=O)(=O)O)ccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_6037 | N,N'-Bis(2-hydroxybenzyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)Cc1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_74 | In^[3+] | ligand_6056 | N,N'-Bis(2-pyridylmethyl)et… | H2L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccn1)Cc1ccccn1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_6042 | N,N'-Bis(3-hydroxy-5-hydrox… | H4L | Cc1ncc(CO)c(CN(CCN(CC(=O)O)Cc2c(CO)cnc(C)c2O)CC(=O)O)c1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_206 | Yb^[3+] | ligand_6037 | N,N'-Bis(2-hydroxybenzyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)Cc1ccccc1O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_6056 | N,N'-Bis(2-pyridylmethyl)et… | H2L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccn1)Cc1ccccn1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_192 | Tm^[3+] | ligand_6037 | N,N'-Bis(2-hydroxybenzyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)Cc1ccccc1O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_55 | Er^[3+] | ligand_6037 | N,N'-Bis(2-hydroxybenzyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)Cc1ccccc1O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_6037 | N,N'-Bis(2-hydroxybenzyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)Cc1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_73 | Ho^[3+] | ligand_6037 | N,N'-Bis(2-hydroxybenzyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)Cc1ccccc1O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_44 | Dy^[3+] | ligand_6037 | N,N'-Bis(2-hydroxybenzyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)Cc1ccccc1O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_64 | Ga^[3+] | ligand_6056 | N,N'-Bis(2-pyridylmethyl)et… | H2L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccn1)Cc1ccccn1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_6276 | N-(2-Hydroxybenzyl)ethylene… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_179 | Tb^[3+] | ligand_6037 | N,N'-Bis(2-hydroxybenzyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)Cc1ccccc1O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_6037 | N,N'-Bis(2-hydroxybenzyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)Cc1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_58 | Eu^[3+] | ligand_6037 | N,N'-Bis(2-hydroxybenzyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)Cc1ccccc1O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_173 | Sm^[3+] | ligand_6037 | N,N'-Bis(2-hydroxybenzyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)Cc1ccccc1O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6037 | N,N'-Bis(2-hydroxybenzyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)Cc1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_6276 | N-(2-Hydroxybenzyl)ethylene… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_110 | Nd^[3+] | ligand_6037 | N,N'-Bis(2-hydroxybenzyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)Cc1ccccc1O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_6037 | N,N'-Bis(2-hydroxybenzyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)Cc1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_139 | Pr^[3+] | ligand_6037 | N,N'-Bis(2-hydroxybenzyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)Cc1ccccc1O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_65 | Gd^[3+] | ligand_6276 | N-(2-Hydroxybenzyl)ethylene… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_6037 | N,N'-Bis(2-hydroxybenzyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)Cc1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_6042 | N,N'-Bis(3-hydroxy-5-hydrox… | H4L | Cc1ncc(CO)c(CN(CCN(CC(=O)O)Cc2c(CO)cnc(C)c2O)CC(=O)O)c1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_27 | Ce^[3+] | ligand_6037 | N,N'-Bis(2-hydroxybenzyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)Cc1ccccc1O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_6272 | N-Benzylethylenedinitrilotr… | H3L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_6276 | N-(2-Hydroxybenzyl)ethylene… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6276 | N-(2-Hydroxybenzyl)ethylene… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6042 | N,N'-Bis(3-hydroxy-5-hydrox… | H4L | Cc1ncc(CO)c(CN(CCN(CC(=O)O)Cc2c(CO)cnc(C)c2O)CC(=O)O)c1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_6056 | N,N'-Bis(2-pyridylmethyl)et… | H2L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccn1)Cc1ccccn1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6037 | N,N'-Bis(2-hydroxybenzyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)Cc1ccccc1O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_2 | Ag^[+] | ligand_6794 | N-(6-Methyl-2-pyridylmethyl… | H2L | Cc1cccc(CN(CC(=O)O)CC(=O)O)n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6056 | N,N'-Bis(2-pyridylmethyl)et… | H2L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccn1)Cc1ccccn1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_94 | Mn^[2+] | ligand_6037 | N,N'-Bis(2-hydroxybenzyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)Cc1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_6056 | N,N'-Bis(2-pyridylmethyl)et… | H2L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccn1)Cc1ccccn1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_6056 | N,N'-Bis(2-pyridylmethyl)et… | H2L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccn1)Cc1ccccn1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_81 | Lu^[3+] | ligand_6272 | N-Benzylethylenedinitrilotr… | H3L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_206 | Yb^[3+] | ligand_6272 | N-Benzylethylenedinitrilotr… | H3L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_192 | Tm^[3+] | ligand_6272 | N-Benzylethylenedinitrilotr… | H3L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6371 | 1,4-Bis[2,5,5-tris(carboxym… | H6L | O=C(O)CN(CCN(CC(=O)O)Cc1ccc(CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O)cc1)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_55 | Er^[3+] | ligand_6272 | N-Benzylethylenedinitrilotr… | H3L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_73 | Ho^[3+] | ligand_6272 | N-Benzylethylenedinitrilotr… | H3L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_44 | Dy^[3+] | ligand_6272 | N-Benzylethylenedinitrilotr… | H3L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_81 | Lu^[3+] | ligand_6794 | N-(6-Methyl-2-pyridylmethyl… | H2L | Cc1cccc(CN(CC(=O)O)CC(=O)O)n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_206 | Yb^[3+] | ligand_6794 | N-(6-Methyl-2-pyridylmethyl… | H2L | Cc1cccc(CN(CC(=O)O)CC(=O)O)n1 | 1 | 1 | 25 | 0.1 | *** | 1 |

### ΔH — 1 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_92 | Mg^[2+] | ligand_6794 | N-(6-Methyl-2-pyridylmethyl… | H2L | Cc1cccc(CN(CC(=O)O)CC(=O)O)n1 | 1 | 1 | 20 | 0.1 | *** | 0 |

---

### Step 16: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_125 AND (c.ligand_name_SRD LIKE '%citric%' OR c.ligand_name_SRD LIKE '%2-Hydroxypropane-1,2,3-tricarboxylic%') AND c.beta_definition_id IN (beta_def_812, beta_def_840, beta_def_872, beta_def_894) AND (s.solvent_name LIKE '%water%' OR s.solvent_name IS NULL) AND s.temperature_c BETWEEN 20 AND 37 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2))",
  "order_by": "s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability — 100 row(s)

### ΔS — 7 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_9072 | Butane-1,2,3,4-tetracarboxy… | H4L | O=C(O)CC(C(=O)O)C(CC(=O)O)C(=O)O | 4 | 4 | 25 | 0 | *** | 0 |
| metal_68 | H^[+] | ligand_8953 | L-Hydroxybutanedioic acid (… | H2L | O=C(O)CC(O)C(=O)O | 4 | 2 | 25 | 0~0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_8955 | D-2,3-Dihydroxybutanedioic … | H2L | O=C(O)C(O)C(O)C(=O)O | 4 | 2 | 25 | 0~0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_8956 | meso-2,3-Dihydroxybutanedio… | H2L | O=C(O)[C@@H](O)[C@@H](O)C(=O)O | 4 | 2 | 25 | 0~0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_9048 | Propane-1,2,3-tricarboxylic… | H3L | O=C(O)CC(CC(=O)O)C(=O)O | 3 | 3 | 25 | 0 | *** | 0 |
| metal_78 | K^[+] | ligand_8953 | L-Hydroxybutanedioic acid (… | H2L | O=C(O)CC(O)C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_106 | Na^[+] | ligand_8955 | D-2,3-Dihydroxybutanedioic … | H2L | O=C(O)C(O)C(O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |

### logK — 45 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_9072 | Butane-1,2,3,4-tetracarboxy… | H4L | O=C(O)CC(C(=O)O)C(CC(=O)O)C(=O)O | 7 | 2 | 25 | 0~3 | *** | 6 |
| metal_174 | Sn^[2+] | ligand_9140 | DL-2,3-Dicarboxypropane-1,1… | H6L | O=C(O)CC(C(=O)O)C(P(=O)(O)O)P(=O)(O)O | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_9077 | rac-1-Hydroxy-3-oxapentane-… | H4L | O=C(O)CC(OC(C(=O)O)C(O)C(=O)O)C(=O)O | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_5 | Al^[3+] | ligand_8955 | D-2,3-Dihydroxybutanedioic … | H2L | O=C(O)C(O)C(O)C(=O)O | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_103 | Mo^[6+] | ligand_8955 | D-2,3-Dihydroxybutanedioic … | H2L | O=C(O)C(O)C(O)C(=O)O | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8953 | L-Hydroxybutanedioic acid (… | H2L | O=C(O)CC(O)C(=O)O | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_9140 | DL-2,3-Dicarboxypropane-1,1… | H6L | O=C(O)CC(C(=O)O)C(P(=O)(O)O)P(=O)(O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_9048 | Propane-1,2,3-tricarboxylic… | H3L | O=C(O)CC(CC(=O)O)C(=O)O | 2 | 1 | 25 | 0~0.1 | *** | 2 |
| metal_202 | VO_[2]^[+] | ligand_8955 | D-2,3-Dihydroxybutanedioic … | H2L | O=C(O)C(O)C(O)C(=O)O | 2 | 2 | 20 | 0.5 | *** | 1 |
| metal_103 | Mo^[6+] | ligand_8953 | L-Hydroxybutanedioic acid (… | H2L | O=C(O)CC(O)C(=O)O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_8955 | D-2,3-Dihydroxybutanedioic … | H2L | O=C(O)C(O)C(O)C(=O)O | 2 | 2 | 25 | 0.5 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8956 | meso-2,3-Dihydroxybutanedio… | H2L | O=C(O)[C@@H](O)[C@@H](O)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_19 | Be^[2+] | ligand_8953 | L-Hydroxybutanedioic acid (… | H2L | O=C(O)CC(O)C(=O)O | 2 | 2 | 25 | 0.5 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_8955 | D-2,3-Dihydroxybutanedioic … | H2L | O=C(O)C(O)C(O)C(=O)O | 2 | 2 | 25 | 0.5 | *** | 1 |
| metal_85 | Me_[2]Sn^[2+] | ligand_9072 | Butane-1,2,3,4-tetracarboxy… | H4L | O=C(O)CC(C(=O)O)C(CC(=O)O)C(=O)O | 2 | 2 | 25 | 0 | *** | 1 |
| metal_79 | La^[3+] | ligand_8955 | D-2,3-Dihydroxybutanedioic … | H2L | O=C(O)C(O)C(O)C(=O)O | 2 | 1 | 25 | 0~0.1 | *** | 2 |
| metal_41 | Cu^[2+] | ligand_9077 | rac-1-Hydroxy-3-oxapentane-… | H4L | O=C(O)CC(OC(C(=O)O)C(O)C(=O)O)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_8953 | L-Hydroxybutanedioic acid (… | H2L | O=C(O)CC(O)C(=O)O | 2 | 1 | 25 | 0.5~1 | *** | 2 |
| metal_19 | Be^[2+] | ligand_8955 | D-2,3-Dihydroxybutanedioic … | H2L | O=C(O)C(O)C(O)C(=O)O | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9077 | rac-1-Hydroxy-3-oxapentane-… | H4L | O=C(O)CC(OC(C(=O)O)C(O)C(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_5 | Al^[3+] | ligand_8956 | meso-2,3-Dihydroxybutanedio… | H2L | O=C(O)[C@@H](O)[C@@H](O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_201 | VO^[2+] | ligand_8955 | D-2,3-Dihydroxybutanedioic … | H2L | O=C(O)C(O)C(O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_74 | In^[3+] | ligand_8956 | meso-2,3-Dihydroxybutanedio… | H2L | O=C(O)[C@@H](O)[C@@H](O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_66 | Ge^[4+] | ligand_8953 | L-Hydroxybutanedioic acid (… | H2L | O=C(O)CC(O)C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_8958 | 2,3,4,5-Tetrahydroxyhexaned… | H2L | O=C(O)C(O)C(O)C(O)C(O)C(=O)O | 1 | 1 | 25 | 1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_8958 | 2,3,4,5-Tetrahydroxyhexaned… | H2L | O=C(O)C(O)C(O)C(O)C(O)C(=O)O | 1 | 1 | 25 | 1 | *** | 1 |
| metal_65 | Gd^[3+] | ligand_9048 | Propane-1,2,3-tricarboxylic… | H3L | O=C(O)CC(CC(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_110 | Nd^[3+] | ligand_8956 | meso-2,3-Dihydroxybutanedio… | H2L | O=C(O)[C@@H](O)[C@@H](O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_8953 | L-Hydroxybutanedioic acid (… | H2L | O=C(O)CC(O)C(=O)O | 1 | 1 | 25 | 1 | *** | 1 |
| metal_68 | H^[+] | ligand_8674 | DL-3-Hydroxybutanoic acid | HL | CC(O)CC(=O)O | 1 | 1 | 25 | 3 | *** | 1 |
| metal_201 | VO^[2+] | ligand_8956 | meso-2,3-Dihydroxybutanedio… | H2L | O=C(O)[C@@H](O)[C@@H](O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_5 | Al^[3+] | ligand_9077 | rac-1-Hydroxy-3-oxapentane-… | H4L | O=C(O)CC(OC(C(=O)O)C(O)C(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_8956 | meso-2,3-Dihydroxybutanedio… | H2L | O=C(O)[C@@H](O)[C@@H](O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_55 | Er^[3+] | ligand_8953 | L-Hydroxybutanedioic acid (… | H2L | O=C(O)CC(O)C(=O)O | 1 | 1 | 25 | 1 | *** | 1 |
| metal_94 | Mn^[2+] | ligand_9077 | rac-1-Hydroxy-3-oxapentane-… | H4L | O=C(O)CC(OC(C(=O)O)C(O)C(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_9077 | rac-1-Hydroxy-3-oxapentane-… | H4L | O=C(O)CC(OC(C(=O)O)C(O)C(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_8955 | D-2,3-Dihydroxybutanedioic … | H2L | O=C(O)C(O)C(O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_85 | Me_[2]Sn^[2+] | ligand_9048 | Propane-1,2,3-tricarboxylic… | H3L | O=C(O)CC(CC(=O)O)C(=O)O | 1 | 1 | 25 | 0 | *** | 1 |
| metal_10 | As^[3+] | ligand_8955 | D-2,3-Dihydroxybutanedioic … | H2L | O=C(O)C(O)C(O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_8955 | D-2,3-Dihydroxybutanedioic … | H2L | O=C(O)C(O)C(O)C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_9077 | rac-1-Hydroxy-3-oxapentane-… | H4L | O=C(O)CC(OC(C(=O)O)C(O)C(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_9077 | rac-1-Hydroxy-3-oxapentane-… | H4L | O=C(O)CC(OC(C(=O)O)C(O)C(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_8956 | meso-2,3-Dihydroxybutanedio… | H2L | O=C(O)[C@@H](O)[C@@H](O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_9057 | DL-1-Hydroxypropane-1,2,3-t… | H3L | O=C(O)CC(C(=O)O)C(O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_55 | Er^[3+] | ligand_8955 | D-2,3-Dihydroxybutanedioic … | H2L | O=C(O)C(O)C(O)C(=O)O | 1 | 1 | 25 | 1 | *** | 1 |

### ΔH — 1 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_9048 | Propane-1,2,3-tricarboxylic… | H3L | O=C(O)CC(CC(=O)O)C(=O)O | 2 | 2 | 25 | 0 | *** | 0 |

---
