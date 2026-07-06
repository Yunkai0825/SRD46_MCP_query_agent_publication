# Q2.1.3 — Tool Results (batch 5)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "hydrogen",
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

### Step 3: `search_ligands`
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

### Step 4: `search_ligands`
**Args:**
```json
{
  "name": "alanine",
  "limit": 25
}
```

[summary]
## search_ligands — 25 result(s)

**stats:** 130 SQL matches · showing 25 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5761 | L-2-Aminopropanoic acid (Alanine) | HL | Amino Acids | 159 | `C[C@H](N)C(=O)O` | (-inf, H2L, 2.33, HL, 9.71, L, +inf) |
| ligand_5777 | L-2-Amino-3-phenylpropanoic acid (Phenylalanine) | HL | Amino Acids | 138 | `N[C@@H](Cc1ccccc1)C(=O)O` | (-inf, H2L, 2.18, HL, 9.09, L, +inf) |
| ligand_5778 | DL-2-Amino-3-chloropropanoic ac… (3-Chloroalanine) | HL | Amino Acids | 10 | `N[C@@H](CCl)C(=O)O` | (-inf, H2L, 2, HL, 8.18, L, +inf) |
| ligand_5780 | DL-2-Amino-3-(2-fluorophenyl)propanoic acid (DL-3… | HL | Amino Acids | 6 | `N[C@@H](Cc1ccccc1F)C(=O)O` | (-inf, H2L, 2.12, HL, 9.01, L, +inf) |
| ligand_5781 | DL-2-Amino-3-(3-fluorophenyl)propanoic acid (DL-3… | HL | Amino Acids | 6 | `N[C@@H](Cc1cccc(F)c1)C(=O)O` | (-inf, H2L, 2.1, HL, 8.98, L, +inf) |
| ligand_5782 | DL-2-Amino-3-(4-fluorophenyl)propanoic acid (DL-3… | HL | Amino Acids | 6 | `N[C@@H](Cc1ccc(F)cc1)C(=O)O` | (-inf, H2L, 2.13, HL, 9.05, L, +inf) |
| ligand_5783 | DL-2-Amino-3-(2-chlorophenyl)propanoic acid (DL-3… | HL | Amino Acids | 2 | `N[C@@H](Cc1ccccc1Cl)C(=O)O` | (-inf, H2L, 2.23, HL, 8.94, L, +inf) |
| ligand_5784 | DL-2-Amino-3-(3-chlorophenyl)propanoic acid (DL-3… | HL | Amino Acids | 2 | `N[C@@H](Cc1cccc(Cl)c1)C(=O)O` | (-inf, H2L, 2.17, HL, 8.91, L, +inf) |
| ligand_5785 | DL-2-Amino-3-(4-chlorophenyl)propanoic acid (DL-3… | HL | Amino Acids | 2 | `N[C@@H](Cc1ccc(Cl)cc1)C(=O)O` | (-inf, H2L, 2.08, HL, 8.96, L, +inf) |
| ligand_5788 | 3-Aminopropanoic acid (beta-Alanine) | HL | Amino Acids | 111 | `NCCC(=O)O` | (-inf, H2L, 3.51, HL, 10.08, L, +inf) |
| ligand_5796 | DL-3-Amino-3-phenylpropanoi… (Phenyl-beta-Alanine) | HL | Amino Acids | 2 | `NC(CC(=O)O)c1ccccc1` | (-inf, H2L, 3.4, HL, 9, L, +inf) |
| ligand_5854 | L-2-Amino-3-(4-methoxyph… (4-Methoxyphenylalanine) | HL | Amino Acids | 5 | `COc1ccc(C[C@H](N)C(=O)O)cc1` | (-inf, HL, -9.15, L, +inf) |
| ligand_5855 | DL-2-Amino-3-(3,4-di… (3,4-Dimethoxyphenylalanine) | HL | Amino Acids | 2 | `COc1ccc(C[C@H](N)C(=O)O)cc1OC` | (-inf, H2L, 2.37, HL, 9.02, L, +inf) |
| ligand_5915 | L-2-Amino-3-(2-pyridyl)propanoic acid (3-(2-Pyrid… | HL | Amino Acids | 14 | `N[C@@H](Cc1ccccn1)C(=O)O` | (-inf, H2L, 3.89, HL, 8.95, L, +inf) |
| ligand_5916 | L-2-Amino-3-(6-methyl-2-pyridyl)propanoic acid (3… | HL | Amino Acids | 14 | `Cc1cccc(C[C@H](N)C(=O)O)n1` | (-inf, H2L, 4.78, HL, 8.95, L, +inf) |
| ligand_6022 | DL-N,N-Bis(2-hydroxyethyl)alanine | HL | Amino Acids | 35 | `CC(C(=O)O)N(CCO)CCO` | (-inf, H2L, -1.7, HL, 8.47, L, +inf) |
| ligand_6373 | Glycyl-beta-alanine (Glycyl-3-aminopropanoic acid) | HL | Peptides | 14 | `NCC(=O)NCCC(=O)O` | (-inf, H2L, 4, HL, 8.11, L, +inf) |
| ligand_6375 | Glycyl-L-alanine | HL | Peptides | 62 | `C[C@H](NC(=O)CN)C(=O)O` | (-inf, H2L, 3.12, HL, 8.15, L, +inf) |
| ligand_6385 | Glycyl-L-phenylalanine | HL | Peptides | 34 | `NCC(=O)N[C@@H](Cc1ccccc1)C(=O)O` | (-inf, H2L, 2.99, HL, 8.09, L, +inf) |
| ligand_6421 | beta-Alanyl-beta-alanine | HL | Peptides | 7 | `NCCC(=O)NCCC(=O)O` | (-inf, H2L, 3.95, HL, 9.36, L, +inf) |
| ligand_6424 | L-Alanyl-L-alanine | HL | Peptides | 19 | `C[C@H](N)C(=O)N[C@@H](C)C(=O)O` | (-inf, H2L, 3.27, HL, 8.15, L, +inf) |
| ligand_6425 | L-Alanyl-D-alanine | HL | Peptides | 35 | `C[C@H](N)C(=O)N[C@H](C)C(=O)O` | (-inf, H2L, 3.13, HL, 8.29, L, +inf) |
| ligand_6426 | L-Alanyl-2-methylalanine | HL | Peptides | 5 | `CC(N)C(=O)NC(C)(C)C(=O)O` | (-inf, H2L, 3.49, HL, 8.22, L, +inf) |
| ligand_6429 | L-Alanyl-L-phenylalanine | HL | Peptides | 13 | `C[C@H](N)C(=O)N[C@@H](Cc1ccccc1)C(=O)O` | (-inf, H2L, 3.2, HL, 7.9, L, +inf) |
| ligand_6430 | L-Alanyl-D-phenylalanine | HL | Peptides | 13 | `C[C@H](N)C(=O)N[C@H](Cc1ccccc1)C(=O)O` | (-inf, H2L, 2.99, HL, 8.13, L, +inf) |

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

### Step 5: `search_pka_values`
**Args:**
```json
{
  "where": "lc.ligand_id IN (ligand_5760, ligand_5761) AND (p.solvent_name LIKE '%water%' OR p.solvent_name = 'water' OR p.solvent_name IS NULL) AND p.temperature_c BETWEEN 24 AND 26 AND (p.ionic_strength_mol_l IS NULL OR p.ionic_strength_mol_l <= 0.1)",
  "order_by": "lc.ligand_id, p.pKa_type, p.temperature_c, p.ionic_strength_mol_l",
  "limit": 60
}
```

[PHASE ERROR] Tool 'search_pka_values' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---
