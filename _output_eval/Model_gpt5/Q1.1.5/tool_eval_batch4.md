# Q1.1.5 — Tool Results (batch 4)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "hydrogen",
  "symbol": "H",
  "limit": 10
}
```

[summary]
## search_metals — 10 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_20 | BuHg^[+] | B | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_23 | BuNH_[3]^[+] | B | 1 |  | *** | *** | beta_totN_1 | ligand_totN_2 | vlm_totN_2 |
| metal_24 | C(NH_[2])_[3]^[+] | C | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_45 | Et_[2]NH_[2]^[+] | E2NH2 | 1 |  | *** | *** | beta_totN_1 | ligand_totN_1 | vlm_totN_1 |
| metal_48 | Et_[3]NH^[+] | E3NH | 1 |  | *** | *** | beta_totN_1 | ligand_totN_1 | vlm_totN_1 |
| metal_53 | EtHg^[+] | EHg | 1 |  | *** | *** | beta_totN_4 | ligand_totN_3 | vlm_totN_6 |
| metal_54 | EtNH_[3]^[+] | ENH3 | 1 |  | *** | *** | beta_totN_1 | ligand_totN_3 | vlm_totN_3 |
| metal_68 | H^[+] | H | 1 | ✓ | [H+] | InChI=1S/p+1 | beta_totN_82 | ligand_totN_4081 | vlm_totN_20720 |
| metal_69 | H_[5]TeO_[6]^[-] | H | -1 |  | *** | *** | beta_totN_1 | ligand_totN_1 | vlm_totN_2 |
| metal_70 | Hf^[4+] | Hf | 4 | ✓ | [Hf+4] | InChI=1S/Hf/q+4 | beta_totN_10 | ligand_totN_14 | vlm_totN_49 |

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "oxalic",
  "limit": 25
}
```

[summary]
## search_ligands — 4 result(s)

