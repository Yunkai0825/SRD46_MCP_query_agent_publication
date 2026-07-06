# Q4.4 — Tool Results (batch 5)

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

### Step 4: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_208 AND c.ligand_class_name = 'Amino Acids'",
  "order_by": "s.constant_value DESC",
  "limit": 80
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 5: `search_ligands`
**Args:**
```json
{
  "ligand_class": "amino acid",
  "limit": 80,
  "exclude": "ligand_5760,ligand_5761,ligand_5762,ligand_5763,ligand_5764,ligand_5765,ligand_5766,ligand_5767,ligand_5768,ligand_5769,ligand_5770,ligand_5771,ligand_5772,ligand_5773,ligand_5774,ligand_5775,ligand_5776,ligand_5777,ligand_5778,ligand_5779,ligand_5780,ligand_5781,ligand_5782,ligand_5783,ligand_5784,ligand_5785,ligand_5786,ligand_5787,ligand_5788,ligand_5789,ligand_5790,ligand_5791,ligand_5792,ligand_5793,ligand_5794,ligand_5795,ligand_5796,ligand_5797,ligand_5798,ligand_5799,ligand_5800,ligand_5801,ligand_5802,ligand_5803,ligand_5804,ligand_5805,ligand_5806,ligand_5807,ligand_5808,ligand_5809,ligand_5810,ligand_5811,ligand_5812,ligand_5813,ligand_5814,ligand_5815,ligand_5816,ligand_5817,ligand_5818,ligand_5819,ligand_5820,ligand_5821,ligand_5822,ligand_5823,ligand_5824,ligand_5825,ligand_5826,ligand_5827,ligand_5828,ligand_5829,ligand_5830,ligand_5831,ligand_5832,ligand_5833,ligand_5834,ligand_5835,ligand_5836,ligand_5837,ligand_5838,ligand_5839"
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

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND c.ligand_class_name LIKE '%Amino%')",
  "order_by": "s.constant_value DESC",
  "limit": 30
}
```

[summary]
## search_stability — 30 row(s)

### ΔS — 16 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_208 | Zn^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 4 | 3 | 25 | 0~0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_8412 | Nitrilotris(methylenephosph… | H6L | O=P(O)(O)CN(CP(=O)(O)O)CP(=O)(O)O | 3 | 2 | 25 | 0~0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5843 | L-2-Aminobutanedioic acid 4… | HL | NC(=O)C[C@H](N)C(=O)O | 3 | 3 | 25 | 3 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5777 | L-2-Amino-3-phenylpropanoic… | HL | N[C@@H](Cc1ccccc1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5761 | L-2-Aminopropanoic acid (Al… | HL | C[C@H](N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5817 | DL-2-Amino-3-(2-hydroxyphen… | H2L | NC(Cc1ccccc1O)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5819 | L-2-Amino-3-(4-hydroxypheny… | H2L | N[C@@H](Cc1ccc(O)cc1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5818 | DL-2-Amino-3-(3-hydroxyphen… | H2L | N[C@@H](Cc1cccc(O)c1)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5837 | D-gluco-2-Amino-3,4,5,6-tet… | HL | N[C@@H](C(=O)O)[C@@H](O)[C@H](O)[C@H](O)CO | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5898 | L-2-Amino-3-(4-imidazolyl)p… | HL | N[C@@H](Cc1c[nH]cn1)C(=O)O | 2 | 1 | 25 | 0.1~3 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5975 | Ethylenediiminodiacetic aci… | H2L | O=C(O)CNCCNCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5828 | L-2-Amino-3-hydroxypropanoi… | HL | N[C@@H](CO)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5829 | L-2-Amino-3-hydroxybutanoic… | HL | C[C@@H](O)[C@H](N)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5907 | L-2-Amino-3-(3-indolyl)prop… | HL | N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5845 | L-2-Amino-6-(2-methylpropam… | HL | CC(C)C(=O)NCCCCC(N)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_5941 | L-4-Hydroxypyrrolidine-2-ca… | HL | O=C(O)C1CC(O)CN1 | 1 | 1 | 25 | 0.1 | *** | 0 |

---

### Step 9: `search_pka_ligands`
**Args:**
```json
{
  "where": "(lc.ligand_class_name LIKE '%Amino%' AND p.pKa > 7.5)",
  "order_by": "p.pKa DESC",
  "limit": 40
}
```

