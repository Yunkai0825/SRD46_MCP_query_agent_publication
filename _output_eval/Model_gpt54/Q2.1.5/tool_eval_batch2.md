# Q2.1.5 — Tool Results (batch 2)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Nickel(II)",
  "limit": 10
}
```

[summary]
## search_metals — 2 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_112 | Ni^[2+] | Ni | 2 | ✓ | [Ni+2] | InChI=1S/Ni/q+2 | beta_totN_149 | ligand_totN_1369 | vlm_totN_5325 |
| metal_113 | Ni^[3+] | Ni | 3 | ✓ | [Ni+3] | InChI=1S/Ni/q+3 | beta_totN_5 | ligand_totN_4 | vlm_totN_7 |

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

### Step 4: `search_ligands`
**Args:**
```json
{
  "name": "ethylenediamine",
  "limit": 10
}
```

[summary]
## search_ligands — 10 result(s)

**stats:** 105 SQL matches · showing 10 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5948 | N-(2-Aminoethyl)glycine (Ethylenediamine m… (EDMA) | HL | Amino Acids | 30 | `NCCNCC(=O)O` | (-inf, H3L, -1.9, H2L, 6.67, HL, 9.84, L, +inf) |
| ligand_6253 | N-(2-Aminoeth… (Ethylenediamine-N,N-diacetic acid) | H2L | NTA and derivatives | 39 | `NCCN(CC(=O)O)CC(=O)O` | (-inf, H2L, 5.53, HL, 10.87, L, +inf) |
| ligand_7029 | Ethylenediamine | L | Aliphatic amines | 310 | `NCCN` | (-inf, H2L, 7.11, HL, 9.92, L, +inf) |
| ligand_7030 | DL-Methylethylenediamine (1,2-Propylenediami… (pn) | L | Aliphatic amines | 86 | `CC(N)CN` | (-inf, H2L, 6.85, HL, 9.81, L, +inf) |
| ligand_7031 | DL-Ethylethylenediamine (1,2-Butylenediamine) | L | Aliphatic amines | 19 | `CCC(N)CN` | (-inf, H2L, 6.65, HL, 9.66, L, +inf) |
| ligand_7032 | DL-(2-Methyl-2-propyl)et… (t-Butylethylenediamine) | L | Aliphatic amines | 2 | `CC(C)(C)C(N)CN` | (-inf, H2L, 6.26, HL, 9.78, L, +inf) |
| ligand_7033 | 1,1-Dimethylethylenediamine | L | Aliphatic amines | 37 | `CC(C)(N)CN` | (-inf, H2L, 6.46, HL, 9.75, L, +inf) |
| ligand_7034 | DL-1,2-Dimethylethylened… (DL-2,3-Butylenediamine) | L | Aliphatic amines | 46 | `CC(N)C(C)N` | (-inf, H2L, 6.6, HL, 9.7, L, +inf) |
| ligand_7035 | meso-1,2-Dimethylethyl… (meso-2,3-Butylenediamine) | L | Aliphatic amines | 53 | `C[C@H](N)[C@@H](C)N` | (-inf, H2L, 6.63, HL, 9.76, L, +inf) |
| ligand_7036 | 1,1,2,2-Tetramethylethylenediamine | L | Aliphatic amines | 15 | `CC(C)(N)C(C)(C)N` | (-inf, H2L, 6.35, HL, 9.93, L, +inf) |

### Functional groups across all SQL matches (85 parseable SMILES)

| group | count | % |
|-------|-------|---|
| primary_amine | 58 | 68% |
| secondary_amine | 43 | 51% |
| tertiary_amine | 23 | 27% |
| hydroxyl | 14 | 16% |
| aromatic_ring | 13 | 15% |
| amide | 7 | 8% |
| phosphonate | 4 | 5% |
| thioether | 4 | 5% |
| phenol | 3 | 4% |
| pyridine | 3 | 4% |
| carboxyl | 2 | 2% |
| sulfonate | 1 | 1% |
| thiol | 1 | 1% |

---

### Step 5: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_112",
  "ligand_id": "ligand_10103"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 6 species

### Ni^[2+] + Ammonia
**metal_id:** metal_112 | **ligand_id:** ligand_10103 | **ligand_def_HxL:** L  
**entries:** 60 | **species:** 6 | **vlm_count:** 60

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 11 |
| beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | [M] + [L]^2 <=> [ML2] | [ML2](aqueous), [M](aqueous), [L](aqueous) | 13 |
| beta_def_872 | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | [M] + [L]^3 <=> [ML3] | [ML3](aqueous), [M](aqueous), [L](aqueous) | 10 |
| beta_def_894 | [ML<sub>4</sub>]/[M][L]<sup>4</sup> | [M] + [L]^4 <=> [ML4] | [ML4](aqueous), [M](aqueous), [L](aqueous) | 10 |
| beta_def_903 | [ML<sub>5</sub>]/[M][L]<sup>5</sup> | [M] + [L]^5 <=> [ML5] | [ML5](aqueous), [M](aqueous), [L](aqueous) | 8 |
| beta_def_907 | [ML<sub>6</sub>]/[M][L]<sup>6</sup> | [M] + [L]^6 <=> [ML6] | [ML6](aqueous), [M](aqueous), [L](aqueous) | 8 |

**vlm_ids:** vlm_173182, vlm_173183, vlm_173184, vlm_173185, vlm_173186, … vlm_173239, vlm_173240, vlm_173241 (60 listed)

**equilibrium_maps:** 5 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_28236 | 6 | 15 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_28237 | 6 | 15 | 19~29 °C | 1.85~2.15 M |
| ref_eq_net_28238 | 4 | 6 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_28239 | 2 | 1 | 19~29 °C | -0.15~0.15 M |
| ref_eq_net_28240 | 1 | 0 | 19~29 °C | 2.85~3.15 M |

---

### Step 7: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_112 AND c.ligand_id IN (ligand_10103, ligand_7029) AND c.beta_definition_id = beta_def_812)",
  "order_by": "c.ligand_id ASC, s.temperature_c ASC, s.ionic_strength_mol_l ASC, s.constant_value DESC",
  "limit": 200
}
```

