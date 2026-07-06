# Q5.1.6 — Tool Results (batch 5)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Lanthanum, Cerium, Praseodymium, Neodymium, Samarium, Europium, Gadolinium, Terbium, Dysprosium, Holmium, Erbium, Thulium, Ytterbium, Lutetium, Yttrium, Scandium",
  "limit": 50
}
```

[summary]
## search_metals

*(no results)*

---

### Step 4: `search_metals`
**Args:**
```json
{
  "symbol": "La, Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, Y, Sc",
  "limit": 50
}
```

[summary]
## search_metals

*(no results)*

---

### Step 5: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_card",
  "group_column": "metal_name_SRD",
  "limit": 50
}
```

[summary]
## db_distribution - ligandmetal_card by metal_name_SRD

**total_rows:** 79063

| value | count | pct |
|-------|-------|-----|
| H^[+] | 20720 | 26.21% |
| Cu^[2+] | 8963 | 11.34% |
| Ni^[2+] | 5325 | 6.74% |
| Zn^[2+] | 4095 | 5.18% |
| Co^[2+] | 2977 | 3.77% |
| Ag^[+] | 2885 | 3.65% |
| Cd^[2+] | 2828 | 3.58% |
| Ca^[2+] | 1761 | 2.23% |
| Pb^[2+] | 1585 | 2.0% |
| Fe^[3+] | 1473 | 1.86% |
| Mg^[2+] | 1422 | 1.8% |
| Mn^[2+] | 1273 | 1.61% |
| Hg^[2+] | 1097 | 1.39% |
| La^[3+] | 931 | 1.18% |
| Gd^[3+] | 897 | 1.13% |
| Eu^[3+] | 870 | 1.1% |
| Sm^[3+] | 844 | 1.07% |
| Nd^[3+] | 794 | 1.0% |
| Er^[3+] | 792 | 1.0% |
| Al^[3+] | 792 | 1.0% |
| Sr^[2+] | 784 | 0.99% |
| Yb^[3+] | 771 | 0.98% |
| Dy^[3+] | 758 | 0.96% |
| Ba^[2+] | 749 | 0.95% |
| UO_[2]^[2+] | 748 | 0.95% |
| Pr^[3+] | 723 | 0.91% |
| Tb^[3+] | 709 | 0.9% |
| Ho^[3+] | 705 | 0.89% |
| Lu^[3+] | 671 | 0.85% |
| Fe^[2+] | 667 | 0.84% |
| Tm^[3+] | 633 | 0.8% |
| Ce^[3+] | 567 | 0.72% |
| Y^[3+] | 533 | 0.67% |
| Th^[4+] | 476 | 0.6% |
| Be^[2+] | 443 | 0.56% |
| In^[3+] | 433 | 0.55% |
| Ga^[3+] | 428 | 0.54% |
| VO^[2+] | 364 | 0.46% |
| Na^[+] | 335 | 0.42% |
| K^[+] | 335 | 0.42% |
| Cu^[+] | 285 | 0.36% |
| Bi^[3+] | 283 | 0.36% |
| Tl^[+] | 272 | 0.34% |
| Pd^[2+] | 245 | 0.31% |
| Li^[+] | 216 | 0.27% |
| B^[3+] | 195 | 0.25% |
| Am^[3+] | 190 | 0.24% |
| Me_[2]Sn^[2+] | 165 | 0.21% |
| Sc^[3+] | 156 | 0.2% |
| MeHg^[+] | 148 | 0.19% |

---

### Step 6: `db_ranked_pairs`
**Args:**
```json
{
  "rank_by": "measurement_count",
  "limit": 100
}
```

[summary]
**db_ranked_pairs:** Error - Unknown rank_by='measurement_count'. Choose from: ['ligands_per_metal', 'measurements_per_ligand', 'measurements_per_metal', 'metals_per_ligand', 'pka_per_ligand']

---

### Step 7: `db_ranked_pairs`
**Args:**
```json
{
  "rank_by": "measurements_per_ligand",
  "limit": 50
}
```

[summary]
## db_ranked_pairs - measurements_per_ligand

