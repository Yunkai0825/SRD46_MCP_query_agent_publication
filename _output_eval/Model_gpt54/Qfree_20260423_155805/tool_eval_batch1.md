# Qfree_20260423_155805 — Tool Results (batch 1)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Fe(II), Fe(III), H+",
  "limit": 10
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
  "name": "iron",
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

### Step 5: `db_ranked_pairs`
**Args:**
```json
{
  "rank_by": "measurement_count",
  "limit": 40,
  "where": "lc.metal_id IN (metal_61, metal_62)"
}
```

[summary]
**db_ranked_pairs:** Error - Unknown rank_by='measurement_count'. Choose from: ['ligands_per_metal', 'measurements_per_ligand', 'measurements_per_metal', 'metals_per_ligand', 'pka_per_ligand']

---

### Step 6: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_61, metal_62) AND s.solvent_name LIKE '%water%' AND s.reaction_type LIKE '%H%')",
  "order_by": "c.ligand_id ASC, c.metal_id ASC, s.constant_value DESC",
  "limit": 400
}
```

[TOOL ERROR] search_stability: Error executing tool search_stability: SQL parse error: Invalid expression / Unexpected token. Line 1, Col: 41.
  SELECT 1 FROM _stub WHERE c.ligand_id [4mASC[0m, c.metal_id ASC, s.constant_value DESC

---

### Step 7: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_stability_measured",
  "group_column": "reaction_type",
  "where": "metal_id IN (61,62)",
  "limit": 50
}
```

[TOOL ERROR] db_distribution: Error executing tool db_distribution: no such column: metal_id

---

### Step 8: `get_table_schema`
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

### Step 9: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_61, metal_62) AND s.solvent_name LIKE '%water%')",
  "order_by": "c.ligand_id ASC, c.metal_id ASC",
  "limit": 400
}
```

[TOOL ERROR] search_stability: Error executing tool search_stability: SQL parse error: Invalid expression / Unexpected token. Line 1, Col: 41.
  SELECT 1 FROM _stub WHERE c.ligand_id [4mASC[0m, c.metal_id ASC

---

### Step 10: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_61, metal_62) AND s.solvent_name LIKE '%water%')",
  "limit": 400
}
```

[summary]
## search_stability

*(no results)*

---

### Step 11: `db_ranked_pairs`
**Args:**
```json
{
  "rank_by": "measurements_per_ligand",
  "limit": 60,
  "where": "lc.metal_id IN (metal_61, metal_62)"
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

---

### Step 12: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61)",
  "limit": 200
}
```

[summary]
## search_stability — 200 row(s)

