# Qfree_20260424_005101 — Tool Results (batch 1)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Fe(II), Fe(III), H+",
  "limit": 20
}
```

[summary]
## search_metals

*(no results)*

---

### Step 3: `search_metals`
**Args:**
```json
{
  "symbol": "Fe, H",
  "limit": 20
}
```

[summary]
## search_metals

*(no results)*

---

### Step 5: `get_table_schema`
**Args:**
```json
{
  "table_name": "ligandmetal_card",
  "database": "equilibrium"
}
```

[summary]
**get_table_schema:** Error - Table 'ligandmetal_card' not found.
Available tables: eq_collection_unassigned, eq_edge, eq_edge_species, eq_export_metadata, eq_map, eq_map_collection, eq_map_stray, eq_network, eq_network_species, eq_node, eq_node_species, sqlite_sequence

---

### Step 6: `get_table_schema`
**Args:**
```json
{
  "table_name": "ligandmetal_stability_measured",
  "database": "equilibrium"
}
```

[summary]
**get_table_schema:** Error - Table 'ligandmetal_stability_measured' not found.
Available tables: eq_collection_unassigned, eq_edge, eq_edge_species, eq_export_metadata, eq_map, eq_map_collection, eq_map_stray, eq_network, eq_network_species, eq_node, eq_node_species, sqlite_sequence

---

### Step 7: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_card",
  "group_column": "metal_name_SRD",
  "where": "metal_name_SRD LIKE '%Fe%' OR metal_name_SRD LIKE '%iron%'",
  "limit": 50
}
```

[summary]
## db_distribution - ligandmetal_card by metal_name_SRD

**total_rows:** 2140

| value | count | pct |
|-------|-------|-----|
| Fe^[3+] | 1473 | 68.83% |
| Fe^[2+] | 667 | 31.17% |

---

### Step 8: `search_stability`
**Args:**
```json
{
  "sql_where_query": "(c.metal_name_SRD = 'Fe^[3+]' OR c.metal_name_SRD = 'Fe^[2+]') AND NOT s.temperature_c IS NULL ORDER BY c.ligand_id, c.metal_name_SRD",
  "include_groups": [
    "carboxylate",
    "aminocarboxylate",
    "hydroxamate",
    "phosphonate",
    "phenolate",
    "catecholate",
    "N-donor",
    "hydroxycarboxylate"
  ],
  "exclude_groups": [
    "macrocycle"
  ],
  "ligand_similarity": false
}
```

[summary]
## search_stability — 7 row(s)

### `Fe^[3+]` + rac-Trimethylenebis[2-(2-hydroxy-3,5-dimethylphenyl)glycine… — 3 measurement(s)
metal_id: metal_61 | ligand_id: ligand_5997
ligand_HxL_def: *** | ligand_SMILES: ***

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_101158 | ref_eq_map_2099 | beta_def_812 | logK | 34.22 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (-12.56, L, +inf) |
| vlm_101159 | ref_eq_map_2099 | beta_def_788 | logK | 2.71 | 25 | 0.1 | `[ML] + [H] <=> [MHL]` | *** |  |  |
| vlm_101160 | ref_eq_map_2099 | beta_def_966 | logK | 11.31 | 25 | 0.1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |

### `Fe^[3+]` + N,N"-Bis(2-hydroxybenzyl)diethylenetrinitrilo-N,N',N"-triac… — 4 measurement(s)
metal_id: metal_61 | ligand_id: ligand_6039
ligand_HxL_def: *** | ligand_SMILES: ***

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_102104 | ref_eq_map_2442 | beta_def_812 | logK | 30.44 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (-12.43, L, +inf) |
| vlm_102105 | ref_eq_map_2442 | beta_def_788 | logK | 8.81 | 25 | 0.1 | `[ML] + [H] <=> [MHL]` | *** |  |  |
| vlm_102106 | ref_eq_map_2442 | beta_def_739 | logK | 4.89 | 25 | 0.1 | `[MHL] + [H] <=> [MH2L]` | *** |  |  |
| vlm_102107 | ref_eq_map_2442 | beta_def_751 | logK | -1.2 | 25 | 0.1 | `[MH2L] + [H] <=> [MH3L]` | *** |  |  |

---

### Step 9: `db_ranked_pairs`
**Args:**
```json
{
  "rank_by": "measurement_count",
  "where": "metal_name_SRD IN ('Fe^[3+]', 'Fe^[2+]')",
  "limit": 100
}
```

[summary]
**db_ranked_pairs:** Error - Unknown rank_by='measurement_count'. Choose from: ['ligands_per_metal', 'measurements_per_ligand', 'measurements_per_metal', 'metals_per_ligand', 'pka_per_ligand']

---

### Step 10: `search_pka_values`
**Args:**
```json
{
  "sql_where_query": "p.pKa BETWEEN 0 AND 12 ORDER BY lc.ligand_id",
  "include_groups": [
    "carboxylate",
    "aminocarboxylate",
    "hydroxamate",
    "phosphonate",
    "phenolate",
    "catecholate",
    "N-donor",
    "hydroxycarboxylate"
  ],
  "exclude_groups": [
    "macrocycle"
  ],
  "ligand_similarity": false
}
```

[summary]
## search_pka_values

*(no results)*

---

### Step 11: `search_stability`
**Args:**
```json
{
  "sql_where_query": "c.metal_name_SRD = 'Fe^[2+]' ORDER BY s.constant_value ASC",
  "include_groups": [
    "carboxylate",
    "aminocarboxylate",
    "hydroxamate",
    "phosphonate",
    "phenolate",
    "catecholate",
    "N-donor",
    "hydroxycarboxylate"
  ],
  "exclude_groups": [
    "macrocycle"
  ],
  "ligand_similarity": false
}
```

[summary]
## search_stability — 12 row(s)

### `Fe^[2+]` + Hydroxide ion — 8 measurement(s)
metal_id: metal_62 | ligand_id: ligand_10076
ligand_HxL_def: *** | ligand_SMILES: ***

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_170679 | *** | beta_def_840 | ΔS | -167.4 | 25 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (13.78, L, +inf) |
| vlm_170682 | *** | beta_def_872 | ΔS | -104.6 | 25 | 0 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (13.78, L, +inf) |
| vlm_170676 | *** | beta_def_812 | ΔS | -83.7 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (13.78, L, +inf) |
| vlm_170684 | ref_eq_map_27358 | beta_def_334 | logK | -14.43 | 25 | 0 | `[ML2(s)] <=> [M] + [L]^2` | solid | [L] | (13.78, L, +inf) |
| vlm_170678 | *** | beta_def_840 | ΔH | -8.4 | 25 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (13.78, L, +inf) |
| vlm_170677 | ref_eq_map_27358 | beta_def_840 | logK | -7.5 | 25 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (13.78, L, +inf) |
| vlm_170675 | *** | beta_def_812 | ΔH | 0 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (13.78, L, +inf) |
| vlm_170681 | *** | beta_def_872 | ΔH | 0 | 25 | 0 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (13.78, L, +inf) |

### `Fe^[2+]` + Chloride ion — 2 measurement(s)
metal_id: metal_62 | ligand_id: ligand_10163
ligand_HxL_def: *** | ligand_SMILES: ***

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_177346 | *** | beta_def_334 | ΔH | -82.8 | 25 | 0 | `[ML2(s)] <=> [M] + [L]^2` | solid | [L] |  |
| vlm_177345 | ref_eq_map_29714 | beta_def_812 | logK | -0.2 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] |  |

### `Fe^[2+]` + N,N',N''-Tris(2,3-dihydroxybenzoyl)cyclo(O-seryl-O-seryl-O-… — 1 measurement(s)
metal_id: metal_62 | ligand_id: ligand_9414
ligand_HxL_def: *** | ligand_SMILES: ***

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_163144 | ref_eq_map_24166 | beta_def_826 | logK | -39.5 | 25 | 0.5 | `[M] + [H6L] <=> [ML] + [H]^6` | *** | [H6L] | (-inf, H6L, 6) |

### `Fe^[2+]` + N,N',N''-Tris(2,3-dihydroxybenzoyl)nitrilotris(ethyleneamin… — 1 measurement(s)
metal_id: metal_62 | ligand_id: ligand_9417
ligand_HxL_def: *** | ligand_SMILES: ***

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_163171 | ref_eq_map_24175 | beta_def_825 | logK | -23.7 | 25 | 0.1 | `[M] + [H3L] <=> [ML] + [H]^3` | *** | [H3L] | (8.75, H3L, +inf) |

---

