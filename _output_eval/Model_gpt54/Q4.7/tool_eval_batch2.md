# Q4.7 — Tool Results (batch 2)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Co(II), Co(III)",
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
  "name": "cobalt",
  "limit": 20
}
```

[summary]
## search_metals — 3 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_33 | Co^[2+] | Co | 2 | ✓ | [Co+2] | InChI=1S/Co/q+2 | beta_totN_92 | ligand_totN_977 | vlm_totN_2977 |
| metal_34 | Co^[3+] | Co | 3 | ✓ | [Co+3] | InChI=1S/Co/q+3 | beta_totN_20 | ligand_totN_19 | vlm_totN_55 |
| metal_181 | TcO^[2+] | Tc | 2 |  | *** | *** | beta_totN_2 | ligand_totN_1 | vlm_totN_2 |

---

### Step 5: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_33, metal_34) AND (c.ligand_name_SRD LIKE '%ethylenediamine%' OR c.ligand_name_SRD LIKE '%diethylenetriamine%' OR c.ligand_name_SRD LIKE '%triethylenetetramine%' OR c.ligand_name_SRD LIKE '%tris(2-aminoethyl)amine%' OR c.ligand_name_SRD LIKE '%cyclam%' OR c.ligand_name_SRD LIKE '%cyclen%' OR c.ligand_name_SRD LIKE '%ammonia%' OR c.ligand_name_SRD LIKE '%glycine%' OR c.ligand_name_SRD LIKE '%EDTA%' OR c.ligand_name_SRD LIKE '%NTA%' OR c.ligand_name_SRD LIKE '%IDA%' OR c.ligand_name_SRD LIKE '%DTPA%' OR c.ligand_name_SRD LIKE '%bipyridine%' OR c.ligand_name_SRD LIKE '%phenanthroline%'))",
  "order_by": "c.ligand_name_SRD ASC, c.metal_id ASC, s.constant_value DESC",
  "limit": 200
}
```

[summary]
## search_stability — 200 row(s)

