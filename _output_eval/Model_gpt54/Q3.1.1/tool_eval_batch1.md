# Q3.1.1 — Tool Results (batch 1)

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
  "name": "EDTA, DTPA, EGTA, HEDTA, NTA, DMSA, succimer, DMPS, Dimercaprol, BAL, Penicillamine, Citrate",
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
  "name": "ethylenediaminetetraacetic acid, diethylenetriaminepentaacetic acid, ethylene glycol-bis(2-aminoethyl ether)-N,N,N',N'-tetraacetic acid, N-(2-hydroxyethyl)ethylenediamine-N,N',N'-triacetic acid, nitrilotriacetic acid, meso-2,3-dimercaptosuccinic acid, 2,3-dimercapto-1-propanesulfonic acid, 2,3-dimercaptopropan-1-ol, penicillamine, citric acid",
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
  "where": "(c.metal_id = metal_125 AND c.beta_definition_id = beta_def_812 AND s.solvent_name LIKE '%water%' AND s.temperature_c >= 20 AND s.temperature_c <= 30 AND s.ionic_strength_mol_l >= 0 AND s.ionic_strength_mol_l <= 0.25)",
  "order_by": "s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability

*(no results)*

---

### Step 9: `search_ligands`
**Args:**
```json
{
  "ligand_id": "ligand_5857",
  "limit": 20
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 20

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5857 | D-2-Amino-3-mercapto-3-methylbuta… (Penicillamine) | H2L | Amino Acids | 91 | `CC(C)(S)[C@H](N)C(=O)O` | (-inf, H3L, -1.9, H2L, 7.96, HL, 10.67, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 1 | 100% |
| primary_amine | 1 | 100% |
| thiol | 1 | 100% |

---

### Step 10: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_125 AND c.ligand_id IN (ligand_5857, ligand_9058, ligand_5856, ligand_6592, ligand_5760, ligand_8907, ligand_7541, ligand_7540))",
  "order_by": "s.constant_value DESC",
  "limit": 200
}
```

[summary]
## search_stability — 119 row(s)

