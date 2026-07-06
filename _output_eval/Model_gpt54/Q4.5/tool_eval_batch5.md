# Q4.5 — Tool Results (batch 5)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Ca(II), H+",
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
  "name": "acetate, lactate, oxalate, malonate, succinate, citrate, tartrate, phosphate, carbonate, glycine, EDTA, NTA",
  "limit": 30
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 5: `build_system_catalog`
**Args:**
```json
{}
```

[summary]
[CATALOG]
## build_system_catalog

**Error:** Provide at least one of metal_id, ligand_id, or beta_definition_id.

---

### Step 6: `search_metals`
**Args:**
```json
{
  "symbol": "Ca",
  "limit": 10
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_25 | Ca^[2+] | Ca | 2 | ✓ | [Ca+2] | InChI=1S/Ca/q+2 | beta_totN_68 | ligand_totN_644 | vlm_totN_1761 |

---

### Step 7: `search_ligands`
**Args:**
```json
{
  "name": "acetate, lactate, oxalate, malonate, succinate, citrate, tartrate, phosphate, carbonate, glycine, EDTA, NTA",
  "limit": 50
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 8: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_25"
}
```

[summary]
[CATALOG]
## build_system_catalog — 20 pair(s), 74 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_156 | [M] + [H2L]^2 <=> [M(H2L)2] |  |
| beta_def_283 | [MHL(s)] <=> [M] + [H] + [L] | solid |
| beta_def_296 | [MHL(H2O)2(s)] <=> [M] + [HL] + [H2O]^2 | solid |
| beta_def_298 | [MHL(s)] <=> [M] + [HL] | solid |
| beta_def_306 | [ML(H2O)2(s,gypsum)] <=> [M] + [L] + [H2O]^2 | solid |
| beta_def_307 | [ML(H2O)3(s)] <=> [M] + [L] + [H2O]^3 | solid |
| beta_def_310 | [ML(H2O)6(s)] <=> [M] + [L] + [H2O]^6 | solid |
| beta_def_313 | [ML(s,aragonite)] <=> [M] + [L] | solid |
| beta_def_316 | [ML(s,calcite)] <=> [M] + [L] | solid |
| beta_def_319 | [ML(s,monohydrocalcite)] <=> [M] + [L] | solid |
| beta_def_324 | [ML(s,vaterite)] <=> [M] + [L] | solid |
| beta_def_327 | [ML(H2O)(s)] <=> [M] + [L] + [H2O] | solid |
| beta_def_332 | [ML2(H2O)6(s)] <=> [M] + [L]^2 + [H2O]^6 | solid |
| beta_def_502 | [M]^2 + [L] <=> [M2L] |  |
| beta_def_516 | [ML] + [M] <=> [M2L] |  |
| beta_def_624 | [M3L2(s)] <=> [M]^3 + [L]^2 | solid |
| beta_def_625 | [M3L2(s,beta)] <=> [M]^3 + [L]^2 | solid |
| beta_def_665 | [M4HL3(H2O)2.5(s)] <=> [M]^4 + [H] + [L]^3 + [H2O]^2.5 | solid |
| beta_def_666 | [M4HL3(H2O)3(s)] <=> [M]^4 + [H] + [L]^3 + [H2O]^3 | solid |
| beta_def_689 | [M5(OH)L3(H2O)(s)] <=> [M]^5 + [OH] + [L]^3 + [H2O] | solid |
| beta_def_732 | [M] + [H2L] <=> [MH2L] |  |
| beta_def_739 | [MHL] + [H] <=> [MH2L] |  |
| beta_def_751 | [MH2L] + [H] <=> [MH3L] |  |
| beta_def_765 | [MH3L] + [H] <=> [MH4L] |  |
| beta_def_779 | [M] + [HL] <=> [MHL] |  |
| beta_def_788 | [ML] + [H] <=> [MHL] |  |
| beta_def_792 | [ML2] + [H] <=> [MHL2] |  |
| beta_def_812 | [M] + [L] <=> [ML] |  |
| beta_def_840 | [M] + [L]^2 <=> [ML2] |  |
| beta_def_966 | [M(OH)L] + [H] <=> [ML] + [H2O] |  |

*(all species aqueous unless noted)*

**1. Ca^[2+] + Hydrogen phosphate (Phosphoric acid)** (metal_25 + ligand_10113) — ligand_def_HxL: H3L | 40 ent, 9 sp, 40 vlms (vlm_174342…vlm_174381)
   - species: beta_def_156(1) beta_def_296(7) beta_def_298(4) beta_def_625(4) beta_def_665(1) beta_def_666(2) beta_def_689(2) beta_def_732(9) beta_def_779(10)
   - eq:10 nets T:13~41°C I:-0.15~3.15M max 8n/28e
**2. Ca^[2+] + Nitrilotris(methylenephosphonic acid) (NTP)** (metal_25 + ligand_8412) — ligand_def_HxL: H6L | 30 ent, 4 sp, 30 vlms (vlm_143294…vlm_143323)
   - species: beta_def_739(4) beta_def_751(2) beta_def_788(12) beta_def_812(12)
   - eq:3 nets T:19~30°C I:-0.15~1.15M max 4n/4e
**3. Ca^[2+] + 1-Hydroxyethane-1,1-diphosphonic acid (Etidronic acid)** (metal_25 + ligand_9142) — ligand_def_HxL: H4L | 22 ent, 3 sp, 22 vlms (vlm_159220…vlm_159241)
   - species: beta_def_502(6) beta_def_779(6) beta_def_812(10)
   - eq:4 nets T:19~30°C I:-0.15~0.65M max 3n/3e
**4. Ca^[2+] + Hydrogen carbonate (Carbonic acid)** (metal_25 + ligand_10096) — ligand_def_HxL: H2L | 21 ent, 7 sp, 21 vlms (vlm_172687…vlm_172707)
   - species: beta_def_310(3) beta_def_313(4) beta_def_316(4) beta_def_319(1) beta_def_324(3) beta_def_779(3) beta_def_812(3)
   - eq:4 nets T:5~45°C I:-0.15~0.85M max 7n/21e
**5. Ca^[2+] + Hydrogen sulfate ion (Sulfuric acid)** (metal_25 + ligand_10148) — ligand_def_HxL: HL | 19 ent, 2 sp, 19 vlms (vlm_175657…vlm_175675)
   - species: beta_def_306(10) beta_def_812(9)
   - eq:9 nets T:19~41°C I:-0.15~6.15M max 2n/1e
**6. Ca^[2+] + N-(Phosphonomethyl)glycine (Glyphosate)** (metal_25 + ligand_5937) — ligand_def_HxL: H3L | 19 ent, 7 sp, 19 vlms (vlm_99765…vlm_99783)
   - species: beta_def_298(1) beta_def_502(4) beta_def_739(4) beta_def_788(4) beta_def_792(1) beta_def_812(4) beta_def_840(1)
   - eq:2 nets T:19~30°C I:-0.05~0.65M max 7n/11e
**7. Ca^[2+] + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid)** (metal_25 + ligand_9058) — ligand_def_HxL: H3L | 18 ent, 5 sp, 18 vlms (vlm_157530…vlm_157547)
   - species: beta_def_283(1) beta_def_624(1) beta_def_732(1) beta_def_779(5) beta_def_812(10)
   - eq:8 nets T:19~41°C I:-0.15~0.3M max 5n/10e
**8. Ca^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_25 + ligand_6277) — ligand_def_HxL: H4L | 18 ent, 2 sp, 18 vlms (vlm_108344…vlm_108361)
   - species: beta_def_788(2) beta_def_812(16)
   - eq:6 nets T:19~41°C I:-0.05~1.15M max 2n/1e
**9. Ca^[2+] + Ethanedioic acid (Oxalic acid)** (metal_25 + ligand_8872) — ligand_def_HxL: H2L | 17 ent, 3 sp, 17 vlms (vlm_151595…vlm_151611)
   - species: beta_def_307(2) beta_def_327(9) beta_def_812(6)
   - eq:9 nets T:13~41°C I:-0.15~1.15M max 3n/3e
**10. Ca^[2+] + Hydrogen triphosphate (Triphosphoric acid)** (metal_25 + ligand_10117) — ligand_def_HxL: H5L | 15 ent, 3 sp, 15 vlms (vlm_174890…vlm_174904)
   - species: beta_def_779(6) beta_def_812(8) beta_def_966(1)
   - eq:5 nets T:19~30°C I:-0.15~1.15M max 3n/2e
**11. Ca^[2+] + Ethylenedinitrilotetrakis(methylenephosphonic acid) (EDTP)** (metal_25 + ligand_8428) — ligand_def_HxL: H8L | 15 ent, 5 sp, 15 vlms (vlm_143717…vlm_143731)
   - species: beta_def_739(3) beta_def_751(3) beta_def_765(3) beta_def_788(3) beta_def_812(3)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 5n/7e
**12. Ca^[2+] + Nitrilotriacetic acid (NTA)** (metal_25 + ligand_6165) — ligand_def_HxL: H3L | 15 ent, 2 sp, 15 vlms (vlm_105256…vlm_105270)
   - species: beta_def_812(9) beta_def_840(6)
   - eq:7 nets T:15~41°C I:-0.15~1.15M max 2n/1e
**13. Ca^[2+] + Hydrogen iodate (Iodic acid)** (metal_25 + ligand_10173) — ligand_def_HxL: HL | 14 ent, 2 sp, 14 vlms (vlm_178632…vlm_178645)
   - species: beta_def_332(9) beta_def_812(5)
   - eq:7 nets T:19~30°C I:-0.05~4.15M max 2n/1e
**14. Ca^[2+] + Propane-1,2,3-tricarboxylic acid (Tricarballylic acid)** (metal_25 + ligand_9048) — ligand_def_HxL: H3L | 13 ent, 4 sp, 13 vlms (vlm_157144…vlm_157156)
   - species: beta_def_502(2) beta_def_732(3) beta_def_779(3) beta_def_812(5)
   - eq:5 nets T:15~30°C I:-0.15~0.25M max 4n/6e
**15. Ca^[2+] + Adenosine-5'-(tetrahydrogentriphosphate) (ATP)** (metal_25 + ligand_8321) — ligand_def_HxL: H4L | 12 ent, 2 sp, 12 vlms (vlm_141536…vlm_141547)
   - species: beta_def_779(5) beta_def_812(7)
   - eq:5 nets T:19~41°C I:-0.05~0.65M max 2n/1e
**16. Ca^[2+] + Triethylenetetranitrilohexaacetic acid (TTHA)** (metal_25 + ligand_6366) — ligand_def_HxL: H6L | 12 ent, 4 sp, 12 vlms (vlm_113057…vlm_113068)
   - species: beta_def_516(3) beta_def_739(3) beta_def_788(3) beta_def_812(3)
   - eq:3 nets T:15~35°C I:-0.05~0.25M max 4n/4e
**17. Ca^[2+] + Tetramethylenedinitrilotetraacetic acid** (metal_25 + ligand_6313) — ligand_def_HxL: H4L | 12 ent, 3 sp, 12 vlms (vlm_110650…vlm_110661)
   - species: beta_def_516(1) beta_def_788(4) beta_def_812(7)
   - eq:3 nets T:15~30°C I:-0.05~0.65M max 3n/3e
**18. Ca^[2+] + Aminoacetic acid (Glycine)** (metal_25 + ligand_5760) — ligand_def_HxL: HL | 12 ent, 2 sp, 12 vlms (vlm_93666…vlm_93677)
   - species: beta_def_779(4) beta_def_812(8)
   - eq:6 nets T:15~41°C I:-0.15~3.15M max 2n/1e
**19. Ca^[2+] + D-2,3-Dihydroxybutanedioic acid (D-Tartaric acid)** (metal_25 + ligand_8955) — ligand_def_HxL: H2L | 11 ent, 2 sp, 11 vlms (vlm_154938…vlm_154948)
   - species: beta_def_779(5) beta_def_812(6)
   - eq:3 nets T:19~30°C I:-0.15~0.25M max 2n/1e
**20. Ca^[2+] + Diethylenetrinitrilopentaacetic acid (DTPA)** (metal_25 + ligand_6356) — ligand_def_HxL: H5L | 11 ent, 3 sp, 11 vlms (vlm_112538…vlm_112548)
   - species: beta_def_516(3) beta_def_788(3) beta_def_812(5)
   - eq:3 nets T:15~41°C I:-0.05~0.3M max 3n/3e

---

### Step 10: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_25 AND c.beta_definition_id = beta_def_812 AND c.ligand_id IN (ligand_5760, ligand_8872, ligand_9058, ligand_6165, ligand_6277, ligand_8955, ligand_10096, ligand_10113) AND s.solvent_name LIKE '%water%' AND s.temperature_c BETWEEN 20 AND 30 AND s.ionic_strength_mol_l <= 0.15)",
  "order_by": "c.ligand_name_SRD ASC, ABS(s.temperature_c-25) ASC, ABS(COALESCE(s.ionic_strength_mol_l,0)-0.1) ASC",
  "limit": 100
}
```

