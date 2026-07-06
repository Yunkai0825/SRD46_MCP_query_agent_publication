# Q2.1.1 — Tool Results (batch 4)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "iron",
  "symbol": "Fe",
  "limit": 10
}
```

[summary]
## search_metals — 2 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_61 | Fe^[3+] | Fe | 3 | ✓ | [Fe+3] | InChI=1S/Fe/q+3 | beta_totN_128 | ligand_totN_406 | vlm_totN_1473 |
| metal_62 | Fe^[2+] | Fe | 2 | ✓ | [Fe+2] | InChI=1S/Fe/q+2 | beta_totN_57 | ligand_totN_217 | vlm_totN_667 |

---

### Step 3: `search_ligands`
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

### Step 4: `search_ligands`
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

### Step 5: `search_ligands`
**Args:**
```json
{
  "name": "nitrilotriacetic",
  "limit": 20
}
```

[summary]
## search_ligands — 20 result(s)

**stats:** 35 SQL matches · showing 20 · limit 20

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6047 | N,N''-Bis(3-hydroxy-6-methyl-2-pyridiny… (DTTA-HP) | H5L | Amino Acids | 24 | `Cc1ccc(O)c(CN(CCN(CCN(CC(=O)O)Cc2nc(C)ccc2O)CC(=O)O)CC(=O)O)n1` | (-inf, H8L, -1.5, H7L, 2.25, H6L, 3.49, H5L, 5.19, H4L, 6.21, H3L, 8.9, H2L, 10.95, HL, 10.95, L, +inf) |
| ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | NTA and derivatives | 534 | `O=C(O)CN(CC(=O)O)CC(=O)O` | (-inf, H4L, -1, H3L, -1, H2L, 2.52, HL, 9.46, L, +inf) |
| ligand_6166 | Nitrilotriacetic acid N-oxide | H3L | NTA and derivatives | 4 | `O=C(O)C[N+]([O-])(CC(=O)O)CC(=O)O` | (-inf, H2L, 2.57, HL, 7.89, L, +inf) |
| ligand_6172 | DL-2-Methylnitrilotriacetic acid | H3L | NTA and derivatives | 50 | `CC(C(=O)O)N(CC(=O)O)CC(=O)O` | (-inf, H3L, -1.5, H2L, -1.5, HL, -2.58, L, +inf) |
| ligand_6173 | DL-2-Ethylnitrilotriacetic acid | H3L | NTA and derivatives | 43 | `CCC(C(=O)O)N(CC(=O)O)CC(=O)O` | (-inf, H3L, -1.9, H2L, -1.9, HL, 9.81, L, +inf) |
| ligand_6174 | DL-2-Propylnitrilotriacetic acid | H3L | NTA and derivatives | 37 | `CCCC(C(=O)O)N(CC(=O)O)CC(=O)O` | (-inf, H3L, -1.6, H2L, 2.46, HL, 9.94, L, +inf) |
| ligand_6175 | DL-2-(2-Propyl)nitrilotriacetic acid | H3L | NTA and derivatives | 37 | `CC(C)C(C(=O)O)N(CC(=O)O)CC(=O)O` | (-inf, H3L, -1.7, H2L, 2.4, HL, 9.68, L, +inf) |
| ligand_6176 | DL-2-Hexylnitrilotriacetic acid | H3L | NTA and derivatives | 25 | `CCCCCCC(C(=O)O)N(CC(=O)O)CC(=O)O` | (-inf, H3L, -1.9, H2L, 2.51, HL, 10.08, L, +inf) |
| ligand_6177 | 2,2-Dimethylnitrilotriacetic acid | H3L | NTA and derivatives | 8 | `CC(C)(C(=O)O)N(CC(=O)O)CC(=O)O` | (-inf, H3L, -1.5, H2L, 2.52, HL, 11.86, L, +inf) |
| ligand_6178 | DL-2-Benzylnitrilotriacetic acid | H3L | NTA and derivatives | 28 | `O=C(O)CN(CC(=O)O)C(Cc1ccccc1)C(=O)O` | (-inf, H3L, 2, H2L, 2.51, HL, 9.59, L, +inf) |
| ligand_6179 | DL-2-Phenylnitrilotriacetic acid | H3L | NTA and derivatives | 8 | `O=C(O)CN(CC(=O)O)C(C(=O)O)c1ccccc1` | (-inf, H3L, -1.5, H2L, 2.39, HL, 9.26, L, +inf) |
| ligand_6180 | DL-2-(4-Chlorophenyl)nitrilotriacetic acid | H3L | NTA and derivatives | 8 | `O=C(O)CN(CC(=O)O)C(C(=O)O)c1ccc(Cl)cc1` | (-inf, H3L, -1.6, H2L, 2.31, HL, 8.88, L, +inf) |
| ligand_6181 | DL-2-(4-Methylphenyl)nitrilotriacetic acid | H3L | NTA and derivatives | 8 | `Cc1ccc(C(C(=O)O)N(CC(=O)O)CC(=O)O)cc1` | (-inf, H3L, -1.5, H2L, 2.4, HL, 9.45, L, +inf) |
| ligand_6182 | DL-2-(4-Methoxyphenyl)nitrilotriacetic acid | H3L | NTA and derivatives | 8 | `COc1ccc(C(C(=O)O)N(CC(=O)O)CC(=O)O)cc1` | (-inf, H3L, -1.5, H2L, 2.44, HL, 9.51, L, +inf) |
| ligand_6183 | DL-2-Methyl-2-phenylnitrilotriacetic acid | H3L | NTA and derivatives | 8 | `CC(C(=O)O)(c1ccccc1)N(CC(=O)O)CC(=O)O` | (-inf, H3L, -1.5, H2L, 2.66, HL, 11.07, L, +inf) |
| ligand_6188 | DL-2-(2-Methylthioethyl)nitrilotriacetic acid | H3L | NTA and derivatives | 32 | `CSCCC(C(=O)O)N(CC(=O)O)CC(=O)O` | (-inf, H4L, 2.11, H3L, 2.47, H2L, 7.6, HL, 7.6, L, +inf) |
| ligand_6189 | 2-Carboxynitrilotriacetic acid | H4L | NTA and derivatives | 8 | `O=C(O)CN(CC(=O)O)C(C(=O)O)C(=O)O` | (-inf, H4L, 2.93, H3L, 3.74, H2L, 3.94, HL, 8.7, L, +inf) |
| ligand_6190 | DL-2-(Carboxymethyl)nitrilotriacetic acid | H4L | NTA and derivatives | 10 | `O=C(O)CC(C(=O)O)N(CC(=O)O)CC(=O)O` | (-inf, H4L, 2.46, H3L, 2.79, H2L, 4.26, HL, 9.18, L, +inf) |
| ligand_6191 | DL-2-(2-Carboxyethyl)nitrilotriacetic acid | H4L | NTA and derivatives | 11 | `O=C(O)CCC(C(=O)O)N(CC(=O)O)CC(=O)O` | (-inf, H4L, 2.56, H3L, 3.49, H2L, 5.03, HL, 9.36, L, +inf) |
| ligand_6229 | N-(Carbamylmethyl)iminodiacetic acid (Nitri… (ADA) | H2L | NTA and derivatives | 57 | `NC(=O)CN(CC(=O)O)CC(=O)O` | (-inf, H2L, 2.31, HL, 6.67, L, +inf) |

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

### Step 6: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_61",
  "ligand_id": "ligand_6277"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 4 species

### Fe^[3+] + Ethylenedinitrilotetraacetic acid (EDTA)
**metal_id:** metal_61 | **ligand_id:** ligand_6277 | **ligand_def_HxL:** H4L  
**entries:** 14 | **species:** 4 | **vlm_count:** 14

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_427 | [M<sub>2</sub>(OH)<sub>2</sub>L<sub>2</… | [M(OH)L]^2 <=> [M2(OH)2L2] | [M2(OH)2L2](aqueous), [M(OH)L](aqueous) | 3 |
| beta_def_788 | [MHL]/[ML][H] | [ML] + [H] <=> [MHL] | [MHL](aqueous), [ML](aqueous), [H](aqueous) | 3 |
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 4 |
| beta_def_966 | [ML]/[M(OH)L][H] | [M(OH)L] + [H] <=> [ML] + [H2O] | [ML](aqueous), [H2O](aqueous), [M(OH)L](aqueous), [H](aqueous) | 4 |

**vlm_ids:** vlm_108639, vlm_108640, vlm_108641, vlm_108642, vlm_108643, … vlm_108650, vlm_108651, vlm_108652 (14 listed)

**equilibrium_maps:** 2 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_5034 | 3 | 3 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_5035 | 3 | 2 | 19~29 °C | 0.85~1.15 M |

---

### Step 7: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_61",
  "ligand_id": "ligand_6165"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 8 species

### Fe^[3+] + Nitrilotriacetic acid (NTA)
**metal_id:** metal_61 | **ligand_id:** ligand_6165 | **ligand_def_HxL:** H3L  
**entries:** 16 | **species:** 8 | **vlm_count:** 16

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_238 | [M(OH)L]/[M(OH)<sub>2</sub>L][H] | [M(OH)2L] + [H] <=> [M(OH)L] + [H2O] | [M(OH)L](aqueous), [H2O](aqueous), [M(OH)2L](aqueous), [H](aqueous) | 2 |
| beta_def_263 | [M(OH)<sub>2</sub>L]/[M(OH)<sub>3</sub>… | [M(OH)3L] + [H] <=> [M(OH)2L] + [H2O] | [M(OH)2L](aqueous), [H2O](aqueous), [M(OH)3L](aqueous), [H](aqueous) | 1 |
| beta_def_423 | [M<sub>2</sub>(OH)<sub>2</sub>L<sub>2</… | [ML]^2 + [H2O]^2 <=> [M2(OH)2L2] + [H]^2 | [M2(OH)2L2](aqueous), [H](aqueous), [ML](aqueous), [H2O](aqueous) | 1 |
| beta_def_427 | [M<sub>2</sub>(OH)<sub>2</sub>L<sub>2</… | [M(OH)L]^2 <=> [M2(OH)2L2] | [M2(OH)2L2](aqueous), [M(OH)L](aqueous) | 1 |
| beta_def_788 | [MHL]/[ML][H] | [ML] + [H] <=> [MHL] | [MHL](aqueous), [ML](aqueous), [H](aqueous) | 1 |
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 4 |
| beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | [M] + [L]^2 <=> [ML2] | [ML2](aqueous), [M](aqueous), [L](aqueous) | 2 |
| beta_def_966 | [ML]/[M(OH)L][H] | [M(OH)L] + [H] <=> [ML] + [H2O] | [ML](aqueous), [H2O](aqueous), [M(OH)L](aqueous), [H](aqueous) | 4 |

**vlm_ids:** vlm_105553, vlm_105554, vlm_105555, vlm_105556, vlm_105557, … vlm_105566, vlm_105567, vlm_105568 (16 listed)

**equilibrium_maps:** 5 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_3758 | 5 | 5 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_3759 | 5 | 8 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_3760 | 2 | 1 | 15~25 °C | -0.05~0.25 M |
| ref_eq_net_3761 | 1 | 0 | 15~25 °C | -0.05~0.25 M |
| ref_eq_net_3762 | 1 | 0 | 19~29 °C | 0.35~0.65 M |

---

### Step 9: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND c.beta_definition_id = beta_def_812 AND c.ligand_id IN (ligand_6277, ligand_6165) AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "c.ligand_id ASC, s.temperature_c ASC, s.ionic_strength_mol_l ASC",
  "limit": 50
}
```

