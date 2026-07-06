# Q3.1.5 — Tool Results (batch 3)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "calcium"
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_25 | Ca^[2+] | Ca | 2 | ✓ | [Ca+2] | InChI=1S/Ca/q+2 | beta_totN_68 | ligand_totN_644 | vlm_totN_1761 |

---

### Step 3: `search_metals`
**Args:**
```json
{
  "name": "copper"
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

### Step 4: `build_system_catalog`
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

### Step 6: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_25 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 20 AND 30 AND s.ionic_strength_mol_l BETWEEN 0 AND 0.2)",
  "order_by": "s.constant_value DESC",
  "limit": 80
}
```

[summary]
## search_stability — 80 row(s)

### ΔS — 55 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_25 | Ca^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 2 | 1 | 25 | 0~0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_9142 | 1-Hydroxyethane-1,1-diphosp… | H4L | CC(O)(P(=O)(O)O)P(=O)(O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6287 | rac-(1,2-Dimethylethylene)d… | H4L | CC(C(C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6102 | 1,4,7,10-Tetraazacyclododec… | H4L | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_8428 | Ethylenedinitrilotetrakis(m… | H8L | O=P(O)(O)CN(CCN(CP(=O)(O)O)CP(=O)(O)O)CP(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_10117 | Hydrogen triphosphate (Trip… | H5L | O=P(O)(O)OP(=O)(O)OP(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_8412 | Nitrilotris(methylenephosph… | H6L | O=P(O)(O)CN(CP(=O)(O)O)CP(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6104 | 1,4,7,10-Tetraazacyclotride… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6109 | 1,4,8,11-Tetraazacyclotetra… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_8634 | DL-2,3-Dihydroxypropanoic a… | H5L | O=C(O)C(COP(=O)(O)O)OP(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_8321 | Adenosine-5'-(tetrahydrogen… | H4L | Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)OP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]1O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6739 | N-(2,5-Dicarboxyphenyl)imin… | H4L | O=C(O)CN(CC(=O)O)c1cc(C(=O)O)ccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6070 | 1,4,10-Trioxa-7,13-diazacyc… | H2L | O=C(O)CN1CCOCCOCCN(CC(=O)O)CCOCC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6243 | 5-Amino-2,4,6-trioxo-1,3-pe… | H3L | O=C(O)CN(CC(=O)O)C1C(=O)NC(=O)NC1=O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6736 | N-(2-Carboxyphenyl)iminodia… | H3L | O=C(O)CN(CC(=O)O)c1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6311 | Trimethylenedinitrilotetraa… | H4L | O=C(O)CN(CCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_10084 | Hydrogen hexacyanoferrate(I… | *** | *** | 1 | 1 | 25 | 0 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6084 | 1-Oxa-4,7,10-triazacyclodod… | H3L | O=C(O)CN1CCOCCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6335 | Oxybis(ethylenenitrilo)tetr… | H4L | O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6342 | Ethylenebis(oxyethylenenitr… | H4L | O=C(O)CN(CCOCCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6313 | Tetramethylenedinitrilotetr… | H4L | O=C(O)CN(CCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6167 | N-(2-Carboxyethyl)iminodiac… | H3L | O=C(O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_7600 | 4,7,13,16,21-Pentaoxa-1,10-… | L | C1COCCN2CCOCCOCCN(CCO1)CCOCC2 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_8877 | Pentane-1,1-dicarboxylic ac… | H2L | CCCCC(C(=O)O)C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_8889 | Pentane-3,3-dicarboxylic ac… | H2L | CCC(CC)(C(=O)O)C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_8892 | Heptane-3,3-dicarboxylic ac… | H2L | CCCCC(CC)(C(=O)O)C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6348 | Thiobis(ethylenenitrilo)tet… | H4L | O=C(O)CN(CCSCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_7601 | 4,7,13,16,21,24-Hexaoxa-1,1… | L | C1COCCN2CCOCCOCCN(CCO1)CCOCCOCC2 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_9161 | alpha-D(-)-Glucose-1-dihydr… | H2L | O=P(O)(O)O[C@H]1OC(CO)[C@@H](O)C(O)[C@@H]1O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_8873 | Propanedioic acid (Malonic … | H2L | O=C(O)CC(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_8875 | Propane-1,1-dicarboxylic ac… | H2L | CCC(C(=O)O)C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_8881 | 2,2-Dimethylpropane-1,1-dic… | H2L | CC(C)(C)C(C(=O)O)C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_8906 | 1,3-Diphenylpropane-2,2-dic… | H2L | O=C(O)C(Cc1ccccc1)(Cc1ccccc1)C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6793 | N-(2-Pyridylmethyl)iminodia… | H2L | O=C(O)CN(CC(=O)O)Cc1ccccn1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_10148 | Hydrogen sulfate ion (Sulfu… | HL | O=S(=O)([O-])O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_10085 | Hexacyanoferrate(III) ion | *** | *** | 1 | 1 | 25 | 0 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_8915 | cis-Butenedioic acid (Malei… | H2L | O=C(O)/C=C\C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6140 | N-Methyliminodiacetic acid … | H2L | CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_10076 | Hydroxide ion | *** | *** | 1 | 1 | 25 | 0 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6731 | N-Phenyliminodiacetic acid | H2L | O=C(O)CN(CC(=O)O)c1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_8312 | Adenosine-5'-(dihydrogenpho… | H2L | Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)O)[C@@H](O)[C@H]1O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6071 | 1,4,10,13-Tetraoxa-7,16-dia… | H2L | O=C(O)CN1CCOCCOCCN(CC(=O)O)CCOCCOCC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6362 | Diethylenetrinitrilopentaac… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_8907 | Butanedioic acid (Succinic … | H2L | O=C(O)CCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_7596 | 4,7,13,18-Tetraoxa-1,10-dia… | L | C1COCCN2CCOCCN(CCO1)CCOCC2 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6204 | N-(2-Hydroxyethyl)iminodiac… | H2L | O=C(O)CN(CCO)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6774 | Pyridine-2,6-dicarboxylic a… | H2L | O=C(O)c1cccc(C(=O)O)n1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_7603 | 4,7,10,16,19,24,27-Heptaoxa… | L | C1COCCN2CCOCCOCCN(CCOCCO1)CCOCCOCC2 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6762 | Pyridine-2-carboxylic acid … | HL | O=C(O)c1ccccn1 | 1 | 1 | 25 | 0.1 | *** | 0 |