[summary]
## search_stability

*(no results)*

---

### Step 11: `search_pka_values`
**Args:**
```json
{
  "where": "(lc.ligand_id IN (ligand_5760, ligand_8872, ligand_9058, ligand_6165, ligand_6277, ligand_8955, ligand_10096, ligand_10113) AND p.solvent_name LIKE '%water%' AND p.temperature_c BETWEEN 20 AND 30 AND (p.ionic_strength_mol_l <= 0.15 OR p.ionic_strength_mol_l IS NULL))",
  "order_by": "lc.ligand_name_SRD ASC, p.pKa ASC",
  "limit": 200
}
```

[summary]
## search_pka_values

*(no results)*

---

### Step 12: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_25 AND c.beta_definition_id = beta_def_812 AND c.ligand_id IN (ligand_5760, ligand_8872, ligand_9058, ligand_6165, ligand_6277, ligand_8955, ligand_10096, ligand_10113))",
  "order_by": "c.ligand_name_SRD ASC, s.constant_value DESC",
  "limit": 200
}
```

[summary]
## search_stability — 58 row(s)

### logK — 7 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_25 | Ca^[2+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 8 | 1 | 25~37 | 0~0.15 | *** | 8 |
| metal_25 | Ca^[2+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 7 | 1 | 20~37 | 0~1 | *** | 7 |
| metal_25 | Ca^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 6 | 1 | 20~37 | 0~3 | *** | 6 |
| metal_25 | Ca^[2+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 6 | 1 | 18~37 | 0~0.5 | *** | 6 |
| metal_25 | Ca^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 6 | 1 | 25~37 | 0.1~1 | *** | 6 |
| metal_25 | Ca^[2+] | ligand_8955 | D-2,3-Dihydroxybutanedioic … | H2L | O=C(O)C(O)C(O)C(=O)O | 3 | 1 | 25 | 0~0.1 | *** | 3 |
| metal_25 | Ca^[2+] | ligand_10096 | Hydrogen carbonate (Carboni… | H2L | O=C(O)O | 1 | 1 | 25 | 0 | *** | 1 |

### ΔH — 6 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_25 | Ca^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 6 | 1 | 15~35 | 0~1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_8955 | D-2,3-Dihydroxybutanedioic … | H2L | O=C(O)C(O)C(O)C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_10096 | Hydrogen carbonate (Carboni… | H2L | O=C(O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 0 |

### ΔS — 6 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_25 | Ca^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 4 | 1 | 25 | 0.1~1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_8955 | D-2,3-Dihydroxybutanedioic … | H2L | O=C(O)C(O)C(O)C(=O)O | 2 | 1 | 25 | 0~0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_10096 | Hydrogen carbonate (Carboni… | H2L | O=C(O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |

---

### Step 13: `search_pka_values`
**Args:**
```json
{
  "where": "(lc.ligand_id IN (ligand_5760, ligand_8872, ligand_9058, ligand_6165, ligand_6277, ligand_8955, ligand_10096, ligand_10113))",
  "order_by": "lc.ligand_name_SRD ASC, p.pKa ASC",
  "limit": 300
}
```

[summary]
## search_pka_values — 23 row(s)

### pKa -2.0–-1.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_105204 | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | -1.81 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_2 |

### pKa -1.5–-1.0 (2 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_108289 | ligand_6277 | Ethylenedinitrilotetraacetic acid … | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | -1.5 | 25 | 0.1 | H4L→H5L | M_tot_1 | M_tot_2 |
| vlm_151532 | ligand_8872 | Ethanedioic acid (Oxalic acid) | H2L | O=C(O)C(=O)O | -1.2 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_7 |

### pKa -1.0–-0.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_105223 | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | -1 | 25 | 0.1 | H3L→H4L | M_tot_1 | M_tot_1 |

### pKa 1.5–2.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_174245 | ligand_10113 | Hydrogen phosphate (Phosphoric aci… | H3L | O=P(O)(O)O | 1.92 | 25 | 0.1 | H2L→H3L | M_tot_2 | M_tot_34 |

### pKa 2.0–2.5 (2 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_108282 | ligand_6277 | Ethylenedinitrilotetraacetic acid … | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 25 | 0.1 | H3L→H4L | M_tot_2 | M_tot_2 |
| vlm_93627 | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 2.33 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_20 |

### pKa 2.5–3.0 (4 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_105186 | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 2.52 | 25 | 0.1 | HL→H2L | M_tot_2 | M_tot_2 |
| vlm_108272 | ligand_6277 | Ethylenedinitrilotetraacetic acid … | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2.69 | 25 | 0.1 | H2L→H3L | M_tot_2 | M_tot_1 |
| vlm_154900 | ligand_8955 | D-2,3-Dihydroxybutanedioic acid (D… | H2L | O=C(O)C(O)C(O)C(=O)O | 2.82 | 25 | 0.1 | HL→H2L | M_tot_3 | M_tot_17 |
| vlm_157473 | ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxyl… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 2.9 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_12 |

### pKa 3.5–4.0 (2 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_151494 | ligand_8872 | Ethanedioic acid (Oxalic acid) | H2L | O=C(O)C(=O)O | 3.8 | 25 | 0.1 | L→HL | M_tot_7 | M_tot_56 |
| vlm_154888 | ligand_8955 | D-2,3-Dihydroxybutanedioic acid (D… | H2L | O=C(O)C(O)C(O)C(=O)O | 3.97 | 25 | 0.1 | L→HL | M_tot_17 | M_tot_49 |

### pKa 4.0–4.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_157459 | ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxyl… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 4.35 | 25 | 0.1 | HL→H2L | M_tot_12 | M_tot_18 |

### pKa 5.5–6.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_157439 | ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxyl… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 5.65 | 25 | 0.1 | L→HL | M_tot_18 | M_tot_57 |

### pKa 6.0–6.5 (2 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_108254 | ligand_6277 | Ethylenedinitrilotetraacetic acid … | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 6.13 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_7 |
| vlm_172632 | ligand_10096 | Hydrogen carbonate (Carbonic acid) | H2L | O=C(O)O | 6.13 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_24 |

### pKa 6.5–7.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_174214 | ligand_10113 | Hydrogen phosphate (Phosphoric aci… | H3L | O=P(O)(O)O | 6.71 | 25 | 0.1 | HL→H2L | M_tot_34 | M_tot_29 |

### pKa 9.0–9.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_105158 | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 9.46 | 25 | 0.1 | L→HL | M_tot_2 | M_tot_68 |

### pKa 9.5–10.0 (3 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_108224 | ligand_6277 | Ethylenedinitrilotetraacetic acid … | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 9.52 | 25 | 0.1 | L→HL | M_tot_7 | M_tot_70 |
| vlm_93606 | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 9.57 | 25 | 0.1 | L→HL | M_tot_20 | M_tot_43 |
| vlm_172612 | ligand_10096 | Hydrogen carbonate (Carbonic acid) | H2L | O=C(O)O | 9.91 | 25 | 0.1 | L→HL | M_tot_24 | M_tot_38 |

### pKa 11.5–12.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_174186 | ligand_10113 | Hydrogen phosphate (Phosphoric aci… | H3L | O=P(O)(O)O | 11.52 | 25 | 0.1 | L→HL | M_tot_29 | M_tot_32 |

---

### Step 14: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_25 AND c.beta_definition_id = beta_def_812 AND c.ligand_id IN (ligand_5760, ligand_8872, ligand_9058, ligand_6165, ligand_6277, ligand_8955, ligand_10096) AND s.temperature_c BETWEEN 24 AND 26 AND (s.ionic_strength_mol_l = 0.1 OR s.ionic_strength_mol_l = 0))",
  "order_by": "c.ligand_name_SRD ASC, s.ionic_strength_mol_l ASC, s.constant_value DESC",
  "limit": 200
}
```

