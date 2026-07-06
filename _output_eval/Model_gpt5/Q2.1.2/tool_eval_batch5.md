# Q2.1.2 — Tool Results (batch 5)

### Step 2: `search_metals`
**Args:**
```json
{
  "symbol": "Mn",
  "limit": 5
}
```

[summary]
## search_metals — 4 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_94 | Mn^[2+] | Mn | 2 | ✓ | [Mn+2] | InChI=1S/Mn/q+2 | beta_totN_44 | ligand_totN_486 | vlm_totN_1273 |
| metal_95 | Mn^[3+] | Mn | 3 | ✓ | [Mn+3] | InChI=1S/Mn/q+3 | beta_totN_8 | ligand_totN_12 | vlm_totN_26 |
| metal_96 | Mn^[4+] | Mn | 4 | ✓ | [Mn+4] | InChI=1S/Mn/q+4 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_97 | MeNH_[3]^[+] | MNH3 | 1 |  | *** | *** | beta_totN_1 | ligand_totN_5 | vlm_totN_9 |

---

### Step 3: `search_metals`
**Args:**
```json
{
  "symbol": "Fe",
  "limit": 5
}
```

[summary]
## search_metals — 2 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_61 | Fe^[3+] | Fe | 3 | ✓ | [Fe+3] | InChI=1S/Fe/q+3 | beta_totN_128 | ligand_totN_406 | vlm_totN_1473 |
| metal_62 | Fe^[2+] | Fe | 2 | ✓ | [Fe+2] | InChI=1S/Fe/q+2 | beta_totN_57 | ligand_totN_217 | vlm_totN_667 |

---

### Step 4: `search_metals`
**Args:**
```json
{
  "symbol": "Co",
  "limit": 5
}
```

[summary]
## search_metals — 3 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_33 | Co^[2+] | Co | 2 | ✓ | [Co+2] | InChI=1S/Co/q+2 | beta_totN_92 | ligand_totN_977 | vlm_totN_2977 |
| metal_34 | Co^[3+] | Co | 3 | ✓ | [Co+3] | InChI=1S/Co/q+3 | beta_totN_20 | ligand_totN_19 | vlm_totN_55 |
| metal_181 | TcO^[2+] | Tc | 2 |  | *** | *** | beta_totN_2 | ligand_totN_1 | vlm_totN_2 |

---

### Step 5: `search_metals`
**Args:**
```json
{
  "symbol": "Ni",
  "limit": 5
}
```

[summary]
## search_metals — 2 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_112 | Ni^[2+] | Ni | 2 | ✓ | [Ni+2] | InChI=1S/Ni/q+2 | beta_totN_149 | ligand_totN_1369 | vlm_totN_5325 |
| metal_113 | Ni^[3+] | Ni | 3 | ✓ | [Ni+3] | InChI=1S/Ni/q+3 | beta_totN_5 | ligand_totN_4 | vlm_totN_7 |

---

### Step 6: `search_metals`
**Args:**
```json
{
  "symbol": "Cu",
  "limit": 5
}
```

[summary]
## search_metals — 3 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_41 | Cu^[2+] | Cu | 2 | ✓ | [Cu+2] | InChI=1S/Cu/q+2 | beta_totN_264 | ligand_totN_1951 | vlm_totN_8963 |
| metal_42 | Cu^[+] | Cu | 1 | ✓ | [Cu+] | InChI=1S/Cu/q+1 | beta_totN_32 | ligand_totN_117 | vlm_totN_285 |
| metal_43 | Cu^[3+] | Cu | 3 | ✓ | [Cu+3] | InChI=1S/Cu/q+3 | beta_totN_4 | ligand_totN_8 | vlm_totN_10 |

---

