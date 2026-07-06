# Q5.1.1 — Tool Results (batch 5)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Hg(I), Hg(II)",
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
  "name": "mercury",
  "symbol": "Hg",
  "limit": 20
}
```

[summary]
## search_metals — 8 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_20 | BuHg^[+] | B | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_53 | EtHg^[+] | EHg | 1 |  | *** | *** | beta_totN_4 | ligand_totN_3 | vlm_totN_6 |
| metal_71 | Hg^[2+] | Hg | 2 | ✓ | [Hg+2] | InChI=1S/Hg/q+2 | beta_totN_68 | ligand_totN_310 | vlm_totN_1097 |
| metal_72 | Hg^[+] | Hg | 1 | ✓ | [Hg+] | InChI=1S/Hg/q+1 | beta_totN_12 | ligand_totN_31 | vlm_totN_83 |
| metal_93 | MeHg^[+] | MHg | 1 |  | *** | *** | beta_totN_18 | ligand_totN_79 | vlm_totN_148 |
| metal_136 | PhHg^[+] | PhHg | 1 |  | *** | *** | beta_totN_2 | ligand_totN_8 | vlm_totN_8 |
| metal_145 | PrHg^[+] | Pr | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_176 | O_[3]SPhHg | S | 0 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |

---

### Step 5: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71)",
  "order_by": "s.constant_value DESC",
  "limit": 200
}
```

[summary]
## search_stability — 200 row(s)

