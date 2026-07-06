# Q3.1.2 — Tool Results (batch 5)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Cu(II), Ni(II)",
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
  "name": "histidine, glycine, cysteine, aspartic acid, glutamic acid, lysine, proline, serine, alanine, methionine",
  "limit": 20
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 4: `search_metals`
**Args:**
```json
{
  "name": "copper, nickel",
  "symbol": "Cu, Ni",
  "limit": 10
}
```

[summary]
## search_metals

*(no results)*

---

### Step 5: `search_ligands`
**Args:**
```json
{
  "name": "L-histidine, histidine, glycine, glycinate, cysteine, L-cysteine, aspartic acid, L-aspartic acid, glutamic acid, L-glutamic acid, lysine, L-lysine, proline, L-proline, serine, L-serine, alanine, L-alanine, methionine, L-methionine",
  "ligand_class": "amino acid",
  "limit": 50
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 7: `build_system_catalog`
**Args:**
```json
{}
```

[summary]
[CATALOG]
## build_system_catalog

**Error:** Provide at least one of metal_id, ligand_id, or beta_definition_id.

---

### Step 9: `get_table_schema`
**Args:**
```json
{
  "table_name": "metals"
}
```

[summary]
**get_table_schema:** Error - Table 'metals' not found.
Available tables: ligand_card, ligand_pka_bracket, ligand_pka_measured, ligandmetal_card, ligandmetal_stability_estimated, ligandmetal_stability_measured, metal_card, ref_author, ref_footnote, ref_literature, ref_literature_alt, ref_vlm_author, ref_vlm_footnote, ref_vlm_literature, ref_vlm_literature_alt, sqlite_sequence

---

### Step 10: `get_table_schema`
**Args:**
```json
{
  "table_name": "ligand_card"
}
```

[summary]
## get_table_schema - 13 column(s)

| cid | name | type | notnull | pk |
|-----|------|------|---------|----|
| 0 | ligand_id | INTEGER | False | True |
| 1 | ligand_name_SRD | TEXT | True | False |
| 2 | ligand_class_id | INTEGER | False | False |
| 3 | ligand_class_name | TEXT | False | False |
| 4 | ligand_SMILES | TEXT | False | False |
| 5 | ligand_InChi | TEXT | False | False |
| 6 | formula | TEXT | False | False |
| 7 | composition | TEXT | False | False |
| 8 | figure_definition | TEXT | False | False |
| 9 | definition_HxL | TEXT | False | False |
| 10 | synonym_iupac_name | TEXT | False | False |
| 11 | synonym_common_name | TEXT | False | False |
| 12 | created_at | TIMESTAMP | False | False |

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

### Step 12: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT DISTINCT metal_id, metal_name_SRD FROM ligandmetal_card WHERE LOWER(metal_name_SRD) LIKE '%copper%' OR metal_name_SRD LIKE '%Cu%';"
}
```

[summary]
## execute_srd46_sql - 3 row(s)

| metal_id | metal_name_SRD |
|----------|----------------|
| metal_41 | Cu^[2+] |
| metal_42 | Cu^[+] |
| metal_43 | Cu^[3+] |

---

### Step 13: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT DISTINCT metal_id, metal_name_SRD FROM ligandmetal_card WHERE LOWER(metal_name_SRD) LIKE '%nickel%' OR metal_name_SRD LIKE '%Ni%';"
}
```

[summary]
## execute_srd46_sql - 2 row(s)

| metal_id | metal_name_SRD |
|----------|----------------|
| metal_112 | Ni^[2+] |
| metal_113 | Ni^[3+] |

---

### Step 14: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT DISTINCT ligand_id, ligand_name_SRD, ligand_class_name FROM ligand_card WHERE LOWER(ligand_class_name) LIKE '%amino%' OR LOWER(ligand_name_SRD) IN ('glycine','histidine','cysteine','aspartic acid','glutamic acid','lysine','proline','serine','alanine','methionine') OR LOWER(COALESCE(synonym_common_name,'')) LIKE '%glycine%' OR LOWER(COALESCE(synonym_common_name,'')) LIKE '%histidine%' OR LOWER(COALESCE(synonym_common_name,'')) LIKE '%cysteine%' OR LOWER(COALESCE(synonym_common_name,'')) LIKE '%aspartic%' OR LOWER(COALESCE(synonym_common_name,'')) LIKE '%glutamic%' OR LOWER(COALESCE(synonym_common_name,'')) LIKE '%lysine%' OR LOWER(COALESCE(synonym_common_name,'')) LIKE '%proline%' OR LOWER(COALESCE(synonym_common_name,'')) LIKE '%serine%' OR LOWER(COALESCE(synonym_common_name,'')) LIKE '%alanine%' OR LOWER(COALESCE(synonym_common_name,'')) LIKE '%methionine%';"
}
```