### Step 7: `search_metals`
**Args:**
```json
{
  "symbol": "Zn",
  "limit": 5
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_208 | Zn^[2+] | Zn | 2 | ✓ | [Zn+2] | InChI=1S/Zn/q+2 | beta_totN_122 | ligand_totN_1169 | vlm_totN_4095 |

---

### Step 8: `search_ligands`
**Args:**
```json
{
  "name": "ammonia",
  "limit": 10
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_10103 | Ammonia | L | Inorganic ligands | 447 | `N` | (-inf, HL, 9.26, L, +inf) |

---

### Step 9: `build_system_catalog`
**Args:**
```json
{
  "ligand_id": "ligand_10103"
}
```

[summary]
[CATALOG]
## build_system_catalog — 20 pair(s), 77 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_79 | [L] + [H] <=> [HL] |  |
| beta_def_249 | [M(OH)2L2] + [H] <=> [M(OH)L2] + [H2O] |  |
| beta_def_270 | [M(OH)3L2] + [H] <=> [M(OH)2L2] + [H2O] |  |
| beta_def_812 | [M] + [L] <=> [ML] |  |
| beta_def_840 | [M] + [L]^2 <=> [ML2] |  |
| beta_def_872 | [M] + [L]^3 <=> [ML3] |  |
| beta_def_882 | [H] + [M(OH)L3(fac)] <=> [ML3] + [H2O] |  |
| beta_def_894 | [M] + [L]^4 <=> [ML4] |  |
| beta_def_895 | [H] + [M(OH)L4(cis)] <=> [ML4] + [H2O] |  |
| beta_def_896 | [H] + [M(OH)L4(trans)] <=> [ML4] + [H2O] |  |
| beta_def_903 | [M] + [L]^5 <=> [ML5] |  |
| beta_def_904 | [M(OH)L5] + [H] <=> [ML5] + [H2O] |  |
| beta_def_905 | [ML4] + [L] <=> [ML5] |  |
| beta_def_906 | *** |  |
| beta_def_907 | [M] + [L]^6 <=> [ML6] |  |
| beta_def_909 | [ML5] + [L] <=> [ML6] |  |
| beta_def_966 | [M(OH)L] + [H] <=> [ML] + [H2O] |  |
| beta_def_984 | [M(OH)L2] + [H] <=> [ML2] + [H2O] |  |
| beta_def_991 | [H] + [M(OH)2L3(fac)] <=> [M(OH)L3] + [H2O] |  |
| beta_def_993 | [H] + [M(OH)2L4(cis)] <=> [M(OH)L4] + [H2O] |  |
| beta_def_994 | [H] + [M(OH)2L4(trans)] <=> [M(OH)L4] + [H2O] |  |

*(all species aqueous unless noted)*

**1. Ni^[2+] + Ammonia** (metal_112 + ligand_10103) — ligand_def_HxL: L | 60 ent, 6 sp, 60 vlms (vlm_173182…vlm_173241)
   - species: beta_def_812(11) beta_def_840(13) beta_def_872(10) beta_def_894(10) beta_def_903(8) beta_def_907(8)
   - eq:5 nets T:19~30°C I:-0.15~3.15M max 6n/15e
**2. Cu^[2+] + Ammonia** (metal_41 + ligand_10103) — ligand_def_HxL: L | 49 ent, 4 sp, 49 vlms (vlm_173242…vlm_173290)
   - species: beta_def_812(13) beta_def_840(12) beta_def_872(12) beta_def_894(12)
   - eq:5 nets T:19~30°C I:-0.15~3.15M max 4n/6e
**3. Cd^[2+] + Ammonia** (metal_26 + ligand_10103) — ligand_def_HxL: L | 49 ent, 4 sp, 49 vlms (vlm_173415…vlm_173463)
   - species: beta_def_812(13) beta_def_840(12) beta_def_872(12) beta_def_894(12)
   - eq:5 nets T:19~30°C I:-0.15~3.15M max 4n/6e
**4. Ag^[+] + Ammonia** (metal_2 + ligand_10103) — ligand_def_HxL: L | 47 ent, 2 sp, 47 vlms (vlm_173338…vlm_173384)
   - species: beta_def_812(22) beta_def_840(25)
   - eq:16 nets T:19~30°C I:-0.05~5.15M max 2n/1e
**5. H^[+] + Ammonia** (metal_68 + ligand_10103) — ligand_def_HxL: L | 35 ent, 1 sp, 35 vlms (vlm_173034…vlm_173068)
   - species: beta_def_79(35)
   - eq:20 nets T:5~45°C I:-0.15~10.15M max 1n/0e
**6. Mn^[2+] + Ammonia** (metal_94 + ligand_10103) — ligand_def_HxL: L | 32 ent, 4 sp, 32 vlms (vlm_173099…vlm_173130)
   - species: beta_def_812(8) beta_def_840(8) beta_def_872(8) beta_def_894(8)
   - eq:6 nets T:19~30°C I:-0.05~5.15M max 4n/6e
**7. Fe^[2+] + Ammonia** (metal_62 + ligand_10103) — ligand_def_HxL: L | 32 ent, 4 sp, 32 vlms (vlm_173131…vlm_173162)
   - species: beta_def_812(8) beta_def_840(8) beta_def_872(8) beta_def_894(8)
   - eq:6 nets T:19~30°C I:-0.05~6.15M max 4n/6e
**8. Zn^[2+] + Ammonia** (metal_208 + ligand_10103) — ligand_def_HxL: L | 21 ent, 4 sp, 21 vlms (vlm_173394…vlm_173414)
   - species: beta_def_812(6) beta_def_840(5) beta_def_872(5) beta_def_894(5)
   - eq:4 nets T:19~30°C I:-0.15~2.15M max 4n/6e
**9. Co^[2+] + Ammonia** (metal_33 + ligand_10103) — ligand_def_HxL: L | 19 ent, 5 sp, 19 vlms (vlm_173163…vlm_173181)
   - species: beta_def_812(7) beta_def_840(3) beta_def_872(3) beta_def_894(3) beta_def_903(3)
   - eq:5 nets T:19~35°C I:-0.15~5.15M max 5n/10e
**10. Cr^[3+] + Ammonia** (metal_37 + ligand_10103) — ligand_def_HxL: L | 14 ent, 12 sp, 14 vlms (vlm_173291…vlm_173304)
   - species: beta_def_249(1) beta_def_270(1) beta_def_895(1) beta_def_896(1) beta_def_904(3) beta_def_905(1) beta_def_907(1) beta_def_909(1) beta_def_966(1) beta_def_984(1) beta_def_993(1) beta_def_994(1)
   - eq:3 nets T:12.5~31.5°C I:0.275~4.725M max 5n/10e
**11. Co^[3+] + Ammonia** (metal_34 + ligand_10103) — ligand_def_HxL: L | 14 ent, 8 sp, 14 vlms (vlm_173305…vlm_173318)
   - species: beta_def_882(1) beta_def_895(1) beta_def_905(3) beta_def_906(1) beta_def_907(2) beta_def_909(4) beta_def_991(1) beta_def_993(1)
   - eq:6 nets T:19~35°C I:-0.05~2.15M max 4n/6e
**12. Rh^[3+] + Ammonia** (metal_160 + ligand_10103) — ligand_def_HxL: L | 13 ent, 5 sp, 13 vlms (vlm_173319…vlm_173331)
   - species: beta_def_895(3) beta_def_896(3) beta_def_904(1) beta_def_993(3) beta_def_994(3)
   - eq:1 nets T:16.5~31.5°C I:0.775~1.225M max 5n/10e
**13. Hg^[2+] + Ammonia** (metal_71 + ligand_10103) — ligand_def_HxL: L | 12 ent, 4 sp, 12 vlms (vlm_173464…vlm_173475)
   - species: beta_def_812(1) beta_def_840(4) beta_def_872(3) beta_def_894(4)
   - eq:3 nets T:19~30°C I:-0.05~2.15M max 4n/6e
**14. Li^[+] + Ammonia** (metal_80 + ligand_10103) — ligand_def_HxL: L | 8 ent, 1 sp, 8 vlms (vlm_173069…vlm_173076)
   - species: beta_def_812(8)
   - eq:6 nets T:19~30°C I:-0.05~5.15M max 1n/0e
**15. Ca^[2+] + Ammonia** (metal_25 + ligand_10103) — ligand_def_HxL: L | 8 ent, 2 sp, 8 vlms (vlm_173083…vlm_173090)
   - species: beta_def_812(4) beta_def_840(4)
   - eq:4 nets T:19~30°C I:-0.05~2.15M max 2n/1e
**16. Mg^[2+] + Ammonia** (metal_92 + ligand_10103) — ligand_def_HxL: L | 6 ent, 3 sp, 6 vlms (vlm_173077…vlm_173082)
   - species: beta_def_812(1) beta_def_840(4) beta_def_872(1)
   - eq:2 nets T:19~30°C I:-0.05~2.15M max 3n/3e
**17. Cu^[+] + Ammonia** (metal_42 + ligand_10103) — ligand_def_HxL: L | 6 ent, 2 sp, 6 vlms (vlm_173332…vlm_173337)
   - species: beta_def_812(1) beta_def_840(5)
   - eq:6 nets T:13~30°C I:-0.05~2.15M max 1n/0e
**18. Sr^[2+] + Ammonia** (metal_177 + ligand_10103) — ligand_def_HxL: L | 4 ent, 1 sp, 4 vlms (vlm_173091…vlm_173094)
   - species: beta_def_812(4)
   - eq:4 nets T:19~30°C I:-0.05~2.15M max 1n/0e
**19. Pd^[2+] + Ammonia** (metal_127 + ligand_10103) — ligand_def_HxL: L | 4 ent, 4 sp, 4 vlms (vlm_173390…vlm_173393)
   - species: beta_def_812(1) beta_def_840(1) beta_def_872(1) beta_def_894(1)
   - eq:1 nets T:16.5~31.5°C I:0.775~1.225M max 4n/6e
**20. Ba^[2+] + Ammonia** (metal_18 + ligand_10103) — ligand_def_HxL: L | 4 ent, 1 sp, 4 vlms (vlm_173095…vlm_173098)
   - species: beta_def_812(4)
   - eq:4 nets T:19~30°C I:-0.05~2.15M max 1n/0e

---

### Step 10: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_94 AND c.ligand_id = ligand_10103 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 24 AND 26 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2)",
  "order_by": "s.ionic_strength_mol_l ASC, s.temperature_c ASC",
  "limit": 10
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. You must call 0_plan_search_strategy first (PHASE 2) before using the execution tools.

---

### Step 11: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_62 AND c.ligand_id = ligand_10103 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 24 AND 26 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2)",
  "order_by": "s.ionic_strength_mol_l ASC, s.temperature_c ASC",
  "limit": 10
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. You must call 0_plan_search_strategy first (PHASE 2) before using the execution tools.

---

### Step 12: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_33 AND c.ligand_id = ligand_10103 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 24 AND 26 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2)",
  "order_by": "s.ionic_strength_mol_l ASC, s.temperature_c ASC",
  "limit": 10
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. You must call 0_plan_search_strategy first (PHASE 2) before using the execution tools.

---

### Step 13: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_112 AND c.ligand_id = ligand_10103 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 24 AND 26 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2)",
  "order_by": "s.ionic_strength_mol_l ASC, s.temperature_c ASC",
  "limit": 10
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. You must call 0_plan_search_strategy first (PHASE 2) before using the execution tools.

---

### Step 14: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_41 AND c.ligand_id = ligand_10103 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 24 AND 26 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2)",
  "order_by": "s.ionic_strength_mol_l ASC, s.temperature_c ASC",
  "limit": 10
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. You must call 0_plan_search_strategy first (PHASE 2) before using the execution tools.

---

### Step 15: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_208 AND c.ligand_id = ligand_10103 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 24 AND 26 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2)",
  "order_by": "s.ionic_strength_mol_l ASC, s.temperature_c ASC",
  "limit": 10
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. You must call 0_plan_search_strategy first (PHASE 2) before using the execution tools.

---

### Step 17: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_94 AND c.ligand_id = ligand_10103 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 24 AND 26 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2) AND (s.solvent_name IS NULL OR s.solvent_name LIKE '%water%'))",
  "order_by": "s.ionic_strength_mol_l ASC, s.temperature_c ASC",
  "limit": 10
}
```

[summary]
## search_stability

*(no results)*

---

### Step 18: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_62 AND c.ligand_id = ligand_10103 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 24 AND 26 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2) AND (s.solvent_name IS NULL OR s.solvent_name LIKE '%water%'))",
  "order_by": "s.ionic_strength_mol_l ASC, s.temperature_c ASC",
  "limit": 10
}
```

