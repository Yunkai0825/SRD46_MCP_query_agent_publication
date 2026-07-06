# Q3.1.5 — Tool Results (batch 1)

### Step 2: `search_metals`
**Args:**
```json
{
  "symbol": "Ca",
  "limit": 5
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
  "symbol": "Cu",
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

### Step 4: `search_ligands`
**Args:**
```json
{
  "name": "phosphate",
  "limit": 12
}
```

[summary]
## search_ligands — 12 result(s)

**stats:** 128 SQL matches · showing 12 · limit 12

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

### Step 5: `search_ligands`
**Args:**
```json
{
  "name": "pyrophosphate",
  "limit": 12
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
  "name": "tripolyphosphate",
  "limit": 12
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 7: `search_ligands`
**Args:**
```json
{
  "name": "carbonate",
  "limit": 12
}
```

[summary]
## search_ligands — 4 result(s)

**stats:** 4 SQL matches · showing 4 · limit 12

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

### Step 8: `search_ligands`
**Args:**
```json
{
  "name": "sulfate",
  "limit": 12
}
```

[summary]
## search_ligands — 11 result(s)

**stats:** 11 SQL matches · showing 11 · limit 12

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6852 | 2-Aminoethyl(hydrogensulfate) | HL | Aliphatic amines | 5 | `NCCOS(=O)(=O)O` | (-inf, HL, 9.182, L, +inf) |
| ligand_9382 | 2,3,4-Trihydroxybenzenesulfon… (Pyrogallolsulfate) | H4L | Catechols | 4 | `O=S(=O)(O)c1ccc(O)c(O)c1O` | (-inf, H3L, 8.28, H2L, 11.3, HL, +inf) |
| ligand_10148 | Hydrogen sulfate ion (Sulfuric acid) | HL | Inorganic ligands | 581 | `O=S(=O)([O-])O` | (-inf, HL, 1.54, L, +inf) |
| ligand_10149 | Hydrogen thiosulfate (Thiosulfuric acid) | H2L | Inorganic ligands | 117 | `O=S(O)(O)=S` | (-inf, H2L, -0.6, HL, -0.6, L, +inf) |
| ligand_10150 | Selenosulfate ion | *** | Inorganic ligands | 1 | *** | *** |
| ligand_10151 | Hydrogen amidosulfate (Sulfamic acid) | HL | Inorganic ligands | 22 | `NS(=O)(=O)O` | (-inf, HL, 0.034, L, +inf) |
| ligand_10152 | Hydrogen hydroxyl… (Hydroxylamine-O-sulfonic acid) | HL | Inorganic ligands | 1 | `NOS(=O)(=O)O` | (-inf, HL, 1.48, L, +inf) |
| ligand_10153 | Hydrogen amidodisulfate (Aminodisulfonic acid) | H2L | Inorganic ligands | 1 | `O=S(=O)(O)NS(=O)(=O)O` | (-inf, HL, 8.5, L, +inf) |
| ligand_10154 | Hydrogen peroxosulfate | H2L | Inorganic ligands | 1 | `O=S(=O)(O)OO` | (-inf, HL, 9.86, L, +inf) |
| ligand_10155 | Hydrogen peroxydisulfate (Peroxydisulfuric acid) | H2L | Inorganic ligands | 27 | `O=S(=O)(O)OOS(=O)(=O)O` | *** |
| ligand_11517 | Hydrogen imidobis(fluorosulfate) | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (9 parseable SMILES)

| group | count | % |
|-------|-------|---|
| hydroxyl | 9 | 100% |
| sulfonate | 8 | 89% |
| primary_amine | 3 | 33% |
| aromatic_ring | 1 | 11% |
| phenol | 1 | 11% |
| secondary_amine | 1 | 11% |

---

### Step 9: `search_ligands`
**Args:**
```json
{
  "name": "oxalate",
  "limit": 12
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
  "name": "citrate",
  "limit": 12
}
```

[summary]
## search_ligands — 4 result(s)

**stats:** 4 SQL matches · showing 4 · limit 12

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

### Step 11: `search_ligands`
**Args:**
```json
{
  "name": "tartrate",
  "limit": 12
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
  "name": "gluconate",
  "limit": 12
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
  "name": "lactate",
  "limit": 12
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 14: `search_ligands`
**Args:**
```json
{
  "name": "18-crown-6",
  "limit": 12
}
```

[summary]
## search_ligands — 8 result(s)

**stats:** 8 SQL matches · showing 8 · limit 12

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_9676 | 1,4,7,10,13,16-Hexaoxacyclooctadecane (18-Crown-6) | *** | miscellaneous crown ether | 76 | *** | *** |
| ligand_9677 | cis-syn-cis-2,5,8,15,… (A-Dicyclohexyl-18-Crown-6) | *** | miscellaneous crown ether | 42 | *** | *** |
| ligand_9678 | cis-anti-cis-2,5,8,15… (B-Dicyclohexyl-18-Crown-6) | *** | miscellaneous crown ether | 39 | *** | *** |
| ligand_9679 | Benzo-1,4,7,10,13,16-hexaoxacy… (Benzo-18-crown-6) | *** | miscellaneous crown ether | 2 | *** | *** |
| ligand_9680 | 2,3,11,12-Dibenzo-1,4,7,10,1… (Dibenzo-18-crown-6) | *** | miscellaneous crown ether | 13 | *** | *** |
| ligand_9681 | 3'-Hydroxymethy… (3-Hydroxymethylbenzo-18-crown-6) | *** | miscellaneous crown ether | 3 | *** | *** |
| ligand_11253 | Cyclohexyl-18-crown-6 | *** | Ligands not selected | 0 | *** | *** |
| ligand_11254 | Bis(t-butylcyclohexyl)-18-crown-6 | *** | Ligands not selected | 0 | *** | *** |

---

### Step 15: `search_ligands`
**Args:**
```json
{
  "name": "Kryptofix 222",
  "limit": 12
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 12

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_7601 | 4,7,13,16,21,24-Hexaoxa-1,10-di… ([2.2.2]cryptand) | L | Aza-oxa-macrocycles | 73 | `C1COCCN2CCOCCOCCN(CCO1)CCOCCOCC2` | (-inf, H2L, 7.31, HL, 9.68, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| ether | 1 | 100% |
| tertiary_amine | 1 | 100% |

---

### Step 16: `search_ligands`
**Args:**
```json
{
  "name": "HEDP",
  "limit": 12
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 12

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_9142 | 1-Hydroxyethane-1,1-diphosphonic… (Etidronic acid) | H4L | Organophosphorus and ars… | 189 | `CC(O)(P(=O)(O)O)P(=O)(O)O` | (-inf, H4L, -1.8, H3L, -1.8, H2L, 6.69, HL, 6.69, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| hydroxyl | 1 | 100% |
| phosphonate | 1 | 100% |

---

### Step 17: `search_ligands`
**Args:**
```json
{
  "name": "etidronic acid",
  "limit": 12
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 12

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_9142 | 1-Hydroxyethane-1,1-diphosphonic… (Etidronic acid) | H4L | Organophosphorus and ars… | 189 | `CC(O)(P(=O)(O)O)P(=O)(O)O` | (-inf, H4L, -1.8, H3L, -1.8, H2L, 6.69, HL, 6.69, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| hydroxyl | 1 | 100% |
| phosphonate | 1 | 100% |

---

### Step 18: `search_ligands`
**Args:**
```json
{
  "name": "phosphoric acid",
  "limit": 12
}
```

[summary]
## search_ligands — 12 result(s)

**stats:** 43 SQL matches · showing 12 · limit 12

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

### Step 19: `search_ligands`
**Args:**
```json
{
  "name": "hydrogen phosphate",
  "limit": 12
}
```

[summary]
## search_ligands — 2 result(s)

**stats:** 2 SQL matches · showing 2 · limit 12

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

### Step 20: `search_ligands`
**Args:**
```json
{
  "name": "dihydrogen phosphate",
  "limit": 12
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 12

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

### Step 21: `search_ligands`
**Args:**
```json
{
  "name": "diphosphate",
  "limit": 12
}
```

[summary]
## search_ligands — 12 result(s)

**stats:** 21 SQL matches · showing 12 · limit 12

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8235 | Cytidine-5'-(trihydrogendiphosphate) (CDP) | H3L | Pyrimidines | 29 | `Nc1ccn([C@@H]2O[C@H](COP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]2O)c(=O)n1` | (-inf, H3L, -1, H2L, 4.46, HL, 4.46, L, +inf) |
| ligand_8243 | Uridine-5'-(trihydrogendiphosphate) (UDP) | H3L | Pyrimidines | 24 | `O=c1ccn([C@@H]2O[C@H](COP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]2O)c(=O)[nH]1` | (-inf, H2L, -1.3, HL, -1.3, L, 9.47, H-1L, +inf) |
| ligand_8248 | Thymidine-5'-(trihydrogendiphosphate) (TDP) | H4L | Pyrimidines | 13 | `Cc1cn([C@H]2C[C@H](O)[C@@H](COP(=O)(O)OP(=O)(O)O)O2)c(=O)[nH]c1=O` | (-inf, H2L, -1.3, HL, 6.33, L, 9.82, H-1L, +inf) |
| ligand_8317 | Inosine-5'-(trihydrogendiphosphate) (IDP) | H3L | Purines phosphates | 4 | `O=P(O)(O)OP(=O)(O)OC[C@H]1O[C@@H](n2cnc3c(O)ncnc32)[C@H](O)[C@@H]1O` | (-inf, HL, 6.69, L, +inf) |
| ligand_8318 | Adenosine-5'-(trihydrogendiphosphate) (ADP) | H3L | Purines phosphates | 123 | `Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]1O` | (-inf, H3L, 1.8, H2L, 3.87, HL, 6.3, L, +inf) |
| ligand_8319 | Guanosine-5'-(trihydrogendiphosphate) (GDP) | H3L | Purines phosphates | 9 | `Nc1nc2c(ncn2[C@@H]2O[C@H](COP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]2O)c(=O)[nH]1` | (-inf, H2L, 2.8, HL, 6.3, L, +inf) |
| ligand_9164 | D(-)-Fructose-1,6-bis(… (Fructose-1,6-diphosphate) | H4L | Organophosphorus and ars… | 6 | `O=P(O)(O)OC[C@@H]1O[C@@](O)(COP(=O)(O)O)[C@@H](O)[C@H]1O` | (-inf, H2L, 5.86, HL, 6.66, L, +inf) |
| ligand_9165 | Diphosphoric acid methyl est… (Methyl diphosphate) | H3L | Organophosphorus and ars… | 9 | `COP(=O)(O)OP(=O)(O)O` | (-inf, H2L, -1.6, HL, 6.37, L, +inf) |
| ligand_9166 | Diphosphoric acid butyl ester (Butyl diphosphate) | H3L | Organophosphorus and ars… | 12 | `CCCCOP(=O)(O)OP(=O)(O)O` | (-inf, H2L, -1.3, HL, 6.65, L, +inf) |
| ligand_9167 | Diphosphoric acid phenyl est… (Phenyl diphosphate) | H3L | Organophosphorus and ars… | 12 | `O=P(O)(O)OP(=O)(O)Oc1ccccc1` | (-inf, H2L, -1.3, HL, 6.32, L, +inf) |
| ligand_10114 | Hydrogen diphosphate (Pyrophosphoric acid) | H4L | Inorganic ligands | 211 | `O=P(O)(O)OP(=O)(O)O` | (-inf, H4L, -0.8, H3L, -0.8, H2L, 5.94, HL, 8.25, L, +inf) |
| ligand_10115 | Hydrogen diphosphate(III,V) | H3L | Inorganic ligands | 13 | `O=[PH](O)OP(=O)(O)O` | (-inf, H2L, -1.6, HL, 6.14, L, +inf) |

### Functional groups across all SQL matches (14 parseable SMILES)

| group | count | % |
|-------|-------|---|
| hydroxyl | 14 | 100% |
| phosphate | 13 | 93% |
| aromatic_ring | 7 | 50% |
| ether | 7 | 50% |
| primary_amine | 3 | 21% |
| secondary_amine | 1 | 7% |

---

### Step 22: `search_ligands`
**Args:**
```json
{
  "name": "triphosphate",
  "limit": 12
}
```

[summary]
## search_ligands — 12 result(s)

**stats:** 17 SQL matches · showing 12 · limit 12

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8236 | Cytidine-5'-(tetrahydrogentriphosphate) (CTP) | H4L | Pyrimidines | 59 | `Nc1ccn([C@@H]2O[C@H](COP(=O)(O)OP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]2O)c(=O)n1` | (-inf, H2L, 4.47, HL, 6.42, L, +inf) |
| ligand_8244 | Uridine-5'-(tetrahydrogentriphosphate) (UTP) | H4L | Pyrimidines | 41 | `O=c1ccn([C@@H]2O[C@H](COP(=O)(O)OP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]2O)c(=O)[nH]1` | (-inf, H2L, -1.9, HL, 6.34, L, 9.59, H-1L, +inf) |
| ligand_8249 | Thymidine-5'-(tetrahydrogentriphosphate) (TTP) | H4L | Pyrimidines | 27 | `Cc1cn([C@H]2C[C@H](O)[C@@H](COP(=O)(O)OP(=O)(O)OP(=O)(O)O)O2)c(=O)[nH]c1=O` | (-inf, H2L, -1.9, HL, 6.4, L, 9.78, H-1L, +inf) |
| ligand_8320 | Inosine-5'-(tetrahydrogentriphosphate) (ITP) | H4L | Purines phosphates | 61 | `O=P(O)(O)OP(=O)(O)OP(=O)(O)OC[C@H]1O[C@@H](n2cnc3c(O)ncnc32)[C@H](O)[C@@H]1O` | (-inf, H2L, 2.15, HL, 6.4, L, 9.1, H-1L, +inf) |
| ligand_8321 | Adenosine-5'-(tetrahydrogentriphosphate) (ATP) | H4L | Purines phosphates | 188 | `Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)OP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]1O` | (-inf, H3L, -1.9, H2L, 3.99, HL, 6.38, L, +inf) |
| ligand_8322 | Guanosine-5'-(tetrahydrogentriphosphate) (GTP) | H4L | Purines phosphates | 49 | `Nc1nc2c(ncn2[C@@H]2O[C@H](COP(=O)(O)OP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]2O)c(=O)[nH]1` | (-inf, H2L, 2.93, HL, 6.41, L, 9.55, H-1L, +inf) |
| ligand_8326 | 1,N(6)-Ethenoadenosine-5'-(tetrahydrogentriphosph… | H4L | Purines phosphates | 12 | `O=P(O)(O)OP(=O)(O)OP(=O)(O)OC[C@H]1O[C@@H](n2cnc3c2ncn2ccnc32)[C@H](O)[C@@H]1O` | (-inf, H2L, 4.45, HL, 6.5, L, +inf) |
| ligand_9168 | Triphosphoric acid methyl e… (Methyl triphosphate) | H4L | Organophosphorus and ars… | 3 | `COP(=O)(O)OP(=O)(O)OP(=O)(O)O` | (-inf, HL, 6.45, L, +inf) |
| ligand_10117 | Hydrogen triphosphate (Triphosphoric acid) | H5L | Inorganic ligands | 176 | `O=P(O)(O)OP(=O)(O)OP(=O)(O)O` | (-inf, H5L, -0.5, H4L, -0.5, H3L, -0.9, H2L, 5.42, HL, 7.77, L, +inf) |
| ligand_10118 | Hydrogen triphosphate(IV,III,IV) | H5L | Inorganic ligands | 8 | `O=P(O)(O)P(=O)(O)P(=O)(O)O` | (-inf, H2L, 7.32, HL, 10.28, L, +inf) |
| ligand_10130 | Hydrogen diimidotriph… (Diimidotriphosphoric acid) | H5L | Inorganic ligands | 18 | `O=P(O)(O)NP(=O)(O)NP(=O)(O)O` | (-inf, H5L, -1, H4L, 2, H3L, 3.03, H2L, 6.61, HL, 9.84, L, +inf) |
| ligand_10819 | Adenosine-3'-(tetrahydrogentriphosphate)-5'-(trih… | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (11 parseable SMILES)

| group | count | % |
|-------|-------|---|
| hydroxyl | 11 | 100% |
| phosphate | 9 | 82% |
| aromatic_ring | 7 | 64% |
| ether | 7 | 64% |
| primary_amine | 3 | 27% |
| secondary_amine | 1 | 9% |

---

### Step 23: `search_ligands`
**Args:**
```json
{
  "name": "oxalic acid",
  "limit": 12
}
```

[summary]
## search_ligands — 4 result(s)

**stats:** 4 SQL matches · showing 4 · limit 12

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

### Step 24: `search_ligands`
**Args:**
```json
{
  "name": "ethanedioate",
  "limit": 12
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 25: `search_ligands`
**Args:**
```json
{
  "name": "citric acid",
  "limit": 12
}
```

[summary]
## search_ligands — 8 result(s)

**stats:** 8 SQL matches · showing 8 · limit 12

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

### Step 26: `search_ligands`
**Args:**
```json
{
  "name": "hydrogen citrate",
  "limit": 12
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 27: `search_ligands`
**Args:**
```json
{
  "name": "tartaric acid",
  "limit": 12
}
```

[summary]
## search_ligands — 9 result(s)

**stats:** 9 SQL matches · showing 9 · limit 12

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

### Step 28: `search_ligands`
**Args:**
```json
{
  "name": "hydrogen tartrate",
  "limit": 12
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 29: `search_ligands`
**Args:**
```json
{
  "name": "gluconic acid",
  "limit": 12
}
```

[summary]
## search_ligands — 2 result(s)

**stats:** 2 SQL matches · showing 2 · limit 12

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8668 | D-gluco-Pentahydroxyhexanoic ac… (D-Gluconic acid) | HL | Carboxylic acids hydroxy | 62 | `O=C(O)[C@H](O)[C@@H](O)[C@H](O)[C@H](O)CO` | (-inf, HL, 3.46, L, +inf) |
| ligand_10317 | 6-[Bis(1-methylethyl)aminoacetyl]… (Pangamic acid) | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 1 | 100% |
| hydroxyl | 1 | 100% |

---

### Step 30: `search_ligands`
**Args:**
```json
{
  "name": "lactic acid",
  "limit": 12
}
```

[summary]
## search_ligands — 4 result(s)

**stats:** 4 SQL matches · showing 4 · limit 12

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

### Step 32: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_25",
  "ligand_id": "ligand_10113"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 9 species

### Ca^[2+] + Hydrogen phosphate (Phosphoric acid)
**metal_id:** metal_25 | **ligand_id:** ligand_10113 | **ligand_def_HxL:** H3L  
**entries:** 40 | **species:** 9 | **vlm_count:** 40

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_156 | [M(H<sub>2</sub>L)<sub>2</sub>]/[M][H<s… | [M] + [H2L]^2 <=> [M(H2L)2] | [M(H2L)2](aqueous), [M](aqueous), [H2L](aqueous) | 1 |
| beta_def_296 | [M][HL]/[MHL(H<sub>2</sub>O)<sub>2</sub… | [MHL(H2O)2(s)] <=> [M] + [HL] + [H2O]^2 | [M](aqueous), [HL](aqueous), [H2O](aqueous), [MHL(H2O)2(s)](solid) | 7 |
| beta_def_298 | [M][HL]/[MHL(s)] | [MHL(s)] <=> [M] + [HL] | [M](aqueous), [HL](aqueous), [MHL(s)](solid) | 4 |
| beta_def_625 | [M]<sup>3</sup>[L]<sup>2</sup>/[M<sub>3… | [M3L2(s,beta)] <=> [M]^3 + [L]^2 | [M](aqueous), [L](aqueous), [M3L2(s,beta)](solid) | 4 |
| beta_def_665 | [M]<sup>4</sup>[H][L]<sup>3</sup>/[M<su… | [M4HL3(H2O)2.5(s)] <=> [M]^4 + [H] + [L… | [M](aqueous), [H](aqueous), [L](aqueous), [H2O](aqueous), [M4HL3(H2O)2.5(s)](so… | 1 |
| beta_def_666 | [M]<sup>4</sup>[H][L]<sup>3</sup>/[M<su… | [M4HL3(H2O)3(s)] <=> [M]^4 + [H] + [L]^… | [M](aqueous), [H](aqueous), [L](aqueous), [H2O](aqueous), [M4HL3(H2O)3(s)](soli… | 2 |
| beta_def_689 | [M]<sup>5</sup>[OH][L]<sup>3</sup>/[M<s… | [M5(OH)L3(H2O)(s)] <=> [M]^5 + [OH] + [… | [M](aqueous), [OH](aqueous), [L](aqueous), [H2O](aqueous), [M5(OH)L3(H2O)(s)](s… | 2 |
| beta_def_732 | [MH<sub>2</sub>L]/[M][H<sub>2</sub>L] | [M] + [H2L] <=> [MH2L] | [MH2L](aqueous), [M](aqueous), [H2L](aqueous) | 9 |
| beta_def_779 | [MHL]/[M][HL] | [M] + [HL] <=> [MHL] | [MHL](aqueous), [M](aqueous), [HL](aqueous) | 10 |

**vlm_ids:** vlm_174342, vlm_174343, vlm_174344, vlm_174345, vlm_174346, … vlm_174379, vlm_174380, vlm_174381 (40 listed)

**equilibrium_maps:** 10 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_28639 | 7 | 21 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_28640 | 8 | 28 | 31~41 °C | -0.15~0.15 M |
| ref_eq_net_28641 | 3 | 3 | 31~41 °C | 0~0.3 M |
| ref_eq_net_28642 | 3 | 3 | 31~41 °C | 0.35~0.65 M |
| ref_eq_net_28643 | 3 | 3 | 19~29 °C | 2.85~3.15 M |
| ref_eq_net_28644 | 2 | 1 | 15~25 °C | 0.55~0.85 M |
| ref_eq_net_28645 | 1 | 0 | 19~29 °C | -0.05~0.25 M |
| ref_eq_net_28646 | 1 | 0 | 19~29 °C | -0.15~0.15 M |
| ref_eq_net_28647 | 1 | 0 | 31~41 °C | 0~0.3 M |
| ref_eq_net_28648 | 1 | 0 | 13~23 °C | -0.15~0.15 M |

---

### Step 33: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id IN (metal_25, metal_41) AND c.ligand_id IN (ligand_10113, ligand_10114, ligand_10117, ligand_10096, ligand_10148, ligand_8872, ligand_9058, ligand_8955, ligand_8956, ligand_8668, ligand_8641, ligand_9676, ligand_7601, ligand_9142) AND (s.solvent_name IS NULL OR s.solvent_name LIKE '%water%') AND (s.temperature_c BETWEEN 20 AND 30) AND (s.ionic_strength_mol_l IS NULL OR s.ionic_strength_mol_l <= 0.2)",
  "order_by": "c.metal_id, c.ligand_id, s.constant_type, s.temperature_c, s.ionic_strength_mol_l",
  "limit": 2000
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. You must call 0_plan_search_strategy first (PHASE 2) before using the execution tools.

---