| ligand_id | name | count |
|-----------|------|-------|
| ligand_10076 | Hydroxide ion | 953 |
| ligand_10162 | Hydrogen fluoride (Hydrofluoric acid) | 642 |
| ligand_6277 | Ethylenedinitrilotetraacetic acid (EDTA) | 596 |
| ligand_10148 | Hydrogen sulfate ion (Sulfuric acid) | 581 |
| ligand_8465 | Ethanoic acid (Acetic acid) | 562 |
| ligand_10163 | Chloride ion | 546 |
| ligand_6165 | Nitrilotriacetic acid (NTA) | 534 |
| ligand_8873 | Propanedioic acid (Malonic acid) | 505 |
| ligand_10103 | Ammonia | 447 |
| ligand_10092 | Hydrogen thiocyanate (Thiocyanic acid) | 434 |
| ligand_5760 | Aminoacetic acid (Glycine) | 428 |
| ligand_8640 | Hydroxyacetic acid (Glycolic acid) | 402 |
| ligand_8872 | Ethanedioic acid (Oxalic acid) | 394 |
| ligand_10168 | Bromide ion | 391 |
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) | 384 |
| ligand_6127 | Iminodiacetic acid (IDA) | 375 |
| ligand_8974 | Oxydiacetic acid (Diglycolic acid) | 363 |
| ligand_10113 | Hydrogen phosphate (Phosphoric acid) | 359 |
| ligand_8641 | D-2-Hydroxypropanoic acid (Lactic acid) | 349 |
| ligand_9526 | Pentane-2,4-dione (Acetylacetone) | 345 |
| ligand_10096 | Hydrogen carbonate (Carbonic acid) | 335 |
| ligand_6356 | Diethylenetrinitrilopentaacetic acid (DTPA) | 322 |
| ligand_6762 | Pyridine-2-carboxylic acid (Picolinic acid) | 316 |
| ligand_7029 | Ethylenediamine | 310 |
| ligand_10109 | Nitrate ion | 260 |
| ligand_8907 | Butanedioic acid (Succinic acid) | 253 |
| ligand_8647 | 2-Hydroxy-2-methylpropanoic acid | 251 |
| ligand_5898 | L-2-Amino-3-(4-imidazolyl)propanoic acid (Histidine) | 250 |
| ligand_6301 | trans-1,2-Cyclohexylenedinitrilotetraacetic acid (CDTA) | 245 |
| ligand_6204 | N-(2-Hydroxyethyl)iminodiacetic acid (HIDA) | 241 |
| ligand_6774 | Pyridine-2,6-dicarboxylic acid (Dipicolinic acid) | 239 |
| ligand_8412 | Nitrilotris(methylenephosphonic acid) (NTP) | 239 |
| ligand_6275 | N-(2-Hydroxyethyl)ethylenedinitrilotriacetic acid (HEDTA) | 237 |
| ligand_7795 | 1,3-Diazole (Imidazole) | 237 |
| ligand_8467 | Propanoic acid (Propionic acid) | 236 |
| ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | 227 |
| ligand_9358 | 1,2-Dihydroxybenzene-3,5-disulfonic acid (Tiron) | 225 |
| ligand_8955 | D-2,3-Dihydroxybutanedioic acid (D-Tartaric acid) | 214 |
| ligand_6366 | Triethylenetetranitrilohexaacetic acid (TTHA) | 212 |
| ligand_10114 | Hydrogen diphosphate (Pyrophosphoric acid) | 211 |
| ligand_8998 | Thiodiacetic acid | 203 |
| ligand_6309 | Ethylenedinitrilo-N,N'-di(3-propanoic)-N,N'-diacetic acid | 201 |
| ligand_10173 | Hydrogen iodate (Iodic acid) | 199 |
| ligand_5975 | Ethylenediiminodiacetic acid (EDDA) | 198 |
| ligand_10090 | Hydrogen cyanide (Hydrocyanic acid) | 194 |
| ligand_10106 | Hydrogen azide (Hydrazoic acid) | 194 |
| ligand_10171 | Iodide ion | 191 |
| ligand_9142 | 1-Hydroxyethane-1,1-diphosphonic acid (Etidronic acid) | 189 |
| ligand_8321 | Adenosine-5'-(tetrahydrogentriphosphate) (ATP) | 188 |
| ligand_6311 | Trimethylenedinitrilotetraacetic acid (TMDTA) | 186 |

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_6277 AND c.metal_name_SRD IN ('La^[3+]', 'Ce^[3+]', 'Pr^[3+]', 'Nd^[3+]', 'Sm^[3+]', 'Eu^[3+]', 'Gd^[3+]', 'Tb^[3+]', 'Dy^[3+]', 'Ho^[3+]', 'Er^[3+]', 'Tm^[3+]', 'Yb^[3+]', 'Lu^[3+]', 'Y^[3+]', 'Sc^[3+]') AND s.constant_type LIKE 'log beta%' AND s.temperature_c = 25)",
  "order_by": "c.ligand_name_SRD, c.metal_name_SRD, s.ionic_strength_mol_l, s.constant_value DESC",
  "limit": 200
}
```

[summary]
## search_stability

*(no results)*

---

### Step 9: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_10162 AND c.metal_name_SRD IN ('La^[3+]', 'Ce^[3+]', 'Pr^[3+]', 'Nd^[3+]', 'Sm^[3+]', 'Eu^[3+]', 'Gd^[3+]', 'Tb^[3+]', 'Dy^[3+]', 'Ho^[3+]', 'Er^[3+]', 'Tm^[3+]', 'Yb^[3+]', 'Lu^[3+]', 'Y^[3+]', 'Sc^[3+]') AND s.constant_type LIKE 'log beta%' AND s.temperature_c = 25)",
  "order_by": "c.ligand_name_SRD, c.metal_name_SRD, s.ionic_strength_mol_l, s.constant_value DESC",
  "limit": 200
}
```

