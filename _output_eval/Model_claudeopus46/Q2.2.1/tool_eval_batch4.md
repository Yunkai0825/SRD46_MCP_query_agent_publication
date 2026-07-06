# Q2.2.1 — Tool Results (batch 4)

### Step 2: `db_count_records`
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

### Step 3: `db_count_records`
**Args:**
```json
{
  "table": "ligandmetal_stability_measured",
  "where": "temperature_c = 25"
}
```

[summary]
## db_count_records

| table | where | count |
|-------|-------|-------|
| ligandmetal_stability_measured | temperature_c = 25 | 67237 |

---

### Step 4: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_stability_measured",
  "group_column": "temperature_c",
  "limit": 10
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

---
