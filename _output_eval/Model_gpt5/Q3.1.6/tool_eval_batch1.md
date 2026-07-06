# Q3.1.6 — Tool Results (batch 1)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "lanthanum",
  "limit": 10
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_79 | La^[3+] | La | 3 | ✓ | [La+3] | InChI=1S/La/q+3 | beta_totN_30 | ligand_totN_297 | vlm_totN_931 |

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "DTPA, EDTA, NTA, citrate, oxalate, tartrate, malonate, acetate, lactate, benzoate",
  "limit": 200
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
  "name": "diethylenetriaminepentaacetic acid, ethylenediaminetetraacetic acid, nitrilotriacetic acid, citric acid, oxalic acid, tartaric acid, malonic acid, acetic acid, lactic acid, benzoic acid",
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
  "metal_id": "metal_79"
}
```

[summary]
[CATALOG]
## build_system_catalog — 20 pair(s), 59 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_194 | [M] + [HL]^2 <=> [M(HL)2] |  |
| beta_def_352 | [ML3(s)] <=> [M] + [L]^3 | solid |
| beta_def_741 | [ML] + [H]^2 <=> [MH2L] |  |
| beta_def_779 | [M] + [HL] <=> [MHL] |  |
| beta_def_788 | [ML] + [H] <=> [MHL] |  |
| beta_def_792 | [ML2] + [H] <=> [MHL2] |  |
| beta_def_812 | [M] + [L] <=> [ML] |  |
| beta_def_840 | [M] + [L]^2 <=> [ML2] |  |
| beta_def_872 | [M] + [L]^3 <=> [ML3] |  |
| beta_def_894 | [M] + [L]^4 <=> [ML4] |  |
| beta_def_981 | [ML] + [OH] <=> [M(OH)L] |  |

*(all species aqueous unless noted)*

**1. La^[3+] + Propanedioic acid (Malonic acid)** (metal_79 + ligand_8873) — ligand_def_HxL: H2L | 20 ent, 4 sp, 20 vlms (vlm_152038…vlm_152057)
   - species: beta_def_779(4) beta_def_792(3) beta_def_812(8) beta_def_840(5)
   - eq:4 nets T:19~30°C I:-0.15~1.15M max 4n/4e
**2. La^[3+] + D-2,3-Dihydroxybutanedioic acid (D-Tartaric acid)** (metal_79 + ligand_8955) — ligand_def_HxL: H2L | 19 ent, 3 sp, 19 vlms (vlm_154960…vlm_154978)
   - species: beta_def_779(6) beta_def_812(7) beta_def_840(6)
   - eq:5 nets T:19~30°C I:-0.15~1.15M max 3n/3e
**3. La^[3+] + Hydroxyacetic acid (Glycolic acid)** (metal_79 + ligand_8640) — ligand_def_HxL: HL | 19 ent, 4 sp, 19 vlms (vlm_147101…vlm_147119)
   - species: beta_def_812(6) beta_def_840(5) beta_def_872(5) beta_def_894(3)
   - eq:4 nets T:19~30°C I:-0.05~2.15M max 4n/6e
**4. La^[3+] + 2-Hydroxy-2-methylpropanoic acid** (metal_79 + ligand_8647) — ligand_def_HxL: HL | 17 ent, 3 sp, 17 vlms (vlm_148045…vlm_148061)
   - species: beta_def_812(6) beta_def_840(6) beta_def_872(5)
   - eq:4 nets T:19~30°C I:-0.05~2.15M max 3n/3e
**5. La^[3+] + Ethanoic acid (Acetic acid)** (metal_79 + ligand_8465) — ligand_def_HxL: HL | 17 ent, 3 sp, 17 vlms (vlm_144473…vlm_144489)
   - species: beta_def_812(6) beta_def_840(6) beta_def_872(5)
   - eq:4 nets T:19~30°C I:-0.15~2.15M max 3n/3e
**6. La^[3+] + Pentane-2,4-dione (Acetylacetone)** (metal_79 + ligand_9526) — ligand_def_HxL: *** | 14 ent, 3 sp, 14 vlms (vlm_165187…vlm_165200)
   - species: beta_def_812(5) beta_def_840(5) beta_def_872(4)
   - eq:3 nets T:19~35°C I:-0.15~2.15M max 3n/3e
**7. La^[3+] + Hydrogen sulfate ion (Sulfuric acid)** (metal_79 + ligand_10148) — ligand_def_HxL: HL | 13 ent, 2 sp, 13 vlms (vlm_175723…vlm_175735)
   - species: beta_def_812(8) beta_def_840(5)
   - eq:4 nets T:19~30°C I:-0.05~2.15M max 2n/1e
**8. La^[3+] + D-2-Hydroxypropanoic acid (Lactic acid)** (metal_79 + ligand_8641) — ligand_def_HxL: HL | 13 ent, 3 sp, 13 vlms (vlm_147517…vlm_147529)
   - species: beta_def_812(5) beta_def_840(4) beta_def_872(4)
   - eq:3 nets T:15~30°C I:-0.05~2.15M max 3n/3e
**9. La^[3+] + Ethylenedinitrilo-N,N'-di(3-propanoic)-N,N'-diacetic acid** (metal_79 + ligand_6309) — ligand_def_HxL: H4L | 12 ent, 2 sp, 12 vlms (vlm_110121…vlm_110132)
   - species: beta_def_779(6) beta_def_812(6)
   - eq:2 nets T:19~30°C I:-0.05~0.65M max 2n/1e
**10. La^[3+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_79 + ligand_6277) — ligand_def_HxL: H4L | 12 ent, 2 sp, 12 vlms (vlm_108389…vlm_108400)
   - species: beta_def_788(3) beta_def_812(9)
   - eq:4 nets T:15~30°C I:-0.05~1.15M max 2n/1e
**11. La^[3+] + Oxydiacetic acid (Diglycolic acid)** (metal_79 + ligand_8974) — ligand_def_HxL: H2L | 11 ent, 3 sp, 11 vlms (vlm_155427…vlm_155437)
   - species: beta_def_812(4) beta_def_840(4) beta_def_872(3)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 3n/3e
**12. La^[3+] + Nitrilotriacetic acid (NTA)** (metal_79 + ligand_6165) — ligand_def_HxL: H3L | 11 ent, 3 sp, 11 vlms (vlm_105294…vlm_105304)
   - species: beta_def_812(6) beta_def_840(3) beta_def_981(2)
   - eq:3 nets T:15~30°C I:-0.05~0.65M max 3n/2e
**13. La^[3+] + Ethylenebis(oxyacetic acid)** (metal_79 + ligand_8986) — ligand_def_HxL: H2L | 10 ent, 4 sp, 10 vlms (vlm_155881…vlm_155890)
   - species: beta_def_792(3) beta_def_812(3) beta_def_840(3) beta_def_872(1)
   - eq:1 nets T:16.5~31.5°C I:0.775~1.225M max 4n/4e
**14. La^[3+] + Ethylenediiminodiacetic acid (EDDA)** (metal_79 + ligand_5975) — ligand_def_HxL: H2L | 10 ent, 4 sp, 10 vlms (vlm_100320…vlm_100329)
   - species: beta_def_741(1) beta_def_788(1) beta_def_812(4) beta_def_840(4)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 4n/4e
**15. La^[3+] + Pyridine-2,6-dicarboxylic acid (Dipicolinic acid)** (metal_79 + ligand_6774) — ligand_def_HxL: H2L | 9 ent, 3 sp, 9 vlms (vlm_119355…vlm_119363)
   - species: beta_def_812(3) beta_def_840(3) beta_def_872(3)
   - eq:1 nets T:16.5~31.5°C I:0.275~0.725M max 3n/3e
**16. La^[3+] + Pyridine-2-carboxylic acid (Picolinic acid)** (metal_79 + ligand_6762) — ligand_def_HxL: HL | 9 ent, 4 sp, 9 vlms (vlm_118694…vlm_118702)
   - species: beta_def_812(4) beta_def_840(2) beta_def_872(2) beta_def_894(1)
   - eq:2 nets T:19~30°C I:-0.05~0.65M max 4n/6e
**17. La^[3+] + Hydrogen fluoride (Hydrofluoric acid)** (metal_79 + ligand_10162) — ligand_def_HxL: HL | 8 ent, 2 sp, 8 vlms (vlm_176718…vlm_176725)
   - species: beta_def_352(2) beta_def_812(6)
   - eq:4 nets T:19~30°C I:-0.15~1.15M max 2n/1e
**18. La^[3+] + L-Hydroxybutanedioic acid (Hydroxysuccinic acid)(Malic acid)** (metal_79 + ligand_8953) — ligand_def_HxL: H2L | 8 ent, 3 sp, 8 vlms (vlm_154773…vlm_154780)
   - species: beta_def_779(2) beta_def_812(3) beta_def_840(3)
   - eq:3 nets T:19~30°C I:-0.05~1.15M max 3n/3e
**19. La^[3+] + Mercaptoacetic acid (Thioglycolic acid)** (metal_79 + ligand_8766) — ligand_def_HxL: H2L | 8 ent, 2 sp, 8 vlms (vlm_150501…vlm_150508)
   - species: beta_def_194(4) beta_def_779(4)
   - eq:2 nets T:19~30°C I:-0.05~2.15M max 2n/1e
**20. La^[3+] + 2-Methylpropanoic acid (Isobutyric acid)** (metal_79 + ligand_8473) — ligand_def_HxL: HL | 8 ent, 2 sp, 8 vlms (vlm_145441…vlm_145448)
   - species: beta_def_812(4) beta_def_840(4)
   - eq:2 nets T:16.5~31.5°C I:0.275~2.225M max 2n/1e

---

### Step 7: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_79 AND c.beta_definition_id = beta_def_812 AND (c.ligand_name_SRD LIKE '%ethylenedinitrilotetraacetic%' OR c.ligand_name_SRD LIKE '%EDTA%') AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 50
}
```