[summary]
## execute_srd46_sql - 50 row(s)

| ligand_id | ligand_name_SRD | ligand_class_name |
|-----------|-----------------|-------------------|
| ligand_5760 | Aminoacetic acid (Glycine) | Amino Acids |
| ligand_5761 | L-2-Aminopropanoic acid (Alanine) | Amino Acids |
| ligand_5762 | DL-2-Aminobutanoic acid | Amino Acids |
| ligand_5763 | DL-2-Aminopentanoic acid (Norvaline) | Amino Acids |
| ligand_5764 | DL-2-Aminohexanoic acid (Norleucine) | Amino Acids |
| ligand_5765 | L-2-Amino-3-methylbutanoic acid (Valine) | Amino Acids |
| ligand_5766 | L-2-Amino-4-methylpentanoic acid (Leucine) | Amino Acids |
| ligand_5767 | L-2-Amino-3-methylpentanoic acid (Isoleucine) | Amino Acids |
| ligand_5768 | D-allo-2-Amino-3-methylpentanoic acid (D-allo-Isoleucine) | Amino Acids |
| ligand_5769 | 2-Amino-2-methylpropanoic acid (2-Aminoisobutyric acid) | Amino Acids |
| ligand_5770 | DL-2-Amino-4-pentenoic acid | Amino Acids |
| ligand_5771 | DL-2-Amino-5-hexenoic acid | Amino Acids |
| ligand_5772 | DL-2-Amino-6-heptenoic acid | Amino Acids |
| ligand_5773 | 1-Aminocyclopentanecarboxylic acid (Cycloleucine) | Amino Acids |
| ligand_5774 | 1-Aminocyclohexanecarboxylic acid | Amino Acids |
| ligand_5775 | 1-Aminocycloheptanecarboxylic acid | Amino Acids |
| ligand_5776 | DL-Aminophenylacetic acid (Phenylglycine) | Amino Acids |
| ligand_5777 | L-2-Amino-3-phenylpropanoic acid (Phenylalanine) | Amino Acids |
| ligand_5778 | DL-2-Amino-3-chloropropanoic acid (3-Chloroalanine) | Amino Acids |
| ligand_5779 | DL-2-Amino-3-chlorobutanoic acid | Amino Acids |
| ligand_5780 | DL-2-Amino-3-(2-fluorophenyl)propanoic acid (DL-3-(2-Fluorophenyl)alanine) | Amino Acids |
| ligand_5781 | DL-2-Amino-3-(3-fluorophenyl)propanoic acid (DL-3-(3-Fluorophenyl)alanine) | Amino Acids |
| ligand_5782 | DL-2-Amino-3-(4-fluorophenyl)propanoic acid (DL-3-(4-Fluorophenyl)alanine) | Amino Acids |
| ligand_5783 | DL-2-Amino-3-(2-chlorophenyl)propanoic acid (DL-3-(2-Chlorophenyl)alanine) | Amino Acids |
| ligand_5784 | DL-2-Amino-3-(3-chlorophenyl)propanoic acid (DL-3-(3-Chlorophenyl)alanine) | Amino Acids |

... 25 more row(s) omitted

---

