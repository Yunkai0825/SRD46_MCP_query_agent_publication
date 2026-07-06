# Q1.1.4 — Tool Results (batch 4)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Ag",
  "limit": 10
}
```

[summary]
## search_metals — 3 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_2 | Ag^[+] | Ag | 1 | ✓ | [Ag+] | InChI=1S/Ag/q+1 | beta_totN_68 | ligand_totN_649 | vlm_totN_2885 |
| metal_3 | Ag^[2+] | Ag | 2 | ✓ | [Ag+2] | InChI=1S/Ag/q+2 | beta_totN_1 | ligand_totN_5 | vlm_totN_5 |
| metal_4 | Ag^[3+] | Ag | 3 | ✓ | [Ag+3] | InChI=1S/Ag/q+3 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "ammonia",
  "limit": 10
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_10103 | Ammonia | L | Inorganic ligands | 447 | `N` | (-inf, HL, 9.26, L, +inf) |

---

### Step 4: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_2",
  "ligand_id": "ligand_10103"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 2 species

### Ag^[+] + Ammonia
**metal_id:** metal_2 | **ligand_id:** ligand_10103 | **ligand_def_HxL:** L  
**entries:** 47 | **species:** 2 | **vlm_count:** 47

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 22 |
| beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | [M] + [L]^2 <=> [ML2] | [ML2](aqueous), [M](aqueous), [L](aqueous) | 25 |

**vlm_ids:** vlm_173338, vlm_173339, vlm_173340, vlm_173341, vlm_173342, … vlm_173382, vlm_173383, vlm_173384 (47 listed)

**equilibrium_maps:** 16 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_28262 | 2 | 1 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_28263 | 2 | 1 | 19~29 °C | 1.85~2.15 M |
| ref_eq_net_28264 | 2 | 1 | 19~29 °C | 2.85~3.15 M |
| ref_eq_net_28265 | 2 | 1 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_28266 | 2 | 1 | 19~29 °C | 1.85~2.15 M |
| ref_eq_net_28267 | 2 | 1 | 19~29 °C | 2.85~3.15 M |
| ref_eq_net_28268 | 2 | 1 | 19~29 °C | 3.85~4.15 M |
| ref_eq_net_28269 | 2 | 1 | 19~29 °C | 4.85~5.15 M |
| ref_eq_net_28270 | 1 | 0 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_28271 | 2 | 1 | 19~29 °C | 0.35~0.65 M |
| ref_eq_net_28272 | 2 | 1 | 19~29 °C | 1.85~2.15 M |
| ref_eq_net_28273 | 2 | 1 | 19~29 °C | 2.85~3.15 M |
| ref_eq_net_28274 | 2 | 1 | 19~29 °C | 3.85~4.15 M |
| ref_eq_net_28275 | 2 | 1 | 19~29 °C | 4.85~5.15 M |
| ref_eq_net_28276 | 1 | 0 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_28277 | 1 | 0 | 19~29 °C | 0.85~1.15 M |

---

### Step 6: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id = metal_2 AND c.ligand_id = ligand_10103)",
  "order_by": "n.network_db_id ASC",
  "limit": 50
}
```

[summary]
## search_networks — 29 row(s)

> **Reference equilibrium networks** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### `Ag^[+]` + Ammonia — 16 network(s)
metal_id: metal_2 | ligand_id: ligand_10103 | ligand_def_HxL: L | ligand_SMILES: N

| beta_def | equation |
|----------|----------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_28262 | 2 | 1 | 20~30 | -0.05~0.25 | 2 | beta_def_812; beta_def_840 | logK | 3.31~7.22 |
| ref_eq_net_28263 | 2 | 1 | 19~29 | 1.85~2.15 | 2 | beta_def_812; beta_def_840 | logK | 3.26~7.22 |
| ref_eq_net_28264 | 2 | 1 | 19~29 | 2.85~3.15 | 2 | beta_def_812; beta_def_840 | logK | 3.2~7.14 |
| ref_eq_net_28265 | 2 | 1 | 19~29 | 0.85~1.15 | 2 | beta_def_812; beta_def_840 | logK | 3.35~7.24 |
| ref_eq_net_28266 | 2 | 1 | 19~29 | 1.85~2.15 | 2 | beta_def_812; beta_def_840 | logK | 3.27~7.28 |
| ref_eq_net_28267 | 2 | 1 | 19~29 | 2.85~3.15 | 2 | beta_def_812; beta_def_840 | logK | 3.25~7.3 |
| ref_eq_net_28268 | 2 | 1 | 19~29 | 3.85~4.15 | 2 | beta_def_812; beta_def_840 | logK | 3.25~7.34 |
| ref_eq_net_28269 | 2 | 1 | 19~29 | 4.85~5.15 | 2 | beta_def_812; beta_def_840 | logK | 3.21~7.14 |
| ref_eq_net_28270 | 1 | 0 | 19~29 | 0.85~1.15 | 1 | beta_def_840 | logK | 7.24 |
| ref_eq_net_28271 | 2 | 1 | 19~29 | 0.35~0.65 | 2 | beta_def_812; beta_def_840 | logK | 3.31~7.31 |
| ref_eq_net_28272 | 2 | 1 | 19~29 | 1.85~2.15 | 2 | beta_def_812; beta_def_840 | logK | 3.53~7.78 |
| ref_eq_net_28273 | 2 | 1 | 19~29 | 2.85~3.15 | 2 | beta_def_812; beta_def_840 | logK | 3.63~7.92 |
| ref_eq_net_28274 | 2 | 1 | 19~29 | 3.85~4.15 | 2 | beta_def_812; beta_def_840 | logK | 3.8~8.18 |
| ref_eq_net_28275 | 2 | 1 | 19~29 | 4.85~5.15 | 2 | beta_def_812; beta_def_840 | logK | 3.28~7.38 |
| ref_eq_net_28276 | 1 | 0 | 19~29 | 0.85~1.15 | 1 | beta_def_840 | logK | 7.34 |
| ref_eq_net_28277 | 1 | 0 | 19~29 | 0.85~1.15 | 1 | beta_def_840 | logK | 7.54 |

