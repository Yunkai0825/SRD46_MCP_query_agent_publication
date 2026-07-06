# Q3.1.2 — Tool Results (batch 2)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "copper"
}
```

[summary]
## search_metals — 3 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_41 | Cu^[2+] | Cu | 2 | ✓ | [Cu+2] | InChI=1S/Cu/q+2 | beta_totN_264 | ligand_totN_1951 | vlm_totN_8963 |
| metal_42 | Cu^[+] | Cu | 1 | ✓ | [Cu+] | InChI=1S/Cu/q+1 | beta_totN_32 | ligand_totN_117 | vlm_totN_285 |
| metal_43 | Cu^[3+] | Cu | 3 | ✓ | [Cu+3] | InChI=1S/Cu/q+3 | beta_totN_4 | ligand_totN_8 | vlm_totN_10 |

---

### Step 3: `search_metals`
**Args:**
```json
{
  "name": "nickel"
}
```

[summary]
## search_metals — 2 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_112 | Ni^[2+] | Ni | 2 | ✓ | [Ni+2] | InChI=1S/Ni/q+2 | beta_totN_149 | ligand_totN_1369 | vlm_totN_5325 |
| metal_113 | Ni^[3+] | Ni | 3 | ✓ | [Ni+3] | InChI=1S/Ni/q+3 | beta_totN_5 | ligand_totN_4 | vlm_totN_7 |

---

### Step 4: `search_ligands`
**Args:**
```json
{
  "ligand_class": "amino acid",
  "limit": 30
}
```

[summary]
## search_ligands — 30 result(s)

**stats:** 297 SQL matches · showing 30 · limit 30

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5760 | Aminoacetic acid (Glycine) | HL | Amino Acids | 428 | `NCC(=O)O` | (-inf, H2L, 2.33, HL, 9.57, L, +inf) |
| ligand_5761 | L-2-Aminopropanoic acid (Alanine) | HL | Amino Acids | 159 | `C[C@H](N)C(=O)O` | (-inf, H2L, 2.33, HL, 9.71, L, +inf) |
| ligand_5762 | DL-2-Aminobutanoic acid | HL | Amino Acids | 53 | `CCC(N)C(=O)O` | (-inf, H2L, 2.3, HL, 9.63, L, +inf) |
| ligand_5763 | DL-2-Aminopentanoic acid (Norvaline) | HL | Amino Acids | 35 | `CCC[C@H](N)C(=O)O` | (-inf, H2L, 2.31, HL, 9.65, L, +inf) |
| ligand_5764 | DL-2-Aminohexanoic acid (Norleucine) | HL | Amino Acids | 33 | `CCCC[C@H](N)C(=O)O` | (-inf, H2L, 2.31, HL, 9.68, L, +inf) |
| ligand_5765 | L-2-Amino-3-methylbutanoic acid (Valine) | HL | Amino Acids | 81 | `CC(C)[C@H](N)C(=O)O` | (-inf, H2L, 2.27, HL, 9.52, L, +inf) |
| ligand_5766 | L-2-Amino-4-methylpentanoic acid (Leucine) | HL | Amino Acids | 49 | `CC(C)C[C@H](N)C(=O)O` | (-inf, H2L, 2.32, HL, 9.58, L, +inf) |
| ligand_5767 | L-2-Amino-3-methylpentanoic acid (Isoleucine) | HL | Amino Acids | 51 | `CC[C@H](C)[C@H](N)C(=O)O` | (-inf, H2L, 2.26, HL, 9.6, L, +inf) |
| ligand_5768 | D-allo-2-Amino-3-methylpentan… (D-allo-Isoleucine) | HL | Amino Acids | 16 | `CC[C@H](C)[C@@H](N)C(=O)O` | (-inf, H2L, 2.2, HL, 9.62, L, +inf) |
| ligand_5769 | 2-Amino-2-methylpropanoi… (2-Aminoisobutyric acid) | HL | Amino Acids | 41 | `CC(C)(N)C(=O)O` | (-inf, H2L, 2.34, HL, 10.1, L, +inf) |
| ligand_5770 | DL-2-Amino-4-pentenoic acid | HL | Amino Acids | 18 | `C=CCC(N)C(=O)O` | (-inf, H2L, 2.13, HL, 9.28, L, +inf) |
| ligand_5771 | DL-2-Amino-5-hexenoic acid | HL | Amino Acids | 15 | `C=CCCC(N)C(=O)O` | (-inf, H2L, 2.25, HL, 9.43, L, +inf) |
| ligand_5772 | DL-2-Amino-6-heptenoic acid | HL | Amino Acids | 15 | `C=CCCCC(N)C(=O)O` | (-inf, H2L, 2.34, HL, 9.52, L, +inf) |
| ligand_5773 | 1-Aminocyclopentanecarboxylic acid (Cycloleucine) | HL | Amino Acids | 11 | `NC1(C(=O)O)CCCC1` | (-inf, H2L, 2.4, HL, 10.31, L, +inf) |
| ligand_5774 | 1-Aminocyclohexanecarboxylic acid | HL | Amino Acids | 11 | `NC1(C(=O)O)CCCCC1` | (-inf, H2L, 2.41, HL, 10.13, L, +inf) |
| ligand_5775 | 1-Aminocycloheptanecarboxylic acid | HL | Amino Acids | 11 | `NC1(C(=O)O)CCCCCC1` | (-inf, H2L, 2.59, HL, 10.46, L, +inf) |
| ligand_5776 | DL-Aminophenylacetic acid (Phenylglycine) | HL | Amino Acids | 12 | `NC(C(=O)O)c1ccccc1` | (-inf, H2L, -1.9, HL, 8.92, L, +inf) |
| ligand_5777 | L-2-Amino-3-phenylpropanoic acid (Phenylalanine) | HL | Amino Acids | 138 | `N[C@@H](Cc1ccccc1)C(=O)O` | (-inf, H2L, 2.18, HL, 9.09, L, +inf) |
| ligand_5778 | DL-2-Amino-3-chloropropanoic ac… (3-Chloroalanine) | HL | Amino Acids | 10 | `N[C@@H](CCl)C(=O)O` | (-inf, H2L, 2, HL, 8.18, L, +inf) |
| ligand_5779 | DL-2-Amino-3-chlorobutanoic acid | HL | Amino Acids | 8 | `CC(Cl)C(N)C(=O)O` | (-inf, H2L, -1.5, HL, 8.07, L, +inf) |
| ligand_5780 | DL-2-Amino-3-(2-fluorophenyl)propanoic acid (DL-3… | HL | Amino Acids | 6 | `N[C@@H](Cc1ccccc1F)C(=O)O` | (-inf, H2L, 2.12, HL, 9.01, L, +inf) |
| ligand_5781 | DL-2-Amino-3-(3-fluorophenyl)propanoic acid (DL-3… | HL | Amino Acids | 6 | `N[C@@H](Cc1cccc(F)c1)C(=O)O` | (-inf, H2L, 2.1, HL, 8.98, L, +inf) |
| ligand_5782 | DL-2-Amino-3-(4-fluorophenyl)propanoic acid (DL-3… | HL | Amino Acids | 6 | `N[C@@H](Cc1ccc(F)cc1)C(=O)O` | (-inf, H2L, 2.13, HL, 9.05, L, +inf) |
| ligand_5783 | DL-2-Amino-3-(2-chlorophenyl)propanoic acid (DL-3… | HL | Amino Acids | 2 | `N[C@@H](Cc1ccccc1Cl)C(=O)O` | (-inf, H2L, 2.23, HL, 8.94, L, +inf) |
| ligand_5784 | DL-2-Amino-3-(3-chlorophenyl)propanoic acid (DL-3… | HL | Amino Acids | 2 | `N[C@@H](Cc1cccc(Cl)c1)C(=O)O` | (-inf, H2L, 2.17, HL, 8.91, L, +inf) |
| ligand_5785 | DL-2-Amino-3-(4-chlorophenyl)propanoic acid (DL-3… | HL | Amino Acids | 2 | `N[C@@H](Cc1ccc(Cl)cc1)C(=O)O` | (-inf, H2L, 2.08, HL, 8.96, L, +inf) |
| ligand_5786 | DL-Amino-4-sulfophenylacet… (4-Sulfophenylglycine) | H2L | Amino Acids | 12 | `NC(C(=O)O)c1ccc(S(=O)(=O)O)cc1` | (-inf, H2L, -1.8, HL, 8.66, L, +inf) |
| ligand_5787 | DL-2-Amino-4-sulfobutanoic acid (Homocysteic acid) | H2L | Amino Acids | 4 | `N[C@@H](CCS(=O)(=O)O)C(=O)O` | (-inf, H2L, 2.11, HL, 8.93, L, +inf) |
| ligand_5788 | 3-Aminopropanoic acid (beta-Alanine) | HL | Amino Acids | 111 | `NCCC(=O)O` | (-inf, H2L, 3.51, HL, 10.08, L, +inf) |
| ligand_5789 | DL-3-Aminobutanoic acid | HL | Amino Acids | 33 | `CC(N)CC(=O)O` | (-inf, H2L, 3.43, HL, 10.05, L, +inf) |

### Functional groups across all SQL matches (294 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 294 | 100% |
| primary_amine | 167 | 57% |
| aromatic_ring | 99 | 34% |
| hydroxyl | 79 | 27% |
| secondary_amine | 68 | 23% |
| tertiary_amine | 48 | 16% |
| amide | 40 | 14% |
| thioether | 26 | 9% |
| phenol | 22 | 7% |
| pyridine | 17 | 6% |
| halide | 13 | 4% |
| thiol | 11 | 4% |
| imine | 9 | 3% |
| ester | 6 | 2% |
| ether | 6 | 2% |
| phosphonate | 6 | 2% |
| phosphate | 5 | 2% |
| sulfonate | 4 | 1% |
| nitrile | 1 | 0% |

---

### Step 5: `search_ligands`
**Args:**
```json
{
  "name": "histidine",
  "ligand_class": "amino acid",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 19 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5860 | DL-2-Amino-3-(2-mercaptoimidazo-4… (Thiohistidine) | H2L | Amino Acids | 20 | `NC(Cc1cnc(S)[nH]1)C(=O)O` | (-inf, H2L, 8.59, HL, 8.59, L, +inf) |
| ligand_5898 | L-2-Amino-3-(4-imidazolyl)propanoic a… (Histidine) | HL | Amino Acids | 250 | `N[C@@H](Cc1c[nH]cn1)C(=O)O` | (-inf, H3L, -1.7, H2L, 6.05, HL, 9.1, L, +inf) |
| ligand_5899 | L-2-Amino-3-(N(1)-methyl-4-imidazolyl)propanoic a… | HL | Amino Acids | 14 | `Cn1cnc(C[C@H](N)C(=O)O)c1` | (-inf, H3L, -1.72, H2L, 5.87, HL, 9.16, L, +inf) |
| ligand_5900 | L-2-Amino-3-(N(3)-methyl-4-imidazolyl)propanoic a… | HL | Amino Acids | 16 | `Cn1cncc1C[C@H](N)C(=O)O` | (-inf, H3L, -1.65, H2L, 6.48, HL, 8.61, L, +inf) |
| ligand_5901 | L-4-(2-Amino-3-carboxypropyl)-1,3-dimethylimidazo… | HL | Amino Acids | 6 | `Cn1c[n+](C)cc1C[C@H](N)C(=O)O` | (-inf, H2L, -1.98, HL, 7.85, L, +inf) |

### Functional groups across all SQL matches (19 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 19 | 100% |
| aromatic_ring | 16 | 84% |
| primary_amine | 8 | 42% |
| amide | 5 | 26% |
| imine | 3 | 16% |
| secondary_amine | 3 | 16% |
| halide | 2 | 11% |
| ester | 1 | 5% |
| tertiary_amine | 1 | 5% |
| thiol | 1 | 5% |

---

### Step 6: `search_ligands`
**Args:**
```json
{
  "name": "cysteine",
  "ligand_class": "amino acid",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 8 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5856 | L-2-Amino-3-mercaptopropanoic acid (Cysteine) | H2L | Amino Acids | 134 | `N[C@@H](CS)C(=O)O` | (-inf, H3L, -1.9, H2L, 8.18, HL, 10.3, L, +inf) |
| ligand_5859 | DL-2-Amino-4-mercaptobutanoic acid (Homocysteine) | H2L | Amino Acids | 3 | `NC(CCS)C(=O)O` | (-inf, H3L, 2.15, H2L, 8.57, HL, 10.38, L, +inf) |
| ligand_5861 | L-2-Amino-3-(methylthio)propan… (S-Methylcysteine) | HL | Amino Acids | 39 | `CSC[C@H](N)C(=O)O` | (-inf, H2L, 2, HL, 8.74, L, +inf) |
| ligand_5862 | L-2-Amino-3-(ethylthio)propanoi… (S-Ethylcysteine) | HL | Amino Acids | 46 | `CCSC[C@H](N)C(=O)O` | (-inf, H2L, -1.9, HL, 8.65, L, +inf) |
| ligand_5871 | L-2-Amino-3-(2-Cyanoethylthio)propanoic acid (L-5… | HL | Amino Acids | 1 | `N#CCCSCC(N)C(=O)O` | (-inf, HL, 8.46, L, +inf) |

### Functional groups across all SQL matches (8 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 8 | 100% |
| primary_amine | 7 | 88% |
| thioether | 5 | 62% |
| thiol | 3 | 38% |
| ester | 1 | 12% |
| nitrile | 1 | 12% |
| secondary_amine | 1 | 12% |

---

### Step 7: `search_ligands`
**Args:**
```json
{
  "name": "aspartic acid",
  "ligand_class": "amino acid",
  "limit": 5
}
```

[summary]
## search_ligands — 2 result(s)

**stats:** 2 SQL matches · showing 2 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5802 | L-Aminobutanedioic acid (Aspartic acid) | H2L | Amino Acids | 174 | `N[C@@H](CC(=O)O)C(=O)O` | (-inf, H3L, 1.95, H2L, 3.71, HL, 9.66, L, +inf) |
| ligand_5803 | DL-2-Amino-3-methylbutane… (3-Methylaspartic acid) | H2L | Amino Acids | 6 | `CC(C(=O)O)[C@H](N)C(=O)O` | (-inf, H3L, 1.99, H2L, 3.59, HL, 9.48, L, +inf) |

### Functional groups across all SQL matches (2 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 2 | 100% |
| primary_amine | 2 | 100% |

---

### Step 8: `search_ligands`
**Args:**
```json
{
  "name": "glutamic acid",
  "ligand_class": "amino acid",
  "limit": 5
}
```

[summary]
## search_ligands — 3 result(s)

**stats:** 3 SQL matches · showing 3 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5804 | L-2-Aminopentanedioic acid (Glutamic acid) | H2L | Amino Acids | 94 | `N[C@@H](CCC(=O)O)C(=O)O` | (-inf, H3L, 2.16, H2L, 4.15, HL, 9.58, L, +inf) |
| ligand_5805 | DL-2-Amino-2-methylpentan… (2-Methylglutamic acid) | H2L | Amino Acids | 4 | `C[C@](N)(CCC(=O)O)C(=O)O` | (-inf, H2L, 4.05, HL, 9.72, L, +inf) |
| ligand_5807 | DL-2-Amino-3-hydroxypent… (3-Hydroxyglutamic acid) | H2L | Amino Acids | 8 | `N[C@H](C(=O)O)C(O)CC(=O)O` | (-inf, H3L, 2.09, H2L, 4.08, HL, 9.06, L, +inf) |

### Functional groups across all SQL matches (3 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 3 | 100% |
| primary_amine | 3 | 100% |
| hydroxyl | 1 | 33% |

---

### Step 9: `search_ligands`
**Args:**
```json
{
  "name": "methionine",
  "ligand_class": "amino acid",
  "limit": 5
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5863 | L-2-Amino-4-(methylthio)butanoic acid (Methionine) | HL | Amino Acids | 63 | `CSCC[C@H](N)C(=O)O` | (-inf, H2L, 2.18, HL, 9.08, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 1 | 100% |
| primary_amine | 1 | 100% |
| thioether | 1 | 100% |

---

### Step 10: `search_ligands`
**Args:**
```json
{
  "name": "serine",
  "ligand_class": "amino acid",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 7 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5809 | L-2-Amino-3-phosphopropanoic acid (Phosphoserine) | H3L | Amino Acids | 52 | `N[C@@H](COP(=O)(O)O)C(=O)O` | (-inf, H4L, -0.7, H3L, 2.14, H2L, 5.7, HL, 9.8, L, +inf) |
| ligand_5828 | L-2-Amino-3-hydroxypropanoic acid (Serine) | HL | Amino Acids | 139 | `N[C@@H](CO)C(=O)O` | (-inf, H2L, 2.16, HL, 9.05, L, +inf) |
| ligand_5831 | erythro-2-Amino-3-hydroxy-… (erythro-Phenylserine) | HL | Amino Acids | 22 | `NC(C(=O)O)C(O)c1ccccc1` | (-inf, H2L, -1.9, HL, 8.7, L, +inf) |
| ligand_5832 | threo-2-Amino-3-hydroxy-3-ph… (threo-Phenylserine) | HL | Amino Acids | 13 | `NC(C(=O)O)C(O)c1ccccc1` | (-inf, H2L, -1.9, HL, 8.87, L, +inf) |
| ligand_5833 | L-2-Amino-4-hydroxybutanoic acid (Homoserine) | HL | Amino Acids | 31 | `N[C@@H](CCO)C(=O)O` | (-inf, H2L, 2.24, HL, 9.28, L, +inf) |

### Functional groups across all SQL matches (7 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 7 | 100% |
| primary_amine | 7 | 100% |
| hydroxyl | 6 | 86% |
| aromatic_ring | 3 | 43% |
| ether | 1 | 14% |
| phosphate | 1 | 14% |

---

### Step 11: `search_ligands`
**Args:**
```json
{
  "name": "threonine",
  "ligand_class": "amino acid",
  "limit": 5
}
```

[summary]
## search_ligands — 3 result(s)

**stats:** 3 SQL matches · showing 3 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5811 | L-2-Amino-3-phosphobutanoic ac… (Phosphothreonine) | H4L | Amino Acids | 3 | `C[C@@H](OP(=O)(O)O)[C@H](N)C(=O)O` | (-inf, H3L, 2.25, H2L, 5.83, HL, 9.67, L, +inf) |
| ligand_5829 | L-2-Amino-3-hydroxybutanoic acid (Threonine) | HL | Amino Acids | 117 | `C[C@@H](O)[C@H](N)C(=O)O` | (-inf, H2L, 2.2, HL, 8.94, L, +inf) |
| ligand_5830 | allo-L-2-Amino-3-hydroxybutano… (L-allo-Threonine) | HL | Amino Acids | 31 | `C[C@H](O)[C@H](N)C(=O)O` | (-inf, H2L, 2.11, HL, 8.92, L, +inf) |

### Functional groups across all SQL matches (3 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 3 | 100% |
| hydroxyl | 3 | 100% |
| primary_amine | 3 | 100% |
| phosphate | 1 | 33% |

---

### Step 12: `search_ligands`
**Args:**
```json
{
  "name": "proline",
  "ligand_class": "amino acid",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 5 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5930 | L-Pyrrolidine-2-carboxylic acid (L-Proline) | HL | Amino Acids | 66 | `O=C(O)C1CCCN1` | (-inf, H2L, 1.89, HL, 10.46, L, +inf) |
| ligand_5935 | S-(1-Carboxy-3-phenylpropyl)-L-alan… (Enalaprilat) | H2L | Amino Acids | 15 | `C[C@H](N[C@@H](CCc1ccccc1)C(=O)O)C(=O)N1CCC[C@H]1C(=O)O` | (-inf, H3L, -1.6, H2L, 3.26, HL, 7.54, L, +inf) |
| ligand_5941 | L-4-Hydroxypyrrolidine-2-carbo… (L-Hydroxyproline) | HL | Amino Acids | 46 | `O=C(O)C1CC(O)CN1` | (-inf, H2L, 1.77, HL, 9.47, L, +inf) |
| ligand_5942 | DL-1,3-Thiazolidine-4-carboxylic… (DL-Thiaproline) | HL | Amino Acids | 22 | `O=C(O)C1CSCN1` | (-inf, H2L, -1.5, HL, -1.5, L, +inf) |
| ligand_6018 | L-N-Benzylproline | HL | Amino Acids | 15 | `O=C(O)[C@@H]1CCCN1Cc1ccccc1` | (-inf, H2L, 1.97, HL, 9.93, L, +inf) |

### Functional groups across all SQL matches (5 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 5 | 100% |
| secondary_amine | 4 | 80% |
| aromatic_ring | 2 | 40% |
| amide | 1 | 20% |
| hydroxyl | 1 | 20% |
| tertiary_amine | 1 | 20% |
| thioether | 1 | 20% |

---

### Step 13: `search_ligands`
**Args:**
```json
{
  "name": "tyrosine",
  "ligand_class": "amino acid",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 7 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5817 | DL-2-Amino-3-(2-hydroxyphenyl)propan… (o-Tyrosine) | H2L | Amino Acids | 71 | `NC(Cc1ccccc1O)C(=O)O` | (-inf, H3L, 2.41, H2L, 8.67, HL, 11.01, L, +inf) |
| ligand_5818 | DL-2-Amino-3-(3-hydroxyphenyl)propan… (m-Tyrosine) | H2L | Amino Acids | 86 | `N[C@@H](Cc1cccc(O)c1)C(=O)O` | (-inf, H3L, 2.22, H2L, 8.95, HL, 10.04, L, +inf) |
| ligand_5819 | L-2-Amino-3-(4-hydroxyphenyl)propanoic… (Tyrosine) | H2L | Amino Acids | 107 | `N[C@@H](Cc1ccc(O)cc1)C(=O)O` | (-inf, H3L, 2.24, H2L, 9.04, HL, 10.1, L, +inf) |
| ligand_5820 | L-2-Amino-2-methyl-3-(4-hydrox… (L-Methyltyrosine) | H2L | Amino Acids | 7 | `CC(N)(Cc1ccc(O)cc1)C(=O)O` | (-inf, H3L, 2.16, H2L, 9.14, HL, 10.24, L, +inf) |
| ligand_5821 | L-2-Amino-3-(4-hydroxy-3,5… (L-3,5-Diiodotyrosine) | H2L | Amino Acids | 3 | `N[C@@H](Cc1cc(I)c(O)c(I)c1)C(=O)O` | (-inf, H2L, 6.16, HL, 9.1, L, +inf) |

### Functional groups across all SQL matches (7 parseable SMILES)

| group | count | % |
|-------|-------|---|
| aromatic_ring | 7 | 100% |
| carboxyl | 7 | 100% |
| hydroxyl | 7 | 100% |
| phenol | 7 | 100% |
| primary_amine | 6 | 86% |
| halide | 2 | 29% |

---

### Step 14: `search_ligands`
**Args:**
```json
{
  "name": "tryptophan",
  "ligand_class": "amino acid",
  "limit": 5
}
```

[summary]
## search_ligands — 2 result(s)

**stats:** 2 SQL matches · showing 2 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5907 | L-2-Amino-3-(3-indolyl)propanoic acid (Tryptophan) | HL | Amino Acids | 107 | `N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O` | (-inf, H2L, 2.37, HL, 9.33, L, +inf) |
| ligand_5945 | L-N-Acetyltryptophan | HL | Amino Acids | 7 | `CC(=O)N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O` | (-inf, HL, 3.23, L, +inf) |

### Functional groups across all SQL matches (2 parseable SMILES)

| group | count | % |
|-------|-------|---|
| aromatic_ring | 2 | 100% |
| carboxyl | 2 | 100% |
| amide | 1 | 50% |
| primary_amine | 1 | 50% |

---

### Step 15: `search_ligands`
**Args:**
```json
{
  "name": "asparagine",
  "ligand_class": "amino acid",
  "limit": 5
}
```

[summary]
## search_ligands — 2 result(s)

**stats:** 2 SQL matches · showing 2 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5816 | D-3-Amino-3-carboxyp… (Asparagine hydroxamic acid) | H2L | Amino Acids | 17 | `NC(CC(=O)NO)C(=O)O` | (-inf, H3L, 2.18, H2L, 8.15, HL, 9.37, L, +inf) |
| ligand_5843 | L-2-Aminobutanedioic acid 4-amide (Asparagine) | HL | Amino Acids | 92 | `NC(=O)C[C@H](N)C(=O)O` | (-inf, H2L, 2.16, HL, 8.73, L, +inf) |

### Functional groups across all SQL matches (2 parseable SMILES)

| group | count | % |
|-------|-------|---|
| amide | 2 | 100% |
| carboxyl | 2 | 100% |
| primary_amine | 2 | 100% |
| hydroxyl | 1 | 50% |

---

### Step 16: `search_ligands`
**Args:**
```json
{
  "name": "glutamine",
  "ligand_class": "amino acid",
  "limit": 5
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5844 | L-2-Aminopentanedioic acid 5-amide (Glutamine) | HL | Amino Acids | 71 | `NC(=O)CC[C@H](N)C(=O)O` | (-inf, H2L, 2.19, HL, 9, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| amide | 1 | 100% |
| carboxyl | 1 | 100% |
| primary_amine | 1 | 100% |

---

### Step 17: `search_ligands`
**Args:**
```json
{
  "name": "lysine",
  "ligand_class": "amino acid",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 5 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5845 | L-2-Amino-6-(2-methylpropamido)hexanoic acid (N(6… | HL | Amino Acids | 30 | `CC(C)C(=O)NCCCCC(N)C(=O)O` | (-inf, H2L, 2.4, HL, 9.42, L, +inf) |
| ligand_5846 | L-6-Amino-2-acetamidohexanoic acid (N(2)-Acetyl-L… | HL | Amino Acids | 1 | `CC(=O)N[C@@H](CCCCN)C(=O)O` | *** |
| ligand_5847 | L-2-Amino-6-acetamidohexanoic acid (N(6)-Acetyl-L… | HL | Amino Acids | 7 | `CC(=O)NCCCCC(N)C(=O)O` | (-inf, H2L, 2.13, HL, 9.52, L, +inf) |
| ligand_5849 | N(6)-d-Biotinyl-L-lysine (d-Biocytin) | HL | Amino Acids | 7 | `NC(CCCCNC(=O)CCCCC1SCC2NC(=O)NC21)C(=O)O` | (-inf, H2L, 2.26, HL, 9.29, L, +inf) |
| ligand_5887 | L-2,6-Diaminohexanoic acid (Lysine) | HL | Amino Acids | 98 | `NCCCC[C@H](N)C(=O)O` | (-inf, H3L, 2.15, H2L, 9.15, HL, 10.66, L, +inf) |

### Functional groups across all SQL matches (5 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 5 | 100% |
| primary_amine | 5 | 100% |
| amide | 4 | 80% |
| thioether | 1 | 20% |

---

### Step 18: `search_ligands`
**Args:**
```json
{
  "name": "arginine",
  "ligand_class": "amino acid",
  "limit": 5
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5917 | L-2-Amino-5-guanidopentanoic acid (Arginine) | H2L | Amino Acids | 45 | `N=C(N)NCCC[C@H](N)C(=O)O` | (-inf, H3L, 2.03, H2L, 9, HL, 9, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 1 | 100% |
| imine | 1 | 100% |
| primary_amine | 1 | 100% |
| secondary_amine | 1 | 100% |

---

### Step 20: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_41",
  "ligand_id": "ligand_5760"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 2 species

### Cu^[2+] + Aminoacetic acid (Glycine)
**metal_id:** metal_41 | **ligand_id:** ligand_5760 | **ligand_def_HxL:** HL  
**entries:** 30 | **species:** 2 | **vlm_count:** 30

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 15 |
| beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | [M] + [L]^2 <=> [ML2] | [ML2](aqueous), [M](aqueous), [L](aqueous) | 15 |

**vlm_ids:** vlm_93847, vlm_93848, vlm_93849, vlm_93850, vlm_93851, … vlm_93874, vlm_93875, vlm_93876 (30 listed)

**equilibrium_maps:** 9 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_86 | 2 | 1 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_87 | 2 | 1 | 31~41 °C | 0~0.3 M |
| ref_eq_net_88 | 2 | 1 | 19~29 °C | 0.35~0.65 M |
| ref_eq_net_89 | 2 | 1 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_90 | 2 | 1 | 19~29 °C | 1.85~2.15 M |
| ref_eq_net_91 | 2 | 1 | 19~29 °C | 2.35~2.65 M |
| ref_eq_net_92 | 2 | 1 | 5~15 °C | -0.15~0.15 M |
| ref_eq_net_93 | 2 | 1 | 19~29 °C | -0.15~0.15 M |
| ref_eq_net_94 | 2 | 1 | 35~45 °C | -0.15~0.15 M |

---

### Step 21: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT c.metal_name_SRD, c.ligand_name_SRD, c.ligand_id, c.beta_definition_name, s.constant_value, s.temperature_c, s.ionic_strength_mol_l FROM ligandmetal_card c JOIN ligandmetal_stability_measured s ON c.card_id = s.card_id WHERE c.metal_id IN (41, 112) AND c.ligand_id IN (5760, 5761, 5765, 5766, 5767, 5777, 5828, 5829, 5930, 5819, 5907, 5802, 5804, 5843, 5844, 5887, 5917, 5898, 5856, 5863) AND c.beta_definition_name LIKE '%[ML]/[M][L]%' AND s.temperature_c BETWEEN 20 AND 30 AND s.ionic_strength_mol_l BETWEEN 0.05 AND 0.2 ORDER BY c.ligand_id, c.metal_id, s.constant_value DESC",
  "attach_equilibrium": true
}
```

[PHASE ERROR] Tool 'execute_srd46_sql' is not available yet. You must call 0_plan_search_strategy first (PHASE 2) before using the execution tools.

---