### Step 15: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT ligand_id, ligand_name_SRD, ligand_class_name FROM ligand_card WHERE ligand_id IN (5760,5761,5785,5791,5792,5793,5796,5797,5800,5802) ORDER BY ligand_id;"
}
```

[summary]
## execute_srd46_sql - 10 row(s)

| ligand_id | ligand_name_SRD | ligand_class_name |
|-----------|-----------------|-------------------|
| ligand_5760 | Aminoacetic acid (Glycine) | Amino Acids |
| ligand_5761 | L-2-Aminopropanoic acid (Alanine) | Amino Acids |
| ligand_5785 | DL-2-Amino-3-(4-chlorophenyl)propanoic acid (DL-3-(4-Chlorophenyl)alanine) | Amino Acids |
| ligand_5791 | trans-2-Aminocyclopentane-1-carboxylic acid | Amino Acids |
| ligand_5792 | cis-2-Aminocyclohexane-1-carboxylic acid | Amino Acids |
| ligand_5793 | trans-2-Aminocyclohexane-1-carboxylic acid | Amino Acids |
| ligand_5796 | DL-3-Amino-3-phenylpropanoic acid (Phenyl-beta-Alanine) | Amino Acids |
| ligand_5797 | 4-Aminobutanoic acid | Amino Acids |
| ligand_5800 | 7-Aminoheptanoic acid | Amino Acids |
| ligand_5802 | L-Aminobutanedioic acid (Aspartic acid) | Amino Acids |

---

### Step 16: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT ligand_id, ligand_name_SRD FROM ligand_card WHERE ligand_class_name = 'Amino Acids' AND (LOWER(ligand_name_SRD) LIKE '%histid%' OR LOWER(ligand_name_SRD) LIKE '%cystein%' OR LOWER(ligand_name_SRD) LIKE '%glutam%' OR LOWER(ligand_name_SRD) LIKE '%lys%' OR LOWER(ligand_name_SRD) LIKE '%prolin%' OR LOWER(ligand_name_SRD) LIKE '%serin%' OR LOWER(ligand_name_SRD) LIKE '%methion%' OR LOWER(ligand_name_SRD) LIKE '%alanine%' OR LOWER(ligand_name_SRD) LIKE '%glycine%' OR LOWER(ligand_name_SRD) LIKE '%aspartic%') ORDER BY ligand_id;"
}
```

[summary]
## execute_srd46_sql - 50 row(s)

| ligand_id | ligand_name_SRD |
|-----------|-----------------|
| ligand_5760 | Aminoacetic acid (Glycine) |
| ligand_5761 | L-2-Aminopropanoic acid (Alanine) |
| ligand_5776 | DL-Aminophenylacetic acid (Phenylglycine) |
| ligand_5777 | L-2-Amino-3-phenylpropanoic acid (Phenylalanine) |
| ligand_5778 | DL-2-Amino-3-chloropropanoic acid (3-Chloroalanine) |
| ligand_5780 | DL-2-Amino-3-(2-fluorophenyl)propanoic acid (DL-3-(2-Fluorophenyl)alanine) |
| ligand_5781 | DL-2-Amino-3-(3-fluorophenyl)propanoic acid (DL-3-(3-Fluorophenyl)alanine) |
| ligand_5782 | DL-2-Amino-3-(4-fluorophenyl)propanoic acid (DL-3-(4-Fluorophenyl)alanine) |
| ligand_5783 | DL-2-Amino-3-(2-chlorophenyl)propanoic acid (DL-3-(2-Chlorophenyl)alanine) |
| ligand_5784 | DL-2-Amino-3-(3-chlorophenyl)propanoic acid (DL-3-(3-Chlorophenyl)alanine) |
| ligand_5785 | DL-2-Amino-3-(4-chlorophenyl)propanoic acid (DL-3-(4-Chlorophenyl)alanine) |
| ligand_5786 | DL-Amino-4-sulfophenylacetic acid (4-Sulfophenylglycine) |
| ligand_5788 | 3-Aminopropanoic acid (beta-Alanine) |
| ligand_5796 | DL-3-Amino-3-phenylpropanoic acid (Phenyl-beta-Alanine) |
| ligand_5802 | L-Aminobutanedioic acid (Aspartic acid) |
| ligand_5803 | DL-2-Amino-3-methylbutanedioic acid (3-Methylaspartic acid) |
| ligand_5804 | L-2-Aminopentanedioic acid (Glutamic acid) |
| ligand_5805 | DL-2-Amino-2-methylpentanedioic acid (2-Methylglutamic acid) |
| ligand_5807 | DL-2-Amino-3-hydroxypentanedioic acid (3-Hydroxyglutamic acid) |
| ligand_5809 | L-2-Amino-3-phosphopropanoic acid (Phosphoserine) |
| ligand_5828 | L-2-Amino-3-hydroxypropanoic acid (Serine) |
| ligand_5831 | erythro-2-Amino-3-hydroxy-3-phenylpropanoic acid (erythro-Phenylserine) |
| ligand_5832 | threo-2-Amino-3-hydroxy-3-phenylpropanoic acid (threo-Phenylserine) |
| ligand_5833 | L-2-Amino-4-hydroxybutanoic acid (Homoserine) |
| ligand_5834 | DL-3-Amino-2-hydroxypropanoic acid (Isoserine) |