**stats:** 4 SQL matches · showing 4 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8872 | Ethanedioic acid (Oxalic acid) | H2L | Carboxylic acids diacids | 394 | `O=C(O)C(=O)O` | (-inf, H2L, -1.2, HL, 3.8, L, +inf) |
| ligand_8960 | Oxopropanedioic acid (Ketomaloni… (Mesoxalic acid) | H2L | Carboxylic acids diacids… | 3 | `O=C(O)C(=O)C(=O)O` | (-inf, H2L, -1.82, HL, 3.52, L, +inf) |
| ligand_9763 | Dithiooxalic acid | H2L | miscellaneous mercaptans | 3 | `O=C(S)C(=O)S` | *** |
| ligand_11304 | Ethanedi(dithioic acid) (Tetrathiooxalic acid) | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (3 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 2 | 67% |
| ketone | 1 | 33% |
| thiol | 1 | 33% |

---

### Step 5: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_68",
  "ligand_id": "ligand_8872"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 2 species

### H^[+] + Ethanedioic acid (Oxalic acid)
**metal_id:** metal_68 | **ligand_id:** ligand_8872 | **ligand_def_HxL:** H2L  
**entries:** 56 | **species:** 2 | **vlm_count:** 56

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_32 | [H<sub>2</sub>L]/[HL][H] | [HL] + [H] <=> [H2L] | [H2L](aqueous), [HL](aqueous), [H](aqueous) | 18 |
| beta_def_79 | [HL]/[L][H] | [L] + [H] <=> [HL] | [HL](aqueous), [L](aqueous), [H](aqueous) | 38 |

**vlm_ids:** vlm_151494, vlm_151495, vlm_151496, vlm_151497, vlm_151498, … vlm_151547, vlm_151548, vlm_151549 (56 listed)

**equilibrium_maps:** 25 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_19902 | 2 | 1 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_19903 | 2 | 1 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_19904 | 2 | 1 | 19~29 °C | 0.35~0.65 M |
| ref_eq_net_19905 | 2 | 1 | 19~29 °C | 1.85~2.15 M |
| ref_eq_net_19906 | 1 | 0 | 31~41 °C | 0~0.3 M |
| ref_eq_net_19907 | 1 | 0 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_19908 | 2 | 1 | 19~29 °C | 2.85~3.15 M |
| ref_eq_net_19909 | 2 | 1 | 19~29 °C | -0.05~0.25 M |
| ref_eq_net_19910 | 1 | 0 | 31~41 °C | 0~0.3 M |
| ref_eq_net_19911 | 1 | 0 | 19~29 °C | 0.35~0.65 M |
| ref_eq_net_19912 | 1 | 0 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_19913 | 2 | 1 | 19~29 °C | 1.85~2.15 M |
| ref_eq_net_19914 | 1 | 0 | 19~29 °C | 3.85~4.15 M |
| ref_eq_net_19915 | 2 | 1 | 19~29 °C | 4.85~5.15 M |
| ref_eq_net_19916 | 2 | 1 | 19~29 °C | 6.85~7.15 M |
| ref_eq_net_19917 | 2 | 1 | 19~29 °C | 8.85~9.15 M |
| ref_eq_net_19918 | 1 | 0 | 19~29 °C | -0.05~0.25 M |
| ref_eq_net_19919 | 1 | 0 | 31~41 °C | 0~0.3 M |
| ref_eq_net_19920 | 1 | 0 | 19~29 °C | 0.35~0.65 M |
| ref_eq_net_19921 | 1 | 0 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_19922 | 1 | 0 | 19~29 °C | 2.85~3.15 M |
| ref_eq_net_19923 | 1 | 0 | 19~29 °C | 3.85~4.15 M |
| ref_eq_net_19924 | 1 | 0 | 5~15 °C | -0.15~0.15 M |
| ref_eq_net_19925 | 1 | 0 | 19~29 °C | -0.15~0.15 M |
| ref_eq_net_19926 | 1 | 0 | 35~45 °C | -0.15~0.15 M |

---

### Step 7: `search_pka_values`
**Args:**
```json
{
  "where": "(lc.ligand_id = ligand_8872 AND (p.solvent_name LIKE '%water%' OR p.solvent_name LIKE '%aqueous%'))",
  "order_by": "ABS(p.temperature_c - 25) ASC, p.ionic_strength_mol_l ASC",
  "limit": 50
}
```

[summary]
## search_pka_values

*(no results)*

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_68 AND c.ligand_id = ligand_8872 AND (c.beta_definition_id = beta_def_79 OR c.beta_definition_id = beta_def_32))",
  "order_by": "ABS(s.temperature_c - 25) ASC, s.ionic_strength_mol_l ASC",
  "limit": 100
}
```

[summary]
## search_stability — 56 row(s)

### `H^[+]` + Ethanedioic acid (Oxalic acid) — 56 measurement(s)
metal_id: metal_68 | ligand_id: ligand_8872
ligand_HxL_def: H2L | ligand_SMILES: O=C(O)C(=O)O

| equation | type | vlm_counts | ref_eq_map | value_range | T°C_range | I(M)_range | beta_defs | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|----------|------|------------|------------|-------------|-----------|------------|-----------|--------------------|--------------|-------------|
| `[L] + [H] <=> [HL]` | logK | 25 | 25 diff ref_eq_map | 3.51~5.11 | 10~40 | 0~9 | beta_def_79 | *** | [L]; [HL] | (-1.2, HL, 3.8, L, +inf) |
| `[L] + [H] <=> [HL]` | ΔH | 8 | *** | 0.8~10.5 | 10~40 | 0~2 | beta_def_79 | *** | [L]; [HL] | (-1.2, HL, 3.8, L, +inf) |
| `[L] + [H] <=> [HL]` | ΔS | 5 | *** | 73.2~103.8 | 25 | 0~2 | beta_def_79 | *** | [L]; [HL] | (-1.2, HL, 3.8, L, +inf) |
| `[HL] + [H] <=> [H2L]` | logK | 10 | 10 diff ref_eq_map | -2.13~1.25 | 25 | 0~9 | beta_def_32 | *** | [HL]; [H2L] | (-inf, H2L, -1.2, HL, 3.8) |
| `[HL] + [H] <=> [H2L]` | ΔH | 4 | *** | -2.9~3.3 | 25 | 0~2 | beta_def_32 | *** | [HL]; [H2L] | (-inf, H2L, -1.2, HL, 3.8) |
| `[HL] + [H] <=> [H2L]` | ΔS | 4 | *** | 13~35.1 | 25 | 0~2 | beta_def_32 | *** | [HL]; [H2L] | (-inf, H2L, -1.2, HL, 3.8) |

Summary stats
| type | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|------|------------|-------------|-----------|------------|--------------------|-------------------|
| logK | 35 | 2 | 10~40 | 0~9 | *** | 25 |
| ΔH | 12 | 2 | 10~40 | 0~2 | *** | 0 |
| ΔS | 9 | 2 | 25 | 0~2 | *** | 0 |

---

### Step 9: `search_pka_ligands`
**Args:**
```json
{
  "where": "(lc.ligand_id = ligand_8872)",
  "order_by": "ABS(p.temperature_c - 25) ASC, p.ionic_strength_mol_l ASC",
  "limit": 50
}
```

[summary]
## search_pka_ligands — 2 row(s)

| ligand_id | ligand_name | HxL_def | formula | smiles | pH_ladder | T°C_range | I(M)_range | similarity_score |
|-----------|-------------|---------|---------|--------|-----------|-----------|------------|------------------|
| ligand_8872 | Ethanedioic acid (Oxalic acid) | H2L | C2H2O4 | O=C(O)C(=O)O | −∞; H2L (M_tot_1); (-1.2, vlm_151532); HL (M_tot_7); (3.8, vlm_151494); L (M_tot_56); +∞ | 25 | 0.1 | *** |

---

### Step 10: `search_citations`
**Args:**
```json
{
  "where": "(rv.vlm_id = vlm_151532)",
  "limit": 50
}
```

[summary]
## search_citations — 50 row(s)

| example_vlm_id | vlm_count | lit_id | shortcut | citation |
|----------------|-----------|--------|----------|----------|
| vlm_151532 | 1 | lit_145 | 24L | E. Larsson, Z. Anorg. Allg. Chem., 1924, 140, 292 |
| vlm_151532 | 1 | lit_217 | 28Sa | H. S. Simms, J. Phys. Chem., 1928, 32, 1121, 1495 |
| vlm_151532 | 1 | lit_280 | 31GI | R. Gane and C. K. Ingold, J. Chem. Soc., 1931, 2153 |
| vlm_151532 | 1 | lit_482 | 38CK | R. K. Cannan and A. Kibrick, J. Amer. Chem. Soc., 1938, 60, 2314 |
| vlm_151532 | 1 | lit_521 | 39HF | H. S. Harned and L. O. Fallon, J. Amer. Chem. Soc., 1939, 61, 3111 |
| vlm_151532 | 1 | lit_530 | 39PG | H. N. Parton and R. C. Gibbons, Trans. Faraday Soc., 1939, 35, 542 |
| vlm_151532 | 1 | lit_531 | 39PN | H. N. Parton and A. J. C. Nicholson, Trans. Faraday Soc., 1939, 35, 546 |
| vlm_151532 | 1 | lit_772 | 48PB | G. D. Pinching and R. G. Bates, J. Res. Nat. Bur. Stand., 1948, 40, 405 |
| vlm_151532 | 1 | lit_1324 | 69CMa | G. F. Condike and A. E. Martell, J. Inorg. Nucl. Chem., 1969, 31, 2455 |
| vlm_151532 | 1 | lit_1542 | 77HO | H. Hedstrom, A. Olin, P. Svanstrom, and E. Aslin, J. Inorg. Nucl. Chem., 1977, … |
| vlm_151532 | 1 | lit_1556 | 77JKS | U. Jain, V. Kumari, R. C. Sharma, and G. K. Chaturvedi, J. Chim. Phys., 1977, 7… |
| vlm_151532 | 1 | lit_1677 | 80MMC | A. Misra, S. Mital, and G. K. Chaturvedi, J. Indian Chem. Soc., 1980, 57, 42 |
| vlm_151532 | 1 | lit_2393 | 57DSa | N. K. Dutt and B. Sur, Z. Anorg. Allg. Chem., 1957, 293, 195 |
| vlm_151532 | 1 | lit_2411 | 57GMM | A. B. Gelman, N. N. Matorina, and A. I. Moskvin, Proc. Acad. Sci. USSR, Chem. S… |
| vlm_151532 | 1 | lit_2460 | 57Ld | J. Lefebvre, J. Chim. Phys., 1957, 54, 567 |
| vlm_151532 | 1 | lit_2643 | 58GM | A. D. Gelman, N. N. Matorina, and A. I. Moskvin, Soviet J. Atomic Energy, 1958,… |
| vlm_151532 | 1 | lit_2848 | 59D | W. H. Dumbaugh, Jr., Thesis, Penn. State Univ., 1959 |
| vlm_151532 | 1 | lit_3233 | 60MN | A. McAuley and G. H. Nancollas, Trans. Faraday Soc., 1960, 56, 1165 |
| vlm_151532 | 1 | lit_3310 | 60YD | Y. Yamane and N. Davidson, J. Amer. Chem. Soc., 1960, 82, 2123 |
| vlm_151532 | 1 | lit_3472 | 61MN | A. McAuley and G. H. Nancollas, J. Chem. Soc., 1961, 2215 |
| vlm_151532 | 1 | lit_3626 | 62BKT | H. J. deBruin, D. Kaitis, and R. B. Temple, Aust. J. Chem., 1962, 15, 457 |
| vlm_151532 | 1 | lit_4690 | 65BCa | E. Bottari and L. Ciavatta, Gazz. Chim. Ital., 1965, 95, 908 |
| vlm_151532 | 1 | lit_4716 | 65BSc | R. F. Bauer and W. M. Smith, Canad. J. Chem., 1965, 43, 2755 |
| vlm_151532 | 1 | lit_4962 | 65Sb | T. Sekine, Acta Chem. Scand., 1965, 19, 1476; J. Inorg. Nucl. Chem., 1964, 26, … |
| vlm_151532 | 1 | lit_5261 | 66LM | G. A. L'Heureux and A. E. Martell, J. Inorg. Nucl. Chem., 1966, 28, 481 |
| vlm_151532 | 1 | lit_5263 | 66LN | S. J. Lyle and S. J. Naqui, J. Inorg. Nucl. Chem., 1966, 28, 2993 |
| vlm_151532 | 1 | lit_5302 | 66MS | E. G. Moorhead and N. Sutin, Inorg. Chem., 1966, 5, 1866 |
| vlm_151532 | 1 | lit_5312 | 66MY | I. N. Maksimova and V. F. Yushkevich, Soviet Electrochem., 1966, 2, 532 (577) |
| vlm_151532 | 1 | lit_5516 | 67CIH | J. J. Christensen, R. M. Izatt, and L. D. Hansen, J. Amer. Chem. Soc., 1967, 89… |
| vlm_151532 | 1 | lit_5681 | 67Mk | I. N. Maksimova, Russ. J. Phys. Chem., 1967, 41, 27 (52) |
| vlm_151532 | 1 | lit_5788 | 67RMa | K. S. Rajan and A. E. Martell, J. Inorg. Nucl. Chem., 1967, 29, 523 |
| vlm_151532 | 1 | lit_6026 | 68DMB | M. Deneux, R. Meilleur, and R. L. Benoit, Canad. J. Chem., 1968, 46, 1383 |
| vlm_151532 | 1 | lit_6100 | 68Ha | R. J. N. Harries, Talanta, 1968, 15, 1345 |
| vlm_151532 | 1 | lit_6500 | 69GGR | I. Grenthe, G. Gardhammar, and E. Rundcrantz, Acta Chem. Scand., 1969, 23, 93 |
| vlm_151532 | 1 | lit_6568 | 69KF | J. L. Kurz and J. M. Farrar, J. Amer. Chem. Soc., 1969, 91, 6057 |
| vlm_151532 | 1 | lit_6882 | 70ABd | J. Ascanio and F. Brito, An. Quim., 1970, 66, 617 |
| vlm_151532 | 1 | lit_6928 | 70BLD | A. Braibanti, E. Leporati, and F. Dallavalle, Inorg. Chim. Acta, 1970, 4, 529 |
| vlm_151532 | 1 | lit_6957 | 70CF | Y. Couturier and J. Faucherre, Bull. Soc. Chim. France, 1970, 1323 |
| vlm_151532 | 1 | lit_7043 | 70GB | V. I. Grebenshchikova, R. V. Bryzgalova, and Yu. M. Rogozin, Soviet Radiochem.,… |
| vlm_151532 | 1 | lit_7221 | 70SH | L. M. Schwartz and L. O. Howard, J. Phys. Chem., 1970, 74, 4374 |
| vlm_151532 | 1 | lit_7237 | 70SPb | A. V. Stepanov and E. M. Pazukhin, Russ. J. Inorg. Chem., 1970, 15, 761 (1483) |
| vlm_151532 | 1 | lit_7444 | 71Gc | R. I. Gelb, Anal. Chem., 1971, 43, 1110 |
| vlm_151532 | 1 | lit_7465 | 71GM | V. I. Gordienko, Yu. I. Mikhailyuk, and V. I. Sidorenko, J. Gen. Chem. USSR, 19… |
| vlm_151532 | 1 | lit_7822 | 71VK | V. P. Vasilev, L. A. Kochergina, and V. I. Eremenko, Russ. J. Phys. Chem., 1971… |
| vlm_151532 | 1 | lit_8162 | 72Ma | I. Mentre, Ann. Chim. (Paris), 1972, 7, 333 |
| vlm_151532 | 1 | lit_8170 | 72MBT | L. Magon, A. Bismondo, G. Tomat, and A. Cassol, Radiochim. Acta, 1972, 17, 164 |
| vlm_151532 | 1 | lit_8436 | 73AD | G. M. Armitage and H. S. Dunsmore, J. Inorg. Nucl. Chem., 1973, 35, 817 |
| vlm_151532 | 1 | lit_8485 | 73BRR | M. Barres, J. P. Redoute, R. Romanetti, H. Tachoire, and C. Zahra, Compt. Rend.… |
| vlm_151532 | 1 | lit_8521 | 73CSb | E. I. Chubakova and N. A. Skorik, Russ. J. Inorg. Chem., 1973, 18, 1446 (2723) |
| vlm_151532 | 1 | lit_8907 | 73VS | V. P. Vasilev, L. D. Shekhanova, and L. A. Kochergina, J. Gen. Chem. USSR, 1973… |

---

### Step 11: `search_citations`
**Args:**
```json
{
  "where": "(rv.vlm_id = vlm_151494)",
  "limit": 50
}
```

[summary]
## search_citations — 50 row(s)

| example_vlm_id | vlm_count | lit_id | shortcut | citation |
|----------------|-----------|--------|----------|----------|
| vlm_151494 | 1 | lit_145 | 24L | E. Larsson, Z. Anorg. Allg. Chem., 1924, 140, 292 |
| vlm_151494 | 1 | lit_217 | 28Sa | H. S. Simms, J. Phys. Chem., 1928, 32, 1121, 1495 |
| vlm_151494 | 1 | lit_280 | 31GI | R. Gane and C. K. Ingold, J. Chem. Soc., 1931, 2153 |
| vlm_151494 | 1 | lit_482 | 38CK | R. K. Cannan and A. Kibrick, J. Amer. Chem. Soc., 1938, 60, 2314 |
| vlm_151494 | 1 | lit_521 | 39HF | H. S. Harned and L. O. Fallon, J. Amer. Chem. Soc., 1939, 61, 3111 |
| vlm_151494 | 1 | lit_530 | 39PG | H. N. Parton and R. C. Gibbons, Trans. Faraday Soc., 1939, 35, 542 |
| vlm_151494 | 1 | lit_531 | 39PN | H. N. Parton and A. J. C. Nicholson, Trans. Faraday Soc., 1939, 35, 546 |
| vlm_151494 | 1 | lit_772 | 48PB | G. D. Pinching and R. G. Bates, J. Res. Nat. Bur. Stand., 1948, 40, 405 |
| vlm_151494 | 1 | lit_1324 | 69CMa | G. F. Condike and A. E. Martell, J. Inorg. Nucl. Chem., 1969, 31, 2455 |
| vlm_151494 | 1 | lit_1542 | 77HO | H. Hedstrom, A. Olin, P. Svanstrom, and E. Aslin, J. Inorg. Nucl. Chem., 1977, … |
| vlm_151494 | 1 | lit_1556 | 77JKS | U. Jain, V. Kumari, R. C. Sharma, and G. K. Chaturvedi, J. Chim. Phys., 1977, 7… |
| vlm_151494 | 1 | lit_1677 | 80MMC | A. Misra, S. Mital, and G. K. Chaturvedi, J. Indian Chem. Soc., 1980, 57, 42 |
| vlm_151494 | 1 | lit_2393 | 57DSa | N. K. Dutt and B. Sur, Z. Anorg. Allg. Chem., 1957, 293, 195 |
| vlm_151494 | 1 | lit_2411 | 57GMM | A. B. Gelman, N. N. Matorina, and A. I. Moskvin, Proc. Acad. Sci. USSR, Chem. S… |
| vlm_151494 | 1 | lit_2460 | 57Ld | J. Lefebvre, J. Chim. Phys., 1957, 54, 567 |
| vlm_151494 | 1 | lit_2643 | 58GM | A. D. Gelman, N. N. Matorina, and A. I. Moskvin, Soviet J. Atomic Energy, 1958,… |
| vlm_151494 | 1 | lit_2848 | 59D | W. H. Dumbaugh, Jr., Thesis, Penn. State Univ., 1959 |
| vlm_151494 | 1 | lit_3233 | 60MN | A. McAuley and G. H. Nancollas, Trans. Faraday Soc., 1960, 56, 1165 |
| vlm_151494 | 1 | lit_3310 | 60YD | Y. Yamane and N. Davidson, J. Amer. Chem. Soc., 1960, 82, 2123 |
| vlm_151494 | 1 | lit_3472 | 61MN | A. McAuley and G. H. Nancollas, J. Chem. Soc., 1961, 2215 |
| vlm_151494 | 1 | lit_3626 | 62BKT | H. J. deBruin, D. Kaitis, and R. B. Temple, Aust. J. Chem., 1962, 15, 457 |
| vlm_151494 | 1 | lit_4690 | 65BCa | E. Bottari and L. Ciavatta, Gazz. Chim. Ital., 1965, 95, 908 |
| vlm_151494 | 1 | lit_4716 | 65BSc | R. F. Bauer and W. M. Smith, Canad. J. Chem., 1965, 43, 2755 |
| vlm_151494 | 1 | lit_4962 | 65Sb | T. Sekine, Acta Chem. Scand., 1965, 19, 1476; J. Inorg. Nucl. Chem., 1964, 26, … |
| vlm_151494 | 1 | lit_5261 | 66LM | G. A. L'Heureux and A. E. Martell, J. Inorg. Nucl. Chem., 1966, 28, 481 |
| vlm_151494 | 1 | lit_5263 | 66LN | S. J. Lyle and S. J. Naqui, J. Inorg. Nucl. Chem., 1966, 28, 2993 |
| vlm_151494 | 1 | lit_5302 | 66MS | E. G. Moorhead and N. Sutin, Inorg. Chem., 1966, 5, 1866 |
| vlm_151494 | 1 | lit_5312 | 66MY | I. N. Maksimova and V. F. Yushkevich, Soviet Electrochem., 1966, 2, 532 (577) |
| vlm_151494 | 1 | lit_5516 | 67CIH | J. J. Christensen, R. M. Izatt, and L. D. Hansen, J. Amer. Chem. Soc., 1967, 89… |
| vlm_151494 | 1 | lit_5681 | 67Mk | I. N. Maksimova, Russ. J. Phys. Chem., 1967, 41, 27 (52) |
| vlm_151494 | 1 | lit_5788 | 67RMa | K. S. Rajan and A. E. Martell, J. Inorg. Nucl. Chem., 1967, 29, 523 |
| vlm_151494 | 1 | lit_6026 | 68DMB | M. Deneux, R. Meilleur, and R. L. Benoit, Canad. J. Chem., 1968, 46, 1383 |
| vlm_151494 | 1 | lit_6100 | 68Ha | R. J. N. Harries, Talanta, 1968, 15, 1345 |
| vlm_151494 | 1 | lit_6500 | 69GGR | I. Grenthe, G. Gardhammar, and E. Rundcrantz, Acta Chem. Scand., 1969, 23, 93 |
| vlm_151494 | 1 | lit_6568 | 69KF | J. L. Kurz and J. M. Farrar, J. Amer. Chem. Soc., 1969, 91, 6057 |
| vlm_151494 | 1 | lit_6882 | 70ABd | J. Ascanio and F. Brito, An. Quim., 1970, 66, 617 |
| vlm_151494 | 1 | lit_6928 | 70BLD | A. Braibanti, E. Leporati, and F. Dallavalle, Inorg. Chim. Acta, 1970, 4, 529 |
| vlm_151494 | 1 | lit_6957 | 70CF | Y. Couturier and J. Faucherre, Bull. Soc. Chim. France, 1970, 1323 |
| vlm_151494 | 1 | lit_7043 | 70GB | V. I. Grebenshchikova, R. V. Bryzgalova, and Yu. M. Rogozin, Soviet Radiochem.,… |
| vlm_151494 | 1 | lit_7221 | 70SH | L. M. Schwartz and L. O. Howard, J. Phys. Chem., 1970, 74, 4374 |
| vlm_151494 | 1 | lit_7237 | 70SPb | A. V. Stepanov and E. M. Pazukhin, Russ. J. Inorg. Chem., 1970, 15, 761 (1483) |
| vlm_151494 | 1 | lit_7444 | 71Gc | R. I. Gelb, Anal. Chem., 1971, 43, 1110 |
| vlm_151494 | 1 | lit_7465 | 71GM | V. I. Gordienko, Yu. I. Mikhailyuk, and V. I. Sidorenko, J. Gen. Chem. USSR, 19… |
| vlm_151494 | 1 | lit_7822 | 71VK | V. P. Vasilev, L. A. Kochergina, and V. I. Eremenko, Russ. J. Phys. Chem., 1971… |
| vlm_151494 | 1 | lit_8162 | 72Ma | I. Mentre, Ann. Chim. (Paris), 1972, 7, 333 |
| vlm_151494 | 1 | lit_8170 | 72MBT | L. Magon, A. Bismondo, G. Tomat, and A. Cassol, Radiochim. Acta, 1972, 17, 164 |
| vlm_151494 | 1 | lit_8436 | 73AD | G. M. Armitage and H. S. Dunsmore, J. Inorg. Nucl. Chem., 1973, 35, 817 |
| vlm_151494 | 1 | lit_8485 | 73BRR | M. Barres, J. P. Redoute, R. Romanetti, H. Tachoire, and C. Zahra, Compt. Rend.… |
| vlm_151494 | 1 | lit_8521 | 73CSb | E. I. Chubakova and N. A. Skorik, Russ. J. Inorg. Chem., 1973, 18, 1446 (2723) |
| vlm_151494 | 1 | lit_8907 | 73VS | V. P. Vasilev, L. D. Shekhanova, and L. A. Kochergina, J. Gen. Chem. USSR, 1973… |

---
