# Q3.1.2 — Tool Results (batch 2)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "copper(II), nickel(II)",
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
  "name": "histidine, cysteine, glycine, aspartic acid, glutamic acid, proline, alanine, serine, lysine, arginine, methionine, tyrosine, threonine, valine, leucine, isoleucine, phenylalanine, tryptophan",
  "limit": 50
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
  "name": "glycine, glycinate, histidine, histidinate, cysteine, cysteinate, alanine, alaninate, aspartic acid, aspartate, glutamic acid, glutamate, proline, prolinate, serine, serinate, lysine, arginine, methionine, tyrosine, threonine, valine, leucine, isoleucine, phenylalanine, tryptophan",
  "limit": 100
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

### Step 9: `db_distribution`
**Args:**
```json
{
  "table": "ligand_card",
  "group_column": "ligand_class_name",
  "limit": 50
}
```

[summary]
## db_distribution - ligand_card by ligand_class_name

**total_rows:** 5750

| value | count | pct |
|-------|-------|-----|
| Ligands not selected | 1339 | 23.29% |
| Amino Acids | 297 | 5.17% |
| Aliphatic amines | 250 | 4.35% |
| Pyridines (azines) | 248 | 4.31% |
| Carboxylic acids | 182 | 3.17% |
| Aza-macrocycles | 165 | 2.87% |
| Peptides | 157 | 2.73% |
| Aliphatic amines secondary N | 139 | 2.42% |
| Pyrroles (azoles) | 134 | 2.33% |
| Aminophosphorus acids | 132 | 2.3% |
| EDTA and derivatives | 115 | 2.0% |
| Aza-oxa-macrocycles | 112 | 1.95% |
| Carboxylic acids diacids | 103 | 1.79% |
| Inorganic ligands | 101 | 1.76% |
| Naphtols | 100 | 1.74% |
| polypeptides | 98 | 1.7% |
| Organophosphorus and arsenic acids | 95 | 1.65% |
| Aliphatic amines tertiary N | 95 | 1.65% |
| Phenols | 92 | 1.6% |
| NTA and derivatives | 91 | 1.58% |
| miscellaneous hydrocarbons | 84 | 1.46% |
| miscellaneous hydroxamic acids | 74 | 1.29% |
| Aniline | 72 | 1.25% |
| Carboxylic acids thio | 71 | 1.23% |
| miscellaneous ureas, hadrazides, amidines | 70 | 1.22% |
| Aza macrocycles with carboxylic acids | 70 | 1.22% |
| miscellaneous alcohols and sugar | 68 | 1.18% |
| tripeptides | 66 | 1.15% |
| Catechols | 66 | 1.15% |
| Aniline carboxylic acids | 66 | 1.15% |
| Aza-oxo-macrocycles | 58 | 1.01% |
| cyclic ketones | 57 | 0.99% |
| miscellaneous amides | 54 | 0.94% |
| Carboxylic acids diacids S-Se-Te-P-As | 53 | 0.92% |
| Purines | 52 | 0.9% |
| Carboxylic acids hydroxy | 52 | 0.9% |
| Cyclic amines  | 51 | 0.89% |
| Phenols salicylic acids | 49 | 0.85% |
| Carboxylic acids polyacids | 49 | 0.85% |
| miscellaneous mercaptans | 46 | 0.8% |
| Carboxylic acids oxy | 45 | 0.78% |
| Ketones (oxo ligands) | 43 | 0.75% |
| Iminodiacetic acid and derivatives | 38 | 0.66% |
| Carboxylic acids keto | 36 | 0.63% |
| Pyrimidines | 35 | 0.61% |
| Pyridine carboxylic acids | 35 | 0.61% |
| Bipyridines | 35 | 0.61% |
| Quinolines | 32 | 0.56% |
| miscellaneous sulfides | 25 | 0.43% |
| miscellaneous crown ether | 24 | 0.42% |

