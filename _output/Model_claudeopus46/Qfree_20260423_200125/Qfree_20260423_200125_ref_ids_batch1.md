# Qfree_20260423_200125 -- Referenced Entity IDs (batch 1)

**Prompt:** I would like to find ligands that can complex Fe(III) to stabilize the acidic solution (pH<5), yet with limited complexation to Fe(II) so that it does not decrease the free Fe2+ concentration too much. This is for Fe electrodeposition since we also try to minimize the hydrogen evolution reaction when Fe electrodeposition happens. The expected concentration of Fe(II) is ~0.1M. Meanwhile, be cautious about ligand pH and its actual state, and be cautious about possible precipitations. If there are missing entries, try to observe similar metal-ligand systems with available data to estimate those with very robust reasons and explanations. You have unlimited time and unlimited turns.

---

### Step 2: `search_metals`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_61 | Fe^[3+] |  |
| metal | metal_62 | Fe^[2+] |  |


### Step 11: `search_pka_ligands`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| ligand | ligand_5937 | N-(Phosphonomethyl)glycine (Glyphosate) | SMILES: O=C(O)CNCP(=O)(O)O; HxL: H3L |
| ligand | ligand_6165 | Nitrilotriacetic acid (NTA) | SMILES: O=C(O)CN(CC(=O)O)CC(=O)O; HxL: H3L |
| ligand | ligand_6277 | Ethylenedinitrilotetraacetic acid (EDTA) | SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O; HxL: H4L |
| ligand | ligand_6770 | Pyridine-2-phosphonic-6-carboxylic acid (2PP6C) | SMILES: O=C(O)c1cccc(P(=O)(O)O)n1; HxL: H3L |
| ligand | ligand_8191 | 1,10-Phenanthroline (Dipyridino[a,c]benzene) | SMILES: c1cnc2c(c1)ccc1cccnc12; HxL: L |
| ligand | ligand_8434 | Pyridine-2,6-diphosphonic acid (2,6-PDPA) | SMILES: O=P(O)(O)c1cccc(P(=O)(O)O)n1; HxL: H4L |
| ligand | ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) | SMILES: O=C(O)CC(O)(CC(=O)O)C(=O)O; HxL: H3L |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_99756 |  |
| pka | pka_399 |  |
| vlm | vlm_99734 |  |
| pka | pka_400 |  |
| vlm | vlm_99712 |  |
| pka | pka_398 |  |
| vlm | vlm_99687 |  |
| pka | pka_401 |  |
| vlm | vlm_105204 |  |
| pka | pka_1159 |  |
| vlm | vlm_105223 |  |
| pka | pka_1161 |  |
| vlm | vlm_105186 |  |
| pka | pka_1158 |  |
| vlm | vlm_105158 |  |
| pka | pka_1160 |  |
| vlm | vlm_108289 |  |
| pka | pka_1464 |  |
| vlm | vlm_108282 |  |
| pka | pka_1466 |  |
| vlm | vlm_108272 |  |
| pka | pka_1465 |  |
| vlm | vlm_108254 |  |
| pka | pka_1467 |  |
| vlm | vlm_108224 |  |
| pka | pka_1463 |  |
| vlm | vlm_119187 |  |
| pka | pka_2916 |  |
| vlm | vlm_119186 |  |
| pka | pka_2915 |  |
| vlm | vlm_139234 |  |
| pka | pka_5881 |  |
| vlm | vlm_139221 |  |
| pka | pka_5882 |  |
| vlm | vlm_143981 |  |
| pka | pka_6490 |  |
| vlm | vlm_143980 |  |
| pka | pka_6489 |  |
| vlm | vlm_143979 |  |
| pka | pka_6488 |  |
| vlm | vlm_157473 |  |
| pka | pka_7350 |  |
| vlm | vlm_157459 |  |
| pka | pka_7351 |  |
| vlm | vlm_157439 |  |
| pka | pka_7352 |  |


### Step 13: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_61 | Fe^[3+] |  |
| ligand | ligand_9912 | Desferriferrioxamin E (Nocardamin) | SMILES: O=C1CCC(=O)N(O)CCCCCNC(=O)CCC(=O)N(O)CCCCCNC(=O)CCC(=O)N(O)CCCCCN1; HxL: H3L |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |
| ligand | ligand_9911 | N-Acetyldesferriferrioxamin B | SMILES: CC(=O)NCCCCCN(O)C(=O)CCC(=O)NCCCCCN(O)C(=O)CCC(=O)NCCCCCN(O)C(C)=O; HxL: H3L |
| ligand | ligand_9916 | Desferricoprogen | SMILES: CC(=O)NC(CCCN(O)C(=O)/C=C(\C)CCO)C(=O)OCC/C(C)=C\C(=O)N(O)CCCC1NC(=O)C(CCCN(O)C(=O)/C=C(\C)CO)NC1=O; HxL: H3L |
| ligand | ligand_9914 | Desferriferrichrysin |  |
| ligand | ligand_9909 | 1,13-Dimethyl-3,11,15,23,26,34-hexaoxa-6,20,29-trioxo-7,19,30-tris(hydroxyaza)bicyclo[11,11,11]pentatriacontane [Tris(hydroxamate) Cryptand] | SMILES: CC12COCCCN(O)C(=O)CCOCC(C)(COCCC(=O)N(O)CCCOC1)COCCC(=O)N(O)CCCOC2; HxL: H3L |
| ligand | ligand_9913 | Desferriferrichrome |  |
| ligand | ligand_9907 | 1,1,1-Tris{[2-{(N-methylhydroxylamino)carbonyl}ethoxy]methyl}ethane | SMILES: CN(O)C(=O)CCOCC(C)(COCCC(=O)N(C)O)COCCC(=O)N(C)O; HxL: H3L |
| ligand | ligand_9908 | 1,1,1-Tris{[3-(N-acetylhydroxylamino)propoxy]methyl}ethane | SMILES: CC(=O)N(O)CCCOCC(C)(COCCCN(O)C(C)=O)COCCCN(O)C(C)=O; HxL: H3L |
| ligand | ligand_9915 | N,N'N''-Tris[2-(N-hydroxycarbamoyl)ethyl]-1,3,5-benzenetricarboxamide (BAMTPH) | SMILES: O=C(CCNC(=O)c1cc(C(=O)NCCC(=O)NO)cc(C(=O)NCCC(=O)NO)c1)NO; HxL: H3L |
| ligand | ligand_9899 | N,N'-Di-2-propyltrimethylenodihydroxamic acid (N,N'-Diisopropylglutarodihydroxamic acid) | SMILES: CC(C)N(O)C(=O)CCCC(=O)N(O)C(C)C; HxL: H2L |
| ligand | ligand_9900 | N,N'-Di-2-propyltetramethylenodihydroxamic acid (N,N'-Diisopropylglutarodihydroxamic acid) | SMILES: CC(C)N(O)C(=O)CCCCC(=O)N(O)C(C)C; HxL: H2L |
| ligand | ligand_9901 | N,N'-Di-2-propylpentamethylenodihydroxamic acid (N,N'-Diisopropylglutarodihydroxamic acid) | SMILES: CC(C)N(O)C(=O)CCCCCC(=O)N(O)C(C)C; HxL: H2L |
| ligand | ligand_9902 | N,N'-Di-2-propylhexamethylenodihydroxamic acid (N,N'-Diisopropylglutarodihydroxamic acid) | SMILES: CC(C)N(O)C(=O)CCCCCCC(=O)N(O)C(C)C; HxL: H2L |
| ligand | ligand_9906 | Rhodotorulic acid | SMILES: CC(=O)N(O)CCCC1NC(=O)C(CCCN(O)C(C)=O)NC1=O; HxL: H2L |
| ligand | ligand_9898 | Octamethylenedihydroxamic acid (Decanodihydroxamic acid) | SMILES: O=C(CCCCCCCCC(=O)NO)NO; HxL: H2L |
| ligand | ligand_9897 | Heptamethylenedihydroxamic acid (Azelaodihydroxamic acid) | SMILES: O=C(CCCCCCCC(=O)NO)NO; HxL: H2L |
| ligand | ligand_9896 | Hexamethylenedihydroxamic acid (Caprylodihydroxamic acid) | SMILES: O=C(CCCCCCC(=O)NO)NO; HxL: H2L |
| ligand | ligand_9895 | Tetramethylenedihydroxamic acid (Adipodihydroxamic acid) | SMILES: O=C(CCCCC(=O)NO)NO; HxL: H2L |
| ligand | ligand_9890 | N-Methyl-4-methoxybenzohydroxamic acid | SMILES: COc1ccc(C(=O)N(C)O)cc1; HxL: HL |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_168857 |  |
| map | ref_eq_map_26704 |  |
| vlm | vlm_168843 |  |
| map | ref_eq_map_26699 |  |
| vlm | vlm_168900 |  |
| map | ref_eq_map_26725 |  |
| vlm | vlm_168872 |  |
| map | ref_eq_map_26710 |  |
| vlm | vlm_168783 |  |
| map | ref_eq_map_26676 |  |
| vlm | vlm_168867 |  |
| map | ref_eq_map_26708 |  |
| vlm | vlm_168767 |  |
| map | ref_eq_map_26670 |  |
| vlm | vlm_168775 |  |
| map | ref_eq_map_26673 |  |
| vlm | vlm_168889 |  |
| map | ref_eq_map_26719 |  |
| vlm | vlm_168719 |  |
| map | ref_eq_map_26653 |  |
| vlm | vlm_168723 |  |
| map | ref_eq_map_26655 |  |
| vlm | vlm_168727 |  |
| map | ref_eq_map_26657 |  |
| vlm | vlm_168731 |  |
| map | ref_eq_map_26659 |  |
| vlm | vlm_168746 |  |
| map | ref_eq_map_26667 |  |
| vlm | vlm_168747 |  |
| map | ref_eq_map_26668 |  |
| vlm | vlm_168712 |  |
| map | ref_eq_map_26647 |  |
| vlm | vlm_168697 |  |
| map | ref_eq_map_26635 |  |
| vlm | vlm_168682 |  |
| map | ref_eq_map_26625 |  |
| vlm | vlm_168666 |  |
| map | ref_eq_map_26615 |  |
| vlm | vlm_168607 |  |
| map | ref_eq_map_26592 |  |


### Step 14: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_61 | Fe^[3+] |  |
| ligand | ligand_8047 | Pyridine-2-carboxaldehyde oxime | SMILES: O/N=C/c1ccccn1; HxL: HL |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |
| ligand | ligand_8872 | Ethanedioic acid (Oxalic acid) | SMILES: O=C(O)C(=O)O; HxL: H2L |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_136897 |  |
| map | ref_eq_map_14392 |  |
| vlm | vlm_151795 |  |
| map | ref_eq_map_19978 |  |
| vlm | vlm_151794 |  |
| map | ref_eq_map_19976 |  |
| vlm | vlm_151793 |  |
| map | ref_eq_map_19977 |  |


### Step 15: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_61 | Fe^[3+] |  |
| ligand | ligand_8956 | meso-2,3-Dihydroxybutanedioic acid (meso-Tartaric acid) | SMILES: O=C(O)[C@@H](O)[C@@H](O)C(=O)O; HxL: H2L |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |
| ligand | ligand_8955 | D-2,3-Dihydroxybutanedioic acid (D-Tartaric acid) | SMILES: O=C(O)C(O)C(O)C(=O)O; HxL: H2L |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_155157 |  |
| map | ref_eq_map_21222 |  |
| vlm | vlm_155036 |  |
| map | ref_eq_map_21191 |  |
| vlm | vlm_155037 |  |
| map | ref_eq_map_21192 |  |


### Step 16: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_62 | Fe^[2+] |  |
| ligand | ligand_8872 | Ethanedioic acid (Oxalic acid) | SMILES: O=C(O)C(=O)O; HxL: H2L |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_151749 |  |
| map | ref_eq_map_19964 |  |


### Step 17: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_62 | Fe^[2+] |  |
| ligand | ligand_8955 | D-2,3-Dihydroxybutanedioic acid (D-Tartaric acid) | SMILES: O=C(O)C(O)C(O)C(=O)O; HxL: H2L |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_155002 |  |
| map | ref_eq_map_21180 |  |


### Step 18: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_68 | H^[+] |  |
| ligand | ligand_9284 | 2-Hydroxy-5-sulfobenzoic acid (5-Sulfosalicylic acid) | SMILES: O=C(O)c1cc(S(=O)(=O)O)ccc1O; HxL: H3L |
| beta_def | beta_def_79 |  | [L] + [H] <=> [HL] |
| ligand | ligand_9362 | 2,5-Dihydroxybenzenecarboxylic acid (Gentistic acid) | SMILES: O=C(O)c1cc(O)ccc1O; HxL: H3L |
| beta_def | beta_def_53 |  | [H2L] + [H] <=> [H3L] |
| metal | metal_44 | Dy^[3+] |  |
| beta_def | beta_def_732 |  | [M] + [H2L] <=> [MH2L] |
| metal | metal_79 | La^[3+] |  |
| metal | metal_173 | Sm^[3+] |  |
| metal | metal_65 | Gd^[3+] |  |
| metal | metal_55 | Er^[3+] |  |
| metal | metal_73 | Ho^[3+] |  |
| beta_def | beta_def_32 |  | [HL] + [H] <=> [H2L] |
| metal | metal_139 | Pr^[3+] |  |
| metal | metal_110 | Nd^[3+] |  |
| metal | metal_41 | Cu^[2+] |  |
| beta_def | beta_def_821 |  | [M] + [HL] <=> [ML] + [H] |
| metal | metal_19 | Be^[2+] |  |
| beta_def | beta_def_194 |  | [M] + [HL]^2 <=> [M(HL)2] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_160819 |  |
| vlm | vlm_162327 |  |
| vlm | vlm_162352 |  |
| vlm | vlm_162328 |  |
| vlm | vlm_162335 |  |
| vlm | vlm_162344 |  |
| vlm | vlm_162348 |  |
| vlm | vlm_162358 |  |
| vlm | vlm_162355 |  |
| vlm | vlm_160829 |  |
| vlm | vlm_162338 |  |
| vlm | vlm_162341 |  |
| vlm | vlm_160903 |  |
| vlm | vlm_160902 |  |
| vlm | vlm_162330 |  |
| map | ref_eq_map_23927 |  |
| vlm | vlm_160815 |  |
| map | ref_eq_map_23275 |  |
| vlm | vlm_160810 |  |
| map | ref_eq_map_23270 |  |
| vlm | vlm_160814 |  |
| map | ref_eq_map_23274 |  |
| vlm | vlm_160813 |  |
| map | ref_eq_map_23273 |  |
| vlm | vlm_160811 |  |
| map | ref_eq_map_23271 |  |


