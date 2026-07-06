# Q2.1.2 — Tool Results (batch 3)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "manganese, iron, cobalt, nickel, copper, zinc",
  "limit": 10
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

### Step 4: `search_metals`
**Args:**
```json
{
  "symbol": "Mn, Fe, Co, Ni, Cu, Zn",
  "limit": 10
}
```

[summary]
## search_metals

*(no results)*

---

### Step 5: `build_system_catalog`
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

### Step 7: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_10103 AND c.beta_definition_id = beta_def_812 AND c.metal_id IN (metal_94, metal_62, metal_33, metal_112, metal_41, metal_208) AND s.solvent_name = 'water' AND s.temperature_c >= 24 AND s.temperature_c <= 26)",
  "order_by": "c.metal_id ASC, s.ionic_strength_mol_l ASC, s.constant_value ASC",
  "limit": 100
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
  "where": "(c.ligand_id = ligand_10103 AND c.beta_definition_id = beta_def_812 AND c.metal_id IN (metal_94, metal_62, metal_33, metal_112, metal_41, metal_208) AND s.temperature_c >= 24 AND s.temperature_c <= 26)",
  "order_by": "c.metal_id ASC, s.solvent_name ASC, s.ionic_strength_mol_l ASC, s.constant_value ASC",
  "limit": 100
}
```

[summary]
## search_stability — 52 row(s)

### logK — 6 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_62 | Fe^[2+] | ligand_10103 | Ammonia | L | N | 6 | 1 | 25 | 0~6 | *** | 6 |
| metal_94 | Mn^[2+] | ligand_10103 | Ammonia | L | N | 6 | 1 | 25 | 0~5 | *** | 6 |
| metal_33 | Co^[2+] | ligand_10103 | Ammonia | L | N | 5 | 1 | 25 | 0~5 | *** | 5 |
| metal_41 | Cu^[2+] | ligand_10103 | Ammonia | L | N | 5 | 1 | 25 | 0~3 | *** | 5 |
| metal_112 | Ni^[2+] | ligand_10103 | Ammonia | L | N | 4 | 1 | 25 | 0~2 | *** | 4 |
| metal_208 | Zn^[2+] | ligand_10103 | Ammonia | L | N | 4 | 1 | 25 | 0~2 | *** | 4 |

### ΔH — 5 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_41 | Cu^[2+] | ligand_10103 | Ammonia | L | N | 4 | 1 | 25 | 0~3 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_10103 | Ammonia | L | N | 4 | 1 | 25 | 0~3 | *** | 0 |
| metal_33 | Co^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 2 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 2 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 2 | *** | 0 |

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

### Step 9: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_10103 AND c.beta_definition_id = beta_def_812 AND c.metal_id IN (metal_94, metal_62, metal_33, metal_112, metal_41, metal_208) AND s.temperature_c = 25 AND s.ionic_strength_mol_l = 2 AND s.constant_type = 'logK')",
  "order_by": "c.metal_id ASC, s.constant_value ASC",
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
  "where": "(c.ligand_id = ligand_10103 AND c.beta_definition_id = beta_def_812 AND c.metal_id IN (metal_94, metal_62, metal_33, metal_112, metal_41, metal_208) AND s.temperature_c = 25 AND s.constant_type = 'logK')",
  "order_by": "c.metal_id ASC, s.ionic_strength_mol_l ASC, s.constant_value ASC",
  "limit": 200
}
```

[summary]
## search_stability

*(no results)*

---

### Step 11: `inspect_card`
**Args:**
```json
{
  "prefix_id": "metal_94"
}
```

[summary]
## inspect_card — Metal | metal_94

**Name:** Mn^[2+]  
**Symbol:** Mn | **Charge:** 2  
**SMILES:** `[Mn+2]`  
**InChI:** `InChI=1S/Mn/q+2`  
**Flags:** simple-ion  

**Partners:** 486 ligand(s), 1273 measurement(s) total

| ligand_id | Ligand | # meas |
|-----------|--------|--------|
| ligand_10103 | Ammonia | 32 |
| ligand_5760 | Aminoacetic acid (Glycine) | 14 |
| ligand_10109 | Nitrate ion | 12 |
| ligand_10076 | Hydroxide ion | 12 |
| ligand_5819 | L-2-Amino-3-(4-hydroxyphenyl)propanoic acid (Tyrosine) | 12 |
| … | *(showing top 5 of 486)* | |

### Functional groups across all ligand partners (474 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 270 | 57% |
| aromatic_ring | 180 | 38% |
| hydroxyl | 171 | 36% |
| tertiary_amine | 157 | 33% |
| primary_amine | 102 | 22% |
| ether | 72 | 15% |
| secondary_amine | 59 | 12% |
| pyridine | 55 | 12% |
| amide | 52 | 11% |
| phosphate | 47 | 10% |
| phenol | 40 | 8% |
| phosphonate | 35 | 7% |
| thioether | 27 | 6% |
| ketone | 16 | 3% |
| sulfonate | 13 | 3% |
| halide | 10 | 2% |
| thiol | 7 | 1% |
| imine | 5 | 1% |
| ester | 4 | 1% |
| imidazole | 4 | 1% |
| pyrazole | 4 | 1% |
| aldehyde | 3 | 1% |
| nitrile | 2 | 0% |
| oxime | 1 | 0% |

