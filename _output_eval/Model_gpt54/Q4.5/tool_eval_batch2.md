# Q4.5 — Tool Results (batch 2)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Ca(II)",
  "limit": 10
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_25 | Ca^[2+] | Ca | 2 | ✓ | [Ca+2] | InChI=1S/Ca/q+2 | beta_totN_68 | ligand_totN_644 | vlm_totN_1761 |

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "acetate, formate, lactate, oxalate, malonate, citrate, tartrate, carbonate, phosphate, sulfate, glycine, EDTA, NTA, aspartate",
  "limit": 50
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

### Step 7: `search_pka_values`
**Args:**
```json
{
  "where": "(lc.ligand_id IN (ligand_5760, ligand_8872, ligand_8955, ligand_9058, ligand_6165, ligand_6277, ligand_6356, ligand_9048, ligand_10096, ligand_10113, ligand_10148))",
  "order_by": "lc.ligand_name_SRD ASC, p.pKa ASC",
  "limit": 200
}
```

[summary]
## search_pka_values — 35 row(s)

### pKa -10.0–-9.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_112470 | ligand_6356 | Diethylenetrinitrilopentaacetic ac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | -9.9 | 25 | 0.1 | L→HL | M_tot_2 | M_tot_58 |

### pKa -8.5–-8.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_112484 | ligand_6356 | Diethylenetrinitrilopentaacetic ac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | -8.4 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_2 |

### pKa -2.0–-1.5 (2 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_105204 | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | -1.81 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_2 |
| vlm_112522 | ligand_6356 | Diethylenetrinitrilopentaacetic ac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | -1.6 | 25 | 0.1 | H5L→H6L | M_tot_1 | M_tot_1 |

### pKa -1.5–-1.0 (2 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_108289 | ligand_6277 | Ethylenedinitrilotetraacetic acid … | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | -1.5 | 25 | 0.1 | H4L→H5L | M_tot_1 | M_tot_2 |
| vlm_151532 | ligand_8872 | Ethanedioic acid (Oxalic acid) | H2L | O=C(O)C(=O)O | -1.2 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_7 |

### pKa -1.0–-0.5 (2 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_105223 | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | -1 | 25 | 0.1 | H3L→H4L | M_tot_1 | M_tot_1 |
| vlm_112524 | ligand_6356 | Diethylenetrinitrilopentaacetic ac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | -0.7 | 25 | 0.1 | H6L→H7L | M_tot_1 | M_tot_1 |

### pKa -0.5–0.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_112526 | ligand_6356 | Diethylenetrinitrilopentaacetic ac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | -0.1 | 25 | 0.1 | H7L→H8L | M_tot_1 | M_tot_1 |