### Step 19: `search_ligands`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| ligand | ligand_9284 | 2-Hydroxy-5-sulfobenzoic acid (5-Sulfosalicylic acid) | SMILES: O=C(O)c1cc(S(=O)(=O)O)ccc1O; HxL: H3L |
| ligand | ligand_9285 | 3-Bromo-2-hydroxy-5-sulfobenzoic acid (3-Bromo-5-sulfosalicylic acid) | SMILES: O=C(O)c1cc(S(=O)(=O)O)cc(Br)c1O; HxL: H3L |
| ligand | ligand_9287 | 2-Hydroxy-3,5-disulfobenzoic acid (3,5-Disulfosalicylic acid) | SMILES: O=C(O)c1cc(S(=O)(=O)O)cc(S(=O)(=O)O)c1O; HxL: H4L |
| ligand | ligand_11011 | 3-Methyl-5-sulfosalicylic acid |  |
| ligand | ligand_11012 | 4-Methyl-5-sulfosalicylic acid |  |
| ligand | ligand_11013 | 5-Methyl-3-sulfosalicylic acid |  |
| ligand | ligand_11015 | 3-Amino-5-sulfosalicylic acid |  |


### Step 20: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_61 | Fe^[3+] |  |
| ligand | ligand_9284 | 2-Hydroxy-5-sulfobenzoic acid (5-Sulfosalicylic acid) | SMILES: O=C(O)c1cc(S(=O)(=O)O)ccc1O; HxL: H3L |
| beta_def | beta_def_821 |  | [M] + [HL] <=> [ML] + [H] |
| beta_def | beta_def_846 |  | [ML] + [HL] <=> [ML2] + [H] |
| beta_def | beta_def_873 |  | [ML2] + [HL] <=> [ML3] + [H] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_160912 |  |
| map | ref_eq_map_23323 |  |
| vlm | vlm_160914 |  |
| map | ref_eq_map_23326 |  |
| vlm | vlm_160915 |  |
| map | ref_eq_map_23324 |  |
| vlm | vlm_160913 |  |
| map | ref_eq_map_23325 |  |
| vlm | vlm_160919 |  |
| vlm | vlm_160918 |  |
| vlm | vlm_160920 |  |


### Step 21: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_62 | Fe^[2+] |  |
| ligand | ligand_9284 | 2-Hydroxy-5-sulfobenzoic acid (5-Sulfosalicylic acid) | SMILES: O=C(O)c1cc(S(=O)(=O)O)ccc1O; HxL: H3L |
| beta_def | beta_def_821 |  | [M] + [HL] <=> [ML] + [H] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_160888 |  |
| map | ref_eq_map_23310 |  |


### Step 22: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_62 | Fe^[2+] |  |
| ligand | ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) | SMILES: O=C(O)CC(O)(CC(=O)O)C(=O)O; HxL: H3L |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |
| beta_def | beta_def_779 |  | [M] + [HL] <=> [MHL] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_157619 |  |
| map | ref_eq_map_22111 |  |
| vlm | vlm_157623 |  |
| map | ref_eq_map_22109 |  |
| vlm | vlm_157624 |  |
| vlm | vlm_157626 |  |
| map | ref_eq_map_22113 |  |
| vlm | vlm_157620 |  |


### Step 23: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_61 | Fe^[3+] |  |
| ligand | ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) | SMILES: O=C(O)CC(O)(CC(=O)O)C(=O)O; HxL: H3L |
| beta_def | beta_def_424 |  | [M]^2 + [L]^2 + [H2O]^2 <=> [M2(OH)2L2] + [H]^2 |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |
| beta_def | beta_def_779 |  | [M] + [HL] <=> [MHL] |
| beta_def | beta_def_966 |  | [M(OH)L] + [H] <=> [ML] + [H2O] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_157689 |  |
| map | ref_eq_map_22123 |  |
| vlm | vlm_157683 |  |
| map | ref_eq_map_22124 |  |
| vlm | vlm_157682 |  |
| vlm | vlm_157684 |  |
| map | ref_eq_map_22125 |  |
| vlm | vlm_157687 |  |
| vlm | vlm_157688 |  |


### Step 24: `search_ligands`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| ligand | ligand_10162 | Hydrogen fluoride (Hydrofluoric acid) | SMILES: F; HxL: HL |


### Step 25: `search_ligands`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| ligand | ligand_6852 | 2-Aminoethyl(hydrogensulfate) | SMILES: NCCOS(=O)(=O)O; HxL: HL |
| ligand | ligand_9382 | 2,3,4-Trihydroxybenzenesulfonic acid (Pyrogallolsulfate) | SMILES: O=S(=O)(O)c1ccc(O)c(O)c1O; HxL: H4L |
| ligand | ligand_10148 | Hydrogen sulfate ion (Sulfuric acid) | SMILES: O=S(=O)([O-])O; HxL: HL |
| ligand | ligand_10149 | Hydrogen thiosulfate (Thiosulfuric acid) | SMILES: O=S(O)(O)=S; HxL: H2L |
| ligand | ligand_10150 | Selenosulfate ion |  |
| ligand | ligand_10151 | Hydrogen amidosulfate (Sulfamic acid) | SMILES: NS(=O)(=O)O; HxL: HL |
| ligand | ligand_10152 | Hydrogen hydroxylamidosulfate (Hydroxylamine-O-sulfonic acid) | SMILES: NOS(=O)(=O)O; HxL: HL |
| ligand | ligand_10153 | Hydrogen amidodisulfate (Aminodisulfonic acid) | SMILES: O=S(=O)(O)NS(=O)(=O)O; HxL: H2L |
| ligand | ligand_10154 | Hydrogen peroxosulfate | SMILES: O=S(=O)(O)OO; HxL: H2L |
| ligand | ligand_10155 | Hydrogen peroxydisulfate (Peroxydisulfuric acid) | SMILES: O=S(=O)(O)OOS(=O)(=O)O; HxL: H2L |
| ligand | ligand_11517 | Hydrogen imidobis(fluorosulfate) |  |


### Step 26: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_61 | Fe^[3+] |  |
| ligand | ligand_10162 | Hydrogen fluoride (Hydrofluoric acid) | SMILES: F; HxL: HL |
| beta_def | beta_def_872 |  | [M] + [L]^3 <=> [ML3] |
| beta_def | beta_def_840 |  | [M] + [L]^2 <=> [ML2] |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_177006 |  |
| map | ref_eq_map_29571 |  |
| vlm | vlm_177005 |  |
| map | ref_eq_map_29570 |  |
| vlm | vlm_177001 |  |
| vlm | vlm_177002 |  |
| vlm | vlm_176998 |  |
| map | ref_eq_map_29569 |  |
| vlm | vlm_176996 |  |
| vlm | vlm_176997 |  |


### Step 27: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_62 | Fe^[2+] |  |
| ligand | ligand_10162 | Hydrogen fluoride (Hydrofluoric acid) | SMILES: F; HxL: HL |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_176954 |  |
| map | ref_eq_map_29545 |  |


### Step 28: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_61 | Fe^[3+] |  |
| ligand | ligand_10148 | Hydrogen sulfate ion (Sulfuric acid) | SMILES: O=S(=O)([O-])O; HxL: HL |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_176065 |  |
| map | ref_eq_map_29192 |  |
| vlm | vlm_176061 |  |
| map | ref_eq_map_29188 |  |
| vlm | vlm_176062 |  |
| map | ref_eq_map_29189 |  |
| vlm | vlm_176063 |  |
| map | ref_eq_map_29190 |  |
| vlm | vlm_176064 |  |
| map | ref_eq_map_29191 |  |


### Step 29: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_62 | Fe^[2+] |  |
| ligand | ligand_10148 | Hydrogen sulfate ion (Sulfuric acid) | SMILES: O=S(=O)([O-])O; HxL: HL |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_176011 |  |
| map | ref_eq_map_29163 |  |


### Step 30: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_62 | Fe^[2+] |  |
| ligand | ligand_9873 | Acetohydroxamic acid | SMILES: CC(=O)NO; HxL: HL |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_168432 |  |
| map | ref_eq_map_26534 |  |


### Step 31: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_62 | Fe^[2+] |  |
| ligand | ligand_8873 | Propanedioic acid (Malonic acid) | SMILES: O=C(O)CC(=O)O; HxL: H2L |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_152297 |  |
| map | ref_eq_map_20098 |  |
| vlm | vlm_152296 |  |
| map | ref_eq_map_20097 |  |


### Step 32: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_62 | Fe^[2+] |  |
| ligand | ligand_8953 | L-Hydroxybutanedioic acid (Hydroxysuccinic acid)(Malic acid) | SMILES: O=C(O)CC(O)C(=O)O; HxL: H2L |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_154812 |  |
| map | ref_eq_map_21103 |  |


### Step 33: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_61 | Fe^[3+] |  |
| ligand | ligand_6774 | Pyridine-2,6-dicarboxylic acid (Dipicolinic acid) | SMILES: O=C(O)c1cccc(C(=O)O)n1; HxL: H2L |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_119514 |  |
| map | ref_eq_map_8532 |  |


### Step 34: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_62 | Fe^[2+] |  |
| ligand | ligand_6774 | Pyridine-2,6-dicarboxylic acid (Dipicolinic acid) | SMILES: O=C(O)c1cccc(C(=O)O)n1; HxL: H2L |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |
| ligand | ligand_6762 | Pyridine-2-carboxylic acid (Picolinic acid) | SMILES: O=C(O)c1ccccn1; HxL: HL |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_119483 |  |
| map | ref_eq_map_8525 |  |
| vlm | vlm_118872 |  |
| map | ref_eq_map_8350 |  |


### Step 35: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_192 | Tm^[3+] |  |
| ligand | ligand_6774 | Pyridine-2,6-dicarboxylic acid (Dipicolinic acid) | SMILES: O=C(O)c1cccc(C(=O)O)n1; HxL: H2L |
| beta_def | beta_def_840 |  | [M] + [L]^2 <=> [ML2] |
| beta_def | beta_def_872 |  | [M] + [L]^3 <=> [ML3] |
| metal | metal_81 | Lu^[3+] |  |
| metal | metal_206 | Yb^[3+] |  |
| metal | metal_205 | Y^[3+] |  |
| metal | metal_55 | Er^[3+] |  |
| metal | metal_73 | Ho^[3+] |  |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_119459 |  |
| vlm | vlm_119462 |  |
| vlm | vlm_119477 |  |
| vlm | vlm_119468 |  |
| vlm | vlm_119354 |  |
| vlm | vlm_119453 |  |
| vlm | vlm_119471 |  |
| vlm | vlm_119450 |  |
| vlm | vlm_119480 |  |
| vlm | vlm_119444 |  |


### Step 36: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_61 | Fe^[3+] |  |
| ligand | ligand_6041 | N,N'-Bis(3-hydroxy-5-phosphomethyl-2-methyl-4-pyridylmethyl)ethylenedinitrilodiacetic acid (DPDP) | SMILES: Cc1ncc(COP(=O)(O)O)c(CN(CCN(CC(=O)O)Cc2c(COP(=O)(O)O)cnc(C)c2O)CC(=O)O)c1O; HxL: H6L |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |
| ligand | ligand_8442 | Ethylenebis(imino(2-hydroxyphenyl)methylenephosphonous acid) | SMILES: O=[PH](O)C(NCCNC(c1ccccc1O)[PH](=O)O)c1ccccc1O; HxL: H4L |
| ligand | ligand_8389 | Ethylenebis[imino(2-hydroxyphenyl)methylenephosphonic acid] | SMILES: O=P(O)(O)C(NCCNC(c1ccccc1O)P(=O)(O)O)c1ccccc1O; HxL: H4L |
| ligand | ligand_8421 | N,N'-Dimethylethylenebis(nitrilomethylenephosphonic acid) | SMILES: CN(CCN(C)CP(=O)(O)O)CP(=O)(O)O; HxL: H4L |
| ligand | ligand_8424 | N,N'-Bis(2-hydroxyethyl)ethylenedinitrilo-N,N'-bis(methylenephosphonic acid) | SMILES: O=P(O)(O)CN(CCO)CCN(CCO)CP(=O)(O)O; HxL: H4L |
| ligand | ligand_8434 | Pyridine-2,6-diphosphonic acid (2,6-PDPA) | SMILES: O=P(O)(O)c1cccc(P(=O)(O)O)n1; HxL: H4L |
| ligand | ligand_8360 | Amino(phenyl)methylenediphosphonic acid | SMILES: NC(c1ccccc1)(P(=O)(O)O)P(=O)(O)O; HxL: H4L |
| ligand | ligand_8400 | Perhydro-1,4-oxazine-4-ylmethylenediphosphonic acid (N-(Diphosphonomethyl)morpholine) | SMILES: O=P(O)(O)C(N1CCOCC1)P(=O)(O)O; HxL: H4L |
| ligand | ligand_8427 | N-(2-Hydroxyethyl)ethylenedinitrilotris(methylenephosphonic acid) | SMILES: O=P(O)(O)CN(CCO)CCN(CP(=O)(O)O)CP(=O)(O)O; HxL: H6L |
| ligand | ligand_6195 | N-(2-Carboxyethyl)-N-(phosphonomethyl)glycine | SMILES: O=C(O)CCN(CC(=O)O)CP(=O)(O)O; HxL: H4L |
| ligand | ligand_5937 | N-(Phosphonomethyl)glycine (Glyphosate) | SMILES: O=C(O)CNCP(=O)(O)O; HxL: H3L |
| ligand | ligand_6770 | Pyridine-2-phosphonic-6-carboxylic acid (2PP6C) | SMILES: O=C(O)c1cccc(P(=O)(O)O)n1; HxL: H3L |
| ligand | ligand_8388 | Ethylenebis[imino(phenyl)methylenephosphonic acid] | SMILES: O=P(O)(O)C(NCCNC(c1ccccc1)P(=O)(O)O)c1ccccc1; HxL: H4L |
| ligand | ligand_9145 | Benzo-1,3-dioxole-2,2-diphosphonic acid [(1,2-Phenylenedioxy)methylenediphosphonic acid] | SMILES: O=P(O)(O)C1(P(=O)(O)O)Oc2ccccc2O1; HxL: H4L |
| ligand | ligand_6019 | N,N-Bis(phosphonomethyl)glycine | SMILES: O=C(O)CN(CP(=O)(O)O)CP(=O)(O)O; HxL: H5L |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_102165 |  |
| map | ref_eq_map_2456 |  |
| vlm | vlm_144047 |  |
| map | ref_eq_map_16802 |  |
| vlm | vlm_142729 |  |
| map | ref_eq_map_16461 |  |
| vlm | vlm_143569 |  |
| map | ref_eq_map_16695 |  |
| vlm | vlm_143632 |  |
| map | ref_eq_map_16712 |  |
| vlm | vlm_143992 |  |
| map | ref_eq_map_16775 |  |
| vlm | vlm_142134 |  |
| map | ref_eq_map_16292 |  |
| vlm | vlm_142932 |  |
| map | ref_eq_map_16548 |  |
| vlm | vlm_143661 |  |
| map | ref_eq_map_16721 |  |
| vlm | vlm_106311 |  |
| map | ref_eq_map_4131 |  |
| vlm | vlm_99817 |  |
| map | ref_eq_map_1596 |  |
| vlm | vlm_119195 |  |
| map | ref_eq_map_8467 |  |
| vlm | vlm_142698 |  |
| map | ref_eq_map_16451 |  |
| vlm | vlm_159347 |  |
| map | ref_eq_map_22651 |  |
| vlm | vlm_101516 |  |
| map | ref_eq_map_2238 |  |


