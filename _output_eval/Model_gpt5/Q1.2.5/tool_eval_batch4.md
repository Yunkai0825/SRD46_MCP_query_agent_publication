# Q1.2.5 — Tool Results (batch 4)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "lead",
  "symbol": "Pb",
  "limit": 10
}
```

[summary]
## search_metals — 10 result(s)

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

### Step 6: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id = metal_125 AND c.ligand_id = ligand_10163 AND nd.beta_definition_id IN (beta_def_812, beta_def_840, beta_def_872))",
  "order_by": "n.network_db_id ASC",
  "limit": 12,
  "ligand_similarity": false
}
```

[summary]
## search_networks — 26 row(s)

> **Reference equilibrium networks** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### `Pb^[2+]` + Chloride ion — 8 network(s)
metal_id: metal_125 | ligand_id: ligand_10163 | ligand_def_HxL: *** | ligand_SMILES: ***

| beta_def | equation |
|----------|----------|
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |
| beta_def_872 | ``[M] + [L]^3 <=> [ML3]`` |
| beta_def_334 | ``[ML2(s)] <=> [M] + [L]^2`` |
| beta_def_812 | ``[M] + [L] <=> [ML]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_29930 | 4 | 6 | 20~30 | -0.05~0.25 | 4 | 4 diff beta_def | logK | -4.78~1.4 |
| ref_eq_net_29931 | 4 | 6 | 19~29 | 2.85~3.15 | 4 | 4 diff beta_def | logK | -5~1.9 |
| ref_eq_net_29932 | 3 | 3 | 19~29 | 0.35~0.65 | 3 | beta_def_812; beta_def_872; beta_def_840 | logK | 0.87~1.2 |
| ref_eq_net_29933 | 3 | 3 | 19~29 | 0.55~0.85 | 3 | beta_def_812; beta_def_872; beta_def_840 | logK | 0.88~1.2 |
| ref_eq_net_29934 | 3 | 3 | 19~29 | 0.85~1.15 | 3 | beta_def_812; beta_def_872; beta_def_840 | logK | 0.9~1.2 |
| ref_eq_net_29935 | 3 | 3 | 19~29 | 1.85~2.15 | 3 | beta_def_812; beta_def_840; beta_def_872 | logK | 1~1.4 |
| ref_eq_net_29936 | 3 | 3 | 19~29 | 3.85~4.15 | 3 | beta_def_812; beta_def_840; beta_def_872 | logK | 1.23~2.2 |
| ref_eq_net_29937 | 3 | 3 | 19~29 | -0.15~0.15 | 3 | beta_def_812; beta_def_872; beta_def_840 | logK | 1.55~2.2 |