### pKa 1.5–2.0 (2 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_175604 | ligand_10148 | Hydrogen sulfate ion (Sulfuric aci… | HL | O=S(=O)([O-])O | 1.54 | 25 | 0.1 | L→HL | M_tot_1 | M_tot_74 |
| vlm_174245 | ligand_10113 | Hydrogen phosphate (Phosphoric aci… | H3L | O=P(O)(O)O | 1.92 | 25 | 0.1 | H2L→H3L | M_tot_2 | M_tot_34 |

### pKa 2.0–2.5 (3 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_112514 | ligand_6356 | Diethylenetrinitrilopentaacetic ac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 2 | 25 | 0.1 | H4L→H5L | M_tot_1 | M_tot_1 |
| vlm_108282 | ligand_6277 | Ethylenedinitrilotetraacetic acid … | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 25 | 0.1 | H3L→H4L | M_tot_2 | M_tot_2 |
| vlm_93627 | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 2.33 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_20 |

### pKa 2.5–3.0 (5 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_105186 | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 2.52 | 25 | 0.1 | HL→H2L | M_tot_2 | M_tot_2 |
| vlm_108272 | ligand_6277 | Ethylenedinitrilotetraacetic acid … | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2.69 | 25 | 0.1 | H2L→H3L | M_tot_2 | M_tot_1 |
| vlm_112506 | ligand_6356 | Diethylenetrinitrilopentaacetic ac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 2.7 | 25 | 0.1 | H3L→H4L | M_tot_1 | M_tot_1 |
| vlm_154900 | ligand_8955 | D-2,3-Dihydroxybutanedioic acid (D… | H2L | O=C(O)C(O)C(O)C(=O)O | 2.82 | 25 | 0.1 | HL→H2L | M_tot_3 | M_tot_17 |
| vlm_157473 | ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxyl… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 2.9 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_12 |

### pKa 3.0–3.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_157112 | ligand_9048 | Propane-1,2,3-tricarboxylic acid (… | H3L | O=C(O)CC(CC(=O)O)C(=O)O | 3.47 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_9 |

### pKa 3.5–4.0 (2 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_151494 | ligand_8872 | Ethanedioic acid (Oxalic acid) | H2L | O=C(O)C(=O)O | 3.8 | 25 | 0.1 | L→HL | M_tot_7 | M_tot_56 |
| vlm_154888 | ligand_8955 | D-2,3-Dihydroxybutanedioic acid (D… | H2L | O=C(O)C(O)C(O)C(=O)O | 3.97 | 25 | 0.1 | L→HL | M_tot_17 | M_tot_49 |

### pKa 4.0–4.5 (2 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_112498 | ligand_6356 | Diethylenetrinitrilopentaacetic ac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 4.28 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_1 |
| vlm_157459 | ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxyl… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 4.35 | 25 | 0.1 | HL→H2L | M_tot_12 | M_tot_18 |

### pKa 4.5–5.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_157102 | ligand_9048 | Propane-1,2,3-tricarboxylic acid (… | H3L | O=C(O)CC(CC(=O)O)C(=O)O | 4.51 | 25 | 0.1 | HL→H2L | M_tot_9 | M_tot_14 |

### pKa 5.5–6.0 (2 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_157439 | ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxyl… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 5.65 | 25 | 0.1 | L→HL | M_tot_18 | M_tot_57 |
| vlm_157092 | ligand_9048 | Propane-1,2,3-tricarboxylic acid (… | H3L | O=C(O)CC(CC(=O)O)C(=O)O | 5.85 | 25 | 0.1 | L→HL | M_tot_14 | M_tot_21 |

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

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_25 AND c.ligand_id IN (ligand_5760, ligand_8872, ligand_8955, ligand_9058, ligand_6165, ligand_6277, ligand_6356, ligand_9048, ligand_10096, ligand_10113, ligand_10148) AND c.beta_definition_id = beta_def_812)",
  "order_by": "c.ligand_name_SRD ASC, s.temperature_c ASC, s.ionic_strength_mol_l ASC, s.constant_value ASC",
  "limit": 200
}
```

[summary]
## search_stability — 77 row(s)

### logK — 10 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_25 | Ca^[2+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 8 | 1 | 25~37 | 0~0.15 | *** | 8 |
| metal_25 | Ca^[2+] | ligand_10148 | Hydrogen sulfate ion (Sulfu… | HL | O=S(=O)([O-])O | 7 | 1 | 25~37 | 0~6 | *** | 7 |
| metal_25 | Ca^[2+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 7 | 1 | 20~37 | 0~1 | *** | 7 |
| metal_25 | Ca^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 6 | 1 | 20~37 | 0~3 | *** | 6 |
| metal_25 | Ca^[2+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 6 | 1 | 18~37 | 0~0.5 | *** | 6 |
| metal_25 | Ca^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 6 | 1 | 25~37 | 0.1~1 | *** | 6 |
| metal_25 | Ca^[2+] | ligand_9048 | Propane-1,2,3-tricarboxylic… | H3L | O=C(O)CC(CC(=O)O)C(=O)O | 5 | 1 | 20~25 | 0~0.1 | *** | 5 |
| metal_25 | Ca^[2+] | ligand_8955 | D-2,3-Dihydroxybutanedioic … | H2L | O=C(O)C(O)C(O)C(=O)O | 3 | 1 | 25 | 0~0.1 | *** | 3 |
| metal_25 | Ca^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 2 | 1 | 25~37 | 0.1~0.15 | *** | 2 |
| metal_25 | Ca^[2+] | ligand_10096 | Hydrogen carbonate (Carboni… | H2L | O=C(O)O | 1 | 1 | 25 | 0 | *** | 1 |

### ΔS — 8 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_25 | Ca^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 4 | 1 | 25 | 0.1~1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_8955 | D-2,3-Dihydroxybutanedioic … | H2L | O=C(O)C(O)C(O)C(=O)O | 2 | 1 | 25 | 0~0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_10096 | Hydrogen carbonate (Carboni… | H2L | O=C(O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_10148 | Hydrogen sulfate ion (Sulfu… | HL | O=S(=O)([O-])O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |

### ΔH — 8 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_25 | Ca^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 6 | 1 | 15~35 | 0~1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_8955 | D-2,3-Dihydroxybutanedioic … | H2L | O=C(O)C(O)C(O)C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_10096 | Hydrogen carbonate (Carboni… | H2L | O=C(O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_10148 | Hydrogen sulfate ion (Sulfu… | HL | O=S(=O)([O-])O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 0 |

---

### Step 9: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_25 AND c.ligand_id IN (ligand_5760, ligand_8872, ligand_8955, ligand_9058, ligand_6165, ligand_6277, ligand_6356, ligand_9048, ligand_10096, ligand_10113, ligand_10148) AND c.beta_definition_id = beta_def_812 AND s.temperature_c = 25 AND s.ionic_strength_mol_l = 0.1)",
  "order_by": "c.ligand_name_SRD ASC, s.constant_value ASC",
  "limit": 200
}
```

[summary]
## search_stability — 26 row(s)

### ΔS — 5 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_25 | Ca^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_8955 | D-2,3-Dihydroxybutanedioic … | H2L | O=C(O)C(O)C(O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |

### ΔH — 3 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_25 | Ca^[2+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |

### logK — 8 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_25 | Ca^[2+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 4 | 1 | 25 | 0.1 | *** | 4 |
| metal_25 | Ca^[2+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 3 | 1 | 25 | 0.1 | *** | 3 |
| metal_25 | Ca^[2+] | ligand_9048 | Propane-1,2,3-tricarboxylic… | H3L | O=C(O)CC(CC(=O)O)C(=O)O | 3 | 1 | 25 | 0.1 | *** | 3 |
| metal_25 | Ca^[2+] | ligand_8955 | D-2,3-Dihydroxybutanedioic … | H2L | O=C(O)C(O)C(O)C(=O)O | 2 | 1 | 25 | 0.1 | *** | 2 |
| metal_25 | Ca^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1 | *** | 2 |
| metal_25 | Ca^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_10148 | Hydrogen sulfate ion (Sulfu… | HL | O=S(=O)([O-])O | 1 | 1 | 25 | 0.1 | *** | 1 |

---
