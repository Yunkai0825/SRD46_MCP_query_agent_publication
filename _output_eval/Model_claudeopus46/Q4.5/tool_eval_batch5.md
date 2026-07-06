# Q4.5 — Tool Results (batch 5)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "calcium"
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
  "name": "magnesium"
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_92 | Mg^[2+] | Mg | 2 | ✓ | [Mg+2] | InChI=1S/Mg/q+2 | beta_totN_53 | ligand_totN_508 | vlm_totN_1422 |

---

### Step 4: `search_metals`
**Args:**
```json
{
  "name": "strontium"
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_177 | Sr^[2+] | Sr | 2 | ✓ | [Sr+2] | InChI=1S/Sr/q+2 | beta_totN_34 | ligand_totN_362 | vlm_totN_784 |

---

### Step 5: `search_metals`
**Args:**
```json
{
  "name": "barium"
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_18 | Ba^[2+] | Ba | 2 | ✓ | [Ba+2] | InChI=1S/Ba/q+2 | beta_totN_36 | ligand_totN_344 | vlm_totN_749 |

---

### Step 6: `search_ligands`
**Args:**
```json
{
  "name": "acetate",
  "limit": 3
}
```

[summary]
## search_ligands — 3 result(s)

**stats:** 3 SQL matches · showing 3 · limit 3

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

### Step 7: `search_ligands`
**Args:**
```json
{
  "name": "glycine",
  "limit": 3
}
```

[summary]
## search_ligands — 3 result(s)

**stats:** 170 SQL matches · showing 3 · limit 3

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5760 | Aminoacetic acid (Glycine) | HL | Amino Acids | 428 | `NCC(=O)O` | (-inf, H2L, 2.33, HL, 9.57, L, +inf) |
| ligand_5776 | DL-Aminophenylacetic acid (Phenylglycine) | HL | Amino Acids | 12 | `NC(C(=O)O)c1ccccc1` | (-inf, H2L, -1.9, HL, 8.92, L, +inf) |
| ligand_5786 | DL-Amino-4-sulfophenylacet… (4-Sulfophenylglycine) | H2L | Amino Acids | 12 | `NC(C(=O)O)c1ccc(S(=O)(=O)O)cc1` | (-inf, H2L, -1.8, HL, 8.66, L, +inf) |

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

### Step 8: `search_ligands`
**Args:**
```json
{
  "name": "oxalate",
  "limit": 3
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 9: `search_ligands`
**Args:**
```json
{
  "name": "citrate",
  "limit": 3
}
```

[summary]
## search_ligands — 3 result(s)

**stats:** 4 SQL matches · showing 3 · limit 3

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8672 | 2-Hydroxypropane-1,2,3-tri… (sym-Dimethyl citrate) | HL | Carboxylic acids hydroxy | 2 | `COC(=O)CC(O)(CC(=O)OC)C(=O)O` | (-inf, HL, 3.02, L, +inf) |
| ligand_8682 | DL-2-Hydroxypropane-1,2,3-t… (as-Dimethyl citrate) | HL | Carboxylic acids hydroxy | 2 | `COC(=O)CC(O)(CC(=O)O)C(=O)OC` | (-inf, HL, 3.78, L, +inf) |
| ligand_8965 | 2-Hydroxypropane-1,2,3-tri… (as-Monomethylcitrate) | H2L | Carboxylic acids diacids… | 4 | `COC(=O)CC(O)(CC(=O)O)C(=O)O` | (-inf, H2L, 2.7, HL, 4.66, L, +inf) |

### Functional groups across all SQL matches (4 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 4 | 100% |
| ester | 4 | 100% |
| hydroxyl | 4 | 100% |

---

### Step 10: `search_ligands`
**Args:**
```json
{
  "name": "EDTA",
  "limit": 3
}
```

[summary]
## search_ligands — 3 result(s)

**stats:** 5 SQL matches · showing 3 · limit 3

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6118 | 6,11,18,23-Tetraoxo-1,4,7,10,13,16,19,… (24edtaen) | *** | Aza macrocycles with car… | 15 | *** | (-inf, H4L, 3.3, H3L, 4.18, H2L, 7.26, HL, 7.78, L, +inf) |
| ligand_6275 | N-(2-Hydroxyethyl)ethylenedinitrilotriace… (HEDTA) | H3L | EDTA and derivatives | 237 | `O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O` | (-inf, H3L, 2.62, H2L, 5.38, HL, 9.7, L, +inf) |
| ligand_6277 | Ethylenedinitrilotetraacetic acid (EDTA) | H4L | EDTA and derivatives | 596 | `O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O` | (-inf, H5L, -1.5, H4L, 2, H3L, 2.69, H2L, 6.13, HL, 9.52, L, +inf) |

### Functional groups across all SQL matches (4 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 4 | 100% |
| tertiary_amine | 4 | 100% |
| ether | 1 | 25% |
| hydroxyl | 1 | 25% |
| thioether | 1 | 25% |

---

### Step 11: `search_ligands`
**Args:**
```json
{
  "name": "malonate",
  "limit": 3
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 3

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8873 | Propanedioic acid (Malonic acid) | H2L | Carboxylic acids diacids | 505 | `O=C(O)CC(=O)O` | (-inf, H2L, 2.65, HL, 5.27, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 1 | 100% |

---

### Step 12: `search_ligands`
**Args:**
```json
{
  "name": "salicylate",
  "limit": 3
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 3

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

### Step 13: `search_ligands`
**Args:**
```json
{
  "name": "tartrate",
  "limit": 3
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
  "name": "NTA",
  "limit": 3
}
```

[summary]
## search_ligands — 3 result(s)

**stats:** 298 SQL matches · showing 3 · limit 3

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5763 | DL-2-Aminopentanoic acid (Norvaline) | HL | Amino Acids | 35 | `CCC[C@H](N)C(=O)O` | (-inf, H2L, 2.31, HL, 9.65, L, +inf) |
| ligand_5766 | L-2-Amino-4-methylpentanoic acid (Leucine) | HL | Amino Acids | 49 | `CC(C)C[C@H](N)C(=O)O` | (-inf, H2L, 2.32, HL, 9.58, L, +inf) |
| ligand_5767 | L-2-Amino-3-methylpentanoic acid (Isoleucine) | HL | Amino Acids | 51 | `CC[C@H](C)[C@H](N)C(=O)O` | (-inf, H2L, 2.26, HL, 9.6, L, +inf) |

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

### Step 15: `search_ligands`
**Args:**
```json
{
  "name": "succinate",
  "limit": 3
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 16: `search_ligands`
**Args:**
```json
{
  "name": "formate",
  "limit": 3
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 17: `search_ligands`
**Args:**
```json
{
  "name": "lactate",
  "limit": 3
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 18: `search_ligands`
**Args:**
```json
{
  "name": "iminodiacetate",
  "limit": 3
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 19: `search_ligands`
**Args:**
```json
{
  "name": "phosphate",
  "limit": 3
}
```

[summary]
## search_ligands — 3 result(s)

**stats:** 128 SQL matches · showing 3 · limit 3

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6391 | Glycyl-DL-… (Glycyl-DL-serine dihydrogenphosphate) | H3L | Peptides | 7 | `NCC(=O)N[C@@H](COP(=O)(O)O)C(=O)O` | (-inf, H3L, 2.91, H2L, 6.03, HL, 8.42, L, +inf) |
| ligand_6412 | DL-Phosphos… (DL-Serylglycine dihydrogenphosphate) | H3L | Peptides | 16 | `NC(COP(=O)(O)O)C(=O)NCC(=O)O` | (-inf, H3L, 3.16, H2L, 5.42, HL, 8.01, L, +inf) |
| ligand_6469 | L-Phosph… (L-Seryl-L-leucine dihydrogen phosphate) | H3L | Peptides | 3 | `CC(C)CC(NC(=O)C(N)COP(=O)(O)O)C(=O)O` | (-inf, H3L, 3.11, H2L, 5.47, HL, 8.26, L, +inf) |

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

### Step 20: `search_ligands`
**Args:**
```json
{
  "name": "carbonate",
  "limit": 3
}
```

[summary]
## search_ligands — 3 result(s)

**stats:** 4 SQL matches · showing 3 · limit 3

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_10096 | Hydrogen carbonate (Carbonic acid) | H2L | Inorganic ligands | 335 | `O=C(O)O` | (-inf, H2L, 6.13, HL, 9.91, L, +inf) |
| ligand_10097 | Hydrogen trithiocarbonate | H2L | Inorganic ligands | 4 | `S=C(S)S` | (-inf, H2L, 2.68, HL, 8.22, L, +inf) |
| ligand_10098 | Hydrogen perthiocarbonate | H2L | Inorganic ligands | 3 | `S=C(S)SS` | (-inf, HL, 7.24, L, +inf) |

### Functional groups across all SQL matches (4 parseable SMILES)

| group | count | % |
|-------|-------|---|
| thiol | 2 | 50% |
| carboxyl | 1 | 25% |

---

### Step 21: `search_ligands`
**Args:**
```json
{
  "name": "sulfate",
  "limit": 3
}
```

[summary]
## search_ligands — 3 result(s)

**stats:** 11 SQL matches · showing 3 · limit 3

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6852 | 2-Aminoethyl(hydrogensulfate) | HL | Aliphatic amines | 5 | `NCCOS(=O)(=O)O` | (-inf, HL, 9.182, L, +inf) |
| ligand_9382 | 2,3,4-Trihydroxybenzenesulfon… (Pyrogallolsulfate) | H4L | Catechols | 4 | `O=S(=O)(O)c1ccc(O)c(O)c1O` | (-inf, H3L, 8.28, H2L, 11.3, HL, +inf) |
| ligand_10148 | Hydrogen sulfate ion (Sulfuric acid) | HL | Inorganic ligands | 581 | `O=S(=O)([O-])O` | (-inf, HL, 1.54, L, +inf) |

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

### Step 22: `search_ligands`
**Args:**
```json
{
  "name": "malate",
  "limit": 3
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 3

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8953 | L-Hydroxybutanedioic acid (Hydroxysuccinic acid)(… | H2L | Carboxylic acids diacids… | 172 | `O=C(O)CC(O)C(=O)O` | (-inf, H2L, 3.24, HL, 4.68, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 1 | 100% |
| hydroxyl | 1 | 100% |

---

### Step 23: `search_ligands`
**Args:**
```json
{
  "name": "oxalic acid",
  "limit": 3
}
```

[summary]
## search_ligands — 3 result(s)

**stats:** 4 SQL matches · showing 3 · limit 3

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8872 | Ethanedioic acid (Oxalic acid) | H2L | Carboxylic acids diacids | 394 | `O=C(O)C(=O)O` | (-inf, H2L, -1.2, HL, 3.8, L, +inf) |
| ligand_8960 | Oxopropanedioic acid (Ketomaloni… (Mesoxalic acid) | H2L | Carboxylic acids diacids… | 3 | `O=C(O)C(=O)C(=O)O` | (-inf, H2L, -1.82, HL, 3.52, L, +inf) |
| ligand_9763 | Dithiooxalic acid | H2L | miscellaneous mercaptans | 3 | `O=C(S)C(=O)S` | *** |

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
  "name": "succinic acid",
  "limit": 3
}
```

[summary]
## search_ligands — 3 result(s)

**stats:** 13 SQL matches · showing 3 · limit 3

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6138 | 2,2'-Bis(2-Carboxymethyl)iminodiacetic acid (Imin… | H4L | Iminodiacetic acid and d… | 26 | `O=C(O)CC(NC(CC(=O)O)C(=O)O)C(=O)O` | (-inf, H4L, -1.97, H3L, 3.24, H2L, 4.24, HL, 10, L, +inf) |
| ligand_8907 | Butanedioic acid (Succinic acid) | H2L | Carboxylic acids diacids | 253 | `O=C(O)CCC(=O)O` | (-inf, H2L, 3.99, HL, 5.24, L, +inf) |
| ligand_8908 | DL-Propane-1,2-dicarboxylic… (Methylsuccinic acid) | H2L | Carboxylic acids diacids | 38 | `CC(CC(=O)O)C(=O)O` | (-inf, H2L, 3.88, HL, 5.35, L, +inf) |

### Functional groups across all SQL matches (11 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 11 | 100% |
| hydroxyl | 2 | 18% |
| secondary_amine | 1 | 9% |

---

### Step 25: `search_ligands`
**Args:**
```json
{
  "name": "formic acid",
  "limit": 3
}
```

[summary]
## search_ligands — 3 result(s)

**stats:** 4 SQL matches · showing 3 · limit 3

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8464 | Methanoic acid (Formic acid) | HL | Carboxylic acids | 128 | `O=CO` | (-inf, HL, 3.57, L, +inf) |
| ligand_8628 | Phosphinoformic acid | H2L | Carboxylic acids | 2 | `O=C(O)[PH](=O)O` | (-inf, H2L, -1.7, HL, 3.19, L, +inf) |
| ligand_8629 | Phosphonoformic acid | H3L | Carboxylic acids | 23 | `O=C(O)P(=O)(O)O` | (-inf, H3L, -1.7, H2L, 3.6, HL, 7.57, L, +inf) |

### Functional groups across all SQL matches (3 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 3 | 100% |
| hydroxyl | 2 | 67% |
| aldehyde | 1 | 33% |
| phosphonate | 1 | 33% |

---

### Step 26: `search_ligands`
**Args:**
```json
{
  "name": "lactic acid",
  "limit": 3
}
```

[summary]
## search_ligands — 3 result(s)

**stats:** 4 SQL matches · showing 3 · limit 3

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8641 | D-2-Hydroxypropanoic acid (Lactic acid) | HL | Carboxylic acids hydroxy | 349 | `CC(O)C(=O)O` | (-inf, HL, 3.67, L, +inf) |
| ligand_8660 | DL-2-Phenyl-2-hydroxypropanoic … (Atrolactic acid) | HL | Carboxylic acids hydroxy | 34 | `CC(O)(C(=O)O)c1ccccc1` | (-inf, HL, 3.53, L, +inf) |
| ligand_8767 | DL-2-Mercaptopropanoic acid (Thiolactic acid) | H2L | Carboxylic acids thio | 71 | `CC(S)C(=O)O` | (-inf, H2L, 3.48, HL, 10.08, L, +inf) |

### Functional groups across all SQL matches (4 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 4 | 100% |
| hydroxyl | 2 | 50% |
| aromatic_ring | 1 | 25% |
| ether | 1 | 25% |
| thiol | 1 | 25% |

---

### Step 27: `search_ligands`
**Args:**
```json
{
  "name": "tartaric acid",
  "limit": 3
}
```

[summary]
## search_ligands — 3 result(s)

**stats:** 9 SQL matches · showing 3 · limit 3

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8955 | D-2,3-Dihydroxybutanedioic acid (D-Tartaric acid) | H2L | Carboxylic acids diacids… | 214 | `O=C(O)C(O)C(O)C(=O)O` | (-inf, H2L, 2.82, HL, 3.97, L, +inf) |
| ligand_8956 | meso-2,3-Dihydroxybutanedioi… (meso-Tartaric acid) | H2L | Carboxylic acids diacids… | 43 | `O=C(O)[C@@H](O)[C@@H](O)C(=O)O` | (-inf, H2L, 2.97, HL, 4.49, L, +inf) |
| ligand_8996 | DL-2,3-Dimercaptobutaned… (DL-Dithiotartaric acid) | H4L | Carboxylic acids diacids… | 9 | `O=C(O)C(S)C(S)C(=O)O` | (-inf, H4L, 2.25, H3L, 3.96, H2L, 9.61, HL, +inf) |

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
  "name": "nitrilotriacetic",
  "limit": 3
}
```

[summary]
## search_ligands — 3 result(s)

**stats:** 35 SQL matches · showing 3 · limit 3

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6047 | N,N''-Bis(3-hydroxy-6-methyl-2-pyridiny… (DTTA-HP) | H5L | Amino Acids | 24 | `Cc1ccc(O)c(CN(CCN(CCN(CC(=O)O)Cc2nc(C)ccc2O)CC(=O)O)CC(=O)O)n1` | (-inf, H8L, -1.5, H7L, 2.25, H6L, 3.49, H5L, 5.19, H4L, 6.21, H3L, 8.9, H2L, 10.95, HL, 10.95, L, +inf) |
| ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | NTA and derivatives | 534 | `O=C(O)CN(CC(=O)O)CC(=O)O` | (-inf, H4L, -1, H3L, -1, H2L, 2.52, HL, 9.46, L, +inf) |
| ligand_6166 | Nitrilotriacetic acid N-oxide | H3L | NTA and derivatives | 4 | `O=C(O)C[N+]([O-])(CC(=O)O)CC(=O)O` | (-inf, H2L, 2.57, HL, 7.89, L, +inf) |

### Functional groups across all SQL matches (34 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 34 | 100% |
| tertiary_amine | 33 | 97% |
| aromatic_ring | 12 | 35% |
| hydroxyl | 4 | 12% |
| amide | 2 | 6% |
| halide | 2 | 6% |
| phenol | 1 | 3% |
| pyridine | 1 | 3% |
| secondary_amine | 1 | 3% |
| sulfonate | 1 | 3% |
| thioether | 1 | 3% |

---

### Step 29: `search_ligands`
**Args:**
```json
{
  "name": "iminodiacetic",
  "limit": 3
}
```

[summary]
## search_ligands — 3 result(s)

**stats:** 140 SQL matches · showing 3 · limit 3

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5975 | Ethylenediiminodiacetic acid (EDDA) | H2L | Amino Acids | 198 | `O=C(O)CNCCNCC(=O)O` | (-inf, H4L, -1.3, H3L, 2.12, H2L, 6.55, HL, 9.61, L, +inf) |
| ligand_5994 | N,N'-Bis(2-hydroxyphenyl)ethylenediiminodi… (HPED) | H4L | Amino Acids | 37 | `O=C(O)CN(CCN(CC(=O)O)c1ccccc1O)c1ccccc1O` | (-inf, H5L, -1.9, H4L, 3.58, H3L, 6.15, H2L, 10.44, HL, 10.44, L, +inf) |
| ligand_6013 | N-(4-Methylphenylsulfonyl)ethylenediiminodiacetic… | H2L | Amino Acids | 2 | `Cc1ccc(S(=O)(=O)N(CCNCC(=O)O)CC(=O)O)cc1` | (-inf, H2L, 2, HL, 7.83, L, +inf) |

### Functional groups across all SQL matches (117 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 117 | 100% |
| tertiary_amine | 106 | 91% |
| aromatic_ring | 51 | 44% |
| hydroxyl | 38 | 32% |
| secondary_amine | 17 | 15% |
| amide | 13 | 11% |
| phenol | 11 | 9% |
| sulfonate | 9 | 8% |
| ether | 3 | 3% |
| halide | 3 | 3% |
| ketone | 3 | 3% |
| primary_amine | 3 | 3% |
| pyridine | 3 | 3% |
| thioether | 3 | 3% |
| phosphonate | 2 | 2% |
| thiol | 2 | 2% |
| ester | 1 | 1% |
| nitrile | 1 | 1% |

---

### Step 30: `search_ligands`
**Args:**
```json
{
  "name": "acetic acid",
  "limit": 3
}
```

[summary]
## search_ligands — 3 result(s)

**stats:** 683 SQL matches · showing 3 · limit 3

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5760 | Aminoacetic acid (Glycine) | HL | Amino Acids | 428 | `NCC(=O)O` | (-inf, H2L, 2.33, HL, 9.57, L, +inf) |
| ligand_5776 | DL-Aminophenylacetic acid (Phenylglycine) | HL | Amino Acids | 12 | `NC(C(=O)O)c1ccccc1` | (-inf, H2L, -1.9, HL, 8.92, L, +inf) |
| ligand_5786 | DL-Amino-4-sulfophenylacet… (4-Sulfophenylglycine) | H2L | Amino Acids | 12 | `NC(C(=O)O)c1ccc(S(=O)(=O)O)cc1` | (-inf, H2L, -1.8, HL, 8.66, L, +inf) |

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

### Step 31: `search_ligands`
**Args:**
```json
{
  "name": "salicylic acid",
  "limit": 3
}
```

[summary]
## search_ligands — 3 result(s)

**stats:** 43 SQL matches · showing 3 · limit 3

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8701 | 2-Acetoxybenzoic acid (Acetylsalicylic acid) | HL | Carboxylic acids keto | 5 | `CC(=O)Oc1ccccc1C(=O)O` | (-inf, HL, 3.45, L, +inf) |
| ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | H2L | Phenols salicylic acids | 227 | `O=C(O)c1ccccc1O` | (-inf, H2L, 2.8, HL, 2.8, L, +inf) |
| ligand_9265 | 2-Hydroxy-3-methylbenzoic acid (3-Methylsalicylic… | H2L | Phenols salicylic acids | 9 | `Cc1cccc(C(=O)O)c1O` | (-inf, H2L, 2.83, HL, 2.83, L, +inf) |

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

### Step 32: `search_ligands`
**Args:**
```json
{
  "name": "citric acid",
  "limit": 3
}
```

[summary]
## search_ligands — 3 result(s)

**stats:** 8 SQL matches · showing 3 · limit 3

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_9057 | DL-1-Hydroxypropane-1,2,3-tricar… (Isocitric acid) | H3L | Carboxylic acids polyaci… | 24 | `O=C(O)CC(C(=O)O)C(O)C(=O)O` | (-inf, H3L, 3.05, H2L, 4.3, HL, 5.73, L, +inf) |
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxyli… (Citric acid) | H3L | Carboxylic acids polyaci… | 384 | `O=C(O)CC(O)(CC(=O)O)C(=O)O` | (-inf, H3L, 2.9, H2L, 4.35, HL, 5.65, L, +inf) |
| ligand_10950 | DL-Methylcitric acid | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (2 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 2 | 100% |
| hydroxyl | 2 | 100% |

---

### Step 33: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_25 AND c.ligand_id IN (ligand_8464, ligand_8641, ligand_8872, ligand_8873, ligand_8907, ligand_8955, ligand_8953, ligand_9058, ligand_9257, ligand_5760, ligand_6165, ligand_6277, ligand_10096, ligand_10148)",
  "order_by": "s.constant_value DESC",
  "limit": 200
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---

### Step 34: `search_pka_values`
**Args:**
```json
{
  "where": "lc.ligand_id IN (ligand_8464, ligand_8641, ligand_8872, ligand_8873, ligand_8907, ligand_8955, ligand_8953, ligand_9058, ligand_9257, ligand_5760, ligand_6165, ligand_6277, ligand_10096, ligand_10148)",
  "order_by": "lc.ligand_id, p.pKa ASC",
  "limit": 200
}
```

[PHASE ERROR] Tool 'search_pka_values' is not available yet. Complete PHASE 1 first: call build_system_catalog, then call 0_plan_search_strategy.

---