#### Reference-state network: ref_eq_net_29930 (4 nodes)
> First network — reference conditions (T 20~30 °C, I -0.05~0.25 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_334 | ``[ML2(s)] <=> [M] + [L]^2`` | logK | -4.78 |
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 1.07 |
| beta_def_872 | ``[M] + [L]^3 <=> [ML3]`` | logK | 1.3 |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` | logK | 1.4 |

---

### Step 7: `search_citations`
**Args:**
```json
{
  "where": "(rv.vlm_id = vlm_177638)"
}
```

[summary]
## search_citations — 50 row(s)

| example_vlm_id | vlm_count | lit_id | shortcut | citation |
|----------------|-----------|--------|----------|----------|
| vlm_177638 | 1 | lit_265 | 30RD | E. C. Righellato and C. W. Davies, Trans. Faraday Soc., 1930, 26, 592 |
| vlm_177638 | 1 | lit_276 | 31F | H. Fromherz, Z. Phys. Chem., 1931, A153, 376 |
| vlm_177638 | 1 | lit_278 | 31FL | H. Fromherz and K. H. Lih, Z. Phys. Chem., 1931, A153, 321, 376 |
| vlm_177638 | 1 | lit_488 | 38G | E. Guntelberg, Thesis, Copenhagen, 1938 |
| vlm_177638 | 1 | lit_602 | 42GN | A. B. Garrett, M. V. Noble, and S. Miller, J. Chem. Educ., 1942, 19, 485 |
| vlm_177638 | 1 | lit_673 | 44NG | M. V. Noble and A. B. Garrett, J. Amer. Chem. Soc., 1944, 66, 231 |
| vlm_177638 | 1 | lit_694 | 45Na | R. Nasanen, Ann. Acad. Sci. Fenn., 1945, AII, No. 13 |
| vlm_177638 | 1 | lit_816 | 49GGa | R. M. Garrels and F. T. Gucker, Jr., Chem. Rev., 1949, 44, 117 |
| vlm_177638 | 1 | lit_825 | 49Jb | J. C. James, J. Amer. Chem. Soc., 1949, 71, 3243 |
| vlm_177638 | 1 | lit_1197 | 56Cc | B. Charreton, Bull. Soc. Chim. France, 1956, 323, 337, 347 |
| vlm_177638 | 1 | lit_1627 | 80LBa | M. Lovric and M. Branica, Croat. Chem. Acta, 1980, 53, 503 |
| vlm_177638 | 1 | lit_2107 | 55BPP | A. I. Biggs, M. H. Panckhurst, and H. N. Parton, Trans. Faraday Soc., 1955, 51,… |
| vlm_177638 | 1 | lit_2108 | 55BPR | A. I. Biggs, H. N. Parton, and R. A. Robinson, J. Amer. Chem. Soc., 1955, 77, 5… |
| vlm_177638 | 1 | lit_2160 | 55K | P. Kivalo, Suomen Kem., 1955, B28, 155 |
| vlm_177638 | 1 | lit_2199 | 55Na | G. H. Nancollas, J. Chem. Soc., 1955, 1458 |
| vlm_177638 | 1 | lit_2277 | 56P | P. Papoff, Suomen Kem., 1956, B29, 97 |
| vlm_177638 | 1 | lit_2452 | 57KL | P. Kivalo and R. Luoto, Suomen Kem., 1957, B30, 163 |
| vlm_177638 | 1 | lit_2512 | 57PCF | P. Papoff, M. A. Caliumi, and G. Ferrari, Ric. Sci., 1957, 27, suppl. A; Polaro… |
| vlm_177638 | 1 | lit_3036 | 59TCa | Ya. I. Turyan and N. G. Chebotar, Russ. J. Inorg. Chem., 1959, 4, 273 (599) |
| vlm_177638 | 1 | lit_3148 | 60FSS | Ya. D. Fridman, D. S. Sarbaev, and R. I. Sorochan, Russ. J. Inorg. Chem., 1960,… |
| vlm_177638 | 1 | lit_3453 | 61M | V. E. Mironov, Russ. J. Inorg. Chem., 1961, 6, 205 (405) |
| vlm_177638 | 1 | lit_3492 | 61NR | C. J. Nyman, D. K. Roe, and R. A. Plane, J. Amer. Chem. Soc., 1961, 83, 323 |
| vlm_177638 | 1 | lit_3675 | 62FCa | J. Faucherre and A. Crego, Bull. Soc. Chim. France, 1962, 1820 |
| vlm_177638 | 1 | lit_4133 | 63MFN | V. E. Mironov, V. A. Fedorov, and V. A. Nazarov, Russ. J. Inorg. Chem., 1963, 8… |
| vlm_177638 | 1 | lit_4140 | 63MKc | V. E. Mironov, F. Ya. Kulba, V. A. Fedorov, and O. B. Tikhomirov, Russ. J. Inor… |
| vlm_177638 | 1 | lit_4317 | 64AP | V. I. Altynov and B. V. Ptitsyn, Russ. J. Inorg. Chem., 1964, 9, 1301 (2407) |
| vlm_177638 | 1 | lit_4343 | 64BMa | E. Ya. Benyash and T. G. Maslakova, Russ. J. Inorg. Chem., 1964, 9, 1472 (2731) |
| vlm_177638 | 1 | lit_4486 | 64MK | V. E. Mironov, F. Ya. Kulba, and V. A. Fedorov, Russ. J. Inorg. Chem., 1964, 9,… |
| vlm_177638 | 1 | lit_4488 | 64MKb | V. E. Mironov, F. Ya. Kulba, V. A. Fedorov, and A. V. Fedorova, Russ. J. Inorg.… |
| vlm_177638 | 1 | lit_4810 | 65HP | G. P. Haight, Jr., and J. R. Peterson, Inorg. Chem., 1965, 4, 1073 |
| vlm_177638 | 1 | lit_4883 | 65MKF | V. E. Mironov, F. Ya. Kulba, and V. A. Fedorov, Russ. J. Inorg. Chem., 1965, 10… |
| vlm_177638 | 1 | lit_5433 | 66VSB | F. Vierling, G. Schorsch, and J. Bye, Rev. Chim. Miner., 1966, 3, 875 |
| vlm_177638 | 1 | lit_6479 | 69FKM | V. A. Fedorov, M. Ya. Kutuzova, and V. E. Mironov, Fiz. Khim. Khim. Tekhnol., 1… |
| vlm_177638 | 1 | lit_6520 | 69Hd | H. C. Helgeson, Amer. J. Sci., 1969, 267, 729 |
| vlm_177638 | 1 | lit_7036 | 70FS | V. A. Fedorov, N. P. Samsonova, and V. E. Mironov, Russ. J. Inorg. Chem., 1970,… |
| vlm_177638 | 1 | lit_7345 | 71BHa | A. M. Bond and G. Hefter, J. Electroanal. Chem., 1971, 31, 477 |
| vlm_177638 | 1 | lit_7820 | 71V | F. Vierling, Bull. Soc. Chim. France, 1971, 22, 25 |
| vlm_177638 | 1 | lit_8011 | 72FSL | V. A. Fedorov, L. P. Shishin, S. G. Likhacheva, A. V. Fedorova, and V. E. Miron… |
| vlm_177638 | 1 | lit_8330 | 72SF | N. P. Samsonova, V. A. Fedorov, and V. E. Mironov, Russ. J. Phys. Chem., 1972, … |
| vlm_177638 | 1 | lit_8468 | 73BH | A. M. Bond and G. Hefter, J. Electroanal. Chem., 1973, 42, 1 |
| vlm_177638 | 1 | lit_8591 | 73HH | M. H. Hutchinson and W. C. E. Higginson, J. Chem. Soc. Dalton, 1973, 1247 |
| vlm_177638 | 1 | lit_8891 | 73V | F. Vierling, Ann. Chim. (Paris), 1973, 8, 53 |
| vlm_177638 | 1 | lit_9515 | 75Fa | V. A. Fedorov, Soviet J. Coord. Chem., 1975, 1, 751 (890) |
| vlm_177638 | 1 | lit_9671 | 75Ma | L. Meites, Talanta, 1975, 22, 733 |
| vlm_177638 | 1 | lit_9982 | 76FS | V. A. Fedorov and L. P. Shishin, Russ. J. Phys. Chem., 1976, 50, 210 (356) |
| vlm_177638 | 1 | lit_10300 | 76YK | E. N. Yurchenko, G. R. Kolonin, G. P. Shironosova, and T. P. Aksenova, Russ. J.… |
| vlm_177638 | 1 | lit_10362 | 77BL | C. Birraux, J. C. Landry, and W. Haerdi, Anal. Chim. Acta, 1977, 90, 51 |
| vlm_177638 | 1 | lit_11061 | 79BKa | S. D. Brown and B. R. Kowalski, Anal. Chem., 1979, 51, 2133 |
| vlm_177638 | 1 | lit_11630 | 80PPb | A. K. Prasad and B. Prasad, J. Indian Chem. Soc., 1980, 57, 155 |
| vlm_177638 | 1 | lit_11710 | 80TK | A. V. Tyulin and Yu. P. Khranilov, Soviet J. Coord. Chem., 1980, 6, 515 (1034) |

---

### Step 8: `search_citations`
**Args:**
```json
{
  "where": "(rv.vlm_id = vlm_177639)"
}
```

[summary]
## search_citations — 50 row(s)

| example_vlm_id | vlm_count | lit_id | shortcut | citation |
|----------------|-----------|--------|----------|----------|
| vlm_177639 | 1 | lit_265 | 30RD | E. C. Righellato and C. W. Davies, Trans. Faraday Soc., 1930, 26, 592 |
| vlm_177639 | 1 | lit_276 | 31F | H. Fromherz, Z. Phys. Chem., 1931, A153, 376 |
| vlm_177639 | 1 | lit_278 | 31FL | H. Fromherz and K. H. Lih, Z. Phys. Chem., 1931, A153, 321, 376 |
| vlm_177639 | 1 | lit_488 | 38G | E. Guntelberg, Thesis, Copenhagen, 1938 |
| vlm_177639 | 1 | lit_602 | 42GN | A. B. Garrett, M. V. Noble, and S. Miller, J. Chem. Educ., 1942, 19, 485 |
| vlm_177639 | 1 | lit_673 | 44NG | M. V. Noble and A. B. Garrett, J. Amer. Chem. Soc., 1944, 66, 231 |
| vlm_177639 | 1 | lit_694 | 45Na | R. Nasanen, Ann. Acad. Sci. Fenn., 1945, AII, No. 13 |
| vlm_177639 | 1 | lit_816 | 49GGa | R. M. Garrels and F. T. Gucker, Jr., Chem. Rev., 1949, 44, 117 |
| vlm_177639 | 1 | lit_825 | 49Jb | J. C. James, J. Amer. Chem. Soc., 1949, 71, 3243 |
| vlm_177639 | 1 | lit_1197 | 56Cc | B. Charreton, Bull. Soc. Chim. France, 1956, 323, 337, 347 |
| vlm_177639 | 1 | lit_1627 | 80LBa | M. Lovric and M. Branica, Croat. Chem. Acta, 1980, 53, 503 |
| vlm_177639 | 1 | lit_2107 | 55BPP | A. I. Biggs, M. H. Panckhurst, and H. N. Parton, Trans. Faraday Soc., 1955, 51,… |
| vlm_177639 | 1 | lit_2108 | 55BPR | A. I. Biggs, H. N. Parton, and R. A. Robinson, J. Amer. Chem. Soc., 1955, 77, 5… |
| vlm_177639 | 1 | lit_2160 | 55K | P. Kivalo, Suomen Kem., 1955, B28, 155 |
| vlm_177639 | 1 | lit_2199 | 55Na | G. H. Nancollas, J. Chem. Soc., 1955, 1458 |
| vlm_177639 | 1 | lit_2277 | 56P | P. Papoff, Suomen Kem., 1956, B29, 97 |
| vlm_177639 | 1 | lit_2452 | 57KL | P. Kivalo and R. Luoto, Suomen Kem., 1957, B30, 163 |
| vlm_177639 | 1 | lit_2512 | 57PCF | P. Papoff, M. A. Caliumi, and G. Ferrari, Ric. Sci., 1957, 27, suppl. A; Polaro… |
| vlm_177639 | 1 | lit_3036 | 59TCa | Ya. I. Turyan and N. G. Chebotar, Russ. J. Inorg. Chem., 1959, 4, 273 (599) |
| vlm_177639 | 1 | lit_3148 | 60FSS | Ya. D. Fridman, D. S. Sarbaev, and R. I. Sorochan, Russ. J. Inorg. Chem., 1960,… |
| vlm_177639 | 1 | lit_3453 | 61M | V. E. Mironov, Russ. J. Inorg. Chem., 1961, 6, 205 (405) |
| vlm_177639 | 1 | lit_3492 | 61NR | C. J. Nyman, D. K. Roe, and R. A. Plane, J. Amer. Chem. Soc., 1961, 83, 323 |
| vlm_177639 | 1 | lit_3675 | 62FCa | J. Faucherre and A. Crego, Bull. Soc. Chim. France, 1962, 1820 |
| vlm_177639 | 1 | lit_4133 | 63MFN | V. E. Mironov, V. A. Fedorov, and V. A. Nazarov, Russ. J. Inorg. Chem., 1963, 8… |
| vlm_177639 | 1 | lit_4140 | 63MKc | V. E. Mironov, F. Ya. Kulba, V. A. Fedorov, and O. B. Tikhomirov, Russ. J. Inor… |
| vlm_177639 | 1 | lit_4317 | 64AP | V. I. Altynov and B. V. Ptitsyn, Russ. J. Inorg. Chem., 1964, 9, 1301 (2407) |
| vlm_177639 | 1 | lit_4343 | 64BMa | E. Ya. Benyash and T. G. Maslakova, Russ. J. Inorg. Chem., 1964, 9, 1472 (2731) |
| vlm_177639 | 1 | lit_4486 | 64MK | V. E. Mironov, F. Ya. Kulba, and V. A. Fedorov, Russ. J. Inorg. Chem., 1964, 9,… |
| vlm_177639 | 1 | lit_4488 | 64MKb | V. E. Mironov, F. Ya. Kulba, V. A. Fedorov, and A. V. Fedorova, Russ. J. Inorg.… |
| vlm_177639 | 1 | lit_4810 | 65HP | G. P. Haight, Jr., and J. R. Peterson, Inorg. Chem., 1965, 4, 1073 |
| vlm_177639 | 1 | lit_4883 | 65MKF | V. E. Mironov, F. Ya. Kulba, and V. A. Fedorov, Russ. J. Inorg. Chem., 1965, 10… |
| vlm_177639 | 1 | lit_5433 | 66VSB | F. Vierling, G. Schorsch, and J. Bye, Rev. Chim. Miner., 1966, 3, 875 |
| vlm_177639 | 1 | lit_6479 | 69FKM | V. A. Fedorov, M. Ya. Kutuzova, and V. E. Mironov, Fiz. Khim. Khim. Tekhnol., 1… |
| vlm_177639 | 1 | lit_6520 | 69Hd | H. C. Helgeson, Amer. J. Sci., 1969, 267, 729 |
| vlm_177639 | 1 | lit_7036 | 70FS | V. A. Fedorov, N. P. Samsonova, and V. E. Mironov, Russ. J. Inorg. Chem., 1970,… |
| vlm_177639 | 1 | lit_7345 | 71BHa | A. M. Bond and G. Hefter, J. Electroanal. Chem., 1971, 31, 477 |
| vlm_177639 | 1 | lit_7820 | 71V | F. Vierling, Bull. Soc. Chim. France, 1971, 22, 25 |
| vlm_177639 | 1 | lit_8011 | 72FSL | V. A. Fedorov, L. P. Shishin, S. G. Likhacheva, A. V. Fedorova, and V. E. Miron… |
| vlm_177639 | 1 | lit_8330 | 72SF | N. P. Samsonova, V. A. Fedorov, and V. E. Mironov, Russ. J. Phys. Chem., 1972, … |
| vlm_177639 | 1 | lit_8468 | 73BH | A. M. Bond and G. Hefter, J. Electroanal. Chem., 1973, 42, 1 |
| vlm_177639 | 1 | lit_8591 | 73HH | M. H. Hutchinson and W. C. E. Higginson, J. Chem. Soc. Dalton, 1973, 1247 |
| vlm_177639 | 1 | lit_8891 | 73V | F. Vierling, Ann. Chim. (Paris), 1973, 8, 53 |
| vlm_177639 | 1 | lit_9515 | 75Fa | V. A. Fedorov, Soviet J. Coord. Chem., 1975, 1, 751 (890) |
| vlm_177639 | 1 | lit_9671 | 75Ma | L. Meites, Talanta, 1975, 22, 733 |
| vlm_177639 | 1 | lit_9982 | 76FS | V. A. Fedorov and L. P. Shishin, Russ. J. Phys. Chem., 1976, 50, 210 (356) |
| vlm_177639 | 1 | lit_10300 | 76YK | E. N. Yurchenko, G. R. Kolonin, G. P. Shironosova, and T. P. Aksenova, Russ. J.… |
| vlm_177639 | 1 | lit_10362 | 77BL | C. Birraux, J. C. Landry, and W. Haerdi, Anal. Chim. Acta, 1977, 90, 51 |
| vlm_177639 | 1 | lit_11061 | 79BKa | S. D. Brown and B. R. Kowalski, Anal. Chem., 1979, 51, 2133 |
| vlm_177639 | 1 | lit_11630 | 80PPb | A. K. Prasad and B. Prasad, J. Indian Chem. Soc., 1980, 57, 155 |
| vlm_177639 | 1 | lit_11710 | 80TK | A. V. Tyulin and Yu. P. Khranilov, Soviet J. Coord. Chem., 1980, 6, 515 (1034) |

---

### Step 9: `search_citations`
**Args:**
```json
{
  "where": "(rv.vlm_id = vlm_177640)"
}
```

[summary]
## search_citations — 50 row(s)

| example_vlm_id | vlm_count | lit_id | shortcut | citation |
|----------------|-----------|--------|----------|----------|
| vlm_177640 | 1 | lit_265 | 30RD | E. C. Righellato and C. W. Davies, Trans. Faraday Soc., 1930, 26, 592 |
| vlm_177640 | 1 | lit_276 | 31F | H. Fromherz, Z. Phys. Chem., 1931, A153, 376 |
| vlm_177640 | 1 | lit_278 | 31FL | H. Fromherz and K. H. Lih, Z. Phys. Chem., 1931, A153, 321, 376 |
| vlm_177640 | 1 | lit_488 | 38G | E. Guntelberg, Thesis, Copenhagen, 1938 |
| vlm_177640 | 1 | lit_602 | 42GN | A. B. Garrett, M. V. Noble, and S. Miller, J. Chem. Educ., 1942, 19, 485 |
| vlm_177640 | 1 | lit_673 | 44NG | M. V. Noble and A. B. Garrett, J. Amer. Chem. Soc., 1944, 66, 231 |
| vlm_177640 | 1 | lit_694 | 45Na | R. Nasanen, Ann. Acad. Sci. Fenn., 1945, AII, No. 13 |
| vlm_177640 | 1 | lit_816 | 49GGa | R. M. Garrels and F. T. Gucker, Jr., Chem. Rev., 1949, 44, 117 |
| vlm_177640 | 1 | lit_825 | 49Jb | J. C. James, J. Amer. Chem. Soc., 1949, 71, 3243 |
| vlm_177640 | 1 | lit_1197 | 56Cc | B. Charreton, Bull. Soc. Chim. France, 1956, 323, 337, 347 |
| vlm_177640 | 1 | lit_1627 | 80LBa | M. Lovric and M. Branica, Croat. Chem. Acta, 1980, 53, 503 |
| vlm_177640 | 1 | lit_2107 | 55BPP | A. I. Biggs, M. H. Panckhurst, and H. N. Parton, Trans. Faraday Soc., 1955, 51,… |
| vlm_177640 | 1 | lit_2108 | 55BPR | A. I. Biggs, H. N. Parton, and R. A. Robinson, J. Amer. Chem. Soc., 1955, 77, 5… |
| vlm_177640 | 1 | lit_2160 | 55K | P. Kivalo, Suomen Kem., 1955, B28, 155 |
| vlm_177640 | 1 | lit_2199 | 55Na | G. H. Nancollas, J. Chem. Soc., 1955, 1458 |
| vlm_177640 | 1 | lit_2277 | 56P | P. Papoff, Suomen Kem., 1956, B29, 97 |
| vlm_177640 | 1 | lit_2452 | 57KL | P. Kivalo and R. Luoto, Suomen Kem., 1957, B30, 163 |
| vlm_177640 | 1 | lit_2512 | 57PCF | P. Papoff, M. A. Caliumi, and G. Ferrari, Ric. Sci., 1957, 27, suppl. A; Polaro… |
| vlm_177640 | 1 | lit_3036 | 59TCa | Ya. I. Turyan and N. G. Chebotar, Russ. J. Inorg. Chem., 1959, 4, 273 (599) |
| vlm_177640 | 1 | lit_3148 | 60FSS | Ya. D. Fridman, D. S. Sarbaev, and R. I. Sorochan, Russ. J. Inorg. Chem., 1960,… |
| vlm_177640 | 1 | lit_3453 | 61M | V. E. Mironov, Russ. J. Inorg. Chem., 1961, 6, 205 (405) |
| vlm_177640 | 1 | lit_3492 | 61NR | C. J. Nyman, D. K. Roe, and R. A. Plane, J. Amer. Chem. Soc., 1961, 83, 323 |
| vlm_177640 | 1 | lit_3675 | 62FCa | J. Faucherre and A. Crego, Bull. Soc. Chim. France, 1962, 1820 |
| vlm_177640 | 1 | lit_4133 | 63MFN | V. E. Mironov, V. A. Fedorov, and V. A. Nazarov, Russ. J. Inorg. Chem., 1963, 8… |
| vlm_177640 | 1 | lit_4140 | 63MKc | V. E. Mironov, F. Ya. Kulba, V. A. Fedorov, and O. B. Tikhomirov, Russ. J. Inor… |
| vlm_177640 | 1 | lit_4317 | 64AP | V. I. Altynov and B. V. Ptitsyn, Russ. J. Inorg. Chem., 1964, 9, 1301 (2407) |
| vlm_177640 | 1 | lit_4343 | 64BMa | E. Ya. Benyash and T. G. Maslakova, Russ. J. Inorg. Chem., 1964, 9, 1472 (2731) |
| vlm_177640 | 1 | lit_4486 | 64MK | V. E. Mironov, F. Ya. Kulba, and V. A. Fedorov, Russ. J. Inorg. Chem., 1964, 9,… |
| vlm_177640 | 1 | lit_4488 | 64MKb | V. E. Mironov, F. Ya. Kulba, V. A. Fedorov, and A. V. Fedorova, Russ. J. Inorg.… |
| vlm_177640 | 1 | lit_4810 | 65HP | G. P. Haight, Jr., and J. R. Peterson, Inorg. Chem., 1965, 4, 1073 |
| vlm_177640 | 1 | lit_4883 | 65MKF | V. E. Mironov, F. Ya. Kulba, and V. A. Fedorov, Russ. J. Inorg. Chem., 1965, 10… |
| vlm_177640 | 1 | lit_5433 | 66VSB | F. Vierling, G. Schorsch, and J. Bye, Rev. Chim. Miner., 1966, 3, 875 |
| vlm_177640 | 1 | lit_6479 | 69FKM | V. A. Fedorov, M. Ya. Kutuzova, and V. E. Mironov, Fiz. Khim. Khim. Tekhnol., 1… |
| vlm_177640 | 1 | lit_6520 | 69Hd | H. C. Helgeson, Amer. J. Sci., 1969, 267, 729 |
| vlm_177640 | 1 | lit_7036 | 70FS | V. A. Fedorov, N. P. Samsonova, and V. E. Mironov, Russ. J. Inorg. Chem., 1970,… |
| vlm_177640 | 1 | lit_7345 | 71BHa | A. M. Bond and G. Hefter, J. Electroanal. Chem., 1971, 31, 477 |
| vlm_177640 | 1 | lit_7820 | 71V | F. Vierling, Bull. Soc. Chim. France, 1971, 22, 25 |
| vlm_177640 | 1 | lit_8011 | 72FSL | V. A. Fedorov, L. P. Shishin, S. G. Likhacheva, A. V. Fedorova, and V. E. Miron… |
| vlm_177640 | 1 | lit_8330 | 72SF | N. P. Samsonova, V. A. Fedorov, and V. E. Mironov, Russ. J. Phys. Chem., 1972, … |
| vlm_177640 | 1 | lit_8468 | 73BH | A. M. Bond and G. Hefter, J. Electroanal. Chem., 1973, 42, 1 |
| vlm_177640 | 1 | lit_8591 | 73HH | M. H. Hutchinson and W. C. E. Higginson, J. Chem. Soc. Dalton, 1973, 1247 |
| vlm_177640 | 1 | lit_8891 | 73V | F. Vierling, Ann. Chim. (Paris), 1973, 8, 53 |
| vlm_177640 | 1 | lit_9515 | 75Fa | V. A. Fedorov, Soviet J. Coord. Chem., 1975, 1, 751 (890) |
| vlm_177640 | 1 | lit_9671 | 75Ma | L. Meites, Talanta, 1975, 22, 733 |
| vlm_177640 | 1 | lit_9982 | 76FS | V. A. Fedorov and L. P. Shishin, Russ. J. Phys. Chem., 1976, 50, 210 (356) |
| vlm_177640 | 1 | lit_10300 | 76YK | E. N. Yurchenko, G. R. Kolonin, G. P. Shironosova, and T. P. Aksenova, Russ. J.… |
| vlm_177640 | 1 | lit_10362 | 77BL | C. Birraux, J. C. Landry, and W. Haerdi, Anal. Chim. Acta, 1977, 90, 51 |
| vlm_177640 | 1 | lit_11061 | 79BKa | S. D. Brown and B. R. Kowalski, Anal. Chem., 1979, 51, 2133 |
| vlm_177640 | 1 | lit_11630 | 80PPb | A. K. Prasad and B. Prasad, J. Indian Chem. Soc., 1980, 57, 155 |
| vlm_177640 | 1 | lit_11710 | 80TK | A. V. Tyulin and Yu. P. Khranilov, Soviet J. Coord. Chem., 1980, 6, 515 (1034) |

---

### Step 10: `search_citations`
**Args:**
```json
{
  "where": "(rv.vlm_id = vlm_177641)"
}
```

[summary]
## search_citations — 50 row(s)

| example_vlm_id | vlm_count | lit_id | shortcut | citation |
|----------------|-----------|--------|----------|----------|
| vlm_177641 | 1 | lit_265 | 30RD | E. C. Righellato and C. W. Davies, Trans. Faraday Soc., 1930, 26, 592 |
| vlm_177641 | 1 | lit_276 | 31F | H. Fromherz, Z. Phys. Chem., 1931, A153, 376 |
| vlm_177641 | 1 | lit_278 | 31FL | H. Fromherz and K. H. Lih, Z. Phys. Chem., 1931, A153, 321, 376 |
| vlm_177641 | 1 | lit_488 | 38G | E. Guntelberg, Thesis, Copenhagen, 1938 |
| vlm_177641 | 1 | lit_602 | 42GN | A. B. Garrett, M. V. Noble, and S. Miller, J. Chem. Educ., 1942, 19, 485 |
| vlm_177641 | 1 | lit_673 | 44NG | M. V. Noble and A. B. Garrett, J. Amer. Chem. Soc., 1944, 66, 231 |
| vlm_177641 | 1 | lit_694 | 45Na | R. Nasanen, Ann. Acad. Sci. Fenn., 1945, AII, No. 13 |
| vlm_177641 | 1 | lit_816 | 49GGa | R. M. Garrels and F. T. Gucker, Jr., Chem. Rev., 1949, 44, 117 |
| vlm_177641 | 1 | lit_825 | 49Jb | J. C. James, J. Amer. Chem. Soc., 1949, 71, 3243 |
| vlm_177641 | 1 | lit_1197 | 56Cc | B. Charreton, Bull. Soc. Chim. France, 1956, 323, 337, 347 |
| vlm_177641 | 1 | lit_1627 | 80LBa | M. Lovric and M. Branica, Croat. Chem. Acta, 1980, 53, 503 |
| vlm_177641 | 1 | lit_2107 | 55BPP | A. I. Biggs, M. H. Panckhurst, and H. N. Parton, Trans. Faraday Soc., 1955, 51,… |
| vlm_177641 | 1 | lit_2108 | 55BPR | A. I. Biggs, H. N. Parton, and R. A. Robinson, J. Amer. Chem. Soc., 1955, 77, 5… |
| vlm_177641 | 1 | lit_2160 | 55K | P. Kivalo, Suomen Kem., 1955, B28, 155 |
| vlm_177641 | 1 | lit_2199 | 55Na | G. H. Nancollas, J. Chem. Soc., 1955, 1458 |
| vlm_177641 | 1 | lit_2277 | 56P | P. Papoff, Suomen Kem., 1956, B29, 97 |
| vlm_177641 | 1 | lit_2452 | 57KL | P. Kivalo and R. Luoto, Suomen Kem., 1957, B30, 163 |
| vlm_177641 | 1 | lit_2512 | 57PCF | P. Papoff, M. A. Caliumi, and G. Ferrari, Ric. Sci., 1957, 27, suppl. A; Polaro… |
| vlm_177641 | 1 | lit_3036 | 59TCa | Ya. I. Turyan and N. G. Chebotar, Russ. J. Inorg. Chem., 1959, 4, 273 (599) |
| vlm_177641 | 1 | lit_3148 | 60FSS | Ya. D. Fridman, D. S. Sarbaev, and R. I. Sorochan, Russ. J. Inorg. Chem., 1960,… |
| vlm_177641 | 1 | lit_3453 | 61M | V. E. Mironov, Russ. J. Inorg. Chem., 1961, 6, 205 (405) |
| vlm_177641 | 1 | lit_3492 | 61NR | C. J. Nyman, D. K. Roe, and R. A. Plane, J. Amer. Chem. Soc., 1961, 83, 323 |
| vlm_177641 | 1 | lit_3675 | 62FCa | J. Faucherre and A. Crego, Bull. Soc. Chim. France, 1962, 1820 |
| vlm_177641 | 1 | lit_4133 | 63MFN | V. E. Mironov, V. A. Fedorov, and V. A. Nazarov, Russ. J. Inorg. Chem., 1963, 8… |
| vlm_177641 | 1 | lit_4140 | 63MKc | V. E. Mironov, F. Ya. Kulba, V. A. Fedorov, and O. B. Tikhomirov, Russ. J. Inor… |
| vlm_177641 | 1 | lit_4317 | 64AP | V. I. Altynov and B. V. Ptitsyn, Russ. J. Inorg. Chem., 1964, 9, 1301 (2407) |
| vlm_177641 | 1 | lit_4343 | 64BMa | E. Ya. Benyash and T. G. Maslakova, Russ. J. Inorg. Chem., 1964, 9, 1472 (2731) |
| vlm_177641 | 1 | lit_4486 | 64MK | V. E. Mironov, F. Ya. Kulba, and V. A. Fedorov, Russ. J. Inorg. Chem., 1964, 9,… |
| vlm_177641 | 1 | lit_4488 | 64MKb | V. E. Mironov, F. Ya. Kulba, V. A. Fedorov, and A. V. Fedorova, Russ. J. Inorg.… |
| vlm_177641 | 1 | lit_4810 | 65HP | G. P. Haight, Jr., and J. R. Peterson, Inorg. Chem., 1965, 4, 1073 |
| vlm_177641 | 1 | lit_4883 | 65MKF | V. E. Mironov, F. Ya. Kulba, and V. A. Fedorov, Russ. J. Inorg. Chem., 1965, 10… |
| vlm_177641 | 1 | lit_5433 | 66VSB | F. Vierling, G. Schorsch, and J. Bye, Rev. Chim. Miner., 1966, 3, 875 |
| vlm_177641 | 1 | lit_6479 | 69FKM | V. A. Fedorov, M. Ya. Kutuzova, and V. E. Mironov, Fiz. Khim. Khim. Tekhnol., 1… |
| vlm_177641 | 1 | lit_6520 | 69Hd | H. C. Helgeson, Amer. J. Sci., 1969, 267, 729 |
| vlm_177641 | 1 | lit_7036 | 70FS | V. A. Fedorov, N. P. Samsonova, and V. E. Mironov, Russ. J. Inorg. Chem., 1970,… |
| vlm_177641 | 1 | lit_7345 | 71BHa | A. M. Bond and G. Hefter, J. Electroanal. Chem., 1971, 31, 477 |
| vlm_177641 | 1 | lit_7820 | 71V | F. Vierling, Bull. Soc. Chim. France, 1971, 22, 25 |
| vlm_177641 | 1 | lit_8011 | 72FSL | V. A. Fedorov, L. P. Shishin, S. G. Likhacheva, A. V. Fedorova, and V. E. Miron… |
| vlm_177641 | 1 | lit_8330 | 72SF | N. P. Samsonova, V. A. Fedorov, and V. E. Mironov, Russ. J. Phys. Chem., 1972, … |
| vlm_177641 | 1 | lit_8468 | 73BH | A. M. Bond and G. Hefter, J. Electroanal. Chem., 1973, 42, 1 |
| vlm_177641 | 1 | lit_8591 | 73HH | M. H. Hutchinson and W. C. E. Higginson, J. Chem. Soc. Dalton, 1973, 1247 |
| vlm_177641 | 1 | lit_8891 | 73V | F. Vierling, Ann. Chim. (Paris), 1973, 8, 53 |
| vlm_177641 | 1 | lit_9515 | 75Fa | V. A. Fedorov, Soviet J. Coord. Chem., 1975, 1, 751 (890) |
| vlm_177641 | 1 | lit_9671 | 75Ma | L. Meites, Talanta, 1975, 22, 733 |
| vlm_177641 | 1 | lit_9982 | 76FS | V. A. Fedorov and L. P. Shishin, Russ. J. Phys. Chem., 1976, 50, 210 (356) |
| vlm_177641 | 1 | lit_10300 | 76YK | E. N. Yurchenko, G. R. Kolonin, G. P. Shironosova, and T. P. Aksenova, Russ. J.… |
| vlm_177641 | 1 | lit_10362 | 77BL | C. Birraux, J. C. Landry, and W. Haerdi, Anal. Chim. Acta, 1977, 90, 51 |
| vlm_177641 | 1 | lit_11061 | 79BKa | S. D. Brown and B. R. Kowalski, Anal. Chem., 1979, 51, 2133 |
| vlm_177641 | 1 | lit_11630 | 80PPb | A. K. Prasad and B. Prasad, J. Indian Chem. Soc., 1980, 57, 155 |
| vlm_177641 | 1 | lit_11710 | 80TK | A. V. Tyulin and Yu. P. Khranilov, Soviet J. Coord. Chem., 1980, 6, 515 (1034) |

---

### Step 11: `search_citations`
**Args:**
```json
{
  "where": "(rv.vlm_id = vlm_177642)"
}
```

[summary]
## search_citations — 50 row(s)

| example_vlm_id | vlm_count | lit_id | shortcut | citation |
|----------------|-----------|--------|----------|----------|
| vlm_177642 | 1 | lit_265 | 30RD | E. C. Righellato and C. W. Davies, Trans. Faraday Soc., 1930, 26, 592 |
| vlm_177642 | 1 | lit_276 | 31F | H. Fromherz, Z. Phys. Chem., 1931, A153, 376 |
| vlm_177642 | 1 | lit_278 | 31FL | H. Fromherz and K. H. Lih, Z. Phys. Chem., 1931, A153, 321, 376 |
| vlm_177642 | 1 | lit_488 | 38G | E. Guntelberg, Thesis, Copenhagen, 1938 |
| vlm_177642 | 1 | lit_602 | 42GN | A. B. Garrett, M. V. Noble, and S. Miller, J. Chem. Educ., 1942, 19, 485 |
| vlm_177642 | 1 | lit_673 | 44NG | M. V. Noble and A. B. Garrett, J. Amer. Chem. Soc., 1944, 66, 231 |
| vlm_177642 | 1 | lit_694 | 45Na | R. Nasanen, Ann. Acad. Sci. Fenn., 1945, AII, No. 13 |
| vlm_177642 | 1 | lit_816 | 49GGa | R. M. Garrels and F. T. Gucker, Jr., Chem. Rev., 1949, 44, 117 |
| vlm_177642 | 1 | lit_825 | 49Jb | J. C. James, J. Amer. Chem. Soc., 1949, 71, 3243 |
| vlm_177642 | 1 | lit_1197 | 56Cc | B. Charreton, Bull. Soc. Chim. France, 1956, 323, 337, 347 |
| vlm_177642 | 1 | lit_1627 | 80LBa | M. Lovric and M. Branica, Croat. Chem. Acta, 1980, 53, 503 |
| vlm_177642 | 1 | lit_2107 | 55BPP | A. I. Biggs, M. H. Panckhurst, and H. N. Parton, Trans. Faraday Soc., 1955, 51,… |
| vlm_177642 | 1 | lit_2108 | 55BPR | A. I. Biggs, H. N. Parton, and R. A. Robinson, J. Amer. Chem. Soc., 1955, 77, 5… |
| vlm_177642 | 1 | lit_2160 | 55K | P. Kivalo, Suomen Kem., 1955, B28, 155 |
| vlm_177642 | 1 | lit_2199 | 55Na | G. H. Nancollas, J. Chem. Soc., 1955, 1458 |
| vlm_177642 | 1 | lit_2277 | 56P | P. Papoff, Suomen Kem., 1956, B29, 97 |
| vlm_177642 | 1 | lit_2452 | 57KL | P. Kivalo and R. Luoto, Suomen Kem., 1957, B30, 163 |
| vlm_177642 | 1 | lit_2512 | 57PCF | P. Papoff, M. A. Caliumi, and G. Ferrari, Ric. Sci., 1957, 27, suppl. A; Polaro… |
| vlm_177642 | 1 | lit_3036 | 59TCa | Ya. I. Turyan and N. G. Chebotar, Russ. J. Inorg. Chem., 1959, 4, 273 (599) |
| vlm_177642 | 1 | lit_3148 | 60FSS | Ya. D. Fridman, D. S. Sarbaev, and R. I. Sorochan, Russ. J. Inorg. Chem., 1960,… |
| vlm_177642 | 1 | lit_3453 | 61M | V. E. Mironov, Russ. J. Inorg. Chem., 1961, 6, 205 (405) |
| vlm_177642 | 1 | lit_3492 | 61NR | C. J. Nyman, D. K. Roe, and R. A. Plane, J. Amer. Chem. Soc., 1961, 83, 323 |
| vlm_177642 | 1 | lit_3675 | 62FCa | J. Faucherre and A. Crego, Bull. Soc. Chim. France, 1962, 1820 |
| vlm_177642 | 1 | lit_4133 | 63MFN | V. E. Mironov, V. A. Fedorov, and V. A. Nazarov, Russ. J. Inorg. Chem., 1963, 8… |
| vlm_177642 | 1 | lit_4140 | 63MKc | V. E. Mironov, F. Ya. Kulba, V. A. Fedorov, and O. B. Tikhomirov, Russ. J. Inor… |
| vlm_177642 | 1 | lit_4317 | 64AP | V. I. Altynov and B. V. Ptitsyn, Russ. J. Inorg. Chem., 1964, 9, 1301 (2407) |
| vlm_177642 | 1 | lit_4343 | 64BMa | E. Ya. Benyash and T. G. Maslakova, Russ. J. Inorg. Chem., 1964, 9, 1472 (2731) |
| vlm_177642 | 1 | lit_4486 | 64MK | V. E. Mironov, F. Ya. Kulba, and V. A. Fedorov, Russ. J. Inorg. Chem., 1964, 9,… |
| vlm_177642 | 1 | lit_4488 | 64MKb | V. E. Mironov, F. Ya. Kulba, V. A. Fedorov, and A. V. Fedorova, Russ. J. Inorg.… |
| vlm_177642 | 1 | lit_4810 | 65HP | G. P. Haight, Jr., and J. R. Peterson, Inorg. Chem., 1965, 4, 1073 |
| vlm_177642 | 1 | lit_4883 | 65MKF | V. E. Mironov, F. Ya. Kulba, and V. A. Fedorov, Russ. J. Inorg. Chem., 1965, 10… |
| vlm_177642 | 1 | lit_5433 | 66VSB | F. Vierling, G. Schorsch, and J. Bye, Rev. Chim. Miner., 1966, 3, 875 |
| vlm_177642 | 1 | lit_6479 | 69FKM | V. A. Fedorov, M. Ya. Kutuzova, and V. E. Mironov, Fiz. Khim. Khim. Tekhnol., 1… |
| vlm_177642 | 1 | lit_6520 | 69Hd | H. C. Helgeson, Amer. J. Sci., 1969, 267, 729 |
| vlm_177642 | 1 | lit_7036 | 70FS | V. A. Fedorov, N. P. Samsonova, and V. E. Mironov, Russ. J. Inorg. Chem., 1970,… |
| vlm_177642 | 1 | lit_7345 | 71BHa | A. M. Bond and G. Hefter, J. Electroanal. Chem., 1971, 31, 477 |
| vlm_177642 | 1 | lit_7820 | 71V | F. Vierling, Bull. Soc. Chim. France, 1971, 22, 25 |
| vlm_177642 | 1 | lit_8011 | 72FSL | V. A. Fedorov, L. P. Shishin, S. G. Likhacheva, A. V. Fedorova, and V. E. Miron… |
| vlm_177642 | 1 | lit_8330 | 72SF | N. P. Samsonova, V. A. Fedorov, and V. E. Mironov, Russ. J. Phys. Chem., 1972, … |
| vlm_177642 | 1 | lit_8468 | 73BH | A. M. Bond and G. Hefter, J. Electroanal. Chem., 1973, 42, 1 |
| vlm_177642 | 1 | lit_8591 | 73HH | M. H. Hutchinson and W. C. E. Higginson, J. Chem. Soc. Dalton, 1973, 1247 |
| vlm_177642 | 1 | lit_8891 | 73V | F. Vierling, Ann. Chim. (Paris), 1973, 8, 53 |
| vlm_177642 | 1 | lit_9515 | 75Fa | V. A. Fedorov, Soviet J. Coord. Chem., 1975, 1, 751 (890) |
| vlm_177642 | 1 | lit_9671 | 75Ma | L. Meites, Talanta, 1975, 22, 733 |
| vlm_177642 | 1 | lit_9982 | 76FS | V. A. Fedorov and L. P. Shishin, Russ. J. Phys. Chem., 1976, 50, 210 (356) |
| vlm_177642 | 1 | lit_10300 | 76YK | E. N. Yurchenko, G. R. Kolonin, G. P. Shironosova, and T. P. Aksenova, Russ. J.… |
| vlm_177642 | 1 | lit_10362 | 77BL | C. Birraux, J. C. Landry, and W. Haerdi, Anal. Chim. Acta, 1977, 90, 51 |
| vlm_177642 | 1 | lit_11061 | 79BKa | S. D. Brown and B. R. Kowalski, Anal. Chem., 1979, 51, 2133 |
| vlm_177642 | 1 | lit_11630 | 80PPb | A. K. Prasad and B. Prasad, J. Indian Chem. Soc., 1980, 57, 155 |
| vlm_177642 | 1 | lit_11710 | 80TK | A. V. Tyulin and Yu. P. Khranilov, Soviet J. Coord. Chem., 1980, 6, 515 (1034) |

---

### Step 12: `search_citations`
**Args:**
```json
{
  "where": "(rv.vlm_id = vlm_177643)"
}
```

[summary]
## search_citations — 50 row(s)

| example_vlm_id | vlm_count | lit_id | shortcut | citation |
|----------------|-----------|--------|----------|----------|
| vlm_177643 | 1 | lit_265 | 30RD | E. C. Righellato and C. W. Davies, Trans. Faraday Soc., 1930, 26, 592 |
| vlm_177643 | 1 | lit_276 | 31F | H. Fromherz, Z. Phys. Chem., 1931, A153, 376 |
| vlm_177643 | 1 | lit_278 | 31FL | H. Fromherz and K. H. Lih, Z. Phys. Chem., 1931, A153, 321, 376 |
| vlm_177643 | 1 | lit_488 | 38G | E. Guntelberg, Thesis, Copenhagen, 1938 |
| vlm_177643 | 1 | lit_602 | 42GN | A. B. Garrett, M. V. Noble, and S. Miller, J. Chem. Educ., 1942, 19, 485 |
| vlm_177643 | 1 | lit_673 | 44NG | M. V. Noble and A. B. Garrett, J. Amer. Chem. Soc., 1944, 66, 231 |
| vlm_177643 | 1 | lit_694 | 45Na | R. Nasanen, Ann. Acad. Sci. Fenn., 1945, AII, No. 13 |
| vlm_177643 | 1 | lit_816 | 49GGa | R. M. Garrels and F. T. Gucker, Jr., Chem. Rev., 1949, 44, 117 |
| vlm_177643 | 1 | lit_825 | 49Jb | J. C. James, J. Amer. Chem. Soc., 1949, 71, 3243 |
| vlm_177643 | 1 | lit_1197 | 56Cc | B. Charreton, Bull. Soc. Chim. France, 1956, 323, 337, 347 |
| vlm_177643 | 1 | lit_1627 | 80LBa | M. Lovric and M. Branica, Croat. Chem. Acta, 1980, 53, 503 |
| vlm_177643 | 1 | lit_2107 | 55BPP | A. I. Biggs, M. H. Panckhurst, and H. N. Parton, Trans. Faraday Soc., 1955, 51,… |
| vlm_177643 | 1 | lit_2108 | 55BPR | A. I. Biggs, H. N. Parton, and R. A. Robinson, J. Amer. Chem. Soc., 1955, 77, 5… |
| vlm_177643 | 1 | lit_2160 | 55K | P. Kivalo, Suomen Kem., 1955, B28, 155 |
| vlm_177643 | 1 | lit_2199 | 55Na | G. H. Nancollas, J. Chem. Soc., 1955, 1458 |
| vlm_177643 | 1 | lit_2277 | 56P | P. Papoff, Suomen Kem., 1956, B29, 97 |
| vlm_177643 | 1 | lit_2452 | 57KL | P. Kivalo and R. Luoto, Suomen Kem., 1957, B30, 163 |
| vlm_177643 | 1 | lit_2512 | 57PCF | P. Papoff, M. A. Caliumi, and G. Ferrari, Ric. Sci., 1957, 27, suppl. A; Polaro… |
| vlm_177643 | 1 | lit_3036 | 59TCa | Ya. I. Turyan and N. G. Chebotar, Russ. J. Inorg. Chem., 1959, 4, 273 (599) |
| vlm_177643 | 1 | lit_3148 | 60FSS | Ya. D. Fridman, D. S. Sarbaev, and R. I. Sorochan, Russ. J. Inorg. Chem., 1960,… |
| vlm_177643 | 1 | lit_3453 | 61M | V. E. Mironov, Russ. J. Inorg. Chem., 1961, 6, 205 (405) |
| vlm_177643 | 1 | lit_3492 | 61NR | C. J. Nyman, D. K. Roe, and R. A. Plane, J. Amer. Chem. Soc., 1961, 83, 323 |
| vlm_177643 | 1 | lit_3675 | 62FCa | J. Faucherre and A. Crego, Bull. Soc. Chim. France, 1962, 1820 |
| vlm_177643 | 1 | lit_4133 | 63MFN | V. E. Mironov, V. A. Fedorov, and V. A. Nazarov, Russ. J. Inorg. Chem., 1963, 8… |
| vlm_177643 | 1 | lit_4140 | 63MKc | V. E. Mironov, F. Ya. Kulba, V. A. Fedorov, and O. B. Tikhomirov, Russ. J. Inor… |
| vlm_177643 | 1 | lit_4317 | 64AP | V. I. Altynov and B. V. Ptitsyn, Russ. J. Inorg. Chem., 1964, 9, 1301 (2407) |
| vlm_177643 | 1 | lit_4343 | 64BMa | E. Ya. Benyash and T. G. Maslakova, Russ. J. Inorg. Chem., 1964, 9, 1472 (2731) |
| vlm_177643 | 1 | lit_4486 | 64MK | V. E. Mironov, F. Ya. Kulba, and V. A. Fedorov, Russ. J. Inorg. Chem., 1964, 9,… |
| vlm_177643 | 1 | lit_4488 | 64MKb | V. E. Mironov, F. Ya. Kulba, V. A. Fedorov, and A. V. Fedorova, Russ. J. Inorg.… |
| vlm_177643 | 1 | lit_4810 | 65HP | G. P. Haight, Jr., and J. R. Peterson, Inorg. Chem., 1965, 4, 1073 |
| vlm_177643 | 1 | lit_4883 | 65MKF | V. E. Mironov, F. Ya. Kulba, and V. A. Fedorov, Russ. J. Inorg. Chem., 1965, 10… |
| vlm_177643 | 1 | lit_5433 | 66VSB | F. Vierling, G. Schorsch, and J. Bye, Rev. Chim. Miner., 1966, 3, 875 |
| vlm_177643 | 1 | lit_6479 | 69FKM | V. A. Fedorov, M. Ya. Kutuzova, and V. E. Mironov, Fiz. Khim. Khim. Tekhnol., 1… |
| vlm_177643 | 1 | lit_6520 | 69Hd | H. C. Helgeson, Amer. J. Sci., 1969, 267, 729 |
| vlm_177643 | 1 | lit_7036 | 70FS | V. A. Fedorov, N. P. Samsonova, and V. E. Mironov, Russ. J. Inorg. Chem., 1970,… |
| vlm_177643 | 1 | lit_7345 | 71BHa | A. M. Bond and G. Hefter, J. Electroanal. Chem., 1971, 31, 477 |
| vlm_177643 | 1 | lit_7820 | 71V | F. Vierling, Bull. Soc. Chim. France, 1971, 22, 25 |
| vlm_177643 | 1 | lit_8011 | 72FSL | V. A. Fedorov, L. P. Shishin, S. G. Likhacheva, A. V. Fedorova, and V. E. Miron… |
| vlm_177643 | 1 | lit_8330 | 72SF | N. P. Samsonova, V. A. Fedorov, and V. E. Mironov, Russ. J. Phys. Chem., 1972, … |
| vlm_177643 | 1 | lit_8468 | 73BH | A. M. Bond and G. Hefter, J. Electroanal. Chem., 1973, 42, 1 |
| vlm_177643 | 1 | lit_8591 | 73HH | M. H. Hutchinson and W. C. E. Higginson, J. Chem. Soc. Dalton, 1973, 1247 |
| vlm_177643 | 1 | lit_8891 | 73V | F. Vierling, Ann. Chim. (Paris), 1973, 8, 53 |
| vlm_177643 | 1 | lit_9515 | 75Fa | V. A. Fedorov, Soviet J. Coord. Chem., 1975, 1, 751 (890) |
| vlm_177643 | 1 | lit_9671 | 75Ma | L. Meites, Talanta, 1975, 22, 733 |
| vlm_177643 | 1 | lit_9982 | 76FS | V. A. Fedorov and L. P. Shishin, Russ. J. Phys. Chem., 1976, 50, 210 (356) |
| vlm_177643 | 1 | lit_10300 | 76YK | E. N. Yurchenko, G. R. Kolonin, G. P. Shironosova, and T. P. Aksenova, Russ. J.… |
| vlm_177643 | 1 | lit_10362 | 77BL | C. Birraux, J. C. Landry, and W. Haerdi, Anal. Chim. Acta, 1977, 90, 51 |
| vlm_177643 | 1 | lit_11061 | 79BKa | S. D. Brown and B. R. Kowalski, Anal. Chem., 1979, 51, 2133 |
| vlm_177643 | 1 | lit_11630 | 80PPb | A. K. Prasad and B. Prasad, J. Indian Chem. Soc., 1980, 57, 155 |
| vlm_177643 | 1 | lit_11710 | 80TK | A. V. Tyulin and Yu. P. Khranilov, Soviet J. Coord. Chem., 1980, 6, 515 (1034) |

---

### Step 13: `search_citations`
**Args:**
```json
{
  "where": "(rv.vlm_id = vlm_177644)"
}
```

[summary]
## search_citations — 50 row(s)

| example_vlm_id | vlm_count | lit_id | shortcut | citation |
|----------------|-----------|--------|----------|----------|
| vlm_177644 | 1 | lit_265 | 30RD | E. C. Righellato and C. W. Davies, Trans. Faraday Soc., 1930, 26, 592 |
| vlm_177644 | 1 | lit_276 | 31F | H. Fromherz, Z. Phys. Chem., 1931, A153, 376 |
| vlm_177644 | 1 | lit_278 | 31FL | H. Fromherz and K. H. Lih, Z. Phys. Chem., 1931, A153, 321, 376 |
| vlm_177644 | 1 | lit_488 | 38G | E. Guntelberg, Thesis, Copenhagen, 1938 |
| vlm_177644 | 1 | lit_602 | 42GN | A. B. Garrett, M. V. Noble, and S. Miller, J. Chem. Educ., 1942, 19, 485 |
| vlm_177644 | 1 | lit_673 | 44NG | M. V. Noble and A. B. Garrett, J. Amer. Chem. Soc., 1944, 66, 231 |
| vlm_177644 | 1 | lit_694 | 45Na | R. Nasanen, Ann. Acad. Sci. Fenn., 1945, AII, No. 13 |
| vlm_177644 | 1 | lit_816 | 49GGa | R. M. Garrels and F. T. Gucker, Jr., Chem. Rev., 1949, 44, 117 |
| vlm_177644 | 1 | lit_825 | 49Jb | J. C. James, J. Amer. Chem. Soc., 1949, 71, 3243 |
| vlm_177644 | 1 | lit_1197 | 56Cc | B. Charreton, Bull. Soc. Chim. France, 1956, 323, 337, 347 |
| vlm_177644 | 1 | lit_1627 | 80LBa | M. Lovric and M. Branica, Croat. Chem. Acta, 1980, 53, 503 |
| vlm_177644 | 1 | lit_2107 | 55BPP | A. I. Biggs, M. H. Panckhurst, and H. N. Parton, Trans. Faraday Soc., 1955, 51,… |
| vlm_177644 | 1 | lit_2108 | 55BPR | A. I. Biggs, H. N. Parton, and R. A. Robinson, J. Amer. Chem. Soc., 1955, 77, 5… |
| vlm_177644 | 1 | lit_2160 | 55K | P. Kivalo, Suomen Kem., 1955, B28, 155 |
| vlm_177644 | 1 | lit_2199 | 55Na | G. H. Nancollas, J. Chem. Soc., 1955, 1458 |
| vlm_177644 | 1 | lit_2277 | 56P | P. Papoff, Suomen Kem., 1956, B29, 97 |
| vlm_177644 | 1 | lit_2452 | 57KL | P. Kivalo and R. Luoto, Suomen Kem., 1957, B30, 163 |
| vlm_177644 | 1 | lit_2512 | 57PCF | P. Papoff, M. A. Caliumi, and G. Ferrari, Ric. Sci., 1957, 27, suppl. A; Polaro… |
| vlm_177644 | 1 | lit_3036 | 59TCa | Ya. I. Turyan and N. G. Chebotar, Russ. J. Inorg. Chem., 1959, 4, 273 (599) |
| vlm_177644 | 1 | lit_3148 | 60FSS | Ya. D. Fridman, D. S. Sarbaev, and R. I. Sorochan, Russ. J. Inorg. Chem., 1960,… |
| vlm_177644 | 1 | lit_3453 | 61M | V. E. Mironov, Russ. J. Inorg. Chem., 1961, 6, 205 (405) |
| vlm_177644 | 1 | lit_3492 | 61NR | C. J. Nyman, D. K. Roe, and R. A. Plane, J. Amer. Chem. Soc., 1961, 83, 323 |
| vlm_177644 | 1 | lit_3675 | 62FCa | J. Faucherre and A. Crego, Bull. Soc. Chim. France, 1962, 1820 |
| vlm_177644 | 1 | lit_4133 | 63MFN | V. E. Mironov, V. A. Fedorov, and V. A. Nazarov, Russ. J. Inorg. Chem., 1963, 8… |
| vlm_177644 | 1 | lit_4140 | 63MKc | V. E. Mironov, F. Ya. Kulba, V. A. Fedorov, and O. B. Tikhomirov, Russ. J. Inor… |
| vlm_177644 | 1 | lit_4317 | 64AP | V. I. Altynov and B. V. Ptitsyn, Russ. J. Inorg. Chem., 1964, 9, 1301 (2407) |
| vlm_177644 | 1 | lit_4343 | 64BMa | E. Ya. Benyash and T. G. Maslakova, Russ. J. Inorg. Chem., 1964, 9, 1472 (2731) |
| vlm_177644 | 1 | lit_4486 | 64MK | V. E. Mironov, F. Ya. Kulba, and V. A. Fedorov, Russ. J. Inorg. Chem., 1964, 9,… |
| vlm_177644 | 1 | lit_4488 | 64MKb | V. E. Mironov, F. Ya. Kulba, V. A. Fedorov, and A. V. Fedorova, Russ. J. Inorg.… |
| vlm_177644 | 1 | lit_4810 | 65HP | G. P. Haight, Jr., and J. R. Peterson, Inorg. Chem., 1965, 4, 1073 |
| vlm_177644 | 1 | lit_4883 | 65MKF | V. E. Mironov, F. Ya. Kulba, and V. A. Fedorov, Russ. J. Inorg. Chem., 1965, 10… |
| vlm_177644 | 1 | lit_5433 | 66VSB | F. Vierling, G. Schorsch, and J. Bye, Rev. Chim. Miner., 1966, 3, 875 |
| vlm_177644 | 1 | lit_6479 | 69FKM | V. A. Fedorov, M. Ya. Kutuzova, and V. E. Mironov, Fiz. Khim. Khim. Tekhnol., 1… |
| vlm_177644 | 1 | lit_6520 | 69Hd | H. C. Helgeson, Amer. J. Sci., 1969, 267, 729 |
| vlm_177644 | 1 | lit_7036 | 70FS | V. A. Fedorov, N. P. Samsonova, and V. E. Mironov, Russ. J. Inorg. Chem., 1970,… |
| vlm_177644 | 1 | lit_7345 | 71BHa | A. M. Bond and G. Hefter, J. Electroanal. Chem., 1971, 31, 477 |
| vlm_177644 | 1 | lit_7820 | 71V | F. Vierling, Bull. Soc. Chim. France, 1971, 22, 25 |
| vlm_177644 | 1 | lit_8011 | 72FSL | V. A. Fedorov, L. P. Shishin, S. G. Likhacheva, A. V. Fedorova, and V. E. Miron… |
| vlm_177644 | 1 | lit_8330 | 72SF | N. P. Samsonova, V. A. Fedorov, and V. E. Mironov, Russ. J. Phys. Chem., 1972, … |
| vlm_177644 | 1 | lit_8468 | 73BH | A. M. Bond and G. Hefter, J. Electroanal. Chem., 1973, 42, 1 |
| vlm_177644 | 1 | lit_8591 | 73HH | M. H. Hutchinson and W. C. E. Higginson, J. Chem. Soc. Dalton, 1973, 1247 |
| vlm_177644 | 1 | lit_8891 | 73V | F. Vierling, Ann. Chim. (Paris), 1973, 8, 53 |
| vlm_177644 | 1 | lit_9515 | 75Fa | V. A. Fedorov, Soviet J. Coord. Chem., 1975, 1, 751 (890) |
| vlm_177644 | 1 | lit_9671 | 75Ma | L. Meites, Talanta, 1975, 22, 733 |
| vlm_177644 | 1 | lit_9982 | 76FS | V. A. Fedorov and L. P. Shishin, Russ. J. Phys. Chem., 1976, 50, 210 (356) |
| vlm_177644 | 1 | lit_10300 | 76YK | E. N. Yurchenko, G. R. Kolonin, G. P. Shironosova, and T. P. Aksenova, Russ. J.… |
| vlm_177644 | 1 | lit_10362 | 77BL | C. Birraux, J. C. Landry, and W. Haerdi, Anal. Chim. Acta, 1977, 90, 51 |
| vlm_177644 | 1 | lit_11061 | 79BKa | S. D. Brown and B. R. Kowalski, Anal. Chem., 1979, 51, 2133 |
| vlm_177644 | 1 | lit_11630 | 80PPb | A. K. Prasad and B. Prasad, J. Indian Chem. Soc., 1980, 57, 155 |
| vlm_177644 | 1 | lit_11710 | 80TK | A. V. Tyulin and Yu. P. Khranilov, Soviet J. Coord. Chem., 1980, 6, 515 (1034) |

---

### Step 14: `search_citations`
**Args:**
```json
{
  "where": "(rv.vlm_id = vlm_177645)"
}
```

[summary]
## search_citations — 50 row(s)

| example_vlm_id | vlm_count | lit_id | shortcut | citation |
|----------------|-----------|--------|----------|----------|
| vlm_177645 | 1 | lit_265 | 30RD | E. C. Righellato and C. W. Davies, Trans. Faraday Soc., 1930, 26, 592 |
| vlm_177645 | 1 | lit_276 | 31F | H. Fromherz, Z. Phys. Chem., 1931, A153, 376 |
| vlm_177645 | 1 | lit_278 | 31FL | H. Fromherz and K. H. Lih, Z. Phys. Chem., 1931, A153, 321, 376 |
| vlm_177645 | 1 | lit_488 | 38G | E. Guntelberg, Thesis, Copenhagen, 1938 |
| vlm_177645 | 1 | lit_602 | 42GN | A. B. Garrett, M. V. Noble, and S. Miller, J. Chem. Educ., 1942, 19, 485 |
| vlm_177645 | 1 | lit_673 | 44NG | M. V. Noble and A. B. Garrett, J. Amer. Chem. Soc., 1944, 66, 231 |
| vlm_177645 | 1 | lit_694 | 45Na | R. Nasanen, Ann. Acad. Sci. Fenn., 1945, AII, No. 13 |
| vlm_177645 | 1 | lit_816 | 49GGa | R. M. Garrels and F. T. Gucker, Jr., Chem. Rev., 1949, 44, 117 |
| vlm_177645 | 1 | lit_825 | 49Jb | J. C. James, J. Amer. Chem. Soc., 1949, 71, 3243 |
| vlm_177645 | 1 | lit_1197 | 56Cc | B. Charreton, Bull. Soc. Chim. France, 1956, 323, 337, 347 |
| vlm_177645 | 1 | lit_1627 | 80LBa | M. Lovric and M. Branica, Croat. Chem. Acta, 1980, 53, 503 |
| vlm_177645 | 1 | lit_2107 | 55BPP | A. I. Biggs, M. H. Panckhurst, and H. N. Parton, Trans. Faraday Soc., 1955, 51,… |
| vlm_177645 | 1 | lit_2108 | 55BPR | A. I. Biggs, H. N. Parton, and R. A. Robinson, J. Amer. Chem. Soc., 1955, 77, 5… |
| vlm_177645 | 1 | lit_2160 | 55K | P. Kivalo, Suomen Kem., 1955, B28, 155 |
| vlm_177645 | 1 | lit_2199 | 55Na | G. H. Nancollas, J. Chem. Soc., 1955, 1458 |
| vlm_177645 | 1 | lit_2277 | 56P | P. Papoff, Suomen Kem., 1956, B29, 97 |
| vlm_177645 | 1 | lit_2452 | 57KL | P. Kivalo and R. Luoto, Suomen Kem., 1957, B30, 163 |
| vlm_177645 | 1 | lit_2512 | 57PCF | P. Papoff, M. A. Caliumi, and G. Ferrari, Ric. Sci., 1957, 27, suppl. A; Polaro… |
| vlm_177645 | 1 | lit_3036 | 59TCa | Ya. I. Turyan and N. G. Chebotar, Russ. J. Inorg. Chem., 1959, 4, 273 (599) |
| vlm_177645 | 1 | lit_3148 | 60FSS | Ya. D. Fridman, D. S. Sarbaev, and R. I. Sorochan, Russ. J. Inorg. Chem., 1960,… |
| vlm_177645 | 1 | lit_3453 | 61M | V. E. Mironov, Russ. J. Inorg. Chem., 1961, 6, 205 (405) |
| vlm_177645 | 1 | lit_3492 | 61NR | C. J. Nyman, D. K. Roe, and R. A. Plane, J. Amer. Chem. Soc., 1961, 83, 323 |
| vlm_177645 | 1 | lit_3675 | 62FCa | J. Faucherre and A. Crego, Bull. Soc. Chim. France, 1962, 1820 |
| vlm_177645 | 1 | lit_4133 | 63MFN | V. E. Mironov, V. A. Fedorov, and V. A. Nazarov, Russ. J. Inorg. Chem., 1963, 8… |
| vlm_177645 | 1 | lit_4140 | 63MKc | V. E. Mironov, F. Ya. Kulba, V. A. Fedorov, and O. B. Tikhomirov, Russ. J. Inor… |
| vlm_177645 | 1 | lit_4317 | 64AP | V. I. Altynov and B. V. Ptitsyn, Russ. J. Inorg. Chem., 1964, 9, 1301 (2407) |
| vlm_177645 | 1 | lit_4343 | 64BMa | E. Ya. Benyash and T. G. Maslakova, Russ. J. Inorg. Chem., 1964, 9, 1472 (2731) |
| vlm_177645 | 1 | lit_4486 | 64MK | V. E. Mironov, F. Ya. Kulba, and V. A. Fedorov, Russ. J. Inorg. Chem., 1964, 9,… |
| vlm_177645 | 1 | lit_4488 | 64MKb | V. E. Mironov, F. Ya. Kulba, V. A. Fedorov, and A. V. Fedorova, Russ. J. Inorg.… |
| vlm_177645 | 1 | lit_4810 | 65HP | G. P. Haight, Jr., and J. R. Peterson, Inorg. Chem., 1965, 4, 1073 |
| vlm_177645 | 1 | lit_4883 | 65MKF | V. E. Mironov, F. Ya. Kulba, and V. A. Fedorov, Russ. J. Inorg. Chem., 1965, 10… |
| vlm_177645 | 1 | lit_5433 | 66VSB | F. Vierling, G. Schorsch, and J. Bye, Rev. Chim. Miner., 1966, 3, 875 |
| vlm_177645 | 1 | lit_6479 | 69FKM | V. A. Fedorov, M. Ya. Kutuzova, and V. E. Mironov, Fiz. Khim. Khim. Tekhnol., 1… |
| vlm_177645 | 1 | lit_6520 | 69Hd | H. C. Helgeson, Amer. J. Sci., 1969, 267, 729 |
| vlm_177645 | 1 | lit_7036 | 70FS | V. A. Fedorov, N. P. Samsonova, and V. E. Mironov, Russ. J. Inorg. Chem., 1970,… |
| vlm_177645 | 1 | lit_7345 | 71BHa | A. M. Bond and G. Hefter, J. Electroanal. Chem., 1971, 31, 477 |
| vlm_177645 | 1 | lit_7820 | 71V | F. Vierling, Bull. Soc. Chim. France, 1971, 22, 25 |
| vlm_177645 | 1 | lit_8011 | 72FSL | V. A. Fedorov, L. P. Shishin, S. G. Likhacheva, A. V. Fedorova, and V. E. Miron… |
| vlm_177645 | 1 | lit_8330 | 72SF | N. P. Samsonova, V. A. Fedorov, and V. E. Mironov, Russ. J. Phys. Chem., 1972, … |
| vlm_177645 | 1 | lit_8468 | 73BH | A. M. Bond and G. Hefter, J. Electroanal. Chem., 1973, 42, 1 |
| vlm_177645 | 1 | lit_8591 | 73HH | M. H. Hutchinson and W. C. E. Higginson, J. Chem. Soc. Dalton, 1973, 1247 |
| vlm_177645 | 1 | lit_8891 | 73V | F. Vierling, Ann. Chim. (Paris), 1973, 8, 53 |
| vlm_177645 | 1 | lit_9515 | 75Fa | V. A. Fedorov, Soviet J. Coord. Chem., 1975, 1, 751 (890) |
| vlm_177645 | 1 | lit_9671 | 75Ma | L. Meites, Talanta, 1975, 22, 733 |
| vlm_177645 | 1 | lit_9982 | 76FS | V. A. Fedorov and L. P. Shishin, Russ. J. Phys. Chem., 1976, 50, 210 (356) |
| vlm_177645 | 1 | lit_10300 | 76YK | E. N. Yurchenko, G. R. Kolonin, G. P. Shironosova, and T. P. Aksenova, Russ. J.… |
| vlm_177645 | 1 | lit_10362 | 77BL | C. Birraux, J. C. Landry, and W. Haerdi, Anal. Chim. Acta, 1977, 90, 51 |
| vlm_177645 | 1 | lit_11061 | 79BKa | S. D. Brown and B. R. Kowalski, Anal. Chem., 1979, 51, 2133 |
| vlm_177645 | 1 | lit_11630 | 80PPb | A. K. Prasad and B. Prasad, J. Indian Chem. Soc., 1980, 57, 155 |
| vlm_177645 | 1 | lit_11710 | 80TK | A. V. Tyulin and Yu. P. Khranilov, Soviet J. Coord. Chem., 1980, 6, 515 (1034) |

---

### Step 15: `search_citations`
**Args:**
```json
{
  "where": "(rv.vlm_id = vlm_177646)"
}
```

[summary]
## search_citations — 50 row(s)

| example_vlm_id | vlm_count | lit_id | shortcut | citation |
|----------------|-----------|--------|----------|----------|
| vlm_177646 | 1 | lit_265 | 30RD | E. C. Righellato and C. W. Davies, Trans. Faraday Soc., 1930, 26, 592 |
| vlm_177646 | 1 | lit_276 | 31F | H. Fromherz, Z. Phys. Chem., 1931, A153, 376 |
| vlm_177646 | 1 | lit_278 | 31FL | H. Fromherz and K. H. Lih, Z. Phys. Chem., 1931, A153, 321, 376 |
| vlm_177646 | 1 | lit_488 | 38G | E. Guntelberg, Thesis, Copenhagen, 1938 |
| vlm_177646 | 1 | lit_602 | 42GN | A. B. Garrett, M. V. Noble, and S. Miller, J. Chem. Educ., 1942, 19, 485 |
| vlm_177646 | 1 | lit_673 | 44NG | M. V. Noble and A. B. Garrett, J. Amer. Chem. Soc., 1944, 66, 231 |
| vlm_177646 | 1 | lit_694 | 45Na | R. Nasanen, Ann. Acad. Sci. Fenn., 1945, AII, No. 13 |
| vlm_177646 | 1 | lit_816 | 49GGa | R. M. Garrels and F. T. Gucker, Jr., Chem. Rev., 1949, 44, 117 |
| vlm_177646 | 1 | lit_825 | 49Jb | J. C. James, J. Amer. Chem. Soc., 1949, 71, 3243 |
| vlm_177646 | 1 | lit_1197 | 56Cc | B. Charreton, Bull. Soc. Chim. France, 1956, 323, 337, 347 |
| vlm_177646 | 1 | lit_1627 | 80LBa | M. Lovric and M. Branica, Croat. Chem. Acta, 1980, 53, 503 |
| vlm_177646 | 1 | lit_2107 | 55BPP | A. I. Biggs, M. H. Panckhurst, and H. N. Parton, Trans. Faraday Soc., 1955, 51,… |
| vlm_177646 | 1 | lit_2108 | 55BPR | A. I. Biggs, H. N. Parton, and R. A. Robinson, J. Amer. Chem. Soc., 1955, 77, 5… |
| vlm_177646 | 1 | lit_2160 | 55K | P. Kivalo, Suomen Kem., 1955, B28, 155 |
| vlm_177646 | 1 | lit_2199 | 55Na | G. H. Nancollas, J. Chem. Soc., 1955, 1458 |
| vlm_177646 | 1 | lit_2277 | 56P | P. Papoff, Suomen Kem., 1956, B29, 97 |
| vlm_177646 | 1 | lit_2452 | 57KL | P. Kivalo and R. Luoto, Suomen Kem., 1957, B30, 163 |
| vlm_177646 | 1 | lit_2512 | 57PCF | P. Papoff, M. A. Caliumi, and G. Ferrari, Ric. Sci., 1957, 27, suppl. A; Polaro… |
| vlm_177646 | 1 | lit_3036 | 59TCa | Ya. I. Turyan and N. G. Chebotar, Russ. J. Inorg. Chem., 1959, 4, 273 (599) |
| vlm_177646 | 1 | lit_3148 | 60FSS | Ya. D. Fridman, D. S. Sarbaev, and R. I. Sorochan, Russ. J. Inorg. Chem., 1960,… |
| vlm_177646 | 1 | lit_3453 | 61M | V. E. Mironov, Russ. J. Inorg. Chem., 1961, 6, 205 (405) |
| vlm_177646 | 1 | lit_3492 | 61NR | C. J. Nyman, D. K. Roe, and R. A. Plane, J. Amer. Chem. Soc., 1961, 83, 323 |
| vlm_177646 | 1 | lit_3675 | 62FCa | J. Faucherre and A. Crego, Bull. Soc. Chim. France, 1962, 1820 |
| vlm_177646 | 1 | lit_4133 | 63MFN | V. E. Mironov, V. A. Fedorov, and V. A. Nazarov, Russ. J. Inorg. Chem., 1963, 8… |
| vlm_177646 | 1 | lit_4140 | 63MKc | V. E. Mironov, F. Ya. Kulba, V. A. Fedorov, and O. B. Tikhomirov, Russ. J. Inor… |
| vlm_177646 | 1 | lit_4317 | 64AP | V. I. Altynov and B. V. Ptitsyn, Russ. J. Inorg. Chem., 1964, 9, 1301 (2407) |
| vlm_177646 | 1 | lit_4343 | 64BMa | E. Ya. Benyash and T. G. Maslakova, Russ. J. Inorg. Chem., 1964, 9, 1472 (2731) |
| vlm_177646 | 1 | lit_4486 | 64MK | V. E. Mironov, F. Ya. Kulba, and V. A. Fedorov, Russ. J. Inorg. Chem., 1964, 9,… |
| vlm_177646 | 1 | lit_4488 | 64MKb | V. E. Mironov, F. Ya. Kulba, V. A. Fedorov, and A. V. Fedorova, Russ. J. Inorg.… |
| vlm_177646 | 1 | lit_4810 | 65HP | G. P. Haight, Jr., and J. R. Peterson, Inorg. Chem., 1965, 4, 1073 |
| vlm_177646 | 1 | lit_4883 | 65MKF | V. E. Mironov, F. Ya. Kulba, and V. A. Fedorov, Russ. J. Inorg. Chem., 1965, 10… |
| vlm_177646 | 1 | lit_5433 | 66VSB | F. Vierling, G. Schorsch, and J. Bye, Rev. Chim. Miner., 1966, 3, 875 |
| vlm_177646 | 1 | lit_6479 | 69FKM | V. A. Fedorov, M. Ya. Kutuzova, and V. E. Mironov, Fiz. Khim. Khim. Tekhnol., 1… |
| vlm_177646 | 1 | lit_6520 | 69Hd | H. C. Helgeson, Amer. J. Sci., 1969, 267, 729 |
| vlm_177646 | 1 | lit_7036 | 70FS | V. A. Fedorov, N. P. Samsonova, and V. E. Mironov, Russ. J. Inorg. Chem., 1970,… |
| vlm_177646 | 1 | lit_7345 | 71BHa | A. M. Bond and G. Hefter, J. Electroanal. Chem., 1971, 31, 477 |
| vlm_177646 | 1 | lit_7820 | 71V | F. Vierling, Bull. Soc. Chim. France, 1971, 22, 25 |
| vlm_177646 | 1 | lit_8011 | 72FSL | V. A. Fedorov, L. P. Shishin, S. G. Likhacheva, A. V. Fedorova, and V. E. Miron… |
| vlm_177646 | 1 | lit_8330 | 72SF | N. P. Samsonova, V. A. Fedorov, and V. E. Mironov, Russ. J. Phys. Chem., 1972, … |
| vlm_177646 | 1 | lit_8468 | 73BH | A. M. Bond and G. Hefter, J. Electroanal. Chem., 1973, 42, 1 |
| vlm_177646 | 1 | lit_8591 | 73HH | M. H. Hutchinson and W. C. E. Higginson, J. Chem. Soc. Dalton, 1973, 1247 |
| vlm_177646 | 1 | lit_8891 | 73V | F. Vierling, Ann. Chim. (Paris), 1973, 8, 53 |
| vlm_177646 | 1 | lit_9515 | 75Fa | V. A. Fedorov, Soviet J. Coord. Chem., 1975, 1, 751 (890) |
| vlm_177646 | 1 | lit_9671 | 75Ma | L. Meites, Talanta, 1975, 22, 733 |
| vlm_177646 | 1 | lit_9982 | 76FS | V. A. Fedorov and L. P. Shishin, Russ. J. Phys. Chem., 1976, 50, 210 (356) |
| vlm_177646 | 1 | lit_10300 | 76YK | E. N. Yurchenko, G. R. Kolonin, G. P. Shironosova, and T. P. Aksenova, Russ. J.… |
| vlm_177646 | 1 | lit_10362 | 77BL | C. Birraux, J. C. Landry, and W. Haerdi, Anal. Chim. Acta, 1977, 90, 51 |
| vlm_177646 | 1 | lit_11061 | 79BKa | S. D. Brown and B. R. Kowalski, Anal. Chem., 1979, 51, 2133 |
| vlm_177646 | 1 | lit_11630 | 80PPb | A. K. Prasad and B. Prasad, J. Indian Chem. Soc., 1980, 57, 155 |
| vlm_177646 | 1 | lit_11710 | 80TK | A. V. Tyulin and Yu. P. Khranilov, Soviet J. Coord. Chem., 1980, 6, 515 (1034) |

---

### Step 16: `search_citations`
**Args:**
```json
{
  "where": "(rv.vlm_id = vlm_177647)"
}
```

[summary]
## search_citations — 50 row(s)

| example_vlm_id | vlm_count | lit_id | shortcut | citation |
|----------------|-----------|--------|----------|----------|
| vlm_177647 | 1 | lit_265 | 30RD | E. C. Righellato and C. W. Davies, Trans. Faraday Soc., 1930, 26, 592 |
| vlm_177647 | 1 | lit_276 | 31F | H. Fromherz, Z. Phys. Chem., 1931, A153, 376 |
| vlm_177647 | 1 | lit_278 | 31FL | H. Fromherz and K. H. Lih, Z. Phys. Chem., 1931, A153, 321, 376 |
| vlm_177647 | 1 | lit_488 | 38G | E. Guntelberg, Thesis, Copenhagen, 1938 |
| vlm_177647 | 1 | lit_602 | 42GN | A. B. Garrett, M. V. Noble, and S. Miller, J. Chem. Educ., 1942, 19, 485 |
| vlm_177647 | 1 | lit_673 | 44NG | M. V. Noble and A. B. Garrett, J. Amer. Chem. Soc., 1944, 66, 231 |
| vlm_177647 | 1 | lit_694 | 45Na | R. Nasanen, Ann. Acad. Sci. Fenn., 1945, AII, No. 13 |
| vlm_177647 | 1 | lit_816 | 49GGa | R. M. Garrels and F. T. Gucker, Jr., Chem. Rev., 1949, 44, 117 |
| vlm_177647 | 1 | lit_825 | 49Jb | J. C. James, J. Amer. Chem. Soc., 1949, 71, 3243 |
| vlm_177647 | 1 | lit_1197 | 56Cc | B. Charreton, Bull. Soc. Chim. France, 1956, 323, 337, 347 |
| vlm_177647 | 1 | lit_1627 | 80LBa | M. Lovric and M. Branica, Croat. Chem. Acta, 1980, 53, 503 |
| vlm_177647 | 1 | lit_2107 | 55BPP | A. I. Biggs, M. H. Panckhurst, and H. N. Parton, Trans. Faraday Soc., 1955, 51,… |
| vlm_177647 | 1 | lit_2108 | 55BPR | A. I. Biggs, H. N. Parton, and R. A. Robinson, J. Amer. Chem. Soc., 1955, 77, 5… |
| vlm_177647 | 1 | lit_2160 | 55K | P. Kivalo, Suomen Kem., 1955, B28, 155 |
| vlm_177647 | 1 | lit_2199 | 55Na | G. H. Nancollas, J. Chem. Soc., 1955, 1458 |
| vlm_177647 | 1 | lit_2277 | 56P | P. Papoff, Suomen Kem., 1956, B29, 97 |
| vlm_177647 | 1 | lit_2452 | 57KL | P. Kivalo and R. Luoto, Suomen Kem., 1957, B30, 163 |
| vlm_177647 | 1 | lit_2512 | 57PCF | P. Papoff, M. A. Caliumi, and G. Ferrari, Ric. Sci., 1957, 27, suppl. A; Polaro… |
| vlm_177647 | 1 | lit_3036 | 59TCa | Ya. I. Turyan and N. G. Chebotar, Russ. J. Inorg. Chem., 1959, 4, 273 (599) |
| vlm_177647 | 1 | lit_3148 | 60FSS | Ya. D. Fridman, D. S. Sarbaev, and R. I. Sorochan, Russ. J. Inorg. Chem., 1960,… |
| vlm_177647 | 1 | lit_3453 | 61M | V. E. Mironov, Russ. J. Inorg. Chem., 1961, 6, 205 (405) |
| vlm_177647 | 1 | lit_3492 | 61NR | C. J. Nyman, D. K. Roe, and R. A. Plane, J. Amer. Chem. Soc., 1961, 83, 323 |
| vlm_177647 | 1 | lit_3675 | 62FCa | J. Faucherre and A. Crego, Bull. Soc. Chim. France, 1962, 1820 |
| vlm_177647 | 1 | lit_4133 | 63MFN | V. E. Mironov, V. A. Fedorov, and V. A. Nazarov, Russ. J. Inorg. Chem., 1963, 8… |
| vlm_177647 | 1 | lit_4140 | 63MKc | V. E. Mironov, F. Ya. Kulba, V. A. Fedorov, and O. B. Tikhomirov, Russ. J. Inor… |
| vlm_177647 | 1 | lit_4317 | 64AP | V. I. Altynov and B. V. Ptitsyn, Russ. J. Inorg. Chem., 1964, 9, 1301 (2407) |
| vlm_177647 | 1 | lit_4343 | 64BMa | E. Ya. Benyash and T. G. Maslakova, Russ. J. Inorg. Chem., 1964, 9, 1472 (2731) |
| vlm_177647 | 1 | lit_4486 | 64MK | V. E. Mironov, F. Ya. Kulba, and V. A. Fedorov, Russ. J. Inorg. Chem., 1964, 9,… |
| vlm_177647 | 1 | lit_4488 | 64MKb | V. E. Mironov, F. Ya. Kulba, V. A. Fedorov, and A. V. Fedorova, Russ. J. Inorg.… |
| vlm_177647 | 1 | lit_4810 | 65HP | G. P. Haight, Jr., and J. R. Peterson, Inorg. Chem., 1965, 4, 1073 |
| vlm_177647 | 1 | lit_4883 | 65MKF | V. E. Mironov, F. Ya. Kulba, and V. A. Fedorov, Russ. J. Inorg. Chem., 1965, 10… |
| vlm_177647 | 1 | lit_5433 | 66VSB | F. Vierling, G. Schorsch, and J. Bye, Rev. Chim. Miner., 1966, 3, 875 |
| vlm_177647 | 1 | lit_6479 | 69FKM | V. A. Fedorov, M. Ya. Kutuzova, and V. E. Mironov, Fiz. Khim. Khim. Tekhnol., 1… |
| vlm_177647 | 1 | lit_6520 | 69Hd | H. C. Helgeson, Amer. J. Sci., 1969, 267, 729 |
| vlm_177647 | 1 | lit_7036 | 70FS | V. A. Fedorov, N. P. Samsonova, and V. E. Mironov, Russ. J. Inorg. Chem., 1970,… |
| vlm_177647 | 1 | lit_7345 | 71BHa | A. M. Bond and G. Hefter, J. Electroanal. Chem., 1971, 31, 477 |
| vlm_177647 | 1 | lit_7820 | 71V | F. Vierling, Bull. Soc. Chim. France, 1971, 22, 25 |
| vlm_177647 | 1 | lit_8011 | 72FSL | V. A. Fedorov, L. P. Shishin, S. G. Likhacheva, A. V. Fedorova, and V. E. Miron… |
| vlm_177647 | 1 | lit_8330 | 72SF | N. P. Samsonova, V. A. Fedorov, and V. E. Mironov, Russ. J. Phys. Chem., 1972, … |
| vlm_177647 | 1 | lit_8468 | 73BH | A. M. Bond and G. Hefter, J. Electroanal. Chem., 1973, 42, 1 |
| vlm_177647 | 1 | lit_8591 | 73HH | M. H. Hutchinson and W. C. E. Higginson, J. Chem. Soc. Dalton, 1973, 1247 |
| vlm_177647 | 1 | lit_8891 | 73V | F. Vierling, Ann. Chim. (Paris), 1973, 8, 53 |
| vlm_177647 | 1 | lit_9515 | 75Fa | V. A. Fedorov, Soviet J. Coord. Chem., 1975, 1, 751 (890) |
| vlm_177647 | 1 | lit_9671 | 75Ma | L. Meites, Talanta, 1975, 22, 733 |
| vlm_177647 | 1 | lit_9982 | 76FS | V. A. Fedorov and L. P. Shishin, Russ. J. Phys. Chem., 1976, 50, 210 (356) |
| vlm_177647 | 1 | lit_10300 | 76YK | E. N. Yurchenko, G. R. Kolonin, G. P. Shironosova, and T. P. Aksenova, Russ. J.… |
| vlm_177647 | 1 | lit_10362 | 77BL | C. Birraux, J. C. Landry, and W. Haerdi, Anal. Chim. Acta, 1977, 90, 51 |
| vlm_177647 | 1 | lit_11061 | 79BKa | S. D. Brown and B. R. Kowalski, Anal. Chem., 1979, 51, 2133 |
| vlm_177647 | 1 | lit_11630 | 80PPb | A. K. Prasad and B. Prasad, J. Indian Chem. Soc., 1980, 57, 155 |
| vlm_177647 | 1 | lit_11710 | 80TK | A. V. Tyulin and Yu. P. Khranilov, Soviet J. Coord. Chem., 1980, 6, 515 (1034) |

---

### Step 17: `inspect_card`
**Args:**
```json
{
  "prefix_id": "vlm_177644"
}
```

[summary]
## inspect_card — VLM | vlm_177644

### Metal
**metal_id:** metal_125 | **metal_name:** Pb^[2+]  
**metal_SMILES:** `[Pb+2]`  
**metal_InChi:** `InChI=1S/Pb/q+2`  

### Ligand
**ligand_id:** ligand_10163 | **ligand_name:** Chloride ion  

### Stability
**vlm_id:** vlm_177644  
**beta_definition_id:** beta_def_812 | **beta_definition_name:** [ML]/[M][L]  
**data_type:** log_K | **log_K:** 1.23  
**temperature:** 25.0 °C | **ionic_strength:** 4.0 M  
**uncertainty:** +/-8  
**solvent:** H_[2]O | **reaction_type:** homogeneous_aqueous  
**equation:** [M] + [L] <=> [ML]  
**Ligand_HxL_involved:** [L]  
**LHS_species:** [M], [L] | **RHS_species:** [ML]  

### Networks
1 network(s)

| network_id | Nodes | Edges | node_id | dup? |
|------------|-------|-------|---------|------|
| ref_eq_net_29936 | 3 | 3 | eq_node_59794 |  |

**total_citations:** 67

---