### Step 37: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_61 | Fe^[3+] |  |
| ligand | ligand_6054 | N,N'-Bis(carboxymethyl)ethylenedinitrilobis(N-2-propylacetohydroxamic acid) | SMILES: CC(C)N(O)C(=O)CN(CCN(CC(=O)O)CC(=O)N(O)C(C)C)CC(=O)O; HxL: H4L |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |
| ligand | ligand_6057 | N,N',N''-Tris(carboxymethyl)diethylenetrinitrilobis(N-2-propylacetohydroxamic acid) | SMILES: CC(C)N(O)C(=O)CN(CCN(CCN(CC(=O)O)CC(=O)N(O)C(C)C)CC(=O)O)CC(=O)O; HxL: H5L |
| ligand | ligand_7320 | Ethylenedinitrilotetraacetohydroxamic acid | SMILES: O=C(CN(CCN(CC(=O)NO)CC(=O)NO)CC(=O)NO)NO; HxL: H4L |
| ligand | ligand_6036 | N,N'-Bis(carboxymethyl)ethylenedinitrilo-N,N'-diacetohydroxamic acid | SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)NO)CC(=O)NO; HxL: H4L |
| ligand | ligand_7295 | Nitrilotriacetohydroxamic acid | SMILES: O=C(CN(CC(=O)NO)CC(=O)NO)NO; HxL: H3L |
| ligand | ligand_6020 | N-(Carboxymethyl)-N-(2-hydroxyethyl)aminoacetohydroxamic acid | SMILES: O=C(O)CN(CCO)CC(=O)NO; HxL: H2L |
| ligand | ligand_7391 | Piperazine-N,N'-diacetohydroxamic acid | SMILES: O=C(CN1CCN(C(=O)NO)CC1)NO; HxL: H2L |
| ligand | ligand_6203 | N,N-Bis(carboxymethyl)aminoacetohydroxamic acid | SMILES: O=C(O)CN(CC(=O)O)CC(=O)NO; HxL: H3L |
| ligand | ligand_5938 | (Carboxymethylamino)acetohydroxamic acid | SMILES: O=C(O)CNCC(=O)NO; HxL: H2L |
| ligand | ligand_7154 | Iminodiacetohydroxamic acid | SMILES: O=C(CNCC(=O)NO)NO; HxL: H2L |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_102391 |  |
| map | ref_eq_map_2532 |  |
| vlm | vlm_102436 |  |
| map | ref_eq_map_2551 |  |
| vlm | vlm_127787 |  |
| map | ref_eq_map_11153 |  |
| vlm | vlm_101953 |  |
| map | ref_eq_map_2399 |  |
| vlm | vlm_127357 |  |
| map | ref_eq_map_10986 |  |
| vlm | vlm_101540 |  |
| map | ref_eq_map_2242 |  |
| vlm | vlm_128758 |  |
| map | ref_eq_map_11395 |  |
| vlm | vlm_106563 |  |
| map | ref_eq_map_4223 |  |
| vlm | vlm_99842 |  |
| map | ref_eq_map_1602 |  |
| vlm | vlm_124724 |  |
| map | ref_eq_map_10255 |  |


### Step 38: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_41 | Cu^[2+] |  |
| ligand | ligand_8938 | Benzene-1,2-dicarboxylic acid (Phthalic acid) | SMILES: O=C(O)c1ccccc1C(=O)O; HxL: H2L |
| beta_def | beta_def_840 |  | [M] + [L]^2 <=> [ML2] |
| metal | metal_68 | H^[+] |  |
| ligand | ligand_9154 | Phosphoric acid 1-naphthyl ester (alpha-Naphthyl phosphate) | SMILES: O=P(O)(O)Oc1cccc2ccccc12; HxL: H2L |
| beta_def | beta_def_79 |  | [L] + [H] <=> [HL] |
| ligand | ligand_9152 | Phosphoric acid phenyl ester (Phenyl phosphate) | SMILES: O=P(O)(O)Oc1ccccc1; HxL: H2L |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |
| ligand | ligand_8758 | 2-Methoxybenzoic acid | SMILES: COc1ccccc1C(=O)O; HxL: HL |
| metal | metal_208 | Zn^[2+] |  |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_154479 |  |
| vlm | vlm_159458 |  |
| vlm | vlm_159441 |  |
| vlm | vlm_159430 |  |
| vlm | vlm_159465 |  |
| vlm | vlm_154376 |  |
| vlm | vlm_154472 |  |
| vlm | vlm_150325 |  |
| vlm | vlm_154494 |  |
| vlm | vlm_154377 |  |


### Step 39: `search_ligands`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| ligand | ligand_8701 | 2-Acetoxybenzoic acid (Acetylsalicylic acid) | SMILES: CC(=O)Oc1ccccc1C(=O)O; HxL: HL |
| ligand | ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | SMILES: O=C(O)c1ccccc1O; HxL: H2L |
| ligand | ligand_9265 | 2-Hydroxy-3-methylbenzoic acid (3-Methylsalicylic acid)(o-Cresotic acid) | SMILES: Cc1cccc(C(=O)O)c1O; HxL: H2L |
| ligand | ligand_9266 | 2-Hydroxy-4-methylbenzoic acid (4-Methylsalicylic acid)(m-Cresotic acid) | SMILES: Cc1ccc(C(=O)O)c(O)c1; HxL: H2L |
| ligand | ligand_9267 | 2-Hydroxy-5-methylbenzoic acid (5-Methylsalicylic acid)(p-Cresotic acid) | SMILES: Cc1ccc(O)c(C(=O)O)c1; HxL: H2L |
| ligand | ligand_9268 | 2-Hydroxy-6-methylbenzoic acid (6-Methylsalicylic acid) | SMILES: Cc1cccc(O)c1C(=O)O; HxL: H2L |
| ligand | ligand_9269 | 2-Hydroxy-3-(2-propyl)benzoic acid (3-Isopropylsalicylic acid) | SMILES: CC(C)c1cccc(C(=O)O)c1O; HxL: H2L |
| ligand | ligand_9274 | 5-Fluoro-2-hydroxybenzoic acid (5-Fluorosalicylic acid) | SMILES: O=C(O)c1cc(F)ccc1O; HxL: H2L |
| ligand | ligand_9275 | 5-Chloro-2-hydroxybenzoic acid (5-Chlorosalicylic acid) | SMILES: O=C(O)c1cc(Cl)ccc1O; HxL: H2L |
| ligand | ligand_9276 | 6-Chloro-2-hydroxybenzoic acid (6-Chlorosalicylic acid) | SMILES: O=C(O)c1c(O)cccc1Cl; HxL: H2L |
| ligand | ligand_9277 | 5-Bromo-2-hydroxybenzoic acid (5-Bromosalicylic acid) | SMILES: O=C(O)c1cc(Br)ccc1O; HxL: H2L |
| ligand | ligand_9278 | 2-Hydroxy-5-iodobenzoic acid (5-Iodosalicylic acid) | SMILES: O=C(O)c1cc(I)ccc1O; HxL: H2L |
| ligand | ligand_9279 | 2-Hydroxy-3-nitrobenzoic acid (3-Nitrosalicylic acid) | SMILES: O=C(O)c1cccc([N+](=O)[O-])c1O; HxL: H2L |
| ligand | ligand_9280 | 2-Hydroxy-4-nitrobenzoic acid (4-Nitrosalicylic acid) | SMILES: O=C(O)c1ccc([N+](=O)[O-])cc1O; HxL: H2L |
| ligand | ligand_9281 | 2-Hydroxy-5-nitrobenzoic acid (5-Nitrosalicylic acid) | SMILES: O=C(O)c1cc([N+](=O)[O-])ccc1O; HxL: H2L |
| ligand | ligand_9282 | 2-Hydroxy-6-nitrobenzoic acid (6-Nitrosalicylic acid) | SMILES: O=C(O)c1c(O)cccc1[N+](=O)[O-]; HxL: H2L |
| ligand | ligand_9283 | 2-Hydroxy-3,5-dinitrobenzoic acid (3,5-Dinitrosalicylic acid) | SMILES: O=C(O)c1cc([N+](=O)[O-])cc([N+](=O)[O-])c1O; HxL: H2L |
| ligand | ligand_9284 | 2-Hydroxy-5-sulfobenzoic acid (5-Sulfosalicylic acid) | SMILES: O=C(O)c1cc(S(=O)(=O)O)ccc1O; HxL: H3L |
| ligand | ligand_9285 | 3-Bromo-2-hydroxy-5-sulfobenzoic acid (3-Bromo-5-sulfosalicylic acid) | SMILES: O=C(O)c1cc(S(=O)(=O)O)cc(Br)c1O; HxL: H3L |
| ligand | ligand_9287 | 2-Hydroxy-3,5-disulfobenzoic acid (3,5-Disulfosalicylic acid) | SMILES: O=C(O)c1cc(S(=O)(=O)O)cc(S(=O)(=O)O)c1O; HxL: H4L |
| ligand | ligand_9288 | 2-Hydroxy-3-methoxybenzoic acid (3-Methoxysalicylic acid) | SMILES: COc1cccc(C(=O)O)c1O; HxL: H2L |
| ligand | ligand_9289 | 2-Hydroxy-5-methoxybenzoic acid (5-Methoxysalicylic acid) | SMILES: COc1ccc(O)c(C(=O)O)c1; HxL: H2L |
| ligand | ligand_9296 | 2-Hydroxy-5-cyanobenzoic acid (5-Cyanosalicylic acid) | SMILES: N#Cc1ccc(O)c(C(=O)O)c1; HxL: H2L |
| ligand | ligand_9297 | 4-Amino-2-hydroxybenzoic acid (p-Aminosalicylic acid) | SMILES: Nc1ccc(C(=O)O)c(O)c1; HxL: H2L |
| ligand | ligand_9298 | 5-Amino-2-hydroxybenzoic acid (m-Aminosalicylic acid) | SMILES: Nc1ccc(O)c(C(=O)O)c1; HxL: H2L |


### Step 40: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_41 | Cu^[2+] |  |
| ligand | ligand_8938 | Benzene-1,2-dicarboxylic acid (Phthalic acid) | SMILES: O=C(O)c1ccccc1C(=O)O; HxL: H2L |
| beta_def | beta_def_840 |  | [M] + [L]^2 <=> [ML2] |
| metal | metal_206 | Yb^[3+] |  |
| ligand | ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | SMILES: O=C(O)c1ccccc1O; HxL: H2L |
| beta_def | beta_def_194 |  | [M] + [HL]^2 <=> [M(HL)2] |
| metal | metal_68 | H^[+] |  |
| beta_def | beta_def_79 |  | [L] + [H] <=> [HL] |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |
| metal | metal_81 | Lu^[3+] |  |
| metal | metal_208 | Zn^[2+] |  |
| metal | metal_73 | Ho^[3+] |  |
| metal | metal_192 | Tm^[3+] |  |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_154479 |  |
| vlm | vlm_160348 |  |
| vlm | vlm_154376 |  |
| vlm | vlm_154472 |  |
| vlm | vlm_160354 |  |
| vlm | vlm_154494 |  |
| vlm | vlm_154377 |  |
| vlm | vlm_154473 |  |
| vlm | vlm_160330 |  |
| vlm | vlm_160342 |  |


### Step 41: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_41 | Cu^[2+] |  |
| ligand | ligand_8938 | Benzene-1,2-dicarboxylic acid (Phthalic acid) | SMILES: O=C(O)c1ccccc1C(=O)O; HxL: H2L |
| beta_def | beta_def_840 |  | [M] + [L]^2 <=> [ML2] |
| metal | metal_206 | Yb^[3+] |  |
| ligand | ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | SMILES: O=C(O)c1ccccc1O; HxL: H2L |
| beta_def | beta_def_194 |  | [M] + [HL]^2 <=> [M(HL)2] |
| metal | metal_68 | H^[+] |  |
| beta_def | beta_def_79 |  | [L] + [H] <=> [HL] |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |
| metal | metal_81 | Lu^[3+] |  |
| metal | metal_208 | Zn^[2+] |  |
| metal | metal_73 | Ho^[3+] |  |
| metal | metal_192 | Tm^[3+] |  |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_154479 |  |
| vlm | vlm_160348 |  |
| vlm | vlm_154376 |  |
| vlm | vlm_154472 |  |
| vlm | vlm_160354 |  |
| vlm | vlm_154494 |  |
| vlm | vlm_154377 |  |
| vlm | vlm_154473 |  |
| vlm | vlm_160330 |  |
| vlm | vlm_160342 |  |


### Step 42: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_61 | Fe^[3+] |  |
| ligand | ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | SMILES: O=C(O)c1ccccc1O; HxL: H2L |
| beta_def | beta_def_779 |  | [M] + [HL] <=> [MHL] |
| beta_def | beta_def_821 |  | [M] + [HL] <=> [ML] + [H] |
| beta_def | beta_def_846 |  | [ML] + [HL] <=> [ML2] + [H] |
| metal | metal_62 | Fe^[2+] |  |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_160412 |  |
| map | ref_eq_map_23105 |  |
| vlm | vlm_160398 |  |
| vlm | vlm_160400 |  |
| map | ref_eq_map_23108 |  |
| vlm | vlm_160402 |  |
| map | ref_eq_map_23110 |  |
| vlm | vlm_160401 |  |
| map | ref_eq_map_23109 |  |
| vlm | vlm_160403 |  |
| map | ref_eq_map_23107 |  |
| vlm | vlm_160411 |  |
| vlm | vlm_160409 |  |
| vlm | vlm_160410 |  |
| map | ref_eq_map_23106 |  |
| vlm | vlm_160399 |  |
| vlm | vlm_160404 |  |
| map | ref_eq_map_23111 |  |
| vlm | vlm_160374 |  |
| map | ref_eq_map_23094 |  |
| vlm | vlm_160375 |  |