[summary]
## search_stability

*(no results)*

---

### Step 10: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_8872 AND c.metal_name_SRD IN ('La^[3+]', 'Ce^[3+]', 'Pr^[3+]', 'Nd^[3+]', 'Sm^[3+]', 'Eu^[3+]', 'Gd^[3+]', 'Tb^[3+]', 'Dy^[3+]', 'Ho^[3+]', 'Er^[3+]', 'Tm^[3+]', 'Yb^[3+]', 'Lu^[3+]', 'Y^[3+]', 'Sc^[3+]') AND s.constant_type LIKE 'log beta%' AND s.temperature_c = 25)",
  "order_by": "c.ligand_name_SRD, c.metal_name_SRD, s.ionic_strength_mol_l, s.constant_value DESC",
  "limit": 200
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
  "where": "(c.ligand_id = ligand_6277 AND c.metal_name_SRD LIKE '%^[3+]%')",
  "order_by": "c.metal_name_SRD, s.temperature_c, s.ionic_strength_mol_l",
  "limit": 50
}
```

[summary]
## search_stability — 50 row(s)

### ΔH — 4 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_5 | Al^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 3 | 3 | 20 | 0.1 | *** | 0 |
| metal_6 | Am^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_27 | Ce^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_31 | Cm^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.5 | *** | 0 |

### logK — 10 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_5 | Al^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 7 | 4 | 25 | 0.1~1 | *** | 3 |
| metal_21 | Bi^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 6 | 3 | 20~25 | 0.1~1 | *** | 3 |
| metal_37 | Cr^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 5 | 3 | 20~25 | 0.1~0.5 | *** | 3 |
| metal_6 | Am^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 3 | 1 | 25 | 0.1~0.5 | *** | 3 |
| metal_27 | Ce^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 3 | 2 | 25 | 0.1~1 | *** | 3 |
| metal_31 | Cm^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 3 | 1 | 25 | 0.1~0.5 | *** | 3 |
| metal_22 | Bk^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1 | *** | 2 |
| metal_29 | Cf^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1 | *** | 2 |
| metal_34 | Co^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 2 | 20~25 | 0.1 | *** | 1 |
| metal_10 | As^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |

### ΔS — 4 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_5 | Al^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 3 | 3 | 25 | 0.1 | *** | 0 |
| metal_6 | Am^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_27 | Ce^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_31 | Cm^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.5 | *** | 0 |

---

### Step 12: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_name_SRD = 'La^[3+]' AND c.ligand_id = ligand_6277)",
  "order_by": "s.temperature_c, s.ionic_strength_mol_l, s.constant_value DESC",
  "limit": 50
}
```

[summary]
## search_stability — 12 row(s)

