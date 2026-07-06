# Q1.2.2 — Tool Results (batch 3)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Cadmium",
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
  "name": "Chloride",
  "limit": 10
}
```

[summary]
## search_ligands — 10 result(s)

**stats:** 12 SQL matches · showing 10 · limit 10

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

### Step 6: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_26 AND c.ligand_id = ligand_10163)",
  "order_by": "c.beta_definition_id, s.constant_value ASC",
  "limit": 100
}
```

[summary]
## search_stability — 30 row(s)

### `Cd^[2+]` + Chloride ion — 30 measurement(s)
metal_id: metal_26 | ligand_id: ligand_10163
ligand_HxL_def: *** | ligand_SMILES: ***

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_177550 | *** | beta_def_812 | ΔH | -0.4 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177549 | *** | beta_def_812 | ΔH | 1.3 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177543 | ref_eq_map_29796 | beta_def_812 | logK | 1.35 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177544 | ref_eq_map_29792 | beta_def_812 | logK | 1.35 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177545 | ref_eq_map_29793 | beta_def_812 | logK | 1.44 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177542 | ref_eq_map_29791 | beta_def_812 | logK | 1.52 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177546 | ref_eq_map_29794 | beta_def_812 | logK | 1.54 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177547 | ref_eq_map_29795 | beta_def_812 | logK | 1.66 | 25 | 4 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177548 | ref_eq_map_29797 | beta_def_812 | logK | 1.98 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177552 | *** | beta_def_812 | ΔS | 28 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177551 | *** | beta_def_812 | ΔS | 30.1 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177560 | *** | beta_def_840 | ΔH | 0 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_177553 | ref_eq_map_29796 | beta_def_840 | logK | 1.7 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_177554 | ref_eq_map_29792 | beta_def_840 | logK | 1.7 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_177555 | ref_eq_map_29793 | beta_def_840 | logK | 1.9 | 25 | 2 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_177556 | ref_eq_map_29794 | beta_def_840 | logK | 2.2 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_177557 | ref_eq_map_29795 | beta_def_840 | logK | 2.4 | 25 | 4 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_177558 | ref_eq_map_29791 | beta_def_840 | logK | 2.6 | 25 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_177559 | *** | beta_def_840 | ΔH | 3.8 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_177562 | *** | beta_def_840 | ΔS | 42.3 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_177561 | *** | beta_def_840 | ΔS | 45.2 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_177563 | ref_eq_map_29792 | beta_def_872 | logK | 1.5 | 25 | 1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_177564 | ref_eq_map_29793 | beta_def_872 | logK | 1.9 | 25 | 2 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_177565 | ref_eq_map_29794 | beta_def_872 | logK | 2.3 | 25 | 3 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_177567 | ref_eq_map_29791 | beta_def_872 | logK | 2.4 | 25 | 0 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_177566 | ref_eq_map_29795 | beta_def_872 | logK | 2.8 | 25 | 4 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_177569 | *** | beta_def_872 | ΔH | 7.9 | 25 | 3 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_177568 | *** | beta_def_872 | ΔH | 10 | 25 | 1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_177570 | *** | beta_def_872 | ΔS | 62.3 | 25 | 1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_177571 | *** | beta_def_872 | ΔS | 70.7 | 25 | 3 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |

---

