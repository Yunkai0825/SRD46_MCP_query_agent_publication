# Q5.2.3 — Tool Results (batch 1)

### Step 3: `get_table_schema`
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

### Step 4: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_stability_measured",
  "group_column": "temperature_c",
  "limit": 30
}
```

[summary]
## db_distribution - ligandmetal_stability_measured by temperature_c

**total_rows:** 79063

| value | count | pct |
|-------|-------|-----|
| 25.0 | 67237 | 85.04% |
| 20.0 | 6845 | 8.66% |
| 37.0 | 1699 | 2.15% |
| 30.0 | 919 | 1.16% |
| 35.0 | 488 | 0.62% |
| 18.0 | 482 | 0.61% |
| 10.0 | 334 | 0.42% |
| 40.0 | 324 | 0.41% |
| 22.0 | 324 | 0.41% |
| 15.0 | 197 | 0.25% |
| 45.0 | 60 | 0.08% |
| 50.0 | 44 | 0.06% |
| 27.0 | 44 | 0.06% |
| 0.0 | 27 | 0.03% |
| 75.0 | 21 | 0.03% |
| 5.0 | 12 | 0.02% |
| 55.0 | 2 | 0.0% |
| 12.0 | 2 | 0.0% |
| 23.0 | 1 | 0.0% |
| 3.0 | 1 | 0.0% |

---
