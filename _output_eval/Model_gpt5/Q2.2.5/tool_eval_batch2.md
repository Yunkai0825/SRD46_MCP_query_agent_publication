# Q2.2.5 — Tool Results (batch 2)

### Step 3: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_stability_measured",
  "group_column": "constant_type",
  "where": "constant_value IS NOT NULL",
  "limit": 200
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
  "table": "ligandmetal_stability_measured",
  "where": "constant_value IS NOT NULL"
}
```

[summary]
## db_count_records

| table | where | count |
|-------|-------|-------|
| ligandmetal_stability_measured | constant_value IS NOT NULL | 79063 |

---

### Step 5: `db_count_records`
**Args:**
```json
{
  "table": "ligandmetal_stability_measured",
  "where": "constant_value IS NOT NULL AND constant_type IS NULL"
}
```

[summary]
## db_count_records

| table | where | count |
|-------|-------|-------|
| ligandmetal_stability_measured | constant_value IS NOT NULL AND constant_type IS NULL | 0 |

---
