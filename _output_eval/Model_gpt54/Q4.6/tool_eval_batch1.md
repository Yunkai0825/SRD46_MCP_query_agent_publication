# Q4.6 — Tool Results (batch 1)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Mn(II), Fe(II), Co(II), Ni(II), Cu(II), Zn(II)",
  "limit": 20
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
  "name": "EDTA, NTA, DTPA, EGTA, citrate, oxalate, malonate, acetate, glycine, histidine, imidazole, ammonia, ethylenediamine, 1,10-phenanthroline, 2,2'-bipyridine, cyanide, thiocyanate, cysteine, mercaptoacetate, cyclam, cyclen, porphyrin",
  "limit": 100
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
  "symbol": "Mn, Fe, Co, Ni, Cu, Zn",
  "limit": 20
}
```

[summary]
## search_metals

*(no results)*

---

### Step 7: `search_ligands`
**Args:**
```json
{
  "name": "ethylenediamine, phenanthroline, bipyridine, glycine, histidine, citrate, oxalate, malonate, acetate, EDTA, NTA, DTPA, EGTA, ammonia, imidazole, cyanide, thiocyanate, cysteine, mercaptoacetate, cyclam, cyclen, porphyrin",
  "limit": 100
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 9: `db_ranked_pairs`
**Args:**
```json
{
  "rank_by": "measurement_count",
  "limit": 30,
  "where": "metal_names = '[''Manganese'', ''Iron'', ''Cobalt'', ''Nickel'', ''Copper'', ''Zinc'']'"
}
```

[summary]
**db_ranked_pairs:** Error - Unknown rank_by='measurement_count'. Choose from: ['ligands_per_metal', 'measurements_per_ligand', 'measurements_per_metal', 'metals_per_ligand', 'pka_per_ligand']

---

### Step 10: `db_ranked_pairs`
**Args:**
```json
{
  "rank_by": "metals_per_ligand",
  "limit": 50,
  "where": "metal_names = '[''Manganese'', ''Iron'', ''Cobalt'', ''Nickel'', ''Copper'', ''Zinc'']'"
}
```

[TOOL ERROR] db_ranked_pairs: Error executing tool db_ranked_pairs: no such column: metal_names

---

### Step 11: `db_ranked_pairs`
**Args:**
```json
{
  "rank_by": "metals_per_ligand",
  "limit": 50
}
```

[summary]
## db_ranked_pairs - metals_per_ligand

| ligand_id | name | count |
|-----------|------|-------|
| ligand_10076 | Hydroxide ion | 98 |
| ligand_10163 | Chloride ion | 81 |
| ligand_10162 | Hydrogen fluoride (Hydrofluoric acid) | 78 |
| ligand_6277 | Ethylenedinitrilotetraacetic acid (EDTA) | 75 |
| ligand_10148 | Hydrogen sulfate ion (Sulfuric acid) | 74 |
| ligand_6165 | Nitrilotriacetic acid (NTA) | 71 |
| ligand_8465 | Ethanoic acid (Acetic acid) | 69 |
| ligand_10092 | Hydrogen thiocyanate (Thiocyanic acid) | 65 |
| ligand_6301 | trans-1,2-Cyclohexylenedinitrilotetraacetic acid (CDTA) | 61 |
| ligand_6356 | Diethylenetrinitrilopentaacetic acid (DTPA) | 59 |
| ligand_8872 | Ethanedioic acid (Oxalic acid) | 59 |
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) | 57 |
| ligand_10109 | Nitrate ion | 55 |
| ligand_6275 | N-(2-Hydroxyethyl)ethylenedinitrilotriacetic acid (HEDTA) | 54 |
| ligand_6127 | Iminodiacetic acid (IDA) | 52 |
| ligand_10113 | Hydrogen phosphate (Phosphoric acid) | 52 |
| ligand_8873 | Propanedioic acid (Malonic acid) | 51 |
| ligand_8955 | D-2,3-Dihydroxybutanedioic acid (D-Tartaric acid) | 51 |
| ligand_10168 | Bromide ion | 51 |
| ligand_5760 | Aminoacetic acid (Glycine) | 50 |
| ligand_8640 | Hydroxyacetic acid (Glycolic acid) | 50 |
| ligand_9526 | Pentane-2,4-dione (Acetylacetone) | 49 |
| ligand_8641 | D-2-Hydroxypropanoic acid (Lactic acid) | 46 |
| ligand_6311 | Trimethylenedinitrilotetraacetic acid (TMDTA) | 45 |
| ligand_8974 | Oxydiacetic acid (Diglycolic acid) | 45 |
| ligand_6366 | Triethylenetetranitrilohexaacetic acid (TTHA) | 44 |
| ligand_6342 | Ethylenebis(oxyethylenenitrilo)tetraacetic acid (EGTA) | 43 |
| ligand_6204 | N-(2-Hydroxyethyl)iminodiacetic acid (HIDA) | 42 |
| ligand_9358 | 1,2-Dihydroxybenzene-3,5-disulfonic acid (Tiron) | 42 |
| ligand_6762 | Pyridine-2-carboxylic acid (Picolinic acid) | 41 |
| ligand_8938 | Benzene-1,2-dicarboxylic acid (Phthalic acid) | 41 |
| ligand_8953 | L-Hydroxybutanedioic acid (Hydroxysuccinic acid)(Malic acid) | 41 |
| ligand_9337 | 1,2-Dihydroxybenzene (Catechol) | 41 |
| ligand_8467 | Propanoic acid (Propionic acid) | 40 |
| ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | 40 |
| ligand_10173 | Hydrogen iodate (Iodic acid) | 40 |
| ligand_6278 | DL-(Methylethylene)dinitrilotetraacetic acid (PDTA) | 39 |
| ligand_8464 | Methanoic acid (Formic acid) | 39 |
| ligand_8907 | Butanedioic acid (Succinic acid) | 39 |
| ligand_10096 | Hydrogen carbonate (Carbonic acid) | 39 |
| ligand_6140 | N-Methyliminodiacetic acid (MIDA) | 38 |
| ligand_5802 | L-Aminobutanedioic acid (Aspartic acid) | 37 |
| ligand_6102 | 1,4,7,10-Tetraazacyclododecane-N,N',N'',N'''-tetraacetic ac… | 37 |
| ligand_6335 | Oxybis(ethylenenitrilo)tetraacetic acid (EEDTA) | 37 |
| ligand_6793 | N-(2-Pyridylmethyl)iminodiacetic acid | 37 |
| ligand_8558 | Chloroacetic acid | 37 |
| ligand_9284 | 2-Hydroxy-5-sulfobenzoic acid (5-Sulfosalicylic acid) | 37 |
| ligand_10114 | Hydrogen diphosphate (Pyrophosphoric acid) | 37 |
| ligand_6315 | Hexamethylenedinitrilotetraacetic acid | 35 |
| ligand_6333 | (2-Hydroxytrimethylene)dinitrilotetraacetic acid | 35 |

