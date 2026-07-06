# Q5.2.4 — Tool Results (batch 2)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "plutonium"
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
  "name": "aspirin"
}
```

[summary]
## search_ligands — 2 result(s)

**stats:** 2 SQL matches · showing 2 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_10895 | 2-(Acetylthio)benzoic acid (thioaspirin) | *** | Ligands not selected | 0 | *** | *** |
| ligand_10913 | Acetylsalicylic acid (Aspirin) | *** | Ligands not selected | 0 | *** | *** |

---

### Step 4: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_149",
  "ligand_id": "ligand_10913"
}
```

[summary]
[CATALOG]
## build_system_catalog

*(no pairs found)*

**summary:** {'n_metals': 0, 'n_ligands': 0, 'n_pairs': 0, 'total_species': 0}

---

### Step 6: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_149 AND c.ligand_id = ligand_10913)"
}
```

[summary]
## search_stability

*(no results)*

---

### Step 7: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_10913"
}
```

[summary]
## inspect_card — Ligand | ligand_10913

**Name:** Acetylsalicylic acid (Aspirin)  
**Formula:** ******** | **Class:** Ligands not selected  

**pKa values:** none

**Partners:** 0 metal(s), 0 measurement(s) total

*(no metal partners)*

---

### Step 8: `search_ligands`
**Args:**
```json
{
  "name": "salicylic acid"
}
```

[summary]
## search_ligands — 25 result(s)

