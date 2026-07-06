# Q5.1.3 — Tool Results (batch 1)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "iron(II), iron(III), copper(I), copper(II)",
  "limit": 20
}
```

[summary]
## search_metals

*(no results)*

---

### Step 3: `search_metals`
**Args:**
```json
{
  "name": "iron, copper",
  "symbol": "Fe, Cu",
  "limit": 20
}
```

[summary]
## search_metals

*(no results)*

---

### Step 5: `get_table_schema`
**Args:**
```json
{
  "table_name": "metal_card",
  "database": "cards"
}
```

[summary]
## get_table_schema - 16 column(s)

| cid | name | type | notnull | pk |
|-----|------|------|---------|----|
| 0 | metal_id | INTEGER | False | True |
| 1 | metal_name_SRD | TEXT | True | False |
| 2 | symbol_pure | TEXT | False | False |
| 3 | charge | INTEGER | False | False |
| 4 | charge_str | TEXT | False | False |
| 5 | SMILES | TEXT | False | False |
| 6 | InChi | TEXT | False | False |
| 7 | InChiKey | TEXT | False | False |
| 8 | parts_used_json | TEXT | False | False |
| 9 | stoichiometry_json | TEXT | False | False |
| 10 | is_simple_ion | INTEGER | False | False |
| 11 | is_organometallic | INTEGER | False | False |
| 12 | primary_metal | TEXT | False | False |
| 13 | formula_components_json | TEXT | False | False |
| 14 | parse_notes | TEXT | False | False |
| 15 | created_at | TIMESTAMP | False | False |

---

### Step 6: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_card",
  "group_column": "metal_id",
  "limit": 20
}
```

[summary]
## db_distribution - ligandmetal_card by metal_id

**total_rows:** 79063

| value | count | pct |
|-------|-------|-----|
| 68 | 20720 | 26.21% |
| 41 | 8963 | 11.34% |
| 112 | 5325 | 6.74% |
| 208 | 4095 | 5.18% |
| 33 | 2977 | 3.77% |
| 2 | 2885 | 3.65% |
| 26 | 2828 | 3.58% |
| 25 | 1761 | 2.23% |
| 125 | 1585 | 2.0% |
| 61 | 1473 | 1.86% |
| 92 | 1422 | 1.8% |
| 94 | 1273 | 1.61% |
| 71 | 1097 | 1.39% |
| 79 | 931 | 1.18% |
| 65 | 897 | 1.13% |
| 58 | 870 | 1.1% |
| 173 | 844 | 1.07% |
| 110 | 794 | 1.0% |
| 5 | 792 | 1.0% |
| 55 | 792 | 1.0% |

---