[summary]
## search_stability

*(no results)*

---

### Step 19: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_33 AND c.ligand_id = ligand_10103 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 24 AND 26 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2) AND (s.solvent_name IS NULL OR s.solvent_name LIKE '%water%'))",
  "order_by": "s.ionic_strength_mol_l ASC, s.temperature_c ASC",
  "limit": 10
}
```

[summary]
## search_stability

*(no results)*

---

### Step 20: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_112 AND c.ligand_id = ligand_10103 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 24 AND 26 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2) AND (s.solvent_name IS NULL OR s.solvent_name LIKE '%water%'))",
  "order_by": "s.ionic_strength_mol_l ASC, s.temperature_c ASC",
  "limit": 10
}
```

[summary]
## search_stability

*(no results)*

---

### Step 21: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_41 AND c.ligand_id = ligand_10103 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 24 AND 26 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2) AND (s.solvent_name IS NULL OR s.solvent_name LIKE '%water%'))",
  "order_by": "s.ionic_strength_mol_l ASC, s.temperature_c ASC",
  "limit": 10
}
```

[summary]
## search_stability

*(no results)*

---

### Step 22: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND c.ligand_id = ligand_10103 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 24 AND 26 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2) AND (s.solvent_name IS NULL OR s.solvent_name LIKE '%water%'))",
  "order_by": "s.ionic_strength_mol_l ASC, s.temperature_c ASC",
  "limit": 10
}
```

