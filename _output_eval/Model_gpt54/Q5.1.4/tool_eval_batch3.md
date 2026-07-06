# Q5.1.4 — Tool Results (batch 3)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Zinc(II)",
  "limit": 10
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_208 | Zn^[2+] | Zn | 2 | ✓ | [Zn+2] | InChI=1S/Zn/q+2 | beta_totN_122 | ligand_totN_1169 | vlm_totN_4095 |

---

### Step 4: `inspect_card`
**Args:**
```json
{
  "prefix_id": "metal_208"
}
```

[summary]
## inspect_card — Metal | metal_208

**Name:** Zn^[2+]  
**Symbol:** Zn | **Charge:** 2  
**SMILES:** `[Zn+2]`  
**InChI:** `InChI=1S/Zn/q+2`  
**Flags:** simple-ion  

**Partners:** 1169 ligand(s), 4095 measurement(s) total

| ligand_id | Ligand | # meas |
|-----------|--------|--------|
| ligand_5760 | Aminoacetic acid (Glycine) | 37 |
| ligand_7029 | Ethylenediamine | 36 |
| ligand_10076 | Hydroxide ion | 33 |
| ligand_10090 | Hydrogen cyanide (Hydrocyanic acid) | 30 |
| ligand_7795 | 1,3-Diazole (Imidazole) | 30 |
| … | *(showing top 5 of 1169)* | |

### Functional groups across all ligand partners (1140 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 523 | 46% |
| aromatic_ring | 478 | 42% |
| hydroxyl | 361 | 32% |
| tertiary_amine | 310 | 27% |
| primary_amine | 282 | 25% |
| secondary_amine | 231 | 20% |
| pyridine | 153 | 13% |
| amide | 143 | 13% |
| ether | 132 | 12% |
| phenol | 97 | 9% |
| thioether | 72 | 6% |
| phosphate | 50 | 4% |
| phosphonate | 48 | 4% |
| sulfonate | 43 | 4% |
| ketone | 37 | 3% |
| halide | 31 | 3% |
| thiol | 30 | 3% |
| imine | 28 | 2% |
| ester | 15 | 1% |
| aldehyde | 9 | 1% |
| thiazole | 8 | 1% |
| nitrile | 6 | 1% |
| oxime | 6 | 1% |
| imidazole | 5 | 0% |
| pyrazole | 5 | 0% |

---

### Step 5: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_stability_measured",
  "group_column": "solvent_name",
  "where": "metal_id = 208",
  "limit": 10
}
```

[TOOL ERROR] db_distribution: Error executing tool db_distribution: no such column: metal_id

---

### Step 6: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_stability_measured",
  "group_column": "temperature_c",
  "where": "metal_id = 208",
  "limit": 10
}
```

[TOOL ERROR] db_distribution: Error executing tool db_distribution: no such column: metal_id

---

### Step 7: `db_ranked_pairs`
**Args:**
```json
{
  "rank_by": "measurement_count",
  "limit": 10,
  "where": "lc.metal_id = 208"
}
```

