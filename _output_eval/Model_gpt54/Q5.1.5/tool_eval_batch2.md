# Q5.1.5 — Tool Results (batch 2)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Calcium, Magnesium, Zinc, Copper(II), Iron(II), Iron(III), Lead, Cadmium, Nickel, Cobalt(II), Manganese(II), Aluminum",
  "limit": 20
}
```

[summary]
## search_metals

*(no results)*

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "EDTA, ethylenediaminetetraacetic acid",
  "limit": 10
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 4: `search_metals`
**Args:**
```json
{
  "symbol": "Ca, Mg, Zn, Cu, Fe, Pb, Cd, Ni, Co, Mn, Al",
  "limit": 20
}
```

[summary]
## search_metals

*(no results)*

---

### Step 5: `search_ligands`
**Args:**
```json
{
  "name": "ethylenediaminetetraacetate",
  "limit": 10
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 7: `build_system_catalog`
**Args:**
```json
{}
```

[summary]
[CATALOG]
## build_system_catalog

**Error:** Provide at least one of metal_id, ligand_id, or beta_definition_id.

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "c.ligand_name_SRD LIKE '%EDTA%' OR c.ligand_name_SRD LIKE '%ethylenediaminetetra%'",
  "order_by": "s.constant_value DESC",
  "limit": 20
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. You must call 0_plan_search_strategy first (PHASE 2) before using the execution tools.

---

### Step 10: `search_similar_ligands`
**Args:**
```json
{
  "ligand_name": "EDTA",
  "top_k": 10
}
```

[summary]
## search_similar_ligands — 0 row(s)

**Query:** ligand_6118

*(no similar ligands found)*

---

### Step 11: `search_similar_ligands`
**Args:**
```json
{
  "ligand_name": "ethylenediaminetetraacetic",
  "top_k": 10
}
```

[TOOL ERROR] search_similar_ligands: Error executing tool search_similar_ligands: No ligand found for name='ethylenediaminetetraacetic'

---

### Step 12: `search_citations`
**Args:**
```json
{
  "where": "(la.citation LIKE '%EDTA%' OR la.citation LIKE '%ethylenediaminetetraac%')",
  "limit": 10
}
```

[summary]
## search_citations — 1 row(s)

| example_vlm_id | vlm_count | lit_id | shortcut | citation |
|----------------|-----------|--------|----------|----------|
| vlm_108224 | 587 | lit_10315 | 77Aee | G. Anderegg, "Critical Survey of Stability Constants of EDTA Complexes", Pergam… |

---

### Step 13: `inspect_literature`
**Args:**
```json
{
  "prefix_id": "vlm_108224"
}
```

[summary]
## inspect_literature — vlm_108224 — 117 citation(s)

| lit_id | shortcut | citation |
|--------|----------|----------|
| lit_739 | 47SA | G. Schwarzenbach and H. Ackerman, Helv. Chim. Acta, 1947, 30, 1798 |
| lit_979 | 51Ca | M. J. Cabell, The Complex Ions formed by Thorium and Uranium with Complexones, … |
| lit_1831 | 53CMb | F. F. Carini and A. E. Martell, J. Amer. Chem. Soc., 1953, 75, 4810 |
| lit_1205 | 56CS | R. A. Care and L. A. K. Staveley, J. Chem. Soc., 1956, 4571 |
| lit_2662 | 58ISE | H. Irving, R. Shelton, and R. Evans, J. Chem. Soc., 1958, 3540 |
| lit_2778 | 58TS | M. J. L. Tillotson and L. A. K. Staveley, J. Chem. Soc., 1958, 3613 |
| lit_2797 | 58YKa | K. B. Yatsimirskii and G. A. Karacheva, Izv. Vyssh. Ucheb. Zaved., Khim., 1958,… |
| lit_2829 | 59BG | M. T. Beck and S. Gorog, Chem. Anal., 1959, 48, 90; Magyar Tud. Akad. Kem. Tud.… |
| lit_3106 | 60BM | T. A. Bohigian and A. E. Martell, US-AEC Report TID-11255, 1960 |
| lit_3112 | 60BT | A. I. Busev, V. G. Tiptsova, and T. A. Sokolova, Russ. J. Inorg. Chem., 1960, 5… |
| lit_3525 | 61Sa | R. B. Simpson, J. Amer. Chem. Soc., 1961, 83, 4711 |
| lit_3572 | 61TT | G. S. Tereshin and I. V. Tananaev, J. Anal. Chem. USSR, 1961, 16, 519 (523) |
| lit_3740 | 62KE | N. N. Krot, N. P. Ermolaev, and A. D. Gelman, Russ. J. Inorg. Chem., 1962, 7, 1… |
| lit_3910 | 63Aa | G. Anderegg, Helv. Chim. Acta, 1963, 46, 1833 |
| lit_3981 | 63DG | A. F. Donda and A. M. Giuliani, Ric. Sci., 1963, 33 (II-A), 819 |
| lit_4074 | 63ID | H. Irving and J. J. R. Frausto da Silva, J. Chem. Soc., 1963, 448 |
| lit_4177 | 63P | V. Palaty, Canad. J. Chem., 1963, 41, 18 |
| lit_4604 | 64SMb | Unpublished values quoted in L. G. Sillen and A. E. Martell, Stability Constant… |
| lit_4691 | 65BCY | J. Botts, A. Chashin, and H. L. Young, Biochem., 1965, 4, 1788 |
| lit_5097 | 66BL | C. Bamberger and F. Laguna, J. Inorg. Nucl. Chem., 1966, 28, 1067 |
| lit_5237 | 66KR | R. J. Kula and G. H. Reed, Anal. Chem., 1966, 38, 697 |
| lit_5238 | 66KRa | R. J. Kula and D. L. Rabenstein, Anal. Chem., 1966, 38, 1934 |
| lit_5218 | 66Ka | R. J. Kula, Anal. Chem., 1966, 38, 1581 |
| lit_5281 | 66MC | T. Moeller and S. K. Chu, J. Inorg. Nucl. Chem., 1966, 28, 153 |
| lit_5446 | 67A | G. Anderegg, Helv. Chim. Acta, 1967, 50, 2333 |
| lit_5604 | 67IM | H. M. Irving, M. G. Miles, and L. D. Pettit, Anal. Chim. Acta, 1967, 38, 475 |
| lit_5718 | 67MV | P. Meszaros, G. Vinek, and N. Konopik, Monat. Chem., 1967, 98, 1810 |
| lit_5850 | 67T | L. I. Tikhonova, Russ. J. Inorg. Chem., 1967, 12, 494 (939) |
| lit_6031 | 68DS | J. J. R. Frausto da Silva and M. L. S. Simoes, Talanta, 1968, 15, 609 |
| lit_6159 | 68KSb | J. R. Kuempel and W. B. Schaap, Inorg. Chem., 1968, 7, 2435 |
| lit_6252 | 68NPP | M. Naarova, J. Podlahova, and J. Podlaha, Coll. Czech. Chem. Comm., 1968, 33, 1… |
| lit_6429 | 68WR | H. Wikberg and A. Ringbom, Suomen Kem., 1968, B41, 177 |
| lit_6432 | 68WSb | J. I. Watters and O. E. Schupp, III, J. Inorg. Nucl. Chem., 1968, 30, 3359 |
| lit_1321 | 69CI | J. J. Christensen, R. M. Izatt, D. P. Wrathall, and L. D. Hansen, J. Chem. Soc.… |
| lit_1358 | 69DS | J. J. R. Frausto da Silva and M. L. S. Simoes, Rev. Port. Quim., 1969, 11, 54; … |
| lit_6894 | 70AMa | G. Anderegg and S. C. Malik, Helv. Chim. Acta, 1970, 53, 577 |
| lit_6907 | 70Bf | M. Bartusek, Spisy Prir. Fak. Univ. Purk. Brne, 1970, E38, 397 |
| lit_1449 | 70KC | G. C. Kugler and G. H. Carey, Talanta, 1970, 10, 907 |
| lit_7742 | 71RMS | D. B. Rorabacher, W. J. MacKellar, G. R. Shu, and M. Bonavita, Anal. Chem., 197… |
| lit_8144 | 72LLa | J. Lagrange and P. Lagrange, Bull. Soc. Chim. France, 1972, 13 |
| lit_8519 | 73CS | J. D. Carr and D. G. Swartzfager, J. Amer. Chem. Soc., 1973, 95, 3569 |
| lit_8537 | 73DR | P. C. Das and G. S. Rao, J. Indian Chem. Soc., 1973, 50, 172 |
| lit_8903 | 73VKY | V. P. Vasilev, L. A. Kochergina, and T. D. Yastrebova, J. Gen. Chem. USSR, 1973… |
| lit_8946 | 74B | E. W. Baumann, J. Inorg. Nucl. Chem., 1974, 36, 1827 |
| lit_9369 | 74VKY | V. P. Vasilev, L. A. Kochergina, and T. D. Yastrebova, J. Gen. Chem. USSR, 1974… |
| lit_9416 | 75APB | G. Anderegg, N. G. Podder, P. Blauenstein, M. Hangartner, and H. Stunzi, J. Coo… |
| lit_9442 | 75BKN | E. Brucher, R. Kiraly, and I. Nagypal, J. Inorg. Nucl. Chem., 1975, 37, 1009 |
| lit_9483 | 75CSc | J. D. Carr and D. G. Swartzfager, J. Amer. Chem. Soc., 1975, 97, 315 |
| lit_9660 | 75LN | K. I. Litovchenko, V. N. Nikitenko, and V. S. Kublanovskii, Soviet J. Coord. Ch… |
| lit_9825 | 75VB | J. Volta and M. Bartusek, Coll. Czech. Chem. Comm., 1975, 40, 2050 |
| lit_9853 | 76A | G. Anderegg, Z. Naturforsch., 1976, 31b, 786 |
| lit_9867 | 76AM | G. Anderegg and S. C. Malik, Helv. Chim. Acta, 1976, 59, 1498 |
| lit_9944 | 76CWW | A. M. Corrie, M. D. Walker, and D. R. Williams, J. Chem. Soc. Dalton, 1976, 1012 |
| lit_10000 | 76GMD | J. M. Gatez, E. Merciny, and G. Duyckaerts, Anal. Chim. Acta, 1976, 84, 383 |
| lit_10284 | 76VKO | V. P. Vasilev, L. A. Kochergina, and T. D. Orlova, J. Gen. Chem. USSR, 1976, 46… |
| lit_10315 | 77Aee | G. Anderegg, "Critical Survey of Stability Constants of EDTA Complexes", Pergam… |
| lit_10386 | 77CB | H. H. Christensen and O. K. Borggaard, Acta Chem. Scand., 1977, A31, 793 |
| lit_10395 | 77CGG | G. R. Choppin, M. P. Goedken, and T. F. Gritmon, J. Inorg. Nucl. Chem., 1977, 3… |
| lit_1515 | 77GGC | T. F. Gritmon, M. P. Goedken, and G. R. Choppin, J. Inorg. Nucl. Chem., 1977, 3… |
| lit_1544 | 77HS | Y. Hojo, Y. Sugiura, and H. Tanaka, J. Inorg. Nucl. Chem., 1977, 39, 715 |
| lit_1587 | 77KST | N. A. Kostromina, V. P. Shelest, T. V. Ternovaya, and Ts. B. Konunova, Russ. J.… |
| lit_10483 | 77OM | N. Oyama, H. Matsuda, and H. Ohtaki, Bull. Chem. Soc. Japan, 1977, 50, 406 |
| lit_10592 | 77VL | V. P. Vasilev, V. P. Lymar, and A. I. Lytkin, Russ. J. Inorg. Chem., 1977, 22, … |
| lit_10593 | 77VLa | V. P. Vasilev, V. P. Lymar, and A. I. Lytkin, Russ. J. Inorg. Chem., 1977, 22, … |
| lit_10634 | 78AMa | G. Arena, S. Musumeci, E. Rizzarelli, and S. Sammartano, Ann. Chim. (Rome), 197… |
| lit_10756 | 78J | M. Jawaid, Talanta, 1978, 25, 215 |
| lit_10848 | 78MGD | E. Merciny, J. M. Gatez, and G. Duyckaerts, Anal. Chim. Acta, 1978, 100, 329 |
| lit_10994 | 78VKO | V. P. Vasilev, L. A. Kochergina, and T. D. Orlova, J. Gen. Chem. USSR, 1978, 48… |
| lit_11221 | 79LM | P. Letkeman and A. E. Martell, Inorg. Chem., 1979, 18, 1284 |
| lit_11416 | 79VKO | V. P. Vasilev, L. A. Kochergina, and T. D. Orlova, J. Gen. Chem. USSR, 1979, 49… |
| lit_1659 | 80MCc | C. Gh. Macarovici and E. Chis, Rev. Roum. Chim., 1980, 25, 503 |
| lit_1668 | 80MHB | A. Mikan, J. Havel, and M. Bartusek, Scr. Fac. Sci. Nat. Univ. Purk. Brun., 198… |
| lit_11708 | 80THa | M. M. Taqui Khan and A. Hussain, Indian J. Chem., 1980, 19A, 50 |
| lit_12078 | 81RMR | K. S. Rajan, S. Mainer, N. L. Rajan, and J. M. Davis, J. Inorg. Biochem., 1981,… |
| lit_12202 | 82AKB | A. Avdeef, D. L. Kearney, J. A. Brown, and A. R. Chemotti, Jr., Anal. Chem., 19… |
| lit_12342 | 82HA | Z. X. Huang, H. S. Al-Falahi, A. Cole, J. R. Duffield, C. Furnival, D. C. Jones… |
| lit_12475 | 82OL | P. A. Overvoll and W. Lund, Anal. Chim. Acta, 1982, 143, 153 |
| lit_12706 | 83DR | P. G. Daniele, C. Rigano, and S. Sammartano, Talanta, 1983, 30, 81 |
| lit_12799 | 83KDc | J. Kragten and L. G. Decnop-Weever, Talanta, 1983, 30, 623 |
| lit_13043 | 83WW | M. J. Willes and D. R. Williams, Inorg. Chim. Acta, 1983, 80, L35 |
| lit_13154 | 84DMW | J. R. Duffield, P. M. May, and D. R. Williams, J. Inorg. Biochem., 1984, 20, 199 |
| lit_13308 | 84MDH | A. Mederos, S. Dominquez, M. Hernandez Padilla, F. Brito, and E. Chinea, Bol. S… |
| lit_13417 | 84SA | M. L. Simoes Goncalves, A. M. Almeida Mota, and J. J. R. Frausto da Silva, Tala… |
| lit_13474 | 84VG | V. P. Vasilev, N. K. Grechina, and N. Yu. Bugrova, J. Gen. Chem. USSR, 1984, 54… |
| lit_13597 | 85DRa | P. G. Daniele, C. Rigano, and S. Sammartano, Anal. Chem., 1985, 57, 2956 (see s… |
| lit_13735 | 85MEB | M. A. Marini, W. J. Evans, and R. L. Berger, J. Biochem. Biophys. Methods, 1985… |
| lit_13854 | 85SM | R. M. Smith, R. J. Motekaitis, and A. E. Martell, Inorg. Chem., 1985, 24, 1132 |
| lit_13883 | 85SYY | S. Singh, P. C. Yadava, and K. L. Yakava, J. Electrochem. Soc. India, 1985, 34,… |
| lit_14147 | 86MEB | M. A. Marini, W. J. Evans, and R. L. Berger, J. Biochem. Biophys. Methods, 1986… |
| lit_14230 | 86SB | Yu. I. Salnikov and G. A. Boos, Russ. J. Inorg. Chem., 1986, 31, 1393 (2417) |
| lit_14360 | 87BK | A. A. Bugaevskii and N. L. Khimenko, Soviet Progr. Chem. (Ukr. Khim. Zh.), 1987… |
| lit_14638 | 87TKS | L. B. Thuan, G. N. Kupriyanova, N. S. Smirnova, L. I. Martynenko, and A. M. Evs… |
| lit_14788 | 88ESK | A. M. Evseev, N. S. Smirnova, Yu. A. Kiryanov, E. M. Nikolaeva, and G. P. Ozero… |
| lit_14821 | 88HH | J. K. Hovey, L. G. Hepler, and P. R. Tremaine, Canad. J. Chem., 1988, 66, 881 |
| lit_15009 | 88THV | M. M. Taqui Khan, A. Hussain, K. Venkatasubramanian, G. Ramachandraiah, and V. … |
| lit_15264 | 89Ma | I. V. Mironov, Russ. J. Inorg. Chem., 1989, 34, 1075 (1892) |
| lit_15318 | 89NS | R. Nagar and R. C. Sharma, Indian J. Chem., 1989, 28A, 627 |
| lit_15369 | 89SBO | Yu. I. Salnikov, G. A. Boos, and I. V. Ovchinnikova, Russ. J. Inorg. Chem., 198… |
| lit_15375 | 89SDS | I. E. Svetlova, N. A. Dobrynina, N. S. Smirnova, L. I. Martynenko, A. V. Evseev… |
| lit_15441 | 90AD | S. Ahrland, A. Dahlgren, and I. Persson, Acta Agric. Scand., 1990, 40, 101 |
| lit_15858 | 91DMW | J. R. Duffield, F. Marsicano, and D. R. Williams, Polyhedron, 1991, 10, 1105 |
| lit_16010 | 91Pa | A. Poczynajlo, J. Radioanal. Nucl. Chem., Art., 1991, 148, 295 |
| lit_16040 | 91SBG | Yu. I. Salnikov, G. A. Boos, Kh. V. Gibadullina, R. R. Basyrova, and N. L. Shak… |
| lit_16103 | 92A | G. Anderegg, Inorg. Chim. Acta, 1992, 194, 31 |
| lit_16196 | 92GH | S. Glab, A. Hulanicki, and U. Nowicka, Talanta, 1992, 39, 1555 |
| lit_16341 | 92TD | D. R. Turner, M. M. C. dos Santos, P. Coutinho, and M. de Lurdes Goncalves, Ana… |
| lit_16429 | 93CR | M. Chen and R. S. Reid, Canad. J. Chem., 1993, 71, 763 |
| lit_16529 | 93MDC | G. A. Mazzocchin, S. Daniele, M. Corbetta, and A. De Lorenzi, Ann. Chim. (Rome)… |
| lit_16757 | 94KCF | K. Kumar, C. A. Chang, L. C. Francesconi, D. D. Dischino, M. F. Malley, J. Z. G… |
| lit_16818 | 94Na | R. Nager, J. Electrochem. Soc. India, 1994, 43, 41 |
| lit_17120 | 95SM | P. Sadowski and M. Majdan, Monat. Chem., 1995, 126, 863 |
| lit_17318 | 96NV | E. Norkus, A. Vaskelis, and I. Zakaite, Talanta, 1996, 43, 465 |
| lit_17338 | 96RH | D. P. Riley, S. L. Henke, P. J. Lennon, R. H. Weiss, W. L. Neumann, W. J. River… |
| lit_17347 | 96SA | Y. Sun, C. J. Anderson, T. S. Pajeau, D. E. Reichert, R. D. Hancock, R. J. Mote… |
| lit_17458 | 97DQ | R. Delgado, S. Quintino, M. Teixira, and A. Zhang, J. Chem. Soc. Dalton, 1997, … |
| lit_17769 | 98SB | S. I. Sinkov and E. I. Bozhenko, J. Alloys Comp., 1998, 271-273, 809 |
| lit_17847 | 99BR | J. Brockmann and F. Rosch, Radiochim. Acta, 1999, 87, 79 |

---

### Step 14: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_name_SRD LIKE '%EDTA%' OR c.ligand_name_SRD LIKE '%ethylenediaminetetraac%')",
  "order_by": "s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability — 20 row(s)

### ΔS — 18 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_205 | Y^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_55 | Er^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_70 | Hf^[4+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_209 | Zr^[4+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_5 | Al^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_185 | Th^[4+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_74 | In^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_192 | Tm^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_81 | Lu^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_206 | Yb^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_185 | Th^[4+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_73 | Ho^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_44 | Dy^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_179 | Tb^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_201 | VO^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_65 | Gd^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_58 | Eu^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |

---

### Step 15: `search_pka_values`
**Args:**
```json
{
  "where": "(lc.ligand_name_SRD LIKE '%EDTA%' OR lc.ligand_name_SRD LIKE '%ethylenediaminetetraac%')",
  "order_by": "p.pKa ASC",
  "limit": 20
}
```

[summary]
## search_pka_values — 20 row(s)

### pKa -2.0–-1.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_111731 | ligand_6335 | Oxybis(ethylenenitrilo)tetraacetic… | H4L | O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | -1.8 | 20 | 0.1 | H3L→H4L | M_tot_1 | M_tot_1 |

### pKa -1.5–-1.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_108289 | ligand_6277 | Ethylenedinitrilotetraacetic acid … | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | -1.5 | 25 | 0.1 | H4L→H5L | M_tot_1 | M_tot_2 |

### pKa 2.0–2.5 (2 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_108282 | ligand_6277 | Ethylenedinitrilotetraacetic acid … | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 25 | 0.1 | H3L→H4L | M_tot_2 | M_tot_2 |
| vlm_112242 | ligand_6348 | Thiobis(ethylenenitrilo)tetraaceti… | H4L | O=C(O)CN(CCSCCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 25 | 0.1 | H3L→H4L | M_tot_1 | M_tot_1 |

### pKa 2.5–3.0 (4 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_107963 | ligand_6275 | N-(2-Hydroxyethyl)ethylenedinitril… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 2.62 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_1 |
| vlm_112239 | ligand_6348 | Thiobis(ethylenenitrilo)tetraaceti… | H4L | O=C(O)CN(CCSCCN(CC(=O)O)CC(=O)O)CC(=O)O | 2.68 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_1 |
| vlm_108272 | ligand_6277 | Ethylenedinitrilotetraacetic acid … | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2.69 | 25 | 0.1 | H2L→H3L | M_tot_2 | M_tot_1 |
| vlm_111729 | ligand_6335 | Oxybis(ethylenenitrilo)tetraacetic… | H4L | O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 2.76 | 20 | 0.1 | H2L→H3L | M_tot_1 | M_tot_1 |

### pKa 3.0–3.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_103959 | ligand_6118 | 6,11,18,23-Tetraoxo-1,4,7,10,13,16… | *** | *** | 3.3 | 25 | 0.1 | H3L→H4L | M_tot_1 | M_tot_1 |

### pKa 4.0–4.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_103958 | ligand_6118 | 6,11,18,23-Tetraoxo-1,4,7,10,13,16… | *** | *** | 4.18 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_1 |

### pKa 5.0–5.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_107958 | ligand_6275 | N-(2-Hydroxyethyl)ethylenedinitril… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 5.38 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_5 |

### pKa 6.0–6.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_108254 | ligand_6277 | Ethylenedinitrilotetraacetic acid … | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 6.13 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_7 |

### pKa 7.0–7.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_103957 | ligand_6118 | 6,11,18,23-Tetraoxo-1,4,7,10,13,16… | *** | *** | 7.26 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_1 |

### pKa 7.5–8.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_103956 | ligand_6118 | 6,11,18,23-Tetraoxo-1,4,7,10,13,16… | *** | *** | 7.78 | 25 | 0.1 | L→HL | M_tot_1 | M_tot_2 |

### pKa 8.0–8.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_112232 | ligand_6348 | Thiobis(ethylenenitrilo)tetraaceti… | H4L | O=C(O)CN(CCSCCN(CC(=O)O)CC(=O)O)CC(=O)O | 8.37 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_1 |

### pKa 8.5–9.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_111721 | ligand_6335 | Oxybis(ethylenenitrilo)tetraacetic… | H4L | O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 8.75 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_1 |

### pKa 9.0–9.5 (2 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_112225 | ligand_6348 | Thiobis(ethylenenitrilo)tetraaceti… | H4L | O=C(O)CN(CCSCCN(CC(=O)O)CC(=O)O)CC(=O)O | 9.31 | 25 | 0.1 | L→HL | M_tot_1 | M_tot_35 |
| vlm_111713 | ligand_6335 | Oxybis(ethylenenitrilo)tetraacetic… | H4L | O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 9.39 | 25 | 0.1 | L→HL | M_tot_1 | M_tot_37 |

### pKa 9.5–10.0 (2 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_108224 | ligand_6277 | Ethylenedinitrilotetraacetic acid … | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 9.52 | 25 | 0.1 | L→HL | M_tot_7 | M_tot_70 |
| vlm_107949 | ligand_6275 | N-(2-Hydroxyethyl)ethylenedinitril… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 9.7 | 25 | 0.1 | L→HL | M_tot_5 | M_tot_47 |

---