[summary]
## search_stability — 8 row(s)

### `Fe^[3+]` + Nitrilotriacetic acid (NTA) — 4 measurement(s)
metal_id: metal_61 | ligand_id: ligand_6165
ligand_HxL_def: H3L | ligand_SMILES: O=C(O)CN(CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_105555 | *** | beta_def_812 | ΔH | 13.4 | 20 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.46, L, +inf) |
| vlm_105553 | ref_eq_map_3754 | beta_def_812 | logK | 15.9 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.46, L, +inf) |
| vlm_105556 | *** | beta_def_812 | ΔS | 349.8 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.46, L, +inf) |
| vlm_105554 | ref_eq_map_3755 | beta_def_812 | logK | 14.78 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.46, L, +inf) |

### `Fe^[3+]` + Ethylenedinitrilotetraacetic acid (EDTA) — 4 measurement(s)
metal_id: metal_61 | ligand_id: ligand_6277
ligand_HxL_def: H4L | ligand_SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_108639 | ref_eq_map_5028 | beta_def_812 | logK | 25.1 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108641 | *** | beta_def_812 | ΔH | -11.3 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108642 | *** | beta_def_812 | ΔS | 442.7 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108640 | ref_eq_map_5029 | beta_def_812 | logK | 23.8 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |

---