### `La^[3+]` + Ethylenedinitrilotetraacetic acid (EDTA) — 12 measurement(s)
metal_id: metal_79 | ligand_id: ligand_6277
ligand_HxL_def: H4L | ligand_SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_108393 | *** | beta_def_812 | ΔH | -22.2 | 10 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108399 | ref_eq_map_4948 | beta_def_788 | logK | 2 | 20 | 0.1 | `[ML] + [H] <=> [MHL]` | *** |  |  |
| vlm_108396 | *** | beta_def_812 | ΔS | 253.6 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108389 | ref_eq_map_4946 | beta_def_812 | logK | 15.36 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108398 | ref_eq_map_4946 | beta_def_788 | logK | 2.24 | 25 | 0.1 | `[ML] + [H] <=> [MHL]` | *** |  |  |
| vlm_108391 | *** | beta_def_812 | ΔH | -12.1 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108397 | *** | beta_def_812 | ΔS | 222.6 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108390 | ref_eq_map_4947 | beta_def_812 | logK | 14.48 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108392 | *** | beta_def_812 | ΔH | -16.3 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108400 | ref_eq_map_4949 | beta_def_788 | logK | 2 | 25 | 1 | `[ML] + [H] <=> [MHL]` | *** |  |  |
| vlm_108394 | *** | beta_def_812 | ΔH | -20.5 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108395 | *** | beta_def_812 | ΔH | -18.8 | 40 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |

---

### Step 13: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_name_SRD = 'La^[3+]' AND c.ligand_id = ligand_8872)",
  "order_by": "s.temperature_c, s.ionic_strength_mol_l, s.constant_value DESC",
  "limit": 50
}
```

[summary]
## search_stability — 6 row(s)

### `La^[3+]` + Ethanedioic acid (Oxalic acid) — 6 measurement(s)
metal_id: metal_79 | ligand_id: ligand_8872
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_151630 | ref_eq_map_19916 | beta_def_459 | logK | -25 | 20 | 0.1 | `[M2L3(s)] <=> [M]^2 + [L]^3` | solid | [L] | (3.8, L, +inf) |
| vlm_151627 | ref_eq_map_19916 | beta_def_840 | logK | 7.83 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (3.8, L, +inf) |
| vlm_151625 | ref_eq_map_19916 | beta_def_812 | logK | 4.71 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (3.8, L, +inf) |
| vlm_151629 | ref_eq_map_19917 | beta_def_872 | logK | 10.3 | 25 | 1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (3.8, L, +inf) |
| vlm_151628 | ref_eq_map_19917 | beta_def_840 | logK | 7.9 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (3.8, L, +inf) |
| vlm_151626 | ref_eq_map_19917 | beta_def_812 | logK | 4.3 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (3.8, L, +inf) |

---

### Step 14: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_6277 AND c.metal_name_SRD IN ('La^[3+]', 'Ce^[3+]', 'Pr^[3+]', 'Nd^[3+]', 'Sm^[3+]', 'Eu^[3+]', 'Gd^[3+]', 'Tb^[3+]', 'Dy^[3+]', 'Ho^[3+]', 'Er^[3+]', 'Tm^[3+]', 'Yb^[3+]', 'Lu^[3+]', 'Y^[3+]', 'Sc^[3+]') AND s.temperature_c = 25 AND s.ionic_strength_mol_l = 0.1 AND s.constant_type = 'logK' AND s.reaction_type = '[M] + [L] <=> [ML]')",
  "order_by": "s.constant_value ASC",
  "limit": 100
}
```

[summary]
## search_stability

*(no results)*

---

### Step 15: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_8872 AND c.metal_name_SRD IN ('La^[3+]', 'Ce^[3+]', 'Pr^[3+]', 'Nd^[3+]', 'Sm^[3+]', 'Eu^[3+]', 'Gd^[3+]', 'Tb^[3+]', 'Dy^[3+]', 'Ho^[3+]', 'Er^[3+]', 'Tm^[3+]', 'Yb^[3+]', 'Lu^[3+]', 'Y^[3+]', 'Sc^[3+]') AND s.temperature_c = 25 AND s.ionic_strength_mol_l = 0.1 AND s.constant_type = 'logK' AND s.reaction_type = '[M] + [L] <=> [ML]')",
  "order_by": "s.constant_value ASC",
  "limit": 100
}
```

[summary]
## search_stability

*(no results)*

---

### Step 16: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_6277 AND c.metal_name_SRD LIKE '%^[3+]%')",
  "order_by": "c.metal_name_SRD, s.temperature_c, s.ionic_strength_mol_l",
  "limit": 200
}
```

[summary]
## search_stability — 200 row(s)