### Step 43: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_61 | Fe^[3+] |  |
| ligand | ligand_6165 | Nitrilotriacetic acid (NTA) | SMILES: O=C(O)CN(CC(=O)O)CC(=O)O; HxL: H3L |
| beta_def | beta_def_840 |  | [M] + [L]^2 <=> [ML2] |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |
| beta_def | beta_def_263 |  | [M(OH)3L] + [H] <=> [M(OH)2L] + [H2O] |
| beta_def | beta_def_788 |  | [ML] + [H] <=> [MHL] |
| beta_def | beta_def_423 |  | [ML]^2 + [H2O]^2 <=> [M2(OH)2L2] + [H]^2 |
| beta_def | beta_def_966 |  | [M(OH)L] + [H] <=> [ML] + [H2O] |
| beta_def | beta_def_427 |  | [M(OH)L]^2 <=> [M2(OH)2L2] |
| beta_def | beta_def_238 |  | [M(OH)2L] + [H] <=> [M(OH)L] + [H2O] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_105558 |  |
| map | ref_eq_map_3756 |  |
| vlm | vlm_105557 |  |
| map | ref_eq_map_3754 |  |
| vlm | vlm_105553 |  |
| vlm | vlm_105554 |  |
| map | ref_eq_map_3755 |  |
| vlm | vlm_105566 |  |
| vlm | vlm_105559 |  |
| vlm | vlm_105568 |  |
| vlm | vlm_105562 |  |
| map | ref_eq_map_3757 |  |
| vlm | vlm_105567 |  |
| vlm | vlm_105561 |  |
| vlm | vlm_105560 |  |
| vlm | vlm_105563 |  |
| vlm | vlm_105564 |  |
| vlm | vlm_105565 |  |


### Step 44: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_62 | Fe^[2+] |  |
| ligand | ligand_6165 | Nitrilotriacetic acid (NTA) | SMILES: O=C(O)CN(CC(=O)O)CC(=O)O; HxL: H3L |
| beta_def | beta_def_840 |  | [M] + [L]^2 <=> [ML2] |
| beta_def | beta_def_966 |  | [M(OH)L] + [H] <=> [ML] + [H2O] |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_105498 |  |
| map | ref_eq_map_3742 |  |
| vlm | vlm_105499 |  |
| map | ref_eq_map_3744 |  |
| vlm | vlm_105500 |  |
| vlm | vlm_105501 |  |
| map | ref_eq_map_3743 |  |
| vlm | vlm_105495 |  |
| vlm | vlm_105496 |  |
| vlm | vlm_105497 |  |


