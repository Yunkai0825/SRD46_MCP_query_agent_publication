# Q3.1.6 — Tool Results (batch 2)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Lanthanum",
  "symbol": "La",
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
  "name": "DTPA, EDTA, HEDTA, DOTA, NTA, citrate, oxalate, tartrate, malonate, succinate",
  "limit": 100
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

### Step 5: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_79 AND c.ligand_class_name LIKE '%carbox%' AND s.temperature_c BETWEEN 23 AND 27 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2)",
  "order_by": "s.constant_value DESC",
  "limit": 50
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. You must call 0_plan_search_strategy first (PHASE 2) before using the execution tools.

---

### Step 7: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_79 AND c.beta_definition_id = beta_def_812 AND c.ligand_class_name LIKE '%carbox%' AND (s.solvent_name IS NULL OR LOWER(s.solvent_name) LIKE '%water%') AND s.temperature_c BETWEEN 23 AND 27 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2))",
  "order_by": "s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability

*(no results)*

---