[summary]
## search_stability — 26 row(s)

### `Ni^[2+]` + Ethylenediamine — 15 measurement(s)
metal_id: metal_112 | ligand_id: ligand_7029
ligand_HxL_def: L | ligand_SMILES: NCCN

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_122371 | ref_eq_map_9574 | beta_def_812 | logK | 7.32 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122376 | *** | beta_def_812 | ΔS | 9.2 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122365 | ref_eq_map_9568 | beta_def_812 | logK | 7.3 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122372 | *** | beta_def_812 | ΔH | 0 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122377 | *** | beta_def_812 | ΔS | 16.3 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122367 | ref_eq_map_9570 | beta_def_812 | logK | 7.45 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122373 | *** | beta_def_812 | ΔH | -37.7 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122378 | *** | beta_def_812 | ΔS | 18.4 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122368 | ref_eq_map_9571 | beta_def_812 | logK | 7.56 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122374 | *** | beta_def_812 | ΔH | -37.7 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122369 | ref_eq_map_9572 | beta_def_812 | logK | 7.9 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122370 | ref_eq_map_9573 | beta_def_812 | logK | 7.87 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122375 | *** | beta_def_812 | ΔH | 0 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122379 | *** | beta_def_812 | ΔS | 0 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122366 | ref_eq_map_9569 | beta_def_812 | logK | 6.98 | 37 | 0.15 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |

### `Ni^[2+]` + Ammonia — 11 measurement(s)
metal_id: metal_112 | ligand_id: ligand_10103
ligand_HxL_def: L | ligand_SMILES: N

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_173185 | ref_eq_map_28130 | beta_def_812 | logK | 2.72 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173190 | *** | beta_def_812 | ΔS | 1.7 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173186 | *** | beta_def_812 | ΔH | -15.1 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173182 | ref_eq_map_28127 | beta_def_812 | logK | 2.73 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173183 | ref_eq_map_28129 | beta_def_812 | logK | 2.8 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173191 | *** | beta_def_812 | ΔS | 1.7 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173187 | *** | beta_def_812 | ΔH | -15.5 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173184 | ref_eq_map_28128 | beta_def_812 | logK | 2.85 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173192 | *** | beta_def_812 | ΔS | 1.3 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173188 | *** | beta_def_812 | ΔH | -15.9 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173189 | *** | beta_def_812 | ΔH | -16.3 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |

---

### Step 8: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_112",
  "ligand_id": "ligand_7029"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 3 species

### Ni^[2+] + Ethylenediamine
**metal_id:** metal_112 | **ligand_id:** ligand_7029 | **ligand_def_HxL:** L  
**entries:** 45 | **species:** 3 | **vlm_count:** 45

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 15 |
| beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | [M] + [L]^2 <=> [ML2] | [ML2](aqueous), [M](aqueous), [L](aqueous) | 15 |
| beta_def_872 | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | [M] + [L]^3 <=> [ML3] | [ML3](aqueous), [M](aqueous), [L](aqueous) | 15 |

