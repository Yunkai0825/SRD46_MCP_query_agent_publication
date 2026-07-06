# Q5.2.3 — Tool Results (batch 2)

### Step 3: `search_stability`
**Args:**
```json
{
  "where": "(s.temperature_c BETWEEN 199 AND 201 AND (s.solvent_name IS NULL OR s.solvent_name LIKE '%water%'))",
  "order_by": "c.metal_name_SRD ASC, c.ligand_name_SRD ASC",
  "limit": 50,
  "ligand_similarity": false
}
```

[summary]
## search_stability

*(no results)*

---

### Step 4: `search_stability`
**Args:**
```json
{
  "where": "(s.temperature_c BETWEEN 180 AND 220)",
  "order_by": "s.temperature_c ASC, c.metal_name_SRD ASC, c.ligand_name_SRD ASC",
  "limit": 200,
  "ligand_similarity": false
}
```

[summary]
## search_stability

*(no results)*

---