### Step 12: `db_ranked_pairs`
**Args:**
```json
{
  "rank_by": "measurements_per_ligand",
  "where": "metal_name_SRD IN ('Fe^[3+]', 'Fe^[2+]')",
  "limit": 50
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
| ligand_5760 | Aminoacetic acid (Glycine) | 20 |
| ligand_6277 | Ethylenedinitrilotetraacetic acid (EDTA) | 20 |
| ligand_6301 | trans-1,2-Cyclohexylenedinitrilotetraacetic acid (CDTA) | 20 |
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) | 19 |
| ligand_6371 | 1,4-Bis[2,5,5-tris(carboxymethyl)-2,5-diazapentyl]benzene (… | 17 |
| ligand_8465 | Ethanoic acid (Acetic acid) | 17 |
| ligand_8873 | Propanedioic acid (Malonic acid) | 17 |
| ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | 17 |
| ligand_7673 | 3,7,11,15-Tetraaza-5,13(2)-dihydroxy-5,13(5)-dimethyl-1,9(2… | 16 |
| ligand_8191 | 1,10-Phenanthroline (Dipyridino[a,c]benzene) | 16 |
| ligand_8434 | Pyridine-2,6-diphosphonic acid (2,6-PDPA) | 16 |
| ligand_9358 | 1,2-Dihydroxybenzene-3,5-disulfonic acid (Tiron) | 16 |
| ligand_10113 | Hydrogen phosphate (Phosphoric acid) | 16 |
| ligand_6275 | N-(2-Hydroxyethyl)ethylenedinitrilotriacetic acid (HEDTA) | 15 |
| ligand_6356 | Diethylenetrinitrilopentaacetic acid (DTPA) | 15 |
| ligand_10163 | Chloride ion | 15 |
| ligand_10162 | Hydrogen fluoride (Hydrofluoric acid) | 14 |
| ligand_5828 | L-2-Amino-3-hydroxypropanoic acid (Serine) | 13 |
| ligand_8126 | 8-Hydroxyquinoline (8-Quinolinol)(Oxine) | 13 |
| ligand_8872 | Ethanedioic acid (Oxalic acid) | 13 |
| ligand_9297 | 4-Amino-2-hydroxybenzoic acid (p-Aminosalicylic acid) | 13 |
| ligand_6770 | Pyridine-2-phosphonic-6-carboxylic acid (2PP6C) | 12 |
| ligand_6995 | DL-2-Amino-3-hydroxybutanohydroxamic acid (Threoninehydroxa… | 12 |
| ligand_9526 | Pentane-2,4-dione (Acetylacetone) | 12 |
| ligand_9873 | Acetohydroxamic acid | 12 |
| ligand_6127 | Iminodiacetic acid (IDA) | 11 |
| ligand_6287 | rac-(1,2-Dimethylethylene)dinitrilotetraacetic acid | 11 |
| ligand_6288 | meso-(1,2-Dimethylethylene)dinitrilotetraacetic acid | 11 |
| ligand_6366 | Triethylenetetranitrilohexaacetic acid (TTHA) | 11 |
| ligand_6985 | DL-2-Aminopentanohydroxamic acid (Norvalinehydroxamic acid) | 11 |
| ligand_6994 | DL-2-Amino-3-hydroxypropanohydroxamic acid (Serinehydroxami… | 11 |
| ligand_7000 | Glycylglycylglycinehydroxamic acid | 11 |
| ligand_8156 | 2,2'-Bipyridyl | 11 |
| ligand_5829 | L-2-Amino-3-hydroxybutanoic acid (Threonine) | 10 |
| ligand_6987 | L-2-Amino-4-methylpentanohydroxamic acid (Leucinehydroxamic… | 10 |
| ligand_8176 | 2-(2-Pyridylmethylenehydrazino)pyridine (Pyridine-2-aldehyd… | 10 |
| ligand_9284 | 2-Hydroxy-5-sulfobenzoic acid (5-Sulfosalicylic acid) | 10 |
| ligand_9337 | 1,2-Dihydroxybenzene (Catechol) | 10 |
| ligand_9360 | 2,3-Dihydroxybenzenecarboxylic acid (o-Pyrocatechuic acid) | 10 |
| ligand_10148 | Hydrogen sulfate ion (Sulfuric acid) | 10 |
| ligand_5907 | L-2-Amino-3-(3-indolyl)propanoic acid (Tryptophan) | 9 |
| ligand_6333 | (2-Hydroxytrimethylene)dinitrilotetraacetic acid | 9 |
| ligand_6982 | Aminoacetohydroxamic acid (Glycinehydroxamic acid) | 9 |
| ligand_6998 | L-2-Amino-5-guanidopentanohydroxamic acid (Argininehydroxam… | 9 |
| ligand_7029 | Ethylenediamine | 9 |

---

### Step 13: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_card",
  "group_column": "ligand_class_name",
  "where": "metal_name_SRD IN ('Fe^[3+]', 'Fe^[2+]')",
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

### Step 14: `search_stability`
**Args:**
```json
{
  "sql_where_query": "c.metal_name_SRD IN ('Fe^[3+]', 'Fe^[2+]') AND c.ligand_id IN (6165, 5760, 9058, 8872, 8465, 6127, 6275, 6277, 9257, 9284, 9337, 9358, 8434, 10163, 10092, 10103) ORDER BY c.ligand_id, c.metal_name_SRD, s.constant_type, s.constant_value DESC",
  "ligand_similarity": false
}
```

[summary]
## search_stability — 295 row(s)

### ΔH — 16 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 6 | 3 | 25 | 0~3 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 4 | 4 | 25 | 0.1~1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_10103 | Ammonia | L | N | 4 | 4 | 25 | 2 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 3 | 1 | 10~40 | 0 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 3 | 3 | 25 | 1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 2 | 2 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 1 | 25 | 1~3 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_10163 | Chloride ion | *** | *** | 2 | 1 | 25 | 0~1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9284 | 2-Hydroxy-5-sulfobenzoic ac… | H3L | O=C(O)c1cc(S(=O)(=O)O)ccc1O | 1 | 1 | 25 | 3 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9337 | 1,2-Dihydroxybenzene (Catec… | H2L | Oc1ccccc1O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_10163 | Chloride ion | *** | *** | 1 | 1 | 25 | 0 | solid | 0 |

### logK — 30 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 27 | 5 | 20~25 | 0~5 | *** | 13 |
| metal_62 | Fe^[2+] | ligand_10103 | Ammonia | L | N | 24 | 4 | 25 | 0~6 | *** | 6 |
| metal_61 | Fe^[3+] | ligand_9358 | 1,2-Dihydroxybenzene-3,5-di… | H4L | O=S(=O)(O)c1cc(O)c(O)c(S(=O)(=O)O)c1 | 16 | 4 | 20~25 | 0.1~1 | *** | 4 |
| metal_61 | Fe^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 14 | 8 | 20~25 | 0.1~1 | *** | 4 |
| metal_61 | Fe^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 12 | 5 | 20~25 | 0.1~3 | *** | 5 |
| metal_62 | Fe^[2+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 11 | 5 | 20~37 | 0.1~3 | *** | 5 |
| metal_61 | Fe^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 11 | 3 | 20~25 | 0~3 | *** | 7 |
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 10 | 3 | 10~40 | 0~3 | *** | 7 |
| metal_62 | Fe^[2+] | ligand_8434 | Pyridine-2,6-diphosphonic a… | H4L | O=P(O)(O)c1cccc(P(=O)(O)O)n1 | 10 | 10 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_10163 | Chloride ion | *** | *** | 9 | 2 | 25 | 0~4 | *** | 7 |
| metal_62 | Fe^[2+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 7 | 3 | 20~25 | 0.1~1 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 7 | 5 | 25 | 0.1~1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_9284 | 2-Hydroxy-5-sulfobenzoic ac… | H3L | O=C(O)c1cc(S(=O)(=O)O)ccc1O | 7 | 3 | 20~25 | 0.1~3 | *** | 4 |
| metal_61 | Fe^[3+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 6 | 3 | 25 | 0.5~3 | *** | 3 |
| metal_62 | Fe^[2+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 6 | 2 | 20~25 | 0.1~1 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 6 | 4 | 25 | 0.1~1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_8434 | Pyridine-2,6-diphosphonic a… | H4L | O=P(O)(O)c1cccc(P(=O)(O)O)n1 | 6 | 6 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 6 | 4 | 20~25 | 0.1~1 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 5 | 4 | 25 | 0.1~1 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 5 | 3 | 25 | 0.5~3 | *** | 3 |
| metal_62 | Fe^[2+] | ligand_9337 | 1,2-Dihydroxybenzene (Catec… | H2L | Oc1ccccc1O | 4 | 3 | 25 | 0.1~1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_9337 | 1,2-Dihydroxybenzene (Catec… | H2L | Oc1ccccc1O | 4 | 3 | 25 | 0.1~1 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 2 | 2 | 25 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 2 | 1 | 25 | 0~3 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 1 | 1 | 25 | 3 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_9284 | 2-Hydroxy-5-sulfobenzoic ac… | H3L | O=C(O)c1cc(S(=O)(=O)O)ccc1O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_10163 | Chloride ion | *** | *** | 1 | 1 | 25 | 0 | *** | 1 |

### ΔS — 15 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 6 | 3 | 25 | 0~3 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 4 | 4 | 20~25 | 0.1~1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_10103 | Ammonia | L | N | 4 | 4 | 25 | 2 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 3 | 3 | 25 | 1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 2 | 2 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 1 | 25 | 1~3 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_10163 | Chloride ion | *** | *** | 2 | 1 | 25 | 0~1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9284 | 2-Hydroxy-5-sulfobenzoic ac… | H3L | O=C(O)c1cc(S(=O)(=O)O)ccc1O | 1 | 1 | 25 | 3 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9337 | 1,2-Dihydroxybenzene (Catec… | H2L | Oc1ccccc1O | 1 | 1 | 25 | 1 | *** | 0 |

---

### Step 15: `search_pka_ligands`
**Args:**
```json
{
  "sql_where_query": "lc.ligand_id IN (6165, 5760, 9058, 8872, 8465, 6127, 6275, 6277, 9257, 9284, 9337, 9358, 8434, 10163, 10092, 10103) ORDER BY lc.ligand_id",
  "ligand_similarity": false
}
```

[summary]
## search_pka_ligands — 36 row(s)

| ligand_id | ligand_name | HxL_def | formula | smiles | pH_ladder | T°C_range | I(M)_range | similarity_score |
|-----------|-------------|---------|---------|--------|-----------|-----------|------------|------------------|
| ligand_5760 | Aminoacetic acid (Glycine) | HL | C2H5N1O2 | NCC(=O)O | −∞; H2L (M_tot_1); (2.33, vlm_93627); HL (M_tot_20); (9.57, vlm_93606); L (M_tot_43); +∞ | 25 | 0.1 | *** |
| ligand_6127 | Iminodiacetic acid (IDA) | H2L | C4H7N1O4 | O=C(O)CNCC(=O)O | −∞; H3L (M_tot_1); (-1.77, vlm_104135); H2L (M_tot_1); (2.62, vlm_104120); HL (M_tot_3); (9.34, vlm_104104); L (M_tot_52); +∞ | 25 | 0.1 | *** |
| ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | C6H9N1O6 | O=C(O)CN(CC(=O)O)CC(=O)O | −∞; H3L (M_tot_1); (-1.81, vlm_105204); H2L (M_tot_2); (-1, vlm_105223); H3L (M_tot_1); (2.52, vlm_105186); HL (M_tot_2); (9.46, vlm_105158); L (M_tot_68); +∞ | 25 | 0.1 | *** |
| ligand_6275 | N-(2-Hydroxyethyl)ethylenedinitrilotriacetic acid (HEDTA) | H3L | C10H18N2O7 | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | −∞; H3L (M_tot_1); (2.62, vlm_107963); H2L (M_tot_1); (5.38, vlm_107958); HL (M_tot_5); (9.7, vlm_107949); L (M_tot_47); +∞ | 25 | 0.1 | *** |
| ligand_6277 | Ethylenedinitrilotetraacetic acid (EDTA) | H4L | C10H16N2O8 | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | −∞; H5L (M_tot_1); (-1.5, vlm_108289); H4L (M_tot_2); (2, vlm_108282); H3L (M_tot_2); (2.69, vlm_108272); H2L (M_tot_1); (6.13, vlm_108254); HL (M_tot_7); (9.52, vlm_108224); L (M_tot_70); +∞ | 25 | 0.1 | *** |
| ligand_8434 | Pyridine-2,6-diphosphonic acid (2,6-PDPA) | H4L | C5H7N1O6 | O=P(O)(O)c1cccc(P(=O)(O)O)n1 | −∞; H3L (M_tot_1); (3.14, vlm_143981); H2L (M_tot_1); (4.67, vlm_143980); HL (M_tot_1); (9.12, vlm_143979); L (M_tot_3); +∞ | 25 | 0.1 | *** |
| ligand_8465 | Ethanoic acid (Acetic acid) | HL | C2H4O2 | CC(=O)O | −∞; HL (M_tot_2); (4.56, vlm_144406); L (M_tot_69); +∞ | 25 | 0.1 | *** |
| ligand_8872 | Ethanedioic acid (Oxalic acid) | H2L | C2H2O4 | O=C(O)C(=O)O | −∞; H2L (M_tot_1); (-1.2, vlm_151532); HL (M_tot_7); (3.8, vlm_151494); L (M_tot_56); +∞ | 25 | 0.1 | *** |
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) | H3L | C6H8O7 | O=C(O)CC(O)(CC(=O)O)C(=O)O | −∞; H3L (M_tot_1); (2.9, vlm_157473); H2L (M_tot_12); (4.35, vlm_157459); HL (M_tot_18); (5.65, vlm_157439); L (M_tot_57); +∞ | 25 | 0.1 | *** |
| ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | H2L | C7H6O3 | O=C(O)c1ccccc1O | −∞; HL (M_tot_37); (-13.4, vlm_160211); L (M_tot_3); (2.8, vlm_160226); HL (M_tot_37); +∞ | 25 | 0.1 | *** |
| ligand_9284 | 2-Hydroxy-5-sulfobenzoic acid (5-Sulfosalicylic acid) | H3L | C7H6O6S1 | O=C(O)c1cc(S(=O)(=O)O)ccc1O | −∞; H2L (M_tot_1); (2.48, vlm_160822); HL (M_tot_37); (11.85, vlm_160810); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_9337 | 1,2-Dihydroxybenzene (Catechol) | H2L | C6H6O2 | Oc1ccccc1O | −∞; HL (M_tot_3); (-13.3, vlm_161529); L (M_tot_3); (9.26, vlm_161533); HL (M_tot_3); +∞ | 25 | 0.1 | *** |
| ligand_9358 | 1,2-Dihydroxybenzene-3,5-disulfonic acid (Tiron) | H4L | C6H6O8S2 | O=S(=O)(O)c1cc(O)c(O)c(S(=O)(=O)O)c1 | −∞; HL (M_tot_18); (-12.5, vlm_161952); L (M_tot_1); (7.62, vlm_161957); HL (M_tot_18); +∞ | 25 | 0.1 | *** |
| ligand_10092 | Hydrogen thiocyanate (Thiocyanic acid) | HL | C1H1N1S1 | N=C=S | −∞; HL (M_tot_1); (-1.1, vlm_172116); L (M_tot_65); +∞ | 20 | 0 | *** |
| ligand_10103 | Ammonia | L | H3N1 | N | −∞; HL (M_tot_1); (9.26, vlm_173034); L (M_tot_23); +∞ | 25 | 0.1 | *** |

---

### Step 16: `search_stability`
**Args:**
```json
{
  "sql_where_query": "c.metal_name_SRD IN ('Fe^[3+]', 'Fe^[2+]') AND c.ligand_id IN (8465, 9058, 8872, 9257, 9284, 10092, 6277, 6165, 6275, 6127, 8434, 9337, 9358) ORDER BY c.ligand_id, c.metal_name_SRD, s.constant_type, s.constant_value DESC",
  "ligand_similarity": false
}
```

[summary]
## search_stability — 228 row(s)

### logK — 25 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 27 | 5 | 20~25 | 0~5 | *** | 13 |
| metal_61 | Fe^[3+] | ligand_9358 | 1,2-Dihydroxybenzene-3,5-di… | H4L | O=S(=O)(O)c1cc(O)c(O)c(S(=O)(=O)O)c1 | 16 | 4 | 20~25 | 0.1~1 | *** | 4 |
| metal_61 | Fe^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 14 | 8 | 20~25 | 0.1~1 | *** | 4 |
| metal_61 | Fe^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 12 | 5 | 20~25 | 0.1~3 | *** | 5 |
| metal_62 | Fe^[2+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 11 | 5 | 20~37 | 0.1~3 | *** | 5 |
| metal_61 | Fe^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 11 | 3 | 20~25 | 0~3 | *** | 7 |
| metal_62 | Fe^[2+] | ligand_8434 | Pyridine-2,6-diphosphonic a… | H4L | O=P(O)(O)c1cccc(P(=O)(O)O)n1 | 10 | 10 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 7 | 3 | 20~25 | 0.1~1 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 7 | 5 | 25 | 0.1~1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_9284 | 2-Hydroxy-5-sulfobenzoic ac… | H3L | O=C(O)c1cc(S(=O)(=O)O)ccc1O | 7 | 3 | 20~25 | 0.1~3 | *** | 4 |
| metal_62 | Fe^[2+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 6 | 2 | 20~25 | 0.1~1 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 6 | 4 | 25 | 0.1~1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_8434 | Pyridine-2,6-diphosphonic a… | H4L | O=P(O)(O)c1cccc(P(=O)(O)O)n1 | 6 | 6 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 6 | 4 | 20~25 | 0.1~1 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 5 | 4 | 25 | 0.1~1 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 5 | 3 | 25 | 0.5~3 | *** | 3 |
| metal_62 | Fe^[2+] | ligand_9337 | 1,2-Dihydroxybenzene (Catec… | H2L | Oc1ccccc1O | 4 | 3 | 25 | 0.1~1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_9337 | 1,2-Dihydroxybenzene (Catec… | H2L | Oc1ccccc1O | 4 | 3 | 25 | 0.1~1 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 2 | 2 | 25 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 2 | 1 | 25 | 0~3 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 1 | 1 | 25 | 3 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_9284 | 2-Hydroxy-5-sulfobenzoic ac… | H3L | O=C(O)c1cc(S(=O)(=O)O)ccc1O | 1 | 1 | 20 | 0.1 | *** | 1 |

### ΔH — 12 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 6 | 3 | 25 | 0~3 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 4 | 4 | 25 | 0.1~1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 3 | 3 | 25 | 1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 2 | 2 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 1 | 25 | 1~3 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9284 | 2-Hydroxy-5-sulfobenzoic ac… | H3L | O=C(O)c1cc(S(=O)(=O)O)ccc1O | 1 | 1 | 25 | 3 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9337 | 1,2-Dihydroxybenzene (Catec… | H2L | Oc1ccccc1O | 1 | 1 | 25 | 1 | *** | 0 |

### ΔS — 12 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 6 | 3 | 25 | 0~3 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 4 | 4 | 20~25 | 0.1~1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 3 | 3 | 25 | 1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 2 | 2 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 1 | 25 | 1~3 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9284 | 2-Hydroxy-5-sulfobenzoic ac… | H3L | O=C(O)c1cc(S(=O)(=O)O)ccc1O | 1 | 1 | 25 | 3 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9337 | 1,2-Dihydroxybenzene (Catec… | H2L | Oc1ccccc1O | 1 | 1 | 25 | 1 | *** | 0 |

---

### Step 17: `search_networks`
**Args:**
```json
{
  "sql_where_query": "c.metal_name IN ('Fe^[3+]', 'Fe^[2+]') AND c.ligand_id IN (8465, 9058, 8872, 9257, 9284, 10092, 6277, 6165, 6275, 6127, 8434, 9337, 9358) ORDER BY c.ligand_id, c.metal_name",
  "ligand_similarity": false
}
```

[summary]
## search_networks — 176 row(s)

> **Reference equilibrium networks (compact)** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### Beta-definition legend
| beta_def | equation |
|----------|----------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |
| beta_def_868 | ``[ML] + [L] <=> [ML2]`` |
| beta_def_779 | ``[M] + [HL] <=> [MHL]`` |
| beta_def_966 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` |
| beta_def_238 | ``[M(OH)2L] + [H] <=> [M(OH)L] + [H2O]`` |
| beta_def_263 | ``[M(OH)3L] + [H] <=> [M(OH)2L] + [H2O]`` |
| beta_def_423 | ``[ML]^2 + [H2O]^2 <=> [M2(OH)2L2] + [H]^2`` |
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` |
| beta_def_427 | ``[M(OH)L]^2 <=> [M2(OH)2L2]`` |
| beta_def_786 | ``[M] + [HL] <=> [MHL]`` |
| beta_def_739 | ``[MHL] + [H] <=> [MH2L]`` |
| beta_def_792 | ``[ML2] + [H] <=> [MHL2]`` |
| beta_def_204 | ``[MHL2] + [H] <=> [M(HL)2]`` |
| beta_def_756 | ``[M(HL)2] + [H] <=> [MH3L2]`` |
| beta_def_171 | ``[MH3L2] + [H] <=> [M(H2L)2]`` |
| beta_def_597 | ``[M]^3 + [L]^6 + [H2O]^2 <=> [M3(OH)2L6] + [H]^2`` |
| beta_def_601 | ``[M]^3 + [L]^2 + [H2O]^3 <=> [M3(OH)3L2] + [H]^3`` |
| beta_def_708 | ``[M]^7 + [L]^6 + [H2O]^9 <=> [M7(OH)9L6] + [H]^9`` |
| beta_def_872 | ``[M] + [L]^3 <=> [ML3]`` |
| beta_def_732 | ``[M] + [H2L] <=> [MH2L]`` |
| beta_def_800 | ``[MHL] + [L] <=> [MHL2]`` |
| beta_def_374 | ``[M]^2 + [L]^2 <=> [M2(H-1L)2] + [H]^2`` |
| beta_def_424 | ``[M]^2 + [L]^2 + [H2O]^2 <=> [M2(OH)2L2] + [H]^2`` |
| beta_def_821 | ``[M] + [HL] <=> [ML] + [H]`` |
| beta_def_846 | ``[ML] + [HL] <=> [ML2] + [H]`` |
| beta_def_873 | ``[ML2] + [HL] <=> [ML3] + [H]`` |
| beta_def_497 | ``[M]^2 + [HL]^2 <=> [M2HL2] + [H]`` |
| beta_def_823 | ``[M] + [H2L] <=> [ML] + [H]^2`` |
| beta_def_853 | ``[ML] + [H2L] <=> [ML2] + [H]^2`` |
| beta_def_876 | ``[ML2] + [H2L] <=> [ML3] + [H]^2`` |
| beta_def_981 | ``[ML] + [OH] <=> [M(OH)L]`` |
| beta_def_894 | ``[M] + [L]^4 <=> [ML4]`` |

### Metal-ligand pair summary
| metal | metal_id | ligand | ligand_id | HxL | T_range | I_range | net_count | max_nodes | max_net_id | ligand_SMILES |
|-------|----------|--------|-----------|-----|---------|---------|-----------|----------|------------|---------------|
| `Fe^[2+]` | metal_62 | Iminodiacetic acid (IDA) | ligand_6127 | H2L | 19~30 | -0.05~1.15 | 3 | 2 | ref_eq_net_3272 | O=C(O)CNCC(=O)O |
| `Fe^[3+]` | metal_61 | Iminodiacetic acid (IDA) | ligand_6127 | H2L | 19~30 | -0.05~1.15 | 3 | 3 | ref_eq_net_3291 | O=C(O)CNCC(=O)O |
| `Fe^[2+]` | metal_62 | Nitrilotriacetic acid (NTA) | ligand_6165 | H3L | 15~30 | -0.05~1.15 | 3 | 3 | ref_eq_net_3746 | O=C(O)CN(CC(=O)O)CC(=O)O |
| `Fe^[3+]` | metal_61 | Nitrilotriacetic acid (NTA) | ligand_6165 | H3L | 15~30 | -0.05~1.15 | 5 | 5 | ref_eq_net_3758 | O=C(O)CN(CC(=O)O)CC(=O)O |
| `Fe^[2+]` | metal_62 | N-(2-Hydroxyethyl)ethylenedinitrilotria… | ligand_6275 | H3L | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_4867 | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O |
| `Fe^[3+]` | metal_61 | N-(2-Hydroxyethyl)ethylenedinitrilotria… | ligand_6275 | H3L | 19~30 | -0.05~1.15 | 2 | 4 | ref_eq_net_4876 | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O |
| `Fe^[2+]` | metal_62 | Ethylenedinitrilotetraacetic acid (EDTA) | ligand_6277 | H4L | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_5020 | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O |
| `Fe^[3+]` | metal_61 | Ethylenedinitrilotetraacetic acid (EDTA) | ligand_6277 | H4L | 19~30 | -0.05~1.15 | 2 | 3 | ref_eq_net_5034 | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O |
| `Fe^[2+]` | metal_62 | Pyridine-2,6-diphosphonic acid (2,6-PDP… | ligand_8434 | H4L | 20~30 | -0.05~0.25 | 1 | 10 | ref_eq_net_16823 | O=P(O)(O)c1cccc(P(=O)(O)O)n1 |
| `Fe^[3+]` | metal_61 | Pyridine-2,6-diphosphonic acid (2,6-PDP… | ligand_8434 | H4L | 20~30 | -0.05~0.25 | 1 | 6 | ref_eq_net_16824 | O=P(O)(O)c1cccc(P(=O)(O)O)n1 |
| `Fe^[2+]` | metal_62 | Ethanoic acid (Acetic acid) | ligand_8465 | HL | 16.5~31.5 | 2.775~3.225 | 1 | 1 | ref_eq_net_17129 | CC(=O)O |
| `Fe^[3+]` | metal_61 | Ethanoic acid (Acetic acid) | ligand_8465 | HL | 15~30 | -0.05~3.15 | 5 | 5 | ref_eq_net_17149 | CC(=O)O |
| `Fe^[2+]` | metal_62 | Ethanedioic acid (Oxalic acid) | ligand_8872 | H2L | 16.5~31.5 | 0.775~1.225 | 1 | 2 | ref_eq_net_20019 | O=C(O)C(=O)O |
| `Fe^[3+]` | metal_61 | Ethanedioic acid (Oxalic acid) | ligand_8872 | H2L | 16.5~31.5 | 0.275~3.225 | 3 | 3 | ref_eq_net_20031 | O=C(O)C(=O)O |
| `Fe^[2+]` | metal_62 | 2-Hydroxypropane-1,2,3-tricarboxylic ac… | ligand_9058 | H3L | 15~41 | -0.05~3.15 | 5 | 5 | ref_eq_net_22169 | O=C(O)CC(O)(CC(=O)O)C(=O)O |
| `Fe^[3+]` | metal_61 | 2-Hydroxypropane-1,2,3-tricarboxylic ac… | ligand_9058 | H3L | 19~30 | -0.05~1.15 | 3 | 4 | ref_eq_net_22182 | O=C(O)CC(O)(CC(=O)O)C(=O)O |
| `Fe^[2+]` | metal_62 | 2-Hydroxybenzoic acid (Salicylic acid) | ligand_9257 | H2L | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_23158 | O=C(O)c1ccccc1O |
| `Fe^[3+]` | metal_61 | 2-Hydroxybenzoic acid (Salicylic acid) | ligand_9257 | H2L | 15~30 | -0.15~3.15 | 7 | 3 | ref_eq_net_23169 | O=C(O)c1ccccc1O |
| `Fe^[2+]` | metal_62 | 2-Hydroxy-5-sulfobenzoic acid (5-Sulfos… | ligand_9284 | H3L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_23374 | O=C(O)c1cc(S(=O)(=O)O)ccc1O |
| `Fe^[3+]` | metal_61 | 2-Hydroxy-5-sulfobenzoic acid (5-Sulfos… | ligand_9284 | H3L | 15~30 | -0.05~3.15 | 4 | 3 | ref_eq_net_23388 | O=C(O)c1cc(S(=O)(=O)O)ccc1O |
| `Fe^[2+]` | metal_62 | 1,2-Dihydroxybenzene (Catechol) | ligand_9337 | H2L | 19~30 | -0.05~1.15 | 2 | 2 | ref_eq_net_23686 | Oc1ccccc1O |
| `Fe^[3+]` | metal_61 | 1,2-Dihydroxybenzene (Catechol) | ligand_9337 | H2L | 19~30 | -0.05~1.15 | 2 | 3 | ref_eq_net_23699 | Oc1ccccc1O |
| `Fe^[3+]` | metal_61 | 1,2-Dihydroxybenzene-3,5-disulfonic aci… | ligand_9358 | H4L | 15~30 | -0.05~1.15 | 4 | 4 | ref_eq_net_23905 | O=S(=O)(O)c1cc(O)c(O)c(S(=O)(=O)O)c1 |
| `Fe^[2+]` | metal_62 | Hydrogen thiocyanate (Thiocyanic acid) | ligand_10092 | HL | 19~30 | -0.05~3.15 | 2 | 1 | ref_eq_net_27923 | N=C=S |
| `Fe^[3+]` | metal_61 | Hydrogen thiocyanate (Thiocyanic acid) | ligand_10092 | HL | 19~30 | -0.15~5.15 | 13 | 4 | ref_eq_net_27953 | N=C=S |

### Global max-node network: `Fe^[2+]` + Pyridine-2,6-diphosphonic acid (2,6-PDPA)
network_id: ref_eq_net_16823 | metal_id: metal_62 | ligand_id: ligand_8434 | ligand_def_HxL: H4L | nodes: 10

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_238 | ``[M(OH)2L] + [H] <=> [M(OH)L] + [H2O]`` | logK | -11.38 |
| beta_def_739 | ``[MHL] + [H] <=> [MH2L]`` | logK | 3.36 |
| beta_def_171 | ``[MH3L2] + [H] <=> [M(H2L)2]`` | logK | 3.57 |
| beta_def_756 | ``[M(HL)2] + [H] <=> [MH3L2]`` | logK | 4.18 |
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` | logK | 4.5 |
| beta_def_204 | ``[MHL2] + [H] <=> [M(HL)2]`` | logK | 4.78 |
| beta_def_792 | ``[ML2] + [H] <=> [MHL2]`` | logK | 6.51 |
| beta_def_966 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` | logK | 9.81 |
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 10.12 |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` | logK | 15.45 |