---

### Step 12: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id IN (ligand_6277, ligand_6165, ligand_6356, ligand_6342, ligand_9058, ligand_8872, ligand_8873, ligand_5760) AND c.metal_name_SRD IN ('Manganese','Iron','Cobalt','Nickel','Copper','Zinc') AND s.reaction_type = 'overall' AND s.solvent_name LIKE '%water%' AND s.temperature_c BETWEEN 20 AND 30 AND s.ionic_strength_mol_l IS NOT NULL)",
  "order_by": "c.ligand_id ASC, s.temperature_c ASC, s.ionic_strength_mol_l ASC, s.constant_value DESC",
  "limit": 500
}
```

[summary]
## search_stability

*(no results)*

---

### Step 13: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id IN (ligand_6277, ligand_6165, ligand_6356, ligand_6342, ligand_9058, ligand_8872, ligand_8873, ligand_5760) AND c.metal_id IN (25,26,27,28,29,30) AND s.temperature_c BETWEEN 20 AND 30 AND s.ionic_strength_mol_l IS NOT NULL)",
  "order_by": "c.ligand_id ASC, c.metal_id ASC, s.temperature_c ASC, s.ionic_strength_mol_l ASC, s.constant_value DESC",
  "limit": 500
}
```

[summary]
## search_stability — 200 row(s)

