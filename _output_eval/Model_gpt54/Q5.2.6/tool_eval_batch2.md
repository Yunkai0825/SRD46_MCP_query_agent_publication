# Q5.2.6 — Tool Results (batch 2)

### Step 3: `search_stability`
**Args:**
```json
{
  "where": "(LOWER(s.solvent_name) LIKE '%supercritical%' AND (LOWER(s.solvent_name) LIKE '%co2%' OR LOWER(s.solvent_name) LIKE '%co₂%'))",
  "order_by": "c.metal_name_SRD ASC, c.ligand_name_SRD ASC, s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability

*(no results)*

---

### Step 4: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_stability_measured",
  "group_column": "solvent_name",
  "where": "LOWER(solvent_name) LIKE '%co2%' OR LOWER(solvent_name) LIKE '%co₂%' OR LOWER(solvent_name) LIKE '%supercritical%'",
  "limit": 50
}
```

[summary]
## db_distribution - ligandmetal_stability_measured by solvent_name

**total_rows:** 0

| value | count | pct |
|-------|-------|-----|

---