... 25 more row(s) omitted

---

### Step 17: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT lc.ligand_id, lc.ligand_name_SRD, SUM(CASE WHEN c.metal_id = 41 THEN 1 ELSE 0 END) AS cu_cards, SUM(CASE WHEN c.metal_id = 112 THEN 1 ELSE 0 END) AS ni_cards FROM ligand_card lc JOIN ligandmetal_card c ON lc.ligand_id = c.ligand_id WHERE lc.ligand_class_name = 'Amino Acids' AND c.metal_id IN (41,112) GROUP BY lc.ligand_id, lc.ligand_name_SRD HAVING cu_cards > 0 AND ni_cards > 0 ORDER BY (cu_cards + ni_cards) DESC, lc.ligand_id LIMIT 30;"
}
```

[summary]
## execute_srd46_sql - 30 row(s)

| ligand_id | ligand_name_SRD | cu_cards | ni_cards |
|-----------|-----------------|----------|----------|
| ligand_5760 | Aminoacetic acid (Glycine) | 30 | 49 |
| ligand_5898 | L-2-Amino-3-(4-imidazolyl)propanoic acid (Histidine) | 50 | 25 |
| ligand_5889 | DL-2,6-Diamino-5-hydroxyhexanoic acid | 28 | 32 |
| ligand_5777 | L-2-Amino-3-phenylpropanoic acid (Phenylalanine) | 33 | 26 |
| ligand_5761 | L-2-Aminopropanoic acid (Alanine) | 21 | 24 |
| ligand_5829 | L-2-Amino-3-hydroxybutanoic acid (Threonine) | 32 | 12 |
| ligand_5887 | L-2,6-Diaminohexanoic acid (Lysine) | 20 | 22 |
| ligand_5828 | L-2-Amino-3-hydroxypropanoic acid (Serine) | 26 | 15 |
| ligand_5819 | L-2-Amino-3-(4-hydroxyphenyl)propanoic acid (Tyrosine) | 15 | 25 |
| ligand_5886 | L-2,5-Diaminopentanoic acid (Ornithine) | 24 | 16 |
| ligand_5818 | DL-2-Amino-3-(3-hydroxyphenyl)propanoic acid (m-Tyrosine) | 12 | 24 |
| ligand_5883 | L-2,3-Diaminopropanoic acid | 19 | 16 |
| ligand_5885 | L-2,4-Diaminobutanoic acid | 22 | 12 |
| ligand_5802 | L-Aminobutanedioic acid (Aspartic acid) | 20 | 11 |
| ligand_5826 | L-2-Amino-3-(3,4-dihydroxyphenyl)propanoic acid (DOPA) | 18 | 13 |
| ligand_5907 | L-2-Amino-3-(3-indolyl)propanoic acid (Tryptophan) | 17 | 13 |
| ligand_5765 | L-2-Amino-3-methylbutanoic acid (Valine) | 12 | 17 |
| ligand_5788 | 3-Aminopropanoic acid (beta-Alanine) | 13 | 16 |
| ligand_5844 | L-2-Aminopentanedioic acid 5-amide (Glutamine) | 14 | 14 |
| ligand_5843 | L-2-Aminobutanedioic acid 4-amide (Asparagine) | 15 | 11 |
| ligand_5817 | DL-2-Amino-3-(2-hydroxyphenyl)propanoic acid (o-Tyrosine) | 12 | 12 |
| ligand_5930 | L-Pyrrolidine-2-carboxylic acid (L-Proline) | 12 | 10 |
| ligand_5804 | L-2-Aminopentanedioic acid (Glutamic acid) | 12 | 9 |
| ligand_5834 | DL-3-Amino-2-hydroxypropanoic acid (Isoserine) | 12 | 9 |
| ligand_5937 | N-(Phosphonomethyl)glycine (Glyphosate) | 13 | 8 |

... 5 more row(s) omitted

---

### Step 18: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_41, metal_112) AND c.ligand_id IN (ligand_5760, ligand_5898, ligand_5887, ligand_5802, ligand_5804, ligand_5930, ligand_5828, ligand_5761) AND s.solvent_name LIKE '%water%' AND s.temperature_c BETWEEN 20 AND 30 AND s.constant_type LIKE 'log%')",
  "order_by": "c.ligand_id ASC, c.metal_id ASC, ABS(COALESCE(s.temperature_c,25)-25) ASC, s.constant_value DESC",
  "limit": 200
}
```