---

### Step 10: `get_table_schema`
**Args:**
```json
{
  "table_name": "ligandmetal_card",
  "database": "cards"
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

### Step 11: `get_table_schema`
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

### Step 12: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT DISTINCT metal_id, metal_name_SRD FROM ligandmetal_card WHERE metal_name_SRD LIKE '%copper%' OR metal_name_SRD LIKE 'Cu%' OR metal_name_SRD LIKE '%nickel%' OR metal_name_SRD LIKE 'Ni%' ORDER BY metal_name_SRD",
  "attach_equilibrium": false,
  "attach_literature": false
}
```

[summary]
## execute_srd46_sql - 5 row(s)

| metal_id | metal_name_SRD |
|----------|----------------|
| metal_42 | Cu^[+] |
| metal_41 | Cu^[2+] |
| metal_43 | Cu^[3+] |
| metal_112 | Ni^[2+] |
| metal_113 | Ni^[3+] |

---

### Step 13: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT ligand_id, ligand_name_SRD, ligand_class_name FROM ligandmetal_card WHERE ligand_class_name = 'Amino Acids' AND (ligand_name_SRD LIKE '%glycin%' OR ligand_name_SRD LIKE '%alanin%' OR ligand_name_SRD LIKE '%valin%' OR ligand_name_SRD LIKE '%leucin%' OR ligand_name_SRD LIKE '%isoleucin%' OR ligand_name_SRD LIKE '%serin%' OR ligand_name_SRD LIKE '%threonin%' OR ligand_name_SRD LIKE '%cystein%' OR ligand_name_SRD LIKE '%methionin%' OR ligand_name_SRD LIKE '%aspart%' OR ligand_name_SRD LIKE '%glutam%' OR ligand_name_SRD LIKE '%asparagin%' OR ligand_name_SRD LIKE '%glutamin%' OR ligand_name_SRD LIKE '%lysin%' OR ligand_name_SRD LIKE '%arginin%' OR ligand_name_SRD LIKE '%histidin%' OR ligand_name_SRD LIKE '%phenylalanin%' OR ligand_name_SRD LIKE '%tyrosin%' OR ligand_name_SRD LIKE '%tryptophan%' OR ligand_name_SRD LIKE '%prolin%') GROUP BY ligand_id, ligand_name_SRD, ligand_class_name ORDER BY ligand_name_SRD",
  "attach_equilibrium": false,
  "attach_literature": false
}
```

[summary]
## execute_srd46_sql - 50 row(s)

| ligand_id | ligand_name_SRD | ligand_class_name |
|-----------|-----------------|-------------------|
| ligand_6126 | (Carboxymethyl)trimethylammonium (nitrate) (N,N,N,-Trimethylglycine) (Betaine) | Amino Acids |
| ligand_5773 | 1-Aminocyclopentanecarboxylic acid (Cycloleucine) | Amino Acids |
| ligand_5959 | 2-(Carboxymethylaminomethyl)azole-4-sulfonic acid (N-(4-Sulfonyl-2-pyrrylmethyl... | Amino Acids |
| ligand_5788 | 3-Aminopropanoic acid (beta-Alanine) | Amino Acids |
| ligand_5760 | Aminoacetic acid (Glycine) | Amino Acids |
| ligand_5816 | D-3-Amino-3-carboxypropanohydroxamic acid (Asparagine hydroxamic acid) | Amino Acids |
| ligand_5768 | D-allo-2-Amino-3-methylpentanoic acid (D-allo-Isoleucine) | Amino Acids |
| ligand_5942 | DL-1,3-Thiazolidine-4-carboxylic acid (DL-Thiaproline) | Amino Acids |
| ligand_5805 | DL-2-Amino-2-methylpentanedioic acid (2-Methylglutamic acid) | Amino Acids |
| ligand_5783 | DL-2-Amino-3-(2-chlorophenyl)propanoic acid (DL-3-(2-Chlorophenyl)alanine) | Amino Acids |
| ligand_5780 | DL-2-Amino-3-(2-fluorophenyl)propanoic acid (DL-3-(2-Fluorophenyl)alanine) | Amino Acids |
| ligand_5817 | DL-2-Amino-3-(2-hydroxyphenyl)propanoic acid (o-Tyrosine) | Amino Acids |
| ligand_5860 | DL-2-Amino-3-(2-mercaptoimidazo-4-yl)propanoic acid (Thiohistidine) | Amino Acids |
| ligand_5855 | DL-2-Amino-3-(3,4-dimethoxyphenyl)propanoic acid (3,4-Dimethoxyphenylalanine) | Amino Acids |
| ligand_5784 | DL-2-Amino-3-(3-chlorophenyl)propanoic acid (DL-3-(3-Chlorophenyl)alanine) | Amino Acids |
| ligand_5781 | DL-2-Amino-3-(3-fluorophenyl)propanoic acid (DL-3-(3-Fluorophenyl)alanine) | Amino Acids |
| ligand_5818 | DL-2-Amino-3-(3-hydroxyphenyl)propanoic acid (m-Tyrosine) | Amino Acids |
| ligand_5785 | DL-2-Amino-3-(4-chlorophenyl)propanoic acid (DL-3-(4-Chlorophenyl)alanine) | Amino Acids |
| ligand_5782 | DL-2-Amino-3-(4-fluorophenyl)propanoic acid (DL-3-(4-Fluorophenyl)alanine) | Amino Acids |
| ligand_5778 | DL-2-Amino-3-chloropropanoic acid (3-Chloroalanine) | Amino Acids |
| ligand_5807 | DL-2-Amino-3-hydroxypentanedioic acid (3-Hydroxyglutamic acid) | Amino Acids |
| ligand_11519 | DL-2-Amino-3-methoxypropanoic acid (3-Methoxyalanine) | Amino Acids |
| ligand_5803 | DL-2-Amino-3-methylbutanedioic acid (3-Methylaspartic acid) | Amino Acids |
| ligand_5859 | DL-2-Amino-4-mercaptobutanoic acid (Homocysteine) | Amino Acids |
| ligand_5764 | DL-2-Aminohexanoic acid (Norleucine) | Amino Acids |

... 25 more row(s) omitted

---

### Step 14: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT ligand_id, ligand_name_SRD FROM ligandmetal_card WHERE ligand_class_name = 'Amino Acids' AND (ligand_name_SRD LIKE '%Glycine%' OR ligand_name_SRD LIKE '%Alanine%' OR ligand_name_SRD LIKE '%Valine%' OR ligand_name_SRD LIKE '%Leucine%' OR ligand_name_SRD LIKE '%Isoleucine%' OR ligand_name_SRD LIKE '%Serine%' OR ligand_name_SRD LIKE '%Threonine%' OR ligand_name_SRD LIKE '%Cysteine%' OR ligand_name_SRD LIKE '%Methionine%' OR ligand_name_SRD LIKE '%Aspartic acid%' OR ligand_name_SRD LIKE '%Aspartate%' OR ligand_name_SRD LIKE '%Glutamic acid%' OR ligand_name_SRD LIKE '%Glutamate%' OR ligand_name_SRD LIKE '%Lysine%' OR ligand_name_SRD LIKE '%Arginine%' OR ligand_name_SRD LIKE '%Histidine%' OR ligand_name_SRD LIKE '%Phenylalanine%' OR ligand_name_SRD LIKE '%Tyrosine%' OR ligand_name_SRD LIKE '%Tryptophan%' OR ligand_name_SRD LIKE '%Proline%') GROUP BY ligand_id, ligand_name_SRD ORDER BY ligand_name_SRD",
  "attach_equilibrium": false,
  "attach_literature": false
}
```