---

### Step 18: `search_networks`
**Args:**
```json
{
  "sql_where_query": "c.metal_name = 'Fe^[3+]' AND c.ligand_id IN (8465, 9058, 8872, 9257, 9284, 10092, 6277, 6165, 6275, 6127, 8434, 9337, 9358) ORDER BY c.ligand_id",
  "ligand_similarity": false
}
```

[summary]
## search_networks — 126 row(s)

> **Reference equilibrium networks (compact)** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### Beta-definition legend
| beta_def | equation |
|----------|----------|
| beta_def_868 | ``[ML] + [L] <=> [ML2]`` |
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_779 | ``[M] + [HL] <=> [MHL]`` |
| beta_def_966 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |
| beta_def_238 | ``[M(OH)2L] + [H] <=> [M(OH)L] + [H2O]`` |
| beta_def_263 | ``[M(OH)3L] + [H] <=> [M(OH)2L] + [H2O]`` |
| beta_def_423 | ``[ML]^2 + [H2O]^2 <=> [M2(OH)2L2] + [H]^2`` |
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` |
| beta_def_427 | ``[M(OH)L]^2 <=> [M2(OH)2L2]`` |
| beta_def_792 | ``[ML2] + [H] <=> [MHL2]`` |
| beta_def_597 | ``[M]^3 + [L]^6 + [H2O]^2 <=> [M3(OH)2L6] + [H]^2`` |
| beta_def_601 | ``[M]^3 + [L]^2 + [H2O]^3 <=> [M3(OH)3L2] + [H]^3`` |
| beta_def_708 | ``[M]^7 + [L]^6 + [H2O]^9 <=> [M7(OH)9L6] + [H]^9`` |
| beta_def_872 | ``[M] + [L]^3 <=> [ML3]`` |
| beta_def_424 | ``[M]^2 + [L]^2 + [H2O]^2 <=> [M2(OH)2L2] + [H]^2`` |
| beta_def_846 | ``[ML] + [HL] <=> [ML2] + [H]`` |
| beta_def_821 | ``[M] + [HL] <=> [ML] + [H]`` |
| beta_def_873 | ``[ML2] + [HL] <=> [ML3] + [H]`` |
| beta_def_823 | ``[M] + [H2L] <=> [ML] + [H]^2`` |
| beta_def_853 | ``[ML] + [H2L] <=> [ML2] + [H]^2`` |
| beta_def_876 | ``[ML2] + [H2L] <=> [ML3] + [H]^2`` |
| beta_def_981 | ``[ML] + [OH] <=> [M(OH)L]`` |
| beta_def_894 | ``[M] + [L]^4 <=> [ML4]`` |

### Metal-ligand pair summary
| metal | metal_id | ligand | ligand_id | HxL | T_range | I_range | net_count | max_nodes | max_net_id | ligand_SMILES |
|-------|----------|--------|-----------|-----|---------|---------|-----------|----------|------------|---------------|
| `Fe^[3+]` | metal_61 | Iminodiacetic acid (IDA) | ligand_6127 | H2L | 19~30 | -0.05~1.15 | 3 | 3 | ref_eq_net_3291 | O=C(O)CNCC(=O)O |
| `Fe^[3+]` | metal_61 | Nitrilotriacetic acid (NTA) | ligand_6165 | H3L | 15~30 | -0.05~1.15 | 5 | 5 | ref_eq_net_3758 | O=C(O)CN(CC(=O)O)CC(=O)O |
| `Fe^[3+]` | metal_61 | N-(2-Hydroxyethyl)ethylenedinitrilotria… | ligand_6275 | H3L | 19~30 | -0.05~1.15 | 2 | 4 | ref_eq_net_4876 | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O |
| `Fe^[3+]` | metal_61 | Ethylenedinitrilotetraacetic acid (EDTA) | ligand_6277 | H4L | 19~30 | -0.05~1.15 | 2 | 3 | ref_eq_net_5034 | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O |
| `Fe^[3+]` | metal_61 | Pyridine-2,6-diphosphonic acid (2,6-PDP… | ligand_8434 | H4L | 20~30 | -0.05~0.25 | 1 | 6 | ref_eq_net_16824 | O=P(O)(O)c1cccc(P(=O)(O)O)n1 |
| `Fe^[3+]` | metal_61 | Ethanoic acid (Acetic acid) | ligand_8465 | HL | 15~30 | -0.05~3.15 | 5 | 5 | ref_eq_net_17149 | CC(=O)O |
| `Fe^[3+]` | metal_61 | Ethanedioic acid (Oxalic acid) | ligand_8872 | H2L | 16.5~31.5 | 0.275~3.225 | 3 | 3 | ref_eq_net_20031 | O=C(O)C(=O)O |
| `Fe^[3+]` | metal_61 | 2-Hydroxypropane-1,2,3-tricarboxylic ac… | ligand_9058 | H3L | 19~30 | -0.05~1.15 | 3 | 4 | ref_eq_net_22182 | O=C(O)CC(O)(CC(=O)O)C(=O)O |
| `Fe^[3+]` | metal_61 | 2-Hydroxybenzoic acid (Salicylic acid) | ligand_9257 | H2L | 15~30 | -0.15~3.15 | 7 | 3 | ref_eq_net_23169 | O=C(O)c1ccccc1O |
| `Fe^[3+]` | metal_61 | 2-Hydroxy-5-sulfobenzoic acid (5-Sulfos… | ligand_9284 | H3L | 15~30 | -0.05~3.15 | 4 | 3 | ref_eq_net_23388 | O=C(O)c1cc(S(=O)(=O)O)ccc1O |
| `Fe^[3+]` | metal_61 | 1,2-Dihydroxybenzene (Catechol) | ligand_9337 | H2L | 19~30 | -0.05~1.15 | 2 | 3 | ref_eq_net_23699 | Oc1ccccc1O |
| `Fe^[3+]` | metal_61 | 1,2-Dihydroxybenzene-3,5-disulfonic aci… | ligand_9358 | H4L | 15~30 | -0.05~1.15 | 4 | 4 | ref_eq_net_23905 | O=S(=O)(O)c1cc(O)c(O)c(S(=O)(=O)O)c1 |
| `Fe^[3+]` | metal_61 | Hydrogen thiocyanate (Thiocyanic acid) | ligand_10092 | HL | 19~30 | -0.15~5.15 | 13 | 4 | ref_eq_net_27953 | N=C=S |

### Global max-node network: `Fe^[3+]` + Pyridine-2,6-diphosphonic acid (2,6-PDPA)
network_id: ref_eq_net_16824 | metal_id: metal_61 | ligand_id: ligand_8434 | ligand_def_HxL: H4L | nodes: 6

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_792 | ``[ML2] + [H] <=> [MHL2]`` | logK | 3.86 |
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` | logK | 4.06 |
| beta_def_966 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` | logK | 6.4 |
| beta_def_238 | ``[M(OH)2L] + [H] <=> [M(OH)L] + [H2O]`` | logK | 8.36 |
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 20.87 |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` | logK | 28.68 |