[summary]
**db_ranked_pairs:** Error - Unknown rank_by='measurement_count'. Choose from: ['ligands_per_metal', 'measurements_per_ligand', 'measurements_per_metal', 'metals_per_ligand', 'pka_per_ligand']

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208)",
  "order_by": "s.solvent_name ASC, s.temperature_c ASC",
  "limit": 200
}
```

[summary]
## search_stability — 200 row(s)

### logK — 100 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_208 | Zn^[2+] | ligand_6329 | 5,5'-Bis[bis(carboxymethyl)… | H6L | CC1=C/C(=C(\c2cc(C)c(O)c(CN(CC(=O)O)CC(=O)O)c2)c2ccccc2C(=O)O)C=C(CN(CC(=O)O)CC(=O)O)C1=O | 6 | 6 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6779 | 4-Hydroxypyridine-2,6-dicar… | H3L | O=C(O)c1cc(O)cc(C(=O)O)n1 | 5 | 5 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5856 | L-2-Amino-3-mercaptopropano… | H2L | N[C@@H](CS)C(=O)O | 4 | 4 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6222 | N-(2-Methoxyethyl)iminodiac… | H2L | COCCN(CC(=O)O)CC(=O)O | 4 | 4 | 20 | 0.1 | *** | 2 |
| metal_208 | Zn^[2+] | ligand_7047 | DL(trans)-Cyclohexane-1,2-d… | L | N[C@@H]1CCCC[C@H]1N | 4 | 4 | 20 | 0.1 | *** | 2 |
| metal_208 | Zn^[2+] | ligand_7048 | meso(cis)-Cyclohexane-1,2-d… | L | N[C@@H]1CCCC[C@@H]1N | 4 | 4 | 20 | 0.1 | *** | 2 |
| metal_208 | Zn^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 3 | 3 | 10 | 0 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_10090 | Hydrogen cyanide (Hydrocyan… | HL | C#N | 3 | 3 | 10 | 0 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5857 | D-2-Amino-3-mercapto-3-meth… | H2L | CC(C)(S)[C@H](N)C(=O)O | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6224 | N-(2-Tetrahydropyranylmethy… | H2L | O=C(O)CN(CC(=O)O)CC1CCCCO1 | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6249 | N-[2-(Methylthio)ethyl]imin… | H2L | CSCCN(CC(=O)O)CC(=O)O | 3 | 3 | 20 | 0.1 | *** | 2 |
| metal_208 | Zn^[2+] | ligand_6315 | Hexamethylenedinitrilotetra… | H4L | O=C(O)CN(CCCCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 3 | 3 | 20 | 0.1 | *** | 2 |
| metal_208 | Zn^[2+] | ligand_6316 | Octamethylenedinitrilotetra… | H4L | O=C(O)CN(CCCCCCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 3 | 3 | 20 | 0.1 | *** | 2 |
| metal_208 | Zn^[2+] | ligand_6320 | trans-1,4-Diaminobut-2-ene-… | H4L | O=C(O)CN(C/C=C/CN(CC(=O)O)CC(=O)O)CC(=O)O | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6321 | 1,4-Diaminobut-2-yne-N,N,N'… | H4L | O=C(O)CN(CC#CCN(CC(=O)O)CC(=O)O)CC(=O)O | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6366 | Triethylenetetranitrilohexa… | H6L | O=C(O)CN(CCN(CCN(CC(=O)O)CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_7049 | DL(trans)-Cycloheptane-1,2-… | L | N[C@@H]1CCCCC[C@H]1N | 2 | 2 | 10 | 0 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6204 | N-(2-Hydroxyethyl)iminodiac… | H2L | O=C(O)CN(CCO)CC(=O)O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5769 | 2-Amino-2-methylpropanoic a… | HL | CC(C)(N)C(=O)O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5773 | 1-Aminocyclopentanecarboxyl… | HL | NC1(C(=O)O)CCCC1 | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5774 | 1-Aminocyclohexanecarboxyli… | HL | NC1(C(=O)O)CCCCC1 | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5775 | 1-Aminocycloheptanecarboxyl… | HL | NC1(C(=O)O)CCCCCC1 | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5909 | DL-2-Amino-3-(5-hydroxy-3-i… | HL | NC(Cc1c[nH]c2ccc(O)cc12)C(=O)O | 2 | 2 | 20 | 0.5 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6149 | N-(3,3-Dimethylbutyl)iminod… | H2L | CC(C)(C)CCN(CC(=O)O)CC(=O)O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6164 | N-(Cyanomethyl)iminodiaceti… | H2L | N#CCN(CC(=O)O)CC(=O)O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6216 | DL-N-(2,3-Dihydroxypropyl)i… | H2L | O=C(O)CN(CC(=O)O)CC(O)CO | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6229 | N-(Carbamylmethyl)iminodiac… | H2L | NC(=O)CN(CC(=O)O)CC(=O)O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6238 | N-(2-Carbamylethyl)iminodia… | H2L | NC(=O)CCN(CC(=O)O)CC(=O)O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6246 | N-[2-(Ethoxyformylamino)eth… | H2L | CCOC(=O)NCCN(CC(=O)O)CC(=O)O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6253 | N-(2-Aminoethyl)iminodiacet… | H2L | NCCN(CC(=O)O)CC(=O)O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6255 | 2-[Bis(carboxymethyl)aminoe… | H2L | C[N+](C)(C)CCN(CC(=O)O)CC(=O)O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6287 | rac-(1,2-Dimethylethylene)d… | H4L | CC(C(C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6288 | meso-(1,2-Dimethylethylene)… | H4L | C[C@H]([C@H](C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6311 | Trimethylenedinitrilotetraa… | H4L | O=C(O)CN(CCCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 2 | 20 | 0.1 | *** | 2 |
| metal_208 | Zn^[2+] | ligand_6313 | Tetramethylenedinitrilotetr… | H4L | O=C(O)CN(CCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 2 | 20 | 0.1 | *** | 2 |
| metal_208 | Zn^[2+] | ligand_6314 | Pentamethylenedinitrilotetr… | H4L | O=C(O)CN(CCCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 2 | 20 | 0.1 | *** | 2 |
| metal_208 | Zn^[2+] | ligand_6337 | Oxybis(trimethylenenitrilo)… | H4L | O=C(O)CN(CCCOCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6342 | Ethylenebis(oxyethylenenitr… | H4L | O=C(O)CN(CCOCCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6763 | 6-Methylpyridine-2-carboxyl… | HL | Cc1cccc(C(=O)O)n1 | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6774 | Pyridine-2,6-dicarboxylic a… | H2L | O=C(O)c1cccc(C(=O)O)n1 | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6780 | 4-Aminopyridine-2,6-dicarbo… | H2L | Nc1cc(C(=O)O)nc(C(=O)O)c1 | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6791 | Pyridine-2,6-diacetic acid | H2L | O=C(O)Cc1cccc(CC(=O)O)n1 | 2 | 2 | 20 | 1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_7046 | Bicyclohexyl-1,1'-diamine | L | NC1(C2(N)CCCCC2)CCCCC1 | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5788 | 3-Aminopropanoic acid (beta… | HL | NCCC(=O)O | 1 | 1 | 15 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_8558 | Chloroacetic acid | HL | O=C(O)CCl | 1 | 1 | 18 | 2 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_8611 | Nitroacetic acid | HL | O=C(O)C[N+](=O)[O-] | 1 | 1 | 18 | 0.5 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5801 | Aminopropanedioic acid (Ami… | H2L | NC(C(=O)O)C(=O)O | 1 | 1 | 20 | 0 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5826 | L-2-Amino-3-(3,4-dihydroxyp… | H3L | NC(Cc1ccc(O)c(O)c1)C(=O)O | 1 | 1 | 20 | 0.5 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5843 | L-2-Aminobutanedioic acid 4… | HL | NC(=O)C[C@H](N)C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5977 | Ethylenediiminodi-2-propano… | H2L | CC(NCCNC(C)C(=O)O)C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5984 | Ethylenediiminodibutanedioi… | H4L | O=C(O)CC(NCCNC(CC(=O)O)C(=O)O)C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_5999 | Ethylenediiminobis(3-hydrox… | H2L | O=C(O)C(CO)NCCNC(CO)C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6000 | Ethylenediiminobis(4-hydrox… | H2L | O=C(O)C(CCO)NCCNC(CCO)C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6022 | DL-N,N-Bis(2-hydroxyethyl)a… | HL | CC(C(=O)O)N(CCO)CCO | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6058 | 1,4-Diazacyclohexane-N,N'-d… | H2L | O=C(O)CN1CCN(CC(=O)O)CC1 | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6152 | N-(Cyclohexyl)iminodiacetic… | H2L | O=C(O)CN(CC(=O)O)C1CCCCC1 | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6172 | DL-2-Methylnitrilotriacetic… | H3L | CC(C(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6173 | DL-2-Ethylnitrilotriacetic … | H3L | CCC(C(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6174 | DL-2-Propylnitrilotriacetic… | H3L | CCCC(C(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6175 | DL-2-(2-Propyl)nitrilotriac… | H3L | CC(C)C(C(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6177 | 2,2-Dimethylnitrilotriaceti… | H3L | CC(C)(C(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6179 | DL-2-Phenylnitrilotriacetic… | H3L | O=C(O)CN(CC(=O)O)C(C(=O)O)c1ccccc1 | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6180 | DL-2-(4-Chlorophenyl)nitril… | H3L | O=C(O)CN(CC(=O)O)C(C(=O)O)c1ccc(Cl)cc1 | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6181 | DL-2-(4-Methylphenyl)nitril… | H3L | Cc1ccc(C(C(=O)O)N(CC(=O)O)CC(=O)O)cc1 | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6182 | DL-2-(4-Methoxyphenyl)nitri… | H3L | COc1ccc(C(C(=O)O)N(CC(=O)O)CC(=O)O)cc1 | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6183 | DL-2-Methyl-2-phenylnitrilo… | H3L | CC(C(=O)O)(c1ccccc1)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6184 | N-(1-Carboxycyclopentyl)imi… | H3L | O=C(O)CN(CC(=O)O)C1(C(=O)O)CCCC1 | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6185 | N-(1-Carboxycyclohexyl)imin… | H3L | O=C(O)CN(CC(=O)O)C1(C(=O)O)CCCCC1 | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6186 | N-(1-Carboxycycloheptyl)imi… | H3L | O=C(O)CN(CC(=O)O)C1(C(=O)O)CCCCCC1 | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6194 | N-(2-Phosphonoethyl)iminodi… | H4L | O=C(O)CN(CCP(=O)(O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6196 | N-(2-Sulfonoethyl)iminodiac… | H2L | O=C(O)CN(CCS(=O)(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6199 | N-(2-Hydroxy-5-nitrobenzyl)… | H3L | O=C(O)CN(CC(=O)O)Cc1cc([N+](=O)[O-])ccc1O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6214 | DL-N-(2-Hydroxyethyl)-2-met… | H2L | CC(C(=O)O)N(CCO)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6248 | N-(2-Mercaptoethyl)iminodia… | H3L | O=C(O)CN(CCS)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6279 | DL-(Ethylethylene)dinitrilo… | H4L | CCC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6280 | DL-(Propylethylene)dinitril… | H4L | CCCC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6281 | DL-(2-Propylethylene)dinitr… | H4L | CC(C)C(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6282 | DL-(Butylethylene)dinitrilo… | H4L | CCCCC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6283 | DL-(2-Methylpropylethylene)… | H4L | CC(C)CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6284 | DL-(Hexylethylene)dinitrilo… | H4L | CCCCCCC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6286 | (1,1-Dimethylethylene)dinit… | H4L | CC(C)(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6289 | DL-(Phenylethylene)dinitril… | H4L | O=C(O)CN(CC(=O)O)CC(c1ccccc1)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6290 | rac-(1,2-Diphenylethylene)d… | H4L | O=C(O)CN(CC(=O)O)C(c1ccccc1)C(c1ccccc1)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6291 | meso-(1,2-Diphenylethylene)… | H4L | O=C(O)CN(CC(=O)O)[C@H](c1ccccc1)[C@H](c1ccccc1)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6292 | DL-Ethylenedinitrilo-N,N'-d… | H4L | CC(C(=O)O)N(CCN(CC(=O)O)C(C)C(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6293 | DL-Ethylenedinitrilo-N,N'-d… | H4L | CCC(C(=O)O)N(CCN(CC(=O)O)C(CC)C(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6294 | DL-Ethylenedinitrilo-N,N'-d… | H4L | CCCC(C(=O)O)N(CCN(CC(=O)O)C(CCC)C(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6295 | DL-Ethylenedinitrilo-N,N'-b… | H4L | CC(C)C(C(=O)O)N(CCN(CC(=O)O)C(C(=O)O)C(C)C)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6319 | rac-(1,3-Dimethyltrimethyle… | H4L | CC(CC(C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6333 | (2-Hydroxytrimethylene)dini… | H4L | O=C(O)CN(CC(=O)O)CC(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6335 | Oxybis(ethylenenitrilo)tetr… | H4L | O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6348 | Thiobis(ethylenenitrilo)tet… | H4L | O=C(O)CN(CCSCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6360 | N'-(2-Allyloxyethyl)diethyl… | H4L | C=CCOCCN(CCN(CCC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6725 | DL-N-(2-Carboxyphenyl)alani… | H2L | CC(Nc1ccccc1C(=O)O)C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6794 | N-(6-Methyl-2-pyridylmethyl… | H2L | Cc1cccc(CN(CC(=O)O)CC(=O)O)n1 | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6882 | 2-(3,4-Dihydroxyphenyl)ethy… | H2L | NCCc1ccc(O)c(O)c1 | 1 | 1 | 20 | 0.5 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6883 | L-2-Amino-1-(3,4-Dihydroxyp… | H2L | NCC(O)c1ccc(O)c(O)c1 | 1 | 1 | 20 | 0.5 | *** | 1 |
| metal_208 | Zn^[2+] | ligand_6884 | Daunorubicin | H2L | COc1cccc2c1C(=O)c1c(O)c3c(c(O)c1C2=O)CC(O)(C(N)=O)CC3OC1CC(N)C(O)C(C)O1 | 1 | 1 | 20 | 0.1 | *** | 1 |

### ΔH — 20 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_208 | Zn^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 3 | 3 | 10 | 0 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_10090 | Hydrogen cyanide (Hydrocyan… | HL | C#N | 3 | 3 | 10 | 0 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_9142 | 1-Hydroxyethane-1,1-diphosp… | H4L | CC(O)(P(=O)(O)O)P(=O)(O)O | 3 | 3 | 15 | 0 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 2 | 2 | 15 | 1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6204 | N-(2-Hydroxyethyl)iminodiac… | H2L | O=C(O)CN(CCO)CC(=O)O | 2 | 2 | 15 | 0 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6140 | N-Methyliminodiacetic acid … | H2L | CN(CC(=O)O)CC(=O)O | 2 | 2 | 20 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 2 | 2 | 20 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6311 | Trimethylenedinitrilotetraa… | H4L | O=C(O)CN(CCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6313 | Tetramethylenedinitrilotetr… | H4L | O=C(O)CN(CCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6314 | Pentamethylenedinitrilotetr… | H4L | O=C(O)CN(CCCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6315 | Hexamethylenedinitrilotetra… | H4L | O=C(O)CN(CCCCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6316 | Octamethylenedinitrilotetra… | H4L | O=C(O)CN(CCCCCCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6335 | Oxybis(ethylenenitrilo)tetr… | H4L | O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6342 | Ethylenebis(oxyethylenenitr… | H4L | O=C(O)CN(CCOCCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6348 | Thiobis(ethylenenitrilo)tet… | H4L | O=C(O)CN(CCSCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6793 | N-(2-Pyridylmethyl)iminodia… | H2L | O=C(O)CN(CC(=O)O)Cc1ccccn1 | 1 | 1 | 20 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6794 | N-(6-Methyl-2-pyridylmethyl… | H2L | Cc1cccc(CN(CC(=O)O)CC(=O)O)n1 | 1 | 1 | 20 | 0.1 | *** | 0 |

### ΔS — 1 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_208 | Zn^[2+] | ligand_6335 | Oxybis(ethylenenitrilo)tetr… | H4L | O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 0 |

---

### Step 9: `db_ranked_pairs`
**Args:**
```json
{
  "rank_by": "ligands_per_metal",
  "limit": 10,
  "where": "lc.metal_id = 208"
}
```

[summary]
## db_ranked_pairs - ligands_per_metal

| metal_id | name | count |
|----------|------|-------|
| metal_208 | Zn^[2+] | 1169 |

---
