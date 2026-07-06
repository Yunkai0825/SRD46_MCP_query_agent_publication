# Q1.2.5 — Tool Results (batch 4)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Pb",
  "symbol": "Pb"
}
```

[summary]
## search_metals — 11 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_16 | Bu_[3]Pb^[+] | B | 1 |  | *** | *** | beta_totN_2 | ligand_totN_1 | vlm_totN_2 |
| metal_46 | Et_[2]Pb^[2+] | E2Pb | 2 |  | *** | *** | beta_totN_2 | ligand_totN_3 | vlm_totN_5 |
| metal_49 | Et_[3]Pb^[+] | E3Pb | 1 |  | *** | *** | beta_totN_2 | ligand_totN_3 | vlm_totN_5 |
| metal_84 | Me_[2]Pb^[2+] | M2Pb | 2 |  | *** | *** | beta_totN_5 | ligand_totN_4 | vlm_totN_9 |
| metal_87 | Me_[3]Pb^[+] | M3Pb | 1 |  | *** | *** | beta_totN_7 | ligand_totN_23 | vlm_totN_33 |
| metal_125 | Pb^[2+] | Pb | 2 | ✓ | [Pb+2] | InChI=1S/Pb/q+2 | beta_totN_80 | ligand_totN_470 | vlm_totN_1585 |
| metal_126 | Pb^[4+] | Pb | 4 | ✓ | [Pb+4] | InChI=1S/Pb/q+4 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_129 | Ph_[2]Pb^[2+] | Ph2Pb | 2 |  | *** | *** | beta_totN_2 | ligand_totN_1 | vlm_totN_2 |
| metal_130 | Ph_[3]Pb^[+] | Ph3Pb | 1 |  | *** | *** | beta_totN_1 | ligand_totN_2 | vlm_totN_2 |
| metal_140 | Pr_[2]Pb^[2+] | Pr | 2 |  | *** | *** | beta_totN_2 | ligand_totN_3 | vlm_totN_5 |
| metal_142 | Pr_[3]Pb^[+] | Pr | 1 |  | *** | *** | beta_totN_2 | ligand_totN_1 | vlm_totN_2 |

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "chloride"
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
  "metal_id": "metal_125",
  "ligand_id": "ligand_10163"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 4 species

### Pb^[2+] + Chloride ion
**metal_id:** metal_125 | **ligand_id:** ligand_10163 | **ligand_def_HxL:** ***  
**entries:** 32 | **species:** 4 | **vlm_count:** 32

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_334 | [M][L]<sup>2</sup>/[ML<sub>2</sub>(s)] | [ML2(s)] <=> [M] + [L]^2 | [M](aqueous), [L](aqueous), [ML2(s)](solid) | 2 |
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 10 |
| beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | [M] + [L]^2 <=> [ML2] | [ML2](aqueous), [M](aqueous), [L](aqueous) | 10 |
| beta_def_872 | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | [M] + [L]^3 <=> [ML3] | [ML3](aqueous), [M](aqueous), [L](aqueous) | 10 |

**vlm_ids:** vlm_177638, vlm_177639, vlm_177640, vlm_177641, vlm_177642, … vlm_177667, vlm_177668, vlm_177669 (32 listed)

**equilibrium_maps:** 8 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_29930 | 4 | 6 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_29931 | 4 | 6 | 19~29 °C | 2.85~3.15 M |
| ref_eq_net_29932 | 3 | 3 | 19~29 °C | 0.35~0.65 M |
| ref_eq_net_29933 | 3 | 3 | 19~29 °C | 0.55~0.85 M |
| ref_eq_net_29934 | 3 | 3 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_29935 | 3 | 3 | 19~29 °C | 1.85~2.15 M |
| ref_eq_net_29936 | 3 | 3 | 19~29 °C | 3.85~4.15 M |
| ref_eq_net_29937 | 3 | 3 | 19~29 °C | -0.15~0.15 M |

---

### Step 6: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_125 AND c.ligand_id = ligand_10163)",
  "limit": 40
}
```

[summary]
## search_stability — 32 row(s)

### `Pb^[2+]` + Chloride ion — 32 measurement(s)
metal_id: metal_125 | ligand_id: ligand_10163
ligand_HxL_def: *** | ligand_SMILES: ***

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_177638 | ref_eq_map_29811 | beta_def_812 | logK | 1.07 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177639 | ref_eq_map_29813 | beta_def_812 | logK | 0.87 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177640 | ref_eq_map_29814 | beta_def_812 | logK | 0.88 | 25 | 0.7 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177641 | ref_eq_map_29815 | beta_def_812 | logK | 0.9 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177642 | ref_eq_map_29816 | beta_def_812 | logK | 1 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177643 | ref_eq_map_29812 | beta_def_812 | logK | 1.12 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177644 | ref_eq_map_29817 | beta_def_812 | logK | 1.23 | 25 | 4 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177645 | ref_eq_map_29818 | beta_def_812 | logK | 1.55 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177646 | *** | beta_def_812 | ΔH | 8.8 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177647 | *** | beta_def_812 | ΔS | 59.4 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177648 | ref_eq_map_29811 | beta_def_840 | logK | 1.4 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_177649 | ref_eq_map_29813 | beta_def_840 | logK | 1.2 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_177650 | ref_eq_map_29814 | beta_def_840 | logK | 1.2 | 25 | 0.7 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_177651 | ref_eq_map_29815 | beta_def_840 | logK | 1.2 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_177652 | ref_eq_map_29816 | beta_def_840 | logK | 1.3 | 25 | 2 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_177653 | ref_eq_map_29812 | beta_def_840 | logK | 1.6 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_177654 | ref_eq_map_29817 | beta_def_840 | logK | 1.8 | 25 | 4 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_177655 | ref_eq_map_29818 | beta_def_840 | logK | 2.2 | 25 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_177656 | *** | beta_def_840 | ΔH | -12.6 | 25 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_177657 | *** | beta_def_840 | ΔS | -83.7 | 25 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_177658 | ref_eq_map_29811 | beta_def_872 | logK | 1.3 | 25 | 0.1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_177659 | ref_eq_map_29813 | beta_def_872 | logK | 1.1 | 25 | 0.5 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_177660 | ref_eq_map_29814 | beta_def_872 | logK | 1.1 | 25 | 0.7 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_177661 | ref_eq_map_29815 | beta_def_872 | logK | 1.1 | 25 | 1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_177662 | ref_eq_map_29816 | beta_def_872 | logK | 1.4 | 25 | 2 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_177663 | ref_eq_map_29812 | beta_def_872 | logK | 1.9 | 25 | 3 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_177664 | ref_eq_map_29817 | beta_def_872 | logK | 2.2 | 25 | 4 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_177665 | ref_eq_map_29818 | beta_def_872 | logK | 1.8 | 25 | 0 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_177666 | *** | beta_def_872 | ΔH | -4.2 | 25 | 0 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_177667 | *** | beta_def_872 | ΔS | -41.8 | 25 | 0 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_177668 | ref_eq_map_29812 | beta_def_334 | logK | -5 | 25 | 3 | `[ML2(s)] <=> [M] + [L]^2` | solid | [L] |  |
| vlm_177669 | ref_eq_map_29811 | beta_def_334 | logK | -4.78 | 25 | 0 | `[ML2(s)] <=> [M] + [L]^2` | solid | [L] |  |

