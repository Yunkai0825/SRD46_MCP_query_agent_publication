# Q5.2.2 — Tool Results (batch 3)

### Step 2: `search_ligands`
**Args:**
```json
{
  "name": "transferrin",
  "limit": 5
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "albumin",
  "limit": 5
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 4: `search_ligands`
**Args:**
```json
{
  "name": "metallothionein",
  "limit": 5
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 5: `search_ligands`
**Args:**
```json
{
  "name": "hemoglobin",
  "limit": 5
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
  "name": "glutathione",
  "limit": 5
}
```

[summary]
## search_ligands — 4 result(s)

**stats:** 4 SQL matches · showing 4 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6592 | L-5-Glutamyl-L-cysteinylglycine (Glutathione) | H3L | tripeptides | 106 | `N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O` | (-inf, H4L, 2.08, H3L, 3.49, H2L, 8.64, HL, 9.51, L, +inf) |
| ligand_6593 | L-5-Glutamyl-(S-methyl-L-cy… (S-methylglutathione) | H2L | tripeptides | 5 | `CSC[C@H](NC(=O)CC[C@H](N)C(=O)O)C(=O)NCC(=O)O` | (-inf, HL, 9.08, L, +inf) |
| ligand_6682 | N,N-[N'',N''''-Di(L-5-glu… (Glutathione disulfide) | *** | polypeptides | 53 | *** | (-inf, H6L, -1.5, H5L, 2.35, H4L, 3.16, H3L, 3.83, H2L, 8.85, HL, 9.81, L, +inf) |
| ligand_10422 | L-5-Glutamyl-… (DL-Cysteine-glutathione disulfide) | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (2 parseable SMILES)

| group | count | % |
|-------|-------|---|
| amide | 2 | 100% |
| carboxyl | 2 | 100% |
| primary_amine | 2 | 100% |
| thioether | 1 | 50% |
| thiol | 1 | 50% |

---

### Step 7: `search_ligands`
**Args:**
```json
{
  "name": "glycine",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 170 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5760 | Aminoacetic acid (Glycine) | HL | Amino Acids | 428 | `NCC(=O)O` | (-inf, H2L, 2.33, HL, 9.57, L, +inf) |
| ligand_5776 | DL-Aminophenylacetic acid (Phenylglycine) | HL | Amino Acids | 12 | `NC(C(=O)O)c1ccccc1` | (-inf, H2L, -1.9, HL, 8.92, L, +inf) |
| ligand_5786 | DL-Amino-4-sulfophenylacet… (4-Sulfophenylglycine) | H2L | Amino Acids | 12 | `NC(C(=O)O)c1ccc(S(=O)(=O)O)cc1` | (-inf, H2L, -1.8, HL, 8.66, L, +inf) |
| ligand_5838 | DL-Amino-4-Methoxyphenyl… (4-Methoxyphenylglycine) | HL | Amino Acids | 12 | `COc1ccc(C(N)C(=O)O)cc1` | (-inf, H2L, 2, HL, 9.07, L, +inf) |
| ligand_5925 | N-Methylglycine (Sarcosine) | HL | Amino Acids | 39 | `CNCC(=O)O` | (-inf, H2L, 2.18, HL, 9.98, L, +inf) |

### Functional groups across all SQL matches (129 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 114 | 88% |
| amide | 96 | 74% |
| primary_amine | 78 | 60% |
| aromatic_ring | 26 | 20% |
| hydroxyl | 25 | 19% |
| secondary_amine | 22 | 17% |
| tertiary_amine | 14 | 11% |
| ester | 9 | 7% |
| thiol | 9 | 7% |
| phenol | 7 | 5% |
| imine | 5 | 4% |
| phosphonate | 3 | 2% |
| thioether | 3 | 2% |
| phosphate | 2 | 2% |
| pyridine | 2 | 2% |
| sulfonate | 2 | 2% |
| ether | 1 | 1% |

---

### Step 8: `search_ligands`
**Args:**
```json
{
  "name": "histidine",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 57 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5860 | DL-2-Amino-3-(2-mercaptoimidazo-4… (Thiohistidine) | H2L | Amino Acids | 20 | `NC(Cc1cnc(S)[nH]1)C(=O)O` | (-inf, H2L, 8.59, HL, 8.59, L, +inf) |
| ligand_5898 | L-2-Amino-3-(4-imidazolyl)propanoic a… (Histidine) | HL | Amino Acids | 250 | `N[C@@H](Cc1c[nH]cn1)C(=O)O` | (-inf, H3L, -1.7, H2L, 6.05, HL, 9.1, L, +inf) |
| ligand_5899 | L-2-Amino-3-(N(1)-methyl-4-imidazolyl)propanoic a… | HL | Amino Acids | 14 | `Cn1cnc(C[C@H](N)C(=O)O)c1` | (-inf, H3L, -1.72, H2L, 5.87, HL, 9.16, L, +inf) |
| ligand_5900 | L-2-Amino-3-(N(3)-methyl-4-imidazolyl)propanoic a… | HL | Amino Acids | 16 | `Cn1cncc1C[C@H](N)C(=O)O` | (-inf, H3L, -1.65, H2L, 6.48, HL, 8.61, L, +inf) |
| ligand_5901 | L-4-(2-Amino-3-carboxypropyl)-1,3-dimethylimidazo… | HL | Amino Acids | 6 | `Cn1c[n+](C)cc1C[C@H](N)C(=O)O` | (-inf, H2L, -1.98, HL, 7.85, L, +inf) |

### Functional groups across all SQL matches (46 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 40 | 87% |
| aromatic_ring | 38 | 83% |
| amide | 31 | 67% |
| primary_amine | 26 | 57% |
| imine | 9 | 20% |
| ester | 5 | 11% |
| secondary_amine | 5 | 11% |
| thiol | 4 | 9% |
| hydroxyl | 3 | 7% |
| halide | 2 | 4% |
| phenol | 2 | 4% |
| pyridine | 1 | 2% |
| tertiary_amine | 1 | 2% |
| thioether | 1 | 2% |

---

### Step 9: `search_ligands`
**Args:**
```json
{
  "name": "cysteine",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 26 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5856 | L-2-Amino-3-mercaptopropanoic acid (Cysteine) | H2L | Amino Acids | 134 | `N[C@@H](CS)C(=O)O` | (-inf, H3L, -1.9, H2L, 8.18, HL, 10.3, L, +inf) |
| ligand_5859 | DL-2-Amino-4-mercaptobutanoic acid (Homocysteine) | H2L | Amino Acids | 3 | `NC(CCS)C(=O)O` | (-inf, H3L, 2.15, H2L, 8.57, HL, 10.38, L, +inf) |
| ligand_5861 | L-2-Amino-3-(methylthio)propan… (S-Methylcysteine) | HL | Amino Acids | 39 | `CSC[C@H](N)C(=O)O` | (-inf, H2L, 2, HL, 8.74, L, +inf) |
| ligand_5862 | L-2-Amino-3-(ethylthio)propanoi… (S-Ethylcysteine) | HL | Amino Acids | 46 | `CCSC[C@H](N)C(=O)O` | (-inf, H2L, -1.9, HL, 8.65, L, +inf) |
| ligand_5871 | L-2-Amino-3-(2-Cyanoethylthio)propanoic acid (L-5… | HL | Amino Acids | 1 | `N#CCCSCC(N)C(=O)O` | (-inf, HL, 8.46, L, +inf) |

### Functional groups across all SQL matches (22 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 19 | 86% |
| primary_amine | 19 | 86% |
| thiol | 12 | 55% |
| amide | 11 | 50% |
| thioether | 10 | 45% |
| ester | 4 | 18% |
| aromatic_ring | 1 | 5% |
| nitrile | 1 | 5% |
| secondary_amine | 1 | 5% |

---

### Step 10: `search_ligands`
**Args:**
```json
{
  "name": "hemin",
  "limit": 5
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
  "name": "porphyrin",
  "limit": 10
}
```

[summary]
## search_ligands — 2 result(s)

**stats:** 2 SQL matches · showing 2 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_10606 | Tetraphenylporphyrinsulfonate | *** | Ligands not selected | 0 | *** | *** |
| ligand_10607 | Hematoporphyrin | *** | Ligands not selected | 0 | *** | *** |

---

### Step 12: `search_ligands`
**Args:**
```json
{
  "name": "imidazole",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 50 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_7795 | 1,3-Diazole (Imidazole) | L | Pyrroles (azoles) | 237 | `c1c[nH]cn1` | (-inf, HL, 7, L, 7, H-1L, +inf) |
| ligand_7796 | 1-Methylimidazole | L | Pyrroles (azoles) | 52 | `Cn1ccnc1` | (-inf, HL, 7.1, L, +inf) |
| ligand_7797 | 1-Ethylimidazole | L | Pyrroles (azoles) | 17 | `CCn1ccnc1` | (-inf, HL, 7.21, L, +inf) |
| ligand_7798 | 1-Propylimidazole | L | Pyrroles (azoles) | 17 | `CCCn1ccnc1` | (-inf, HL, 7.22, L, +inf) |
| ligand_7799 | 1-Butylimidazole | L | Pyrroles (azoles) | 16 | `CCCCn1ccnc1` | (-inf, HL, 7.22, L, +inf) |

### Functional groups across all SQL matches (44 parseable SMILES)

| group | count | % |
|-------|-------|---|
| aromatic_ring | 44 | 100% |
| hydroxyl | 7 | 16% |
| primary_amine | 6 | 14% |
| pyridine | 3 | 7% |
| thiol | 3 | 7% |
| ester | 1 | 2% |
| secondary_amine | 1 | 2% |
| tertiary_amine | 1 | 2% |

---

### Step 13: `db_distribution`
**Args:**
```json
{
  "table": "ligand_card",
  "group_column": "ligand_class_name",
  "limit": 40
}
```

[PHASE ERROR] Tool 'db_distribution' is not available yet. You must call 0_plan_search_strategy first (PHASE 2) before using the execution tools.

---