### Step 45: `search_ligands`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| ligand | ligand_5938 | (Carboxymethylamino)acetohydroxamic acid | SMILES: O=C(O)CNCC(=O)NO; HxL: H2L |
| ligand | ligand_6020 | N-(Carboxymethyl)-N-(2-hydroxyethyl)aminoacetohydroxamic acid | SMILES: O=C(O)CN(CCO)CC(=O)NO; HxL: H2L |
| ligand | ligand_6036 | N,N'-Bis(carboxymethyl)ethylenedinitrilo-N,N'-diacetohydroxamic acid | SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)NO)CC(=O)NO; HxL: H4L |
| ligand | ligand_6054 | N,N'-Bis(carboxymethyl)ethylenedinitrilobis(N-2-propylacetohydroxamic acid) | SMILES: CC(C)N(O)C(=O)CN(CCN(CC(=O)O)CC(=O)N(O)C(C)C)CC(=O)O; HxL: H4L |
| ligand | ligand_6057 | N,N',N''-Tris(carboxymethyl)diethylenetrinitrilobis(N-2-propylacetohydroxamic acid) | SMILES: CC(C)N(O)C(=O)CN(CCN(CCN(CC(=O)O)CC(=O)N(O)C(C)C)CC(=O)O)CC(=O)O; HxL: H5L |
| ligand | ligand_6203 | N,N-Bis(carboxymethyl)aminoacetohydroxamic acid | SMILES: O=C(O)CN(CC(=O)O)CC(=O)NO; HxL: H3L |
| ligand | ligand_6982 | Aminoacetohydroxamic acid (Glycinehydroxamic acid) | SMILES: NCC(=O)NO; HxL: HL |
| ligand | ligand_6992 | Methylaminoacetohydroxamic acid (Sarcosinehydroxamic acid) | SMILES: CNCC(=O)NO; HxL: HL |
| ligand | ligand_7154 | Iminodiacetohydroxamic acid | SMILES: O=C(CNCC(=O)NO)NO; HxL: H2L |
| ligand | ligand_7282 | N,N-Bis(2-hydroxyethyl)aminoacetohydroxamic acid | SMILES: O=C(CCN(CCO)CCO)NO; HxL: HL |
| ligand | ligand_7295 | Nitrilotriacetohydroxamic acid | SMILES: O=C(CN(CC(=O)NO)CC(=O)NO)NO; HxL: H3L |
| ligand | ligand_7320 | Ethylenedinitrilotetraacetohydroxamic acid | SMILES: O=C(CN(CCN(CC(=O)NO)CC(=O)NO)CC(=O)NO)NO; HxL: H4L |
| ligand | ligand_7391 | Piperazine-N,N'-diacetohydroxamic acid | SMILES: O=C(CN1CCN(C(=O)NO)CC1)NO; HxL: H2L |
| ligand | ligand_7709 | 5,7-Dioxo-1,4,8,11-tetraazacyclotetradecane-4,8-bis(N-methylacetohydroxamic acid) | SMILES: CN(O)C(=O)CN1CCNCCCNCCN(CC(=O)N(C)O)C(=O)CC1=O; HxL: H2L |
| ligand | ligand_9873 | Acetohydroxamic acid | SMILES: CC(=O)NO; HxL: HL |
| ligand | ligand_9875 | N-Methylacetohydroxamic acid | SMILES: CC(=O)N(C)O; HxL: HL |
| ligand | ligand_9876 | N-Phenylacetohydroxamic acid | SMILES: CC(=O)N(O)c1ccccc1; HxL: HL |
| ligand | ligand_9877 | N-(4-Methylphenyl)acetohydroxamic acid | SMILES: CC(=O)N(O)c1ccc(C)cc1; HxL: HL |
| ligand | ligand_9878 | N-(3-Cyanophenyl)acetohydroxamic acid | SMILES: CC(=O)N(O)c1cccc(C#N)c1; HxL: HL |
| ligand | ligand_9879 | N-(4-Cyanophenyl)acetohydroxamic acid | SMILES: CC(=O)N(O)c1ccc(C#N)cc1; HxL: HL |
| ligand | ligand_9880 | N-(4-Chlorophenyl)acetohydroxamic acid | SMILES: CC(=O)N(O)c1ccc(Cl)cc1; HxL: HL |
| ligand | ligand_9881 | N-(3-Iodophenyl)acetohydroxamic acid | SMILES: CC(=O)N(O)c1cccc(I)c1; HxL: HL |
| ligand | ligand_9882 | N-(4-Iodophenyl)acetohydroxamic acid | SMILES: CC(=O)N(O)c1ccc(I)cc1; HxL: HL |
| ligand | ligand_9883 | N-(3-Acetylphenyl)acetohydroxamic acid | SMILES: CC(=O)c1cccc(N(O)C(C)=O)c1; HxL: HL |
| ligand | ligand_11339 | Phenylacetohydroxamic acid |  |


### Step 46: `search_ligands`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| ligand | ligand_8668 | D-gluco-Pentahydroxyhexanoic acid (D-Gluconic acid) | SMILES: O=C(O)[C@H](O)[C@@H](O)[C@H](O)[C@H](O)CO; HxL: HL |
| ligand | ligand_10317 | 6-[Bis(1-methylethyl)aminoacetyl]gluconic acid (Pangamic acid) |  |


### Step 47: `search_ligands`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| ligand | ligand_9150 | Phosphoric acid methyl ester (Methyl phosphate) | SMILES: COP(=O)(O)O; HxL: H2L |
| ligand | ligand_9151 | Phosphoric acid butyl ester (Butyl phosphate) | SMILES: CCCCOP(=O)(O)O; HxL: H2L |
| ligand | ligand_9152 | Phosphoric acid phenyl ester (Phenyl phosphate) | SMILES: O=P(O)(O)Oc1ccccc1; HxL: H2L |
| ligand | ligand_9153 | Phosphoric acid 4-nitrophenyl ester (4-Nitrophenyl phosphate) | SMILES: O=[N+]([O-])c1ccc(OP(=O)(O)O)cc1; HxL: H2L |
| ligand | ligand_9154 | Phosphoric acid 1-naphthyl ester (alpha-Naphthyl phosphate) | SMILES: O=P(O)(O)Oc1cccc2ccccc12; HxL: H2L |
| ligand | ligand_9155 | Phosphoric acid 2-naphthyl ester (beta-Naphthyl phosphate) | SMILES: O=P(O)(O)Oc1ccc2ccccc2c1; HxL: H2L |
| ligand | ligand_9156 | Phosphoric acid 4-nitrophenyl ester (p-Nitrophenyl phosphate) | SMILES: O=[N+]([O-])c1ccc(OP(=O)(O)O)cc1; HxL: H2L |
| ligand | ligand_9163 | Phosphoric acid dibutyl ester (Dibutyl phosphate) | SMILES: CCCCOP(=O)(O)OCCCC; HxL: HL |
| ligand | ligand_9165 | Diphosphoric acid methyl ester (Methyl diphosphate) | SMILES: COP(=O)(O)OP(=O)(O)O; HxL: H3L |
| ligand | ligand_9166 | Diphosphoric acid butyl ester (Butyl diphosphate) | SMILES: CCCCOP(=O)(O)OP(=O)(O)O; HxL: H3L |
| ligand | ligand_9167 | Diphosphoric acid phenyl ester (Phenyl diphosphate) | SMILES: O=P(O)(O)OP(=O)(O)Oc1ccccc1; HxL: H3L |
| ligand | ligand_9168 | Triphosphoric acid methyl ester (Methyl triphosphate) | SMILES: COP(=O)(O)OP(=O)(O)OP(=O)(O)O; HxL: H4L |
| ligand | ligand_9173 | Phosphorodithioic acid O,O-dibutyl ester (Dibutyldithiophosphoric acid) | SMILES: CCCCOP(=S)(S)OCCCC; HxL: HL |
| ligand | ligand_9174 | Phosphorodithioic acid O,O-bis(2-methylpropyl) ester (Diisobutyldithiophosphoric acid) | SMILES: CC(C)COP(=S)(S)OCC(C)C; HxL: HL |
| ligand | ligand_10113 | Hydrogen phosphate (Phosphoric acid) | SMILES: O=P(O)(O)O; HxL: H3L |
| ligand | ligand_10114 | Hydrogen diphosphate (Pyrophosphoric acid) | SMILES: O=P(O)(O)OP(=O)(O)O; HxL: H4L |
| ligand | ligand_10116 | Hydrogen hypophosphate (Hypophosphoric acid) | SMILES: O=P(O)(O)P(=O)(O)O; HxL: H4L |
| ligand | ligand_10117 | Hydrogen triphosphate (Triphosphoric acid) | SMILES: O=P(O)(O)OP(=O)(O)OP(=O)(O)O; HxL: H5L |
| ligand | ligand_10119 | Hydrogen tetraphosphate (Tetraphosphoric acid) | SMILES: O=P(O)(O)OP(=O)(O)OP(=O)(O)OP(=O)(O)O; HxL: H6L |
| ligand | ligand_10120 | Hydrogen pentaphosphate (Pentaphosphoric acid) | SMILES: O=P(O)(O)OP(=O)(O)OP(=O)(O)OP(=O)(O)OP(=O)(O)O; HxL: H6L |
| ligand | ligand_10121 | Hydrogen hexaphosphate (Hexaphosphoric acid) | SMILES: O=P(O)(O)OP(=O)(O)OP(=O)(O)OP(=O)(O)O[PH](O)(O)OP(=O)(O)O; HxL: H7L |
| ligand | ligand_10122 | Hydrogen heptaphosphate (Heptaphosphoric acid) | SMILES: O=P(O)(O)OP(=O)(O)OP(=O)(O)OP(=O)(O)O[PH](O)(O)O[PH](O)(O)OP(=O)(O)O; HxL: H8L |
| ligand | ligand_10123 | Hydrogen trimetaphosphate (Trimetaphosphoric acid) | SMILES: O=P1(O)OP(=O)(O)OP(=O)(O)O1; HxL: H3L |
| ligand | ligand_10124 | Hydrogen tetrametaphosphate (Tetrametaphosphoric acid) | SMILES: O=P1(O)OP(=O)(O)OP(=O)(O)OP(=O)(O)O1; HxL: H4L |
| ligand | ligand_10125 | Hydrogen hexametaphosphate (Hexametaphosphoric acid) | SMILES: O=P1(O)OP(=O)(O)OP(=O)(O)OP(=O)(O)OP(=O)(O)OP(=O)(O)O1; HxL: H6L |


### Step 48: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_61 | Fe^[3+] |  |
| ligand | ligand_10113 | Hydrogen phosphate (Phosphoric acid) | SMILES: O=P(O)(O)O; HxL: H3L |
| beta_def | beta_def_779 |  | [M] + [HL] <=> [MHL] |
| beta_def | beta_def_172 |  | [M] + [H2L]^3 <=> [M(H2L)3] |
| beta_def | beta_def_156 |  | [M] + [H2L]^2 <=> [M(H2L)2] |
| beta_def | beta_def_732 |  | [M] + [H2L] <=> [MH2L] |
| beta_def | beta_def_751 |  | [MH2L] + [H] <=> [MH3L] |
| beta_def | beta_def_305 |  | [ML(H2O)2(s,am)] <=> [M] + [L] + [H2O]^2 |
| beta_def | beta_def_304 |  | [ML(H2O)2(s)] <=> [M] + [L] + [H2O]^2 |
| metal | metal_62 | Fe^[2+] |  |
| beta_def | beta_def_171 |  | [MH3L2] + [H] <=> [M(H2L)2] |
| beta_def | beta_def_623 |  | [M3L2(H2O)8(s,vivianite)] <=> [M]^3 + [L]^2 + [H2O]^8 |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_174470 |  |
| map | ref_eq_map_28587 |  |
| vlm | vlm_174475 |  |
| map | ref_eq_map_28586 |  |
| vlm | vlm_174471 |  |
| vlm | vlm_174474 |  |
| vlm | vlm_174472 |  |
| vlm | vlm_174473 |  |
| vlm | vlm_174476 |  |
| vlm | vlm_174478 |  |
| vlm | vlm_174477 |  |
| map | ref_eq_map_28585 |  |
| vlm | vlm_174448 |  |
| map | ref_eq_map_28575 |  |
| vlm | vlm_174445 |  |
| vlm | vlm_174447 |  |
| vlm | vlm_174446 |  |
| vlm | vlm_174449 |  |
| map | ref_eq_map_28574 |  |


### Step 49: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_61 | Fe^[3+] |  |
| ligand | ligand_8668 | D-gluco-Pentahydroxyhexanoic acid (D-Gluconic acid) | SMILES: O=C(O)[C@H](O)[C@@H](O)[C@H](O)[C@H](O)CO; HxL: HL |
| beta_def | beta_def_187 |  | [M(OH)(H-3L)] + [H] <=> [M(H-3L)] + [H2O] |
| beta_def | beta_def_831 |  | [M(H-2L)] + [H]^2 <=> [ML] |
| beta_def | beta_def_153 |  | [M(H-3L)] + [H] <=> [M(H-2L)] |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |
| metal | metal_62 | Fe^[2+] |  |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_149280 |  |
| map | ref_eq_map_18879 |  |
| vlm | vlm_149278 |  |
| vlm | vlm_149279 |  |
| vlm | vlm_149277 |  |
| vlm | vlm_149274 |  |
| map | ref_eq_map_18877 |  |


### Step 50: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_1 | Ac^[3+] |  |
| ligand | ligand_10113 | Hydrogen phosphate (Phosphoric acid) | SMILES: O=P(O)(O)O; HxL: H3L |
| beta_def | beta_def_732 |  | [M] + [H2L] <=> [MH2L] |
| metal | metal_2 | Ag^[+] |  |
| beta_def | beta_def_739 |  | [MHL] + [H] <=> [MH2L] |
| beta_def | beta_def_756 |  | [M(HL)2] + [H] <=> [MH3L2] |
| beta_def | beta_def_156 |  | [M] + [H2L]^2 <=> [M(H2L)2] |
| beta_def | beta_def_621 |  | [M3L(s)] <=> [M]^3 + [L] |
| metal | metal_5 | Al^[3+] |  |
| ligand | ligand_10114 | Hydrogen diphosphate (Pyrophosphoric acid) | SMILES: O=P(O)(O)OP(=O)(O)O; HxL: H4L |
| beta_def | beta_def_840 |  | [M] + [L]^2 <=> [ML2] |
| ligand | ligand_10117 | Hydrogen triphosphate (Triphosphoric acid) | SMILES: O=P(O)(O)OP(=O)(O)OP(=O)(O)O; HxL: H5L |
| beta_def | beta_def_502 |  | [M]^2 + [L] <=> [M2L] |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |
| beta_def | beta_def_779 |  | [M] + [HL] <=> [MHL] |
| beta_def | beta_def_512 |  | [M2(OH)2L] + [H]^2 <=> [M2L] + [H2O]^2 |
| beta_def | beta_def_966 |  | [M(OH)L] + [H] <=> [ML] + [H2O] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_174423 |  |
| map | ref_eq_map_28566 |  |
| vlm | vlm_174492 |  |
| map | ref_eq_map_28594 |  |
| vlm | vlm_174493 |  |
| vlm | vlm_174491 |  |
| vlm | vlm_174490 |  |
| vlm | vlm_174494 |  |
| map | ref_eq_map_28593 |  |
| vlm | vlm_174772 |  |
| map | ref_eq_map_28683 |  |
| vlm | vlm_174984 |  |
| map | ref_eq_map_28754 |  |
| vlm | vlm_174530 |  |
| map | ref_eq_map_28610 |  |
| vlm | vlm_174529 |  |
| map | ref_eq_map_28609 |  |
| vlm | vlm_174528 |  |
| vlm | vlm_174771 |  |
| vlm | vlm_174983 |  |
| vlm | vlm_174985 |  |
| vlm | vlm_174773 |  |
| vlm | vlm_174538 |  |
| vlm | vlm_174987 |  |
| vlm | vlm_174775 |  |
| vlm | vlm_174532 |  |
| vlm | vlm_174537 |  |


### Step 51: `search_pka_values`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| ligand | ligand_7295 | Nitrilotriacetohydroxamic acid | SMILES: O=C(CN(CC(=O)NO)CC(=O)NO)NO; HxL: H3L |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_127316 |  |
| pka | pka_3850 |  |
| vlm | vlm_127331 |  |
| pka | pka_3849 |  |
| vlm | vlm_127326 |  |
| pka | pka_3851 |  |
| vlm | vlm_127321 |  |
| pka | pka_3848 |  |


### Step 52: `search_ligands`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| ligand | ligand_8640 | Hydroxyacetic acid (Glycolic acid) | SMILES: O=C(O)CO; HxL: HL |
| ligand | ligand_8766 | Mercaptoacetic acid (Thioglycolic acid) | SMILES: O=C(O)CS; HxL: H2L |
| ligand | ligand_8974 | Oxydiacetic acid (Diglycolic acid) | SMILES: O=C(O)COCC(=O)O; HxL: H2L |
| ligand | ligand_10907 | Acrylamidoglycolic acid |  |


### Step 53: `search_ligands`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| ligand | ligand_8641 | D-2-Hydroxypropanoic acid (Lactic acid) | SMILES: CC(O)C(=O)O; HxL: HL |
| ligand | ligand_8660 | DL-2-Phenyl-2-hydroxypropanoic acid (Atrolactic acid) | SMILES: CC(O)(C(=O)O)c1ccccc1; HxL: HL |
| ligand | ligand_8767 | DL-2-Mercaptopropanoic acid (Thiolactic acid) | SMILES: CC(S)C(=O)O; HxL: H2L |
| ligand | ligand_8976 | DL-2,2'-Oxydipropanoic acid (Dilactic acid) | SMILES: CC(OC(C)C(=O)O)C(=O)O; HxL: H2L |


### Step 54: `search_ligands`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| ligand | ligand_9601 | L-3,4-Dihydroxy-5-(1,2-dihydroxyethyl)-2,5-H-oxole-2-one (L-Ascorbic acid) | SMILES: O=C1O[C@H]([C@@H](O)CO)C(O)=C1O; HxL: H2L |
| ligand | ligand_11203 | Dehydroascorbic acid |  |


### Step 55: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_61 | Fe^[3+] |  |
| ligand | ligand_8640 | Hydroxyacetic acid (Glycolic acid) | SMILES: O=C(O)CO; HxL: HL |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |
| beta_def | beta_def_136 |  | [M(H-1L)] + [L] <=> [M(H-1L)L] |
| beta_def | beta_def_140 |  | [M(H-1L)L] + [L] <=> [M(H-1L)L2] |
| beta_def | beta_def_107 |  | [M(H-1L)] + [H] <=> [ML] |
| metal | metal_62 | Fe^[2+] |  |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_147409 |  |
| map | ref_eq_map_18185 |  |
| vlm | vlm_147411 |  |
| vlm | vlm_147412 |  |
| vlm | vlm_147410 |  |
| vlm | vlm_147386 |  |
| map | ref_eq_map_18174 |  |


### Step 56: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_2 | Ag^[+] |  |
| ligand | ligand_5761 | L-2-Aminopropanoic acid (Alanine) | SMILES: C[C@H](N)C(=O)O; HxL: HL |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |
| beta_def | beta_def_840 |  | [M] + [L]^2 <=> [ML2] |
| metal | metal_5 | Al^[3+] |  |
| ligand | ligand_8874 | Ethane-1,1-dicarboxylic acid (Methylmalonic acid) | SMILES: CC(C(=O)O)C(=O)O; HxL: H2L |
| beta_def | beta_def_872 |  | [M] + [L]^3 <=> [ML3] |
| ligand | ligand_8641 | D-2-Hydroxypropanoic acid (Lactic acid) | SMILES: CC(O)C(=O)O; HxL: HL |
| beta_def | beta_def_834 |  | [M(OH)2L] + [H]^2 <=> [ML] + [H2O]^2 |
| beta_def | beta_def_839 |  | [M(OH)L] + [H] <=> [ML] + [H2O] |
| beta_def | beta_def_984 |  | [M(OH)L2] + [H] <=> [ML2] + [H2O] |
| beta_def | beta_def_415 |  | [M]^2 + [L] + [H2O]^2 <=> [M2(OH)2L] + [H]^2 |
| beta_def | beta_def_411 |  | [M]^2 + [HL]^2 + [H2O]^2 <=> [M2(OH)2(H-1L)2] + [H]^6 |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_94297 |  |
| map | ref_eq_map_209 |  |
| vlm | vlm_94298 |  |
| vlm | vlm_94299 |  |
| map | ref_eq_map_210 |  |
| vlm | vlm_152506 |  |
| map | ref_eq_map_20166 |  |
| vlm | vlm_147807 |  |
| map | ref_eq_map_18330 |  |
| vlm | vlm_152505 |  |
| vlm | vlm_147804 |  |
| vlm | vlm_147805 |  |
| map | ref_eq_map_18331 |  |
| vlm | vlm_152504 |  |
| vlm | vlm_147802 |  |
| vlm | vlm_147803 |  |
| vlm | vlm_147806 |  |
| vlm | vlm_147808 |  |
| vlm | vlm_147809 |  |
| vlm | vlm_147800 |  |
| vlm | vlm_147801 |  |
| vlm | vlm_147811 |  |
| vlm | vlm_147810 |  |
| vlm | vlm_147812 |  |
| vlm | vlm_147813 |  |


### Step 57: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_61 | Fe^[3+] |  |
| ligand | ligand_9601 | L-3,4-Dihydroxy-5-(1,2-dihydroxyethyl)-2,5-H-oxole-2-one (L-Ascorbic acid) | SMILES: O=C1O[C@H]([C@@H](O)CO)C(O)=C1O; HxL: H2L |
| beta_def | beta_def_194 |  | [M] + [HL]^2 <=> [M(HL)2] |
| metal | metal_62 | Fe^[2+] |  |
| beta_def | beta_def_788 |  | [ML] + [H] <=> [MHL] |
| beta_def | beta_def_779 |  | [M] + [HL] <=> [MHL] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_166776 |  |
| map | ref_eq_map_25795 |  |
| vlm | vlm_166768 |  |
| map | ref_eq_map_25789 |  |
| vlm | vlm_166767 |  |


### Step 58: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_2 | Ag^[+] |  |
| ligand | ligand_5761 | L-2-Aminopropanoic acid (Alanine) | SMILES: C[C@H](N)C(=O)O; HxL: HL |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |
| beta_def | beta_def_840 |  | [M] + [L]^2 <=> [ML2] |
| metal | metal_5 | Al^[3+] |  |
| ligand | ligand_8874 | Ethane-1,1-dicarboxylic acid (Methylmalonic acid) | SMILES: CC(C(=O)O)C(=O)O; HxL: H2L |
| beta_def | beta_def_872 |  | [M] + [L]^3 <=> [ML3] |
| ligand | ligand_8641 | D-2-Hydroxypropanoic acid (Lactic acid) | SMILES: CC(O)C(=O)O; HxL: HL |
| beta_def | beta_def_834 |  | [M(OH)2L] + [H]^2 <=> [ML] + [H2O]^2 |
| beta_def | beta_def_839 |  | [M(OH)L] + [H] <=> [ML] + [H2O] |
| beta_def | beta_def_984 |  | [M(OH)L2] + [H] <=> [ML2] + [H2O] |
| beta_def | beta_def_415 |  | [M]^2 + [L] + [H2O]^2 <=> [M2(OH)2L] + [H]^2 |
| beta_def | beta_def_411 |  | [M]^2 + [HL]^2 + [H2O]^2 <=> [M2(OH)2(H-1L)2] + [H]^6 |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_94297 |  |
| map | ref_eq_map_209 |  |
| vlm | vlm_94298 |  |
| vlm | vlm_94299 |  |
| map | ref_eq_map_210 |  |
| vlm | vlm_152506 |  |
| map | ref_eq_map_20166 |  |
| vlm | vlm_147807 |  |
| map | ref_eq_map_18330 |  |
| vlm | vlm_152505 |  |
| vlm | vlm_147804 |  |
| vlm | vlm_147805 |  |
| map | ref_eq_map_18331 |  |
| vlm | vlm_152504 |  |
| vlm | vlm_147802 |  |
| vlm | vlm_147803 |  |
| vlm | vlm_147806 |  |
| vlm | vlm_147808 |  |
| vlm | vlm_147809 |  |
| vlm | vlm_147800 |  |
| vlm | vlm_147801 |  |
| vlm | vlm_147811 |  |
| vlm | vlm_147810 |  |
| vlm | vlm_147812 |  |
| vlm | vlm_147813 |  |


### Step 59: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_61 | Fe^[3+] |  |
| ligand | ligand_6277 | Ethylenedinitrilotetraacetic acid (EDTA) | SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O; HxL: H4L |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |
| beta_def | beta_def_966 |  | [M(OH)L] + [H] <=> [ML] + [H2O] |
| beta_def | beta_def_427 |  | [M(OH)L]^2 <=> [M2(OH)2L2] |
| beta_def | beta_def_788 |  | [ML] + [H] <=> [MHL] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_108639 |  |
| map | ref_eq_map_5028 |  |
| vlm | vlm_108640 |  |
| map | ref_eq_map_5029 |  |
| vlm | vlm_108647 |  |
| vlm | vlm_108646 |  |
| vlm | vlm_108650 |  |
| vlm | vlm_108643 |  |


### Step 60: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_62 | Fe^[2+] |  |
| ligand | ligand_6277 | Ethylenedinitrilotetraacetic acid (EDTA) | SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O; HxL: H4L |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |
| beta_def | beta_def_786 |  | [M] + [HL] <=> [MHL] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_108566 |  |
| map | ref_eq_map_5014 |  |
| vlm | vlm_108569 |  |


### Step 61: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_61 | Fe^[3+] |  |
| ligand | ligand_8191 | 1,10-Phenanthroline (Dipyridino[a,c]benzene) | SMILES: c1cnc2c(c1)ccc1cccnc12; HxL: L |
| beta_def | beta_def_872 |  | [M] + [L]^3 <=> [ML3] |
| beta_def | beta_def_840 |  | [M] + [L]^2 <=> [ML2] |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |
| beta_def | beta_def_587 |  | [M2(OH)L4] + [H] <=> [M2L4] + [H2O] |
| beta_def | beta_def_588 |  | [M2(OH)2L4] + [H] <=> [M2(OH)L4] + [H2O] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_139323 |  |
| map | ref_eq_map_15189 |  |
| vlm | vlm_139322 |  |
| map | ref_eq_map_15188 |  |
| vlm | vlm_139324 |  |
| map | ref_eq_map_15190 |  |
| vlm | vlm_139321 |  |
| vlm | vlm_139320 |  |
| vlm | vlm_139327 |  |
| vlm | vlm_139328 |  |


### Step 62: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_62 | Fe^[2+] |  |
| ligand | ligand_8191 | 1,10-Phenanthroline (Dipyridino[a,c]benzene) | SMILES: c1cnc2c(c1)ccc1cccnc12; HxL: L |
| beta_def | beta_def_872 |  | [M] + [L]^3 <=> [ML3] |
| beta_def | beta_def_840 |  | [M] + [L]^2 <=> [ML2] |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_139269 |  |
| map | ref_eq_map_15178 |  |
| vlm | vlm_139270 |  |
| map | ref_eq_map_15179 |  |
| vlm | vlm_139268 |  |
| vlm | vlm_139266 |  |
| vlm | vlm_139267 |  |


### Step 63: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_61 | Fe^[3+] |  |
| ligand | ligand_5937 | N-(Phosphonomethyl)glycine (Glyphosate) | SMILES: O=C(O)CNCP(=O)(O)O; HxL: H3L |
| beta_def | beta_def_840 |  | [M] + [L]^2 <=> [ML2] |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |
| beta_def | beta_def_238 |  | [M(OH)2L] + [H] <=> [M(OH)L] + [H2O] |
| beta_def | beta_def_966 |  | [M(OH)L] + [H] <=> [ML] + [H2O] |
| beta_def | beta_def_788 |  | [ML] + [H] <=> [MHL] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_99818 |  |
| map | ref_eq_map_1596 |  |
| vlm | vlm_99817 |  |
| vlm | vlm_99821 |  |
| vlm | vlm_99820 |  |
| vlm | vlm_99819 |  |


### Step 64: `search_ligands`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| ligand | ligand_5801 | Aminopropanedioic acid (Aminomalonic acid) | SMILES: NC(C(=O)O)C(=O)O; HxL: H2L |
| ligand | ligand_5808 | (3-Aminopropyl)malonic acid | SMILES: NCCCC(C(=O)O)C(=O)O; HxL: H2L |
| ligand | ligand_8873 | Propanedioic acid (Malonic acid) | SMILES: O=C(O)CC(=O)O; HxL: H2L |
| ligand | ligand_8874 | Ethane-1,1-dicarboxylic acid (Methylmalonic acid) | SMILES: CC(C(=O)O)C(=O)O; HxL: H2L |
| ligand | ligand_8875 | Propane-1,1-dicarboxylic acid (Ethylmalonic acid) | SMILES: CCC(C(=O)O)C(=O)O; HxL: H2L |
| ligand | ligand_8876 | Butane-1,1-dicarboxylic acid (Propylmalonic acid) | SMILES: CCCC(C(=O)O)C(=O)O; HxL: H2L |
| ligand | ligand_8877 | Pentane-1,1-dicarboxylic acid (Butylmalonic acid) | SMILES: CCCCC(C(=O)O)C(=O)O; HxL: H2L |
| ligand | ligand_8878 | Hexane-1,1-dicarboxylic acid (Pentylmalonic acid) | SMILES: CCCCCC(C(=O)O)C(=O)O; HxL: H2L |
| ligand | ligand_8879 | 2-Methylpropane-1,1-dicarboxylic acid (Isopropylmalonic acid) | SMILES: CC(C)C(C(=O)O)C(=O)O; HxL: H2L |
| ligand | ligand_8880 | 3-Methylbutane-1,1-dicarboxylic acid (Isobutylmalonic acid) | SMILES: CC(C)CC(C(=O)O)C(=O)O; HxL: H2L |
| ligand | ligand_8881 | 2,2-Dimethylpropane-1,1-dicarboxylic acid (t-Butylmalonic acid) | SMILES: CC(C)(C)C(C(=O)O)C(=O)O; HxL: H2L |
| ligand | ligand_8882 | But-3-ene-1,1-dicarboxylic acid (Allylmalonic acid) | SMILES: C=CCC(C(=O)O)C(=O)O; HxL: H2L |
| ligand | ligand_8885 | 2-Phenylethane-1,1-dicarboxylic acid (Benzylmalonic acid) | SMILES: O=C(O)C(Cc1ccccc1)C(=O)O; HxL: H2L |
| ligand | ligand_8886 | Phenylmethanedicarboxylic acid (Phenylmalonic acid) | SMILES: O=C(O)C(C(=O)O)c1ccccc1; HxL: H2L |
| ligand | ligand_8887 | Propane-2,2-dicarboxylic acid (Dimethylmalonic acid) | SMILES: CC(C)(C(=O)O)C(=O)O; HxL: H2L |
| ligand | ligand_8888 | Butane-2,2-dicarboxylic acid (Ethylmethylmalonic acid) | SMILES: CCC(C)(C(=O)O)C(=O)O; HxL: H2L |
| ligand | ligand_8889 | Pentane-3,3-dicarboxylic acid (Diethylmalonic acid) | SMILES: CCC(CC)(C(=O)O)C(=O)O; HxL: H2L |
| ligand | ligand_8890 | Hexane-3,3-dicarboxylic acid (Ethylpropylmalonic acid) | SMILES: CCCC(CC)(C(=O)O)C(=O)O; HxL: H2L |
| ligand | ligand_8891 | 2-Methylpentane-3,3-dicarboxylic acid (Ethyl-2-propylmalonic acid) | SMILES: CCC(C(=O)O)(C(=O)O)C(C)C; HxL: H2L |
| ligand | ligand_8892 | Heptane-3,3-dicarboxylic acid (Butylethylmalonic acid) | SMILES: CCCCC(CC)(C(=O)O)C(=O)O; HxL: H2L |
| ligand | ligand_8893 | Heptane-4,4-dicarboxylic acid (Dipropylmalonic acid) | SMILES: CCCC(CCC)(C(=O)O)C(=O)O; HxL: H2L |
| ligand | ligand_8894 | 4-Methylhexane-3,3-dicarboxylic acid (s-Butylethylmalonic acid) | SMILES: CCC(C)C(CC)(C(=O)O)C(=O)O; HxL: H2L |
| ligand | ligand_8895 | 2,4-Dimethylpentane-3,3-dicarboxylic acid (Di-2-propylmalonic acid) | SMILES: CC(C)C(C(=O)O)(C(=O)O)C(C)C; HxL: H2L |
| ligand | ligand_8896 | 6-Methylheptane-3,3-dicarboxylic acid (Ethylisopentylmalonic acid) | SMILES: CCC(CCC(C)C)(C(=O)O)C(=O)O; HxL: H2L |
| ligand | ligand_8897 | Nonane-5,5-dicarboxylic acid (Dibutylmalonic acid) | SMILES: CCCCC(CCCC)(C(=O)O)C(=O)O; HxL: H2L |


### Step 65: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_62 | Fe^[2+] |  |
| ligand | ligand_5937 | N-(Phosphonomethyl)glycine (Glyphosate) | SMILES: O=C(O)CNCP(=O)(O)O; HxL: H3L |
| beta_def | beta_def_840 |  | [M] + [L]^2 <=> [ML2] |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |
| beta_def | beta_def_788 |  | [ML] + [H] <=> [MHL] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_99791 |  |
| map | ref_eq_map_1591 |  |
| vlm | vlm_99790 |  |
| vlm | vlm_99792 |  |


### Step 66: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_61 | Fe^[3+] |  |
| ligand | ligand_8873 | Propanedioic acid (Malonic acid) | SMILES: O=C(O)CC(=O)O; HxL: H2L |
| beta_def | beta_def_872 |  | [M] + [L]^3 <=> [ML3] |
| beta_def | beta_def_840 |  | [M] + [L]^2 <=> [ML2] |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_152347 |  |
| map | ref_eq_map_20112 |  |
| vlm | vlm_152348 |  |
| map | ref_eq_map_20113 |  |
| vlm | vlm_152342 |  |
| map | ref_eq_map_20111 |  |
| vlm | vlm_152343 |  |
| vlm | vlm_152344 |  |
| vlm | vlm_152337 |  |
| vlm | vlm_152338 |  |
| vlm | vlm_152339 |  |


### Step 67: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_62 | Fe^[2+] |  |
| ligand | ligand_8873 | Propanedioic acid (Malonic acid) | SMILES: O=C(O)CC(=O)O; HxL: H2L |
| beta_def | beta_def_840 |  | [M] + [L]^2 <=> [ML2] |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_152298 |  |
| map | ref_eq_map_20097 |  |
| vlm | vlm_152297 |  |
| map | ref_eq_map_20098 |  |
| vlm | vlm_152296 |  |


### Step 68: `search_ligands`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| ligand | ligand_9358 | 1,2-Dihydroxybenzene-3,5-disulfonic acid (Tiron) | SMILES: O=S(=O)(O)c1cc(O)c(O)c(S(=O)(=O)O)c1; HxL: H4L |


### Step 69: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_61 | Fe^[3+] |  |
| ligand | ligand_5760 | Aminoacetic acid (Glycine) | SMILES: NCC(=O)O; HxL: HL |
| beta_def | beta_def_194 |  | [M] + [HL]^2 <=> [M(HL)2] |
| beta_def | beta_def_779 |  | [M] + [HL] <=> [MHL] |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_93885 |  |
| map | ref_eq_map_96 |  |
| vlm | vlm_93884 |  |
| vlm | vlm_93882 |  |
| map | ref_eq_map_97 |  |
| vlm | vlm_93883 |  |
| map | ref_eq_map_98 |  |
| vlm | vlm_93880 |  |
| vlm | vlm_93881 |  |


### Step 70: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_61 | Fe^[3+] |  |
| ligand | ligand_9358 | 1,2-Dihydroxybenzene-3,5-disulfonic acid (Tiron) | SMILES: O=S(=O)(O)c1cc(O)c(O)c(S(=O)(=O)O)c1; HxL: H4L |
| beta_def | beta_def_788 |  | [ML] + [H] <=> [MHL] |
| beta_def | beta_def_823 |  | [M] + [H2L] <=> [ML] + [H]^2 |
| beta_def | beta_def_853 |  | [ML] + [H2L] <=> [ML2] + [H]^2 |
| beta_def | beta_def_876 |  | [ML2] + [H2L] <=> [ML3] + [H]^2 |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_162100 |  |
| map | ref_eq_map_23841 |  |
| vlm | vlm_162101 |  |
| map | ref_eq_map_23842 |  |
| vlm | vlm_162103 |  |
| map | ref_eq_map_23844 |  |
| vlm | vlm_162102 |  |
| map | ref_eq_map_23843 |  |
| vlm | vlm_162089 |  |
| vlm | vlm_162088 |  |
| vlm | vlm_162090 |  |
| vlm | vlm_162091 |  |
| vlm | vlm_162095 |  |
| vlm | vlm_162094 |  |
| vlm | vlm_162093 |  |
| vlm | vlm_162092 |  |
| vlm | vlm_162099 |  |
| vlm | vlm_162098 |  |
| vlm | vlm_162097 |  |
| vlm | vlm_162096 |  |


### Step 71: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_61 | Fe^[3+] |  |
| ligand | ligand_6770 | Pyridine-2-phosphonic-6-carboxylic acid (2PP6C) | SMILES: O=C(O)c1cccc(P(=O)(O)O)n1; HxL: H3L |
| beta_def | beta_def_840 |  | [M] + [L]^2 <=> [ML2] |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |
| beta_def | beta_def_238 |  | [M(OH)2L] + [H] <=> [M(OH)L] + [H2O] |
| beta_def | beta_def_966 |  | [M(OH)L] + [H] <=> [ML] + [H2O] |
| beta_def | beta_def_792 |  | [ML2] + [H] <=> [MHL2] |
| metal | metal_62 | Fe^[2+] |  |
| beta_def | beta_def_204 |  | [MHL2] + [H] <=> [M(HL)2] |
| beta_def | beta_def_788 |  | [ML] + [H] <=> [MHL] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_119196 |  |
| map | ref_eq_map_8467 |  |
| vlm | vlm_119195 |  |
| vlm | vlm_119198 |  |
| vlm | vlm_119197 |  |
| vlm | vlm_119199 |  |
| vlm | vlm_119189 |  |
| map | ref_eq_map_8466 |  |
| vlm | vlm_119192 |  |
| vlm | vlm_119191 |  |
| vlm | vlm_119188 |  |
| vlm | vlm_119193 |  |
| vlm | vlm_119194 |  |
| vlm | vlm_119190 |  |


### Step 72: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_68 | H^[+] |  |
| ligand | ligand_9358 | 1,2-Dihydroxybenzene-3,5-disulfonic acid (Tiron) | SMILES: O=S(=O)(O)c1cc(O)c(O)c(S(=O)(=O)O)c1; HxL: H4L |
| beta_def | beta_def_32 |  | [HL] + [H] <=> [H2L] |
| ligand | ligand_9470 | 1,8-Dihydroxynaphthalene-3,6-disulfonic acid (Chromotropic acid) | SMILES: O=S(=O)(O)c1cc(O)c2c(O)cc(S(=O)(=O)O)cc2c1; HxL: H4L |
| metal | metal_108 | Nb^[5+] |  |
| beta_def | beta_def_891 |  | [MO2] + [H] + [HL]^3 <=> [ML3] + [H2O]^2 |
| metal | metal_187 | Ti^[3+] |  |
| beta_def | beta_def_874 |  | [MO] + [HL]^3 <=> [ML3] + [H] + [H2O] |
| metal | metal_185 | Th^[4+] |  |
| beta_def | beta_def_546 |  | [M2(OH)2L3] + [H]^2 <=> [M2L3] + [H2O]^2 |
| beta_def | beta_def_5 |  | [M2(OH)2L3] + [H]^4 <=> [ML]^2 + [H2L] + [H2O]^2 |
| beta_def | beta_def_79 |  | [L] + [H] <=> [HL] |
| ligand | ligand_9426 | 1-Naphthol-3,8-disulfonic acid | SMILES: O=S(=O)(O)c1cc(O)c2c(S(=O)(=O)O)cccc2c1; HxL: H3L |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_161963 |  |
| vlm | vlm_164207 |  |
| vlm | vlm_164249 |  |
| map | ref_eq_map_24759 |  |
| vlm | vlm_164242 |  |
| map | ref_eq_map_24756 |  |
| vlm | vlm_162043 |  |
| map | ref_eq_map_23823 |  |
| vlm | vlm_162042 |  |
| vlm | vlm_161953 |  |
| map | ref_eq_map_23787 |  |
| vlm | vlm_161954 |  |
| map | ref_eq_map_23788 |  |
| vlm | vlm_161955 |  |
| map | ref_eq_map_23789 |  |
| vlm | vlm_163235 |  |
| map | ref_eq_map_24212 |  |


### Step 73: `search_ligands`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| ligand | ligand_9337 | 1,2-Dihydroxybenzene (Catechol) | SMILES: Oc1ccccc1O; HxL: H2L |
| ligand | ligand_9340 | 1,2-Dihydroxy-4-methylbenzene (4-Methylcatechol) | SMILES: Cc1ccc(O)c(O)c1; HxL: H2L |
| ligand | ligand_9341 | 1,2-Dihydroxy-4-(2-methyl-2-propyl)benzene (4-t-Butylcatechol) | SMILES: CC(C)(C)c1ccc(O)c(O)c1; HxL: H2L |
| ligand | ligand_9344 | 4-Cyano-1,2-dihydroxybenzene (4-Cyanocatechol) | SMILES: N#Cc1ccc(O)c(O)c1; HxL: H2L |
| ligand | ligand_9346 | 4-Chloro-1,2-dihydroxybenzene (4-Chlorocatechol) | SMILES: Oc1ccc(Cl)cc1O; HxL: H2L |
| ligand | ligand_9347 | 4,5-Dichloro-1,2-dihydroxybenzene (4,5-Dichlorocatechol) | SMILES: Oc1cc(Cl)c(Cl)cc1O; HxL: H2L |
| ligand | ligand_9349 | Tetrachloro-1,2-dihydroxybenzene (Tetrachlorocatechol) | SMILES: Oc1c(O)c(Cl)c(Cl)c(Cl)c1Cl; HxL: H2L |
| ligand | ligand_9350 | 4-Bromo-1,2-dihydroxybenzene (4-Bromocatechol) | SMILES: Oc1ccc(Br)cc1O; HxL: H2L |
| ligand | ligand_9351 | 1,2-Dihydroxy-3-nitrobenzene (3-Nitrocatechol) | SMILES: O=[N+]([O-])c1cccc(O)c1O; HxL: H2L |
| ligand | ligand_9352 | 1,2-Dihydroxy-4-nitrobenzene (4-Nitrocatechol) | SMILES: O=[N+]([O-])c1ccc(O)c(O)c1; HxL: H2L |
| ligand | ligand_9353 | 1,2-Dihydroxy-3,4-dinitrobenzene (3,4-Dinitrocatechol) | SMILES: O=[N+]([O-])c1ccc(O)c(O)c1[N+](=O)[O-]; HxL: H2L |
| ligand | ligand_9354 | 1,2-Dihydroxy-3,5-Nitrobenzene (3,5-Dinitrocatechol) | SMILES: O=[N+]([O-])c1cc(O)c(O)c([N+](=O)[O-])c1; HxL: H2L |
| ligand | ligand_9357 | 1,2-Dihydroxybenzene-4-sulfonic acid (4-Sulfocatechol) | SMILES: O=S(=O)(O)c1ccc(O)c(O)c1; HxL: H3L |
| ligand | ligand_9396 | 3,3',4'-Trihydroxyfuchson-2''-sulfonic acid (Pyrocatechol Violet) | SMILES: O=C1C=C/C(=C(\c2ccc(O)c(O)c2)c2ccccc2S(=O)(=O)O)C=C1O; HxL: H4L |
| ligand | ligand_11044 | 1,2-Dihydroxy-3-methylbenzene (3-Methylcatechol) |  |
| ligand | ligand_11052 | 2,3-Dihydroxy-4'-nitroazobenzene (4-Nitrophenylazocatechol) |  |
| ligand | ligand_11087 | 4,4'-Bis(catecholazo)biphenyl |  |


### Step 74: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_61 | Fe^[3+] |  |
| ligand | ligand_9337 | 1,2-Dihydroxybenzene (Catechol) | SMILES: Oc1ccccc1O; HxL: H2L |
| beta_def | beta_def_823 |  | [M] + [H2L] <=> [ML] + [H]^2 |
| beta_def | beta_def_853 |  | [ML] + [H2L] <=> [ML2] + [H]^2 |
| beta_def | beta_def_876 |  | [ML2] + [H2L] <=> [ML3] + [H]^2 |
| metal | metal_62 | Fe^[2+] |  |
| beta_def | beta_def_497 |  | [M]^2 + [HL]^2 <=> [M2HL2] + [H] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_161602 |  |
| map | ref_eq_map_23636 |  |
| vlm | vlm_161601 |  |
| map | ref_eq_map_23635 |  |
| vlm | vlm_161605 |  |
| vlm | vlm_161606 |  |
| vlm | vlm_161570 |  |
| map | ref_eq_map_23622 |  |
| vlm | vlm_161567 |  |
| vlm | vlm_161568 |  |
| map | ref_eq_map_23623 |  |
| vlm | vlm_161569 |  |


### Step 75: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_61 | Fe^[3+] |  |
| ligand | ligand_9352 | 1,2-Dihydroxy-4-nitrobenzene (4-Nitrocatechol) | SMILES: O=[N+]([O-])c1ccc(O)c(O)c1; HxL: H2L |
| beta_def | beta_def_823 |  | [M] + [H2L] <=> [ML] + [H]^2 |
| beta_def | beta_def_853 |  | [ML] + [H2L] <=> [ML2] + [H]^2 |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_161832 |  |
| map | ref_eq_map_23725 |  |
| vlm | vlm_161833 |  |


### Step 76: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_5 | Al^[3+] |  |
| ligand | ligand_9283 | 2-Hydroxy-3,5-dinitrobenzoic acid (3,5-Dinitrosalicylic acid) | SMILES: O=C(O)c1cc([N+](=O)[O-])cc([N+](=O)[O-])c1O; HxL: H2L |
| beta_def | beta_def_821 |  | [M] + [HL] <=> [ML] + [H] |
| beta_def | beta_def_846 |  | [ML] + [HL] <=> [ML2] + [H] |
| beta_def | beta_def_873 |  | [ML2] + [HL] <=> [ML3] + [H] |
| ligand | ligand_9352 | 1,2-Dihydroxy-4-nitrobenzene (4-Nitrocatechol) | SMILES: O=[N+]([O-])c1ccc(O)c(O)c1; HxL: H2L |
| beta_def | beta_def_823 |  | [M] + [H2L] <=> [ML] + [H]^2 |
| beta_def | beta_def_853 |  | [ML] + [H2L] <=> [ML2] + [H]^2 |
| beta_def | beta_def_876 |  | [ML2] + [H2L] <=> [ML3] + [H]^2 |
| metal | metal_10 | As^[3+] |  |
| beta_def | beta_def_245 |  | [M(OH)4] + [H2L] <=> [M(OH)2L] + [H2O]^2 |
| metal | metal_15 | B^[3+] |  |
| metal | metal_18 | Ba^[2+] |  |
| metal | metal_19 | Be^[2+] |  |
| ligand | ligand_9354 | 1,2-Dihydroxy-3,5-Nitrobenzene (3,5-Dinitrocatechol) | SMILES: O=[N+]([O-])c1cc(O)c(O)c([N+](=O)[O-])c1; HxL: H2L |
| metal | metal_25 | Ca^[2+] |  |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_160782 |  |
| map | ref_eq_map_23267 |  |
| vlm | vlm_160784 |  |
| vlm | vlm_160783 |  |
| map | ref_eq_map_23268 |  |
| vlm | vlm_160785 |  |
| vlm | vlm_161845 |  |
| map | ref_eq_map_23734 |  |
| vlm | vlm_161846 |  |
| vlm | vlm_161847 |  |
| vlm | vlm_161850 |  |
| map | ref_eq_map_23737 |  |
| vlm | vlm_161841 |  |
| map | ref_eq_map_23730 |  |
| vlm | vlm_161840 |  |
| map | ref_eq_map_23729 |  |
| vlm | vlm_161806 |  |
| map | ref_eq_map_23715 |  |
| vlm | vlm_161807 |  |
| vlm | vlm_160764 |  |
| map | ref_eq_map_23256 |  |
| vlm | vlm_160765 |  |
| vlm | vlm_161872 |  |
| map | ref_eq_map_23741 |  |
| vlm | vlm_161873 |  |
| vlm | vlm_161798 |  |
| map | ref_eq_map_23711 |  |
| vlm | vlm_161799 |  |
| vlm | vlm_161877 |  |
| map | ref_eq_map_23743 |  |
| vlm | vlm_161878 |  |


### Step 77: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_61 | Fe^[3+] |  |
| ligand | ligand_9351 | 1,2-Dihydroxy-3-nitrobenzene (3-Nitrocatechol) | SMILES: O=[N+]([O-])c1cccc(O)c1O; HxL: H2L |
| beta_def | beta_def_823 |  | [M] + [H2L] <=> [ML] + [H]^2 |
| beta_def | beta_def_853 |  | [ML] + [H2L] <=> [ML2] + [H]^2 |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_161777 |  |
| map | ref_eq_map_23703 |  |
| vlm | vlm_161778 |  |


### Step 78: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_61 | Fe^[3+] |  |
| ligand | ligand_8434 | Pyridine-2,6-diphosphonic acid (2,6-PDPA) | SMILES: O=P(O)(O)c1cccc(P(=O)(O)O)n1; HxL: H4L |
| beta_def | beta_def_840 |  | [M] + [L]^2 <=> [ML2] |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |
| beta_def | beta_def_238 |  | [M(OH)2L] + [H] <=> [M(OH)L] + [H2O] |
| beta_def | beta_def_966 |  | [M(OH)L] + [H] <=> [ML] + [H2O] |
| beta_def | beta_def_788 |  | [ML] + [H] <=> [MHL] |
| beta_def | beta_def_792 |  | [ML2] + [H] <=> [MHL2] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_143993 |  |
| map | ref_eq_map_16775 |  |
| vlm | vlm_143992 |  |
| vlm | vlm_143996 |  |
| vlm | vlm_143995 |  |
| vlm | vlm_143994 |  |
| vlm | vlm_143997 |  |


### Step 79: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_62 | Fe^[2+] |  |
| ligand | ligand_8434 | Pyridine-2,6-diphosphonic acid (2,6-PDPA) | SMILES: O=P(O)(O)c1cccc(P(=O)(O)O)n1; HxL: H4L |
| beta_def | beta_def_840 |  | [M] + [L]^2 <=> [ML2] |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |
| beta_def | beta_def_966 |  | [M(OH)L] + [H] <=> [ML] + [H2O] |
| beta_def | beta_def_792 |  | [ML2] + [H] <=> [MHL2] |
| beta_def | beta_def_204 |  | [MHL2] + [H] <=> [M(HL)2] |
| beta_def | beta_def_788 |  | [ML] + [H] <=> [MHL] |
| beta_def | beta_def_756 |  | [M(HL)2] + [H] <=> [MH3L2] |
| beta_def | beta_def_171 |  | [MH3L2] + [H] <=> [M(H2L)2] |
| beta_def | beta_def_739 |  | [MHL] + [H] <=> [MH2L] |
| beta_def | beta_def_238 |  | [M(OH)2L] + [H] <=> [M(OH)L] + [H2O] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_143983 |  |
| map | ref_eq_map_16774 |  |
| vlm | vlm_143982 |  |
| vlm | vlm_143986 |  |
| vlm | vlm_143988 |  |
| vlm | vlm_143989 |  |
| vlm | vlm_143984 |  |
| vlm | vlm_143990 |  |
| vlm | vlm_143991 |  |
| vlm | vlm_143985 |  |
| vlm | vlm_143987 |  |


### Step 80: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_61 | Fe^[3+] |  |
| ligand | ligand_10076 | Hydroxide ion |  |
| beta_def | beta_def_649 |  | [M]^3 + [L]^4 <=> [M3L4] |
| beta_def | beta_def_894 |  | [M] + [L]^4 <=> [ML4] |
| beta_def | beta_def_519 |  | [M]^2 + [L]^2 <=> [M2L2] |
| beta_def | beta_def_840 |  | [M] + [L]^2 <=> [ML2] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_170820 |  |
| map | ref_eq_map_27396 |  |
| vlm | vlm_170819 |  |
| map | ref_eq_map_27391 |  |
| vlm | vlm_170821 |  |
| map | ref_eq_map_27390 |  |
| vlm | vlm_170808 |  |
| vlm | vlm_170813 |  |
| vlm | vlm_170812 |  |
| vlm | vlm_170814 |  |
| vlm | vlm_170811 |  |
| map | ref_eq_map_27394 |  |
| vlm | vlm_170810 |  |
| map | ref_eq_map_27393 |  |
| vlm | vlm_170809 |  |
| map | ref_eq_map_27392 |  |
| vlm | vlm_170807 |  |
| vlm | vlm_170806 |  |
| vlm | vlm_170805 |  |
| vlm | vlm_170802 |  |
| vlm | vlm_170804 |  |


### Step 81: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_61 | Fe^[3+] |  |
| ligand | ligand_10076 | Hydroxide ion |  |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_170797 |  |
| map | ref_eq_map_27397 |  |
| vlm | vlm_170791 |  |
| map | ref_eq_map_27390 |  |
| vlm | vlm_170796 |  |
| map | ref_eq_map_27391 |  |
| vlm | vlm_170795 |  |
| map | ref_eq_map_27394 |  |
| vlm | vlm_170792 |  |
| map | ref_eq_map_27392 |  |
| vlm | vlm_170793 |  |
| map | ref_eq_map_27395 |  |
| vlm | vlm_170794 |  |
| map | ref_eq_map_27393 |  |


### Step 82: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_61 | Fe^[3+] |  |
| ligand | ligand_7295 | Nitrilotriacetohydroxamic acid | SMILES: O=C(CN(CC(=O)NO)CC(=O)NO)NO; HxL: H3L |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |
| beta_def | beta_def_741 |  | [ML] + [H]^2 <=> [MH2L] |
| beta_def | beta_def_966 |  | [M(OH)L] + [H] <=> [ML] + [H2O] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_127357 |  |
| map | ref_eq_map_10986 |  |
| vlm | vlm_127359 |  |
| vlm | vlm_127358 |  |


### Step 83: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_61 | Fe^[3+] |  |
| ligand | ligand_9894 | Trimethylenedihydroxamic acid (Glutarodihydroxamic acid) | SMILES: O=C(CCCC(=O)NO)NO; HxL: H2L |
| beta_def | beta_def_408 |  | [M]^2 + [HL]^2 + [L]^2 <=> [M2(HL)2L2] |
| beta_def | beta_def_583 |  | [M]^2 + [OH] + [L]^2 <=> [M2(OH)L2] |
| ligand | ligand_7154 | Iminodiacetohydroxamic acid | SMILES: O=C(CNCC(=O)NO)NO; HxL: H2L |
| beta_def | beta_def_540 |  | [M]^2 + [L]^3 <=> [M2L3] |
| ligand | ligand_6982 | Aminoacetohydroxamic acid (Glycinehydroxamic acid) | SMILES: NCC(=O)NO; HxL: HL |
| beta_def | beta_def_872 |  | [M] + [L]^3 <=> [ML3] |
| metal | metal_41 | Cu^[2+] |  |
| ligand | ligand_7320 | Ethylenedinitrilotetraacetohydroxamic acid | SMILES: O=C(CN(CCN(CC(=O)NO)CC(=O)NO)CC(=O)NO)NO; HxL: H4L |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |
| ligand | ligand_6020 | N-(Carboxymethyl)-N-(2-hydroxyethyl)aminoacetohydroxamic acid | SMILES: O=C(O)CN(CCO)CC(=O)NO; HxL: H2L |
| beta_def | beta_def_247 |  | [ML] + [OH]^2 <=> [M(OH)2L] |
| ligand | ligand_6036 | N,N'-Bis(carboxymethyl)ethylenedinitrilo-N,N'-diacetohydroxamic acid | SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)NO)CC(=O)NO; HxL: H4L |
| beta_def | beta_def_840 |  | [M] + [L]^2 <=> [ML2] |
| metal | metal_112 | Ni^[2+] |  |
| ligand | ligand_7295 | Nitrilotriacetohydroxamic acid | SMILES: O=C(CN(CC(=O)NO)CC(=O)NO)NO; HxL: H3L |
| beta_def | beta_def_581 |  | [M]^2 + [L]^2 + [H2O] <=> [M2(OH)L2] + [H] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_168650 |  |
| map | ref_eq_map_26606 |  |
| vlm | vlm_168649 |  |
| vlm | vlm_124725 |  |
| map | ref_eq_map_10255 |  |
| vlm | vlm_121461 |  |
| map | ref_eq_map_9344 |  |
| vlm | vlm_127783 |  |
| map | ref_eq_map_11152 |  |
| vlm | vlm_127787 |  |
| map | ref_eq_map_11153 |  |
| vlm | vlm_101541 |  |
| map | ref_eq_map_2242 |  |
| vlm | vlm_101953 |  |
| map | ref_eq_map_2399 |  |
| vlm | vlm_121460 |  |
| vlm | vlm_127352 |  |
| map | ref_eq_map_10984 |  |


