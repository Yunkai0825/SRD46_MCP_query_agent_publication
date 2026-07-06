# Q3.1.4 — Tool Results (batch 3)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "iron",
  "limit": 10
}
```

[summary]
## search_metals — 2 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_61 | Fe^[3+] | Fe | 3 | ✓ | [Fe+3] | InChI=1S/Fe/q+3 | beta_totN_128 | ligand_totN_406 | vlm_totN_1473 |
| metal_62 | Fe^[2+] | Fe | 2 | ✓ | [Fe+2] | InChI=1S/Fe/q+2 | beta_totN_57 | ligand_totN_217 | vlm_totN_667 |

---

### Step 3: `search_metals`
**Args:**
```json
{
  "symbol": "Fe",
  "limit": 10
}
```

[summary]
## search_metals — 2 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_61 | Fe^[3+] | Fe | 3 | ✓ | [Fe+3] | InChI=1S/Fe/q+3 | beta_totN_128 | ligand_totN_406 | vlm_totN_1473 |
| metal_62 | Fe^[2+] | Fe | 2 | ✓ | [Fe+2] | InChI=1S/Fe/q+2 | beta_totN_57 | ligand_totN_217 | vlm_totN_667 |

---

### Step 5: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT COUNT(DISTINCT ligand_id) AS n_shared_ligands FROM ligandmetal_card WHERE metal_id = 61 AND ligand_id IN (SELECT ligand_id FROM ligandmetal_card WHERE metal_id = 62)",
  "attach_equilibrium": true
}
```

[summary]
## execute_srd46_sql - 1 row(s)

| n_shared_ligands |
|------------------|
| 94 |

---

### Step 6: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "\nSELECT \n  c.ligand_id,\n  c.ligand_name_SRD,\n  c.metal_id,\n  c.metal_name_SRD,\n  c.beta_definition_name,\n  AVG(s.constant_value) AS avg_logbeta,\n  COUNT(*) AS n_measurements\nFROM ligandmetal_card c\nJOIN ligandmetal_stability_measured s ON c.card_id = s.card_id\nWHERE c.metal_id IN (61, 62)\n  AND c.ligand_id IN (\n    SELECT ligand_id FROM ligandmetal_card WHERE metal_id = 61\n    INTERSECT\n    SELECT ligand_id FROM ligandmetal_card WHERE metal_id = 62\n  )\n  AND s.constant_type = 'log'\n  AND c.beta_definition_name LIKE 'ML'\nGROUP BY c.ligand_id, c.metal_id, c.beta_definition_name\nORDER BY c.ligand_id, c.metal_id\nLIMIT 200\n",
  "attach_equilibrium": true
}
```

[summary]
## execute_srd46_sql

*(no results)*

---
