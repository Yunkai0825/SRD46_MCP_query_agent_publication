# Q5.2.2 — Tool Results (batch 4)

### Step 1: `search_ligands`
**Args:**
```json
{
  "name": "transferrin",
  "limit": 10
}
```

[PHASE ERROR] Call 0_preplan_decision first to triage the question before L0 searches.

---

### Step 2: `search_ligands`
**Args:**
```json
{
  "ligand_class": "protein",
  "limit": 10
}
```

[PHASE ERROR] Call 0_preplan_decision first to triage the question before L0 searches.

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "protein",
  "limit": 10
}
```

[PHASE ERROR] Call 0_preplan_decision first to triage the question before L0 searches.

---

### Step 5: `search_ligands`
**Args:**
```json
{
  "name": "transferrin",
  "limit": 20
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 6: `search_ligands`
**Args:**
```json
{
  "name": "albumin",
  "limit": 20
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 7: `search_ligands`
**Args:**
```json
{
  "name": "protein",
  "limit": 20
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 8: `search_ligands`
**Args:**
```json
{
  "ligand_class": "protein",
  "limit": 10
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 9: `search_ligands`
**Args:**
```json
{
  "name": "peptide",
  "limit": 10
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6692 | L-Alanyl-L-aspartyl-L-serylgly… (fibrinopeptide A) | *** | polypeptides | 12 | *** | (-inf, H6L, 2.6, H5L, 3.5, H4L, 3.62, H3L, 4.31, H2L, 5.03, HL, 8.4, L, +inf) |

---

### Step 10: `search_ligands`
**Args:**
```json
{
  "name": "ferritin",
  "limit": 10
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 11: `search_ligands`
**Args:**
```json
{
  "ligand_class": "polypeptide",
  "limit": 20
}
```

[summary]
## search_ligands — 20 result(s)

**stats:** 98 SQL matches · showing 20 · limit 20

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6595 | Glycylglycylglycylglycine (Tetraglycine) | HL | polypeptides | 46 | `NCC(=O)NCC(=O)NCC(=O)NCC(=O)O` | (-inf, H2L, 3.2, HL, 7.88, L, +inf) |
| ligand_6596 | L-Alanylglycylglycylglycine | HL | polypeptides | 6 | `C[C@H](N)C(=O)NCC(=O)NCC(=O)NCC(=O)O` | (-inf, H2L, 3.18, HL, 7.85, L, +inf) |
| ligand_6597 | L-Alanyl-L-alanyl-L-alanyl-L-alanine | HL | polypeptides | 10 | `C[C@H](N)C(=O)N[C@@H](C)C(=O)N[C@@H](C)C(=O)N[C@@H](C)C(=O)O` | (-inf, H2L, 3.31, HL, 7.83, L, +inf) |
| ligand_6598 | L-Alanyl-L-alanyl-D-alanyl-L-alanine | HL | polypeptides | 2 | `C[C@H](N)C(=O)N[C@@H](C)C(=O)N[C@H](C)C(=O)N[C@@H](C)C(=O)O` | (-inf, H2L, 3.13, HL, 7.82, L, +inf) |
| ligand_6599 | L-Alanyl-D-alanyl-L-alanyl-L-alanine | HL | polypeptides | 2 | `C[C@H](N)C(=O)N[C@H](C)C(=O)N[C@@H](C)C(=O)N[C@@H](C)C(=O)O` | (-inf, H2L, 3.11, HL, 7.88, L, +inf) |
| ligand_6600 | D-Alanyl-L-alanyl-L-alanyl-L-alanine | HL | polypeptides | 2 | `C[C@H](NC(=O)[C@H](C)NC(=O)[C@H](C)NC(=O)[C@@H](C)N)C(=O)O` | (-inf, H2L, 3.31, HL, 7.83, L, +inf) |
| ligand_6601 | Glycylglycyl-2-methylalanylglycine | HL | polypeptides | 6 | `CC(C)(NC(=O)CNC(=O)CN)C(=O)NCC(=O)O` | (-inf, H2L, 3.55, HL, 7.98, L, +inf) |
| ligand_6602 | 2-Methylalanyl-2-methylalanyl-2-methylalanylglyci… | HL | polypeptides | 6 | `CC(C)(N)C(=O)NC(C)(C)C(=O)NC(C)(C)C(=O)NCC(=O)O` | (-inf, H2L, 3.46, HL, 8.33, L, +inf) |
| ligand_6603 | 2-Methylalanyl-2-methylalanyl-2-methylalanyl-2-me… | HL | polypeptides | 6 | `CC(C)(N)C(=O)NC(C)(C)C(=O)NC(C)(C)C(=O)NC(C)(C)C(=O)O` | (-inf, H2L, 3.8, HL, 7.78, L, +inf) |
| ligand_6604 | Glycylglycylglycylsarcosine | HL | polypeptides | 6 | `CN(CC(=O)O)C(=O)CNC(=O)CNC(=O)CN` | (-inf, H2L, 3.04, HL, 7.92, L, +inf) |
| ligand_6605 | Glycylglycylsarcosylglycine | HL | polypeptides | 6 | `CN(CC(=O)NCC(=O)O)C(=O)CNC(=O)CN` | (-inf, H2L, 3.34, HL, 7.97, L, +inf) |
| ligand_6606 | Glycylsarcosylglycylglycine | HL | polypeptides | 7 | `CN(CC(=O)NCC(=O)NCC(=O)O)C(=O)CN` | (-inf, H2L, 3.35, HL, 8.28, L, +inf) |
| ligand_6607 | Sarcosylglycylglycylglycine | HL | polypeptides | 6 | `CNCC(=O)NCC(=O)NCC(=O)NCC(=O)O` | (-inf, H2L, 3.34, HL, 8.39, L, +inf) |
| ligand_6608 | Glycylglycylglycyl-L-proline | HL | polypeptides | 6 | `NCC(=O)NCC(=O)NCC(=O)N1CCC[C@H]1C(=O)O` | (-inf, H2L, 2.91, HL, 8.04, L, +inf) |
| ligand_6609 | Glycylglycyl-L-prolylglycine | HL | polypeptides | 6 | `NCC(=O)NCC(=O)N1CCC[C@H]1C(=O)NCC(=O)O` | (-inf, H2L, 3.17, HL, 8.06, L, +inf) |
| ligand_6610 | Glycyl-L-prolylglycylglycine | HL | polypeptides | 7 | `NCC(=O)N1CCC[C@H]1C(=O)NCC(=O)NCC(=O)O` | (-inf, H2L, 3.11, HL, 8.25, L, +inf) |
| ligand_6611 | L-Prolylglycylglycylglycine | HL | polypeptides | 6 | `O=C(O)CNC(=O)CNC(=O)CNC(=O)[C@@H]1CCCN1` | (-inf, H2L, 3.27, HL, 8.67, L, +inf) |
| ligand_6612 | L-Alanyl-L-alanyl-L-alanyl-L-proline | HL | polypeptides | 6 | `C[C@H](N)C(=O)N[C@@H](C)C(=O)N[C@@H](C)C(=O)N1CCC[C@H]1C(=O)O` | (-inf, H2L, 3.16, HL, 8.2, L, +inf) |
| ligand_6613 | L-Alanyl-L-alanyl-L-prolyl-L-alanine | HL | polypeptides | 6 | `C[C@H](N)C(=O)N[C@@H](C)C(=O)N1CCC[C@H]1C(=O)N[C@@H](C)C(=O)O` | (-inf, H2L, 3.34, HL, 8.2, L, +inf) |
| ligand_6614 | L-Alanyl-L-prolyl-L-alanyl-L-alanine | HL | polypeptides | 7 | `C[C@H](N)C(=O)N1CCC[C@H]1C(=O)N[C@@H](C)C(=O)N[C@@H](C)C(=O)O` | (-inf, H2L, 3.31, HL, 8.28, L, +inf) |

### Functional groups across all SQL matches (55 parseable SMILES)

| group | count | % |
|-------|-------|---|
| amide | 55 | 100% |
| carboxyl | 55 | 100% |
| primary_amine | 52 | 95% |
| aromatic_ring | 12 | 22% |
| hydroxyl | 5 | 9% |
| phenol | 5 | 9% |
| secondary_amine | 3 | 5% |
| imine | 1 | 2% |

---