### ΔS — 41 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_71 | Hg^[2+] | ligand_10163 | Chloride ion | *** | *** | 8 | 4 | 25 | 0.5~3 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_10168 | Bromide ion | *** | *** | 8 | 4 | 25 | 0.5~3 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_10076 | Hydroxide ion | *** | *** | 5 | 3 | 25 | 1~3 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6335 | Oxybis(ethylenenitrilo)tetr… | H4L | O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6794 | N-(6-Methyl-2-pyridylmethyl… | H2L | Cc1cccc(CN(CC(=O)O)CC(=O)O)n1 | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6793 | N-(2-Pyridylmethyl)iminodia… | H2L | O=C(O)CN(CC(=O)O)Cc1ccccn1 | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_8177 | Ethylenebis(aminomethylene-… | L | c1ccc(CNCCNCc2ccccn2)nc1 | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_10022 | Selenocarbamide (Selenourea) | L | NC(N)=[Se] | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_10106 | Hydrogen azide (Hydrazoic a… | HL | [N-]=[N+]=N | 2 | 2 | 25 | 1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_10171 | Iodide ion | *** | *** | 1 | 1 | 25 | 0.5 | solid | 0 |
| metal_71 | Hg^[2+] | ligand_10147 | Hydrogen sulfite (Sulfurous… | H2L | O=[SH](=O)O | 1 | 1 | 25 | 0.5 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6751 | 1,2-Phenylenedinitrilotetra… | H4L | O=C(O)CN(CC(=O)O)c1ccccc1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6316 | Octamethylenedinitrilotetra… | H4L | O=C(O)CN(CCCCCCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6348 | Thiobis(ethylenenitrilo)tet… | H4L | O=C(O)CN(CCSCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6313 | Tetramethylenedinitrilotetr… | H4L | O=C(O)CN(CCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_9704 | 4,7,13,16-Tetraoxa-1,10-dit… | *** | *** | 1 | 1 | 25 | 0.5 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_7601 | 4,7,13,16,21,24-Hexaoxa-1,1… | L | C1COCCN2CCOCCOCCN(CCO1)CCOCCOCC2 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6311 | Trimethylenedinitrilotetraa… | H4L | O=C(O)CN(CCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6315 | Hexamethylenedinitrilotetra… | H4L | O=C(O)CN(CCCCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6342 | Ethylenebis(oxyethylenenitr… | H4L | O=C(O)CN(CCOCCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_7226 | 1,4,9,12-Tetraazadodecane (… | L | NCCNCCCCNCCN | 1 | 1 | 25 | 1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_7359 | Pentamethyleneimine (Piperi… | L | C1CCNCC1 | 1 | 1 | 25 | 0.5 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_7225 | 1,4,8,11-Tetraazaundecane (… | L | NCCNCCCNCCN | 1 | 1 | 25 | 1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_8206 | Nitrilotris[methylene(6-met… | L | Cc1cccc(CN(Cc2cccc(C)n2)Cc2cccc(C)n2)n1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6887 | 2-Aminoethanol (Ethanolamin… | L | NCCO | 1 | 1 | 25 | 0 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_7161 | N-Methylethylenediamine | L | CNCCN | 1 | 1 | 25 | 1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_8209 | Ethylenedinitrilotetrakis(m… | L | c1ccc(CN(CCN(Cc2ccccn2)Cc2ccccn2)Cc2ccccn2)nc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_8174 | Iminobis(methylene-2-pyridi… | L | c1ccc(CNCc2ccccn2)nc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 1 | 1 | 25 | 1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_8112 | 2-(Methylaminomethyl)pyridi… | L | CNCc1ccccn1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_8205 | Nitrilotris(methylene-2-pyr… | L | c1ccc(CN(Cc2ccccn2)Cc2ccccn2)nc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_8179 | Tetramethylenebis(aminometh… | L | c1ccc(CNCCCCNCc2ccccn2)nc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_8178 | Trimethylenebis(aminomethyl… | L | c1ccc(CNCCCNCc2ccccn2)nc1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_10023 | Semicarbazide | L | NNC(N)=O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_9705 | 7,10,13,16-Tetraoxa-1,4-dit… | *** | *** | 1 | 1 | 25 | 0.5 | *** | 0 |

### logK — 81 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_71 | Hg^[2+] | ligand_10090 | Hydrogen cyanide (Hydrocyan… | HL | C#N | 17 | 4 | 10~40 | 0~2 | *** | 6 |
| metal_71 | Hg^[2+] | ligand_10147 | Hydrogen sulfite (Sulfurous… | H2L | O=[SH](=O)O | 5 | 2 | 18~25 | 0~3 | *** | 3 |
| metal_71 | Hg^[2+] | ligand_10004 | Thiocarbamide (Thiourea) | L | NC(N)=S | 5 | 3 | 25 | 0.1~0.5 | *** | 2 |
| metal_71 | Hg^[2+] | ligand_10171 | Iodide ion | *** | *** | 3 | 3 | 25 | 0.5 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_10022 | Selenocarbamide (Selenourea) | L | NC(N)=[Se] | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_10156 | Hydrogen selenide (Hydrosel… | H2L | [SeH2] | 3 | 3 | 25 | 1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 3 | 1 | 25 | 0.1~1 | *** | 3 |
| metal_71 | Hg^[2+] | ligand_8866 | Diphenylphosphinoacetic aci… | HL | O=C(O)CP(c1ccccc1)c1ccccc1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_10037 | Selenosemicarbazide | L | NNC(N)=[Se] | 3 | 3 | 25~30 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_9868 | 3-(Diphenylphosphino)benzen… | HL | O=S(=O)(O)c1cccc(P(c2ccccc2)c2ccccc2)c1 | 3 | 3 | 25 | 1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_10093 | Selenocyanate ion | L | N#C[Se-] | 3 | 2 | 25 | 0.5~0.7 | *** | 2 |
| metal_71 | Hg^[2+] | ligand_10025 | Thiosemicarbazide | L | NNC(N)=S | 3 | 3 | 25 | 0.1~0.7 | *** | 2 |
| metal_71 | Hg^[2+] | ligand_10076 | Hydroxide ion | *** | *** | 2 | 1 | 25 | 0~3 | *** | 2 |
| metal_71 | Hg^[2+] | ligand_6794 | N-(6-Methyl-2-pyridylmethyl… | H2L | Cc1cccc(CN(CC(=O)O)CC(=O)O)n1 | 2 | 1 | 20~25 | 0.1 | *** | 2 |
| metal_71 | Hg^[2+] | ligand_9759 | 2,3-Dimercaptopropanol (BAL) | H2L | OCC(S)CS | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_9033 | P-Phenylphosphinodiacetic a… | H2L | O=C(O)CP(CC(=O)O)c1ccccc1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_9069 | Phosphinotriacetic acid [Tr… | H3L | O=C(O)CP(CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_10149 | Hydrogen thiosulfate (Thios… | H2L | O=S(O)(O)=S | 2 | 2 | 25 | 3 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_7212 | 1,4,7-Triazaheptane (Diethy… | L | NCCNCCN | 2 | 1 | 20~25 | 0.1~0.5 | *** | 2 |
| metal_71 | Hg^[2+] | ligand_7029 | Ethylenediamine | L | NCCN | 2 | 1 | 25 | 0.1~1 | *** | 2 |
| metal_71 | Hg^[2+] | ligand_8191 | 1,10-Phenanthroline (Dipyri… | L | c1cnc2c(c1)ccc1cccnc12 | 2 | 1 | 20~25 | 0.1 | *** | 2 |
| metal_71 | Hg^[2+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_6335 | Oxybis(ethylenenitrilo)tetr… | H4L | O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_6348 | Thiobis(ethylenenitrilo)tet… | H4L | O=C(O)CN(CCSCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_6793 | N-(2-Pyridylmethyl)iminodia… | H2L | O=C(O)CN(CC(=O)O)Cc1ccccn1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_6342 | Ethylenebis(oxyethylenenitr… | H4L | O=C(O)CN(CCOCCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_8177 | Ethylenebis(aminomethylene-… | L | c1ccc(CNCCNCc2ccccn2)nc1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_7225 | 1,4,8,11-Tetraazaundecane (… | L | NCCNCCCNCCN | 1 | 1 | 25 | 1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_7161 | N-Methylethylenediamine | L | CNCCN | 1 | 1 | 25 | 1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_8209 | Ethylenedinitrilotetrakis(m… | L | c1ccc(CN(CCN(Cc2ccccn2)Cc2ccccn2)Cc2ccccn2)nc1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_8174 | Iminobis(methylene-2-pyridi… | L | c1ccc(CNCc2ccccn2)nc1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_9091 | Benzene-1,2-bis[methylbis(t… | H4L | O=C(O)CSC(SCC(=O)O)c1ccccc1C(SCC(=O)O)SCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_8205 | Nitrilotris(methylene-2-pyr… | L | c1ccc(CN(Cc2ccccn2)Cc2ccccn2)nc1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_8766 | Mercaptoacetic acid (Thiogl… | H2L | O=C(O)CS | 1 | 1 | 25 | 1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_9032 | P-Ethylphosphinodiacetic ac… | H2L | CCP(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_10144 | Hydrogen sulfide (Hydrosulf… | H2L | S | 1 | 1 | 20 | 1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_9867 | 2-Hydroxyethyldiethylphosph… | L | CCP(CC)CCO | 1 | 1 | 20 | 1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_10150 | Selenosulfate ion | *** | *** | 1 | 1 | 25 | 1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_7348 | Ethylenedinitrilotetrakis(e… | L | NCCN(CCN)CCN(CCN)CCN | 1 | 1 | 20 | 0.5 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_7511 | 1,4,7,10,13,16-Hexaazacyclo… | L | C1CNCCNCCNCCNCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_7499 | 1,4,7,10,13-Pentaazacyclope… | L | C1CNCCNCCNCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_6115 | 1,4,7,10,13-Pentaazacyclope… | H5L | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_6355 | Ethylenebis[(N-methylimino)… | H4L | CN(CCN(C)CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_7500 | 1,4,7,10,13-Pentaazacyclohe… | L | C1CNCCNCCNCCNCCNC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_10017 | N-Allylthiourea | L | C=CCNC(N)=S | 1 | 1 | 25 | 1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_6367 | Tetraethylenepentanitrilohe… | H7L | O=C(O)CN(CCN(CCN(CC(=O)O)CC(=O)O)CC(=O)O)CCN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_6366 | Triethylenetetranitrilohexa… | H6L | O=C(O)CN(CCN(CCN(CC(=O)O)CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_7630 | 4,7-Dimethyl-13,18-dioxa-1,… | L | CN1CCN(C)CCN2CCOCCN(CCOCC2)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_7506 | 1,4,7,11,14-Pentaazacyclohe… | L | C1CNCCNCCCNCCNCCNC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_6102 | 1,4,7,10-Tetraazacyclododec… | H4L | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_6333 | (2-Hydroxytrimethylene)dini… | H4L | O=C(O)CN(CC(=O)O)CC(O)CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_7655 | 13,16,21,24-Tetramethyl-4,7… | L | CN1CCN(C)CCN2CCOCCOCCN(CC1)CCN(C)CCN(C)CC2 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_6109 | 1,4,8,11-Tetraazacyclotetra… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_9169 | D-myo-Inositol-1,2,6-tris(d… | H6L | O=P(O)(O)O[C@@H]1[C@@H](OP(=O)(O)O)[C@H](O)[C@@H](O)[C@H](O)[C@@H]1OP(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_7428 | 1,4,7,10-Tetraazacyclotride… | L | C1CNCCNCCNCCNC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_6116 | 1,4,7,10,13,16-Hexaazacyclo… | H6L | O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_5795 | trans-2-Amino-4-cyclohexene… | HL | N[C@@H]1CC=CC[C@H]1C(=O)O | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_7755 | 1-Thia-4,7,11,14-tetraazacy… | L | C1CNCCNCCSCCNCCNC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_10019 | N-Phenylthiourea | L | NC(=S)Nc1ccccc1 | 1 | 1 | 40 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_5857 | D-2-Amino-3-mercapto-3-meth… | H2L | CC(C)(S)[C@H](N)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_7634 | 21,24-Dimethyl-4,7,13,16-te… | L | CN1CCN(C)CCN2CCOCCOCCN(CCOCCOCC2)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_6352 | N-Methyliminobis(ethyleneni… | H4L | CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_6780 | 4-Aminopyridine-2,6-dicarbo… | H2L | Nc1cc(C(=O)O)nc(C(=O)O)c1 | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_7751 | 1-Thia-4,7,10-triazacyclodo… | L | C1CNCCSCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_6287 | rac-(1,2-Dimethylethylene)d… | H4L | CC(C(C)N(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_6350 | Ethylenebis(thioethylenenit… | H4L | O=C(O)CN(CCSCCSCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_7475 | 1,4,8,12-Tetraazacyclopenta… | L | C1CNCCCNCCNCCCNC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_9549 | 4-Phenylbutane-2,4-dione (B… | *** | *** | 1 | 1 | 25 | 1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_6298 | trans-1,2-Cyclopentylenedin… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCC[C@H]1N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_6290 | rac-(1,2-Diphenylethylene)d… | H4L | O=C(O)CN(CC(=O)O)C(c1ccccc1)C(c1ccccc1)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_7439 | 1,4,8,11-Tetraazacyclotetra… | L | C1CNCCNCCCNCCNC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_6778 | 4-Hydroxyquinoline-2-carbox… | H2L | O=C(O)c1cc(O)c2ccccc2n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_7345 | Nitrilotris(ethyleneamine) … | L | NCCN(CCN)CCN | 1 | 1 | 20 | 0.5 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_7723 | 14-Oxo-1,4,7,10,13-pentaaza… | L | O=C1CCNCCNCCNCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_6284 | DL-(Hexylethylene)dinitrilo… | H4L | CCCCCCC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_6286 | (1,1-Dimethylethylene)dinit… | H4L | CC(C)(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_71 | Hg^[2+] | ligand_9096 | rac-3,6-Dioxaoctane-1,2,4,5… | H6L | O=C(O)CC(OC(C(=O)O)C(OC(CC(=O)O)C(=O)O)C(=O)O)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |

### ΔH — 2 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_71 | Hg^[2+] | ligand_10171 | Iodide ion | *** | *** | 1 | 1 | 25 | 0.5 | solid | 0 |
| metal_71 | Hg^[2+] | ligand_10076 | Hydroxide ion | *** | *** | 1 | 1 | 25 | 1 | solid | 0 |

---

### Step 6: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_72)",
  "order_by": "s.constant_value DESC",
  "limit": 120
}
```

[summary]
## search_stability — 83 row(s)

### ΔS — 7 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_72 | Hg^[+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_72 | Hg^[+] | ligand_9678 | cis-anti-cis-2,5,8,15,18,21… | *** | *** | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_72 | Hg^[+] | ligand_10106 | Hydrogen azide (Hydrazoic a… | HL | [N-]=[N+]=N | 1 | 1 | 25 | 0 | solid | 0 |
| metal_72 | Hg^[+] | ligand_10148 | Hydrogen sulfate ion (Sulfu… | HL | O=S(=O)([O-])O | 1 | 1 | 25 | 0 | solid | 0 |
| metal_72 | Hg^[+] | ligand_10163 | Chloride ion | *** | *** | 1 | 1 | 25 | 0 | solid | 0 |
| metal_72 | Hg^[+] | ligand_10171 | Iodide ion | *** | *** | 1 | 1 | 25 | 0.5 | solid | 0 |
| metal_72 | Hg^[+] | ligand_10168 | Bromide ion | *** | *** | 1 | 1 | 25 | 0.5 | solid | 0 |

### ΔH — 7 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_72 | Hg^[+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_72 | Hg^[+] | ligand_9678 | cis-anti-cis-2,5,8,15,18,21… | *** | *** | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_72 | Hg^[+] | ligand_10106 | Hydrogen azide (Hydrazoic a… | HL | [N-]=[N+]=N | 1 | 1 | 25 | 0 | solid | 0 |
| metal_72 | Hg^[+] | ligand_10148 | Hydrogen sulfate ion (Sulfu… | HL | O=S(=O)([O-])O | 1 | 1 | 25 | 0 | solid | 0 |
| metal_72 | Hg^[+] | ligand_10163 | Chloride ion | *** | *** | 1 | 1 | 25 | 0 | solid | 0 |
| metal_72 | Hg^[+] | ligand_10171 | Iodide ion | *** | *** | 1 | 1 | 25 | 0.5 | solid | 0 |
| metal_72 | Hg^[+] | ligand_10168 | Bromide ion | *** | *** | 1 | 1 | 25 | 0.5 | solid | 0 |

### logK — 31 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_72 | Hg^[+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 7 | 3 | 25 | 0~3 | solid | 5 |
| metal_72 | Hg^[+] | ligand_10076 | Hydroxide ion | *** | *** | 4 | 3 | 25 | 0.5~3 | *** | 2 |
| metal_72 | Hg^[+] | ligand_10148 | Hydrogen sulfate ion (Sulfu… | HL | O=S(=O)([O-])O | 4 | 3 | 25 | 0~3 | solid | 3 |
| metal_72 | Hg^[+] | ligand_10109 | Nitrate ion | *** | *** | 3 | 2 | 25 | 0.5~3 | *** | 2 |
| metal_72 | Hg^[+] | ligand_10113 | Hydrogen phosphate (Phospho… | H3L | O=P(O)(O)O | 3 | 2 | 25 | 0~3 | solid | 2 |
| metal_72 | Hg^[+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_72 | Hg^[+] | ligand_10114 | Hydrogen diphosphate (Pyrop… | H4L | O=P(O)(O)OP(=O)(O)O | 2 | 2 | 27 | 0.7 | *** | 1 |
| metal_72 | Hg^[+] | ligand_10117 | Hydrogen triphosphate (Trip… | H5L | O=P(O)(O)OP(=O)(O)OP(=O)(O)O | 2 | 2 | 27 | 0.7 | *** | 1 |
| metal_72 | Hg^[+] | ligand_8887 | Propane-2,2-dicarboxylic ac… | H2L | CC(C)(C(=O)O)C(=O)O | 2 | 2 | 27 | 0.7 | *** | 1 |
| metal_72 | Hg^[+] | ligand_8907 | Butanedioic acid (Succinic … | H2L | O=C(O)CCC(=O)O | 2 | 2 | 27 | 2.5 | *** | 1 |
| metal_72 | Hg^[+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 2 | 2 | 27 | 2.5 | *** | 1 |
| metal_72 | Hg^[+] | ligand_8467 | Propanoic acid (Propionic a… | HL | CCC(=O)O | 2 | 2 | 25 | 3 | *** | 1 |
| metal_72 | Hg^[+] | ligand_8724 | 3-Methoxypropanoic acid | HL | COCCC(=O)O | 2 | 2 | 25 | 3 | *** | 1 |
| metal_72 | Hg^[+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 2 | 2 | 25 | 3 | *** | 1 |
| metal_72 | Hg^[+] | ligand_8464 | Methanoic acid (Formic acid) | HL | O=CO | 2 | 2 | 25 | 3 | *** | 1 |
| metal_72 | Hg^[+] | ligand_8721 | Methoxyacetic acid | HL | COCC(=O)O | 2 | 2 | 25 | 3 | *** | 1 |
| metal_72 | Hg^[+] | ligand_8558 | Chloroacetic acid | HL | O=C(O)CCl | 2 | 2 | 25 | 3 | *** | 1 |
| metal_72 | Hg^[+] | ligand_10096 | Hydrogen carbonate (Carboni… | H2L | O=C(O)O | 2 | 2 | 25 | 0~3 | solid | 2 |
| metal_72 | Hg^[+] | ligand_9678 | cis-anti-cis-2,5,8,15,18,21… | *** | *** | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_72 | Hg^[+] | ligand_10163 | Chloride ion | *** | *** | 2 | 1 | 25 | 0~0.5 | solid | 2 |
| metal_72 | Hg^[+] | ligand_10092 | Hydrogen thiocyanate (Thioc… | HL | N=C=S | 2 | 1 | 25 | 0~1 | solid | 2 |
| metal_72 | Hg^[+] | ligand_10171 | Iodide ion | *** | *** | 2 | 1 | 25 | 0~0.5 | solid | 2 |
| metal_72 | Hg^[+] | ligand_10168 | Bromide ion | *** | *** | 2 | 1 | 25 | 0~0.5 | solid | 2 |
| metal_72 | Hg^[+] | ligand_10106 | Hydrogen azide (Hydrazoic a… | HL | [N-]=[N+]=N | 1 | 1 | 25 | 0 | solid | 1 |
| metal_72 | Hg^[+] | ligand_8938 | Benzene-1,2-dicarboxylic ac… | H2L | O=C(O)c1ccccc1C(=O)O | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_72 | Hg^[+] | ligand_6817 | Aminobenzene (Aniline) | L | Nc1ccccc1 | 1 | 1 | 27 | 1 | *** | 1 |
| metal_72 | Hg^[+] | ligand_8674 | DL-3-Hydroxybutanoic acid | HL | CC(O)CC(=O)O | 1 | 1 | 25 | 3 | *** | 1 |
| metal_72 | Hg^[+] | ligand_10079 | Hydrogen chromate (Chromic … | H2L | [O]=[Cr](=[O])([OH])[OH] | 1 | 1 | 25 | 0 | solid | 1 |
| metal_72 | Hg^[+] | ligand_10173 | Hydrogen iodate (Iodic acid) | HL | [O-][I+2]([O-])O | 1 | 1 | 25 | 0 | solid | 1 |
| metal_72 | Hg^[+] | ligand_10086 | Hexacyanocobaltate(III) ion | *** | *** | 1 | 1 | 25 | 0 | solid | 1 |
| metal_72 | Hg^[+] | ligand_10090 | Hydrogen cyanide (Hydrocyan… | HL | C#N | 1 | 1 | 25 | 0 | solid | 1 |

---

### Step 7: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.ligand_name IN ('chloride','bromide','iodide','cyanide','thiocyanate','thiosulfate','hydroxide'))",
  "order_by": "n.node_count DESC",
  "limit": 20
}
```

[summary]
## search_networks

*(no results)*

---