**vlm_ids:** vlm_122365, vlm_122366, vlm_122367, vlm_122368, vlm_122369, … vlm_122407, vlm_122408, vlm_122409 (45 listed)

**equilibrium_maps:** 7 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_9591 | 3 | 3 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_9592 | 3 | 3 | 31~41 °C | 0~0.3 M |
| ref_eq_net_9593 | 3 | 3 | 19~29 °C | 0.35~0.65 M |
| ref_eq_net_9594 | 3 | 3 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_9595 | 3 | 3 | 19~29 °C | 1.85~2.15 M |
| ref_eq_net_9596 | 3 | 3 | 19~29 °C | 2.85~3.15 M |
| ref_eq_net_9597 | 3 | 3 | 19~29 °C | -0.15~0.15 M |

---

### Step 9: `inspect_literature`
**Args:**
```json
{
  "prefix_id": "vlm_122371"
}
```

[summary]
## inspect_literature — vlm_122371 — 57 citation(s)

| lit_id | shortcut | citation |
|--------|----------|----------|
| lit_562 | 41B | J. Bjerrum, Metal Amine Formation in Aqueous Solution, P. Haase and Son, Copenh… |
| lit_682 | 45CM | G. A. Carlson, J. P. McReynolds, and F. H. Verhoek, J. Amer. Chem. Soc., 1945, … |
| lit_906 | 50E | L. J. Edwards, Diss., Univ. Michigan, 1950 (see 61KE and 64SMb) |
| lit_1076 | 52BMa | F. Basolo and R. K. Murmann, J. Amer. Chem. Soc., 1952, 74, 5243 |
| lit_1109 | 52H | G. B. Hares, Diss., Penn. State Coll., 1952 |
| lit_1893 | 53Ma | G. H. McIntyre, Diss., Penn. State Coll., 1953 |
| lit_1967 | 54BM | F. Basolo and R. K. Murmann, J. Amer. Chem. Soc., 1954, 76, 211 |
| lit_1994 | 54DSS | T. Davies, S. S. Singer, and L. A. K. Staveley, J. Chem. Soc., 1954, 2304 |
| lit_2115 | 55CH | F. A. Cotton and F. E. Harris, J. Phys. Chem., 1955, 59, 1203 |
| lit_2207 | 55PB | I. Poulsen and J. Bjerrum, Acta Chem. Scand., 1955, 9, 1407 |
| lit_2466 | 57Lj | R. G. Lacoste, Diss., Clark Univ., 1957 (see 64SMb) |
| lit_2592 | 58BF | C. R. Bertsch, W. C. Fernelius, and B. P. Block, J. Phys. Chem., 1958, 62, 444 |
| lit_2945 | 59MB | G. H. McIntyre, Jr., B. P. Block, and W. C. Fernelius, J. Amer. Chem. Soc., 195… |
| lit_3128 | 60CP | M. Ciampolini, P. Paoletti, and L. Sacconi, J. Chem. Soc., 1960, 4553 |
| lit_3307 | 60WD | J. I. Watters and R. DeWitt, J. Amer. Chem. Soc., 1960, 82, 1333 |
| lit_3427 | 61KE | R. N. Keller and L. J. Edwards, Univ. Colo. Studies, Ser. Chem. Pharm., 1961, N… |
| lit_3557 | 61SSa | W. Schaeg and F. Schneider, Z. Physiol. Chem., 1961, 326, 40 |
| lit_3965 | 63Cd | C. Caullet, Bull. Soc. Chim. France, 1963, 688 |
| lit_4604 | 64SMb | Unpublished values quoted in L. G. Sillen and A. E. Martell, Stability Constant… |
| lit_4907 | 65NKc | R. Nasanen, M. Koskinen, and K. Kajander, Suomen Kem., 1965, B38, 103 |
| lit_5599 | 67HWa | F. Holmes and D. R. Williams, J. Chem. Soc. (A), 1967, 1702 |
| lit_5831 | 67SS | W. F. Stack and H. A. Skinner, Trans. Faraday Soc., 1967, 63, 1136 |
| lit_6288 | 68PKd | E. Peltonen and P. Kivalo, Suomen Kem., 1968, B41, 187 |
| lit_6302 | 68PSa | D. D. Perrin and V. S. Sharma, J. Chem. Soc. (A), 1968, 446 |
| lit_6434 | 68YM | M. Yokoi, Y. Mori, E. Kubota, and K. Murata, Nippon Kagaku Zasshi, 1968, 89, 11… |
| lit_7035 | 70FRR | G. Faraglia, F. J. C. Rossotti, and H. S. Rossotti, Inorg. Chim. Acta, 1970, 4,… |
| lit_7089 | 70MAd | V. M. Mylnikova and K. V. Astakhov, Russ. J. Phys. Chem., 1970, 44, 1417 (2500) |
| lit_7469 | 71GS | R. Griesser and H. Sigel, Inorg. Chem., 1971, 10, 2229 |
| lit_8221 | 72NBC | M. S. Newman, D. H. Busch, G. E. Cheney, and C. R. Gustafson, Inorg. Chem., 197… |
| lit_9212 | 74MMN | K. K. Mui, W. A. E. McBryde, and E. Nieboer, Canad. J. Chem., 1974, 52, 1821 |
| lit_9269 | 74PB | P. C. Parikh and P. K. Bhattacharya, Indian J. Chem., 1974, 12, 402 |
| lit_9329 | 74SKT | V. A. Shormanov, G. A. Krestov, and E. A. Trupikov, Russ. J. Inorg. Chem., 1974… |
| lit_9656 | 75LM | D. J. Leggett and W. A. E. McBryde, Anal. Chem., 1975, 47, 1065 |
| lit_10942 | 78SKG | I. Sovago, T. Kiss, and A. Gergely, J. Chem. Soc. Dalton, 1978, 964 |
| lit_10962 | 78SSf | V. A. Sharnin, V. A. Shormanov, and G. A. Krestov, Izv. Vyssh. Uchebn. Zaved., … |
| lit_11132 | 79FS | A. Ya. Fridman, G. M. Sycheva, and Yu. A. Afanasev, Soviet J. Coord. Chem., 197… |
| lit_11152 | 79GSK | V. D. Gusev, V. A. Shormanov, and G. A. Krestov, Soviet J. Coord. Chem., 1979, … |
| lit_11366 | 79SG | I. Sovago and A. Gergely, Inorg. Chim. Acta, 1979, 37, 233 |
| lit_12086 | 81RSa | V. V. Ramanujam and V. M. Selvarajan, J. Indian Chem. Soc., 1981, 58, 1131 |
| lit_12380 | 82KJ | S. Khanna, A. K. Jain, and G. K. Chaturvedi, Indian J. Chem., 1982, 21A, 206 |
| lit_12424 | 82MEA | H. M. Marafie, M. S. El-Ezaby, B. A. Abd-El-Nabey, and N. Kittaneh, Trans. Met.… |
| lit_12777 | 83IOO | S. Ishiguro, Y. Oka, and H. Ohtaki, Bull. Chem. Soc. Japan, 1983, 56, 2426 |
| lit_12937 | 83RK | P. Ramesh, B. V. Kumar, and G. R. Reddy, Indian J. Chem., 1983, 22A, 822 |
| lit_13379 | 84PR | J. G. H. du Preez, H. E. Rohwer, B. J. van Brecht, and M. R. Caira, J. Chem. So… |
| lit_13358 | 84Pa | P. Paoletti, Pure Appl. Chem., 1984, 56, 491 |
| lit_14352 | 87BDK | S. I. Berezina, N. G. Dobrenkov, and T. D. Keshner, Russ. J. Inorg. Chem., 1987… |
| lit_14689 | 88AFT | T. Amari, S. Funahashi, and M. Tanaka, Inorg. Chem., 1988, 27, 3368 |
| lit_15323 | 89OF | M. T. Oms, R. Forteza, V. Cerda, and F. Borrull, Thermochim. Acta, 1989, 138, 1 |
| lit_15358 | 89RSR | G. Reddy, S. Satyanarayana, and K. V. Reddy, Indian J. Chem., 1989, 28A, 337 |
| lit_15362 | 89RVM | A. K. Rao, P. Venkataiah, M. S. Mohan, and H. B. Bathina, J. Coord. Chem., 1989… |
| lit_15391 | 89SRb | Shivaraj and M. G. R. Reddy, Indian J. Chem., 1989, 28A, 1016 |
| lit_15407 | 89VBa | V. P. Vasilev and V. A. Borodin, Russ. J. Inorg. Chem., 1989, 34, 1506 (2636) |
| lit_16507 | 93KK | B. Kurzak and D. Kroczewska, Trans. Met. Chem. (London), 1993, 18, 295 |
| lit_16845 | 94RSR | C. V. R. Reddy, Shivaraj, and M. G. R. Reddy, J. Indian Chem. Soc., 1994, 71, 59 |
| lit_16861 | 94SR | Shivaraj, C. V. R. Reddy, and M. G. R. Reddy, Acta Ciencia Indica, 1994, 80, 105 |
| lit_17013 | 95KKa | B. Kurzak and D. Kroczewska, J. Coord. Chem., 1995, 34, 67 |
| lit_17490 | 97HR | E. Hosten and H. E. Rohwer, Anal. Chim. Acta, 1997, 355, 95 |