### logK — 74 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 14 | 8 | 20~25 | 0.1~1 | *** | 4 |
| metal_61 | Fe^[3+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 6 | 3 | 25 | 0.5~3 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_6204 | N-(2-Hydroxyethyl)iminodiac… | H2L | O=C(O)CN(CCO)CC(=O)O | 6 | 5 | 20~25 | 0.1~1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_5937 | N-(Phosphonomethyl)glycine … | H3L | O=C(O)CNCP(=O)(O)O | 5 | 5 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6041 | N,N'-Bis(3-hydroxy-5-phosph… | H6L | Cc1ncc(COP(=O)(O)O)c(CN(CCN(CC(=O)O)Cc2c(COP(=O)(O)O)cnc(C)c2O)CC(=O)O)c1O | 5 | 5 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6047 | N,N''-Bis(3-hydroxy-6-methy… | H5L | Cc1ccc(O)c(CN(CCN(CCN(CC(=O)O)Cc2nc(C)ccc2O)CC(=O)O)CC(=O)O)n1 | 5 | 5 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 5 | 4 | 25 | 0.1~1 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_5777 | L-2-Amino-3-phenylpropanoic… | HL | N[C@@H](Cc1ccccc1)C(=O)O | 4 | 3 | 20~25 | 1~3 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_5938 | (Carboxymethylamino)acetohy… | H2L | O=C(O)CNCC(=O)NO | 4 | 4 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6036 | N,N'-Bis(carboxymethyl)ethy… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)NO)CC(=O)NO | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6039 | N,N"-Bis(2-hydroxybenzyl)di… | *** | *** | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6054 | N,N'-Bis(carboxymethyl)ethy… | H4L | CC(C)N(O)C(=O)CN(CCN(CC(=O)O)CC(=O)N(O)C(C)C)CC(=O)O | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6057 | N,N',N''-Tris(carboxymethyl… | H5L | CC(C)N(O)C(=O)CN(CCN(CCN(CC(=O)O)CC(=O)N(O)C(C)C)CC(=O)O)CC(=O)O | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6113 | 1-Oxa-4,7,10,13-tetraazacyc… | H4L | O=C(O)CN1CCOCCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6123 | 7,24-Dihydroxy-8,23-dioxo-1… | H2L | O=C(O)CN1CCOCCOCCN(CC(=O)O)CCC(=O)N(O)CCOCCOCCN(O)C(=O)CC1 | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6124 | 6,16-Bis(carboxymethyl)-1,1… | *** | *** | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6125 | 7,19-Bis(carboxymethyl)-1,1… | *** | *** | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6203 | N,N-Bis(carboxymethyl)amino… | H3L | O=C(O)CN(CC(=O)O)CC(=O)NO | 4 | 4 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5809 | L-2-Amino-3-phosphopropanoi… | H3L | N[C@@H](COP(=O)(O)O)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5976 | Ethylenediiminodi-3-propano… | H2L | O=C(O)CCNCCNCCC(=O)O | 3 | 3 | 30 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5977 | Ethylenediiminodi-2-propano… | H2L | CC(NCCNC(C)C(=O)O)C(=O)O | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5996 | meso-Ethylenediiminobis[(2-… | H4L | O=C(O)C(Cc1ccccc1O)NCCNC(Cc1ccccc1O)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5997 | rac-Trimethylenebis[2-(2-hy… | *** | *** | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5998 | meso-Trimethylenebis[2-(2-h… | H4L | Cc1cc(C)c(O)c([C@H](NCCCN[C@@H](C(=O)O)c2cc(C)cc(C)c2O)C(=O)O)c1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6019 | N,N-Bis(phosphonomethyl)gly… | H5L | O=C(O)CN(CP(=O)(O)O)CP(=O)(O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6020 | N-(Carboxymethyl)-N-(2-hydr… | H2L | O=C(O)CN(CCO)CC(=O)NO | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6042 | N,N'-Bis(3-hydroxy-5-hydrox… | H4L | Cc1ncc(CO)c(CN(CCN(CC(=O)O)Cc2c(CO)cnc(C)c2O)CC(=O)O)c1O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6044 | N-(2-Hydroxybenzyl)-N'-(3-h… | H4L | Cc1ncc(CO)c(CN(CCN(CC(=O)O)Cc2ccccc2O)CC(=O)O)c1O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6046 | N,N'-Bis(3-hydroxy-6-methyl… | H4L | Cc1ccc(O)c(CN(CCN(CC(=O)O)Cc2nc(C)ccc2O)CC(=O)O)n1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6084 | 1-Oxa-4,7,10-triazacyclodod… | H3L | O=C(O)CN1CCOCCN(CC(=O)O)CCN(CC(=O)O)CC1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6086 | 1-Oxa-4,8,12-triazacyclotet… | H3L | O=C(O)CN1CCCN(CC(=O)O)CCOCCN(CC(=O)O)CCC1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6087 | 1,7-Dioxa-4,10,13-triazacyc… | H3L | O=C(O)CN1CCOCCN(CC(=O)O)CCN(CC(=O)O)CCOCC1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6121 | 3,6,9-Tris(carboxymethyl)-3… | H3L | O=C(O)CN1CCN(CC(=O)O)Cc2cccc(n2)CN(CC(=O)O)CC1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6135 | L-2-(Carboxymethyl)iminodia… | H3L | O=C(O)CNC(CC(=O)O)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6188 | DL-2-(2-Methylthioethyl)nit… | H3L | CSCCC(C(=O)O)N(CC(=O)O)CC(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6197 | N-(2-Hydroxybenzyl)iminodia… | H3L | O=C(O)CN(CC(=O)O)Cc1ccccc1O | 3 | 3 | 25 | 0.1~1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_5761 | L-2-Aminopropanoic acid (Al… | HL | C[C@H](N)C(=O)O | 2 | 2 | 25 | 0.5 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5994 | N,N'-Bis(2-hydroxyphenyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)c1ccccc1O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5995 | rac-Ethylenediiminobis[(2-h… | H4L | O=C(O)C(Cc1ccccc1O)NCCNC(Cc1ccccc1O)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5999 | Ethylenediiminobis(3-hydrox… | H2L | O=C(O)C(CO)NCCNC(CO)C(=O)O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6000 | Ethylenediiminobis(4-hydrox… | H2L | O=C(O)C(CCO)NCCNC(CCO)C(=O)O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6021 | N,N-Bis(2-hydroxyethyl)glyc… | HL | O=C(O)CN(CCO)CCO | 2 | 2 | 20~25 | 0.1~0.5 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_6035 | N,N'-Bis(carboxymethylamino… | H4L | O=C(O)CNC(=O)CN(CCN(CC(=O)O)CC(=O)NCC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6037 | N,N'-Bis(2-hydroxybenzyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)Cc1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6038 | N,N'-Bis(2-hydroxy-5-sulfob… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1cc(S(=O)(=O)O)ccc1O)Cc1cc(S(=O)(=O)O)ccc1O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6048 | N,N'-Bis(2-hydroxyethyl)eth… | H2L | O=C(O)CN(CCO)CCN(CCO)CC(=O)O | 2 | 2 | 30 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6085 | 1-Oxa-4,7,11-triazacyclotri… | H3L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCOCC1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6088 | 1,7,13-Trioxa-4,10,16-triaz… | H3L | O=C(O)CN1CCOCCN(CC(=O)O)CCOCCN(CC(=O)O)CCOCC1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6102 | 1,4,7,10-Tetraazacyclododec… | H4L | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6104 | 1,4,7,10-Tetraazacyclotride… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6109 | 1,4,8,11-Tetraazacyclotetra… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCCN(CC(=O)O)CC1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6120 | 3,11-Bis(carboxymethyl)-7-m… | H2L | CN1CCCN(CC(=O)O)Cc2cccc(n2)CN(CC(=O)O)CCC1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5804 | L-2-Aminopentanedioic acid … | H2L | N[C@@H](CCC(=O)O)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5826 | L-2-Amino-3-(3,4-dihydroxyp… | H3L | NC(Cc1ccc(O)c(O)c1)C(=O)O | 1 | 1 | 25 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5828 | L-2-Amino-3-hydroxypropanoi… | HL | N[C@@H](CO)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5829 | L-2-Amino-3-hydroxybutanoic… | HL | C[C@@H](O)[C@H](N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5843 | L-2-Aminobutanedioic acid 4… | HL | NC(=O)C[C@H](N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5863 | L-2-Amino-4-(methylthio)but… | HL | CSCC[C@H](N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5886 | L-2,5-Diaminopentanoic acid… | HL | NCCC[C@H](N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5907 | L-2-Amino-3-(3-indolyl)prop… | HL | N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5911 | L-2-Amino-3-(3-hydroxo-4-ox… | HL | N[C@@H](Cn1ccc(=O)c(O)c1)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5917 | L-2-Amino-5-guanidopentanoi… | H2L | N=C(N)NCCC[C@H](N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5925 | N-Methylglycine (Sarcosine) | HL | CNCC(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5930 | L-Pyrrolidine-2-carboxylic … | HL | O=C(O)C1CCCN1 | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5941 | L-4-Hydroxypyrrolidine-2-ca… | HL | O=C(O)C1CC(O)CN1 | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5984 | Ethylenediiminodibutanedioi… | H4L | O=C(O)CC(NCCNC(CC(=O)O)C(=O)O)C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6043 | N,N'-Bis(3-hydroxy-5-hydrox… | H4L | Cc1c([O-])c(CN(CCN(CC(=O)O)Cc2c(CO)c[n+](C)c(C)c2[O-])CC(=O)O)c(CO)c[n+]1C | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6045 | N-(2-Hydroxy-3,5-dimethylbe… | H4L | Cc1cc(C)c(O)c(CN(CCN(CC(=O)O)Cc2c(C)c[n+](C)c(C)c2[O-])CC(=O)O)c1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6063 | 1,5-Diazacyclooctane-N,N'-d… | H2L | O=C(O)CN1CCCN(CC(=O)O)CCC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6076 | 1,4,7-Triazacyclononane-N,N… | H3L | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6195 | N-(2-Carboxyethyl)-N-(phosp… | H4L | O=C(O)CCN(CC(=O)O)CP(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6200 | N-(3-Carboxy-2-hydroxy-5-su… | H4L | O=C(O)CN(CC(=O)O)Cc1cc(S(=O)(=O)O)cc(C(=O)O)c1O | 1 | 1 | 25 | 0.1 | *** | 1 |