[summary]
## search_stability

*(no results)*

---

### Step 19: `search_pka_values`
**Args:**
```json
{
  "where": "(lc.ligand_id IN (ligand_5760, ligand_5898, ligand_5887, ligand_5802, ligand_5804, ligand_5930, ligand_5828, ligand_5761) AND p.solvent_name LIKE '%water%')",
  "order_by": "lc.ligand_id ASC, p.pKa ASC",
  "limit": 200
}
```

[summary]
## search_pka_values

*(no results)*

---

### Step 20: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_41, metal_112) AND c.ligand_id IN (ligand_5760, ligand_5898, ligand_5887, ligand_5802, ligand_5804, ligand_5930, ligand_5828, ligand_5761))",
  "order_by": "c.ligand_id ASC, c.metal_id ASC",
  "limit": 100
}
```

[summary]
## search_networks — 212 row(s)

> **Reference equilibrium networks (compact)** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### Beta-definition legend
| beta_def | equation |
|----------|----------|
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_872 | ``[M] + [L]^3 <=> [ML3]`` |
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` |
| beta_def_779 | ``[M] + [HL] <=> [MHL]`` |
| beta_def_984 | ``[M(OH)L2] + [H] <=> [ML2] + [H2O]`` |
| beta_def_249 | ``[M(OH)2L2] + [H] <=> [M(OH)L2] + [H2O]`` |
| beta_def_194 | ``[M] + [HL]^2 <=> [M(HL)2]`` |
| beta_def_792 | ``[ML2] + [H] <=> [MHL2]`` |
| beta_def_204 | ``[MHL2] + [H] <=> [M(HL)2]`` |
| beta_def_208 | ``[M] + [HL]^3 <=> [M(HL)3]`` |
| beta_def_214 | ``[MH2L3] + [H] <=> [M(HL)3]`` |
| beta_def_744 | ``[MHL3] + [H] <=> [MH2L3]`` |
| beta_def_803 | ``[ML3] + [H] <=> [MHL3]`` |
| beta_def_424 | ``[M]^2 + [L]^2 + [H2O]^2 <=> [M2(OH)2L2] + [H]^2`` |
| beta_def_966 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` |

### Metal-ligand pair summary
| metal | metal_id | ligand | ligand_id | HxL | T_range | I_range | net_count | max_nodes | max_net_id | ligand_SMILES |
|-------|----------|--------|-----------|-----|---------|---------|-----------|----------|------------|---------------|
| `Cu^[2+]` | metal_41 | Aminoacetic acid (Glycine) | ligand_5760 | HL | 5~45 | -0.15~2.65 | 9 | 2 | ref_eq_net_86 | NCC(=O)O |
| `Ni^[2+]` | metal_112 | Aminoacetic acid (Glycine) | ligand_5760 | HL | 5~45 | -0.15~3.15 | 9 | 3 | ref_eq_net_77 | NCC(=O)O |
| `Cu^[2+]` | metal_41 | L-2-Aminopropanoic acid (Alanine) | ligand_5761 | HL | 19~41 | -0.15~5.15 | 7 | 3 | ref_eq_net_201 | C[C@H](N)C(=O)O |
| `Ni^[2+]` | metal_112 | L-2-Aminopropanoic acid (Alanine) | ligand_5761 | HL | 19~41 | -0.15~1.15 | 5 | 3 | ref_eq_net_159 | C[C@H](N)C(=O)O |
| `Cu^[2+]` | metal_41 | L-Aminobutanedioic acid (Aspartic acid) | ligand_5802 | H2L | 19~41 | -0.05~2.15 | 5 | 3 | ref_eq_net_595 | N[C@@H](CC(=O)O)C(=O)O |
| `Ni^[2+]` | metal_112 | L-Aminobutanedioic acid (Aspartic acid) | ligand_5802 | H2L | 19~30 | -0.05~0.65 | 2 | 3 | ref_eq_net_593 | N[C@@H](CC(=O)O)C(=O)O |
| `Cu^[2+]` | metal_41 | L-2-Aminopentanedioic acid (Glutamic ac… | ligand_5804 | H2L | 20~41 | -0.05~0.3 | 2 | 3 | ref_eq_net_638 | N[C@@H](CCC(=O)O)C(=O)O |
| `Ni^[2+]` | metal_112 | L-2-Aminopentanedioic acid (Glutamic ac… | ligand_5804 | H2L | 20~41 | -0.05~0.3 | 3 | 4 | ref_eq_net_636 | N[C@@H](CCC(=O)O)C(=O)O |
| `Cu^[2+]` | metal_41 | L-2-Amino-3-hydroxypropanoic acid (Seri… | ligand_5828 | HL | 19~41 | -0.05~3.15 | 5 | 4 | ref_eq_net_802 | N[C@@H](CO)C(=O)O |
| `Ni^[2+]` | metal_112 | L-2-Amino-3-hydroxypropanoic acid (Seri… | ligand_5828 | HL | 19~41 | -0.05~3.15 | 3 | 3 | ref_eq_net_799 | N[C@@H](CO)C(=O)O |
| `Cu^[2+]` | metal_41 | L-2,6-Diaminohexanoic acid (Lysine) | ligand_5887 | HL | 19~41 | -0.05~1.15 | 3 | 4 | ref_eq_net_1253 | NCCCC[C@H](N)C(=O)O |
| `Ni^[2+]` | metal_112 | L-2,6-Diaminohexanoic acid (Lysine) | ligand_5887 | HL | 20~41 | -0.05~0.3 | 2 | 9 | ref_eq_net_1251 | NCCCC[C@H](N)C(=O)O |
| `Cu^[2+]` | metal_41 | L-2-Amino-3-(4-imidazolyl)propanoic aci… | ligand_5898 | HL | 19~41 | -0.05~3.15 | 6 | 8 | ref_eq_net_1343 | N[C@@H](Cc1c[nH]cn1)C(=O)O |
| `Ni^[2+]` | metal_112 | L-2-Amino-3-(4-imidazolyl)propanoic aci… | ligand_5898 | HL | 19~41 | -0.05~3.15 | 6 | 4 | ref_eq_net_1337 | N[C@@H](Cc1c[nH]cn1)C(=O)O |
| `Cu^[2+]` | metal_41 | L-Pyrrolidine-2-carboxylic acid (L-Prol… | ligand_5930 | HL | 19~41 | -0.05~0.65 | 3 | 4 | ref_eq_net_1537 | O=C(O)C1CCCN1 |
| `Ni^[2+]` | metal_112 | L-Pyrrolidine-2-carboxylic acid (L-Prol… | ligand_5930 | HL | 19~30 | -0.05~1.15 | 2 | 3 | ref_eq_net_1534 | O=C(O)C1CCCN1 |

### Global max-node network: `Ni^[2+]` + L-2,6-Diaminohexanoic acid (Lysine)
network_id: ref_eq_net_1251 | metal_id: metal_112 | ligand_id: ligand_5887 | ligand_def_HxL: HL | nodes: 9

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_779 | ``[M] + [HL] <=> [MHL]`` | logK | 4.9 |
| beta_def_194 | ``[M] + [HL]^2 <=> [M(HL)2]`` | logK | 9.2 |
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` | logK | 9.85 |
| beta_def_204 | ``[MHL2] + [H] <=> [M(HL)2]`` | logK | 9.9 |
| beta_def_214 | ``[MH2L3] + [H] <=> [M(HL)3]`` | logK | 10 |
| beta_def_792 | ``[ML2] + [H] <=> [MHL2]`` | logK | 10.1 |
| beta_def_744 | ``[MHL3] + [H] <=> [MH2L3]`` | logK | 10.4 |
| beta_def_803 | ``[ML3] + [H] <=> [MHL3]`` | logK | 10.9 |
| beta_def_208 | ``[M] + [HL]^3 <=> [M(HL)3]`` | logK | 12 |

---