### Step 84: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_2 | Ag^[+] |  |
| ligand | ligand_9034 | As-Phenylarsinodiacetic acid [Bis(carboxymethyl)phenylarsine] | SMILES: O=C(O)C[As](CC(=O)O)c1ccccc1; HxL: H2L |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |
| beta_def | beta_def_779 |  | [M] + [HL] <=> [MHL] |
| beta_def | beta_def_732 |  | [M] + [H2L] <=> [MH2L] |
| ligand | ligand_9019 | Benzene-1,2-bis(thioacetic acid) | SMILES: O=C(O)CSc1ccccc1SCC(=O)O; HxL: H2L |
| ligand | ligand_6731 | N-Phenyliminodiacetic acid | SMILES: O=C(O)CN(CC(=O)O)c1ccccc1; HxL: H2L |
| metal | metal_18 | Ba^[2+] |  |
| ligand | ligand_8985 | Benzene-1,2-bis(oxyacetic acid) | SMILES: O=C(O)COc1ccccc1OCC(=O)O; HxL: H2L |
| metal | metal_25 | Ca^[2+] |  |
| metal | metal_26 | Cd^[2+] |  |
| ligand | ligand_6723 | N-Phenylglycine | SMILES: O=C(O)CNc1ccccc1; HxL: HL |
| ligand | ligand_8521 | Phenylacetic acid | SMILES: O=C(O)Cc1ccccc1; HxL: HL |
| beta_def | beta_def_840 |  | [M] + [L]^2 <=> [ML2] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_157010 |  |
| map | ref_eq_map_21856 |  |
| vlm | vlm_157011 |  |
| vlm | vlm_157012 |  |
| vlm | vlm_156822 |  |
| map | ref_eq_map_21769 |  |
| vlm | vlm_117830 |  |
| map | ref_eq_map_8043 |  |
| vlm | vlm_155799 |  |
| map | ref_eq_map_21429 |  |
| vlm | vlm_117814 |  |
| vlm | vlm_117813 |  |
| vlm | vlm_155797 |  |
| map | ref_eq_map_21427 |  |
| vlm | vlm_117812 |  |
| map | ref_eq_map_8036 |  |
| vlm | vlm_155868 |  |
| map | ref_eq_map_21451 |  |
| vlm | vlm_117834 |  |
| map | ref_eq_map_8045 |  |
| vlm | vlm_117726 |  |
| map | ref_eq_map_8000 |  |
| vlm | vlm_146074 |  |
| map | ref_eq_map_17657 |  |
| vlm | vlm_146073 |  |


