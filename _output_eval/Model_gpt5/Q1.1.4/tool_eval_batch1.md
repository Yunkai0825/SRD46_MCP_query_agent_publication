# Q1.1.4 — Tool Results (batch 1)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "silver",
  "symbol": "Ag",
  "limit": 5
}
```

[summary]
## search_metals — 3 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_2 | Ag^[+] | Ag | 1 | ✓ | [Ag+] | InChI=1S/Ag/q+1 | beta_totN_68 | ligand_totN_649 | vlm_totN_2885 |
| metal_3 | Ag^[2+] | Ag | 2 | ✓ | [Ag+2] | InChI=1S/Ag/q+2 | beta_totN_1 | ligand_totN_5 | vlm_totN_5 |
| metal_4 | Ag^[3+] | Ag | 3 | ✓ | [Ag+3] | InChI=1S/Ag/q+3 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "ammonia",
  "formula": "NH3",
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
  "name": "ammine",
  "limit": 20
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
  "metal_id": "metal_2"
}
```

[summary]
[CATALOG]
## build_system_catalog — 20 pair(s), 148 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_149 | [M(HL)2] + [H] <=> [M(H2L)(HL)] |  |
| beta_def_156 | [M] + [H2L]^2 <=> [M(H2L)2] |  |
| beta_def_163 | [M(H2L)(HL)] + [H] <=> [M(H2L)2] |  |
| beta_def_167 | [M(HL)2] + [H]^2 <=> [M(H2L)2] |  |
| beta_def_171 | [MH3L2] + [H] <=> [M(H2L)2] |  |
| beta_def_194 | [M] + [HL]^2 <=> [M(HL)2] |  |
| beta_def_204 | [MHL2] + [H] <=> [M(HL)2] |  |
| beta_def_311 | [ML(s)] <=> [M] + [L] | solid |
| beta_def_406 | [M2HL2] + [H] <=> [M2(HL)2] |  |
| beta_def_478 | [M2HL2] + [H] <=> [M2H2L2] |  |
| beta_def_494 | [MHL] + [M] <=> [M2HL] |  |
| beta_def_499 | [M2L2] + [H] <=> [M2HL2] |  |
| beta_def_502 | [M]^2 + [L] <=> [M2L] |  |
| beta_def_519 | [M]^2 + [L]^2 <=> [M2L2] |  |
| beta_def_538 | [ML2] + [M] <=> [M2L2] |  |
| beta_def_540 | [M]^2 + [L]^3 <=> [M2L3] |  |
| beta_def_548 | [M]^2 + [L]^4 <=> [M2L4] |  |
| beta_def_550 | [M]^2 + [L]^6 <=> [M2L6] |  |
| beta_def_652 | [M]^3 + [L]^5 <=> [M3L5] |  |
| beta_def_655 | [M]^3 + [L]^8 <=> [M3L8] |  |
| beta_def_706 | [M]^6 + [L]^8 <=> [M6L8] |  |
| beta_def_732 | [M] + [H2L] <=> [MH2L] |  |
| beta_def_739 | [MHL] + [H] <=> [MH2L] |  |
| beta_def_756 | [M(HL)2] + [H] <=> [MH3L2] |  |
| beta_def_779 | [M] + [HL] <=> [MHL] |  |
| beta_def_792 | [ML2] + [H] <=> [MHL2] |  |
| beta_def_798 | [M] + [HL] + [L] <=> [MHL2] |  |
| beta_def_812 | [M] + [L] <=> [ML] |  |
| beta_def_840 | [M] + [L]^2 <=> [ML2] |  |
| beta_def_872 | [M] + [L]^3 <=> [ML3] |  |
| beta_def_894 | [M] + [L]^4 <=> [ML4] |  |

*(all species aqueous unless noted)*

**1. Ag^[+] + Ammonia** (metal_2 + ligand_10103) — ligand_def_HxL: L | 47 ent, 2 sp, 47 vlms (vlm_173338…vlm_173384)
   - species: beta_def_812(22) beta_def_840(25)
   - eq:16 nets T:19~30°C I:-0.05~5.15M max 2n/1e
