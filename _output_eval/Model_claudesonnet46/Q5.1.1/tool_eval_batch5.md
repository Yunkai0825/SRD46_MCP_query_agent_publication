# Q5.1.1 — Tool Results (batch 5)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "mercury",
  "limit": 10
}
```

[summary]
## search_metals — 8 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_20 | BuHg^[+] | B | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_53 | EtHg^[+] | EHg | 1 |  | *** | *** | beta_totN_4 | ligand_totN_3 | vlm_totN_6 |
| metal_71 | Hg^[2+] | Hg | 2 | ✓ | [Hg+2] | InChI=1S/Hg/q+2 | beta_totN_68 | ligand_totN_310 | vlm_totN_1097 |
| metal_72 | Hg^[+] | Hg | 1 | ✓ | [Hg+] | InChI=1S/Hg/q+1 | beta_totN_12 | ligand_totN_31 | vlm_totN_83 |
| metal_93 | MeHg^[+] | MHg | 1 |  | *** | *** | beta_totN_18 | ligand_totN_79 | vlm_totN_148 |
| metal_136 | PhHg^[+] | PhHg | 1 |  | *** | *** | beta_totN_2 | ligand_totN_8 | vlm_totN_8 |
| metal_145 | PrHg^[+] | Pr | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_176 | O_[3]SPhHg | S | 0 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |

---

### Step 3: `db_ranked_pairs`
**Args:**
```json
{
  "rank_by": "measurement_count",
  "limit": 20,
  "where": {
    "metal_id": "metal_41"
  }
}
```

[PHASE ERROR] Tool 'db_ranked_pairs' is not available yet. You must call 0_plan_search_strategy first (PHASE 2) before using the execution tools.

---

### Step 5: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_card",
  "group_column": "ligand_class_name",
  "where": "metal_id = 71",
  "limit": 25
}
```

[summary]
## db_distribution - ligandmetal_card by ligand_class_name

**total_rows:** 1097

| value | count | pct |
|-------|-------|-----|
| Inorganic ligands | 253 | 23.06% |
| EDTA and derivatives | 109 | 9.94% |
| miscellaneous ureas, hadrazides, amidines | 79 | 7.2% |
| Amino Acids | 76 | 6.93% |
| Aliphatic amines | 74 | 6.75% |
| miscellaneous sulfides | 40 | 3.65% |
| Carboxylic acids polyacids | 39 | 3.56% |
| Aza-macrocycles | 39 | 3.56% |
| Aliphatic amines secondary N | 36 | 3.28% |
| Pyridine carboxylic acids | 29 | 2.64% |
| Carboxylic acids | 29 | 2.64% |
| NTA and derivatives | 28 | 2.55% |
| Bipyridines | 28 | 2.55% |
| Aza-oxa-macrocycles | 23 | 2.1% |
| Carboxylic acids diacids S-Se-Te-P-As | 20 | 1.82% |
| Aza macrocycles with carboxylic acids | 19 | 1.73% |
| Pyridines (azines) | 17 | 1.55% |
| Tripyridines | 14 | 1.28% |
| Pyrroles (azoles) | 14 | 1.28% |
| miscellaneous crown ether | 12 | 1.09% |
| miscellaneous amides | 12 | 1.09% |
| Iminodiacetic acid and derivatives | 11 | 1.0% |
| Aliphatic amines tertiary N | 10 | 0.91% |
| tripeptides | 8 | 0.73% |
| Aza-oxo-macrocycles | 8 | 0.73% |

---

### Step 6: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND s.constant_type = 'log_beta')",
  "order_by": "s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability

*(no results)*

---

### Step 7: `db_ranked_pairs`
**Args:**
```json
{
  "rank_by": "measurement_count",
  "limit": 15,
  "where": "lc.metal_id = 'metal_71'"
}
```

[summary]
**db_ranked_pairs:** Error - Unknown rank_by='measurement_count'. Choose from: ['ligands_per_metal', 'measurements_per_ligand', 'measurements_per_metal', 'metals_per_ligand', 'pka_per_ligand']

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_93 AND s.constant_type = 'log_beta')",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[summary]
## search_stability

*(no results)*

---