---

### Step 7: `inspect_literature`
**Args:**
```json
{
  "prefix_id": "vlm_177638"
}
```

[summary]
## inspect_literature — vlm_177638 — 67 citation(s)

| lit_id | shortcut | citation |
|--------|----------|----------|
| lit_265 | 30RD | E. C. Righellato and C. W. Davies, Trans. Faraday Soc., 1930, 26, 592 |
| lit_276 | 31F | H. Fromherz, Z. Phys. Chem., 1931, A153, 376 |
| lit_278 | 31FL | H. Fromherz and K. H. Lih, Z. Phys. Chem., 1931, A153, 321, 376 |
| lit_488 | 38G | E. Guntelberg, Thesis, Copenhagen, 1938 |
| lit_602 | 42GN | A. B. Garrett, M. V. Noble, and S. Miller, J. Chem. Educ., 1942, 19, 485 |
| lit_673 | 44NG | M. V. Noble and A. B. Garrett, J. Amer. Chem. Soc., 1944, 66, 231 |
| lit_694 | 45Na | R. Nasanen, Ann. Acad. Sci. Fenn., 1945, AII, No. 13 |
| lit_816 | 49GGa | R. M. Garrels and F. T. Gucker, Jr., Chem. Rev., 1949, 44, 117 |
| lit_825 | 49Jb | J. C. James, J. Amer. Chem. Soc., 1949, 71, 3243 |
| lit_2107 | 55BPP | A. I. Biggs, M. H. Panckhurst, and H. N. Parton, Trans. Faraday Soc., 1955, 51,… |
| lit_2108 | 55BPR | A. I. Biggs, H. N. Parton, and R. A. Robinson, J. Amer. Chem. Soc., 1955, 77, 5… |
| lit_2160 | 55K | P. Kivalo, Suomen Kem., 1955, B28, 155 |
| lit_2199 | 55Na | G. H. Nancollas, J. Chem. Soc., 1955, 1458 |
| lit_1197 | 56Cc | B. Charreton, Bull. Soc. Chim. France, 1956, 323, 337, 347 |
| lit_2277 | 56P | P. Papoff, Suomen Kem., 1956, B29, 97 |
| lit_2452 | 57KL | P. Kivalo and R. Luoto, Suomen Kem., 1957, B30, 163 |
| lit_2512 | 57PCF | P. Papoff, M. A. Caliumi, and G. Ferrari, Ric. Sci., 1957, 27, suppl. A; Polaro… |
| lit_3036 | 59TCa | Ya. I. Turyan and N. G. Chebotar, Russ. J. Inorg. Chem., 1959, 4, 273 (599) |
| lit_3148 | 60FSS | Ya. D. Fridman, D. S. Sarbaev, and R. I. Sorochan, Russ. J. Inorg. Chem., 1960,… |
| lit_3453 | 61M | V. E. Mironov, Russ. J. Inorg. Chem., 1961, 6, 205 (405) |
| lit_3492 | 61NR | C. J. Nyman, D. K. Roe, and R. A. Plane, J. Amer. Chem. Soc., 1961, 83, 323 |
| lit_3675 | 62FCa | J. Faucherre and A. Crego, Bull. Soc. Chim. France, 1962, 1820 |
| lit_4133 | 63MFN | V. E. Mironov, V. A. Fedorov, and V. A. Nazarov, Russ. J. Inorg. Chem., 1963, 8… |
| lit_4140 | 63MKc | V. E. Mironov, F. Ya. Kulba, V. A. Fedorov, and O. B. Tikhomirov, Russ. J. Inor… |
| lit_4317 | 64AP | V. I. Altynov and B. V. Ptitsyn, Russ. J. Inorg. Chem., 1964, 9, 1301 (2407) |
| lit_4343 | 64BMa | E. Ya. Benyash and T. G. Maslakova, Russ. J. Inorg. Chem., 1964, 9, 1472 (2731) |
| lit_4486 | 64MK | V. E. Mironov, F. Ya. Kulba, and V. A. Fedorov, Russ. J. Inorg. Chem., 1964, 9,… |
| lit_4488 | 64MKb | V. E. Mironov, F. Ya. Kulba, V. A. Fedorov, and A. V. Fedorova, Russ. J. Inorg.… |
| lit_4810 | 65HP | G. P. Haight, Jr., and J. R. Peterson, Inorg. Chem., 1965, 4, 1073 |
| lit_4883 | 65MKF | V. E. Mironov, F. Ya. Kulba, and V. A. Fedorov, Russ. J. Inorg. Chem., 1965, 10… |
| lit_5433 | 66VSB | F. Vierling, G. Schorsch, and J. Bye, Rev. Chim. Miner., 1966, 3, 875 |
| lit_6479 | 69FKM | V. A. Fedorov, M. Ya. Kutuzova, and V. E. Mironov, Fiz. Khim. Khim. Tekhnol., 1… |
| lit_6520 | 69Hd | H. C. Helgeson, Amer. J. Sci., 1969, 267, 729 |
| lit_7036 | 70FS | V. A. Fedorov, N. P. Samsonova, and V. E. Mironov, Russ. J. Inorg. Chem., 1970,… |
| lit_7345 | 71BHa | A. M. Bond and G. Hefter, J. Electroanal. Chem., 1971, 31, 477 |
| lit_7820 | 71V | F. Vierling, Bull. Soc. Chim. France, 1971, 22, 25 |
| lit_8011 | 72FSL | V. A. Fedorov, L. P. Shishin, S. G. Likhacheva, A. V. Fedorova, and V. E. Miron… |
| lit_8330 | 72SF | N. P. Samsonova, V. A. Fedorov, and V. E. Mironov, Russ. J. Phys. Chem., 1972, … |
| lit_8468 | 73BH | A. M. Bond and G. Hefter, J. Electroanal. Chem., 1973, 42, 1 |
| lit_8591 | 73HH | M. H. Hutchinson and W. C. E. Higginson, J. Chem. Soc. Dalton, 1973, 1247 |
| lit_8891 | 73V | F. Vierling, Ann. Chim. (Paris), 1973, 8, 53 |
| lit_9515 | 75Fa | V. A. Fedorov, Soviet J. Coord. Chem., 1975, 1, 751 (890) |
| lit_9671 | 75Ma | L. Meites, Talanta, 1975, 22, 733 |
| lit_9982 | 76FS | V. A. Fedorov and L. P. Shishin, Russ. J. Phys. Chem., 1976, 50, 210 (356) |
| lit_10300 | 76YK | E. N. Yurchenko, G. R. Kolonin, G. P. Shironosova, and T. P. Aksenova, Russ. J.… |
| lit_10362 | 77BL | C. Birraux, J. C. Landry, and W. Haerdi, Anal. Chim. Acta, 1977, 90, 51 |
| lit_11061 | 79BKa | S. D. Brown and B. R. Kowalski, Anal. Chem., 1979, 51, 2133 |
| lit_1627 | 80LBa | M. Lovric and M. Branica, Croat. Chem. Acta, 1980, 53, 503 |
| lit_11630 | 80PPb | A. K. Prasad and B. Prasad, J. Indian Chem. Soc., 1980, 57, 155 |
| lit_11710 | 80TK | A. V. Tyulin and Yu. P. Khranilov, Soviet J. Coord. Chem., 1980, 6, 515 (1034) |
| lit_11821 | 81BYM | R. H. Byrne, R. W. Young, and W. L. Miller, J. Soln. Chem., 1981, 10, 243 |
| lit_12077 | 81RM | R. P. Rafalskii and A. P. Masalovich, Geochem. Int., 1981, 18, No. 6, 158 (1868) |
| lit_12234 | 82BMS | H. Bendiab, J. Meullemeestre, M. J. Schwing, and F. Vierling, J. Chem. Res. (S)… |
| lit_12495 | 82R | R. Rohl, Anal. Chim. Acta, 1982, 135, 99 |
| lit_12657 | 83BRS | M. Barrera, J. C. Rodriguez Placeres, J. A. Sanchez, and A. Arevalo, An. Quim.,… |
| lit_13103 | 84BM | R. H. Byrne and W. L. Miller, Amer. J. Sci., 1984, 284, 79 |
| lit_13293 | 84LSC | J. Lozar, L. Schuffenecker, G. Cudey, and J. B. Bourdef, Thermochim. Acta, 1984… |
| lit_13300 | 84MB | F. J. Millero and R. H. Byrne, Geochim. Cosmochim. Acta, 1984, 48, 1145 |
| lit_13408 | 84S | T. M. Seward, Geochim. Cosmochim. Acta, 1984, 48, 121 |
| lit_13812 | 85RP | J. C. Rodriguez Placeres, J. J. Perez Canino, F. Ramos Steffens, and A. Arevalo… |
| lit_14794 | 88FSd | D. Ferri and F. Salvatore, Ann. Chim. (Rome), 1988, 78, 509 |
| lit_14877 | 88LS | T. Li, S. Shi, and Y. Hu, Wuji Huaxue (J. Inorg. Chem.), 1989, 4, 117 |
| lit_14936 | 88PB | I. Pizeta and M. Branica, J. Electroanal. Chem., 1988, 250, 293 |
| lit_15204 | 89HS | A. Hannisdal and K. H. Schroder, J. Electroanal. Chem., 1989, 263, 23 |
| lit_15558 | 90H | G. T. Hefter, Polyhedron, 1990, 9, 2429 |
| lit_16375 | 92ZB | M. Zelic and M. Branica, Anal. Chim. Acta, 1992, 268, 275 |
| lit_16696 | 94CIO | X. Chem, R. M. Izatt, and J. L. Oscarson, Chem. Rev., 1994, 94, 467 |