**2. Ag^[+] + Ethylenediamine** (metal_2 + ligand_7029) — ligand_def_HxL: L | 40 ent, 6 sp, 40 vlms (vlm_122464…vlm_122503)
   - species: beta_def_194(5) beta_def_519(9) beta_def_779(6) beta_def_792(5) beta_def_812(5) beta_def_840(10)
   - eq:6 nets T:15~30°C I:-0.05~3.15M max 6n/11e
**3. Ag^[+] + Chloride ion** (metal_2 + ligand_10163) — ligand_def_HxL: *** | 37 ent, 5 sp, 37 vlms (vlm_177429…vlm_177465)
   - species: beta_def_311(14) beta_def_812(7) beta_def_840(7) beta_def_872(5) beta_def_894(4)
   - eq:7 nets T:11~41°C I:-0.15~5.15M max 5n/10e
**4. Ag^[+] + Thiocarbamide (Thiourea)** (metal_2 + ligand_10004) — ligand_def_HxL: L | 33 ent, 5 sp, 33 vlms (vlm_169451…vlm_169483)
   - species: beta_def_540(3) beta_def_812(9) beta_def_840(9) beta_def_872(9) beta_def_894(3)
   - eq:3 nets T:19~30°C I:-0.05~1.15M max 4n/6e
**5. Ag^[+] + Bromide ion** (metal_2 + ligand_10168) — ligand_def_HxL: *** | 27 ent, 5 sp, 27 vlms (vlm_178014…vlm_178040)
   - species: beta_def_311(14) beta_def_812(2) beta_def_840(2) beta_def_872(5) beta_def_894(4)
   - eq:6 nets T:11~41°C I:-0.15~5.15M max 5n/10e
**6. Ag^[+] + Iodide ion** (metal_2 + ligand_10171) — ligand_def_HxL: *** | 26 ent, 7 sp, 26 vlms (vlm_178425…vlm_178450)
   - species: beta_def_311(11) beta_def_550(1) beta_def_655(1) beta_def_812(2) beta_def_840(2) beta_def_872(6) beta_def_894(3)
   - eq:7 nets T:13~41°C I:-0.15~7.15M max 7n/21e
**7. Ag^[+] + 2-[2-(2-Aminoethylthio)ethyl]pyridine** (metal_2 + ligand_8063) — ligand_def_HxL: L | 26 ent, 10 sp, 26 vlms (vlm_137193…vlm_137218)
   - species: beta_def_149(3) beta_def_167(3) beta_def_194(3) beta_def_478(3) beta_def_494(1) beta_def_499(3) beta_def_502(1) beta_def_519(3) beta_def_739(3) beta_def_779(3)
   - eq:1 nets T:16.5~31.5°C I:0.275~0.725M max 10n/25e
**8. Ag^[+] + 2-[3-Aminopropylthiomethyl]pyridine** (metal_2 + ligand_8062) — ligand_def_HxL: L | 26 ent, 10 sp, 26 vlms (vlm_137152…vlm_137177)
   - species: beta_def_149(3) beta_def_167(3) beta_def_194(3) beta_def_478(3) beta_def_494(1) beta_def_499(3) beta_def_502(1) beta_def_519(3) beta_def_739(3) beta_def_779(3)
   - eq:1 nets T:16.5~31.5°C I:0.275~0.725M max 10n/25e
**9. Ag^[+] + 2-(2-Aminoethylthio)ethanol** (metal_2 + ligand_7016) — ligand_def_HxL: L | 25 ent, 7 sp, 25 vlms (vlm_122188…vlm_122212)
   - species: beta_def_194(3) beta_def_502(3) beta_def_519(3) beta_def_779(3) beta_def_798(3) beta_def_812(5) beta_def_840(5)
   - eq:3 nets T:19~35°C I:-0.05~1.15M max 7n/21e
