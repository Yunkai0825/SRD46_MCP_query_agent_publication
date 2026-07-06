# Q5.2.6 — Tool Results (batch 5)

### Step 2: `search_stability`
**Args:**
```json
{
  "where": "(s.solvent_name LIKE '%CO2%' OR s.solvent_name LIKE '%carbon dioxide%' OR s.solvent_name LIKE '%supercritical%' OR s.solvent_name LIKE '%scCO2%' OR s.solvent_name LIKE '%sc-CO2%')",
  "limit": 50
}
```

[summary]
## search_stability

*(no results)*

---

### Step 3: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_stability_measured",
  "group_column": "solvent_name",
  "limit": 100
}
```

[summary]
## db_distribution - ligandmetal_stability_measured by solvent_name

**total_rows:** 79063

| value | count | pct |
|-------|-------|-----|
| H_[2]O | 79063 | 100.0% |

---
