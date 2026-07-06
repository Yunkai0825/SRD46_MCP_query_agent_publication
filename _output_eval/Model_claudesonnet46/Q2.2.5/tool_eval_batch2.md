# Q2.2.5 — Tool Results (batch 2)

### Step 3: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_stability_measured",
  "group_column": "constant_type",
  "limit": 50
}
```

[summary]
## db_distribution - ligandmetal_stability_measured by constant_type

**total_rows:** 79063

| value | count | pct |
|-------|-------|-----|
| K | 60540 | 76.57% |
| H | 9693 | 12.26% |
| S | 8830 | 11.17% |

---

### Step 4: `db_count_records`
**Args:**
```json
{
  "table": "ligandmetal_stability_measured"
}
```

[summary]
## db_count_records

| table | where | count |
|-------|-------|-------|
| ligandmetal_stability_measured | (all) | 79063 |

---

### Step 5: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_stability_measured",
  "group_column": "reaction_type",
  "limit": 30
}
```

[summary]
## db_distribution - ligandmetal_stability_measured by reaction_type

**total_rows:** 79063

| value | count | pct |
|-------|-------|-----|
| homogeneous_aqueous | 77969 | 98.62% |
| dissolution | 1067 | 1.35% |
| gas_absorption | 22 | 0.03% |
| *** | 4 | 0.01% |
| unknown | 1 | 0.0% |

---