---

### Step 19: `search_networks`
**Args:**
```json
{
  "sql_where_query": "c.metal_name = 'Fe^[2+]' AND c.ligand_id IN (8465, 9058, 8872, 9257, 9284, 10092, 6277, 6165, 6275, 6127, 8434, 9337, 9358) ORDER BY c.ligand_id",
  "ligand_similarity": false
}
```

[summary]
## search_networks — 50 row(s)

> **Reference equilibrium networks (compact)** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### Beta-definition legend
| beta_def | equation |
|----------|----------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |
| beta_def_966 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` |
| beta_def_786 | ``[M] + [HL] <=> [MHL]`` |
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` |
| beta_def_739 | ``[MHL] + [H] <=> [MH2L]`` |
| beta_def_238 | ``[M(OH)2L] + [H] <=> [M(OH)L] + [H2O]`` |
| beta_def_792 | ``[ML2] + [H] <=> [MHL2]`` |
| beta_def_204 | ``[MHL2] + [H] <=> [M(HL)2]`` |
| beta_def_756 | ``[M(HL)2] + [H] <=> [MH3L2]`` |
| beta_def_171 | ``[MH3L2] + [H] <=> [M(H2L)2]`` |
| beta_def_779 | ``[M] + [HL] <=> [MHL]`` |
| beta_def_732 | ``[M] + [H2L] <=> [MH2L]`` |
| beta_def_800 | ``[MHL] + [L] <=> [MHL2]`` |
| beta_def_374 | ``[M]^2 + [L]^2 <=> [M2(H-1L)2] + [H]^2`` |
| beta_def_821 | ``[M] + [HL] <=> [ML] + [H]`` |
| beta_def_846 | ``[ML] + [HL] <=> [ML2] + [H]`` |
| beta_def_497 | ``[M]^2 + [HL]^2 <=> [M2HL2] + [H]`` |
| beta_def_823 | ``[M] + [H2L] <=> [ML] + [H]^2`` |
| beta_def_853 | ``[ML] + [H2L] <=> [ML2] + [H]^2`` |

