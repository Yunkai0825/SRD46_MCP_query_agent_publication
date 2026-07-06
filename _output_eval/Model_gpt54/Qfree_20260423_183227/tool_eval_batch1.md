# Qfree_20260423_183227 — Tool Results (batch 1)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Fe(II), Fe(III), H+",
  "limit": 10
}
```

[summary]
## search_metals

*(no results)*

---

### Step 3: `search_metals`
**Args:**
```json
{
  "name": "iron(II), iron(III), hydrogen",
  "symbol": "Fe, H",
  "limit": 20
}
```

[summary]
## search_metals

*(no results)*

---

### Step 4: `search_metals`
**Args:**
```json
{
  "symbol": "Fe, H",
  "limit": 20
}
```

[summary]
## search_metals

*(no results)*

---

### Step 6: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_name_SRD LIKE '%Fe%' OR c.metal_name_SRD LIKE '%iron%')",
  "order_by": "c.metal_name_SRD ASC, c.ligand_name_SRD ASC",
  "limit": 200
}
```

[summary]
## search_stability — 200 row(s)

### logK — 74 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_62 | Fe^[2+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 11 | 5 | 20~37 | 0.1~3 | *** | 5 |
| metal_62 | Fe^[2+] | ligand_6371 | 1,4-Bis[2,5,5-tris(carboxym… | H6L | O=C(O)CN(CCN(CC(=O)O)Cc1ccc(CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O)cc1)CC(=O)O | 9 | 9 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7673 | 3,7,11,15-Tetraaza-5,13(2)-… | H2L | Cc1cc2c(O)c(c1)CNCc1cccc(n1)CNCc1cc(C)cc(c1O)CNCc1cccc(n1)CNC2 | 7 | 7 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8156 | 2,2'-Bipyridyl | L | c1ccc(-c2ccccn2)nc1 | 6 | 3 | 25~30 | 0~1 | *** | 3 |
| metal_62 | Fe^[2+] | ligand_8191 | 1,10-Phenanthroline (Dipyri… | L | c1cnc2c(c1)ccc1cccnc12 | 5 | 3 | 25 | 0~0.1 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_9083 | (Ethanediylidenetetrathio)t… | H4L | O=C(O)CSC(SCC(=O)O)C(SCC(=O)O)SCC(=O)O | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7645 | 1,13-Dioxa-4,7,10,16,19,22-… | L | C1CNCCOCCNCCNCCNCCOCCNCCN1 | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7771 | 1,2-Diazole (Pyrazole) | L | c1cn[nH]c1 | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_9337 | 1,2-Dihydroxybenzene (Catec… | H2L | Oc1ccccc1O | 4 | 3 | 25 | 0.1~1 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_8176 | 2-(2-Pyridylmethylenehydraz… | L | C(=N/Nc1ccccn1)\c1ccccn1 | 4 | 3 | 20~25 | 0~0.1 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_6109 | 1,4,8,11-Tetraazacyclotetra… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCCN(CC(=O)O)CC1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6760 | 1,4-Diazine-2-carboxylic ac… | HL | O=C(O)c1cnccn1 | 3 | 3 | 25 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_9759 | 2,3-Dimercaptopropanol (BAL) | H2L | OCC(S)CS | 3 | 3 | 30 | 0.1 | solid | 1 |
| metal_62 | Fe^[2+] | ligand_8204 | 2,6-Di(2-pyridyl)pyridine (… | L | c1ccc(-c2cccc(-c3ccccn3)n2)nc1 | 3 | 2 | 25 | 0.1~0.5 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_8071 | 2-(2-Pyridyl)-1,3-thiazole | L | c1ccc(-c2nccs2)nc1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7862 | 2-(2-Pyridyl)imidazole | L | c1ccc(-c2ncc[nH]2)nc1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8341 | 2-Amino-2-propylphosphonic … | H2L | CC(C)(N)P(=O)(O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8192 | 2-Methyl-1,10-phenanthroline | L | Cc1ccc2ccc3cccnc3c2n1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8072 | 4-(2-Pyridyl)-1,3-thiazole | L | c1ccc(-c2cscn2)nc1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7863 | 4-(2-Pyridyl)imidazole | L | c1ccc(-c2c[nH]cn2)nc1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6333 | (2-Hydroxytrimethylene)dini… | H4L | O=C(O)CN(CC(=O)O)CC(O)CN(CC(=O)O)CC(=O)O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_9064 | (Carboxymethoxy)propanedioi… | H3L | O=C(O)COC(C(=O)O)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_9015 | (Ethylenedithio)diacetic ac… | H2L | O=C(O)CSCCSCC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_9467 | 1,2-Dihydroxynaphthalene-4-… | H3L | O=S(=O)(O)c1cc(O)c(O)c2ccccc12 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6751 | 1,2-Phenylenedinitrilotetra… | H4L | O=C(O)CN(CC(=O)O)c1ccccc1N(CC(=O)O)CC(=O)O | 2 | 2 | 25 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7795 | 1,3-Diazole (Imidazole) | L | c1c[nH]cn1 | 2 | 2 | 30 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7530 | 1,4,7,10,13,16,19-Heptaazac… | L | C1CNCCNCCNCCNCCNCCNCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6102 | 1,4,7,10-Tetraazacyclododec… | H4L | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6104 | 1,4,7,10-Tetraazacyclotride… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 2 | 1 | 25 | 0.1~1 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_7212 | 1,4,7-Triazaheptane (Diethy… | L | NCCNCCN | 2 | 2 | 25 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7614 | 1,4-Dioxa-7,10,13-triazacyc… | L | C1CNCCOCCOCCNCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7616 | 1,4-Dioxa-7,10,14-triazacyc… | L | C1CNCCNCCOCCOCCNC1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6068 | 1,4-Dioxa-7,11-diazacyclotr… | H2L | O=C(O)CN1CCCN(CC(=O)O)CCOCCOCC1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_10035 | 1-(4-Sulfobenzo[1,2-d]-2,3-… | HL | NC(=S)N/N=C1\Nc2ccc(S(=O)(=O)O)cc2C1=O | 2 | 2 | 37 | 0.15 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_10036 | 1-(N-Methyl-4-sulfobenzo[1,… | HL | CN1/C(=N\NC(N)=S)C(=O)c2cc(S(=O)(=O)O)ccc21 | 2 | 2 | 37 | 0.15 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6082 | 1-Oxa-4,7,10-triazacyclodod… | H2L | O=C(O)CN1CCNCCN(CC(=O)O)CCOCC1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6084 | 1-Oxa-4,7,10-triazacyclodod… | H3L | O=C(O)CN1CCOCCN(CC(=O)O)CCN(CC(=O)O)CC1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7739 | 1-Thia-4,7-diazacyclononane… | L | C1CNCCSCCN1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8208 | 2,4,6-Tri(2-pyridyl)-1,3,5-… | L | c1ccc(-c2nc(-c3ccccn3)nc(-c3ccccn3)n2)nc1 | 2 | 1 | 22~25 | 0.1~0.5 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_8081 | 2-(Aminomethyl)pyridine (2-… | L | NCc1ccccn1 | 2 | 2 | 30 | 0 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8112 | 2-(Methylaminomethyl)pyridi… | L | CNCc1ccccn1 | 2 | 2 | 30 | 0 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_9946 | 2-Mercapto-4,5,6-trioxoperh… | H3L | O=C1NC(=S)NC(=O)C1=NO | 2 | 1 | 25 | 0.1~0.5 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_9384 | 3,4,5-Trihydroxybenzoic aci… | H4L | O=C(O)c1cc(O)c(O)c(O)c1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7491 | 3,7,11-Triaza-1(2,6)-pyridi… | L | c1cc2nc(c1)CNCCCNCCCNC2 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8217 | 3-Hydrazinobenzo[d]-1,2-dia… | L | NNc1nncc2ccccc12 | 2 | 2 | 37 | 0.15 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6780 | 4-Aminopyridine-2,6-dicarbo… | H2L | Nc1cc(C(=O)O)nc(C(=O)O)c1 | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8196 | 5,6-Dimethyl-1,10-phenanthr… | L | Cc1c(C)c2cccnc2c2ncccc12 | 2 | 2 | 25 | 0~0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_9945 | 1,3-Dimethyl-2,4,5,6-tetrao… | HL | CN1C(=O)C(=NO)C(=O)N(C)C1=O | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6071 | 1,4,10,13-Tetraoxa-7,16-dia… | H2L | O=C(O)CN1CCOCCOCCN(CC(=O)O)CCOCCOCC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6070 | 1,4,10-Trioxa-7,13-diazacyc… | H2L | O=C(O)CN1CCOCCOCCN(CC(=O)O)CCOCC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7500 | 1,4,7,10,13-Pentaazacyclohe… | L | C1CNCCNCCNCCNCCNC1 | 1 | 1 | 35 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6067 | 1,4-Dioxa-7,10-diazacyclodo… | H2L | O=C(O)CN1CCOCCOCCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6069 | 1,7-Dioxa-4,10-diazacyclodo… | H2L | O=C(O)CN1CCOCCN(CC(=O)O)CCOCC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_9943 | 1-Methyl-2,4,5,6-tetraoxope… | H2L | CN1C(=O)NC(=O)/C(=N/O)C1=O | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7618 | 1-Oxa-4,7,10,13-tetraazacyc… | L | C1CNCCNCCOCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7569 | 1-Oxa-4,7-diazacyclononane … | L | C1CNCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6064 | 1-Oxa-4,7-diazacyclononane-… | H2L | O=C(O)CN1CCOCCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7751 | 1-Thia-4,7,10-triazacyclodo… | L | C1CNCCSCCNCCN1 | 1 | 1 | 35 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7755 | 1-Thia-4,7,11,14-tetraazacy… | L | C1CNCCNCCSCCNCCNC1 | 1 | 1 | 35 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_9942 | 2,4,5,6-Tetraoxoperhydro-1,… | H3L | O=C1NC(=O)C(=NO)C(=O)N1 | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5769 | 2-Amino-2-methylpropanoic a… | HL | CC(C)(N)C(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8198 | 2-Chloro-1,10-phenanthroline | L | Clc1ccc2ccc3cccnc3c2n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_9284 | 2-Hydroxy-5-sulfobenzoic ac… | H3L | O=C(O)c1cc(S(=O)(=O)O)ccc1O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8693 | 2-Oxopropanoic acid (Pyruvi… | HL | CC(=O)C(=O)O | 1 | 1 | 25 | 3 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7508 | 3,6,10,13-Tetraaza-1(2,6)-p… | L | c1cc2nc(c1)CNCCNCCCNCCNC2 | 1 | 1 | 35 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7489 | 3,6,9-Triaza-1(2,6)-pyridin… | L | c1cc2nc(c1)CNCCNCCNC2 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5788 | 3-Aminopropanoic acid (beta… | HL | NCCC(=O)O | 1 | 1 | 25 | 1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8216 | 3-Hydrazino-6{2-[3-(1,1-dim… | L | CC(C)(C)NCC(O)COc1ccccc1-c1ccc(NN)nn1 | 1 | 1 | 37 | 0.15 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7490 | 4,7,11-Triaza-1(2,6)-pyrini… | L | c1cc2nc(c1)CNCCNCCCNC2 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_8195 | 4,7-Dimethyl-1,10-phenanthr… | L | Cc1ccnc2c1ccc1c(C)ccnc12 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_7661 | 5-(2-Hydroxyphenyl)-1,4,8,1… | HL | Oc1ccccc1C1CCNCCNCCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |

### ΔH — 10 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_62 | Fe^[2+] | ligand_8176 | 2-(2-Pyridylmethylenehydraz… | L | C(=N/Nc1ccccn1)\c1ccccn1 | 3 | 3 | 25 | 0 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7212 | 1,4,7-Triazaheptane (Diethy… | L | NCCNCCN | 2 | 2 | 25 | 0.1~1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_8156 | 2,2'-Bipyridyl | L | c1ccc(-c2ccccn2)nc1 | 2 | 1 | 20~30 | 0.1~1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_8191 | 1,10-Phenanthroline (Dipyri… | L | c1cnc2c(c1)ccc1cccnc12 | 1 | 1 | 20 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_8204 | 2,6-Di(2-pyridyl)pyridine (… | L | c1ccc(-c2cccc(-c3ccccn3)n2)nc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7862 | 2-(2-Pyridyl)imidazole | L | c1ccc(-c2ncc[nH]2)nc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7863 | 4-(2-Pyridyl)imidazole | L | c1ccc(-c2c[nH]cn2)nc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_8196 | 5,6-Dimethyl-1,10-phenanthr… | L | Cc1c(C)c2cccnc2c2ncccc12 | 1 | 1 | 25 | 0 | *** | 0 |

### ΔS — 10 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_62 | Fe^[2+] | ligand_8176 | 2-(2-Pyridylmethylenehydraz… | L | C(=N/Nc1ccccn1)\c1ccccn1 | 3 | 3 | 25 | 0 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7212 | 1,4,7-Triazaheptane (Diethy… | L | NCCNCCN | 2 | 2 | 25 | 1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_8156 | 2,2'-Bipyridyl | L | c1ccc(-c2ccccn2)nc1 | 2 | 1 | 25 | 0.1~1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_8191 | 1,10-Phenanthroline (Dipyri… | L | c1cnc2c(c1)ccc1cccnc12 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_8204 | 2,6-Di(2-pyridyl)pyridine (… | L | c1ccc(-c2cccc(-c3ccccn3)n2)nc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7862 | 2-(2-Pyridyl)imidazole | L | c1ccc(-c2ncc[nH]2)nc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_7863 | 4-(2-Pyridyl)imidazole | L | c1ccc(-c2c[nH]cn2)nc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_8196 | 5,6-Dimethyl-1,10-phenanthr… | L | Cc1c(C)c2cccnc2c2ncccc12 | 1 | 1 | 25 | 0 | *** | 0 |

---

### Step 7: `db_distribution`
**Args:**
```json
{
  "table": "ligandmetal_card",
  "group_column": "metal_name_SRD",
  "where": "metal_name_SRD LIKE '%Fe%' OR metal_name_SRD LIKE '%iron%'",
  "limit": 50
}
```

[summary]
## db_distribution - ligandmetal_card by metal_name_SRD

**total_rows:** 2140

| value | count | pct |
|-------|-------|-----|
| Fe^[3+] | 1473 | 68.83% |
| Fe^[2+] | 667 | 31.17% |

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_name_SRD = 'Fe^[3+]' AND s.solvent_name LIKE '%water%' AND (s.temperature_c BETWEEN 20 AND 30 OR s.temperature_c IS NULL) AND (s.constant_type LIKE 'log%' OR s.constant_type LIKE '%beta%'))",
  "order_by": "c.ligand_name_SRD ASC, s.constant_value DESC",
  "limit": 200
}
```

[summary]
## search_stability

*(no results)*

---

### Step 9: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_name_SRD = 'Fe^[2+]' AND s.solvent_name LIKE '%water%' AND (s.temperature_c BETWEEN 20 AND 30 OR s.temperature_c IS NULL) AND (s.constant_type LIKE 'log%' OR s.constant_type LIKE '%beta%'))",
  "order_by": "c.ligand_name_SRD ASC, s.constant_value DESC",
  "limit": 200
}
```

[summary]
## search_stability

*(no results)*

---

### Step 10: `search_pka_ligands`
**Args:**
```json
{
  "where": "(lc.ligand_name_SRD LIKE '%citr%' OR lc.ligand_name_SRD LIKE '%pyridine%carbox%' OR lc.ligand_name_SRD LIKE '%iminodiac%' OR lc.ligand_name_SRD LIKE '%nitrilotriac%' OR lc.ligand_name_SRD LIKE '%oxal%' OR lc.ligand_name_SRD LIKE '%malon%' OR lc.ligand_name_SRD LIKE '%tartr%' OR lc.ligand_name_SRD LIKE '%salic%' OR lc.ligand_name_SRD LIKE '%glycin%' OR lc.ligand_name_SRD LIKE '%lact%')",
  "order_by": "lc.ligand_name_SRD ASC, p.pKa ASC",
  "limit": 200
}
```

[summary]
## search_pka_ligands — 200 row(s)

| ligand_id | ligand_name | HxL_def | formula | smiles | pH_ladder | T°C_range | I(M)_range | similarity_score |
|-----------|-------------|---------|---------|--------|-----------|-----------|------------|------------------|
| ligand_5808 | (3-Aminopropyl)malonic acid | H2L | C6H11N1O4 | NCCCC(C(=O)O)C(=O)O | −∞; H3L (M_tot_1); (2.52, vlm_95888); H2L (M_tot_1); (4.86, vlm_95885); HL (M_tot_2); (10.45, vlm_95882); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_6126 | (Carboxymethyl)trimethylammonium (nitrate) (N,N,N,-Trimethy… | HL | C5H12N1O2/+ | C[N+](C)(C)CC(=O)O.O=[N+]([O-])[O-] | −∞; HL (M_tot_1); (-1.7, vlm_104099); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_8906 | 1,3-Diphenylpropane-2,2-dicarboxylic acid (Dibenzylmalonic … | H2L | C17H16O4 | O=C(O)C(Cc1ccccc1)(Cc1ccccc1)C(=O)O | −∞; HL (M_tot_1); (7.75, vlm_153258); L (M_tot_4); +∞ | 25 | 0 | *** |
| ligand_8962 | 1-Oxopropane-1,2-dicarboxylic acid (2-Oxalopropanoic acid) | H2L | C5H6O5 | CC(C(=O)O)C(=O)C(=O)O | −∞; L (M_tot_4); (-13.1, vlm_155300); H-1L (M_tot_1); (-1.7, vlm_155302); HL (M_tot_1); (4.18, vlm_155301); L (M_tot_4); +∞ | 25 | 0.1 | *** |
| ligand_8904 | 1-Phenylpropane-1,1-dicarboxylic acid (Ethylphenylmalonic a… | H2L | C11H12O4 | CCC(C(=O)O)(C(=O)O)c1ccccc1 | −∞; H2L (M_tot_1); (-1.8, vlm_153255); HL (M_tot_1); (7.01, vlm_153254); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6138 | 2,2'-Bis(2-Carboxymethyl)iminodiacetic acid (Iminodisuccini… | H4L | C8H11N1O8 | O=C(O)CC(NC(CC(=O)O)C(=O)O)C(=O)O | −∞; H4L (M_tot_1); (-1.97, vlm_104613); H3L (M_tot_1); (3.24, vlm_104612); H2L (M_tot_1); (4.24, vlm_104611); HL (M_tot_1); (10, vlm_104610); L (M_tot_12); +∞ | 25 | 0.1 | *** |
| ligand_6177 | 2,2-Dimethylnitrilotriacetic acid | H3L | C8H13N1O6 | CC(C)(C(=O)O)N(CC(=O)O)CC(=O)O | −∞; H3L (M_tot_1); (-1.5, vlm_106004); H2L (M_tot_1); (2.52, vlm_106003); HL (M_tot_1); (11.86, vlm_106002); L (M_tot_6); +∞ | 20 | 0.1 | *** |
| ligand_8881 | 2,2-Dimethylpropane-1,1-dicarboxylic acid (t-Butylmalonic a… | H2L | C7H12O4 | CC(C)(C)C(C(=O)O)C(=O)O | −∞; HL (M_tot_1); (7.03, vlm_152747); L (M_tot_7); +∞ | 25 | 0 | *** |
| ligand_8958 | 2,3,4,5-Tetrahydroxyhexanedioic acid (Galactaric acid)(Muci… | H2L | C6H10O8 | O=C(O)C(O)C(O)C(O)C(O)C(=O)O | −∞; H2L (M_tot_1); (3.16, vlm_155191); HL (M_tot_1); (3.86, vlm_155189); L (M_tot_3); +∞ | 25 | 0.1 | *** |
| ligand_8895 | 2,4-Dimethylpentane-3,3-dicarboxylic acid (Di-2-propylmalon… | H2L | C9H16O4 | CC(C)C(C(=O)O)(C(=O)O)C(C)C | −∞; H2L (M_tot_1); (2.07, vlm_153073); HL (M_tot_1); (8.49, vlm_153072); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6717 | 2,5-[Bis(2-hydroxyethyl)amino]benzene-1,4-dicarboxylic acid… | HL | C16H22N2O7 | O=C(O)c1cc2c(cc1N(CCO)CCO)N(CCO)CCOC2=O | −∞; HL (M_tot_1); (6.84, vlm_117680); L (M_tot_4); +∞ | 25 | 0.1 | *** |
| ligand_8020 | 2,6-Dimethylpyridine-4-carboxylic acid ethyl ester | L | C10H13N1O2 | CCOC(=O)c1cc(C)nc(C)c1 | −∞; HL (M_tot_1); (5.27, vlm_136657); L (M_tot_2); +∞ | 25 | 0.5 | *** |
| ligand_9493 | 2-(2-Oxalophenylazo)-1,8-dihydroxynaphthalene-3,6-disulfoni… | H5L | C18H12N2O11S2 | O=CC(=O)c1ccccc1/N=N/c1c(S(=O)(=O)O)cc2cc(S(=O)(=O)O)cc(O)c2c1O | −∞; H3L (M_tot_1); (3.54, vlm_164610); H2L (M_tot_1); (9.96, vlm_164609); HL (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_6724 | 2-(Carboxymethylamino)benzoic acid (N-(2-Carboxyphenyl)glyc… | H2L | C9H9N1O4 | O=C(O)CNc1ccccc1C(=O)O | −∞; H2L (M_tot_1); (3.33, vlm_117728); HL (M_tot_1); (4.9, vlm_117727); L (M_tot_6); +∞ | 25 | 0.1 | *** |
| ligand_5959 | 2-(Carboxymethylaminomethyl)azole-4-sulfonic acid (N-(4-Sul… | H2L | C7H10N2O5S1 | O=C(O)CNCc1cc(S(=O)(=O)O)c[nH]1 | −∞; H2L (M_tot_1); (2.25, vlm_100094); HL (M_tot_1); (8.71, vlm_100093); L (M_tot_2); +∞ | 25 | 1 | *** |
| ligand_8701 | 2-Acetoxybenzoic acid (Acetylsalicylic acid) | HL | C9H8O4 | CC(=O)Oc1ccccc1C(=O)O | −∞; HL (M_tot_1); (3.45, vlm_149911); L (M_tot_4); +∞ | 37 | 0.15 | *** |
| ligand_6189 | 2-Carboxynitrilotriacetic acid | H4L | C7H9N1O8 | O=C(O)CN(CC(=O)O)C(C(=O)O)C(=O)O | −∞; H4L (M_tot_1); (2.93, vlm_106182); H3L (M_tot_1); (3.74, vlm_106181); H2L (M_tot_1); (3.94, vlm_106180); HL (M_tot_1); (8.7, vlm_106179); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_9309 | 2-Hydroxy-3,5-dinitrobenzaldehyde (3,5-Dinitrosalicylaldehy… | HL | C7H4N2O7 | O=Cc1cc([N+](=O)[O-])cc([N+](=O)[O-])c1O | −∞; HL (M_tot_1); (2.09, vlm_161279); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_9283 | 2-Hydroxy-3,5-dinitrobenzoic acid (3,5-Dinitrosalicylic aci… | H2L | C7H4N2O7 | O=C(O)c1cc([N+](=O)[O-])cc([N+](=O)[O-])c1O | −∞; H2L (M_tot_1); (-0.3, vlm_160759); HL (M_tot_11); (7.07, vlm_160754); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_9287 | 2-Hydroxy-3,5-disulfobenzoic acid (3,5-Disulfosalicylic aci… | H4L | C7H6O9S2 | O=C(O)c1cc(S(=O)(=O)O)cc(S(=O)(=O)O)c1O | −∞; HL (M_tot_18); (-11.55, vlm_161059); L (M_tot_1); (2.03, vlm_161063); HL (M_tot_18); +∞ | 25 | 0.1 | *** |
| ligand_9269 | 2-Hydroxy-3-(2-propyl)benzoic acid (3-Isopropylsalicylic ac… | H2L | C10H12O3 | CC(C)c1cccc(C(=O)O)c1O | −∞; H2L (M_tot_1); (2.76, vlm_160616); HL (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_9288 | 2-Hydroxy-3-methoxybenzoic acid (3-Methoxysalicylic acid) | H2L | C8H8O4 | COc1cccc(C(=O)O)c1O | −∞; HL (M_tot_2); (-13.95, vlm_161110); L (M_tot_1); (2.69, vlm_161111); HL (M_tot_2); +∞ | 25 | 0 | *** |
| ligand_9265 | 2-Hydroxy-3-methylbenzoic acid (3-Methylsalicylic acid)(o-C… | H2L | C8H8O3 | Cc1cccc(C(=O)O)c1O | −∞; HL (M_tot_3); (-14.8, vlm_160581); L (M_tot_1); (2.83, vlm_160582); HL (M_tot_3); +∞ | 25 | 0~0.1 | *** |
| ligand_9307 | 2-Hydroxy-3-nitrobenzaldehyde (3-Nitrosalicylaldehyde) | HL | C7H5N1O5 | O=Cc1cccc([N+](=O)[O-])c1O | −∞; HL (M_tot_1); (5.21, vlm_161268); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_9279 | 2-Hydroxy-3-nitrobenzoic acid (3-Nitrosalicylic acid) | H2L | C7H5N1O5 | O=C(O)c1cccc([N+](=O)[O-])c1O | −∞; H2L (M_tot_1); (-1.73, vlm_160687); HL (M_tot_8); (9.87, vlm_160684); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_9266 | 2-Hydroxy-4-methylbenzoic acid (4-Methylsalicylic acid)(m-C… | H2L | C8H8O3 | Cc1ccc(C(=O)O)c(O)c1 | −∞; HL (M_tot_3); (-14.1, vlm_160591); L (M_tot_1); (2.96, vlm_160592); HL (M_tot_3); +∞ | 25 | 0~0.1 | *** |
| ligand_9280 | 2-Hydroxy-4-nitrobenzoic acid (4-Nitrosalicylic acid) | H2L | C7H5N1O5 | O=C(O)c1ccc([N+](=O)[O-])cc1O | −∞; H2L (M_tot_1); (2.05, vlm_160704); HL (M_tot_2); (10.91, vlm_160703); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_9296 | 2-Hydroxy-5-cyanobenzoic acid (5-Cyanosalicylic acid) | H2L | C8H5N1O3 | N#Cc1ccc(O)c(C(=O)O)c1 | −∞; HL (M_tot_2); (-11.3, vlm_161143); L (M_tot_1); (2.36, vlm_161144); HL (M_tot_2); +∞ | 25 | 0 | *** |
| ligand_9278 | 2-Hydroxy-5-iodobenzoic acid (5-Iodosalicylic acid) | H2L | C7H5I1O3 | O=C(O)c1cc(I)ccc1O | −∞; HL (M_tot_4); (-12.4, vlm_160673); L (M_tot_1); (-2.54, vlm_160675); HL (M_tot_4); +∞ | 25 | 0.1 | *** |
| ligand_9289 | 2-Hydroxy-5-methoxybenzoic acid (5-Methoxysalicylic acid) | H2L | C8H8O4 | COc1ccc(O)c(C(=O)O)c1 | −∞; HL (M_tot_2); (-13.85, vlm_161114); L (M_tot_1); (2.92, vlm_161115); HL (M_tot_2); +∞ | 25 | 0 | *** |
| ligand_9267 | 2-Hydroxy-5-methylbenzoic acid (5-Methylsalicylic acid)(p-C… | H2L | C8H8O3 | Cc1ccc(O)c(C(=O)O)c1 | −∞; HL (M_tot_2); (-14.3, vlm_160601); L (M_tot_1); (2.88, vlm_160602); HL (M_tot_2); +∞ | 25 | 0~0.1 | *** |
| ligand_9308 | 2-Hydroxy-5-nitrobenzaldehyde (5-Nitrosalicylaldehyde) | HL | C7H5N1O5 | O=Cc1cc([N+](=O)[O-])ccc1O | −∞; HL (M_tot_1); (5.32, vlm_161273); L (M_tot_6); +∞ | 25 | 0.1 | *** |
| ligand_9281 | 2-Hydroxy-5-nitrobenzoic acid (5-Nitrosalicylic acid) | H2L | C7H5N1O5 | O=C(O)c1cc([N+](=O)[O-])ccc1O | −∞; H2L (M_tot_1); (-1.94, vlm_160717); HL (M_tot_14); (9.9, vlm_160711); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_9310 | 2-Hydroxy-5-sulfobenzaldehyde (5-Sulfosalicylaldehyde) | H2L | C7H6O5S1 | O=Cc1cc(S(=O)(=O)O)ccc1O | −∞; HL (M_tot_1); (6.93, vlm_161284); L (M_tot_3); +∞ | 25 | 0.1 | *** |
| ligand_9336 | 2-Hydroxy-5-sulfobenzaldehyde oxime (5-Sulfosalicylaldoxime) | H2L | C7H7N1O5S1 | O=S(=O)(O)c1ccc(O)c(/C=N/O)c1 | −∞; H2L (M_tot_1); (8.03, vlm_161511); HL (M_tot_2); (11.4, vlm_161506); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_9284 | 2-Hydroxy-5-sulfobenzoic acid (5-Sulfosalicylic acid) | H3L | C7H6O6S1 | O=C(O)c1cc(S(=O)(=O)O)ccc1O | −∞; H2L (M_tot_1); (2.48, vlm_160822); HL (M_tot_37); (11.85, vlm_160810); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_9268 | 2-Hydroxy-6-methylbenzoic acid (6-Methylsalicylic acid) | H2L | C8H8O3 | Cc1cccc(O)c1C(=O)O | −∞; H2L (M_tot_1); (3.16, vlm_160611); HL (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_9282 | 2-Hydroxy-6-nitrobenzoic acid (6-Nitrosalicylic acid) | H2L | C7H5N1O5 | O=C(O)c1c(O)cccc1[N+](=O)[O-] | −∞; H2L (M_tot_1); (1.99, vlm_160751); HL (M_tot_2); (9.04, vlm_160750); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_9300 | 2-Hydroxybenzaldehyde (Salicylaldehyde) | HL | C7H6O3 | O=Cc1ccccc1O | −∞; HL (M_tot_1); (8.14, vlm_161204); L (M_tot_13); +∞ | 25 | 0.1 | *** |
| ligand_9335 | 2-Hydroxybenzaldehyde oxime (Salicylaldoxime) | HL | C7H7N1O2 | O/N=C/c1ccccc1O | −∞; H3L (M_tot_1); (-1.37, vlm_161492); H2L (M_tot_1); (8.95, vlm_161488); HL (M_tot_1); (11.7, vlm_161484); L (M_tot_1); +∞ | 25 | 0~0.1 | *** |
| ligand_9257 | 2-Hydroxybenzoic acid (Salicylic acid) | H2L | C7H6O3 | O=C(O)c1ccccc1O | −∞; HL (M_tot_37); (-13.4, vlm_160211); L (M_tot_3); (2.8, vlm_160226); HL (M_tot_37); +∞ | 25 | 0.1 | *** |
| ligand_8636 | 2-Hydroxybenzoic acid 2-(dihydrogenphosphate) (Salicyl phos… | H4L | C7H7O6P1 | O=C(O)c1ccccc1OP(=O)(O)O | −∞; H2L (M_tot_1); (3.69, vlm_147033); HL (M_tot_1); (6.61, vlm_147030); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_9320 | 2-Hydroxybenzoic acid amide (Salicylamide) | HL | C7H7N1O2 | NC(=O)c1ccccc1O | −∞; HL (M_tot_2); (8.89, vlm_161368); L (M_tot_2); +∞ | 25 | 3 | *** |
| ligand_9317 | 2-Hydroxybenzoic acid methyl ester (Methyl salicylate) | HL | C8H8O3 | COC(=O)c1ccccc1O | −∞; HL (M_tot_1); (9.75, vlm_161358); L (M_tot_3); +∞ | 20 | 0.1 | *** |
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid) | H3L | C6H8O7 | O=C(O)CC(O)(CC(=O)O)C(=O)O | −∞; H3L (M_tot_1); (2.9, vlm_157473); H2L (M_tot_12); (4.35, vlm_157459); HL (M_tot_18); (5.65, vlm_157439); L (M_tot_57); +∞ | 25 | 0.1 | *** |
| ligand_8672 | 2-Hydroxypropane-1,2,3-tricarboxylic acid 1,3-dimethylester… | HL | C8H12O7 | COC(=O)CC(O)(CC(=O)OC)C(=O)O | −∞; HL (M_tot_1); (3.02, vlm_149461); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_8965 | 2-Hydroxypropane-1,2,3-tricarboxylic acid 1-methyl ester (a… | H2L | C7H10O7 | COC(=O)CC(O)(CC(=O)O)C(=O)O | −∞; H2L (M_tot_1); (2.7, vlm_155326); HL (M_tot_1); (4.66, vlm_155324); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_8966 | 2-Hydroxypropane-1,2,3-tricarboxylic acid 2-methyl ester (s… | H2L | C7H10O7 | COC(=O)C(O)(CC(=O)O)CC(=O)O | −∞; H2L (M_tot_1); (3.39, vlm_155330); HL (M_tot_1); (4.63, vlm_155328); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6602 | 2-Methylalanyl-2-methylalanyl-2-methylalanylglycine | HL | C14H26N4O5 | CC(C)(N)C(=O)NC(C)(C)C(=O)NC(C)(C)C(=O)NCC(=O)O | −∞; H2L (M_tot_1); (3.46, vlm_116800); HL (M_tot_1); (8.33, vlm_116799); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_8891 | 2-Methylpentane-3,3-dicarboxylic acid (Ethyl-2-propylmaloni… | H2L | C8H14O4 | CCC(C(=O)O)(C(=O)O)C(C)C | −∞; H2L (M_tot_1); (1.92, vlm_152983); HL (M_tot_1); (7.99, vlm_152982); L (M_tot_1); +∞ | 25 | 0 | *** |
| ligand_8879 | 2-Methylpropane-1,1-dicarboxylic acid (Isopropylmalonic aci… | H2L | C6H10O4 | CC(C)C(C(=O)O)C(=O)O | −∞; H2L (M_tot_1); (2.78, vlm_152713); HL (M_tot_2); (5.5, vlm_152709); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_8698 | 2-Oxobutanedioic acid 4-ethyl ester (4-Ethyl oxaloacetate) | HL | C6H8O5 | CCOC(=O)CC(=O)C(=O)O | −∞; HL (M_tot_1); (9.3, vlm_149904); L (M_tot_3); +∞ | 25 | 0.5 | *** |
| ligand_8885 | 2-Phenylethane-1,1-dicarboxylic acid (Benzylmalonic acid) | H2L | C10H10O4 | O=C(O)C(Cc1ccccc1)C(=O)O | −∞; H2L (M_tot_1); (2.91, vlm_152795); HL (M_tot_1); (5.86, vlm_152791); L (M_tot_9); +∞ | 25 | 0 | *** |
| ligand_8905 | 2-Phenylethene-1,1-dicarboxylic acid (Benzalmalonic acid) | H2L | C10H8O4 | O=C(O)C(=Cc1ccccc1)C(=O)O | −∞; H2L (M_tot_1); (2.11, vlm_153257); HL (M_tot_1); (4.77, vlm_153256); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6254 | 2-[Bis(carboxymethyl)aminomethyl]azole-4-sulfonic acid (N-(… | H2L | C9H12N2O7S1 | O=C(O)CN(CC(=O)O)Cc1cc(S(=O)(=O)O)c[nH]1 | −∞; H3L (M_tot_1); (-1.5, vlm_107703); H2L (M_tot_1); (2.3, vlm_107702); HL (M_tot_1); (8.3, vlm_107701); L (M_tot_2); +∞ | 25 | 1 | *** |
| ligand_9285 | 3-Bromo-2-hydroxy-5-sulfobenzoic acid (3-Bromo-5-sulfosalic… | H3L | C7H5Br1O6S1 | O=C(O)c1cc(S(=O)(=O)O)cc(Br)c1O | −∞; H2L (M_tot_1); (2.02, vlm_160958); HL (M_tot_15); (10.52, vlm_160956); L (M_tot_16); +∞ | 25 | 0.1 | *** |
| ligand_9303 | 3-Chloro-2-hydroxybenzaldehyde (3-Chlorosalicylaldehyde) | HL | C7H5Cl1O3 | O=Cc1cccc(Cl)c1O | −∞; HL (M_tot_1); (6.61, vlm_161247); L (M_tot_6); +∞ | 25 | 0.1 | *** |
| ligand_7969 | 3-Hydroxy-2,5-dimethylpyridine-4-carboxaldehyde (Deoxypyrid… | HL | C8H9N1O2 | Cc1cnc(C)c(O)c1C=O | −∞; H2L (M_tot_1); (4.06, vlm_136209); HL (M_tot_1); (7.98, vlm_136205); L (M_tot_6); +∞ | 25 | 0.1 | *** |
| ligand_7972 | 3-Hydroxy-2-methyl-5-(2-carboxyethyl)pyridine-4-carboxaldeh… | HL | C10H11N1O5 | Cc1ncc(CCC(=O)O)c(C=O)c1O | −∞; H3L (M_tot_1); (3.34, vlm_136245); H2L (M_tot_1); (4.45, vlm_136244); HL (M_tot_1); (8.11, vlm_136243); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_7975 | 3-Hydroxy-2-methyl-5-(2-sulfonoethyl)pyridine-4-carboxaldeh… | HL | C9H11N1O5S1 | Cc1ncc(CCS(=O)(=O)O)c(C=O)c1O | −∞; H2L (M_tot_1); (3.37, vlm_136252); HL (M_tot_1); (7.47, vlm_136251); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_7974 | 3-Hydroxy-4-hydroxymethyl-2-methyl-5-(2-carboxyethyl)pyridi… | HL | C10H11N1O5 | Cc1ncc(CCC(=O)O)c(CO)c1O | −∞; H2L (M_tot_1); (4.83, vlm_136250); HL (M_tot_1); (8.75, vlm_136249); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_7970 | 3-Hydroxy-5-hydroxymethyl-2-methylpyridine-4-carboxaldehyde… | HL | C8H9N1O3 | Cc1ncc(CO)c(C=O)c1O | −∞; L (M_tot_6); (-12.9, vlm_136223); H-1L (M_tot_1); (4.1, vlm_136229); HL (M_tot_1); (8.53, vlm_136226); L (M_tot_6); +∞ | 25 | 0.1 | *** |
| ligand_7968 | 3-Hydroxy-N,2,5-trimethyl-4-oxomethylpyridinium (chloride) … | HL | C9H12N1O2+ | Cc1c[n+](C)c(C)c(O)c1C=O | −∞; L (M_tot_1); (-13.1, vlm_136203); H-1L (M_tot_1); (4.34, vlm_136204); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_7966 | 3-Hydroxypyridine-2-carboxaldehyde | HL | C6H7N1O2 | O=Cc1ncccc1O | −∞; H2L (M_tot_1); (3.4, vlm_136198); HL (M_tot_1); (6.95, vlm_136197); L (M_tot_1); +∞ | 20 | 0.1 | *** |
| ligand_7967 | 3-Hydroxypyridine-4-carboxaldehyde | HL | C6H7N1O2 | O=Cc1ccncc1O | −∞; H2L (M_tot_1); (4.04, vlm_136201); HL (M_tot_1); (6.7, vlm_136199); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_7964 | 3-Methoxypyridine-2-carboxaldehyde | HL | C7H9N1O2 | COc1cccnc1C=O | −∞; L (M_tot_1); (-12.95, vlm_136193); H-1L (M_tot_1); (2.89, vlm_136194); L (M_tot_1); +∞ | 20 | 0.1 | *** |
| ligand_7965 | 3-Methoxypyridine-4-carboxaldehyde | HL | C7H9N1O2 | COc1cnccc1C=O | −∞; L (M_tot_1); (-11.7, vlm_136195); H-1L (M_tot_1); (4.45, vlm_136196); L (M_tot_1); +∞ | 20 | 0.1 | *** |
| ligand_8880 | 3-Methylbutane-1,1-dicarboxylic acid (Isobutylmalonic acid) | H2L | C7H12O4 | CC(C)CC(C(=O)O)C(=O)O | −∞; H2L (M_tot_1); (2.87, vlm_152733); HL (M_tot_2); (5.36, vlm_152730); L (M_tot_3); +∞ | 25 | 0.1 | *** |
| ligand_6782 | 4-(Dimethylamino)pyridine-2,6-dicarboxylic acid | H2L | C9H10N2O4 | CN(C)c1cc(C(=O)O)nc(C(=O)O)c1 | −∞; H2L (M_tot_1); (-1.5, vlm_119634); HL (M_tot_1); (9.77, vlm_119633); L (M_tot_5); +∞ | 22 | 0.1 | *** |
| ligand_6781 | 4-(Methylamino)pyridine-2,6-dicarboxylic acid | H2L | C8H8N2O4 | CNc1cc(C(=O)O)nc(C(=O)O)c1 | −∞; H2L (M_tot_1); (-1.3, vlm_119628); HL (M_tot_1); (9.68, vlm_119627); L (M_tot_5); +∞ | 22 | 0.1 | *** |
| ligand_6783 | 4-(Phenylamino)pyridine-2,6-dicarboxylic acid | H2L | C13H10N2O4 | O=C(O)c1cc(Nc2ccccc2)cc(C(=O)O)n1 | −∞; H2L (M_tot_1); (-1.4, vlm_119640); HL (M_tot_1); (8.65, vlm_119639); L (M_tot_4); +∞ | 22 | 0.1 | *** |
| ligand_9297 | 4-Amino-2-hydroxybenzoic acid (p-Aminosalicylic acid) | H2L | C7H7N1O3 | Nc1ccc(C(=O)O)c(O)c1 | −∞; H3L (M_tot_1); (-1.8, vlm_161157); H2L (M_tot_1); (3.63, vlm_161151); HL (M_tot_4); +∞ | 25 | 0.1 | *** |
| ligand_9322 | 4-Amino-2-hydroxybenzoic acid amide (4-Aminosalicylamide) | HL | C7H8N2O2 | NC(=O)c1ccc(N)cc1O | −∞; H2L (M_tot_1); (3, vlm_161383); HL (M_tot_2); (9.11, vlm_161380); L (M_tot_2); +∞ | 25 | 3 | *** |
| ligand_6780 | 4-Aminopyridine-2,6-dicarboxylic acid | H2L | C7H6N2O4 | Nc1cc(C(=O)O)nc(C(=O)O)c1 | −∞; H2L (M_tot_1); (2.29, vlm_119601); HL (M_tot_1); (9.05, vlm_119600); L (M_tot_15); +∞ | 20 | 0.1 | *** |
| ligand_9304 | 4-Chloro-2-hydroxybenzaldehyde (4-Chlorosalicylaldehyde) | HL | C7H5Cl1O3 | O=Cc1ccc(Cl)cc1O | −∞; HL (M_tot_1); (7.18, vlm_161253); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_6777 | 4-Chloropyridine-2,6-dicarboxylic acid | H2L | C7H4Cl1N1O4 | O=C(O)c1cc(Cl)cc(C(=O)O)n1 | −∞; H2L (M_tot_1); (-1.7, vlm_119557); HL (M_tot_1); (3.75, vlm_119556); L (M_tot_5); +∞ | 22 | 0.1 | *** |
| ligand_6779 | 4-Hydroxypyridine-2,6-dicarboxylic acid (Chelidamic acid) | H3L | C7H5N1O5 | O=C(O)c1cc(O)cc(C(=O)O)n1 | −∞; H3L (M_tot_1); (-1.4, vlm_119568); H2L (M_tot_1); (3.11, vlm_119567); HL (M_tot_1); (10.88, vlm_119566); L (M_tot_10); +∞ | 20 | 0.1 | *** |
| ligand_8894 | 4-Methylhexane-3,3-dicarboxylic acid (s-Butylethylmalonic a… | H2L | C9H16O4 | CCC(C)C(CC)(C(=O)O)C(=O)O | −∞; HL (M_tot_1); (8.4, vlm_153056); L (M_tot_6); +∞ | 25 | 0 | *** |
| ligand_9298 | 5-Amino-2-hydroxybenzoic acid (m-Aminosalicylic acid) | H2L | C7H7N1O3 | Nc1ccc(O)c(C(=O)O)c1 | −∞; HL (M_tot_4); (-11.54, vlm_161185); L (M_tot_3); (-5.6, vlm_161187); HL (M_tot_4); (2.28, vlm_161189); H2L (M_tot_1); +∞ | 25 | 0.5 | *** |
| ligand_9277 | 5-Bromo-2-hydroxybenzoic acid (5-Bromosalicylic acid) | H2L | C7H5Br1O3 | O=C(O)c1cc(Br)ccc1O | −∞; HL (M_tot_4); (-12.5, vlm_160658); L (M_tot_1); (2.44, vlm_160660); HL (M_tot_4); +∞ | 25 | 0.1 | *** |
| ligand_8670 | 5-Carboxy-D-galactopyranose (D-Galacturonic acid) | HL | C6H10O7 | O=C(O)[C@H]1O[C@H](O)[C@H](O)[C@@H](O)[C@H]1O | −∞; HL (M_tot_1); (3.2, vlm_149404); L (M_tot_7); +∞ | 25 | 0.1 | *** |
| ligand_9305 | 5-Chloro-2-hydroxybenzaldehyde (5-Chlorosalicylaldehyde) | HL | C7H5Cl1O3 | O=Cc1cc(Cl)ccc1O | −∞; HL (M_tot_1); (7.41, vlm_161258); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_9275 | 5-Chloro-2-hydroxybenzoic acid (5-Chlorosalicylic acid) | H2L | C7H5Cl1O3 | O=C(O)c1cc(Cl)ccc1O | −∞; HL (M_tot_7); (-12.7, vlm_160634); L (M_tot_1); (2.46, vlm_160636); HL (M_tot_7); +∞ | 25 | 0.1 | *** |
| ligand_9274 | 5-Fluoro-2-hydroxybenzoic acid (5-Fluorosalicylic acid) | H2L | C7H5F1O3 | O=C(O)c1cc(F)ccc1O | −∞; HL (M_tot_2); (-13.7, vlm_160630); L (M_tot_1); (2.56, vlm_160631); HL (M_tot_2); +∞ | 25 | 0 | *** |
| ligand_8257 | 5-Hydroxybenzo[b]-1,4-diazine (5-Hydroxyquinoxaline) | HL | C10H6N2O1 | Oc1cccc2nccnc12 | −∞; H2L (M_tot_1); (-0.8, vlm_140468); HL (M_tot_1); (8.75, vlm_140466); L (M_tot_1); +∞ | 25 | 0 | *** |
| ligand_7971 | 5-Hydroxymethyl-2-methyl-3-methoxypyridine-4-carboxaldehyde… | L | C9H11N1O3 | COc1c(C)ncc(CO)c1C=O | −∞; HL (M_tot_1); (4.64, vlm_136242); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_9306 | 6-Chloro-2-hydroxybenzaldehyde (6-Chlorosalicylaldehyde) | HL | C7H5Cl1O3 | O=Cc1c(O)cccc1Cl | −∞; HL (M_tot_1); (8.26, vlm_161263); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_9276 | 6-Chloro-2-hydroxybenzoic acid (6-Chlorosalicylic acid) | H2L | C7H5Cl1O3 | O=C(O)c1c(O)cccc1Cl | −∞; H2L (M_tot_1); (2.63, vlm_160657); HL (M_tot_1); +∞ | 25 | 0 | *** |
| ligand_8896 | 6-Methylheptane-3,3-dicarboxylic acid (Ethylisopentylmaloni… | H2L | C10H18O4 | CCC(CCC(C)C)(C(=O)O)C(=O)O | −∞; H2L (M_tot_1); (2.04, vlm_153075); HL (M_tot_1); (7.2, vlm_153074); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_8049 | 6-Methylpyridine-2-carboxaldehyde oxime | HL | C7H8N2O1 | Cc1cccc(/C=N/O)n1 | −∞; H2L (M_tot_1); (4.26, vlm_136925); HL (M_tot_2); (9.94, vlm_136924); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_6763 | 6-Methylpyridine-2-carboxylic acid | HL | C7H7N1O2 | Cc1cccc(C(=O)O)n1 | −∞; H2L (M_tot_1); (-1.2, vlm_118974); HL (M_tot_1); (5.86, vlm_118972); L (M_tot_15); +∞ | 25 | 0.1 | *** |
| ligand_5760 | Aminoacetic acid (Glycine) | HL | C2H5N1O2 | NCC(=O)O | −∞; H2L (M_tot_1); (2.33, vlm_93627); HL (M_tot_20); (9.57, vlm_93606); L (M_tot_43); +∞ | 25 | 0.1 | *** |
| ligand_6982 | Aminoacetohydroxamic acid (Glycinehydroxamic acid) | HL | C2H6N2O2 | NCC(=O)NO | −∞; H2L (M_tot_1); (7.45, vlm_121429); HL (M_tot_2); (9.18, vlm_121426); L (M_tot_9); +∞ | 25 | 0.1 | *** |
| ligand_5801 | Aminopropanedioic acid (Aminomalonic acid) | H2L | C3H5N1O4 | NC(C(=O)O)C(=O)O | −∞; H3L (M_tot_1); (-1.8, vlm_95531); H2L (M_tot_1); (2.94, vlm_95527); HL (M_tot_1); (9.22, vlm_95523); L (M_tot_4); +∞ | 25 | 0.1 | *** |
| ligand_8882 | But-3-ene-1,1-dicarboxylic acid (Allylmalonic acid) | H2L | C6H8O4 | C=CCC(C(=O)O)C(=O)O | −∞; H2L (M_tot_1); (2.63, vlm_152767); HL (M_tot_1); (5.24, vlm_152766); L (M_tot_7); +∞ | 25 | 0.1 | *** |
| ligand_8876 | Butane-1,1-dicarboxylic acid (Propylmalonic acid) | H2L | C6H10O4 | CCCC(C(=O)O)C(=O)O | −∞; H2L (M_tot_1); (2.84, vlm_152577); HL (M_tot_2); (5.45, vlm_152573); L (M_tot_15); +∞ | 25 | 0.1 | *** |
| ligand_8888 | Butane-2,2-dicarboxylic acid (Ethylmethylmalonic acid) | H2L | C6H10O4 | CCC(C)(C(=O)O)C(=O)O | −∞; H2L (M_tot_1); (2.86, vlm_152908); HL (M_tot_1); (6.41, vlm_152907); L (M_tot_1); +∞ | 25 | 0 | *** |
| ligand_8641 | D-2-Hydroxypropanoic acid (Lactic acid) | HL | C3H6O3 | CC(O)C(=O)O | −∞; HL (M_tot_3); (3.67, vlm_147468); L (M_tot_45); +∞ | 25 | 0.1 | *** |
| ligand_6906 | D-Galactosamine | L | C6H13N1O5 | N[C@@H]1[C@@H](O)[C@@H](O)[C@@H](CO)O[C@@H]1O | −∞; HL (M_tot_1); (7.72, vlm_121085); L (M_tot_3); +∞ | 25 | 0.1 | *** |
| ligand_6555 | D-Leucyl-L-leucylglycine | HL | C14H27N3O4 | CC(C)C[C@@H](N)C(=O)N[C@@H](CC(C)C)C(=O)NCC(=O)O | −∞; H2L (M_tot_1); (3.33, vlm_116206); HL (M_tot_1); (7.87, vlm_116205); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_9655 | D-galacto-Hexose (alpha-D(+)-Galactose) | *** | C6H12O6 | *** | −∞; L (M_tot_4); (-12.35, vlm_167303); H-1L (M_tot_1); +∞ | 25 | 0 | *** |
| ligand_8784 | DL-(2,3-Dimercaptopropionyl)glycine | H3L | C5H9N1O3S2 | O=C(O)CNC(=O)C(S)CS | −∞; H3L (M_tot_1); (3.63, vlm_150900); H2L (M_tot_1); (7.63, vlm_150899); HL (M_tot_1); (10.66, vlm_150898); L (M_tot_3); +∞ | 20 | 0.1 | *** |
| ligand_8781 | DL-(2-Mercapto-2-phenylacetyl)glycine | H2L | C10H10N1O3S1 | O=C(O)CNC(=O)C(S)c1ccccc1 | −∞; H2L (M_tot_1); (3.2, vlm_150888); HL (M_tot_1); (7.8, vlm_150887); L (M_tot_1); +∞ | 20 | 0.1 | *** |
| ligand_8779 | DL-(2-Mercapto-3-methylbutanonyl)glycine | H2L | C7H13N1O3S1 | CC(C)C(S)C(=O)NCC(=O)O | −∞; H2L (M_tot_1); (3.77, vlm_150884); HL (M_tot_1); (9.07, vlm_150883); L (M_tot_1); +∞ | 20 | 0.1 | *** |
| ligand_8782 | DL-(2-Mercapto-3-phenylpropionyl)glycine | H2L | C11H12N1O3S1 | O=C(O)CNC(=O)C(S)Cc1ccccc1 | −∞; H2L (M_tot_1); (3.47, vlm_150890); HL (M_tot_1); (8.41, vlm_150889); L (M_tot_1); +∞ | 20 | 0.1 | *** |
| ligand_8775 | DL-(2-Mercaptopropionyl)glycine | H2L | C5H9N1O3S1 | CC(S)C(=O)NCC(=O)O | −∞; H2L (M_tot_1); (3.4, vlm_150847); HL (M_tot_1); (8.37, vlm_150843); L (M_tot_6); +∞ | 25 | 0.1 | *** |

---

### Step 11: `search_ligands`
**Args:**
```json
{
  "name": "citric acid, lactic acid, glycine, salicylic acid, iminodisuccinic acid, nitrilotriacetic acid, chelidamic acid",
  "limit": 20
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 12: `search_stability`
**Args:**
```json
{
  "where": "((c.metal_name_SRD = 'Fe^[3+]' OR c.metal_name_SRD = 'Fe^[2+]') AND (c.ligand_name_SRD LIKE '%citric acid%' OR c.ligand_name_SRD LIKE '%lactic acid%' OR c.ligand_name_SRD LIKE '%glycine%' OR c.ligand_name_SRD LIKE '%salicylic acid%' OR c.ligand_name_SRD LIKE '%iminodisuccinic%' OR c.ligand_name_SRD LIKE '%nitrilotriacetic%' OR c.ligand_name_SRD LIKE '%chelidamic%'))",
  "order_by": "c.ligand_name_SRD ASC, c.metal_name_SRD ASC, s.constant_value DESC",
  "limit": 300
}
```

[summary]
## search_stability — 200 row(s)

### logK — 42 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 11 | 3 | 20~25 | 0~3 | *** | 7 |
| metal_62 | Fe^[2+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 11 | 5 | 20~37 | 0.1~3 | *** | 5 |
| metal_61 | Fe^[3+] | ligand_9297 | 4-Amino-2-hydroxybenzoic ac… | H2L | Nc1ccc(C(=O)O)c(O)c1 | 11 | 4 | 20~25 | 0.1~3 | *** | 4 |
| metal_61 | Fe^[3+] | ligand_7000 | Glycylglycylglycinehydroxam… | HL | NCC(=O)NCC(=O)NCC(=O)NO | 11 | 11 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 10 | 3 | 10~40 | 0~3 | *** | 7 |
| metal_61 | Fe^[3+] | ligand_6982 | Aminoacetohydroxamic acid (… | HL | NCC(=O)NO | 9 | 8 | 20~25 | 0.1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_9284 | 2-Hydroxy-5-sulfobenzoic ac… | H3L | O=C(O)c1cc(S(=O)(=O)O)ccc1O | 7 | 3 | 20~25 | 0.1~3 | *** | 4 |
| metal_61 | Fe^[3+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 7 | 5 | 25 | 0.1~1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 6 | 4 | 20~25 | 0.1~1 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 6 | 3 | 25 | 0.5~3 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_6999 | Glycylglycinehydroxamic acid | HL | NCC(=O)NCC(=O)NO | 6 | 6 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_7002 | L-Prolyl-L-leucylglycinehyd… | HL | CC(C)C[C@H](NC(=O)[C@@H]1CCCN1)C(=O)NCC(=O)NO | 6 | 6 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9265 | 2-Hydroxy-3-methylbenzoic a… | H2L | Cc1cccc(C(=O)O)c1O | 5 | 4 | 25 | 0~0.1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_9275 | 5-Chloro-2-hydroxybenzoic a… | H2L | O=C(O)c1cc(Cl)ccc1O | 5 | 3 | 25 | 0~1 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_6047 | N,N''-Bis(3-hydroxy-6-methy… | H5L | Cc1ccc(O)c(CN(CCN(CCN(CC(=O)O)Cc2nc(C)ccc2O)CC(=O)O)CC(=O)O)n1 | 5 | 5 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9266 | 2-Hydroxy-4-methylbenzoic a… | H2L | Cc1ccc(C(=O)O)c(O)c1 | 4 | 3 | 20~25 | 0.1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_9277 | 5-Bromo-2-hydroxybenzoic ac… | H2L | O=C(O)c1cc(Br)ccc1O | 4 | 3 | 25 | 0~0.1 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_6188 | DL-2-(2-Methylthioethyl)nit… | H3L | CSCCC(C(=O)O)N(CC(=O)O)CC(=O)O | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9292 | N-(2-Hydroxybenzoyl)glycine… | H2L | O=C(O)CNC(=O)c1ccccc1O | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9278 | 2-Hydroxy-5-iodobenzoic aci… | H2L | O=C(O)c1cc(I)ccc1O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9267 | 2-Hydroxy-5-methylbenzoic a… | H2L | Cc1ccc(O)c(C(=O)O)c1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9281 | 2-Hydroxy-5-nitrobenzoic ac… | H2L | O=C(O)c1cc([N+](=O)[O-])ccc1O | 3 | 1 | 25~30 | 0~1 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_9268 | 2-Hydroxy-6-methylbenzoic a… | H2L | Cc1cccc(O)c1C(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6188 | DL-2-(2-Methylthioethyl)nit… | H3L | CSCCC(C(=O)O)N(CC(=O)O)CC(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6239 | N,N-Bis(carboxymethyl)glycy… | H3L | O=C(O)CNC(=O)CN(CC(=O)O)CC(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6019 | N,N-Bis(phosphonomethyl)gly… | H5L | O=C(O)CN(CP(=O)(O)O)CP(=O)(O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_5937 | N-(Phosphonomethyl)glycine … | H3L | O=C(O)CNCP(=O)(O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9283 | 2-Hydroxy-3,5-dinitrobenzoi… | H2L | O=C(O)c1cc([N+](=O)[O-])cc([N+](=O)[O-])c1O | 2 | 1 | 25~30 | 0.1~1 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_9279 | 2-Hydroxy-3-nitrobenzoic ac… | H2L | O=C(O)c1cccc([N+](=O)[O-])c1O | 2 | 1 | 25~30 | 0~0.1 | *** | 2 |
| metal_62 | Fe^[2+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6021 | N,N-Bis(2-hydroxyethyl)glyc… | HL | O=C(O)CN(CCO)CCO | 2 | 2 | 30 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6021 | N,N-Bis(2-hydroxyethyl)glyc… | HL | O=C(O)CN(CCO)CCO | 2 | 2 | 20~25 | 0.1~0.5 | *** | 2 |
| metal_61 | Fe^[3+] | ligand_6240 | N,N-Bis(carboxymethyl)glycy… | H3L | O=C(O)CNC(=O)CNC(=O)CN(CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6241 | N,N-Bis(carboxymethyl)glycy… | H3L | O=C(O)CNC(=O)CNC(=O)CNC(=O)CN(CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6276 | N-(2-Hydroxybenzyl)ethylene… | H4L | O=C(O)CN(CCN(CC(=O)O)Cc1ccccc1O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9269 | 2-Hydroxy-3-(2-propyl)benzo… | H2L | CC(C)c1cccc(C(=O)O)c1O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_9284 | 2-Hydroxy-5-sulfobenzoic ac… | H3L | O=C(O)c1cc(S(=O)(=O)O)ccc1O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_9298 | 5-Amino-2-hydroxybenzoic ac… | H2L | Nc1ccc(O)c(C(=O)O)c1 | 1 | 1 | 37 | 0.15 | *** | 1 |
| metal_62 | Fe^[2+] | ligand_6372 | Glycylglycine (Diglycine) | HL | NCC(=O)NCC(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6372 | Glycylglycine (Diglycine) | HL | NCC(=O)NCC(=O)O | 1 | 1 | 20 | 1 | *** | 1 |
| metal_61 | Fe^[3+] | ligand_6195 | N-(2-Carboxyethyl)-N-(phosp… | H4L | O=C(O)CCN(CC(=O)O)CP(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 1 |

### ΔH — 7 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 3 | 1 | 10~40 | 0 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 1 | 25 | 1~3 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9284 | 2-Hydroxy-5-sulfobenzoic ac… | H3L | O=C(O)c1cc(S(=O)(=O)O)ccc1O | 1 | 1 | 25 | 3 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9297 | 4-Amino-2-hydroxybenzoic ac… | H2L | Nc1ccc(C(=O)O)c(O)c1 | 1 | 1 | 25 | 1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |

### ΔS — 7 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_61 | Fe^[3+] | ligand_9257 | 2-Hydroxybenzoic acid (Sali… | H2L | O=C(O)c1ccccc1O | 2 | 1 | 25 | 1~3 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9284 | 2-Hydroxy-5-sulfobenzoic ac… | H3L | O=C(O)c1cc(S(=O)(=O)O)ccc1O | 1 | 1 | 25 | 3 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9058 | 2-Hydroxypropane-1,2,3-tric… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_9297 | 4-Amino-2-hydroxybenzoic ac… | H2L | Nc1ccc(C(=O)O)c(O)c1 | 1 | 1 | 25 | 1 | *** | 0 |
| metal_62 | Fe^[2+] | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |

---

### Step 13: `search_stability`
**Args:**
```json
{
  "where": "((c.metal_name_SRD = 'Fe^[3+]' OR c.metal_name_SRD = 'Fe^[2+]') AND c.ligand_id IN (ligand_9058, ligand_5760, ligand_9257, ligand_9284, ligand_6275, ligand_6021, ligand_6372) AND s.constant_type = 'logK' AND (s.temperature_c BETWEEN 20 AND 30 OR s.temperature_c IS NULL) AND (s.ionic_strength_mol_l BETWEEN 0.05 AND 1.0 OR s.ionic_strength_mol_l IS NULL) AND s.solvent_name LIKE '%water%')",
  "order_by": "c.ligand_id ASC, c.metal_name_SRD ASC, s.ionic_strength_mol_l ASC, s.constant_value DESC",
  "limit": 300
}
```

[summary]
## search_stability

*(no results)*

---

### Step 14: `search_pka_values`
**Args:**
```json
{
  "where": "(lc.ligand_id IN (ligand_9058, ligand_5760, ligand_9257, ligand_9284, ligand_6275, ligand_6021, ligand_6372))",
  "order_by": "lc.ligand_name_SRD ASC, p.pKa ASC",
  "limit": 200
}
```

[summary]
## search_pka_values — 16 row(s)

### pKa -13.5–-13.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_160211 | ligand_9257 | 2-Hydroxybenzoic acid (Salicylic a… | H2L | O=C(O)c1ccccc1O | -13.4 | 25 | 0.1 | L→HL | M_tot_37 | M_tot_3 |

### pKa -2.0–-1.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_101550 | ligand_6021 | N,N-Bis(2-hydroxyethyl)glycine (Bi… | HL | O=C(O)CN(CCO)CCO | -1.7 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_2 |

### pKa 2.0–2.5 (2 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_93627 | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 2.33 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_20 |
| vlm_160822 | ligand_9284 | 2-Hydroxy-5-sulfobenzoic acid (5-S… | H3L | O=C(O)c1cc(S(=O)(=O)O)ccc1O | 2.48 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_37 |

### pKa 2.5–3.0 (3 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_107963 | ligand_6275 | N-(2-Hydroxyethyl)ethylenedinitril… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 2.62 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_1 |
| vlm_160226 | ligand_9257 | 2-Hydroxybenzoic acid (Salicylic a… | H2L | O=C(O)c1ccccc1O | 2.8 | 25 | 0.1 | HL→H2L | M_tot_4 | M_tot_37 |
| vlm_157473 | ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxyl… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 2.9 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_12 |

### pKa 3.0–3.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_113459 | ligand_6372 | Glycylglycine (Diglycine) | HL | NCC(=O)NCC(=O)O | 3.11 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_3 |

### pKa 4.0–4.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_157459 | ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxyl… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 4.35 | 25 | 0.1 | HL→H2L | M_tot_12 | M_tot_18 |

### pKa 5.0–5.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_107958 | ligand_6275 | N-(2-Hydroxyethyl)ethylenedinitril… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 5.38 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_5 |

### pKa 5.5–6.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_157439 | ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxyl… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 5.65 | 25 | 0.1 | L→HL | M_tot_18 | M_tot_57 |

### pKa 8.0–8.5 (2 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_113440 | ligand_6372 | Glycylglycine (Diglycine) | HL | NCC(=O)NCC(=O)O | 8.09 | 25 | 0.1 | L→HL | M_tot_3 | M_tot_16 |
| vlm_101543 | ligand_6021 | N,N-Bis(2-hydroxyethyl)glycine (Bi… | HL | O=C(O)CN(CCO)CCO | 8.11 | 25 | 0.1 | L→HL | M_tot_2 | M_tot_26 |

### pKa 9.5–10.0 (2 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_93606 | ligand_5760 | Aminoacetic acid (Glycine) | HL | NCC(=O)O | 9.57 | 25 | 0.1 | L→HL | M_tot_20 | M_tot_43 |
| vlm_107949 | ligand_6275 | N-(2-Hydroxyethyl)ethylenedinitril… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 9.7 | 25 | 0.1 | L→HL | M_tot_5 | M_tot_47 |

### pKa 11.5–12.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_160810 | ligand_9284 | 2-Hydroxy-5-sulfobenzoic acid (5-S… | H3L | O=C(O)c1cc(S(=O)(=O)O)ccc1O | 11.85 | 25 | 0.1 | L→HL | M_tot_37 | M_tot_1 |

---

### Step 15: `search_networks`
**Args:**
```json
{
  "where": "((c.metal_name = 'Fe^[3+]' OR c.metal_name = 'Fe^[2+]') AND c.ligand_id IN (ligand_9058, ligand_5760, ligand_9257, ligand_9284, ligand_6275, ligand_6021, ligand_6372))",
  "order_by": "c.ligand_name ASC, n.node_count DESC",
  "limit": 50
}
```

[summary]
## search_networks — 69 row(s)

> **Reference equilibrium networks (compact)** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### Beta-definition legend
| beta_def | equation |
|----------|----------|
| beta_def_873 | ``[ML2] + [HL] <=> [ML3] + [H]`` |
| beta_def_821 | ``[M] + [HL] <=> [ML] + [H]`` |
| beta_def_846 | ``[ML] + [HL] <=> [ML2] + [H]`` |
| beta_def_779 | ``[M] + [HL] <=> [MHL]`` |
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_732 | ``[M] + [H2L] <=> [MH2L]`` |
| beta_def_800 | ``[MHL] + [L] <=> [MHL2]`` |
| beta_def_374 | ``[M]^2 + [L]^2 <=> [M2(H-1L)2] + [H]^2`` |
| beta_def_966 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` |
| beta_def_424 | ``[M]^2 + [L]^2 + [H2O]^2 <=> [M2(OH)2L2] + [H]^2`` |
| beta_def_872 | ``[M] + [L]^3 <=> [ML3]`` |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |
| beta_def_194 | ``[M] + [HL]^2 <=> [M(HL)2]`` |
| beta_def_268 | ``[M] + [OH]^3 + [L] <=> [M(OH)3L]`` |
| beta_def_246 | ``[M] + [OH]^2 + [L] <=> [M(OH)2L]`` |
| beta_def_238 | ``[M(OH)2L] + [H] <=> [M(OH)L] + [H2O]`` |
| beta_def_263 | ``[M(OH)3L] + [H] <=> [M(OH)2L] + [H2O]`` |
| beta_def_427 | ``[M(OH)L]^2 <=> [M2(OH)2L2]`` |
| beta_def_786 | ``[M] + [HL] <=> [MHL]`` |

### Metal-ligand pair summary
| metal | metal_id | ligand | ligand_id | HxL | T_range | I_range | net_count | max_nodes | max_net_id | ligand_SMILES |
|-------|----------|--------|-----------|-----|---------|---------|-----------|----------|------------|---------------|
| `Fe^[3+]` | metal_61 | 2-Hydroxy-5-sulfobenzoic acid (5-Sulfos… | ligand_9284 | H3L | 15~30 | -0.05~3.15 | 4 | 3 | ref_eq_net_23388 | O=C(O)c1cc(S(=O)(=O)O)ccc1O |
| `Fe^[2+]` | metal_62 | 2-Hydroxy-5-sulfobenzoic acid (5-Sulfos… | ligand_9284 | H3L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_23374 | O=C(O)c1cc(S(=O)(=O)O)ccc1O |
| `Fe^[3+]` | metal_61 | 2-Hydroxybenzoic acid (Salicylic acid) | ligand_9257 | H2L | 15~30 | -0.15~3.15 | 7 | 3 | ref_eq_net_23169 | O=C(O)c1ccccc1O |
| `Fe^[2+]` | metal_62 | 2-Hydroxybenzoic acid (Salicylic acid) | ligand_9257 | H2L | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_23158 | O=C(O)c1ccccc1O |
| `Fe^[2+]` | metal_62 | 2-Hydroxypropane-1,2,3-tricarboxylic ac… | ligand_9058 | H3L | 15~41 | -0.05~3.15 | 5 | 5 | ref_eq_net_22169 | O=C(O)CC(O)(CC(=O)O)C(=O)O |
| `Fe^[3+]` | metal_61 | 2-Hydroxypropane-1,2,3-tricarboxylic ac… | ligand_9058 | H3L | 19~30 | -0.05~1.15 | 3 | 4 | ref_eq_net_22182 | O=C(O)CC(O)(CC(=O)O)C(=O)O |
| `Fe^[2+]` | metal_62 | Aminoacetic acid (Glycine) | ligand_5760 | HL | 5~45 | -0.15~3.15 | 7 | 3 | ref_eq_net_64 | NCC(=O)O |
| `Fe^[3+]` | metal_61 | Aminoacetic acid (Glycine) | ligand_5760 | HL | 16.5~31.5 | 0.275~3.225 | 3 | 3 | ref_eq_net_96 | NCC(=O)O |
| `Fe^[2+]` | metal_62 | Glycylglycine (Diglycine) | ligand_6372 | HL | 12.5~27.5 | 0.775~1.225 | 1 | 1 | ref_eq_net_6939 | NCC(=O)NCC(=O)O |
| `Fe^[3+]` | metal_61 | Glycylglycine (Diglycine) | ligand_6372 | HL | 12.5~27.5 | 0.775~1.225 | 1 | 1 | ref_eq_net_6955 | NCC(=O)NCC(=O)O |
| `Fe^[2+]` | metal_62 | N,N-Bis(2-hydroxyethyl)glycine (Bicine) | ligand_6021 | HL | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_2267 | O=C(O)CN(CCO)CCO |
| `Fe^[3+]` | metal_61 | N,N-Bis(2-hydroxyethyl)glycine (Bicine) | ligand_6021 | HL | 19~30 | -0.05~0.65 | 2 | 1 | ref_eq_net_2278 | O=C(O)CN(CCO)CCO |
| `Fe^[3+]` | metal_61 | N-(2-Hydroxyethyl)ethylenedinitrilotria… | ligand_6275 | H3L | 19~30 | -0.05~1.15 | 2 | 4 | ref_eq_net_4876 | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O |
| `Fe^[2+]` | metal_62 | N-(2-Hydroxyethyl)ethylenedinitrilotria… | ligand_6275 | H3L | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_4867 | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O |

### Global max-node network: `Fe^[2+]` + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid)
network_id: ref_eq_net_22169 | metal_id: metal_62 | ligand_id: ligand_9058 | ligand_def_HxL: H3L | nodes: 5

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_374 | ``[M]^2 + [L]^2 <=> [M2(H-1L)2] + [H]^2`` | logK | -5.4 |
| beta_def_732 | ``[M] + [H2L] <=> [MH2L]`` | logK | 1.1 |
| beta_def_779 | ``[M] + [HL] <=> [MHL]`` | logK | 3.1 |
| beta_def_800 | ``[MHL] + [L] <=> [MHL2]`` | logK | 3.19 |
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 4.56 |

---