### ΔH — 18 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_58 | Eu^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 6 | 1 | 10~40 | 0.1~2 | *** | 0 |
| metal_65 | Gd^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 5 | 1 | 10~40 | 0.1~1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 5 | 1 | 10~40 | 0.1~1 | *** | 0 |
| metal_110 | Nd^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 5 | 1 | 10~40 | 0.1~1 | *** | 0 |
| metal_173 | Sm^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 5 | 1 | 10~40 | 0.1~1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 4 | 4 | 25 | 0.1~1 | *** | 0 |
| metal_73 | Ho^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 4 | 1 | 10~40 | 0.1~1 | *** | 0 |
| metal_139 | Pr^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 4 | 1 | 10~40 | 0.1~1 | *** | 0 |
| metal_179 | Tb^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 4 | 1 | 10~40 | 0.1~1 | *** | 0 |
| metal_5 | Al^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 3 | 3 | 20 | 0.1 | *** | 0 |
| metal_6 | Am^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_27 | Ce^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_55 | Er^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_31 | Cm^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.5 | *** | 0 |
| metal_44 | Dy^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_74 | In^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 0 |
| metal_81 | Lu^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_192 | Tm^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |

### logK — 32 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_64 | Ga^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 8 | 3 | 20~25 | 0.1~0.5 | *** | 3 |
| metal_5 | Al^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 7 | 4 | 25 | 0.1~1 | *** | 3 |
| metal_21 | Bi^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 6 | 3 | 20~25 | 0.1~1 | *** | 3 |
| metal_37 | Cr^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 6 | 3 | 20~25 | 0.1~0.5 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 6 | 4 | 25 | 0.1~1 | *** | 2 |
| metal_74 | In^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 6 | 3 | 20~25 | 0.1~0.5 | *** | 3 |
| metal_79 | La^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 5 | 2 | 20~25 | 0.1~1 | *** | 4 |
| metal_148 | Pu^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 5 | 4 | 25 | 0.1~1 | *** | 2 |
| metal_167 | Sb^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 5 | 4 | 20~25 | 0.1~1 | *** | 2 |
| metal_110 | Nd^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 4 | 2 | 20~25 | 0.1~1 | *** | 3 |
| metal_187 | Ti^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_190 | Tl^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 4 | 2 | 20~25 | 0.1~1 | *** | 3 |
| metal_6 | Am^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 3 | 1 | 25 | 0.1~0.5 | *** | 3 |
| metal_27 | Ce^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 3 | 2 | 25 | 0.1~1 | *** | 3 |
| metal_31 | Cm^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 3 | 1 | 25 | 0.1~0.5 | *** | 3 |
| metal_44 | Dy^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 3 | 2 | 25 | 0.1~1 | *** | 3 |
| metal_58 | Eu^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 3 | 2 | 25 | 0.1~1 | *** | 3 |
| metal_65 | Gd^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 3 | 2 | 25 | 0.1~1 | *** | 3 |
| metal_73 | Ho^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 3 | 2 | 25 | 0.1~1 | *** | 3 |
| metal_139 | Pr^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 3 | 2 | 25 | 0.1~1 | *** | 3 |
| metal_169 | Sc^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_173 | Sm^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 3 | 2 | 25 | 0.1~1 | *** | 3 |
| metal_179 | Tb^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 3 | 2 | 25 | 0.1~1 | *** | 3 |
| metal_22 | Bk^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1 | *** | 2 |
| metal_29 | Cf^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1 | *** | 2 |
| metal_34 | Co^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 2 | 20~25 | 0.1 | *** | 1 |
| metal_55 | Er^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 2 |
| metal_81 | Lu^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 2 |
| metal_192 | Tm^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 2 |
| metal_10 | As^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_95 | Mn^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_137 | Pm^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |

### ΔS — 18 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 4 | 4 | 20~25 | 0.1~1 | *** | 0 |
| metal_5 | Al^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 3 | 3 | 25 | 0.1 | *** | 0 |
| metal_6 | Am^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_27 | Ce^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_55 | Er^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_58 | Eu^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_79 | La^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_110 | Nd^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_173 | Sm^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_31 | Cm^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.5 | *** | 0 |
| metal_44 | Dy^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_65 | Gd^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_73 | Ho^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_74 | In^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_81 | Lu^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_139 | Pr^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_179 | Tb^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_192 | Tm^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |

---