[summary]
## search_pka_ligands — 40 row(s)

| ligand_id | ligand_name | HxL_def | formula | smiles | pH_ladder | T°C_range | I(M)_range | similarity_score |
|-----------|-------------|---------|---------|--------|-----------|-----------|------------|------------------|
| ligand_5910 | DL-2-Amino-3-(6-oxo-1,6-dihydro-2-pyridinyl)propanoic acid | HL | C8H10N2O3 | NC(Cc1cccc(=O)[nH]1)C(=O)O | −∞; L (M_tot_3); (11.7, vlm_99250); H-1L (M_tot_1); +∞ | 37 | 0.15 | *** |
| ligand_8362 | 4-Amino-1-hydroxybutane-1,1-diphosphonic acid | H4L | C4H13N1O7P2 | NCCCC(O)(P(=O)(O)O)P(=O)(O)O | −∞; HL (M_tot_1); (11.6, vlm_142154); L (M_tot_3); +∞ | 25 | 0.1 | *** |
| ligand_8347 | Piperidine-2-phosphonic acid | H2L | C5H11N1O3P1 | O=P(O)(O)C1CCCCN1 | −∞; HL (M_tot_1); (11.31, vlm_142010); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_8354 | DL-1-Amino-2-(cyclohexylamino)ethylphosphonic acid | H2L | C9H20N2O3P1 | NC(CNC1CCCCC1)P(=O)(O)O | −∞; HL (M_tot_2); (11.1, vlm_142069); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_8346 | DL-1-Amino-2-(pentamethylenenitrilo)ethylphosphonic acid | H2L | C7H17N1O3P1 | NC(CN1CCCCC1)P(=O)(O)O | −∞; HL (M_tot_2); (11.05, vlm_142002); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_8343 | 3-Aminopropylphosphonic acid | H2L | C3H10N1O3P1 | NCCCP(=O)(O)O | −∞; HL (M_tot_1); (11.04, vlm_141979); L (M_tot_4); +∞ | 25 | 0.1 | *** |
| ligand_5817 | DL-2-Amino-3-(2-hydroxyphenyl)propanoic acid (o-Tyrosine) | H2L | C9H11N1O3 | NC(Cc1ccccc1O)C(=O)O | −∞; HL (M_tot_6); (11.01, vlm_96070); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_6037 | N,N'-Bis(2-hydroxybenzyl)ethylenedinitrilodiacetic acid (HB… | H4L | C20H24N2O6 | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)Cc1ccccc1O | −∞; H2L (M_tot_1); (11.01, vlm_101962); HL (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_8379 | N-Ethylaminomethylphosphonic acid | H2L | C3H10N1O3P1 | CCNCP(=O)(O)O | −∞; HL (M_tot_1); (11.01, vlm_142403); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_5934 | L-2-(Iminomethylamino)pentanedioic acid | H2L | C6H10N2O4 | N=CNC(CCC(=O)O)C(=O)O | −∞; HL (M_tot_1); (11, vlm_99641); L (M_tot_3); +∞ | 25 | 0.1 | *** |
| ligand_6039 | N,N"-Bis(2-hydroxybenzyl)diethylenetrinitrilo-N,N',N"-triac… | *** | C24H31N3O8 | *** | −∞; H2L (M_tot_1); (10.98, vlm_102077); HL (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_8342 | 2-Aminoethylphosphonic acid (b-Ala-P) | H2L | C2H8N1O3P1 | NCCP(=O)(O)O | −∞; HL (M_tot_7); (10.98, vlm_141949); L (M_tot_7); +∞ | 25 | 0.1 | *** |
| ligand_8393 | N,N-Dimethylaminomethylphosphonic acid | H2L | C3H10N1O3P1 | CN(C)CP(=O)(O)O | −∞; HL (M_tot_1); (10.98, vlm_142833); L (M_tot_11); +∞ | 25 | 0.1 | *** |
| ligand_6047 | N,N''-Bis(3-hydroxy-6-methyl-2-pyridinylmethyl)diethylenetr… | H5L | C24H33N5O8 | Cc1ccc(O)c(CN(CCN(CCN(CC(=O)O)Cc2nc(C)ccc2O)CC(=O)O)CC(=O)O)n1 | −∞; H2L (M_tot_1); (10.95, vlm_102254); HL (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5936 | L-N-(2-Hydroxybenzyl)-2-aminopropanoic acid | H2L | C10H13N1O2 | CC(NCc1ccccc1O)C(=O)O | −∞; HL (M_tot_1); (10.94, vlm_99662); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_5918 | DL-2-Amino-3-(4-guanidinophenyl)propanoic acid | HL | C10H14N4O2 | N=C(N)Nc1ccc(CC(N)C(=O)O)cc1 | −∞; HL (M_tot_1); (10.91, vlm_99439); L (M_tot_1); +∞ | 37 | 0.15 | *** |
| ligand_8378 | N-Methylaminomethylphosphonic acid (Sar-P) | H2L | C2H8N1O3P1 | CNCP(=O)(O)O | −∞; HL (M_tot_1); (10.91, vlm_142394); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_5995 | rac-Ethylenediiminobis[(2-hydroxyphenyl)acetic acid] (EHPG) | H4L | C18H20N2O6 | O=C(O)C(Cc1ccccc1O)NCCNC(Cc1ccccc1O)C(=O)O | −∞; H2L (M_tot_1); (10.87, vlm_101089); HL (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5996 | meso-Ethylenediiminobis[(2-hydroxyphenyl)acetic acid] (EHPG) | H4L | C18H20N2O6 | O=C(O)C(Cc1ccccc1O)NCCNC(Cc1ccccc1O)C(=O)O | −∞; H2L (M_tot_1); (10.85, vlm_101131); HL (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6057 | N,N',N''-Tris(carboxymethyl)diethylenetrinitrilobis(N-2-pro… | H5L | C20H39N5O10 | CC(C)N(O)C(=O)CN(CCN(CCN(CC(=O)O)CC(=O)N(O)C(C)C)CC(=O)O)CC(=O)O | −∞; HL (M_tot_1); (10.85, vlm_102431); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_8418 | N-(2-Aminoethyl)iminobis(methylenephosphonic acid) (Ethylen… | H4L | C4H14N2O6P2 | NCCN(CP(=O)(O)O)CP(=O)(O)O | −∞; HL (M_tot_1); (10.85, vlm_143528); L (M_tot_4); +∞ | 25 | 0.1 | *** |
| ligand_8442 | Ethylenebis(imino(2-hydroxyphenyl)methylenephosphonous acid) | H4L | C16H22N2O6P2 | O=[PH](O)C(NCCNC(c1ccccc1O)[PH](=O)O)c1ccccc1O | −∞; H2L (M_tot_1); (10.84, vlm_144038); HL (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6042 | N,N'-Bis(3-hydroxy-5-hydroxymethyl-2-methyl-4-pyridylmethyl… | H4L | C22H30N4O8 | Cc1ncc(CO)c(CN(CCN(CC(=O)O)Cc2c(CO)cnc(C)c2O)CC(=O)O)c1O | −∞; HL (M_tot_1); (10.82, vlm_102175); L (M_tot_8); +∞ | 25 | 0.1 | *** |
| ligand_8353 | DL-1-Amino-2-(methylamino)ethylphosphonic acid | H2L | C4H12N2O3P1 | CNCC(N)P(=O)(O)O | −∞; HL (M_tot_2); (10.82, vlm_142061); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_8406 | N-Benzyl-N-methylaminomethylenediphosphonic acid | H4L | C9H15N1O6P2 | CN(Cc1ccccc1)C(P(=O)(O)O)P(=O)(O)O | −∞; HL (M_tot_1); (10.82, vlm_143100); L (M_tot_4); +∞ | 25 | 0.1 | *** |
| ligand_6029 | N,N-Bis(2-aminoethyl)glycine | HL | C6H15N3O2 | NCCN(CCN)CC(=O)O | −∞; HL (M_tot_1); (10.81, vlm_101747); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_5799 | 6-Aminohexanoic acid | HL | C6H13N1O2 | NCCCCCC(=O)O | −∞; HL (M_tot_2); (10.804, vlm_95486); L (M_tot_4); +∞ | 25 | 0 | *** |
| ligand_8361 | 3-Amino-1-hydroxypropane-1,1-diphosphonic acid | H4L | C7H11N1O6P2 | NCCC(O)(P(=O)(O)O)P(=O)(O)O | −∞; HL (M_tot_1); (10.8, vlm_142147); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_8416 | 1-Hydroxy-3-(dimethylamino)propane-1,1-diphosphonic acid | H4L | C5H15N1O7P2 | CN(C)CCC(O)(P(=O)(O)O)P(=O)(O)O | −∞; HL (M_tot_1); (10.8, vlm_143492); L (M_tot_9); +∞ | 25 | 0.1 | *** |
| ligand_6040 | N,N'-Bis(2-mercaptoethyl)ethylenedinitrilodiacetic acid | H4L | C10H20N2O4S2 | O=C(O)CN(CCS)CCN(CCS)CC(=O)O | −∞; HL (M_tot_1); (10.79, vlm_102125); L (M_tot_6); +∞ | 25 | 0.1 | *** |
| ligand_8380 | Iminobis(methylenephosphonic acid) (IDP) | H4L | C2H9N1O6P2 | O=P(O)(O)CNCP(=O)(O)O | −∞; HL (M_tot_2); (10.79, vlm_142412); L (M_tot_14); +∞ | 25 | 0.1 | *** |
| ligand_8381 | N-Methylaminomethylenediphosphonic acid | H4L | C2H9N1O6P2 | CNC(P(=O)(O)O)P(=O)(O)O | −∞; HL (M_tot_1); (10.78, vlm_142528); L (M_tot_3); +∞ | 25 | 0.1 | *** |
| ligand_5798 | 5-Aminopentanoic acid | HL | C5H11N1O2 | NCCCCC(=O)O | −∞; HL (M_tot_1); (10.766, vlm_95464); L (M_tot_3); +∞ | 25 | 0 | *** |
| ligand_5813 | DL-2-Amino-3-phosphonopropanoic acid | H4L | C3H8N1O5P1 | NC(CP(=O)(O)O)C(=O)O | −∞; HL (M_tot_4); (10.74, vlm_95974); L (M_tot_7); +∞ | 25 | 0.1 | *** |
| ligand_6010 | Ethane-1,1,1-tris(methyleneiminoacetic acid) | H3L | C11H21N3O6 | CC(CNCC(=O)O)(CNCC(=O)O)CNCC(=O)O | −∞; HL (M_tot_1); (10.73, vlm_101376); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_6044 | N-(2-Hydroxybenzyl)-N'-(3-hydroxy-5-hydroxymethyl-2-methyl-… | H4L | C21H27N3O7 | Cc1ncc(CO)c(CN(CCN(CC(=O)O)Cc2ccccc2O)CC(=O)O)c1O | −∞; H2L (M_tot_1); (10.73, vlm_102216); HL (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_8397 | (Pentamethyleneimino)methylenediphosphonic acid (N-(Diphosp… | H4L | C6H15N1O6P2 | O=P(O)(O)C(N1CCCCC1)P(=O)(O)O | −∞; HL (M_tot_1); (10.72, vlm_142903); L (M_tot_6); +∞ | 25 | 0.1 | *** |
| ligand_8431 | Oxybis[ethylenenitrilobis(methylenephosphonic acid)] | H4L | C8H24N2O13P4 | O=P(O)(O)CN(CCOCCN(CP(=O)(O)O)CP(=O)(O)O)CP(=O)(O)O | −∞; HL (M_tot_1); (10.72, vlm_143856); L (M_tot_5); +∞ | 20 | 0.1 | *** |
| ligand_5857 | D-2-Amino-3-mercapto-3-methylbutanoic acid (Penicillamine) | H2L | C5H11N1O2S1 | CC(C)(S)[C@H](N)C(=O)O | −∞; HL (M_tot_9); (10.67, vlm_97549); L (M_tot_14); +∞ | 25 | 0.1 | *** |
| ligand_5989 | trans-1,2-Cyclohexylenediiminodibutanedioic acid | H4L | C14H22N2O8 | O=C(O)CC(N[C@@H]1CCCC[C@H]1NC(CC(=O)O)C(=O)O)C(=O)O | −∞; HL (M_tot_1); (10.67, vlm_100945); L (M_tot_17); +∞ | 25 | 0.1 | *** |

---
