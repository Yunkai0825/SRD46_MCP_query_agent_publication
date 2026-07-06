# Q4.1 — Tool Results (batch 1)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "iron",
  "symbol": "Fe",
  "limit": 5
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
  "name": "dimethylformamide",
  "limit": 10
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_11422 | N,N-Dimethylformamide (DMF) | *** | Ligands not selected | 0 | *** | *** |

---

### Step 4: `search_ligands`
**Args:**
```json
{
  "name": "acetonitrile",
  "limit": 10
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_9825 | Cyanomethane (Acetonitrile) | L | miscellaneous hydrocarbo… | 7 | `CC#N` | *** |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| nitrile | 1 | 100% |

---

### Step 5: `search_ligands`
**Args:**
```json
{
  "name": "tetrahydrofuran",
  "limit": 10
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
  "name": "ethylene glycol",
  "limit": 10
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_9621 | Ethane-1,2-diol (Ethylene glycol) | *** | miscellaneous alcohols a… | 22 | *** | *** |

---

### Step 8: `search_ligands`
**Args:**
```json
{
  "name": "oxolane",
  "limit": 10
}
```

[summary]
## search_ligands — 2 result(s)

**stats:** 2 SQL matches · showing 2 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6340 | 2,5-Bis[bis(carboxymethyl)aminomethyl]oxolane | H4L | EDTA and derivatives | 5 | `O=C(O)CN(CC(=O)O)CC1CCC(CN(CC(=O)O)CC(=O)O)O1` | (-inf, H4L, 2.42, H3L, 2.73, H2L, 8.67, HL, 8.95, L, +inf) |
| ligand_8979 | H2L Oxolane… (Perhydrofuran-2,5-dicarboxylic acid) | H2L | Carboxylic acids diacids | 1 | `O=C(O)C1CCC(C(=O)O)O1` | *** |

### Functional groups across all SQL matches (2 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 2 | 100% |
| ether | 2 | 100% |
| tertiary_amine | 1 | 50% |

---

### Step 9: `search_ligands`
**Args:**
```json
{
  "name": "THF",
  "limit": 10
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 10: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_62",
  "ligand_id": "ligand_9825"
}
```

[summary]
[CATALOG]
## build_system_catalog

*(no pairs found)*

**summary:** {'n_metals': 0, 'n_ligands': 0, 'n_pairs': 0, 'total_species': 0}

---

### Step 11: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_61",
  "ligand_id": "ligand_9825"
}
```

[summary]
[CATALOG]
## build_system_catalog

*(no pairs found)*

**summary:** {'n_metals': 0, 'n_ligands': 0, 'n_pairs': 0, 'total_species': 0}

---

### Step 12: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_62",
  "ligand_id": "ligand_9621"
}
```

[summary]
[CATALOG]
## build_system_catalog

*(no pairs found)*

**summary:** {'n_metals': 0, 'n_ligands': 0, 'n_pairs': 0, 'total_species': 0}

---

### Step 13: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_61",
  "ligand_id": "ligand_9621"
}
```

[summary]
[CATALOG]
## build_system_catalog

*(no pairs found)*

**summary:** {'n_metals': 0, 'n_ligands': 0, 'n_pairs': 0, 'total_species': 0}

---

### Step 14: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_62",
  "ligand_id": "ligand_11422"
}
```

[summary]
[CATALOG]
## build_system_catalog

*(no pairs found)*

**summary:** {'n_metals': 0, 'n_ligands': 0, 'n_pairs': 0, 'total_species': 0}

---

### Step 15: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_61",
  "ligand_id": "ligand_11422"
}
```

[summary]
[CATALOG]
## build_system_catalog

*(no pairs found)*

**summary:** {'n_metals': 0, 'n_ligands': 0, 'n_pairs': 0, 'total_species': 0}

---