**stats:** 43 SQL matches · showing 25 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8701 | 2-Acetoxybenzoic acid (Acetylsalicylic acid) | HL | Carboxylic acids keto | 5 | `CC(=O)Oc1ccccc1C(=O)O` | (-inf, HL, 3.45, L, +inf) |
| ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | H2L | Phenols salicylic acids | 227 | `O=C(O)c1ccccc1O` | (-inf, H2L, 2.8, HL, 2.8, L, +inf) |
| ligand_9265 | 2-Hydroxy-3-methylbenzoic acid (3-Methylsalicylic… | H2L | Phenols salicylic acids | 9 | `Cc1cccc(C(=O)O)c1O` | (-inf, H2L, 2.83, HL, 2.83, L, +inf) |
| ligand_9266 | 2-Hydroxy-4-methylbenzoic acid (4-Methylsalicylic… | H2L | Phenols salicylic acids | 8 | `Cc1ccc(C(=O)O)c(O)c1` | (-inf, H2L, 2.96, HL, 2.96, L, +inf) |
| ligand_9267 | 2-Hydroxy-5-methylbenzoic acid (5-Methylsalicylic… | H2L | Phenols salicylic acids | 6 | `Cc1ccc(O)c(C(=O)O)c1` | (-inf, H2L, 2.88, HL, 2.88, L, +inf) |
| ligand_9268 | 2-Hydroxy-6-methylbenzoi… (6-Methylsalicylic acid) | H2L | Phenols salicylic acids | 5 | `Cc1cccc(O)c1C(=O)O` | (-inf, H2L, 3.16, HL, +inf) |
| ligand_9269 | 2-Hydroxy-3-(2-propyl… (3-Isopropylsalicylic acid) | H2L | Phenols salicylic acids | 2 | `CC(C)c1cccc(C(=O)O)c1O` | (-inf, H2L, 2.76, HL, +inf) |
| ligand_9274 | 5-Fluoro-2-hydroxybenzoi… (5-Fluorosalicylic acid) | H2L | Phenols salicylic acids | 3 | `O=C(O)c1cc(F)ccc1O` | (-inf, H2L, 2.56, HL, 2.56, L, +inf) |
| ligand_9275 | 5-Chloro-2-hydroxybenzoi… (5-Chlorosalicylic acid) | H2L | Phenols salicylic acids | 19 | `O=C(O)c1cc(Cl)ccc1O` | (-inf, H2L, 2.46, HL, 2.46, L, +inf) |
| ligand_9276 | 6-Chloro-2-hydroxybenzoi… (6-Chlorosalicylic acid) | H2L | Phenols salicylic acids | 1 | `O=C(O)c1c(O)cccc1Cl` | (-inf, H2L, 2.63, HL, +inf) |
| ligand_9277 | 5-Bromo-2-hydroxybenzoic … (5-Bromosalicylic acid) | H2L | Phenols salicylic acids | 11 | `O=C(O)c1cc(Br)ccc1O` | (-inf, H2L, 2.44, HL, 2.44, L, +inf) |
| ligand_9278 | 2-Hydroxy-5-iodobenzoic ac… (5-Iodosalicylic acid) | H2L | Phenols salicylic acids | 10 | `O=C(O)c1cc(I)ccc1O` | (-inf, H2L, -2.54, HL, -2.54, L, +inf) |
| ligand_9279 | 2-Hydroxy-3-nitrobenzoic … (3-Nitrosalicylic acid) | H2L | Phenols salicylic acids | 14 | `O=C(O)c1cccc([N+](=O)[O-])c1O` | (-inf, H2L, -1.73, HL, 9.87, L, +inf) |
| ligand_9280 | 2-Hydroxy-4-nitrobenzoic … (4-Nitrosalicylic acid) | H2L | Phenols salicylic acids | 4 | `O=C(O)c1ccc([N+](=O)[O-])cc1O` | (-inf, H2L, 2.05, HL, 10.91, L, +inf) |
| ligand_9281 | 2-Hydroxy-5-nitrobenzoic … (5-Nitrosalicylic acid) | H2L | Phenols salicylic acids | 36 | `O=C(O)c1cc([N+](=O)[O-])ccc1O` | (-inf, H2L, -1.94, HL, 9.9, L, +inf) |
| ligand_9282 | 2-Hydroxy-6-nitrobenzoic … (6-Nitrosalicylic acid) | H2L | Phenols salicylic acids | 4 | `O=C(O)c1c(O)cccc1[N+](=O)[O-]` | (-inf, H2L, 1.99, HL, 9.04, L, +inf) |
| ligand_9283 | 2-Hydroxy-3,5-dinitro… (3,5-Dinitrosalicylic acid) | H2L | Phenols salicylic acids | 35 | `O=C(O)c1cc([N+](=O)[O-])cc([N+](=O)[O-])c1O` | (-inf, H2L, -0.3, HL, 7.07, L, +inf) |
| ligand_9284 | 2-Hydroxy-5-sulfobenzoic … (5-Sulfosalicylic acid) | H3L | Phenols salicylic acids | 127 | `O=C(O)c1cc(S(=O)(=O)O)ccc1O` | (-inf, H2L, 2.48, HL, 11.85, L, +inf) |
| ligand_9285 | 3-Bromo-2-hydroxy… (3-Bromo-5-sulfosalicylic acid) | H3L | Phenols salicylic acids | 89 | `O=C(O)c1cc(S(=O)(=O)O)cc(Br)c1O` | (-inf, H2L, 2.02, HL, 10.52, L, +inf) |
| ligand_9287 | 2-Hydroxy-3,5-disulfo… (3,5-Disulfosalicylic acid) | H4L | Phenols salicylic acids | 51 | `O=C(O)c1cc(S(=O)(=O)O)cc(S(=O)(=O)O)c1O` | (-inf, H2L, 2.03, HL, 2.03, L, +inf) |
| ligand_9288 | 2-Hydroxy-3-methoxybenz… (3-Methoxysalicylic acid) | H2L | Phenols salicylic acids | 3 | `COc1cccc(C(=O)O)c1O` | (-inf, H2L, 2.69, HL, 2.69, L, +inf) |
| ligand_9289 | 2-Hydroxy-5-methoxybenz… (5-Methoxysalicylic acid) | H2L | Phenols salicylic acids | 3 | `COc1ccc(O)c(C(=O)O)c1` | (-inf, H2L, 2.92, HL, 2.92, L, +inf) |
| ligand_9296 | 2-Hydroxy-5-cyanobenzoic … (5-Cyanosalicylic acid) | H2L | Phenols salicylic acids | 3 | `N#Cc1ccc(O)c(C(=O)O)c1` | (-inf, H2L, 2.36, HL, 2.36, L, +inf) |
| ligand_9297 | 4-Amino-2-hydroxybenzoic … (p-Aminosalicylic acid) | H2L | Phenols salicylic acids | 31 | `Nc1ccc(C(=O)O)c(O)c1` | (-inf, H3L, -1.8, H2L, 3.63, HL, +inf) |
| ligand_9298 | 5-Amino-2-hydroxybenzoic … (m-Aminosalicylic acid) | H2L | Phenols salicylic acids | 18 | `Nc1ccc(O)c(C(=O)O)c1` | (-inf, H3L, 2.28, H2L, 2.28, HL, -5.6, L, +inf) |

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

### Step 9: `search_citations`
**Args:**
```json
{
  "where": "(la.citation LIKE '%aspirin%' OR la.citation LIKE '%acetylsalicyl%')"
}
```

[summary]
## search_citations

*(no results)*

---

### Step 10: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_149 AND c.ligand_id = ligand_8701)"
}
```

[summary]
## search_stability

*(no results)*

---

### Step 11: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_149 AND c.ligand_id = ligand_9257)"
}
```

[summary]
## search_stability

*(no results)*

---

### Step 12: `build_system_catalog`
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

### Step 13: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_8701"
}
```

[summary]
## inspect_card — Ligand | ligand_8701

**Name:** 2-Acetoxybenzoic acid (Acetylsalicylic acid)  
**Formula:** C9H8O4 | **Class:** Carboxylic acids keto  
**SMILES:** `CC(=O)Oc1ccccc1C(=O)O`  
**InChI:** `InChI=1S/C9H8O4/c1-6(10)13-8-5-3-2-4-7(8)9(11)12/h2-5H,1H3,(H,11,12)`  
**HxL definition:** HL  

**pKa values:** 1

| source_vlm | pKa | T (°C) | I (M) | From → To | Solvent | Method | Quality |
|------------|-----|--------|-------|-----------|---------|--------|---------|
| vlm_149911 | 3.45 | 37.0 | 0.15 | L → HL | *** | *** | *** |

**Partners:** 4 metal(s), 5 measurement(s) total

| metal_id | Metal | # meas |
|----------|-------|--------|
| metal_41 | Cu^[2+] | 2 |
| metal_92 | Mg^[2+] | 1 |
| metal_68 | H^[+] | 1 |
| metal_25 | Ca^[2+] | 1 |

---

### Step 14: `inspect_card`
**Args:**
```json
{
  "prefix_id": "metal_149"
}
```

[summary]
## inspect_card — Metal | metal_149

**Name:** Pu^[4+]  
**Symbol:** Pu | **Charge:** 4  
**SMILES:** `[Pu+4]`  
**InChI:** `InChI=1S/Pu/q+4`  
**Flags:** simple-ion  

**Partners:** 11 ligand(s), 36 measurement(s) total

| ligand_id | Ligand | # meas |
|-----------|--------|--------|
| ligand_10109 | Nitrate ion | 9 |
| ligand_10076 | Hydroxide ion | 5 |
| ligand_10162 | Hydrogen fluoride (Hydrofluoric acid) | 4 |
| ligand_10148 | Hydrogen sulfate ion (Sulfuric acid) | 4 |
| ligand_9526 | Pentane-2,4-dione (Acetylacetone) | 4 |
| … | *(showing top 5 of 11)* | |

### Functional groups across all ligand partners (6 parseable SMILES)

| group | count | % |
|-------|-------|---|
| hydroxyl | 3 | 50% |
| carboxyl | 2 | 33% |
| sulfonate | 2 | 33% |
| halide | 1 | 17% |
| primary_amine | 1 | 17% |
| tertiary_amine | 1 | 17% |

---