### Step 85: `search_ligands`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| ligand | ligand_8872 | Ethanedioic acid (Oxalic acid) | SMILES: O=C(O)C(=O)O; HxL: H2L |
| ligand | ligand_8960 | Oxopropanedioic acid (Ketomalonic acid) (Mesoxalic acid) | SMILES: O=C(O)C(=O)C(=O)O; HxL: H2L |
| ligand | ligand_9763 | Dithiooxalic acid | SMILES: O=C(S)C(=O)S; HxL: H2L |
| ligand | ligand_11304 | Ethanedi(dithioic acid) (Tetrathiooxalic acid) |  |


### Step 86: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_61 | Fe^[3+] |  |
| ligand | ligand_8872 | Ethanedioic acid (Oxalic acid) | SMILES: O=C(O)C(=O)O; HxL: H2L |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_151795 |  |
| map | ref_eq_map_19978 |  |
| vlm | vlm_151794 |  |
| map | ref_eq_map_19976 |  |
| vlm | vlm_151793 |  |
| map | ref_eq_map_19977 |  |


### Step 87: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_62 | Fe^[2+] |  |
| ligand | ligand_8872 | Ethanedioic acid (Oxalic acid) | SMILES: O=C(O)C(=O)O; HxL: H2L |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_151749 |  |
| map | ref_eq_map_19964 |  |


