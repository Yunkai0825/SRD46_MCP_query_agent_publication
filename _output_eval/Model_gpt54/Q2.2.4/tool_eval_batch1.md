# Q2.2.4 — Tool Results (batch 1)

### Step 3: `get_table_schema`
**Args:**
```json
{
  "table_name": "ligand_card",
  "database": "cards"
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

### Step 4: `db_distribution`
**Args:**
```json
{
  "table": "ligand_card",
  "group_column": "ligand_class_name",
  "where": "ligand_class_name = '{''$ne'': None}'",
  "limit": 200
}
```

[summary]
## db_distribution - ligand_card by ligand_class_name

**total_rows:** 0

| value | count | pct |
|-------|-------|-----|

---

### Step 5: `db_distribution`
**Args:**
```json
{
  "table": "ligand_card",
  "group_column": "ligand_class_name",
  "limit": 200
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
| Carboxylic acids seleno | 22 | 0.38% |
| Purines phosphates | 21 | 0.37% |
| Aza-thia-macrocycles | 20 | 0.35% |
| Catechols fuchsons | 15 | 0.26% |
| Carboxylic acids diacids hydroxy | 15 | 0.26% |
| Phenanthrolines | 13 | 0.23% |
| miscellaneous sulfonic acids | 12 | 0.21% |
| Tripyridines | 6 | 0.1% |
| Carboxylic acids diacids keto | 5 | 0.09% |

---

### Step 6: `db_count_records`
**Args:**
```json
{
  "table": "ligand_card"
}
```

[summary]
## db_count_records

| table | where | count |
|-------|-------|-------|
| ligand_card | (all) | 5750 |

---