### Step 7: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT metal_id, metal_name_SRD, symbol_pure, charge, charge_str, primary_metal, is_simple_ion FROM metal_card WHERE symbol_pure IN ('Fe','Cu') OR primary_metal IN ('Fe','Cu') ORDER BY symbol_pure, charge;"
}
```

[summary]
## execute_srd46_sql - 5 row(s)

| metal_id | metal_name_SRD | symbol_pure | charge | charge_str | primary_metal | is_simple_ion |
|----------|----------------|-------------|--------|------------|---------------|---------------|
| metal_42 | Cu^[+] | Cu | 1 | + | Cu | 1 |
| metal_41 | Cu^[2+] | Cu | 2 | 2+ | Cu | 1 |
| metal_43 | Cu^[3+] | Cu | 3 | 3+ | Cu | 1 |
| metal_62 | Fe^[2+] | Fe | 2 | 2+ | Fe | 1 |
| metal_61 | Fe^[3+] | Fe | 3 | 3+ | Fe | 1 |

---

### Step 8: `inspect_card`
**Args:**
```json
{
  "prefix_id": "metal_41"
}
```

[summary]
## inspect_card — Metal | metal_41

**Name:** Cu^[2+]  
**Symbol:** Cu | **Charge:** 2  
**SMILES:** `[Cu+2]`  
**InChI:** `InChI=1S/Cu/q+2`  
**Flags:** simple-ion  

**Partners:** 1951 ligand(s), 8963 measurement(s) total

| ligand_id | Ligand | # meas |
|-----------|--------|--------|
| ligand_5898 | L-2-Amino-3-(4-imidazolyl)propanoic acid (Histidine) | 50 |
| ligand_10103 | Ammonia | 49 |
| ligand_7795 | 1,3-Diazole (Imidazole) | 42 |
| ligand_7172 | N,N'-Dimethylethylenediamine | 39 |
| ligand_8465 | Ethanoic acid (Acetic acid) | 37 |
| … | *(showing top 5 of 1951)* | |

### Functional groups across all ligand partners (1852 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 875 | 47% |
| aromatic_ring | 736 | 40% |
| primary_amine | 640 | 35% |
| hydroxyl | 585 | 32% |
| amide | 487 | 26% |
| secondary_amine | 439 | 24% |
| tertiary_amine | 423 | 23% |
| pyridine | 211 | 11% |
| phenol | 169 | 9% |
| ether | 165 | 9% |
| thioether | 139 | 8% |
| phosphonate | 104 | 6% |
| imine | 58 | 3% |
| phosphate | 52 | 3% |
| sulfonate | 52 | 3% |
| halide | 47 | 3% |
| ketone | 36 | 2% |
| ester | 23 | 1% |
| oxime | 21 | 1% |
| aldehyde | 18 | 1% |
| thiazole | 7 | 0% |
| imidazole | 6 | 0% |
| pyrazole | 6 | 0% |
| nitrile | 5 | 0% |

---

### Step 9: `inspect_card`
**Args:**
```json
{
  "prefix_id": "metal_68"
}
```

[summary]
## inspect_card — Metal | metal_68

**Name:** H^[+]  
**Symbol:** H | **Charge:** 1  
**SMILES:** `[H+]`  
**InChI:** `InChI=1S/p+1`  
**Flags:** simple-ion  

**Partners:** 4081 ligand(s), 20720 measurement(s) total

| ligand_id | Ligand | # meas |
|-----------|--------|--------|
| ligand_10077 | Hydrogen vanadate (Vanadic acid) | 92 |
| ligand_10113 | Hydrogen phosphate (Phosphoric acid) | 84 |
| ligand_6277 | Ethylenedinitrilotetraacetic acid (EDTA) | 75 |
| ligand_7246 | 1,4,7,10,13,16-Hexaazahexadecane (Pentaethy… (2,2,2,2,2-hex) | 72 |
| ligand_6165 | Nitrilotriacetic acid (NTA) | 72 |
| … | *(showing top 5 of 4081)* | |

### Functional groups across all ligand partners (3910 parseable SMILES)

| group | count | % |
|-------|-------|---|
| aromatic_ring | 1851 | 47% |
| carboxyl | 1646 | 42% |
| hydroxyl | 1390 | 36% |
| primary_amine | 1070 | 27% |
| tertiary_amine | 802 | 21% |
| amide | 738 | 19% |
| secondary_amine | 691 | 18% |
| phenol | 458 | 12% |
| pyridine | 425 | 11% |
| halide | 266 | 7% |
| ether | 262 | 7% |
| thioether | 247 | 6% |
| sulfonate | 193 | 5% |
| phosphonate | 176 | 5% |
| thiol | 111 | 3% |
| imine | 104 | 3% |
| phosphate | 97 | 2% |
| ester | 92 | 2% |
| ketone | 88 | 2% |
| oxime | 48 | 1% |
| aldehyde | 42 | 1% |
| nitrile | 30 | 1% |
| thiazole | 10 | 0% |
| imidazole | 8 | 0% |
| pyrazole | 8 | 0% |
| carboxylate | 1 | 0% |

---

### Step 10: `inspect_card`
**Args:**
```json
{
  "prefix_id": "metal_61"
}
```

[summary]
## inspect_card — Metal | metal_61

**Name:** Fe^[3+]  
**Symbol:** Fe | **Charge:** 3  
**SMILES:** `[Fe+3]`  
**InChI:** `InChI=1S/Fe/q+3`  
**Flags:** simple-ion  

**Partners:** 406 ligand(s), 1473 measurement(s) total

| ligand_id | Ligand | # meas |
|-----------|--------|--------|
| ligand_10092 | Hydrogen thiocyanate (Thiocyanic acid) | 39 |
| ligand_10076 | Hydroxide ion | 38 |
| ligand_10106 | Hydrogen azide (Hydrazoic acid) | 22 |
| ligand_9358 | 1,2-Dihydroxybenzene-3,5-disulfonic acid (Tiron) | 16 |
| ligand_8465 | Ethanoic acid (Acetic acid) | 16 |
| … | *(showing top 5 of 406)* | |

### Functional groups across all ligand partners (367 parseable SMILES)

| group | count | % |
|-------|-------|---|
| hydroxyl | 264 | 72% |
| aromatic_ring | 185 | 50% |
| carboxyl | 166 | 45% |
| phenol | 106 | 29% |
| tertiary_amine | 91 | 25% |
| amide | 84 | 23% |
| pyridine | 40 | 11% |
| primary_amine | 38 | 10% |
| secondary_amine | 34 | 9% |
| halide | 31 | 8% |
| sulfonate | 28 | 8% |
| ether | 24 | 7% |
| phosphonate | 21 | 6% |
| ketone | 12 | 3% |
| nitrile | 9 | 2% |
| thioether | 7 | 2% |
| aldehyde | 4 | 1% |
| imine | 4 | 1% |
| ester | 3 | 1% |
| phosphate | 3 | 1% |
| oxime | 2 | 1% |
| thiol | 2 | 1% |

---

### Step 11: `inspect_card`
**Args:**
```json
{
  "prefix_id": "metal_62"
}
```

[summary]
## inspect_card — Metal | metal_62

**Name:** Fe^[2+]  
**Symbol:** Fe | **Charge:** 2  
**SMILES:** `[Fe+2]`  
**InChI:** `InChI=1S/Fe/q+2`  
**Flags:** simple-ion  

**Partners:** 217 ligand(s), 667 measurement(s) total

| ligand_id | Ligand | # meas |
|-----------|--------|--------|
| ligand_10103 | Ammonia | 32 |
| ligand_5760 | Aminoacetic acid (Glycine) | 14 |
| ligand_10076 | Hydroxide ion | 13 |
| ligand_5828 | L-2-Amino-3-hydroxypropanoic acid (Serine) | 12 |
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) | 11 |
| … | *(showing top 5 of 217)* | |

### Functional groups across all ligand partners (211 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 123 | 58% |
| aromatic_ring | 68 | 32% |
| tertiary_amine | 67 | 32% |
| hydroxyl | 49 | 23% |
| pyridine | 44 | 21% |
| primary_amine | 42 | 20% |
| secondary_amine | 41 | 19% |
| ether | 25 | 12% |
| thioether | 14 | 7% |
| amide | 13 | 6% |
| imine | 11 | 5% |
| phosphonate | 10 | 5% |
| phenol | 8 | 4% |
| oxime | 7 | 3% |
| sulfonate | 5 | 2% |
| thiol | 5 | 2% |
| halide | 4 | 2% |
| ketone | 3 | 1% |
| phosphate | 2 | 1% |
| thiazole | 2 | 1% |
| ester | 1 | 0% |
| imidazole | 1 | 0% |
| nitrile | 1 | 0% |
| pyrazole | 1 | 0% |

---

### Step 12: `inspect_card`
**Args:**
```json
{
  "prefix_id": "metal_42"
}
```

[summary]
## inspect_card — Metal | metal_42

**Name:** Cu^[+]  
**Symbol:** Cu | **Charge:** 1  
**SMILES:** `[Cu+]`  
**InChI:** `InChI=1S/Cu/q+1`  
**Flags:** simple-ion  

**Partners:** 117 ligand(s), 285 measurement(s) total

| ligand_id | Ligand | # meas |
|-----------|--------|--------|
| ligand_10090 | Hydrogen cyanide (Hydrocyanic acid) | 15 |
| ligand_10163 | Chloride ion | 14 |
| ligand_10171 | Iodide ion | 8 |
| ligand_10168 | Bromide ion | 7 |
| ligand_10103 | Ammonia | 6 |
| … | *(showing top 5 of 117)* | |

### Functional groups across all ligand partners (89 parseable SMILES)

| group | count | % |
|-------|-------|---|
| aromatic_ring | 35 | 39% |
| primary_amine | 27 | 30% |
| carboxyl | 25 | 28% |
| secondary_amine | 24 | 27% |
| pyridine | 19 | 21% |
| hydroxyl | 10 | 11% |
| thioether | 8 | 9% |
| amide | 5 | 6% |
| imine | 5 | 6% |
| sulfonate | 5 | 6% |
| tertiary_amine | 3 | 3% |
| thiol | 3 | 3% |
| ketone | 2 | 2% |
| nitrile | 2 | 2% |
| halide | 1 | 1% |
| oxime | 1 | 1% |
| phosphate | 1 | 1% |

---

### Step 13: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_41, metal_42, metal_61, metal_62) AND c.ligand_id IN (ligand_10103, ligand_9058, ligand_5760) AND s.temperature_c BETWEEN 24 AND 26)",
  "order_by": "c.ligand_id, c.metal_id, s.constant_value DESC",
  "limit": 200
}
```