---

### Step 8: `inspect_literature`
**Args:**
```json
{
  "prefix_id": "vlm_177645"
}
```

[summary]
## inspect_literature — vlm_177645 — 67 citation(s)

| lit_id | shortcut | citation |
|--------|----------|----------|
| lit_265 | 30RD | E. C. Righellato and C. W. Davies, Trans. Faraday Soc., 1930, 26, 592 |
| lit_276 | 31F | H. Fromherz, Z. Phys. Chem., 1931, A153, 376 |
| lit_278 | 31FL | H. Fromherz and K. H. Lih, Z. Phys. Chem., 1931, A153, 321, 376 |
| lit_488 | 38G | E. Guntelberg, Thesis, Copenhagen, 1938 |
| lit_602 | 42GN | A. B. Garrett, M. V. Noble, and S. Miller, J. Chem. Educ., 1942, 19, 485 |
| lit_673 | 44NG | M. V. Noble and A. B. Garrett, J. Amer. Chem. Soc., 1944, 66, 231 |
| lit_694 | 45Na | R. Nasanen, Ann. Acad. Sci. Fenn., 1945, AII, No. 13 |
| lit_816 | 49GGa | R. M. Garrels and F. T. Gucker, Jr., Chem. Rev., 1949, 44, 117 |
| lit_825 | 49Jb | J. C. James, J. Amer. Chem. Soc., 1949, 71, 3243 |
| lit_2107 | 55BPP | A. I. Biggs, M. H. Panckhurst, and H. N. Parton, Trans. Faraday Soc., 1955, 51,… |
| lit_2108 | 55BPR | A. I. Biggs, H. N. Parton, and R. A. Robinson, J. Amer. Chem. Soc., 1955, 77, 5… |
| lit_2160 | 55K | P. Kivalo, Suomen Kem., 1955, B28, 155 |
| lit_2199 | 55Na | G. H. Nancollas, J. Chem. Soc., 1955, 1458 |
| lit_1197 | 56Cc | B. Charreton, Bull. Soc. Chim. France, 1956, 323, 337, 347 |
| lit_2277 | 56P | P. Papoff, Suomen Kem., 1956, B29, 97 |
| lit_2452 | 57KL | P. Kivalo and R. Luoto, Suomen Kem., 1957, B30, 163 |
| lit_2512 | 57PCF | P. Papoff, M. A. Caliumi, and G. Ferrari, Ric. Sci., 1957, 27, suppl. A; Polaro… |
| lit_3036 | 59TCa | Ya. I. Turyan and N. G. Chebotar, Russ. J. Inorg. Chem., 1959, 4, 273 (599) |
| lit_3148 | 60FSS | Ya. D. Fridman, D. S. Sarbaev, and R. I. Sorochan, Russ. J. Inorg. Chem., 1960,… |
| lit_3453 | 61M | V. E. Mironov, Russ. J. Inorg. Chem., 1961, 6, 205 (405) |
| lit_3492 | 61NR | C. J. Nyman, D. K. Roe, and R. A. Plane, J. Amer. Chem. Soc., 1961, 83, 323 |
| lit_3675 | 62FCa | J. Faucherre and A. Crego, Bull. Soc. Chim. France, 1962, 1820 |
| lit_4133 | 63MFN | V. E. Mironov, V. A. Fedorov, and V. A. Nazarov, Russ. J. Inorg. Chem., 1963, 8… |
| lit_4140 | 63MKc | V. E. Mironov, F. Ya. Kulba, V. A. Fedorov, and O. B. Tikhomirov, Russ. J. Inor… |
| lit_4317 | 64AP | V. I. Altynov and B. V. Ptitsyn, Russ. J. Inorg. Chem., 1964, 9, 1301 (2407) |
| lit_4343 | 64BMa | E. Ya. Benyash and T. G. Maslakova, Russ. J. Inorg. Chem., 1964, 9, 1472 (2731) |
| lit_4486 | 64MK | V. E. Mironov, F. Ya. Kulba, and V. A. Fedorov, Russ. J. Inorg. Chem., 1964, 9,… |
| lit_4488 | 64MKb | V. E. Mironov, F. Ya. Kulba, V. A. Fedorov, and A. V. Fedorova, Russ. J. Inorg.… |
| lit_4810 | 65HP | G. P. Haight, Jr., and J. R. Peterson, Inorg. Chem., 1965, 4, 1073 |
| lit_4883 | 65MKF | V. E. Mironov, F. Ya. Kulba, and V. A. Fedorov, Russ. J. Inorg. Chem., 1965, 10… |
| lit_5433 | 66VSB | F. Vierling, G. Schorsch, and J. Bye, Rev. Chim. Miner., 1966, 3, 875 |
| lit_6479 | 69FKM | V. A. Fedorov, M. Ya. Kutuzova, and V. E. Mironov, Fiz. Khim. Khim. Tekhnol., 1… |
| lit_6520 | 69Hd | H. C. Helgeson, Amer. J. Sci., 1969, 267, 729 |
| lit_7036 | 70FS | V. A. Fedorov, N. P. Samsonova, and V. E. Mironov, Russ. J. Inorg. Chem., 1970,… |
| lit_7345 | 71BHa | A. M. Bond and G. Hefter, J. Electroanal. Chem., 1971, 31, 477 |
| lit_7820 | 71V | F. Vierling, Bull. Soc. Chim. France, 1971, 22, 25 |
| lit_8011 | 72FSL | V. A. Fedorov, L. P. Shishin, S. G. Likhacheva, A. V. Fedorova, and V. E. Miron… |
| lit_8330 | 72SF | N. P. Samsonova, V. A. Fedorov, and V. E. Mironov, Russ. J. Phys. Chem., 1972, … |
| lit_8468 | 73BH | A. M. Bond and G. Hefter, J. Electroanal. Chem., 1973, 42, 1 |
| lit_8591 | 73HH | M. H. Hutchinson and W. C. E. Higginson, J. Chem. Soc. Dalton, 1973, 1247 |
| lit_8891 | 73V | F. Vierling, Ann. Chim. (Paris), 1973, 8, 53 |
| lit_9515 | 75Fa | V. A. Fedorov, Soviet J. Coord. Chem., 1975, 1, 751 (890) |
| lit_9671 | 75Ma | L. Meites, Talanta, 1975, 22, 733 |
| lit_9982 | 76FS | V. A. Fedorov and L. P. Shishin, Russ. J. Phys. Chem., 1976, 50, 210 (356) |
| lit_10300 | 76YK | E. N. Yurchenko, G. R. Kolonin, G. P. Shironosova, and T. P. Aksenova, Russ. J.… |
| lit_10362 | 77BL | C. Birraux, J. C. Landry, and W. Haerdi, Anal. Chim. Acta, 1977, 90, 51 |
| lit_11061 | 79BKa | S. D. Brown and B. R. Kowalski, Anal. Chem., 1979, 51, 2133 |
| lit_1627 | 80LBa | M. Lovric and M. Branica, Croat. Chem. Acta, 1980, 53, 503 |
| lit_11630 | 80PPb | A. K. Prasad and B. Prasad, J. Indian Chem. Soc., 1980, 57, 155 |
| lit_11710 | 80TK | A. V. Tyulin and Yu. P. Khranilov, Soviet J. Coord. Chem., 1980, 6, 515 (1034) |
| lit_11821 | 81BYM | R. H. Byrne, R. W. Young, and W. L. Miller, J. Soln. Chem., 1981, 10, 243 |
| lit_12077 | 81RM | R. P. Rafalskii and A. P. Masalovich, Geochem. Int., 1981, 18, No. 6, 158 (1868) |
| lit_12234 | 82BMS | H. Bendiab, J. Meullemeestre, M. J. Schwing, and F. Vierling, J. Chem. Res. (S)… |
| lit_12495 | 82R | R. Rohl, Anal. Chim. Acta, 1982, 135, 99 |
| lit_12657 | 83BRS | M. Barrera, J. C. Rodriguez Placeres, J. A. Sanchez, and A. Arevalo, An. Quim.,… |
| lit_13103 | 84BM | R. H. Byrne and W. L. Miller, Amer. J. Sci., 1984, 284, 79 |
| lit_13293 | 84LSC | J. Lozar, L. Schuffenecker, G. Cudey, and J. B. Bourdef, Thermochim. Acta, 1984… |
| lit_13300 | 84MB | F. J. Millero and R. H. Byrne, Geochim. Cosmochim. Acta, 1984, 48, 1145 |
| lit_13408 | 84S | T. M. Seward, Geochim. Cosmochim. Acta, 1984, 48, 121 |
| lit_13812 | 85RP | J. C. Rodriguez Placeres, J. J. Perez Canino, F. Ramos Steffens, and A. Arevalo… |
| lit_14794 | 88FSd | D. Ferri and F. Salvatore, Ann. Chim. (Rome), 1988, 78, 509 |
| lit_14877 | 88LS | T. Li, S. Shi, and Y. Hu, Wuji Huaxue (J. Inorg. Chem.), 1989, 4, 117 |
| lit_14936 | 88PB | I. Pizeta and M. Branica, J. Electroanal. Chem., 1988, 250, 293 |
| lit_15204 | 89HS | A. Hannisdal and K. H. Schroder, J. Electroanal. Chem., 1989, 263, 23 |
| lit_15558 | 90H | G. T. Hefter, Polyhedron, 1990, 9, 2429 |
| lit_16375 | 92ZB | M. Zelic and M. Branica, Anal. Chim. Acta, 1992, 268, 275 |
| lit_16696 | 94CIO | X. Chem, R. M. Izatt, and J. L. Oscarson, Chem. Rev., 1994, 94, 467 |