### ΔH — 1 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 0 |

### ΔS — 1 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |

---

### Step 13: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_62)",
  "limit": 200
}
```

[summary]
## search_stability — 200 row(s)

### logK — 70 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 10 | 3 | 10~40 | 0~3 | *** | 7 |
| metal_62 | Fe^[2+] | ligand_5828 | L-2-Amino-3-hydroxypropanoi… | HL | N[C@@H](CO)C(=O)O | 8 | 3 | 20~37 | 0.1~3 | *** | 4 |
| metal_62 | Fe^[2+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 7 | 3 | 20~25 | 0.1~1 | *** | 3 |
| metal_62 | Fe^[2+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 6 | 2 | 20~25 | 0.1~1 | *** | 3 |
| metal_62 | Fe^[2+] | ligand_5829 | L-2-Amino-3-hydroxybutanoic… | HL | C[C@@H](O)[C@H](N)C(=O)O | 5 | 2 | 20~37 | 0.1~1 | *** | 3 |
| metal_62 | Fe^[2+] | ligand_6140 | N-Methyliminodiacetic acid … | H2L | CN(CC(=O)O)CC(=O)O | 5 | 3 | 20~25 | 0.1 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_6193 | N-(Phosphonomethyl)iminodia… | H4L | O=C(O)CN(CC(=O)O)CP(=O)(O)O | 5 | 5 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6287 | rac-(1,2-Dimethylethylene)d… | H4L | CC(C(C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 5 | 3 | 20~25 | 0.1 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_6288 | meso-(1,2-Dimethylethylene)… | H4L | C[C@H]([C@H](C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 5 | 3 | 20~25 | 0.1 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_5777 | L-2-Amino-3-phenylpropanoic… | HL | N[C@@H](Cc1ccccc1)C(=O)O | 4 | 3 | 20~25 | 1~3 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_5843 | L-2-Aminobutanedioic acid 4… | HL | NC(=O)C[C@H](N)C(=O)O | 4 | 3 | 20~25 | 1~3 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_5907 | L-2-Amino-3-(3-indolyl)prop… | HL | N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O | 4 | 3 | 20~25 | 1~3 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_6135 | L-2-(Carboxymethyl)iminodia… | H3L | O=C(O)CNC(CC(=O)O)C(=O)O | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6188 | DL-2-(2-Methylthioethyl)nit… | H3L | CSCCC(C(=O)O)N(CC(=O)O)CC(=O)O | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7653 | 6,16-Dioxa-3,9,13,19-tetraa… | L | c1cc2nc(c1)CNCCOCCNCc1cccc(n1)CNCCOCCNC2 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5844 | L-2-Aminopentanedioic acid … | HL | NC(=O)CC[C@H](N)C(=O)O | 3 | 3 | 25 | 3 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5937 | N-(Phosphonomethyl)glycine … | H3L | O=C(O)CNCP(=O)(O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6051 | DL-1-Ethylethylenedinitrilo… | H2L | CCC(CN(CC(N)=O)CC(=O)O)N(CC(N)=O)CC(=O)O | 3 | 3 | 37 | 0.15 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6052 | rac-1,2-Dimethylethylenedin… | H2L | CC(C(C)N(CC(N)=O)CC(=O)O)N(CC(N)=O)CC(=O)O | 3 | 3 | 37 | 0.15 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6053 | meso-1,2-Dimethylethylenedi… | H2L | CC(C(C)N(CC(N)=O)CC(=O)O)N(CC(N)=O)CC(=O)O | 3 | 3 | 37 | 0.15 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6109 | 1,4,8,11-Tetraazacyclotetra… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCCN(CC(=O)O)CC1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6142 | N-Propyliminodiacetic acid | H2L | CCCN(CC(=O)O)CC(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6253 | N-(2-Aminoethyl)iminodiacet… | H2L | NCCN(CC(=O)O)CC(=O)O | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5860 | DL-2-Amino-3-(2-mercaptoimi… | H2L | NC(Cc1cnc(S)[nH]1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 2 | 2 | 25 | 3 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5917 | L-2-Amino-5-guanidopentanoi… | H2L | N=C(N)NCCC[C@H](N)C(=O)O | 2 | 1 | 20~25 | 0.1~1 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_5975 | Ethylenediiminodiacetic aci… | H2L | O=C(O)CNCCNCC(=O)O | 2 | 2 | 25 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6021 | N,N-Bis(2-hydroxyethyl)glyc… | HL | O=C(O)CN(CCO)CCO | 2 | 2 | 30 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6050 | DL-1-Methylethylenedinitril… | H2L | CC(CN(CC(N)=O)CC(=O)O)N(CC(N)=O)CC(=O)O | 2 | 2 | 37 | 0.15 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6068 | 1,4-Dioxa-7,11-diazacyclotr… | H2L | O=C(O)CN1CCCN(CC(=O)O)CCOCCOCC1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6082 | 1-Oxa-4,7,10-triazacyclodod… | H2L | O=C(O)CN1CCNCCN(CC(=O)O)CCOCC1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6084 | 1-Oxa-4,7,10-triazacyclodod… | H3L | O=C(O)CN1CCOCCN(CC(=O)O)CCN(CC(=O)O)CC1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6102 | 1,4,7,10-Tetraazacyclododec… | H4L | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6104 | 1,4,7,10-Tetraazacyclotride… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6141 | N-Ethyliminodiacetic acid | H2L | CCN(CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6204 | N-(2-Hydroxyethyl)iminodiac… | H2L | O=C(O)CN(CCO)CC(=O)O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6222 | N-(2-Methoxyethyl)iminodiac… | H2L | COCCN(CC(=O)O)CC(=O)O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6248 | N-(2-Mercaptoethyl)iminodia… | H3L | O=C(O)CN(CCS)CC(=O)O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6249 | N-[2-(Methylthio)ethyl]imin… | H2L | CSCCN(CC(=O)O)CC(=O)O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6292 | DL-Ethylenedinitrilo-N,N'-d… | H4L | CC(C(=O)O)N(CCN(CC(=O)O)C(C)C(=O)O)CC(=O)O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5761 | L-2-Aminopropanoic acid (Al… | HL | C[C@H](N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5762 | DL-2-Aminobutanoic acid | HL | CCC(N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5765 | L-2-Amino-3-methylbutanoic … | HL | CC(C)[C@H](N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5766 | L-2-Amino-4-methylpentanoic… | HL | CC(C)C[C@H](N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5769 | 2-Amino-2-methylpropanoic a… | HL | CC(C)(N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5770 | DL-2-Amino-4-pentenoic acid | HL | C=CCC(N)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5788 | 3-Aminopropanoic acid (beta… | HL | NCCC(=O)O | 1 | 1 | 25 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5804 | L-2-Aminopentanedioic acid … | H2L | N[C@@H](CCC(=O)O)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5856 | L-2-Amino-3-mercaptopropano… | H2L | N[C@@H](CS)C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5863 | L-2-Amino-4-(methylthio)but… | HL | CSCC[C@H](N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5886 | L-2,5-Diaminopentanoic acid… | HL | NCCC[C@H](N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5889 | DL-2,6-Diamino-5-hydroxyhex… | HL | NCC(O)CCC(N)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5925 | N-Methylglycine (Sarcosine) | HL | CNCC(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5930 | L-Pyrrolidine-2-carboxylic … | HL | O=C(O)C1CCCN1 | 1 | 1 | 20 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5941 | L-4-Hydroxypyrrolidine-2-ca… | HL | O=C(O)C1CC(O)CN1 | 1 | 1 | 20 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5976 | Ethylenediiminodi-3-propano… | H2L | O=C(O)CCNCCNCCC(=O)O | 1 | 1 | 30 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5977 | Ethylenediiminodi-2-propano… | H2L | CC(NCCNC(C)C(=O)O)C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6056 | N,N'-Bis(2-pyridylmethyl)et… | H2L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccn1)Cc1ccccn1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6064 | 1-Oxa-4,7-diazacyclononane-… | H2L | O=C(O)CN1CCOCCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6067 | 1,4-Dioxa-7,10-diazacyclodo… | H2L | O=C(O)CN1CCOCCOCCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6069 | 1,7-Dioxa-4,10-diazacyclodo… | H2L | O=C(O)CN1CCOCCN(CC(=O)O)CCOCC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6070 | 1,4,10-Trioxa-7,13-diazacyc… | H2L | O=C(O)CN1CCOCCOCCN(CC(=O)O)CCOCC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6071 | 1,4,10,13-Tetraoxa-7,16-dia… | H2L | O=C(O)CN1CCOCCOCCN(CC(=O)O)CCOCCOCC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6224 | N-(2-Tetrahydropyranylmethy… | H2L | O=C(O)CN(CC(=O)O)CC1CCCCO1 | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6243 | 5-Amino-2,4,6-trioxo-1,3-pe… | H3L | O=C(O)CN(CC(=O)O)C1C(=O)NC(=O)NC1=O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |

### ΔH — 8 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 3 | 1 | 10~40 | 0 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_5828 | L-2-Amino-3-hydroxypropanoi… | HL | N[C@@H](CO)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_5829 | L-2-Amino-3-hydroxybutanoic… | HL | C[C@@H](O)[C@H](N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 2 | 2 | 25 | 3 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_5907 | L-2-Amino-3-(3-indolyl)prop… | HL | N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O | 2 | 2 | 25 | 3 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |

### ΔS — 8 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_62 | Fe^[2+] | ligand_5828 | L-2-Amino-3-hydroxypropanoi… | HL | N[C@@H](CO)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_5829 | L-2-Amino-3-hydroxybutanoic… | HL | C[C@@H](O)[C@H](N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 2 | 2 | 25 | 3 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_5907 | L-2-Amino-3-(3-indolyl)prop… | HL | N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O | 2 | 2 | 25 | 3 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |

---

### Step 14: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT c.metal_id, c.metal_name_SRD, c.ligand_id, c.ligand_name_SRD, c.beta_definition_id, c.beta_definition_name, s.constant_type, s.constant_value, s.temperature_c, s.ionic_strength_mol_l, s.reaction_type, s.solvent_name, s.electrolyte_composition FROM ligandmetal_card AS c JOIN ligandmetal_stability_measured AS s ON c.ligandmetal_id = s.ligandmetal_id WHERE c.metal_id IN (61, 62) AND c.ligand_id IN (6165, 6127, 6204, 5937, 5760, 6021, 6135, 6188, 5802, 5804, 5777, 5761, 5976, 5977, 6084, 6102, 6104, 6109) ORDER BY c.ligand_id, c.metal_id, s.constant_type, s.temperature_c, s.ionic_strength_mol_l, s.constant_value DESC",
  "attach_equilibrium": false,
  "attach_literature": false
}
```