[summary]
## search_stability — 148 row(s)

### ΔS — 6 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_41 | Cu^[2+] | ligand_10103 | Ammonia | L | N | 16 | 4 | 25 | 0~3 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 5 | 5 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 4 | 2 | 25 | 0~0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_10103 | Ammonia | L | N | 4 | 4 | 25 | 2 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |

### logK — 10 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_62 | Fe^[2+] | ligand_10103 | Ammonia | L | N | 24 | 4 | 25 | 0~6 | *** | 6 |
| metal_41 | Cu^[2+] | ligand_10103 | Ammonia | L | N | 17 | 4 | 25 | 0~3 | *** | 5 |
| metal_41 | Cu^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 12 | 2 | 25 | 0~2.5 | *** | 6 |
| metal_41 | Cu^[2+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 9 | 5 | 25 | 0.1 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 7 | 3 | 25 | 0~3 | *** | 4 |
| metal_61 | Fe^[3+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 6 | 3 | 25 | 0.5~3 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 5 | 3 | 25 | 0.1~1 | *** | 3 |
| metal_62 | Fe^[2+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 3 | 2 | 25 | 0.1~3 | *** | 2 |
| metal_42 | Cu^[+] | ligand_10103 | Ammonia | L | N | 2 | 1 | 25 | 0.5~2 | *** | 2 |
| metal_42 | Cu^[+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |

### ΔH — 6 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_41 | Cu^[2+] | ligand_10103 | Ammonia | L | N | 16 | 4 | 25 | 0~3 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 5 | 5 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 4 | 2 | 25 | 0~0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_10103 | Ammonia | L | N | 4 | 4 | 25 | 2 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |

---

### Step 14: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_41, metal_42, metal_61, metal_62) AND c.ligand_id = ligand_10163)",
  "order_by": "c.metal_id, s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability — 48 row(s)

### `Cu^[2+]` + Chloride ion — 19 measurement(s)
metal_id: metal_41 | ligand_id: ligand_10163
ligand_HxL_def: *** | ligand_SMILES: ***

| equation | type | vlm_counts | ref_eq_map | value_range | T°C_range | I(M)_range | beta_defs | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|----------|------|------------|------------|-------------|-----------|------------|-----------|--------------------|--------------|-------------|
| `[M] + [L] <=> [ML]` | ΔS | 3 | *** | 25.1~46 | 25 | 2~5 | beta_def_812 | *** | [L] |  |
| `[M] + [L] <=> [ML]` | ΔH | 3 | *** | 8.4~12.1 | 25 | 2~5 | beta_def_812 | *** | [L] |  |
| `[M] + [L] <=> [ML]` | logK | 9 | 9 diff ref_eq_map | -0.2~0.27 | 25 | 0~6 | beta_def_812 | *** | [L] |  |
| * | ΔS | 1 | *** | 0 | 25 | 0 | beta_def_280 | *** |  |  |
| * | logK | 2 | ref_eq_map_29722; ref_eq_map_29723 | -17.3~-17.16 | 25 | 0~1 | beta_def_280 | *** |  |  |
| * | ΔH | 1 | *** | -37.7 | 25 | 0 | beta_def_280 | *** |  |  |

Summary stats
| type | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|------|------------|-------------|-----------|------------|--------------------|-------------------|
| ΔS | 4 | 2 | 25 | 0~5 | *** | 0 |
| ΔH | 4 | 2 | 25 | 0~5 | *** | 0 |
| logK | 11 | 2 | 25 | 0~6 | *** | 9 |

### `Cu^[+]` + Chloride ion — 14 measurement(s)
metal_id: metal_42 | ligand_id: ligand_10163
ligand_HxL_def: *** | ligand_SMILES: ***

| equation | type | vlm_counts | ref_eq_map | value_range | T°C_range | I(M)_range | beta_defs | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|----------|------|------------|------------|-------------|-----------|------------|-----------|--------------------|--------------|-------------|
| `[M]^2 + [L]^4 <=> [M2L4]` | logK | 1 | ref_eq_map_29751 | 13 | 25 | 5 | beta_def_548 | *** | [L] |  |
| `[M] + [L]^2 <=> [ML2]` | logK | 4 | 4 diff ref_eq_map | 5.42~6.06 | 20~25 | 0~5 | beta_def_840 | *** | [L] |  |
| `[M] + [L] <=> [ML]` | logK | 2 | ref_eq_map_29750; ref_eq_map_29751 | 2.7~3.1 | 25 | 0~5 | beta_def_812 | *** | [L] |  |
| `[ML2] + [L] <=> [ML3]` | logK | 3 | ref_eq_map_29750; ref_eq_map_29751; ref_eq_map_29752 | -0.67~-0.12 | 25 | 0~5 | beta_def_888 | *** | [L] |  |
| `[ML(s)] <=> [M] + [L]` | logK | 2 | ref_eq_map_29750; ref_eq_map_29751 | -7.38~-6.73 | 25 | 0~5 | beta_def_311 | solid | [L] |  |
| `[ML2] + [L] <=> [ML3]` | ΔH | 1 | *** | -20.1 | 25 | 5 | beta_def_888 | *** | [L] |  |
| `[ML2] + [L] <=> [ML3]` | ΔS | 1 | *** | -69.9 | 25 | 5 | beta_def_888 | *** | [L] |  |

Summary stats
| type | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|------|------------|-------------|-----------|------------|--------------------|-------------------|
| logK | 12 | 5 | 20~25 | 0~5 | solid | 4 |
| ΔH | 1 | 1 | 25 | 5 | *** | 0 |
| ΔS | 1 | 1 | 25 | 5 | *** | 0 |

### `Fe^[3+]` + Chloride ion — 13 measurement(s)
metal_id: metal_61 | ligand_id: ligand_10163
ligand_HxL_def: *** | ligand_SMILES: ***

| equation | type | vlm_counts | ref_eq_map | value_range | T°C_range | I(M)_range | beta_defs | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|----------|------|------------|------------|-------------|-----------|------------|-----------|--------------------|--------------|-------------|
| `[M] + [L] <=> [ML]` | ΔS | 2 | *** | 71.1~108.8 | 25 | 0~1 | beta_def_812 | *** | [L] |  |
| `[M] + [L] <=> [ML]` | ΔH | 2 | *** | 18~23.4 | 25 | 0~1 | beta_def_812 | *** | [L] |  |
| `[M] + [L]^2 <=> [ML2]` | logK | 2 | ref_eq_map_29736; ref_eq_map_29737 | 0.75~2.13 | 25 | 0~1 | beta_def_840 | *** | [L] |  |
| `[M] + [L] <=> [ML]` | logK | 7 | 7 diff ref_eq_map | 0.63~1.48 | 25 | 0~4 | beta_def_812 | *** | [L] |  |

Summary stats
| type | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|------|------------|-------------|-----------|------------|--------------------|-------------------|
| ΔS | 2 | 1 | 25 | 0~1 | *** | 0 |
| ΔH | 2 | 1 | 25 | 0~1 | *** | 0 |
| logK | 9 | 2 | 25 | 0~4 | *** | 7 |

### `Fe^[2+]` + Chloride ion — 2 measurement(s)
metal_id: metal_62 | ligand_id: ligand_10163
ligand_HxL_def: *** | ligand_SMILES: ***

| equation | type | vlm_counts | ref_eq_map | value_range | T°C_range | I(M)_range | beta_defs | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|----------|------|------------|------------|-------------|-----------|------------|-----------|--------------------|--------------|-------------|
| `[M] + [L] <=> [ML]` | logK | 1 | ref_eq_map_29714 | -0.2 | 25 | 0 | beta_def_812 | *** | [L] |  |
| `[ML2(s)] <=> [M] + [L]^2` | ΔH | 1 | *** | -82.8 | 25 | 0 | beta_def_334 | solid | [L] |  |

Summary stats
| type | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|------|------------|-------------|-----------|------------|--------------------|-------------------|
| logK | 1 | 1 | 25 | 0 | *** | 1 |
| ΔH | 1 | 1 | 25 | 0 | solid | 0 |

---