### Step 7: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_stability_measured",
  "group_column": "beta_definition_id",
  "where": "metal_id = 26 AND ligand_id = 10163",
  "limit": 20
}
```

[TOOL ERROR] db_distribution: Error executing tool db_distribution: no such column: metal_id

---

### Step 8: `search_citations`
**Args:**
```json
{
  "where": "(rv.vlm_id IN (177542,177543,177544,177545,177546,177547,177548,177549,177550,177551,177552,177553,177554,177555,177556,177557,177558,177559,177560,177561,177562,177563,177564,177565,177566,177567,177568,177569,177570,177571))",
  "order_by": "la.shortcut ASC",
  "limit": 100
}
```

[summary]
## search_citations — 68 row(s)

| example_vlm_id | vlm_count | lit_id | shortcut | citation |
|----------------|-----------|--------|----------|----------|
| vlm_177542 | 30 | lit_265 | 30RD | E. C. Righellato and C. W. Davies, Trans. Faraday Soc., 1930, 26, 592 |
| vlm_177542 | 30 | lit_318 | 32RG | H. L. Riley and V. Gallafent, J. Chem. Soc., 1932, 514 |
| vlm_177542 | 30 | lit_426 | 36HF | H. S. Harned and M. E. Fitzgerald, J. Amer. Chem. Soc., 1936, 58, 2624 |
| vlm_177542 | 30 | lit_581 | 41L | I. Leden, Z. Phys. Chem., 1941, A188, 160 |
| vlm_177542 | 30 | lit_829 | 49K | E. L. King, J. Amer. Chem. Soc., 1949, 71, 319 |
| vlm_177542 | 30 | lit_969 | 51BA | J. E. Barney, W. J. Argersinger. Jr., and C. A. Reynolds, J. Amer. Chem. Soc., … |
| vlm_177542 | 30 | lit_1839 | 53E | L. Eriksson, Acta Chem. Scand., 1953, 7, 1146 |
| vlm_177542 | 30 | lit_1851 | 53G | A. M. Golub, Ukr. Khim. Zh., 1953, 19, 205, 467 |
| vlm_177542 | 30 | lit_1938 | 53VD | C. E. Vanderzee and H. J. Dawson, Jr., J. Amer. Chem. Soc., 1953, 75, 5659 |
| vlm_177542 | 30 | lit_2315 | 56Tb | Ya. I. Turyan, J. Inorg. Chem. USSR, 1956, 1, No. 10, 171 (2337) |
| vlm_177542 | 30 | lit_2452 | 57KL | P. Kivalo and R. Luoto, Suomen Kem., 1957, B30, 163 |
| vlm_177542 | 30 | lit_2552 | 57TS | Ya. I. Turyan and G. F. Serova, J. Inorg. Chem. USSR, 1957, 2, No. 2, 165 (336) |
| vlm_177542 | 30 | lit_2775 | 58TF | W. B. Truemann and L. M. Ferris, J. Amer. Chem. Soc., 1958, 80, 5048 |
| vlm_177542 | 30 | lit_2938 | 59Ma | Y. Marcus, J. Phys. Chem., 1959, 63, 1000 |
| vlm_177542 | 30 | lit_3148 | 60FSS | Ya. D. Fridman, D. S. Sarbaev, and R. I. Sorochan, Russ. J. Inorg. Chem., 1960,… |
| vlm_177542 | 30 | lit_3301 | 60TZ | Ya. I. Turyan and B. P. Zhantalai, Russ. J. Inorg. Chem., 1960, 5, 848 (1748) |
| vlm_177542 | 30 | lit_3502 | 61PF | A. Patterson, Jr., and H. Freitag, J. Electrochem. Soc., 1961, 108, 529 |
| vlm_177542 | 30 | lit_3603 | 62AP | V. I. Altynov and B. V. Ptitsyn, Russ. J. Inorg. Chem., 1962, 7, 1088 (2103) |
| vlm_177542 | 30 | lit_3622 | 62BDJ | O. D. Bonner, H. Dolyniuk, C. F. Jordan, and G. B. Hanson, J. Inorg. Nucl. Chem… |
| vlm_177542 | 30 | lit_3633 | 62BSa | D. Banerjea and I. P. Singh, J. Indian Chem. Soc., 1962, 39, 353 |
| vlm_177542 | 30 | lit_4141 | 63MKN | V. E. Mironov, F. Ya. Kulba, and V. A. Nazarov, Russ. J. Inorg. Chem., 1963, 8,… |
| vlm_177542 | 30 | lit_4415 | 64GL | M. Grimaldi and A. Liberti, J. Chromatogr., 1964, 15, 510 |
| vlm_177542 | 30 | lit_4802 | 65HA | J. D. Hefley and E. S. Amis, J. Phys. Chem., 1965, 69, 2082 |
| vlm_177542 | 30 | lit_4811 | 65HS | H. E. Hellwege and G. K. Schweitzer, J. Inorg. Nucl. Chem., 1965, 27, 99 |
| vlm_177542 | 30 | lit_4872 | 65M | L. W. Marple, J. Inorg. Nucl. Chem., 1965, 27, 1693 |
| vlm_177542 | 30 | lit_5161 | 66G | P. Gerding, Acta Chem. Scand., 1966, 20, 79 |
| vlm_177542 | 30 | lit_5194 | 66HP | J. T. Huang and K. Pan, J. Chinese Chem. Soc. (Taiwan), 1966, 13, 64 |
| vlm_177542 | 30 | lit_5275 | 66Mg | L. W. Marple, J. Inorg. Nucl. Chem., 1966, 28, 1319 |
| vlm_177542 | 30 | lit_5381 | 66SG | A. Swinarski and A. Grodzicki, Rocz. Chem., 1966, 40, 373 |
| vlm_177542 | 30 | lit_5449 | 67Ac | S. Ahrland, Helv. Chim. Acta, 1967, 50, 306 |
| vlm_177542 | 30 | lit_5691 | 67MF | V. E. Mironov and A. V. Fokina, Russ. J. Inorg. Chem., 1967, 12, 1357 (2571) |
| vlm_177542 | 30 | lit_6083 | 68GJ | P. Gerding and I. Jonsson, Acta Chem. Scand., 1968, 22, 2247 |
| vlm_177542 | 30 | lit_6646 | 69MMd | V. I. Malkova, G. D. Malchikov, and B. I. Peshchevitskii, Izv. Akad. Nauk Sib. … |
| vlm_177542 | 30 | lit_6812 | 69SP | G. Sahu and B. Prasad, J. Indian Chem. Soc., 1969, 46, 233 |
| vlm_177542 | 30 | lit_7200 | 70RS | P. J. Reilly and R. H. Stokes, Aust. J. Chem., 1970, 23, 1397 |
| vlm_177542 | 30 | lit_7426 | 71FCK | V. A. Fedorov, G. E. Chernikova, T. N. Kalosh, and V. E. Mironov, Russ. J. Inor… |
| vlm_177542 | 30 | lit_7698 | 71PBb | M. Polasek and M. Bartusek, Scr. Fac. Sci. Nat. Univ. Purk. Brun., 1971, 1, 109 |
| vlm_177542 | 30 | lit_8004 | 72FKM | V. A. Fedorov, L. I. Kiprin, and V. E. Mironov, Russ. J. Inorg. Chem., 1972, 17… |
| vlm_177542 | 30 | lit_8075 | 72J | J. B. Jensen, Acta Chem. Scand., 1972, 26, 4031 |
| vlm_177542 | 30 | lit_8591 | 73HH | M. H. Hutchinson and W. C. E. Higginson, J. Chem. Soc. Dalton, 1973, 1247 |
| vlm_177542 | 30 | lit_8971 | 74BLL | G. Biedermann, J. Lagrange, and P. Lagrange, Chem. Scr., 1974, 5, 153 |
| vlm_177542 | 30 | lit_8970 | 74BLb | J. W. Bixler and T. M. Larson, J. Inorg. Nucl. Chem., 1974, 36, 224 |
| vlm_177542 | 30 | lit_9015 | 74EM | I. Eliezer and A. Moreno, J. Chem. Eng. Data, 1974, 19, 226 |
| vlm_177542 | 30 | lit_9046 | 74FRP | V. A. Fedorov, A. M. Robov, V. P. Plekhanov, V. V. Kudruk, M. A. Kuznechikhina,… |
| vlm_177542 | 30 | lit_9051 | 74Ga | J. Gardiner, Water Res., 1974, 8, 23 |
| vlm_177542 | 30 | lit_9430 | 75BA | E. A. Belousov and A. A. Alovyainikov, Russ. J. Inorg. Chem., 1975, 20, 803 (14… |
| vlm_177542 | 30 | lit_9619 | 75KLF | M. Ya. Kutuzova, L. E. Leshchishina, and V. A. Fedorov, Russ. J. Inorg. Chem., … |
| vlm_177542 | 30 | lit_1538 | 77HHa | G. A. Heath and G. Hefter, J. Electroanal. Chem., 1977, 84, 295 |
| vlm_177542 | 30 | lit_10638 | 78AR | A. Arevalo, J. C. Rodriguez Placeres, T. Moreno, and J. Segura, J. Electroanal.… |
| vlm_177542 | 30 | lit_11061 | 79BKa | S. D. Brown and B. R. Kowalski, Anal. Chem., 1979, 51, 2133 |
| vlm_177542 | 30 | lit_11298 | 79O | W. A. de Oliveira, J. Coord. Chem., 1979, 9, 7 |
| vlm_177542 | 30 | lit_1624 | 80L | D. J. Leggett, Talanta, 1980, 27, 787 |
| vlm_177542 | 30 | lit_11845 | 81DB | N. V. Deryabina and V. I. Bakanov, Izv. Vyssh. Ucheb. Zaved., Khim., 1981, 24, … |
| vlm_177542 | 30 | lit_11846 | 81DBD | D. De Marco, A. Bellomo, and A. De Robertis, J. Inorg. Nucl. Chem., 1981, 43, 1… |
| vlm_177542 | 30 | lit_12130 | 81SV | M. de L. S. Simoes, M. Candida T. A. Vaz, and J. J. R. Frausto da Silva, Talant… |
| vlm_177542 | 30 | lit_12470 | 82NN | R. Nikolic and O. Neskovic, J. Chem. Soc. Dalton, 1982, 1417 |
| vlm_177542 | 30 | lit_12744 | 83GS | I. Granberg and S. Sjoberg, Acta Chem. Scand., 1983, A37, 415 |
| vlm_177542 | 30 | lit_18297 | 84MA | E. A. Mambetkaziev, M. U. Abilova, A. M. Shaldybaeva, S. I. Zhdanov, and Sh. A.… |
| vlm_177542 | 30 | lit_13366 | 84PE | V. A. Prokuev, R. V. Elntrop, and E. A. Belousov, Russ. J. Inorg. Chem., 1984, … |
| vlm_177542 | 30 | lit_13624 | 85GN | I. G. R. Gutz and E. A. Neves, J. Electroanal. Chem., 1985, 183, 123 |
| vlm_177542 | 30 | lit_13728 | 85MC | J. Maslowska and E. Chruscinska, Polish J. Chem., 1985, 59, 339 |
| vlm_177542 | 30 | lit_13782 | 85PBa | V. A. Prokuev and E. A. Belousov, Russ. J. Inorg. Chem., 1985, 30, 679, (1203) |
| vlm_177542 | 30 | lit_13847 | 85SGB | R. Stella, M. T. Ganzerli Valentini, and P. A. Borroni, "Ion-Selective Electrod… |
| vlm_177542 | 30 | lit_14834 | 88IB | I. V. Ion and F. G. Banica, Rev. Chim. (Bucuresti), 1988, 39, 438 |
| vlm_177542 | 30 | lit_14936 | 88PB | I. Pizeta and M. Branica, J. Electroanal. Chem., 1988, 250, 293 |
| vlm_177542 | 30 | lit_15113 | 89BPB | M. Branica, I. Pizeta, G. Branica-Jurkovic, and M. Zelic, Marine Chem., 1989, 2… |
| vlm_177542 | 30 | lit_16462 | 93GA | M. A. Ghandour, E. Aboul-Kasim, A. H. Amrallah, and O. A. Farghall, J. Indian C… |
| vlm_177542 | 30 | lit_16624 | 93VJ | M. Visic, A. Jadric, and I. Mekjavic, Croat. Chem. Acta, 1993, 66, 489 |

---

### Step 9: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id = metal_26 AND c.ligand_id = ligand_10163)",
  "order_by": "n.network_db_id ASC",
  "limit": 20
}
```

