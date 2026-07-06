# Q5.1.3 — Tool Results (batch 4)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "iron",
  "limit": 20
}
```

[summary]
## search_metals — 2 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_61 | Fe^[3+] | Fe | 3 | ✓ | [Fe+3] | InChI=1S/Fe/q+3 | beta_totN_128 | ligand_totN_406 | vlm_totN_1473 |
| metal_62 | Fe^[2+] | Fe | 2 | ✓ | [Fe+2] | InChI=1S/Fe/q+2 | beta_totN_57 | ligand_totN_217 | vlm_totN_667 |

---

### Step 3: `search_metals`
**Args:**
```json
{
  "name": "copper",
  "limit": 20
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

### Step 5: `search_ligands`
**Args:**
```json
{
  "name": "EDTA",
  "limit": 20
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 5 SQL matches · showing 5 · limit 20

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6118 | 6,11,18,23-Tetraoxo-1,4,7,10,13,16,19,… (24edtaen) | *** | Aza macrocycles with car… | 15 | *** | (-inf, H4L, 3.3, H3L, 4.18, H2L, 7.26, HL, 7.78, L, +inf) |
| ligand_6275 | N-(2-Hydroxyethyl)ethylenedinitrilotriace… (HEDTA) | H3L | EDTA and derivatives | 237 | `O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O` | (-inf, H3L, 2.62, H2L, 5.38, HL, 9.7, L, +inf) |
| ligand_6277 | Ethylenedinitrilotetraacetic acid (EDTA) | H4L | EDTA and derivatives | 596 | `O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O` | (-inf, H5L, -1.5, H4L, 2, H3L, 2.69, H2L, 6.13, HL, 9.52, L, +inf) |
| ligand_6335 | Oxybis(ethylenenitrilo)tetraacetic acid (EEDTA) | H4L | EDTA and derivatives | 124 | `O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O` | (-inf, H4L, -1.8, H3L, 2.76, H2L, 8.75, HL, 9.39, L, +inf) |
| ligand_6348 | Thiobis(ethylenenitrilo)tetraacetic acid (TEDTA) | H4L | EDTA and derivatives | 101 | `O=C(O)CN(CCSCCN(CC(=O)O)CC(=O)O)CC(=O)O` | (-inf, H4L, 2, H3L, 2.68, H2L, 8.37, HL, 9.31, L, +inf) |

### Functional groups across all SQL matches (4 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 4 | 100% |
| tertiary_amine | 4 | 100% |
| ether | 1 | 25% |
| hydroxyl | 1 | 25% |
| thioether | 1 | 25% |

---

### Step 6: `search_ligands`
**Args:**
```json
{
  "name": "NTA",
  "limit": 20
}
```

[summary]
## search_ligands — 20 result(s)

**stats:** 298 SQL matches · showing 20 · limit 20

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5763 | DL-2-Aminopentanoic acid (Norvaline) | HL | Amino Acids | 35 | `CCC[C@H](N)C(=O)O` | (-inf, H2L, 2.31, HL, 9.65, L, +inf) |
| ligand_5766 | L-2-Amino-4-methylpentanoic acid (Leucine) | HL | Amino Acids | 49 | `CC(C)C[C@H](N)C(=O)O` | (-inf, H2L, 2.32, HL, 9.58, L, +inf) |
| ligand_5767 | L-2-Amino-3-methylpentanoic acid (Isoleucine) | HL | Amino Acids | 51 | `CC[C@H](C)[C@H](N)C(=O)O` | (-inf, H2L, 2.26, HL, 9.6, L, +inf) |
| ligand_5768 | D-allo-2-Amino-3-methylpentan… (D-allo-Isoleucine) | HL | Amino Acids | 16 | `CC[C@H](C)[C@@H](N)C(=O)O` | (-inf, H2L, 2.2, HL, 9.62, L, +inf) |
| ligand_5773 | 1-Aminocyclopentanecarboxylic acid (Cycloleucine) | HL | Amino Acids | 11 | `NC1(C(=O)O)CCCC1` | (-inf, H2L, 2.4, HL, 10.31, L, +inf) |
| ligand_5790 | cis-2-Aminocyclopentane-1-carboxylic acid | HL | Amino Acids | 6 | `N[C@H]1CCC[C@H]1C(=O)O` | (-inf, H2L, 3.54, HL, 10.1, L, +inf) |
| ligand_5791 | trans-2-Aminocyclopentane-1-carboxylic acid | HL | Amino Acids | 3 | `N[C@@H]1CCC[C@H]1C(=O)O` | (-inf, H2L, 3.75, HL, 9.91, L, +inf) |
| ligand_5798 | 5-Aminopentanoic acid | HL | Amino Acids | 20 | `NCCCCC(=O)O` | (-inf, H2L, 4.27, HL, 10.766, L, +inf) |
| ligand_5804 | L-2-Aminopentanedioic acid (Glutamic acid) | H2L | Amino Acids | 94 | `N[C@@H](CCC(=O)O)C(=O)O` | (-inf, H3L, 2.16, H2L, 4.15, HL, 9.58, L, +inf) |
| ligand_5805 | DL-2-Amino-2-methylpentan… (2-Methylglutamic acid) | H2L | Amino Acids | 4 | `C[C@](N)(CCC(=O)O)C(=O)O` | (-inf, H2L, 4.05, HL, 9.72, L, +inf) |
| ligand_5807 | DL-2-Amino-3-hydroxypent… (3-Hydroxyglutamic acid) | H2L | Amino Acids | 8 | `N[C@H](C(=O)O)C(O)CC(=O)O` | (-inf, H3L, 2.09, H2L, 4.08, HL, 9.06, L, +inf) |
| ligand_5840 | DL-2-Aminopentanedioic acid 5… (5-Ethyl glutamate) | HL | Amino Acids | 2 | `CCOC(=O)CC[C@H](N)C(=O)O` | (-inf, H2L, 2.15, HL, 9.19, L, +inf) |
| ligand_5841 | L-2-Aminopentanedioic acid 5… (5-Benzyl glutamate) | HL | Amino Acids | 2 | `N[C@@H](CCC(=O)OCc1ccccc1)C(=O)O` | (-inf, H2L, 2.06, HL, 8.89, L, +inf) |
| ligand_5842 | DL-2-Aminopentanedioic acid 1… (1-Ethyl glutamate) | HL | Amino Acids | 2 | `CCOC(=O)[C@@H](N)CCC(=O)O` | (-inf, H2L, 3.85, HL, 7.84, L, +inf) |
| ligand_5844 | L-2-Aminopentanedioic acid 5-amide (Glutamine) | HL | Amino Acids | 71 | `NC(=O)CC[C@H](N)C(=O)O` | (-inf, H2L, 2.19, HL, 9, L, +inf) |
| ligand_5852 | L-2-Amino-5-ureidopentanoic acid (Citrulline) | HL | Amino Acids | 16 | `NC(=O)NCCC[C@H](N)C(=O)O` | (-inf, H2L, 2.3, HL, 9.33, L, +inf) |
| ligand_5858 | DL-2-Amino-3-mercapto-3-methylpentanoic acid | H2L | Amino Acids | 2 | `CCC(C)(S)C(N)C(=O)O` | (-inf, H2L, 7.96, HL, 10.5, L, +inf) |
| ligand_5875 | 5-Amino-3-thi… (S-2-Aminoethylmercaptoacetic acid) | HL | Amino Acids | 32 | `NCCSCC(=O)O` | (-inf, H2L, 3.18, HL, 9.53, L, +inf) |
| ligand_5886 | L-2,5-Diaminopentanoic acid (Ornithine) | HL | Amino Acids | 84 | `NCCC[C@H](N)C(=O)O` | (-inf, H3L, 2, H2L, 8.78, HL, 10.52, L, +inf) |
| ligand_5917 | L-2-Amino-5-guanidopentanoic acid (Arginine) | H2L | Amino Acids | 45 | `N=C(N)NCCC[C@H](N)C(=O)O` | (-inf, H3L, 2.03, H2L, 9, HL, 9, L, +inf) |

### Functional groups across all SQL matches (223 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 88 | 39% |
| secondary_amine | 81 | 36% |
| tertiary_amine | 60 | 27% |
| amide | 46 | 21% |
| primary_amine | 45 | 20% |
| hydroxyl | 38 | 17% |
| ether | 37 | 17% |
| aromatic_ring | 31 | 14% |
| thioether | 13 | 6% |
| phosphonate | 10 | 4% |
| pyridine | 9 | 4% |
| imine | 7 | 3% |
| ketone | 7 | 3% |
| ester | 6 | 3% |
| halide | 6 | 3% |
| thiol | 5 | 2% |
| oxime | 3 | 1% |
| phenol | 2 | 1% |
| phosphate | 2 | 1% |
| sulfonate | 1 | 0% |

---

### Step 7: `search_ligands`
**Args:**
```json
{
  "name": "glycine",
  "limit": 20
}
```

[summary]
## search_ligands — 20 result(s)

**stats:** 170 SQL matches · showing 20 · limit 20

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5760 | Aminoacetic acid (Glycine) | HL | Amino Acids | 428 | `NCC(=O)O` | (-inf, H2L, 2.33, HL, 9.57, L, +inf) |
| ligand_5776 | DL-Aminophenylacetic acid (Phenylglycine) | HL | Amino Acids | 12 | `NC(C(=O)O)c1ccccc1` | (-inf, H2L, -1.9, HL, 8.92, L, +inf) |
| ligand_5786 | DL-Amino-4-sulfophenylacet… (4-Sulfophenylglycine) | H2L | Amino Acids | 12 | `NC(C(=O)O)c1ccc(S(=O)(=O)O)cc1` | (-inf, H2L, -1.8, HL, 8.66, L, +inf) |
| ligand_5838 | DL-Amino-4-Methoxyphenyl… (4-Methoxyphenylglycine) | HL | Amino Acids | 12 | `COc1ccc(C(N)C(=O)O)cc1` | (-inf, H2L, 2, HL, 9.07, L, +inf) |
| ligand_5925 | N-Methylglycine (Sarcosine) | HL | Amino Acids | 39 | `CNCC(=O)O` | (-inf, H2L, 2.18, HL, 9.98, L, +inf) |
| ligand_5926 | N-Ethylglycine | HL | Amino Acids | 6 | `CCNCC(=O)O` | (-inf, H2L, 2.3, HL, 10.1, L, +inf) |
| ligand_5927 | N-Propylglycine | HL | Amino Acids | 6 | `CCCNCC(=O)O` | (-inf, H2L, 2.28, HL, 10.03, L, +inf) |
| ligand_5928 | N-Butylglycine | HL | Amino Acids | 6 | `CCCCNCC(=O)O` | (-inf, H2L, 2.29, HL, 10.07, L, +inf) |
| ligand_5929 | N-(2-Propyl)glycine | HL | Amino Acids | 5 | `CC(C)NCC(=O)O` | (-inf, H2L, 2.36, HL, 10.06, L, +inf) |
| ligand_5937 | N-(Phosphonomethyl)glycine (Glyphosate) | H3L | Amino Acids | 146 | `O=C(O)CNCP(=O)(O)O` | (-inf, H4L, -0.5, H3L, 2.2, H2L, 5.45, HL, 10.1, L, +inf) |
| ligand_5948 | N-(2-Aminoethyl)glycine (Ethylenediamine m… (EDMA) | HL | Amino Acids | 30 | `NCCNCC(=O)O` | (-inf, H3L, -1.9, H2L, 6.67, HL, 9.84, L, +inf) |
| ligand_5949 | N-[Tris(hydroxymethyl)methyl]glycine (Tricine) | HL | Amino Acids | 10 | `O=C(O)CNC(CO)(CO)CO` | (-inf, H2L, 2.023, HL, 8.135, L, +inf) |
| ligand_5959 | 2-(Carboxymethylaminomethyl)azole-4-sulfonic acid… | H2L | Amino Acids | 9 | `O=C(O)CNCc1cc(S(=O)(=O)O)c[nH]1` | (-inf, H2L, 2.25, HL, 8.71, L, +inf) |
| ligand_5971 | N-Acetylglycyl-L-histidylglycine | HL | Amino Acids | 7 | `CC(=O)NCC(=O)N[C@@H](CC1C=NC=N1)C(=O)NCC(=O)O` | (-inf, H2L, 3.13, HL, 6.74, L, +inf) |
| ligand_5972 | N-Acetylglycyl(N(3)-benzyl-L-histidyl)glycine | HL | Amino Acids | 7 | `CC(=O)NCC(=O)NC(Cc1cncn1Cc1ccccc1)C(=O)NCC(=O)O` | (-inf, H2L, 3.18, HL, 6.25, L, +inf) |
| ligand_5974 | N-Acetylglycylglycyl-L-histidylglycine | HL | Amino Acids | 11 | `CC(=O)NCC(=O)NCC(=O)N[C@@H](CC1C=NC=N1)C(=O)NCC(=O)O` | (-inf, H2L, 3.17, HL, 6.78, L, +inf) |
| ligand_5997 | rac-Trimethylenebis[2-(2-hydroxy-3,5… (rac-TMPHPG) | *** | Amino Acids | 13 | *** | (-inf, H6L, 2.42, H5L, 2.49, H4L, 7.33, H3L, 8.94, H2L, 8.94, HL, -11.65, L, +inf) |
| ligand_5998 | meso-Trimethylenebis[2-(2-hydroxy-3… (meso-TMPHPG) | H4L | Amino Acids | 13 | `Cc1cc(C)c(O)c([C@H](NCCCN[C@@H](C(=O)O)c2cc(C)cc(C)c2O)C(=O)O)c1` | (-inf, H6L, -1.8, H5L, 2.29, H4L, 7.33, H3L, 9.14, H2L, 9.14, HL, -12.08, L, +inf) |
| ligand_6015 | N,N-Dimethylglycine | HL | Amino Acids | 25 | `CN(C)CC(=O)O` | (-inf, H2L, 2, HL, 9.77, L, +inf) |
| ligand_6016 | N,N-Diethylglycine | HL | Amino Acids | 5 | `CCN(CC)CC(=O)O` | (-inf, H2L, 2.04, HL, 10.47, L, +inf) |

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
