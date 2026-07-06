# Q2.2.4 — Tool Results (batch 3)

### Step 2: `db_distribution`
**Args:**
```json
{
  "table": "ligand_card",
  "group_column": "ligand_class_name",
  "limit": 10
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

---

### Step 3: `db_count_records`
**Args:**
```json
{
  "table": "ligand_card",
  "where": "ligand_class_name = '{''not'': None}'"
}
```

[summary]
## db_count_records

| table | where | count |
|-------|-------|-------|
| ligand_card | ligand_class_name = '{''not'': None}' | 0 |

---

### Step 4: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT COUNT(DISTINCT ligand_class_name) AS distinct_classes FROM ligand_card WHERE ligand_class_name IS NOT NULL AND ligand_class_name != ''"
}
```

[summary]
## execute_srd46_sql - 1 row(s)

| distinct_classes |
|------------------|
| 59 |

---
