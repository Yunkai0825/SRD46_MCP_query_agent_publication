# Q4.1 — Tool Results (batch 5)

### Step 2: `search_metals`
**Args:**
```json
{
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
  "name": "N,N-dimethylformamide",
  "limit": 25
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_11422 | N,N-Dimethylformamide (DMF) | *** | Ligands not selected | 0 | *** | *** |

---

### Step 4: `search_ligands`
**Args:**
```json
{
  "name": "acetonitrile",
  "limit": 25
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 25

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
  "name": "ethylene glycol",
  "limit": 25
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_9621 | Ethane-1,2-diol (Ethylene glycol) | *** | miscellaneous alcohols a… | 22 | *** | *** |

---

### Step 7: `search_ligands`
**Args:**
```json
{
  "name": "ethane-1,2-diol",
  "limit": 25
}
```

[summary]
## search_ligands — 3 result(s)

**stats:** 3 SQL matches · showing 3 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_9621 | Ethane-1,2-diol (Ethylene glycol) | *** | miscellaneous alcohols a… | 22 | *** | *** |
| ligand_10764 | 1,2-Di-2-pyridylethane-1,2-diol | *** | Ligands not selected | 0 | *** | *** |
| ligand_10765 | 1,2-Bis(6-methyl-2-pyridyl)ethane-1,2-diol | *** | Ligands not selected | 0 | *** | *** |

---

### Step 9: `search_ligands`
**Args:**
```json
{
  "name": "oxolane",
  "limit": 25
}
```

[summary]
## search_ligands — 2 result(s)

**stats:** 2 SQL matches · showing 2 · limit 25

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

### Step 10: `search_ligands`
**Args:**
```json
{
  "name": "THF",
  "limit": 25
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 11: `build_system_catalog`
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

### Step 12: `build_system_catalog`
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

### Step 13: `build_system_catalog`
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

### Step 14: `build_system_catalog`
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

### Step 15: `build_system_catalog`
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

### Step 16: `build_system_catalog`
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

### Step 18: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_62 AND (c.ligand_name_SRD LIKE '%dimethylformamide%' OR c.ligand_name_SRD LIKE '%DMF%') AND (s.solvent_name LIKE '%water%' OR s.solvent_name IS NULL) AND (s.temperature_c BETWEEN 293 AND 303))",
  "order_by": "s.constant_value DESC",
  "limit": 50
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
  "where": "(c.metal_id = metal_61 AND (c.ligand_name_SRD LIKE '%dimethylformamide%' OR c.ligand_name_SRD LIKE '%DMF%') AND (s.solvent_name LIKE '%water%' OR s.solvent_name IS NULL) AND (s.temperature_c BETWEEN 293 AND 303))",
  "order_by": "s.constant_value DESC",
  "limit": 50
}
```

[summary]
## search_stability

*(no results)*

---

### Step 20: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_62 AND (c.ligand_name_SRD LIKE '%acetonitrile%' OR c.ligand_name_SRD LIKE '%cyanomethane%') AND (s.solvent_name LIKE '%water%' OR s.solvent_name IS NULL) AND (s.temperature_c BETWEEN 293 AND 303))",
  "order_by": "s.constant_value DESC",
  "limit": 50
}
```

[summary]
## search_stability — 50 row(s)

### ΔS — 8 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_26 | Cd^[2+] | ligand_10093 | Selenocyanate ion | L | N#C[Se-] | 2 | 1 | 25 | 0~1 | *** | 0 |
| metal_68 | H^[+] | ligand_8626 | 2-Cyano-3-methyl-2-(2-propy… | HL | CC(C)C(C#N)(C(=O)O)C(C)C | 1 | 1 | 25 | 0 | *** | 0 |
| metal_68 | H^[+] | ligand_8625 | 2-Cyano-3-methylbutanoic ac… | HL | CC(C)C(C#N)C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_68 | H^[+] | ligand_8624 | 2-Cyano-2-methylpropanoic a… | HL | CC(C)(C#N)C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_33 | Co^[2+] | ligand_10093 | Selenocyanate ion | L | N#C[Se-] | 1 | 1 | 25 | 0 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_10093 | Selenocyanate ion | L | N#C[Se-] | 1 | 1 | 25 | 0 | *** | 0 |
| metal_127 | Pd^[2+] | ligand_9825 | Cyanomethane (Acetonitrile) | L | CC#N | 1 | 1 | 25 | 1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_10093 | Selenocyanate ion | L | N#C[Se-] | 1 | 1 | 25 | 1 | *** | 0 |

### ΔH — 6 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_8626 | 2-Cyano-3-methyl-2-(2-propy… | HL | CC(C)C(C#N)(C(=O)O)C(C)C | 1 | 1 | 25 | 0 | *** | 0 |
| metal_68 | H^[+] | ligand_8625 | 2-Cyano-3-methylbutanoic ac… | HL | CC(C)C(C#N)C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_68 | H^[+] | ligand_8624 | 2-Cyano-2-methylpropanoic a… | HL | CC(C)(C#N)C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_26 | Cd^[2+] | ligand_10093 | Selenocyanate ion | L | N#C[Se-] | 1 | 1 | 25 | 1 | *** | 0 |
| metal_127 | Pd^[2+] | ligand_9825 | Cyanomethane (Acetonitrile) | L | CC#N | 1 | 1 | 25 | 1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_10093 | Selenocyanate ion | L | N#C[Se-] | 1 | 1 | 25 | 1 | *** | 0 |

### logK — 21 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_26 | Cd^[2+] | ligand_10093 | Selenocyanate ion | L | N#C[Se-] | 5 | 4 | 25 | 0~1 | *** | 2 |
| metal_71 | Hg^[2+] | ligand_10093 | Selenocyanate ion | L | N#C[Se-] | 3 | 2 | 25 | 0.5~0.7 | *** | 2 |
| metal_112 | Ni^[2+] | ligand_10093 | Selenocyanate ion | L | N#C[Se-] | 3 | 2 | 25 | 0~1 | *** | 2 |
| metal_71 | Hg^[2+] | ligand_6816 | Cyanomethylamine | L | N#CCN | 2 | 2 | 25 | 0.5 | *** | 1 |
| metal_68 | H^[+] | ligand_6816 | Cyanomethylamine | L | N#CCN | 2 | 1 | 25 | 0.1~0.5 | *** | 2 |
| metal_2 | Ag^[+] | ligand_6816 | Cyanomethylamine | L | N#CCN | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_127 | Pd^[2+] | ligand_9825 | Cyanomethane (Acetonitrile) | L | CC#N | 2 | 2 | 25 | 1 | *** | 1 |
| metal_2 | Ag^[+] | ligand_9825 | Cyanomethane (Acetonitrile) | L | CC#N | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_10093 | Selenocyanate ion | L | N#C[Se-] | 2 | 2 | 25 | 1 | *** | 1 |
| metal_68 | H^[+] | ligand_8626 | 2-Cyano-3-methyl-2-(2-propy… | HL | CC(C)C(C#N)(C(=O)O)C(C)C | 1 | 1 | 25 | 0 | *** | 1 |
| metal_68 | H^[+] | ligand_8625 | 2-Cyano-3-methylbutanoic ac… | HL | CC(C)C(C#N)C(=O)O | 1 | 1 | 25 | 0 | *** | 1 |
| metal_68 | H^[+] | ligand_8624 | 2-Cyano-2-methylpropanoic a… | HL | CC(C)(C#N)C(=O)O | 1 | 1 | 25 | 0 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_9757 | 1,2-Dicyanoethene-1,2-dithi… | H2L | N#C/C(S)=C(\S)C#N | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_2 | Ag^[+] | ligand_10093 | Selenocyanate ion | L | N#C[Se-] | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_9754 | 2,2-Dicyanoethene-1,1-dithi… | H2L | N#CC(C#N)=C(S)S | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_10093 | Selenocyanate ion | L | N#C[Se-] | 1 | 1 | 25 | 0 | *** | 1 |
| metal_93 | MeHg^[+] | ligand_10093 | Selenocyanate ion | L | N#C[Se-] | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_42 | Cu^[+] | ligand_9825 | Cyanomethane (Acetonitrile) | L | CC#N | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_7921 | 4-Cyano-2,6-dimethylpyridine | L | Cc1cc(C#N)cc(C)n1 | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_2 | Ag^[+] | ligand_7921 | 4-Cyano-2,6-dimethylpyridine | L | Cc1cc(C#N)cc(C)n1 | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_7921 | 4-Cyano-2,6-dimethylpyridine | L | Cc1cc(C#N)cc(C)n1 | 1 | 1 | 25 | 0.5 | *** | 1 |

---

### Step 21: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND (c.ligand_name_SRD LIKE '%acetonitrile%' OR c.ligand_name_SRD LIKE '%cyanomethane%') AND (s.solvent_name LIKE '%water%' OR s.solvent_name IS NULL) AND (s.temperature_c BETWEEN 293 AND 303))",
  "order_by": "s.constant_value DESC",
  "limit": 50
}
```