[summary]
## search_stability — 31 row(s)

### ΔS — 6 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_79 | La^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_79 | La^[3+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_79 | La^[3+] | ligand_6311 | Trimethylenedinitrilotetraa… | H4L | O=C(O)CN(CCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6335 | Oxybis(ethylenenitrilo)tetr… | H4L | O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6348 | Thiobis(ethylenenitrilo)tet… | H4L | O=C(O)CN(CCSCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6313 | Tetramethylenedinitrilotetr… | H4L | O=C(O)CN(CCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |

### ΔH — 6 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_79 | La^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 3 | 1 | 25 | 0.1~1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_79 | La^[3+] | ligand_6311 | Trimethylenedinitrilotetraa… | H4L | O=C(O)CN(CCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6335 | Oxybis(ethylenenitrilo)tetr… | H4L | O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6348 | Thiobis(ethylenenitrilo)tet… | H4L | O=C(O)CN(CCSCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6313 | Tetramethylenedinitrilotetr… | H4L | O=C(O)CN(CCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 0 |

### logK — 8 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_79 | La^[3+] | ligand_6311 | Trimethylenedinitrilotetraa… | H4L | O=C(O)CN(CCCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1 | *** | 2 |
| metal_79 | La^[3+] | ligand_6335 | Oxybis(ethylenenitrilo)tetr… | H4L | O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1 | *** | 2 |
| metal_79 | La^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 2 |
| metal_79 | La^[3+] | ligand_6348 | Thiobis(ethylenenitrilo)tet… | H4L | O=C(O)CN(CCSCCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1 | *** | 2 |
| metal_79 | La^[3+] | ligand_6313 | Tetramethylenedinitrilotetr… | H4L | O=C(O)CN(CCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1 | *** | 2 |
| metal_79 | La^[3+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 2 |
| metal_79 | La^[3+] | ligand_6314 | Pentamethylenedinitrilotetr… | H4L | O=C(O)CN(CCCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6315 | Hexamethylenedinitrilotetra… | H4L | O=C(O)CN(CCCCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 1 | *** | 1 |

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_79 AND c.beta_definition_id = beta_def_812 AND (c.ligand_name_SRD LIKE '%diethylenetriaminepentaacetic%' OR c.ligand_name_SRD LIKE '%DTPA%') AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 50
}
```

[summary]
## search_stability — 7 row(s)

### `La^[3+]` + Diethylenetrinitrilopentaacetic acid (DTPA) — 4 measurement(s)
metal_id: metal_79 | ligand_id: ligand_6356
ligand_HxL_def: H5L | ligand_SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_112571 | *** | beta_def_812 | ΔS | 298.7 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (-9.9, L, +inf) |
| vlm_112568 | ref_eq_map_6657 | beta_def_812 | logK | 19.49 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (-9.9, L, +inf) |
| vlm_112569 | ref_eq_map_6658 | beta_def_812 | logK | -18.23 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (-9.9, L, +inf) |
| vlm_112570 | *** | beta_def_812 | ΔH | -22.2 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (-9.9, L, +inf) |

### `La^[3+]` + Diethylenetrinitrilopentaacetic acid N,N"-bis(methylamide) … — 3 measurement(s)
metal_id: metal_79 | ligand_id: ligand_6362
ligand_HxL_def: *** | ligand_SMILES: ***

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_112948 | *** | beta_def_812 | ΔS | 221.3 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.37, L, +inf) |
| vlm_112946 | ref_eq_map_6789 | beta_def_812 | logK | 14.55 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.37, L, +inf) |
| vlm_112947 | *** | beta_def_812 | ΔH | -17.2 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.37, L, +inf) |

---

### Step 9: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_79 AND c.beta_definition_id = beta_def_812 AND c.ligand_name_SRD LIKE '%nitrilotriacetic%' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 50
}
```

[summary]
## search_stability — 25 row(s)

### ΔS — 3 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_79 | La^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_79 | La^[3+] | ligand_6267 | N-Methylethylenedinitrilotr… | H3L | CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_79 | La^[3+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |

### logK — 10 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_79 | La^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 2 |
| metal_79 | La^[3+] | ligand_6267 | N-Methylethylenedinitrilotr… | H3L | CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 2 |
| metal_79 | La^[3+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 2 |
| metal_79 | La^[3+] | ligand_6172 | DL-2-Methylnitrilotriacetic… | H3L | CC(C(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6178 | DL-2-Benzylnitrilotriacetic… | H3L | O=C(O)CN(CC(=O)O)C(Cc1ccccc1)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6272 | N-Benzylethylenedinitrilotr… | H3L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6173 | DL-2-Ethylnitrilotriacetic … | H3L | CCC(C(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6176 | DL-2-Hexylnitrilotriacetic … | H3L | CCCCCCC(C(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6174 | DL-2-Propylnitrilotriacetic… | H3L | CCCC(C(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6175 | DL-2-(2-Propyl)nitrilotriac… | H3L | CC(C)C(C(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |

### ΔH — 3 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_79 | La^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1~0.5 | *** | 0 |
| metal_79 | La^[3+] | ligand_6267 | N-Methylethylenedinitrilotr… | H3L | CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_79 | La^[3+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |

---

### Step 10: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_79 AND c.beta_definition_id = beta_def_812 AND (c.ligand_name_SRD LIKE '%citric%' OR c.ligand_name_SRD LIKE '%2-hydroxypropane-1,2,3-tricarboxylic%') AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 50
}
```

[summary]
## search_stability — 3 row(s)

### `La^[3+]` + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) — 3 measurement(s)
metal_id: metal_79 | ligand_id: ligand_9058
ligand_HxL_def: H3L | ligand_SMILES: O=C(O)CC(O)(CC(=O)O)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_157560 | ref_eq_map_22059 | beta_def_812 | logK | 7.17 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (5.65, L, +inf) |
| vlm_157561 | ref_eq_map_22060 | beta_def_812 | logK | -6.65 | 20 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (5.65, L, +inf) |
| vlm_157562 | ref_eq_map_22061 | beta_def_812 | logK | -9.18 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (5.65, L, +inf) |

---

### Step 11: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_79 AND c.beta_definition_id = beta_def_812 AND c.ligand_name_SRD LIKE '%oxalic%' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 50
}
```

[summary]
## search_stability — 2 row(s)

### `La^[3+]` + Ethanedioic acid (Oxalic acid) — 2 measurement(s)
metal_id: metal_79 | ligand_id: ligand_8872
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_151625 | ref_eq_map_19916 | beta_def_812 | logK | 4.71 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (3.8, L, +inf) |
| vlm_151626 | ref_eq_map_19917 | beta_def_812 | logK | 4.3 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (3.8, L, +inf) |

---

### Step 12: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_79 AND c.beta_definition_id = beta_def_812 AND c.ligand_id = ligand_8955 AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 50
}
```

[summary]
## search_stability — 7 row(s)

### `La^[3+]` + D-2,3-Dihydroxybutanedioic acid (D-Tartaric acid) — 7 measurement(s)
metal_id: metal_79 | ligand_id: ligand_8955
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)C(O)C(O)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_154964 | ref_eq_map_21160 | beta_def_812 | logK | 4.61 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (3.97, L, +inf) |
| vlm_154960 | ref_eq_map_21157 | beta_def_812 | logK | 3.74 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (3.97, L, +inf) |
| vlm_154961 | ref_eq_map_21161 | beta_def_812 | logK | 3.68 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (3.97, L, +inf) |
| vlm_154962 | ref_eq_map_21158 | beta_def_812 | logK | 2.95 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (3.97, L, +inf) |
| vlm_154963 | ref_eq_map_21159 | beta_def_812 | logK | 2.72 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (3.97, L, +inf) |
| vlm_154965 | *** | beta_def_812 | ΔH | 0 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (3.97, L, +inf) |
| vlm_154966 | *** | beta_def_812 | ΔS | -83.7 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (3.97, L, +inf) |

---

### Step 13: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_79 AND c.beta_definition_id = beta_def_812 AND c.ligand_id = ligand_8873 AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 50
}
```

[summary]
## search_stability — 8 row(s)

### `La^[3+]` + Propanedioic acid (Malonic acid) — 8 measurement(s)
metal_id: metal_79 | ligand_id: ligand_8873
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_152044 | *** | beta_def_812 | ΔS | 122.6 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (5.27, L, +inf) |
| vlm_152045 | *** | beta_def_812 | ΔS | 99.6 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (5.27, L, +inf) |
| vlm_152042 | *** | beta_def_812 | ΔH | 15.5 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (5.27, L, +inf) |
| vlm_152043 | *** | beta_def_812 | ΔH | 12.1 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (5.27, L, +inf) |
| vlm_152041 | ref_eq_map_20060 | beta_def_812 | logK | 4.94 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (5.27, L, +inf) |
| vlm_152039 | ref_eq_map_20059 | beta_def_812 | logK | 3.99 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (5.27, L, +inf) |
| vlm_152038 | ref_eq_map_20057 | beta_def_812 | logK | 3.69 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (5.27, L, +inf) |
| vlm_152040 | ref_eq_map_20058 | beta_def_812 | logK | 3.06 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (5.27, L, +inf) |

---

### Step 14: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_79 AND c.beta_definition_id = beta_def_812 AND c.ligand_id = ligand_8465 AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 50
}
```

[summary]
## search_stability — 6 row(s)

### `La^[3+]` + Ethanoic acid (Acetic acid) — 6 measurement(s)
metal_id: metal_79 | ligand_id: ligand_8465
ligand_HxL_def: HL | ligand_SMILES: CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_144478 | *** | beta_def_812 | ΔS | 61.1 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (4.56, L, +inf) |
| vlm_144477 | *** | beta_def_812 | ΔH | 9.2 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (4.56, L, +inf) |
| vlm_144476 | ref_eq_map_17017 | beta_def_812 | logK | 2.55 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (4.56, L, +inf) |
| vlm_144473 | ref_eq_map_17014 | beta_def_812 | logK | 1.8 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (4.56, L, +inf) |
| vlm_144475 | ref_eq_map_17016 | beta_def_812 | logK | 1.57 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (4.56, L, +inf) |
| vlm_144474 | ref_eq_map_17015 | beta_def_812 | logK | 1.54 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (4.56, L, +inf) |

---

### Step 15: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_79 AND c.beta_definition_id = beta_def_812 AND c.ligand_id = ligand_8641 AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 50
}
```

[summary]
## search_stability — 5 row(s)

### `La^[3+]` + D-2-Hydroxypropanoic acid (Lactic acid) — 5 measurement(s)
metal_id: metal_79 | ligand_id: ligand_8641
ligand_HxL_def: HL | ligand_SMILES: CC(O)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_147521 | *** | beta_def_812 | ΔS | 20.9 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (3.67, L, +inf) |
| vlm_147518 | ref_eq_map_18239 | beta_def_812 | logK | 2.6 | 20 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (3.67, L, +inf) |
| vlm_147517 | ref_eq_map_18237 | beta_def_812 | logK | 2.51 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (3.67, L, +inf) |
| vlm_147519 | ref_eq_map_18238 | beta_def_812 | logK | 2.27 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (3.67, L, +inf) |
| vlm_147520 | *** | beta_def_812 | ΔH | -6.7 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (3.67, L, +inf) |

---

### Step 16: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_79 AND c.beta_definition_id = beta_def_812 AND c.ligand_name_SRD LIKE '%benzoic%' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 50
}
```

[summary]
## search_stability — 22 row(s)

### ΔS — 7 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_79 | La^[3+] | ligand_8520 | Benzenecarboxylic acid (Ben… | HL | O=C(O)c1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8583 | 4-Fluorobenzoic acid | HL | O=C(O)c1ccc(F)cc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8760 | 4-Methoxybenzoic acid (p-An… | HL | COc1ccc(C(=O)O)cc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8759 | 3-Methoxybenzoic acid | HL | COc1cccc(C(=O)O)c1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8582 | 3-Fluorobenzoic acid | HL | O=C(O)c1cccc(F)c1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8614 | 3-Nitrobenzoic acid | HL | O=C(O)c1cccc([N+](=O)[O-])c1 | 1 | 1 | 25 | 0.1 | *** | 0 |

### ΔH — 7 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_79 | La^[3+] | ligand_8520 | Benzenecarboxylic acid (Ben… | HL | O=C(O)c1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8583 | 4-Fluorobenzoic acid | HL | O=C(O)c1ccc(F)cc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8760 | 4-Methoxybenzoic acid (p-An… | HL | COc1ccc(C(=O)O)cc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8759 | 3-Methoxybenzoic acid | HL | COc1cccc(C(=O)O)c1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8582 | 3-Fluorobenzoic acid | HL | O=C(O)c1cccc(F)c1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8614 | 3-Nitrobenzoic acid | HL | O=C(O)c1cccc([N+](=O)[O-])c1 | 1 | 1 | 25 | 0.1 | *** | 0 |

### logK — 8 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_79 | La^[3+] | ligand_8520 | Benzenecarboxylic acid (Ben… | HL | O=C(O)c1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_8583 | 4-Fluorobenzoic acid | HL | O=C(O)c1ccc(F)cc1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_8760 | 4-Methoxybenzoic acid (p-An… | HL | COc1ccc(C(=O)O)cc1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_8759 | 3-Methoxybenzoic acid | HL | COc1cccc(C(=O)O)c1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_8582 | 3-Fluorobenzoic acid | HL | O=C(O)c1cccc(F)c1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_8614 | 3-Nitrobenzoic acid | HL | O=C(O)c1cccc([N+](=O)[O-])c1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_9285 | 3-Bromo-2-hydroxy-5-sulfobe… | H3L | O=C(O)c1cc(S(=O)(=O)O)cc(Br)c1O | 1 | 1 | 25 | 0.1 | *** | 1 |

---

### Step 17: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_79 AND c.beta_definition_id = beta_def_812 AND c.ligand_id = ligand_6774 AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 50
}
```

[summary]
## search_stability — 3 row(s)

### `La^[3+]` + Pyridine-2,6-dicarboxylic acid (Dipicolinic acid) — 3 measurement(s)
metal_id: metal_79 | ligand_id: ligand_6774
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)c1cccc(C(=O)O)n1

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_119357 | *** | beta_def_812 | ΔS | 108.4 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (4.66, L, +inf) |
| vlm_119355 | ref_eq_map_8510 | beta_def_812 | logK | 7.94 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (4.66, L, +inf) |
| vlm_119356 | *** | beta_def_812 | ΔH | -13 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (4.66, L, +inf) |

---

### Step 18: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_79 AND c.beta_definition_id = beta_def_812 AND c.ligand_id = ligand_6762 AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 50
}
```

[summary]
## search_stability — 4 row(s)

### `La^[3+]` + Pyridine-2-carboxylic acid (Picolinic acid) — 4 measurement(s)
metal_id: metal_79 | ligand_id: ligand_6762
ligand_HxL_def: HL | ligand_SMILES: O=C(O)c1ccccn1

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_118697 | *** | beta_def_812 | ΔS | 49.8 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (5.21, L, +inf) |
| vlm_118694 | ref_eq_map_8312 | beta_def_812 | logK | 3.51 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (5.21, L, +inf) |
| vlm_118695 | ref_eq_map_8313 | beta_def_812 | logK | 3.19 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (5.21, L, +inf) |
| vlm_118696 | *** | beta_def_812 | ΔH | -3.3 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (5.21, L, +inf) |

---

### Step 19: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_79 AND c.beta_definition_id = beta_def_812 AND c.ligand_id = ligand_6277 AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 50
}
```

[summary]
## search_stability — 7 row(s)

### `La^[3+]` + Ethylenedinitrilotetraacetic acid (EDTA) — 7 measurement(s)
metal_id: metal_79 | ligand_id: ligand_6277
ligand_HxL_def: H4L | ligand_SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_108396 | *** | beta_def_812 | ΔS | 253.6 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108397 | *** | beta_def_812 | ΔS | 222.6 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108389 | ref_eq_map_4946 | beta_def_812 | logK | 15.36 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108390 | ref_eq_map_4947 | beta_def_812 | logK | 14.48 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108391 | *** | beta_def_812 | ΔH | -12.1 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108392 | *** | beta_def_812 | ΔH | -16.3 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108394 | *** | beta_def_812 | ΔH | -20.5 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |

---