### Metal-ligand pair summary
| metal | metal_id | ligand | ligand_id | HxL | T_range | I_range | net_count | max_nodes | max_net_id | ligand_SMILES |
|-------|----------|--------|-----------|-----|---------|---------|-----------|----------|------------|---------------|
| `Fe^[2+]` | metal_62 | Iminodiacetic acid (IDA) | ligand_6127 | H2L | 19~30 | -0.05~1.15 | 3 | 2 | ref_eq_net_3272 | O=C(O)CNCC(=O)O |
| `Fe^[2+]` | metal_62 | Nitrilotriacetic acid (NTA) | ligand_6165 | H3L | 15~30 | -0.05~1.15 | 3 | 3 | ref_eq_net_3746 | O=C(O)CN(CC(=O)O)CC(=O)O |
| `Fe^[2+]` | metal_62 | N-(2-Hydroxyethyl)ethylenedinitrilotria… | ligand_6275 | H3L | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_4867 | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O |
| `Fe^[2+]` | metal_62 | Ethylenedinitrilotetraacetic acid (EDTA) | ligand_6277 | H4L | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_5020 | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O |
| `Fe^[2+]` | metal_62 | Pyridine-2,6-diphosphonic acid (2,6-PDP… | ligand_8434 | H4L | 20~30 | -0.05~0.25 | 1 | 10 | ref_eq_net_16823 | O=P(O)(O)c1cccc(P(=O)(O)O)n1 |
| `Fe^[2+]` | metal_62 | Ethanoic acid (Acetic acid) | ligand_8465 | HL | 16.5~31.5 | 2.775~3.225 | 1 | 1 | ref_eq_net_17129 | CC(=O)O |
| `Fe^[2+]` | metal_62 | Ethanedioic acid (Oxalic acid) | ligand_8872 | H2L | 16.5~31.5 | 0.775~1.225 | 1 | 2 | ref_eq_net_20019 | O=C(O)C(=O)O |
| `Fe^[2+]` | metal_62 | 2-Hydroxypropane-1,2,3-tricarboxylic ac… | ligand_9058 | H3L | 15~41 | -0.05~3.15 | 5 | 5 | ref_eq_net_22169 | O=C(O)CC(O)(CC(=O)O)C(=O)O |
| `Fe^[2+]` | metal_62 | 2-Hydroxybenzoic acid (Salicylic acid) | ligand_9257 | H2L | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_23158 | O=C(O)c1ccccc1O |
| `Fe^[2+]` | metal_62 | 2-Hydroxy-5-sulfobenzoic acid (5-Sulfos… | ligand_9284 | H3L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_23374 | O=C(O)c1cc(S(=O)(=O)O)ccc1O |
| `Fe^[2+]` | metal_62 | 1,2-Dihydroxybenzene (Catechol) | ligand_9337 | H2L | 19~30 | -0.05~1.15 | 2 | 2 | ref_eq_net_23686 | Oc1ccccc1O |
| `Fe^[2+]` | metal_62 | Hydrogen thiocyanate (Thiocyanic acid) | ligand_10092 | HL | 19~30 | -0.05~3.15 | 2 | 1 | ref_eq_net_27923 | N=C=S |

### Global max-node network: `Fe^[2+]` + Pyridine-2,6-diphosphonic acid (2,6-PDPA)
network_id: ref_eq_net_16823 | metal_id: metal_62 | ligand_id: ligand_8434 | ligand_def_HxL: H4L | nodes: 10

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_238 | ``[M(OH)2L] + [H] <=> [M(OH)L] + [H2O]`` | logK | -11.38 |
| beta_def_739 | ``[MHL] + [H] <=> [MH2L]`` | logK | 3.36 |
| beta_def_171 | ``[MH3L2] + [H] <=> [M(H2L)2]`` | logK | 3.57 |
| beta_def_756 | ``[M(HL)2] + [H] <=> [MH3L2]`` | logK | 4.18 |
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` | logK | 4.5 |
| beta_def_204 | ``[MHL2] + [H] <=> [M(HL)2]`` | logK | 4.78 |
| beta_def_792 | ``[ML2] + [H] <=> [MHL2]`` | logK | 6.51 |
| beta_def_966 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` | logK | 9.81 |
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 10.12 |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` | logK | 15.45 |

---

### Step 20: `search_stability`
**Args:**
```json
{
  "sql_where_query": "c.metal_name_SRD IN ('Fe^[3+]', 'Fe^[2+]') AND c.ligand_id IN (6275, 8434, 9358, 6165, 6127, 6277, 9058, 8465, 8872, 9257, 9284, 10092) ORDER BY c.ligand_id, c.metal_name_SRD, s.constant_type, s.constant_value DESC",
  "ligand_similarity": false
}
```

[summary]
## search_stability — 218 row(s)

### logK — 23 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 27 | 5 | 20~25 | 0~5 | *** | 13 |
| metal_61 | Fe^[3+] | ligand_9358 | 1,2-Dihydroxybenzene-3,5-di… | H4L | O=S(=O)(O)c1cc(O)c(O)c(S(=O)(=O)O)c1 | 16 | 4 | 20~25 | 0.1~1 | *** | 4 |
| metal_61 | Fe^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 14 | 8 | 20~25 | 0.1~1 | *** | 4 |
| metal_61 | Fe^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 12 | 5 | 20~25 | 0.1~3 | *** | 5 |
| metal_62 | Fe^[2+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 11 | 5 | 20~37 | 0.1~3 | *** | 5 |
| metal_61 | Fe^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 11 | 3 | 20~25 | 0~3 | *** | 7 |
| metal_62 | Fe^[2+] | ligand_8434 | Pyridine-2,6-diphosphonic a… | H4L | O=P(O)(O)c1cccc(P(=O)(O)O)n1 | 10 | 10 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 7 | 3 | 20~25 | 0.1~1 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 7 | 5 | 25 | 0.1~1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_9284 | 2-Hydroxy-5-sulfobenzoic ac… | H3L | O=C(O)c1cc(S(=O)(=O)O)ccc1O | 7 | 3 | 20~25 | 0.1~3 | *** | 4 |
| metal_62 | Fe^[2+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 6 | 2 | 20~25 | 0.1~1 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 6 | 4 | 25 | 0.1~1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_8434 | Pyridine-2,6-diphosphonic a… | H4L | O=P(O)(O)c1cccc(P(=O)(O)O)n1 | 6 | 6 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 6 | 4 | 20~25 | 0.1~1 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 5 | 4 | 25 | 0.1~1 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 5 | 3 | 25 | 0.5~3 | *** | 3 |
| metal_62 | Fe^[2+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 2 | 2 | 25 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 2 | 1 | 25 | 0~3 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 1 | 1 | 25 | 3 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_9284 | 2-Hydroxy-5-sulfobenzoic ac… | H3L | O=C(O)c1cc(S(=O)(=O)O)ccc1O | 1 | 1 | 20 | 0.1 | *** | 1 |

### ΔH — 11 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 6 | 3 | 25 | 0~3 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 4 | 4 | 25 | 0.1~1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 3 | 3 | 25 | 1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 2 | 2 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 1 | 25 | 1~3 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9284 | 2-Hydroxy-5-sulfobenzoic ac… | H3L | O=C(O)c1cc(S(=O)(=O)O)ccc1O | 1 | 1 | 25 | 3 | *** | 0 |

### ΔS — 11 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 6 | 3 | 25 | 0~3 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 4 | 4 | 20~25 | 0.1~1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 3 | 3 | 25 | 1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 2 | 2 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 1 | 25 | 1~3 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9284 | 2-Hydroxy-5-sulfobenzoic ac… | H3L | O=C(O)c1cc(S(=O)(=O)O)ccc1O | 1 | 1 | 25 | 3 | *** | 0 |

---

### Step 21: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_6275"
}
```

[summary]
## inspect_card — Ligand | ligand_6275

**Name:** N-(2-Hydroxyethyl)ethylenedinitrilotriacetic acid (HEDTA)  
**Formula:** C10H18N2O7 | **Class:** EDTA and derivatives  
**SMILES:** `O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O`  
**InChI:** `InChI=1S/C10H18N2O7/c13-4-3-11(5-8(14)15)1-2-12(6-9(16)17)7-10(18)19/h13H,1-7H2,(H,14,15)(H,16,17)(H,18,19)`  
**HxL definition:** H3L  

**pKa values:** 3

| source_vlm | pKa | T (°C) | I (M) | From → To | Solvent | Method | Quality |
|------------|-----|--------|-------|-----------|---------|--------|---------|
| vlm_107963 | 2.62 | 25.0 | 0.1 | H2L → H3L | *** | *** | *** |
| vlm_107958 | 5.38 | 25.0 | 0.1 | HL → H2L | *** | *** | *** |
| vlm_107949 | 9.70 | 25.0 | 0.1 | L → HL | *** | *** | *** |

**Partners:** 54 metal(s), 237 measurement(s) total

| metal_id | Metal | # meas |
|----------|-------|--------|
| metal_68 | H^[+] | 20 |
| metal_61 | Fe^[3+] | 9 |
| metal_206 | Yb^[3+] | 7 |
| metal_205 | Y^[3+] | 7 |
| metal_192 | Tm^[3+] | 7 |
| … | *(showing top 5 of 54)* | |

---

### Step 22: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_8434"
}
```

[summary]
## inspect_card — Ligand | ligand_8434

**Name:** Pyridine-2,6-diphosphonic acid (2,6-PDPA)  
**Formula:** C5H7N1O6 | **Class:** Aminophosphorus acids  
**SMILES:** `O=P(O)(O)c1cccc(P(=O)(O)O)n1`  
**InChI:** `InChI=1S/C5H7NO6P2/c7-13(8,9)4-2-1-3-5(6-4)14(10,11)12/h1-3H,(H2,7,8,9)(H2,10,11,12)`  
**HxL definition:** H4L  

**pKa values:** 3

| source_vlm | pKa | T (°C) | I (M) | From → To | Solvent | Method | Quality |
|------------|-----|--------|-------|-----------|---------|--------|---------|
| vlm_143981 | 3.14 | 25.0 | 0.1 | H2L → H3L | *** | *** | *** |
| vlm_143980 | 4.67 | 25.0 | 0.1 | HL → H2L | *** | *** | *** |
| vlm_143979 | 9.12 | 25.0 | 0.1 | L → HL | *** | *** | *** |

**Partners:** 3 metal(s), 19 measurement(s) total

| metal_id | Metal | # meas |
|----------|-------|--------|
| metal_62 | Fe^[2+] | 10 |
| metal_61 | Fe^[3+] | 6 |
| metal_68 | H^[+] | 3 |

---

### Step 23: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_9358"
}
```

[summary]
## inspect_card — Ligand | ligand_9358

**Name:** 1,2-Dihydroxybenzene-3,5-disulfonic acid (Tiron)  
**Formula:** C6H6O8S2 | **Class:** Catechols  
**SMILES:** `O=S(=O)(O)c1cc(O)c(O)c(S(=O)(=O)O)c1`  
**InChI:** `InChI=1S/C6H6O8S2/c7-4-1-3(15(9,10)11)2-5(6(4)8)16(12,13)14/h1-2,7-8H,(H,9,10,11)(H,12,13,14)`  
**HxL definition:** H4L  

**pKa values:** 2

| source_vlm | pKa | T (°C) | I (M) | From → To | Solvent | Method | Quality |
|------------|-----|--------|-------|-----------|---------|--------|---------|
| vlm_161952 | -12.50 | 25.0 | 0.1 | L → HL | *** | *** | *** |
| vlm_161957 | 7.62 | 25.0 | 0.1 | HL → H2L | *** | *** | *** |

**Partners:** 42 metal(s), 225 measurement(s) total

| metal_id | Metal | # meas |
|----------|-------|--------|
| metal_61 | Fe^[3+] | 16 |
| metal_68 | H^[+] | 12 |
| metal_5 | Al^[3+] | 12 |
| metal_208 | Zn^[2+] | 11 |
| metal_41 | Cu^[2+] | 11 |
| … | *(showing top 5 of 42)* | |

---

### Step 24: `inspect_card`
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

### Step 25: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_6127"
}
```

[summary]
## inspect_card — Ligand | ligand_6127

**Name:** Iminodiacetic acid (IDA)  
**Formula:** C4H7N1O4 | **Class:** Iminodiacetic acid and derivatives  
**SMILES:** `O=C(O)CNCC(=O)O`  
**InChI:** `InChI=1S/C4H7NO4/c6-3(7)1-5-2-4(8)9/h5H,1-2H2,(H,6,7)(H,8,9)`  
**HxL definition:** H2L  

**pKa values:** 3

| source_vlm | pKa | T (°C) | I (M) | From → To | Solvent | Method | Quality |
|------------|-----|--------|-------|-----------|---------|--------|---------|
| vlm_104135 | -1.77 | 25.0 | 0.1 | H2L → H3L | *** | *** | *** |
| vlm_104120 | 2.62 | 25.0 | 0.1 | HL → H2L | *** | *** | *** |
| vlm_104104 | 9.34 | 25.0 | 0.1 | L → HL | *** | *** | *** |

**Partners:** 52 metal(s), 375 measurement(s) total

| metal_id | Metal | # meas |
|----------|-------|--------|
| metal_68 | H^[+] | 45 |
| metal_41 | Cu^[2+] | 32 |
| metal_112 | Ni^[2+] | 28 |
| metal_208 | Zn^[2+] | 20 |
| metal_33 | Co^[2+] | 19 |
| … | *(showing top 5 of 52)* | |

---

### Step 26: `inspect_card`
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

### Step 27: `inspect_card`
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

### Step 28: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_8465"
}
```

