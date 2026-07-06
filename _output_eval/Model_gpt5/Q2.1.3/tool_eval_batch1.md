# Q2.1.3 — Tool Results (batch 1)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "H+",
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

### Step 6: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_68",
  "ligand_id": "ligand_5760"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 2 species

### H^[+] + Aminoacetic acid (Glycine)
**metal_id:** metal_68 | **ligand_id:** ligand_5760 | **ligand_def_HxL:** HL  
**entries:** 48 | **species:** 2 | **vlm_count:** 48

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_32 | [H<sub>2</sub>L]/[HL][H] | [HL] + [H] <=> [H2L] | [H2L](aqueous), [HL](aqueous), [H](aqueous) | 27 |
| beta_def_79 | [HL]/[L][H] | [L] + [H] <=> [HL] | [HL](aqueous), [L](aqueous), [H](aqueous) | 21 |

**vlm_ids:** vlm_93606, vlm_93607, vlm_93608, vlm_93609, vlm_93610, … vlm_93651, vlm_93652, vlm_93653 (48 listed)

**equilibrium_maps:** 15 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_1 | 2 | 1 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_2 | 2 | 1 | 19~29 °C | 2.85~3.15 M |
| ref_eq_net_3 | 2 | 1 | 19~29 °C | 1.85~2.15 M |
| ref_eq_net_4 | 2 | 1 | 19~29 °C | 2.85~3.15 M |
| ref_eq_net_5 | 2 | 1 | 19~29 °C | 1.85~2.15 M |
| ref_eq_net_6 | 2 | 1 | 19~29 °C | 2.85~3.15 M |
| ref_eq_net_7 | 2 | 1 | 31~41 °C | 0~0.3 M |
| ref_eq_net_8 | 2 | 1 | 19~29 °C | 0.35~0.65 M |
| ref_eq_net_9 | 2 | 1 | 19~29 °C | 0.55~0.85 M |
| ref_eq_net_10 | 2 | 1 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_11 | 2 | 1 | 5~15 °C | -0.15~0.15 M |
| ref_eq_net_12 | 2 | 1 | 19~29 °C | -0.15~0.15 M |
| ref_eq_net_13 | 2 | 1 | 35~45 °C | -0.15~0.15 M |
| ref_eq_net_14 | 1 | 0 | 19~29 °C | 1.85~2.15 M |
| ref_eq_net_15 | 1 | 0 | 19~29 °C | 2.85~3.15 M |

---

### Step 7: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_68",
  "ligand_id": "ligand_5761"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 2 species

### H^[+] + L-2-Aminopropanoic acid (Alanine)
**metal_id:** metal_68 | **ligand_id:** ligand_5761 | **ligand_def_HxL:** HL  
**entries:** 40 | **species:** 2 | **vlm_count:** 40

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_32 | [H<sub>2</sub>L]/[HL][H] | [HL] + [H] <=> [H2L] | [H2L](aqueous), [HL](aqueous), [H](aqueous) | 20 |
| beta_def_79 | [HL]/[L][H] | [L] + [H] <=> [HL] | [HL](aqueous), [L](aqueous), [H](aqueous) | 20 |

**vlm_ids:** vlm_94058, vlm_94059, vlm_94060, vlm_94061, vlm_94062, … vlm_94095, vlm_94096, vlm_94097 (40 listed)

**equilibrium_maps:** 11 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_136 | 2 | 1 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_137 | 2 | 1 | 19~29 °C | 2.85~3.15 M |
| ref_eq_net_138 | 2 | 1 | 31~41 °C | 0~0.3 M |
| ref_eq_net_139 | 2 | 1 | 19~29 °C | 0.35~0.65 M |
| ref_eq_net_140 | 2 | 1 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_141 | 2 | 1 | 19~29 °C | 1.85~2.15 M |
| ref_eq_net_142 | 2 | 1 | 19~29 °C | 2.85~3.15 M |
| ref_eq_net_143 | 2 | 1 | 19~29 °C | 4.85~5.15 M |
| ref_eq_net_144 | 2 | 1 | 5~15 °C | -0.15~0.15 M |
| ref_eq_net_145 | 2 | 1 | 19~29 °C | -0.15~0.15 M |
| ref_eq_net_146 | 2 | 1 | 35~45 °C | -0.15~0.15 M |

---

### Step 9: `search_pka_values`
**Args:**
```json
{
  "where": "(lc.ligand_id IN (ligand_5760, ligand_5761) AND p.temperature_c BETWEEN 24 AND 26 AND (p.ionic_strength_mol_l IS NULL OR p.ionic_strength_mol_l BETWEEN 0.00 AND 0.15))",
  "order_by": "lc.ligand_id, p.pKa_type ASC, p.temperature_c ASC, p.ionic_strength_mol_l ASC",
  "limit": 20
}
```

[summary]
## search_pka_values — 4 row(s)

### pKa 2.0–2.5 (2 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_93627 | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 2.33 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_20 |
| vlm_94078 | ligand_5761 | L-2-Aminopropanoic acid (Alanine) | HL | C[C@H](N)C(=O)O | 2.33 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_6 |

### pKa 9.5–10.0 (2 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_93606 | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 9.57 | 25 | 0.1 | L→HL | M_tot_20 | M_tot_43 |
| vlm_94058 | ligand_5761 | L-2-Aminopropanoic acid (Alanine) | HL | C[C@H](N)C(=O)O | 9.71 | 25 | 0.1 | L→HL | M_tot_6 | M_tot_19 |

---
