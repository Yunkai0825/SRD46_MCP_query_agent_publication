# Q3.1.4 — Tool Results (batch 4)

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

### Step 4: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT COUNT(*) AS shared_ligand_count FROM (SELECT DISTINCT ligand_id FROM ligandmetal_card WHERE metal_id = 61 INTERSECT SELECT DISTINCT ligand_id FROM ligandmetal_card WHERE metal_id = 62)",
  "attach_equilibrium": true
}
```

[summary]
## execute_srd46_sql - 1 row(s)

| shared_ligand_count |
|---------------------|
| 94 |

---

### Step 5: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT c.ligand_id, c.ligand_name_SRD, c.metal_id, c.metal_name_SRD, c.beta_definition_name, s.constant_value, s.temperature_c, s.ionic_strength_mol_l FROM ligandmetal_card c JOIN ligandmetal_stability_measured s ON c.complex_system_id = c.complex_system_id WHERE c.metal_id IN (61, 62) AND c.ligand_id IN (SELECT ligand_id FROM ligandmetal_card WHERE metal_id = 61 INTERSECT SELECT ligand_id FROM ligandmetal_card WHERE metal_id = 62) AND c.beta_definition_name LIKE 'ML%' AND s.constant_type = 'log_beta' ORDER BY c.ligand_id, c.metal_id, c.beta_definition_name, s.constant_value DESC",
  "attach_equilibrium": true
}
```

[summary]
## execute_srd46_sql

*(no results)*

---
