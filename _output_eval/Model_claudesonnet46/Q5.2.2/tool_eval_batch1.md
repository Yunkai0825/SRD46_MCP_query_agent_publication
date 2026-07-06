# Q5.2.2 — Tool Results (batch 1)

### Step 2: `search_ligands`
**Args:**
```json
{
  "name": "transferrin",
  "limit": 10
}
```

[PHASE ERROR] Call 0_preplan_decision first to triage the question before L0 searches.

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "albumin",
  "limit": 10
}
```

[PHASE ERROR] Call 0_preplan_decision first to triage the question before L0 searches.

---

### Step 4: `search_ligands`
**Args:**
```json
{
  "name": "peptide",
  "limit": 10
}
```

[PHASE ERROR] Call 0_preplan_decision first to triage the question before L0 searches.

---

### Step 6: `search_metals`
**Args:**
```json
{
  "name": "iron",
  "limit": 5
}
```

[summary]
## search_metals — 2 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_61 | Fe^[3+] | Fe | 3 | ✓ | [Fe+3] | InChI=1S/Fe/q+3 | beta_totN_128 | ligand_totN_406 | vlm_totN_1473 |
| metal_62 | Fe^[2+] | Fe | 2 | ✓ | [Fe+2] | InChI=1S/Fe/q+2 | beta_totN_57 | ligand_totN_217 | vlm_totN_667 |

---

### Step 7: `search_ligands`
**Args:**
```json
{
  "name": "transferrin",
  "limit": 10
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
  "name": "albumin",
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
  "name": "lactoferrin",
  "limit": 10
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 10: `search_ligands`
**Args:**
```json
{
  "name": "metallothionein",
  "limit": 10
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 11: `search_metals`
**Args:**
```json
{
  "name": "copper",
  "limit": 5
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

### Step 12: `search_metals`
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

### Step 13: `search_ligands`
**Args:**
```json
{
  "ligand_class": "amino acids",
  "limit": 20
}
```

[summary]
## search_ligands — 20 result(s)

**stats:** 297 SQL matches · showing 20 · limit 20

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

### Step 14: `search_ligands`
**Args:**
```json
{
  "ligand_class": "peptides",
  "limit": 20
}
```

[summary]
## search_ligands — 20 result(s)

**stats:** 321 SQL matches · showing 20 · limit 20

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6372 | Glycylglycine (Diglycine) | HL | Peptides | 172 | `NCC(=O)NCC(=O)O` | (-inf, H2L, 3.11, HL, 8.09, L, +inf) |
| ligand_6373 | Glycyl-beta-alanine (Glycyl-3-aminopropanoic acid) | HL | Peptides | 14 | `NCC(=O)NCCC(=O)O` | (-inf, H2L, 4, HL, 8.11, L, +inf) |
| ligand_6374 | Glycyl-4-aminobutanoic acid | HL | Peptides | 30 | `NCC(=O)NCCCC(=O)O` | (-inf, H2L, 4.22, HL, 8.12, L, +inf) |
| ligand_6375 | Glycyl-L-alanine | HL | Peptides | 62 | `C[C@H](NC(=O)CN)C(=O)O` | (-inf, H2L, 3.12, HL, 8.15, L, +inf) |
| ligand_6376 | Glycyl-L-alan-2-ene | HL | Peptides | 18 | `C=C(NC(=O)CN)C(=O)O` | (-inf, H2L, 2.83, HL, 7.97, L, +inf) |
| ligand_6377 | Glycyl-DL-2-aminobutanoic acid | HL | Peptides | 10 | `CCC(NC(=O)CN)C(=O)O` | (-inf, H2L, 3.155, HL, 8.331, L, +inf) |
| ligand_6378 | Glycyl-DL-norvaline | HL | Peptides | 6 | `CCCC(NC(=O)CN)C(=O)O` | (-inf, H2L, 3.17, HL, 8.22, L, +inf) |
| ligand_6379 | Glycyl-DL-norleucine | HL | Peptides | 6 | `CCCCC(NC(=O)CN)C(=O)O` | (-inf, H2L, -3.33, HL, 8.23, L, +inf) |
| ligand_6380 | Glycyl-L-valine | HL | Peptides | 19 | `CC(C)[C@H](NC(=O)CN)C(=O)O` | (-inf, H2L, 3.14, HL, 8.14, L, +inf) |
| ligand_6381 | Glycyl-L-val-2-ene | HL | Peptides | 6 | `CC(C)=C(NC(=O)CN)C(=O)O` | (-inf, H2L, 3.65, HL, 8.15, L, +inf) |
| ligand_6382 | Glycyl-L-leucine | HL | Peptides | 33 | `CC(C)C[C@H](NC(=O)CN)C(=O)O` | (-inf, H2L, 3.1, HL, 8.18, L, +inf) |
| ligand_6383 | Glycyl-L-leuc-2-ene | HL | Peptides | 17 | `CC(C)/C=C(/NC(=O)CN)C(=O)O` | (-inf, H2L, 3.47, HL, 8.06, L, +inf) |
| ligand_6384 | Glycyl-L-isoleucine | HL | Peptides | 4 | `CC[C@H](C)[C@H](NC(=O)CN)C(=O)O` | (-inf, H2L, 3, HL, 8.15, L, +inf) |
| ligand_6385 | Glycyl-L-phenylalanine | HL | Peptides | 34 | `NCC(=O)N[C@@H](Cc1ccccc1)C(=O)O` | (-inf, H2L, 2.99, HL, 8.09, L, +inf) |
| ligand_6386 | Glycyl-L-phenylalan-2-ene | HL | Peptides | 23 | `NCC(=O)N/C(=C/c1ccccc1)C(=O)O` | (-inf, H2L, 3.17, HL, 8, L, +inf) |
| ligand_6387 | Glycylsarcosine | HL | Peptides | 14 | `CN(CC(=O)O)C(=O)CN` | (-inf, H2L, 2.85, HL, 8.53, L, +inf) |
| ligand_6388 | Glycyl-L-proline | HL | Peptides | 20 | `NCC(=O)N1CCC[C@H]1C(=O)O` | (-inf, H2L, 2.82, HL, 8.46, L, +inf) |
| ligand_6389 | Glycyl-L-aspartic acid | H2L | Peptides | 34 | `NCC(=O)N[C@@H](CC(=O)O)C(=O)O` | (-inf, H3L, 2.8, H2L, 4.3, HL, 8.34, L, +inf) |
| ligand_6390 | Glycyl-L-glutamic acid | H2L | Peptides | 25 | `NCC(=O)N[C@@H](CCC(=O)O)C(=O)O` | (-inf, H3L, 2.83, H2L, 4.34, HL, 8.3, L, +inf) |
| ligand_6391 | Glycyl-DL-… (Glycyl-DL-serine dihydrogenphosphate) | H3L | Peptides | 7 | `NCC(=O)N[C@@H](COP(=O)(O)O)C(=O)O` | (-inf, H3L, 2.91, H2L, 6.03, HL, 8.42, L, +inf) |

### Functional groups across all SQL matches (270 parseable SMILES)

| group | count | % |
|-------|-------|---|
| amide | 270 | 100% |
| carboxyl | 270 | 100% |
| primary_amine | 252 | 93% |
| aromatic_ring | 89 | 33% |
| hydroxyl | 52 | 19% |
| phenol | 36 | 13% |
| thioether | 20 | 7% |
| secondary_amine | 17 | 6% |
| thiol | 10 | 4% |
| imine | 8 | 3% |
| phosphate | 7 | 3% |
| ester | 1 | 0% |
| pyridine | 1 | 0% |

---