### Step 17: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_61, metal_62) AND c.ligand_id IN (ligand_9825, ligand_9621, ligand_11422))",
  "order_by": "s.constant_value DESC",
  "limit": 200
}
```

[summary]
## search_stability

*(no results)*

---

### Step 18: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_61, metal_62) AND (c.ligand_name_SRD LIKE '%tetrahydrofuran%' OR c.ligand_name_SRD LIKE '%oxolane%'))",
  "order_by": "s.constant_value DESC",
  "limit": 200
}
```

[summary]
## search_stability

*(no results)*

---

### Step 19: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_61, metal_62) AND (c.ligand_name_SRD LIKE '%nitrile%' OR c.ligand_name_SRD LIKE '%benzonitrile%' OR c.ligand_name_SRD LIKE '%propionitrile%' OR c.ligand_name_SRD LIKE '%acrylonitrile%' OR c.ligand_name_SRD LIKE '%cyan%'))",
  "order_by": "s.constant_value DESC",
  "limit": 300
}
```

[summary]
## search_stability — 76 row(s)

### ΔS — 9 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 6 | 3 | 25 | 0~3 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9251 | 3-Cyanophenol | HL | N#Cc1cccc(O)c1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9250 | 2-Cyanophenol | HL | N#Cc1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9252 | 4-Cyanophenol | HL | N#Cc1ccc(O)cc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_10090 | Hydrogen cyanide (Hydrocyan… | HL | C#N | 1 | 1 | 25 | 0 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_10090 | Hydrogen cyanide (Hydrocyan… | HL | C#N | 1 | 1 | 25 | 0 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9878 | N-(3-Cyanophenyl)acetohydro… | HL | CC(=O)N(O)c1cccc(C#N)c1 | 1 | 1 | 25 | 2 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9879 | N-(4-Cyanophenyl)acetohydro… | HL | CC(=O)N(O)c1ccc(C#N)cc1 | 1 | 1 | 25 | 2 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_10085 | Hexacyanoferrate(III) ion | *** | *** | 1 | 1 | 25 | 0.5 | *** | 0 |

### logK — 16 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 27 | 5 | 20~25 | 0~5 | *** | 13 |
| metal_61 | Fe^[3+] | ligand_9394 | 3,3'-Dimethyl-4'-hydroxy-2'… | H4L | CC1=C/C(=C(/c2cc(C)c(O)c(C(=O)O)c2)c2ccccc2S(=O)(=O)O)C=C(C(=O)O)C1=O | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_10087 | Octacyanomolybdate(IV) ion | *** | *** | 2 | 2 | 25 | 0.3 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_10086 | Hexacyanocobaltate(III) ion | *** | *** | 2 | 1 | 25 | 0.5~1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_10085 | Hexacyanoferrate(III) ion | *** | *** | 2 | 1 | 25 | 0.5~1 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 2 | 1 | 25 | 0~3 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_9251 | 3-Cyanophenol | HL | N#Cc1cccc(O)c1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9250 | 2-Cyanophenol | HL | N#Cc1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9252 | 4-Cyanophenol | HL | N#Cc1ccc(O)cc1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_10090 | Hydrogen cyanide (Hydrocyan… | HL | C#N | 1 | 1 | 25 | 0 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_10090 | Hydrogen cyanide (Hydrocyan… | HL | C#N | 1 | 1 | 25 | 0 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9878 | N-(3-Cyanophenyl)acetohydro… | HL | CC(=O)N(O)c1cccc(C#N)c1 | 1 | 1 | 25 | 2 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9879 | N-(4-Cyanophenyl)acetohydro… | HL | CC(=O)N(O)c1ccc(C#N)cc1 | 1 | 1 | 25 | 2 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9573 | 5-Cyano-1-hydroxycyclohepta… | HL | N#Cc1ccc(O)c(=O)cc1 | 1 | 1 | 25 | 2 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9572 | 3-Cyano-1-hydroxycyclohepta… | HL | N#Cc1ccccc(O)c1=O | 1 | 1 | 25 | 2 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9344 | 4-Cyano-1,2-dihydroxybenzen… | H2L | N#Cc1ccc(O)c(O)c1 | 1 | 1 | 25 | 1 | *** | 1 |

### ΔH — 9 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 6 | 3 | 25 | 0~3 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9251 | 3-Cyanophenol | HL | N#Cc1cccc(O)c1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9250 | 2-Cyanophenol | HL | N#Cc1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9252 | 4-Cyanophenol | HL | N#Cc1ccc(O)cc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_10090 | Hydrogen cyanide (Hydrocyan… | HL | C#N | 1 | 1 | 25 | 0 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_10090 | Hydrogen cyanide (Hydrocyan… | HL | C#N | 1 | 1 | 25 | 0 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9878 | N-(3-Cyanophenyl)acetohydro… | HL | CC(=O)N(O)c1cccc(C#N)c1 | 1 | 1 | 25 | 2 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9879 | N-(4-Cyanophenyl)acetohydro… | HL | CC(=O)N(O)c1ccc(C#N)cc1 | 1 | 1 | 25 | 2 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_10085 | Hexacyanoferrate(III) ion | *** | *** | 1 | 1 | 25 | 0.5 | *** | 0 |

---

### Step 20: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_61, metal_62) AND (c.ligand_name_SRD LIKE '%amide%' OR c.ligand_name_SRD LIKE '%formamide%' OR c.ligand_name_SRD LIKE '%acetamide%' OR c.ligand_name_SRD LIKE '%propionamide%' OR c.ligand_name_SRD LIKE '%dimethylformamide%' OR c.ligand_name_SRD LIKE '%dimethylacetamide%' OR c.ligand_name_SRD LIKE '%N-methylacetamide%'))",
  "order_by": "s.constant_value DESC",
  "limit": 300
}
```