[summary]
## search_stability — 50 row(s)

### ΔS — 8 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_26 | Cd^[2+] | ligand_10093 | Selenocyanate ion | L | N#C[Se-] | 2 | 1 | 25 | 0~1 | *** | 0 |
| metal_68 | H^[+] | ligand_8626 | 2-Cyano-3-methyl-2-(2-propy… | HL | CC(C)C(C#N)(C(=O)O)C(C)C | 1 | 1 | 25 | 0 | *** | 0 |
| metal_68 | H^[+] | ligand_8625 | 2-Cyano-3-methylbutanoic ac… | HL | CC(C)C(C#N)C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_68 | H^[+] | ligand_8624 | 2-Cyano-2-methylpropanoic a… | HL | CC(C)(C#N)C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_33 | Co^[2+] | ligand_10093 | Selenocyanate ion | L | N#C[Se-] | 1 | 1 | 25 | 0 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_10093 | Selenocyanate ion | L | N#C[Se-] | 1 | 1 | 25 | 0 | *** | 0 |
| metal_127 | Pd^[2+] | ligand_9825 | Cyanomethane (Acetonitrile) | L | CC#N | 1 | 1 | 25 | 1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_10093 | Selenocyanate ion | L | N#C[Se-] | 1 | 1 | 25 | 1 | *** | 0 |

### ΔH — 6 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_8626 | 2-Cyano-3-methyl-2-(2-propy… | HL | CC(C)C(C#N)(C(=O)O)C(C)C | 1 | 1 | 25 | 0 | *** | 0 |
| metal_68 | H^[+] | ligand_8625 | 2-Cyano-3-methylbutanoic ac… | HL | CC(C)C(C#N)C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_68 | H^[+] | ligand_8624 | 2-Cyano-2-methylpropanoic a… | HL | CC(C)(C#N)C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_26 | Cd^[2+] | ligand_10093 | Selenocyanate ion | L | N#C[Se-] | 1 | 1 | 25 | 1 | *** | 0 |
| metal_127 | Pd^[2+] | ligand_9825 | Cyanomethane (Acetonitrile) | L | CC#N | 1 | 1 | 25 | 1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_10093 | Selenocyanate ion | L | N#C[Se-] | 1 | 1 | 25 | 1 | *** | 0 |

### logK — 21 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_26 | Cd^[2+] | ligand_10093 | Selenocyanate ion | L | N#C[Se-] | 5 | 4 | 25 | 0~1 | *** | 2 |
| metal_71 | Hg^[2+] | ligand_10093 | Selenocyanate ion | L | N#C[Se-] | 3 | 2 | 25 | 0.5~0.7 | *** | 2 |
| metal_112 | Ni^[2+] | ligand_10093 | Selenocyanate ion | L | N#C[Se-] | 3 | 2 | 25 | 0~1 | *** | 2 |
| metal_71 | Hg^[2+] | ligand_6816 | Cyanomethylamine | L | N#CCN | 2 | 2 | 25 | 0.5 | *** | 1 |
| metal_68 | H^[+] | ligand_6816 | Cyanomethylamine | L | N#CCN | 2 | 1 | 25 | 0.1~0.5 | *** | 2 |
| metal_2 | Ag^[+] | ligand_6816 | Cyanomethylamine | L | N#CCN | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_127 | Pd^[2+] | ligand_9825 | Cyanomethane (Acetonitrile) | L | CC#N | 2 | 2 | 25 | 1 | *** | 1 |
| metal_2 | Ag^[+] | ligand_9825 | Cyanomethane (Acetonitrile) | L | CC#N | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_10093 | Selenocyanate ion | L | N#C[Se-] | 2 | 2 | 25 | 1 | *** | 1 |
| metal_68 | H^[+] | ligand_8626 | 2-Cyano-3-methyl-2-(2-propy… | HL | CC(C)C(C#N)(C(=O)O)C(C)C | 1 | 1 | 25 | 0 | *** | 1 |
| metal_68 | H^[+] | ligand_8625 | 2-Cyano-3-methylbutanoic ac… | HL | CC(C)C(C#N)C(=O)O | 1 | 1 | 25 | 0 | *** | 1 |
| metal_68 | H^[+] | ligand_8624 | 2-Cyano-2-methylpropanoic a… | HL | CC(C)(C#N)C(=O)O | 1 | 1 | 25 | 0 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_9757 | 1,2-Dicyanoethene-1,2-dithi… | H2L | N#C/C(S)=C(\S)C#N | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_2 | Ag^[+] | ligand_10093 | Selenocyanate ion | L | N#C[Se-] | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_9754 | 2,2-Dicyanoethene-1,1-dithi… | H2L | N#CC(C#N)=C(S)S | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_10093 | Selenocyanate ion | L | N#C[Se-] | 1 | 1 | 25 | 0 | *** | 1 |
| metal_93 | MeHg^[+] | ligand_10093 | Selenocyanate ion | L | N#C[Se-] | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_42 | Cu^[+] | ligand_9825 | Cyanomethane (Acetonitrile) | L | CC#N | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_7921 | 4-Cyano-2,6-dimethylpyridine | L | Cc1cc(C#N)cc(C)n1 | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_2 | Ag^[+] | ligand_7921 | 4-Cyano-2,6-dimethylpyridine | L | Cc1cc(C#N)cc(C)n1 | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_7921 | 4-Cyano-2,6-dimethylpyridine | L | Cc1cc(C#N)cc(C)n1 | 1 | 1 | 25 | 0.5 | *** | 1 |

---

### Step 22: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_62 AND (c.ligand_name_SRD LIKE '%tetrahydrofuran%' OR c.ligand_name_SRD LIKE '%oxolane%') AND (s.solvent_name LIKE '%water%' OR s.solvent_name IS NULL) AND (s.temperature_c BETWEEN 293 AND 303))",
  "order_by": "s.constant_value DESC",
  "limit": 50
}
```

[summary]
## search_stability

*(no results)*

---

### Step 23: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND (c.ligand_name_SRD LIKE '%tetrahydrofuran%' OR c.ligand_name_SRD LIKE '%oxolane%') AND (s.solvent_name LIKE '%water%' OR s.solvent_name IS NULL) AND (s.temperature_c BETWEEN 293 AND 303))",
  "order_by": "s.constant_value DESC",
  "limit": 50
}
```

[summary]
## search_stability

*(no results)*

---

### Step 24: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_62 AND (c.ligand_name_SRD LIKE '%ethylene glycol%' OR c.ligand_name_SRD LIKE '%ethane-1,2-diol%') AND (s.solvent_name LIKE '%water%' OR s.solvent_name IS NULL) AND (s.temperature_c BETWEEN 293 AND 303))",
  "order_by": "s.constant_value DESC",
  "limit": 50
}
```

[summary]
## search_stability

*(no results)*

---

### Step 25: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND (c.ligand_name_SRD LIKE '%ethylene glycol%' OR c.ligand_name_SRD LIKE '%ethane-1,2-diol%') AND (s.solvent_name LIKE '%water%' OR s.solvent_name IS NULL) AND (s.temperature_c BETWEEN 293 AND 303))",
  "order_by": "s.constant_value DESC",
  "limit": 50
}
```

[summary]
## search_stability

*(no results)*

---

### Step 26: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_62 AND (c.ligand_name_SRD LIKE '%formamide%' OR c.ligand_name_SRD LIKE '%acetamide%' OR c.ligand_name_SRD LIKE '%N-methylformamide%' OR c.ligand_name_SRD LIKE '%dimethylacetamide%') AND (s.solvent_name LIKE '%water%' OR s.solvent_name IS NULL) AND (s.temperature_c BETWEEN 293 AND 303))",
  "order_by": "s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability

*(no results)*

---

### Step 27: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND (c.ligand_name_SRD LIKE '%formamide%' OR c.ligand_name_SRD LIKE '%acetamide%' OR c.ligand_name_SRD LIKE '%N-methylformamide%' OR c.ligand_name_SRD LIKE '%dimethylacetamide%') AND (s.solvent_name LIKE '%water%' OR s.solvent_name IS NULL) AND (s.temperature_c BETWEEN 293 AND 303))",
  "order_by": "s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability

*(no results)*

---

### Step 28: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_62 AND (c.ligand_name_SRD LIKE '%propionitrile%' OR c.ligand_name_SRD LIKE '%benzonitrile%') AND (s.solvent_name LIKE '%water%' OR s.solvent_name IS NULL) AND (s.temperature_c BETWEEN 293 AND 303))",
  "order_by": "s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability — 100 row(s)

### ΔS — 34 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 8 | 2 | 25 | 0~1 | *** | 0 |
| metal_68 | H^[+] | ligand_7246 | 1,4,7,10,13,16-Hexaazahexad… | L | NCCNCCNCCNCCNCCN | 7 | 2 | 25 | 0~1 | *** | 0 |
| metal_68 | H^[+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 4 | 2 | 25 | 0.1~1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 3 | 2 | 25 | 0.1~1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 2 | 1 | 25 | 0.1~1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 2 | 1 | 25 | 0.1~1 | *** | 0 |
| metal_26 | Cd^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 2 | 1 | 25 | 0.1~1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_7253 | 2,5,8,11,14,17,20,23,26,29-… | L | CNCCNCCNCCNCCNCCNCCNCCNCCNCCNC | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 2 | 1 | 25 | 0.1~1 | *** | 0 |
| metal_68 | H^[+] | ligand_7236 | 2,5,8,11-Tetraazadodecane | L | CNCCNCCNCCNC | 2 | 2 | 25 | 0.5 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_7251 | 2,5,8,11,14,17,20,23-Octaaz… | L | CNCCNCCNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_7252 | 2,5,8,11,14,17,20,23,26-Non… | L | CNCCNCCNCCNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_7236 | 2,5,8,11-Tetraazadodecane | L | CNCCNCCNCCNC | 1 | 1 | 25 | 0.5 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_7249 | 2,5,8,11,14,17-Hexaazaoctad… | L | CNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_7250 | 2,5,8,11,14,17,20-Heptaazah… | L | CNCCNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_26 | Cd^[2+] | ligand_7253 | 2,5,8,11,14,17,20,23,26,29-… | L | CNCCNCCNCCNCCNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_26 | Cd^[2+] | ligand_7251 | 2,5,8,11,14,17,20,23-Octaaz… | L | CNCCNCCNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_26 | Cd^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_26 | Cd^[2+] | ligand_7252 | 2,5,8,11,14,17,20,23,26-Non… | L | CNCCNCCNCCNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_26 | Cd^[2+] | ligand_7249 | 2,5,8,11,14,17-Hexaazaoctad… | L | CNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_7251 | 2,5,8,11,14,17,20,23-Octaaz… | L | CNCCNCCNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_26 | Cd^[2+] | ligand_7250 | 2,5,8,11,14,17,20-Heptaazah… | L | CNCCNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_7249 | 2,5,8,11,14,17-Hexaazaoctad… | L | CNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 1 | 1 | 25 | 1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_7250 | 2,5,8,11,14,17,20-Heptaazah… | L | CNCCNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 0 |

### logK — 30 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_41 | Cu^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 3 | 1 | 25~37 | 0.1~1 | *** | 3 |
| metal_112 | Ni^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 3 | 1 | 25 | 0.1~1 | *** | 3 |
| metal_71 | Hg^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 3 | 1 | 25 | 0.1~1 | *** | 3 |
| metal_26 | Cd^[2+] | ligand_7253 | 2,5,8,11,14,17,20,23,26,29-… | L | CNCCNCCNCCNCCNCCNCCNCCNCCNCCNC | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_7253 | 2,5,8,11,14,17,20,23,26,29-… | L | CNCCNCCNCCNCCNCCNCCNCCNCCNCCNC | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_7251 | 2,5,8,11,14,17,20,23-Octaaz… | L | CNCCNCCNCCNCCNCCNCCNCCNC | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_127 | Pd^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 2 | 1 | 25 | 0.1~1 | *** | 2 |
| metal_41 | Cu^[2+] | ligand_7252 | 2,5,8,11,14,17,20,23,26-Non… | L | CNCCNCCNCCNCCNCCNCCNCCNCCNC | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_7251 | 2,5,8,11,14,17,20,23-Octaaz… | L | CNCCNCCNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_7252 | 2,5,8,11,14,17,20,23,26-Non… | L | CNCCNCCNCCNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_7236 | 2,5,8,11-Tetraazadodecane | L | CNCCNCCNCCNC | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_7249 | 2,5,8,11,14,17-Hexaazaoctad… | L | CNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_7250 | 2,5,8,11,14,17,20-Heptaazah… | L | CNCCNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_7251 | 2,5,8,11,14,17,20,23-Octaaz… | L | CNCCNCCNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_7252 | 2,5,8,11,14,17,20,23,26-Non… | L | CNCCNCCNCCNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_7249 | 2,5,8,11,14,17-Hexaazaoctad… | L | CNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_7250 | 2,5,8,11,14,17,20-Heptaazah… | L | CNCCNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_7249 | 2,5,8,11,14,17-Hexaazaoctad… | L | CNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_7250 | 2,5,8,11,14,17,20-Heptaazah… | L | CNCCNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_7253 | 2,5,8,11,14,17,20,23,26,29-… | L | CNCCNCCNCCNCCNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_21 | Bi^[3+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_21 | Bi^[3+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_7175 | N,N'-Dipropylethylenediamine | L | CCCNCCNCCC | 1 | 1 | 25 | 0.7 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_7220 | 3,6,9-Triazaundecane dinitr… | L | N#CCCNCCNCCNCCC#N | 1 | 1 | 25 | 0.5 | *** | 1 |

---

### Step 29: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND (c.ligand_name_SRD LIKE '%propionitrile%' OR c.ligand_name_SRD LIKE '%benzonitrile%') AND (s.solvent_name LIKE '%water%' OR s.solvent_name IS NULL) AND (s.temperature_c BETWEEN 293 AND 303))",
  "order_by": "s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability — 100 row(s)

### ΔS — 34 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 8 | 2 | 25 | 0~1 | *** | 0 |
| metal_68 | H^[+] | ligand_7246 | 1,4,7,10,13,16-Hexaazahexad… | L | NCCNCCNCCNCCNCCN | 7 | 2 | 25 | 0~1 | *** | 0 |
| metal_68 | H^[+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 4 | 2 | 25 | 0.1~1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 3 | 2 | 25 | 0.1~1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 2 | 1 | 25 | 0.1~1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 2 | 1 | 25 | 0.1~1 | *** | 0 |
| metal_26 | Cd^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 2 | 1 | 25 | 0.1~1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_7253 | 2,5,8,11,14,17,20,23,26,29-… | L | CNCCNCCNCCNCCNCCNCCNCCNCCNCCNC | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 2 | 1 | 25 | 0.1~1 | *** | 0 |
| metal_68 | H^[+] | ligand_7236 | 2,5,8,11-Tetraazadodecane | L | CNCCNCCNCCNC | 2 | 2 | 25 | 0.5 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_7251 | 2,5,8,11,14,17,20,23-Octaaz… | L | CNCCNCCNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_7252 | 2,5,8,11,14,17,20,23,26-Non… | L | CNCCNCCNCCNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_7236 | 2,5,8,11-Tetraazadodecane | L | CNCCNCCNCCNC | 1 | 1 | 25 | 0.5 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_7249 | 2,5,8,11,14,17-Hexaazaoctad… | L | CNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_7250 | 2,5,8,11,14,17,20-Heptaazah… | L | CNCCNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_26 | Cd^[2+] | ligand_7253 | 2,5,8,11,14,17,20,23,26,29-… | L | CNCCNCCNCCNCCNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_26 | Cd^[2+] | ligand_7251 | 2,5,8,11,14,17,20,23-Octaaz… | L | CNCCNCCNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_26 | Cd^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_26 | Cd^[2+] | ligand_7252 | 2,5,8,11,14,17,20,23,26-Non… | L | CNCCNCCNCCNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_26 | Cd^[2+] | ligand_7249 | 2,5,8,11,14,17-Hexaazaoctad… | L | CNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_7251 | 2,5,8,11,14,17,20,23-Octaaz… | L | CNCCNCCNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_26 | Cd^[2+] | ligand_7250 | 2,5,8,11,14,17,20-Heptaazah… | L | CNCCNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_7249 | 2,5,8,11,14,17-Hexaazaoctad… | L | CNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 1 | 1 | 25 | 1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_7250 | 2,5,8,11,14,17,20-Heptaazah… | L | CNCCNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 0 |

### logK — 30 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_41 | Cu^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 3 | 1 | 25~37 | 0.1~1 | *** | 3 |
| metal_112 | Ni^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 3 | 1 | 25 | 0.1~1 | *** | 3 |
| metal_71 | Hg^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 3 | 1 | 25 | 0.1~1 | *** | 3 |
| metal_26 | Cd^[2+] | ligand_7253 | 2,5,8,11,14,17,20,23,26,29-… | L | CNCCNCCNCCNCCNCCNCCNCCNCCNCCNC | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_7253 | 2,5,8,11,14,17,20,23,26,29-… | L | CNCCNCCNCCNCCNCCNCCNCCNCCNCCNC | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_7251 | 2,5,8,11,14,17,20,23-Octaaz… | L | CNCCNCCNCCNCCNCCNCCNCCNC | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_127 | Pd^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 2 | 1 | 25 | 0.1~1 | *** | 2 |
| metal_41 | Cu^[2+] | ligand_7252 | 2,5,8,11,14,17,20,23,26-Non… | L | CNCCNCCNCCNCCNCCNCCNCCNCCNC | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_7251 | 2,5,8,11,14,17,20,23-Octaaz… | L | CNCCNCCNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_7252 | 2,5,8,11,14,17,20,23,26-Non… | L | CNCCNCCNCCNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_7236 | 2,5,8,11-Tetraazadodecane | L | CNCCNCCNCCNC | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_7249 | 2,5,8,11,14,17-Hexaazaoctad… | L | CNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_7250 | 2,5,8,11,14,17,20-Heptaazah… | L | CNCCNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_7251 | 2,5,8,11,14,17,20,23-Octaaz… | L | CNCCNCCNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_7252 | 2,5,8,11,14,17,20,23,26-Non… | L | CNCCNCCNCCNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_7249 | 2,5,8,11,14,17-Hexaazaoctad… | L | CNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_7250 | 2,5,8,11,14,17,20-Heptaazah… | L | CNCCNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_7249 | 2,5,8,11,14,17-Hexaazaoctad… | L | CNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_7250 | 2,5,8,11,14,17,20-Heptaazah… | L | CNCCNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_7253 | 2,5,8,11,14,17,20,23,26,29-… | L | CNCCNCCNCCNCCNCCNCCNCCNCCNCCNC | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_21 | Bi^[3+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_21 | Bi^[3+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_7175 | N,N'-Dipropylethylenediamine | L | CCCNCCNCCC | 1 | 1 | 25 | 0.7 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_7220 | 3,6,9-Triazaundecane dinitr… | L | N#CCCNCCNCCNCCC#N | 1 | 1 | 25 | 0.5 | *** | 1 |

---

### Step 30: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_62 AND (c.ligand_name_SRD LIKE '%1,4-dioxane%' OR c.ligand_name_SRD LIKE '%1,2-dimethoxyethane%' OR c.ligand_name_SRD LIKE '%diglyme%') AND (s.solvent_name LIKE '%water%' OR s.solvent_name IS NULL) AND (s.temperature_c BETWEEN 293 AND 303))",
  "order_by": "s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability

*(no results)*

---

### Step 31: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND (c.ligand_name_SRD LIKE '%1,4-dioxane%' OR c.ligand_name_SRD LIKE '%1,2-dimethoxyethane%' OR c.ligand_name_SRD LIKE '%diglyme%') AND (s.solvent_name LIKE '%water%' OR s.solvent_name IS NULL) AND (s.temperature_c BETWEEN 293 AND 303))",
  "order_by": "s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability

*(no results)*

---

### Step 32: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_62 AND (c.ligand_name_SRD LIKE '%diethylene glycol%' OR c.ligand_name_SRD LIKE '%1,2-propanediol%' OR c.ligand_name_SRD LIKE '%glycerol%') AND (s.solvent_name LIKE '%water%' OR s.solvent_name IS NULL) AND (s.temperature_c BETWEEN 293 AND 303))",
  "order_by": "s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability — 100 row(s)

### ΔS — 9 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 4 | 2 | 25 | 0~0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_7583 | 1,4,7,13-Tetraoxa-10,16-dia… | L | C1COCCNCCOCCOCCOCCN1 | 2 | 2 | 25 | 0 | *** | 0 |
| metal_68 | H^[+] | ligand_7546 | Perhydro-1,4-oxazine (Morph… | L | C1COCCN1 | 2 | 1 | 25 | 0~0.5 | *** | 0 |
| metal_2 | Ag^[+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_26 | Cd^[2+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.5 | *** | 0 |
| metal_18 | Ba^[2+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_177 | Sr^[2+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 0 |

### logK — 47 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_7546 | Perhydro-1,4-oxazine (Morph… | L | C1COCCN1 | 5 | 1 | 10~25 | 0~1 | *** | 5 |
| metal_41 | Cu^[2+] | ligand_7649 | 1,4,16,19-Tetraoxa-7,10,13,… | L | C1CNCCNCCOCCOCCNCCNCCNCCOCCOCCNCCN1 | 5 | 5 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_7648 | 1,4,16,19-Tetraoxa-7,10,13,… | L | C1CNCCOCCOCCNCCNCCNCCOCCOCCNCCN1 | 5 | 5 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_7648 | 1,4,16,19-Tetraoxa-7,10,13,… | L | C1CNCCOCCOCCNCCNCCNCCOCCOCCNCCN1 | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_7648 | 1,4,16,19-Tetraoxa-7,10,13,… | L | C1CNCCOCCOCCNCCNCCNCCOCCOCCNCCN1 | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_7649 | 1,4,16,19-Tetraoxa-7,10,13,… | L | C1CNCCNCCOCCOCCNCCNCCNCCOCCOCCNCCN1 | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_7648 | 1,4,16,19-Tetraoxa-7,10,13,… | L | C1CNCCOCCOCCNCCNCCNCCOCCOCCNCCN1 | 4 | 2 | 25~35 | 0.1 | *** | 3 |
| metal_68 | H^[+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 3 | 1 | 25 | 0~0.5 | *** | 3 |
| metal_33 | Co^[2+] | ligand_7648 | 1,4,16,19-Tetraoxa-7,10,13,… | L | C1CNCCOCCOCCNCCNCCNCCOCCOCCNCCN1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_7614 | 1,4-Dioxa-7,10,13-triazacyc… | L | C1CNCCOCCOCCNCCN1 | 3 | 2 | 25~35 | 0.1 | *** | 2 |
| metal_208 | Zn^[2+] | ligand_7648 | 1,4,16,19-Tetraoxa-7,10,13,… | L | C1CNCCOCCOCCNCCNCCNCCOCCOCCNCCN1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_7614 | 1,4-Dioxa-7,10,13-triazacyc… | L | C1CNCCOCCOCCNCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_7649 | 1,4,16,19-Tetraoxa-7,10,13,… | L | C1CNCCNCCOCCOCCNCCNCCNCCOCCOCCNCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_7642 | 1,4-Dioxa-7,10,13,16,19-pen… | L | C1CNCCNCCOCCOCCNCCNCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_7648 | 1,4,16,19-Tetraoxa-7,10,13,… | L | C1CNCCOCCOCCNCCNCCNCCOCCOCCNCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_7620 | 1,4-Dioxa-7,10,13,16-tetraa… | L | C1CNCCNCCOCCOCCNCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_7614 | 1,4-Dioxa-7,10,13-triazacyc… | L | C1CNCCOCCOCCNCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_7583 | 1,4,7,13-Tetraoxa-10,16-dia… | L | C1COCCNCCOCCOCCOCCN1 | 1 | 1 | 25 | 0 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_7620 | 1,4-Dioxa-7,10,13,16-tetraa… | L | C1CNCCNCCOCCOCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_7579 | 1,4,10-Trioxa-7,13-diazacyc… | L | C1COCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_7642 | 1,4-Dioxa-7,10,13,16,19-pen… | L | C1CNCCNCCOCCOCCNCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7579 | 1,4,10-Trioxa-7,13-diazacyc… | L | C1COCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_64 | Ga^[3+] | ligand_7579 | 1,4,10-Trioxa-7,13-diazacyc… | L | C1COCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_64 | Ga^[3+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_7642 | 1,4-Dioxa-7,10,13,16,19-pen… | L | C1CNCCNCCOCCOCCNCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_7642 | 1,4-Dioxa-7,10,13,16,19-pen… | L | C1CNCCNCCOCCOCCNCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_7620 | 1,4-Dioxa-7,10,13,16-tetraa… | L | C1CNCCNCCOCCOCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_7642 | 1,4-Dioxa-7,10,13,16,19-pen… | L | C1CNCCNCCOCCOCCNCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7573 | 1,7-Dioxa-4,10-diazacyclodo… | L | C1COCCNCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_7614 | 1,4-Dioxa-7,10,13-triazacyc… | L | C1CNCCOCCOCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_7614 | 1,4-Dioxa-7,10,13-triazacyc… | L | C1CNCCOCCOCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_7620 | 1,4-Dioxa-7,10,13,16-tetraa… | L | C1CNCCNCCOCCOCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_7620 | 1,4-Dioxa-7,10,13,16-tetraa… | L | C1CNCCNCCOCCOCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_5 | Al^[3+] | ligand_7579 | 1,4,10-Trioxa-7,13-diazacyc… | L | C1COCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_5 | Al^[3+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_7573 | 1,7-Dioxa-4,10-diazacyclodo… | L | C1COCCNCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_7573 | 1,7-Dioxa-4,10-diazacyclodo… | L | C1COCCNCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_37 | Cr^[3+] | ligand_7579 | 1,4,10-Trioxa-7,13-diazacyc… | L | C1COCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_37 | Cr^[3+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_7614 | 1,4-Dioxa-7,10,13-triazacyc… | L | C1CNCCOCCOCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_7620 | 1,4-Dioxa-7,10,13,16-tetraa… | L | C1CNCCNCCOCCOCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7614 | 1,4-Dioxa-7,10,13-triazacyc… | L | C1CNCCOCCOCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_7572 | 1,4-Dioxa-7,10-diazacyclodo… | L | C1CNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_7579 | 1,4,10-Trioxa-7,13-diazacyc… | L | C1COCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_7573 | 1,7-Dioxa-4,10-diazacyclodo… | L | C1COCCNCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |

---

### Step 33: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_61 AND (c.ligand_name_SRD LIKE '%diethylene glycol%' OR c.ligand_name_SRD LIKE '%1,2-propanediol%' OR c.ligand_name_SRD LIKE '%glycerol%') AND (s.solvent_name LIKE '%water%' OR s.solvent_name IS NULL) AND (s.temperature_c BETWEEN 293 AND 303))",
  "order_by": "s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability — 100 row(s)

### ΔS — 9 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 4 | 2 | 25 | 0~0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_7583 | 1,4,7,13-Tetraoxa-10,16-dia… | L | C1COCCNCCOCCOCCOCCN1 | 2 | 2 | 25 | 0 | *** | 0 |
| metal_68 | H^[+] | ligand_7546 | Perhydro-1,4-oxazine (Morph… | L | C1COCCN1 | 2 | 1 | 25 | 0~0.5 | *** | 0 |
| metal_2 | Ag^[+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_26 | Cd^[2+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_125 | Pb^[2+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.5 | *** | 0 |
| metal_18 | Ba^[2+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_177 | Sr^[2+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 0 |

### logK — 47 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_7546 | Perhydro-1,4-oxazine (Morph… | L | C1COCCN1 | 5 | 1 | 10~25 | 0~1 | *** | 5 |
| metal_41 | Cu^[2+] | ligand_7649 | 1,4,16,19-Tetraoxa-7,10,13,… | L | C1CNCCNCCOCCOCCNCCNCCNCCOCCOCCNCCN1 | 5 | 5 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_7648 | 1,4,16,19-Tetraoxa-7,10,13,… | L | C1CNCCOCCOCCNCCNCCNCCOCCOCCNCCN1 | 5 | 5 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_7648 | 1,4,16,19-Tetraoxa-7,10,13,… | L | C1CNCCOCCOCCNCCNCCNCCOCCOCCNCCN1 | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_7648 | 1,4,16,19-Tetraoxa-7,10,13,… | L | C1CNCCOCCOCCNCCNCCNCCOCCOCCNCCN1 | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_7649 | 1,4,16,19-Tetraoxa-7,10,13,… | L | C1CNCCNCCOCCOCCNCCNCCNCCOCCOCCNCCN1 | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_7648 | 1,4,16,19-Tetraoxa-7,10,13,… | L | C1CNCCOCCOCCNCCNCCNCCOCCOCCNCCN1 | 4 | 2 | 25~35 | 0.1 | *** | 3 |
| metal_68 | H^[+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 3 | 1 | 25 | 0~0.5 | *** | 3 |
| metal_33 | Co^[2+] | ligand_7648 | 1,4,16,19-Tetraoxa-7,10,13,… | L | C1CNCCOCCOCCNCCNCCNCCOCCOCCNCCN1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_7614 | 1,4-Dioxa-7,10,13-triazacyc… | L | C1CNCCOCCOCCNCCN1 | 3 | 2 | 25~35 | 0.1 | *** | 2 |
| metal_208 | Zn^[2+] | ligand_7648 | 1,4,16,19-Tetraoxa-7,10,13,… | L | C1CNCCOCCOCCNCCNCCNCCOCCOCCNCCN1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_7614 | 1,4-Dioxa-7,10,13-triazacyc… | L | C1CNCCOCCOCCNCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_7649 | 1,4,16,19-Tetraoxa-7,10,13,… | L | C1CNCCNCCOCCOCCNCCNCCNCCOCCOCCNCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_7642 | 1,4-Dioxa-7,10,13,16,19-pen… | L | C1CNCCNCCOCCOCCNCCNCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_7648 | 1,4,16,19-Tetraoxa-7,10,13,… | L | C1CNCCOCCOCCNCCNCCNCCOCCOCCNCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_7620 | 1,4-Dioxa-7,10,13,16-tetraa… | L | C1CNCCNCCOCCOCCNCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_7614 | 1,4-Dioxa-7,10,13-triazacyc… | L | C1CNCCOCCOCCNCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_7583 | 1,4,7,13-Tetraoxa-10,16-dia… | L | C1COCCNCCOCCOCCOCCN1 | 1 | 1 | 25 | 0 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_7620 | 1,4-Dioxa-7,10,13,16-tetraa… | L | C1CNCCNCCOCCOCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_7579 | 1,4,10-Trioxa-7,13-diazacyc… | L | C1COCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_7642 | 1,4-Dioxa-7,10,13,16,19-pen… | L | C1CNCCNCCOCCOCCNCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7579 | 1,4,10-Trioxa-7,13-diazacyc… | L | C1COCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_64 | Ga^[3+] | ligand_7579 | 1,4,10-Trioxa-7,13-diazacyc… | L | C1COCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_64 | Ga^[3+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_7642 | 1,4-Dioxa-7,10,13,16,19-pen… | L | C1CNCCNCCOCCOCCNCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_7642 | 1,4-Dioxa-7,10,13,16,19-pen… | L | C1CNCCNCCOCCOCCNCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_7620 | 1,4-Dioxa-7,10,13,16-tetraa… | L | C1CNCCNCCOCCOCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_7642 | 1,4-Dioxa-7,10,13,16,19-pen… | L | C1CNCCNCCOCCOCCNCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7573 | 1,7-Dioxa-4,10-diazacyclodo… | L | C1COCCNCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_7614 | 1,4-Dioxa-7,10,13-triazacyc… | L | C1CNCCOCCOCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_7614 | 1,4-Dioxa-7,10,13-triazacyc… | L | C1CNCCOCCOCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_7620 | 1,4-Dioxa-7,10,13,16-tetraa… | L | C1CNCCNCCOCCOCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_7620 | 1,4-Dioxa-7,10,13,16-tetraa… | L | C1CNCCNCCOCCOCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_5 | Al^[3+] | ligand_7579 | 1,4,10-Trioxa-7,13-diazacyc… | L | C1COCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_5 | Al^[3+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_7573 | 1,7-Dioxa-4,10-diazacyclodo… | L | C1COCCNCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_7573 | 1,7-Dioxa-4,10-diazacyclodo… | L | C1COCCNCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_37 | Cr^[3+] | ligand_7579 | 1,4,10-Trioxa-7,13-diazacyc… | L | C1COCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_37 | Cr^[3+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_7614 | 1,4-Dioxa-7,10,13-triazacyc… | L | C1CNCCOCCOCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_7620 | 1,4-Dioxa-7,10,13,16-tetraa… | L | C1CNCCNCCOCCOCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7614 | 1,4-Dioxa-7,10,13-triazacyc… | L | C1CNCCOCCOCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_7572 | 1,4-Dioxa-7,10-diazacyclodo… | L | C1CNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_7579 | 1,4,10-Trioxa-7,13-diazacyc… | L | C1COCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_7573 | 1,7-Dioxa-4,10-diazacyclodo… | L | C1COCCNCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |

---