[TOOL ERROR] execute_srd46_sql: Error executing tool execute_srd46_sql: no such column: c.ligandmetal_id

---

### Step 15: `search_pka_values`
**Args:**
```json
{
  "where": "(lc.ligand_id IN (ligand_6165, ligand_6127, ligand_6204, ligand_5937, ligand_5760, ligand_6021, ligand_6135, ligand_6188))",
  "order_by": "lc.ligand_id ASC, p.pKa ASC",
  "limit": 200
}
```

[TOOL ERROR] search_pka_values: Error executing tool search_pka_values: SQL parse error: Invalid expression / Unexpected token. Line 1, Col: 42.
  SELECT 1 FROM _stub WHERE lc.ligand_id [4mASC[0m, p.pKa ASC

---

### Step 16: `search_pka_values`
**Args:**
```json
{
  "where": "(lc.ligand_id IN (ligand_5802, ligand_5804, ligand_5777, ligand_5761, ligand_5976, ligand_5977, ligand_6084, ligand_6102, ligand_6104, ligand_6109))",
  "order_by": "lc.ligand_id ASC, p.pKa ASC",
  "limit": 200
}
```

[TOOL ERROR] search_pka_values: Error executing tool search_pka_values: SQL parse error: Invalid expression / Unexpected token. Line 1, Col: 42.
  SELECT 1 FROM _stub WHERE lc.ligand_id [4mASC[0m, p.pKa ASC

---

### Step 17: `search_pka_ligands`
**Args:**
```json
{
  "where": "(lc.ligand_name_SRD LIKE '%nitrilotriacetic%' OR lc.ligand_name_SRD LIKE '%iminodiacetic%' OR lc.ligand_name_SRD LIKE '%glycine%' OR lc.ligand_name_SRD LIKE '%serine%' OR lc.ligand_name_SRD LIKE '%threonine%' OR lc.ligand_name_SRD LIKE '%glyphosate%' OR lc.ligand_name_SRD LIKE '%hydroxyethyl%iminodiacetic%')",
  "limit": 50
}
```

[summary]
## search_pka_ligands — 50 row(s)

| ligand_id | ligand_name | HxL_def | formula | smiles | pH_ladder | T°C_range | I(M)_range | similarity_score |
|-----------|-------------|---------|---------|--------|-----------|-----------|------------|------------------|
| ligand_5760 | Aminoacetic acid (Glycine) | HL | C2H5N1O2 | NCC(=O)O | −∞; H2L (M_tot_1); (2.33, vlm_93627); HL (M_tot_20); (9.57, vlm_93606); L (M_tot_43); +∞ | 25 | 0.1 | *** |
| ligand_5776 | DL-Aminophenylacetic acid (Phenylglycine) | HL | C8H9N1O2 | NC(C(=O)O)c1ccccc1 | −∞; H2L (M_tot_1); (-1.9, vlm_94963); HL (M_tot_1); (8.92, vlm_94962); L (M_tot_6); +∞ | 25 | 0.1 | *** |
| ligand_5786 | DL-Amino-4-sulfophenylacetic acid (4-Sulfophenylglycine) | H2L | C8H9N1O5S1 | NC(C(=O)O)c1ccc(S(=O)(=O)O)cc1 | −∞; H2L (M_tot_1); (-1.8, vlm_95189); HL (M_tot_1); (8.66, vlm_95188); L (M_tot_6); +∞ | 25 | 0.1 | *** |
| ligand_5809 | L-2-Amino-3-phosphopropanoic acid (Phosphoserine) | H3L | C3H8N1O6P1 | N[C@@H](COP(=O)(O)O)C(=O)O | −∞; H4L (M_tot_1); (-0.7, vlm_95914); H3L (M_tot_1); (2.14, vlm_95911); H2L (M_tot_1); (5.7, vlm_95904); HL (M_tot_1); (9.8, vlm_95900); L (M_tot_11); +∞ | 25 | 0.1 | *** |
| ligand_5811 | L-2-Amino-3-phosphobutanoic acid (Phosphothreonine) | H4L | C4H10N1O6P1 | C[C@@H](OP(=O)(O)O)[C@H](N)C(=O)O | −∞; H3L (M_tot_1); (2.25, vlm_95964); H2L (M_tot_1); (5.83, vlm_95963); HL (M_tot_1); (9.67, vlm_95962); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5828 | L-2-Amino-3-hydroxypropanoic acid (Serine) | HL | C3H7N1O3 | N[C@@H](CO)C(=O)O | −∞; H2L (M_tot_1); (2.16, vlm_96511); HL (M_tot_3); (9.05, vlm_96498); L (M_tot_16); +∞ | 25 | 0.1 | *** |
| ligand_5829 | L-2-Amino-3-hydroxybutanoic acid (Threonine) | HL | C4H9N1O3 | C[C@@H](O)[C@H](N)C(=O)O | −∞; H2L (M_tot_1); (2.2, vlm_96687); HL (M_tot_2); (8.94, vlm_96674); L (M_tot_11); +∞ | 25 | 0.1 | *** |
| ligand_5830 | allo-L-2-Amino-3-hydroxybutanoic acid (L-allo-Threonine) | HL | C4H9N1O3 | C[C@H](O)[C@H](N)C(=O)O | −∞; H2L (M_tot_1); (2.11, vlm_96824); HL (M_tot_1); (8.92, vlm_96819); L (M_tot_4); +∞ | 25 | 0.1 | *** |
| ligand_5831 | erythro-2-Amino-3-hydroxy-3-phenylpropanoic acid (erythro-P… | HL | C9H11N1O3 | NC(C(=O)O)C(O)c1ccccc1 | −∞; H2L (M_tot_1); (-1.9, vlm_96854); HL (M_tot_1); (8.7, vlm_96851); L (M_tot_7); +∞ | 25 | 0.1 | *** |
| ligand_5832 | threo-2-Amino-3-hydroxy-3-phenylpropanoic acid (threo-Pheny… | HL | C9H11N1O3 | NC(C(=O)O)C(O)c1ccccc1 | −∞; H2L (M_tot_1); (-1.9, vlm_96877); HL (M_tot_1); (8.87, vlm_96876); L (M_tot_4); +∞ | 25 | 0.1 | *** |
| ligand_5833 | L-2-Amino-4-hydroxybutanoic acid (Homoserine) | HL | C4H9N1O3 | N[C@@H](CCO)C(=O)O | −∞; H2L (M_tot_1); (2.24, vlm_96895); HL (M_tot_1); (9.28, vlm_96890); L (M_tot_7); +∞ | 25 | 0.1 | *** |
| ligand_5834 | DL-3-Amino-2-hydroxypropanoic acid (Isoserine) | HL | C3H7N1O3 | NCC(O)C(=O)O | −∞; H2L (M_tot_1); (2.66, vlm_96924); HL (M_tot_5); (9.13, vlm_96921); L (M_tot_6); +∞ | 25 | 0.1 | *** |
| ligand_5838 | DL-Amino-4-Methoxyphenylacetic acid (4-Methoxyphenylglycine) | HL | C9H11N1O3 | COc1ccc(C(N)C(=O)O)cc1 | −∞; H2L (M_tot_1); (2, vlm_97021); HL (M_tot_1); (9.07, vlm_97020); L (M_tot_6); +∞ | 25 | 0.1 | *** |
| ligand_5853 | L-2-Amino-3-(phenylmethoxy)propanoic acid (O-Benzylserine) | HL | C10H13N1O3 | N[C@@H](COCc1ccccc1)C(=O)O | −∞; H2L (M_tot_1); (-1.9, vlm_97361); HL (M_tot_1); (9.03, vlm_97360); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_5925 | N-Methylglycine (Sarcosine) | HL | C3H7N1O2 | CNCC(=O)O | −∞; H2L (M_tot_1); (2.18, vlm_99459); HL (M_tot_1); (9.98, vlm_99451); L (M_tot_7); +∞ | 25 | 0.1 | *** |
| ligand_5926 | N-Ethylglycine | HL | C4H9N1O2 | CCNCC(=O)O | −∞; H2L (M_tot_1); (2.3, vlm_99498); HL (M_tot_1); (10.1, vlm_99497); L (M_tot_3); +∞ | 25 | 0.1 | *** |
| ligand_5927 | N-Propylglycine | HL | C5H11N1O2 | CCCNCC(=O)O | −∞; H2L (M_tot_1); (2.28, vlm_99506); HL (M_tot_1); (10.03, vlm_99505); L (M_tot_3); +∞ | 25 | 0.1 | *** |
| ligand_5928 | N-Butylglycine | HL | C6H13N1O2 | CCCCNCC(=O)O | −∞; H2L (M_tot_1); (2.29, vlm_99512); HL (M_tot_1); (10.07, vlm_99511); L (M_tot_3); +∞ | 25 | 0.1 | *** |
| ligand_5929 | N-(2-Propyl)glycine | HL | C5H11N1O2 | CC(C)NCC(=O)O | −∞; H2L (M_tot_1); (2.36, vlm_99518); HL (M_tot_1); (10.06, vlm_99517); L (M_tot_3); +∞ | 25 | 0.1 | *** |
| ligand_5937 | N-(Phosphonomethyl)glycine (Glyphosate) | H3L | C3H8N1O5P1 | O=C(O)CNCP(=O)(O)O | −∞; H4L (M_tot_1); (-0.5, vlm_99756); H3L (M_tot_1); (2.2, vlm_99734); H2L (M_tot_1); (5.45, vlm_99712); HL (M_tot_2); (10.1, vlm_99687); L (M_tot_14); +∞ | 20~25 | 0.1 | *** |
| ligand_5948 | N-(2-Aminoethyl)glycine (Ethylenediamine monoacetic acid) (… | HL | C4H10N2O2 | NCCNCC(=O)O | −∞; H3L (M_tot_1); (-1.9, vlm_99990); H2L (M_tot_1); (6.67, vlm_99987); HL (M_tot_1); (9.84, vlm_99984); L (M_tot_8); +∞ | 25 | 0.1 | *** |
| ligand_5949 | N-[Tris(hydroxymethyl)methyl]glycine (Tricine) | HL | C6H15N1O5 | O=C(O)CNC(CO)(CO)CO | −∞; H2L (M_tot_1); (2.023, vlm_100021); HL (M_tot_1); (8.135, vlm_100016); L (M_tot_1); +∞ | 25 | 0 | *** |

---

### Step 18: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_name_SRD IN ('Fe(III)', 'Fe(II)') AND (c.ligand_name_SRD LIKE '%nitrilotriacetic%' OR c.ligand_name_SRD LIKE '%iminodiacetic%' OR c.ligand_name_SRD LIKE '%glycine%' OR c.ligand_name_SRD LIKE '%serine%' OR c.ligand_name_SRD LIKE '%threonine%' OR c.ligand_name_SRD LIKE '%glyphosate%' OR c.ligand_name_SRD LIKE '%hydroxyethyl%iminodiacetic%'))",
  "limit": 300
}
```

[summary]
## search_stability — 200 row(s)

### logK — 54 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 14 | 8 | 20~25 | 0.1~1 | *** | 4 |
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 10 | 3 | 10~40 | 0~3 | *** | 7 |
| metal_62 | Fe^[2+] | ligand_5828 | L-2-Amino-3-hydroxypropanoi… | HL | N[C@@H](CO)C(=O)O | 8 | 3 | 20~37 | 0.1~3 | *** | 4 |
| metal_62 | Fe^[2+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 7 | 3 | 20~25 | 0.1~1 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 7 | 5 | 25 | 0.1~1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 6 | 3 | 25 | 0.5~3 | *** | 3 |
| metal_62 | Fe^[2+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 6 | 2 | 20~25 | 0.1~1 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_6204 | N-(2-Hydroxyethyl)iminodiac… | H2L | O=C(O)CN(CCO)CC(=O)O | 6 | 5 | 20~25 | 0.1~1 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_5829 | L-2-Amino-3-hydroxybutanoic… | HL | C[C@@H](O)[C@H](N)C(=O)O | 5 | 2 | 20~37 | 0.1~1 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_5937 | N-(Phosphonomethyl)glycine … | H3L | O=C(O)CNCP(=O)(O)O | 5 | 5 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6047 | N,N''-Bis(3-hydroxy-6-methy… | H5L | Cc1ccc(O)c(CN(CCN(CCN(CC(=O)O)Cc2nc(C)ccc2O)CC(=O)O)CC(=O)O)n1 | 5 | 5 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 5 | 4 | 25 | 0.1~1 | *** | 3 |
| metal_62 | Fe^[2+] | ligand_6140 | N-Methyliminodiacetic acid … | H2L | CN(CC(=O)O)CC(=O)O | 5 | 3 | 20~25 | 0.1 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_6193 | N-(Phosphonomethyl)iminodia… | H4L | O=C(O)CN(CC(=O)O)CP(=O)(O)O | 5 | 5 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6135 | L-2-(Carboxymethyl)iminodia… | H3L | O=C(O)CNC(CC(=O)O)C(=O)O | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6188 | DL-2-(2-Methylthioethyl)nit… | H3L | CSCCC(C(=O)O)N(CC(=O)O)CC(=O)O | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6253 | N-(2-Aminoethyl)iminodiacet… | H2L | NCCN(CC(=O)O)CC(=O)O | 4 | 4 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5809 | L-2-Amino-3-phosphopropanoi… | H3L | N[C@@H](COP(=O)(O)O)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5937 | N-(Phosphonomethyl)glycine … | H3L | O=C(O)CNCP(=O)(O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5997 | rac-Trimethylenebis[2-(2-hy… | *** | *** | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5998 | meso-Trimethylenebis[2-(2-h… | H4L | Cc1cc(C)c(O)c([C@H](NCCCN[C@@H](C(=O)O)c2cc(C)cc(C)c2O)C(=O)O)c1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6019 | N,N-Bis(phosphonomethyl)gly… | H5L | O=C(O)CN(CP(=O)(O)O)CP(=O)(O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6135 | L-2-(Carboxymethyl)iminodia… | H3L | O=C(O)CNC(CC(=O)O)C(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6142 | N-Propyliminodiacetic acid | H2L | CCCN(CC(=O)O)CC(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6188 | DL-2-(2-Methylthioethyl)nit… | H3L | CSCCC(C(=O)O)N(CC(=O)O)CC(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6197 | N-(2-Hydroxybenzyl)iminodia… | H3L | O=C(O)CN(CC(=O)O)Cc1ccccc1O | 3 | 3 | 25 | 0.1~1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_6239 | N,N-Bis(carboxymethyl)glycy… | H3L | O=C(O)CNC(=O)CN(CC(=O)O)CC(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6253 | N-(2-Aminoethyl)iminodiacet… | H2L | NCCN(CC(=O)O)CC(=O)O | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5975 | Ethylenediiminodiacetic aci… | H2L | O=C(O)CNCCNCC(=O)O | 2 | 2 | 25 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5994 | N,N'-Bis(2-hydroxyphenyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)c1ccccc1O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6021 | N,N-Bis(2-hydroxyethyl)glyc… | HL | O=C(O)CN(CCO)CCO | 2 | 2 | 30 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6021 | N,N-Bis(2-hydroxyethyl)glyc… | HL | O=C(O)CN(CCO)CCO | 2 | 2 | 20~25 | 0.1~0.5 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_6141 | N-Ethyliminodiacetic acid | H2L | CCN(CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6204 | N-(2-Hydroxyethyl)iminodiac… | H2L | O=C(O)CN(CCO)CC(=O)O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6222 | N-(2-Methoxyethyl)iminodiac… | H2L | COCCN(CC(=O)O)CC(=O)O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6240 | N,N-Bis(carboxymethyl)glycy… | H3L | O=C(O)CNC(=O)CNC(=O)CN(CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6241 | N,N-Bis(carboxymethyl)glycy… | H3L | O=C(O)CNC(=O)CNC(=O)CNC(=O)CN(CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6248 | N-(2-Mercaptoethyl)iminodia… | H3L | O=C(O)CN(CCS)CC(=O)O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6249 | N-[2-(Methylthio)ethyl]imin… | H2L | CSCCN(CC(=O)O)CC(=O)O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6276 | N-(2-Hydroxybenzyl)ethylene… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6793 | N-(2-Pyridylmethyl)iminodia… | H2L | O=C(O)CN(CC(=O)O)Cc1ccccn1 | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6982 | Aminoacetohydroxamic acid (… | HL | NCC(=O)NO | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5828 | L-2-Amino-3-hydroxypropanoi… | HL | N[C@@H](CO)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5829 | L-2-Amino-3-hydroxybutanoic… | HL | C[C@@H](O)[C@H](N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5925 | N-Methylglycine (Sarcosine) | HL | CNCC(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5925 | N-Methylglycine (Sarcosine) | HL | CNCC(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6195 | N-(2-Carboxyethyl)-N-(phosp… | H4L | O=C(O)CCN(CC(=O)O)CP(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6200 | N-(3-Carboxy-2-hydroxy-5-su… | H4L | O=C(O)CN(CC(=O)O)Cc1cc(S(=O)(=O)O)cc(C(=O)O)c1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6224 | N-(2-Tetrahydropyranylmethy… | H2L | O=C(O)CN(CC(=O)O)CC1CCCCO1 | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6372 | Glycylglycine (Diglycine) | HL | NCC(=O)NCC(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6372 | Glycylglycine (Diglycine) | HL | NCC(=O)NCC(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6731 | N-Phenyliminodiacetic acid | H2L | O=C(O)CN(CC(=O)O)c1ccccc1 | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6794 | N-(6-Methyl-2-pyridylmethyl… | H2L | Cc1cccc(CN(CC(=O)O)CC(=O)O)n1 | 1 | 1 | 20 | 0.1 | *** | 1 |

### ΔH — 6 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 3 | 1 | 10~40 | 0 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_5828 | L-2-Amino-3-hydroxypropanoi… | HL | N[C@@H](CO)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_5829 | L-2-Amino-3-hydroxybutanoic… | HL | C[C@@H](O)[C@H](N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |

### ΔS — 6 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_62 | Fe^[2+] | ligand_5828 | L-2-Amino-3-hydroxypropanoi… | HL | N[C@@H](CO)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_5829 | L-2-Amino-3-hydroxybutanoic… | HL | C[C@@H](O)[C@H](N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |

---