[summary]
## execute_srd46_sql - 50 row(s)

| ligand_id | ligand_name_SRD |
|-----------|-----------------|
| ligand_6126 | (Carboxymethyl)trimethylammonium (nitrate) (N,N,N,-Trimethylglycine) (Betaine) |
| ligand_5773 | 1-Aminocyclopentanecarboxylic acid (Cycloleucine) |
| ligand_5959 | 2-(Carboxymethylaminomethyl)azole-4-sulfonic acid (N-(4-Sulfonyl-2-pyrrylmethyl... |
| ligand_5788 | 3-Aminopropanoic acid (beta-Alanine) |
| ligand_5760 | Aminoacetic acid (Glycine) |
| ligand_5768 | D-allo-2-Amino-3-methylpentanoic acid (D-allo-Isoleucine) |
| ligand_5942 | DL-1,3-Thiazolidine-4-carboxylic acid (DL-Thiaproline) |
| ligand_5805 | DL-2-Amino-2-methylpentanedioic acid (2-Methylglutamic acid) |
| ligand_5783 | DL-2-Amino-3-(2-chlorophenyl)propanoic acid (DL-3-(2-Chlorophenyl)alanine) |
| ligand_5780 | DL-2-Amino-3-(2-fluorophenyl)propanoic acid (DL-3-(2-Fluorophenyl)alanine) |
| ligand_5817 | DL-2-Amino-3-(2-hydroxyphenyl)propanoic acid (o-Tyrosine) |
| ligand_5860 | DL-2-Amino-3-(2-mercaptoimidazo-4-yl)propanoic acid (Thiohistidine) |
| ligand_5855 | DL-2-Amino-3-(3,4-dimethoxyphenyl)propanoic acid (3,4-Dimethoxyphenylalanine) |
| ligand_5784 | DL-2-Amino-3-(3-chlorophenyl)propanoic acid (DL-3-(3-Chlorophenyl)alanine) |
| ligand_5781 | DL-2-Amino-3-(3-fluorophenyl)propanoic acid (DL-3-(3-Fluorophenyl)alanine) |
| ligand_5818 | DL-2-Amino-3-(3-hydroxyphenyl)propanoic acid (m-Tyrosine) |
| ligand_5785 | DL-2-Amino-3-(4-chlorophenyl)propanoic acid (DL-3-(4-Chlorophenyl)alanine) |
| ligand_5782 | DL-2-Amino-3-(4-fluorophenyl)propanoic acid (DL-3-(4-Fluorophenyl)alanine) |
| ligand_5778 | DL-2-Amino-3-chloropropanoic acid (3-Chloroalanine) |
| ligand_5807 | DL-2-Amino-3-hydroxypentanedioic acid (3-Hydroxyglutamic acid) |
| ligand_11519 | DL-2-Amino-3-methoxypropanoic acid (3-Methoxyalanine) |
| ligand_5803 | DL-2-Amino-3-methylbutanedioic acid (3-Methylaspartic acid) |
| ligand_5859 | DL-2-Amino-4-mercaptobutanoic acid (Homocysteine) |
| ligand_5764 | DL-2-Aminohexanoic acid (Norleucine) |
| ligand_5842 | DL-2-Aminopentanedioic acid 1-ethyl ester (1-Ethyl glutamate) |

... 25 more row(s) omitted

---

### Step 15: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT DISTINCT ligand_id, ligand_name_SRD FROM ligandmetal_card WHERE ligand_class_name = 'Amino Acids' AND (ligand_name_SRD IN ('Aminoacetic acid (Glycine)','2-Amino-3-(1H-imidazol-4-yl)propanoic acid (Histidine)','2-Amino-3-mercaptopropanoic acid (Cysteine)','2-Aminobutanedioic acid (Aspartic acid)','2-Aminopentanedioic acid (Glutamic acid)','2-Amino-3-hydroxypropanoic acid (Serine)','2-Amino-4-methylthiobutanoic acid (Methionine)','2-Amino-3-(4-hydroxyphenyl)propanoic acid (Tyrosine)','2-Aminopropanoic acid (Alanine)','Pyrrolidine-2-carboxylic acid (Proline)','2-Amino-3-methylbutanoic acid (Valine)','2-Amino-4-methylpentanoic acid (Leucine)','2-Amino-3-methylpentanoic acid (Isoleucine)','2-Amino-3-phenylpropanoic acid (Phenylalanine)','2-Amino-3-(1H-indol-3-yl)propanoic acid (Tryptophan)','2,6-Diaminohexanoic acid (Lysine)','2-Amino-5-guanidinopentanoic acid (Arginine)','2-Amino-3-hydroxybutanoic acid (Threonine)') OR ligand_name_SRD LIKE '%(Glycine)%' OR ligand_name_SRD LIKE '%(Histidine)%' OR ligand_name_SRD LIKE '%(Cysteine)%' OR ligand_name_SRD LIKE '%(Aspartic acid)%' OR ligand_name_SRD LIKE '%(Glutamic acid)%' OR ligand_name_SRD LIKE '%(Serine)%' OR ligand_name_SRD LIKE '%(Methionine)%' OR ligand_name_SRD LIKE '%(Tyrosine)%' OR ligand_name_SRD LIKE '%(Alanine)%' OR ligand_name_SRD LIKE '%(Proline)%' OR ligand_name_SRD LIKE '%(Valine)%' OR ligand_name_SRD LIKE '%(Leucine)%' OR ligand_name_SRD LIKE '%(Isoleucine)%' OR ligand_name_SRD LIKE '%(Phenylalanine)%' OR ligand_name_SRD LIKE '%(Tryptophan)%' OR ligand_name_SRD LIKE '%(Lysine)%' OR ligand_name_SRD LIKE '%(Arginine)%' OR ligand_name_SRD LIKE '%(Threonine)%') ORDER BY ligand_name_SRD",
  "attach_equilibrium": false,
  "attach_literature": false
}
```

[summary]
## execute_srd46_sql - 17 row(s)

| ligand_id | ligand_name_SRD |
|-----------|-----------------|
| ligand_5760 | Aminoacetic acid (Glycine) |
| ligand_5887 | L-2,6-Diaminohexanoic acid (Lysine) |
| ligand_5907 | L-2-Amino-3-(3-indolyl)propanoic acid (Tryptophan) |
| ligand_5819 | L-2-Amino-3-(4-hydroxyphenyl)propanoic acid (Tyrosine) |
| ligand_5898 | L-2-Amino-3-(4-imidazolyl)propanoic acid (Histidine) |
| ligand_5829 | L-2-Amino-3-hydroxybutanoic acid (Threonine) |
| ligand_5828 | L-2-Amino-3-hydroxypropanoic acid (Serine) |
| ligand_5856 | L-2-Amino-3-mercaptopropanoic acid (Cysteine) |
| ligand_5765 | L-2-Amino-3-methylbutanoic acid (Valine) |
| ligand_5767 | L-2-Amino-3-methylpentanoic acid (Isoleucine) |
| ligand_5777 | L-2-Amino-3-phenylpropanoic acid (Phenylalanine) |
| ligand_5863 | L-2-Amino-4-(methylthio)butanoic acid (Methionine) |
| ligand_5766 | L-2-Amino-4-methylpentanoic acid (Leucine) |
| ligand_5917 | L-2-Amino-5-guanidopentanoic acid (Arginine) |
| ligand_5804 | L-2-Aminopentanedioic acid (Glutamic acid) |
| ligand_5761 | L-2-Aminopropanoic acid (Alanine) |
| ligand_5802 | L-Aminobutanedioic acid (Aspartic acid) |

---

### Step 16: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id IN (ligand_5760, ligand_5887, ligand_5907, ligand_5819, ligand_5898, ligand_5829, ligand_5828, ligand_5856, ligand_5765, ligand_5767, ligand_5777, ligand_5863, ligand_5766, ligand_5917, ligand_5804, ligand_5761, ligand_5802) AND c.metal_id IN (metal_41, metal_112))",
  "order_by": "c.ligand_name_SRD, c.metal_name_SRD, s.temperature_c, s.ionic_strength_mol_l, s.constant_value DESC",
  "limit": 500
}
```

[summary]
## search_stability — 200 row(s)

### logK — 9 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_112 | Ni^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 27 | 3 | 10~40 | 0~3 | *** | 9 |
| metal_41 | Cu^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 18 | 2 | 10~40 | 0~2.5 | *** | 9 |
| metal_112 | Ni^[2+] | ligand_5887 | L-2,6-Diaminohexanoic acid … | HL | NCCCC[C@H](N)C(=O)O | 14 | 9 | 25~37 | 0.1~0.15 | *** | 2 |
| metal_41 | Cu^[2+] | ligand_5887 | L-2,6-Diaminohexanoic acid … | HL | NCCCC[C@H](N)C(=O)O | 12 | 4 | 25~37 | 0.1~1 | *** | 3 |
| metal_41 | Cu^[2+] | ligand_5907 | L-2-Amino-3-(3-indolyl)prop… | HL | N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O | 9 | 3 | 25~37 | 0.1~3 | *** | 4 |
| metal_112 | Ni^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 9 | 9 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_5907 | L-2-Amino-3-(3-indolyl)prop… | HL | N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O | 7 | 3 | 25~35 | 0.1~3 | *** | 3 |
| metal_41 | Cu^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 7 | 5 | 25 | 0.1~0.5 | *** | 2 |
| metal_41 | Cu^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |

### ΔH — 8 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_112 | Ni^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 14 | 3 | 10~40 | 0~1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 8 | 2 | 10~40 | 0~0.1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 8 | 8 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5887 | L-2,6-Diaminohexanoic acid … | HL | NCCCC[C@H](N)C(=O)O | 4 | 4 | 25 | 0.1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_5887 | L-2,6-Diaminohexanoic acid … | HL | NCCCC[C@H](N)C(=O)O | 4 | 4 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5907 | L-2-Amino-3-(3-indolyl)prop… | HL | N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O | 4 | 2 | 25 | 0.1~3 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 4 | 4 | 25 | 0.1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_5907 | L-2-Amino-3-(3-indolyl)prop… | HL | N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O | 3 | 3 | 25 | 3 | *** | 0 |

### ΔS — 9 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_112 | Ni^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 8 | 3 | 25 | 0~1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 8 | 8 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 7 | 7 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 4 | 2 | 25 | 0~0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5887 | L-2,6-Diaminohexanoic acid … | HL | NCCCC[C@H](N)C(=O)O | 4 | 4 | 25 | 0.1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_5887 | L-2,6-Diaminohexanoic acid … | HL | NCCCC[C@H](N)C(=O)O | 4 | 4 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5907 | L-2-Amino-3-(3-indolyl)prop… | HL | N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O | 4 | 2 | 25 | 0.1~3 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 4 | 4 | 25 | 0.1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_5907 | L-2-Amino-3-(3-indolyl)prop… | HL | N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O | 3 | 3 | 25 | 3 | *** | 0 |

---

### Step 17: `search_pka_values`
**Args:**
```json
{
  "where": "(lc.ligand_id IN (ligand_5760, ligand_5887, ligand_5907, ligand_5819, ligand_5898, ligand_5829, ligand_5828, ligand_5856, ligand_5765, ligand_5767, ligand_5777, ligand_5863, ligand_5766, ligand_5917, ligand_5804, ligand_5761, ligand_5802))",
  "order_by": "lc.ligand_name_SRD, p.temperature_c, p.ionic_strength_mol_l, p.pKa ASC",
  "limit": 500
}
```

[summary]
## search_pka_values — 41 row(s)

### pKa -12.5–-12.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_99378 | ligand_5917 | L-2-Amino-5-guanidopentanoic acid … | H2L | N=C(N)NCCC[C@H](N)C(=O)O | -12.1 | 25 | 0.1 | L→HL | M_tot_11 | M_tot_3 |

### pKa -2.0–-1.5 (2 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_97397 | ligand_5856 | L-2-Amino-3-mercaptopropanoic acid… | H2L | N[C@@H](CS)C(=O)O | -1.9 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_2 |
| vlm_98740 | ligand_5898 | L-2-Amino-3-(4-imidazolyl)propanoi… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | -1.7 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_3 |

### pKa 1.5–2.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_95563 | ligand_5802 | L-Aminobutanedioic acid (Aspartic … | H2L | N[C@@H](CC(=O)O)C(=O)O | 1.95 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_1 |

### pKa 2.0–2.5 (14 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_99389 | ligand_5917 | L-2-Amino-5-guanidopentanoic acid … | H2L | N=C(N)NCCC[C@H](N)C(=O)O | 2.03 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_2 |
| vlm_98379 | ligand_5887 | L-2,6-Diaminohexanoic acid (Lysine) | HL | NCCCC[C@H](N)C(=O)O | 2.15 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_2 |
| vlm_96511 | ligand_5828 | L-2-Amino-3-hydroxypropanoic acid … | HL | N[C@@H](CO)C(=O)O | 2.16 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_3 |
| vlm_95761 | ligand_5804 | L-2-Aminopentanedioic acid (Glutam… | H2L | N[C@@H](CCC(=O)O)C(=O)O | 2.16 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_2 |
| vlm_94993 | ligand_5777 | L-2-Amino-3-phenylpropanoic acid (… | HL | N[C@@H](Cc1ccccc1)C(=O)O | 2.18 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_1 |

**Band stats (all 14 entries):**

| stat | value |
|------|-------|
| entries | 14 |
| unique ligands | 14 |
| pKa range | 2.03 – 2.37 |
| T°C range | 25 – 25 |
| I(M) range | 0.1 – 0.1 |
| HxL forms | HL(11), H2L(3) |
| functional groups | carboxyl(14), primary_amine(14), aromatic_ring(3), hydroxyl(3), imine(1), phenol(1), secondary_amine(1), thioether(1) |

### pKa 3.5–4.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_95550 | ligand_5802 | L-Aminobutanedioic acid (Aspartic … | H2L | N[C@@H](CC(=O)O)C(=O)O | 3.71 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_9 |

### pKa 4.0–4.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_95750 | ligand_5804 | L-2-Aminopentanedioic acid (Glutam… | H2L | N[C@@H](CCC(=O)O)C(=O)O | 4.15 | 25 | 0.1 | HL→H2L | M_tot_2 | M_tot_8 |

### pKa 6.0–6.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_98723 | ligand_5898 | L-2-Amino-3-(4-imidazolyl)propanoi… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 6.05 | 25 | 0.1 | HL→H2L | M_tot_3 | M_tot_6 |

### pKa 8.0–8.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_97384 | ligand_5856 | L-2-Amino-3-mercaptopropanoic acid… | H2L | N[C@@H](CS)C(=O)O | 8.18 | 25 | 0.1 | HL→H2L | M_tot_2 | M_tot_9 |

### pKa 8.5–9.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_96674 | ligand_5829 | L-2-Amino-3-hydroxybutanoic acid (… | HL | C[C@@H](O)[C@H](N)C(=O)O | 8.94 | 25 | 0.1 | L→HL | M_tot_2 | M_tot_11 |

### pKa 9.0–9.5 (8 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_99382 | ligand_5917 | L-2-Amino-5-guanidopentanoic acid … | H2L | N=C(N)NCCC[C@H](N)C(=O)O | 9 | 25 | 0.1 | HL→H2L | M_tot_2 | M_tot_11 |
| vlm_96234 | ligand_5819 | L-2-Amino-3-(4-hydroxyphenyl)propa… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 9.04 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_10 |
| vlm_96498 | ligand_5828 | L-2-Amino-3-hydroxypropanoic acid … | HL | N[C@@H](CO)C(=O)O | 9.05 | 25 | 0.1 | L→HL | M_tot_3 | M_tot_16 |
| vlm_97802 | ligand_5863 | L-2-Amino-4-(methylthio)butanoic a… | HL | CSCC[C@H](N)C(=O)O | 9.08 | 25 | 0.1 | L→HL | M_tot_3 | M_tot_15 |
| vlm_94975 | ligand_5777 | L-2-Amino-3-phenylpropanoic acid (… | HL | N[C@@H](Cc1ccccc1)C(=O)O | 9.09 | 25 | 0.1 | L→HL | M_tot_1 | M_tot_11 |

**Band stats (all 8 entries):**

| stat | value |
|------|-------|
| entries | 8 |
| unique ligands | 8 |
| pKa range | 9.00 – 9.33 |
| T°C range | 25 – 25 |
| I(M) range | 0.1 – 0.1 |
| HxL forms | HL(6), H2L(2) |
| functional groups | carboxyl(8), primary_amine(8), aromatic_ring(4), hydroxyl(2), imine(1), phenol(1), secondary_amine(1), thioether(1) |

### pKa 9.5–10.0 (7 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_94551 | ligand_5765 | L-2-Amino-3-methylbutanoic acid (V… | HL | CC(C)[C@H](N)C(=O)O | 9.52 | 25 | 0.1 | L→HL | M_tot_3 | M_tot_11 |
| vlm_93606 | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 9.57 | 25 | 0.1 | L→HL | M_tot_20 | M_tot_43 |
| vlm_94665 | ligand_5766 | L-2-Amino-4-methylpentanoic acid (… | HL | CC(C)C[C@H](N)C(=O)O | 9.58 | 25 | 0.1 | L→HL | M_tot_3 | M_tot_7 |
| vlm_95739 | ligand_5804 | L-2-Aminopentanedioic acid (Glutam… | H2L | N[C@@H](CCC(=O)O)C(=O)O | 9.58 | 25 | 0.1 | L→HL | M_tot_8 | M_tot_17 |
| vlm_94748 | ligand_5767 | L-2-Amino-3-methylpentanoic acid (… | HL | CC[C@H](C)[C@H](N)C(=O)O | 9.6 | 25 | 0.1 | L→HL | M_tot_2 | M_tot_7 |

**Band stats (all 7 entries):**

| stat | value |
|------|-------|
| entries | 7 |
| unique ligands | 7 |
| pKa range | 9.52 – 9.71 |
| T°C range | 25 – 25 |
| I(M) range | 0.1 – 0.1 |
| HxL forms | HL(5), H2L(2) |
| functional groups | carboxyl(7), primary_amine(7) |

### pKa 10.0–10.5 (2 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_96227 | ligand_5819 | L-2-Amino-3-(4-hydroxyphenyl)propa… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 10.1 | 25 | 0.1 | L→HL | M_tot_10 | M_tot_1 |
| vlm_97371 | ligand_5856 | L-2-Amino-3-mercaptopropanoic acid… | H2L | N[C@@H](CS)C(=O)O | 10.3 | 25 | 0.1 | L→HL | M_tot_9 | M_tot_17 |

### pKa 10.5–11.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_98363 | ligand_5887 | L-2,6-Diaminohexanoic acid (Lysine) | HL | NCCCC[C@H](N)C(=O)O | 10.66 | 25 | 0.1 | L→HL | M_tot_8 | M_tot_4 |

---