---

### Step 12: `search_networks`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_10103 AND nd.beta_definition_id = beta_def_812 AND c.metal_id IN (metal_94, metal_62, metal_33, metal_112, metal_41, metal_208))",
  "order_by": "c.metal_id ASC",
  "limit": 50
}
```

[summary]
## search_networks — 113 row(s)

> **Reference equilibrium networks (compact)** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### Beta-definition legend
| beta_def | equation |
|----------|----------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |
| beta_def_872 | ``[M] + [L]^3 <=> [ML3]`` |
| beta_def_894 | ``[M] + [L]^4 <=> [ML4]`` |
| beta_def_903 | ``[M] + [L]^5 <=> [ML5]`` |
| beta_def_907 | ``[M] + [L]^6 <=> [ML6]`` |

### Metal-ligand pair summary
| metal | metal_id | ligand | ligand_id | HxL | T_range | I_range | net_count | max_nodes | ligand_SMILES |
|-------|----------|--------|-----------|-----|---------|---------|-----------|----------|---------------|
| `Co^[2+]` | metal_33 | Ammonia | ligand_10103 | L | 19~35 | -0.15~5.15 | 5 | 5 | N |
| `Cu^[2+]` | metal_41 | Ammonia | ligand_10103 | L | 19~30 | -0.15~3.15 | 5 | 4 | N |
| `Fe^[2+]` | metal_62 | Ammonia | ligand_10103 | L | 19~30 | -0.05~6.15 | 6 | 4 | N |
| `Mn^[2+]` | metal_94 | Ammonia | ligand_10103 | L | 19~30 | -0.05~5.15 | 6 | 4 | N |
| `Ni^[2+]` | metal_112 | Ammonia | ligand_10103 | L | 19~30 | -0.15~2.15 | 4 | 6 | N |
| `Zn^[2+]` | metal_208 | Ammonia | ligand_10103 | L | 19~30 | -0.15~2.15 | 4 | 4 | N |

### Max-node network per pair
| metal | metal_id | ligand | ligand_id | max_net_id | max_nodes | max_edge_counts | max_T_range | max_I_range | max_vlm_counts | max_beta_def_ids | max_type | max_values |
|-------|----------|--------|----------|------------|-----------|------------------|-------------|-------------|----------------|------------------|----------|------------|
| `Co^[2+]` | metal_33 | Ammonia | ligand_10103 | ref_eq_net_28231 | 5 | 10 | 20~30 | -0.05~0.25 | 5 | 5 diff beta_def | logK | 2.08~5.13 |
| `Cu^[2+]` | metal_41 | Ammonia | ligand_10103 | ref_eq_net_28241 | 4 | 6 | 20~30 | -0.05~0.25 | 4 | 4 diff beta_def | logK | 4.1~12.3 |
| `Fe^[2+]` | metal_62 | Ammonia | ligand_10103 | ref_eq_net_28225 | 4 | 6 | 20~30 | -0.05~0.25 | 4 | 4 diff beta_def | logK | 1.4~2.75 |
| `Mn^[2+]` | metal_94 | Ammonia | ligand_10103 | ref_eq_net_28219 | 4 | 6 | 20~30 | -0.05~0.25 | 4 | 4 diff beta_def | logK | 0.84~1.38 |
| `Ni^[2+]` | metal_112 | Ammonia | ligand_10103 | ref_eq_net_28236 | 6 | 15 | 20~30 | -0.05~0.25 | 6 | 6 diff beta_def | logK | 2.73~8.33 |
| `Zn^[2+]` | metal_208 | Ammonia | ligand_10103 | ref_eq_net_28282 | 4 | 6 | 20~30 | -0.05~0.25 | 4 | 4 diff beta_def | logK | 2.33~8.89 |

### Global max-node network: `Ni^[2+]` + Ammonia
network_id: ref_eq_net_28236 | metal_id: metal_112 | ligand_id: ligand_10103 | ligand_def_HxL: L | nodes: 6

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 2.73 |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` | logK | 4.89 |
| beta_def_872 | ``[M] + [L]^3 <=> [ML3]`` | logK | 6.54 |
| beta_def_894 | ``[M] + [L]^4 <=> [ML4]`` | logK | 7.67 |
| beta_def_907 | ``[M] + [L]^6 <=> [ML6]`` | logK | 8.3 |
| beta_def_903 | ``[M] + [L]^5 <=> [ML5]`` | logK | 8.33 |

---
