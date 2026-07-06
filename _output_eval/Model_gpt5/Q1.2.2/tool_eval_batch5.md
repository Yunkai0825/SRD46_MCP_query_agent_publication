# Q1.2.2 — Tool Results (batch 5)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "cadmium",
  "symbol": "Cd",
  "limit": 10
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_26 | Cd^[2+] | Cd | 2 | ✓ | [Cd+2] | InChI=1S/Cd/q+2 | beta_totN_95 | ligand_totN_818 | vlm_totN_2828 |

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "chloride",
  "limit": 25
}
```

[summary]
## search_ligands — 12 result(s)

**stats:** 12 SQL matches · showing 12 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5923 | L-[1-Carboxy-2-(4-hydroxypheny… (Tyrosine betaine) | H2L | Amino Acids | 1 | `C[N+](C)(C)C(Cc1ccc(O)cc1)C(=O)O.[Cl-]` | (-inf, HL, 9.63, L, +inf) |
| ligand_5947 | DL-[1-Carboxy-2-(2-mercapto-4-imi… (Ergothioneine) | H2L | Amino Acids | 4 | `C[N+](C)(C)C(Cc1cnc(S)[nH]1)C(=O)O.[Cl-]` | (-inf, HL, 10.44, L, +inf) |
| ligand_6769 | 3-Carboxy-N-methylpyridi… (Nicotinic acid betaine) | HL | Pyridine carboxylic acids | 1 | `C[n+]1cccc(C(=O)O)c1` | (-inf, HL, 2.04, L, +inf) |
| ligand_7954 | 3-Hydroxy-N-methylpyridinium (chloride) | HL | Pyridines (azines) | 3 | `C[n+]1cccc(O)c1` | (-inf, HL, 4.81, L, +inf) |
| ligand_7968 | 3-Hydroxy-N,2,5-… (Deoxypyridoxal N-methochloride) | HL | Pyridines (azines) | 2 | `Cc1c[n+](C)c(C)c(O)c1C=O` | (-inf, HL, 4.34, L, 4.34, H-1L, +inf) |
| ligand_8251 | 3-[(4-Amino-2-methyl-5-pyrimidinyl)met… (Thiamine) | L | Pyrimidines | 1 | `Cc1ncc(C[n+]2csc(CCO)c2C)c(N)n1` | (-inf, HL, 4.79, L, +inf) |
| ligand_9333 | 3-Hydroxyphenyltrimethylammonium (chloride) | HL | Phenols | 3 | `C[N+](C)(C)c1cccc(O)c1` | (-inf, HL, 8.06, L, +inf) |
| ligand_9334 | 4-Hydroxyphenyltrimethylammonium (chloride) | HL | Phenols | 3 | `C[N+](C)(C)c1ccc(O)cc1` | (-inf, HL, 8.35, L, +inf) |
| ligand_10163 | Chloride ion | *** | Inorganic ligands | 546 | *** | *** |
| ligand_10207 | DL-(3-Amino-3-carbo… (S-Methylmethionine chloride) | *** | Ligands not selected | 0 | *** | *** |
| ligand_11318 | 3-Chloropropene (Allyl chloride) | *** | Ligands not selected | 0 | *** | *** |
| ligand_11394 | Methyl(dimethyl)(dimethylglyoxime)ammonium chlori… | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (8 parseable SMILES)

| group | count | % |
|-------|-------|---|
| aromatic_ring | 8 | 100% |
| hydroxyl | 6 | 75% |
| carboxyl | 3 | 38% |
| phenol | 3 | 38% |
| pyridine | 3 | 38% |
| halide | 2 | 25% |
| aldehyde | 1 | 12% |
| primary_amine | 1 | 12% |
| thiazole | 1 | 12% |
| thioether | 1 | 12% |
| thiol | 1 | 12% |

---

### Step 4: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_26",
  "ligand_id": "ligand_10163"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 3 species

### Cd^[2+] + Chloride ion
**metal_id:** metal_26 | **ligand_id:** ligand_10163 | **ligand_def_HxL:** ***  
**entries:** 30 | **species:** 3 | **vlm_count:** 30

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 11 |
| beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | [M] + [L]^2 <=> [ML2] | [ML2](aqueous), [M](aqueous), [L](aqueous) | 10 |
| beta_def_872 | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | [M] + [L]^3 <=> [ML3] | [ML3](aqueous), [M](aqueous), [L](aqueous) | 9 |

**vlm_ids:** vlm_177542, vlm_177543, vlm_177544, vlm_177545, vlm_177546, … vlm_177569, vlm_177570, vlm_177571 (30 listed)

**equilibrium_maps:** 7 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_29910 | 3 | 3 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_29911 | 3 | 3 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_29912 | 3 | 3 | 19~29 °C | 1.85~2.15 M |
| ref_eq_net_29913 | 3 | 3 | 19~29 °C | 2.85~3.15 M |
| ref_eq_net_29914 | 3 | 3 | 19~29 °C | 3.85~4.15 M |
| ref_eq_net_29915 | 2 | 1 | 19~29 °C | 0.35~0.65 M |
| ref_eq_net_29916 | 1 | 0 | 19~29 °C | -0.15~0.15 M |

---
