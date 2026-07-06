# Q3.1.4 — Tool Results (batch 2)

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

### Step 4: `get_table_schema`
**Args:**
```json
{
  "table_name": "ligandmetal_card",
  "database": "equilibrium"
}
```

[summary]
**get_table_schema:** Error - Table 'ligandmetal_card' not found.
Available tables: eq_collection_unassigned, eq_edge, eq_edge_species, eq_export_metadata, eq_map, eq_map_collection, eq_map_stray, eq_network, eq_network_species, eq_node, eq_node_species, sqlite_sequence

---

### Step 5: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT COUNT(*) AS overlap_count FROM (SELECT c.ligand_id FROM ligandmetal_card c WHERE c.metal_id IN (61, 62) GROUP BY c.ligand_id HAVING COUNT(DISTINCT c.metal_id) = 2)",
  "attach_equilibrium": false
}
```

[summary]
## execute_srd46_sql - 1 row(s)

| overlap_count |
|---------------|
| 94 |

---
