# Q5.2.4 — Tool Results (batch 2)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Plutonium(IV)",
  "limit": 10
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
  "name": "Aspirin, Acetylsalicylic acid",
  "limit": 10
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 5: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_149"
}
```

[summary]
[CATALOG]
## build_system_catalog — 11 pair(s), 19 species *(compact)*

### Pu^[4+] + Nitrate ion
**metal_id:** metal_149 | **ligand_id:** ligand_10109 | **ligand_def_HxL:** ***  
**entries:** 9 | **species:** 3 | **vlm_count:** 9

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 6 |
| beta_def_840 | [M] + [L]^2 <=> [ML2] | 2 |
| beta_def_872 | [M] + [L]^3 <=> [ML3] | 1 |

**vlm_ids:** 9 (vlm_173938…vlm_173946)

**eq_maps:** 4 ref nets (ref_eq_net_28485, ref_eq_net_28486, ref_eq_net_28487…ref_eq_net_28488) | T: 15~30 °C | I: -0.05~4.15 M | max 3 nodes, 3 edges

---

### Pu^[4+] + Hydroxide ion
**metal_id:** metal_149 | **ligand_id:** ligand_10076 | **ligand_def_HxL:** ***  
**entries:** 5 | **species:** 1 | **vlm_count:** 5

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 5 |

**vlm_ids:** 5 (vlm_170588…vlm_170592)

**eq_maps:** 3 ref nets (ref_eq_net_27406, ref_eq_net_27407, ref_eq_net_27408) | T: 16.5~31.5 °C | I: 0.275~2.225 M | max 1 nodes, 0 edges

---

### Pu^[4+] + Hydrogen fluoride (Hydrofluoric acid)
**metal_id:** metal_149 | **ligand_id:** ligand_10162 | **ligand_def_HxL:** HL  
**entries:** 4 | **species:** 1 | **vlm_count:** 4

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 4 |

**vlm_ids:** 4 (vlm_176898…vlm_176901)

**eq_maps:** 2 ref nets (ref_eq_net_29637, ref_eq_net_29638) | T: 16.5~31.5 °C | I: 1.775~2.225 M | max 1 nodes, 0 edges

---

### Pu^[4+] + Hydrogen sulfate ion (Sulfuric acid)
**metal_id:** metal_149 | **ligand_id:** ligand_10148 | **ligand_def_HxL:** HL  
**entries:** 4 | **species:** 2 | **vlm_count:** 4

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 3 |
| beta_def_840 | [M] + [L]^2 <=> [ML2] | 1 |

**vlm_ids:** 4 (vlm_175959…vlm_175962)

**eq_maps:** 1 ref nets (ref_eq_net_29258) | T: 16.5~31.5 °C | I: 1.775~2.225 M | max 2 nodes, 1 edges

---

### Pu^[4+] + Pentane-2,4-dione (Acetylacetone)
**metal_id:** metal_149 | **ligand_id:** ligand_9526 | **ligand_def_HxL:** ***  
**entries:** 4 | **species:** 4 | **vlm_count:** 4

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 1 |
| beta_def_840 | [M] + [L]^2 <=> [ML2] | 1 |
| beta_def_872 | [M] + [L]^3 <=> [ML3] | 1 |
| beta_def_894 | [M] + [L]^4 <=> [ML4] | 1 |

**vlm_ids:** 4 (vlm_165352…vlm_165355)

**eq_maps:** 1 ref nets (ref_eq_net_25226) | T: 20~30 °C | I: -0.05~0.25 M | max 4 nodes, 6 edges

---

### Pu^[4+] + Chloride ion
**metal_id:** metal_149 | **ligand_id:** ligand_10163 | **ligand_def_HxL:** ***  
**entries:** 3 | **species:** 1 | **vlm_count:** 3

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 3 |

**vlm_ids:** vlm_177329, vlm_177330, vlm_177331

**eq_maps:** 3 ref nets (ref_eq_net_29818, ref_eq_net_29819, ref_eq_net_29820) | T: 12.5~31.5 °C | I: 0.775~4.225 M | max 1 nodes, 0 edges

---

### Pu^[4+] + Hydrogen peroxide
**metal_id:** metal_149 | **ligand_id:** ligand_10143 | **ligand_def_HxL:** H2L  
**entries:** 2 | **species:** 2 | **vlm_count:** 2

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_527 | [M]^2 + [H2L]^2 <=> [M2L2] + [H]^4 | 1 |
| beta_def_572 | [M]^2 + [H2L] + [H2O] <=> [M2(OH)L] + [H]^3 | 1 |

**vlm_ids:** vlm_175363, vlm_175364

**eq_maps:** 1 ref nets (ref_eq_net_29035) | T: 16.5~31.5 °C | I: 0.275~0.725 M | max 2 nodes, 1 edges

---

### Pu^[4+] + Ethanedioic acid (Oxalic acid)
**metal_id:** metal_149 | **ligand_id:** ligand_8872 | **ligand_def_HxL:** H2L  
**entries:** 2 | **species:** 2 | **vlm_count:** 2

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 1 |
| beta_def_840 | [M] + [L]^2 <=> [ML2] | 1 |

**vlm_ids:** vlm_151713, vlm_151714

**eq_maps:** 1 ref nets (ref_eq_net_20006) | T: 16.5~31.5 °C | I: 3.775~4.225 M | max 2 nodes, 1 edges

---

### Pu^[4+] + Bromide ion
**metal_id:** metal_149 | **ligand_id:** ligand_10168 | **ligand_def_HxL:** ***  
**entries:** 1 | **species:** 1 | **vlm_count:** 1

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 1 |

**vlm_ids:** vlm_177973

**eq_maps:** 1 ref nets (ref_eq_net_30048) | T: 16.5~31.5 °C | I: 1.775~2.225 M | max 1 nodes, 0 edges

---

### Pu^[4+] + Hydrogen amidosulfate (Sulfamic acid)
**metal_id:** metal_149 | **ligand_id:** ligand_10151 | **ligand_def_HxL:** HL  
**entries:** 1 | **species:** 1 | **vlm_count:** 1

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 1 |

**vlm_ids:** vlm_176333

**eq_maps:** 1 ref nets (ref_eq_net_29413) | T: 16.5~31.5 °C | I: 1.775~2.225 M | max 1 nodes, 0 edges

---

### Pu^[4+] + Diethylenetrinitrilopentaacetic acid (DTPA)
**metal_id:** metal_149 | **ligand_id:** ligand_6356 | **ligand_def_HxL:** H5L  
**entries:** 1 | **species:** 1 | **vlm_count:** 1

*(all species aqueous)*
| beta_def_id | equation_str | n |
|-------------|--------------|---|
| beta_def_812 | [M] + [L] <=> [ML] | 1 |

**vlm_ids:** vlm_112670

**eq_maps:** 1 ref nets (ref_eq_net_6721) | T: 12.5~27.5 °C | I: 0.275~0.725 M | max 1 nodes, 0 edges

---

### Step 7: `search_ligands`
**Args:**
```json
{
  "name": "acetylsalicylate, acetylsalicylic acid, 2-acetoxybenzoate, o-acetoxybenzoate, ASA, salicylate, salicylic acid, 2-hydroxybenzoate",
  "limit": 20
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 8: `search_citations`
**Args:**
```json
{
  "where": "(la.citation LIKE '%acetylsalicyl%' OR la.citation LIKE '%aspirin%' OR la.citation LIKE '%salicyl%')",
  "order_by": "la.shortcut ASC",
  "limit": 20
}
```

[summary]
## search_citations — 1 row(s)

| example_vlm_id | vlm_count | lit_id | shortcut | citation |
|----------------|-----------|--------|----------|----------|
| vlm_160211 | 79 | lit_1949 | 54Aa | A. Agren, Acta Chem. Scand., 1954, 8, 1059 (for salicylic acid + H+ = 3.86, rea… |

---

### Step 9: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_149 AND (c.ligand_name_SRD LIKE '%salicyl%' OR c.ligand_name_SRD LIKE '%hydroxybenzo%'))",
  "order_by": "s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability — 20 row(s)

### ΔS — 16 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_41 | Cu^[2+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 3 | 2 | 25 | 0~0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 2 | 1 | 25 | 0~0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 2 | 1 | 25 | 0~0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_9154 | Phosphoric acid 1-naphthyl … | H2L | O=P(O)(O)Oc1cccc2ccccc12 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_9152 | Phosphoric acid phenyl este… | H2L | O=P(O)(O)Oc1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_68 | H^[+] | ligand_9152 | Phosphoric acid phenyl este… | H2L | O=P(O)(O)Oc1ccccc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_9154 | Phosphoric acid 1-naphthyl … | H2L | O=P(O)(O)Oc1cccc2ccccc12 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_94 | Mn^[2+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_33 | Co^[2+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_192 | Tm^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_81 | Lu^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_73 | Ho^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_44 | Dy^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_55 | Er^[3+] | ligand_8758 | 2-Methoxybenzoic acid | HL | COc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |

---

### Step 10: `inspect_literature`
**Args:**
```json
{
  "prefix_id": "vlm_160211"
}
```

[summary]
## inspect_literature — vlm_160211 — 109 citation(s)

| lit_id | shortcut | citation |
|--------|----------|----------|
| lit_233 | 29La | E. Larsson, Z. Anorg. Allg. Chem., 1929, 183, 30 |
| lit_289 | 31LAb | E. Larsson and B. Adell, Z. Phys. Chem., 1931, A157, 342 |
| lit_366 | 34FR | E. Ferrell, J. M. Ridgion, and H. L. Riley, J. Chem. Soc., 1934, 1440 |
| lit_476 | 38AJ | C. T. Abichandani and S. K. K. Jatkar, J. Indian Inst. Sci., 1938, 21A, 417; Ch… |
| lit_513 | 39EWa | D. H. Everett and W. F. K. Wynne-Jones, Trans. Faraday Soc., 1939, 35, 1380 |
| lit_977 | 51BW | R. P. Bell and G. M. Waind, J. Chem. Soc., 1951, 2357 |
| lit_1861 | 53Hb | B. Hok, Svensk Kem. Tidskr., 1953, 65, 182 |
| lit_1949 | 54Aa | A. Agren, Acta Chem. Scand., 1954, 8, 1059 (for salicylic acid + H+ = 3.86, rea… |
| lit_2092 | 55Aa | A. Agren, Acta Chem. Scand., 1955, 9, 49 |
| lit_1155 | 55WS | A. V. Willi and J. F. Stocker, Helv. Chim. Acta, 1955, 38, 1279 |
| lit_1161 | 56Aa | A. Agren, Svensk Kem. Tidskr., 1956, 68, 185 |
| lit_2362 | 57BDH | L. G. Bray, J. F. J. Dippy, S. R. C. Hughes, and L. W. Laxton, J. Chem. Soc., 1… |
| lit_2511 | 57PC | B. Peltier and M. Conti, Compt. Rend. Acad. Sci. Paris, 1957, 244, 2811 |
| lit_2727 | 58P | D. D. Perrin, Nature (London), 1958, 182, 741 |
| lit_3119 | 60Cd | J. C. Colleter, Ann. Chim. (Paris), 1960, 5, 415 |
| lit_3510 | 61PSa | R. L. Pecsok and W. P. Schaefer, J. Amer. Chem. Soc., 1961, 83, 62 |
| lit_3573 | 61U | E. Uhlig, Z. Anorg. Allg. Chem., 1961, 311, 249 |
| lit_3626 | 62BKT | H. J. deBruin, D. Kaitis, and R. B. Temple, Aust. J. Chem., 1962, 15, 457 |
| lit_3653 | 62CTC | M. Cefola, A. S. Tompa, A. V. Celiano, and P. S. Gentile, Inorg. Chem., 1962, 1… |
| lit_4002 | 63EM | Z. L. Ernst and J. Menashi, Trans. Faraday Soc., 1963, 59, 230 |
| lit_4073 | 63Ib | Y. J. Israeli, Canad. J. Chem., 1963, 41, 2710 |
| lit_4389 | 64EI | Z. L. Ernst, R. J. Irving, and J. Menashi, Trans. Faraday Soc., 1964, 60, 56 |
| lit_4789 | 65Gc | P. K. Glasoe, J. Phys. Chem., 1965, 69, 4416 |
| lit_5134 | 66DKa | G. E. Dunn and F. Kung, Canad. J. Chem., 1966, 44, 1261 |
| lit_5261 | 66LM | G. A. L'Heureux and A. E. Martell, J. Inorg. Nucl. Chem., 1966, 28, 481 |
| lit_5292 | 66MM | G. E. Mont and A. E. Martell, J. Amer. Chem. Soc., 1966, 88, 1387 |
| lit_5334 | 66P | M. V. Park, J. Chem. Soc. (A), 1966, 816; Nature (London), 1963, 197, 283 |
| lit_5429 | 66VM | V. P. Vasilev, P. S. Mukhina, and A. F. Belyakova, Izv. Vyssh. Ucheb. Zaved., K… |
| lit_5470 | 67B | M. Bartusek, Coll. Czech. Chem. Comm., 1967, 32, 116 |
| lit_5777 | 67PSS | D. D. Perrin, I. G. Sayce, and V. S. Sharma, J. Chem. Soc. (A), 1967, 1755 |
| lit_5881 | 67VKa | S. Varvicka and J. Koryta, Coll. Czech. Chem. Comm., 1967, 32, 2346 |
| lit_6100 | 68Ha | R. J. N. Harries, Talanta, 1968, 15, 1345 |
| lit_1324 | 69CMa | G. F. Condike and A. E. Martell, J. Inorg. Nucl. Chem., 1969, 31, 2455 |
| lit_6528 | 69HH | J. Havel, L. Havelkova, and M. Bartusek, Chem. Zvesti, 1969, 23, 582 |
| lit_6885 | 70AH | G. Ackermann, D. Hesse, and P. Volland, Z. Anorg. Allg. Chem., 1970, 377, 92 |
| lit_1449 | 70KC | G. C. Kugler and G. H. Carey, Talanta, 1970, 10, 907 |
| lit_7117 | 70MRP | W. A. E. McBryde, J. L. Rohr, J. S. Penciner, and J. A. Page, Canad. J. Chem., … |
| lit_7231 | 70SMb | G. Saini and E. Mentasti, Inorg. Chim. Acta, 1970, 4, 585 |
| lit_7391 | 71CSb | M. C. Chattopadhyaya and R. S. Singh, Indian J. Chem., 1971, 9, 490 |
| lit_7846 | 71ZB | J. Zelinka and M. Bartusek, Coll. Czech. Chem. Comm., 1971, 36, 2615 |
| lit_8145 | 72LLb | Y. H. Lee and G. Lundgren, Trans. Roy. Inst. Tech. Stockholm, 1972, No. 267 |
| lit_8162 | 72Ma | I. Mentre, Ann. Chim. (Paris), 1972, 7, 333 |
| lit_8322 | 72Sg | H. Stober, KFK-1657, July 1972 |
| lit_8432 | 73Ac | R. Aruga, Atti Accad. Sci. Torino, 1973, 107, 207 |
| lit_8622 | 73JK | D. V. Jahagirdar and D. D. Khanolkar, J. Inorg. Nucl. Chem., 1973, 35, 921 |
| lit_8679 | 73L | Y. H. Lee, Acta Chem. Scand., 1973, 27, 1807 |
| lit_8806 | 73RMa | S. Ramamoorthy and P. G. Manning, J. Inorg. Nucl. Chem., 1973, 35, 1571 |
| lit_9106 | 74Jc | A. P. Joshi, J. Indian Chem. Soc., 1974, 51, 643 |
| lit_9458 | 75BSb | P. F. Brun and K. H. Schroder, J. Electroanal. Chem., 1975, 66, 9 |
| lit_9491 | 75DI | A. W. L. Dudeney and R. J. Irving, J. Chem. Soc. Faraday I, 1975, 71, 1215 |
| lit_9665 | 75LSb | B. M. Lowe and D. G. Smith, J. Chem. Soc. Faraday I, 1975, 71, 1379 |
| lit_9803 | 75ST | S. P. Singh and J. P. Tandon, Monat. Chem., 1975, 106, 271 |
| lit_9807 | 75SV | F. Secco and M. Venturini, Inorg. Chem., 1975, 14, 1978 |
| lit_9858 | 76ABb | S. A. Abbasi, B. G. Bhat, and R. S. Singh, Inorg. Nucl. Chem. Lett., 1976, 12, … |
| lit_9859 | 76ABc | S. A. Abbasi, B. G. Bhat, and R. S. Singh, Indian J. Chem., 1976, 14A, 718 |
| lit_10336 | 77AR | S. Aditya, A. K. Roy, and S. C. Lahiri, Z. Phys. Chem. (Leipzig), 1977, 258, 10… |
| lit_1501 | 77FB | A. I. Falicheva, R. I. Burdykina, and V. I. Shatalova, Izv. Vyssh. Ucheb. Zaved… |
| lit_1556 | 77JKS | U. Jain, V. Kumari, R. C. Sharma, and G. K. Chaturvedi, J. Chim. Phys., 1977, 7… |
| lit_10632 | 78AKW | G. Arena, G. Kavu, and D. R. Williams, J. Inorg. Nucl. Chem., 1978, 40, 1221 |
| lit_10656 | 78BJ | E. Bottari and R. Jasionowska, Ann. Chim. (Rome), 1978, 68, 791 |
| lit_10765 | 78JSC | A. K. Jain, R. C. Sharma, and G. K. Chaturvedi, Polish J. Chem., 1978, 52, 259 |
| lit_10831 | 78LTa | L. Lajunen and M. Tikanmaki, Acta Univ. Oul., 1978, A74, Chem. 8 |
| lit_10895 | 78Pb | E. M. Perdue, Geochim. Cosmochim. Acta, 1978, 42, 1351 |
| lit_11437 | 79ZKV | A. P. Zharkov, F. Ya. Kulva, and V. N. Volkov, Soviet J. Coord. Chem., 1979, 5,… |
| lit_11494 | 80BL | A. Bhattacharyya and S. C. Lahiri, J. Indian Chem. Soc., 1980, 57, 971 |
| lit_11499 | 80BP | L. Babcock and R. Pizer, Inorg. Chem., 1980, 19, 56 |
| lit_11517 | 80CS | M. C. Chattopadhyaya and R. S. Singh, Indian J. Chem., 1980, 19A, 141 |
| lit_11640 | 80RCB | F. Rodante, G. Ceccaroni, and M. G. Bonicelli, Thermochim. Acta, 1980, 42, 223 |
| lit_11825 | 81CCM | V. Cerda, E. Casassas, and F. G. Montelongo, Thermochim. Acta, 1981, 47, 343 |
| lit_11979 | 81LLb | O. Lukkari and H. Lukkari, Finn. Chem. Lett., 1981, 62 |
| lit_12078 | 81RMR | K. S. Rajan, S. Mainer, N. L. Rajan, and J. M. Davis, J. Inorg. Biochem., 1981,… |
| lit_12132 | 81SYa | R. K. P. Singh, J. R. Yadava, and K. L. Yadava, Nat. Acad. Sci. Lett. (India), … |
| lit_12251 | 82C | M. C. Chattopadhyaya, J. Indian Chem. Soc., 1982, 59, 1416 |
| lit_12278 | 82CSV | R. Corigli, F. Secco, and M. Venturini, Inorg. Chem., 1982, 21, 2992 |
| lit_12292 | 82DJ | C. R. Dhat and D. V. Jahagirdar, Indian J. Chem., 1982, 21A, 792 |
| lit_12334 | 82GSS | V. P. Gupta, J. K. Sthapak, and D. D. Sharma, Indian J. Chem., 1982, 21A, 546 |
| lit_12830 | 83LE | L. H. J. Lajunen, E. Eijarvi, and H. Hayrynen, Acta Univ. Oul., 1983, A152, Che… |
| lit_12835 | 83LLK | L. H. J. Lajunen, H. Lippo, and P. Kokkonen, Finn. Chem. Lett., 1983, 107 |
| lit_12908 | 83OS | L. O. Ohman and S. Sjoberg, Acta Chem. Scand., 1983, A37, 875 |
| lit_13137 | 84CT | E. Casassas and R. Tauler, J. Chim. Phys., 1984, 81, 233 |
| lit_13365 | 84PD | M. Puttemans, L. Dryon, and D. L. Massart, Anal. Chim. Acta, 1984, 161, 221 |
| lit_13487 | 84VSL | G. Venkatnarayana, S. J. Swamy, and P. Lingaiah, Indian J. Chem., 1984, 23A, 501 |
| lit_13588 | 85DDD | P. G. Daniele, A. De Robertis, C. De Stefano, S. Sammartano, and C. Rigano, J. … |
| lit_13697 | 85KSR | C. R. Krishnamoorthy, S. Sunil, and K. Ramalingam, Polyhedron, 1985, 4, 1451 |
| lit_13952 | 86BA | R. J. Barrio Diez-Caballero, J. F. Arranz Valentin, A. Arranz Garcia, and P. Sa… |
| lit_14262 | 86SPT | B. D. Struck, M. Peric, and D. Triefenbach, J. Electroanal. Chem., 1986, 214, 4… |
| lit_14430 | 87GM | M. L. Simoes Goncalves and A. M. Mota, Talanta, 1987, 34, 839 |
| lit_14533 | 87MMI | M. Maeda, Y. Murata, and K. Ito, J. Chem. Soc. Dalton, 1987, 1853 |
| lit_14772 | 88DO | M. Dahlund and A. Olin, Acta Chem. Scand., 1988, A42, 273 |
| lit_15149 | 89Dc | A. K. Das, J. Electrochem. Soc. India, 1989, 38, 149 |
| lit_15203 | 89HM | Y. Hasagawa, Y. Morita, M. Hase, and M. Nagata, Bull. Chem. Soc. Japan, 1989, 6… |
| lit_15391 | 89SRb | Shivaraj and M. G. R. Reddy, Indian J. Chem., 1989, 28A, 1016 |
| lit_15429 | 89YA | Y. Z. Yousif and F. J. M. Al-Imarah, Trans. Met. Chem. (London), 1989, 14, 123 |
| lit_15510 | 90DDR | A. De Robertis, C. De Stefano, C. Rigano, and S. Sammartano, J. Soln. Chem., 19… |
| lit_15571 | 90HY | Y. Hasegawa, N. Yamazaki, S. Usui, and G. R. Choppin, Bull. Chem. Soc. Japan, 1… |
| lit_15580 | 90JK | G. E. Jackson and M. J. Kelly, J. Chem. Soc. Dalton, 1990, 1889 |
| lit_16011 | 91PA | N. Papadopoulos and A. Avranas, J. Soln. Chem., 1991, 20, 293 |
| lit_16168 | 92DMa | S. C. Dutta, A. K. Mondal, S. C. Lahiri, and B. P. Dey, J. Indian Chem. Soc., 1… |
| lit_16498 | 93KAJ | T. Kiss, K. Atkari, M. Jezowska-Bojczuk, and P. Decock, J. Coord. Chem., 1993, … |
| lit_16553 | 93NK | M. S. K. Niazi and A. Khan, J. Chem. Eng. Data, 1993, 38, 98 |
| lit_16557 | 93NS | J. Noro and T. Sekine, Bull. Chem. Soc. Japan, 1993, 66, 1647 |
| lit_16843 | 94RRS | C. V. R. Reddy, M. G. R. Reddy, and Shivaraj, Indian J. Chem., 1994, 33A, 792 |
| lit_16861 | 94SR | Shivaraj, C. V. R. Reddy, and M. G. R. Reddy, Acta Ciencia Indica, 1994, 80, 105 |
| lit_16915 | 95BBc | V. Brumas, B. Brumas, and G. Berthon, J. Inorg. Biochem., 1995, 57, 191 |
| lit_17260 | 96KDa | V. Kolhe and K. Dwivedi, J. Indian Chem. Soc., 1996, 73, 265 |
| lit_17299 | 96MM | A. L. R. Merce, A. S. Mangrich, B. Szpoganicz, N. M. Levy, and J. Felcman, J. B… |
| lit_17362 | 96SN | M. Singh and R. Nayan, Asian J. Chem., 1996, 8, 470 |
| lit_17525 | 97LP | L. H. J. Lajunen, R. Portanova, J. Piispanen, and M. Talazzi, Pure Appl. Chem.,… |
| lit_17715 | 98KR | M. M. Khalil and A. M. Radalla, Talanta, 1998, 46, 53 |

---