[summary]
## search_stability — 31 row(s)

### logK — 7 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_25 | Ca^[2+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 5 | 1 | 25 | 0~0.1 | *** | 5 |
| metal_25 | Ca^[2+] | ligand_8955 | D-2,3-Dihydroxybutanedioic … | H2L | O=C(O)C(O)C(O)C(=O)O | 3 | 1 | 25 | 0~0.1 | *** | 3 |
| metal_25 | Ca^[2+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 3 | 1 | 25 | 0.1 | *** | 3 |
| metal_25 | Ca^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 2 | 1 | 25 | 0~0.1 | *** | 2 |
| metal_25 | Ca^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1 | *** | 2 |
| metal_25 | Ca^[2+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 1 | 1 | 25 | 0 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_10096 | Hydrogen carbonate (Carboni… | H2L | O=C(O)O | 1 | 1 | 25 | 0 | *** | 1 |

### ΔH — 5 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_25 | Ca^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0~0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_8955 | D-2,3-Dihydroxybutanedioic … | H2L | O=C(O)C(O)C(O)C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_10096 | Hydrogen carbonate (Carboni… | H2L | O=C(O)O | 1 | 1 | 25 | 0 | *** | 0 |

### ΔS — 6 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_25 | Ca^[2+] | ligand_8955 | D-2,3-Dihydroxybutanedioic … | H2L | O=C(O)C(O)C(O)C(=O)O | 2 | 1 | 25 | 0~0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_10096 | Hydrogen carbonate (Carboni… | H2L | O=C(O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |

---

### Step 15: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_5760"
}
```

[summary]
## inspect_card — Ligand | ligand_5760

**Name:** Aminoacetic acid (Glycine)  
**Formula:** C2H5N1O2 | **Class:** Amino Acids  
**SMILES:** `NCC(=O)O`  
**InChI:** `InChI=1S/C2H5NO2/c3-1-2(4)5/h1,3H2,(H,4,5)`  
**HxL definition:** HL  

**pKa values:** 2

| source_vlm | pKa | T (°C) | I (M) | From → To | Solvent | Method | Quality |
|------------|-----|--------|-------|-----------|---------|--------|---------|
| vlm_93627 | 2.33 | 25.0 | 0.1 | HL → H2L | *** | *** | *** |
| vlm_93606 | 9.57 | 25.0 | 0.1 | L → HL | *** | *** | *** |

**Partners:** 50 metal(s), 428 measurement(s) total

| metal_id | Metal | # meas |
|----------|-------|--------|
| metal_112 | Ni^[2+] | 49 |
| metal_68 | H^[+] | 48 |
| metal_208 | Zn^[2+] | 37 |
| metal_33 | Co^[2+] | 37 |
| metal_26 | Cd^[2+] | 32 |
| … | *(showing top 5 of 50)* | |

---

### Step 16: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_8872"
}
```

[summary]
## inspect_card — Ligand | ligand_8872

**Name:** Ethanedioic acid (Oxalic acid)  
**Formula:** C2H2O4 | **Class:** Carboxylic acids diacids  
**SMILES:** `O=C(O)C(=O)O`  
**InChI:** `InChI=1S/C2H2O4/c3-1(4)2(5)6/h(H,3,4)(H,5,6)`  
**HxL definition:** H2L  

**pKa values:** 2

| source_vlm | pKa | T (°C) | I (M) | From → To | Solvent | Method | Quality |
|------------|-----|--------|-------|-----------|---------|--------|---------|
| vlm_151532 | -1.20 | 25.0 | 0.1 | HL → H2L | *** | *** | *** |
| vlm_151494 | 3.80 | 25.0 | 0.1 | L → HL | *** | *** | *** |

**Partners:** 59 metal(s), 394 measurement(s) total

| metal_id | Metal | # meas |
|----------|-------|--------|
| metal_68 | H^[+] | 56 |
| metal_195 | UO_[2]^[2+] | 21 |
| metal_5 | Al^[3+] | 18 |
| metal_25 | Ca^[2+] | 17 |
| metal_19 | Be^[2+] | 16 |
| … | *(showing top 5 of 59)* | |

---

### Step 17: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_9058"
}
```

[summary]
## inspect_card — Ligand | ligand_9058

**Name:** 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid)  
**Formula:** C6H8O7 | **Class:** Carboxylic acids polyacids  
**SMILES:** `O=C(O)CC(O)(CC(=O)O)C(=O)O`  
**InChI:** `InChI=1S/C6H8O7/c7-3(8)1-6(13,5(11)12)2-4(9)10/h13H,1-2H2,(H,7,8)(H,9,10)(H,11,12)`  
**HxL definition:** H3L  

**pKa values:** 3

| source_vlm | pKa | T (°C) | I (M) | From → To | Solvent | Method | Quality |
|------------|-----|--------|-------|-----------|---------|--------|---------|
| vlm_157473 | 2.90 | 25.0 | 0.1 | H2L → H3L | *** | *** | *** |
| vlm_157459 | 4.35 | 25.0 | 0.1 | HL → H2L | *** | *** | *** |
| vlm_157439 | 5.65 | 25.0 | 0.1 | L → HL | *** | *** | *** |

**Partners:** 57 metal(s), 384 measurement(s) total

| metal_id | Metal | # meas |
|----------|-------|--------|
| metal_68 | H^[+] | 48 |
| metal_112 | Ni^[2+] | 25 |
| metal_204 | W^[6+] | 24 |
| metal_26 | Cd^[2+] | 22 |
| metal_208 | Zn^[2+] | 19 |
| … | *(showing top 5 of 57)* | |

---

### Step 18: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_6165"
}
```

[summary]
## inspect_card — Ligand | ligand_6165

**Name:** Nitrilotriacetic acid (NTA)  
**Formula:** C6H9N1O6 | **Class:** NTA and derivatives  
**SMILES:** `O=C(O)CN(CC(=O)O)CC(=O)O`  
**InChI:** `InChI=1S/C6H9NO6/c8-4(9)1-7(2-5(10)11)3-6(12)13/h1-3H2,(H,8,9)(H,10,11)(H,12,13)`  
**HxL definition:** H3L  

**pKa values:** 4

| source_vlm | pKa | T (°C) | I (M) | From → To | Solvent | Method | Quality |
|------------|-----|--------|-------|-----------|---------|--------|---------|
| vlm_105204 | -1.81 | 25.0 | 0.1 | H2L → H3L | *** | *** | *** |
| vlm_105223 | -1.00 | 25.0 | 0.1 | H3L → H4L | *** | *** | *** |
| vlm_105186 | 2.52 | 25.0 | 0.1 | HL → H2L | *** | *** | *** |
| vlm_105158 | 9.46 | 25.0 | 0.1 | L → HL | *** | *** | *** |

**Partners:** 71 metal(s), 534 measurement(s) total

| metal_id | Metal | # meas |
|----------|-------|--------|
| metal_68 | H^[+] | 72 |
| metal_103 | Mo^[6+] | 20 |
| metal_112 | Ni^[2+] | 19 |
| metal_208 | Zn^[2+] | 16 |
| metal_61 | Fe^[3+] | 16 |
| … | *(showing top 5 of 71)* | |

---

### Step 19: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_6277"
}
```

[summary]
## inspect_card — Ligand | ligand_6277

**Name:** Ethylenedinitrilotetraacetic acid (EDTA)  
**Formula:** C10H16N2O8 | **Class:** EDTA and derivatives  
**SMILES:** `O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O`  
**InChI:** `InChI=1S/C10H16N2O8/c13-7(14)3-11(4-8(15)16)1-2-12(5-9(17)18)6-10(19)20/h1-6H2,(H,13,14)(H,15,16)(H,17,18)(H,19,20)`  
**HxL definition:** H4L  

**pKa values:** 5

| source_vlm | pKa | T (°C) | I (M) | From → To | Solvent | Method | Quality |
|------------|-----|--------|-------|-----------|---------|--------|---------|
| vlm_108289 | -1.50 | 25.0 | 0.1 | H4L → H5L | *** | *** | *** |
| vlm_108282 | 2.00 | 25.0 | 0.1 | H3L → H4L | *** | *** | *** |
| vlm_108272 | 2.69 | 25.0 | 0.1 | H2L → H3L | *** | *** | *** |
| vlm_108254 | 6.13 | 25.0 | 0.1 | HL → H2L | *** | *** | *** |
| vlm_108224 | 9.52 | 25.0 | 0.1 | L → HL | *** | *** | *** |

**Partners:** 75 metal(s), 596 measurement(s) total

| metal_id | Metal | # meas |
|----------|-------|--------|
| metal_68 | H^[+] | 75 |
| metal_26 | Cd^[2+] | 23 |
| metal_41 | Cu^[2+] | 20 |
| metal_112 | Ni^[2+] | 19 |
| metal_208 | Zn^[2+] | 18 |
| … | *(showing top 5 of 75)* | |

---

### Step 20: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_8955"
}
```