### Step 88: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_61 | Fe^[3+] |  |
| ligand | ligand_8872 | Ethanedioic acid (Oxalic acid) | SMILES: O=C(O)C(=O)O; HxL: H2L |
| beta_def | beta_def_872 |  | [M] + [L]^3 <=> [ML3] |
| beta_def | beta_def_840 |  | [M] + [L]^2 <=> [ML2] |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_151801 |  |
| map | ref_eq_map_19976 |  |
| vlm | vlm_151798 |  |
| vlm | vlm_151795 |  |
| map | ref_eq_map_19978 |  |
| vlm | vlm_151794 |  |
| vlm | vlm_151793 |  |
| map | ref_eq_map_19977 |  |


### Step 89: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_62 | Fe^[2+] |  |
| ligand | ligand_8872 | Ethanedioic acid (Oxalic acid) | SMILES: O=C(O)C(=O)O; HxL: H2L |
| beta_def | beta_def_840 |  | [M] + [L]^2 <=> [ML2] |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_151750 |  |
| map | ref_eq_map_19964 |  |
| vlm | vlm_151749 |  |


### Step 90: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_195 | UO_[2]^[2+] |  |
| ligand | ligand_10096 | Hydrogen carbonate (Carbonic acid) | SMILES: O=C(O)O; HxL: H2L |
| beta_def | beta_def_653 |  | [M]^3 + [L]^6 <=> [M3L6] |
| metal | metal_193 | U^[4+] |  |
| beta_def | beta_def_903 |  | [M] + [L]^5 <=> [ML5] |
| metal | metal_61 | Fe^[3+] |  |
| ligand | ligand_8465 | Ethanoic acid (Acetic acid) | SMILES: CC(=O)O; HxL: HL |
| beta_def | beta_def_597 |  | [M]^3 + [L]^6 + [H2O]^2 <=> [M3(OH)2L6] + [H]^2 |
| metal | metal_185 | Th^[4+] |  |
| ligand | ligand_8873 | Propanedioic acid (Malonic acid) | SMILES: O=C(O)CC(=O)O; HxL: H2L |
| beta_def | beta_def_872 |  | [M] + [L]^3 <=> [ML3] |
| metal | metal_169 | Sc^[3+] |  |
| ligand | ligand_8872 | Ethanedioic acid (Oxalic acid) | SMILES: O=C(O)C(=O)O; HxL: H2L |
| beta_def | beta_def_894 |  | [M] + [L]^4 <=> [ML4] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_172827 |  |
| vlm | vlm_172826 |  |
| vlm | vlm_172789 |  |
| vlm | vlm_144796 |  |
| vlm | vlm_152275 |  |
| vlm | vlm_152035 |  |
| vlm | vlm_151803 |  |
| vlm | vlm_152350 |  |
| vlm | vlm_144672 |  |
| vlm | vlm_144669 |  |


### Step 91: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_61 | Fe^[3+] |  |
| ligand | ligand_7320 | Ethylenedinitrilotetraacetohydroxamic acid | SMILES: O=C(CN(CCN(CC(=O)NO)CC(=O)NO)CC(=O)NO)NO; HxL: H4L |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |
| beta_def | beta_def_754 |  | [MHL] + [H]^2 <=> [MH3L] |
| beta_def | beta_def_788 |  | [ML] + [H] <=> [MHL] |
| beta_def | beta_def_981 |  | [ML] + [OH] <=> [M(OH)L] |
| beta_def | beta_def_765 |  | [MH3L] + [H] <=> [MH4L] |
| beta_def | beta_def_248 |  | [M(OH)L] + [OH] <=> [M(OH)2L] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_127787 |  |
| map | ref_eq_map_11153 |  |
| vlm | vlm_127789 |  |
| vlm | vlm_127788 |  |
| vlm | vlm_127791 |  |
| vlm | vlm_127790 |  |
| vlm | vlm_127792 |  |


### Step 92: `search_ligands`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| ligand | ligand_5938 | (Carboxymethylamino)acetohydroxamic acid | SMILES: O=C(O)CNCC(=O)NO; HxL: H2L |
| ligand | ligand_6020 | N-(Carboxymethyl)-N-(2-hydroxyethyl)aminoacetohydroxamic acid | SMILES: O=C(O)CN(CCO)CC(=O)NO; HxL: H2L |
| ligand | ligand_6036 | N,N'-Bis(carboxymethyl)ethylenedinitrilo-N,N'-diacetohydroxamic acid | SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)NO)CC(=O)NO; HxL: H4L |
| ligand | ligand_6054 | N,N'-Bis(carboxymethyl)ethylenedinitrilobis(N-2-propylacetohydroxamic acid) | SMILES: CC(C)N(O)C(=O)CN(CCN(CC(=O)O)CC(=O)N(O)C(C)C)CC(=O)O; HxL: H4L |
| ligand | ligand_6057 | N,N',N''-Tris(carboxymethyl)diethylenetrinitrilobis(N-2-propylacetohydroxamic acid) | SMILES: CC(C)N(O)C(=O)CN(CCN(CCN(CC(=O)O)CC(=O)N(O)C(C)C)CC(=O)O)CC(=O)O; HxL: H5L |
| ligand | ligand_6203 | N,N-Bis(carboxymethyl)aminoacetohydroxamic acid | SMILES: O=C(O)CN(CC(=O)O)CC(=O)NO; HxL: H3L |
| ligand | ligand_6982 | Aminoacetohydroxamic acid (Glycinehydroxamic acid) | SMILES: NCC(=O)NO; HxL: HL |
| ligand | ligand_6992 | Methylaminoacetohydroxamic acid (Sarcosinehydroxamic acid) | SMILES: CNCC(=O)NO; HxL: HL |
| ligand | ligand_7154 | Iminodiacetohydroxamic acid | SMILES: O=C(CNCC(=O)NO)NO; HxL: H2L |
| ligand | ligand_7282 | N,N-Bis(2-hydroxyethyl)aminoacetohydroxamic acid | SMILES: O=C(CCN(CCO)CCO)NO; HxL: HL |
| ligand | ligand_7295 | Nitrilotriacetohydroxamic acid | SMILES: O=C(CN(CC(=O)NO)CC(=O)NO)NO; HxL: H3L |
| ligand | ligand_7320 | Ethylenedinitrilotetraacetohydroxamic acid | SMILES: O=C(CN(CCN(CC(=O)NO)CC(=O)NO)CC(=O)NO)NO; HxL: H4L |
| ligand | ligand_7391 | Piperazine-N,N'-diacetohydroxamic acid | SMILES: O=C(CN1CCN(C(=O)NO)CC1)NO; HxL: H2L |
| ligand | ligand_7709 | 5,7-Dioxo-1,4,8,11-tetraazacyclotetradecane-4,8-bis(N-methylacetohydroxamic acid) | SMILES: CN(O)C(=O)CN1CCNCCCNCCN(CC(=O)N(C)O)C(=O)CC1=O; HxL: H2L |
| ligand | ligand_9873 | Acetohydroxamic acid | SMILES: CC(=O)NO; HxL: HL |
| ligand | ligand_9875 | N-Methylacetohydroxamic acid | SMILES: CC(=O)N(C)O; HxL: HL |
| ligand | ligand_9876 | N-Phenylacetohydroxamic acid | SMILES: CC(=O)N(O)c1ccccc1; HxL: HL |
| ligand | ligand_9877 | N-(4-Methylphenyl)acetohydroxamic acid | SMILES: CC(=O)N(O)c1ccc(C)cc1; HxL: HL |
| ligand | ligand_9878 | N-(3-Cyanophenyl)acetohydroxamic acid | SMILES: CC(=O)N(O)c1cccc(C#N)c1; HxL: HL |
| ligand | ligand_9879 | N-(4-Cyanophenyl)acetohydroxamic acid | SMILES: CC(=O)N(O)c1ccc(C#N)cc1; HxL: HL |
| ligand | ligand_9880 | N-(4-Chlorophenyl)acetohydroxamic acid | SMILES: CC(=O)N(O)c1ccc(Cl)cc1; HxL: HL |
| ligand | ligand_9881 | N-(3-Iodophenyl)acetohydroxamic acid | SMILES: CC(=O)N(O)c1cccc(I)c1; HxL: HL |
| ligand | ligand_9882 | N-(4-Iodophenyl)acetohydroxamic acid | SMILES: CC(=O)N(O)c1ccc(I)cc1; HxL: HL |
| ligand | ligand_9883 | N-(3-Acetylphenyl)acetohydroxamic acid | SMILES: CC(=O)c1cccc(N(O)C(C)=O)c1; HxL: HL |
| ligand | ligand_11339 | Phenylacetohydroxamic acid |  |


### Step 93: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_61 | Fe^[3+] |  |
| ligand | ligand_9873 | Acetohydroxamic acid | SMILES: CC(=O)NO; HxL: HL |
| beta_def | beta_def_872 |  | [M] + [L]^3 <=> [ML3] |
| beta_def | beta_def_840 |  | [M] + [L]^2 <=> [ML2] |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_168455 |  |
| map | ref_eq_map_26541 |  |
| vlm | vlm_168456 |  |
| map | ref_eq_map_26542 |  |
| vlm | vlm_168453 |  |
| vlm | vlm_168454 |  |
| vlm | vlm_168448 |  |
| map | ref_eq_map_26543 |  |
| vlm | vlm_168447 |  |
| vlm | vlm_168449 |  |
| map | ref_eq_map_26544 |  |
| vlm | vlm_168450 |  |


### Step 94: `search_stability`

### Referenced entity IDs
| type | prefixed_id | name | detail |
|------|-------------|------|--------|
| metal | metal_62 | Fe^[2+] |  |
| ligand | ligand_9873 | Acetohydroxamic acid | SMILES: CC(=O)NO; HxL: HL |
| beta_def | beta_def_840 |  | [M] + [L]^2 <=> [ML2] |
| beta_def | beta_def_812 |  | [M] + [L] <=> [ML] |

| type | prefixed_id | label |
|------|-------------|-------|
| vlm | vlm_168433 |  |
| map | ref_eq_map_26534 |  |
| vlm | vlm_168432 |  |