**10. Ag^[+] + 2-[2-(3-Aminopropylthio)ethyl]pyridine** (metal_2 + ligand_8064) — ligand_def_HxL: L | 24 ent, 10 sp, 24 vlms (vlm_137225…vlm_137248)
   - species: beta_def_149(3) beta_def_163(3) beta_def_194(3) beta_def_478(1) beta_def_494(1) beta_def_499(3) beta_def_502(1) beta_def_519(3) beta_def_739(3) beta_def_779(3)
   - eq:1 nets T:16.5~31.5°C I:0.275~0.725M max 10n/24e
**11. Ag^[+] + 2-[2-Aminoethylthiomethyl]pyridine** (metal_2 + ligand_8061) — ligand_def_HxL: L | 23 ent, 9 sp, 23 vlms (vlm_137117…vlm_137139)
   - species: beta_def_149(3) beta_def_167(1) beta_def_194(3) beta_def_478(3) beta_def_499(3) beta_def_502(1) beta_def_519(3) beta_def_739(3) beta_def_779(3)
   - eq:1 nets T:16.5~31.5°C I:0.275~0.725M max 9n/20e
**12. Ag^[+] + Hydrogen nitrite (Nitrous acid)** (metal_2 + ligand_10108) — ligand_def_HxL: HL | 21 ent, 3 sp, 21 vlms (vlm_173782…vlm_173802)
   - species: beta_def_311(7) beta_def_812(7) beta_def_840(7)
   - eq:5 nets T:15~30°C I:-0.05~3.15M max 3n/3e
**13. Ag^[+] + Hydrogen thiocyanate (Thiocyanic acid)** (metal_2 + ligand_10092) — ligand_def_HxL: HL | 21 ent, 5 sp, 21 vlms (vlm_172335…vlm_172355)
   - species: beta_def_311(4) beta_def_812(5) beta_def_840(4) beta_def_872(4) beta_def_894(4)
   - eq:4 nets T:19~30°C I:-0.15~4.15M max 5n/10e
**14. Ag^[+] + Hydrogen thiosulfate (Thiosulfuric acid)** (metal_2 + ligand_10149) — ligand_def_HxL: H2L | 19 ent, 6 sp, 19 vlms (vlm_176253…vlm_176271)
   - species: beta_def_548(1) beta_def_652(1) beta_def_706(1) beta_def_812(5) beta_def_840(7) beta_def_872(4)
   - eq:4 nets T:19~30°C I:-0.05~4.15M max 6n/15e
**15. Ag^[+] + N,N-Diethyl-2-(methylthio)ethylamine** (metal_2 + ligand_7292) — ligand_def_HxL: L | 19 ent, 7 sp, 19 vlms (vlm_127281…vlm_127299)
   - species: beta_def_194(3) beta_def_502(3) beta_def_519(3) beta_def_779(3) beta_def_792(3) beta_def_812(1) beta_def_840(3)
   - eq:1 nets T:16.5~31.5°C I:0.275~0.725M max 7n/16e
**16. Ag^[+] + N,N-Dimethyl-2-(methylthio)ethylamine** (metal_2 + ligand_7291) — ligand_def_HxL: L | 19 ent, 7 sp, 19 vlms (vlm_127259…vlm_127277)
   - species: beta_def_194(3) beta_def_502(3) beta_def_519(3) beta_def_779(3) beta_def_792(3) beta_def_812(1) beta_def_840(3)
   - eq:1 nets T:16.5~31.5°C I:0.275~0.725M max 7n/16e
**17. Ag^[+] + 5-Thia-1,10-diazadecane** (metal_2 + ligand_7086) — ligand_def_HxL: L | 19 ent, 11 sp, 19 vlms (vlm_123852…vlm_123870)
   - species: beta_def_156(3) beta_def_171(1) beta_def_204(1) beta_def_406(1) beta_def_499(1) beta_def_502(1) beta_def_538(3) beta_def_732(3) beta_def_756(1) beta_def_792(1) beta_def_840(3)
   - eq:1 nets T:16.5~31.5°C I:0.275~0.725M max 11n/29e