### logK — 16 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_25 | Ca^[2+] | ligand_6287 | rac-(1,2-Dimethylethylene)d… | H4L | CC(C(C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1 | *** | 2 |
| metal_25 | Ca^[2+] | ligand_6102 | 1,4,7,10-Tetraazacyclododec… | H4L | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 2 | 1 | 25 | 0.1 | *** | 2 |
| metal_25 | Ca^[2+] | ligand_6290 | rac-(1,2-Diphenylethylene)d… | H4L | O=C(O)CN(CC(=O)O)C(c1ccccc1)C(c1ccccc1)N(CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1 | *** | 2 |
| metal_25 | Ca^[2+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_6104 | 1,4,7,10-Tetraazacyclotride… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_6084 | 1-Oxa-4,7,10-triazacyclodod… | H3L | O=C(O)CN1CCOCCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_6100 | N'''-2-Hydroxypropyl-1,4,7,… | H3L | CC(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_5994 | N,N'-Bis(2-hydroxyphenyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)c1ccccc1O)c1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_6098 | 1,4,7,10-Tetraazacyclododec… | H3L | CC(C(=O)O)N1CCNCCN(C(C)C(=O)O)CCN(C(C)C(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_6121 | 3,6,9-Tris(carboxymethyl)-3… | H3L | O=C(O)CN1CCN(CC(=O)O)Cc2cccc(n2)CN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_6283 | DL-(2-Methylpropylethylene)… | H4L | CC(C)CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_6285 | DL-(2-Methyl-2-propylethyle… | H4L | CC(C)(C)C(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_6281 | DL-(2-Propylethylene)dinitr… | H4L | CC(C)C(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_6279 | DL-(Ethylethylene)dinitrilo… | H4L | CCC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_6280 | DL-(Propylethylene)dinitril… | H4L | CCCC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_6097 | 1,4,7,10-Tetraazacyclododec… | H3L | O=C(O)CN1CCNCCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |

### ΔH — 3 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_25 | Ca^[2+] | ligand_10117 | Hydrogen triphosphate (Trip… | H5L | O=P(O)(O)OP(=O)(O)OP(=O)(O)O | 2 | 1 | 20~25 | 0~0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_8634 | DL-2,3-Dihydroxypropanoic a… | H5L | O=C(O)C(COP(=O)(O)O)OP(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_8321 | Adenosine-5'-(tetrahydrogen… | H4L | Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)OP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]1O | 1 | 1 | 25 | 0.1 | *** | 0 |

---

### Step 7: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_41 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 20 AND 30 AND s.ionic_strength_mol_l BETWEEN 0 AND 0.2)",
  "order_by": "s.constant_value DESC",
  "limit": 80
}
```

[summary]
## search_stability — 80 row(s)

### ΔS — 78 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_41 | Cu^[2+] | ligand_6335 | Oxybis(ethylenenitrilo)tetr… | H4L | O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_8873 | Propanedioic acid (Malonic … | H2L | O=C(O)CC(=O)O | 2 | 1 | 25 | 0~0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6311 | Trimethylenedinitrilotetraa… | H4L | O=C(O)CN(CCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_10117 | Hydrogen triphosphate (Trip… | H5L | O=P(O)(O)OP(=O)(O)OP(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6313 | Tetramethylenedinitrilotetr… | H4L | O=C(O)CN(CCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6739 | N-(2,5-Dicarboxyphenyl)imin… | H4L | O=C(O)CN(CC(=O)O)c1cc(C(=O)O)ccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6109 | 1,4,8,11-Tetraazacyclotetra… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6736 | N-(2-Carboxyphenyl)iminodia… | H3L | O=C(O)CN(CC(=O)O)c1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6112 | 1,4,8,12-Tetraazacyclopenta… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCCN(CC(=O)O)CCN(CC(=O)O)CCC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6104 | 1,4,7,10-Tetraazacyclotride… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6065 | 1-Thia-4,7-diazacyclononane… | H2L | O=C(O)CN1CCSCCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6071 | 1,4,10,13-Tetraoxa-7,16-dia… | H2L | O=C(O)CN1CCOCCOCCN(CC(=O)O)CCOCCOCC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6070 | 1,4,10-Trioxa-7,13-diazacyc… | H2L | O=C(O)CN1CCOCCOCCN(CC(=O)O)CCOCC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_9142 | 1-Hydroxyethane-1,1-diphosp… | H4L | CC(O)(P(=O)(O)O)P(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6167 | N-(2-Carboxyethyl)iminodiac… | H3L | O=C(O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6030 | N,N'-Dimethylethylenedinitr… | H2L | CN(CCN(C)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6342 | Ethylenebis(oxyethylenenitr… | H4L | O=C(O)CN(CCOCCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5937 | N-(Phosphonomethyl)glycine … | H3L | O=C(O)CNCP(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6794 | N-(6-Methyl-2-pyridylmethyl… | H2L | Cc1cccc(CN(CC(=O)O)CC(=O)O)n1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6348 | Thiobis(ethylenenitrilo)tet… | H4L | O=C(O)CN(CCSCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6243 | 5-Amino-2,4,6-trioxo-1,3-pe… | H3L | O=C(O)CN(CC(=O)O)C1C(=O)NC(=O)NC1=O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6731 | N-Phenyliminodiacetic acid | H2L | O=C(O)CN(CC(=O)O)c1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_9158 | Propane-1,2,3-triol-2-(dihy… | H2L | O=P(O)(O)OC(CO)CO | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6793 | N-(2-Pyridylmethyl)iminodia… | H2L | O=C(O)CN(CC(=O)O)Cc1ccccn1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6031 | 5-Thia-2,8-diazanonane-N,N'… | H2L | CN(CCSCCN(C)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_7457 | 1,4,8,11-Tetramethyl-1,4,8,… | L | CN1CCCN(C)CCN(C)CCCN(C)CC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_7528 | 3,6,10,13-Tetraaza-1,8(2,6)… | L | c1cc2nc(c1)CNCCNCc1cccc(n1)CNCCNC2 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6140 | N-Methyliminodiacetic acid … | H2L | CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6316 | Octamethylenedinitrilotetra… | H4L | O=C(O)CN(CCCCCCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_7643 | 10,13,16-Trimethyl-1,4-diox… | L | CN1CCNCCOCCOCCNCCN(C)CCN(C)CC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6247 | N-Uridoiminodiacetic acid (… | H2L | NC(=O)NN(CC(=O)O)CC(=O)O | 1 | 1 | 30 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6314 | Pentamethylenedinitrilotetr… | H4L | O=C(O)CN(CCCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_9150 | Phosphoric acid methyl este… | H2L | COP(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_7425 | 1,4,7,10-Tetraazacyclododec… | L | C1CNCCNCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_7752 | 12,17-Dimethyl-5-thia-1,9,1… | L | CN1CCN2CCCSCCCN(CC1)CCN(C)CC2 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_7644 | 13,16,19-Trimethyl-1,4,7-tr… | L | CN1CCNCCOCCOCCOCCNCCN(C)CCN(C)CC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_7513 | 1,4,7,13-Tetramethyl-1,4,7,… | L | CN1CCNCCN(C)CCN(C)CCN(C)CCNCC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_7529 | 3,7,11,15-Tetraaza-1,9(2,6)… | L | c1cc2nc(c1)CNCCCNCc1cccc(n1)CNCCCNC2 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6204 | N-(2-Hydroxyethyl)iminodiac… | H2L | O=C(O)CN(CCO)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_8893 | Heptane-4,4-dicarboxylic ac… | H2L | CCCC(CCC)(C(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_8897 | Nonane-5,5-dicarboxylic aci… | H2L | CCCCC(CCCC)(C(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_8887 | Propane-2,2-dicarboxylic ac… | H2L | CC(C)(C(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_8321 | Adenosine-5'-(tetrahydrogen… | H4L | Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)OP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]1O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_8901 | Cyclopentane-1,1-dicarboxyl… | H2L | O=C(O)C1(C(=O)O)CCCC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_8902 | Cyclohexane-1,1-dicarboxyli… | H2L | O=C(O)C1(C(=O)O)CCCCC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6774 | Pyridine-2,6-dicarboxylic a… | H2L | O=C(O)c1cccc(C(=O)O)n1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_8900 | Cyclobutane-1,1-dicarboxyli… | H2L | O=C(O)C1(C(=O)O)CCC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_7436 | 1,4,7,11-Tetraazacyclotetra… | L | C1CNCCCNCCNCCNC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_7511 | 1,4,7,10,13,16-Hexaazacyclo… | L | C1CNCCNCCNCCNCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_8907 | Butanedioic acid (Succinic … | H2L | O=C(O)CCC(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_8876 | Butane-1,1-dicarboxylic aci… | H2L | CCCC(C(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_8877 | Pentane-1,1-dicarboxylic ac… | H2L | CCCCC(C(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_8880 | 3-Methylbutane-1,1-dicarbox… | H2L | CC(C)CC(C(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_8879 | 2-Methylpropane-1,1-dicarbo… | H2L | CC(C)C(C(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_8974 | Oxydiacetic acid (Diglycoli… | H2L | O=C(O)COCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_9083 | (Ethanediylidenetetrathio)t… | H4L | O=C(O)CSC(SCC(=O)O)C(SCC(=O)O)SCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_8899 | Cyclopropane-1,1-dicarboxyl… | H2L | O=C(O)C1(C(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_9161 | alpha-D(-)-Glucose-1-dihydr… | H2L | O=P(O)(O)O[C@H]1OC(CO)[C@@H](O)C(O)[C@@H]1O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_8874 | Ethane-1,1-dicarboxylic aci… | H2L | CC(C(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_9152 | Phosphoric acid phenyl este… | H2L | O=P(O)(O)Oc1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6562 | Glycylglycyl-L-tyrosine | H2L | NCC(=O)NCC(=O)N[C@@H](Cc1ccc(O)cc1)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6564 | L-Tyrosylglycylglycine | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)NCC(=O)NCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_8134 | 8-Hydroxyquinoline-5-sulfon… | H2L | O=S(=O)(O)c1ccc(O)c2ncccc12 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6251 | N-(Thiourido)iminodiacetic … | H2L | NC(=S)NN(CC(=O)O)CC(=O)O | 1 | 1 | 30 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_9154 | Phosphoric acid 1-naphthyl … | H2L | O=P(O)(O)Oc1cccc2ccccc12 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_8915 | cis-Butenedioic acid (Malei… | H2L | O=C(O)/C=C\C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_8885 | 2-Phenylethane-1,1-dicarbox… | H2L | O=C(O)C(Cc1ccccc1)C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_9004 | 3,3'-Thiodipropanoic acid | H2L | O=C(O)CCSCCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_7531 | 1,4,7-Trimethyl-1,4,7,10,13… | L | CN1CCNCCNCCNCCNCCN(C)CCN(C)CC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_9156 | Phosphoric acid 4-nitrophen… | H2L | O=[N+]([O-])c1ccc(OP(=O)(O)O)cc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |

---
