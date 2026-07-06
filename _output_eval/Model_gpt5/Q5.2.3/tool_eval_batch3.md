# Q5.2.3 — Tool Results (batch 3)

### Step 3: `search_stability`
**Args:**
```json
{
  "where": "(s.temperature_c BETWEEN 195 AND 205)",
  "order_by": "s.temperature_c ASC",
  "limit": 500
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
  "where": "(s.temperature_c BETWEEN 150 AND 250)",
  "order_by": "s.temperature_c ASC",
  "limit": 500
}
```

[summary]
## search_stability

*(no results)*

---

### Step 5: `search_stability`
**Args:**
```json
{
  "where": "(s.temperature_c BETWEEN 100 AND 300)",
  "order_by": "ABS(s.temperature_c - 200) ASC, s.temperature_c ASC",
  "limit": 1000
}
```

[summary]
## search_stability

*(no results)*

---

### Step 6: `search_stability`
**Args:**
```json
{
  "where": "(s.temperature_c IS NOT NULL)",
  "order_by": "ABS(s.temperature_c - 200) ASC, s.temperature_c ASC",
  "limit": 25
}
```

[summary]
## search_stability — 25 row(s)

### logK — 5 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_8318 | Adenosine-5'-(trihydrogendi… | H3L | Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]1O | 3 | 3 | 75 | 0 | *** | 1 |
| metal_92 | Mg^[2+] | ligand_8318 | Adenosine-5'-(trihydrogendi… | H3L | Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]1O | 3 | 3 | 75 | 0 | *** | 1 |
| metal_68 | H^[+] | ligand_9500 | 1-(2-Hydroxy-5-sulfophenyla… | H3L | O=S(=O)(O)c1ccc(O)c(/N=N/c2c(O)ccc3ccccc23)c1 | 2 | 2 | 75 | 0 | *** | 1 |
| metal_29 | Cf^[3+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 2 | 2 | 55 | 2 | *** | 1 |
| metal_37 | Cr^[3+] | ligand_9500 | 1-(2-Hydroxy-5-sulfophenyla… | H3L | O=S(=O)(O)c1ccc(O)c(/N=N/c2c(O)ccc3ccccc23)c1 | 1 | 1 | 75 | 0 | *** | 1 |

### ΔH — 4 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_8318 | Adenosine-5'-(trihydrogendi… | H3L | Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]1O | 3 | 3 | 75 | 0 | *** | 0 |
| metal_92 | Mg^[2+] | ligand_8318 | Adenosine-5'-(trihydrogendi… | H3L | Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]1O | 3 | 3 | 75 | 0 | *** | 0 |
| metal_68 | H^[+] | ligand_6797 | Methylamine | L | CN | 1 | 1 | 50 | 0 | *** | 0 |
| metal_68 | H^[+] | ligand_6802 | Hexylamine | L | CCCCCCN | 1 | 1 | 50 | 0 | *** | 0 |

### ΔS — 2 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_8318 | Adenosine-5'-(trihydrogendi… | H3L | Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]1O | 3 | 3 | 75 | 0 | *** | 0 |
| metal_92 | Mg^[2+] | ligand_8318 | Adenosine-5'-(trihydrogendi… | H3L | Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]1O | 3 | 3 | 75 | 0 | *** | 0 |

---
