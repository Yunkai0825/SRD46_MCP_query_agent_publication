# Q4.5 — Tool Results (batch 4)

### Step 2: `search_metals`
**Args:**
```json
{
  "symbol": "Ca",
  "limit": 10
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_25 | Ca^[2+] | Ca | 2 | ✓ | [Ca+2] | InChI=1S/Ca/q+2 | beta_totN_68 | ligand_totN_644 | vlm_totN_1761 |

---

### Step 3: `search_metals`
**Args:**
```json
{
  "symbol": "H",
  "limit": 10
}
```

[summary]
## search_metals — 10 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_20 | BuHg^[+] | B | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_23 | BuNH_[3]^[+] | B | 1 |  | *** | *** | beta_totN_1 | ligand_totN_2 | vlm_totN_2 |
| metal_24 | C(NH_[2])_[3]^[+] | C | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_45 | Et_[2]NH_[2]^[+] | E2NH2 | 1 |  | *** | *** | beta_totN_1 | ligand_totN_1 | vlm_totN_1 |
| metal_48 | Et_[3]NH^[+] | E3NH | 1 |  | *** | *** | beta_totN_1 | ligand_totN_1 | vlm_totN_1 |
| metal_53 | EtHg^[+] | EHg | 1 |  | *** | *** | beta_totN_4 | ligand_totN_3 | vlm_totN_6 |
| metal_54 | EtNH_[3]^[+] | ENH3 | 1 |  | *** | *** | beta_totN_1 | ligand_totN_3 | vlm_totN_3 |
| metal_68 | H^[+] | H | 1 | ✓ | [H+] | InChI=1S/p+1 | beta_totN_82 | ligand_totN_4081 | vlm_totN_20720 |
| metal_69 | H_[5]TeO_[6]^[-] | H | -1 |  | *** | *** | beta_totN_1 | ligand_totN_1 | vlm_totN_2 |
| metal_70 | Hf^[4+] | Hf | 4 | ✓ | [Hf+4] | InChI=1S/Hf/q+4 | beta_totN_10 | ligand_totN_14 | vlm_totN_49 |

---

### Step 4: `search_ligands`
**Args:**
```json
{
  "name": "acetate",
  "limit": 25
}
```

[summary]
## search_ligands — 3 result(s)

**stats:** 3 SQL matches · showing 3 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6365 | {Bis[3-(bis(carboxymethyl)amino)propyl]methylammo… | H4L | EDTA and derivatives | 32 | `C[N+](CCCN(CC(=O)O)CC(=O)O)(CCCN(CC(=O)O)CC(=O)O)CC(=O)[O-]` | (-inf, H4L, 2.14, H3L, 2.82, H2L, 7.95, HL, 8.84, L, +inf) |
| ligand_8698 | 2-Oxobutanedioic acid 4-et… (4-Ethyl oxaloacetate) | HL | Carboxylic acids keto | 5 | `CCOC(=O)CC(=O)C(=O)O` | (-inf, HL, 9.3, L, +inf) |
| ligand_9801 | Acetic acid vinyl ester (Vinyl acetate) | *** | miscellaneous hydrocarbo… | 2 | *** | *** |

### Functional groups across all SQL matches (2 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 2 | 100% |
| carboxylate | 1 | 50% |
| ester | 1 | 50% |
| ketone | 1 | 50% |
| tertiary_amine | 1 | 50% |

---

### Step 5: `search_ligands`
**Args:**
```json
{
  "name": "oxalate",
  "limit": 25
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
  "name": "citrate",
  "limit": 25
}
```

[summary]
## search_ligands — 4 result(s)

**stats:** 4 SQL matches · showing 4 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8672 | 2-Hydroxypropane-1,2,3-tri… (sym-Dimethyl citrate) | HL | Carboxylic acids hydroxy | 2 | `COC(=O)CC(O)(CC(=O)OC)C(=O)O` | (-inf, HL, 3.02, L, +inf) |
| ligand_8682 | DL-2-Hydroxypropane-1,2,3-t… (as-Dimethyl citrate) | HL | Carboxylic acids hydroxy | 2 | `COC(=O)CC(O)(CC(=O)O)C(=O)OC` | (-inf, HL, 3.78, L, +inf) |
| ligand_8965 | 2-Hydroxypropane-1,2,3-tri… (as-Monomethylcitrate) | H2L | Carboxylic acids diacids… | 4 | `COC(=O)CC(O)(CC(=O)O)C(=O)O` | (-inf, H2L, 2.7, HL, 4.66, L, +inf) |
| ligand_8966 | 2-Hydroxypropane-1,2,3-tr… (sym-Monomethylcitrate) | H2L | Carboxylic acids diacids… | 4 | `COC(=O)C(O)(CC(=O)O)CC(=O)O` | (-inf, H2L, 3.39, HL, 4.63, L, +inf) |

### Functional groups across all SQL matches (4 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 4 | 100% |
| ester | 4 | 100% |
| hydroxyl | 4 | 100% |

---

### Step 7: `search_ligands`
**Args:**
```json
{
  "name": "EDTA",
  "limit": 25
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 5 SQL matches · showing 5 · limit 25

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

### Step 8: `search_ligands`
**Args:**
```json
{
  "name": "EGTA",
  "limit": 25
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6342 | Ethylenebis(oxyethylenenitrilo)tetraacetic… (EGTA) | H4L | EDTA and derivatives | 169 | `O=C(O)CN(CCOCCOCCN(CC(=O)O)CC(=O)O)CC(=O)O` | (-inf, H4L, -1.9, H3L, 2.7, H2L, 8.71, HL, 9.32, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 1 | 100% |
| ether | 1 | 100% |
| tertiary_amine | 1 | 100% |

---

### Step 9: `search_ligands`
**Args:**
```json
{
  "name": "NTA",
  "limit": 25
}
```

[summary]
## search_ligands — 25 result(s)

**stats:** 298 SQL matches · showing 25 · limit 25

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
| ligand_5934 | L-2-(Iminomethylamino)pentanedioic acid | H2L | Amino Acids | 6 | `N=CNC(CCC(=O)O)C(=O)O` | (-inf, H2L, 4.44, HL, 11, L, +inf) |
| ligand_5985 | Ethylenediiminodi-2-pentanedioic acid (EDDG) | H4L | Amino Acids | 63 | `O=C(O)CCC(NCCNC(CCC(=O)O)C(=O)O)C(=O)O` | (-inf, H4L, -3.28, H3L, 4.25, H2L, 6.81, HL, 6.81, L, +inf) |
| ligand_6017 | N,N-Pentamethyleneglyc… (Piperidine-N-acetic acid) | HL | Amino Acids | 6 | `O=C(O)CN1CCCCC1` | (-inf, H2L, 2.13, HL, 10.25, L, +inf) |
| ligand_6062 | 1,4-Diazacycloheptane-N,N'-di(2-pentanoic acid) | H2L | Aza macrocycles with car… | 3 | `CCCC(C(=O)O)N1CCCN(C(CCC)C(=O)O)CC1` | (-inf, H2L, 5.67, HL, 9.88, L, +inf) |
| ligand_6070 | 1,4,10-Trioxa-7,13-diazacyclopentadecane-N,N'-dia… | H2L | Aza macrocycles with car… | 74 | `O=C(O)CN1CCOCCOCCN(CC(=O)O)CCOCC1` | (-inf, H3L, 2, H2L, 8.45, HL, 8.63, L, +inf) |

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

### Step 10: `search_ligands`
**Args:**
```json
{
  "name": "glycine",
  "limit": 25
}
```

[summary]
## search_ligands — 25 result(s)

**stats:** 170 SQL matches · showing 25 · limit 25

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
| ligand_6017 | N,N-Pentamethyleneglyc… (Piperidine-N-acetic acid) | HL | Amino Acids | 6 | `O=C(O)CN1CCCCC1` | (-inf, H2L, 2.13, HL, 10.25, L, +inf) |
| ligand_6019 | N,N-Bis(phosphonomethyl)glycine | H5L | Amino Acids | 55 | `O=C(O)CN(CP(=O)(O)O)CP(=O)(O)O` | (-inf, H5L, -1.7, H4L, 2.1, H3L, 5.04, H2L, 6.4, HL, 6.4, L, +inf) |
| ligand_6021 | N,N-Bis(2-hydroxyethyl)glycine (Bicine) | HL | Amino Acids | 82 | `O=C(O)CN(CCO)CCO` | (-inf, H2L, -1.7, HL, 8.11, L, +inf) |
| ligand_6023 | N,N-Bis(2-hydroxypropyl)glycine | HL | Amino Acids | 14 | `CC(O)CN(CC(=O)O)CC(C)O` | (-inf, HL, 8.13, L, +inf) |
| ligand_6024 | N,N-Bis(3-oxo-3-(4-oxa-1-azacyclohexyl)propyl)gly… | HL | Amino Acids | 9 | `O=C(O)CN(CCC(=O)N1CCOCC1)CCC(=O)N1CCOCC1` | (-inf, H2L, -1.9, HL, 8.2, L, +inf) |

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

### Step 11: `search_ligands`
**Args:**
```json
{
  "name": "lactate",
  "limit": 25
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 12: `search_ligands`
**Args:**
```json
{
  "name": "tartrate",
  "limit": 25
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 13: `search_ligands`
**Args:**
```json
{
  "name": "malate",
  "limit": 25
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8953 | L-Hydroxybutanedioic acid (Hydroxysuccinic acid)(… | H2L | Carboxylic acids diacids… | 172 | `O=C(O)CC(O)C(=O)O` | (-inf, H2L, 3.24, HL, 4.68, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 1 | 100% |
| hydroxyl | 1 | 100% |

---

### Step 14: `search_ligands`
**Args:**
```json
{
  "name": "succinate",
  "limit": 25
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 15: `search_ligands`
**Args:**
```json
{
  "name": "phosphate",
  "limit": 25
}
```

[summary]
## search_ligands — 25 result(s)

**stats:** 128 SQL matches · showing 25 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6391 | Glycyl-DL-… (Glycyl-DL-serine dihydrogenphosphate) | H3L | Peptides | 7 | `NCC(=O)N[C@@H](COP(=O)(O)O)C(=O)O` | (-inf, H3L, 2.91, H2L, 6.03, HL, 8.42, L, +inf) |
| ligand_6412 | DL-Phosphos… (DL-Serylglycine dihydrogenphosphate) | H3L | Peptides | 16 | `NC(COP(=O)(O)O)C(=O)NCC(=O)O` | (-inf, H3L, 3.16, H2L, 5.42, HL, 8.01, L, +inf) |
| ligand_6469 | L-Phosph… (L-Seryl-L-leucine dihydrogen phosphate) | H3L | Peptides | 3 | `CC(C)CC(NC(=O)C(N)COP(=O)(O)O)C(=O)O` | (-inf, H3L, 3.11, H2L, 5.47, HL, 8.26, L, +inf) |
| ligand_6470 | L… (L-O-Phenylseryl-L-leucine dihydrogenphosphate) | H2L | Peptides | 2 | `CC(C)CC(NC(=O)C(N)COP(=O)(O)Oc1ccccc1)C(=O)O` | (-inf, H2L, 3.16, HL, 7.12, L, +inf) |
| ligand_6504 | L-P… (L-Seryl-L-glutamic acid dihydrogenphosphate) | H4L | Peptides | 25 | `NC(COP(=O)(O)O)C(=O)NC(CCC(=O)O)C(=O)O` | (-inf, H4L, 3.04, H3L, 4.4, H2L, 5.69, HL, 8.22, L, +inf) |
| ligand_6506 | L-Phosphos… (L-Seryl-L-lysine dihydrogenphosphate) | H3L | Peptides | 10 | `NCCCCC(NC(=O)C(N)COP(=O)(O)O)C(=O)O` | (-inf, H4L, 2.99, H3L, 5.34, H2L, 5.59, HL, 11.05, L, +inf) |
| ligand_6572 | Glyc… (Glycyl-DL-serylglycine dihydrogenphosphate) | H3L | tripeptides | 9 | `NCC(=O)NC(COP(=O)(O)O)C(=O)NCC(=O)O` | (-inf, H3L, 3.29, H2L, 5.77, HL, 8.22, L, +inf) |
| ligand_7977 | Pyridoxal-5'-(dihydrogenphosphate) | H3L | Pyridines (azines) | 51 | `Cc1ncc(COP(=O)(O)O)c(C=O)c1O` | (-inf, H4L, -1.4, H3L, 3.51, H2L, 6.04, HL, 8.25, L, +inf) |
| ligand_7980 | Pyridoxamine-5'-(dihydrogenphosphate) | H3L | Pyridines (azines) | 16 | `Cc1ncc(COP(=O)(O)O)c(CN)c1O` | (-inf, H4L, 3.4, H3L, 5.64, H2L, 8.42, HL, 10.8, L, +inf) |
| ligand_7981 | 5-Aminomethyl-3-hydrox… (Isopyridoxaminephosphate) | H3L | Pyridines (azines) | 4 | `Cc1ncc(CN)c(COP(=O)(O)O)c1O` | (-inf, H4L, 3.64, H3L, 5.55, H2L, 8.44, HL, 10.69, L, +inf) |
| ligand_8232 | Cytidine-3'-(dihydrogenphosphate) (CMP-3) | H2L | Pyrimidines | 2 | `Nc1ccn([C@@H]2O[C@H](CO)[C@@H](OP(=O)(O)O)[C@H]2O)c(=O)n1` | (-inf, H2L, 4.24, HL, +inf) |
| ligand_8233 | 2'-Deoxycytidine-5'-(dihydrogenphosphate) | H2L | Pyrimidines | 7 | `Nc1ccn([C@H]2C[C@H](O)[C@@H](COP(=O)(O)O)O2)c(=O)n1` | (-inf, H2L, 4.46, HL, 6.24, L, +inf) |
| ligand_8234 | Cytidine-5'-(dihydrogenphosphate) (CMP-5) | H2L | Pyrimidines | 40 | `Nc1ccn([C@@H]2O[C@H](COP(=O)(O)O)[C@@H](O)[C@H]2O)c(=O)n1` | (-inf, H2L, 4.33, HL, 6.19, L, +inf) |
| ligand_8235 | Cytidine-5'-(trihydrogendiphosphate) (CDP) | H3L | Pyrimidines | 29 | `Nc1ccn([C@@H]2O[C@H](COP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]2O)c(=O)n1` | (-inf, H3L, -1, H2L, 4.46, HL, 4.46, L, +inf) |
| ligand_8236 | Cytidine-5'-(tetrahydrogentriphosphate) (CTP) | H4L | Pyrimidines | 59 | `Nc1ccn([C@@H]2O[C@H](COP(=O)(O)OP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]2O)c(=O)n1` | (-inf, H2L, 4.47, HL, 6.42, L, +inf) |
| ligand_8240 | Uridine-3'-(dihydrogenphosphate) (UMP-3) | H2L | Pyrimidines | 1 | `O=c1ccn([C@@H]2O[C@H](CO)[C@@H](OP(=O)(O)O)[C@H]2O)c(=O)[nH]1` | (-inf, L, 9.23, H-1L, +inf) |
| ligand_8241 | Uridine-5'-(dihydrogenphosphate) (UMP-5) | H2L | Pyrimidines | 37 | `O=c1ccn([C@@H]2O[C@H](COP(=O)(O)O)[C@@H](O)[C@H]2O)c(=O)[nH]1` | (-inf, H2L, -0.7, HL, 6.1, L, 9.4, H-1L, +inf) |
| ligand_8242 | Orotidine-5'-(dihydrogenphosphate) (OMP-5) | H3L | Pyrimidines | 22 | `O=C(O)c1cc(=O)[nH]c(=O)n1[C@@H]1O[C@H](COP(=O)(O)O)[C@@H](O)[C@H]1O` | (-inf, H3L, -0.7, H2L, -0.7, HL, 6.4, L, 9.35, H-1L, +inf) |
| ligand_8243 | Uridine-5'-(trihydrogendiphosphate) (UDP) | H3L | Pyrimidines | 24 | `O=c1ccn([C@@H]2O[C@H](COP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]2O)c(=O)[nH]1` | (-inf, H2L, -1.3, HL, -1.3, L, 9.47, H-1L, +inf) |
| ligand_8244 | Uridine-5'-(tetrahydrogentriphosphate) (UTP) | H4L | Pyrimidines | 41 | `O=c1ccn([C@@H]2O[C@H](COP(=O)(O)OP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]2O)c(=O)[nH]1` | (-inf, H2L, -1.9, HL, 6.34, L, 9.59, H-1L, +inf) |
| ligand_8247 | Thymidine-5'-(dihydrogenphosphate) (TMP-5) | H2L | Pyrimidines | 28 | `Cc1cn([C@H]2C[C@H](O)[C@@H](COP(=O)(O)O)O2)c(=O)[nH]c1=O` | (-inf, H2L, -1.1, HL, 6.2, L, 9.77, H-1L, +inf) |
| ligand_8248 | Thymidine-5'-(trihydrogendiphosphate) (TDP) | H4L | Pyrimidines | 13 | `Cc1cn([C@H]2C[C@H](O)[C@@H](COP(=O)(O)OP(=O)(O)O)O2)c(=O)[nH]c1=O` | (-inf, H2L, -1.3, HL, 6.33, L, 9.82, H-1L, +inf) |
| ligand_8249 | Thymidine-5'-(tetrahydrogentriphosphate) (TTP) | H4L | Pyrimidines | 27 | `Cc1cn([C@H]2C[C@H](O)[C@@H](COP(=O)(O)OP(=O)(O)OP(=O)(O)O)O2)c(=O)[nH]c1=O` | (-inf, H2L, -1.9, HL, 6.4, L, 9.78, H-1L, +inf) |
| ligand_8305 | 9-(beta-D-Ribofuran… (Tubercidin-5'-monophosphate) | H2L | Purines phosphates | 12 | `Nc1ncnc2c1ccn2[C@@H]1O[C@H](COP(=O)(O)O)[C@@H](O)[C@H]1O` | (-inf, H2L, 5.28, HL, 6.32, L, +inf) |
| ligand_8306 | Inosine-5'-(dihydrogenphosphate) (IMP-5) | H2L | Purines phosphates | 27 | `O=P(O)(O)OC[C@H]1O[C@@H](n2cnc3c(O)ncnc32)[C@H](O)[C@@H]1O` | (-inf, H3L, -0.4, H2L, -0.4, HL, 6.18, L, 9.04, H-1L, +inf) |

### Functional groups across all SQL matches (103 parseable SMILES)

| group | count | % |
|-------|-------|---|
| hydroxyl | 101 | 98% |
| phosphate | 93 | 90% |
| aromatic_ring | 51 | 50% |
| ether | 38 | 37% |
| primary_amine | 34 | 33% |
| carboxyl | 14 | 14% |
| amide | 7 | 7% |
| pyridine | 7 | 7% |
| ester | 2 | 2% |
| secondary_amine | 2 | 2% |
| tertiary_amine | 2 | 2% |
| aldehyde | 1 | 1% |
| halide | 1 | 1% |
| phosphonate | 1 | 1% |
| thiol | 1 | 1% |

---

### Step 16: `search_ligands`
**Args:**
```json
{
  "name": "carbonate",
  "limit": 25
}
```

[summary]
## search_ligands — 4 result(s)

**stats:** 4 SQL matches · showing 4 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_10096 | Hydrogen carbonate (Carbonic acid) | H2L | Inorganic ligands | 335 | `O=C(O)O` | (-inf, H2L, 6.13, HL, 9.91, L, +inf) |
| ligand_10097 | Hydrogen trithiocarbonate | H2L | Inorganic ligands | 4 | `S=C(S)S` | (-inf, H2L, 2.68, HL, 8.22, L, +inf) |
| ligand_10098 | Hydrogen perthiocarbonate | H2L | Inorganic ligands | 3 | `S=C(S)SS` | (-inf, HL, 7.24, L, +inf) |
| ligand_10099 | Hydrogen triselenocarbonate | H2L | Inorganic ligands | 4 | `[Se]=C([SeH])[SeH]` | (-inf, HL, 7.13, L, +inf) |

### Functional groups across all SQL matches (4 parseable SMILES)

| group | count | % |
|-------|-------|---|
| thiol | 2 | 50% |
| carboxyl | 1 | 25% |

---

### Step 17: `search_ligands`
**Args:**
```json
{
  "name": "salicylate",
  "limit": 25
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_9317 | 2-Hydroxybenzoic acid methyl … (Methyl salicylate) | HL | Phenols salicylic acids | 8 | `COC(=O)c1ccccc1O` | (-inf, HL, 9.75, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| aromatic_ring | 1 | 100% |
| ester | 1 | 100% |
| hydroxyl | 1 | 100% |
| phenol | 1 | 100% |

---

### Step 18: `search_ligands`
**Args:**
```json
{
  "name": "acetic acid",
  "limit": 25
}
```

[summary]
## search_ligands — 25 result(s)

**stats:** 683 SQL matches · showing 25 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5760 | Aminoacetic acid (Glycine) | HL | Amino Acids | 428 | `NCC(=O)O` | (-inf, H2L, 2.33, HL, 9.57, L, +inf) |
| ligand_5776 | DL-Aminophenylacetic acid (Phenylglycine) | HL | Amino Acids | 12 | `NC(C(=O)O)c1ccccc1` | (-inf, H2L, -1.9, HL, 8.92, L, +inf) |
| ligand_5786 | DL-Amino-4-sulfophenylacet… (4-Sulfophenylglycine) | H2L | Amino Acids | 12 | `NC(C(=O)O)c1ccc(S(=O)(=O)O)cc1` | (-inf, H2L, -1.8, HL, 8.66, L, +inf) |
| ligand_5825 | DL-2-Amino-2-(3,4-dihydroxyphenyl)acetic a… (DOPG) | H3L | Amino Acids | 6 | `NC(C(=O)O)c1ccc(O)c(O)c1` | (-inf, H4L, 2, H3L, 8.56, H2L, 9.75, HL, 9.75, L, +inf) |
| ligand_5838 | DL-Amino-4-Methoxyphenyl… (4-Methoxyphenylglycine) | HL | Amino Acids | 12 | `COc1ccc(C(N)C(=O)O)cc1` | (-inf, H2L, 2, HL, 9.07, L, +inf) |
| ligand_5875 | 5-Amino-3-thi… (S-2-Aminoethylmercaptoacetic acid) | HL | Amino Acids | 32 | `NCCSCC(=O)O` | (-inf, H2L, 3.18, HL, 9.53, L, +inf) |
| ligand_5876 | 6-Amino-3-th… (S-3-Aminopropylmercaptoacetic acid) | HL | Amino Acids | 21 | `NCCCSCC(=O)O` | (-inf, H2L, 3.35, HL, 10.19, L, +inf) |
| ligand_5948 | N-(2-Aminoethyl)glycine (Ethylenediamine m… (EDMA) | HL | Amino Acids | 30 | `NCCNCC(=O)O` | (-inf, H3L, -1.9, H2L, 6.67, HL, 9.84, L, +inf) |
| ligand_5958 | Diethylenetriamine-N(1)-acetic acid | HL | Amino Acids | 15 | `NCCNCCNCC(=O)O` | (-inf, H4L, -1.3, H3L, 4.32, H2L, 8.7, HL, 9.92, L, +inf) |
| ligand_5964 | 4-Imidazolylacetic acid | HL | Amino Acids | 10 | `O=C(O)Cc1c[nH]cn1` | (-inf, H2L, 3.1, HL, 7.26, L, +inf) |
| ligand_5975 | Ethylenediiminodiacetic acid (EDDA) | H2L | Amino Acids | 198 | `O=C(O)CNCCNCC(=O)O` | (-inf, H4L, -1.3, H3L, 2.12, H2L, 6.55, HL, 9.61, L, +inf) |
| ligand_5979 | Ethylenediiminobis(dimethylacetic acid) | H2L | Amino Acids | 4 | `CC(C)(NCCNC(C)(C)C(=O)O)C(=O)O` | (-inf, H2L, 7, HL, 9.85, L, +inf) |
| ligand_5980 | 1,4-Diaminobutane-N,N'-diacetic acid | H2L | Amino Acids | 12 | `O=C(O)CNCCCCNCC(=O)O` | (-inf, H4L, -1.84, H3L, 2.52, H2L, 9.04, HL, 10.33, L, +inf) |
| ligand_5994 | N,N'-Bis(2-hydroxyphenyl)ethylenediiminodi… (HPED) | H4L | Amino Acids | 37 | `O=C(O)CN(CCN(CC(=O)O)c1ccccc1O)c1ccccc1O` | (-inf, H5L, -1.9, H4L, 3.58, H3L, 6.15, H2L, 10.44, HL, 10.44, L, +inf) |
| ligand_5995 | rac-Ethylenediiminobis[(2-hydroxyphenyl)ac… (EHPG) | H4L | Amino Acids | 21 | `O=C(O)C(Cc1ccccc1O)NCCNC(Cc1ccccc1O)C(=O)O` | (-inf, H4L, 6.33, H3L, 8.79, H2L, 10.87, HL, 10.87, L, +inf) |
| ligand_5996 | meso-Ethylenediiminobis[(2-hydroxyphenyl)a… (EHPG) | H4L | Amino Acids | 22 | `O=C(O)C(Cc1ccccc1O)NCCNC(Cc1ccccc1O)C(=O)O` | (-inf, H4L, 6.36, H3L, 8.76, H2L, 10.85, HL, 10.85, L, +inf) |
| ligand_6003 | 6-Oxa-3,9-diazaundecanedioic acid [Oxybis(ethylen… | H2L | Amino Acids | 8 | `O=C(O)CNCCOCCNCC(=O)O` | (-inf, H4L, -1.9, H3L, 2.6, H2L, 8.65, HL, 9.61, L, +inf) |
| ligand_6006 | N,N'-Bis(2,2-dimethyl-2-mercaptoethyl)ethylenedii… | H3L | Amino Acids | 10 | `CC(C)(S)CNCC(CC(=O)O)NCC(C)(C)S` | (-inf, H5L, -1.8, H4L, 4.95, H3L, 7.91, H2L, 10.03, HL, 10.03, L, +inf) |
| ligand_6007 | L,L-Ethylenediimino-… (N,N'-Ethylenedi-L-cysteine) | H4L | Amino Acids | 32 | `O=C(O)C(CS)NCCNC(CS)C(=O)O` | (-inf, H5L, -1.7, H4L, 5.4, H3L, 7.91, H2L, 9.88, HL, 9.88, L, +inf) |
| ligand_6008 | N,N'-Bis(2,2-dimethyl-2-mercaptoethyl)ethylenedin… | H4L | Amino Acids | 10 | `CC(C)(S)CN(CCN(CC(=O)O)CC(C)(C)S)CC(=O)O` | (-inf, H5L, 2.7, H4L, 4.24, H3L, 8.99, H2L, 10.56, HL, 10.56, L, +inf) |
| ligand_6009 | N,N'-Bis(2,2-dimethyl-2-mercaptoethyl)-1-[4-(carb… | H5L | Amino Acids | 11 | `CC(C)(S)CN(CC(=O)O)CC(Cc1ccc(OCC(=O)O)cc1)N(CC(=O)O)CC(C)(C)S` | (-inf, H5L, 2.9, H4L, 3.89, H3L, 9.85, H2L, 9.85, HL, -11.7, L, +inf) |
| ligand_6010 | Ethane-1,1,1-tris(methyleneiminoacetic acid) | H3L | Amino Acids | 11 | `CC(CNCC(=O)O)(CNCC(=O)O)CNCC(=O)O` | (-inf, H3L, 4.69, H2L, 7.73, HL, 10.73, L, +inf) |
| ligand_6011 | cis,cis-Cyclohexane-1,3,5-tris(iminoacetic acid) | H3L | Amino Acids | 11 | `O=C(O)CN[C@H]1C[C@@H](NCC(=O)O)C[C@@H](NCC(=O)O)C1` | (-inf, H3L, 6.45, H2L, 8.06, HL, 9.6, L, +inf) |
| ligand_6013 | N-(4-Methylphenylsulfonyl)ethylenediiminodiacetic… | H2L | Amino Acids | 2 | `Cc1ccc(S(=O)(=O)N(CCNCC(=O)O)CC(=O)O)cc1` | (-inf, H2L, 2, HL, 7.83, L, +inf) |
| ligand_6017 | N,N-Pentamethyleneglyc… (Piperidine-N-acetic acid) | HL | Amino Acids | 6 | `O=C(O)CN1CCCCC1` | (-inf, H2L, 2.13, HL, 10.25, L, +inf) |

### Functional groups across all SQL matches (567 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 557 | 98% |
| tertiary_amine | 324 | 57% |
| aromatic_ring | 227 | 40% |
| hydroxyl | 88 | 16% |
| thioether | 76 | 13% |
| ether | 54 | 10% |
| halide | 49 | 9% |
| amide | 43 | 8% |
| secondary_amine | 36 | 6% |
| phenol | 27 | 5% |
| pyridine | 19 | 3% |
| primary_amine | 15 | 3% |
| sulfonate | 14 | 2% |
| thiol | 11 | 2% |
| ester | 6 | 1% |
| nitrile | 6 | 1% |
| ketone | 5 | 1% |
| phosphonate | 5 | 1% |
| phosphate | 2 | 0% |
| aldehyde | 1 | 0% |
| imine | 1 | 0% |

---

### Step 19: `search_ligands`
**Args:**
```json
{
  "name": "oxalic acid",
  "limit": 25
}
```

[summary]
## search_ligands — 4 result(s)

**stats:** 4 SQL matches · showing 4 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8872 | Ethanedioic acid (Oxalic acid) | H2L | Carboxylic acids diacids | 394 | `O=C(O)C(=O)O` | (-inf, H2L, -1.2, HL, 3.8, L, +inf) |
| ligand_8960 | Oxopropanedioic acid (Ketomaloni… (Mesoxalic acid) | H2L | Carboxylic acids diacids… | 3 | `O=C(O)C(=O)C(=O)O` | (-inf, H2L, -1.82, HL, 3.52, L, +inf) |
| ligand_9763 | Dithiooxalic acid | H2L | miscellaneous mercaptans | 3 | `O=C(S)C(=O)S` | *** |
| ligand_11304 | Ethanedi(dithioic acid) (Tetrathiooxalic acid) | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (3 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 2 | 67% |
| ketone | 1 | 33% |
| thiol | 1 | 33% |

---

### Step 20: `search_ligands`
**Args:**
```json
{
  "name": "citric acid",
  "limit": 25
}
```

[summary]
## search_ligands — 8 result(s)

**stats:** 8 SQL matches · showing 8 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_9057 | DL-1-Hydroxypropane-1,2,3-tricar… (Isocitric acid) | H3L | Carboxylic acids polyaci… | 24 | `O=C(O)CC(C(=O)O)C(O)C(=O)O` | (-inf, H3L, 3.05, H2L, 4.3, HL, 5.73, L, +inf) |
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxyli… (Citric acid) | H3L | Carboxylic acids polyaci… | 384 | `O=C(O)CC(O)(CC(=O)O)C(=O)O` | (-inf, H3L, 2.9, H2L, 4.35, HL, 5.65, L, +inf) |
| ligand_10950 | DL-Methylcitric acid | *** | Ligands not selected | 0 | *** | *** |
| ligand_10951 | DL-Homocitric acid | *** | Ligands not selected | 0 | *** | *** |
| ligand_10952 | DL-threo-2-Methylisocitric acid | *** | Ligands not selected | 0 | *** | *** |
| ligand_10953 | DL-erytho-2-Methylisocitric acid | *** | Ligands not selected | 0 | *** | *** |
| ligand_10954 | DL-threo-Homoisocitric acid | *** | Ligands not selected | 0 | *** | *** |
| ligand_10955 | DL-erythro-Fluorocitric acid | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (2 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 2 | 100% |
| hydroxyl | 2 | 100% |

---

### Step 21: `search_ligands`
**Args:**
```json
{
  "name": "lactic acid",
  "limit": 25
}
```

[summary]
## search_ligands — 4 result(s)

**stats:** 4 SQL matches · showing 4 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8641 | D-2-Hydroxypropanoic acid (Lactic acid) | HL | Carboxylic acids hydroxy | 349 | `CC(O)C(=O)O` | (-inf, HL, 3.67, L, +inf) |
| ligand_8660 | DL-2-Phenyl-2-hydroxypropanoic … (Atrolactic acid) | HL | Carboxylic acids hydroxy | 34 | `CC(O)(C(=O)O)c1ccccc1` | (-inf, HL, 3.53, L, +inf) |
| ligand_8767 | DL-2-Mercaptopropanoic acid (Thiolactic acid) | H2L | Carboxylic acids thio | 71 | `CC(S)C(=O)O` | (-inf, H2L, 3.48, HL, 10.08, L, +inf) |
| ligand_8976 | DL-2,2'-Oxydipropanoic acid (Dilactic acid) | H2L | Carboxylic acids diacids | 30 | `CC(OC(C)C(=O)O)C(=O)O` | *** |

### Functional groups across all SQL matches (4 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 4 | 100% |
| hydroxyl | 2 | 50% |
| aromatic_ring | 1 | 25% |
| ether | 1 | 25% |
| thiol | 1 | 25% |

---

### Step 22: `search_ligands`
**Args:**
```json
{
  "name": "tartaric acid",
  "limit": 25
}
```

[summary]
## search_ligands — 9 result(s)

**stats:** 9 SQL matches · showing 9 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8955 | D-2,3-Dihydroxybutanedioic acid (D-Tartaric acid) | H2L | Carboxylic acids diacids… | 214 | `O=C(O)C(O)C(O)C(=O)O` | (-inf, H2L, 2.82, HL, 3.97, L, +inf) |
| ligand_8956 | meso-2,3-Dihydroxybutanedioi… (meso-Tartaric acid) | H2L | Carboxylic acids diacids… | 43 | `O=C(O)[C@@H](O)[C@@H](O)C(=O)O` | (-inf, H2L, 2.97, HL, 4.49, L, +inf) |
| ligand_8996 | DL-2,3-Dimercaptobutaned… (DL-Dithiotartaric acid) | H4L | Carboxylic acids diacids… | 9 | `O=C(O)C(S)C(S)C(=O)O` | (-inf, H4L, 2.25, H3L, 3.96, H2L, 9.61, HL, +inf) |
| ligand_8997 | meso-2,3-Dimercaptobut… (meso-Dithiotartaric acid) | H4L | Carboxylic acids diacids… | 41 | `O=C(O)[C@@H](S)[C@@H](S)C(=O)O` | (-inf, H4L, 2.4, H3L, 3.46, H2L, 9.64, HL, 9.64, L, +inf) |
| ligand_10941 | erthro-2-Methyltartaric acid | *** | Ligands not selected | 0 | *** | *** |
| ligand_10942 | threo-2-Methyltartaric acid | *** | Ligands not selected | 0 | *** | *** |
| ligand_10943 | meso-2,3-Dimethyltartaric acid | *** | Ligands not selected | 0 | *** | *** |
| ligand_10944 | threo-2,3-Dimethyltartaric acid | *** | Ligands not selected | 0 | *** | *** |
| ligand_11398 | N,N'-Dimethyltartaric acid diamide | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (4 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 4 | 100% |
| hydroxyl | 2 | 50% |
| thiol | 2 | 50% |

---

### Step 23: `search_ligands`
**Args:**
```json
{
  "name": "succinic acid",
  "limit": 25
}
```

[summary]
## search_ligands — 13 result(s)

**stats:** 13 SQL matches · showing 13 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6138 | 2,2'-Bis(2-Carboxymethyl)iminodiacetic acid (Imin… | H4L | Iminodiacetic acid and d… | 26 | `O=C(O)CC(NC(CC(=O)O)C(=O)O)C(=O)O` | (-inf, H4L, -1.97, H3L, 3.24, H2L, 4.24, HL, 10, L, +inf) |
| ligand_8907 | Butanedioic acid (Succinic acid) | H2L | Carboxylic acids diacids | 253 | `O=C(O)CCC(=O)O` | (-inf, H2L, 3.99, HL, 5.24, L, +inf) |
| ligand_8908 | DL-Propane-1,2-dicarboxylic… (Methylsuccinic acid) | H2L | Carboxylic acids diacids | 38 | `CC(CC(=O)O)C(=O)O` | (-inf, H2L, 3.88, HL, 5.35, L, +inf) |
| ligand_8909 | 2-Methylpropane-1,2-d… (2,2-Dimethylsuccinic acid) | H2L | Carboxylic acids diacids | 11 | `CC(C)(CC(=O)O)C(=O)O` | (-inf, HL, 5.86, L, +inf) |
| ligand_8910 | meso-Butane-2,3-… (meso-2,3-Dimethylsuccinic acid) | H2L | Carboxylic acids diacids | 10 | `C[C@H](C(=O)O)[C@@H](C)C(=O)O` | (-inf, H2L, 3.67, HL, 5.3, L, +inf) |
| ligand_8911 | DL-Butane-2,3-dica… (DL-2,3-Dimethylsuccinic acid) | H2L | Carboxylic acids diacids | 11 | `CC(C(=O)O)C(C)C(=O)O` | (-inf, H2L, 3.82, HL, 5.93, L, +inf) |
| ligand_8912 | 2,2,3,3-Tetramethylbut… (Tetramethylsuccinic acid) | H2L | Carboxylic acids diacids | 2 | `CC(C)(C(=O)O)C(C)(C)C(=O)O` | (-inf, H2L, 3.53, HL, 7.35, L, +inf) |
| ligand_8913 | 2,2,3,3-Tetraethylbutan… (Tetraethylsuccinic acid) | H2L | Carboxylic acids diacids | 2 | `CCC(CC)(C(=O)O)C(CC)(CC)C(=O)O` | (-inf, H2L, 3.39, HL, 8.06, L, +inf) |
| ligand_8914 | rac-2,2,5,5-Tetramethylhexane-3,4-dicarboxylic ac… | H2L | Carboxylic acids diacids | 4 | `CC(C)(C)C(C(=O)O)C(C(=O)O)C(C)(C)C` | (-inf, H2L, 2.2, HL, 10.25, L, +inf) |
| ligand_8953 | L-Hydroxybutanedioic acid (Hydroxysuccinic acid)(… | H2L | Carboxylic acids diacids… | 172 | `O=C(O)CC(O)C(=O)O` | (-inf, H2L, 3.24, HL, 4.68, L, +inf) |
| ligand_8954 | DL-2-Hydroxy-2-methylbutanedioi… (Citramalic acid) | H2L | Carboxylic acids diacids… | 8 | `CC(O)(CC(=O)O)C(=O)O` | (-inf, H2L, 3.24, HL, 4.83, L, +inf) |
| ligand_10307 | N,N'-Bis(2-hydroxyethyl)ethylenedinitrilodisuccin… | *** | Ligands not selected | 0 | *** | *** |
| ligand_10922 | Chlorosuccinic acid | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (11 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 11 | 100% |
| hydroxyl | 2 | 18% |
| secondary_amine | 1 | 9% |

---

### Step 24: `search_ligands`
**Args:**
```json
{
  "name": "salicylic acid",
  "limit": 25
}
```

[summary]
## search_ligands — 25 result(s)

**stats:** 43 SQL matches · showing 25 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8701 | 2-Acetoxybenzoic acid (Acetylsalicylic acid) | HL | Carboxylic acids keto | 5 | `CC(=O)Oc1ccccc1C(=O)O` | (-inf, HL, 3.45, L, +inf) |
| ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | H2L | Phenols salicylic acids | 227 | `O=C(O)c1ccccc1O` | (-inf, H2L, 2.8, HL, 2.8, L, +inf) |
| ligand_9265 | 2-Hydroxy-3-methylbenzoic acid (3-Methylsalicylic… | H2L | Phenols salicylic acids | 9 | `Cc1cccc(C(=O)O)c1O` | (-inf, H2L, 2.83, HL, 2.83, L, +inf) |
| ligand_9266 | 2-Hydroxy-4-methylbenzoic acid (4-Methylsalicylic… | H2L | Phenols salicylic acids | 8 | `Cc1ccc(C(=O)O)c(O)c1` | (-inf, H2L, 2.96, HL, 2.96, L, +inf) |
| ligand_9267 | 2-Hydroxy-5-methylbenzoic acid (5-Methylsalicylic… | H2L | Phenols salicylic acids | 6 | `Cc1ccc(O)c(C(=O)O)c1` | (-inf, H2L, 2.88, HL, 2.88, L, +inf) |
| ligand_9268 | 2-Hydroxy-6-methylbenzoi… (6-Methylsalicylic acid) | H2L | Phenols salicylic acids | 5 | `Cc1cccc(O)c1C(=O)O` | (-inf, H2L, 3.16, HL, +inf) |
| ligand_9269 | 2-Hydroxy-3-(2-propyl… (3-Isopropylsalicylic acid) | H2L | Phenols salicylic acids | 2 | `CC(C)c1cccc(C(=O)O)c1O` | (-inf, H2L, 2.76, HL, +inf) |
| ligand_9274 | 5-Fluoro-2-hydroxybenzoi… (5-Fluorosalicylic acid) | H2L | Phenols salicylic acids | 3 | `O=C(O)c1cc(F)ccc1O` | (-inf, H2L, 2.56, HL, 2.56, L, +inf) |
| ligand_9275 | 5-Chloro-2-hydroxybenzoi… (5-Chlorosalicylic acid) | H2L | Phenols salicylic acids | 19 | `O=C(O)c1cc(Cl)ccc1O` | (-inf, H2L, 2.46, HL, 2.46, L, +inf) |
| ligand_9276 | 6-Chloro-2-hydroxybenzoi… (6-Chlorosalicylic acid) | H2L | Phenols salicylic acids | 1 | `O=C(O)c1c(O)cccc1Cl` | (-inf, H2L, 2.63, HL, +inf) |
| ligand_9277 | 5-Bromo-2-hydroxybenzoic … (5-Bromosalicylic acid) | H2L | Phenols salicylic acids | 11 | `O=C(O)c1cc(Br)ccc1O` | (-inf, H2L, 2.44, HL, 2.44, L, +inf) |
| ligand_9278 | 2-Hydroxy-5-iodobenzoic ac… (5-Iodosalicylic acid) | H2L | Phenols salicylic acids | 10 | `O=C(O)c1cc(I)ccc1O` | (-inf, H2L, -2.54, HL, -2.54, L, +inf) |
| ligand_9279 | 2-Hydroxy-3-nitrobenzoic … (3-Nitrosalicylic acid) | H2L | Phenols salicylic acids | 14 | `O=C(O)c1cccc([N+](=O)[O-])c1O` | (-inf, H2L, -1.73, HL, 9.87, L, +inf) |
| ligand_9280 | 2-Hydroxy-4-nitrobenzoic … (4-Nitrosalicylic acid) | H2L | Phenols salicylic acids | 4 | `O=C(O)c1ccc([N+](=O)[O-])cc1O` | (-inf, H2L, 2.05, HL, 10.91, L, +inf) |
| ligand_9281 | 2-Hydroxy-5-nitrobenzoic … (5-Nitrosalicylic acid) | H2L | Phenols salicylic acids | 36 | `O=C(O)c1cc([N+](=O)[O-])ccc1O` | (-inf, H2L, -1.94, HL, 9.9, L, +inf) |
| ligand_9282 | 2-Hydroxy-6-nitrobenzoic … (6-Nitrosalicylic acid) | H2L | Phenols salicylic acids | 4 | `O=C(O)c1c(O)cccc1[N+](=O)[O-]` | (-inf, H2L, 1.99, HL, 9.04, L, +inf) |
| ligand_9283 | 2-Hydroxy-3,5-dinitro… (3,5-Dinitrosalicylic acid) | H2L | Phenols salicylic acids | 35 | `O=C(O)c1cc([N+](=O)[O-])cc([N+](=O)[O-])c1O` | (-inf, H2L, -0.3, HL, 7.07, L, +inf) |
| ligand_9284 | 2-Hydroxy-5-sulfobenzoic … (5-Sulfosalicylic acid) | H3L | Phenols salicylic acids | 127 | `O=C(O)c1cc(S(=O)(=O)O)ccc1O` | (-inf, H2L, 2.48, HL, 11.85, L, +inf) |
| ligand_9285 | 3-Bromo-2-hydroxy… (3-Bromo-5-sulfosalicylic acid) | H3L | Phenols salicylic acids | 89 | `O=C(O)c1cc(S(=O)(=O)O)cc(Br)c1O` | (-inf, H2L, 2.02, HL, 10.52, L, +inf) |
| ligand_9287 | 2-Hydroxy-3,5-disulfo… (3,5-Disulfosalicylic acid) | H4L | Phenols salicylic acids | 51 | `O=C(O)c1cc(S(=O)(=O)O)cc(S(=O)(=O)O)c1O` | (-inf, H2L, 2.03, HL, 2.03, L, +inf) |
| ligand_9288 | 2-Hydroxy-3-methoxybenz… (3-Methoxysalicylic acid) | H2L | Phenols salicylic acids | 3 | `COc1cccc(C(=O)O)c1O` | (-inf, H2L, 2.69, HL, 2.69, L, +inf) |
| ligand_9289 | 2-Hydroxy-5-methoxybenz… (5-Methoxysalicylic acid) | H2L | Phenols salicylic acids | 3 | `COc1ccc(O)c(C(=O)O)c1` | (-inf, H2L, 2.92, HL, 2.92, L, +inf) |
| ligand_9296 | 2-Hydroxy-5-cyanobenzoic … (5-Cyanosalicylic acid) | H2L | Phenols salicylic acids | 3 | `N#Cc1ccc(O)c(C(=O)O)c1` | (-inf, H2L, 2.36, HL, 2.36, L, +inf) |
| ligand_9297 | 4-Amino-2-hydroxybenzoic … (p-Aminosalicylic acid) | H2L | Phenols salicylic acids | 31 | `Nc1ccc(C(=O)O)c(O)c1` | (-inf, H3L, -1.8, H2L, 3.63, HL, +inf) |
| ligand_9298 | 5-Amino-2-hydroxybenzoic … (m-Aminosalicylic acid) | H2L | Phenols salicylic acids | 18 | `Nc1ccc(O)c(C(=O)O)c1` | (-inf, H3L, 2.28, H2L, 2.28, HL, -5.6, L, +inf) |

### Functional groups across all SQL matches (25 parseable SMILES)

| group | count | % |
|-------|-------|---|
| aromatic_ring | 25 | 100% |
| carboxyl | 25 | 100% |
| hydroxyl | 24 | 96% |
| phenol | 24 | 96% |
| halide | 6 | 24% |
| tertiary_amine | 5 | 20% |
| sulfonate | 3 | 12% |
| primary_amine | 2 | 8% |
| ester | 1 | 4% |
| nitrile | 1 | 4% |

---

### Step 25: `search_ligands`
**Args:**
```json
{
  "name": "phosphoric acid",
  "limit": 25
}
```

[summary]
## search_ligands — 25 result(s)

**stats:** 43 SQL matches · showing 25 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_9150 | Phosphoric acid methyl ester (Methyl phosphate) | H2L | Organophosphorus and ars… | 12 | `COP(=O)(O)O` | (-inf, HL, 6.25, L, +inf) |
| ligand_9151 | Phosphoric acid butyl ester (Butyl phosphate) | H2L | Organophosphorus and ars… | 11 | `CCCCOP(=O)(O)O` | (-inf, HL, 6.72, L, +inf) |
| ligand_9152 | Phosphoric acid phenyl ester (Phenyl phosphate) | H2L | Organophosphorus and ars… | 24 | `O=P(O)(O)Oc1ccccc1` | (-inf, H2L, -0.9, HL, 5.78, L, +inf) |
| ligand_9153 | Phosphoric acid 4-nitro… (4-Nitrophenyl phosphate) | H2L | Organophosphorus and ars… | 4 | `O=[N+]([O-])c1ccc(OP(=O)(O)O)cc1` | (-inf, HL, 5.01, L, +inf) |
| ligand_9154 | Phosphoric acid 1-naph… (alpha-Naphthyl phosphate) | H2L | Organophosphorus and ars… | 18 | `O=P(O)(O)Oc1cccc2ccccc12` | (-inf, H2L, -0.9, HL, 5.74, L, +inf) |
| ligand_9155 | Phosphoric acid 2-napht… (beta-Naphthyl phosphate) | H2L | Organophosphorus and ars… | 6 | `O=P(O)(O)Oc1ccc2ccccc2c1` | (-inf, H2L, -1.2, HL, 5.74, L, +inf) |
| ligand_9156 | Phosphoric acid 4-nitro… (p-Nitrophenyl phosphate) | H2L | Organophosphorus and ars… | 18 | `O=[N+]([O-])c1ccc(OP(=O)(O)O)cc1` | (-inf, HL, 5.02, L, +inf) |
| ligand_9163 | Phosphoric acid dibutyl ester (Dibutyl phosphate) | HL | Organophosphorus and ars… | 1 | `CCCCOP(=O)(O)OCCCC` | (-inf, HL, 1, L, +inf) |
| ligand_9165 | Diphosphoric acid methyl est… (Methyl diphosphate) | H3L | Organophosphorus and ars… | 9 | `COP(=O)(O)OP(=O)(O)O` | (-inf, H2L, -1.6, HL, 6.37, L, +inf) |
| ligand_9166 | Diphosphoric acid butyl ester (Butyl diphosphate) | H3L | Organophosphorus and ars… | 12 | `CCCCOP(=O)(O)OP(=O)(O)O` | (-inf, H2L, -1.3, HL, 6.65, L, +inf) |
| ligand_9167 | Diphosphoric acid phenyl est… (Phenyl diphosphate) | H3L | Organophosphorus and ars… | 12 | `O=P(O)(O)OP(=O)(O)Oc1ccccc1` | (-inf, H2L, -1.3, HL, 6.32, L, +inf) |
| ligand_9168 | Triphosphoric acid methyl e… (Methyl triphosphate) | H4L | Organophosphorus and ars… | 3 | `COP(=O)(O)OP(=O)(O)OP(=O)(O)O` | (-inf, HL, 6.45, L, +inf) |
| ligand_9173 | Phosphorodithioic … (Dibutyldithiophosphoric acid) | HL | Organophosphorus and ars… | 2 | `CCCCOP(=S)(S)OCCCC` | (-inf, HL, 0.08, L, +inf) |
| ligand_9174 | Phosphorodithio… (Diisobutyldithiophosphoric acid) | HL | Organophosphorus and ars… | 2 | `CC(C)COP(=S)(S)OCC(C)C` | (-inf, HL, -0.04, L, +inf) |
| ligand_10113 | Hydrogen phosphate (Phosphoric acid) | H3L | Inorganic ligands | 359 | `O=P(O)(O)O` | (-inf, H3L, 1.92, H2L, 6.71, HL, 11.52, L, +inf) |
| ligand_10114 | Hydrogen diphosphate (Pyrophosphoric acid) | H4L | Inorganic ligands | 211 | `O=P(O)(O)OP(=O)(O)O` | (-inf, H4L, -0.8, H3L, -0.8, H2L, 5.94, HL, 8.25, L, +inf) |
| ligand_10116 | Hydrogen hypophosphate (Hypophosphoric acid) | H4L | Inorganic ligands | 5 | `O=P(O)(O)P(=O)(O)O` | (-inf, H3L, 2.1, H2L, 6.77, HL, 9.48, L, +inf) |
| ligand_10117 | Hydrogen triphosphate (Triphosphoric acid) | H5L | Inorganic ligands | 176 | `O=P(O)(O)OP(=O)(O)OP(=O)(O)O` | (-inf, H5L, -0.5, H4L, -0.5, H3L, -0.9, H2L, 5.42, HL, 7.77, L, +inf) |
| ligand_10119 | Hydrogen tetraphosphate (Tetraphosphoric acid) | H6L | Inorganic ligands | 40 | `O=P(O)(O)OP(=O)(O)OP(=O)(O)OP(=O)(O)O` | (-inf, H2L, 5.84, HL, 7.43, L, +inf) |
| ligand_10120 | Hydrogen pentaphosphate (Pentaphosphoric acid) | H6L | Inorganic ligands | 2 | `O=P(O)(O)OP(=O)(O)OP(=O)(O)OP(=O)(O)OP(=O)(O)O` | (-inf, H2L, 7.03, HL, 8.15, L, +inf) |
| ligand_10121 | Hydrogen hexaphosphate (Hexaphosphoric acid) | H7L | Inorganic ligands | 2 | `O=P(O)(O)OP(=O)(O)OP(=O)(O)OP(=O)(O)O[PH](O)(O)OP(=O)(O)O` | (-inf, H2L, 7.16, HL, 8.12, L, +inf) |
| ligand_10122 | Hydrogen heptaphosphate (Heptaphosphoric acid) | H8L | Inorganic ligands | 2 | `O=P(O)(O)OP(=O)(O)OP(=O)(O)OP(=O)(O)O[PH](O)(O)O[PH](O)(O)OP(=O)(O)O` | (-inf, H2L, 7.18, HL, 8.07, L, +inf) |
| ligand_10123 | Hydrogen trimetaphosphate (Trimetaphosphoric acid) | H3L | Inorganic ligands | 37 | `O=P1(O)OP(=O)(O)OP(=O)(O)O1` | (-inf, HL, 2.05, L, +inf) |
| ligand_10124 | Hydrogen tetrametaphos… (Tetrametaphosphoric acid) | H4L | Inorganic ligands | 37 | `O=P1(O)OP(=O)(O)OP(=O)(O)OP(=O)(O)O1` | (-inf, HL, -1.9, L, +inf) |
| ligand_10125 | Hydrogen hexametaphosph… (Hexametaphosphoric acid) | H6L | Inorganic ligands | 7 | `O=P1(O)OP(=O)(O)OP(=O)(O)OP(=O)(O)OP(=O)(O)OP(=O)(O)O1` | (-inf, HL, 3.7, L, +inf) |

### Functional groups across all SQL matches (28 parseable SMILES)

| group | count | % |
|-------|-------|---|
| hydroxyl | 26 | 93% |
| phosphate | 23 | 82% |
| aromatic_ring | 6 | 21% |
| secondary_amine | 2 | 7% |
| tertiary_amine | 2 | 7% |
| thiol | 2 | 7% |

---

### Step 26: `search_ligands`
**Args:**
```json
{
  "name": "hydrogen phosphate",
  "limit": 25
}
```

[summary]
## search_ligands — 2 result(s)

**stats:** 2 SQL matches · showing 2 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6469 | L-Phosph… (L-Seryl-L-leucine dihydrogen phosphate) | H3L | Peptides | 3 | `CC(C)CC(NC(=O)C(N)COP(=O)(O)O)C(=O)O` | (-inf, H3L, 3.11, H2L, 5.47, HL, 8.26, L, +inf) |
| ligand_10113 | Hydrogen phosphate (Phosphoric acid) | H3L | Inorganic ligands | 359 | `O=P(O)(O)O` | (-inf, H3L, 1.92, H2L, 6.71, HL, 11.52, L, +inf) |

### Functional groups across all SQL matches (2 parseable SMILES)

| group | count | % |
|-------|-------|---|
| hydroxyl | 2 | 100% |
| phosphate | 2 | 100% |
| amide | 1 | 50% |
| carboxyl | 1 | 50% |
| primary_amine | 1 | 50% |

---

### Step 27: `search_ligands`
**Args:**
```json
{
  "name": "dihydrogen phosphate",
  "limit": 25
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6469 | L-Phosph… (L-Seryl-L-leucine dihydrogen phosphate) | H3L | Peptides | 3 | `CC(C)CC(NC(=O)C(N)COP(=O)(O)O)C(=O)O` | (-inf, H3L, 3.11, H2L, 5.47, HL, 8.26, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| amide | 1 | 100% |
| carboxyl | 1 | 100% |
| hydroxyl | 1 | 100% |
| phosphate | 1 | 100% |
| primary_amine | 1 | 100% |

---

### Step 29: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_25 AND c.ligand_id IN (ligand_8872, ligand_9058, ligand_8641, ligand_8953, ligand_8907, ligand_8955, ligand_5760, ligand_6277, ligand_6342, ligand_10113, ligand_10096) AND (s.solvent_name LIKE '%water%' OR s.solvent_name IS NULL) AND s.temperature_c BETWEEN 20 AND 30 AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l BETWEEN 0 AND 0.2)",
  "order_by": "c.ligand_id, s.constant_type, s.temperature_c",
  "limit": 200
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 30: `search_pka_values`
**Args:**
```json
{
  "where": "lc.ligand_id IN (ligand_8872, ligand_9058, ligand_8641, ligand_8953, ligand_8907, ligand_8955, ligand_5760, ligand_6277, ligand_6342, ligand_10113, ligand_10096) AND (p.solvent_name LIKE '%water%' OR p.solvent_name IS NULL) AND p.temperature_c BETWEEN 20 AND 30 AND (p.ionic_strength_mol_l IS NULL OR p.ionic_strength_mol_l BETWEEN 0 AND 0.2)",
  "order_by": "lc.ligand_id, p.pKa ASC",
  "limit": 200
}
```

[PHASE ERROR] Tool 'search_pka_values' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---