### logK — 8 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_125 | Pb^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 17 | 8 | 25 | 0.1~3 | *** | 4 |
| metal_125 | Pb^[2+] | ligand_8907 | Butanedioic acid (Succinic … | H2L | O=C(O)CCC(=O)O | 16 | 8 | 25 | 0.1~3 | *** | 3 |
| metal_125 | Pb^[2+] | ligand_5857 | D-2-Amino-3-mercapto-3-meth… | H2L | CC(C)(S)[C@H](N)C(=O)O | 13 | 7 | 25~37 | 0.1~3 | *** | 3 |
| metal_125 | Pb^[2+] | ligand_7541 | 1,4,7,10,13,16,19,22,25,28,… | L | C1CNCCNCCNCCNCCNCCNCCNCCNCCNCCNCCNCCN1 | 12 | 12 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 12 | 8 | 25 | 1~2 | *** | 2 |
| metal_125 | Pb^[2+] | ligand_7540 | 1,4,7,10,13,16,19,22,25,28,… | L | C1CNCCNCCNCCNCCNCCNCCNCCNCCNCCNCCN1 | 11 | 11 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_5856 | L-2-Amino-3-mercaptopropano… | H2L | N[C@@H](CS)C(=O)O | 10 | 5 | 25 | 0.1~3 | *** | 4 |
| metal_125 | Pb^[2+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 6 | 6 | 25 | 3 | *** | 1 |

### ΔH — 3 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_125 | Pb^[2+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 4 | 4 | 25 | 3 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 4 | 3 | 25 | 0.1~3 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_5856 | L-2-Amino-3-mercaptopropano… | H2L | N[C@@H](CS)C(=O)O | 3 | 3 | 25 | 3 | *** | 0 |

### ΔS — 3 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_125 | Pb^[2+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 4 | 4 | 25 | 3 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 4 | 3 | 25 | 0.1~3 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_5856 | L-2-Amino-3-mercaptopropano… | H2L | N[C@@H](CS)C(=O)O | 3 | 3 | 25 | 3 | *** | 0 |

---

### Step 11: `search_ligands`
**Args:**
```json
{
  "name": "penicillamine, citric acid, cysteine, glutathione, glycine, succinic acid, [36]aneN12, [33]aneN11, EDTA, edetate, calcium disodium edetate, diethylenetriaminepentaacetic acid, nitrilotriacetic acid, meso-2,3-dimercaptosuccinic acid, succimer, dimercaprol, 2,3-dimercapto-1-propanesulfonic acid, DMPS",
  "limit": 100
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 12: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_125 AND c.ligand_id IN (ligand_5857, ligand_9058, ligand_5856, ligand_6592, ligand_5760, ligand_8907, ligand_7541, ligand_7540) AND s.constant_type = 'logK')",
  "order_by": "s.constant_value DESC",
  "limit": 200
}
```

[summary]
## search_stability

*(no results)*

---

### Step 13: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_7541"
}
```

[summary]
## inspect_card — Ligand | ligand_7541

**Name:** 1,4,7,10,13,16,19,22,25,28,31,34-Dodecaazacyclohexatriacontane ([36]aneN12)  
**Formula:** C24H60N12 | **Class:** Aza-macrocycles  
**SMILES:** `C1CNCCNCCNCCNCCNCCNCCNCCNCCNCCNCCNCCN1`  
**InChI:** `InChI=1S/C24H60N12/c1-2-26-5-6-28-9-10-30-13-14-32-17-18-34-21-22-36-24-23-35-20-19-33-16-15-31-12-11-29-8-7-27-4-3-25-1/h25-36H,1-24H2`  
**HxL definition:** L  

**pKa values:** 11

| source_vlm | pKa | T (°C) | I (M) | From → To | Solvent | Method | Quality |
|------------|-----|--------|-------|-----------|---------|--------|---------|
| vlm_130845 | -8.96 | 25.0 | 0.1 | H3L → H4L | *** | *** | *** |
| vlm_130844 | -8.88 | 25.0 | 0.1 | H2L → H3L | *** | *** | *** |
| vlm_130852 | 2.30 | 25.0 | 0.1 | H10L → H11L | *** | *** | *** |
| vlm_130851 | 2.62 | 25.0 | 0.1 | H9L → H10L | *** | *** | *** |
| vlm_130850 | 3.58 | 25.0 | 0.1 | H8L → H9L | *** | *** | *** |
| vlm_130849 | 4.27 | 25.0 | 0.1 | H7L → H8L | *** | *** | *** |
| vlm_130848 | 5.66 | 25.0 | 0.1 | H6L → H7L | *** | *** | *** |
| vlm_130847 | 7.82 | 25.0 | 0.1 | H5L → H6L | *** | *** | *** |
| vlm_130846 | 8.12 | 25.0 | 0.1 | H4L → H5L | *** | *** | *** |
| vlm_130843 | 9.65 | 25.0 | 0.1 | HL → H2L | *** | *** | *** |
| vlm_130842 | 9.75 | 25.0 | 0.1 | L → HL | *** | *** | *** |

**Partners:** 6 metal(s), 48 measurement(s) total

| metal_id | Metal | # meas |
|----------|-------|--------|
| metal_125 | Pb^[2+] | 12 |
| metal_68 | H^[+] | 11 |
| metal_41 | Cu^[2+] | 8 |
| metal_208 | Zn^[2+] | 6 |
| metal_33 | Co^[2+] | 6 |
| … | *(showing top 5 of 6)* | |

---

### Step 14: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_7540"
}
```

[summary]
## inspect_card — Ligand | ligand_7540

**Name:** 1,4,7,10,13,16,19,22,25,28,31-Undecaazacyclotritriacontane ([33]aneN11)  
**Formula:** C22H55N11 | **Class:** Aza-macrocycles  
**SMILES:** `C1CNCCNCCNCCNCCNCCNCCNCCNCCNCCNCCN1`  
**InChI:** `InChI=1S/C22H55N11/c1-2-24-5-6-26-9-10-28-13-14-30-17-18-32-21-22-33-20-19-31-16-15-29-12-11-27-8-7-25-4-3-23-1/h23-33H,1-22H2`  
**HxL definition:** L  

**pKa values:** 11

| source_vlm | pKa | T (°C) | I (M) | From → To | Solvent | Method | Quality |
|------------|-----|--------|-------|-----------|---------|--------|---------|
| vlm_130806 | -1.70 | 25.0 | 0.1 | H10L → H11L | *** | *** | *** |
| vlm_130805 | 2.26 | 25.0 | 0.1 | H9L → H10L | *** | *** | *** |
| vlm_130804 | 2.76 | 25.0 | 0.1 | H8L → H9L | *** | *** | *** |
| vlm_130803 | 3.58 | 25.0 | 0.1 | H7L → H8L | *** | *** | *** |
| vlm_130802 | 4.49 | 25.0 | 0.1 | H6L → H7L | *** | *** | *** |
| vlm_130801 | 6.44 | 25.0 | 0.1 | H5L → H6L | *** | *** | *** |
| vlm_130800 | 8.06 | 25.0 | 0.1 | H4L → H5L | *** | *** | *** |
| vlm_130799 | 8.64 | 25.0 | 0.1 | H3L → H4L | *** | *** | *** |
| vlm_130798 | 9.02 | 25.0 | 0.1 | H2L → H3L | *** | *** | *** |
| vlm_130797 | 9.48 | 25.0 | 0.1 | HL → H2L | *** | *** | *** |
| vlm_130796 | 9.79 | 25.0 | 0.1 | L → HL | *** | *** | *** |

**Partners:** 7 metal(s), 46 measurement(s) total

| metal_id | Metal | # meas |
|----------|-------|--------|
| metal_125 | Pb^[2+] | 11 |
| metal_68 | H^[+] | 11 |
| metal_41 | Cu^[2+] | 8 |
| metal_208 | Zn^[2+] | 5 |
| metal_112 | Ni^[2+] | 4 |
| … | *(showing top 5 of 7)* | |

---
