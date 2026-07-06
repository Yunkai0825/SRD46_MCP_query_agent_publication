# Q3.1.3 — Tool Results (batch 1)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Zn(II)",
  "limit": 10
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_208 | Zn^[2+] | Zn | 2 | ✓ | [Zn+2] | InChI=1S/Zn/q+2 | beta_totN_122 | ligand_totN_1169 | vlm_totN_4095 |

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "histidine",
  "limit": 10
}
```

[summary]
## search_ligands — 10 result(s)

**stats:** 57 SQL matches · showing 10 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5860 | DL-2-Amino-3-(2-mercaptoimidazo-4… (Thiohistidine) | H2L | Amino Acids | 20 | `NC(Cc1cnc(S)[nH]1)C(=O)O` | (-inf, H2L, 8.59, HL, 8.59, L, +inf) |
| ligand_5898 | L-2-Amino-3-(4-imidazolyl)propanoic a… (Histidine) | HL | Amino Acids | 250 | `N[C@@H](Cc1c[nH]cn1)C(=O)O` | (-inf, H3L, -1.7, H2L, 6.05, HL, 9.1, L, +inf) |
| ligand_5899 | L-2-Amino-3-(N(1)-methyl-4-imidazolyl)propanoic a… | HL | Amino Acids | 14 | `Cn1cnc(C[C@H](N)C(=O)O)c1` | (-inf, H3L, -1.72, H2L, 5.87, HL, 9.16, L, +inf) |
| ligand_5900 | L-2-Amino-3-(N(3)-methyl-4-imidazolyl)propanoic a… | HL | Amino Acids | 16 | `Cn1cncc1C[C@H](N)C(=O)O` | (-inf, H3L, -1.65, H2L, 6.48, HL, 8.61, L, +inf) |
| ligand_5901 | L-4-(2-Amino-3-carboxypropyl)-1,3-dimethylimidazo… | HL | Amino Acids | 6 | `Cn1c[n+](C)cc1C[C@H](N)C(=O)O` | (-inf, H2L, -1.98, HL, 7.85, L, +inf) |
| ligand_5902 | L-1-Carboxy-2-(4-imidazolyl)ethyl(dimethyl)ammoni… | HL | Amino Acids | 9 | `C[NH+](C)C(Cc1cnc[nH]1)C(=O)O` | (-inf, H3L, -1.03, H2L, 6.03, HL, 8.86, L, +inf) |
| ligand_5903 | L-1-Carboxy-2-(4-imidazolyl)ethyl(trimethyl)ammon… | HL | Amino Acids | 6 | `C[N+](C)(C)C(Cc1c[nH]cn1)C(=O)O` | (-inf, H2L, -0.98, HL, 6, L, +inf) |
| ligand_5904 | L-2-Amino-3-(N(3)-benzyl-4-imidazolyl)propanoic a… | HL | Amino Acids | 18 | `NC(Cc1cncn1Cc1ccccc1)C(=O)O` | (-inf, H3L, 1.94, H2L, 5.53, HL, 9.21, L, +inf) |
| ligand_5905 | L-2-Amino-3-(5-iodo-4-imidazol… (5-Iodo-Histidine) | HL | Amino Acids | 23 | `N[C@@H](Cc1nc[nH]c1I)C(=O)O` | (-inf, H3L, -1.47, H2L, 4.21, HL, 8.6, L, +inf) |
| ligand_5906 | L-2-Amino-3-(2,5-diiodo-4-… (2,5-Diiodo-Histidine) | HL | Amino Acids | 27 | `N[C@@H](Cc1nc(I)[nH]c1I)C(=O)O` | (-inf, H4L, -1.55, H3L, 2.74, H2L, 8.12, HL, 9.57, L, +inf) |

### Functional groups across all SQL matches (46 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 40 | 87% |
| aromatic_ring | 38 | 83% |
| amide | 31 | 67% |
| primary_amine | 26 | 57% |
| imine | 9 | 20% |
| ester | 5 | 11% |
| secondary_amine | 5 | 11% |
| thiol | 4 | 9% |
| hydroxyl | 3 | 7% |
| halide | 2 | 4% |
| phenol | 2 | 4% |
| pyridine | 1 | 2% |
| tertiary_amine | 1 | 2% |
| thioether | 1 | 2% |

---

### Step 4: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_208",
  "ligand_id": "ligand_5898"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 6 species

### Zn^[2+] + L-2-Amino-3-(4-imidazolyl)propanoic acid (Histidine)
**metal_id:** metal_208 | **ligand_id:** ligand_5898 | **ligand_def_HxL:** HL  
**entries:** 29 | **species:** 6 | **vlm_count:** 29

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_204 | [M(HL)<sub>2</sub>]/[MHL<sub>2</sub>][H] | [MHL2] + [H] <=> [M(HL)2] | [M(HL)2](aqueous), [MHL2](aqueous), [H](aqueous) | 1 |
| beta_def_788 | [MHL]/[ML][H] | [ML] + [H] <=> [MHL] | [MHL](aqueous), [ML](aqueous), [H](aqueous) | 4 |
| beta_def_792 | [MHL<sub>2</sub>]/[ML<sub>2</sub>][H] | [ML2] + [H] <=> [MHL2] | [MHL2](aqueous), [ML2](aqueous), [H](aqueous) | 3 |
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 8 |
| beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | [M] + [L]^2 <=> [ML2] | [ML2](aqueous), [M](aqueous), [L](aqueous) | 12 |
| beta_def_984 | [ML<sub>2</sub>]/[M(OH)L<sub>2</sub>][H] | [M(OH)L2] + [H] <=> [ML2] + [H2O] | [ML2](aqueous), [H2O](aqueous), [M(OH)L2](aqueous), [H](aqueous) | 1 |

**vlm_ids:** vlm_98899, vlm_98900, vlm_98901, vlm_98902, vlm_98903, … vlm_98925, vlm_98926, vlm_98927 (29 listed)

**equilibrium_maps:** 6 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_1354 | 5 | 6 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_1355 | 4 | 4 | 31~41 °C | 0~0.3 M |
| ref_eq_net_1356 | 3 | 2 | 19~29 °C | 0.35~0.65 M |
| ref_eq_net_1357 | 2 | 1 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_1358 | 2 | 1 | 19~29 °C | 2.85~3.15 M |
| ref_eq_net_1359 | 2 | 1 | 19~29 °C | -0.05~0.25 M |

---

### Step 6: `search_citations`
**Args:**
```json
{
  "where": "(la.citation LIKE '%histidine%' AND la.citation LIKE '%zinc%' AND la.citation LIKE '%2005%')",
  "order_by": "la.citation",
  "limit": 20
}
```

[summary]
## search_citations

*(no results)*

---

### Step 7: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND c.ligand_id = ligand_5898 AND s.temperature_c >= 20 AND s.temperature_c <= 30)",
  "order_by": "s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability — 25 row(s)

### `Zn^[2+]` + L-2-Amino-3-(4-imidazolyl)propanoic acid (Histidine) — 25 measurement(s)
metal_id: metal_208 | ligand_id: ligand_5898
ligand_HxL_def: HL | ligand_SMILES: N[C@@H](Cc1c[nH]cn1)C(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_98916 | *** | beta_def_840 | ΔS | 72 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.1, L, +inf) |
| vlm_98918 | *** | beta_def_840 | ΔS | 58.2 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.1, L, +inf) |
| vlm_98906 | *** | beta_def_812 | ΔS | 57.3 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.1, L, +inf) |
| vlm_98912 | ref_eq_map_1357 | beta_def_840 | logK | 12.74 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.1, L, +inf) |
| vlm_98911 | ref_eq_map_1356 | beta_def_840 | logK | 12.29 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.1, L, +inf) |
| vlm_98907 | ref_eq_map_1353 | beta_def_840 | logK | 12.04 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.1, L, +inf) |
| vlm_98910 | ref_eq_map_1355 | beta_def_840 | logK | 11.91 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.1, L, +inf) |
| vlm_98927 | ref_eq_map_1355 | beta_def_984 | logK | 9.95 | 25 | 0.5 | `[M(OH)L2] + [H] <=> [ML2] + [H2O]` | *** |  |  |
| vlm_98903 | ref_eq_map_1357 | beta_def_812 | logK | 7.07 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (9.1, L, +inf) |
| vlm_98902 | ref_eq_map_1356 | beta_def_812 | logK | 6.58 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.1, L, +inf) |
| vlm_98899 | ref_eq_map_1353 | beta_def_812 | logK | 6.51 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.1, L, +inf) |
| vlm_98901 | ref_eq_map_1355 | beta_def_812 | logK | 6.48 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.1, L, +inf) |
| vlm_98924 | ref_eq_map_1353 | beta_def_792 | logK | 5.8 | 25 | 0.1 | `[ML2] + [H] <=> [MHL2]` | *** |  |  |
| vlm_98923 | ref_eq_map_1353 | beta_def_204 | logK | 5.67 | 25 | 0.1 | `[MHL2] + [H] <=> [M(HL)2]` | *** |  |  |
| vlm_98919 | ref_eq_map_1353 | beta_def_788 | logK | 4.86 | 25 | 0.1 | `[ML] + [H] <=> [MHL]` | *** |  |  |
| vlm_98922 | *** | beta_def_788 | ΔS | 0.4 | 25 | 0.1 | `[ML] + [H] <=> [MHL]` | *** |  |  |
| vlm_98914 | *** | beta_def_840 | ΔH | 0 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.1, L, +inf) |
| vlm_98925 | ref_eq_map_1358 | beta_def_792 | logK | -5.54 | 25 | 0.1 | `[ML2] + [H] <=> [MHL2]` | *** |  |  |
| vlm_98908 | ref_eq_map_1358 | beta_def_840 | logK | -12.18 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.1, L, +inf) |
| vlm_98904 | *** | beta_def_812 | ΔH | -20.1 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.1, L, +inf) |
| vlm_98905 | *** | beta_def_812 | ΔH | -23 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (9.1, L, +inf) |
| vlm_98921 | *** | beta_def_788 | ΔH | -27.6 | 25 | 0.1 | `[ML] + [H] <=> [MHL]` | *** |  |  |
| vlm_98913 | *** | beta_def_840 | ΔH | -47.3 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.1, L, +inf) |
| vlm_98915 | *** | beta_def_840 | ΔH | -49.4 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.1, L, +inf) |
| vlm_98917 | *** | beta_def_840 | ΔS | -67.4 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.1, L, +inf) |

---

### Step 8: `inspect_literature`
**Args:**
```json
{
  "prefix_id": "vlm_98899"
}
```

[summary]
## inspect_literature — vlm_98899 — 53 citation(s)

| lit_id | shortcut | citation |
|--------|----------|----------|
| lit_855 | 49MM | L. E. Maley and D. P. Mellor, Aust. J. Sci. Res., 1949, A2, 579 |
| lit_1066 | 52A | A. Albert, Biochem. J., 1952, 50, 690 |
| lit_1902 | 53P | D. J. Perkins, Biochem. J., 1953, 55, 649 |
| lit_2179 | 55LM | N. C. Li and R. A. Manning, J. Amer. Chem. Soc., 1955, 77, 5225 |
| lit_2619 | 58Ea | J. Engelmann, Diss., U. Giesson, 1958 (see 60WS) |
| lit_2935 | 59LR | R. Leberman and B. R. Rabin, Trans. Faraday Soc., 1959, 55, 1660 |
| lit_3533 | 61Si | I. C. Smith, Diss., Kansas State Univ., 1961 |
| lit_3968 | 63CC | A. Chakravorty and F. A. Cotton, J. Phys. Chem., 1963, 67, 2878 |
| lit_4678 | 65AZ | A. C. Andrews and D. M. Zebolsky, J. Chem. Soc., 1965, 742 |
| lit_5337 | 66PA | O. N. Puplikova, L. N. Akimova, and I. A. Savich, Moscow Univ. Chem. Bull., 196… |
| lit_5774 | 67PSa | D. D. Perrin and V. S. Sharma, J. Chem. Soc. (A), 1967, 724 |
| lit_5831 | 67SS | W. F. Stack and H. A. Skinner, Trans. Faraday Soc., 1967, 63, 1136 |
| lit_6621 | 69MBb | R. P. Martin and M. Blanc, Bull. Soc. Chim. France, 1969, 1866 |
| lit_6752 | 69RM | E. V. Raju and H. B. Mathur, J. Inorg. Nucl. Chem., 1969, 31, 425 |
| lit_6838 | 69TS | A. C. R. Thornton and H. A. Skinner, Trans. Faraday Soc., 1969, 65, 2044 |
| lit_7106 | 70MMb | P. J. Morris and R. B. Martin, J. Inorg. Nucl. Chem., 1970, 32, 2891 |
| lit_7116 | 70MRa | R. P. Martin and J. Riaute, J. Chim. Phys., 1970, 67, 1952 |
| lit_7282 | 70W | D. R. Williams, J. Chem. Soc. (A), 1970, 1550 |
| lit_7356 | 71BP | D. S. Barnes and L. D. Pettit, J. Inorg. Nucl. Chem., 1971, 33, 2177 |
| lit_8020 | 72GH | E. L. Giroux and R. I. Henkin, Biochim. Biophys. Acta, 1972, 273, 64 |
| lit_9386 | 74YA | A. Yokoyama, H. Aiba and H. Tanaka, Bull. Chem. Soc. Japan, 1974, 47, 112 |
| lit_9415 | 75APa | R. P. Agarwal and D. D. Perrin, J. Chem. Soc. Dalton, 1975, 1045 |
| lit_9911 | 76BPa | G. Brookes and L. D. Pettit, J. Chem. Soc. Dalton, 1976, 1224 |
| lit_10189 | 76PS | L. D. Pettit and J. L. M. Swash, J. Chem. Soc. Dalton, 1976, 588 |
| lit_10197 | 76R | J. H. Ritsma, J. Inorg. Nucl. Chem., 1976, 38, 907 |
| lit_1482 | 77DO | P. G. Daniele and G. Ostacoli, Ann. Chim. (Rome), 1977, 67, 37 |
| lit_10942 | 78SKG | I. Sovago, T. Kiss, and A. Gergely, J. Chem. Soc. Dalton, 1978, 964 |
| lit_11383 | 79SP | H. Stunzi and D. D. Perrin, J. Inorg. Biochem., 1979, 10, 309 |
| lit_11530 | 80DMY | N. K. Davidenko, P. A. Manorik, and K. B. Yatsimirskii, Russ. J. Inorg. Chem., … |
| lit_11757 | 81AB | T. Alemdaroglu and G. Berthon, Bioelectrochem. Bioenerg., 1981, 8, 49 |
| lit_11837 | 81CMW | A. Cole, P. M. May, and D. R. Williams, Agents Actions, 1981, 11, 296 |
| lit_11936 | 81JM | G. E. Jackson, P. M. May, and D. R. Williams, J. Inorg. Nucl. Chem., 1981, 43, … |
| lit_12302 | 82EA | M. S. El-Ezaby and F. M. Al-Sogair, Polyhedron, 1982, 1, 791 |
| lit_12342 | 82HA | Z. X. Huang, H. S. Al-Falahi, A. Cole, J. R. Duffield, C. Furnival, D. C. Jones… |
| lit_12473 | 82NV | M. S. Nair, K. Venkatachalapathi, and M. Santappa, J. Chem. Soc. Dalton, 1982, … |
| lit_13013 | 83TS | M. M. Taqui Khan and S. Satyanarayana, Indian J. Chem., 1983, 22A, 584 |
| lit_13070 | 84AC | G. Arena, R. Cali, V. Cucinotta, S. Musumeci, E. Rizzarelli, and S. Sammartano,… |
| lit_13357 | 84P | L. D. Pettit, Pure Appl. Chem., 1984, 56, 247 |
| lit_13571 | 85CFH | A. Cole, C. Furnival, Z. X. Huang, D. C. Jones, P. M. May, G. L. Smith, J. Whit… |
| lit_13654 | 85ISB | M. M. Islam, R. S. Singh, and B. G. Bhat, Proc. Indian Acad. Sci., Chem. Sci., … |
| lit_13815 | 85RRb | P. R. Reddy and M. H. Reddy, J. Chem. Soc. Dalton, 1985, 239 |
| lit_13844 | 85SG | S. Singh, D. Gupta, and K. L. Yadava, Electrochim. Acta, 1985, 30, 223 |
| lit_15358 | 89RSR | G. Reddy, S. Satyanarayana, and K. V. Reddy, Indian J. Chem., 1989, 28A, 337 |
| lit_15362 | 89RVM | A. K. Rao, P. Venkataiah, M. S. Mohan, and H. B. Bathina, J. Coord. Chem., 1989… |
| lit_15457 | 90BF | E. Bottari and M. R. Festa, J. Coord. Chem., 1990, 22, 237 |
| lit_16254 | 92LP | A. Lu, L. D. Pettit, and J. E. Gregor, Gaodeng Xuexiao Huaxue Xuebao (Chem. J. … |
| lit_16354 | 92VB | A. Varghese and P. K. Bhattacharya, J. Inorg. Biochem., 1992, 46, 223 |
| lit_16472 | 93GV | P. Gockel, H. Vahrenkamp, and A. D. Zuberbuhler, Helv. Chim. Acta, 1993, 76, 511 |
| lit_18256 | 94KM | M. Khodari, H. Mansour, M. A. Ghandour, and H. S. El Din, J. Electrochem. Soc. … |
| lit_16878 | 94VBc | A. V. Vaidyan and P. K. Bhattacharya, Canad. J. Chem., 1994, 72, 1107 |
| lit_16884 | 94WC | J. Wang, E. Collange, D. J. Aymes, M. R. Paris, and R. Fournaise, Bull. Soc. Ch… |
| lit_17768 | 98RR | P. R. Reddy, A. M. Reddy, and M. Radhika, Indian J. Chem., 1998, 37A, 775 |
| lit_17817 | 99AA | Z. M. Anwar and H. A. Azab, J. Chem. Eng. Data, 1999, 44, 1151 |

---

### Step 9: `inspect_literature`
**Args:**
```json
{
  "prefix_id": "vlm_98919"
}
```

[summary]
## inspect_literature — vlm_98919 — 53 citation(s)

| lit_id | shortcut | citation |
|--------|----------|----------|
| lit_855 | 49MM | L. E. Maley and D. P. Mellor, Aust. J. Sci. Res., 1949, A2, 579 |
| lit_1066 | 52A | A. Albert, Biochem. J., 1952, 50, 690 |
| lit_1902 | 53P | D. J. Perkins, Biochem. J., 1953, 55, 649 |
| lit_2179 | 55LM | N. C. Li and R. A. Manning, J. Amer. Chem. Soc., 1955, 77, 5225 |
| lit_2619 | 58Ea | J. Engelmann, Diss., U. Giesson, 1958 (see 60WS) |
| lit_2935 | 59LR | R. Leberman and B. R. Rabin, Trans. Faraday Soc., 1959, 55, 1660 |
| lit_3533 | 61Si | I. C. Smith, Diss., Kansas State Univ., 1961 |
| lit_3968 | 63CC | A. Chakravorty and F. A. Cotton, J. Phys. Chem., 1963, 67, 2878 |
| lit_4678 | 65AZ | A. C. Andrews and D. M. Zebolsky, J. Chem. Soc., 1965, 742 |
| lit_5337 | 66PA | O. N. Puplikova, L. N. Akimova, and I. A. Savich, Moscow Univ. Chem. Bull., 196… |
| lit_5774 | 67PSa | D. D. Perrin and V. S. Sharma, J. Chem. Soc. (A), 1967, 724 |
| lit_5831 | 67SS | W. F. Stack and H. A. Skinner, Trans. Faraday Soc., 1967, 63, 1136 |
| lit_6621 | 69MBb | R. P. Martin and M. Blanc, Bull. Soc. Chim. France, 1969, 1866 |
| lit_6752 | 69RM | E. V. Raju and H. B. Mathur, J. Inorg. Nucl. Chem., 1969, 31, 425 |
| lit_6838 | 69TS | A. C. R. Thornton and H. A. Skinner, Trans. Faraday Soc., 1969, 65, 2044 |
| lit_7106 | 70MMb | P. J. Morris and R. B. Martin, J. Inorg. Nucl. Chem., 1970, 32, 2891 |
| lit_7116 | 70MRa | R. P. Martin and J. Riaute, J. Chim. Phys., 1970, 67, 1952 |
| lit_7282 | 70W | D. R. Williams, J. Chem. Soc. (A), 1970, 1550 |
| lit_7356 | 71BP | D. S. Barnes and L. D. Pettit, J. Inorg. Nucl. Chem., 1971, 33, 2177 |
| lit_8020 | 72GH | E. L. Giroux and R. I. Henkin, Biochim. Biophys. Acta, 1972, 273, 64 |
| lit_9386 | 74YA | A. Yokoyama, H. Aiba and H. Tanaka, Bull. Chem. Soc. Japan, 1974, 47, 112 |
| lit_9415 | 75APa | R. P. Agarwal and D. D. Perrin, J. Chem. Soc. Dalton, 1975, 1045 |
| lit_9911 | 76BPa | G. Brookes and L. D. Pettit, J. Chem. Soc. Dalton, 1976, 1224 |
| lit_10189 | 76PS | L. D. Pettit and J. L. M. Swash, J. Chem. Soc. Dalton, 1976, 588 |
| lit_10197 | 76R | J. H. Ritsma, J. Inorg. Nucl. Chem., 1976, 38, 907 |
| lit_1482 | 77DO | P. G. Daniele and G. Ostacoli, Ann. Chim. (Rome), 1977, 67, 37 |
| lit_10942 | 78SKG | I. Sovago, T. Kiss, and A. Gergely, J. Chem. Soc. Dalton, 1978, 964 |
| lit_11383 | 79SP | H. Stunzi and D. D. Perrin, J. Inorg. Biochem., 1979, 10, 309 |
| lit_11530 | 80DMY | N. K. Davidenko, P. A. Manorik, and K. B. Yatsimirskii, Russ. J. Inorg. Chem., … |
| lit_11757 | 81AB | T. Alemdaroglu and G. Berthon, Bioelectrochem. Bioenerg., 1981, 8, 49 |
| lit_11837 | 81CMW | A. Cole, P. M. May, and D. R. Williams, Agents Actions, 1981, 11, 296 |
| lit_11936 | 81JM | G. E. Jackson, P. M. May, and D. R. Williams, J. Inorg. Nucl. Chem., 1981, 43, … |
| lit_12302 | 82EA | M. S. El-Ezaby and F. M. Al-Sogair, Polyhedron, 1982, 1, 791 |
| lit_12342 | 82HA | Z. X. Huang, H. S. Al-Falahi, A. Cole, J. R. Duffield, C. Furnival, D. C. Jones… |
| lit_12473 | 82NV | M. S. Nair, K. Venkatachalapathi, and M. Santappa, J. Chem. Soc. Dalton, 1982, … |
| lit_13013 | 83TS | M. M. Taqui Khan and S. Satyanarayana, Indian J. Chem., 1983, 22A, 584 |
| lit_13070 | 84AC | G. Arena, R. Cali, V. Cucinotta, S. Musumeci, E. Rizzarelli, and S. Sammartano,… |
| lit_13357 | 84P | L. D. Pettit, Pure Appl. Chem., 1984, 56, 247 |
| lit_13571 | 85CFH | A. Cole, C. Furnival, Z. X. Huang, D. C. Jones, P. M. May, G. L. Smith, J. Whit… |
| lit_13654 | 85ISB | M. M. Islam, R. S. Singh, and B. G. Bhat, Proc. Indian Acad. Sci., Chem. Sci., … |
| lit_13815 | 85RRb | P. R. Reddy and M. H. Reddy, J. Chem. Soc. Dalton, 1985, 239 |
| lit_13844 | 85SG | S. Singh, D. Gupta, and K. L. Yadava, Electrochim. Acta, 1985, 30, 223 |
| lit_15358 | 89RSR | G. Reddy, S. Satyanarayana, and K. V. Reddy, Indian J. Chem., 1989, 28A, 337 |
| lit_15362 | 89RVM | A. K. Rao, P. Venkataiah, M. S. Mohan, and H. B. Bathina, J. Coord. Chem., 1989… |
| lit_15457 | 90BF | E. Bottari and M. R. Festa, J. Coord. Chem., 1990, 22, 237 |
| lit_16254 | 92LP | A. Lu, L. D. Pettit, and J. E. Gregor, Gaodeng Xuexiao Huaxue Xuebao (Chem. J. … |
| lit_16354 | 92VB | A. Varghese and P. K. Bhattacharya, J. Inorg. Biochem., 1992, 46, 223 |
| lit_16472 | 93GV | P. Gockel, H. Vahrenkamp, and A. D. Zuberbuhler, Helv. Chim. Acta, 1993, 76, 511 |
| lit_18256 | 94KM | M. Khodari, H. Mansour, M. A. Ghandour, and H. S. El Din, J. Electrochem. Soc. … |
| lit_16878 | 94VBc | A. V. Vaidyan and P. K. Bhattacharya, Canad. J. Chem., 1994, 72, 1107 |
| lit_16884 | 94WC | J. Wang, E. Collange, D. J. Aymes, M. R. Paris, and R. Fournaise, Bull. Soc. Ch… |
| lit_17768 | 98RR | P. R. Reddy, A. M. Reddy, and M. Radhika, Indian J. Chem., 1998, 37A, 775 |
| lit_17817 | 99AA | Z. M. Anwar and H. A. Azab, J. Chem. Eng. Data, 1999, 44, 1151 |

---

### Step 10: `inspect_literature`
**Args:**
```json
{
  "prefix_id": "vlm_98927"
}
```

[summary]
## inspect_literature — vlm_98927 — 53 citation(s)

| lit_id | shortcut | citation |
|--------|----------|----------|
| lit_855 | 49MM | L. E. Maley and D. P. Mellor, Aust. J. Sci. Res., 1949, A2, 579 |
| lit_1066 | 52A | A. Albert, Biochem. J., 1952, 50, 690 |
| lit_1902 | 53P | D. J. Perkins, Biochem. J., 1953, 55, 649 |
| lit_2179 | 55LM | N. C. Li and R. A. Manning, J. Amer. Chem. Soc., 1955, 77, 5225 |
| lit_2619 | 58Ea | J. Engelmann, Diss., U. Giesson, 1958 (see 60WS) |
| lit_2935 | 59LR | R. Leberman and B. R. Rabin, Trans. Faraday Soc., 1959, 55, 1660 |
| lit_3533 | 61Si | I. C. Smith, Diss., Kansas State Univ., 1961 |
| lit_3968 | 63CC | A. Chakravorty and F. A. Cotton, J. Phys. Chem., 1963, 67, 2878 |
| lit_4678 | 65AZ | A. C. Andrews and D. M. Zebolsky, J. Chem. Soc., 1965, 742 |
| lit_5337 | 66PA | O. N. Puplikova, L. N. Akimova, and I. A. Savich, Moscow Univ. Chem. Bull., 196… |
| lit_5774 | 67PSa | D. D. Perrin and V. S. Sharma, J. Chem. Soc. (A), 1967, 724 |
| lit_5831 | 67SS | W. F. Stack and H. A. Skinner, Trans. Faraday Soc., 1967, 63, 1136 |
| lit_6621 | 69MBb | R. P. Martin and M. Blanc, Bull. Soc. Chim. France, 1969, 1866 |
| lit_6752 | 69RM | E. V. Raju and H. B. Mathur, J. Inorg. Nucl. Chem., 1969, 31, 425 |
| lit_6838 | 69TS | A. C. R. Thornton and H. A. Skinner, Trans. Faraday Soc., 1969, 65, 2044 |
| lit_7106 | 70MMb | P. J. Morris and R. B. Martin, J. Inorg. Nucl. Chem., 1970, 32, 2891 |
| lit_7116 | 70MRa | R. P. Martin and J. Riaute, J. Chim. Phys., 1970, 67, 1952 |
| lit_7282 | 70W | D. R. Williams, J. Chem. Soc. (A), 1970, 1550 |
| lit_7356 | 71BP | D. S. Barnes and L. D. Pettit, J. Inorg. Nucl. Chem., 1971, 33, 2177 |
| lit_8020 | 72GH | E. L. Giroux and R. I. Henkin, Biochim. Biophys. Acta, 1972, 273, 64 |
| lit_9386 | 74YA | A. Yokoyama, H. Aiba and H. Tanaka, Bull. Chem. Soc. Japan, 1974, 47, 112 |
| lit_9415 | 75APa | R. P. Agarwal and D. D. Perrin, J. Chem. Soc. Dalton, 1975, 1045 |
| lit_9911 | 76BPa | G. Brookes and L. D. Pettit, J. Chem. Soc. Dalton, 1976, 1224 |
| lit_10189 | 76PS | L. D. Pettit and J. L. M. Swash, J. Chem. Soc. Dalton, 1976, 588 |
| lit_10197 | 76R | J. H. Ritsma, J. Inorg. Nucl. Chem., 1976, 38, 907 |
| lit_1482 | 77DO | P. G. Daniele and G. Ostacoli, Ann. Chim. (Rome), 1977, 67, 37 |
| lit_10942 | 78SKG | I. Sovago, T. Kiss, and A. Gergely, J. Chem. Soc. Dalton, 1978, 964 |
| lit_11383 | 79SP | H. Stunzi and D. D. Perrin, J. Inorg. Biochem., 1979, 10, 309 |
| lit_11530 | 80DMY | N. K. Davidenko, P. A. Manorik, and K. B. Yatsimirskii, Russ. J. Inorg. Chem., … |
| lit_11757 | 81AB | T. Alemdaroglu and G. Berthon, Bioelectrochem. Bioenerg., 1981, 8, 49 |
| lit_11837 | 81CMW | A. Cole, P. M. May, and D. R. Williams, Agents Actions, 1981, 11, 296 |
| lit_11936 | 81JM | G. E. Jackson, P. M. May, and D. R. Williams, J. Inorg. Nucl. Chem., 1981, 43, … |
| lit_12302 | 82EA | M. S. El-Ezaby and F. M. Al-Sogair, Polyhedron, 1982, 1, 791 |
| lit_12342 | 82HA | Z. X. Huang, H. S. Al-Falahi, A. Cole, J. R. Duffield, C. Furnival, D. C. Jones… |
| lit_12473 | 82NV | M. S. Nair, K. Venkatachalapathi, and M. Santappa, J. Chem. Soc. Dalton, 1982, … |
| lit_13013 | 83TS | M. M. Taqui Khan and S. Satyanarayana, Indian J. Chem., 1983, 22A, 584 |
| lit_13070 | 84AC | G. Arena, R. Cali, V. Cucinotta, S. Musumeci, E. Rizzarelli, and S. Sammartano,… |
| lit_13357 | 84P | L. D. Pettit, Pure Appl. Chem., 1984, 56, 247 |
| lit_13571 | 85CFH | A. Cole, C. Furnival, Z. X. Huang, D. C. Jones, P. M. May, G. L. Smith, J. Whit… |
| lit_13654 | 85ISB | M. M. Islam, R. S. Singh, and B. G. Bhat, Proc. Indian Acad. Sci., Chem. Sci., … |
| lit_13815 | 85RRb | P. R. Reddy and M. H. Reddy, J. Chem. Soc. Dalton, 1985, 239 |
| lit_13844 | 85SG | S. Singh, D. Gupta, and K. L. Yadava, Electrochim. Acta, 1985, 30, 223 |
| lit_15358 | 89RSR | G. Reddy, S. Satyanarayana, and K. V. Reddy, Indian J. Chem., 1989, 28A, 337 |
| lit_15362 | 89RVM | A. K. Rao, P. Venkataiah, M. S. Mohan, and H. B. Bathina, J. Coord. Chem., 1989… |
| lit_15457 | 90BF | E. Bottari and M. R. Festa, J. Coord. Chem., 1990, 22, 237 |
| lit_16254 | 92LP | A. Lu, L. D. Pettit, and J. E. Gregor, Gaodeng Xuexiao Huaxue Xuebao (Chem. J. … |
| lit_16354 | 92VB | A. Varghese and P. K. Bhattacharya, J. Inorg. Biochem., 1992, 46, 223 |
| lit_16472 | 93GV | P. Gockel, H. Vahrenkamp, and A. D. Zuberbuhler, Helv. Chim. Acta, 1993, 76, 511 |
| lit_18256 | 94KM | M. Khodari, H. Mansour, M. A. Ghandour, and H. S. El Din, J. Electrochem. Soc. … |
| lit_16878 | 94VBc | A. V. Vaidyan and P. K. Bhattacharya, Canad. J. Chem., 1994, 72, 1107 |
| lit_16884 | 94WC | J. Wang, E. Collange, D. J. Aymes, M. R. Paris, and R. Fournaise, Bull. Soc. Ch… |
| lit_17768 | 98RR | P. R. Reddy, A. M. Reddy, and M. Radhika, Indian J. Chem., 1998, 37A, 775 |
| lit_17817 | 99AA | Z. M. Anwar and H. A. Azab, J. Chem. Eng. Data, 1999, 44, 1151 |

---
