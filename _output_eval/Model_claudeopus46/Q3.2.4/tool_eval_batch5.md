# Q3.2.4 — Tool Results (batch 5)

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

### Step 4: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_card",
  "group_column": "ligand_class_name",
  "where": "metal_id = 61",
  "limit": 30
}
```

[summary]
## db_distribution - ligandmetal_card by ligand_class_name

**total_rows:** 1473

| value | count | pct |
|-------|-------|-----|
| Inorganic ligands | 198 | 13.44% |
| Catechols | 140 | 9.5% |
| miscellaneous hydroxamic acids | 124 | 8.42% |
| Amino Acids | 116 | 7.88% |
| EDTA and derivatives | 106 | 7.2% |
| Aliphatic amines | 102 | 6.92% |
| Phenols salicylic acids | 99 | 6.72% |
| Phenols | 67 | 4.55% |
| Carboxylic acids | 61 | 4.14% |
| Pyridines (azines) | 49 | 3.33% |
| NTA and derivatives | 45 | 3.05% |
| Aza macrocycles with carboxylic acids | 42 | 2.85% |
| Carboxylic acids diacids | 36 | 2.44% |
| cyclic ketones | 34 | 2.31% |
| Carboxylic acids polyacids | 33 | 2.24% |
| Aminophosphorus acids | 33 | 2.24% |
| Naphtols | 29 | 1.97% |
| Quinolines | 22 | 1.49% |
| Aza-macrocycles | 15 | 1.02% |
| Aliphatic amines secondary N | 15 | 1.02% |
| Aliphatic amines tertiary N | 14 | 0.95% |
| Carboxylic acids diacids hydroxy | 13 | 0.88% |
| Pyridine carboxylic acids | 12 | 0.81% |
| Phenanthrolines | 11 | 0.75% |
| Ketones (oxo ligands) | 9 | 0.61% |
| Iminodiacetic acid and derivatives | 8 | 0.54% |
| Carboxylic acids hydroxy | 8 | 0.54% |
| Catechols fuchsons | 6 | 0.41% |
| Carboxylic acids diacids S-Se-Te-P-As | 6 | 0.41% |
| Cyclic amines  | 5 | 0.34% |

---

### Step 5: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_card",
  "group_column": "ligand_class_name",
  "where": "metal_id = 62",
  "limit": 30
}
```

[summary]
## db_distribution - ligandmetal_card by ligand_class_name

**total_rows:** 667

| value | count | pct |
|-------|-------|-----|
| Amino Acids | 101 | 15.14% |
| EDTA and derivatives | 78 | 11.69% |
| Inorganic ligands | 75 | 11.24% |
| Phenanthrolines | 33 | 4.95% |
| Aminophosphorus acids | 31 | 4.65% |
| Bipyridines | 30 | 4.5% |
| NTA and derivatives | 29 | 4.35% |
| Pyridines (azines) | 28 | 4.2% |
| Pyridine carboxylic acids | 24 | 3.6% |
| Carboxylic acids polyacids | 23 | 3.45% |
| Iminodiacetic acid and derivatives | 20 | 3.0% |
| Aza macrocycles with carboxylic acids | 18 | 2.7% |
| Pyrroles (azoles) | 16 | 2.4% |
| Aza-macrocycles | 16 | 2.4% |
| Tripyridines | 15 | 2.25% |
| Catechols | 15 | 2.25% |
| Aza-oxa-macrocycles | 15 | 2.25% |
| Aliphatic amines secondary N | 15 | 2.25% |
| Carboxylic acids diacids S-Se-Te-P-As | 11 | 1.65% |
| Carboxylic acids diacids | 11 | 1.65% |
| Aliphatic amines tertiary N | 10 | 1.5% |
| miscellaneous hydroxamic acids | 9 | 1.35% |
| Aliphatic amines | 9 | 1.35% |
| Ketones (oxo ligands) | 5 | 0.75% |
| miscellaneous ureas, hadrazides, amidines | 4 | 0.6% |
| Aza-thia-macrocycles | 4 | 0.6% |
| miscellaneous mercaptans | 3 | 0.45% |
| Phenols salicylic acids | 3 | 0.45% |
| Aniline carboxylic acids | 3 | 0.45% |
| cyclic ketones | 2 | 0.3% |

---

### Step 6: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT c.metal_id, c.metal_name_SRD, c.ligand_class_name, c.beta_definition_name, COUNT(*) as n_measurements, ROUND(AVG(s.constant_value),2) as avg_logK, ROUND(MIN(s.constant_value),2) as min_logK, ROUND(MAX(s.constant_value),2) as max_logK FROM ligandmetal_card c JOIN ligandmetal_stability_measured s ON c.complex_system_id = c.complex_system_id WHERE c.metal_id IN (61, 62) AND s.constant_type = 'log_beta' AND s.temperature_c BETWEEN 20 AND 30 AND s.ionic_strength_mol_l BETWEEN 0.0 AND 1.0 AND c.beta_definition_name LIKE 'ML%' AND c.beta_definition_name NOT LIKE '%H%' AND c.beta_definition_name NOT LIKE '%OH%' GROUP BY c.metal_id, c.ligand_class_name, c.beta_definition_name ORDER BY c.metal_id, c.ligand_class_name, avg_logK DESC",
  "attach_equilibrium": false,
  "attach_literature": false
}
```

[summary]
## execute_srd46_sql

*(no results)*

---
