# Q5.2.4 — Tool Results (batch 5)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "plutonium",
  "limit": 50
}
```

[summary]
## search_metals — 4 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_148 | Pu^[3+] | Pu | 3 | ✓ | [Pu+3] | InChI=1S/Pu/q+3 | beta_totN_7 | ligand_totN_12 | vlm_totN_28 |
| metal_149 | Pu^[4+] | Pu | 4 | ✓ | [Pu+4] | InChI=1S/Pu/q+4 | beta_totN_6 | ligand_totN_11 | vlm_totN_36 |
| metal_150 | PuO_[2]^[2+] | Pu | 2 |  | *** | *** | beta_totN_10 | ligand_totN_22 | vlm_totN_76 |
| metal_151 | PuO_[2]^[+] | Pu | 1 |  | *** | *** | beta_totN_2 | ligand_totN_6 | vlm_totN_6 |

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "acetylsalicylic",
  "limit": 50
}
```

[summary]
## search_ligands — 2 result(s)

**stats:** 2 SQL matches · showing 2 · limit 50

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8701 | 2-Acetoxybenzoic acid (Acetylsalicylic acid) | HL | Carboxylic acids keto | 5 | `CC(=O)Oc1ccccc1C(=O)O` | (-inf, HL, 3.45, L, +inf) |
| ligand_10913 | Acetylsalicylic acid (Aspirin) | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| aromatic_ring | 1 | 100% |
| carboxyl | 1 | 100% |
| ester | 1 | 100% |

---

### Step 5: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_149",
  "ligand_id": "ligand_8701"
}
```

[summary]
[CATALOG]
## build_system_catalog

*(no pairs found)*

**summary:** {'n_metals': 0, 'n_ligands': 0, 'n_pairs': 0, 'total_species': 0}

---

### Step 7: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_149 AND (c.ligand_name_SRD LIKE '%acetylsalicy%' OR c.ligand_name_SRD LIKE '%aspirin%' OR c.ligand_name_SRD LIKE '%acetylsalicylate%' OR c.ligand_name_SRD LIKE '%2-acetoxybenzoate%' OR c.ligand_name_SRD LIKE '%o-acetoxybenzoate%'))",
  "limit": 200
}
```

[summary]
## search_stability — 200 row(s)