[summary]
## inspect_card — Ligand | ligand_8955

**Name:** D-2,3-Dihydroxybutanedioic acid (D-Tartaric acid)  
**Formula:** C4H6O6 | **Class:** Carboxylic acids diacids hydroxy  
**SMILES:** `O=C(O)C(O)C(O)C(=O)O`  
**InChI:** `InChI=1S/C4H6O6/c5-1(3(7)8)2(6)4(9)10/h1-2,5-6H,(H,7,8)(H,9,10)`  
**HxL definition:** H2L  

**pKa values:** 2

| source_vlm | pKa | T (°C) | I (M) | From → To | Solvent | Method | Quality |
|------------|-----|--------|-------|-----------|---------|--------|---------|
| vlm_154900 | 2.82 | 25.0 | 0.1 | HL → H2L | *** | *** | *** |
| vlm_154888 | 3.97 | 25.0 | 0.1 | L → HL | *** | *** | *** |

**Partners:** 51 metal(s), 214 measurement(s) total

| metal_id | Metal | # meas |
|----------|-------|--------|
| metal_68 | H^[+] | 23 |
| metal_41 | Cu^[2+] | 23 |
| metal_79 | La^[3+] | 19 |
| metal_26 | Cd^[2+] | 11 |
| metal_25 | Ca^[2+] | 11 |
| … | *(showing top 5 of 51)* | |

---

### Step 21: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_10096"
}
```

[summary]
## inspect_card — Ligand | ligand_10096

**Name:** Hydrogen carbonate (Carbonic acid)  
**Formula:** C1H2O3 | **Class:** Inorganic ligands  
**SMILES:** `O=C(O)O`  
**InChI:** `InChI=1S/CH2O3/c2-1(3)4/h(H2,2,3,4)`  
**HxL definition:** H2L  

**pKa values:** 2

| source_vlm | pKa | T (°C) | I (M) | From → To | Solvent | Method | Quality |
|------------|-----|--------|-------|-----------|---------|--------|---------|
| vlm_172632 | 6.13 | 25.0 | 0.1 | HL → H2L | *** | *** | *** |
| vlm_172612 | 9.91 | 25.0 | 0.1 | L → HL | *** | *** | *** |

**Partners:** 39 metal(s), 335 measurement(s) total

| metal_id | Metal | # meas |
|----------|-------|--------|
| metal_68 | H^[+] | 48 |
| metal_195 | UO_[2]^[2+] | 33 |
| metal_25 | Ca^[2+] | 21 |
| metal_41 | Cu^[2+] | 20 |
| metal_92 | Mg^[2+] | 16 |
| … | *(showing top 5 of 39)* | |

---