[summary]
## search_stability

*(no results)*

---

### Step 23: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_94 AND c.ligand_id = ligand_10103 AND c.beta_definition_id = beta_def_812)",
  "order_by": "s.temperature_c ASC, s.ionic_strength_mol_l ASC",
  "limit": 5
}
```

[summary]
## search_stability — 5 row(s)

### `Mn^[2+]` + Ammonia — 5 measurement(s)
metal_id: metal_94 | ligand_id: ligand_10103
ligand_HxL_def: L | ligand_SMILES: N

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_173104 | ref_eq_map_28110 | beta_def_812 | logK | 0.84 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173099 | ref_eq_map_28111 | beta_def_812 | logK | 0.9 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173100 | ref_eq_map_28112 | beta_def_812 | logK | 0.97 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173105 | *** | beta_def_812 | ΔH | -5 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173106 | *** | beta_def_812 | ΔS | 1.7 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |

---

### Step 24: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_62 AND c.ligand_id = ligand_10103 AND c.beta_definition_id = beta_def_812)",
  "order_by": "s.temperature_c ASC, s.ionic_strength_mol_l ASC",
  "limit": 5
}
```

[summary]
## search_stability — 5 row(s)

### `Fe^[2+]` + Ammonia — 5 measurement(s)
metal_id: metal_62 | ligand_id: ligand_10103
ligand_HxL_def: L | ligand_SMILES: N

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_173136 | ref_eq_map_28116 | beta_def_812 | logK | 1.4 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173131 | ref_eq_map_28117 | beta_def_812 | logK | 1.53 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173137 | *** | beta_def_812 | ΔH | -7.9 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173138 | *** | beta_def_812 | ΔS | 2.5 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173132 | ref_eq_map_28118 | beta_def_812 | logK | 1.6 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |

---

### Step 25: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_33 AND c.ligand_id = ligand_10103 AND c.beta_definition_id = beta_def_812)",
  "order_by": "s.temperature_c ASC, s.ionic_strength_mol_l ASC",
  "limit": 5
}
```

[summary]
## search_stability — 5 row(s)

### `Co^[2+]` + Ammonia — 5 measurement(s)
metal_id: metal_33 | ligand_id: ligand_10103
ligand_HxL_def: L | ligand_SMILES: N

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_173167 | ref_eq_map_28126 | beta_def_812 | logK | 2.03 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173163 | ref_eq_map_28122 | beta_def_812 | logK | 2.08 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173164 | ref_eq_map_28125 | beta_def_812 | logK | 2.1 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173165 | ref_eq_map_28124 | beta_def_812 | logK | 2.14 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173168 | *** | beta_def_812 | ΔH | -13.4 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |

---

### Step 26: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_112 AND c.ligand_id = ligand_10103 AND c.beta_definition_id = beta_def_812)",
  "order_by": "s.temperature_c ASC, s.ionic_strength_mol_l ASC",
  "limit": 5
}
```

[summary]
## search_stability — 5 row(s)

### `Ni^[2+]` + Ammonia — 5 measurement(s)
metal_id: metal_112 | ligand_id: ligand_10103
ligand_HxL_def: L | ligand_SMILES: N

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_173185 | ref_eq_map_28130 | beta_def_812 | logK | 2.72 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173186 | *** | beta_def_812 | ΔH | -15.1 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173190 | *** | beta_def_812 | ΔS | 1.7 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173182 | ref_eq_map_28127 | beta_def_812 | logK | 2.73 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173183 | ref_eq_map_28129 | beta_def_812 | logK | 2.8 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |

---

### Step 27: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_41 AND c.ligand_id = ligand_10103 AND c.beta_definition_id = beta_def_812)",
  "order_by": "s.temperature_c ASC, s.ionic_strength_mol_l ASC",
  "limit": 5
}
```

[summary]
## search_stability — 5 row(s)

### `Cu^[2+]` + Ammonia — 5 measurement(s)
metal_id: metal_41 | ligand_id: ligand_10103
ligand_HxL_def: L | ligand_SMILES: N

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_173246 | ref_eq_map_28136 | beta_def_812 | logK | 4.02 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173247 | *** | beta_def_812 | ΔH | -20.1 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173251 | *** | beta_def_812 | ΔS | 9.6 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173242 | ref_eq_map_28132 | beta_def_812 | logK | 4.1 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173243 | ref_eq_map_28133 | beta_def_812 | logK | 4.12 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |

---

### Step 28: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND c.ligand_id = ligand_10103 AND c.beta_definition_id = beta_def_812)",
  "order_by": "s.temperature_c ASC, s.ionic_strength_mol_l ASC",
  "limit": 5
}
```

[summary]
## search_stability — 5 row(s)

### `Zn^[2+]` + Ammonia — 5 measurement(s)
metal_id: metal_208 | ligand_id: ligand_10103
ligand_HxL_def: L | ligand_SMILES: N

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_173397 | ref_eq_map_28175 | beta_def_812 | logK | 2.21 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173394 | ref_eq_map_28172 | beta_def_812 | logK | 2.33 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173395 | ref_eq_map_28173 | beta_def_812 | logK | 2.3 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173396 | ref_eq_map_28174 | beta_def_812 | logK | 2.41 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173399 | *** | beta_def_812 | ΔS | 9.6 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |

---
