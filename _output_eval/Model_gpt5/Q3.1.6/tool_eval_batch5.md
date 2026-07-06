# Q3.1.6 — Tool Results (batch 5)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Lanthanum",
  "symbol": "La",
  "limit": 5
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
  "name": "DTPA",
  "limit": 10
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 5 SQL matches · showing 5 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6117 | 9,17-Dioxo-1,4,7,10,13,16-hexaazacycl… (DTPA-dien) | H3L | Aza macrocycles with car… | 6 | `O=C(O)CN1CCN(CC(=O)O)CC(=O)NCCNCCNC(=O)CN(CC(=O)O)CC1` | (-inf, H5L, -1.8, H4L, 2.62, H3L, 4.1, H2L, 8.87, HL, 10.02, L, +inf) |
| ligand_6356 | Diethylenetrinitrilopentaacetic acid (DTPA) | H5L | EDTA and derivatives | 322 | `O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O` | (-inf, H8L, -0.1, H7L, -0.1, H6L, -0.7, H5L, 2, H4L, 2.7, H3L, 4.28, H2L, 4.28, HL, -8.4, L, +inf) |
| ligand_6362 | Diethylenetrinitrilopentaacetic acid N… (DTPA-BMA) | *** | EDTA and derivatives | 43 | *** | (-inf, H4L, -1.4, H3L, 3.31, H2L, 4.38, HL, 9.37, L, +inf) |
| ligand_6363 | Diethylenetrinitrilopentaacetic acid N… (DTPA-BBA) | *** | EDTA and derivatives | 9 | *** | (-inf, H3L, 3.31, H2L, 4.44, HL, 9.36, L, +inf) |
| ligand_6364 | N,N"-Bis(2-pyridylmethyl)diethylenetrin… (DTPA-BP) | *** | EDTA and derivatives | 14 | *** | (-inf, H5L, 2.28, H4L, 3.41, H3L, 4.76, H2L, 6.46, HL, 9.5, L, +inf) |

### Functional groups across all SQL matches (2 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 2 | 100% |
| tertiary_amine | 2 | 100% |
| amide | 1 | 50% |
| secondary_amine | 1 | 50% |

---