---

### Step 9: `inspect_literature`
**Args:**
```json
{
  "prefix_id": "vlm_177655"
}
```

[summary]
## inspect_literature — vlm_177655 — 67 citation(s)

| lit_id | shortcut | citation |
|--------|----------|----------|
| lit_265 | 30RD | E. C. Righellato and C. W. Davies, Trans. Faraday Soc., 1930, 26, 592 |
| lit_276 | 31F | H. Fromherz, Z. Phys. Chem., 1931, A153, 376 |
| lit_278 | 31FL | H. Fromherz and K. H. Lih, Z. Phys. Chem., 1931, A153, 321, 376 |
| lit_488 | 38G | E. Guntelberg, Thesis, Copenhagen, 1938 |
| lit_602 | 42GN | A. B. Garrett, M. V. Noble, and S. Miller, J. Chem. Educ., 1942, 19, 485 |
| lit_673 | 44NG | M. V. Noble and A. B. Garrett, J. Amer. Chem. Soc., 1944, 66, 231 |
| lit_694 | 45Na | R. Nasanen, Ann. Acad. Sci. Fenn., 1945, AII, No. 13 |
| lit_816 | 49GGa | R. M. Garrels and F. T. Gucker, Jr., Chem. Rev., 1949, 44, 117 |
| lit_825 | 49Jb | J. C. James, J. Amer. Chem. Soc., 1949, 71, 3243 |
| lit_2107 | 55BPP | A. I. Biggs, M. H. Panckhurst, and H. N. Parton, Trans. Faraday Soc., 1955, 51,… |
| lit_2108 | 55BPR | A. I. Biggs, H. N. Parton, and R. A. Robinson, J. Amer. Chem. Soc., 1955, 77, 5… |
| lit_2160 | 55K | P. Kivalo, Suomen Kem., 1955, B28, 155 |
| lit_2199 | 55Na | G. H. Nancollas, J. Chem. Soc., 1955, 1458 |
| lit_1197 | 56Cc | B. Charreton, Bull. Soc. Chim. France, 1956, 323, 337, 347 |
| lit_2277 | 56P | P. Papoff, Suomen Kem., 1956, B29, 97 |
| lit_2452 | 57KL | P. Kivalo and R. Luoto, Suomen Kem., 1957, B30, 163 |
| lit_2512 | 57PCF | P. Papoff, M. A. Caliumi, and G. Ferrari, Ric. Sci., 1957, 27, suppl. A; Polaro… |
| lit_3036 | 59TCa | Ya. I. Turyan and N. G. Chebotar, Russ. J. Inorg. Chem., 1959, 4, 273 (599) |
| lit_3148 | 60FSS | Ya. D. Fridman, D. S. Sarbaev, and R. I. Sorochan, Russ. J. Inorg. Chem., 1960,… |
| lit_3453 | 61M | V. E. Mironov, Russ. J. Inorg. Chem., 1961, 6, 205 (405) |
| lit_3492 | 61NR | C. J. Nyman, D. K. Roe, and R. A. Plane, J. Amer. Chem. Soc., 1961, 83, 323 |
| lit_3675 | 62FCa | J. Faucherre and A. Crego, Bull. Soc. Chim. France, 1962, 1820 |
| lit_4133 | 63MFN | V. E. Mironov, V. A. Fedorov, and V. A. Nazarov, Russ. J. Inorg. Chem., 1963, 8… |
| lit_4140 | 63MKc | V. E. Mironov, F. Ya. Kulba, V. A. Fedorov, and O. B. Tikhomirov, Russ. J. Inor… |
| lit_4317 | 64AP | V. I. Altynov and B. V. Ptitsyn, Russ. J. Inorg. Chem., 1964, 9, 1301 (2407) |
| lit_4343 | 64BMa | E. Ya. Benyash and T. G. Maslakova, Russ. J. Inorg. Chem., 1964, 9, 1472 (2731) |
| lit_4486 | 64MK | V. E. Mironov, F. Ya. Kulba, and V. A. Fedorov, Russ. J. Inorg. Chem., 1964, 9,… |
| lit_4488 | 64MKb | V. E. Mironov, F. Ya. Kulba, V. A. Fedorov, and A. V. Fedorova, Russ. J. Inorg.… |
| lit_4810 | 65HP | G. P. Haight, Jr., and J. R. Peterson, Inorg. Chem., 1965, 4, 1073 |
| lit_4883 | 65MKF | V. E. Mironov, F. Ya. Kulba, and V. A. Fedorov, Russ. J. Inorg. Chem., 1965, 10… |
| lit_5433 | 66VSB | F. Vierling, G. Schorsch, and J. Bye, Rev. Chim. Miner., 1966, 3, 875 |
| lit_6479 | 69FKM | V. A. Fedorov, M. Ya. Kutuzova, and V. E. Mironov, Fiz. Khim. Khim. Tekhnol., 1… |
| lit_6520 | 69Hd | H. C. Helgeson, Amer. J. Sci., 1969, 267, 729 |
| lit_7036 | 70FS | V. A. Fedorov, N. P. Samsonova, and V. E. Mironov, Russ. J. Inorg. Chem., 1970,… |
| lit_7345 | 71BHa | A. M. Bond and G. Hefter, J. Electroanal. Chem., 1971, 31, 477 |
| lit_7820 | 71V | F. Vierling, Bull. Soc. Chim. France, 1971, 22, 25 |
| lit_8011 | 72FSL | V. A. Fedorov, L. P. Shishin, S. G. Likhacheva, A. V. Fedorova, and V. E. Miron… |
| lit_8330 | 72SF | N. P. Samsonova, V. A. Fedorov, and V. E. Mironov, Russ. J. Phys. Chem., 1972, … |
| lit_8468 | 73BH | A. M. Bond and G. Hefter, J. Electroanal. Chem., 1973, 42, 1 |
| lit_8591 | 73HH | M. H. Hutchinson and W. C. E. Higginson, J. Chem. Soc. Dalton, 1973, 1247 |
| lit_8891 | 73V | F. Vierling, Ann. Chim. (Paris), 1973, 8, 53 |
| lit_9515 | 75Fa | V. A. Fedorov, Soviet J. Coord. Chem., 1975, 1, 751 (890) |
| lit_9671 | 75Ma | L. Meites, Talanta, 1975, 22, 733 |
| lit_9982 | 76FS | V. A. Fedorov and L. P. Shishin, Russ. J. Phys. Chem., 1976, 50, 210 (356) |
| lit_10300 | 76YK | E. N. Yurchenko, G. R. Kolonin, G. P. Shironosova, and T. P. Aksenova, Russ. J.… |
| lit_10362 | 77BL | C. Birraux, J. C. Landry, and W. Haerdi, Anal. Chim. Acta, 1977, 90, 51 |
| lit_11061 | 79BKa | S. D. Brown and B. R. Kowalski, Anal. Chem., 1979, 51, 2133 |
| lit_1627 | 80LBa | M. Lovric and M. Branica, Croat. Chem. Acta, 1980, 53, 503 |
| lit_11630 | 80PPb | A. K. Prasad and B. Prasad, J. Indian Chem. Soc., 1980, 57, 155 |
| lit_11710 | 80TK | A. V. Tyulin and Yu. P. Khranilov, Soviet J. Coord. Chem., 1980, 6, 515 (1034) |
| lit_11821 | 81BYM | R. H. Byrne, R. W. Young, and W. L. Miller, J. Soln. Chem., 1981, 10, 243 |
| lit_12077 | 81RM | R. P. Rafalskii and A. P. Masalovich, Geochem. Int., 1981, 18, No. 6, 158 (1868) |
| lit_12234 | 82BMS | H. Bendiab, J. Meullemeestre, M. J. Schwing, and F. Vierling, J. Chem. Res. (S)… |
| lit_12495 | 82R | R. Rohl, Anal. Chim. Acta, 1982, 135, 99 |
| lit_12657 | 83BRS | M. Barrera, J. C. Rodriguez Placeres, J. A. Sanchez, and A. Arevalo, An. Quim.,… |
| lit_13103 | 84BM | R. H. Byrne and W. L. Miller, Amer. J. Sci., 1984, 284, 79 |
| lit_13293 | 84LSC | J. Lozar, L. Schuffenecker, G. Cudey, and J. B. Bourdef, Thermochim. Acta, 1984… |
| lit_13300 | 84MB | F. J. Millero and R. H. Byrne, Geochim. Cosmochim. Acta, 1984, 48, 1145 |
| lit_13408 | 84S | T. M. Seward, Geochim. Cosmochim. Acta, 1984, 48, 121 |
| lit_13812 | 85RP | J. C. Rodriguez Placeres, J. J. Perez Canino, F. Ramos Steffens, and A. Arevalo… |
| lit_14794 | 88FSd | D. Ferri and F. Salvatore, Ann. Chim. (Rome), 1988, 78, 509 |
| lit_14877 | 88LS | T. Li, S. Shi, and Y. Hu, Wuji Huaxue (J. Inorg. Chem.), 1989, 4, 117 |
| lit_14936 | 88PB | I. Pizeta and M. Branica, J. Electroanal. Chem., 1988, 250, 293 |
| lit_15204 | 89HS | A. Hannisdal and K. H. Schroder, J. Electroanal. Chem., 1989, 263, 23 |
| lit_15558 | 90H | G. T. Hefter, Polyhedron, 1990, 9, 2429 |
| lit_16375 | 92ZB | M. Zelic and M. Branica, Anal. Chim. Acta, 1992, 268, 275 |
| lit_16696 | 94CIO | X. Chem, R. M. Izatt, and J. L. Oscarson, Chem. Rev., 1994, 94, 467 |