[summary]
## search_networks — 18 row(s)

> **Reference equilibrium networks** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### `Cd^[2+]` + Chloride ion — 7 network(s)
metal_id: metal_26 | ligand_id: ligand_10163 | ligand_def_HxL: *** | ligand_SMILES: ***

| beta_def | equation |
|----------|----------|
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_872 | ``[M] + [L]^3 <=> [ML3]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_29910 | 3 | 3 | 20~30 | -0.05~0.25 | 3 | beta_def_812; beta_def_872; beta_def_840 | logK | 1.52~2.6 |
| ref_eq_net_29911 | 3 | 3 | 19~29 | 0.85~1.15 | 3 | beta_def_812; beta_def_872; beta_def_840 | logK | 1.35~1.7 |
| ref_eq_net_29912 | 3 | 3 | 19~29 | 1.85~2.15 | 3 | beta_def_812; beta_def_840; beta_def_872 | logK | 1.44~1.9 |
| ref_eq_net_29913 | 3 | 3 | 19~29 | 2.85~3.15 | 3 | beta_def_812; beta_def_840; beta_def_872 | logK | 1.54~2.3 |
| ref_eq_net_29914 | 3 | 3 | 19~29 | 3.85~4.15 | 3 | beta_def_812; beta_def_840; beta_def_872 | logK | 1.66~2.8 |
| ref_eq_net_29915 | 2 | 1 | 19~29 | 0.35~0.65 | 2 | beta_def_812; beta_def_840 | logK | 1.35~1.7 |
| ref_eq_net_29916 | 1 | 0 | 19~29 | -0.15~0.15 | 1 | beta_def_812 | logK | 1.98 |

#### Reference-state network: ref_eq_net_29910 (3 nodes)
> First network — reference conditions (T 20~30 °C, I -0.05~0.25 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 1.52 |
| beta_def_872 | ``[M] + [L]^3 <=> [ML3]`` | logK | 2.4 |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` | logK | 2.6 |

---