**18. Ag^[+] + 4-Thia-1,9-diazanonane** (metal_2 + ligand_7084) — ligand_def_HxL: L | 19 ent, 11 sp, 19 vlms (vlm_123814…vlm_123832)
   - species: beta_def_156(3) beta_def_204(1) beta_def_406(1) beta_def_499(1) beta_def_502(1) beta_def_538(3) beta_def_732(3) beta_def_739(1) beta_def_756(1) beta_def_792(1) beta_def_840(3)
   - eq:1 nets T:16.5~31.5°C I:0.275~0.725M max 11n/29e
**19. Ag^[+] + 4-Thia-1,8-diazaoctane** (metal_2 + ligand_7083) — ligand_def_HxL: L | 19 ent, 11 sp, 19 vlms (vlm_123787…vlm_123805)
   - species: beta_def_156(3) beta_def_204(1) beta_def_406(1) beta_def_499(1) beta_def_502(1) beta_def_538(3) beta_def_732(3) beta_def_739(1) beta_def_756(1) beta_def_792(1) beta_def_840(3)
   - eq:1 nets T:16.5~31.5°C I:0.275~0.725M max 11n/29e
**20. Ag^[+] + 4-Thia-1,7-diazaheptane (Thiobis(ethyleneamine))** (metal_2 + ligand_7082) — ligand_def_HxL: L | 19 ent, 11 sp, 19 vlms (vlm_123726…vlm_123744)
   - species: beta_def_156(3) beta_def_204(1) beta_def_406(1) beta_def_499(1) beta_def_502(1) beta_def_538(3) beta_def_732(3) beta_def_739(1) beta_def_756(1) beta_def_792(1) beta_def_840(3)
   - eq:1 nets T:16.5~31.5°C I:0.275~0.725M max 11n/29e

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_2 AND c.ligand_id = ligand_10103 AND c.beta_definition_id IN (beta_def_812, beta_def_840))",
  "order_by": "c.beta_definition_id ASC, s.constant_type ASC, s.temperature_c ASC, s.ionic_strength_mol_l ASC",
  "limit": 500
}
```

[summary]
## search_stability — 47 row(s)

### `Ag^[+]` + Ammonia — 47 measurement(s)
metal_id: metal_2 | ligand_id: ligand_10103
ligand_HxL_def: L | ligand_SMILES: N

| equation | type | vlm_counts | ref_eq_map | value_range | T°C_range | I(M)_range | beta_defs | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|----------|------|------------|------------|-------------|-----------|------------|-----------|--------------------|--------------|-------------|
| `[M] + [L] <=> [ML]` | ΔH | 5 | *** | -25.9~-20.5 | 25 | 0~3 | beta_def_812 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L] <=> [ML]` | logK | 13 | 13 diff ref_eq_map | 3.2~3.8 | 25 | 0~5 | beta_def_812 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L] <=> [ML]` | ΔS | 4 | *** | -12.1~-5.4 | 25 | 0~3 | beta_def_812 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^2 <=> [ML2]` | ΔH | 5 | *** | -61.9~-56.1 | 25 | 0~3 | beta_def_840 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^2 <=> [ML2]` | logK | 16 | 16 diff ref_eq_map | 7.14~8.18 | 25 | 0~5 | beta_def_840 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^2 <=> [ML2]` | ΔS | 4 | *** | -55.6~-46.4 | 25 | 0~3 | beta_def_840 | *** | [L] | (9.26, L, +inf) |

Summary stats
| type | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|------|------------|-------------|-----------|------------|--------------------|-------------------|
| ΔH | 10 | 2 | 25 | 0~3 | *** | 0 |
| logK | 29 | 2 | 25 | 0~5 | *** | 16 |
| ΔS | 8 | 2 | 25 | 0~3 | *** | 0 |

---