[summary]
## inspect_card — Ligand | ligand_8465

**Name:** Ethanoic acid (Acetic acid)  
**Formula:** C2H4O2 | **Class:** Carboxylic acids  
**SMILES:** `CC(=O)O`  
**InChI:** `InChI=1S/C2H4O2/c1-2(3)4/h1H3,(H,3,4)`  
**HxL definition:** HL  

**pKa values:** 1

| source_vlm | pKa | T (°C) | I (M) | From → To | Solvent | Method | Quality |
|------------|-----|--------|-------|-----------|---------|--------|---------|
| vlm_144406 | 4.56 | 25.0 | 0.1 | L → HL | *** | *** | *** |

**Partners:** 69 metal(s), 562 measurement(s) total

| metal_id | Metal | # meas |
|----------|-------|--------|
| metal_26 | Cd^[2+] | 40 |
| metal_41 | Cu^[2+] | 37 |
| metal_68 | H^[+] | 29 |
| metal_185 | Th^[4+] | 25 |
| metal_112 | Ni^[2+] | 22 |
| … | *(showing top 5 of 69)* | |

---

### Step 29: `inspect_card`
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

### Step 30: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_9257"
}
```

[summary]
## inspect_card — Ligand | ligand_9257

**Name:** 2-Hydroxybenzoic acid (Salicylic acid)  
**Formula:** C7H6O3 | **Class:** Phenols salicylic acids  
**SMILES:** `O=C(O)c1ccccc1O`  
**InChI:** `InChI=1S/C7H6O3/c8-6-4-2-1-3-5(6)7(9)10/h1-4,8H,(H,9,10)`  
**HxL definition:** H2L  

**pKa values:** 2

| source_vlm | pKa | T (°C) | I (M) | From → To | Solvent | Method | Quality |
|------------|-----|--------|-------|-----------|---------|--------|---------|
| vlm_160211 | -13.40 | 25.0 | 0.1 | L → HL | *** | *** | *** |
| vlm_160226 | 2.80 | 25.0 | 0.1 | HL → H2L | *** | *** | *** |

**Partners:** 40 metal(s), 227 measurement(s) total

| metal_id | Metal | # meas |
|----------|-------|--------|
| metal_68 | H^[+] | 36 |
| metal_61 | Fe^[3+] | 15 |
| metal_19 | Be^[2+] | 11 |
| metal_195 | UO_[2]^[2+] | 10 |
| metal_41 | Cu^[2+] | 10 |
| … | *(showing top 5 of 40)* | |

---

### Step 31: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_9284"
}
```

