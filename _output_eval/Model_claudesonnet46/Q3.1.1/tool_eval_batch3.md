# Q3.1.1 — Tool Results (batch 3)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "lead",
  "limit": 5
}
```

[summary]
## search_metals — 5 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_16 | Bu_[3]Pb^[+] | B | 1 |  | *** | *** | beta_totN_2 | ligand_totN_1 | vlm_totN_2 |
| metal_46 | Et_[2]Pb^[2+] | E2Pb | 2 |  | *** | *** | beta_totN_2 | ligand_totN_3 | vlm_totN_5 |
| metal_49 | Et_[3]Pb^[+] | E3Pb | 1 |  | *** | *** | beta_totN_2 | ligand_totN_3 | vlm_totN_5 |
| metal_84 | Me_[2]Pb^[2+] | M2Pb | 2 |  | *** | *** | beta_totN_5 | ligand_totN_4 | vlm_totN_9 |
| metal_87 | Me_[3]Pb^[+] | M3Pb | 1 |  | *** | *** | beta_totN_7 | ligand_totN_23 | vlm_totN_33 |

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "EDTA",
  "limit": 3
}
```

[summary]
## search_ligands — 3 result(s)

**stats:** 5 SQL matches · showing 3 · limit 3

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6118 | 6,11,18,23-Tetraoxo-1,4,7,10,13,16,19,… (24edtaen) | *** | Aza macrocycles with car… | 15 | *** | (-inf, H4L, 3.3, H3L, 4.18, H2L, 7.26, HL, 7.78, L, +inf) |
| ligand_6275 | N-(2-Hydroxyethyl)ethylenedinitrilotriace… (HEDTA) | H3L | EDTA and derivatives | 237 | `O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O` | (-inf, H3L, 2.62, H2L, 5.38, HL, 9.7, L, +inf) |
| ligand_6277 | Ethylenedinitrilotetraacetic acid (EDTA) | H4L | EDTA and derivatives | 596 | `O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O` | (-inf, H5L, -1.5, H4L, 2, H3L, 2.69, H2L, 6.13, HL, 9.52, L, +inf) |

### Functional groups across all SQL matches (4 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 4 | 100% |
| tertiary_amine | 4 | 100% |
| ether | 1 | 25% |
| hydroxyl | 1 | 25% |
| thioether | 1 | 25% |

---

### Step 4: `search_ligands`
**Args:**
```json
{
  "name": "DTPA",
  "limit": 3
}
```

[summary]
## search_ligands — 3 result(s)

**stats:** 5 SQL matches · showing 3 · limit 3

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6117 | 9,17-Dioxo-1,4,7,10,13,16-hexaazacycl… (DTPA-dien) | H3L | Aza macrocycles with car… | 6 | `O=C(O)CN1CCN(CC(=O)O)CC(=O)NCCNCCNC(=O)CN(CC(=O)O)CC1` | (-inf, H5L, -1.8, H4L, 2.62, H3L, 4.1, H2L, 8.87, HL, 10.02, L, +inf) |
| ligand_6356 | Diethylenetrinitrilopentaacetic acid (DTPA) | H5L | EDTA and derivatives | 322 | `O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O` | (-inf, H8L, -0.1, H7L, -0.1, H6L, -0.7, H5L, 2, H4L, 2.7, H3L, 4.28, H2L, 4.28, HL, -8.4, L, +inf) |
| ligand_6362 | Diethylenetrinitrilopentaacetic acid N… (DTPA-BMA) | *** | EDTA and derivatives | 43 | *** | (-inf, H4L, -1.4, H3L, 3.31, H2L, 4.38, HL, 9.37, L, +inf) |

### Functional groups across all SQL matches (2 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 2 | 100% |
| tertiary_amine | 2 | 100% |
| amide | 1 | 50% |
| secondary_amine | 1 | 50% |

---

### Step 5: `search_metals`
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

### Step 6: `search_ligands`
**Args:**
```json
{
  "name": "DMSA",
  "limit": 3
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 3

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8997 | meso-2,3-Dimercaptobut… (meso-Dithiotartaric acid) | H4L | Carboxylic acids diacids… | 41 | `O=C(O)[C@@H](S)[C@@H](S)C(=O)O` | (-inf, H4L, 2.4, H3L, 3.46, H2L, 9.64, HL, 9.64, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 1 | 100% |
| thiol | 1 | 100% |

---

### Step 7: `search_ligands`
**Args:**
```json
{
  "name": "penicillamine",
  "limit": 3
}
```

[summary]
## search_ligands — 3 result(s)

**stats:** 6 SQL matches · showing 3 · limit 3

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5857 | D-2-Amino-3-mercapto-3-methylbuta… (Penicillamine) | H2L | Amino Acids | 91 | `CC(C)(S)[C@H](N)C(=O)O` | (-inf, H3L, -1.9, H2L, 7.96, HL, 10.67, L, +inf) |
| ligand_5891 | D-3,3'-Dithiobis(2-amin… (Penicillamine disulfide) | H2L | Amino Acids | 23 | `CC(C)(SSC(C)(C)C(N)C(=O)O)C(N)C(=O)O` | (-inf, H4L, -1.3, H3L, 2.04, H2L, 7.77, HL, 8.74, L, +inf) |
| ligand_6657 | L-5-Glutamyl… (Penicillamine-glutatione disulfide) | H3L | polypeptides | 2 | `CC(C)(SSCC(NC(=O)CCC(N)C(=O)O)C(=O)NCC(=O)O)C(N)C(=O)O` | (-inf, H2L, 7.99, HL, 9.1, L, +inf) |

### Functional groups across all SQL matches (4 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 4 | 100% |
| primary_amine | 3 | 75% |
| amide | 2 | 50% |
| thiol | 2 | 50% |

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_125 AND c.ligand_id = ligand_6277",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 9: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_125 AND c.ligand_id = ligand_6356",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 10: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_125 AND c.ligand_id = ligand_8997",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 11: `build_system_catalog`
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

### Step 13: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_125 AND c.ligand_id = ligand_6277 AND s.constant_type = 'log_beta')",
  "order_by": "s.constant_value DESC",
  "limit": 5
}
```

[summary]
## search_stability

*(no results)*

---

### Step 14: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_125 AND c.ligand_id = ligand_6356 AND s.constant_type = 'log_beta')",
  "order_by": "s.constant_value DESC",
  "limit": 5
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
  "where": "(c.metal_id = metal_125 AND c.ligand_id = ligand_8997 AND s.constant_type = 'log_beta')",
  "order_by": "s.constant_value DESC",
  "limit": 5
}
```

[summary]
## search_stability

*(no results)*

---

### Step 16: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_125 AND c.ligand_id = ligand_5857 AND s.constant_type = 'log_beta')",
  "order_by": "s.constant_value DESC",
  "limit": 5
}
```

[summary]
## search_stability

*(no results)*

---