---

### Step 10: `inspect_literature`
**Args:**
```json
{
  "prefix_id": "vlm_177665"
}
```

[summary]
## inspect_literature — vlm_177665 — 67 citation(s)

| lit_id | shortcut | citation |
|--------|----------|----------|
| lit_265 | 30RD | E. C. Righellato and C. W. Davies, Trans. Faraday Soc., 1930, 26, 592 |
| lit_276 | 31F | H. Fromherz, Z. Phys. Chem., 1931, A153, 376 |
| lit_278 | 31FL | H. Fromherz and K. H. Lih, Z. Phys. Chem., 1931, A153, 321, 376 |
| lit_488 | 38G | E. Guntelberg, Thesis, Copenhagen, 1938 |
| lit_602 | 42GN | A. B. Garrett, M. V. Noble, and S. Miller, J. Chem. Educ., 1942, 19, 485 |
| lit_673 | 44NG | M. V. Noble and A. B. Garrett, J. Amer. Chem. Soc., 1944, 66, 231 |
| lit_694 | 45Na | R. Nasanen, Ann. Acad. Sci. Fenn., 1945, AII, No. 13 |
| lit_816 | 49GGa | R. M. Garrels and F. T. Gucker, Jr., Chem. Rev., 1949, 44, 117 |
| lit_825 | 49Jb | J. C. James, J. Amer. Chem. Soc., 1949, 71, 3243 |
| lit_2107 | 55BPP | A. I. Biggs, M. H. Panckhurst, and H. N. Parton, Trans. Faraday Soc., 1955, 51,… |
| lit_2108 | 55BPR | A. I. Biggs, H. N. Parton, and R. A. Robinson, J. Amer. Chem. Soc., 1955, 77, 5… |
| lit_2160 | 55K | P. Kivalo, Suomen Kem., 1955, B28, 155 |
| lit_2199 | 55Na | G. H. Nancollas, J. Chem. Soc., 1955, 1458 |
| lit_1197 | 56Cc | B. Charreton, Bull. Soc. Chim. France, 1956, 323, 337, 347 |
| lit_2277 | 56P | P. Papoff, Suomen Kem., 1956, B29, 97 |
| lit_2452 | 57KL | P. Kivalo and R. Luoto, Suomen Kem., 1957, B30, 163 |
| lit_2512 | 57PCF | P. Papoff, M. A. Caliumi, and G. Ferrari, Ric. Sci., 1957, 27, suppl. A; Polaro… |
| lit_3036 | 59TCa | Ya. I. Turyan and N. G. Chebotar, Russ. J. Inorg. Chem., 1959, 4, 273 (599) |
| lit_3148 | 60FSS | Ya. D. Fridman, D. S. Sarbaev, and R. I. Sorochan, Russ. J. Inorg. Chem., 1960,… |
| lit_3453 | 61M | V. E. Mironov, Russ. J. Inorg. Chem., 1961, 6, 205 (405) |
| lit_3492 | 61NR | C. J. Nyman, D. K. Roe, and R. A. Plane, J. Amer. Chem. Soc., 1961, 83, 323 |
| lit_3675 | 62FCa | J. Faucherre and A. Crego, Bull. Soc. Chim. France, 1962, 1820 |
| lit_4133 | 63MFN | V. E. Mironov, V. A. Fedorov, and V. A. Nazarov, Russ. J. Inorg. Chem., 1963, 8… |
| lit_4140 | 63MKc | V. E. Mironov, F. Ya. Kulba, V. A. Fedorov, and O. B. Tikhomirov, Russ. J. Inor… |
| lit_4317 | 64AP | V. I. Altynov and B. V. Ptitsyn, Russ. J. Inorg. Chem., 1964, 9, 1301 (2407) |
| lit_4343 | 64BMa | E. Ya. Benyash and T. G. Maslakova, Russ. J. Inorg. Chem., 1964, 9, 1472 (2731) |
| lit_4486 | 64MK | V. E. Mironov, F. Ya. Kulba, and V. A. Fedorov, Russ. J. Inorg. Chem., 1964, 9,… |
| lit_4488 | 64MKb | V. E. Mironov, F. Ya. Kulba, V. A. Fedorov, and A. V. Fedorova, Russ. J. Inorg.… |
| lit_4810 | 65HP | G. P. Haight, Jr., and J. R. Peterson, Inorg. Chem., 1965, 4, 1073 |
| lit_4883 | 65MKF | V. E. Mironov, F. Ya. Kulba, and V. A. Fedorov, Russ. J. Inorg. Chem., 1965, 10… |
| lit_5433 | 66VSB | F. Vierling, G. Schorsch, and J. Bye, Rev. Chim. Miner., 1966, 3, 875 |
| lit_6479 | 69FKM | V. A. Fedorov, M. Ya. Kutuzova, and V. E. Mironov, Fiz. Khim. Khim. Tekhnol., 1… |
| lit_6520 | 69Hd | H. C. Helgeson, Amer. J. Sci., 1969, 267, 729 |
| lit_7036 | 70FS | V. A. Fedorov, N. P. Samsonova, and V. E. Mironov, Russ. J. Inorg. Chem., 1970,… |
| lit_7345 | 71BHa | A. M. Bond and G. Hefter, J. Electroanal. Chem., 1971, 31, 477 |
| lit_7820 | 71V | F. Vierling, Bull. Soc. Chim. France, 1971, 22, 25 |
| lit_8011 | 72FSL | V. A. Fedorov, L. P. Shishin, S. G. Likhacheva, A. V. Fedorova, and V. E. Miron… |
| lit_8330 | 72SF | N. P. Samsonova, V. A. Fedorov, and V. E. Mironov, Russ. J. Phys. Chem., 1972, … |
| lit_8468 | 73BH | A. M. Bond and G. Hefter, J. Electroanal. Chem., 1973, 42, 1 |
| lit_8591 | 73HH | M. H. Hutchinson and W. C. E. Higginson, J. Chem. Soc. Dalton, 1973, 1247 |
| lit_8891 | 73V | F. Vierling, Ann. Chim. (Paris), 1973, 8, 53 |
| lit_9515 | 75Fa | V. A. Fedorov, Soviet J. Coord. Chem., 1975, 1, 751 (890) |
| lit_9671 | 75Ma | L. Meites, Talanta, 1975, 22, 733 |
| lit_9982 | 76FS | V. A. Fedorov and L. P. Shishin, Russ. J. Phys. Chem., 1976, 50, 210 (356) |
| lit_10300 | 76YK | E. N. Yurchenko, G. R. Kolonin, G. P. Shironosova, and T. P. Aksenova, Russ. J.… |
| lit_10362 | 77BL | C. Birraux, J. C. Landry, and W. Haerdi, Anal. Chim. Acta, 1977, 90, 51 |
| lit_11061 | 79BKa | S. D. Brown and B. R. Kowalski, Anal. Chem., 1979, 51, 2133 |
| lit_1627 | 80LBa | M. Lovric and M. Branica, Croat. Chem. Acta, 1980, 53, 503 |
| lit_11630 | 80PPb | A. K. Prasad and B. Prasad, J. Indian Chem. Soc., 1980, 57, 155 |
| lit_11710 | 80TK | A. V. Tyulin and Yu. P. Khranilov, Soviet J. Coord. Chem., 1980, 6, 515 (1034) |
| lit_11821 | 81BYM | R. H. Byrne, R. W. Young, and W. L. Miller, J. Soln. Chem., 1981, 10, 243 |
| lit_12077 | 81RM | R. P. Rafalskii and A. P. Masalovich, Geochem. Int., 1981, 18, No. 6, 158 (1868) |
| lit_12234 | 82BMS | H. Bendiab, J. Meullemeestre, M. J. Schwing, and F. Vierling, J. Chem. Res. (S)… |
| lit_12495 | 82R | R. Rohl, Anal. Chim. Acta, 1982, 135, 99 |
| lit_12657 | 83BRS | M. Barrera, J. C. Rodriguez Placeres, J. A. Sanchez, and A. Arevalo, An. Quim.,… |
| lit_13103 | 84BM | R. H. Byrne and W. L. Miller, Amer. J. Sci., 1984, 284, 79 |
| lit_13293 | 84LSC | J. Lozar, L. Schuffenecker, G. Cudey, and J. B. Bourdef, Thermochim. Acta, 1984… |
| lit_13300 | 84MB | F. J. Millero and R. H. Byrne, Geochim. Cosmochim. Acta, 1984, 48, 1145 |
| lit_13408 | 84S | T. M. Seward, Geochim. Cosmochim. Acta, 1984, 48, 121 |
| lit_13812 | 85RP | J. C. Rodriguez Placeres, J. J. Perez Canino, F. Ramos Steffens, and A. Arevalo… |
| lit_14794 | 88FSd | D. Ferri and F. Salvatore, Ann. Chim. (Rome), 1988, 78, 509 |
| lit_14877 | 88LS | T. Li, S. Shi, and Y. Hu, Wuji Huaxue (J. Inorg. Chem.), 1989, 4, 117 |
| lit_14936 | 88PB | I. Pizeta and M. Branica, J. Electroanal. Chem., 1988, 250, 293 |
| lit_15204 | 89HS | A. Hannisdal and K. H. Schroder, J. Electroanal. Chem., 1989, 263, 23 |
| lit_15558 | 90H | G. T. Hefter, Polyhedron, 1990, 9, 2429 |
| lit_16375 | 92ZB | M. Zelic and M. Branica, Anal. Chim. Acta, 1992, 268, 275 |
| lit_16696 | 94CIO | X. Chem, R. M. Izatt, and J. L. Oscarson, Chem. Rev., 1994, 94, 467 |

---
