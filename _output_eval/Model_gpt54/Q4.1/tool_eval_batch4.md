# Q4.1 — Tool Results (batch 4)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Fe(II), Fe(III)",
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
  "name": "DMF, acetonitrile, THF, ethylene glycol",
  "limit": 20
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
  "name": "iron",
  "symbol": "Fe",
  "limit": 20
}
```

[summary]
## search_metals — 2 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_61 | Fe^[3+] | Fe | 3 | ✓ | [Fe+3] | InChI=1S/Fe/q+3 | beta_totN_128 | ligand_totN_406 | vlm_totN_1473 |
| metal_62 | Fe^[2+] | Fe | 2 | ✓ | [Fe+2] | InChI=1S/Fe/q+2 | beta_totN_57 | ligand_totN_217 | vlm_totN_667 |

---

### Step 7: `search_ligands`
**Args:**
```json
{
  "name": "dimethylformamide, N,N-dimethylformamide, acetonitrile, methyl cyanide, tetrahydrofuran, oxolane, ethylene glycol, ethanediol",
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
  "metal_id": "metal_61"
}
```

[summary]
[CATALOG]
## build_system_catalog — 20 pair(s), 113 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_194 | [M] + [HL]^2 <=> [M(HL)2] |  |
| beta_def_204 | [MHL2] + [H] <=> [M(HL)2] |  |
| beta_def_207 | [MHL3] + [H] <=> [M(HL)2L] |  |
| beta_def_208 | [M] + [HL]^3 <=> [M(HL)3] |  |
| beta_def_213 | [M(HL)2L] + [H] <=> [M(HL)3] |  |
| beta_def_214 | [MH2L3] + [H] <=> [M(HL)3] |  |
| beta_def_238 | [M(OH)2L] + [H] <=> [M(OH)L] + [H2O] |  |
| beta_def_263 | [M(OH)3L] + [H] <=> [M(OH)2L] + [H2O] |  |
| beta_def_351 | [(M2O3)0.5(s,alpha)] + [H2O]^1.5 <=> [M] + [OH]^3 | solid |
| beta_def_352 | [ML3(s)] <=> [M] + [L]^3 | solid |
| beta_def_357 | [MOOH(s,alpha)] + [H2O] <=> [M] + [OH]^3 | solid |
| beta_def_423 | [ML]^2 + [H2O]^2 <=> [M2(OH)2L2] + [H]^2 |  |
| beta_def_424 | [M]^2 + [L]^2 + [H2O]^2 <=> [M2(OH)2L2] + [H]^2 |  |
| beta_def_427 | [M(OH)L]^2 <=> [M2(OH)2L2] |  |
| beta_def_502 | [M]^2 + [L] <=> [M2L] |  |
| beta_def_519 | [M]^2 + [L]^2 <=> [M2L2] |  |
| beta_def_585 | [M]^2 + [L]^3 + [H2O] <=> [M2(OH)L3] + [H] |  |
| beta_def_597 | [M]^3 + [L]^6 + [H2O]^2 <=> [M3(OH)2L6] + [H]^2 |  |
| beta_def_601 | [M]^3 + [L]^2 + [H2O]^3 <=> [M3(OH)3L2] + [H]^3 |  |
| beta_def_649 | [M]^3 + [L]^4 <=> [M3L4] |  |
| beta_def_708 | [M]^7 + [L]^6 + [H2O]^9 <=> [M7(OH)9L6] + [H]^9 |  |
| beta_def_748 | [ML3] + [H]^2 <=> [MH2L3] |  |
| beta_def_779 | [M] + [HL] <=> [MHL] |  |
| beta_def_788 | [ML] + [H] <=> [MHL] |  |
| beta_def_792 | [ML2] + [H] <=> [MHL2] |  |
| beta_def_803 | [ML3] + [H] <=> [MHL3] |  |
| beta_def_812 | [M] + [L] <=> [ML] |  |
| beta_def_821 | [M] + [HL] <=> [ML] + [H] |  |
| beta_def_823 | [M] + [H2L] <=> [ML] + [H]^2 |  |
| beta_def_840 | [M] + [L]^2 <=> [ML2] |  |
| beta_def_846 | [ML] + [HL] <=> [ML2] + [H] |  |
| beta_def_853 | [ML] + [H2L] <=> [ML2] + [H]^2 |  |
| beta_def_864 | [M(OH)2L2] + [H]^2 <=> [ML2] + [H2O]^2 |  |
| beta_def_872 | [M] + [L]^3 <=> [ML3] |  |
| beta_def_873 | [ML2] + [HL] <=> [ML3] + [H] |  |
| beta_def_876 | [ML2] + [H2L] <=> [ML3] + [H]^2 |  |
| beta_def_892 | [M(OH)L3] + [H] <=> [ML3] + [H2O] |  |
| beta_def_894 | [M] + [L]^4 <=> [ML4] |  |
| beta_def_903 | [M] + [L]^5 <=> [ML5] |  |
| beta_def_966 | [M(OH)L] + [H] <=> [ML] + [H2O] |  |
| beta_def_981 | [ML] + [OH] <=> [M(OH)L] |  |
| beta_def_984 | [M(OH)L2] + [H] <=> [ML2] + [H2O] |  |

*(all species aqueous unless noted)*

**1. Fe^[3+] + Hydrogen thiocyanate (Thiocyanic acid)** (metal_61 + ligand_10092) — ligand_def_HxL: HL | 39 ent, 5 sp, 39 vlms (vlm_172282…vlm_172320)
   - species: beta_def_812(21) beta_def_840(8) beta_def_872(5) beta_def_894(1) beta_def_981(4)
   - eq:13 nets T:19~30°C I:-0.15~5.15M max 4n/6e
**2. Fe^[3+] + Hydroxide ion** (metal_61 + ligand_10076) — ligand_def_HxL: *** | 38 ent, 8 sp, 38 vlms (vlm_170791…vlm_170828)
   - species: beta_def_351(1) beta_def_352(2) beta_def_357(2) beta_def_519(10) beta_def_649(5) beta_def_812(11) beta_def_840(6) beta_def_894(1)
   - eq:8 nets T:19~30°C I:-0.15~3.15M max 8n/28e
**3. Fe^[3+] + Hydrogen azide (Hydrazoic acid)** (metal_61 + ligand_10106) — ligand_def_HxL: HL | 22 ent, 5 sp, 22 vlms (vlm_173624…vlm_173645)
   - species: beta_def_812(6) beta_def_840(4) beta_def_872(4) beta_def_894(4) beta_def_903(4)
   - eq:4 nets T:19~30°C I:-0.15~3.15M max 5n/10e
**4. Fe^[3+] + 1,2-Dihydroxybenzene-3,5-disulfonic acid (Tiron)** (metal_61 + ligand_9358) — ligand_def_HxL: H4L | 16 ent, 4 sp, 16 vlms (vlm_162088…vlm_162103)
   - species: beta_def_788(4) beta_def_823(4) beta_def_853(4) beta_def_876(4)
   - eq:4 nets T:15~30°C I:-0.05~1.15M max 4n/6e
**5. Fe^[3+] + Ethanoic acid (Acetic acid)** (metal_61 + ligand_8465) — ligand_def_HxL: HL | 16 ent, 5 sp, 16 vlms (vlm_144783…vlm_144798)
   - species: beta_def_597(5) beta_def_601(1) beta_def_708(1) beta_def_812(6) beta_def_840(3)
   - eq:5 nets T:15~30°C I:-0.05~3.15M max 5n/10e
**6. Fe^[3+] + Nitrilotriacetic acid (NTA)** (metal_61 + ligand_6165) — ligand_def_HxL: H3L | 16 ent, 8 sp, 16 vlms (vlm_105553…vlm_105568)
   - species: beta_def_238(2) beta_def_263(1) beta_def_423(1) beta_def_427(1) beta_def_788(1) beta_def_812(4) beta_def_840(2) beta_def_966(4)
   - eq:5 nets T:15~30°C I:-0.05~1.15M max 5n/8e
**7. Fe^[3+] + 2-Hydroxybenzoic acid (Salicylic acid)** (metal_61 + ligand_9257) — ligand_def_HxL: H2L | 15 ent, 3 sp, 15 vlms (vlm_160398…vlm_160412)
   - species: beta_def_779(1) beta_def_821(11) beta_def_846(3)
   - eq:7 nets T:15~30°C I:-0.15~3.15M max 3n/3e
**8. Fe^[3+] + Propanedioic acid (Malonic acid)** (metal_61 + ligand_8873) — ligand_def_HxL: H2L | 14 ent, 3 sp, 14 vlms (vlm_152337…vlm_152350)
   - species: beta_def_812(5) beta_def_840(5) beta_def_872(4)
   - eq:3 nets T:19~30°C I:-0.05~1.15M max 3n/3e
**9. Fe^[3+] + trans-1,2-Cyclohexylenedinitrilotetraacetic acid (CDTA)** (metal_61 + ligand_6301) — ligand_def_HxL: H4L | 14 ent, 4 sp, 14 vlms (vlm_109793…vlm_109806)
   - species: beta_def_423(3) beta_def_427(3) beta_def_812(4) beta_def_966(4)
   - eq:3 nets T:15~30°C I:-0.05~1.15M max 3n/3e
**10. Fe^[3+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_61 + ligand_6277) — ligand_def_HxL: H4L | 14 ent, 4 sp, 14 vlms (vlm_108639…vlm_108652)
   - species: beta_def_427(3) beta_def_788(3) beta_def_812(4) beta_def_966(4)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 3n/3e
**11. Fe^[3+] + Chloride ion** (metal_61 + ligand_10163) — ligand_def_HxL: *** | 13 ent, 2 sp, 13 vlms (vlm_177390…vlm_177402)
   - species: beta_def_812(11) beta_def_840(2)
   - eq:7 nets T:19~30°C I:-0.15~4.15M max 2n/1e
**12. Fe^[3+] + Hydrogen fluoride (Hydrofluoric acid)** (metal_61 + ligand_10162) — ligand_def_HxL: HL | 13 ent, 3 sp, 13 vlms (vlm_176996…vlm_177008)
   - species: beta_def_812(5) beta_def_840(4) beta_def_872(4)
   - eq:3 nets T:19~30°C I:-0.05~1.15M max 3n/3e
**13. Fe^[3+] + 4-Amino-2-hydroxybenzoic acid (p-Aminosalicylic acid)** (metal_61 + ligand_9297) — ligand_def_HxL: H2L | 13 ent, 4 sp, 13 vlms (vlm_161165…vlm_161177)
   - species: beta_def_779(6) beta_def_821(3) beta_def_846(2) beta_def_873(2)
   - eq:4 nets T:19~30°C I:-0.05~3.15M max 4n/6e
**14. Fe^[3+] + 8-Hydroxyquinoline (8-Quinolinol)(Oxine)** (metal_61 + ligand_8126) — ligand_def_HxL: HL | 13 ent, 4 sp, 13 vlms (vlm_137976…vlm_137988)
   - species: beta_def_352(1) beta_def_812(4) beta_def_840(4) beta_def_872(4)
   - eq:4 nets T:19~30°C I:-0.15~1.15M max 4n/6e
**15. Fe^[3+] + DL-2-Amino-3-hydroxybutanohydroxamic acid (Threoninehydroxamic acid)** (metal_61 + ligand_6995) — ligand_def_HxL: HL | 12 ent, 12 sp, 12 vlms (vlm_121724…vlm_121735)
   - species: beta_def_194(1) beta_def_204(1) beta_def_207(1) beta_def_208(1) beta_def_213(1) beta_def_424(1) beta_def_779(1) beta_def_792(1) beta_def_803(1) beta_def_840(1) beta_def_872(1) beta_def_892(1)
   - eq:1 nets T:16.5~31.5°C I:0.275~0.725M max 12n/41e
**16. Fe^[3+] + Ethanedioic acid (Oxalic acid)** (metal_61 + ligand_8872) — ligand_def_HxL: H2L | 11 ent, 3 sp, 11 vlms (vlm_151793…vlm_151803)
   - species: beta_def_812(5) beta_def_840(3) beta_def_872(3)
   - eq:3 nets T:16.5~31.5°C I:0.275~3.225M max 3n/3e
**17. Fe^[3+] + Glycylglycylglycinehydroxamic acid** (metal_61 + ligand_7000) — ligand_def_HxL: HL | 11 ent, 11 sp, 11 vlms (vlm_121837…vlm_121847)
   - species: beta_def_194(1) beta_def_204(1) beta_def_208(1) beta_def_214(1) beta_def_502(1) beta_def_748(1) beta_def_792(1) beta_def_812(1) beta_def_840(1) beta_def_864(1) beta_def_872(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 11n/30e
**18. Fe^[3+] + DL-2-Amino-3-hydroxypropanohydroxamic acid (Serinehydroxamic acid)** (metal_61 + ligand_6994) — ligand_def_HxL: HL | 11 ent, 11 sp, 11 vlms (vlm_121699…vlm_121709)
   - species: beta_def_194(1) beta_def_204(1) beta_def_207(1) beta_def_208(1) beta_def_213(1) beta_def_424(1) beta_def_779(1) beta_def_792(1) beta_def_803(1) beta_def_840(1) beta_def_872(1)
   - eq:1 nets T:16.5~31.5°C I:0.275~0.725M max 11n/34e
**19. Fe^[3+] + DL-2-Aminopentanohydroxamic acid (Norvalinehydroxamic acid)** (metal_61 + ligand_6985) — ligand_def_HxL: HL | 11 ent, 11 sp, 11 vlms (vlm_121560…vlm_121570)
   - species: beta_def_194(1) beta_def_207(1) beta_def_424(1) beta_def_585(1) beta_def_779(1) beta_def_792(1) beta_def_803(1) beta_def_840(1) beta_def_872(1) beta_def_892(1) beta_def_984(1)
   - eq:1 nets T:16.5~31.5°C I:0.275~0.725M max 11n/39e
**20. Fe^[3+] + Acetohydroxamic acid** (metal_61 + ligand_9873) — ligand_def_HxL: HL | 10 ent, 3 sp, 10 vlms (vlm_168447…vlm_168456)
   - species: beta_def_812(6) beta_def_840(2) beta_def_872(2)
   - eq:4 nets T:15~30°C I:-0.05~2.15M max 3n/3e

---

### Step 10: `search_stability`
**Args:**
```json
{
  "where": "((c.metal_id = metal_61 OR c.metal_id = metal_62) AND (c.ligand_name_SRD LIKE '%formamide%' OR c.ligand_name_SRD LIKE '%dimethylformamide%' OR c.ligand_name_SRD LIKE '%acetonitrile%' OR c.ligand_name_SRD LIKE '%methyl cyanide%' OR c.ligand_name_SRD LIKE '%tetrahydrofuran%' OR c.ligand_name_SRD LIKE '%oxolane%' OR c.ligand_name_SRD LIKE '%ethylene glycol%' OR c.ligand_name_SRD LIKE '%ethanediol%' OR c.ligand_name_SRD LIKE '%1,2-ethanediol%'))",
  "order_by": "c.metal_name_SRD, c.ligand_name_SRD, s.constant_type, s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability

*(no results)*

---

### Step 11: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_card",
  "group_column": "ligand_class_name",
  "where": "(metal_id = 61 OR metal_id = 62)",
  "limit": 30
}
```

[summary]
## db_distribution - ligandmetal_card by ligand_class_name

**total_rows:** 2140

| value | count | pct |
|-------|-------|-----|
| Inorganic ligands | 273 | 12.76% |
| Amino Acids | 217 | 10.14% |
| EDTA and derivatives | 184 | 8.6% |
| Catechols | 155 | 7.24% |
| miscellaneous hydroxamic acids | 133 | 6.21% |
| Aliphatic amines | 111 | 5.19% |
| Phenols salicylic acids | 102 | 4.77% |
| Pyridines (azines) | 77 | 3.6% |
| NTA and derivatives | 74 | 3.46% |
| Phenols | 67 | 3.13% |
| Aminophosphorus acids | 64 | 2.99% |
| Carboxylic acids | 62 | 2.9% |
| Aza macrocycles with carboxylic acids | 60 | 2.8% |
| Carboxylic acids polyacids | 56 | 2.62% |
| Carboxylic acids diacids | 47 | 2.2% |
| Phenanthrolines | 44 | 2.06% |
| cyclic ketones | 36 | 1.68% |
| Pyridine carboxylic acids | 36 | 1.68% |
| Naphtols | 31 | 1.45% |
| Bipyridines | 31 | 1.45% |
| Aza-macrocycles | 31 | 1.45% |
| Aliphatic amines secondary N | 30 | 1.4% |
| Iminodiacetic acid and derivatives | 28 | 1.31% |
| Aliphatic amines tertiary N | 24 | 1.12% |
| Quinolines | 22 | 1.03% |
| Aza-oxa-macrocycles | 20 | 0.93% |
| Carboxylic acids diacids S-Se-Te-P-As | 17 | 0.79% |
| Pyrroles (azoles) | 16 | 0.75% |
| Tripyridines | 15 | 0.7% |
| Carboxylic acids diacids hydroxy | 15 | 0.7% |

---

### Step 12: `db_ranked_pairs`
**Args:**
```json
{
  "rank_by": "measurement_count",
  "limit": 50,
  "where": "(lc.metal_id = 61 OR lc.metal_id = 62)"
}
```

[summary]
**db_ranked_pairs:** Error - Unknown rank_by='measurement_count'. Choose from: ['ligands_per_metal', 'measurements_per_ligand', 'measurements_per_metal', 'metals_per_ligand', 'pka_per_ligand']

---

### Step 13: `db_ranked_pairs`
**Args:**
```json
{
  "rank_by": "measurements_per_ligand",
  "limit": 80,
  "where": "(lc.metal_id = 61 OR lc.metal_id = 62)"
}
```

[summary]
## db_ranked_pairs - measurements_per_ligand

| ligand_id | name | count |
|-----------|------|-------|
| ligand_10076 | Hydroxide ion | 51 |
| ligand_10092 | Hydrogen thiocyanate (Thiocyanic acid) | 41 |
| ligand_10103 | Ammonia | 32 |
| ligand_6165 | Nitrilotriacetic acid (NTA) | 23 |
| ligand_10106 | Hydrogen azide (Hydrazoic acid) | 22 |
| ligand_6301 | trans-1,2-Cyclohexylenedinitrilotetraacetic acid (CDTA) | 20 |
| ligand_6277 | Ethylenedinitrilotetraacetic acid (EDTA) | 20 |
| ligand_5760 | Aminoacetic acid (Glycine) | 20 |
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) | 19 |
| ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | 17 |
| ligand_8873 | Propanedioic acid (Malonic acid) | 17 |
| ligand_8465 | Ethanoic acid (Acetic acid) | 17 |
| ligand_6371 | 1,4-Bis[2,5,5-tris(carboxymethyl)-2,5-diazapentyl]benzene (… | 17 |
| ligand_10113 | Hydrogen phosphate (Phosphoric acid) | 16 |
| ligand_9358 | 1,2-Dihydroxybenzene-3,5-disulfonic acid (Tiron) | 16 |
| ligand_8434 | Pyridine-2,6-diphosphonic acid (2,6-PDPA) | 16 |
| ligand_8191 | 1,10-Phenanthroline (Dipyridino[a,c]benzene) | 16 |
| ligand_7673 | 3,7,11,15-Tetraaza-5,13(2)-dihydroxy-5,13(5)-dimethyl-1,9(2… | 16 |
| ligand_10163 | Chloride ion | 15 |
| ligand_6356 | Diethylenetrinitrilopentaacetic acid (DTPA) | 15 |
| ligand_6275 | N-(2-Hydroxyethyl)ethylenedinitrilotriacetic acid (HEDTA) | 15 |
| ligand_10162 | Hydrogen fluoride (Hydrofluoric acid) | 14 |
| ligand_9297 | 4-Amino-2-hydroxybenzoic acid (p-Aminosalicylic acid) | 13 |
| ligand_8872 | Ethanedioic acid (Oxalic acid) | 13 |
| ligand_8126 | 8-Hydroxyquinoline (8-Quinolinol)(Oxine) | 13 |
| ligand_5828 | L-2-Amino-3-hydroxypropanoic acid (Serine) | 13 |
| ligand_9873 | Acetohydroxamic acid | 12 |
| ligand_9526 | Pentane-2,4-dione (Acetylacetone) | 12 |
| ligand_6995 | DL-2-Amino-3-hydroxybutanohydroxamic acid (Threoninehydroxa… | 12 |
| ligand_6770 | Pyridine-2-phosphonic-6-carboxylic acid (2PP6C) | 12 |
| ligand_8156 | 2,2'-Bipyridyl | 11 |
| ligand_7000 | Glycylglycylglycinehydroxamic acid | 11 |
| ligand_6994 | DL-2-Amino-3-hydroxypropanohydroxamic acid (Serinehydroxami… | 11 |
| ligand_6985 | DL-2-Aminopentanohydroxamic acid (Norvalinehydroxamic acid) | 11 |
| ligand_6366 | Triethylenetetranitrilohexaacetic acid (TTHA) | 11 |
| ligand_6288 | meso-(1,2-Dimethylethylene)dinitrilotetraacetic acid | 11 |
| ligand_6287 | rac-(1,2-Dimethylethylene)dinitrilotetraacetic acid | 11 |
| ligand_6127 | Iminodiacetic acid (IDA) | 11 |
| ligand_10148 | Hydrogen sulfate ion (Sulfuric acid) | 10 |
| ligand_9360 | 2,3-Dihydroxybenzenecarboxylic acid (o-Pyrocatechuic acid) | 10 |
| ligand_9337 | 1,2-Dihydroxybenzene (Catechol) | 10 |
| ligand_9284 | 2-Hydroxy-5-sulfobenzoic acid (5-Sulfosalicylic acid) | 10 |
| ligand_8176 | 2-(2-Pyridylmethylenehydrazino)pyridine (Pyridine-2-aldehyd… | 10 |
| ligand_6987 | L-2-Amino-4-methylpentanohydroxamic acid (Leucinehydroxamic… | 10 |
| ligand_5829 | L-2-Amino-3-hydroxybutanoic acid (Threonine) | 10 |
| ligand_9414 | N,N',N''-Tris(2,3-dihydroxybenzoyl)cyclo(O-seryl-O-seryl-O-… | 9 |
| ligand_9361 | 2,4-Dihydroxybenzenecarboxylic acid (b-Resorcylic acid) | 9 |
| ligand_8047 | Pyridine-2-carboxaldehyde oxime | 9 |
| ligand_7029 | Ethylenediamine | 9 |
| ligand_6998 | L-2-Amino-5-guanidopentanohydroxamic acid (Argininehydroxam… | 9 |
| ligand_6982 | Aminoacetohydroxamic acid (Glycinehydroxamic acid) | 9 |
| ligand_6333 | (2-Hydroxytrimethylene)dinitrilotetraacetic acid | 9 |
| ligand_5907 | L-2-Amino-3-(3-indolyl)propanoic acid (Tryptophan) | 9 |
| ligand_10168 | Bromide ion | 8 |
| ligand_9884 | Benzohydroxamic acid | 8 |
| ligand_9593 | 5-Hydroxy-2-hydroxymethyl-4-pyrone (Kojic acid) | 8 |
| ligand_9096 | rac-3,6-Dioxaoctane-1,2,4,5,7,8-hexacarboxylic acid (TDS) | 8 |
| ligand_8955 | D-2,3-Dihydroxybutanedioic acid (D-Tartaric acid) | 8 |
| ligand_6996 | L-2-Amino-3-(4-imidazolyl)propanohydroxamic acid (Histidine… | 8 |
| ligand_6986 | DL-2-Aminohexanohydroxamic acid (Norleucinehydroxamic acid) | 8 |
| ligand_6204 | N-(2-Hydroxyethyl)iminodiacetic acid (HIDA) | 8 |
| ligand_5937 | N-(Phosphonomethyl)glycine (Glyphosate) | 8 |
| ligand_5777 | L-2-Amino-3-phenylpropanoic acid (Phenylalanine) | 8 |
| ligand_9402 | N,N',N''-Tris(2,3-dihydroxybenzoyl)-O-seryl-O-serylserine (… | 7 |
| ligand_9364 | 3,4-Dihydroxybenzenecarboxylic acid (Protocatechuic acid) | 7 |
| ligand_8360 | Amino(phenyl)methylenediphosphonic acid | 7 |
| ligand_8193 | 5-Methyl-1,10-phenanthroline | 7 |
| ligand_7953 | 1,2-Dihydroxypyridin-2-one | 7 |
| ligand_7944 | 2,3-Dihydroxypyridine (3-Hydroxy-1,2-dihydropyridin-2-one) … | 7 |
| ligand_6253 | N-(2-Aminoethyl)iminodiacetic acid (Ethylenediamine-N,N-dia… | 7 |
| ligand_6188 | DL-2-(2-Methylthioethyl)nitrilotriacetic acid | 7 |
| ligand_6135 | L-2-(Carboxymethyl)iminodiacetic acid | 7 |
| ligand_5898 | L-2-Amino-3-(4-imidazolyl)propanoic acid (Histidine) | 7 |
| ligand_10090 | Hydrogen cyanide (Hydrocyanic acid) | 6 |
| ligand_9910 | Desferriferrioxamin B | 6 |
| ligand_9483 | 2,3-Dihydroxynaphthalene-6-sulfonic acid | 6 |
| ligand_9410 | 1,3,5-Tris(2,3-dihydroxy-5-sulfobenzoylaminomethyl)benzene … | 6 |
| ligand_8998 | Thiodiacetic acid | 6 |
| ligand_8479 | 3-Methylbutanoic acid (Isovaleric acid) | 6 |
| ligand_8473 | 2-Methylpropanoic acid (Isobutyric acid) | 6 |

---

### Step 14: `search_stability`
**Args:**
```json
{
  "where": "((c.metal_id = metal_61 OR c.metal_id = metal_62) AND (c.ligand_class_name LIKE '%amide%' OR c.ligand_class_name LIKE '%nitrile%' OR c.ligand_class_name LIKE '%ether%' OR c.ligand_class_name LIKE '%glycol%' OR c.ligand_class_name LIKE '%diol%' OR c.ligand_class_name LIKE '%cyclic ketone%'))",
  "order_by": "c.ligand_class_name, c.ligand_name_SRD, s.constant_type, s.constant_value DESC",
  "limit": 120
}
```

[summary]
## search_stability — 36 row(s)

### logK — 19 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_9593 | 5-Hydroxy-2-hydroxymethyl-4… | HL | O=c1cc(CO)occ1O | 8 | 7 | 15~25 | 0.1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_9586 | 3-Hydroxy-2-methyl-4-pyrone… | HL | Cc1occc(=O)c1O | 5 | 5 | 25 | 2 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9579 | 1-Hydroxy-2-oxocyclohepta-3… | H2L | O=c1ccc(S(=O)(=O)O)ccc1O | 3 | 3 | 25 | 2 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9605 | 3,6-Dichloro-2,5-dihydroxy-… | H2L | O=C1C(O)=C(Cl)C(=O)C(O)=C1Cl | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_9601 | L-3,4-Dihydroxy-5-(1,2-dihy… | H2L | O=C1O[C@H]([C@@H](O)CO)C(O)=C1O | 2 | 2 | 25 | 3 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9570 | 1-Hydroxy-4-(1-methylethyl)… | HL | CC(C)c1cccc(O)c(=O)c1 | 1 | 1 | 25 | 2 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9571 | 1-Hydroxy-5-(1-methylethyl)… | HL | CC(C)c1ccc(O)c(=O)cc1 | 1 | 1 | 25 | 2 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9568 | 1-Hydroxycyclohepta-3,5,7-t… | HL | O=c1cccccc1O | 1 | 1 | 25 | 2 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9575 | 3-Bromo-1-hydroxycyclohepta… | HL | O=c1c(O)ccccc1Br | 1 | 1 | 25 | 2 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9572 | 3-Cyano-1-hydroxycyclohepta… | HL | N#Cc1ccccc(O)c1=O | 1 | 1 | 25 | 2 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9580 | 4-Acetyl-1-hydroxycyclohept… | HL | CC(=O)c1cccc(O)c(=O)c1 | 1 | 1 | 25 | 2 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9581 | 4-Amino-1-hydroxycyclohepta… | HL | Nc1cccc(O)c(=O)c1 | 1 | 1 | 25 | 2 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9576 | 4-Bromo-1-hydroxycyclohepta… | HL | O=c1cc(Br)cccc1O | 1 | 1 | 25 | 2 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9577 | 5-Bromo-1-hydroxycyclohepta… | HL | O=c1ccc(Br)ccc1O | 1 | 1 | 25 | 2 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9574 | 5-Chloro-1-hydroxycyclohept… | HL | O=c1ccc(Cl)ccc1O | 1 | 1 | 25 | 2 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9573 | 5-Cyano-1-hydroxycyclohepta… | HL | N#Cc1ccc(O)c(=O)cc1 | 1 | 1 | 25 | 2 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9578 | 5-Nitro-1-hydroxycyclohepta… | HL | O=c1ccc([N+](=O)[O-])ccc1O | 1 | 1 | 25 | 2 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9564 | Dihydroxycyclobutenedione (… | H2L | O=c1c(O)c(O)c1=O | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9601 | L-3,4-Dihydroxy-5-(1,2-dihy… | H2L | O=C1O[C@H]([C@@H](O)CO)C(O)=C1O | 1 | 1 | 25 | 0.1 | *** | 1 |

### ΔH — 1 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_9601 | L-3,4-Dihydroxy-5-(1,2-dihy… | H2L | O=C1O[C@H]([C@@H](O)CO)C(O)=C1O | 1 | 1 | 25 | 0.1 | *** | 0 |

### ΔS — 1 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_9601 | L-3,4-Dihydroxy-5-(1,2-dihy… | H2L | O=C1O[C@H]([C@@H](O)CO)C(O)=C1O | 1 | 1 | 25 | 0.1 | *** | 0 |

---
