# Q4.4 — Tool Results (batch 1)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "zinc"
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
  "limit": 100
}
```

[summary]
## search_ligands — 100 result(s)

**stats:** 297 SQL matches · showing 100 · limit 100

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

### Step 4: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_208 AND c.ligand_class_name = 'Amino Acids'",
  "order_by": "s.constant_value DESC",
  "limit": 200
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 5: `search_ligands`
**Args:**
```json
{
  "name": "histidine",
  "ligand_class": "amino acid",
  "limit": 20
}
```

[summary]
## search_ligands — 19 result(s)

**stats:** 19 SQL matches · showing 19 · limit 20

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5860 | DL-2-Amino-3-(2-mercaptoimidazo-4… (Thiohistidine) | H2L | Amino Acids | 20 | `NC(Cc1cnc(S)[nH]1)C(=O)O` | (-inf, H2L, 8.59, HL, 8.59, L, +inf) |
| ligand_5898 | L-2-Amino-3-(4-imidazolyl)propanoic a… (Histidine) | HL | Amino Acids | 250 | `N[C@@H](Cc1c[nH]cn1)C(=O)O` | (-inf, H3L, -1.7, H2L, 6.05, HL, 9.1, L, +inf) |
| ligand_5899 | L-2-Amino-3-(N(1)-methyl-4-imidazolyl)propanoic a… | HL | Amino Acids | 14 | `Cn1cnc(C[C@H](N)C(=O)O)c1` | (-inf, H3L, -1.72, H2L, 5.87, HL, 9.16, L, +inf) |
| ligand_5900 | L-2-Amino-3-(N(3)-methyl-4-imidazolyl)propanoic a… | HL | Amino Acids | 16 | `Cn1cncc1C[C@H](N)C(=O)O` | (-inf, H3L, -1.65, H2L, 6.48, HL, 8.61, L, +inf) |
| ligand_5901 | L-4-(2-Amino-3-carboxypropyl)-1,3-dimethylimidazo… | HL | Amino Acids | 6 | `Cn1c[n+](C)cc1C[C@H](N)C(=O)O` | (-inf, H2L, -1.98, HL, 7.85, L, +inf) |
| ligand_5902 | L-1-Carboxy-2-(4-imidazolyl)ethyl(dimethyl)ammoni… | HL | Amino Acids | 9 | `C[NH+](C)C(Cc1cnc[nH]1)C(=O)O` | (-inf, H3L, -1.03, H2L, 6.03, HL, 8.86, L, +inf) |
| ligand_5903 | L-1-Carboxy-2-(4-imidazolyl)ethyl(trimethyl)ammon… | HL | Amino Acids | 6 | `C[N+](C)(C)C(Cc1c[nH]cn1)C(=O)O` | (-inf, H2L, -0.98, HL, 6, L, +inf) |
| ligand_5904 | L-2-Amino-3-(N(3)-benzyl-4-imidazolyl)propanoic a… | HL | Amino Acids | 18 | `NC(Cc1cncn1Cc1ccccc1)C(=O)O` | (-inf, H3L, 1.94, H2L, 5.53, HL, 9.21, L, +inf) |
| ligand_5905 | L-2-Amino-3-(5-iodo-4-imidazol… (5-Iodo-Histidine) | HL | Amino Acids | 23 | `N[C@@H](Cc1nc[nH]c1I)C(=O)O` | (-inf, H3L, -1.47, H2L, 4.21, HL, 8.6, L, +inf) |
| ligand_5906 | L-2-Amino-3-(2,5-diiodo-4-… (2,5-Diiodo-Histidine) | HL | Amino Acids | 27 | `N[C@@H](Cc1nc(I)[nH]c1I)C(=O)O` | (-inf, H4L, -1.55, H3L, 2.74, H2L, 8.12, HL, 9.57, L, +inf) |
| ligand_5960 | L-2-(Methylamino)-3-(4-imidazolyl)propanoic acid … | HL | Amino Acids | 17 | `CNC(Cc1cnc[nH]1)C(=O)O` | (-inf, H3L, -1.4, H2L, 5.93, HL, 9.32, L, +inf) |
| ligand_5961 | L-2-(Benzylamino)-3-(4-imidazolyl)propanoic acid … | HL | Amino Acids | 18 | `O=C(O)C(Cc1cnc[nH]1)NCc1ccccc1` | (-inf, H3L, -1.3, H2L, 5.94, HL, 8.32, L, +inf) |
| ligand_5962 | L-2-(Benzylamino)-3-(3-benzyl-5-imidazolyl)propan… | HL | Amino Acids | 14 | `O=C(O)C(Cc1cn(Cc2ccccc2)cn1)NCc1ccccc1` | (-inf, H3L, 2, H2L, 5.5, HL, 8.47, L, +inf) |
| ligand_5967 | N-Acetyl-L-histidine | HL | Amino Acids | 23 | `CC(=O)N[C@@H](Cc1c[nH]cn1)C(=O)O` | (-inf, H2L, 2.84, HL, 7.02, L, +inf) |
| ligand_5968 | N-(2-Methyl-2-propoxycarbonyl)-L-histidine | HL | Amino Acids | 6 | `CC(C)OC(=O)NC(Cc1c[nH]cn1)C(=O)O` | (-inf, H2L, 2.98, HL, 7.06, L, +inf) |
| ligand_5969 | N-Acetylglycyl-L-histidine | HL | Amino Acids | 6 | `CC(=O)NCC(=O)N[C@@H](CC1C=NC=N1)C(=O)O` | (-inf, H2L, 2.87, HL, 6.99, L, +inf) |
| ligand_5970 | N-Acetylglycylglycyl-L-histidine | HL | Amino Acids | 12 | `CC(=O)NCC(=O)NCC(=O)N[C@@H](CC1C=NC=N1)C(=O)O` | (-inf, H2L, 2.96, HL, 7.06, L, +inf) |
| ligand_5973 | N-Acetylglycylglycylglycyl-L-histidine | HL | Amino Acids | 7 | `CC(=O)NCC(=O)NCC(=O)NCC(=O)N[C@@H](CC1C=NC=N1)C(=O)O` | (-inf, H2L, 3.04, HL, 7.09, L, +inf) |
| ligand_6027 | L-2-(Dimethylamino)-3-(4-imidazolyl)propanoic aci… | HL | Amino Acids | 20 | `CN(C)C(Cc1cnc[nH]1)C(=O)O` | (-inf, H3L, -1.1, H2L, 6.01, HL, 8.88, L, +inf) |

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
  "name": "methionine",
  "ligand_class": "amino acid",
  "limit": 10
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 10

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

### Step 7: `search_ligands`
**Args:**
```json
{
  "name": "tryptophan",
  "ligand_class": "amino acid",
  "limit": 10
}
```

[summary]
## search_ligands — 2 result(s)

**stats:** 2 SQL matches · showing 2 · limit 10

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

### Step 8: `search_ligands`
**Args:**
```json
{
  "name": "proline",
  "ligand_class": "amino acid",
  "limit": 10
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 5 SQL matches · showing 5 · limit 10

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

### Step 9: `search_ligands`
**Args:**
```json
{
  "name": "lysine",
  "ligand_class": "amino acid",
  "limit": 10
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 5 SQL matches · showing 5 · limit 10

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

### Step 10: `search_ligands`
**Args:**
```json
{
  "name": "arginine",
  "ligand_class": "amino acid",
  "limit": 10
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 10

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

### Step 11: `build_system_catalog`
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

### Step 13: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND c.ligand_class_name = 'Amino Acids' AND c.beta_definition_id = beta_def_812)",
  "order_by": "s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability — 100 row(s)

### ΔS — 12 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_208 | Zn^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 2 | 1 | 25 | 0~0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5907 | L-2-Amino-3-(3-indolyl)prop… | HL | N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O | 2 | 1 | 25 | 0.1~3 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5975 | Ethylenediiminodiacetic aci… | H2L | O=C(O)CNCCNCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5777 | L-2-Amino-3-phenylpropanoic… | HL | N[C@@H](Cc1ccccc1)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5761 | L-2-Aminopropanoic acid (Al… | HL | C[C@H](N)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5837 | D-gluco-2-Amino-3,4,5,6-tet… | HL | N[C@@H](C(=O)O)[C@@H](O)[C@H](O)[C@H](O)CO | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5843 | L-2-Aminobutanedioic acid 4… | HL | NC(=O)C[C@H](N)C(=O)O | 1 | 1 | 25 | 3 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5941 | L-4-Hydroxypyrrolidine-2-ca… | HL | O=C(O)C1CC(O)CN1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5828 | L-2-Amino-3-hydroxypropanoi… | HL | N[C@@H](CO)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5845 | L-2-Amino-6-(2-methylpropam… | HL | CC(C)C(=O)NCCCCC(N)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5829 | L-2-Amino-3-hydroxybutanoic… | HL | C[C@@H](O)[C@H](N)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |

### logK — 71 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_208 | Zn^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 5 | 1 | 25~37 | 0.1~3 | *** | 5 |
| metal_208 | Zn^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 4 | 1 | 10~40 | 0~0.1 | *** | 4 |
| metal_208 | Zn^[2+] | ligand_5802 | L-Aminobutanedioic acid (As… | H2L | N[C@@H](CC(=O)O)C(=O)O | 4 | 1 | 25~37 | 0.1~1 | *** | 4 |
| metal_208 | Zn^[2+] | ligand_5948 | N-(2-Aminoethyl)glycine (Et… | HL | NCCNCC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 2 |
| metal_208 | Zn^[2+] | ligand_5813 | DL-2-Amino-3-phosphonopropa… | H4L | NC(CP(=O)(O)O)C(=O)O | 2 | 1 | 25 | 0.1~1 | *** | 2 |
| metal_208 | Zn^[2+] | ligand_6021 | N,N-Bis(2-hydroxyethyl)glyc… | HL | O=C(O)CN(CCO)CCO | 2 | 1 | 25~30 | 0.1 | *** | 2 |
| metal_208 | Zn^[2+] | ligand_5930 | L-Pyrrolidine-2-carboxylic … | HL | O=C(O)C1CCCN1 | 2 | 1 | 25~37 | 0.1~0.15 | *** | 2 |
| metal_208 | Zn^[2+] | ligand_5865 | L-2-Amino-3-(carboxymethylt… | H2L | NC(CSCC(=O)O)C(=O)O | 2 | 1 | 25~37 | 0.1~0.15 | *** | 2 |
| metal_208 | Zn^[2+] | ligand_5975 | Ethylenediiminodiacetic aci… | H2L | O=C(O)CNCCNCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5761 | L-2-Aminopropanoic acid (Al… | HL | C[C@H](N)C(=O)O | 1 | 1 | 25 | 0 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5843 | L-2-Aminobutanedioic acid 4… | HL | NC(=O)C[C@H](N)C(=O)O | 1 | 1 | 25 | 3 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5941 | L-4-Hydroxypyrrolidine-2-ca… | HL | O=C(O)C1CC(O)CN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5907 | L-2-Amino-3-(3-indolyl)prop… | HL | N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O | 1 | 1 | 25 | 3 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6040 | N,N'-Bis(2-mercaptoethyl)et… | H4L | O=C(O)CN(CCS)CCN(CCS)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6007 | L,L-Ethylenediimino-2,2'-bi… | H4L | O=C(O)C(CS)NCCNC(CS)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5994 | N,N'-Bis(2-hydroxyphenyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)c1ccccc1O)c1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6055 | N,N'-Bis(2-aminoethyl)ethyl… | H2L | NCCN(CCN(CCN)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6037 | N,N'-Bis(2-hydroxybenzyl)et… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)Cc1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6041 | N,N'-Bis(3-hydroxy-5-phosph… | H6L | Cc1ncc(COP(=O)(O)O)c(CN(CCN(CC(=O)O)Cc2c(COP(=O)(O)O)cnc(C)c2O)CC(=O)O)c1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5995 | rac-Ethylenediiminobis[(2-h… | H4L | O=C(O)C(Cc1ccccc1O)NCCNC(Cc1ccccc1O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6039 | N,N"-Bis(2-hydroxybenzyl)di… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5996 | meso-Ethylenediiminobis[(2-… | H4L | O=C(O)C(Cc1ccccc1O)NCCNC(Cc1ccccc1O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6042 | N,N'-Bis(3-hydroxy-5-hydrox… | H4L | Cc1ncc(CO)c(CN(CCN(CC(=O)O)Cc2c(CO)cnc(C)c2O)CC(=O)O)c1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6056 | N,N'-Bis(2-pyridylmethyl)et… | H2L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccn1)Cc1ccccn1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6036 | N,N'-Bis(carboxymethyl)ethy… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)NO)CC(=O)NO | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6011 | cis,cis-Cyclohexane-1,3,5-t… | H3L | O=C(O)CN[C@H]1C[C@@H](NCC(=O)O)C[C@@H](NCC(=O)O)C1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5984 | Ethylenediiminodibutanedioi… | H4L | O=C(O)CC(NCCNC(CC(=O)O)C(=O)O)C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6029 | N,N-Bis(2-aminoethyl)glycine | HL | NCCN(CCN)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5958 | Diethylenetriamine-N(1)-ace… | HL | NCCNCCNCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6010 | Ethane-1,1,1-tris(methylene… | H3L | CC(CNCC(=O)O)(CNCC(=O)O)CNCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6030 | N,N'-Dimethylethylenedinitr… | H2L | CN(CCN(C)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5993 | DL-2,3-Diaminopropanoic-N,N… | H4L | O=C(O)C(CNC(C(=O)O)C(=O)O)NC(C(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6052 | rac-1,2-Dimethylethylenedin… | H2L | CC(C(C)N(CC(N)=O)CC(=O)O)N(CC(N)=O)CC(=O)O | 1 | 1 | 37 | 0.15 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6051 | DL-1-Ethylethylenedinitrilo… | H2L | CCC(CN(CC(N)=O)CC(=O)O)N(CC(N)=O)CC(=O)O | 1 | 1 | 37 | 0.15 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5983 | Ethylenediiminodipropanedio… | H4L | O=C(O)C(NCCNC(C(=O)O)C(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6005 | Oxybis(ethyleneiminopropane… | H4L | O=C(O)C(NCCOCCNC(C(=O)O)C(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5985 | Ethylenediiminodi-2-pentane… | H4L | O=C(O)CCC(NCCNC(CCC(=O)O)C(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5999 | Ethylenediiminobis(3-hydrox… | H2L | O=C(O)C(CO)NCCNC(CO)C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6003 | 6-Oxa-3,9-diazaundecanedioi… | H2L | O=C(O)CNCCOCCNCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5977 | Ethylenediiminodi-2-propano… | H2L | CC(NCCNC(C)C(=O)O)C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6053 | meso-1,2-Dimethylethylenedi… | H2L | CC(C(C)N(CC(N)=O)CC(=O)O)N(CC(N)=O)CC(=O)O | 1 | 1 | 37 | 0.15 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6000 | Ethylenediiminobis(4-hydrox… | H2L | O=C(O)C(CCO)NCCNC(CCO)C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5978 | Ethylenediiminodi-2-butanoi… | H2L | CCC(NCCNC(CC)C(=O)O)C(=O)O | 1 | 1 | 37 | 0.15 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6050 | DL-1-Methylethylenedinitril… | H2L | CC(CN(CC(N)=O)CC(=O)O)N(CC(N)=O)CC(=O)O | 1 | 1 | 37 | 0.15 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6031 | 5-Thia-2,8-diazanonane-N,N'… | H2L | CN(CCSCCN(C)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5860 | DL-2-Amino-3-(2-mercaptoimi… | H2L | NC(Cc1cnc(S)[nH]1)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5856 | L-2-Amino-3-mercaptopropano… | H2L | N[C@@H](CS)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5936 | L-N-(2-Hydroxybenzyl)-2-ami… | H2L | CC(NCc1ccccc1O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5937 | N-(Phosphonomethyl)glycine … | H3L | O=C(O)CNCP(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5976 | Ethylenediiminodi-3-propano… | H2L | O=C(O)CCNCCNCCC(=O)O | 1 | 1 | 30 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5893 | L-Methylenedithio-3,3'-bis(… | H2L | NC(CSCSCC(N)C(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5906 | L-2-Amino-3-(2,5-diiodo-4-i… | HL | N[C@@H](Cc1nc(I)[nH]c1I)C(=O)O | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6026 | 3-(3-Hydroxy-4-oxo-1,4-dihy… | HL | O=C(O)CCn1ccc(=O)c(O)c1 | 1 | 1 | 37 | 0.15 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5885 | L-2,4-Diaminobutanoic acid | HL | NCCC(N)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5890 | L-3,3'-Dithiobis(2-aminopro… | H2L | NC(CSSC[C@H](N)C(=O)O)C(=O)O | 1 | 1 | 37 | 0.15 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5815 | DL-3-Amino-2-phosphonopropa… | H4L | NCC(C(=O)O)P(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5904 | L-2-Amino-3-(N(3)-benzyl-4-… | HL | NC(Cc1cncn1Cc1ccccc1)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5814 | DL-2-Amino-4-phosphonobutan… | H4L | NC(CCP(=O)(O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5801 | Aminopropanedioic acid (Ami… | H2L | NC(C(=O)O)C(=O)O | 1 | 1 | 20 | 0 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5960 | L-2-(Methylamino)-3-(4-imid… | HL | CNC(Cc1cnc[nH]1)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6027 | L-2-(Dimethylamino)-3-(4-im… | HL | CN(C)C(Cc1cnc[nH]1)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5883 | L-2,3-Diaminopropanoic acid | HL | NCC(N)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5884 | L-2-Amino-3-(methylamino)pr… | HL | CNCC(N)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5809 | L-2-Amino-3-phosphopropanoi… | H3L | N[C@@H](COP(=O)(O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5961 | L-2-(Benzylamino)-3-(4-imid… | HL | O=C(O)C(Cc1cnc[nH]1)NCc1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5962 | L-2-(Benzylamino)-3-(3-benz… | HL | O=C(O)C(Cc1cn(Cc2ccccc2)cn1)NCc1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5864 | L-2-Amino-4-(ethylthio)buta… | HL | CCSCC[C@H](N)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5905 | L-2-Amino-3-(5-iodo-4-imida… | HL | N[C@@H](Cc1nc[nH]c1I)C(=O)O | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6023 | N,N-Bis(2-hydroxypropyl)gly… | HL | CC(O)CN(CC(=O)O)CC(C)O | 1 | 1 | 30 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5891 | D-3,3'-Dithiobis(2-amino-3-… | H2L | CC(C)(SSC(C)(C)C(N)C(=O)O)C(N)C(=O)O | 1 | 1 | 37 | 0.15 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6022 | DL-N,N-Bis(2-hydroxyethyl)a… | HL | CC(C(=O)O)N(CCO)CCO | 1 | 1 | 20 | 0.1 | *** | 1 |

---

### Step 14: `search_pka_ligands`
**Args:**
```json
{
  "where": "(lc.ligand_id IN ('ligand_5765', 'ligand_5766', 'ligand_5767', 'ligand_5777', 'ligand_5828', 'ligand_5829', 'ligand_5802', 'ligand_5804', 'ligand_5843', 'ligand_5844', 'ligand_5887', 'ligand_5917', 'ligand_5863', 'ligand_5819', 'ligand_5907', 'ligand_5930'))",
  "limit": 100
}
```

[summary]
## search_pka_ligands — 37 row(s)

| ligand_id | ligand_name | HxL_def | formula | smiles | pH_ladder | T°C_range | I(M)_range | similarity_score |
|-----------|-------------|---------|---------|--------|-----------|-----------|------------|------------------|
| ligand_5765 | L-2-Amino-3-methylbutanoic acid (Valine) | HL | C5H11N1O2 | CC(C)[C@H](N)C(=O)O | −∞; H2L (M_tot_1); (2.27, vlm_94563); HL (M_tot_3); (9.52, vlm_94551); L (M_tot_11); +∞ | 25 | 0.1 | *** |
| ligand_5766 | L-2-Amino-4-methylpentanoic acid (Leucine) | HL | C6H13N1O2 | CC(C)C[C@H](N)C(=O)O | −∞; H2L (M_tot_1); (2.32, vlm_94676); HL (M_tot_3); (9.58, vlm_94665); L (M_tot_7); +∞ | 25 | 0.1 | *** |
| ligand_5767 | L-2-Amino-3-methylpentanoic acid (Isoleucine) | HL | C6H13N1O2 | CC[C@H](C)[C@H](N)C(=O)O | −∞; H2L (M_tot_1); (2.26, vlm_94759); HL (M_tot_2); (9.6, vlm_94748); L (M_tot_7); +∞ | 25 | 0.1 | *** |
| ligand_5777 | L-2-Amino-3-phenylpropanoic acid (Phenylalanine) | HL | C9H11N1O2 | N[C@@H](Cc1ccccc1)C(=O)O | −∞; H2L (M_tot_1); (2.18, vlm_94993); HL (M_tot_1); (9.09, vlm_94975); L (M_tot_11); +∞ | 25 | 0.1 | *** |
| ligand_5802 | L-Aminobutanedioic acid (Aspartic acid) | H2L | C4H7N1O4 | N[C@@H](CC(=O)O)C(=O)O | −∞; H3L (M_tot_1); (1.95, vlm_95563); H2L (M_tot_1); (3.71, vlm_95550); HL (M_tot_9); (9.66, vlm_95537); L (M_tot_36); +∞ | 25 | 0.1 | *** |
| ligand_5804 | L-2-Aminopentanedioic acid (Glutamic acid) | H2L | C5H9N1O4 | N[C@@H](CCC(=O)O)C(=O)O | −∞; H3L (M_tot_1); (2.16, vlm_95761); H2L (M_tot_2); (4.15, vlm_95750); HL (M_tot_8); (9.58, vlm_95739); L (M_tot_17); +∞ | 25 | 0.1 | *** |
| ligand_5819 | L-2-Amino-3-(4-hydroxyphenyl)propanoic acid (Tyrosine) | H2L | C9H11N1O3 | N[C@@H](Cc1ccc(O)cc1)C(=O)O | −∞; H3L (M_tot_1); (2.24, vlm_96241); H2L (M_tot_1); (9.04, vlm_96234); HL (M_tot_10); (10.1, vlm_96227); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5828 | L-2-Amino-3-hydroxypropanoic acid (Serine) | HL | C3H7N1O3 | N[C@@H](CO)C(=O)O | −∞; H2L (M_tot_1); (2.16, vlm_96511); HL (M_tot_3); (9.05, vlm_96498); L (M_tot_16); +∞ | 25 | 0.1 | *** |
| ligand_5829 | L-2-Amino-3-hydroxybutanoic acid (Threonine) | HL | C4H9N1O3 | C[C@@H](O)[C@H](N)C(=O)O | −∞; H2L (M_tot_1); (2.2, vlm_96687); HL (M_tot_2); (8.94, vlm_96674); L (M_tot_11); +∞ | 25 | 0.1 | *** |
| ligand_5843 | L-2-Aminobutanedioic acid 4-amide (Asparagine) | HL | C4H8N2O3 | NC(=O)C[C@H](N)C(=O)O | −∞; H2L (M_tot_1); (2.16, vlm_97048); HL (M_tot_2); (8.73, vlm_97039); L (M_tot_14); +∞ | 25 | 0.1 | *** |
| ligand_5844 | L-2-Aminopentanedioic acid 5-amide (Glutamine) | HL | C5H10N2O3 | NC(=O)CC[C@H](N)C(=O)O | −∞; H2L (M_tot_1); (2.19, vlm_97179); HL (M_tot_1); (9, vlm_97170); L (M_tot_10); +∞ | 25 | 0.1 | *** |
| ligand_5863 | L-2-Amino-4-(methylthio)butanoic acid (Methionine) | HL | C5H11N1O2S1 | CSCC[C@H](N)C(=O)O | −∞; H2L (M_tot_1); (2.18, vlm_97809); HL (M_tot_3); (9.08, vlm_97802); L (M_tot_15); +∞ | 25 | 0.1 | *** |
| ligand_5887 | L-2,6-Diaminohexanoic acid (Lysine) | HL | C6H14N2O2 | NCCCC[C@H](N)C(=O)O | −∞; H3L (M_tot_1); (2.15, vlm_98379); H2L (M_tot_2); (9.15, vlm_98371); HL (M_tot_8); (10.66, vlm_98363); L (M_tot_4); +∞ | 25 | 0.1 | *** |
| ligand_5907 | L-2-Amino-3-(3-indolyl)propanoic acid (Tryptophan) | HL | C11H12N2O2 | N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O | −∞; H2L (M_tot_1); (2.37, vlm_99112); HL (M_tot_2); (9.33, vlm_99103); L (M_tot_12); +∞ | 25 | 0.1 | *** |
| ligand_5917 | L-2-Amino-5-guanidopentanoic acid (Arginine) | H2L | C6H14N4O2 | N=C(N)NCCC[C@H](N)C(=O)O | −∞; HL (M_tot_11); (-12.1, vlm_99378); L (M_tot_3); (2.03, vlm_99389); H2L (M_tot_2); (9, vlm_99382); HL (M_tot_11); +∞ | 25 | 0.1 | *** |
| ligand_5930 | L-Pyrrolidine-2-carboxylic acid (L-Proline) | HL | C5H9N1O2 | O=C(O)C1CCCN1 | −∞; H2L (M_tot_1); (1.89, vlm_99533); HL (M_tot_3); (10.46, vlm_99522); L (M_tot_10); +∞ | 25 | 0.1 | *** |

---