### logK — 64 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 25 | 2 | 10~40 | 0~3 | *** | 14 |
| metal_41 | Cu^[2+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 10 | 3 | 25 | 0~2 | *** | 5 |
| metal_195 | UO_[2]^[2+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 7 | 3 | 25 | 0.1~1 | *** | 3 |
| metal_33 | Co^[2+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 6 | 2 | 25 | 0~2 | *** | 5 |
| metal_112 | Ni^[2+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 6 | 2 | 25 | 0~2 | *** | 5 |
| metal_25 | Ca^[2+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 5 | 2 | 25 | 0~0.1 | *** | 3 |
| metal_185 | Th^[4+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_201 | VO^[2+] | ligand_8636 | 2-Hydroxybenzoic acid 2-(di… | H4L | O=C(O)c1ccccc1OP(=O)(O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_19 | Be^[2+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 3 | 3 | 25 | 0.5 | *** | 1 |
| metal_68 | H^[+] | ligand_8636 | 2-Hydroxybenzoic acid 2-(di… | H4L | O=C(O)c1ccccc1OP(=O)(O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_8701 | 2-Acetoxybenzoic acid (Acet… | HL | CC(=O)Oc1ccccc1C(=O)O | 2 | 2 | 37 | 0.15 | *** | 1 |
| metal_68 | H^[+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 2 | 1 | 25 | 0~0.1 | *** | 2 |
| metal_80 | Li^[+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 2 | 1 | 25~37 | 0~0.15 | *** | 2 |
| metal_106 | Na^[+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 2 | 1 | 25~37 | 0~0.15 | *** | 2 |
| metal_78 | K^[+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 2 | 1 | 25~37 | 0~0.15 | *** | 2 |
| metal_111 | NH_[4]^[+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 2 | 1 | 25 | 0~0.1 | *** | 2 |
| metal_18 | Ba^[2+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 2 | 1 | 25 | 0~0.1 | *** | 2 |
| metal_79 | La^[3+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 2 | 1 | 25 | 0~0.1 | *** | 2 |
| metal_185 | Th^[4+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 2 | 2 | 20 | 1 | *** | 1 |
| metal_118 | NpO_[2]^[+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 2 | 1 | 20~25 | 1 | *** | 2 |
| metal_94 | Mn^[2+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 2 | 1 | 25 | 0~0.1 | *** | 2 |
| metal_68 | H^[+] | ligand_8530 | 2-Methylbenzoic acid | HL | Cc1ccccc1C(=O)O | 1 | 1 | 25 | 0 | *** | 1 |
| metal_68 | H^[+] | ligand_8701 | 2-Acetoxybenzoic acid (Acet… | HL | CC(=O)Oc1ccccc1C(=O)O | 1 | 1 | 37 | 0.15 | *** | 1 |
| metal_92 | Mg^[2+] | ligand_8701 | 2-Acetoxybenzoic acid (Acet… | HL | CC(=O)Oc1ccccc1C(=O)O | 1 | 1 | 37 | 0.15 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_8701 | 2-Acetoxybenzoic acid (Acet… | HL | CC(=O)Oc1ccccc1C(=O)O | 1 | 1 | 37 | 0.15 | *** | 1 |
| metal_205 | Y^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_139 | Pr^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_110 | Nd^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_173 | Sm^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_58 | Eu^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_65 | Gd^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_179 | Tb^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_44 | Dy^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_73 | Ho^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_55 | Er^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_192 | Tm^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_206 | Yb^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_81 | Lu^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_125 | Pb^[2+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_68 | H^[+] | ligand_8761 | 2-Phenoxybenzoic acid | HL | O=C(O)c1ccccc1Oc1ccccc1 | 1 | 1 | 25 | 0 | *** | 1 |
| metal_68 | H^[+] | ligand_8765 | 2,3-Dimethoxybenzoic acid | HL | COc1cccc(C(=O)O)c1OC | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_92 | Mg^[2+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 1 | 1 | 25 | 0 | *** | 1 |
| metal_177 | Sr^[2+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 1 | 1 | 25 | 0 | *** | 1 |
| metal_205 | Y^[3+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_139 | Pr^[3+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_110 | Nd^[3+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_173 | Sm^[3+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_58 | Eu^[3+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_65 | Gd^[3+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_179 | Tb^[3+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_44 | Dy^[3+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_73 | Ho^[3+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_55 | Er^[3+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_192 | Tm^[3+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_206 | Yb^[3+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_81 | Lu^[3+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_150 | PuO_[2]^[2+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_36 | Cr^[2+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 1 | 1 | 25 | 1 | *** | 1 |
| metal_201 | VO^[2+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |

### ΔH — 24 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 4 | 2 | 25 | 0~0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 4 | 3 | 25 | 0~0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_8636 | 2-Hydroxybenzoic acid 2-(di… | H4L | O=C(O)c1ccccc1OP(=O)(O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 2 | 1 | 25 | 0~0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_8530 | 2-Methylbenzoic acid | HL | Cc1ccccc1C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_205 | Y^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_139 | Pr^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_110 | Nd^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_173 | Sm^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_58 | Eu^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_65 | Gd^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_179 | Tb^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_44 | Dy^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_73 | Ho^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_55 | Er^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_192 | Tm^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_206 | Yb^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_81 | Lu^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_106 | Na^[+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_78 | K^[+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_33 | Co^[2+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |

### ΔS — 24 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 4 | 2 | 25 | 0~0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 4 | 3 | 25 | 0~0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_8636 | 2-Hydroxybenzoic acid 2-(di… | H4L | O=C(O)c1ccccc1OP(=O)(O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 2 | 1 | 25 | 0~0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_8530 | 2-Methylbenzoic acid | HL | Cc1ccccc1C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_205 | Y^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_139 | Pr^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_110 | Nd^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_173 | Sm^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_58 | Eu^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_65 | Gd^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_179 | Tb^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_44 | Dy^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_73 | Ho^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_55 | Er^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_192 | Tm^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_206 | Yb^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_81 | Lu^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_106 | Na^[+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_78 | K^[+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_33 | Co^[2+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_149 AND (c.ligand_name_SRD LIKE '%salicylate%' OR c.ligand_name_SRD LIKE '%2-hydroxybenzoate%'))",
  "limit": 200
}
```

[summary]
## search_stability — 200 row(s)

### logK — 39 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 15 | 2 | 10~40 | 0~3 | *** | 10 |
| metal_195 | UO_[2]^[2+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 10 | 3 | 20~30 | 0~0.7 | *** | 6 |
| metal_19 | Be^[2+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 9 | 7 | 25 | 0.1~1 | *** | 2 |
| metal_41 | Cu^[2+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 8 | 2 | 25~37 | 0.1~1 | *** | 5 |
| metal_92 | Mg^[2+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 5 | 2 | 25~37 | 0~0.5 | *** | 4 |
| metal_25 | Ca^[2+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 5 | 2 | 25~37 | 0~0.5 | *** | 4 |
| metal_185 | Th^[4+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_79 | La^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 3 | 2 | 25 | 0~0.1 | *** | 2 |
| metal_33 | Co^[2+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 3 | 2 | 20~25 | 0.1 | *** | 2 |
| metal_112 | Ni^[2+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 3 | 2 | 20~25 | 0.1 | *** | 2 |
| metal_68 | H^[+] | ligand_8143 | 8-Hydroxyquinoline-2-carbox… | HL | COC(=O)c1ccc2cccc(O)c2n1 | 2 | 1 | 25 | 0~0.1 | *** | 2 |
| metal_68 | H^[+] | ligand_8637 | 2-Carboxy-6-(methoxycarbony… | H3L | COC(=O)c1cccc(C(=O)O)c1OP(=O)(O)O | 2 | 2 | 35 | 0.1 | *** | 1 |
| metal_18 | Ba^[2+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 1 | 25 | 0~0.1 | *** | 2 |
| metal_139 | Pr^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_110 | Nd^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_173 | Sm^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_58 | Eu^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_65 | Gd^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_179 | Tb^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_44 | Dy^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_73 | Ho^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_55 | Er^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_192 | Tm^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_206 | Yb^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_81 | Lu^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_36 | Cr^[2+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 25 | 3 | *** | 1 |
| metal_94 | Mn^[2+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_199 | V^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 27 | 1 | *** | 1 |
| metal_68 | H^[+] | ligand_6945 | 2-Aminobenzoic acid methyl … | L | COC(=O)c1ccccc1N | 1 | 1 | 25 | 0 | *** | 1 |
| metal_68 | H^[+] | ligand_8017 | Pyridine-2-carboxylic acid … | L | COC(=O)c1ccccn1 | 1 | 1 | 22 | 0 | *** | 1 |
| metal_94 | Mn^[2+] | ligand_8143 | 8-Hydroxyquinoline-2-carbox… | HL | COC(=O)c1ccc2cccc(O)c2n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_8143 | 8-Hydroxyquinoline-2-carbox… | HL | COC(=O)c1ccc2cccc(O)c2n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_112 | Ni^[2+] | ligand_8143 | 8-Hydroxyquinoline-2-carbox… | HL | COC(=O)c1ccc2cccc(O)c2n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_8143 | 8-Hydroxyquinoline-2-carbox… | HL | COC(=O)c1ccc2cccc(O)c2n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_106 | Na^[+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_78 | K^[+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_118 | NpO_[2]^[+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 1 | 1 | 25 | 2 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |

### ΔH — 20 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 13 | 2 | 10~40 | 0~3 | *** | 0 |
| metal_79 | La^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_139 | Pr^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_110 | Nd^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_173 | Sm^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_58 | Eu^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_65 | Gd^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_179 | Tb^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_44 | Dy^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_73 | Ho^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_55 | Er^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_192 | Tm^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_206 | Yb^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_81 | Lu^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_199 | V^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 25 | 1 | *** | 0 |
| metal_68 | H^[+] | ligand_6945 | 2-Aminobenzoic acid methyl … | L | COC(=O)c1ccccc1N | 1 | 1 | 25 | 0 | *** | 0 |
| metal_19 | Be^[2+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_92 | Mg^[2+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 1 | 1 | 25 | 0.5 | *** | 0 |

### ΔS — 20 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_68 | H^[+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 8 | 2 | 25 | 0~3 | *** | 0 |
| metal_79 | La^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_139 | Pr^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_110 | Nd^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_173 | Sm^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_58 | Eu^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_65 | Gd^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_179 | Tb^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_44 | Dy^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_73 | Ho^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_55 | Er^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_192 | Tm^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_206 | Yb^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_81 | Lu^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_199 | V^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 27 | 1 | *** | 0 |
| metal_68 | H^[+] | ligand_6945 | 2-Aminobenzoic acid methyl … | L | COC(=O)c1ccccc1N | 1 | 1 | 25 | 0 | *** | 0 |
| metal_19 | Be^[2+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_92 | Mg^[2+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 1 | 1 | 25 | 0.5 | *** | 0 |

---
