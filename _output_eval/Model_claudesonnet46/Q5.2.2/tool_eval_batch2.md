# Q5.2.2 — Tool Results (batch 2)

### Step 1: `search_ligands`
**Args:**
```json
{
  "name": "transferrin",
  "limit": 10
}
```

[PHASE ERROR] Call 0_preplan_decision first to triage the question before L0 searches.

---

### Step 2: `search_ligands`
**Args:**
```json
{
  "name": "albumin",
  "limit": 10
}
```

[PHASE ERROR] Call 0_preplan_decision first to triage the question before L0 searches.

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "protein",
  "limit": 10
}
```

[PHASE ERROR] Call 0_preplan_decision first to triage the question before L0 searches.

---

### Step 5: `search_ligands`
**Args:**
```json
{
  "name": "transferrin",
  "limit": 10
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 6: `search_ligands`
**Args:**
```json
{
  "name": "lactoferrin",
  "limit": 10
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 7: `search_ligands`
**Args:**
```json
{
  "name": "albumin",
  "limit": 10
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 8: `search_ligands`
**Args:**
```json
{
  "name": "metallothionein",
  "limit": 10
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 9: `search_ligands`
**Args:**
```json
{
  "name": "ferritin",
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
  "name": "casein",
  "limit": 10
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 12: `db_distribution`
**Args:**
```json
{
  "table": "ligand_card",
  "group_column": "ligand_class_name",
  "limit": 30
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

---

### Step 13: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_class_name IN ('amino acid', 'peptide', 'imidazole') AND c.metal_name_SRD IN ('iron(III)', 'copper(II)', 'zinc(II)'))",
  "order_by": "s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability

*(no results)*

---
