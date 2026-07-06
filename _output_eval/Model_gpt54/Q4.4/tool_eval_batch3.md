# Q4.4 — Tool Results (batch 3)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Zn2+",
  "limit": 10
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

### Step 4: `build_system_catalog`
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

### Step 6: `search_pka_ligands`
**Args:**
```json
{
  "where": "(lc.ligand_class_name LIKE '%amino acid%')",
  "order_by": "lc.ligand_name_SRD ASC",
  "limit": 200
}
```

[summary]
## search_pka_ligands — 200 row(s)

| ligand_id | ligand_name | HxL_def | formula | smiles | pH_ladder | T°C_range | I(M)_range | similarity_score |
|-----------|-------------|---------|---------|--------|-----------|-----------|------------|------------------|
| ligand_5808 | (3-Aminopropyl)malonic acid | H2L | C6H11N1O4 | NCCCC(C(=O)O)C(=O)O | −∞; H3L (M_tot_1); (2.52, vlm_95888); H2L (M_tot_1); (4.86, vlm_95885); HL (M_tot_2); (10.45, vlm_95882); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_6126 | (Carboxymethyl)trimethylammonium (nitrate) (N,N,N,-Trimethy… | HL | C5H12N1O2/+ | C[N+](C)(C)CC(=O)O.O=[N+]([O-])[O-] | −∞; HL (M_tot_1); (-1.7, vlm_104099); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_5939 | (Carboxymethylamino)aceto-N-methylhydroxamic acid | H2L | C5H10N2O4 | CN(O)C(=O)CNCC(=O)O | −∞; H3L (M_tot_1); (-1.9, vlm_99848); H2L (M_tot_1); (7.58, vlm_99847); HL (M_tot_1); (9.22, vlm_99846); L (M_tot_2); +∞ | 20 | 0.1 | *** |
| ligand_5938 | (Carboxymethylamino)acetohydroxamic acid | H2L | C4H8N2O4 | O=C(O)CNCC(=O)NO | −∞; H3L (M_tot_1); (-1.8, vlm_99837); H2L (M_tot_1); (6.99, vlm_99836); HL (M_tot_1); (9.09, vlm_99835); L (M_tot_3); +∞ | 20 | 0.1 | *** |
| ligand_5956 | 1,2,3-Triazole-4,5-dicarboxylic acid | H2L | C4H3N3O4 | O=C(O)c1nn[nH]c1C(=O)O | −∞; H3L (M_tot_1); (-1.86, vlm_100065); H2L (M_tot_1); (5.9, vlm_100062); HL (M_tot_1); (9.3, vlm_100059); L (M_tot_3); +∞ | 25 | 0 | *** |
| ligand_5953 | 1,2,3-Triazole-4-carboxylic acid | HL | C3H3N3O2 | O=C(O)c1cn[nH]n1 | −∞; H2L (M_tot_1); (3.22, vlm_100050); HL (M_tot_1); (8.7, vlm_100047); L (M_tot_1); +∞ | 25 | 0 | *** |
| ligand_6033 | 1,4,7-Trimethyl-1,7-bis(4-carboxybenzyl)-1,4,7-triazaheptane | H2L | C20H29N3O4 | CN(CCN(C)Cc1ccc(C(=O)O)cc1)CCN(C)Cc1ccc(C(=O)O)cc1 | −∞; H5L (M_tot_1); (-1.6, vlm_101869); H4L (M_tot_1); (3.19, vlm_101866); H3L (M_tot_1); (3.7, vlm_101863); H2L (M_tot_1); (6.89, vlm_101860); HL (M_tot_1); (8.25, vlm_101857); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_5980 | 1,4-Diaminobutane-N,N'-diacetic acid | H2L | C8H16N2O4 | O=C(O)CNCCCCNCC(=O)O | −∞; H4L (M_tot_1); (-1.84, vlm_100526); H3L (M_tot_1); (2.52, vlm_100525); H2L (M_tot_1); (9.04, vlm_100524); HL (M_tot_1); (10.33, vlm_100523); L (M_tot_3); +∞ | 25 | 1 | *** |
| ligand_6028 | 1,5-Diazacyclooctane-N-acetic acid | HL | C8H16N2O2 | O=C(O)CN1CCCNCCC1 | −∞; HL (M_tot_1); (-11.8, vlm_101743); L (M_tot_2); (-1.7, vlm_101745); H2L (M_tot_1); (5.18, vlm_101744); HL (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5775 | 1-Aminocycloheptanecarboxylic acid | HL | C8H15N1O2 | NC1(C(=O)O)CCCCCC1 | −∞; H2L (M_tot_1); (2.59, vlm_94952); HL (M_tot_2); (10.46, vlm_94951); L (M_tot_5); +∞ | 20 | 0.1 | *** |
| ligand_5774 | 1-Aminocyclohexanecarboxylic acid | HL | C7H13N1O2 | NC1(C(=O)O)CCCCC1 | −∞; H2L (M_tot_1); (2.41, vlm_94941); HL (M_tot_1); (10.13, vlm_94940); L (M_tot_6); +∞ | 20 | 0.1 | *** |
| ligand_5773 | 1-Aminocyclopentanecarboxylic acid (Cycloleucine) | HL | C6H11N1O2 | NC1(C(=O)O)CCCC1 | −∞; H2L (M_tot_1); (2.4, vlm_94930); HL (M_tot_2); (10.31, vlm_94929); L (M_tot_5); +∞ | 20 | 0.1 | *** |
| ligand_5957 | 1-Phenyl-1,2,3-triazole-4,5-dicarboxylic acid | H2L | C10H8N3O4 | O=C(O)c1nnn(-c2ccccc2)c1C(=O)O | −∞; H2L (M_tot_1); (2.1, vlm_100075); HL (M_tot_1); (4.93, vlm_100072); L (M_tot_1); +∞ | 25 | 0 | *** |
| ligand_5954 | 1-Phenyl-1,2,3-triazole-4-carboxylic acid | HL | C9H8N3O2 | O=C(O)c1cn(-c2ccccc2)nn1 | −∞; HL (M_tot_1); (2.88, vlm_100053); L (M_tot_1); +∞ | 25 | 0 | *** |
| ligand_5959 | 2-(Carboxymethylaminomethyl)azole-4-sulfonic acid (N-(4-Sul… | H2L | C7H10N2O5S1 | O=C(O)CNCc1cc(S(=O)(=O)O)c[nH]1 | −∞; H2L (M_tot_1); (2.25, vlm_100094); HL (M_tot_1); (8.71, vlm_100093); L (M_tot_2); +∞ | 25 | 1 | *** |
| ligand_5769 | 2-Amino-2-methylpropanoic acid (2-Aminoisobutyric acid) | HL | C4H9N1O2 | CC(C)(N)C(=O)O | −∞; H2L (M_tot_1); (2.34, vlm_94845); HL (M_tot_2); (10.1, vlm_94835); L (M_tot_7); +∞ | 25 | 0.1 | *** |
| ligand_6002 | 2-Hydroxy-1,3-propylenediiminodibutanedioic acid (rac- or m… | H4L | C11H18N2O9 | O=C(O)CC(NCC(O)CNC(CC(=O)O)C(=O)O)C(=O)O | −∞; H4L (M_tot_1); (3.16, vlm_101238); H3L (M_tot_1); (4.08, vlm_101237); H2L (M_tot_1); (8.78, vlm_101236); HL (M_tot_1); (10.02, vlm_101235); L (M_tot_23); +∞ | 25 | 0.1 | *** |
| ligand_6001 | 2-Hydroxy-1,3-propylenediiminodipropanedioic acid | H4L | C9H14N2O9 | O=C(O)C(NCC(O)CNC(C(=O)O)C(=O)O)C(=O)O | −∞; H4L (M_tot_1); (2.41, vlm_101215); H3L (M_tot_1); (3.4, vlm_101214); H2L (M_tot_1); (8.9, vlm_101213); HL (M_tot_1); (10.4, vlm_101212); L (M_tot_8); +∞ | 25 | 0.1 | *** |
| ligand_5966 | 2-Hydroxy-3-(4-imidazolyl)propanoic acid | HL | C6H8N2O3 | O=C(O)C(O)Cc1c[nH]cn1 | −∞; H2L (M_tot_1); (3, vlm_100192); HL (M_tot_1); (7.31, vlm_100189); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5932 | 2-Indolecarboxylic acid | HL | C9H7N1O2 | O=C(O)c1cc2ccccc2[nH]1 | −∞; HL (M_tot_1); (3.68, vlm_99629); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_6012 | 3,3',5,5'-Tetramethyl-2,2'-dipyrrolmethene-4,4'-dicarboxyli… | H2L | C15H14N2O4 | CC1=C(C(=O)O)C(C)/C(=C/c2[nH]c(C)c(C(=O)O)c2C)=N1 | −∞; HL (M_tot_1); (-16.1, vlm_101398); L (M_tot_3); (3.6, vlm_101401); H3L (M_tot_1); (4.2, vlm_101400); H2L (M_tot_1); (8.03, vlm_101399); HL (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5940 | 3-(2-Hydroxyethylamino)propanoic acid | HL | C5H11N1O3 | O=C(O)CCNCCO | −∞; H2L (M_tot_1); (3.4, vlm_99853); HL (M_tot_1); (9.72, vlm_99852); L (M_tot_4); +∞ | 20 | 0.1 | *** |
| ligand_6026 | 3-(3-Hydroxy-4-oxo-1,4-dihydro-1-pyridinyl)propanoic acid (… | HL | C8H9N1O4 | O=C(O)CCn1ccc(=O)c(O)c1 | −∞; H3L (M_tot_1); (2.8, vlm_101708); H2L (M_tot_1); (3.84, vlm_101707); HL (M_tot_1); (8.79, vlm_101706); L (M_tot_5); +∞ | 37 | 0.15 | *** |
| ligand_5965 | 3-(4-Imidazolyl)propanoic acid | HL | C6H8N2O2 | O=C(O)CCc1c[nH]cn1 | −∞; H2L (M_tot_1); (3.83, vlm_100178); HL (M_tot_1); (7.44, vlm_100175); L (M_tot_4); +∞ | 25 | 0.1 | *** |
| ligand_5982 | 3-(Carboxymethyl)-2-oxo-1,4-diazacyclohexane-1-butanedioic … | H3L | C12H14N2O7 | O=C(O)CC1NCCN(C(CC(=O)O)C(=O)O)C1=O | −∞; H3L (M_tot_1); (3.38, vlm_100567); H2L (M_tot_1); (4.39, vlm_100553); HL (M_tot_4); (7, vlm_100539); L (M_tot_7); +∞ | 25 | 0.1 | *** |
| ligand_5788 | 3-Aminopropanoic acid (beta-Alanine) | HL | C3H7N1O2 | NCCC(=O)O | −∞; H2L (M_tot_1); (3.51, vlm_95222); HL (M_tot_3); (10.08, vlm_95204); L (M_tot_11); +∞ | 25 | 0.1 | *** |
| ligand_6004 | 4,7,10-Triazatridecanedioic acid [Iminobis(ethyleneiminopro… | H2L | C10H21N3O4 | O=C(O)CCNCCNCCNCCC(=O)O | −∞; H5L (M_tot_1); (2.98, vlm_101287); H4L (M_tot_1); (3.55, vlm_101286); H3L (M_tot_1); (4.4, vlm_101285); H2L (M_tot_1); (9.31, vlm_101284); HL (M_tot_1); (9.99, vlm_101283); L (M_tot_2); +∞ | 25 | 0.5 | *** |
| ligand_5797 | 4-Aminobutanoic acid | HL | C4H9N1O2 | NCCCC(=O)O | −∞; H2L (M_tot_1); (4.02, vlm_95418); HL (M_tot_5); (10.35, vlm_95408); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_5964 | 4-Imidazolylacetic acid | HL | C5H6N2O2 | O=C(O)Cc1c[nH]cn1 | −∞; H2L (M_tot_1); (3.1, vlm_100166); HL (M_tot_1); (7.26, vlm_100165); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_5875 | 5-Amino-3-thiapentanoic acid (S-2-Aminoethylmercaptoacetic … | HL | C5H11N1O2S1 | NCCSCC(=O)O | −∞; H2L (M_tot_1); (3.18, vlm_98012); HL (M_tot_2); (9.53, vlm_98009); L (M_tot_4); +∞ | 25 | 0.5 | *** |
| ligand_5798 | 5-Aminopentanoic acid | HL | C5H11N1O2 | NCCCCC(=O)O | −∞; H2L (M_tot_1); (4.27, vlm_95469); HL (M_tot_1); (10.766, vlm_95464); L (M_tot_3); +∞ | 25 | 0 | *** |
| ligand_5955 | 5-Methyl-1-phenyl-1,2,3-triazole-4-carboxylic acid | HL | C10H10N3O2 | Cc1c(C(=O)O)nnn1-c1ccccc1 | −∞; HL (M_tot_1); (3.73, vlm_100056); L (M_tot_1); +∞ | 25 | 0 | *** |
| ligand_6031 | 5-Thia-2,8-diazanonane-N,N'-diacetic acid | H2L | C10H20N2O4S1 | CN(CCSCCN(C)CC(=O)O)CC(=O)O | −∞; H4L (M_tot_1); (-1.3, vlm_101822); H3L (M_tot_1); (2.2, vlm_101819); H2L (M_tot_1); (8.24, vlm_101816); HL (M_tot_1); (9.3, vlm_101813); L (M_tot_10); +∞ | 25 | 0.1 | *** |
| ligand_5876 | 6-Amino-3-thiahexanoic acid (S-3-Aminopropylmercaptoacetic … | HL | C6H13N1O2S1 | NCCCSCC(=O)O | −∞; H2L (M_tot_1); (3.35, vlm_98044); HL (M_tot_2); (10.19, vlm_98041); L (M_tot_3); +∞ | 25 | 0.5 | *** |
| ligand_5877 | 6-Amino-4-thiahexanoic acid (S-2-Aminoethyl-3-mercaptopropa… | HL | C6H13N1O2S1 | NCCSCCC(=O)O | −∞; HL (M_tot_2); (9.54, vlm_98062); L (M_tot_4); +∞ | 20 | 0.1 | *** |
| ligand_5799 | 6-Aminohexanoic acid | HL | C6H13N1O2 | NCCCCCC(=O)O | −∞; H2L (M_tot_1); (4.373, vlm_95495); HL (M_tot_2); (10.804, vlm_95486); L (M_tot_4); +∞ | 25 | 0 | *** |
| ligand_6003 | 6-Oxa-3,9-diazaundecanedioic acid [Oxybis(ethyleneiminoacet… | H2L | C8H16N2O5 | O=C(O)CNCCOCCNCC(=O)O | −∞; H4L (M_tot_1); (-1.9, vlm_101277); H3L (M_tot_1); (2.6, vlm_101276); H2L (M_tot_1); (8.65, vlm_101275); HL (M_tot_1); (9.61, vlm_101274); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_5800 | 7-Aminoheptanoic acid | HL | C7H15N1O2 | NCCCCCCC(=O)O | −∞; H2L (M_tot_1); (4.502, vlm_95520); HL (M_tot_1); +∞ | 25 | 0 | *** |
| ligand_5760 | Aminoacetic acid (Glycine) | HL | C2H5N1O2 | NCC(=O)O | −∞; H2L (M_tot_1); (2.33, vlm_93627); HL (M_tot_20); (9.57, vlm_93606); L (M_tot_43); +∞ | 25 | 0.1 | *** |
| ligand_5801 | Aminopropanedioic acid (Aminomalonic acid) | H2L | C3H5N1O4 | NC(C(=O)O)C(=O)O | −∞; H3L (M_tot_1); (-1.8, vlm_95531); H2L (M_tot_1); (2.94, vlm_95527); HL (M_tot_1); (9.22, vlm_95523); L (M_tot_4); +∞ | 25 | 0.1 | *** |
| ligand_5981 | Bis(carboxymethyliminomethyl)phosphinic acid | H3L | C6H13N2O6P1 | O=C(O)CNCP(=O)(O)CNCC(=O)O | −∞; H3L (M_tot_1); (2.1, vlm_100537); H2L (M_tot_1); (6.55, vlm_100536); HL (M_tot_1); (9, vlm_100535); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_5857 | D-2-Amino-3-mercapto-3-methylbutanoic acid (Penicillamine) | H2L | C5H11N1O2S1 | CC(C)(S)[C@H](N)C(=O)O | −∞; H3L (M_tot_1); (-1.9, vlm_97563); H2L (M_tot_1); (7.96, vlm_97556); HL (M_tot_9); (10.67, vlm_97549); L (M_tot_14); +∞ | 25 | 0.1 | *** |
| ligand_5891 | D-3,3'-Dithiobis(2-amino-3-methylbutanoic acid) (Penicillam… | H2L | C10H20N2O4S2 | CC(C)(SSC(C)(C)C(N)C(=O)O)C(N)C(=O)O | −∞; H4L (M_tot_1); (-1.3, vlm_98611); H3L (M_tot_1); (2.04, vlm_98609); H2L (M_tot_1); (7.77, vlm_98606); HL (M_tot_5); (8.74, vlm_98603); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_5816 | D-3-Amino-3-carboxypropanohydroxamic acid (Asparagine hydro… | H2L | C4H8N2O4 | NC(CC(=O)NO)C(=O)O | −∞; H3L (M_tot_1); (2.18, vlm_96046); H2L (M_tot_1); (8.15, vlm_96045); HL (M_tot_1); (9.37, vlm_96044); L (M_tot_4); +∞ | 25 | 0.5 | *** |
| ligand_5768 | D-allo-2-Amino-3-methylpentanoic acid (D-allo-Isoleucine) | HL | C6H13N1O2 | CC[C@H](C)[C@@H](N)C(=O)O | −∞; H2L (M_tot_1); (2.2, vlm_94822); HL (M_tot_1); (9.62, vlm_94819); L (M_tot_3); +∞ | 25 | 0.1 | *** |
| ligand_5837 | D-gluco-2-Amino-3,4,5,6-tetrahydroxyhexanoic acid (D-Glucos… | HL | C6H13N1O6 | N[C@@H](C(=O)O)[C@@H](O)[C@H](O)[C@H](O)CO | −∞; H2L (M_tot_1); (2.2, vlm_96988); HL (M_tot_1); (9.08, vlm_96985); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_5924 | DL-(4-Amino-4-carboxybutyl)trimethylammonium ion (N(5)-Trim… | HL | C8H19N2O2/+ | C[N+](C)(C)CCCC(N)C(=O)O | −∞; H2L (M_tot_1); (-1.8, vlm_99448); HL (M_tot_1); (8.7, vlm_99447); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_5942 | DL-1,3-Thiazolidine-4-carboxylic acid (DL-Thiaproline) | HL | C4H7N1O2S1 | O=C(O)C1CSCN1 | −∞; HL (M_tot_1); (-6.11, vlm_99933); L (M_tot_8); (-1.5, vlm_99935); HL (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6051 | DL-1-Ethylethylenedinitrilotetraacetic acid N,N'-diamide | H2L | C12H22N4O6 | CCC(CN(CC(N)=O)CC(=O)O)N(CC(N)=O)CC(=O)O | −∞; H3L (M_tot_1); (-1.7, vlm_102336); H2L (M_tot_2); (3.7, vlm_102335); HL (M_tot_2); (7.58, vlm_102334); L (M_tot_9); +∞ | 37 | 0.15 | *** |
| ligand_6050 | DL-1-Methylethylenedinitrilotetraacetic acid N,N'-diamide | H2L | C11H20N4O6 | CC(CN(CC(N)=O)CC(=O)O)N(CC(N)=O)CC(=O)O | −∞; H3L (M_tot_1); (-1.7, vlm_102305); H2L (M_tot_1); (-1.5, vlm_102306); H3L (M_tot_1); (3.8, vlm_102304); HL (M_tot_1); (7.56, vlm_102303); L (M_tot_10); +∞ | 37 | 0.15 | *** |
| ligand_5993 | DL-2,3-Diaminopropanoic-N,N'-dipropanedioic acid | H4L | C9H12N2O10 | O=C(O)C(CNC(C(=O)O)C(=O)O)NC(C(=O)O)C(=O)O | −∞; H5L (M_tot_1); (-1.6, vlm_101014); H4L (M_tot_1); (2.45, vlm_101013); H3L (M_tot_1); (2.98, vlm_101012); H2L (M_tot_1); (6.55, vlm_101011); HL (M_tot_1); (9.71, vlm_101010); L (M_tot_26); +∞ | 25 | 0.1 | *** |
| ligand_5889 | DL-2,6-Diamino-5-hydroxyhexanoic acid | HL | C6H12N2O5 | NCC(O)CCC(N)C(=O)O | −∞; H3L (M_tot_1); (2.1, vlm_98513); H2L (M_tot_1); (8.84, vlm_98509); HL (M_tot_7); (9.79, vlm_98505); L (M_tot_3); +∞ | 25 | 0.1 | *** |
| ligand_5888 | DL-2,7-Diaminooctanedioic acid | HL | C8H16N2O4 | NC(CCCCC(N)C(=O)O)C(=O)O | −∞; H4L (M_tot_1); (-1.8, vlm_98498); H3L (M_tot_1); (2.62, vlm_98497); H2L (M_tot_1); (9.23, vlm_98496); HL (M_tot_2); (9.89, vlm_98495); L (M_tot_2); +∞ | 20 | 0.1 | *** |
| ligand_5878 | DL-2-(Acetylamino)-3-(2-aminoethylthio)propanoic acid | HL | C7H14N2O3S1 | CC(=O)NC(CSCCN)C(=O)O | −∞; HL (M_tot_1); (9.39, vlm_98094); L (M_tot_1); +∞ | 20 | 0.1 | *** |
| ligand_5825 | DL-2-Amino-2-(3,4-dihydroxyphenyl)acetic acid (DOPG) | H3L | C8H9N1O4 | NC(C(=O)O)c1ccc(O)c(O)c1 | −∞; HL (M_tot_1); (-13.6, vlm_96379); L (M_tot_1); (2, vlm_96382); H3L (M_tot_1); (8.56, vlm_96381); H2L (M_tot_2); (9.75, vlm_96380); HL (M_tot_1); +∞ | 25 | 1 | *** |
| ligand_5805 | DL-2-Amino-2-methylpentanedioic acid (2-Methylglutamic acid) | H2L | C6H11N1O4 | C[C@](N)(CCC(=O)O)C(=O)O | −∞; H2L (M_tot_1); (4.05, vlm_95867); HL (M_tot_1); (9.72, vlm_95866); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_5783 | DL-2-Amino-3-(2-chlorophenyl)propanoic acid (DL-3-(2-Chloro… | HL | C9H10Cl1N1O2 | N[C@@H](Cc1ccccc1Cl)C(=O)O | −∞; H2L (M_tot_1); (2.23, vlm_95183); HL (M_tot_1); (8.94, vlm_95182); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5780 | DL-2-Amino-3-(2-fluorophenyl)propanoic acid (DL-3-(2-Fluoro… | HL | C9H10F1N1O2 | N[C@@H](Cc1ccccc1F)C(=O)O | −∞; H2L (M_tot_1); (2.12, vlm_95166); HL (M_tot_1); (9.01, vlm_95163); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5817 | DL-2-Amino-3-(2-hydroxyphenyl)propanoic acid (o-Tyrosine) | H2L | C9H11N1O3 | NC(Cc1ccccc1O)C(=O)O | −∞; H3L (M_tot_1); (2.41, vlm_96078); H2L (M_tot_1); (8.67, vlm_96074); HL (M_tot_6); (11.01, vlm_96070); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_5860 | DL-2-Amino-3-(2-mercaptoimidazo-4-yl)propanoic acid (Thiohi… | H2L | C6H9N3O2S1 | NC(Cc1cnc(S)[nH]1)C(=O)O | −∞; HL (M_tot_1); (-11.77, vlm_97676); L (M_tot_9); (8.59, vlm_97679); HL (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5855 | DL-2-Amino-3-(3,4-dimethoxyphenyl)propanoic acid (3,4-Dimet… | HL | C11H15N1O4 | COc1ccc(C[C@H](N)C(=O)O)cc1OC | −∞; H2L (M_tot_1); (2.37, vlm_97370); HL (M_tot_1); (9.02, vlm_97369); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5784 | DL-2-Amino-3-(3-chlorophenyl)propanoic acid (DL-3-(3-Chloro… | HL | C9H10Cl1N1O2 | N[C@@H](Cc1cccc(Cl)c1)C(=O)O | −∞; H2L (M_tot_1); (2.17, vlm_95185); HL (M_tot_1); (8.91, vlm_95184); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5781 | DL-2-Amino-3-(3-fluorophenyl)propanoic acid (DL-3-(3-Fluoro… | HL | C9H10F1N1O2 | N[C@@H](Cc1cccc(F)c1)C(=O)O | −∞; H2L (M_tot_1); (2.1, vlm_95172); HL (M_tot_1); (8.98, vlm_95169); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5822 | DL-2-Amino-3-(3-hydroxy-4-methoxyphenyl)propanoic acid | H2L | C10H13N1O4 | COc1ccc(CC(N)C(=O)O)cc1O | −∞; H3L (M_tot_1); (2.23, vlm_96366); H2L (M_tot_1); (8.84, vlm_96365); HL (M_tot_1); (10.12, vlm_96364); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5818 | DL-2-Amino-3-(3-hydroxyphenyl)propanoic acid (m-Tyrosine) | H2L | C9H11N1O3 | N[C@@H](Cc1cccc(O)c1)C(=O)O | −∞; H3L (M_tot_1); (2.22, vlm_96149); H2L (M_tot_1); (8.95, vlm_96145); HL (M_tot_6); (10.04, vlm_96141); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5921 | DL-2-Amino-3-(4-(aminomethyl)phenyl)propanoic acid | HL | C10H13N2O2 | NCc1ccc(CC(N)C(=O)O)cc1 | −∞; H2L (M_tot_1); (8.4, vlm_99444); HL (M_tot_1); (8.42, vlm_99443); L (M_tot_1); +∞ | 37 | 0.15 | *** |
| ligand_5922 | DL-2-Amino-3-(4-(dimethylamino)phenyl)propanoic acid | HL | C11H15N1O2 | CN(C)c1ccc(CC(N)C(=O)O)cc1 | −∞; HL (M_tot_1); (8.86, vlm_99445); L (M_tot_1); +∞ | 37 | 0.15 | *** |
| ligand_5920 | DL-2-Amino-3-(4-aminophenyl)propanoic acid | HL | C9H11N1O2 | Nc1ccc(CC(N)C(=O)O)cc1 | −∞; HL (M_tot_1); (8.93, vlm_99442); L (M_tot_1); +∞ | 37 | 0.15 | *** |
| ligand_5785 | DL-2-Amino-3-(4-chlorophenyl)propanoic acid (DL-3-(4-Chloro… | HL | C9H10Cl1N1O2 | N[C@@H](Cc1ccc(Cl)cc1)C(=O)O | −∞; H2L (M_tot_1); (2.08, vlm_95187); HL (M_tot_1); (8.96, vlm_95186); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5782 | DL-2-Amino-3-(4-fluorophenyl)propanoic acid (DL-3-(4-Fluoro… | HL | C9H10F1N1O2 | N[C@@H](Cc1ccc(F)cc1)C(=O)O | −∞; H2L (M_tot_1); (2.13, vlm_95178); HL (M_tot_1); (9.05, vlm_95175); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5919 | DL-2-Amino-3-(4-guanidinomethylphenyl)propanoic acid | HL | C12H16N4O2 | N=C(N)NCc1ccc(CC(N)C(=O)O)cc1 | −∞; H2L (M_tot_1); (8.83, vlm_99441); HL (M_tot_1); +∞ | 37 | 0.15 | *** |
| ligand_5918 | DL-2-Amino-3-(4-guanidinophenyl)propanoic acid | HL | C10H14N4O2 | N=C(N)Nc1ccc(CC(N)C(=O)O)cc1 | −∞; H2L (M_tot_1); (8.44, vlm_99440); HL (M_tot_1); (10.91, vlm_99439); L (M_tot_1); +∞ | 37 | 0.15 | *** |
| ligand_5823 | DL-2-Amino-3-(4-hydroxy-3-methoxyphenyl)propanoic acid | H2L | C10H13N1O4 | COc1cc(CC(N)C(=O)O)ccc1O | −∞; H3L (M_tot_1); (2.13, vlm_96369); H2L (M_tot_1); (8.78, vlm_96368); HL (M_tot_1); (10.14, vlm_96367); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5912 | DL-2-Amino-3-(5-hydroxo-4-oxo-1,4-dihydro-2-pyridinyl)propa… | HL | C8H10N2O4 | NC(Cc1cc(=O)c(O)c[nH]1)C(=O)O | −∞; H4L (M_tot_1); (-1.3, vlm_99290); H3L (M_tot_1); (3.01, vlm_99289); H2L (M_tot_1); (7.72, vlm_99288); HL (M_tot_2); (9.17, vlm_99287); L (M_tot_4); +∞ | 37 | 0.15 | *** |
| ligand_5913 | DL-2-Amino-3-(5-hydroxo-6-oxo-1,6-dihydro-2-pyridinyl)propa… | HL | C8H10N2O4 | NC(Cc1ccc(O)c(=O)[nH]1)C(=O)O | −∞; H3L (M_tot_1); (-1.9, vlm_99310); H2L (M_tot_1); (7.85, vlm_99309); HL (M_tot_3); (9.01, vlm_99308); L (M_tot_5); +∞ | 37 | 0.15 | *** |
| ligand_5909 | DL-2-Amino-3-(5-hydroxy-3-indolyl)propanoic acid (5-Hydroxy… | HL | C11H12N2O3 | NC(Cc1c[nH]c2ccc(O)cc12)C(=O)O | −∞; H3L (M_tot_1); (2.51, vlm_99238); H2L (M_tot_1); (9.49, vlm_99237); HL (M_tot_6); (10.54, vlm_99236); L (M_tot_1); +∞ | 20 | 0.5 | *** |
| ligand_5910 | DL-2-Amino-3-(6-oxo-1,6-dihydro-2-pyridinyl)propanoic acid | HL | C8H10N2O3 | NC(Cc1cccc(=O)[nH]1)C(=O)O | −∞; H2L (M_tot_1); (-1.8, vlm_99252); HL (M_tot_1); (7.8, vlm_99251); L (M_tot_3); (11.7, vlm_99250); H-1L (M_tot_1); +∞ | 37 | 0.15 | *** |
| ligand_5812 | DL-2-Amino-3-(phenylphospho)propanoic acid | H3L | C9H12N1O6P1 | NC(COP(=O)(O)Oc1ccccc1)C(=O)O | −∞; H2L (M_tot_1); (2.13, vlm_95973); HL (M_tot_1); (8.79, vlm_95972); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5779 | DL-2-Amino-3-chlorobutanoic acid | HL | C4H8Cl1N1O2 | CC(Cl)C(N)C(=O)O | −∞; H2L (M_tot_1); (-1.5, vlm_95156); HL (M_tot_1); (8.07, vlm_95155); L (M_tot_4); +∞ | 25 | 0.1 | *** |
| ligand_5778 | DL-2-Amino-3-chloropropanoic acid (3-Chloroalanine) | HL | C3H6Cl1N1O2 | N[C@@H](CCl)C(=O)O | −∞; HL (M_tot_1); (8.18, vlm_95145); L (M_tot_4); +∞ | 25 | 0.1 | *** |

---

### Step 7: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND c.ligand_id IN (ligand_5760,ligand_5761,ligand_5802,ligand_5804,ligand_5828,ligand_5829,ligand_5843,ligand_5844,ligand_5856,ligand_5857,ligand_5859,ligand_5898,ligand_5765,ligand_5766,ligand_5767,ligand_5777,ligand_5819,ligand_5826))",
  "order_by": "c.ligand_name_SRD ASC, s.constant_type ASC, s.temperature_c ASC, s.ionic_strength_mol_l ASC",
  "limit": 300
}
```

[summary]
## search_stability — 200 row(s)

### ΔH — 7 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_208 | Zn^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 10 | 3 | 10~40 | 0~0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 6 | 3 | 25 | 0.1~3 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 5 | 5 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5843 | L-2-Aminobutanedioic acid 4… | HL | NC(=O)C[C@H](N)C(=O)O | 3 | 3 | 25 | 3 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5829 | L-2-Amino-3-hydroxybutanoic… | HL | C[C@@H](O)[C@H](N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5828 | L-2-Amino-3-hydroxypropanoi… | HL | N[C@@H](CO)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5777 | L-2-Amino-3-phenylpropanoic… | HL | N[C@@H](Cc1ccccc1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |

### logK — 15 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_208 | Zn^[2+] | ligand_5856 | L-2-Amino-3-mercaptopropano… | H2L | N[C@@H](CS)C(=O)O | 23 | 8 | 20~37 | 0.1~3 | *** | 4 |
| metal_208 | Zn^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 22 | 4 | 10~40 | 0~1 | *** | 7 |
| metal_208 | Zn^[2+] | ligand_5857 | D-2-Amino-3-mercapto-3-meth… | H2L | CC(C)(S)[C@H](N)C(=O)O | 18 | 8 | 20~37 | 0.1~3 | *** | 4 |
| metal_208 | Zn^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 18 | 6 | 25~37 | 0.1~3 | *** | 6 |
| metal_208 | Zn^[2+] | ligand_5828 | L-2-Amino-3-hydroxypropanoi… | HL | N[C@@H](CO)C(=O)O | 8 | 3 | 25~37 | 0.1~3 | *** | 3 |
| metal_208 | Zn^[2+] | ligand_5765 | L-2-Amino-3-methylbutanoic … | HL | CC(C)[C@H](N)C(=O)O | 8 | 4 | 25~37 | 0.1~0.5 | *** | 3 |
| metal_208 | Zn^[2+] | ligand_5826 | L-2-Amino-3-(3,4-dihydroxyp… | H3L | NC(Cc1ccc(O)c(O)c1)C(=O)O | 7 | 5 | 20~25 | 0.1~0.5 | *** | 3 |
| metal_208 | Zn^[2+] | ligand_5767 | L-2-Amino-3-methylpentanoic… | HL | CC[C@H](C)[C@H](N)C(=O)O | 6 | 4 | 25~37 | 0.15~0.5 | *** | 2 |
| metal_208 | Zn^[2+] | ligand_5766 | L-2-Amino-4-methylpentanoic… | HL | CC(C)C[C@H](N)C(=O)O | 6 | 4 | 25~37 | 0.1~0.15 | *** | 2 |
| metal_208 | Zn^[2+] | ligand_5843 | L-2-Aminobutanedioic acid 4… | HL | NC(=O)C[C@H](N)C(=O)O | 6 | 3 | 20~37 | 0.1~3 | *** | 3 |
| metal_208 | Zn^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 5 | 5 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5829 | L-2-Amino-3-hydroxybutanoic… | HL | C[C@@H](O)[C@H](N)C(=O)O | 5 | 3 | 25~37 | 0.1~0.15 | *** | 2 |
| metal_208 | Zn^[2+] | ligand_5804 | L-2-Aminopentanedioic acid … | H2L | N[C@@H](CCC(=O)O)C(=O)O | 5 | 2 | 25~37 | 0.15~1 | *** | 3 |
| metal_208 | Zn^[2+] | ligand_5844 | L-2-Aminopentanedioic acid … | HL | NC(=O)CC[C@H](N)C(=O)O | 5 | 3 | 25~37 | 0.15~3 | *** | 2 |
| metal_208 | Zn^[2+] | ligand_5777 | L-2-Amino-3-phenylpropanoic… | HL | N[C@@H](Cc1ccccc1)C(=O)O | 4 | 2 | 25~37 | 0.1~0.15 | *** | 2 |

### ΔS — 7 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_208 | Zn^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 5 | 3 | 25 | 0~0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 5 | 5 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 5 | 3 | 25 | 0.1~3 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5843 | L-2-Aminobutanedioic acid 4… | HL | NC(=O)C[C@H](N)C(=O)O | 3 | 3 | 25 | 3 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5829 | L-2-Amino-3-hydroxybutanoic… | HL | C[C@@H](O)[C@H](N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5828 | L-2-Amino-3-hydroxypropanoi… | HL | N[C@@H](CO)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5777 | L-2-Amino-3-phenylpropanoic… | HL | N[C@@H](Cc1ccccc1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |

---