### logK — 26 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_26 | Cd^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 12 | 3 | 25 | 0~1 | *** | 4 |
| metal_26 | Cd^[2+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 12 | 3 | 25 | 1~2 | *** | 4 |
| metal_27 | Ce^[3+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 10 | 5 | 20~25 | 0~1 | solid | 3 |
| metal_26 | Cd^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 9 | 4 | 25 | 0~3 | *** | 5 |
| metal_25 | Ca^[2+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 8 | 2 | 20~25 | 0~1 | *** | 5 |
| metal_26 | Cd^[2+] | ligand_8873 | Propanedioic acid (Malonic … | H2L | O=C(O)CC(=O)O | 7 | 3 | 20~25 | 0~1 | *** | 4 |
| metal_25 | Ca^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 6 | 2 | 20~25 | 0~3 | *** | 5 |
| metal_25 | Ca^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 6 | 2 | 20~25 | 0.1~1 | *** | 4 |
| metal_25 | Ca^[2+] | ligand_8873 | Propanedioic acid (Malonic … | H2L | O=C(O)CC(=O)O | 6 | 2 | 25 | 0~1 | *** | 4 |
| metal_26 | Cd^[2+] | ligand_6342 | Ethylenebis(oxyethylenenitr… | H4L | O=C(O)CN(CCOCCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 5 | 2 | 20~25 | 0.1~3 | *** | 3 |
| metal_25 | Ca^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 5 | 3 | 20~25 | 0.1 | *** | 2 |
| metal_26 | Cd^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 5 | 3 | 20~25 | 0.1 | *** | 2 |
| metal_25 | Ca^[2+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 5 | 3 | 20~25 | 0~0.1 | solid | 3 |
| metal_27 | Ce^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 4 | 3 | 20~25 | 0.1~0.5 | *** | 2 |
| metal_26 | Cd^[2+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_29 | Cf^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 3 | 2 | 25 | 0.1~0.5 | *** | 2 |
| metal_27 | Ce^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 3 | 2 | 25 | 0.1~1 | *** | 3 |
| metal_25 | Ca^[2+] | ligand_6342 | Ethylenebis(oxyethylenenitr… | H4L | O=C(O)CN(CCOCCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 3 | 2 | 20~25 | 0.1~0.5 | *** | 2 |
| metal_29 | Cf^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1 | *** | 2 |
| metal_27 | Ce^[3+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 2 |
| metal_29 | Cf^[3+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1 | *** | 2 |
| metal_29 | Cf^[3+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_27 | Ce^[3+] | ligand_8873 | Propanedioic acid (Malonic … | H2L | O=C(O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_27 | Ce^[3+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 20 | 2 | *** | 1 |
| metal_27 | Ce^[3+] | ligand_6342 | Ethylenebis(oxyethylenenitr… | H4L | O=C(O)CN(CCOCCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_29 | Cf^[3+] | ligand_6342 | Ethylenebis(oxyethylenenitr… | H4L | O=C(O)CN(CCOCCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |

### ΔH — 17 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_26 | Cd^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 6 | 3 | 25 | 0~1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 4 | 1 | 25 | 0~1 | *** | 0 |
| metal_26 | Cd^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 3 | 3 | 25 | 0 | *** | 0 |
| metal_26 | Cd^[2+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 3 | 3 | 20~25 | 0.1 | *** | 0 |
| metal_27 | Ce^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 3 | 2 | 20~25 | 0.1~0.5 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 2 | 2 | 25 | 0 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 2 | 2 | 20 | 0.1 | *** | 0 |
| metal_27 | Ce^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6342 | Ethylenebis(oxyethylenenitr… | H4L | O=C(O)CN(CCOCCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1 | *** | 0 |
| metal_26 | Cd^[2+] | ligand_6342 | Ethylenebis(oxyethylenenitr… | H4L | O=C(O)CN(CCOCCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1 | *** | 0 |
| metal_26 | Cd^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_8873 | Propanedioic acid (Malonic … | H2L | O=C(O)CC(=O)O | 2 | 2 | 25 | 0~0.1 | *** | 0 |
| metal_27 | Ce^[3+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 2 | *** | 0 |
| metal_27 | Ce^[3+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_26 | Cd^[2+] | ligand_8873 | Propanedioic acid (Malonic … | H2L | O=C(O)CC(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_27 | Ce^[3+] | ligand_8873 | Propanedioic acid (Malonic … | H2L | O=C(O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |

### ΔS — 17 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_26 | Cd^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 6 | 3 | 25 | 0~1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 4 | 1 | 25 | 0.1~1 | *** | 0 |
| metal_26 | Cd^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 3 | 3 | 25 | 0 | *** | 0 |
| metal_26 | Cd^[2+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 3 | 3 | 25 | 0.1 | *** | 0 |
| metal_27 | Ce^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 3 | 2 | 25 | 0.1~0.5 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 2 | 2 | 25 | 0~0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_27 | Ce^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_8873 | Propanedioic acid (Malonic … | H2L | O=C(O)CC(=O)O | 2 | 2 | 25 | 0~0.1 | *** | 0 |
| metal_27 | Ce^[3+] | ligand_8873 | Propanedioic acid (Malonic … | H2L | O=C(O)CC(=O)O | 2 | 2 | 25 | 0.1~1 | *** | 0 |
| metal_27 | Ce^[3+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 20 | 2 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6342 | Ethylenebis(oxyethylenenitr… | H4L | O=C(O)CN(CCOCCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_26 | Cd^[2+] | ligand_6342 | Ethylenebis(oxyethylenenitr… | H4L | O=C(O)CN(CCOCCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_26 | Cd^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_27 | Ce^[3+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_26 | Cd^[2+] | ligand_8873 | Propanedioic acid (Malonic … | H2L | O=C(O)CC(=O)O | 1 | 1 | 25 | 0 | *** | 0 |

---

### Step 14: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_name_SRD IN ('Mn^[2+]','Fe^[2+]','Co^[2+]','Ni^[2+]','Cu^[2+]','Zn^[2+]') AND s.temperature_c BETWEEN 20 AND 30 AND s.solvent_name IS NOT NULL)",
  "order_by": "c.ligand_id ASC, c.metal_name_SRD ASC",
  "limit": 300
}
```

[summary]
## search_stability — 200 row(s)

### logK — 16 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_112 | Ni^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 18 | 3 | 25 | 0~3 | *** | 6 |
| metal_33 | Co^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 13 | 4 | 25 | 0~1 | *** | 4 |
| metal_41 | Cu^[2+] | ligand_5761 | L-2-Aminopropanoic acid (Al… | HL | C[C@H](N)C(=O)O | 13 | 3 | 25 | 0~5 | *** | 6 |
| metal_41 | Cu^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 12 | 2 | 25 | 0~2.5 | *** | 6 |
| metal_208 | Zn^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 12 | 3 | 25 | 0~1 | *** | 4 |
| metal_112 | Ni^[2+] | ligand_5761 | L-2-Aminopropanoic acid (Al… | HL | C[C@H](N)C(=O)O | 11 | 3 | 25 | 0~1 | *** | 4 |
| metal_208 | Zn^[2+] | ligand_5761 | L-2-Aminopropanoic acid (Al… | HL | C[C@H](N)C(=O)O | 11 | 4 | 25 | 0~1 | *** | 4 |
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 8 | 3 | 20~25 | 0~3 | *** | 5 |
| metal_94 | Mn^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 5 | 2 | 25 | 0~0.5 | *** | 3 |
| metal_33 | Co^[2+] | ligand_5761 | L-2-Aminopropanoic acid (Al… | HL | C[C@H](N)C(=O)O | 5 | 3 | 25 | 0~0.1 | *** | 2 |
| metal_41 | Cu^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 5 | 3 | 25 | 0.1~5 | *** | 2 |
| metal_94 | Mn^[2+] | ligand_5761 | L-2-Aminopropanoic acid (Al… | HL | C[C@H](N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5761 | L-2-Aminopropanoic acid (Al… | HL | C[C@H](N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |

### ΔH — 13 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_112 | Ni^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 8 | 3 | 25 | 0~1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_5761 | L-2-Aminopropanoic acid (Al… | HL | C[C@H](N)C(=O)O | 5 | 3 | 25 | 0.1~1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 4 | 2 | 25 | 0~0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 4 | 3 | 25 | 0~0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 3 | 3 | 25 | 0 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5761 | L-2-Aminopropanoic acid (Al… | HL | C[C@H](N)C(=O)O | 3 | 2 | 25 | 0.1~0.5 | *** | 0 |
| metal_33 | Co^[2+] | ligand_5761 | L-2-Aminopropanoic acid (Al… | HL | C[C@H](N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5761 | L-2-Aminopropanoic acid (Al… | HL | C[C@H](N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |

### ΔS — 12 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_112 | Ni^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 8 | 3 | 25 | 0~1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 6 | 3 | 25 | 0~0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 5 | 3 | 25 | 0~0.1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_5761 | L-2-Aminopropanoic acid (Al… | HL | C[C@H](N)C(=O)O | 5 | 3 | 25 | 0.1~1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 4 | 2 | 25 | 0~0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5761 | L-2-Aminopropanoic acid (Al… | HL | C[C@H](N)C(=O)O | 3 | 2 | 25 | 0.1~0.5 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 2 | 1 | 25 | 0~0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_5761 | L-2-Aminopropanoic acid (Al… | HL | C[C@H](N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5761 | L-2-Aminopropanoic acid (Al… | HL | C[C@H](N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 0 | *** | 0 |

---
