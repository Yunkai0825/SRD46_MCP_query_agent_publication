# Q2.1.2 — Tool Results (batch 1)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "manganese, iron, cobalt, nickel, copper, zinc",
  "limit": 50
}
```

[summary]
## search_metals

*(no results)*

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "ammonia",
  "limit": 50
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 50

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_10103 | Ammonia | L | Inorganic ligands | 447 | `N` | (-inf, HL, 9.26, L, +inf) |

---

### Step 4: `search_metals`
**Args:**
```json
{
  "symbol": "Mn, Fe, Co, Ni, Cu, Zn",
  "limit": 100
}
```

[summary]
## search_metals

*(no results)*

---

### Step 6: `build_system_catalog`
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

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_10103 AND c.beta_definition_id = beta_def_812 AND c.metal_id IN (metal_94, metal_62, metal_33, metal_112, metal_41, metal_208) AND (s.solvent_name LIKE '%water%' OR s.solvent_name IS NULL) AND s.temperature_c BETWEEN 20 AND 30 AND s.ionic_strength_mol_l BETWEEN 0.0 AND 0.2 AND (s.electrolyte_composition IS NULL OR s.electrolyte_composition NOT LIKE '%NH4%'))",
  "order_by": "c.metal_id, s.temperature_c ASC, s.ionic_strength_mol_l ASC",
  "limit": 300
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
  "where": "(c.ligand_id = ligand_10103 AND c.beta_definition_id = beta_def_812 AND c.metal_id IN (metal_94, metal_62, metal_33, metal_112, metal_41, metal_208))",
  "order_by": "c.metal_id, s.temperature_c ASC",
  "limit": 1000
}
```

[summary]
## search_stability — 53 row(s)

### logK — 6 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_62 | Fe^[2+] | ligand_10103 | Ammonia | L | N | 6 | 1 | 25 | 0~6 | *** | 6 |
| metal_94 | Mn^[2+] | ligand_10103 | Ammonia | L | N | 6 | 1 | 25 | 0~5 | *** | 6 |
| metal_33 | Co^[2+] | ligand_10103 | Ammonia | L | N | 5 | 1 | 25 | 0~5 | *** | 5 |
| metal_41 | Cu^[2+] | ligand_10103 | Ammonia | L | N | 5 | 1 | 25 | 0~3 | *** | 5 |
| metal_112 | Ni^[2+] | ligand_10103 | Ammonia | L | N | 4 | 1 | 25 | 0~2 | *** | 4 |
| metal_208 | Zn^[2+] | ligand_10103 | Ammonia | L | N | 4 | 1 | 25 | 0~2 | *** | 4 |

### ΔH — 6 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_41 | Cu^[2+] | ligand_10103 | Ammonia | L | N | 4 | 1 | 25 | 0~3 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_10103 | Ammonia | L | N | 4 | 1 | 25 | 0~3 | *** | 0 |
| metal_33 | Co^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 2 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 2 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 2 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 27 | 2 | *** | 0 |

### ΔS — 6 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_41 | Cu^[2+] | ligand_10103 | Ammonia | L | N | 4 | 1 | 25 | 0~3 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_10103 | Ammonia | L | N | 3 | 1 | 25 | 0~2 | *** | 0 |
| metal_33 | Co^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 2 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 2 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 2 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 2 | *** | 0 |

---