[summary]
## inspect_card — Ligand | ligand_9284

**Name:** 2-Hydroxy-5-sulfobenzoic acid (5-Sulfosalicylic acid)  
**Formula:** C7H6O6S1 | **Class:** Phenols salicylic acids  
**SMILES:** `O=C(O)c1cc(S(=O)(=O)O)ccc1O`  
**InChI:** `InChI=1S/C7H6O6S/c8-6-2-1-4(14(11,12)13)3-5(6)7(9)10/h1-3,8H,(H,9,10)(H,11,12,13)`  
**HxL definition:** H3L  

**pKa values:** 2

| source_vlm | pKa | T (°C) | I (M) | From → To | Solvent | Method | Quality |
|------------|-----|--------|-------|-----------|---------|--------|---------|
| vlm_160822 | 2.48 | 25.0 | 0.1 | HL → H2L | *** | *** | *** |
| vlm_160810 | 11.85 | 25.0 | 0.1 | L → HL | *** | *** | *** |

**Partners:** 37 metal(s), 127 measurement(s) total

| metal_id | Metal | # meas |
|----------|-------|--------|
| metal_68 | H^[+] | 20 |
| metal_41 | Cu^[2+] | 14 |
| metal_61 | Fe^[3+] | 9 |
| metal_195 | UO_[2]^[2+] | 7 |
| metal_19 | Be^[2+] | 7 |
| … | *(showing top 5 of 37)* | |

