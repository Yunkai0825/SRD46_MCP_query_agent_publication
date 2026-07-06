# Q5.2.3 — Tool Results (batch 4)

### Step 3: `search_stability`
**Args:**
```json
{
  "where": "(s.temperature_c BETWEEN 195 AND 205 AND (s.solvent_name LIKE '%water%' OR s.solvent_name LIKE '%aqueous%' OR s.solvent_name IS NULL))",
  "order_by": "s.temperature_c ASC",
  "limit": 500
}
```

[summary]
## search_stability

*(no results)*

---

### Step 4: `search_networks`
**Args:**
```json
{
  "where": "(m.condition_temp_min <= 200 AND m.condition_temp_max >= 200)",
  "order_by": "m.condition_temp_min ASC",
  "limit": 100,
  "ligand_similarity": false
}
```

[summary]
## search_networks

*(no results)*

---

### Step 5: `search_stability`
**Args:**
```json
{
  "where": "(s.temperature_c >= 150)",
  "order_by": "s.temperature_c DESC",
  "limit": 1000
}
```

[summary]
## search_stability

*(no results)*

---

### Step 6: `search_citations`
**Args:**
```json
{
  "where": "(la.citation LIKE '%200 C%' OR la.citation LIKE '%473 K%' OR la.citation LIKE '%hydrothermal%' OR la.citation LIKE '%bar%' OR la.citation LIKE '%MPa%')",
  "order_by": "la.citation ASC",
  "limit": 200
}
```

[summary]
## search_citations — 200 row(s)

