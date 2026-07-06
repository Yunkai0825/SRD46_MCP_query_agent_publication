# Q2.2.1 — Tool Results (batch 2)

### Step 3: `db_count_records`
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

### Step 4: `db_count_records`
**Args:**
```json
{
  "table": "ligandmetal_stability_measured",
  "where": "temperature_c = '{''$ne'': None}'"
}
```

[summary]
## db_count_records

| table | where | count |
|-------|-------|-------|
| ligandmetal_stability_measured | temperature_c = '{''$ne'': None}' | 0 |

---

### Step 5: `search_stability`
**Args:**
```json
{
  "where": "(s.temperature_c >= 24.9 AND s.temperature_c <= 25.1)",
  "limit": 1
}
```

[summary]
## search_stability — 1 row(s)

### `H^[+]` + Aminoacetic acid (Glycine) — 1 measurement(s)
metal_id: metal_68 | ligand_id: ligand_5760
ligand_HxL_def: HL | ligand_SMILES: NCC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_93606 | ref_eq_map_1 | beta_def_79 | logK | 9.57 | 25 | 0.1 | `[L] + [H] <=> [HL]` | *** | [L]; [HL] | (2.33, HL, 9.57, L, +inf) |

---

### Step 6: `search_stability`
**Args:**
```json
{
  "where": "(s.temperature_c >= 298.0 AND s.temperature_c <= 298.3)",
  "limit": 1
}
```

[summary]
## search_stability

*(no results)*

---

### Step 7: `db_count_records`
**Args:**
```json
{
  "table": "ligandmetal_stability_measured",
  "where": "temperature_c IS NOT NULL"
}
```

[summary]
## db_count_records

| table | where | count |
|-------|-------|-------|
| ligandmetal_stability_measured | temperature_c IS NOT NULL | 79063 |

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(s.temperature_c >= 24.9 AND s.temperature_c <= 25.1)",
  "limit": 100000
}
```

[summary]
## search_stability — 200 row(s)

### logK — 30 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 22 | 2 | 25 | 0~3 | *** | 12 |
| metal_112 | Ni^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 18 | 3 | 25 | 0~3 | *** | 6 |
| metal_33 | Co^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 13 | 4 | 25 | 0~1 | *** | 4 |
| metal_41 | Cu^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 12 | 2 | 25 | 0~2.5 | *** | 6 |
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 7 | 3 | 25 | 0~3 | *** | 4 |
| metal_92 | Mg^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 6 | 3 | 25 | 0~3 | *** | 4 |
| metal_25 | Ca^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 5 | 2 | 25 | 0~3 | *** | 4 |
| metal_94 | Mn^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 5 | 2 | 25 | 0~0.5 | *** | 3 |
| metal_106 | Na^[+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 3 | 1 | 25 | 0~0.5 | *** | 3 |
| metal_110 | Nd^[3+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_185 | Th^[4+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 3 | 3 | 25 | 1 | *** | 1 |
| metal_195 | UO_[2]^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 3 | 2 | 25 | 0.1~1 | *** | 2 |
| metal_177 | Sr^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 2 | 1 | 25 | 0~0.1 | *** | 2 |
| metal_58 | Eu^[3+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 2 | 2 | 25 | 0.1~2 | *** | 2 |
| metal_65 | Gd^[3+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_118 | NpO_[2]^[+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_36 | Cr^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 2 | 2 | 25 | 1 | *** | 1 |
| metal_187 | Ti^[3+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 2 | 2 | 25 | 1 | *** | 1 |
| metal_18 | Ba^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 0 | *** | 1 |
| metal_205 | Y^[3+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_139 | Pr^[3+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_173 | Sm^[3+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_179 | Tb^[3+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_44 | Dy^[3+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_73 | Ho^[3+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_55 | Er^[3+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_206 | Yb^[3+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_81 | Lu^[3+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_151 | PuO_[2]^[+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |

### ΔH — 15 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 8 | 2 | 25 | 0~3 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 8 | 3 | 25 | 0~1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 4 | 2 | 25 | 0~0.1 | *** | 0 |
| metal_185 | Th^[4+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 3 | 3 | 25 | 1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 3 | 3 | 25 | 0 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 2 | 2 | 25 | 0 | *** | 0 |
| metal_195 | UO_[2]^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 2 | 2 | 25 | 1 | *** | 0 |
| metal_92 | Mg^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_27 | Ce^[3+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 2 | *** | 0 |
| metal_137 | Pm^[3+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 2 | *** | 0 |
| metal_58 | Eu^[3+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 2 | *** | 0 |
| metal_6 | Am^[3+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 2 | *** | 0 |
| metal_31 | Cm^[3+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 2 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 0 | *** | 0 |

### ΔS — 11 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 8 | 2 | 25 | 0~3 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 8 | 3 | 25 | 0~1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 6 | 3 | 25 | 0~0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 4 | 2 | 25 | 0~0.1 | *** | 0 |
| metal_185 | Th^[4+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 3 | 3 | 25 | 1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 2 | 2 | 25 | 0~0.1 | *** | 0 |
| metal_195 | UO_[2]^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 2 | 2 | 25 | 1 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 2 | 1 | 25 | 0~0.1 | *** | 0 |
| metal_92 | Mg^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_58 | Eu^[3+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 2 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 0 | *** | 0 |

---
