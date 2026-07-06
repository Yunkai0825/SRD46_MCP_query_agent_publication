# Q4.4 — Tool Results (batch 3)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "zinc",
  "limit": 5
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_208 | Zn^[2+] | Zn | 2 | ✓ | [Zn+2] | InChI=1S/Zn/q+2 | beta_totN_122 | ligand_totN_1169 | vlm_totN_4095 |

---

### Step 3: `search_metals`
**Args:**
```json
{
  "name": "hydrogen",
  "limit": 5
}
```

[summary]
## search_metals — 5 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_20 | BuHg^[+] | B | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_23 | BuNH_[3]^[+] | B | 1 |  | *** | *** | beta_totN_1 | ligand_totN_2 | vlm_totN_2 |
| metal_24 | C(NH_[2])_[3]^[+] | C | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_45 | Et_[2]NH_[2]^[+] | E2NH2 | 1 |  | *** | *** | beta_totN_1 | ligand_totN_1 | vlm_totN_1 |
| metal_48 | Et_[3]NH^[+] | E3NH | 1 |  | *** | *** | beta_totN_1 | ligand_totN_1 | vlm_totN_1 |

---

### Step 4: `search_ligands`
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

### Step 5: `search_ligands`
**Args:**
```json
{
  "name": "alanine",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 130 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5761 | L-2-Aminopropanoic acid (Alanine) | HL | Amino Acids | 159 | `C[C@H](N)C(=O)O` | (-inf, H2L, 2.33, HL, 9.71, L, +inf) |
| ligand_5777 | L-2-Amino-3-phenylpropanoic acid (Phenylalanine) | HL | Amino Acids | 138 | `N[C@@H](Cc1ccccc1)C(=O)O` | (-inf, H2L, 2.18, HL, 9.09, L, +inf) |
| ligand_5778 | DL-2-Amino-3-chloropropanoic ac… (3-Chloroalanine) | HL | Amino Acids | 10 | `N[C@@H](CCl)C(=O)O` | (-inf, H2L, 2, HL, 8.18, L, +inf) |
| ligand_5780 | DL-2-Amino-3-(2-fluorophenyl)propanoic acid (DL-3… | HL | Amino Acids | 6 | `N[C@@H](Cc1ccccc1F)C(=O)O` | (-inf, H2L, 2.12, HL, 9.01, L, +inf) |
| ligand_5781 | DL-2-Amino-3-(3-fluorophenyl)propanoic acid (DL-3… | HL | Amino Acids | 6 | `N[C@@H](Cc1cccc(F)c1)C(=O)O` | (-inf, H2L, 2.1, HL, 8.98, L, +inf) |

### Functional groups across all SQL matches (106 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 96 | 91% |
| primary_amine | 93 | 88% |
| amide | 81 | 76% |
| aromatic_ring | 43 | 41% |
| hydroxyl | 9 | 8% |
| secondary_amine | 8 | 8% |
| ester | 7 | 7% |
| halide | 7 | 7% |
| phenol | 5 | 5% |
| thioether | 3 | 3% |
| pyridine | 2 | 2% |
| thiol | 2 | 2% |
| ether | 1 | 1% |
| tertiary_amine | 1 | 1% |

---

### Step 6: `search_ligands`
**Args:**
```json
{
  "name": "serine",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 22 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5809 | L-2-Amino-3-phosphopropanoic acid (Phosphoserine) | H3L | Amino Acids | 52 | `N[C@@H](COP(=O)(O)O)C(=O)O` | (-inf, H4L, -0.7, H3L, 2.14, H2L, 5.7, HL, 9.8, L, +inf) |
| ligand_5828 | L-2-Amino-3-hydroxypropanoic acid (Serine) | HL | Amino Acids | 139 | `N[C@@H](CO)C(=O)O` | (-inf, H2L, 2.16, HL, 9.05, L, +inf) |
| ligand_5831 | erythro-2-Amino-3-hydroxy-… (erythro-Phenylserine) | HL | Amino Acids | 22 | `NC(C(=O)O)C(O)c1ccccc1` | (-inf, H2L, -1.9, HL, 8.7, L, +inf) |
| ligand_5832 | threo-2-Amino-3-hydroxy-3-ph… (threo-Phenylserine) | HL | Amino Acids | 13 | `NC(C(=O)O)C(O)c1ccccc1` | (-inf, H2L, -1.9, HL, 8.87, L, +inf) |
| ligand_5833 | L-2-Amino-4-hydroxybutanoic acid (Homoserine) | HL | Amino Acids | 31 | `N[C@@H](CCO)C(=O)O` | (-inf, H2L, 2.24, HL, 9.28, L, +inf) |

### Functional groups across all SQL matches (15 parseable SMILES)

| group | count | % |
|-------|-------|---|
| primary_amine | 15 | 100% |
| hydroxyl | 12 | 80% |
| carboxyl | 10 | 67% |
| amide | 6 | 40% |
| aromatic_ring | 4 | 27% |
| phosphate | 3 | 20% |
| ester | 2 | 13% |
| ether | 1 | 7% |

---

### Step 7: `search_ligands`
**Args:**
```json
{
  "name": "threonine",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 6 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5811 | L-2-Amino-3-phosphobutanoic ac… (Phosphothreonine) | H4L | Amino Acids | 3 | `C[C@@H](OP(=O)(O)O)[C@H](N)C(=O)O` | (-inf, H3L, 2.25, H2L, 5.83, HL, 9.67, L, +inf) |
| ligand_5829 | L-2-Amino-3-hydroxybutanoic acid (Threonine) | HL | Amino Acids | 117 | `C[C@@H](O)[C@H](N)C(=O)O` | (-inf, H2L, 2.2, HL, 8.94, L, +inf) |
| ligand_5830 | allo-L-2-Amino-3-hydroxybutano… (L-allo-Threonine) | HL | Amino Acids | 31 | `C[C@H](O)[C@H](N)C(=O)O` | (-inf, H2L, 2.11, HL, 8.92, L, +inf) |
| ligand_6394 | Glycyl-L-threonine | HL | Peptides | 14 | `C[C@@H](O)[C@H](NC(=O)CN)C(=O)O` | (-inf, H2L, 3, HL, 8.14, L, +inf) |
| ligand_6995 | DL-2-Amino-3-hydroxybu… (Threoninehydroxamic acid) | HL | Aliphatic amines | 26 | `C[C@@H](O)[C@H](N)C(=O)NO` | (-inf, H2L, 6.92, HL, 8.89, L, +inf) |

### Functional groups across all SQL matches (5 parseable SMILES)

| group | count | % |
|-------|-------|---|
| hydroxyl | 5 | 100% |
| primary_amine | 5 | 100% |
| carboxyl | 4 | 80% |
| amide | 2 | 40% |
| phosphate | 1 | 20% |

---

### Step 8: `search_ligands`
**Args:**
```json
{
  "name": "valine",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 25 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5763 | DL-2-Aminopentanoic acid (Norvaline) | HL | Amino Acids | 35 | `CCC[C@H](N)C(=O)O` | (-inf, H2L, 2.31, HL, 9.65, L, +inf) |
| ligand_5765 | L-2-Amino-3-methylbutanoic acid (Valine) | HL | Amino Acids | 81 | `CC(C)[C@H](N)C(=O)O` | (-inf, H2L, 2.27, HL, 9.52, L, +inf) |
| ligand_6378 | Glycyl-DL-norvaline | HL | Peptides | 6 | `CCCC(NC(=O)CN)C(=O)O` | (-inf, H2L, 3.17, HL, 8.22, L, +inf) |
| ligand_6380 | Glycyl-L-valine | HL | Peptides | 19 | `CC(C)[C@H](NC(=O)CN)C(=O)O` | (-inf, H2L, 3.14, HL, 8.14, L, +inf) |
| ligand_6446 | L-Valyl-L-valine | HL | Peptides | 17 | `CC(C)[C@H](N)C(=O)N[C@H](C(=O)O)C(C)C` | (-inf, H2L, 3.4, HL, 7.96, L, +inf) |

### Functional groups across all SQL matches (14 parseable SMILES)

| group | count | % |
|-------|-------|---|
| primary_amine | 14 | 100% |
| carboxyl | 10 | 71% |
| amide | 9 | 64% |
| ester | 3 | 21% |
| aromatic_ring | 2 | 14% |
| thioether | 2 | 14% |
| hydroxyl | 1 | 7% |

---

### Step 9: `search_ligands`
**Args:**
```json
{
  "name": "leucine",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 45 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5764 | DL-2-Aminohexanoic acid (Norleucine) | HL | Amino Acids | 33 | `CCCC[C@H](N)C(=O)O` | (-inf, H2L, 2.31, HL, 9.68, L, +inf) |
| ligand_5766 | L-2-Amino-4-methylpentanoic acid (Leucine) | HL | Amino Acids | 49 | `CC(C)C[C@H](N)C(=O)O` | (-inf, H2L, 2.32, HL, 9.58, L, +inf) |
| ligand_5767 | L-2-Amino-3-methylpentanoic acid (Isoleucine) | HL | Amino Acids | 51 | `CC[C@H](C)[C@H](N)C(=O)O` | (-inf, H2L, 2.26, HL, 9.6, L, +inf) |
| ligand_5768 | D-allo-2-Amino-3-methylpentan… (D-allo-Isoleucine) | HL | Amino Acids | 16 | `CC[C@H](C)[C@@H](N)C(=O)O` | (-inf, H2L, 2.2, HL, 9.62, L, +inf) |
| ligand_5773 | 1-Aminocyclopentanecarboxylic acid (Cycloleucine) | HL | Amino Acids | 11 | `NC1(C(=O)O)CCCC1` | (-inf, H2L, 2.4, HL, 10.31, L, +inf) |

### Functional groups across all SQL matches (39 parseable SMILES)

| group | count | % |
|-------|-------|---|
| primary_amine | 37 | 95% |
| amide | 29 | 74% |
| carboxyl | 29 | 74% |
| hydroxyl | 9 | 23% |
| aromatic_ring | 4 | 10% |
| ester | 4 | 10% |
| secondary_amine | 3 | 8% |
| phenol | 2 | 5% |
| phosphate | 2 | 5% |

---

### Step 10: `search_ligands`
**Args:**
```json
{
  "name": "isoleucine",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 7 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5767 | L-2-Amino-3-methylpentanoic acid (Isoleucine) | HL | Amino Acids | 51 | `CC[C@H](C)[C@H](N)C(=O)O` | (-inf, H2L, 2.26, HL, 9.6, L, +inf) |
| ligand_5768 | D-allo-2-Amino-3-methylpentan… (D-allo-Isoleucine) | HL | Amino Acids | 16 | `CC[C@H](C)[C@@H](N)C(=O)O` | (-inf, H2L, 2.2, HL, 9.62, L, +inf) |
| ligand_6384 | Glycyl-L-isoleucine | HL | Peptides | 4 | `CC[C@H](C)[C@H](NC(=O)CN)C(=O)O` | (-inf, H2L, 3, HL, 8.15, L, +inf) |
| ligand_6457 | L-Leucyl-L-isoleucine | HL | Peptides | 11 | `CC[C@H](C)[C@H](NC(=O)[C@@H](N)CC(C)C)C(=O)O` | (-inf, H2L, 3.42, HL, 7.78, L, +inf) |
| ligand_6458 | D-Leucyl-L-isoleucine | HL | Peptides | 11 | `CC[C@H](C)[C@H](NC(=O)[C@H](N)CC(C)C)C(=O)O` | (-inf, H2L, 3.06, HL, 8.09, L, +inf) |

### Functional groups across all SQL matches (7 parseable SMILES)

| group | count | % |
|-------|-------|---|
| primary_amine | 7 | 100% |
| carboxyl | 5 | 71% |
| amide | 4 | 57% |
| ester | 1 | 14% |
| hydroxyl | 1 | 14% |

---

### Step 11: `search_ligands`
**Args:**
```json
{
  "name": "aspartic acid",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 22 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5802 | L-Aminobutanedioic acid (Aspartic acid) | H2L | Amino Acids | 174 | `N[C@@H](CC(=O)O)C(=O)O` | (-inf, H3L, 1.95, H2L, 3.71, HL, 9.66, L, +inf) |
| ligand_5803 | DL-2-Amino-3-methylbutane… (3-Methylaspartic acid) | H2L | Amino Acids | 6 | `CC(C(=O)O)[C@H](N)C(=O)O` | (-inf, H3L, 1.99, H2L, 3.59, HL, 9.48, L, +inf) |
| ligand_6389 | Glycyl-L-aspartic acid | H2L | Peptides | 34 | `NCC(=O)N[C@@H](CC(=O)O)C(=O)O` | (-inf, H3L, 2.8, H2L, 4.3, HL, 8.34, L, +inf) |
| ligand_6561 | L-Aspartyl-L-aspartyl-L-aspartic acid | *** | tripeptides | 10 | *** | (-inf, H5L, -1.8, H4L, 2.04, H3L, 3.87, H2L, 4.78, HL, 8.13, L, +inf) |
| ligand_6585 | L-Arginyl-L-lysyl-L-aspartic acid | *** | tripeptides | 11 | *** | (-inf, H4L, 2.77, H3L, 4.2, H2L, 7.44, HL, 10.49, L, +inf) |

### Functional groups across all SQL matches (8 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 8 | 100% |
| primary_amine | 7 | 88% |
| amide | 5 | 62% |
| secondary_amine | 2 | 25% |
| aromatic_ring | 1 | 12% |
| imine | 1 | 12% |

---

### Step 12: `search_ligands`
**Args:**
```json
{
  "name": "glutamic acid",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 23 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5804 | L-2-Aminopentanedioic acid (Glutamic acid) | H2L | Amino Acids | 94 | `N[C@@H](CCC(=O)O)C(=O)O` | (-inf, H3L, 2.16, H2L, 4.15, HL, 9.58, L, +inf) |
| ligand_5805 | DL-2-Amino-2-methylpentan… (2-Methylglutamic acid) | H2L | Amino Acids | 4 | `C[C@](N)(CCC(=O)O)C(=O)O` | (-inf, H2L, 4.05, HL, 9.72, L, +inf) |
| ligand_5807 | DL-2-Amino-3-hydroxypent… (3-Hydroxyglutamic acid) | H2L | Amino Acids | 8 | `N[C@H](C(=O)O)C(O)CC(=O)O` | (-inf, H3L, 2.09, H2L, 4.08, HL, 9.06, L, +inf) |
| ligand_6390 | Glycyl-L-glutamic acid | H2L | Peptides | 25 | `NCC(=O)N[C@@H](CCC(=O)O)C(=O)O` | (-inf, H3L, 2.83, H2L, 4.34, HL, 8.3, L, +inf) |
| ligand_6485 | L-Tyrosyl-L-glutamic acid | H3L | Peptides | 11 | `N[C@@H](Cc1ccc(O)cc1)C(=O)N[C@@H](CCC(=O)O)C(=O)O` | (-inf, H4L, 3.17, H3L, 4.48, H2L, 7.69, HL, 10.09, L, +inf) |

### Functional groups across all SQL matches (17 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 15 | 88% |
| amide | 12 | 71% |
| primary_amine | 11 | 65% |
| aromatic_ring | 5 | 29% |
| hydroxyl | 5 | 29% |
| ester | 2 | 12% |
| phenol | 2 | 12% |
| phosphate | 1 | 6% |
| tertiary_amine | 1 | 6% |

---

### Step 13: `search_ligands`
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

### Step 14: `search_ligands`
**Args:**
```json
{
  "name": "lysine",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 25 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5845 | L-2-Amino-6-(2-methylpropamido)hexanoic acid (N(6… | HL | Amino Acids | 30 | `CC(C)C(=O)NCCCCC(N)C(=O)O` | (-inf, H2L, 2.4, HL, 9.42, L, +inf) |
| ligand_5846 | L-6-Amino-2-acetamidohexanoic acid (N(2)-Acetyl-L… | HL | Amino Acids | 1 | `CC(=O)N[C@@H](CCCCN)C(=O)O` | *** |
| ligand_5847 | L-2-Amino-6-acetamidohexanoic acid (N(6)-Acetyl-L… | HL | Amino Acids | 7 | `CC(=O)NCCCCC(N)C(=O)O` | (-inf, H2L, 2.13, HL, 9.52, L, +inf) |
| ligand_5849 | N(6)-d-Biotinyl-L-lysine (d-Biocytin) | HL | Amino Acids | 7 | `NC(CCCCNC(=O)CCCCC1SCC2NC(=O)NC21)C(=O)O` | (-inf, H2L, 2.26, HL, 9.29, L, +inf) |
| ligand_5887 | L-2,6-Diaminohexanoic acid (Lysine) | HL | Amino Acids | 98 | `NCCCC[C@H](N)C(=O)O` | (-inf, H3L, 2.15, H2L, 9.15, HL, 10.66, L, +inf) |

### Functional groups across all SQL matches (20 parseable SMILES)

| group | count | % |
|-------|-------|---|
| primary_amine | 20 | 100% |
| amide | 18 | 90% |
| carboxyl | 18 | 90% |
| hydroxyl | 4 | 20% |
| aromatic_ring | 3 | 15% |
| ester | 1 | 5% |
| phenol | 1 | 5% |
| phosphate | 1 | 5% |
| thioether | 1 | 5% |

---

### Step 15: `search_ligands`
**Args:**
```json
{
  "name": "arginine",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 8 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5917 | L-2-Amino-5-guanidopentanoic acid (Arginine) | H2L | Amino Acids | 45 | `N=C(N)NCCC[C@H](N)C(=O)O` | (-inf, H3L, 2.03, H2L, 9, HL, 9, L, +inf) |
| ligand_6432 | L-Alanyl-L-arginine | HL | Peptides | 6 | `C[C@H](N)C(=O)N[C@@H](CCCNC(=N)N)C(=O)O` | (-inf, H2L, 2.99, HL, 7.95, L, +inf) |
| ligand_6487 | L-Tyrosyl-L-arginine | H2L | Peptides | 9 | `N=C(N)NCCC[C@H](NC(=O)[C@@H](N)Cc1ccc(O)cc1)C(=O)O` | (-inf, H3L, 3.09, H2L, 7.24, HL, 9.82, L, +inf) |
| ligand_6488 | L-Tyrosyl-D-arginine | H2L | Peptides | 9 | `N=C(N)NCCC[C@@H](NC(=O)[C@@H](N)Cc1ccc(O)cc1)C(=O)O` | (-inf, H3L, 2.81, H2L, 7.62, HL, 9.82, L, +inf) |
| ligand_6692 | L-Alanyl-L-aspartyl-L-serylgly… (fibrinopeptide A) | *** | polypeptides | 12 | *** | (-inf, H6L, 2.6, H5L, 3.5, H4L, 3.62, H3L, 4.31, H2L, 5.03, HL, 8.4, L, +inf) |

### Functional groups across all SQL matches (5 parseable SMILES)

| group | count | % |
|-------|-------|---|
| imine | 5 | 100% |
| primary_amine | 5 | 100% |
| secondary_amine | 5 | 100% |
| amide | 4 | 80% |
| carboxyl | 4 | 80% |
| hydroxyl | 3 | 60% |
| aromatic_ring | 2 | 40% |
| phenol | 2 | 40% |

---

### Step 16: `search_ligands`
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

### Step 17: `search_ligands`
**Args:**
```json
{
  "name": "methionine",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 22 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5863 | L-2-Amino-4-(methylthio)butanoic acid (Methionine) | HL | Amino Acids | 63 | `CSCC[C@H](N)C(=O)O` | (-inf, H2L, 2.18, HL, 9.08, L, +inf) |
| ligand_6192 | N,N,S-Tris(carboxymethyl)methionine | H4L | NTA and derivatives | 4 | `C[S+](CC[C@@H](C(=O)O)N(CC(=O)O)CC(=O)O)CC(=O)O` | (-inf, H4L, 2.1, H3L, 2.6, H2L, 7.49, HL, 7.49, L, +inf) |
| ligand_6399 | Glycyl-L-methionine | HL | Peptides | 26 | `CSCC[C@H](NC(=O)CN)C(=O)O` | (-inf, H2L, 3.02, HL, 8.12, L, +inf) |
| ligand_6475 | L-Phenylalanyl-L-methionine | HL | Peptides | 12 | `CSCC[C@H](NC(=O)[C@@H](N)Cc1ccccc1)C(=O)O` | (-inf, H2L, 3.24, HL, 7.27, L, +inf) |
| ligand_6519 | L-S-Methylcysteinyl-L-methionine | HL | Peptides | 9 | `CSCC[C@H](NC(=O)[C@@H](N)CSC)C(=O)O` | (-inf, H2L, 3.18, HL, 7.03, L, +inf) |

### Functional groups across all SQL matches (13 parseable SMILES)

| group | count | % |
|-------|-------|---|
| primary_amine | 12 | 92% |
| thioether | 12 | 92% |
| amide | 9 | 69% |
| carboxyl | 9 | 69% |
| aromatic_ring | 3 | 23% |
| ester | 1 | 8% |
| secondary_amine | 1 | 8% |
| tertiary_amine | 1 | 8% |

---

### Step 18: `search_ligands`
**Args:**
```json
{
  "name": "tyrosine",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 37 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5817 | DL-2-Amino-3-(2-hydroxyphenyl)propan… (o-Tyrosine) | H2L | Amino Acids | 71 | `NC(Cc1ccccc1O)C(=O)O` | (-inf, H3L, 2.41, H2L, 8.67, HL, 11.01, L, +inf) |
| ligand_5818 | DL-2-Amino-3-(3-hydroxyphenyl)propan… (m-Tyrosine) | H2L | Amino Acids | 86 | `N[C@@H](Cc1cccc(O)c1)C(=O)O` | (-inf, H3L, 2.22, H2L, 8.95, HL, 10.04, L, +inf) |
| ligand_5819 | L-2-Amino-3-(4-hydroxyphenyl)propanoic… (Tyrosine) | H2L | Amino Acids | 107 | `N[C@@H](Cc1ccc(O)cc1)C(=O)O` | (-inf, H3L, 2.24, H2L, 9.04, HL, 10.1, L, +inf) |
| ligand_5820 | L-2-Amino-2-methyl-3-(4-hydrox… (L-Methyltyrosine) | H2L | Amino Acids | 7 | `CC(N)(Cc1ccc(O)cc1)C(=O)O` | (-inf, H3L, 2.16, H2L, 9.14, HL, 10.24, L, +inf) |
| ligand_5821 | L-2-Amino-3-(4-hydroxy-3,5… (L-3,5-Diiodotyrosine) | H2L | Amino Acids | 3 | `N[C@@H](Cc1cc(I)c(O)c(I)c1)C(=O)O` | (-inf, H2L, 6.16, HL, 9.1, L, +inf) |

### Functional groups across all SQL matches (30 parseable SMILES)

| group | count | % |
|-------|-------|---|
| aromatic_ring | 30 | 100% |
| hydroxyl | 29 | 97% |
| phenol | 29 | 97% |
| primary_amine | 25 | 83% |
| carboxyl | 24 | 80% |
| amide | 20 | 67% |
| ester | 4 | 13% |
| halide | 2 | 7% |
| aldehyde | 1 | 3% |

---

### Step 19: `search_ligands`
**Args:**
```json
{
  "name": "phenylalanine",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 37 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5777 | L-2-Amino-3-phenylpropanoic acid (Phenylalanine) | HL | Amino Acids | 138 | `N[C@@H](Cc1ccccc1)C(=O)O` | (-inf, H2L, 2.18, HL, 9.09, L, +inf) |
| ligand_5854 | L-2-Amino-3-(4-methoxyph… (4-Methoxyphenylalanine) | HL | Amino Acids | 5 | `COc1ccc(C[C@H](N)C(=O)O)cc1` | (-inf, HL, -9.15, L, +inf) |
| ligand_5855 | DL-2-Amino-3-(3,4-di… (3,4-Dimethoxyphenylalanine) | HL | Amino Acids | 2 | `COc1ccc(C[C@H](N)C(=O)O)cc1OC` | (-inf, H2L, 2.37, HL, 9.02, L, +inf) |
| ligand_6385 | Glycyl-L-phenylalanine | HL | Peptides | 34 | `NCC(=O)N[C@@H](Cc1ccccc1)C(=O)O` | (-inf, H2L, 2.99, HL, 8.09, L, +inf) |
| ligand_6429 | L-Alanyl-L-phenylalanine | HL | Peptides | 13 | `C[C@H](N)C(=O)N[C@@H](Cc1ccccc1)C(=O)O` | (-inf, H2L, 3.2, HL, 7.9, L, +inf) |

### Functional groups across all SQL matches (29 parseable SMILES)

| group | count | % |
|-------|-------|---|
| aromatic_ring | 29 | 100% |
| carboxyl | 26 | 90% |
| primary_amine | 26 | 90% |
| amide | 24 | 83% |
| hydroxyl | 4 | 14% |
| ester | 3 | 10% |
| phenol | 3 | 10% |
| secondary_amine | 2 | 7% |
| thioether | 2 | 7% |

---

### Step 20: `search_ligands`
**Args:**
```json
{
  "name": "tryptophan",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 9 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5907 | L-2-Amino-3-(3-indolyl)propanoic acid (Tryptophan) | HL | Amino Acids | 107 | `N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O` | (-inf, H2L, 2.37, HL, 9.33, L, +inf) |
| ligand_5945 | L-N-Acetyltryptophan | HL | Amino Acids | 7 | `CC(=O)N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O` | (-inf, HL, 3.23, L, +inf) |
| ligand_6495 | L-Tyrosyl-L-tryptophan | H2L | Peptides | 9 | `N[C@@H](Cc1ccc(O)cc1)C(=O)N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O` | (-inf, H3L, 3.51, H2L, 7.37, HL, 9.91, L, +inf) |
| ligand_6496 | L-Tyrosyl-D-tryptophan | H2L | Peptides | 9 | `N[C@@H](Cc1ccc(O)cc1)C(=O)N[C@H](Cc1c[nH]c2ccccc12)C(=O)O` | (-inf, H3L, 3.28, H2L, 7.91, HL, 10.05, L, +inf) |
| ligand_6690 | L-Pyroglutamyl-L-hystidyl-L-tryptophanyl-L… (LHRH) | *** | polypeptides | 4 | *** | (-inf, H2L, 6.19, HL, 9.6, L, +inf) |

### Functional groups across all SQL matches (6 parseable SMILES)

| group | count | % |
|-------|-------|---|
| aromatic_ring | 6 | 100% |
| primary_amine | 5 | 83% |
| amide | 4 | 67% |
| carboxyl | 4 | 67% |
| hydroxyl | 3 | 50% |
| phenol | 2 | 33% |
| ester | 1 | 17% |

---

### Step 21: `search_ligands`
**Args:**
```json
{
  "name": "proline",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 28 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5930 | L-Pyrrolidine-2-carboxylic acid (L-Proline) | HL | Amino Acids | 66 | `O=C(O)C1CCCN1` | (-inf, H2L, 1.89, HL, 10.46, L, +inf) |
| ligand_5935 | S-(1-Carboxy-3-phenylpropyl)-L-alan… (Enalaprilat) | H2L | Amino Acids | 15 | `C[C@H](N[C@@H](CCc1ccccc1)C(=O)O)C(=O)N1CCC[C@H]1C(=O)O` | (-inf, H3L, -1.6, H2L, 3.26, HL, 7.54, L, +inf) |
| ligand_5941 | L-4-Hydroxypyrrolidine-2-carbo… (L-Hydroxyproline) | HL | Amino Acids | 46 | `O=C(O)C1CC(O)CN1` | (-inf, H2L, 1.77, HL, 9.47, L, +inf) |
| ligand_5942 | DL-1,3-Thiazolidine-4-carboxylic… (DL-Thiaproline) | HL | Amino Acids | 22 | `O=C(O)C1CSCN1` | (-inf, H2L, -1.5, HL, -1.5, L, +inf) |
| ligand_6018 | L-N-Benzylproline | HL | Amino Acids | 15 | `O=C(O)[C@@H]1CCCN1Cc1ccccc1` | (-inf, H2L, 1.97, HL, 9.93, L, +inf) |

### Functional groups across all SQL matches (15 parseable SMILES)

| group | count | % |
|-------|-------|---|
| amide | 11 | 73% |
| carboxyl | 11 | 73% |
| primary_amine | 6 | 40% |
| aromatic_ring | 5 | 33% |
| hydroxyl | 4 | 27% |
| secondary_amine | 4 | 27% |
| imine | 2 | 13% |
| phenol | 2 | 13% |
| pyridine | 1 | 7% |
| tertiary_amine | 1 | 7% |
| thioether | 1 | 7% |

---

### Step 22: `search_ligands`
**Args:**
```json
{
  "name": "asparagine",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 6 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5816 | D-3-Amino-3-carboxyp… (Asparagine hydroxamic acid) | H2L | Amino Acids | 17 | `NC(CC(=O)NO)C(=O)O` | (-inf, H3L, 2.18, H2L, 8.15, HL, 9.37, L, +inf) |
| ligand_5843 | L-2-Aminobutanedioic acid 4-amide (Asparagine) | HL | Amino Acids | 92 | `NC(=O)C[C@H](N)C(=O)O` | (-inf, H2L, 2.16, HL, 8.73, L, +inf) |
| ligand_6396 | Glycyl-L-asparagine | HL | Peptides | 40 | `NCC(=O)N[C@@H](CC(N)=O)C(=O)O` | (-inf, H2L, 3.12, HL, 8.12, L, +inf) |
| ligand_6689 | L-Pyroglutamyl-L-alanyl-L-lysyl-L-sery… (Thymulin) | *** | polypeptides | 4 | *** | (-inf, H2L, 3.23, HL, 9.7, L, +inf) |
| ligand_10210 | L-Isoasparagine | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (3 parseable SMILES)

| group | count | % |
|-------|-------|---|
| amide | 3 | 100% |
| carboxyl | 3 | 100% |
| primary_amine | 3 | 100% |
| hydroxyl | 1 | 33% |

---

### Step 23: `search_ligands`
**Args:**
```json
{
  "name": "glutamine",
  "limit": 5
}
```

[summary]
## search_ligands — 3 result(s)

**stats:** 3 SQL matches · showing 3 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5844 | L-2-Aminopentanedioic acid 5-amide (Glutamine) | HL | Amino Acids | 71 | `NC(=O)CC[C@H](N)C(=O)O` | (-inf, H2L, 2.19, HL, 9, L, +inf) |
| ligand_6663 | Glycyl-L-prolylglycyl-L-prolyl-L-glutamine | *** | polypeptides | 4 | *** | (-inf, H2L, 3.22, HL, 8.29, L, +inf) |
| ligand_6668 | L-Arginyl-L-prolyl-L-lysyl-L-prolyl-L-glutamine | *** | polypeptides | 5 | *** | (-inf, H3L, 4, H2L, 7.27, HL, 9.85, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| amide | 1 | 100% |
| carboxyl | 1 | 100% |
| primary_amine | 1 | 100% |

---

### Step 25: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_208",
  "ligand_id": "ligand_5760"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 4 species

### Zn^[2+] + Aminoacetic acid (Glycine)
**metal_id:** metal_208 | **ligand_id:** ligand_5760 | **ligand_def_HxL:** HL  
**entries:** 37 | **species:** 4 | **vlm_count:** 37

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 12 |
| beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | [M] + [L]^2 <=> [ML2] | [ML2](aqueous), [M](aqueous), [L](aqueous) | 13 |
| beta_def_872 | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | [M] + [L]^3 <=> [ML3] | [ML3](aqueous), [M](aqueous), [L](aqueous) | 11 |
| beta_def_966 | [ML]/[M(OH)L][H] | [M(OH)L] + [H] <=> [ML] + [H2O] | [ML](aqueous), [H2O](aqueous), [M(OH)L](aqueous), [H](aqueous) | 1 |

**vlm_ids:** vlm_93924, vlm_93925, vlm_93926, vlm_93927, vlm_93928, … vlm_93958, vlm_93959, vlm_93960 (37 listed)

**equilibrium_maps:** 7 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_112 | 3 | 3 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_113 | 4 | 4 | 31~41 °C | 0~0.3 M |
| ref_eq_net_114 | 3 | 3 | 19~29 °C | 0.35~0.65 M |
| ref_eq_net_115 | 3 | 3 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_116 | 3 | 3 | 5~15 °C | -0.15~0.15 M |
| ref_eq_net_117 | 3 | 3 | 19~29 °C | -0.15~0.15 M |
| ref_eq_net_118 | 3 | 3 | 35~45 °C | -0.15~0.15 M |

---

### Step 27: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND c.ligand_id IN (ligand_5760, ligand_5761, ligand_5828, ligand_5829, ligand_5765, ligand_5766, ligand_5767, ligand_5802, ligand_5804, ligand_5898, ligand_5887, ligand_5917, ligand_5856, ligand_5863, ligand_5819, ligand_5777, ligand_5907, ligand_5930, ligand_5843, ligand_5844) AND (s.solvent_name LIKE '%water%' OR s.solvent_name LIKE '%aqueous%'))",
  "order_by": "c.ligand_id ASC, s.constant_type ASC",
  "limit": 500
}
```

[summary]
## search_stability

*(no results)*

---

### Step 28: `search_pka_values`
**Args:**
```json
{
  "where": "(lc.ligand_id IN (ligand_5856, ligand_5898, ligand_5802, ligand_5804, ligand_5819, ligand_5887) AND (p.solvent_name LIKE '%water%' OR p.solvent_name LIKE '%aqueous%') AND (p.temperature_c BETWEEN 20 AND 30) AND (p.ionic_strength_mol_l IS NULL OR p.ionic_strength_mol_l <= 0.2))",
  "order_by": "lc.ligand_id ASC, p.pKa_type ASC",
  "limit": 200
}
```

[summary]
## search_pka_values

*(no results)*

---

### Step 29: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND c.ligand_id = ligand_5760 AND (s.solvent_name LIKE '%water%' OR s.solvent_name LIKE '%aqueous%') AND (s.temperature_c BETWEEN 20 AND 30 OR s.temperature_c IS NULL) AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2))",
  "order_by": "s.constant_type ASC, s.constant_value DESC",
  "limit": 50
}
```

[summary]
## search_stability

*(no results)*

---