### logK — 57 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_33 | Co^[2+] | ligand_7795 | 1,3-Diazole (Imidazole) | L | c1c[nH]cn1 | 13 | 4 | 25~37 | 0.1~3 | *** | 4 |
| metal_33 | Co^[2+] | ligand_7796 | 1-Methylimidazole | L | Cn1ccnc1 | 8 | 4 | 25 | 0.1~0.5 | *** | 2 |
| metal_33 | Co^[2+] | ligand_7541 | 1,4,7,10,13,16,19,22,25,28,… | L | C1CNCCNCCNCCNCCNCCNCCNCCNCCNCCNCCNCCN1 | 6 | 6 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_6112 | 1,4,8,12-Tetraazacyclopenta… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCCN(CC(=O)O)CCN(CC(=O)O)CCC1 | 5 | 5 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7540 | 1,4,7,10,13,16,19,22,25,28,… | L | C1CNCCNCCNCCNCCNCCNCCNCCNCCNCCNCCN1 | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7539 | 1,4,7,10,13,16,19,22,25,28-… | L | C1CNCCNCCNCCNCCNCCNCCNCCNCCNCCN1 | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 4 | 2 | 20~25 | 0.1~1 | *** | 2 |
| metal_33 | Co^[2+] | ligand_7212 | 1,4,7-Triazaheptane (Diethy… | L | NCCNCCN | 4 | 2 | 25 | 0.1~1 | *** | 2 |
| metal_33 | Co^[2+] | ligand_6087 | 1,7-Dioxa-4,10,13-triazacyc… | H3L | O=C(O)CN1CCOCCN(CC(=O)O)CCN(CC(=O)O)CCOCC1 | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7799 | 1-Butylimidazole | L | CCCCn1ccnc1 | 4 | 4 | 25 | 0.5 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7797 | 1-Ethylimidazole | L | CCn1ccnc1 | 4 | 4 | 25 | 0.5 | *** | 1 |
| metal_33 | Co^[2+] | ligand_6113 | 1-Oxa-4,7,10,13-tetraazacyc… | H4L | O=C(O)CN1CCOCCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7798 | 1-Propylimidazole | L | CCCn1ccnc1 | 4 | 4 | 25 | 0.5 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7809 | 1-Vinylimidazole | L | C=Cn1ccnc1 | 4 | 4 | 25 | 0.5 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7726 | 14,16-Dioxo-1,4,7,10,13-pen… | L | O=C1CC(=O)NCCNCCNCCNCCN1 | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7728 | 14,16-Dioxo-15-ethyl-1,4,7,… | L | CCC1C(=O)NCCNCCNCCNCCNC1=O | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_9550 | 1,1,1-Trifluoropentane-2,4-… | HL | CC(=O)CC(=O)C(F)(F)F | 3 | 2 | 25 | 0.5~1 | *** | 2 |
| metal_33 | Co^[2+] | ligand_8191 | 1,10-Phenanthroline (Dipyri… | L | c1cnc2c(c1)ccc1cccnc12 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7439 | 1,4,8,11-Tetraazacyclotetra… | L | C1CNCCNCCCNCCNC1 | 3 | 2 | 25~35 | 0.1 | *** | 2 |
| metal_33 | Co^[2+] | ligand_7847 | 2-(2-Aminoethyl)imidazole (… | L | NCCc1ncc[nH]1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7181 | 2-(2-Aminoethylamino)ethano… | L | NCCNCCO | 3 | 3 | 25 | 0.5 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7862 | 2-(2-Pyridyl)imidazole | L | c1ccc(-c2ncc[nH]2)nc1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7183 | 2-(3-Aminopropylamino)ethan… | L | NCCCNCCO | 3 | 3 | 25 | 0.5 | *** | 1 |
| metal_33 | Co^[2+] | ligand_8383 | 2-Aminoethylaminomethylphos… | H2L | NCCNCP(=O)(O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_8366 | (L-2-Amino-4-methylpentanoy… | H2L | CC(C)CC(N)C(=O)NCP(=O)(O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_8397 | (Pentamethyleneimino)methyl… | H4L | O=P(O)(O)C(N1CCCCC1)P(=O)(O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_9552 | 1,1,1,5,5,5-Hexafluoropenta… | HL | O=C(CC(=O)C(F)(F)F)C(F)(F)F | 2 | 2 | 25 | 1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7871 | 1,11-Di-4-imidazolyl-2,6,10… | L | c1nc(CNCCCNCCCNCc2cnc[nH]2)c[nH]1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_8210 | 1,2-Diazine (Pyridazine) | L | c1ccnnc1 | 2 | 2 | 25 | 0.5 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7059 | 1,3-Diamino-2-propanol (2-H… | L | NCC(O)CN | 2 | 2 | 30 | 1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_6070 | 1,4,10-Trioxa-7,13-diazacyc… | H2L | O=C(O)CN1CCOCCOCCN(CC(=O)O)CCOCC1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7869 | 1,9-Di-4-imidazolyl-2,5,8-t… | L | c1nc(CNCCNCCNCc2cnc[nH]2)c[nH]1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_5773 | 1-Aminocyclopentanecarboxyl… | HL | NC1(C(=O)O)CCCC1 | 2 | 2 | 20 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_8656 | 1-Hydroxycyclopentanecarbox… | HL | O=C(O)C1(O)CCCC1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7039 | 2,2-Dimethyltrimethylenedia… | L | CC(C)(CN)CN | 2 | 2 | 30 | 1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7832 | 2,5-Bis(4-imidazolylmethyl)… | H2L | O=C1NC(Cc2c[nH]cn2)C(=O)NC1Cc1c[nH]cn1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_8194 | 2,9-Dimethyl-1,10-phenanthr… | L | Cc1ccc2ccc3ccc(C)nc3c2n1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_8117 | 2-(2-Aminoethylaminomethyl)… | L | NCCNCc1ccccn1 | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7870 | 1,11-Di-2-imidazolyl-2,6,10… | L | c1c[nH]c(CNCCCNCCCNCc2ncc[nH]2)n1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7804 | 1,2-Dimethylimidazole | L | Cc1nccn1C | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7579 | 1,4,10-Trioxa-7,13-diazacyc… | L | C1COCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7503 | 1,4,7,10,13-Pentaazacyclohe… | L | C1CCNCCNCCNCCNCCNC1 | 1 | 1 | 35 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7500 | 1,4,7,10,13-Pentaazacyclohe… | L | C1CNCCNCCNCCNCCNC1 | 1 | 1 | 35 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7505 | 1,4,7,10,13-Pentaazacyclono… | L | C1CCCNCCNCCNCCNCCNCC1 | 1 | 1 | 35 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7504 | 1,4,7,10,13-Pentaazacyclooc… | L | C1CCNCCNCCNCCNCCNCC1 | 1 | 1 | 35 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7499 | 1,4,7,10,13-Pentaazacyclope… | L | C1CNCCNCCNCCNCCN1 | 1 | 1 | 35 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7425 | 1,4,7,10-Tetraazacyclododec… | L | C1CNCCNCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7434 | 1,4,7,10-Tetraazacyclopenta… | L | C1CCNCCNCCNCCNCC1 | 1 | 1 | 35 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7436 | 1,4,7,11-Tetraazacyclotetra… | L | C1CNCCCNCCNCCNC1 | 1 | 1 | 35 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7474 | 1,4,8,11-Tetraazacyclopenta… | L | C1CCNCCNCCCNCCNC1 | 1 | 1 | 35 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7614 | 1,4-Dioxa-7,10,13-triazacyc… | L | C1CNCCOCCOCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7867 | 1,9-Di-4-imidazolyl-5-oxa-2… | L | c1nc(CNCCOCCNCc2cnc[nH]2)c[nH]1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7747 | 1-Oxa-4,13-dithia-7,10-diaz… | L | C1CNCCSCCOCCSCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7618 | 1-Oxa-4,7,10,13-tetraazacyc… | L | C1CNCCNCCOCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7748 | 1-Oxa-7,10-dithia-4,13-diaz… | L | C1COCCNCCSCCSCCN1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_6724 | 2-(Carboxymethylamino)benzo… | H2L | O=C(O)CNc1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |

### ΔS — 13 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_33 | Co^[2+] | ligand_7795 | 1,3-Diazole (Imidazole) | L | c1c[nH]cn1 | 4 | 4 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_8191 | 1,10-Phenanthroline (Dipyri… | L | c1cnc2c(c1)ccc1cccnc12 | 3 | 3 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7862 | 2-(2-Pyridyl)imidazole | L | c1ccc(-c2ncc[nH]2)nc1 | 3 | 3 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 2 | 1 | 25 | 0.1~1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7212 | 1,4,7-Triazaheptane (Diethy… | L | NCCNCCN | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7039 | 2,2-Dimethyltrimethylenedia… | L | CC(C)(CN)CN | 2 | 2 | 30 | 1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7871 | 1,11-Di-4-imidazolyl-2,6,10… | L | c1nc(CNCCCNCCCNCc2cnc[nH]2)c[nH]1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_6070 | 1,4,10-Trioxa-7,13-diazacyc… | H2L | O=C(O)CN1CCOCCOCCN(CC(=O)O)CCOCC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7425 | 1,4,7,10-Tetraazacyclododec… | L | C1CNCCNCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7439 | 1,4,8,11-Tetraazacyclotetra… | L | C1CNCCNCCCNCCNC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7869 | 1,9-Di-4-imidazolyl-2,5,8-t… | L | c1nc(CNCCNCCNCc2cnc[nH]2)c[nH]1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7796 | 1-Methylimidazole | L | Cn1ccnc1 | 1 | 1 | 25 | 0.5 | *** | 0 |

### ΔH — 14 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_33 | Co^[2+] | ligand_7795 | 1,3-Diazole (Imidazole) | L | c1c[nH]cn1 | 4 | 4 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_8191 | 1,10-Phenanthroline (Dipyri… | L | c1cnc2c(c1)ccc1cccnc12 | 3 | 3 | 20 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7862 | 2-(2-Pyridyl)imidazole | L | c1ccc(-c2ncc[nH]2)nc1 | 3 | 3 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 2 | 1 | 25 | 0.1~1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7212 | 1,4,7-Triazaheptane (Diethy… | L | NCCNCCN | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7039 | 2,2-Dimethyltrimethylenedia… | L | CC(C)(CN)CN | 2 | 2 | 25 | 1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7871 | 1,11-Di-4-imidazolyl-2,6,10… | L | c1nc(CNCCCNCCCNCc2cnc[nH]2)c[nH]1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_6070 | 1,4,10-Trioxa-7,13-diazacyc… | H2L | O=C(O)CN1CCOCCOCCN(CC(=O)O)CCOCC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7425 | 1,4,7,10-Tetraazacyclododec… | L | C1CNCCNCCNCCN1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7439 | 1,4,8,11-Tetraazacyclotetra… | L | C1CNCCNCCCNCCNC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7475 | 1,4,8,12-Tetraazacyclopenta… | L | C1CNCCCNCCNCCCNC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7869 | 1,9-Di-4-imidazolyl-2,5,8-t… | L | c1nc(CNCCNCCNCc2cnc[nH]2)c[nH]1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7796 | 1-Methylimidazole | L | Cn1ccnc1 | 1 | 1 | 25 | 1 | *** | 0 |

---

### Step 6: `db_ranked_pairs`
**Args:**
```json
{
  "rank_by": "measurement_count",
  "limit": 50,
  "where": "metal_ids = '[''metal_33'', ''metal_34'']'"
}
```

[summary]
**db_ranked_pairs:** Error - Unknown rank_by='measurement_count'. Choose from: ['ligands_per_metal', 'measurements_per_ligand', 'measurements_per_metal', 'metals_per_ligand', 'pka_per_ligand']

---

### Step 7: `db_ranked_pairs`
**Args:**
```json
{
  "rank_by": "metals_per_ligand",
  "limit": 100,
  "where": "metal_ids = '[''metal_33'', ''metal_34'']'"
}
```

[TOOL ERROR] db_ranked_pairs: Error executing tool db_ranked_pairs: no such column: metal_ids

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_33, metal_34) AND c.ligand_name_SRD IN ('1,4,7-Triazaheptane (Diethylenetriamine)','1,4,7,10-Tetraazadecane (Triethylenetetramine)','1,4,7,10-Tetraazacyclododecane','1,4,8,11-Tetraazacyclotetradecane','1,10-Phenanthroline (Dipyridophenazine)','1,3-Diazole (Imidazole)','1-Methylimidazole'))",
  "order_by": "c.ligand_name_SRD ASC, c.metal_id ASC, s.temperature_c ASC, s.ionic_strength_mol_l ASC, s.constant_type ASC, s.constant_value DESC",
  "limit": 200
}
```

[summary]
## search_stability — 31 row(s)

### `Co^[2+]` + 1,3-Diazole (Imidazole) — 21 measurement(s)
metal_id: metal_33 | ligand_id: ligand_7795
ligand_HxL_def: L | ligand_SMILES: c1c[nH]cn1

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_133835 | *** | beta_def_812 | ΔH | 0 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (-14.5, L, 7) |
| vlm_133840 | *** | beta_def_840 | ΔH | 0 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (-14.5, L, 7) |
| vlm_133845 | *** | beta_def_872 | ΔH | 0 | 25 | 0.1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (-14.5, L, 7) |
| vlm_133850 | *** | beta_def_894 | ΔH | 0 | 25 | 0.1 | `[M] + [L]^4 <=> [ML4]` | *** | [L] | (-14.5, L, 7) |
| vlm_133847 | ref_eq_map_13282 | beta_def_894 | logK | 6.7 | 25 | 0.1 | `[M] + [L]^4 <=> [ML4]` | *** | [L] | (-14.5, L, 7) |
| vlm_133842 | ref_eq_map_13282 | beta_def_872 | logK | 5.76 | 25 | 0.1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (-14.5, L, 7) |
| vlm_133837 | ref_eq_map_13282 | beta_def_840 | logK | 4.34 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (-14.5, L, 7) |
| vlm_133831 | ref_eq_map_13282 | beta_def_812 | logK | 2.44 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (-14.5, L, 7) |
| vlm_133836 | *** | beta_def_812 | ΔS | 0 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (-14.5, L, 7) |
| vlm_133841 | *** | beta_def_840 | ΔS | 0 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (-14.5, L, 7) |
| vlm_133846 | *** | beta_def_872 | ΔS | 0 | 25 | 0.1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (-14.5, L, 7) |
| vlm_133851 | *** | beta_def_894 | ΔS | 0 | 25 | 0.1 | `[M] + [L]^4 <=> [ML4]` | *** | [L] | (-14.5, L, 7) |
| vlm_133833 | ref_eq_map_13285 | beta_def_812 | logK | 2.49 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (-14.5, L, 7) |
| vlm_133849 | ref_eq_map_13284 | beta_def_894 | logK | 7.5 | 25 | 3 | `[M] + [L]^4 <=> [ML4]` | *** | [L] | (-14.5, L, 7) |
| vlm_133844 | ref_eq_map_13284 | beta_def_872 | logK | 6.53 | 25 | 3 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (-14.5, L, 7) |
| vlm_133839 | ref_eq_map_13284 | beta_def_840 | logK | 4.92 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (-14.5, L, 7) |
| vlm_133834 | ref_eq_map_13284 | beta_def_812 | logK | 2.73 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (-14.5, L, 7) |
| vlm_133848 | ref_eq_map_13283 | beta_def_894 | logK | 6.1 | 37 | 0.15 | `[M] + [L]^4 <=> [ML4]` | *** | [L] | (-14.5, L, 7) |
| vlm_133843 | ref_eq_map_13283 | beta_def_872 | logK | 5.31 | 37 | 0.15 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (-14.5, L, 7) |
| vlm_133838 | ref_eq_map_13283 | beta_def_840 | logK | 4.04 | 37 | 0.15 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (-14.5, L, 7) |
| vlm_133832 | ref_eq_map_13283 | beta_def_812 | logK | 2.3 | 37 | 0.15 | `[M] + [L] <=> [ML]` | *** | [L] | (-14.5, L, 7) |

### `Co^[2+]` + 1-Methylimidazole — 10 measurement(s)
metal_id: metal_33 | ligand_id: ligand_7796
ligand_HxL_def: L | ligand_SMILES: Cn1ccnc1

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_134050 | ref_eq_map_13331 | beta_def_894 | logK | 6.7 | 25 | 0.1 | `[M] + [L]^4 <=> [ML4]` | *** | [L] | (7.1, L, +inf) |
| vlm_134042 | ref_eq_map_13331 | beta_def_812 | logK | 2.29 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (7.1, L, +inf) |
| vlm_134046 | ref_eq_map_13331 | beta_def_840 | logK | -4.25 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (7.1, L, +inf) |
| vlm_134048 | ref_eq_map_13331 | beta_def_872 | logK | -5.32 | 25 | 0.1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (7.1, L, +inf) |
| vlm_134049 | ref_eq_map_13332 | beta_def_872 | logK | 5.85 | 25 | 0.5 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (7.1, L, +inf) |
| vlm_134047 | ref_eq_map_13332 | beta_def_840 | logK | 4.4 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (7.1, L, +inf) |
| vlm_134043 | ref_eq_map_13332 | beta_def_812 | logK | 2.4 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (7.1, L, +inf) |
| vlm_134051 | ref_eq_map_13332 | beta_def_894 | logK | -6.95 | 25 | 0.5 | `[M] + [L]^4 <=> [ML4]` | *** | [L] | (7.1, L, +inf) |
| vlm_134045 | *** | beta_def_812 | ΔS | -10 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (7.1, L, +inf) |
| vlm_134044 | *** | beta_def_812 | ΔH | -16.7 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (7.1, L, +inf) |

---