[summary]
## search_stability — 35 row(s)

### logK — 12 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_62 | Fe^[2+] | ligand_5843 | L-2-Aminobutanedioic acid 4… | HL | NC(=O)C[C@H](N)C(=O)O | 4 | 3 | 20~25 | 1~3 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_9322 | 4-Amino-2-hydroxybenzoic ac… | HL | NC(=O)c1ccc(N)cc1O | 3 | 3 | 25 | 3 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6052 | rac-1,2-Dimethylethylenedin… | H2L | CC(C(C)N(CC(N)=O)CC(=O)O)N(CC(N)=O)CC(=O)O | 3 | 3 | 37 | 0.15 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6051 | DL-1-Ethylethylenedinitrilo… | H2L | CCC(CN(CC(N)=O)CC(=O)O)N(CC(N)=O)CC(=O)O | 3 | 3 | 37 | 0.15 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6053 | meso-1,2-Dimethylethylenedi… | H2L | CC(C(C)N(CC(N)=O)CC(=O)O)N(CC(N)=O)CC(=O)O | 3 | 3 | 37 | 0.15 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9373 | 2,3-Dihydroxy-5-sulfobenzoi… | H3L | CN(C)C(=O)c1cc(S(=O)(=O)O)cc(O)c1O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9374 | 2,3-Dihydroxybenzoic acid d… | H2L | CN(C)C(=O)c1cccc(O)c1O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5844 | L-2-Aminopentanedioic acid … | HL | NC(=O)CC[C@H](N)C(=O)O | 3 | 3 | 25 | 3 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9320 | 2-Hydroxybenzoic acid amide… | HL | NC(=O)c1ccccc1O | 2 | 2 | 25 | 3 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6050 | DL-1-Methylethylenedinitril… | H2L | CC(CN(CC(N)=O)CC(=O)O)N(CC(N)=O)CC(=O)O | 2 | 2 | 37 | 0.15 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9915 | N,N'N''-Tris[2-(N-hydroxyca… | H3L | O=C(CCNC(=O)c1cc(C(=O)NCCC(=O)NO)cc(C(=O)NCCC(=O)NO)c1)NO | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_5843 | L-2-Aminobutanedioic acid 4… | HL | NC(=O)C[C@H](N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |

### ΔH — 2 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_9322 | 4-Amino-2-hydroxybenzoic ac… | HL | NC(=O)c1ccc(N)cc1O | 1 | 1 | 25 | 3 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9320 | 2-Hydroxybenzoic acid amide… | HL | NC(=O)c1ccccc1O | 1 | 1 | 25 | 3 | *** | 0 |

### ΔS — 2 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_9322 | 4-Amino-2-hydroxybenzoic ac… | HL | NC(=O)c1ccc(N)cc1O | 1 | 1 | 25 | 3 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9320 | 2-Hydroxybenzoic acid amide… | HL | NC(=O)c1ccccc1O | 1 | 1 | 25 | 3 | *** | 0 |

---

### Step 21: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_61, metal_62) AND (c.ligand_name_SRD LIKE '%diol%' OR c.ligand_name_SRD LIKE '%glycol%' OR c.ligand_name_SRD LIKE '%glycerol%' OR c.ligand_name_SRD LIKE '%diethylene glycol%' OR c.ligand_name_SRD LIKE '%propylene glycol%' OR c.ligand_class_name LIKE '%alcohol%'))",
  "order_by": "s.constant_value DESC",
  "limit": 300
}
```

[summary]
## search_stability — 10 row(s)

### `Fe^[2+]` + Mercaptoacetic acid (Thioglycolic acid) — 2 measurement(s)
metal_id: metal_62 | ligand_id: ligand_8766
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)CS

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_150592 | ref_eq_map_19472 | beta_def_840 | logK | 10.92 | 25 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (10.11, L, +inf) |
| vlm_150593 | ref_eq_map_19472 | beta_def_966 | logK | 1.62 | 25 | 0 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |

### `Fe^[3+]` + Oxydiacetic acid (Diglycolic acid) — 1 measurement(s)
metal_id: metal_61 | ligand_id: ligand_8974
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)COCC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_155690 | ref_eq_map_21371 | beta_def_812 | logK | 5.04 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (3.94, L, +inf) |

### `Fe^[3+]` + Hydroxyacetic acid (Glycolic acid) — 4 measurement(s)
metal_id: metal_61 | ligand_id: ligand_8640
ligand_HxL_def: HL | ligand_SMILES: O=C(O)CO

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_147409 | ref_eq_map_18185 | beta_def_812 | logK | 2.9 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (3.62, L, +inf) |
| vlm_147411 | ref_eq_map_18185 | beta_def_136 | logK | 2.41 | 25 | 1 | `[M(H-1L)] + [L] <=> [M(H-1L)L]` | *** | [L] | (3.62, L, +inf) |
| vlm_147412 | ref_eq_map_18185 | beta_def_140 | logK | 1.5 | 25 | 1 | `[M(H-1L)L] + [L] <=> [M(H-1L)L2]` | *** | [L] | (3.62, L, +inf) |
| vlm_147410 | ref_eq_map_18185 | beta_def_107 | logK | 1.31 | 25 | 1 | `[M(H-1L)] + [H] <=> [ML]` | *** |  |  |

### `Fe^[2+]` + Oxydiacetic acid (Diglycolic acid) — 2 measurement(s)
metal_id: metal_62 | ligand_id: ligand_8974
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)COCC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_155667 | ref_eq_map_21364 | beta_def_812 | logK | 2.56 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (3.94, L, +inf) |
| vlm_155668 | ref_eq_map_21364 | beta_def_779 | logK | 0.64 | 25 | 0.1 | `[M] + [HL] <=> [MHL]` | *** | [HL] | (2.82, HL, 3.94) |

### `Fe^[2+]` + Hydroxyacetic acid (Glycolic acid) — 1 measurement(s)
metal_id: metal_62 | ligand_id: ligand_8640
ligand_HxL_def: HL | ligand_SMILES: O=C(O)CO

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_147386 | ref_eq_map_18174 | beta_def_812 | logK | 1.33 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (3.62, L, +inf) |

---