### Step 4: `search_ligands`
**Args:**
```json
{
  "name": "EDTA",
  "limit": 10
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 5 SQL matches · showing 5 · limit 10

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

### Step 5: `search_ligands`
**Args:**
```json
{
  "name": "HEDTA",
  "limit": 10
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6275 | N-(2-Hydroxyethyl)ethylenedinitrilotriace… (HEDTA) | H3L | EDTA and derivatives | 237 | `O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O` | (-inf, H3L, 2.62, H2L, 5.38, HL, 9.7, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 1 | 100% |
| hydroxyl | 1 | 100% |
| tertiary_amine | 1 | 100% |

---

### Step 6: `search_ligands`
**Args:**
```json
{
  "name": "EGTA",
  "limit": 10
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6342 | Ethylenebis(oxyethylenenitrilo)tetraacetic… (EGTA) | H4L | EDTA and derivatives | 169 | `O=C(O)CN(CCOCCOCCN(CC(=O)O)CC(=O)O)CC(=O)O` | (-inf, H4L, -1.9, H3L, 2.7, H2L, 8.71, HL, 9.32, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 1 | 100% |
| ether | 1 | 100% |
| tertiary_amine | 1 | 100% |

---

### Step 7: `search_ligands`
**Args:**
```json
{
  "name": "NTA",
  "limit": 10
}
```

[summary]
## search_ligands — 10 result(s)

**stats:** 298 SQL matches · showing 10 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5763 | DL-2-Aminopentanoic acid (Norvaline) | HL | Amino Acids | 35 | `CCC[C@H](N)C(=O)O` | (-inf, H2L, 2.31, HL, 9.65, L, +inf) |
| ligand_5766 | L-2-Amino-4-methylpentanoic acid (Leucine) | HL | Amino Acids | 49 | `CC(C)C[C@H](N)C(=O)O` | (-inf, H2L, 2.32, HL, 9.58, L, +inf) |
| ligand_5767 | L-2-Amino-3-methylpentanoic acid (Isoleucine) | HL | Amino Acids | 51 | `CC[C@H](C)[C@H](N)C(=O)O` | (-inf, H2L, 2.26, HL, 9.6, L, +inf) |
| ligand_5768 | D-allo-2-Amino-3-methylpentan… (D-allo-Isoleucine) | HL | Amino Acids | 16 | `CC[C@H](C)[C@@H](N)C(=O)O` | (-inf, H2L, 2.2, HL, 9.62, L, +inf) |
| ligand_5773 | 1-Aminocyclopentanecarboxylic acid (Cycloleucine) | HL | Amino Acids | 11 | `NC1(C(=O)O)CCCC1` | (-inf, H2L, 2.4, HL, 10.31, L, +inf) |
| ligand_5790 | cis-2-Aminocyclopentane-1-carboxylic acid | HL | Amino Acids | 6 | `N[C@H]1CCC[C@H]1C(=O)O` | (-inf, H2L, 3.54, HL, 10.1, L, +inf) |
| ligand_5791 | trans-2-Aminocyclopentane-1-carboxylic acid | HL | Amino Acids | 3 | `N[C@@H]1CCC[C@H]1C(=O)O` | (-inf, H2L, 3.75, HL, 9.91, L, +inf) |
| ligand_5798 | 5-Aminopentanoic acid | HL | Amino Acids | 20 | `NCCCCC(=O)O` | (-inf, H2L, 4.27, HL, 10.766, L, +inf) |
| ligand_5804 | L-2-Aminopentanedioic acid (Glutamic acid) | H2L | Amino Acids | 94 | `N[C@@H](CCC(=O)O)C(=O)O` | (-inf, H3L, 2.16, H2L, 4.15, HL, 9.58, L, +inf) |
| ligand_5805 | DL-2-Amino-2-methylpentan… (2-Methylglutamic acid) | H2L | Amino Acids | 4 | `C[C@](N)(CCC(=O)O)C(=O)O` | (-inf, H2L, 4.05, HL, 9.72, L, +inf) |

### Functional groups across all SQL matches (223 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 88 | 39% |
| secondary_amine | 81 | 36% |
| tertiary_amine | 60 | 27% |
| amide | 46 | 21% |
| primary_amine | 45 | 20% |
| hydroxyl | 38 | 17% |
| ether | 37 | 17% |
| aromatic_ring | 31 | 14% |
| thioether | 13 | 6% |
| phosphonate | 10 | 4% |
| pyridine | 9 | 4% |
| imine | 7 | 3% |
| ketone | 7 | 3% |
| ester | 6 | 3% |
| halide | 6 | 3% |
| thiol | 5 | 2% |
| oxime | 3 | 1% |
| phenol | 2 | 1% |
| phosphate | 2 | 1% |
| sulfonate | 1 | 0% |

---

### Step 8: `search_ligands`
**Args:**
```json
{
  "name": "citrate",
  "limit": 10
}
```

[summary]
## search_ligands — 4 result(s)

**stats:** 4 SQL matches · showing 4 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8672 | 2-Hydroxypropane-1,2,3-tri… (sym-Dimethyl citrate) | HL | Carboxylic acids hydroxy | 2 | `COC(=O)CC(O)(CC(=O)OC)C(=O)O` | (-inf, HL, 3.02, L, +inf) |
| ligand_8682 | DL-2-Hydroxypropane-1,2,3-t… (as-Dimethyl citrate) | HL | Carboxylic acids hydroxy | 2 | `COC(=O)CC(O)(CC(=O)O)C(=O)OC` | (-inf, HL, 3.78, L, +inf) |
| ligand_8965 | 2-Hydroxypropane-1,2,3-tri… (as-Monomethylcitrate) | H2L | Carboxylic acids diacids… | 4 | `COC(=O)CC(O)(CC(=O)O)C(=O)O` | (-inf, H2L, 2.7, HL, 4.66, L, +inf) |
| ligand_8966 | 2-Hydroxypropane-1,2,3-tr… (sym-Monomethylcitrate) | H2L | Carboxylic acids diacids… | 4 | `COC(=O)C(O)(CC(=O)O)CC(=O)O` | (-inf, H2L, 3.39, HL, 4.63, L, +inf) |

### Functional groups across all SQL matches (4 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 4 | 100% |
| ester | 4 | 100% |
| hydroxyl | 4 | 100% |

---

### Step 9: `search_ligands`
**Args:**
```json
{
  "name": "oxalate",
  "limit": 10
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 10: `search_ligands`
**Args:**
```json
{
  "name": "tartrate",
  "limit": 10
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 12: `build_system_catalog`
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

### Step 14: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_79 AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability — 100 row(s)

### ΔS — 61 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_79 | La^[3+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1~0.5 | *** | 0 |
| metal_79 | La^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_79 | La^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_79 | La^[3+] | ligand_6267 | N-Methylethylenedinitrilotr… | H3L | CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_79 | La^[3+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_79 | La^[3+] | ligand_6309 | Ethylenedinitrilo-N,N'-di(3… | H4L | O=C(O)CCN(CCN(CCC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_79 | La^[3+] | ligand_10148 | Hydrogen sulfate ion (Sulfu… | HL | O=S(=O)([O-])O | 2 | 1 | 25 | 0~2 | *** | 0 |
| metal_79 | La^[3+] | ligand_8873 | Propanedioic acid (Malonic … | H2L | O=C(O)CC(=O)O | 2 | 1 | 25 | 0.1~1 | *** | 0 |
| metal_79 | La^[3+] | ligand_9593 | 5-Hydroxy-2-hydroxymethyl-4… | HL | O=c1cc(CO)occ1O | 2 | 1 | 25 | 0.1~2 | *** | 0 |
| metal_79 | La^[3+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6298 | trans-1,2-Cyclopentylenedin… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCC[C@H]1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6311 | Trimethylenedinitrilotetraa… | H4L | O=C(O)CN(CCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6335 | Oxybis(ethylenenitrilo)tetr… | H4L | O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6751 | 1,2-Phenylenedinitrilotetra… | H4L | O=C(O)CN(CC(=O)O)c1ccccc1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6348 | Thiobis(ethylenenitrilo)tet… | H4L | O=C(O)CN(CCSCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6342 | Ethylenebis(oxyethylenenitr… | H4L | O=C(O)CN(CCOCCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6362 | Diethylenetrinitrilopentaac… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6313 | Tetramethylenedinitrilotetr… | H4L | O=C(O)CN(CCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_9054 | Benzene-1,2,3-tricarboxylic… | H3L | O=C(O)c1cccc(C(=O)O)c1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8937 | trans-Cyclohexane-1,4-dicar… | H2L | O=C(O)[C@H]1CC[C@H](C(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_5975 | Ethylenediiminodiacetic aci… | H2L | O=C(O)CNCCNCC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8915 | cis-Butenedioic acid (Malei… | H2L | O=C(O)/C=C\C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6774 | Pyridine-2,6-dicarboxylic a… | H2L | O=C(O)c1cccc(C(=O)O)n1 | 1 | 1 | 25 | 0.5 | *** | 0 |
| metal_79 | La^[3+] | ligand_8986 | Ethylenebis(oxyacetic acid) | H2L | O=C(O)COCCOCC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8933 | Hexanedioic acid (Adipic ac… | H2L | O=C(O)CCCCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8921 | Pentanedioic acid (Glutaric… | H2L | O=C(O)CCCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8907 | Butanedioic acid (Succinic … | H2L | O=C(O)CCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8974 | Oxydiacetic acid (Diglycoli… | H2L | O=C(O)COCC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_79 | La^[3+] | ligand_9526 | Pentane-2,4-dione (Acetylac… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_10086 | Hexacyanocobaltate(III) ion | *** | *** | 1 | 1 | 25 | 0 | *** | 0 |
| metal_79 | La^[3+] | ligand_10162 | Hydrogen fluoride (Hydroflu… | HL | F | 1 | 1 | 25 | 1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8939 | Benzene-1,3-dicarboxylic ac… | H2L | O=C(O)c1cccc(C(=O)O)c1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8917 | trans-Butenedioic acid (Fum… | H2L | O=C(O)/C=C/C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_10085 | Hexacyanoferrate(III) ion | *** | *** | 1 | 1 | 25 | 0 | *** | 0 |
| metal_79 | La^[3+] | ligand_9568 | 1-Hydroxycyclohepta-3,5,7-t… | HL | O=c1cccccc1O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8473 | 2-Methylpropanoic acid (Iso… | HL | CC(C)C(=O)O | 1 | 1 | 25 | 2 | *** | 0 |
| metal_79 | La^[3+] | ligand_9564 | Dihydroxycyclobutenedione (… | H2L | O=c1c(O)c(O)c1=O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6771 | Pyridine-2,3-dicarboxylic a… | H2L | O=C(O)c1cccnc1C(=O)O | 1 | 1 | 25 | 0.5 | *** | 0 |
| metal_79 | La^[3+] | ligand_9566 | Dihydroxycyclopentenetrione… | H2L | O=c1c(O)c(O)c(=O)c1=O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8521 | Phenylacetic acid | HL | O=C(O)Cc1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_9601 | L-3,4-Dihydroxy-5-(1,2-dihy… | H2L | O=C1O[C@H]([C@@H](O)CO)C(O)=C1O | 1 | 1 | 25 | 2 | *** | 0 |
| metal_79 | La^[3+] | ligand_8673 | 3-Hydroxypropanoic acid | HL | O=C(O)CCO | 1 | 1 | 25 | 2 | *** | 0 |
| metal_79 | La^[3+] | ligand_8467 | Propanoic acid (Propionic a… | HL | CCC(=O)O | 1 | 1 | 25 | 2 | *** | 0 |
| metal_79 | La^[3+] | ligand_8520 | Benzenecarboxylic acid (Ben… | HL | O=C(O)c1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8583 | 4-Fluorobenzoic acid | HL | O=C(O)c1ccc(F)cc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8760 | 4-Methoxybenzoic acid (p-An… | HL | COc1ccc(C(=O)O)cc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 1 | 1 | 25 | 2 | *** | 0 |
| metal_79 | La^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8759 | 3-Methoxybenzoic acid | HL | COc1cccc(C(=O)O)c1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8582 | 3-Fluorobenzoic acid | HL | O=C(O)c1cccc(F)c1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6762 | Pyridine-2-carboxylic acid … | HL | O=C(O)c1ccccn1 | 1 | 1 | 25 | 0.5 | *** | 0 |
| metal_79 | La^[3+] | ligand_8728 | Oxole-2-carboxylic acid (2-… | HL | O=C(O)c1ccco1 | 1 | 1 | 25 | 2 | *** | 0 |
| metal_79 | La^[3+] | ligand_8614 | 3-Nitrobenzoic acid | HL | O=C(O)c1cccc([N+](=O)[O-])c1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6760 | 1,4-Diazine-2-carboxylic ac… | HL | O=C(O)c1cnccn1 | 1 | 1 | 25 | 1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 1 | 1 | 25 | 2 | *** | 0 |
| metal_79 | La^[3+] | ligand_8641 | D-2-Hydroxypropanoic acid (… | HL | CC(O)C(=O)O | 1 | 1 | 25 | 2 | *** | 0 |
| metal_79 | La^[3+] | ligand_8659 | L-Phenyl(hydroxy)acetic aci… | HL | O=C(O)C(O)c1ccccc1 | 1 | 1 | 25 | 2 | *** | 0 |
| metal_79 | La^[3+] | ligand_10163 | Chloride ion | *** | *** | 1 | 1 | 25 | 1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8647 | 2-Hydroxy-2-methylpropanoic… | HL | CC(C)(O)C(=O)O | 1 | 1 | 25 | 2 | *** | 0 |

### logK — 22 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_79 | La^[3+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1~1 | *** | 2 |
| metal_79 | La^[3+] | ligand_6335 | Oxybis(ethylenenitrilo)tetr… | H4L | O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1 | *** | 2 |
| metal_79 | La^[3+] | ligand_6342 | Ethylenebis(oxyethylenenitr… | H4L | O=C(O)CN(CCOCCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1 | *** | 2 |
| metal_79 | La^[3+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6298 | trans-1,2-Cyclopentylenedin… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCC[C@H]1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6366 | Triethylenetetranitrilohexa… | H6L | O=C(O)CN(CCN(CCN(CC(=O)O)CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6102 | 1,4,7,10-Tetraazacyclododec… | H4L | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6116 | 1,4,7,10,13,16-Hexaazacyclo… | H6L | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6358 | Diethylenetrinitrilotetraac… | H5L | O=C(O)CCN(CCN(CCN(CC(=O)O)CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6104 | 1,4,7,10-Tetraazacyclotride… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_10114 | Hydrogen diphosphate (Pyrop… | H4L | O=P(O)(O)OP(=O)(O)O | 1 | 1 | 25 | 0 | *** | 1 |
| metal_79 | La^[3+] | ligand_6287 | rac-(1,2-Dimethylethylene)d… | H4L | CC(C(C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6279 | DL-(Ethylethylene)dinitrilo… | H4L | CCC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6280 | DL-(Propylethylene)dinitril… | H4L | CCCC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6282 | DL-(Butylethylene)dinitrilo… | H4L | CCCCC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6283 | DL-(2-Methylpropylethylene)… | H4L | CC(C)CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6284 | DL-(Hexylethylene)dinitrilo… | H4L | CCCCCCC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6037 | N,N'-Bis(2-hydroxybenzyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)Cc1ccccc1O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6281 | DL-(2-Propylethylene)dinitr… | H4L | CC(C)C(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6353 | N-Ethyliminobis(ethylenenit… | H4L | CCN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_6289 | DL-(Phenylethylene)dinitril… | H4L | O=C(O)CN(CC(=O)O)CC(c1ccccc1)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |

### ΔH — 4 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_79 | La^[3+] | ligand_10148 | Hydrogen sulfate ion (Sulfu… | HL | O=S(=O)([O-])O | 2 | 1 | 25 | 0~2 | *** | 0 |
| metal_79 | La^[3+] | ligand_6311 | Trimethylenedinitrilotetraa… | H4L | O=C(O)CN(CCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8873 | Propanedioic acid (Malonic … | H2L | O=C(O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |

---

### Step 15: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_79 AND c.beta_definition_id = beta_def_812 AND s.constant_type = 'logK' AND s.temperature_c BETWEEN 20 AND 30 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l BETWEEN 0.05 AND 1.2))",
  "order_by": "s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability

*(no results)*

---