---

### Step 10: `inspect_literature`
**Args:**
```json
{
  "prefix_id": "vlm_173185"
}
```

[summary]
## inspect_literature — vlm_173185 — 26 citation(s)

| lit_id | shortcut | citation |
|--------|----------|----------|
| lit_41 | 04E | H. von Euler, Chem. Ber., 1904, 37, 2768 |
| lit_167 | 25W | H. J. de Wijs, Rec. Trav. Chim., 1925, 44, 663 |
| lit_562 | 41B | J. Bjerrum, Metal Amine Formation in Aqueous Solution, P. Haase and Son, Copenh… |
| lit_641 | 43DV | P. F. Derr and W. C. Vosburgh, J. Amer. Chem. Soc., 1943, 65, 2408 |
| lit_1098 | 52Fb | W. S. Fyfe, J. Chem. Soc., 1952, 2023 |
| lit_1792 | 52YG | K. B. Yatsimirskii and Z. M. Grafova, J. Gen. Chem. USSR, 1952, 22, (1726) |
| lit_2029 | 54La | R. Lloyd, Thesis, Temple Univ., Phila., Penn., 1954 |
| lit_2207 | 55PB | I. Poulsen and J. Bjerrum, Acta Chem. Scand., 1955, 9, 1407 |
| lit_2567 | 57YMa | K. B. Yatsimirskii and P. M. Milyukov, Zh. Fiz. Khim., 1957, 31, 842 |
| lit_3008 | 59Sl | J. L. Schultz, Thesis, Univ. Minnesota, 1959 |
| lit_3468 | 61ML | C. H. Muendel, H. B. Linford, and W. A. Selke, J. Amer. Inst. Chem. Eng., 1961,… |
| lit_3512 | 61R | J. Rydberg, Acta Chem. Scand., 1961, 15, 1723 |
| lit_5157 | 66FL | Ya. D. Fridman, M. G. Levina, and R. I. Sorochan, Russ. J. Inorg. Chem., 1966, … |
| lit_5262 | 66LMP | C. Luca, V. Magearu, and G. Popa, J. Electroanal. Chem., 1966, 12, 45 |
| lit_7063 | 70Lg | F. Letowski, Rocz. Chem., 1970, 44, 1665 |
| lit_7086 | 70MAa | V. M. Mylnikova, K. V. Astakhov, and S. A. Barkov, Russ. J. Phys. Chem., 1970, … |
| lit_7648 | 71MR | W. J. MacKellar and D. B. Rorabacher, J. Amer. Chem. Soc., 1971, 93, 4379 |
| lit_7741 | 71RMb | D. B. Rorabacher and C. A. Melendez-Cepeda, J. Amer. Chem. Soc., 1971, 93, 6071 |
| lit_10082 | 76KSA | G. A. Krestov, V. A. Shormanov, and V. N. Afanasev, Russ. J. Inorg. Chem., 1976… |
| lit_10543 | 77SFa | G. M. Sycheva, A. Ya. Fridman, and Yu. A. Afanasev, Soviet J. Coord. Chem., 197… |
| lit_11806 | 81BKS | D. Banerjea, T. A. Kaden, and H. Sigel, Inorg. Chem., 1981, 20, 2586 |
| lit_12508 | 82RM | G. N. Rao, C. S. R. Murthy, and A. Prakash, Indian J. Chem., 1982, 21A, 203 |
| lit_12577 | 82VB | V. P. Vasilev, V. A. Borodin, and A. I. Lytkin, Russ. J. Inorg. Chem., 1982, 27… |
| lit_13972 | 86BKV | V. A. Borodin, E. V. Kozlovskii, and V. P. Vasilev, Russ. J. Inorg. Chem., 1986… |
| lit_14648 | 87VBa | V. P. Vasilev and V. A. Borodin, Russ. J. Inorg. Chem., 1987, 32, 1099 (1860) |
| lit_16808 | 94MP | V. E. Mironov, G. L. Pashkov, T. V. Stupko, and Zh. A. Pavlovskaya, Russ. J. In… |

---
