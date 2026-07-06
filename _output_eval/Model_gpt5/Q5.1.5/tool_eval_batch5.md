# Q5.1.5 — Tool Results (batch 5)

### Step 2: `search_ligands`
**Args:**
```json
{
  "name": "EDTA",
  "limit": 20
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 5 SQL matches · showing 5 · limit 20

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6118 | 6,11,18,23-Tetraoxo-1,4,7,10,13,16,19,… (24edtaen) | *** | Aza macrocycles with car… | 15 | *** | (-inf, H4L, 3.3, H3L, 4.18, H2L, 7.26, HL, 7.78, L, +inf) |
| ligand_6275 | N-(2-Hydroxyethyl)ethylenedinitrilotriace… (HEDTA) | H3L | EDTA and derivatives | 237 | `O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O` | (-inf, H3L, 2.62, H2L, 5.38, HL, 9.7, L, +inf) |
| ligand_6277 | Ethylenedinitrilotetraacetic acid (EDTA) | H4L | EDTA and derivatives | 596 | `O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O` | (-inf, H5L, -1.5, H4L, 2, H3L, 2.69, H2L, 6.13, HL, 9.52, L, +inf) |
| ligand_6335 | Oxybis(ethylenenitrilo)tetraacetic acid (EEDTA) | H4L | EDTA and derivatives | 124 | `O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O` | (-inf, H4L, -1.8, H3L, 2.76, H2L, 8.75, HL, 9.39, L, +inf) |
| ligand_6348 | Thiobis(ethylenenitrilo)tetraacetic acid (TEDTA) | H4L | EDTA and derivatives | 101 | `O=C(O)CN(CCSCCN(CC(=O)O)CC(=O)O)CC(=O)O` | (-inf, H4L, 2, H3L, 2.68, H2L, 8.37, HL, 9.31, L, +inf) |

### Functional groups across all SQL matches (4 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 4 | 100% |
| tertiary_amine | 4 | 100% |
| ether | 1 | 25% |
| hydroxyl | 1 | 25% |
| thioether | 1 | 25% |

---

### Step 3: `search_metals`
**Args:**
```json
{
  "symbol": "Fe",
  "limit": 1
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_61 | Fe^[3+] | Fe | 3 | ✓ | [Fe+3] | InChI=1S/Fe/q+3 | beta_totN_128 | ligand_totN_406 | vlm_totN_1473 |

---

### Step 4: `search_metals`
**Args:**
```json
{
  "symbol": "Cu",
  "limit": 1
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_41 | Cu^[2+] | Cu | 2 | ✓ | [Cu+2] | InChI=1S/Cu/q+2 | beta_totN_264 | ligand_totN_1951 | vlm_totN_8963 |

---

### Step 5: `search_metals`
**Args:**
```json
{
  "symbol": "Zn",
  "limit": 1
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_208 | Zn^[2+] | Zn | 2 | ✓ | [Zn+2] | InChI=1S/Zn/q+2 | beta_totN_122 | ligand_totN_1169 | vlm_totN_4095 |

---

### Step 6: `search_metals`
**Args:**
```json
{
  "symbol": "Ni",
  "limit": 1
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_112 | Ni^[2+] | Ni | 2 | ✓ | [Ni+2] | InChI=1S/Ni/q+2 | beta_totN_149 | ligand_totN_1369 | vlm_totN_5325 |

---

### Step 7: `search_metals`
**Args:**
```json
{
  "symbol": "Co",
  "limit": 1
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_33 | Co^[2+] | Co | 2 | ✓ | [Co+2] | InChI=1S/Co/q+2 | beta_totN_92 | ligand_totN_977 | vlm_totN_2977 |

---

### Step 8: `search_metals`
**Args:**
```json
{
  "symbol": "Pb",
  "limit": 1
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_16 | Bu_[3]Pb^[+] | B | 1 |  | *** | *** | beta_totN_2 | ligand_totN_1 | vlm_totN_2 |

---

### Step 9: `search_metals`
**Args:**
```json
{
  "symbol": "Cd",
  "limit": 1
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_26 | Cd^[2+] | Cd | 2 | ✓ | [Cd+2] | InChI=1S/Cd/q+2 | beta_totN_95 | ligand_totN_818 | vlm_totN_2828 |

---

### Step 10: `search_metals`
**Args:**
```json
{
  "symbol": "Al",
  "limit": 1
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_5 | Al^[3+] | Al | 3 | ✓ | [Al+3] | InChI=1S/Al/q+3 | beta_totN_108 | ligand_totN_187 | vlm_totN_792 |

---

### Step 11: `search_metals`
**Args:**
```json
{
  "symbol": "Ca",
  "limit": 1
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_25 | Ca^[2+] | Ca | 2 | ✓ | [Ca+2] | InChI=1S/Ca/q+2 | beta_totN_68 | ligand_totN_644 | vlm_totN_1761 |

---

### Step 12: `search_metals`
**Args:**
```json
{
  "symbol": "Mg",
  "limit": 1
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_92 | Mg^[2+] | Mg | 2 | ✓ | [Mg+2] | InChI=1S/Mg/q+2 | beta_totN_53 | ligand_totN_508 | vlm_totN_1422 |

---

### Step 13: `search_metals`
**Args:**
```json
{
  "symbol": "Hg",
  "limit": 1
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_20 | BuHg^[+] | B | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |

---

### Step 14: `search_metals`
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

### Step 15: `search_metals`
**Args:**
```json
{
  "symbol": "Pb",
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

### Step 17: `build_system_catalog`
**Args:**
```json
{
  "ligand_id": "ligand_6277"
}
```

[summary]
[CATALOG]
## build_system_catalog — 20 pair(s), 66 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_32 | [HL] + [H] <=> [H2L] |  |
| beta_def_53 | [H2L] + [H] <=> [H3L] |  |
| beta_def_64 | [H3L] + [H] <=> [H4L] |  |
| beta_def_68 | [H4L] + [H] <=> [H5L] |  |
| beta_def_72 | [H5L] + [H] <=> [H6L] |  |
| beta_def_79 | [L] + [H] <=> [HL] |  |
| beta_def_238 | [M(OH)2L] + [H] <=> [M(OH)L] + [H2O] |  |
| beta_def_423 | [ML]^2 + [H2O]^2 <=> [M2(OH)2L2] + [H]^2 |  |
| beta_def_427 | [M(OH)L]^2 <=> [M2(OH)2L2] |  |
| beta_def_502 | [M]^2 + [L] <=> [M2L] |  |
| beta_def_536 | [M2L] + [L] <=> [M2L2] |  |
| beta_def_570 | [M2(OH)L] + [H] <=> [M2L] + [H2O] |  |
| beta_def_662 | [M]^4 + [L]^2 + [H2O]^4 <=> [M4(OH)4L2] + [H]^4 |  |
| beta_def_699 | [M]^6 + [L]^3 + [H2O]^4 <=> [M6(OH)4L3] + [H]^4 |  |
| beta_def_739 | [MHL] + [H] <=> [MH2L] |  |
| beta_def_751 | [MH2L] + [H] <=> [MH3L] |  |
| beta_def_779 | [M] + [HL] <=> [MHL] |  |
| beta_def_788 | [ML] + [H] <=> [MHL] |  |
| beta_def_812 | [M] + [L] <=> [ML] |  |
| beta_def_966 | [M(OH)L] + [H] <=> [ML] + [H2O] |  |

*(all species aqueous)*

**1. H^[+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_68 + ligand_6277) — ligand_def_HxL: H4L | 75 ent, 6 sp, 75 vlms (vlm_108224…vlm_108298)
   - species: beta_def_32(18) beta_def_53(10) beta_def_64(7) beta_def_68(6) beta_def_72(4) beta_def_79(30)
   - eq:14 nets T:19~41°C I:-0.15~3.15M max 6n/15e
**2. Cd^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_26 + ligand_6277) — ligand_def_HxL: H4L | 23 ent, 4 sp, 23 vlms (vlm_108725…vlm_108747)
   - species: beta_def_739(1) beta_def_788(5) beta_def_812(14) beta_def_966(3)
   - eq:5 nets T:19~30°C I:-0.15~3.15M max 4n/5e
**3. Cu^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_41 + ligand_6277) — ligand_def_HxL: H4L | 20 ent, 4 sp, 20 vlms (vlm_108604…vlm_108623)
   - species: beta_def_739(2) beta_def_788(4) beta_def_812(8) beta_def_966(6)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 4n/5e
**4. Ni^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_112 + ligand_6277) — ligand_def_HxL: H4L | 19 ent, 4 sp, 19 vlms (vlm_108585…vlm_108603)
   - species: beta_def_739(1) beta_def_788(4) beta_def_812(8) beta_def_966(6)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 3n/3e
**5. Zn^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_208 + ligand_6277) — ligand_def_HxL: H4L | 18 ent, 4 sp, 18 vlms (vlm_108707…vlm_108724)
   - species: beta_def_739(1) beta_def_788(5) beta_def_812(6) beta_def_966(6)
   - eq:5 nets T:19~30°C I:-0.15~3.15M max 4n/5e
**6. Mg^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_92 + ligand_6277) — ligand_def_HxL: H4L | 18 ent, 2 sp, 18 vlms (vlm_108326…vlm_108343)
   - species: beta_def_788(2) beta_def_812(16)
   - eq:6 nets T:19~41°C I:-0.05~1.15M max 2n/1e
**7. Ca^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_25 + ligand_6277) — ligand_def_HxL: H4L | 18 ent, 2 sp, 18 vlms (vlm_108344…vlm_108361)
   - species: beta_def_788(2) beta_def_812(16)
   - eq:6 nets T:19~41°C I:-0.05~1.15M max 2n/1e
**8. Fe^[3+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_61 + ligand_6277) — ligand_def_HxL: H4L | 14 ent, 4 sp, 14 vlms (vlm_108639…vlm_108652)
   - species: beta_def_427(3) beta_def_788(3) beta_def_812(4) beta_def_966(4)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 3n/3e
**9. VO_[2]^[+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_202 + ligand_6277) — ligand_def_HxL: H4L | 13 ent, 4 sp, 13 vlms (vlm_108673…vlm_108685)
   - species: beta_def_739(5) beta_def_751(1) beta_def_788(5) beta_def_812(2)
   - eq:3 nets T:19~30°C I:-0.05~3.15M max 4n/4e
**10. Co^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_33 + ligand_6277) — ligand_def_HxL: H4L | 13 ent, 3 sp, 13 vlms (vlm_108572…vlm_108584)
   - species: beta_def_739(1) beta_def_788(4) beta_def_812(8)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 2n/1e
**11. Al^[3+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_5 + ligand_6277) — ligand_def_HxL: H4L | 13 ent, 4 sp, 13 vlms (vlm_108770…vlm_108782)
   - species: beta_def_238(2) beta_def_788(4) beta_def_812(3) beta_def_966(4)
   - eq:3 nets T:19~30°C I:-0.05~1.15M max 4n/5e
**12. La^[3+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_79 + ligand_6277) — ligand_def_HxL: H4L | 12 ent, 2 sp, 12 vlms (vlm_108389…vlm_108400)
   - species: beta_def_788(3) beta_def_812(9)
   - eq:4 nets T:15~30°C I:-0.05~1.15M max 2n/1e
**13. Nd^[3+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_110 + ligand_6277) — ligand_def_HxL: H4L | 11 ent, 2 sp, 11 vlms (vlm_108416…vlm_108426)
   - species: beta_def_788(2) beta_def_812(9)
   - eq:3 nets T:19~30°C I:-0.05~1.15M max 2n/1e
**14. Hg^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_71 + ligand_6277) — ligand_def_HxL: H4L | 11 ent, 4 sp, 11 vlms (vlm_108748…vlm_108758)
   - species: beta_def_739(1) beta_def_788(4) beta_def_812(5) beta_def_966(1)
   - eq:3 nets T:19~30°C I:-0.05~1.15M max 3n/3e
**15. Eu^[3+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_58 + ligand_6277) — ligand_def_HxL: H4L | 11 ent, 2 sp, 11 vlms (vlm_108438…vlm_108448)
   - species: beta_def_788(1) beta_def_812(10)
   - eq:3 nets T:19~30°C I:-0.05~1.15M max 1n/0e
**16. UO_[2]^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_195 + ligand_6277) — ligand_def_HxL: H4L | 10 ent, 6 sp, 10 vlms (vlm_108542…vlm_108551)
   - species: beta_def_502(2) beta_def_536(1) beta_def_570(1) beta_def_662(1) beta_def_699(1) beta_def_779(4)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 6n/13e
**17. Th^[4+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_185 + ligand_6277) — ligand_def_HxL: H4L | 10 ent, 4 sp, 10 vlms (vlm_108521…vlm_108530)
   - species: beta_def_423(2) beta_def_788(3) beta_def_812(4) beta_def_966(1)
   - eq:3 nets T:15~30°C I:-0.05~0.65M max 4n/6e
**18. Sm^[3+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_173 + ligand_6277) — ligand_def_HxL: H4L | 10 ent, 2 sp, 10 vlms (vlm_108428…vlm_108437)
   - species: beta_def_788(1) beta_def_812(9)
   - eq:3 nets T:19~30°C I:-0.05~1.15M max 1n/0e
**19. Sr^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_177 + ligand_6277) — ligand_def_HxL: H4L | 9 ent, 2 sp, 9 vlms (vlm_108362…vlm_108370)
   - species: beta_def_788(1) beta_def_812(8)
   - eq:2 nets T:20~41°C I:-0.05~0.3M max 2n/1e
**20. Na^[+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_106 + ligand_6277) — ligand_def_HxL: H4L | 9 ent, 1 sp, 9 vlms (vlm_108307…vlm_108315)
   - species: beta_def_812(9)
   - eq:3 nets T:19~30°C I:-0.05~1.15M max 1n/0e

---

### Step 19: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_41 AND c.ligand_id = ligand_6277 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 24.5 AND 25.5 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.1))",
  "order_by": "s.ionic_strength_mol_l ASC, s.temperature_c ASC",
  "limit": 5
}
```

[summary]
## search_stability — 4 row(s)

### `Cu^[2+]` + Ethylenedinitrilotetraacetic acid (EDTA) — 4 measurement(s)
metal_id: metal_41 | ligand_id: ligand_6277
ligand_HxL_def: H4L | ligand_SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_108605 | *** | beta_def_812 | ΔH | -33.1 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108604 | ref_eq_map_5019 | beta_def_812 | logK | 18.78 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108606 | *** | beta_def_812 | ΔH | -34.3 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108611 | *** | beta_def_812 | ΔS | 244.8 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |

---

### Step 20: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND c.ligand_id = ligand_6277 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 24.5 AND 25.5 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.1))",
  "order_by": "s.ionic_strength_mol_l ASC, s.temperature_c ASC",
  "limit": 5
}
```

[summary]
## search_stability — 4 row(s)

### `Zn^[2+]` + Ethylenedinitrilotetraacetic acid (EDTA) — 4 measurement(s)
metal_id: metal_208 | ligand_id: ligand_6277
ligand_HxL_def: H4L | ligand_SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_108710 | ref_eq_map_5053 | beta_def_812 | logK | 18 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108707 | ref_eq_map_5050 | beta_def_812 | logK | 16.5 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108711 | *** | beta_def_812 | ΔH | -19.7 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108712 | *** | beta_def_812 | ΔS | 250.2 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |

---

### Step 21: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_112 AND c.ligand_id = ligand_6277 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 24.5 AND 25.5 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.1))",
  "order_by": "s.ionic_strength_mol_l ASC, s.temperature_c ASC",
  "limit": 5
}
```

[summary]
## search_stability — 4 row(s)

### `Ni^[2+]` + Ethylenedinitrilotetraacetic acid (EDTA) — 4 measurement(s)
metal_id: metal_112 | ligand_id: ligand_6277
ligand_HxL_def: H4L | ligand_SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_108586 | *** | beta_def_812 | ΔH | -30.1 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108585 | ref_eq_map_5017 | beta_def_812 | logK | 18.4 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108587 | *** | beta_def_812 | ΔH | -31.4 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108592 | *** | beta_def_812 | ΔS | 247.3 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |

---

### Step 22: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_33 AND c.ligand_id = ligand_6277 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 24.5 AND 25.5 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.1))",
  "order_by": "s.ionic_strength_mol_l ASC, s.temperature_c ASC",
  "limit": 5
}
```

[summary]
## search_stability — 4 row(s)

### `Co^[2+]` + Ethylenedinitrilotetraacetic acid (EDTA) — 4 measurement(s)
metal_id: metal_33 | ligand_id: ligand_6277
ligand_HxL_def: H4L | ligand_SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_108573 | *** | beta_def_812 | ΔH | -15.9 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108572 | ref_eq_map_5015 | beta_def_812 | logK | 16.45 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108574 | *** | beta_def_812 | ΔH | -17.2 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108579 | *** | beta_def_812 | ΔS | 257.7 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |

---

### Step 23: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_26 AND c.ligand_id = ligand_6277 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 24.5 AND 25.5 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.1))",
  "order_by": "s.ionic_strength_mol_l ASC, s.temperature_c ASC",
  "limit": 5
}
```

[summary]
## search_stability — 5 row(s)

### `Cd^[2+]` + Ethylenedinitrilotetraacetic acid (EDTA) — 5 measurement(s)
metal_id: metal_26 | ligand_id: ligand_6277
ligand_HxL_def: H4L | ligand_SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_108728 | ref_eq_map_5058 | beta_def_812 | logK | 18.1 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108729 | *** | beta_def_812 | ΔH | -36.8 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108735 | *** | beta_def_812 | ΔS | 224.7 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108725 | ref_eq_map_5055 | beta_def_812 | logK | 16.5 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108730 | *** | beta_def_812 | ΔH | -38.1 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |

---

### Step 24: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND c.ligand_id = ligand_6277 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 24.5 AND 25.5 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.1))",
  "order_by": "s.ionic_strength_mol_l ASC, s.temperature_c ASC",
  "limit": 5
}
```

[summary]
## search_stability — 3 row(s)

### `Fe^[3+]` + Ethylenedinitrilotetraacetic acid (EDTA) — 3 measurement(s)
metal_id: metal_61 | ligand_id: ligand_6277
ligand_HxL_def: H4L | ligand_SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_108639 | ref_eq_map_5028 | beta_def_812 | logK | 25.1 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108641 | *** | beta_def_812 | ΔH | -11.3 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108642 | *** | beta_def_812 | ΔS | 442.7 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |

---

### Step 25: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_5 AND c.ligand_id = ligand_6277 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 24.5 AND 25.5 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.1))",
  "order_by": "s.ionic_strength_mol_l ASC, s.temperature_c ASC",
  "limit": 5
}
```

[summary]
## search_stability — 2 row(s)

### `Al^[3+]` + Ethylenedinitrilotetraacetic acid (EDTA) — 2 measurement(s)
metal_id: metal_5 | ligand_id: ligand_6277
ligand_HxL_def: H4L | ligand_SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_108770 | ref_eq_map_5067 | beta_def_812 | logK | 16.4 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108772 | *** | beta_def_812 | ΔS | 491.2 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |

---

### Step 26: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_25 AND c.ligand_id = ligand_6277 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 24.5 AND 25.5 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.1))",
  "order_by": "s.ionic_strength_mol_l ASC, s.temperature_c ASC",
  "limit": 5
}
```

[summary]
## search_stability — 5 row(s)

### `Ca^[2+]` + Ethylenedinitrilotetraacetic acid (EDTA) — 5 measurement(s)
metal_id: metal_25 | ligand_id: ligand_6277
ligand_HxL_def: H4L | ligand_SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_108350 | *** | beta_def_812 | ΔH | -22.2 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108344 | ref_eq_map_4932 | beta_def_812 | logK | 10.65 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108345 | ref_eq_map_4934 | beta_def_812 | logK | 10.81 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108352 | *** | beta_def_812 | ΔH | -25.5 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108356 | *** | beta_def_812 | ΔS | 118.4 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |

---

### Step 27: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_92 AND c.ligand_id = ligand_6277 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 24.5 AND 25.5 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.1))",
  "order_by": "s.ionic_strength_mol_l ASC, s.temperature_c ASC",
  "limit": 5
}
```

[summary]
## search_stability — 5 row(s)

### `Mg^[2+]` + Ethylenedinitrilotetraacetic acid (EDTA) — 5 measurement(s)
metal_id: metal_92 | ligand_id: ligand_6277
ligand_HxL_def: H4L | ligand_SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_108332 | *** | beta_def_812 | ΔH | 18 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108326 | ref_eq_map_4926 | beta_def_812 | logK | 8.79 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108327 | ref_eq_map_4928 | beta_def_812 | logK | 8.96 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108334 | *** | beta_def_812 | ΔH | 14.2 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108338 | *** | beta_def_812 | ΔS | 216.3 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |

---

### Step 28: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.ligand_id = ligand_6277 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 24.5 AND 25.5 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.1))",
  "order_by": "s.ionic_strength_mol_l ASC, s.temperature_c ASC",
  "limit": 5
}
```

[summary]
## search_stability — 2 row(s)

### `Hg^[2+]` + Ethylenedinitrilotetraacetic acid (EDTA) — 2 measurement(s)
metal_id: metal_71 | ligand_id: ligand_6277
ligand_HxL_def: H4L | ligand_SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_108748 | ref_eq_map_5060 | beta_def_812 | logK | 21.5 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108752 | *** | beta_def_812 | ΔS | 146.4 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |

---

### Step 29: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_79 AND c.ligand_id = ligand_6277 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 24.5 AND 25.5 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.1))",
  "order_by": "s.ionic_strength_mol_l ASC, s.temperature_c ASC",
  "limit": 5
}
```

[summary]
## search_stability — 3 row(s)

### `La^[3+]` + Ethylenedinitrilotetraacetic acid (EDTA) — 3 measurement(s)
metal_id: metal_79 | ligand_id: ligand_6277
ligand_HxL_def: H4L | ligand_SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_108389 | ref_eq_map_4946 | beta_def_812 | logK | 15.36 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108391 | *** | beta_def_812 | ΔH | -12.1 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108396 | *** | beta_def_812 | ΔS | 253.6 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |

---

### Step 30: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_195 AND c.ligand_id = ligand_6277 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 24.5 AND 25.5 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.1))",
  "order_by": "s.ionic_strength_mol_l ASC, s.temperature_c ASC",
  "limit": 5
}
```

[summary]
## search_stability

*(no results)*

---
