# Q4.4 — Tool Results (batch 1)

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

### Step 3: `search_ligands`
**Args:**
```json
{
  "ligand_class": "amino acid",
  "limit": 80
}
```

[summary]
## search_ligands — 80 result(s)

**stats:** 297 SQL matches · showing 80 · limit 80

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
| ligand_5790 | cis-2-Aminocyclopentane-1-carboxylic acid | HL | Amino Acids | 6 | `N[C@H]1CCC[C@H]1C(=O)O` | (-inf, H2L, 3.54, HL, 10.1, L, +inf) |
| ligand_5791 | trans-2-Aminocyclopentane-1-carboxylic acid | HL | Amino Acids | 3 | `N[C@@H]1CCC[C@H]1C(=O)O` | (-inf, H2L, 3.75, HL, 9.91, L, +inf) |
| ligand_5792 | cis-2-Aminocyclohexane-1-carboxylic acid | HL | Amino Acids | 6 | `N[C@H]1CCCC[C@H]1C(=O)O` | (-inf, H2L, 3.49, HL, 10.54, L, +inf) |
| ligand_5793 | trans-2-Aminocyclohexane-1-carboxylic acid | HL | Amino Acids | 6 | `N[C@@H]1CCCC[C@H]1C(=O)O` | (-inf, H2L, 3.47, HL, 10.01, L, +inf) |
| ligand_5794 | cis-2-Amino-4-cyclohexene-1-carboxylic acid | HL | Amino Acids | 6 | `N[C@H]1CC=CC[C@H]1C(=O)O` | (-inf, H2L, 3.29, HL, 10.2, L, +inf) |
| ligand_5795 | trans-2-Amino-4-cyclohexene-1-carboxylic acid | HL | Amino Acids | 5 | `N[C@@H]1CC=CC[C@H]1C(=O)O` | (-inf, H2L, 3.33, HL, 10.29, L, +inf) |
| ligand_5796 | DL-3-Amino-3-phenylpropanoi… (Phenyl-beta-Alanine) | HL | Amino Acids | 2 | `NC(CC(=O)O)c1ccccc1` | (-inf, H2L, 3.4, HL, 9, L, +inf) |
| ligand_5797 | 4-Aminobutanoic acid | HL | Amino Acids | 51 | `NCCCC(=O)O` | (-inf, H2L, 4.02, HL, 10.35, L, +inf) |
| ligand_5798 | 5-Aminopentanoic acid | HL | Amino Acids | 20 | `NCCCCC(=O)O` | (-inf, H2L, 4.27, HL, 10.766, L, +inf) |
| ligand_5799 | 6-Aminohexanoic acid | HL | Amino Acids | 29 | `NCCCCCC(=O)O` | (-inf, H2L, 4.373, HL, 10.804, L, +inf) |
| ligand_5800 | 7-Aminoheptanoic acid | HL | Amino Acids | 3 | `NCCCCCCC(=O)O` | (-inf, H2L, 4.502, HL, +inf) |
| ligand_5801 | Aminopropanedioic acid (Aminomalonic acid) | H2L | Amino Acids | 14 | `NC(C(=O)O)C(=O)O` | (-inf, H3L, -1.8, H2L, 2.94, HL, 9.22, L, +inf) |
| ligand_5802 | L-Aminobutanedioic acid (Aspartic acid) | H2L | Amino Acids | 174 | `N[C@@H](CC(=O)O)C(=O)O` | (-inf, H3L, 1.95, H2L, 3.71, HL, 9.66, L, +inf) |
| ligand_5803 | DL-2-Amino-3-methylbutane… (3-Methylaspartic acid) | H2L | Amino Acids | 6 | `CC(C(=O)O)[C@H](N)C(=O)O` | (-inf, H3L, 1.99, H2L, 3.59, HL, 9.48, L, +inf) |
| ligand_5804 | L-2-Aminopentanedioic acid (Glutamic acid) | H2L | Amino Acids | 94 | `N[C@@H](CCC(=O)O)C(=O)O` | (-inf, H3L, 2.16, H2L, 4.15, HL, 9.58, L, +inf) |
| ligand_5805 | DL-2-Amino-2-methylpentan… (2-Methylglutamic acid) | H2L | Amino Acids | 4 | `C[C@](N)(CCC(=O)O)C(=O)O` | (-inf, H2L, 4.05, HL, 9.72, L, +inf) |
| ligand_5806 | DL-2-Aminohexanedioic acid | H2L | Amino Acids | 1 | `NC(CCCC(=O)O)C(=O)O` | (-inf, HL, 9.73, L, +inf) |
| ligand_5807 | DL-2-Amino-3-hydroxypent… (3-Hydroxyglutamic acid) | H2L | Amino Acids | 8 | `N[C@H](C(=O)O)C(O)CC(=O)O` | (-inf, H3L, 2.09, H2L, 4.08, HL, 9.06, L, +inf) |
| ligand_5808 | (3-Aminopropyl)malonic acid | H2L | Amino Acids | 18 | `NCCCC(C(=O)O)C(=O)O` | (-inf, H3L, 2.52, H2L, 4.86, HL, 10.45, L, +inf) |
| ligand_5809 | L-2-Amino-3-phosphopropanoic acid (Phosphoserine) | H3L | Amino Acids | 52 | `N[C@@H](COP(=O)(O)O)C(=O)O` | (-inf, H4L, -0.7, H3L, 2.14, H2L, 5.7, HL, 9.8, L, +inf) |
| ligand_5810 | L-2-Amino-2-methyl-3-phosphopropanoic acid | H4L | Amino Acids | 3 | `CC(N)(COP(=O)(O)O)C(=O)O` | (-inf, H3L, 2.07, H2L, 5.68, HL, 10.07, L, +inf) |
| ligand_5811 | L-2-Amino-3-phosphobutanoic ac… (Phosphothreonine) | H4L | Amino Acids | 3 | `C[C@@H](OP(=O)(O)O)[C@H](N)C(=O)O` | (-inf, H3L, 2.25, H2L, 5.83, HL, 9.67, L, +inf) |
| ligand_5812 | DL-2-Amino-3-(phenylphospho)propanoic acid | H3L | Amino Acids | 2 | `NC(COP(=O)(O)Oc1ccccc1)C(=O)O` | (-inf, H2L, 2.13, HL, 8.79, L, +inf) |
| ligand_5813 | DL-2-Amino-3-phosphonopropanoic acid | H4L | Amino Acids | 31 | `NC(CP(=O)(O)O)C(=O)O` | (-inf, H3L, 2.37, H2L, 6.06, HL, 10.74, L, +inf) |
| ligand_5814 | DL-2-Amino-4-phosphonobutanoic acid | H4L | Amino Acids | 16 | `NC(CCP(=O)(O)O)C(=O)O` | (-inf, H3L, 2.51, H2L, 6.9, HL, 10.21, L, +inf) |
| ligand_5815 | DL-3-Amino-2-phosphonopropanoic acid | H4L | Amino Acids | 20 | `NCC(C(=O)O)P(=O)(O)O` | (-inf, H3L, 3.44, H2L, 5.52, HL, 10.07, L, +inf) |
| ligand_5816 | D-3-Amino-3-carboxyp… (Asparagine hydroxamic acid) | H2L | Amino Acids | 17 | `NC(CC(=O)NO)C(=O)O` | (-inf, H3L, 2.18, H2L, 8.15, HL, 9.37, L, +inf) |
| ligand_5817 | DL-2-Amino-3-(2-hydroxyphenyl)propan… (o-Tyrosine) | H2L | Amino Acids | 71 | `NC(Cc1ccccc1O)C(=O)O` | (-inf, H3L, 2.41, H2L, 8.67, HL, 11.01, L, +inf) |
| ligand_5818 | DL-2-Amino-3-(3-hydroxyphenyl)propan… (m-Tyrosine) | H2L | Amino Acids | 86 | `N[C@@H](Cc1cccc(O)c1)C(=O)O` | (-inf, H3L, 2.22, H2L, 8.95, HL, 10.04, L, +inf) |
| ligand_5819 | L-2-Amino-3-(4-hydroxyphenyl)propanoic… (Tyrosine) | H2L | Amino Acids | 107 | `N[C@@H](Cc1ccc(O)cc1)C(=O)O` | (-inf, H3L, 2.24, H2L, 9.04, HL, 10.1, L, +inf) |
| ligand_5820 | L-2-Amino-2-methyl-3-(4-hydrox… (L-Methyltyrosine) | H2L | Amino Acids | 7 | `CC(N)(Cc1ccc(O)cc1)C(=O)O` | (-inf, H3L, 2.16, H2L, 9.14, HL, 10.24, L, +inf) |
| ligand_5821 | L-2-Amino-3-(4-hydroxy-3,5… (L-3,5-Diiodotyrosine) | H2L | Amino Acids | 3 | `N[C@@H](Cc1cc(I)c(O)c(I)c1)C(=O)O` | (-inf, H2L, 6.16, HL, 9.1, L, +inf) |
| ligand_5822 | DL-2-Amino-3-(3-hydroxy-4-methoxyphenyl)propanoic… | H2L | Amino Acids | 3 | `COc1ccc(CC(N)C(=O)O)cc1O` | (-inf, H3L, 2.23, H2L, 8.84, HL, 10.12, L, +inf) |
| ligand_5823 | DL-2-Amino-3-(4-hydroxy-3-methoxyphenyl)propanoic… | H2L | Amino Acids | 3 | `COc1cc(CC(N)C(=O)O)ccc1O` | (-inf, H3L, 2.13, H2L, 8.78, HL, 10.14, L, +inf) |
| ligand_5824 | L-2-Amino-3-(3-amino-4-hydroxyp… (m-Aminotyrosine) | H2L | Amino Acids | 9 | `Nc1cc(C[C@H](N)C(=O)O)ccc1O` | (-inf, H4L, 2, H3L, 4.48, H2L, 9.09, HL, 10.19, L, +inf) |
| ligand_5825 | DL-2-Amino-2-(3,4-dihydroxyphenyl)acetic a… (DOPG) | H3L | Amino Acids | 6 | `NC(C(=O)O)c1ccc(O)c(O)c1` | (-inf, H4L, 2, H3L, 8.56, H2L, 9.75, HL, 9.75, L, +inf) |
| ligand_5826 | L-2-Amino-3-(3,4-dihydroxyphenyl)propanoic… (DOPA) | H3L | Amino Acids | 91 | `NC(Cc1ccc(O)c(O)c1)C(=O)O` | (-inf, H4L, 2.2, H3L, 8.75, H2L, 9.81, HL, 9.81, L, +inf) |
| ligand_5827 | L-2-Amino-2-methyl-3-(3,4-dihydr… (L-2-MethylDOPA) | H3L | Amino Acids | 13 | `CC(N)(Cc1ccc(O)c(O)c1)C(=O)O` | (-inf, H4L, 2.24, H3L, 8.88, H2L, 9.99, HL, +inf) |
| ligand_5828 | L-2-Amino-3-hydroxypropanoic acid (Serine) | HL | Amino Acids | 139 | `N[C@@H](CO)C(=O)O` | (-inf, H2L, 2.16, HL, 9.05, L, +inf) |
| ligand_5829 | L-2-Amino-3-hydroxybutanoic acid (Threonine) | HL | Amino Acids | 117 | `C[C@@H](O)[C@H](N)C(=O)O` | (-inf, H2L, 2.2, HL, 8.94, L, +inf) |
| ligand_5830 | allo-L-2-Amino-3-hydroxybutano… (L-allo-Threonine) | HL | Amino Acids | 31 | `C[C@H](O)[C@H](N)C(=O)O` | (-inf, H2L, 2.11, HL, 8.92, L, +inf) |
| ligand_5831 | erythro-2-Amino-3-hydroxy-… (erythro-Phenylserine) | HL | Amino Acids | 22 | `NC(C(=O)O)C(O)c1ccccc1` | (-inf, H2L, -1.9, HL, 8.7, L, +inf) |
| ligand_5832 | threo-2-Amino-3-hydroxy-3-ph… (threo-Phenylserine) | HL | Amino Acids | 13 | `NC(C(=O)O)C(O)c1ccccc1` | (-inf, H2L, -1.9, HL, 8.87, L, +inf) |
| ligand_5833 | L-2-Amino-4-hydroxybutanoic acid (Homoserine) | HL | Amino Acids | 31 | `N[C@@H](CCO)C(=O)O` | (-inf, H2L, 2.24, HL, 9.28, L, +inf) |
| ligand_5834 | DL-3-Amino-2-hydroxypropanoic acid (Isoserine) | HL | Amino Acids | 36 | `NCC(O)C(=O)O` | (-inf, H2L, 2.66, HL, 9.13, L, +inf) |
| ligand_5835 | DL-4-Amino-3-hydroxybutanoic acid | HL | Amino Acids | 21 | `NCC(O)CC(=O)O` | (-inf, H2L, 3.9, HL, 9.46, L, +inf) |
| ligand_5836 | L-trans-2-Amino-3-hydroxy-2,3-dihydrobenzoic acid | HL | Amino Acids | 6 | `N[C@H]1C(C(=O)O)=CC=C[C@@H]1O` | (-inf, H2L, 3.36, HL, 8.56, L, +inf) |
| ligand_5837 | D-gluco-2-Amino-3,4,5,6-tet… (D-Glucosaminic acid) | HL | Amino Acids | 30 | `N[C@@H](C(=O)O)[C@@H](O)[C@H](O)[C@H](O)CO` | (-inf, H2L, 2.2, HL, 9.08, L, +inf) |
| ligand_5838 | DL-Amino-4-Methoxyphenyl… (4-Methoxyphenylglycine) | HL | Amino Acids | 12 | `COc1ccc(C(N)C(=O)O)cc1` | (-inf, H2L, 2, HL, 9.07, L, +inf) |
| ligand_5839 | L-2-Aminobutanedioic acid 4-… (4-Methyl aspartate) | HL | Amino Acids | 1 | `COC(=O)CC(N)C(=O)O` | (-inf, HL, 8.5, L, +inf) |

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

### Step 4: `search_ligands`
**Args:**
```json
{
  "ligand_class": "amino acid",
  "limit": 80,
  "exclude": "5760, 5761, 5762, 5763, 5764, 5765, 5766, 5767, 5768, 5769, 5770, 5771, 5772, 5773, 5774, 5775, 5776, 5777, 5778, 5779, 5780, 5781, 5782, 5783, 5784, 5785, 5786, 5787, 5788, 5789, 5790, 5791, 5792, 5793, 5794, 5795, 5796, 5797, 5798, 5799, 5800, 5801, 5802, 5803, 5804, 5805, 5806, 5807, 5808, 5809, 5810, 5811, 5812, 5813, 5814, 5815, 5816, 5817, 5818, 5819, 5820, 5821, 5822, 5823, 5824, 5825, 5826, 5827, 5828, 5829, 5830, 5831, 5832, 5833, 5834, 5835, 5836, 5837, 5838, 5839"
}
```

[summary]
## search_ligands — 80 result(s)

**stats:** 217 SQL matches · showing 80 · limit 80

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5840 | DL-2-Aminopentanedioic acid 5… (5-Ethyl glutamate) | HL | Amino Acids | 2 | `CCOC(=O)CC[C@H](N)C(=O)O` | (-inf, H2L, 2.15, HL, 9.19, L, +inf) |
| ligand_5841 | L-2-Aminopentanedioic acid 5… (5-Benzyl glutamate) | HL | Amino Acids | 2 | `N[C@@H](CCC(=O)OCc1ccccc1)C(=O)O` | (-inf, H2L, 2.06, HL, 8.89, L, +inf) |
| ligand_5842 | DL-2-Aminopentanedioic acid 1… (1-Ethyl glutamate) | HL | Amino Acids | 2 | `CCOC(=O)[C@@H](N)CCC(=O)O` | (-inf, H2L, 3.85, HL, 7.84, L, +inf) |
| ligand_5843 | L-2-Aminobutanedioic acid 4-amide (Asparagine) | HL | Amino Acids | 92 | `NC(=O)C[C@H](N)C(=O)O` | (-inf, H2L, 2.16, HL, 8.73, L, +inf) |
| ligand_5844 | L-2-Aminopentanedioic acid 5-amide (Glutamine) | HL | Amino Acids | 71 | `NC(=O)CC[C@H](N)C(=O)O` | (-inf, H2L, 2.19, HL, 9, L, +inf) |
| ligand_5845 | L-2-Amino-6-(2-methylpropamido)hexanoic acid (N(6… | HL | Amino Acids | 30 | `CC(C)C(=O)NCCCCC(N)C(=O)O` | (-inf, H2L, 2.4, HL, 9.42, L, +inf) |
| ligand_5846 | L-6-Amino-2-acetamidohexanoic acid (N(2)-Acetyl-L… | HL | Amino Acids | 1 | `CC(=O)N[C@@H](CCCCN)C(=O)O` | *** |
| ligand_5847 | L-2-Amino-6-acetamidohexanoic acid (N(6)-Acetyl-L… | HL | Amino Acids | 7 | `CC(=O)NCCCCC(N)C(=O)O` | (-inf, H2L, 2.13, HL, 9.52, L, +inf) |
| ligand_5848 | L-2-Amino-3-(oxalylamido)propanoic acid | HL | Amino Acids | 10 | `NC(CNC(=O)C(=O)O)C(=O)O` | (-inf, H3L, -1.2, H2L, 2.44, HL, 8.95, L, +inf) |
| ligand_5849 | N(6)-d-Biotinyl-L-lysine (d-Biocytin) | HL | Amino Acids | 7 | `NC(CCCCNC(=O)CCCCC1SCC2NC(=O)NC21)C(=O)O` | (-inf, H2L, 2.26, HL, 9.29, L, +inf) |
| ligand_5850 | d-Biocytin sulfoxide | HL | Amino Acids | 4 | `NC(CCCCNC(=O)CCCCC1C2NC(=O)NC2CS1=O)C(=O)O` | (-inf, HL, 9.3, L, +inf) |
| ligand_5851 | d-Biocytin sulfone | HL | Amino Acids | 4 | `NC(CCCCNC(=O)CCCCC1C2NC(=O)NC2CS1(=O)=O)C(=O)O` | (-inf, HL, 9.31, L, +inf) |
| ligand_5852 | L-2-Amino-5-ureidopentanoic acid (Citrulline) | HL | Amino Acids | 16 | `NC(=O)NCCC[C@H](N)C(=O)O` | (-inf, H2L, 2.3, HL, 9.33, L, +inf) |
| ligand_5853 | L-2-Amino-3-(phenylmethoxy)propa… (O-Benzylserine) | HL | Amino Acids | 4 | `N[C@@H](COCc1ccccc1)C(=O)O` | (-inf, H2L, -1.9, HL, 9.03, L, +inf) |
| ligand_5854 | L-2-Amino-3-(4-methoxyph… (4-Methoxyphenylalanine) | HL | Amino Acids | 5 | `COc1ccc(C[C@H](N)C(=O)O)cc1` | (-inf, HL, -9.15, L, +inf) |
| ligand_5855 | DL-2-Amino-3-(3,4-di… (3,4-Dimethoxyphenylalanine) | HL | Amino Acids | 2 | `COc1ccc(C[C@H](N)C(=O)O)cc1OC` | (-inf, H2L, 2.37, HL, 9.02, L, +inf) |
| ligand_5856 | L-2-Amino-3-mercaptopropanoic acid (Cysteine) | H2L | Amino Acids | 134 | `N[C@@H](CS)C(=O)O` | (-inf, H3L, -1.9, H2L, 8.18, HL, 10.3, L, +inf) |
| ligand_5857 | D-2-Amino-3-mercapto-3-methylbuta… (Penicillamine) | H2L | Amino Acids | 91 | `CC(C)(S)[C@H](N)C(=O)O` | (-inf, H3L, -1.9, H2L, 7.96, HL, 10.67, L, +inf) |
| ligand_5858 | DL-2-Amino-3-mercapto-3-methylpentanoic acid | H2L | Amino Acids | 2 | `CCC(C)(S)C(N)C(=O)O` | (-inf, H2L, 7.96, HL, 10.5, L, +inf) |
| ligand_5859 | DL-2-Amino-4-mercaptobutanoic acid (Homocysteine) | H2L | Amino Acids | 3 | `NC(CCS)C(=O)O` | (-inf, H3L, 2.15, H2L, 8.57, HL, 10.38, L, +inf) |
| ligand_5860 | DL-2-Amino-3-(2-mercaptoimidazo-4… (Thiohistidine) | H2L | Amino Acids | 20 | `NC(Cc1cnc(S)[nH]1)C(=O)O` | (-inf, H2L, 8.59, HL, 8.59, L, +inf) |
| ligand_5861 | L-2-Amino-3-(methylthio)propan… (S-Methylcysteine) | HL | Amino Acids | 39 | `CSC[C@H](N)C(=O)O` | (-inf, H2L, 2, HL, 8.74, L, +inf) |
| ligand_5862 | L-2-Amino-3-(ethylthio)propanoi… (S-Ethylcysteine) | HL | Amino Acids | 46 | `CCSC[C@H](N)C(=O)O` | (-inf, H2L, -1.9, HL, 8.65, L, +inf) |
| ligand_5863 | L-2-Amino-4-(methylthio)butanoic acid (Methionine) | HL | Amino Acids | 63 | `CSCC[C@H](N)C(=O)O` | (-inf, H2L, 2.18, HL, 9.08, L, +inf) |
| ligand_5864 | L-2-Amino-4-(ethylthio)butanoic acid (Ethionine) | HL | Amino Acids | 28 | `CCSCC[C@H](N)C(=O)O` | (-inf, H2L, 2.19, HL, 9.05, L, +inf) |
| ligand_5865 | L-2-Amino-3-(carboxymethylthio)propanoic acid | H2L | Amino Acids | 48 | `NC(CSCC(=O)O)C(=O)O` | (-inf, H3L, 2, H2L, 3.36, HL, 8.89, L, +inf) |
| ligand_5866 | L-2-Amino-3-(2-carboxyethylthio)propanoic acid | H2L | Amino Acids | 17 | `NC(CSCCC(=O)O)C(=O)O` | (-inf, H3L, 2.14, H2L, 4.36, HL, 9.08, L, +inf) |
| ligand_5867 | L-2-Amino-3-(2-hydroxyethylthio)propanoic acid | HL | Amino Acids | 3 | `NC(CSCCO)C(=O)O` | (-inf, HL, 8.64, L, +inf) |
| ligand_5868 | L-2-Amino-3-(2-acetamidoethylthio)propanoic acid | HL | Amino Acids | 3 | `CC(=O)NCCSCC(N)C(=O)O` | (-inf, HL, 8.65, L, +inf) |
| ligand_5869 | L-2-Amino-3-(2-acetamidoethylsulfinyl)propanoic a… | HL | Amino Acids | 3 | `CC(=O)NCCS(=O)CC(N)C(=O)O` | (-inf, HL, 7.57, L, +inf) |
| ligand_5870 | L-2-Amino-3-(2-acetamidoethylsulfonyl)propanoic a… | HL | Amino Acids | 3 | `CC(=O)NCCS(=O)(=O)CC(N)C(=O)O` | (-inf, HL, 7.44, L, +inf) |
| ligand_5871 | L-2-Amino-3-(2-Cyanoethylthio)propanoic acid (L-5… | HL | Amino Acids | 1 | `N#CCCSCC(N)C(=O)O` | (-inf, HL, 8.46, L, +inf) |
| ligand_5872 | L-2-Amino-3-(Ethoxy-3-oxopropylthio)propanoic aci… | HL | Amino Acids | 1 | `CCOC(=O)CCSCC(N)C(=O)O` | (-inf, HL, 8.51, L, +inf) |
| ligand_5873 | L-2-Amino-3-(carboxymethylsulfinyl)propanoic acid | H2L | Amino Acids | 1 | `NC(CS(=O)CC(=O)O)C(=O)O` | (-inf, HL, 7.9, L, +inf) |
| ligand_5874 | L-2-Amino-3-(carboxymethylsulfonyl)propanoic acid | H2L | Amino Acids | 1 | `NC(CS(=O)(=O)CC(=O)O)C(=O)O` | (-inf, HL, 7.68, L, +inf) |
| ligand_5875 | 5-Amino-3-thi… (S-2-Aminoethylmercaptoacetic acid) | HL | Amino Acids | 32 | `NCCSCC(=O)O` | (-inf, H2L, 3.18, HL, 9.53, L, +inf) |
| ligand_5876 | 6-Amino-3-th… (S-3-Aminopropylmercaptoacetic acid) | HL | Amino Acids | 21 | `NCCCSCC(=O)O` | (-inf, H2L, 3.35, HL, 10.19, L, +inf) |
| ligand_5877 | 6-Amino… (S-2-Aminoethyl-3-mercaptopropanoic acid) | HL | Amino Acids | 32 | `NCCSCCC(=O)O` | (-inf, HL, 9.54, L, +inf) |
| ligand_5878 | DL-2-(Acetylamino)-3-(2-aminoethylthio)propanoic … | HL | Amino Acids | 1 | `CC(=O)NC(CSCCN)C(=O)O` | (-inf, HL, 9.39, L, +inf) |
| ligand_5879 | L-2-Amino-3-(2-aminoethylthio)propanoic acid (S-(… | HL | Amino Acids | 22 | `NCCSC[C@H](N)C(=O)O` | (-inf, H3L, -1.7, H2L, 8.32, HL, 9.67, L, +inf) |
| ligand_5880 | L-2-Amino-3-(2-aminoethylsulfinyl)propanoic acid | HL | Amino Acids | 4 | `NCCS(=O)CC(N)C(=O)O` | (-inf, H2L, 7.18, HL, 8.37, L, +inf) |
| ligand_5881 | L-2-Amino-3-(2-aminoethylsulfonyl)propanoic acid | HL | Amino Acids | 4 | `NCCS(=O)(=O)CC(N)C(=O)O` | (-inf, H2L, 6.86, HL, 8.02, L, +inf) |
| ligand_5882 | L-2-Amino-3-(2-aminoethyldithio)propanoic acid | HL | Amino Acids | 4 | `NCCSSCC(N)C(=O)O` | (-inf, H2L, 8.28, HL, 9.3, L, +inf) |
| ligand_5883 | L-2,3-Diaminopropanoic acid | HL | Amino Acids | 66 | `NCC(N)C(=O)O` | (-inf, H3L, -1.3, H2L, 6.7, HL, 9.39, L, +inf) |
| ligand_5884 | L-2-Amino-3-(methylamino)propanoic acid | HL | Amino Acids | 19 | `CNCC(N)C(=O)O` | (-inf, H2L, 6.63, HL, 9.76, L, +inf) |
| ligand_5885 | L-2,4-Diaminobutanoic acid | HL | Amino Acids | 55 | `NCCC(N)C(=O)O` | (-inf, H3L, -1.9, H2L, 8.23, HL, 10.28, L, +inf) |
| ligand_5886 | L-2,5-Diaminopentanoic acid (Ornithine) | HL | Amino Acids | 84 | `NCCC[C@H](N)C(=O)O` | (-inf, H3L, 2, H2L, 8.78, HL, 10.52, L, +inf) |
| ligand_5887 | L-2,6-Diaminohexanoic acid (Lysine) | HL | Amino Acids | 98 | `NCCCC[C@H](N)C(=O)O` | (-inf, H3L, 2.15, H2L, 9.15, HL, 10.66, L, +inf) |
| ligand_5888 | DL-2,7-Diaminooctanedioic acid | HL | Amino Acids | 10 | `NC(CCCCC(N)C(=O)O)C(=O)O` | (-inf, H4L, -1.8, H3L, 2.62, H2L, 9.23, HL, 9.89, L, +inf) |
| ligand_5889 | DL-2,6-Diamino-5-hydroxyhexanoic acid | HL | Amino Acids | 78 | `NCC(O)CCC(N)C(=O)O` | (-inf, H3L, 2.1, H2L, 8.84, HL, 9.79, L, +inf) |
| ligand_5890 | L-3,3'-Dithiobis(2-aminopropanoic acid) (Cystine) | H2L | Amino Acids | 17 | `NC(CSSC[C@H](N)C(=O)O)C(=O)O` | (-inf, H2L, 8.03, HL, 8.8, L, +inf) |
| ligand_5891 | D-3,3'-Dithiobis(2-amin… (Penicillamine disulfide) | H2L | Amino Acids | 23 | `CC(C)(SSC(C)(C)C(N)C(=O)O)C(N)C(=O)O` | (-inf, H4L, -1.3, H3L, 2.04, H2L, 7.77, HL, 8.74, L, +inf) |
| ligand_5892 | DL-4,4'-Dithiobis(2-aminobutanoic a… (Homocystine) | H2L | Amino Acids | 26 | `N[C@H](CCSSCC[C@H](N)C(=O)O)C(=O)O` | (-inf, H3L, 2.52, H2L, 8.68, HL, 9.41, L, +inf) |
| ligand_5893 | L-Methylenedithio-3,3'-bis(2-ami… (Dienkolic acid) | H2L | Amino Acids | 33 | `NC(CSCSCC(N)C(=O)O)C(=O)O` | (-inf, H4L, -1.4, H3L, 2.17, H2L, 8.16, HL, 8.97, L, +inf) |
| ligand_5894 | L-Ethylenedithio-3,3'-bis(2-aminopropanoic acid) | H2L | Amino Acids | 5 | `NC(CSCCSCC(N)C(=O)O)C(=O)O` | (-inf, H2L, 8.36, HL, 9.13, L, +inf) |
| ligand_5895 | L-Trimethylenedithio-3,3'-bis(2-aminopropanoic ac… | H2L | Amino Acids | 5 | `NC(CSCCCSCC(N)C(=O)O)C(=O)O` | (-inf, H2L, 8.38, HL, 9.15, L, +inf) |
| ligand_5896 | L-Tetramethylenedithio-3,3'-bis(2-aminopropanoic … | H2L | Amino Acids | 5 | `NC(CSCCCCSCC(N)C(=O)O)C(=O)O` | (-inf, H2L, 8.46, HL, 9.2, L, +inf) |
| ligand_5897 | L-2-Hydroxytrimethylenedithio-3,3'-bis(2-aminopro… | H2L | Amino Acids | 6 | `NC(CSCC(O)CSCC(N)C(=O)O)C(=O)O` | (-inf, H4L, -1.5, H3L, 2.19, H2L, 8.36, HL, 9.2, L, +inf) |
| ligand_5898 | L-2-Amino-3-(4-imidazolyl)propanoic a… (Histidine) | HL | Amino Acids | 250 | `N[C@@H](Cc1c[nH]cn1)C(=O)O` | (-inf, H3L, -1.7, H2L, 6.05, HL, 9.1, L, +inf) |
| ligand_5899 | L-2-Amino-3-(N(1)-methyl-4-imidazolyl)propanoic a… | HL | Amino Acids | 14 | `Cn1cnc(C[C@H](N)C(=O)O)c1` | (-inf, H3L, -1.72, H2L, 5.87, HL, 9.16, L, +inf) |
| ligand_5900 | L-2-Amino-3-(N(3)-methyl-4-imidazolyl)propanoic a… | HL | Amino Acids | 16 | `Cn1cncc1C[C@H](N)C(=O)O` | (-inf, H3L, -1.65, H2L, 6.48, HL, 8.61, L, +inf) |
| ligand_5901 | L-4-(2-Amino-3-carboxypropyl)-1,3-dimethylimidazo… | HL | Amino Acids | 6 | `Cn1c[n+](C)cc1C[C@H](N)C(=O)O` | (-inf, H2L, -1.98, HL, 7.85, L, +inf) |
| ligand_5902 | L-1-Carboxy-2-(4-imidazolyl)ethyl(dimethyl)ammoni… | HL | Amino Acids | 9 | `C[NH+](C)C(Cc1cnc[nH]1)C(=O)O` | (-inf, H3L, -1.03, H2L, 6.03, HL, 8.86, L, +inf) |
| ligand_5903 | L-1-Carboxy-2-(4-imidazolyl)ethyl(trimethyl)ammon… | HL | Amino Acids | 6 | `C[N+](C)(C)C(Cc1c[nH]cn1)C(=O)O` | (-inf, H2L, -0.98, HL, 6, L, +inf) |
| ligand_5904 | L-2-Amino-3-(N(3)-benzyl-4-imidazolyl)propanoic a… | HL | Amino Acids | 18 | `NC(Cc1cncn1Cc1ccccc1)C(=O)O` | (-inf, H3L, 1.94, H2L, 5.53, HL, 9.21, L, +inf) |
| ligand_5905 | L-2-Amino-3-(5-iodo-4-imidazol… (5-Iodo-Histidine) | HL | Amino Acids | 23 | `N[C@@H](Cc1nc[nH]c1I)C(=O)O` | (-inf, H3L, -1.47, H2L, 4.21, HL, 8.6, L, +inf) |
| ligand_5906 | L-2-Amino-3-(2,5-diiodo-4-… (2,5-Diiodo-Histidine) | HL | Amino Acids | 27 | `N[C@@H](Cc1nc(I)[nH]c1I)C(=O)O` | (-inf, H4L, -1.55, H3L, 2.74, H2L, 8.12, HL, 9.57, L, +inf) |
| ligand_5907 | L-2-Amino-3-(3-indolyl)propanoic acid (Tryptophan) | HL | Amino Acids | 107 | `N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O` | (-inf, H2L, 2.37, HL, 9.33, L, +inf) |
| ligand_5908 | L-2-Amino-3-(1-methyl-3-indol… (1-Methyltryptopan) | HL | Amino Acids | 4 | `Cn1cc(CC(N)C(=O)O)c2ccccc21` | (-inf, H2L, 2.32, HL, 9.5, L, +inf) |
| ligand_5909 | DL-2-Amino-3-(5-hydroxy-3-in… (5-Hydroxytryptopan) | HL | Amino Acids | 14 | `NC(Cc1c[nH]c2ccc(O)cc12)C(=O)O` | (-inf, H3L, 2.51, H2L, 9.49, HL, 10.54, L, +inf) |
| ligand_5910 | DL-2-Amino-3-(6-oxo-1,6-dihydro-2-pyridinyl)propa… | HL | Amino Acids | 17 | `NC(Cc1cccc(=O)[nH]1)C(=O)O` | (-inf, H2L, -1.8, HL, 7.8, L, 11.7, H-1L, +inf) |
| ligand_5911 | L-2-Amino-3-(3-hydroxo-4-oxo-1,4-dihyd… (Mimosine) | HL | Amino Acids | 15 | `N[C@@H](Cn1ccc(=O)c(O)c1)C(=O)O` | (-inf, H4L, -1, H3L, 2.5, H2L, 6.87, HL, 8.72, L, +inf) |
| ligand_5912 | DL-2-Amino-3-(5-hydroxo-4-oxo-1,4-d… (Isomimosine) | HL | Amino Acids | 21 | `NC(Cc1cc(=O)c(O)c[nH]1)C(=O)O` | (-inf, H4L, -1.3, H3L, 3.01, H2L, 7.72, HL, 9.17, L, +inf) |
| ligand_5913 | DL-2-Amino-3-(5-hydroxo-6-oxo-1,6-dihydro-2-pyrid… | HL | Amino Acids | 30 | `NC(Cc1ccc(O)c(=O)[nH]1)C(=O)O` | (-inf, H3L, -1.9, H2L, 7.85, HL, 9.01, L, +inf) |
| ligand_5914 | L-2-Amino-3-(3-methoxy-4-… (Mimosine methyl ether) | HL | Amino Acids | 12 | `COc1cn(C[C@H](N)C(=O)O)ccc1=O` | (-inf, H2L, 2.19, HL, 6.86, L, +inf) |
| ligand_5915 | L-2-Amino-3-(2-pyridyl)propanoic acid (3-(2-Pyrid… | HL | Amino Acids | 14 | `N[C@@H](Cc1ccccn1)C(=O)O` | (-inf, H2L, 3.89, HL, 8.95, L, +inf) |
| ligand_5916 | L-2-Amino-3-(6-methyl-2-pyridyl)propanoic acid (3… | HL | Amino Acids | 14 | `Cc1cccc(C[C@H](N)C(=O)O)n1` | (-inf, H2L, 4.78, HL, 8.95, L, +inf) |
| ligand_5917 | L-2-Amino-5-guanidopentanoic acid (Arginine) | H2L | Amino Acids | 45 | `N=C(N)NCCC[C@H](N)C(=O)O` | (-inf, H3L, 2.03, H2L, 9, HL, 9, L, +inf) |
| ligand_5918 | DL-2-Amino-3-(4-guanidinophenyl)propanoic acid | HL | Amino Acids | 2 | `N=C(N)Nc1ccc(CC(N)C(=O)O)cc1` | (-inf, H2L, 8.44, HL, 10.91, L, +inf) |
| ligand_5919 | DL-2-Amino-3-(4-guanidinomethylphenyl)propanoic a… | HL | Amino Acids | 1 | `N=C(N)NCc1ccc(CC(N)C(=O)O)cc1` | (-inf, H2L, 8.83, HL, +inf) |

### Functional groups across all SQL matches (214 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 214 | 100% |
| primary_amine | 87 | 41% |
| aromatic_ring | 74 | 35% |
| secondary_amine | 68 | 32% |
| tertiary_amine | 48 | 22% |
| hydroxyl | 47 | 22% |
| amide | 39 | 18% |
| thioether | 26 | 12% |
| pyridine | 17 | 8% |
| phenol | 11 | 5% |
| thiol | 11 | 5% |
| imine | 9 | 4% |
| ether | 6 | 3% |
| ester | 5 | 2% |
| halide | 4 | 2% |
| phosphonate | 3 | 1% |
| sulfonate | 2 | 1% |
| nitrile | 1 | 0% |
| phosphate | 1 | 0% |

---

### Step 5: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_208 AND c.ligand_class_name = 'Amino Acids'",
  "order_by": "s.constant_value DESC",
  "limit": 100
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 6: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_208"
}
```

[summary]
[CATALOG]
## build_system_catalog — 20 pair(s), 94 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_204 | [MHL2] + [H] <=> [M(HL)2] |  |
| beta_def_238 | [M(OH)2L] + [H] <=> [M(OH)L] + [H2O] |  |
| beta_def_334 | [ML2(s)] <=> [M] + [L]^2 | solid |
| beta_def_337 | [ML2(s,am)] <=> [M] + [L]^2 | solid |
| beta_def_340 | [ML2(s,beta1)] <=> [M] + [L]^2 | solid |
| beta_def_341 | [ML2(s,beta2)] <=> [M] + [L]^2 | solid |
| beta_def_343 | [ML2(s,delta)] <=> [M] + [L]^2 | solid |
| beta_def_344 | [ML2(s,epsilon)] <=> [M] + [L]^2 | solid |
| beta_def_345 | [ML2(s,gamma)] <=> [M] + [L]^2 | solid |
| beta_def_347 | [MO(s)] + [H2O] <=> [M] + [OH]^2 | solid |
| beta_def_374 | [M]^2 + [L]^2 <=> [M2(H-1L)2] + [H]^2 |  |
| beta_def_502 | [M]^2 + [L] <=> [M2L] |  |
| beta_def_636 | [M]^3 + [H] + [L]^4 <=> [M3HL4] |  |
| beta_def_637 | [M3L4] + [H] <=> [M3HL4] |  |
| beta_def_651 | [M3(OH)L4] + [H] <=> [M3L4] + [H2O] |  |
| beta_def_674 | [M]^4 + [L]^4 <=> [M4L4] |  |
| beta_def_739 | [MHL] + [H] <=> [MH2L] |  |
| beta_def_751 | [MH2L] + [H] <=> [MH3L] |  |
| beta_def_765 | [MH3L] + [H] <=> [MH4L] |  |
| beta_def_779 | [M] + [HL] <=> [MHL] |  |
| beta_def_788 | [ML] + [H] <=> [MHL] |  |
| beta_def_792 | [ML2] + [H] <=> [MHL2] |  |
| beta_def_812 | [M] + [L] <=> [ML] |  |
| beta_def_840 | [M] + [L]^2 <=> [ML2] |  |
| beta_def_872 | [M] + [L]^3 <=> [ML3] |  |
| beta_def_894 | [M] + [L]^4 <=> [ML4] |  |
| beta_def_966 | [M(OH)L] + [H] <=> [ML] + [H2O] |  |
| beta_def_984 | [M(OH)L2] + [H] <=> [ML2] + [H2O] |  |

*(all species aqueous unless noted)*

**1. Zn^[2+] + Aminoacetic acid (Glycine)** (metal_208 + ligand_5760) — ligand_def_HxL: HL | 37 ent, 4 sp, 37 vlms (vlm_93924…vlm_93960)
   - species: beta_def_812(12) beta_def_840(13) beta_def_872(11) beta_def_966(1)
   - eq:7 nets T:5~45°C I:-0.15~1.15M max 4n/4e
**2. Zn^[2+] + Ethylenediamine** (metal_208 + ligand_7029) — ligand_def_HxL: L | 36 ent, 3 sp, 36 vlms (vlm_122508…vlm_122543)
   - species: beta_def_812(12) beta_def_840(12) beta_def_872(12)
   - eq:8 nets T:19~41°C I:-0.15~3.15M max 3n/3e
**3. Zn^[2+] + Hydroxide ion** (metal_208 + ligand_10076) — ligand_def_HxL: *** | 33 ent, 13 sp, 33 vlms (vlm_170929…vlm_170961)
   - species: beta_def_337(4) beta_def_340(2) beta_def_341(2) beta_def_343(2) beta_def_344(2) beta_def_345(2) beta_def_347(4) beta_def_502(3) beta_def_674(1) beta_def_812(5) beta_def_840(2) beta_def_872(2) beta_def_894(2)
   - eq:4 nets T:19~30°C I:-0.15~3.15M max 11n/55e
**4. Zn^[2+] + Hydrogen cyanide (Hydrocyanic acid)** (metal_208 + ligand_10090) — ligand_def_HxL: HL | 30 ent, 5 sp, 30 vlms (vlm_171980…vlm_172009)
   - species: beta_def_334(1) beta_def_812(2) beta_def_840(9) beta_def_872(9) beta_def_894(9)
   - eq:5 nets T:5~45°C I:-0.15~3.15M max 5n/10e
**5. Zn^[2+] + 1,3-Diazole (Imidazole)** (metal_208 + ligand_7795) — ligand_def_HxL: L | 30 ent, 4 sp, 30 vlms (vlm_133954…vlm_133983)
   - species: beta_def_812(9) beta_def_840(7) beta_def_872(7) beta_def_894(7)
   - eq:7 nets T:19~41°C I:-0.05~3.15M max 4n/6e
**6. Zn^[2+] + L-2-Amino-3-(4-imidazolyl)propanoic acid (Histidine)** (metal_208 + ligand_5898) — ligand_def_HxL: HL | 29 ent, 6 sp, 29 vlms (vlm_98899…vlm_98927)
   - species: beta_def_204(1) beta_def_788(4) beta_def_792(3) beta_def_812(8) beta_def_840(12) beta_def_984(1)
   - eq:6 nets T:19~41°C I:-0.05~3.15M max 5n/6e
**7. Zn^[2+] + Hydrogen thiocyanate (Thiocyanic acid)** (metal_208 + ligand_10092) — ligand_def_HxL: HL | 24 ent, 4 sp, 24 vlms (vlm_172381…vlm_172404)
   - species: beta_def_812(8) beta_def_840(6) beta_def_872(5) beta_def_894(5)
   - eq:6 nets T:19~30°C I:-0.15~5.15M max 4n/6e
**8. Zn^[2+] + L-2-Amino-3-mercaptopropanoic acid (Cysteine)** (metal_208 + ligand_5856) — ligand_def_HxL: H2L | 23 ent, 8 sp, 23 vlms (vlm_97446…vlm_97468)
   - species: beta_def_204(4) beta_def_636(4) beta_def_637(3) beta_def_651(1) beta_def_779(2) beta_def_792(4) beta_def_812(1) beta_def_840(4)
   - eq:4 nets T:15~41°C I:-0.05~3.15M max 7n/14e
**9. Zn^[2+] + Ammonia** (metal_208 + ligand_10103) — ligand_def_HxL: L | 21 ent, 4 sp, 21 vlms (vlm_173394…vlm_173414)
   - species: beta_def_812(6) beta_def_840(5) beta_def_872(5) beta_def_894(5)
   - eq:4 nets T:19~30°C I:-0.15~2.15M max 4n/6e
**10. Zn^[2+] + Nitrilotris(methylenephosphonic acid) (NTP)** (metal_208 + ligand_8412) — ligand_def_HxL: H6L | 21 ent, 5 sp, 21 vlms (vlm_143422…vlm_143442)
   - species: beta_def_739(2) beta_def_751(2) beta_def_765(1) beta_def_788(7) beta_def_812(9)
   - eq:2 nets T:19~30°C I:-0.15~0.25M max 5n/7e
**11. Zn^[2+] + Iminodiacetic acid (IDA)** (metal_208 + ligand_6127) — ligand_def_HxL: H2L | 20 ent, 2 sp, 20 vlms (vlm_104424…vlm_104443)
   - species: beta_def_812(10) beta_def_840(10)
   - eq:3 nets T:19~41°C I:-0.05~1.15M max 2n/1e
**12. Zn^[2+] + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid)** (metal_208 + ligand_9058) — ligand_def_HxL: H3L | 19 ent, 4 sp, 19 vlms (vlm_157746…vlm_157764)
   - species: beta_def_374(3) beta_def_779(5) beta_def_812(6) beta_def_840(5)
   - eq:4 nets T:19~41°C I:-0.05~0.65M max 4n/6e
**13. Zn^[2+] + 1,10-Phenanthroline (Dipyridino[a,c]benzene)** (metal_208 + ligand_8191) — ligand_def_HxL: L | 19 ent, 3 sp, 19 vlms (vlm_139340…vlm_139358)
   - species: beta_def_812(7) beta_def_840(6) beta_def_872(6)
   - eq:3 nets T:19~30°C I:-0.15~1.15M max 3n/3e
**14. Zn^[2+] + L-2-Aminopropanoic acid (Alanine)** (metal_208 + ligand_5761) — ligand_def_HxL: HL | 19 ent, 4 sp, 19 vlms (vlm_94305…vlm_94323)
   - species: beta_def_812(7) beta_def_840(7) beta_def_872(3) beta_def_966(2)
   - eq:5 nets T:19~41°C I:-0.15~1.15M max 4n/4e
**15. Zn^[2+] + 2,2'-Bipyridyl** (metal_208 + ligand_8156) — ligand_def_HxL: L | 18 ent, 3 sp, 18 vlms (vlm_138658…vlm_138675)
   - species: beta_def_812(6) beta_def_840(6) beta_def_872(6)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 3n/3e
**16. Zn^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_208 + ligand_6277) — ligand_def_HxL: H4L | 18 ent, 4 sp, 18 vlms (vlm_108707…vlm_108724)
   - species: beta_def_739(1) beta_def_788(5) beta_def_812(6) beta_def_966(6)
   - eq:5 nets T:19~30°C I:-0.15~3.15M max 4n/5e
**17. Zn^[2+] + N-(2-Hydroxyethyl)iminodiacetic acid (HIDA)** (metal_208 + ligand_6204) — ligand_def_HxL: H2L | 18 ent, 4 sp, 18 vlms (vlm_106769…vlm_106786)
   - species: beta_def_238(1) beta_def_812(8) beta_def_840(8) beta_def_966(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 4n/3e
**18. Zn^[2+] + D-2-Amino-3-mercapto-3-methylbutanoic acid (Penicillamine)** (metal_208 + ligand_5857) — ligand_def_HxL: H2L | 18 ent, 8 sp, 18 vlms (vlm_97593…vlm_97610)
   - species: beta_def_204(4) beta_def_636(1) beta_def_637(1) beta_def_779(2) beta_def_792(4) beta_def_812(1) beta_def_840(4) beta_def_984(1)
   - eq:4 nets T:15~41°C I:-0.05~3.15M max 6n/13e
**19. Zn^[2+] + Ethanoic acid (Acetic acid)** (metal_208 + ligand_8465) — ligand_def_HxL: HL | 17 ent, 3 sp, 17 vlms (vlm_144834…vlm_144850)
   - species: beta_def_812(8) beta_def_840(6) beta_def_872(3)
   - eq:6 nets T:19~30°C I:-0.15~3.15M max 3n/3e
**20. Zn^[2+] + DL-Methylethylenediamine (1,2-Propylenediamine) (pn)** (metal_208 + ligand_7030) — ligand_def_HxL: L | 17 ent, 3 sp, 17 vlms (vlm_122671…vlm_122687)
   - species: beta_def_812(8) beta_def_840(8) beta_def_872(1)
   - eq:8 nets T:19~35°C I:-0.15~2.15M max 3n/3e

---