---

### Step 32: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_10092"
}
```

[summary]
## inspect_card — Ligand | ligand_10092

**Name:** Hydrogen thiocyanate (Thiocyanic acid)  
**Formula:** C1H1N1S1 | **Class:** Inorganic ligands  
**SMILES:** `N=C=S`  
**InChI:** `InChI=1S/CHNS/c2-1-3/h2H`  
**HxL definition:** HL  

**pKa values:** 1

| source_vlm | pKa | T (°C) | I (M) | From → To | Solvent | Method | Quality |
|------------|-----|--------|-------|-----------|---------|--------|---------|
| vlm_172116 | -1.10 | 20.0 | 0.0 | L → HL | *** | *** | *** |

**Partners:** 65 metal(s), 434 measurement(s) total

| metal_id | Metal | # meas |
|----------|-------|--------|
| metal_26 | Cd^[2+] | 51 |
| metal_61 | Fe^[3+] | 39 |
| metal_21 | Bi^[3+] | 38 |
| metal_208 | Zn^[2+] | 24 |
| metal_41 | Cu^[2+] | 21 |
| … | *(showing top 5 of 65)* | |

---

### Step 33: `search_stability`
**Args:**
```json
{
  "sql_where_query": "c.metal_name_SRD IN ('Fe^[3+]', 'Fe^[2+]') AND c.ligand_id IN (9058, 9284, 9257, 8465, 8872, 10092, 6127, 6165, 6275, 6277, 8434) ORDER BY c.ligand_id, c.metal_name_SRD, s.constant_type, s.reaction_type, s.constant_value DESC",
  "ligand_similarity": false
}
```

[summary]
## search_stability — 202 row(s)

### logK — 22 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 27 | 5 | 20~25 | 0~5 | *** | 13 |
| metal_61 | Fe^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 14 | 8 | 20~25 | 0.1~1 | *** | 4 |
| metal_61 | Fe^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 12 | 5 | 20~25 | 0.1~3 | *** | 5 |
| metal_62 | Fe^[2+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 11 | 5 | 20~37 | 0.1~3 | *** | 5 |
| metal_61 | Fe^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 11 | 3 | 20~25 | 0~3 | *** | 7 |
| metal_62 | Fe^[2+] | ligand_8434 | Pyridine-2,6-diphosphonic a… | H4L | O=P(O)(O)c1cccc(P(=O)(O)O)n1 | 10 | 10 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 7 | 3 | 20~25 | 0.1~1 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 7 | 5 | 25 | 0.1~1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_9284 | 2-Hydroxy-5-sulfobenzoic ac… | H3L | O=C(O)c1cc(S(=O)(=O)O)ccc1O | 7 | 3 | 20~25 | 0.1~3 | *** | 4 |
| metal_62 | Fe^[2+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 6 | 2 | 20~25 | 0.1~1 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 6 | 4 | 25 | 0.1~1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_8434 | Pyridine-2,6-diphosphonic a… | H4L | O=P(O)(O)c1cccc(P(=O)(O)O)n1 | 6 | 6 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 6 | 4 | 20~25 | 0.1~1 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 5 | 4 | 25 | 0.1~1 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 5 | 3 | 25 | 0.5~3 | *** | 3 |
| metal_62 | Fe^[2+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 2 | 2 | 25 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 2 | 1 | 25 | 0~3 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 1 | 1 | 25 | 3 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_9284 | 2-Hydroxy-5-sulfobenzoic ac… | H3L | O=C(O)c1cc(S(=O)(=O)O)ccc1O | 1 | 1 | 20 | 0.1 | *** | 1 |

### ΔH — 11 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 6 | 3 | 25 | 0~3 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 4 | 4 | 25 | 0.1~1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 3 | 3 | 25 | 1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 2 | 2 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 1 | 25 | 1~3 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9284 | 2-Hydroxy-5-sulfobenzoic ac… | H3L | O=C(O)c1cc(S(=O)(=O)O)ccc1O | 1 | 1 | 25 | 3 | *** | 0 |

### ΔS — 11 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 6 | 3 | 25 | 0~3 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 4 | 4 | 20~25 | 0.1~1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 3 | 3 | 25 | 1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 2 | 2 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 1 | 25 | 1~3 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9284 | 2-Hydroxy-5-sulfobenzoic ac… | H3L | O=C(O)c1cc(S(=O)(=O)O)ccc1O | 1 | 1 | 25 | 3 | *** | 0 |

---

### Step 34: `search_citations`
**Args:**
```json
{
  "sql_where_query": "rv.vlm_id IN (SELECT rv.vlm_id FROM literature.rv_vlm AS rv LIMIT 1) LIMIT 1"
}
```

[TOOL ERROR] search_citations: Error executing tool search_citations: no such table: literature.rv_vlm

---