#### Reference-state network: ref_eq_net_28262 (2 nodes)
> First network — reference conditions (T 20~30 °C, I -0.05~0.25 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 3.31 |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` | logK | 7.22 |

---

### Step 7: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_2 AND c.ligand_id = ligand_10103)",
  "order_by": "s.constant_type ASC, s.temperature_c ASC, s.ionic_strength_mol_l ASC, s.constant_value ASC",
  "limit": 200
}
```

[summary]
## search_stability — 47 row(s)

### `Ag^[+]` + Ammonia — 47 measurement(s)
metal_id: metal_2 | ligand_id: ligand_10103
ligand_HxL_def: L | ligand_SMILES: N

| equation | type | vlm_counts | ref_eq_map | value_range | T°C_range | I(M)_range | beta_defs | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|----------|------|------------|------------|-------------|-----------|------------|-----------|--------------------|--------------|-------------|
| `[M] + [L]^2 <=> [ML2]` | ΔH | 5 | *** | -61.9~-56.1 | 25 | 0~3 | beta_def_840 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L] <=> [ML]` | ΔH | 5 | *** | -25.9~-20.5 | 25 | 0~3 | beta_def_812 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L] <=> [ML]` | logK | 13 | 13 diff ref_eq_map | 3.2~3.8 | 25 | 0~5 | beta_def_812 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^2 <=> [ML2]` | logK | 16 | 16 diff ref_eq_map | 7.14~8.18 | 25 | 0~5 | beta_def_840 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^2 <=> [ML2]` | ΔS | 4 | *** | -55.6~-46.4 | 25 | 0~3 | beta_def_840 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L] <=> [ML]` | ΔS | 4 | *** | -12.1~-5.4 | 25 | 0~3 | beta_def_812 | *** | [L] | (9.26, L, +inf) |

Summary stats
| type | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|------|------------|-------------|-----------|------------|--------------------|-------------------|
| ΔH | 10 | 2 | 25 | 0~3 | *** | 0 |
| logK | 29 | 2 | 25 | 0~5 | *** | 16 |
| ΔS | 8 | 2 | 25 | 0~3 | *** | 0 |

---

### Step 8: `search_citations`
**Args:**
```json
{
  "where": "(rv.vlm_id IN (173338,173339,173340,173341,173342,173343,173344,173345,173346,173347,173348,173349,173350,173351,173352,173353,173354,173355,173356,173357,173358,173359,173360,173361,173362,173363,173364,173365,173366,173367,173368,173369,173370,173371,173372,173373,173374,173375,173376,173377,173378,173379,173380,173381,173382,173383,173384))",
  "order_by": "la.shortcut ASC",
  "limit": 200
}
```

[summary]
## search_citations — 33 row(s)

| example_vlm_id | vlm_count | lit_id | shortcut | citation |
|----------------|-----------|--------|----------|----------|
| vlm_173338 | 47 | lit_7 | 00BD | D. Berthelot and M. Delepine, Compt. Rend. Acad. Sci. Paris, 1899, 129, 326 |
| vlm_173338 | 47 | lit_27 | 02BF | G. Bodlander and R. Fittig, Z. Phys. Chem., 1902, 39, 597 |
| vlm_173338 | 47 | lit_34 | 03E | H. von Euler, Chem. Ber., 1903, 36, 1854, 3400 |
| vlm_173338 | 47 | lit_154 | 25B | J. Breszina, Rec. Trav. Chim., 1925, 44, 520 |
| vlm_173338 | 47 | lit_205 | 28J | P. Job, Ann. Chim. (Paris), 1928, 9, 113 |
| vlm_173338 | 47 | lit_256 | 30K | F. K. V. Koch, J. Chem. Soc., 1930, 2053 |
| vlm_173338 | 47 | lit_266 | 30RH | M. Randall and J. O. Halford, J. Amer. Chem. Soc., 1930, 52, 178 |
| vlm_173338 | 47 | lit_325 | 33BW | H. T. S. Britton and B. M. Wilson, J. Chem. Soc., 1933, 1050 |
| vlm_173338 | 47 | lit_400 | 35BW | H. T. S. Britton and W. C. Williams, J. Chem. Soc., 1935, 796 |
| vlm_173338 | 47 | lit_473 | 37SBP | W. V. Smith, O. L. I. Brown, and K. S. Pitzer, J. Amer. Chem. Soc., 1937, 59, 1… |
| vlm_173338 | 47 | lit_562 | 41B | J. Bjerrum, Metal Amine Formation in Aqueous Solution, P. Haase and Son, Copenh… |
| vlm_173338 | 47 | lit_566 | 41DS | P. F. Derr, R. M. Stockdale, and W. C. Vosburgh, J. Amer. Chem. Soc., 1941, 63,… |
| vlm_173338 | 47 | lit_659 | 43VM | W. C. Vosburgh and R. S. McClure, J. Amer. Chem. Soc., 1943, 65, 1060 |
| vlm_173338 | 47 | lit_665 | 44KN | S. Kilpi and R. Nasanen, Suomen Kem., 1944, B17, 9 |
| vlm_173338 | 47 | lit_738 | 47N | R. Nasanen, Acta Chem. Scand., 1947, 1, 763 |
| vlm_173338 | 47 | lit_823 | 49J | W. Jaenicke, Z. Naturforsch., 1949, 4a, 353 |
| vlm_173338 | 47 | lit_2033 | 54LP | K. S. Lyalikov and V. N. Piskunova, Russ. J. Phys. Chem., 1954, 28, (127), (595) |
| vlm_173338 | 47 | lit_2029 | 54La | R. Lloyd, Thesis, Temple Univ., Phila., Penn., 1954 |
| vlm_173338 | 47 | lit_2133 | 55Fa | W. S. Fyfe, J. Chem. Soc., 1955, 1347 |
| vlm_173338 | 47 | lit_3445 | 61LP | I. Leden and G. Persson, Acta Chem. Scand., 1961, 15, 1141 |
| vlm_173338 | 47 | lit_5209 | 66Ja | S. Johansson, quoted in P. Paoletti, A. Vacca, and D. Arenare, J. Phys. Chem., … |
| vlm_173338 | 47 | lit_5277 | 66Mi | R. Matejec, Ber. Buns. Phys. Chem., 1966, 70, 703 |
| vlm_173338 | 47 | lit_6575 | 69KL | B. Kozlowska, F. Letowski, and J. Niemiec, Rocz. Chem., 1969, 43, 1597 |
| vlm_173338 | 47 | lit_11157 | 79Hb | R. D. Hancock, S. Afr. J. Chem., 1979, 32, 49 |
| vlm_173338 | 47 | lit_11239 | 79MA | M. Maeda, R. Arnek, and G. Biedermann, J. Inorg. Nucl. Chem., 1979, 41, 343 |
| vlm_173338 | 47 | lit_12789 | 83K | B. Kolodziej, Canad. J. Chem., 1983, 61, 383 |
| vlm_173338 | 47 | lit_12871 | 83MNB | M. Maeda, G. Nakagawa, and G. Biedermann, J. Phys. Chem., 1983, 87, 121 |
| vlm_173338 | 47 | lit_13144 | 84DBL | D. De Marco, A. Bellomo, F. Licastro, and A. Casale, Ann. Chim. (Rome), 1984, 7… |
| vlm_173338 | 47 | lit_13928 | 85YWa | A. Yuchi, H. Wada, and G. Nakagawa, Anal. Sci., 1985, 1, 409 |
| vlm_173338 | 47 | lit_13951 | 86Ba | J. Bjerrum, Acta Chem. Scand., 1986, A40, 392 |
| vlm_173338 | 47 | lit_14017 | 86DLM | D. De Marco, F. Licastro, G. Mauceri, and A. Marchese, Ann. Chim. (Rome), 1986,… |
| vlm_173338 | 47 | lit_16249 | 92LH | M. Lundeen and Z. Z. Hugus, Thermochim. Acta, 1992, 196, 93 |
| vlm_173338 | 47 | lit_16476 | 93GYc | R. Garner, J. Yperman, J. Mullens, and L. C. Van Pouche, J. Coord. Chem., 1993,… |

---
