# Qfree_20260423_144922 — Tool Results (batch 1)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "iron"
}
```

[summary]
## search_metals — 2 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_61 | Fe^[3+] | Fe | 3 | ✓ | [Fe+3] | InChI=1S/Fe/q+3 | beta_totN_128 | ligand_totN_406 | vlm_totN_1473 |
| metal_62 | Fe^[2+] | Fe | 2 | ✓ | [Fe+2] | InChI=1S/Fe/q+2 | beta_totN_57 | ligand_totN_217 | vlm_totN_667 |

---

### Step 4: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND s.constant_type = 'log_beta' AND s.temperature_c BETWEEN 20 AND 30 AND s.ionic_strength_mol_l BETWEEN 0 AND 1.5)",
  "order_by": "s.constant_value DESC",
  "limit": 100
}
```

[TOOL ERROR] search_stability: Error executing tool search_stability: SQL parse error: Invalid expression / Unexpected token. Line 1, Col: 47.
  SELECT 1 FROM _stub WHERE s.constant_value [4mDESC[0m

---

### Step 5: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_62 AND s.constant_type = 'log_beta' AND s.temperature_c BETWEEN 20 AND 30 AND s.ionic_strength_mol_l BETWEEN 0 AND 1.5)",
  "order_by": "s.constant_value DESC",
  "limit": 100
}
```

[TOOL ERROR] search_stability: Error executing tool search_stability: SQL parse error: Invalid expression / Unexpected token. Line 1, Col: 47.
  SELECT 1 FROM _stub WHERE s.constant_value [4mDESC[0m

---

### Step 6: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND s.constant_type = 'log_beta' AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.constant_value DESC",
  "limit": 80
}
```

[TOOL ERROR] search_stability: Error executing tool search_stability: SQL parse error: Invalid expression / Unexpected token. Line 1, Col: 47.
  SELECT 1 FROM _stub WHERE s.constant_value [4mDESC[0m

---

### Step 7: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND s.constant_type = 'log_beta')",
  "order_by": "constant_value DESC",
  "limit": 80
}
```

[TOOL ERROR] search_stability: Error executing tool search_stability: SQL parse error: Invalid expression / Unexpected token. Line 1, Col: 45.
  SELECT 1 FROM _stub WHERE constant_value [4mDESC[0m

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND s.constant_type = 'log_beta')",
  "order_by": "s.constant_value",
  "limit": 50
}
```

[summary]
## search_stability

*(no results)*

---

### Step 9: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_stability_measured",
  "group_column": "constant_type"
}
```

[summary]
## db_distribution - ligandmetal_stability_measured by constant_type

**total_rows:** 79063

| value | count | pct |
|-------|-------|-----|
| K | 60540 | 76.57% |
| H | 9693 | 12.26% |
| S | 8830 | 11.17% |

---

### Step 10: `get_table_schema`
**Args:**
```json
{
  "table_name": "ligandmetal_stability_measured"
}
```

[summary]
## get_table_schema - 25 column(s)

| cid | name | type | notnull | pk |
|-----|------|------|---------|----|
| 0 | stability_id | INTEGER | False | True |
| 1 | card_id | INTEGER | True | False |
| 2 | constant_type | TEXT | False | False |
| 3 | constant_value | REAL | False | False |
| 4 | temperature_c | REAL | False | False |
| 5 | ionic_strength_mol_l | REAL | False | False |
| 6 | solvent_id | INTEGER | False | False |
| 7 | solvent_name | TEXT | False | False |
| 8 | electrolyte_composition | TEXT | False | False |
| 9 | equation_python | TEXT | False | False |
| 10 | raw_definition | TEXT | False | False |
| 11 | normalized_definition | TEXT | False | False |
| 12 | equation_str | TEXT | False | False |
| 13 | equation_tree_json | TEXT | False | False |
| 14 | equation_sides_json | TEXT | False | False |
| 15 | LHS_species_json | TEXT | False | False |
| 16 | RHS_species_json | TEXT | False | False |
| 17 | HxL_involved_json | TEXT | False | False |
| 18 | presence_flags_json | TEXT | False | False |
| 19 | reaction_type | TEXT | False | False |
| 20 | element_conserved | INTEGER | False | False |
| 21 | citations_json | TEXT | False | False |
| 22 | audit_timestamp | TEXT | False | False |
| 23 | error | TEXT | False | False |
| 24 | notes | TEXT | False | False |

---

### Step 11: `get_table_schema`
**Args:**
```json
{
  "table_name": "ligandmetal_card"
}
```

[summary]
## get_table_schema - 17 column(s)

| cid | name | type | notnull | pk |
|-----|------|------|---------|----|
| 0 | card_id | INTEGER | False | True |
| 1 | complex_system_id | INTEGER | True | False |
| 2 | metal_id | INTEGER | True | False |
| 3 | ligand_id | INTEGER | True | False |
| 4 | beta_definition_id | INTEGER | True | False |
| 5 | complex_id | TEXT | False | False |
| 6 | ligand_class_id | INTEGER | False | False |
| 7 | ligand_class_name | TEXT | False | False |
| 8 | metal_name_SRD | TEXT | False | False |
| 9 | metal_SMILES | TEXT | False | False |
| 10 | metal_InChi | TEXT | False | False |
| 11 | ligand_name_SRD | TEXT | False | False |
| 12 | ligand_SMILES | TEXT | False | False |
| 13 | ligand_InChi | TEXT | False | False |
| 14 | ligand_HxL_definition_SRD | TEXT | False | False |
| 15 | beta_definition_name | TEXT | False | False |
| 16 | created_at | TIMESTAMP | False | False |

---

### Step 12: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND s.constant_type = 'K')",
  "order_by": "s.constant_value",
  "limit": 50
}
```

[summary]
## search_stability — 50 row(s)

### logK — 26 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_10076 | Hydroxide ion | *** | *** | 6 | 4 | 25 | 0~3 | solid | 3 |
| metal_61 | Fe^[3+] | ligand_6985 | DL-2-Aminopentanohydroxamic… | HL | CCC[C@H](N)C(=O)NO | 5 | 5 | 25 | 0.5 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6287 | rac-(1,2-Dimethylethylene)d… | H4L | CC(C(C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 4 | 3 | 20 | 0.1~0.5 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_6986 | DL-2-Aminohexanohydroxamic … | HL | CCCC[C@H](N)C(=O)NO | 3 | 3 | 25 | 0.5 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5777 | L-2-Amino-3-phenylpropanoic… | HL | N[C@@H](Cc1ccccc1)C(=O)O | 3 | 3 | 25 | 3 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6288 | meso-(1,2-Dimethylethylene)… | H4L | C[C@H]([C@H](C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 3 | 2 | 20 | 0.1~0.5 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_8955 | D-2,3-Dihydroxybutanedioic … | H2L | O=C(O)C(O)C(O)C(=O)O | 3 | 2 | 20~25 | 0.1~1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_10113 | Hydrogen phosphate (Phospho… | H3L | O=P(O)(O)O | 2 | 2 | 25 | 0~3 | solid | 2 |
| metal_61 | Fe^[3+] | ligand_9360 | 2,3-Dihydroxybenzenecarboxy… | H3L | O=C(O)c1cccc(O)c1O | 2 | 2 | 27 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9483 | 2,3-Dihydroxynaphthalene-6-… | H3L | O=S(=O)(O)c1ccc2cc(O)c(O)cc2c1 | 2 | 1 | 20~25 | 0.1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_9358 | 1,2-Dihydroxybenzene-3,5-di… | H4L | O=S(=O)(O)c1cc(O)c(O)c(S(=O)(=O)O)c1 | 2 | 1 | 20~25 | 0.1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_8126 | 8-Hydroxyquinoline (8-Quino… | HL | Oc1cccc2cccnc12 | 1 | 1 | 25 | 0.1 | solid | 1 |
| metal_61 | Fe^[3+] | ligand_6330 | 5,5'-Bis[bis(carboxymethyl)… | H6L | CC1=C/C(=C(\c2cc(C)c(O)c(CN(CC(=O)O)CC(=O)O)c2)c2ccccc2S(=O)(=O)O)C=C(CN(CC(=O)O)CC(=O)O)C1=O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6331 | 5,5'-Bis[bis(carboxymethyl)… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5809 | L-2-Amino-3-phosphopropanoi… | H3L | N[C@@H](COP(=O)(O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9366 | 3,4-Dihydroxyphenylacetic a… | H3L | O=C(O)Cc1ccc(O)c(O)c1 | 1 | 1 | 27 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9337 | 1,2-Dihydroxybenzene (Catec… | H2L | Oc1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9364 | 3,4-Dihydroxybenzenecarboxy… | H3L | O=C(O)c1ccc(O)c(O)c1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5998 | meso-Trimethylenebis[2-(2-h… | H4L | Cc1cc(C)c(O)c([C@H](NCCCN[C@@H](C(=O)O)c2cc(C)cc(C)c2O)C(=O)O)c1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9374 | 2,3-Dihydroxybenzoic acid d… | H2L | CN(C)C(=O)c1cccc(O)c1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7402 | 1,4,7-Triazacyclononane ([9… | L | C1CNCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9482 | 2,3-Dihydroxynaphthalene | H2L | Oc1cc2ccccc2cc1O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9357 | 1,2-Dihydroxybenzene-4-sulf… | H3L | O=S(=O)(O)c1ccc(O)c(O)c1 | 1 | 1 | 30 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9373 | 2,3-Dihydroxy-5-sulfobenzoi… | H3L | CN(C)C(=O)c1cc(S(=O)(=O)O)cc(O)c1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9593 | 5-Hydroxy-2-hydroxymethyl-4… | HL | O=c1cc(CO)occ1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 3 | *** | 1 |

---

### Step 13: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT c.ligand_id, c.ligand_name_SRD, c.beta_definition_name, s.constant_type, s.constant_value, s.temperature_c, s.ionic_strength_mol_l, s.reaction_type, s.equation_str FROM ligandmetal_card AS c JOIN ligandmetal_stability_measured AS s ON c.card_id = s.card_id WHERE c.metal_id = 61 AND s.constant_type = 'K' ORDER BY s.constant_value DESC LIMIT 100"
}
```

[summary]
## execute_srd46_sql - 50 row(s)

| ligand_id | ligand_name_SRD | beta_definition_name | constant_type | constant_value | temperature_c | ionic_strength_mol_l | reaction_type |
|-----------|-----------------|----------------------|---------------|----------------|---------------|----------------------|---------------|
| ligand_9894 | Trimethylenedihydroxamic acid (Glutarodihydroxamic acid) | [M<sub>2</sub>(HL)<sub>2</sub>L<sub>2</sub>]/[M]<sup>2</sup>[HL]<sup>2</sup>[L]... | K | 66.34 | 20.0 | 0.1 | homogeneous_aqueous |
| ligand_9901 | N,N'-Di-2-propylpentamethylenodihydroxamic acid (N,N'-Diisopropylglutarodihydro... | [M<sub>2</sub>L<sub>3</sub>]/[M]<sup>2</sup>[L]<sup>3</sup> | K | 62.4 | 25.0 | 0.1 | homogeneous_aqueous |
| ligand_9902 | N,N'-Di-2-propylhexamethylenodihydroxamic acid (N,N'-Diisopropylglutarodihydrox... | [M<sub>2</sub>L<sub>3</sub>]/[M]<sup>2</sup>[L]<sup>3</sup> | K | 62.3 | 25.0 | 0.1 | homogeneous_aqueous |
| ligand_9900 | N,N'-Di-2-propyltetramethylenodihydroxamic acid (N,N'-Diisopropylglutarodihydro... | [M<sub>2</sub>L<sub>3</sub>]/[M]<sup>2</sup>[L]<sup>3</sup> | K | 62.2 | 25.0 | 0.1 | homogeneous_aqueous |
| ligand_9906 | Rhodotorulic acid | [M<sub>2</sub>L<sub>3</sub>]/[M]<sup>2</sup>[L]<sup>3</sup> | K | 62.2 | 25.0 | 0.1 | homogeneous_aqueous |
| ligand_9899 | N,N'-Di-2-propyltrimethylenodihydroxamic acid (N,N'-Diisopropylglutarodihydroxa... | [M<sub>2</sub>L<sub>3</sub>]/[M]<sup>2</sup>[L]<sup>3</sup> | K | 62.1 | 25.0 | 0.1 | homogeneous_aqueous |
| ligand_9894 | Trimethylenedihydroxamic acid (Glutarodihydroxamic acid) | [M<sub>2</sub>(OH)L<sub>2</sub>]/[M]<sup>2</sup>[OH][L]<sup>2</sup> | K | 56.74 | 20.0 | 0.1 | homogeneous_aqueous |
| ligand_9905 | Trimethylenebis[aminocarbonyl(1,6-dihydro-1-hydroxy-6-oxo-2-pyridine)] (3-HOPOC... | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | K | 52.3 | 25.0 | 0.1 | homogeneous_aqueous |
| ligand_10076 | Hydroxide ion | [M<sub>3</sub>L<sub>4</sub>]/[M]<sup>3</sup>[L]<sup>4</sup> | K | 51.0 | 25.0 | 3.0 | homogeneous_aqueous |
| ligand_7391 | Piperazine-N,N'-diacetohydroxamic acid | [M<sub>2</sub>L<sub>4</sub>]/[M]<sup>2</sup>[L]<sup>4</sup> | K | 50.9 | 20.0 | 0.1 | homogeneous_aqueous |
| ligand_7422 | 1,4,7-Tris(3-hydroxy-6-methyl-2-pyridylmethyl)-1,4,7-triazacyclononane | [ML]/[M][L] | K | 50.0 | 25.0 | 0.1 | homogeneous_aqueous |
| ligand_10076 | Hydroxide ion | [M<sub>3</sub>L<sub>4</sub>]/[M]<sup>3</sup>[L]<sup>4</sup> | K | 49.7 | 25.0 | 3.0 | homogeneous_aqueous |
| ligand_10076 | Hydroxide ion | [M<sub>3</sub>L<sub>4</sub>]/[M]<sup>3</sup>[L]<sup>4</sup> | K | 49.7 | 25.0 | 0.0 | homogeneous_aqueous |
| ligand_7391 | Piperazine-N,N'-diacetohydroxamic acid | [M<sub>2</sub>H<sub>2</sub>L<sub>4</sub>]/[M]<sup>2</sup>[HL]<sup>2</sup>[L]<su... | K | 48.8 | 20.0 | 0.1 | homogeneous_aqueous |
| ligand_7154 | Iminodiacetohydroxamic acid | [M<sub>2</sub>L<sub>3</sub>]/[M]<sup>2</sup>[L]<sup>3</sup> | K | 44.0 | 20.0 | 0.1 | homogeneous_aqueous |
| ligand_10090 | Hydrogen cyanide (Hydrocyanic acid) | [ML<sub>6</sub>]/[M][L]<sup>6</sup> | K | 43.6 | 25.0 | 0.0 | homogeneous_aqueous |
| ligand_9906 | Rhodotorulic acid | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | K | 40.73 | 25.0 | 1.0 | homogeneous_aqueous |
| ligand_6037 | N,N'-Bis(2-hydroxybenzyl)ethylenedinitrilodiacetic acid (HBED) | [ML]/[M][L] | K | 39.01 | 25.0 | 0.1 | homogeneous_aqueous |
| ligand_6371 | 1,4-Bis[2,5,5-tris(carboxymethyl)-2,5-diazapentyl]benzene (PXED3A) | [M<sub>2</sub>L]/[M]<sup>2</sup>[L] | K | 39.0 | 25.0 | 0.1 | homogeneous_aqueous |
| ligand_8126 | 8-Hydroxyquinoline (8-Quinolinol)(Oxine) | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | K | 38.4 | 25.0 | 0.0 | homogeneous_aqueous |
| ligand_6021 | N,N-Bis(2-hydroxyethyl)glycine (Bicine) | [M(OH)<sub>3</sub>L]/[M][OH]<sup>3</sup>[L] | K | 38.0 | 20.0 | 0.1 | homogeneous_aqueous |
| ligand_6124 | 6,16-Bis(carboxymethyl)-1,11(2,3)-tetrahydroxy-2,10,12,20-tetraoxo-3,6,9,13,16,... | [ML]/[M][L] | K | 37.6 | 25.0 | 0.1 | homogeneous_aqueous |
| ligand_7340 | 1,3,5-Tris(dimethylamino)-1,3,5-trideoxy-cis-inositol | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | K | 37.1 | 25.0 | 0.1 | homogeneous_aqueous |
| ligand_8126 | 8-Hydroxyquinoline (8-Quinolinol)(Oxine) | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | K | 37.0 | 25.0 | 0.1 | homogeneous_aqueous |
| ligand_8126 | 8-Hydroxyquinoline (8-Quinolinol)(Oxine) | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | K | 36.9 | 25.0 | 1.0 | homogeneous_aqueous |

... 25 more row(s) omitted

---

### Step 14: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT c.ligand_id, c.ligand_name_SRD, c.beta_definition_name, s.constant_type, s.constant_value, s.temperature_c, s.ionic_strength_mol_l, s.reaction_type, s.equation_str FROM ligandmetal_card AS c JOIN ligandmetal_stability_measured AS s ON c.card_id = s.card_id WHERE c.metal_id = 62 AND s.constant_type = 'K' ORDER BY s.constant_value DESC LIMIT 100"
}
```

[summary]
## execute_srd46_sql - 50 row(s)

| ligand_id | ligand_name_SRD | beta_definition_name | constant_type | constant_value | temperature_c | ionic_strength_mol_l | reaction_type |
|-----------|-----------------|----------------------|---------------|----------------|---------------|----------------------|---------------|
| ligand_10090 | Hydrogen cyanide (Hydrocyanic acid) | [ML<sub>6</sub>]/[M][L]<sup>6</sup> | K | 35.4 | 25.0 | 0.0 | homogeneous_aqueous |
| ligand_9759 | 2,3-Dimercaptopropanol (BAL) | [M<sub>2</sub>L<sub>3</sub>]/[M]<sup>2</sup>[L]<sup>3</sup> | K | 28.0 | 30.0 | 0.1 | homogeneous_aqueous |
| ligand_6349 | Dithiobis(ethylenenitrilo)tetraacetic acid | [M<sub>2</sub>L<sub>2</sub>]/[M]<sup>2</sup>[L]<sup>2</sup> | K | 25.96 | 25.0 | 0.1 | homogeneous_aqueous |
| ligand_8193 | 5-Methyl-1,10-phenanthroline | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | K | 22.1 | 25.0 | 0.1 | homogeneous_aqueous |
| ligand_8196 | 5,6-Dimethyl-1,10-phenanthroline | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | K | 21.97 | 25.0 | 0.0 | homogeneous_aqueous |
| ligand_8204 | 2,6-Di(2-pyridyl)pyridine (2,2',6',2''-Terpyridine) | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | K | 21.1 | 25.0 | 0.5 | homogeneous_aqueous |
| ligand_8191 | 1,10-Phenanthroline (Dipyridino[a,c]benzene) | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | K | 21.0 | 25.0 | 0.1 | homogeneous_aqueous |
| ligand_8191 | 1,10-Phenanthroline (Dipyridino[a,c]benzene) | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | K | 21.0 | 25.0 | 0.0 | homogeneous_aqueous |
| ligand_8204 | 2,6-Di(2-pyridyl)pyridine (2,2',6',2''-Terpyridine) | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | K | 20.7 | 25.0 | 0.1 | homogeneous_aqueous |
| ligand_6102 | 1,4,7,10-Tetraazacyclododecane-N,N',N'',N'''-tetraacetic acid (DOTA) | [ML]/[M][L] | K | 19.8 | 25.0 | 0.1 | homogeneous_aqueous |
| ligand_8199 | 5-Chloro-1,10-phenanthroline | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | K | 19.7 | 25.0 | 0.1 | homogeneous_aqueous |
| ligand_6301 | trans-1,2-Cyclohexylenedinitrilotetraacetic acid (CDTA) | [ML]/[M][L] | K | 18.9 | 25.0 | 0.1 | homogeneous_aqueous |
| ligand_6104 | 1,4,7,10-Tetraazacyclotridecane-N,N',N'',N'''-tetraacetic acid (TRITA) | [ML]/[M][L] | K | 17.6 | 25.0 | 0.1 | homogeneous_aqueous |
| ligand_8156 | 2,2'-Bipyridyl | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | K | 17.5 | 25.0 | 1.0 | homogeneous_aqueous |
| ligand_8156 | 2,2'-Bipyridyl | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | K | 17.4 | 25.0 | 0.0 | homogeneous_aqueous |
| ligand_8201 | 5-Nitro-1,10-phenanthroline | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | K | 17.39 | 25.0 | 0.0 | homogeneous_aqueous |
| ligand_8156 | 2,2'-Bipyridyl | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | K | 17.2 | 25.0 | 0.1 | homogeneous_aqueous |
| ligand_8176 | 2-(2-Pyridylmethylenehydrazino)pyridine (Pyridine-2-aldehyde 2'-pyridylhydrazon... | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | K | 17.2 | 20.0 | 0.1 | homogeneous_aqueous |
| ligand_6287 | rac-(1,2-Dimethylethylene)dinitrilotetraacetic acid | [ML]/[M][L] | K | 17.18 | 20.0 | 0.1 | homogeneous_aqueous |
| ligand_6287 | rac-(1,2-Dimethylethylene)dinitrilotetraacetic acid | [ML]/[M][L] | K | 17.08 | 25.0 | 0.1 | homogeneous_aqueous |
| ligand_8176 | 2-(2-Pyridylmethylenehydrazino)pyridine (Pyridine-2-aldehyde 2'-pyridylhydrazon... | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | K | 16.57 | 25.0 | 0.0 | homogeneous_aqueous |
| ligand_6084 | 1-Oxa-4,7,10-triazacyclododecane-4,7,10-triacetic acid | [ML]/[M][L] | K | 16.55 | 25.0 | 0.1 | homogeneous_aqueous |
| ligand_6356 | Diethylenetrinitrilopentaacetic acid (DTPA) | [ML]/[M][L] | K | 16.2 | 25.0 | 0.1 | homogeneous_aqueous |
| ligand_6366 | Triethylenetetranitrilohexaacetic acid (TTHA) | [ML]/[M][L] | K | 15.8 | 25.0 | 0.1 | homogeneous_aqueous |
| ligand_9759 | 2,3-Dimercaptopropanol (BAL) | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | K | 15.8 | 30.0 | 0.1 | homogeneous_aqueous |

... 25 more row(s) omitted

---

### Step 15: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT c.ligand_id, c.ligand_name_SRD, c.beta_definition_name, s.constant_value, s.temperature_c, s.ionic_strength_mol_l FROM ligandmetal_card AS c JOIN ligandmetal_stability_measured AS s ON c.card_id = s.card_id WHERE c.metal_id = 61 AND s.constant_type = 'K' AND c.beta_definition_name LIKE '%[ML]/[M][L]%' ORDER BY s.constant_value DESC LIMIT 80"
}
```

[summary]
## execute_srd46_sql - 50 row(s)

| ligand_id | ligand_name_SRD | beta_definition_name | constant_value | temperature_c | ionic_strength_mol_l |
|-----------|-----------------|----------------------|----------------|---------------|----------------------|
| ligand_7422 | 1,4,7-Tris(3-hydroxy-6-methyl-2-pyridylmethyl)-1,4,7-triazacyclononane | [ML]/[M][L] | 50.0 | 25.0 | 0.1 |
| ligand_6037 | N,N'-Bis(2-hydroxybenzyl)ethylenedinitrilodiacetic acid (HBED) | [ML]/[M][L] | 39.01 | 25.0 | 0.1 |
| ligand_6124 | 6,16-Bis(carboxymethyl)-1,11(2,3)-tetrahydroxy-2,10,12,20-tetraoxo-3,6,9,13,16,... | [ML]/[M][L] | 37.6 | 25.0 | 0.1 |
| ligand_6038 | N,N'-Bis(2-hydroxy-5-sulfobenzyl)ethylenedinitrilodiacetic acid (SHBED) | [ML]/[M][L] | 36.87 | 25.0 | 0.1 |
| ligand_6125 | 7,19-Bis(carboxymethyl)-1,13(2,3)-tetrahydroxy-2,12,14,24-tetraoxo-3,7,11,15,19... | [ML]/[M][L] | 36.0 | 25.0 | 0.1 |
| ligand_5995 | rac-Ethylenediiminobis[(2-hydroxyphenyl)acetic acid] (EHPG) | [ML]/[M][L] | 35.54 | 25.0 | 0.1 |
| ligand_6046 | N,N'-Bis(3-hydroxy-6-methyl-2-pyridinylmethyl)ethylenedinitrilodiacetic acid (E... | [ML]/[M][L] | 35.08 | 25.0 | 0.1 |
| ligand_5998 | meso-Trimethylenebis[2-(2-hydroxy-3,5-dimethylphenyl)glycine] (meso-TMPHPG) | [ML]/[M][L] | 34.83 | 25.0 | 0.1 |
| ligand_5997 | rac-Trimethylenebis[2-(2-hydroxy-3,5-dimethylphenyl)glycine] (rac-TMPHPG) | [ML]/[M][L] | 34.22 | 25.0 | 0.1 |
| ligand_6041 | N,N'-Bis(3-hydroxy-5-phosphomethyl-2-methyl-4-pyridylmethyl)ethylenedinitrilodi... | [ML]/[M][L] | 33.5 | 25.0 | 0.1 |
| ligand_5996 | meso-Ethylenediiminobis[(2-hydroxyphenyl)acetic acid] (EHPG) | [ML]/[M][L] | 33.28 | 25.0 | 0.1 |
| ligand_6045 | N-(2-Hydroxy-3,5-dimethylbenzyl)-N'-(3-hydroxy-1,2,5-trimethyl-4-pyridiumylmeth... | [ML]/[M][L] | 33.0 | 25.0 | 0.1 |
| ligand_6047 | N,N''-Bis(3-hydroxy-6-methyl-2-pyridinylmethyl)diethylenetrinitrilotriacetic ac... | [ML]/[M][L] | 32.7 | 25.0 | 0.1 |
| ligand_9912 | Desferriferrioxamin E (Nocardamin) | [ML]/[M][L] | 32.49 | 20.0 | 0.1 |
| ligand_6276 | N-(2-Hydroxybenzyl)ethylenedinitrilotriacetic acid (HBET) | [ML]/[M][L] | 32.02 | 25.0 | 0.1 |
| ligand_7673 | 3,7,11,15-Tetraaza-5,13(2)-dihydroxy-5,13(5)-dimethyl-1,9(2,6)-dipyridina-5,13(... | [ML]/[M][L] | 32.0 | 25.0 | 0.1 |
| ligand_5994 | N,N'-Bis(2-hydroxyphenyl)ethylenediiminodiacetic acid (HPED) | [ML]/[M][L] | 31.8 | 25.0 | 0.1 |
| ligand_8453 | Ethylenebis[imino(2-hydroxyphenyl)methylene(methyl)phosphinic acid] | [ML]/[M][L] | 31.25 | 25.0 | 0.1 |
| ligand_6044 | N-(2-Hydroxybenzyl)-N'-(3-hydroxy-5-hydroxymethyl-2-methyl-4-pyridylmethyl)ethy... | [ML]/[M][L] | 31.0 | 25.0 | 0.1 |
| ligand_8442 | Ethylenebis(imino(2-hydroxyphenyl)methylenephosphonous acid) | [ML]/[M][L] | 31.0 | 25.0 | 0.1 |
| ligand_6042 | N,N'-Bis(3-hydroxy-5-hydroxymethyl-2-methyl-4-pyridylmethyl)ethylenedinitrilodi... | [ML]/[M][L] | 30.8 | 25.0 | 0.1 |
| ligand_9911 | N-Acetyldesferriferrioxamin B | [ML]/[M][L] | 30.76 | 20.0 | 0.1 |
| ligand_6039 | N,N"-Bis(2-hydroxybenzyl)diethylenetrinitrilo-N,N',N"-triacetic acid (HBDT) | [ML]/[M][L] | 30.44 | 25.0 | 0.1 |
| ligand_6054 | N,N'-Bis(carboxymethyl)ethylenedinitrilobis(N-2-propylacetohydroxamic acid) | [ML]/[M][L] | 30.2 | 25.0 | 0.1 |
| ligand_9916 | Desferricoprogen | [ML]/[M][L] | 30.2 | 25.0 | 0.1 |

... 25 more row(s) omitted

---

### Step 16: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT c.ligand_id, c.ligand_name_SRD, c.beta_definition_name, s.constant_value, s.temperature_c, s.ionic_strength_mol_l FROM ligandmetal_card AS c JOIN ligandmetal_stability_measured AS s ON c.card_id = s.card_id WHERE c.metal_id = 62 AND s.constant_type = 'K' AND c.beta_definition_name LIKE '%[ML]/[M][L]%' ORDER BY s.constant_value DESC LIMIT 80"
}
```

[summary]
## execute_srd46_sql - 50 row(s)

| ligand_id | ligand_name_SRD | beta_definition_name | constant_value | temperature_c | ionic_strength_mol_l |
|-----------|-----------------|----------------------|----------------|---------------|----------------------|
| ligand_6102 | 1,4,7,10-Tetraazacyclododecane-N,N',N'',N'''-tetraacetic acid (DOTA) | [ML]/[M][L] | 19.8 | 25.0 | 0.1 |
| ligand_6301 | trans-1,2-Cyclohexylenedinitrilotetraacetic acid (CDTA) | [ML]/[M][L] | 18.9 | 25.0 | 0.1 |
| ligand_6104 | 1,4,7,10-Tetraazacyclotridecane-N,N',N'',N'''-tetraacetic acid (TRITA) | [ML]/[M][L] | 17.6 | 25.0 | 0.1 |
| ligand_6287 | rac-(1,2-Dimethylethylene)dinitrilotetraacetic acid | [ML]/[M][L] | 17.18 | 20.0 | 0.1 |
| ligand_6287 | rac-(1,2-Dimethylethylene)dinitrilotetraacetic acid | [ML]/[M][L] | 17.08 | 25.0 | 0.1 |
| ligand_6084 | 1-Oxa-4,7,10-triazacyclododecane-4,7,10-triacetic acid | [ML]/[M][L] | 16.55 | 25.0 | 0.1 |
| ligand_6356 | Diethylenetrinitrilopentaacetic acid (DTPA) | [ML]/[M][L] | 16.2 | 25.0 | 0.1 |
| ligand_6366 | Triethylenetetranitrilohexaacetic acid (TTHA) | [ML]/[M][L] | 15.8 | 25.0 | 0.1 |
| ligand_6278 | DL-(Methylethylene)dinitrilotetraacetic acid (PDTA) | [ML]/[M][L] | 15.5 | 25.0 | 0.1 |
| ligand_6288 | meso-(1,2-Dimethylethylene)dinitrilotetraacetic acid | [ML]/[M][L] | 15.33 | 25.0 | 0.1 |
| ligand_7673 | 3,7,11,15-Tetraaza-5,13(2)-dihydroxy-5,13(5)-dimethyl-1,9(2,6)-dipyridina-5,13(... | [ML]/[M][L] | 15.3 | 25.0 | 0.1 |
| ligand_7661 | 5-(2-Hydroxyphenyl)-1,4,8,11-tetraazacyclotetradecane | [ML]/[M][L] | 14.8 | 25.0 | 0.1 |
| ligand_7500 | 1,4,7,10,13-Pentaazacyclohexadecane ([16]aneN5) | [ML]/[M][L] | 14.57 | 35.0 | 0.1 |
| ligand_6082 | 1-Oxa-4,7,10-triazacyclododecane-4,10-diacetic acid | [ML]/[M][L] | 14.46 | 25.0 | 0.1 |
| ligand_8209 | Ethylenedinitrilotetrakis(methylene-2-pyridine) (N,N,N',N'-Tetra-2-picolylethyl... | [ML]/[M][L] | 14.38 | 25.0 | 0.1 |
| ligand_6277 | Ethylenedinitrilotetraacetic acid (EDTA) | [ML]/[M][L] | 14.3 | 25.0 | 0.1 |
| ligand_6335 | Oxybis(ethylenenitrilo)tetraacetic acid (EEDTA) | [ML]/[M][L] | 14.2 | 25.0 | 0.1 |
| ligand_6292 | DL-Ethylenedinitrilo-N,N'-di(2-propanoic)-N,N'-diacetic acid | [ML]/[M][L] | 14.18 | 20.0 | 0.1 |
| ligand_6371 | 1,4-Bis[2,5,5-tris(carboxymethyl)-2,5-diazapentyl]benzene (PXED3A) | [ML]/[M][L] | 13.54 | 25.0 | 0.1 |
| ligand_8412 | Nitrilotris(methylenephosphonic acid) (NTP) | [ML]/[M][L] | 13.5 | 25.0 | 0.1 |
| ligand_6311 | Trimethylenedinitrilotetraacetic acid (TMDTA) | [ML]/[M][L] | 13.42 | 20.0 | 0.1 |
| ligand_6109 | 1,4,8,11-Tetraazacyclotetradecane-N,N',N'',N'''-tetraacetic acid (TETA) | [ML]/[M][L] | 13.32 | 25.0 | 0.1 |
| ligand_6313 | Tetramethylenedinitrilotetraacetic acid | [ML]/[M][L] | 13.16 | 20.0 | 0.1 |
| ligand_6070 | 1,4,10-Trioxa-7,13-diazacyclopentadecane-N,N'-diacetic acid | [ML]/[M][L] | 13.0 | 25.0 | 0.1 |
| ligand_8427 | N-(2-Hydroxyethyl)ethylenedinitrilotris(methylenephosphonic acid) | [ML]/[M][L] | 12.8 | 25.0 | 0.1 |

... 25 more row(s) omitted

---

### Step 17: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT fe3.ligand_id, fe3.ligand_name_SRD, fe3.constant_value AS logK_Fe3, fe2.constant_value AS logK_Fe2, (fe3.constant_value - fe2.constant_value) AS delta_logK, fe3.temperature_c, fe3.ionic_strength_mol_l FROM (SELECT c.ligand_id, c.ligand_name_SRD, s.constant_value, s.temperature_c, s.ionic_strength_mol_l FROM ligandmetal_card AS c JOIN ligandmetal_stability_measured AS s ON c.card_id = s.card_id WHERE c.metal_id = 61 AND s.constant_type = 'K' AND c.beta_definition_name LIKE '%[ML]/[M][L]%') AS fe3 JOIN (SELECT c.ligand_id, s.constant_value, s.temperature_c, s.ionic_strength_mol_l FROM ligandmetal_card AS c JOIN ligandmetal_stability_measured AS s ON c.card_id = s.card_id WHERE c.metal_id = 62 AND s.constant_type = 'K' AND c.beta_definition_name LIKE '%[ML]/[M][L]%') AS fe2 ON fe3.ligand_id = fe2.ligand_id AND fe3.temperature_c = fe2.temperature_c AND fe3.ionic_strength_mol_l = fe2.ionic_strength_mol_l ORDER BY delta_logK DESC LIMIT 60"
}
```

[summary]
## execute_srd46_sql - 50 row(s)

| ligand_id | ligand_name_SRD | logK_Fe3 | logK_Fe2 | delta_logK | temperature_c | ionic_strength_mol_l |
|-----------|-----------------|----------|----------|------------|---------------|----------------------|
| ligand_7673 | 3,7,11,15-Tetraaza-5,13(2)-dihydroxy-5,13(5)-dimethyl-1,9(2,6)-dipyridina-5,13(... | 32.0 | 15.3 | 16.7 | 25.0 | 0.1 |
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) | 11.27 | -4.8 | 16.07 | 25.0 | 0.1 |
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) | 11.19 | -4.8 | 15.989999999999998 | 25.0 | 0.1 |
| ligand_6109 | 1,4,8,11-Tetraazacyclotetradecane-N,N',N'',N'''-tetraacetic acid (TETA) | 26.46 | 13.32 | 13.14 | 25.0 | 0.1 |
| ligand_5843 | L-2-Aminobutanedioic acid 4-amide (Asparagine) | 8.6 | -3.4 | 12.0 | 20.0 | 1.0 |
| ligand_6356 | Diethylenetrinitrilopentaacetic acid (DTPA) | 28.0 | 16.2 | 11.8 | 25.0 | 0.1 |
| ligand_6292 | DL-Ethylenedinitrilo-N,N'-di(2-propanoic)-N,N'-diacetic acid | 25.28 | 14.18 | 11.100000000000001 | 20.0 | 0.1 |
| ligand_6301 | trans-1,2-Cyclohexylenedinitrilotetraacetic acid (CDTA) | 30.0 | 18.9 | 11.100000000000001 | 25.0 | 0.1 |
| ligand_6366 | Triethylenetetranitrilohexaacetic acid (TTHA) | 26.8 | 15.8 | 11.0 | 25.0 | 0.1 |
| ligand_6287 | rac-(1,2-Dimethylethylene)dinitrilotetraacetic acid | 28.05 | 17.08 | 10.970000000000002 | 25.0 | 0.1 |
| ligand_6277 | Ethylenedinitrilotetraacetic acid (EDTA) | 25.1 | 14.3 | 10.8 | 25.0 | 0.1 |
| ligand_8434 | Pyridine-2,6-diphosphonic acid (2,6-PDPA) | 20.87 | 10.12 | 10.750000000000002 | 25.0 | 0.1 |
| ligand_6278 | DL-(Methylethylene)dinitrilotetraacetic acid (PDTA) | 26.0 | 15.5 | 10.5 | 25.0 | 0.1 |
| ligand_6288 | meso-(1,2-Dimethylethylene)dinitrilotetraacetic acid | 25.65 | 15.33 | 10.319999999999999 | 25.0 | 0.1 |
| ligand_6084 | 1-Oxa-4,7,10-triazacyclododecane-4,7,10-triacetic acid | 26.8 | 16.55 | 10.25 | 25.0 | 0.1 |
| ligand_6104 | 1,4,7,10-Tetraazacyclotridecane-N,N',N'',N'''-tetraacetic acid (TRITA) | 27.5 | 17.6 | 9.899999999999999 | 25.0 | 0.1 |
| ligand_8360 | Amino(phenyl)methylenediphosphonic acid | 20.15 | 10.4 | 9.749999999999998 | 25.0 | 0.1 |
| ligand_6102 | 1,4,7,10-Tetraazacyclododecane-N,N',N'',N'''-tetraacetic acid (DOTA) | 29.4 | 19.8 | 9.599999999999998 | 25.0 | 0.1 |
| ligand_5937 | N-(Phosphonomethyl)glycine (Glyphosate) | 16.09 | 6.87 | 9.219999999999999 | 25.0 | 0.1 |
| ligand_6348 | Thiobis(ethylenenitrilo)tetraacetic acid (TEDTA) | 20.41 | 11.57 | 8.84 | 20.0 | 0.1 |
| ligand_6342 | Ethylenebis(oxyethylenenitrilo)tetraacetic acid (EGTA) | 20.5 | 11.8 | 8.7 | 25.0 | 0.1 |
| ligand_5804 | L-2-Aminopentanedioic acid (Glutamic acid) | 12.1 | 3.52 | 8.58 | 20.0 | 1.0 |
| ligand_6310 | Ethylenedinitrilotetra(3-propanoic acid) (EDTP) | 14.4 | 6.2 | 8.2 | 30.0 | 0.1 |
| ligand_6333 | (2-Hydroxytrimethylene)dinitrilotetraacetic acid | 20.1 | 11.91 | 8.190000000000001 | 20.0 | 0.1 |
| ligand_6311 | Trimethylenedinitrilotetraacetic acid (TMDTA) | 21.61 | 13.42 | 8.19 | 20.0 | 0.1 |

... 25 more row(s) omitted

---

### Step 18: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT DISTINCT c.ligand_id, c.ligand_name_SRD FROM ligandmetal_card AS c WHERE c.metal_id = 61 AND c.ligand_id IN (SELECT c2.ligand_id FROM ligandmetal_card AS c2 WHERE c2.metal_id = 62) ORDER BY c.ligand_name_SRD LIMIT 100"
}
```

[summary]
## execute_srd46_sql - 50 row(s)

| ligand_id | ligand_name_SRD |
|-----------|-----------------|
| ligand_6333 | (2-Hydroxytrimethylene)dinitrilotetraacetic acid |
| ligand_9015 | (Ethylenedithio)diacetic acid |
| ligand_8191 | 1,10-Phenanthroline (Dipyridino[a,c]benzene) |
| ligand_9337 | 1,2-Dihydroxybenzene (Catechol) |
| ligand_9467 | 1,2-Dihydroxynaphthalene-4-sulfonic acid |
| ligand_6102 | 1,4,7,10-Tetraazacyclododecane-N,N',N'',N'''-tetraacetic acid (DOTA) |
| ligand_6104 | 1,4,7,10-Tetraazacyclotridecane-N,N',N'',N'''-tetraacetic acid (TRITA) |
| ligand_6109 | 1,4,8,11-Tetraazacyclotetradecane-N,N',N'',N'''-tetraacetic acid (TETA) |
| ligand_6371 | 1,4-Bis[2,5,5-tris(carboxymethyl)-2,5-diazapentyl]benzene (PXED3A) |
| ligand_6760 | 1,4-Diazine-2-carboxylic acid (Pyrazinecarboxylic acid) |
| ligand_6084 | 1-Oxa-4,7,10-triazacyclododecane-4,7,10-triacetic acid |
| ligand_8156 | 2,2'-Bipyridyl |
| ligand_9759 | 2,3-Dimercaptopropanol (BAL) |
| ligand_9284 | 2-Hydroxy-5-sulfobenzoic acid (5-Sulfosalicylic acid) |
| ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) |
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) |
| ligand_7673 | 3,7,11,15-Tetraaza-5,13(2)-dihydroxy-5,13(5)-dimethyl-1,9(2,6)-dipyridina-5,13(... |
| ligand_6780 | 4-Aminopyridine-2,6-dicarboxylic acid |
| ligand_8196 | 5,6-Dimethyl-1,10-phenanthroline |
| ligand_8201 | 5-Nitro-1,10-phenanthroline |
| ligand_9873 | Acetohydroxamic acid |
| ligand_8360 | Amino(phenyl)methylenediphosphonic acid |
| ligand_5760 | Aminoacetic acid (Glycine) |
| ligand_8907 | Butanedioic acid (Succinic acid) |
| ligand_10163 | Chloride ion |

... 25 more row(s) omitted

---

### Step 19: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT fe3.ligand_id, fe3.ligand_name_SRD, fe3.constant_value AS logK_Fe3, fe2.constant_value AS logK_Fe2, (fe3.constant_value - fe2.constant_value) AS delta_logK, fe3.temperature_c, fe3.ionic_strength_mol_l FROM (SELECT c.ligand_id, c.ligand_name_SRD, s.constant_value, s.temperature_c, s.ionic_strength_mol_l FROM ligandmetal_card AS c JOIN ligandmetal_stability_measured AS s ON c.card_id = s.card_id WHERE c.metal_id = 61 AND s.constant_type = 'K' AND c.beta_definition_name LIKE '%[ML]/[M][L]%') AS fe3 JOIN (SELECT c.ligand_id, s.constant_value, s.temperature_c, s.ionic_strength_mol_l FROM ligandmetal_card AS c JOIN ligandmetal_stability_measured AS s ON c.card_id = s.card_id WHERE c.metal_id = 62 AND s.constant_type = 'K' AND c.beta_definition_name LIKE '%[ML]/[M][L]%') AS fe2 ON fe3.ligand_id = fe2.ligand_id AND fe3.temperature_c = fe2.temperature_c AND fe3.ionic_strength_mol_l = fe2.ionic_strength_mol_l WHERE fe3.ligand_id IN (9058, 9284, 9257, 5760, 8907, 10163, 8191, 8156, 9337, 9873, 5937, 5804, 5843, 6760, 6277, 9015) ORDER BY delta_logK DESC LIMIT 50"
}
```

[summary]
## execute_srd46_sql - 10 row(s)

| ligand_id | ligand_name_SRD | logK_Fe3 | logK_Fe2 | delta_logK | temperature_c | ionic_strength_mol_l |
|-----------|-----------------|----------|----------|------------|---------------|----------------------|
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) | 11.27 | -4.8 | 16.07 | 25.0 | 0.1 |
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) | 11.19 | -4.8 | 15.989999999999998 | 25.0 | 0.1 |
| ligand_5843 | L-2-Aminobutanedioic acid 4-amide (Asparagine) | 8.6 | -3.4 | 12.0 | 20.0 | 1.0 |
| ligand_6277 | Ethylenedinitrilotetraacetic acid (EDTA) | 25.1 | 14.3 | 10.8 | 25.0 | 0.1 |
| ligand_5937 | N-(Phosphonomethyl)glycine (Glyphosate) | 16.09 | 6.87 | 9.219999999999999 | 25.0 | 0.1 |
| ligand_5804 | L-2-Aminopentanedioic acid (Glutamic acid) | 12.1 | 3.52 | 8.58 | 20.0 | 1.0 |
| ligand_9873 | Acetohydroxamic acid | 11.42 | 4.8 | 6.62 | 20.0 | 0.1 |
| ligand_6760 | 1,4-Diazine-2-carboxylic acid (Pyrazinecarboxylic acid) | 7.5 | 4.1 | 3.4000000000000004 | 25.0 | 1.0 |
| ligand_10163 | Chloride ion | 1.48 | -0.2 | 1.68 | 25.0 | 0.0 |
| ligand_5760 | Aminoacetic acid (Glycine) | -9.25 | 4.2 | -13.45 | 25.0 | 3.0 |

---

### Step 20: `search_pka_values`
**Args:**
```json
{
  "where": "(lc.ligand_id IN (9058, 9284, 9257, 5760, 8907, 9873, 5937, 5804, 5843))",
  "order_by": "lc.ligand_id, p.pKa ASC",
  "limit": 80
}
```

[summary]
## search_pka_values — 21 row(s)

### pKa -13.5–-13.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_160211 | ligand_9257 | 2-Hydroxybenzoic acid (Salicylic a… | H2L | O=C(O)c1ccccc1O | -13.4 | 25 | 0.1 | L→HL | M_tot_37 | M_tot_3 |

### pKa -0.5–0.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_99756 | ligand_5937 | N-(Phosphonomethyl)glycine (Glypho… | H3L | O=C(O)CNCP(=O)(O)O | -0.5 | 20 | 0.1 | H3L→H4L | M_tot_1 | M_tot_1 |

### pKa 2.0–2.5 (5 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_95761 | ligand_5804 | L-2-Aminopentanedioic acid (Glutam… | H2L | N[C@@H](CCC(=O)O)C(=O)O | 2.16 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_2 |
| vlm_97048 | ligand_5843 | L-2-Aminobutanedioic acid 4-amide … | HL | NC(=O)C[C@H](N)C(=O)O | 2.16 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_2 |
| vlm_99734 | ligand_5937 | N-(Phosphonomethyl)glycine (Glypho… | H3L | O=C(O)CNCP(=O)(O)O | 2.2 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_1 |
| vlm_93627 | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 2.33 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_20 |
| vlm_160822 | ligand_9284 | 2-Hydroxy-5-sulfobenzoic acid (5-S… | H3L | O=C(O)c1cc(S(=O)(=O)O)ccc1O | 2.48 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_37 |

### pKa 2.5–3.0 (2 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_160226 | ligand_9257 | 2-Hydroxybenzoic acid (Salicylic a… | H2L | O=C(O)c1ccccc1O | 2.8 | 25 | 0.1 | HL→H2L | M_tot_4 | M_tot_37 |
| vlm_157473 | ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxyl… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 2.9 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_12 |

### pKa 3.5–4.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_153300 | ligand_8907 | Butanedioic acid (Succinic acid) | H2L | O=C(O)CCC(=O)O | 3.99 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_27 |

### pKa 4.0–4.5 (2 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_95750 | ligand_5804 | L-2-Aminopentanedioic acid (Glutam… | H2L | N[C@@H](CCC(=O)O)C(=O)O | 4.15 | 25 | 0.1 | HL→H2L | M_tot_2 | M_tot_8 |
| vlm_157459 | ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxyl… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 4.35 | 25 | 0.1 | HL→H2L | M_tot_12 | M_tot_18 |

### pKa 5.0–5.5 (2 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_153268 | ligand_8907 | Butanedioic acid (Succinic acid) | H2L | O=C(O)CCC(=O)O | 5.24 | 25 | 0.1 | L→HL | M_tot_27 | M_tot_36 |
| vlm_99712 | ligand_5937 | N-(Phosphonomethyl)glycine (Glypho… | H3L | O=C(O)CNCP(=O)(O)O | 5.45 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_2 |

### pKa 5.5–6.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_157439 | ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxyl… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 5.65 | 25 | 0.1 | L→HL | M_tot_18 | M_tot_57 |

### pKa 8.5–9.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_97039 | ligand_5843 | L-2-Aminobutanedioic acid 4-amide … | HL | NC(=O)C[C@H](N)C(=O)O | 8.73 | 25 | 0.1 | L→HL | M_tot_2 | M_tot_14 |

### pKa 9.0–9.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_168403 | ligand_9873 | Acetohydroxamic acid | HL | CC(=O)NO | 9.29 | 25 | 0.1 | L→HL | M_tot_1 | M_tot_19 |

### pKa 9.5–10.0 (2 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_93606 | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 9.57 | 25 | 0.1 | L→HL | M_tot_20 | M_tot_43 |
| vlm_95739 | ligand_5804 | L-2-Aminopentanedioic acid (Glutam… | H2L | N[C@@H](CCC(=O)O)C(=O)O | 9.58 | 25 | 0.1 | L→HL | M_tot_8 | M_tot_17 |

### pKa 10.0–10.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_99687 | ligand_5937 | N-(Phosphonomethyl)glycine (Glypho… | H3L | O=C(O)CNCP(=O)(O)O | 10.1 | 25 | 0.1 | L→HL | M_tot_2 | M_tot_14 |

### pKa 11.5–12.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_160810 | ligand_9284 | 2-Hydroxy-5-sulfobenzoic acid (5-S… | H3L | O=C(O)c1cc(S(=O)(=O)O)ccc1O | 11.85 | 25 | 0.1 | L→HL | M_tot_37 | M_tot_1 |

---

### Step 21: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND c.ligand_id IN (ligand_9284, ligand_9257, ligand_9337, ligand_8191, ligand_8156) AND s.constant_type = 'K')",
  "order_by": "c.ligand_id, s.constant_value DESC",
  "limit": 60
}
```

[summary]
## search_stability — 30 row(s)

### logK — 5 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 11 | 3 | 20~25 | 0~3 | *** | 7 |
| metal_61 | Fe^[3+] | ligand_8191 | 1,10-Phenanthroline (Dipyri… | L | c1cnc2c(c1)ccc1cccnc12 | 7 | 5 | 20~25 | 0~1.5 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_9284 | 2-Hydroxy-5-sulfobenzoic ac… | H3L | O=C(O)c1cc(S(=O)(=O)O)ccc1O | 7 | 3 | 20~25 | 0.1~3 | *** | 4 |
| metal_61 | Fe^[3+] | ligand_9337 | 1,2-Dihydroxybenzene (Catec… | H2L | Oc1ccccc1O | 4 | 3 | 25 | 0.1~1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_8156 | 2,2'-Bipyridyl | L | c1ccc(-c2ccccn2)nc1 | 1 | 1 | 20 | 0.1 | *** | 1 |

---

### Step 22: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_62 AND c.ligand_id IN (ligand_9284, ligand_9257, ligand_9337, ligand_8191, ligand_8156) AND s.constant_type = 'K')",
  "order_by": "c.ligand_id, s.constant_value DESC",
  "limit": 60
}
```

[summary]
## search_stability — 18 row(s)

### `Fe^[2+]` + 2,2'-Bipyridyl — 6 measurement(s)
metal_id: metal_62 | ligand_id: ligand_8156
ligand_HxL_def: L | ligand_SMILES: c1ccc(-c2ccccn2)nc1

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_138567 | ref_eq_map_14952 | beta_def_872 | logK | 17.5 | 25 | 1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (4.41, L, +inf) |
| vlm_138568 | ref_eq_map_14953 | beta_def_872 | logK | 17.4 | 25 | 0 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (4.41, L, +inf) |
| vlm_138566 | ref_eq_map_14951 | beta_def_872 | logK | 17.2 | 25 | 0.1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (4.41, L, +inf) |
| vlm_138565 | ref_eq_map_14951 | beta_def_840 | logK | 7.9 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (4.41, L, +inf) |
| vlm_138564 | ref_eq_map_14952 | beta_def_812 | logK | 4.65 | 30 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (4.41, L, +inf) |
| vlm_138563 | ref_eq_map_14951 | beta_def_812 | logK | 4.2 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (4.41, L, +inf) |

### `Fe^[2+]` + 1,10-Phenanthroline (Dipyridino[a,c]benzene) — 5 measurement(s)
metal_id: metal_62 | ligand_id: ligand_8191
ligand_HxL_def: L | ligand_SMILES: c1cnc2c(c1)ccc1cccnc12

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_139269 | ref_eq_map_15178 | beta_def_872 | logK | 21 | 25 | 0.1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (4.92, L, +inf) |
| vlm_139270 | ref_eq_map_15179 | beta_def_872 | logK | 21 | 25 | 0 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (4.92, L, +inf) |
| vlm_139268 | ref_eq_map_15178 | beta_def_840 | logK | 11.15 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (4.92, L, +inf) |
| vlm_139266 | ref_eq_map_15178 | beta_def_812 | logK | 5.85 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (4.92, L, +inf) |
| vlm_139267 | ref_eq_map_15179 | beta_def_812 | logK | -5.87 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (4.92, L, +inf) |

### `Fe^[2+]` + 2-Hydroxybenzoic acid (Salicylic acid) — 2 measurement(s)
metal_id: metal_62 | ligand_id: ligand_9257
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)c1ccccc1O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_160374 | ref_eq_map_23094 | beta_def_821 | logK | -6.8 | 20 | 0.1 | `[M] + [HL] <=> [ML] + [H]` | *** | [HL] | (-13.4, HL, 2.8) |
| vlm_160375 | ref_eq_map_23094 | beta_def_846 | logK | -8.9 | 20 | 0.1 | `[ML] + [HL] <=> [ML2] + [H]` | *** | [HL] | (-13.4, HL, 2.8) |

### `Fe^[2+]` + 2-Hydroxy-5-sulfobenzoic acid (5-Sulfosalicylic acid) — 1 measurement(s)
metal_id: metal_62 | ligand_id: ligand_9284
ligand_HxL_def: H3L | ligand_SMILES: O=C(O)c1cc(S(=O)(=O)O)ccc1O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_160888 | ref_eq_map_23310 | beta_def_821 | logK | -5.9 | 20 | 0.1 | `[M] + [HL] <=> [ML] + [H]` | *** | [HL] | (2.48, HL, 11.85) |

### `Fe^[2+]` + 1,2-Dihydroxybenzene (Catechol) — 4 measurement(s)
metal_id: metal_62 | ligand_id: ligand_9337
ligand_HxL_def: H2L | ligand_SMILES: Oc1ccccc1O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_161570 | ref_eq_map_23622 | beta_def_497 | logK | 10.9 | 25 | 0.1 | `[M]^2 + [HL]^2 <=> [M2HL2] + [H]` | *** | [HL] | (-13.3, HL, 9.26) |
| vlm_161567 | ref_eq_map_23622 | beta_def_823 | logK | -14.3 | 25 | 0.1 | `[M] + [H2L] <=> [ML] + [H]^2` | *** | [H2L] | (-inf, H2L, 9.26) |
| vlm_161568 | ref_eq_map_23623 | beta_def_823 | logK | -14.33 | 25 | 1 | `[M] + [H2L] <=> [ML] + [H]^2` | *** | [H2L] | (-inf, H2L, 9.26) |
| vlm_161569 | ref_eq_map_23623 | beta_def_853 | logK | -16.7 | 25 | 1 | `[ML] + [H2L] <=> [ML2] + [H]^2` | *** | [H2L] | (-inf, H2L, 9.26) |

---

### Step 23: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT c.ligand_id, c.ligand_name_SRD, c.beta_definition_name, s.constant_value, s.temperature_c, s.ionic_strength_mol_l, s.equation_str FROM ligandmetal_card AS c JOIN ligandmetal_stability_measured AS s ON c.card_id = s.card_id WHERE c.metal_id = 61 AND c.ligand_id IN (9284, 9257, 9337, 8191, 8156) AND s.constant_type = 'K' AND c.beta_definition_name LIKE '%[ML]/[M][L]%' ORDER BY c.ligand_id, s.constant_value DESC LIMIT 50"
}
```

[summary]
## execute_srd46_sql - 1 row(s)

| ligand_id | ligand_name_SRD | beta_definition_name | constant_value | temperature_c | ionic_strength_mol_l | equation_str |
|-----------|-----------------|----------------------|----------------|---------------|----------------------|--------------|
| ligand_8191 | 1,10-Phenanthroline (Dipyridino[a,c]benzene) | [ML]/[M][L] | 6.5 | 20.0 | 0.1 | [M] + [L] <=> [ML] |

---

### Step 24: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT c.ligand_id, c.ligand_name_SRD, c.beta_definition_name, s.constant_value, s.temperature_c, s.ionic_strength_mol_l, s.equation_str FROM ligandmetal_card AS c JOIN ligandmetal_stability_measured AS s ON c.card_id = s.card_id WHERE c.metal_id = 61 AND c.ligand_id IN (9284, 9257, 9337) AND s.constant_type = 'K' ORDER BY c.ligand_id, s.constant_value DESC LIMIT 60"
}
```

[summary]
## execute_srd46_sql - 22 row(s)

| ligand_id | ligand_name_SRD | beta_definition_name | constant_value | temperature_c | ionic_strength_mol_l | equation_str |
|-----------|-----------------|----------------------|----------------|---------------|----------------------|--------------|
| ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | [MHL]/[M][HL] | 4.4 | 25.0 | 0.1 | [M] + [HL] <=> [MHL] |
| ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | [ML][H]/[M][HL] | 2.9 | 25.0 | 0.1 | [M] + [HL] <=> [ML] + [H] |
| ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | [ML][H]/[M][HL] | 2.85 | 25.0 | 0.5 | [M] + [HL] <=> [ML] + [H] |
| ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | [ML][H]/[M][HL] | 2.73 | 20.0 | 1.0 | [M] + [HL] <=> [ML] + [H] |
| ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | [ML][H]/[M][HL] | 2.7 | 25.0 | 1.0 | [M] + [HL] <=> [ML] + [H] |
| ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | [ML][H]/[M][HL] | 2.69 | 25.0 | 3.0 | [M] + [HL] <=> [ML] + [H] |
| ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | [ML<sub>2</sub>][H]/[ML][HL] | -1.5 | 25.0 | 3.0 | [ML] + [HL] <=> [ML2] + [H] |
| ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | [ML<sub>2</sub>][H]/[ML][HL] | -1.7 | 25.0 | 0.1 | [ML] + [HL] <=> [ML2] + [H] |
| ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | [ML<sub>2</sub>][H]/[ML][HL] | -1.7 | 20.0 | 0.1 | [ML] + [HL] <=> [ML2] + [H] |
| ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | [ML][H]/[M][HL] | -2.74 | 20.0 | 0.1 | [M] + [HL] <=> [ML] + [H] |
| ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | [ML][H]/[M][HL] | -3.85 | 25.0 | 0.0 | [M] + [HL] <=> [ML] + [H] |
| ligand_9284 | 2-Hydroxy-5-sulfobenzoic acid (5-Sulfosalicylic acid) | [ML][H]/[M][HL] | 2.7 | 25.0 | 0.1 | [M] + [HL] <=> [ML] + [H] |
| ligand_9284 | 2-Hydroxy-5-sulfobenzoic acid (5-Sulfosalicylic acid) | [ML][H]/[M][HL] | 2.69 | 25.0 | 1.0 | [M] + [HL] <=> [ML] + [H] |
| ligand_9284 | 2-Hydroxy-5-sulfobenzoic acid (5-Sulfosalicylic acid) | [ML][H]/[M][HL] | 2.68 | 25.0 | 3.0 | [M] + [HL] <=> [ML] + [H] |
| ligand_9284 | 2-Hydroxy-5-sulfobenzoic acid (5-Sulfosalicylic acid) | [ML][H]/[M][HL] | 2.65 | 20.0 | 0.1 | [M] + [HL] <=> [ML] + [H] |
| ligand_9284 | 2-Hydroxy-5-sulfobenzoic acid (5-Sulfosalicylic acid) | [ML<sub>2</sub>][H]/[ML][HL] | -0.9 | 25.0 | 3.0 | [ML] + [HL] <=> [ML2] + [H] |
| ligand_9284 | 2-Hydroxy-5-sulfobenzoic acid (5-Sulfosalicylic acid) | [ML<sub>2</sub>][H]/[ML][HL] | -1.4 | 20.0 | 0.1 | [ML] + [HL] <=> [ML2] + [H] |
| ligand_9284 | 2-Hydroxy-5-sulfobenzoic acid (5-Sulfosalicylic acid) | [ML<sub>3</sub>][H]/[ML<sub>2</sub>][HL] | -4.7 | 25.0 | 3.0 | [ML2] + [HL] <=> [ML3] + [H] |
| ligand_9337 | 1,2-Dihydroxybenzene (Catechol) | [ML][H]<sup>2</sup>/[M][H<sub>2</sub>L] | -1.36 | 25.0 | 1.0 | [M] + [H2L] <=> [ML] + [H]^2 |
| ligand_9337 | 1,2-Dihydroxybenzene (Catechol) | [ML][H]<sup>2</sup>/[M][H<sub>2</sub>L] | -2.2 | 25.0 | 0.1 | [M] + [H2L] <=> [ML] + [H]^2 |
| ligand_9337 | 1,2-Dihydroxybenzene (Catechol) | [ML<sub>2</sub>][H]<sup>2</sup>/[ML][H<sub>2</sub>L] | -7.53 | 25.0 | 0.1 | [ML] + [H2L] <=> [ML2] + [H]^2 |
| ligand_9337 | 1,2-Dihydroxybenzene (Catechol) | [ML<sub>3</sub>][H]<sup>2</sup>/[ML<sub>2</sub>][H<sub>2</sub>L] | -13.16 | 25.0 | 0.1 | [ML2] + [H2L] <=> [ML3] + [H]^2 |

---

### Step 25: `search_ligands`
**Args:**
```json
{
  "name": "oxalic acid",
  "limit": 5
}
```

[summary]
## search_ligands — 4 result(s)

**stats:** 4 SQL matches · showing 4 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8872 | Ethanedioic acid (Oxalic acid) | H2L | Carboxylic acids diacids | 394 | `O=C(O)C(=O)O` | (-inf, H2L, -1.2, HL, 3.8, L, +inf) |
| ligand_8960 | Oxopropanedioic acid (Ketomaloni… (Mesoxalic acid) | H2L | Carboxylic acids diacids… | 3 | `O=C(O)C(=O)C(=O)O` | (-inf, H2L, -1.82, HL, 3.52, L, +inf) |
| ligand_9763 | Dithiooxalic acid | H2L | miscellaneous mercaptans | 3 | `O=C(S)C(=O)S` | *** |
| ligand_11304 | Ethanedi(dithioic acid) (Tetrathiooxalic acid) | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (3 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 2 | 67% |
| ketone | 1 | 33% |
| thiol | 1 | 33% |

---

### Step 26: `search_ligands`
**Args:**
```json
{
  "name": "tartaric acid",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 9 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8955 | D-2,3-Dihydroxybutanedioic acid (D-Tartaric acid) | H2L | Carboxylic acids diacids… | 214 | `O=C(O)C(O)C(O)C(=O)O` | (-inf, H2L, 2.82, HL, 3.97, L, +inf) |
| ligand_8956 | meso-2,3-Dihydroxybutanedioi… (meso-Tartaric acid) | H2L | Carboxylic acids diacids… | 43 | `O=C(O)[C@@H](O)[C@@H](O)C(=O)O` | (-inf, H2L, 2.97, HL, 4.49, L, +inf) |
| ligand_8996 | DL-2,3-Dimercaptobutaned… (DL-Dithiotartaric acid) | H4L | Carboxylic acids diacids… | 9 | `O=C(O)C(S)C(S)C(=O)O` | (-inf, H4L, 2.25, H3L, 3.96, H2L, 9.61, HL, +inf) |
| ligand_8997 | meso-2,3-Dimercaptobut… (meso-Dithiotartaric acid) | H4L | Carboxylic acids diacids… | 41 | `O=C(O)[C@@H](S)[C@@H](S)C(=O)O` | (-inf, H4L, 2.4, H3L, 3.46, H2L, 9.64, HL, 9.64, L, +inf) |
| ligand_10941 | erthro-2-Methyltartaric acid | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (4 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 4 | 100% |
| hydroxyl | 2 | 50% |
| thiol | 2 | 50% |

---

### Step 27: `search_ligands`
**Args:**
```json
{
  "name": "malonic acid",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 36 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5801 | Aminopropanedioic acid (Aminomalonic acid) | H2L | Amino Acids | 14 | `NC(C(=O)O)C(=O)O` | (-inf, H3L, -1.8, H2L, 2.94, HL, 9.22, L, +inf) |
| ligand_5808 | (3-Aminopropyl)malonic acid | H2L | Amino Acids | 18 | `NCCCC(C(=O)O)C(=O)O` | (-inf, H3L, 2.52, H2L, 4.86, HL, 10.45, L, +inf) |
| ligand_8873 | Propanedioic acid (Malonic acid) | H2L | Carboxylic acids diacids | 505 | `O=C(O)CC(=O)O` | (-inf, H2L, 2.65, HL, 5.27, L, +inf) |
| ligand_8874 | Ethane-1,1-dicarboxylic acid (Methylmalonic acid) | H2L | Carboxylic acids diacids | 71 | `CC(C(=O)O)C(=O)O` | (-inf, H2L, 2.87, HL, 5.38, L, +inf) |
| ligand_8875 | Propane-1,1-dicarboxylic acid (Ethylmalonic acid) | H2L | Carboxylic acids diacids | 61 | `CCC(C(=O)O)C(=O)O` | (-inf, H2L, 2.77, HL, 5.46, L, +inf) |

### Functional groups across all SQL matches (32 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 32 | 100% |
| aromatic_ring | 6 | 19% |
| primary_amine | 2 | 6% |
| hydroxyl | 1 | 3% |
| ketone | 1 | 3% |

---

### Step 28: `search_ligands`
**Args:**
```json
{
  "name": "phosphoric acid",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 43 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_9150 | Phosphoric acid methyl ester (Methyl phosphate) | H2L | Organophosphorus and ars… | 12 | `COP(=O)(O)O` | (-inf, HL, 6.25, L, +inf) |
| ligand_9151 | Phosphoric acid butyl ester (Butyl phosphate) | H2L | Organophosphorus and ars… | 11 | `CCCCOP(=O)(O)O` | (-inf, HL, 6.72, L, +inf) |
| ligand_9152 | Phosphoric acid phenyl ester (Phenyl phosphate) | H2L | Organophosphorus and ars… | 24 | `O=P(O)(O)Oc1ccccc1` | (-inf, H2L, -0.9, HL, 5.78, L, +inf) |
| ligand_9153 | Phosphoric acid 4-nitro… (4-Nitrophenyl phosphate) | H2L | Organophosphorus and ars… | 4 | `O=[N+]([O-])c1ccc(OP(=O)(O)O)cc1` | (-inf, HL, 5.01, L, +inf) |
| ligand_9154 | Phosphoric acid 1-naph… (alpha-Naphthyl phosphate) | H2L | Organophosphorus and ars… | 18 | `O=P(O)(O)Oc1cccc2ccccc12` | (-inf, H2L, -0.9, HL, 5.74, L, +inf) |

### Functional groups across all SQL matches (28 parseable SMILES)

| group | count | % |
|-------|-------|---|
| hydroxyl | 26 | 93% |
| phosphate | 23 | 82% |
| aromatic_ring | 6 | 21% |
| secondary_amine | 2 | 7% |
| tertiary_amine | 2 | 7% |
| thiol | 2 | 7% |

---

### Step 29: `search_ligands`
**Args:**
```json
{
  "name": "fluoride",
  "limit": 5
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_10162 | Hydrogen fluoride (Hydrofluoric acid) | HL | Inorganic ligands | 642 | `F` | (-inf, HL, 2.94, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| halide | 1 | 100% |

---

### Step 30: `search_ligands`
**Args:**
```json
{
  "name": "thiocyanate",
  "limit": 5
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_10092 | Hydrogen thiocyanate (Thiocyanic acid) | HL | Inorganic ligands | 434 | `N=C=S` | (-inf, HL, -1.1, L, +inf) |

---

### Step 31: `search_ligands`
**Args:**
```json
{
  "name": "sulfate",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 11 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6852 | 2-Aminoethyl(hydrogensulfate) | HL | Aliphatic amines | 5 | `NCCOS(=O)(=O)O` | (-inf, HL, 9.182, L, +inf) |
| ligand_9382 | 2,3,4-Trihydroxybenzenesulfon… (Pyrogallolsulfate) | H4L | Catechols | 4 | `O=S(=O)(O)c1ccc(O)c(O)c1O` | (-inf, H3L, 8.28, H2L, 11.3, HL, +inf) |
| ligand_10148 | Hydrogen sulfate ion (Sulfuric acid) | HL | Inorganic ligands | 581 | `O=S(=O)([O-])O` | (-inf, HL, 1.54, L, +inf) |
| ligand_10149 | Hydrogen thiosulfate (Thiosulfuric acid) | H2L | Inorganic ligands | 117 | `O=S(O)(O)=S` | (-inf, H2L, -0.6, HL, -0.6, L, +inf) |
| ligand_10150 | Selenosulfate ion | *** | Inorganic ligands | 1 | *** | *** |

### Functional groups across all SQL matches (9 parseable SMILES)

| group | count | % |
|-------|-------|---|
| hydroxyl | 9 | 100% |
| sulfonate | 8 | 89% |
| primary_amine | 3 | 33% |
| aromatic_ring | 1 | 11% |
| phenol | 1 | 11% |
| secondary_amine | 1 | 11% |

---

### Step 32: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT c.ligand_id, c.ligand_name_SRD, c.beta_definition_name, s.constant_value, s.temperature_c, s.ionic_strength_mol_l, s.equation_str FROM ligandmetal_card AS c JOIN ligandmetal_stability_measured AS s ON c.card_id = s.card_id WHERE c.metal_id = 61 AND c.ligand_id IN (8872, 10162, 10148, 10092, 8873, 8955) AND s.constant_type = 'K' ORDER BY c.ligand_id, c.beta_definition_name, s.constant_value DESC LIMIT 80"
}
```

[summary]
## execute_srd46_sql - 50 row(s)

| ligand_id | ligand_name_SRD | beta_definition_name | constant_value | temperature_c | ionic_strength_mol_l | equation_str |
|-----------|-----------------|----------------------|----------------|---------------|----------------------|--------------|
| ligand_8872 | Ethanedioic acid (Oxalic acid) | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | 13.81 | 25.0 | 1.0 | [M] + [L]^2 <=> [ML2] |
| ligand_8872 | Ethanedioic acid (Oxalic acid) | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | 18.6 | 25.0 | 1.0 | [M] + [L]^3 <=> [ML3] |
| ligand_8872 | Ethanedioic acid (Oxalic acid) | [ML]/[M][L] | 7.74 | 25.0 | 3.0 | [M] + [L] <=> [ML] |
| ligand_8872 | Ethanedioic acid (Oxalic acid) | [ML]/[M][L] | 7.58 | 25.0 | 1.0 | [M] + [L] <=> [ML] |
| ligand_8872 | Ethanedioic acid (Oxalic acid) | [ML]/[M][L] | 7.53 | 25.0 | 0.5 | [M] + [L] <=> [ML] |
| ligand_8873 | Propanedioic acid (Malonic acid) | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | 14.0 | 25.0 | 0.1 | [M] + [L]^2 <=> [ML2] |
| ligand_8873 | Propanedioic acid (Malonic acid) | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | 13.29 | 25.0 | 0.5 | [M] + [L]^2 <=> [ML2] |
| ligand_8873 | Propanedioic acid (Malonic acid) | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | 13.04 | 25.0 | 1.0 | [M] + [L]^2 <=> [ML2] |
| ligand_8873 | Propanedioic acid (Malonic acid) | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | 16.93 | 25.0 | 0.5 | [M] + [L]^3 <=> [ML3] |
| ligand_8873 | Propanedioic acid (Malonic acid) | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | 16.6 | 25.0 | 1.0 | [M] + [L]^3 <=> [ML3] |
| ligand_8873 | Propanedioic acid (Malonic acid) | [ML]/[M][L] | 8.12 | 25.0 | 0.1 | [M] + [L] <=> [ML] |
| ligand_8873 | Propanedioic acid (Malonic acid) | [ML]/[M][L] | 7.52 | 25.0 | 0.5 | [M] + [L] <=> [ML] |
| ligand_8873 | Propanedioic acid (Malonic acid) | [ML]/[M][L] | 7.5 | 25.0 | 1.0 | [M] + [L] <=> [ML] |
| ligand_8955 | D-2,3-Dihydroxybutanedioic acid (D-Tartaric acid) | [M<sub>2</sub>(H<sub>-1</sub>L)<sub>2</sub>]/[M<sub>2</sub>(H<sub>-1</sub>L)(H<... | -2.8 | 20.0 | 0.1 | [M2(H-1L)(H-2L)] + [H] <=> [M2(H-1L)2] |
| ligand_8955 | D-2,3-Dihydroxybutanedioic acid (D-Tartaric acid) | [M<sub>2</sub>(H<sub>-1</sub>L)<sub>2</sub>]/[M<sub>2</sub>(H<sub>-2</sub>L)<su... | -4.9 | 25.0 | 1.0 | [M2(H-2L)2] + [H]^2 <=> [M2(H-1L)2] |
| ligand_8955 | D-2,3-Dihydroxybutanedioic acid (D-Tartaric acid) | [M<sub>2</sub>(H<sub>-1</sub>L)<sub>2</sub>][H]<sup>2</sup>/[M]<sup>2</sup>[L]<... | -10.9 | 25.0 | 1.0 | [M]^2 + [L]^2 <=> [M2(H-1L)2] + [H]^2 |
| ligand_8955 | D-2,3-Dihydroxybutanedioic acid (D-Tartaric acid) | [M<sub>2</sub>(H<sub>-1</sub>L)<sub>2</sub>][H]<sup>2</sup>/[M]<sup>2</sup>[L]<... | -11.87 | 20.0 | 0.1 | [M]^2 + [L]^2 <=> [M2(H-1L)2] + [H]^2 |
| ligand_8955 | D-2,3-Dihydroxybutanedioic acid (D-Tartaric acid) | [M<sub>3</sub>(H<sub>-2</sub>L)<sub>3</sub>][H]<sup>6</sup>/[M]<sup>3</sup>[L]<... | -9.5 | 20.0 | 0.1 | [M]^3 + [L]^3 <=> [M3(H-2L)3] + [H]^6 |
| ligand_8955 | D-2,3-Dihydroxybutanedioic acid (D-Tartaric acid) | [ML]/[M][L] | 6.49 | 20.0 | 0.1 | [M] + [L] <=> [ML] |
| ligand_8955 | D-2,3-Dihydroxybutanedioic acid (D-Tartaric acid) | [ML]/[M][L] | 5.73 | 25.0 | 1.0 | [M] + [L] <=> [ML] |
| ligand_10092 | Hydrogen thiocyanate (Thiocyanic acid) | [M(OH)L]/[ML][OH] | -0.6 | 25.0 | 0.0 | [ML] + [OH] <=> [M(OH)L] |
| ligand_10092 | Hydrogen thiocyanate (Thiocyanic acid) | [M(OH)L]/[ML][OH] | -1.1 | 25.0 | 0.1 | [ML] + [OH] <=> [M(OH)L] |
| ligand_10092 | Hydrogen thiocyanate (Thiocyanic acid) | [M(OH)L]/[ML][OH] | -1.2 | 25.0 | 0.5 | [ML] + [OH] <=> [M(OH)L] |
| ligand_10092 | Hydrogen thiocyanate (Thiocyanic acid) | [M(OH)L]/[ML][OH] | -1.2 | 25.0 | 1.0 | [ML] + [OH] <=> [M(OH)L] |
| ligand_10092 | Hydrogen thiocyanate (Thiocyanic acid) | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | 4.6 | 20.0 | 0.0 | [M] + [L]^2 <=> [ML2] |

... 25 more row(s) omitted

---

### Step 33: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT c.ligand_id, c.ligand_name_SRD, c.beta_definition_name, s.constant_value, s.temperature_c, s.ionic_strength_mol_l, s.equation_str FROM ligandmetal_card AS c JOIN ligandmetal_stability_measured AS s ON c.card_id = s.card_id WHERE c.metal_id = 62 AND c.ligand_id IN (8872, 10162, 10148, 10092, 8873, 8955) AND s.constant_type = 'K' ORDER BY c.ligand_id, c.beta_definition_name, s.constant_value DESC LIMIT 80"
}
```

[summary]
## execute_srd46_sql - 10 row(s)

| ligand_id | ligand_name_SRD | beta_definition_name | constant_value | temperature_c | ionic_strength_mol_l | equation_str |
|-----------|-----------------|----------------------|----------------|---------------|----------------------|--------------|
| ligand_8872 | Ethanedioic acid (Oxalic acid) | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | 5.08 | 25.0 | 1.0 | [M] + [L]^2 <=> [ML2] |
| ligand_8872 | Ethanedioic acid (Oxalic acid) | [ML]/[M][L] | 3.05 | 25.0 | 1.0 | [M] + [L] <=> [ML] |
| ligand_8873 | Propanedioic acid (Malonic acid) | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | 3.21 | 25.0 | 1.0 | [M] + [L]^2 <=> [ML2] |
| ligand_8873 | Propanedioic acid (Malonic acid) | [ML]/[M][L] | 2.24 | 25.0 | 1.0 | [M] + [L] <=> [ML] |
| ligand_8873 | Propanedioic acid (Malonic acid) | [ML]/[M][L] | 2.17 | 25.0 | 1.0 | [M] + [L] <=> [ML] |
| ligand_8955 | D-2,3-Dihydroxybutanedioic acid (D-Tartaric acid) | [ML]/[M][L] | 2.24 | 20.0 | 0.1 | [M] + [L] <=> [ML] |
| ligand_10092 | Hydrogen thiocyanate (Thiocyanic acid) | [ML]/[M][L] | 1.31 | 25.0 | 0.0 | [M] + [L] <=> [ML] |
| ligand_10092 | Hydrogen thiocyanate (Thiocyanic acid) | [ML]/[M][L] | 0.81 | 25.0 | 3.0 | [M] + [L] <=> [ML] |
| ligand_10148 | Hydrogen sulfate ion (Sulfuric acid) | [ML]/[M][L] | -2.39 | 25.0 | 0.0 | [M] + [L] <=> [ML] |
| ligand_10162 | Hydrogen fluoride (Hydrofluoric acid) | [ML]/[M][L] | 0.8 | 25.0 | 1.0 | [M] + [L] <=> [ML] |

---

### Step 34: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT c.ligand_id, c.ligand_name_SRD, c.beta_definition_name, s.constant_value, s.temperature_c, s.ionic_strength_mol_l FROM ligandmetal_card AS c JOIN ligandmetal_stability_measured AS s ON c.card_id = s.card_id WHERE c.metal_id = 61 AND c.ligand_id IN (10162, 10148, 10092) AND s.constant_type = 'K' AND c.beta_definition_name LIKE '%[ML]/[M][L]%' ORDER BY c.ligand_id, s.constant_value DESC LIMIT 30"
}
```

[summary]
## execute_srd46_sql - 21 row(s)

| ligand_id | ligand_name_SRD | beta_definition_name | constant_value | temperature_c | ionic_strength_mol_l |
|-----------|-----------------|----------------------|----------------|---------------|----------------------|
| ligand_10092 | Hydrogen thiocyanate (Thiocyanic acid) | [ML]/[M][L] | 3.03 | 25.0 | 0.0 |
| ligand_10092 | Hydrogen thiocyanate (Thiocyanic acid) | [ML]/[M][L] | 2.61 | 25.0 | 5.0 |
| ligand_10092 | Hydrogen thiocyanate (Thiocyanic acid) | [ML]/[M][L] | 2.43 | 25.0 | 4.0 |
| ligand_10092 | Hydrogen thiocyanate (Thiocyanic acid) | [ML]/[M][L] | 2.37 | 25.0 | 0.1 |
| ligand_10092 | Hydrogen thiocyanate (Thiocyanic acid) | [ML]/[M][L] | 2.29 | 25.0 | 3.0 |
| ligand_10092 | Hydrogen thiocyanate (Thiocyanic acid) | [ML]/[M][L] | 2.19 | 25.0 | 3.0 |
| ligand_10092 | Hydrogen thiocyanate (Thiocyanic acid) | [ML]/[M][L] | 2.19 | 25.0 | 4.0 |
| ligand_10092 | Hydrogen thiocyanate (Thiocyanic acid) | [ML]/[M][L] | 2.15 | 25.0 | 0.5 |
| ligand_10092 | Hydrogen thiocyanate (Thiocyanic acid) | [ML]/[M][L] | 2.11 | 25.0 | 2.0 |
| ligand_10092 | Hydrogen thiocyanate (Thiocyanic acid) | [ML]/[M][L] | 2.08 | 25.0 | 1.0 |
| ligand_10092 | Hydrogen thiocyanate (Thiocyanic acid) | [ML]/[M][L] | 2.08 | 25.0 | 3.0 |
| ligand_10092 | Hydrogen thiocyanate (Thiocyanic acid) | [ML]/[M][L] | 2.01 | 25.0 | 2.0 |
| ligand_10092 | Hydrogen thiocyanate (Thiocyanic acid) | [ML]/[M][L] | 1.97 | 25.0 | 2.0 |
| ligand_10148 | Hydrogen sulfate ion (Sulfuric acid) | [ML]/[M][L] | 4.05 | 25.0 | 0.0 |
| ligand_10148 | Hydrogen sulfate ion (Sulfuric acid) | [ML]/[M][L] | 2.8 | 25.0 | 0.1 |
| ligand_10148 | Hydrogen sulfate ion (Sulfuric acid) | [ML]/[M][L] | 2.34 | 25.0 | 0.5 |
| ligand_10148 | Hydrogen sulfate ion (Sulfuric acid) | [ML]/[M][L] | 1.96 | 25.0 | 1.0 |
| ligand_10148 | Hydrogen sulfate ion (Sulfuric acid) | [ML]/[M][L] | 1.93 | 25.0 | 3.0 |
| ligand_10162 | Hydrogen fluoride (Hydrofluoric acid) | [ML]/[M][L] | 6.04 | 25.0 | 0.0 |
| ligand_10162 | Hydrogen fluoride (Hydrofluoric acid) | [ML]/[M][L] | 5.17 | 25.0 | 0.5 |
| ligand_10162 | Hydrogen fluoride (Hydrofluoric acid) | [ML]/[M][L] | 5.15 | 25.0 | 1.0 |

---

### Step 35: `search_pka_values`
**Args:**
```json
{
  "where": "(lc.ligand_id IN (8872, 8873, 8955, 10162, 10148, 10092, 9337))",
  "order_by": "lc.ligand_id, p.pKa ASC",
  "limit": 50
}
```

[summary]
## search_pka_values — 11 row(s)

### pKa -13.5–-13.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_161529 | ligand_9337 | 1,2-Dihydroxybenzene (Catechol) | H2L | Oc1ccccc1O | -13.3 | 25 | 0.1 | L→HL | M_tot_3 | M_tot_3 |

### pKa -1.5–-1.0 (2 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_151532 | ligand_8872 | Ethanedioic acid (Oxalic acid) | H2L | O=C(O)C(=O)O | -1.2 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_7 |
| vlm_172116 | ligand_10092 | Hydrogen thiocyanate (Thiocyanic a… | HL | N=C=S | -1.1 | 20 | 0 | L→HL | M_tot_1 | M_tot_65 |

### pKa 1.5–2.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_175604 | ligand_10148 | Hydrogen sulfate ion (Sulfuric aci… | HL | O=S(=O)([O-])O | 1.54 | 25 | 0.1 | L→HL | M_tot_1 | M_tot_74 |

### pKa 2.5–3.0 (3 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_151949 | ligand_8873 | Propanedioic acid (Malonic acid) | H2L | O=C(O)CC(=O)O | 2.65 | 25 | 0.1 | HL→H2L | M_tot_2 | M_tot_26 |
| vlm_154900 | ligand_8955 | D-2,3-Dihydroxybutanedioic acid (D… | H2L | O=C(O)C(O)C(O)C(=O)O | 2.82 | 25 | 0.1 | HL→H2L | M_tot_3 | M_tot_17 |
| vlm_176587 | ligand_10162 | Hydrogen fluoride (Hydrofluoric ac… | HL | F | 2.94 | 25 | 0.1 | L→HL | M_tot_2 | M_tot_77 |

### pKa 3.5–4.0 (2 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_151494 | ligand_8872 | Ethanedioic acid (Oxalic acid) | H2L | O=C(O)C(=O)O | 3.8 | 25 | 0.1 | L→HL | M_tot_7 | M_tot_56 |
| vlm_154888 | ligand_8955 | D-2,3-Dihydroxybutanedioic acid (D… | H2L | O=C(O)C(O)C(O)C(=O)O | 3.97 | 25 | 0.1 | L→HL | M_tot_17 | M_tot_49 |

### pKa 5.0–5.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_151918 | ligand_8873 | Propanedioic acid (Malonic acid) | H2L | O=C(O)CC(=O)O | 5.27 | 25 | 0.1 | L→HL | M_tot_26 | M_tot_50 |

### pKa 9.0–9.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_161533 | ligand_9337 | 1,2-Dihydroxybenzene (Catechol) | H2L | Oc1ccccc1O | 9.26 | 25 | 0.1 | HL→H2L | M_tot_41 | M_tot_3 |

---

### Step 36: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT c.ligand_id, c.ligand_name_SRD, c.beta_definition_name, s.constant_value, s.temperature_c, s.ionic_strength_mol_l FROM ligandmetal_card AS c JOIN ligandmetal_stability_measured AS s ON c.card_id = s.card_id WHERE c.metal_id = 61 AND c.ligand_id IN (9058, 9284, 9257) AND s.constant_type = 'K' AND c.beta_definition_name LIKE '%[ML]%[M]%[L]%' ORDER BY c.ligand_id, c.beta_definition_name, s.constant_value DESC LIMIT 50"
}
```

[summary]
## execute_srd46_sql - 3 row(s)

| ligand_id | ligand_name_SRD | beta_definition_name | constant_value | temperature_c | ionic_strength_mol_l |
|-----------|-----------------|----------------------|----------------|---------------|----------------------|
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) | [ML]/[M][L] | 11.27 | 25.0 | 0.1 |
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) | [ML]/[M][L] | 11.19 | 25.0 | 0.1 |
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) | [ML]/[M][L] | 10.25 | 25.0 | 1.0 |

---

### Step 37: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT c.ligand_id, c.ligand_name_SRD, c.beta_definition_name, s.constant_value, s.temperature_c, s.ionic_strength_mol_l FROM ligandmetal_card AS c JOIN ligandmetal_stability_measured AS s ON c.card_id = s.card_id WHERE c.metal_id = 62 AND c.ligand_id IN (9058, 9284, 9257) AND s.constant_type = 'K' ORDER BY c.ligand_id, c.beta_definition_name, s.constant_value DESC LIMIT 50"
}
```

[summary]
## execute_srd46_sql - 14 row(s)

| ligand_id | ligand_name_SRD | beta_definition_name | constant_value | temperature_c | ionic_strength_mol_l |
|-----------|-----------------|----------------------|----------------|---------------|----------------------|
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) | [M<sub>2</sub>(H<sub>-1</sub>L)<sub>2</sub>][H]<sup>2</sup>/[M]<sup>2</sup>[L]<... | -5.4 | 37.0 | 0.15 |
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) | [MH<sub>2</sub>L]/[M][H<sub>2</sub>L] | 1.1 | 37.0 | 0.15 |
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) | [MHL<sub>2</sub>]/[MHL][L] | 3.19 | 37.0 | 0.15 |
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) | [MHL]/[M][HL] | 3.1 | 37.0 | 0.15 |
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) | [MHL]/[M][HL] | 2.9 | 25.0 | 0.1 |
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) | [MHL]/[M][HL] | 2.65 | 20.0 | 0.1 |
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) | [MHL]/[M][HL] | 2.6 | 25.0 | 3.0 |
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) | [ML]/[M][L] | 4.7 | 37.0 | 0.15 |
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) | [ML]/[M][L] | 4.56 | 37.0 | 0.15 |
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) | [ML]/[M][L] | 4.4 | 20.0 | 0.1 |
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) | [ML]/[M][L] | -4.8 | 25.0 | 0.1 |
| ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | [ML<sub>2</sub>][H]/[ML][HL] | -8.9 | 20.0 | 0.1 |
| ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | [ML][H]/[M][HL] | -6.8 | 20.0 | 0.1 |
| ligand_9284 | 2-Hydroxy-5-sulfobenzoic acid (5-Sulfosalicylic acid) | [ML][H]/[M][HL] | -5.9 | 20.0 | 0.1 |

---

### Step 38: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT c.ligand_id, c.ligand_name_SRD, c.beta_definition_name, s.constant_value, s.temperature_c, s.ionic_strength_mol_l FROM ligandmetal_card AS c JOIN ligandmetal_stability_measured AS s ON c.card_id = s.card_id WHERE c.metal_id = 61 AND c.ligand_id IN (9284, 9257, 9337) AND s.constant_type = 'K' ORDER BY c.ligand_id, c.beta_definition_name, s.constant_value DESC LIMIT 60"
}
```

[summary]
## execute_srd46_sql - 22 row(s)

| ligand_id | ligand_name_SRD | beta_definition_name | constant_value | temperature_c | ionic_strength_mol_l |
|-----------|-----------------|----------------------|----------------|---------------|----------------------|
| ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | [MHL]/[M][HL] | 4.4 | 25.0 | 0.1 |
| ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | [ML<sub>2</sub>][H]/[ML][HL] | -1.5 | 25.0 | 3.0 |
| ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | [ML<sub>2</sub>][H]/[ML][HL] | -1.7 | 25.0 | 0.1 |
| ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | [ML<sub>2</sub>][H]/[ML][HL] | -1.7 | 20.0 | 0.1 |
| ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | [ML][H]/[M][HL] | 2.9 | 25.0 | 0.1 |
| ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | [ML][H]/[M][HL] | 2.85 | 25.0 | 0.5 |
| ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | [ML][H]/[M][HL] | 2.73 | 20.0 | 1.0 |
| ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | [ML][H]/[M][HL] | 2.7 | 25.0 | 1.0 |
| ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | [ML][H]/[M][HL] | 2.69 | 25.0 | 3.0 |
| ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | [ML][H]/[M][HL] | -2.74 | 20.0 | 0.1 |
| ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | [ML][H]/[M][HL] | -3.85 | 25.0 | 0.0 |
| ligand_9284 | 2-Hydroxy-5-sulfobenzoic acid (5-Sulfosalicylic acid) | [ML<sub>2</sub>][H]/[ML][HL] | -0.9 | 25.0 | 3.0 |
| ligand_9284 | 2-Hydroxy-5-sulfobenzoic acid (5-Sulfosalicylic acid) | [ML<sub>2</sub>][H]/[ML][HL] | -1.4 | 20.0 | 0.1 |
| ligand_9284 | 2-Hydroxy-5-sulfobenzoic acid (5-Sulfosalicylic acid) | [ML<sub>3</sub>][H]/[ML<sub>2</sub>][HL] | -4.7 | 25.0 | 3.0 |
| ligand_9284 | 2-Hydroxy-5-sulfobenzoic acid (5-Sulfosalicylic acid) | [ML][H]/[M][HL] | 2.7 | 25.0 | 0.1 |
| ligand_9284 | 2-Hydroxy-5-sulfobenzoic acid (5-Sulfosalicylic acid) | [ML][H]/[M][HL] | 2.69 | 25.0 | 1.0 |
| ligand_9284 | 2-Hydroxy-5-sulfobenzoic acid (5-Sulfosalicylic acid) | [ML][H]/[M][HL] | 2.68 | 25.0 | 3.0 |
| ligand_9284 | 2-Hydroxy-5-sulfobenzoic acid (5-Sulfosalicylic acid) | [ML][H]/[M][HL] | 2.65 | 20.0 | 0.1 |
| ligand_9337 | 1,2-Dihydroxybenzene (Catechol) | [ML<sub>2</sub>][H]<sup>2</sup>/[ML][H<sub>2</sub>L] | -7.53 | 25.0 | 0.1 |
| ligand_9337 | 1,2-Dihydroxybenzene (Catechol) | [ML<sub>3</sub>][H]<sup>2</sup>/[ML<sub>2</sub>][H<sub>2</sub>L] | -13.16 | 25.0 | 0.1 |
| ligand_9337 | 1,2-Dihydroxybenzene (Catechol) | [ML][H]<sup>2</sup>/[M][H<sub>2</sub>L] | -1.36 | 25.0 | 1.0 |
| ligand_9337 | 1,2-Dihydroxybenzene (Catechol) | [ML][H]<sup>2</sup>/[M][H<sub>2</sub>L] | -2.2 | 25.0 | 0.1 |

---