| example_vlm_id | vlm_count | lit_id | shortcut | citation |
|----------------|-----------|--------|----------|----------|
| vlm_120986 | 34 | lit_13160 | 84EA | A. A. El-Harakany, F. M. Abdel Halim, and A. O. Barakat, J. Electroanal. Chem.,… |
| vlm_139221 | 20 | lit_9323 | 74SD | A. A. Schilt and W. E. Dunbar, Tetrahedron, 1974, 30, 401 |
| vlm_125881 | 16 | lit_10322 | 77AFB | A. Anichini, L. Fabbrizzi, R. Barbucci, and A. Mastroianni, J. Chem. Soc. Dalto… |
| vlm_126677 | 90 | lit_15775 | 91AB | A. Apelblat and J. Barthel, Z. Naturforsch., 1991,  46a, 131 |
| vlm_153819 | 3 | lit_13980 | 86BPb | A. Baral and R. K. Patnaik, J. Inst. Chemists (India), 1986, 58, 134 |
| vlm_153818 | 2 | lit_15466 | 90BP | A. Baral and R. K. Patnaik, J. Inst. Chemists (India), 1990, 62, 6 |
| vlm_168569 | 3 | lit_5083 | 66BBB | A. Barocas, F. Baroncelli, G. B. Biondi, and G. Grossi, J. Inorg. Nucl. Chem., … |
| vlm_102868 | 44 | lit_14356 | 87BGH | A. Bevilacqua, R. I. Gelb, W. B. Hebard, and L. J. Zompa, Inorg. Chem., 1987, 2… |
| vlm_177067 | 14 | lit_5120 | 66CP | A. Cassol, R. Portanova, and L. Magon, Ric. Sci., 1966, 36, 1180; A. Cassol, L.… |
| vlm_160882 | 7 | lit_7187 | 70PSa | A. D. Parulekar and P. R. Subbaraman, Indian J. Chem., 1970, 8, 266 |
| vlm_160889 | 18 | lit_8280 | 72PS | A. D. Parulekar and P. R. Subbaraman, Indian J. Chem., 1972, 10, 205 |
| vlm_104277 | 25 | lit_1341 | 69DB | A. Delle Site and R. D. Baybarz, J. Inorg. Nucl. Chem., 1969, 31, 2201 |
| vlm_177497 | 3 | lit_8955 | 74BC | A. J. Barker and A. B. Clarke, J. Inorg. Nucl. Chem., 1974, 36, 921 |
| vlm_154888 | 37 | lit_15456 | 90BCU | A. J. Barwise, R. G. Compton, and P. R. Unwin, J. Chem. Soc. Faraday, 1990, 86,… |
| vlm_119251 | 1 | lit_8500 | 73CBa | A. K. Chakrabarti and S. P. Bag, Z. Anal. Chem., 1973, 265, 269 |
| vlm_180752 | 1 | lit_8983 | 74CB | A. K. Chakrabarti and S. P. Bag, Z. Anal. Chem., 1974, 272, 124 |
| vlm_183258 | 1 | lit_2698 | 58MC | A. K. Majumdar and M. M. Chakrabartty, Anal. Chim. Acta, 1958, 19, 372 |
| vlm_106172 | 3 | lit_1679 | 80MMM | A. Mederos, E. Medina de la Rosa and P. Martin Barroso, An. Quim., 1980, 76B, 2… |
| vlm_104573 | 3 | lit_12432 | 82MMA | A. Mederos, E. Medina de la Rosa, J. J. Alvarez Colomer, and P. Martin Barrosa,… |
| vlm_106147 | 7 | lit_11254 | 79MFM | A. Mederos, J. Fuentes, E. Madina, P. Martin Barroso, and B. Rodriguez Rios, An… |
| vlm_106147 | 68 | lit_1664 | 80MFa | A. Mederos, J. Fuentes, E. Medina de la Rosa, P. Martin Barroso, and R. B. Rodr… |
| vlm_167006 | 76 | lit_1654 | 80MBb | A. Mikan and M. Bartusek, Coll. Czech. Chem. Comm., 1980, 45, 2645 |
| vlm_108224 | 75 | lit_1668 | 80MHB | A. Mikan, J. Havel, and M. Bartusek, Scr. Fac. Sci. Nat. Univ. Purk. Brun., 198… |
| vlm_171259 | 1 | lit_8635 | 73KBc | A. P. Klintsova and V. L. Barsukov, Geochem. Int., 1973, 10, 540 (709) |
| vlm_182787 | 1 | lit_4928 | 65PB | A. Polaczek and E. Baranowska, J. Inorg. Nucl. Chem., 1965, 27, 1649 |
| vlm_111567 | 1 | lit_10524 | 77RSK | A. R. Rajput, M. Sugawara, and T. Kambara, J. Electroanal. Chem., 1977, 75, 573 |
| vlm_122610 | 199 | lit_6883 | 70ABP | A. T. Advani, D. S. Barnes, and L. D. Pettit, J. Chem. Soc. (A), 1970, 2691 |
| vlm_99687 | 70 | lit_13105 | 84BMY | A. V. Barsukov, T. A. Matkovskaya, G. F. Yaroshenko, G. R. Allakhverdov, and N.… |
| vlm_181349 | 16 | lit_9792 | 75SLB | A. V. Serdyukova, A. N. Lazarev, G. M. Baranov, and V. V. Perekalin, Russ. J. I… |
| vlm_133587 | 55 | lit_15104 | 89BL | B. Barszcz and B. Lenarcik, Polish J. Chem., 1989, 63, 371 |
| vlm_133435 | 18 | lit_13967 | 86BGK | B. Barszcz, M. Gabryszewski, J. Kulig, and B. Lenarcik, J. Chem. Soc. Dalton, 1… |
| vlm_133792 | 61 | lit_13540 | 85BGK | B. Barszcz, M. Gabryszewski, and J. Kulig, Polish J. Chem., 1985, 59, 121 |
| vlm_133518 | 53 | lit_15075 | 89Bb | B. Barszcz, Polish J. Chem., 1989, 63, 9 |
| vlm_144327 | 144 | lit_7048 | 70GF | B. Grabaric and I. Filipovic, Croat. Chem. Acta, 1970, 42, 479 |
| vlm_144333 | 77 | lit_9989 | 76GF | B. Grabaric and I. Filipovic, Croat. Chem. Acta, 1976, 48, 17 |
| vlm_145274 | 11 | lit_9548 | 75GM | B. Grabaric, B. Mayer, I. Piljac, and I. Filipovic, Electrochim. Acta, 1975, 20… |
| vlm_145241 | 59 | lit_9066 | 74GMa | B. Grabaric, B. Mayer, I. Piljac, and I. Filipovic, J. Inorg. Nucl. Chem., 1974… |
| vlm_147883 | 3 | lit_8577 | 73GP | B. Grabaric, I. Piljac, and I. Filipovic, Anal. Chem., 1973, 45, 1932 |
| vlm_145274 | 5 | lit_9554 | 75GT | B. Grabaric, M. Tkalcec, I. Piljac, I. Filipovic, and V. Simeon, Anal. Chim. Ac… |
| vlm_134204 | 10 | lit_1626 | 80LB | B. Lenarcik and B. Barszcz, J. Chem. Soc. Dalton, 1980, 24 |
| vlm_134088 | 34 | lit_11213 | 79LB | B. Lenarcik and B. Barszcz, Polish J. Chem., 1979, 53, 963 |
| vlm_134034 | 41 | lit_10415 | 77LB | B. Lenarcik and B. Barszcz, Rocz. Chem., 1977, 51, 1849 |
| vlm_134122 | 16 | lit_10417 | 77LBK | B. Lenarcik, B. Barszcz, and J. Kulig, Rocz. Chem., 1977, 51, 1315 |
| vlm_133426 | 12 | lit_9173 | 74LKB | B. Lenarcik, J. Kulig, and B. Barszcz, Rocz. Chem., 1974, 48, 2111 |
| vlm_133440 | 10 | lit_10098 | 76LK | B. Lenarcik, J. Kulig, and B. Barszcz, Rocz. Chem., 1976, 50, 183 |
| vlm_147832 | 42 | lit_10859 | 78MMG | B. Mayer, K. Medancic, B. Grabaric, and I. Filipovic, Croat. Chem. Acta, 1978, … |
| vlm_160912 | 9 | lit_7147 | 70NPC | B. P. Nikolskii, V. V. Palchevskii, A. D. Chegodaeva, and N. K. Barkova, Dokl. … |
| vlm_117788 | 13 | lit_13396 | 84RF | B. Rodriguez Rios, J. Fuentes Diaz, and R. Reboso Barroso, An. Quim., 1984, 80B… |
| vlm_117772 | 16 | lit_13398 | 84RFb | B. Rodriguez Rios, J. Fuentes Diaz, and R. Reboso Barroso, An. Quim., 1984, 80B… |
| vlm_177217 | 6 | lit_10914 | 78RBa | C. E. Roberson and R. B. Barnes, Chem. Geol., 1978, 21, 239 |
| vlm_178616 | 1 | lit_13302 | 84MBH | C. Madic, G. M. Begun, D. E. Hobart, and R. L. Hahn, Inorg. Chem., 1984, 23, 19… |
| vlm_118645 | 107 | lit_7168 | 70PBF | C. Petitfaux, J. P. Barbier, and J. Faucherre, Bull. Soc. Chim. France, 1970, 3… |
| vlm_98363 | 32 | lit_7775 | 71SLZ | C. S. Sokol, H. Laussegger, L. J. Zompa, and C. S. Brubaker, Jr., J. Inorg. Nuc… |
| vlm_168927 | 14 | lit_2587 | 58BB | C. V. Banks and D. W. Barnum, J. Amer. Chem. Soc., 1958, 80, 3579 |
| vlm_168403 | 16 | lit_10651 | 78BC | D. A. Brown, M. V. Chidambaram, J. J. Clarke, and D. M. McAleese, Bioinorg. Che… |
| vlm_121426 | 15 | lit_11479 | 80BC | D. A. Brown, M. V. Chidambaram, and J. D. Glennon, Inorg. Chem., 1980, 19, 3260 |
| vlm_150134 | 104 | lit_1282 | 69BLP | D. Barnes, P. G. Laye, and L. D. Pettit, J. Chem. Soc. (A), 1969, 2073 |
| vlm_144406 | 150 | lit_17833 | 99BBR | D. Barron, S. Buti, M. Ruiz, and J. Barbosa, Polyhedron, 1999, 18, 3281 |
| vlm_182245 | 1 | lit_13191 | 84GGa | D. G. Gambarov and A. G. Guseinov, J. Anal. Chem. USSR, 1984, 39, 669 |
| vlm_164761 | 7 | lit_15186 | 89GGA | D. G. Gambarov, E. L. Glushchenko, A. R. Abramov, and F. T. Aslanova, Russ. J. … |
| vlm_101376 | 11 | lit_1547 | 77HZ | D. M. Higgins and L. J. Zompa, J. Coord. Chem., 1977, 7, 105 |
| vlm_94273 | 307 | lit_7356 | 71BP | D. S. Barnes and L. D. Pettit, J. Inorg. Nucl. Chem., 1971, 33, 2177 |
| vlm_150997 | 71 | lit_7340 | 71BFP | D. S. Barnes, G. J. Ford, L. D. Pettit, and C. Sherrington, J. Chem. Soc. (A), … |
| vlm_166167 | 26 | lit_1315 | 69CB | E. Chiacchierini and M. Bartusek, Coll. Czech. Chem. Comm., 1969, 34, 530 |
| vlm_104542 | 19 | lit_11267 | 79MMM | E. Medina de la Rosa, A. Mederos, P. Martin Barroso, and J. J. Alvarez Colomer,… |
| vlm_147424 | 9 | lit_12001 | 81MB | E. Mikanova and M. Bartusek, Ser. Fac. Sci. Nat. Univ. Purk. Brun., 1981, 11, 4… |
| vlm_166167 | 30 | lit_12002 | 81MBa | E. Mikanova and M. Bartusek, Ser. Fac. Sci. Nat. Univ. Purk. Brun., 1981, 11, 4… |
| vlm_105691 | 7 | lit_12016 | 81MMB | E. Mikanova, M. Mikesova, and M. Bartusek, Coll. Czech. Chem. Comm., 1981, 46, … |
| vlm_170604 | 37 | lit_2273 | 56OB | E. Orban, M. K. Barnett, J. S. Boyle, J. R. Heiks, and L. V. Jones, J. Phys. Ch… |
| vlm_168539 | 11 | lit_4694 | 65BG | F. Baroncelli and G. Grossi, J. Inorg. Nucl. Chem., 1965, 27, 1085 |
| vlm_135288 | 42 | lit_3935 | 63BBS | F. Becker, J. Barthel, N. G. Schmahl, and H. M. Luschow, Z. Phys. Chem. N. F. (… |
| vlm_149926 | 14 | lit_9319 | 74SB | F. Sprta and M. Bartusek, Coll. Czech. Chem. Comm., 1974, 39, 2023 |
| vlm_166958 | 39 | lit_8832 | 73SBd | F. Sprta and M. Bartusek, Scr. Fac. Sci. Nat. Univ. Purk. Brun., Chem., 1973, 3… |
| vlm_171266 | 92 | lit_4375 | 64DG | F. Z. Dzhabarov and S. V. Gorbachev, Russ. J. Inorg. Chem., 1964, 9, 1297 (2399) |
| vlm_159859 | 28 | lit_16655 | 94AEF | G. Arana, N. Etxebarria, and L. A. Fernandez, F. J. Anal. Chem., 1994, 349, 703 |
| vlm_153129 | 27 | lit_10319 | 77AC | G. Arena, R. Cali, E. Rizzarelli, S. Sammartano, R. Barbucci, and M. J. M. Camp… |
| vlm_152316 | 50 | lit_10625 | 78AC | G. Arena, R. Cali, E. Rizzarelli, S. Sammartano, R. Barbucci, and M. J. M. Camp… |
| vlm_157609 | 81 | lit_6919 | 70BC | G. Besse, J. L. Chabard, G. Voissiere, J. Pettit, and J. A. Berger, Bull. Soc. … |
| vlm_170786 | 5 | lit_10667 | 78BP | G. Biedermann and R. Palombari, Acta Chem. Scand., 1978, A32, 381 |
| vlm_178334 | 1 | lit_6374 | 68SRR | G. C. Stocco, E. Rivarola, R. Romeo, and R. Barbieri, J. Inorg. Nucl. Chem., 19… |
| vlm_96008 | 22 | lit_14353 | 87BDP | G. M. Baranov, L. I. Deiko, V. V. Perekalin, O. G. Pomerantseva, E. M. Speransk… |
| vlm_93606 | 202 | lit_15453 | 90BBG | G. M. Barnard, T. Boddington, J. E. Gregor, L. D. Pettit, and N. Taylor, Talant… |
| vlm_173558 | 11 | lit_15123 | 89CB | G. R. Choppin and D. W. Barber, J. Less-Common Met., 1989, 149, 231; in "Rare E… |
| vlm_147054 | 26 | lit_1260 | 69BBe | G. V. Bakore and M. S. Bararia, Z. Phys. Chem. (Leipzig), 1969, 242, 102 |
| vlm_175475 | 8 | lit_5498 | 67BRS | H. L. Barnes, S. B. Romberger, and M. Stemprok, Econ. Geol., 1967, 62, 957 |
| vlm_94975 | 84 | lit_17172 | 96AS | H. M. Abd Elbary, H. A. Shehata, M. A. F. El Arab, A. A. Mohamed, and M. M. Ema… |
| vlm_177477 | 18 | lit_363 | 34CL | I. A. Cowperthwaite, V. K. LaMer, and J. Barksdale, J. Amer. Chem. Soc., 1934, … |
| vlm_174994 | 1 | lit_7758 | 71SBa | I. A. Sheka and L. P. Barchuk, Russ. J. Inorg. Chem., 1971, 16, 1573 (2961) |
| vlm_182174 | 1 | lit_12793 | 83KBa | I. E. Kalinichenko, V. A. Barovskii, and A. T. Pilipenko, J. Gen. Chem. USSR, 1… |
| vlm_157504 | 11 | lit_2138 | 55FT | I. Feldman, T. Y. Toribara, J. R. Havill, and W. F. Neuman, J. Amer. Chem. Soc.… |
| vlm_144406 | 129 | lit_8560 | 73FPB | I. Filipovic, I. Piljac, B. Bach-Dragutinovic, I. Krlak, and B. Grabaric, Croat… |
| vlm_147832 | 16 | lit_9532 | 75FPG | I. Filipovic, I. Piljac, B. Grabaric, and B. Mayer, Anal. Chim. Acta, 1975, 76,… |
| vlm_144327 | 23 | lit_15542 | 90FT | I. Filipovic, M. Tkalcec, and B. S. Grabaric, Inorg. Chem., 1990, 29, 1092 |
| vlm_147468 | 130 | lit_10053 | 76KGF | I. Kruhak, B. Grabaric, I. Filipovic, and I. Piljac, Croat. Chem. Acta, 1976, 4… |
| vlm_148937 | 10 | lit_9739 | 75PG | I. Piljac, B. Grabaric, M. Tkalcec, S. Skoljoli, and I. Filipovic, Croat. Chem.… |
| vlm_147892 | 2 | lit_8778 | 73PG | I. Piljac, B. Grabaric, and I. Filipovic, J. Electroanal. Chem., 1973, 42, 433 |
| vlm_175400 | 16 | lit_12235 | 82BMT | J. A. Barbero, K. G. McCurdy, and P. R. Tremaine, Canad. J. Chem., 1982, 60, 18… |
| vlm_172612 | 82 | lit_12646 | 83BHM | J. A. Barbero, L. G. Hepler, K. G. McCurdy, and P. R. Tremaine, Canad. J. Chem.… |
| vlm_130904 | 1 | lit_17378 | 96TB | J. A. Thompson, M. E. Barr, D. K. Ford, L. A. Silks, III, J. McCormick, and P. … |
| vlm_176001 | 10 | lit_7373 | 71BW | J. Bard and J. O. Wear, Z. Naturforsch., 1971, 26b, 1091 |
| vlm_145241 | 212 | lit_3329 | 61BBS | J. Barthel, F. Becker, and N. G. Schmahl, Z. Phys. Chem. N. F. (Frankfurt), 196… |
| vlm_175749 | 22 | lit_4342 | 64BM | J. C. Barnes and C. B. Monk, Trans. Faraday Soc., 1964, 60, 578 |
| vlm_157092 | 39 | lit_1256 | 69BBa | J. C. Barnes and P. A. Bristow, J. Less-Common Met., 1969, 18, 381 |
| vlm_157439 | 51 | lit_6916 | 70BBd | J. C. Barnes and P. A. Bristow, J. Less-Common Met., 1970, 22, 463 |
| vlm_172133 | 24 | lit_4326 | 64Bc | J. C. Barnes, J. Chem. Soc., 1964, 3880 |
| vlm_151850 | 31 | lit_13391 | 84RBF | J. C. Rodriguez Placeres, M. Barrera, R. M. Fernandez, and A. Arevalo, J. Elect… |
| vlm_130124 | 18 | lit_12265 | 82CGM | J. Cullinane, R. I. Gelb, T. N. Margulis, and L. J. Zompa, J. Amer. Chem. Soc.,… |
| vlm_151581 | 104 | lit_969 | 51BA | J. E. Barney, W. J. Argersinger. Jr., and C. A. Reynolds, J. Amer. Chem. Soc., … |
| vlm_160211 | 38 | lit_6528 | 69HH | J. Havel, L. Havelkova, and M. Bartusek, Chem. Zvesti, 1969, 23, 582 |
| vlm_170507 | 20 | lit_13243 | 84KBL | J. I. Kim, M. Bernkopf, C. Lierse, and F. Koppold, in Geochem. Behavior of Disp… |
| vlm_138883 | 49 | lit_6313 | 68RB | J. K. Romary, J. D. Barger, and J. E. Bunds, Inorg. Chem., 1968, 7, 1142 |
| vlm_138883 | 7 | lit_5783 | 67RBB | J. K. Romary, J. E. Bunds, and J. D. Barger, J. Chem. Eng. Data, 1967, 12, 224 |
| vlm_93733 | 167 | lit_9466 | 75CB | J. L. Chabard, G. Besse, D. Pepin, J. Petit, and J. A. Berger, Bull. Soc. Chim.… |
| vlm_93847 | 123 | lit_13363 | 84PBP | J. M. Pingarron Carrazon, I. del Barrio Marcaida, and L. M. Polo Diez, An. Quim… |
| vlm_164814 | 33 | lit_14137 | 86MBa | J. Magnam, D. Barthes, and J. J. Giraud, Ann. Pharm. Fr., 1986, 44, 467 |
| vlm_137818 | 4 | lit_1308 | 69BZR | J. O. Barger, R. D. Zachariasen and J. K. Romary, J. Inorg. Nucl. Chem., 1969, … |
| vlm_144406 | 107 | lit_7996 | 72FB | J. R. Fisher and H. L. Barnes, J. Phys. Chem., 1972, 76, 90 |
| vlm_174782 | 22 | lit_958 | 50VC | J. R. van Wazer and D. A. Campanella, J. Amer. Chem. Soc., 1950, 72, 655 |
| vlm_104104 | 50 | lit_7331 | 71BB | J. T. Bell, R. D. Baybarz, and D. M. Helton, J. Inorg. Nucl. Chem., 1971, 33, 3… |
| vlm_105158 | 311 | lit_9825 | 75VB | J. Volta and M. Bartusek, Coll. Czech. Chem. Comm., 1975, 40, 2050 |
| vlm_161653 | 18 | lit_10585 | 77VBa | J. Votava and M. Bartusek, Coll. Czech. Chem. Comm., 1977, 42, 620 |
| vlm_155355 | 4 | lit_9829 | 75VH | J. Votava, J. Havel, and M. Bartusek, Chem. Zvesti, 1975, 29, 734 |
| vlm_161788 | 78 | lit_9830 | 75VHa | J. Votava, J. Havel, and M. Bartusek, Scr. Fac. Sci. Nat. Univ. Purk. Brun., Ch… |
| vlm_160211 | 127 | lit_7846 | 71ZB | J. Zelinka and M. Bartusek, Coll. Czech. Chem. Comm., 1971, 36, 2615 |
| vlm_161593 | 11 | lit_9395 | 74ZB | J. Zelinka, M. Bartusek, and A. Okac, Coll. Czech. Chem. Comm., 1974, 39, 83 |
| vlm_168118 | 4 | lit_6887 | 70AJ | K. I. Aspila, S. J. Joris, and C. L. Chakrabarti, J. Phys. Chem., 1970, 74, 3625 |
| vlm_112068 | 9 | lit_1717 | 80OSK | K. Ohzeki, M. Saruhashi, and T. Kambara, Bull. Chem. Soc. Japan, 1980, 53, 2548 |
| vlm_144259 | 184 | lit_10370 | 77BMf | L. Barcza and K. Mihalyi, Z. Phys. Chem. N. F. (Frankfurt), 1977, 104, 199, 213 |
| vlm_176419 | 28 | lit_7361 | 71BSa | L. Barcza and L. G. Sillen, Acta Chem. Scand., 1971, 25, 1250 |
| vlm_177572 | 38 | lit_9878 | 76Bc | L. Barcza, J. Phys. Chem., 1976, 80, 821 |
| vlm_128722 | 22 | lit_7363 | 71BSc | L. Barnes and J. M. Sturtevant, Biochem., 1971, 10, 2120 |
| vlm_118645 | 21 | lit_10389 | 77CCb | L. Campanella, E. Chiacchierini, G. De Angelis, and V. Petrone, Ann. Chim. (Rom… |
| vlm_119536 | 4 | lit_7926 | 72CDN | L. Campanella, G. De Angelis, and A. Napoli, Bull. Soc. Chim. Belg., 1972, 81, … |
| vlm_174571 | 63 | lit_12682 | 83CPa | L. Ciavatta and R. Palombari, Gazz. Chim. Ital., 1983, 113, 557 |
| vlm_170604 | 70 | lit_11076 | 79CF | L. Ciavatta, D. Ferri, M. Grimaldi, R. Palombari, and F. Salvatore, J. Inorg. N… |
| vlm_170985 | 87 | lit_9471 | 75CGP | L. Ciavatta, M. Grimaldi, and R. Palombari, J. Inorg. Nucl. Chem., 1975, 37, 16… |
| vlm_172456 | 58 | lit_9927 | 76CGP | L. Ciavatta, M. Grimaldi, and R. Palombari, J. Inorg. Nucl. Chem., 1976, 38, 823 |
| vlm_174467 | 3 | lit_11840 | 81CPB | L. Ciavatta, R. Palombari, and E. Belli, J. Inorg. Nucl. Chem., 1981, 43, 2485 |
| vlm_176992 | 4 | lit_11827 | 81CDP | L. Ciavatta, R. de Capua, and R. Palombari, J. Inorg. Nucl. Chem., 1981, 43, 13… |
| vlm_128851 | 19 | lit_1510 | 77FZ | L. Fabbrizzi and L. J. Zompa, Inorg. Nucl. Chem. Lett., 1977, 13, 287 |
| vlm_126095 | 56 | lit_7997 | 72FBP | L. Fabbrizzi, R. Barbucci, and P. Paoletti, J. Chem. Soc. Dalton, 1972, 1529 |
| vlm_161788 | 22 | lit_6102 | 68HB | L. Havelkova and M. Bartusek, Coll. Czech. Chem. Comm., 1968, 33, 385 |
| vlm_161529 | 76 | lit_6103 | 68HBa | L. Havelkova and M. Bartusek, Coll. Czech. Chem. Comm., 1968, 33, 4188 |
| vlm_161617 | 3 | lit_6521 | 69HB | L. Havelkova and M. Bartusek, Coll. Czech. Chem. Comm., 1969, 34, 2919 |
| vlm_160428 | 45 | lit_6522 | 69HBa | L. Havelkova and M. Bartusek, Coll. Czech. Chem. Comm., 1969, 34, 3722 |
| vlm_108572 | 31 | lit_12770 | 83IE | L. Ilcheva, N. Elenkova, and M. Tabbara, God. Vissh. Khim. Teknol. Inst., Sofia… |
| vlm_124215 | 11 | lit_5442 | 66ZB | L. J. Zampa and R. F. Bogucki, J. Amer. Chem. Soc., 1966, 88, 5186 |
| vlm_128876 | 12 | lit_17151 | 95ZD | L. J. Zompa, H. Diaz, and T. N. Margulis, Inorg. Chim. Acta, 1995, 232, 131 |
| vlm_101387 | 11 | lit_7844 | 71Z | L. J. Zompa, Inorg. Chem., 1971, 10, 2647 |
| vlm_128938 | 33 | lit_11018 | 78Z | L. J. Zompa, Inorg. Chem., 1978, 17, 2531 |
| vlm_180638 | 6 | lit_7307 | 71AGO | L. P. Adamovich, A. P. Gershuns, A. A. Oleinik, and N. M. Shkabara, J. Anal. Ch… |
| vlm_174784 | 1 | lit_7362 | 71BSb | L. P. Barchuk and I. A. Sheka, Russ. J. Inorg. Chem., 1971, 16, 1268 (2378) |
| vlm_160949 | 2 | lit_10582 | 77UB | L. Urbancik and M. Bartusek, Coll. Czech. Chem. Comm., 1977, 42, 446 |
| vlm_124219 | 12 | lit_6438 | 68ZB | L. Y. Zompa and R. F. Bogucki, J. Amer. Chem. Soc., 1968, 91, 4569 |
| vlm_175400 | 65 | lit_14967 | 88SBa | M. A. A. Schoonen and H. L. Barnes, Geochim. Cosmochim. Acta, 1988, 52, 649 |
| vlm_94038 | 18 | lit_13069 | 84ABO | M. A. Abdullah, J. Barrett, and P. O'Brien, J. Chem. Soc. Dalton, 1984, 1647 |
| vlm_170275 | 76 | lit_16561 | 93OB | M. A. Olazabal, G. Borge, R. Castano, N. Etxebarria, and J. M. Madariaga, J. So… |
| vlm_178352 | 4 | lit_2584 | 58AT | M. Anbar and H. Taube, J. Amer. Chem. Soc., 1958, 80, 1073 |
| vlm_163807 | 6 | lit_8938 | 74AN | M. Atchayya, O. G. B. Nambiar, and P. R. Subbaraman, Indian J. Chem., 1974, 12,… |
| vlm_151749 | 2 | lit_8452 | 73BBa | M. Baranowska-Zralko and J. Biernat, Electrochim. Acta, 1973, 17, 1877 |
| vlm_177638 | 32 | lit_12657 | 83BRS | M. Barrera, J. C. Rodriguez Placeres, J. A. Sanchez, and A. Arevalo, An. Quim.,… |
| vlm_151494 | 96 | lit_9434 | 75BDR | M. Barres, J. P. Dubes, R. Romanetti, H. Tachoire, and C. Zahra, Thermochim. Ac… |
| vlm_122282 | 84 | lit_9435 | 75BDT | M. Barres, J. P. Dubes, and H. Tachoire, Compt. Rend. Acad. Sci. Paris, 1975, 2… |
| vlm_151494 | 139 | lit_8485 | 73BRR | M. Barres, J. P. Redoute, R. Romanetti, H. Tachoire, and C. Zahra, Compt. Rend.… |
| vlm_170275 | 83 | lit_5472 | 67Bb | M. Barres, Rev. Chim. Miner., 1967, 4, 803 |
| vlm_129620 | 87 | lit_12211 | 82BBb | M. Bartolini, A. Bianchi, M. Micheloni, and P. Paoletti, J. Chem. Soc. Perkin I… |
| vlm_159874 | 17 | lit_5100 | 66BR | M. Bartusek and J. Ruzickova, Coll. Czech. Chem. Comm., 1966, 31, 207 |
| vlm_172191 | 65 | lit_9459 | 75BSc | M. Bartusek and J. Senkyr, Scr. Fac. Sci. Nat. Univ. Purk. Brun., Chem. 1, 1975… |
| vlm_160249 | 91 | lit_5503 | 67BZ | M. Bartusek and J. Zelinka, Coll. Czech. Chem. Comm., 1967, 32, 992 |
| vlm_164202 | 48 | lit_5485 | 67BHa | M. Bartusek and L. Havelkova, Coll. Czech. Chem. Comm., 1967, 32, 3853 |
| vlm_167063 | 4 | lit_15102 | 89BK | M. Bartusek and L. Kosikova, Scr. Fac. Sci. Nat. Univ. Purk. Brun., 1989, 19, 1… |
| vlm_159859 | 120 | lit_4713 | 65BS | M. Bartusek and L. Sommer, J. Inorg. Nucl. Chem., 1965, 27, 2397 |
| vlm_170604 | 37 | lit_4350 | 64BSa | M. Bartusek and L. Sommer, Z. Phys. Chem. (Leipzig), 1964, 226, 309 |
| vlm_147054 | 34 | lit_13559 | 85BV | M. Bartusek and M. Vichova, Scr. Fac. Sci. Nat. Univ. Purk. Brun., 1985, 15, 485 |
| vlm_161928 | 6 | lit_4714 | 65BSa | M. Bartusek and O. Stankova, Coll. Czech. Chem. Comm., 1965, 30, 3415 |
| vlm_147054 | 123 | lit_12659 | 83BS | M. Bartusek and V. Sustacek, Coll. Czech. Chem. Comm., 1983, 48, 2785 |
| vlm_164245 | 5 | lit_6921 | 70BGS | M. Bartusek, B. Grebenova, and L. Sommer, Spisy Prir. Fak. Univ. Purk. Brne, 19… |
| vlm_162729 | 2 | lit_4681 | 65Bb | M. Bartusek, Coll. Czech. Chem. Comm., 1965, 30, 2746 |
| vlm_160211 | 85 | lit_5470 | 67B | M. Bartusek, Coll. Czech. Chem. Comm., 1967, 32, 116 |
| vlm_160085 | 46 | lit_5471 | 67Ba | M. Bartusek, Coll. Czech. Chem. Comm., 1967, 32, 757 |
| vlm_161617 | 12 | lit_8448 | 73Bb | M. Bartusek, Coll. Czech. Chem. Comm., 1973, 38, 2255 |
| vlm_154695 | 93 | lit_13970 | 86BHM | M. Bartusek, J. Havel, and D. Matula, Coll. Czech. Chem. Comm., 1986, 51, 2702 |
| vlm_164278 | 3 | lit_1262 | 69BBH | M. Bartusek, L. Brchan, and L. Havelkova, Spisy Prir. Fak. Univ. Purk. Brne, 19… |
| vlm_108822 | 4 | lit_14694 | 88B | M. Bartusek, Scr. Fac. Sci. Nat. Univ. Purk. Brun., 1988, 18, 139 |
| vlm_108224 | 104 | lit_6907 | 70Bf | M. Bartusek, Spisy Prir. Fak. Univ. Purk. Brne, 1970, E38, 397 |
| vlm_147708 | 33 | lit_1807 | 53BB | M. Bobtelsky and I. Bar-Gadda, Bull. Soc. Chim. France, 1953, 276, 382, 687 |
| vlm_108427 | 1 | lit_3327 | 61BB | M. Bruno and R. Barbieri, Gazz. Chim. Ital., 1961, 91, 1055 |
| vlm_93606 | 455 | lit_3653 | 62CTC | M. Cefola, A. S. Tompa, A. V. Celiano, and P. S. Gentile, Inorg. Chem., 1962, 1… |
| vlm_125589 | 75 | lit_11535 | 80DS | M. Delfini, A. L. Segre, F. Conti, R. Barbucci, V. Barone, and P. Ferruti, J. C… |
| vlm_172235 | 113 | lit_3742 | 62KH | M. Kodama and K. Hanawa, Ibaraki Daigaku Bunrigakubu Kiyo, Shizen Kagaku, 1962,… |
| vlm_96258 | 55 | lit_8455 | 73BBK | M. L. Barr, E. Baumgartner, and K. Kustin, J. Coord. Chem., 1973, 2, 263 |
| vlm_96385 | 43 | lit_8473 | 73BKL | M. L. Barr, K. Kustin, and S. T. Liu, Inorg. Chem., 1973, 12, 1486 |
| vlm_146138 | 9 | lit_15870 | 91EAW | M. M. Emara, H. M. Abd Elbary, A. M. Wasfi, H. A. Shehata, and M. F. Bakr, J. C… |
| vlm_154395 | 6 | lit_14027 | 86EF | M. M. Emara, N. A. Farid, A. M. Wasfi, M. M. Bahr, and H. M. Abd-Elbary, J. Ind… |
| vlm_160498 | 6 | lit_13161 | 84EF | M. M. Emara, N. A. Farid, A. M. Wasfi, M. M. Bahr, and H. M. Abd-Elbary, J. Phy… |
| vlm_94297 | 43 | lit_11278 | 79MST | M. Machtinger, M. Sloim-Bombard, and B. Tremillon, Anal. Chim. Acta, 1979, 107,… |
| vlm_154888 | 23 | lit_16258 | 92MB | M. Meloun and M. Bartos, Mikrochim. Acta, 1992, 108, 227 |
| vlm_138405 | 15 | lit_14894 | 88MJ | M. Meloun, M. Javurek, and M. Bartos, Analyst, 1988, 113, 1357 |
| vlm_160423 | 10 | lit_10840 | 78MBa | M. Mikesova and M. Bartusek, Chem. Zvesti, 1978, 32, 472 |
| vlm_151809 | 30 | lit_10839 | 78MB | M. Mikesova and M. Bartusek, Coll. Czech. Chem. Comm., 1978, 43, 1867 |

---
