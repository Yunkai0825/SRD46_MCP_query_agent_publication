# Q4.7 — Tool Results (batch 1)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Cobalt(II), Cobalt(III)",
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
  "where": "(c.metal_id IN (metal_33, metal_34) AND c.ligand_name_SRD IN ('ethylenediamine','diethylenetriamine','triethylenetetramine','tris(2-aminoethyl)amine','cyclam','cyclen','ammonia') AND s.reaction_type LIKE '%M + L = ML%' AND s.solvent_name LIKE '%water%')",
  "order_by": "c.ligand_name_SRD ASC, c.metal_id ASC, s.temperature_c ASC, s.ionic_strength_mol_l ASC, s.constant_value DESC",
  "limit": 200
}
```

[summary]
## search_stability

*(no results)*

---

### Step 6: `search_ligands`
**Args:**
```json
{
  "name": "ethylenediamine, diethylenetriamine, triethylenetetramine, tris(2-aminoethyl)amine, cyclam, cyclen, ammonia",
  "limit": 50
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 7: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_33, metal_34) AND c.ligand_class_name LIKE '%amine%')",
  "order_by": "c.ligand_name_SRD ASC, c.metal_id ASC, s.constant_value DESC",
  "limit": 200
}
```

[summary]
## search_stability — 200 row(s)

### logK — 54 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_33 | Co^[2+] | ligand_7254 | 1,3-Bis(2,5,8,11-tetraazaun… | L | NCCNCCNCCNCc1cccc(CNCCNCCNCCN)c1 | 10 | 10 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7029 | Ethylenediamine | L | NCCN | 9 | 3 | 25~37 | 0.1~1 | *** | 3 |
| metal_33 | Co^[2+] | ligand_6982 | Aminoacetohydroxamic acid (… | HL | NCC(=O)NO | 8 | 5 | 25 | 0.1~0.5 | *** | 2 |
| metal_34 | Co^[3+] | ligand_7029 | Ethylenediamine | L | NCCN | 8 | 4 | 25~30 | 1 | *** | 3 |
| metal_33 | Co^[2+] | ligand_6887 | 2-Aminoethanol (Ethanolamin… | L | NCCO | 6 | 2 | 25 | 0.1~2 | *** | 3 |
| metal_33 | Co^[2+] | ligand_6984 | DL-2-Aminobutanohydroxamic … | HL | CCC(N)C(=O)NO | 5 | 5 | 25 | 0.5 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7092 | 1,2,3-Triaminopropane | L | NCC(N)CN | 4 | 2 | 20~25 | 0.1 | *** | 2 |
| metal_33 | Co^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 4 | 2 | 20~25 | 0.1~1 | *** | 2 |
| metal_33 | Co^[2+] | ligand_7212 | 1,4,7-Triazaheptane (Diethy… | L | NCCNCCN | 4 | 2 | 25 | 0.1~1 | *** | 2 |
| metal_33 | Co^[2+] | ligand_7145 | 2,2'-Iminodiethanol (Dietha… | L | OCCNCCO | 4 | 2 | 25 | 0.5~2 | *** | 2 |
| metal_33 | Co^[2+] | ligand_6962 | D-4-Amino-1,2-oxazolidin-3-… | L | NC1CONC1=O | 4 | 3 | 25 | 0.1~0.5 | *** | 2 |
| metal_33 | Co^[2+] | ligand_6995 | DL-2-Amino-3-hydroxybutanoh… | HL | C[C@@H](O)[C@H](N)C(=O)NO | 4 | 4 | 25 | 0.5 | *** | 1 |
| metal_33 | Co^[2+] | ligand_6994 | DL-2-Amino-3-hydroxypropano… | HL | N[C@@H](CO)C(=O)NO | 4 | 4 | 25 | 0.5 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7314 | DL-Ethylenedinitrilotetrapr… | L | CC(O)CN(CCN(CC(C)O)CC(C)O)CC(C)O | 4 | 3 | 25 | 0.1~0.5 | *** | 2 |
| metal_33 | Co^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7226 | 1,4,9,12-Tetraazadodecane (… | L | NCCNCCCCNCCN | 3 | 3 | 25 | 1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7351 | 1,4-Bis[bis(2-aminoethyl)am… | L | NCCN(CCN)c1ccc(N(CCN)CCN)cc1 | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7181 | 2-(2-Aminoethylamino)ethano… | L | NCCNCCO | 3 | 3 | 25 | 0.5 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7183 | 2-(3-Aminopropylamino)ethan… | L | NCCCNCCO | 3 | 3 | 25 | 0.5 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7090 | 4,7-Dithia-1,10-diazadecane… | L | NCCSCCSCCN | 3 | 2 | 25~30 | 0.1~1 | *** | 2 |
| metal_33 | Co^[2+] | ligand_7046 | Bicyclohexyl-1,1'-diamine | L | NC1(C2(N)CCCCC2)CCCCC1 | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7047 | DL(trans)-Cyclohexane-1,2-d… | L | N[C@@H]1CCCC[C@H]1N | 3 | 3 | 20 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_6986 | DL-2-Aminohexanohydroxamic … | HL | CCCC[C@H](N)C(=O)NO | 3 | 3 | 25 | 0.5 | *** | 1 |
| metal_33 | Co^[2+] | ligand_6985 | DL-2-Aminopentanohydroxamic… | HL | CCC[C@H](N)C(=O)NO | 3 | 3 | 25 | 0.5 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7313 | DL-N-(2-Hydroxyethyl)ethyle… | L | CC(O)CN(CCO)CCN(CC(C)O)CC(C)O | 3 | 3 | 25 | 0.5 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7059 | 1,3-Diamino-2-propanol (2-H… | L | NCC(O)CN | 2 | 2 | 30 | 1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7225 | 1,4,8,11-Tetraazaundecane (… | L | NCCNCCCNCCN | 2 | 1 | 25 | 0.1~1 | *** | 2 |
| metal_33 | Co^[2+] | ligand_7213 | 1,4,8-Triazaoctane (2,3-tri) | L | NCCCNCCN | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7215 | 1,5,9-Triazanonane (3,3-tri) | L | NCCCNCCCN | 2 | 1 | 25 | 0.1~1 | *** | 2 |
| metal_33 | Co^[2+] | ligand_7285 | 2,2',2''-Nitrilotriethanol … | L | OCCN(CCO)CCO | 2 | 1 | 25 | 0.1~0.5 | *** | 2 |
| metal_33 | Co^[2+] | ligand_7039 | 2,2-Dimethyltrimethylenedia… | L | CC(C)(CN)CN | 2 | 2 | 30 | 1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7151 | 2-(Carbamylmethylamino)etha… | HL | NC(=O)CNCCS(=O)(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_6901 | 2-Amino-2-deoxy-D-glucopyra… | L | N[C@H]1C(O)O[C@H](CO)[C@@H](O)[C@@H]1O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7040 | 2-Methylenetrimethylenediam… | L | C=C(CN)CN | 2 | 2 | 25 | 0.5 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7149 | 2-[Tris(hydroxymethyl)methy… | HL | O=S(=O)(O)CCNC(CO)(CO)CO | 2 | 1 | 20~25 | 0.1 | *** | 2 |
| metal_33 | Co^[2+] | ligand_7082 | 4-Thia-1,7-diazaheptane (Th… | L | NCCSCCN | 2 | 2 | 30 | 1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7329 | 5-Methyl-1,5,9-triazanonane | L | CN(CCCN)CCCN | 2 | 2 | 10 | 0 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7242 | 7-Oxa-1,4,10,13-tetraazatri… | L | NCCNCCOCCNCCN | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7243 | 7-Thia-1,4,10,13-tetraazatr… | L | NCCNCCSCCNCCN | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_6907 | D-Mannosamine | L | N[C@H]1[C@@H](O)[C@H](O)[C@@H](CO)O[C@@H]1O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7034 | DL-1,2-Dimethylethylenediam… | L | CC(N)C(C)N | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7372 | DL-2-(Aminomethyl)piperidine | L | NCC1CCCCN1 | 2 | 2 | 25 | 0 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7185 | DL-Ethylenediiminodipropan-… | L | CC(O)CNCCNCC(C)O | 2 | 2 | 25 | 0.5 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7204 | Ethylenebis[imino-4-(4-meth… | L | C/C(CC(C)(C)NCCNC(C)(C)C/C(C)=N/O)=N\O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7205 | Ethylenebis[imino-4-(4-meth… | L | CO/N=C(\C)CC(C)(C)NCCNC(C)(C)C/C(C)=N/O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7184 | Ethylenediiminodi-2-ethanol… | L | OCCNCCNCCO | 2 | 2 | 25 | 0.5 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7312 | Ethylenedinitrilotetra-2-et… | L | OCCN(CCO)CCN(CCO)CCO | 2 | 2 | 25 | 0.5 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7099 | 1,1,2,2-Tetrakis(2-aminoeth… | L | NCCSC(SCCN)C(SCCN)SCCN | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7232 | 1,5,9,13-Tetraazatridecane … | L | NCCCNCCCNCCCN | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_6882 | 2-(3,4-Dihydroxyphenyl)ethy… | H2L | NCCc1ccc(O)c(O)c1 | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_33 | Co^[2+] | ligand_6900 | 2-Amino-2-hydroxymethyl-1,3… | L | NC(CO)(CO)CO | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7289 | 2-[Bis(2-hydroxyethyl)amino… | L | OCCN(CCO)C(CO)(CO)CO | 1 | 1 | 25 | 1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7202 | 8-Oxa-5,11-dithia-2,14-diaz… | L | CNCCSCCOCCSCCNC | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_7180 | Ethylenebis(iminomethylene-… | H2L | Oc1ccccc1CNCCNCc1ccccc1O | 1 | 1 | 25 | 0.1 | *** | 1 |

### ΔS — 12 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_33 | Co^[2+] | ligand_7029 | Ethylenediamine | L | NCCN | 3 | 3 | 25 | 1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 2 | 1 | 25 | 0.1~1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7212 | 1,4,7-Triazaheptane (Diethy… | L | NCCNCCN | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7225 | 1,4,8,11-Tetraazaundecane (… | L | NCCNCCCNCCN | 2 | 1 | 25 | 0.1~1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7039 | 2,2-Dimethyltrimethylenedia… | L | CC(C)(CN)CN | 2 | 2 | 30 | 1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7082 | 4-Thia-1,7-diazaheptane (Th… | L | NCCSCCN | 2 | 2 | 30 | 1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7372 | DL-2-(Aminomethyl)piperidine | L | NCC1CCCCN1 | 2 | 2 | 25 | 0 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7213 | 1,4,8-Triazaoctane (2,3-tri) | L | NCCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7226 | 1,4,9,12-Tetraazadodecane (… | L | NCCNCCCCNCCN | 1 | 1 | 25 | 1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7232 | 1,5,9,13-Tetraazatridecane … | L | NCCCNCCCNCCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7215 | 1,5,9-Triazanonane (3,3-tri) | L | NCCCNCCCN | 1 | 1 | 25 | 0.1 | *** | 0 |

### ΔH — 11 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_33 | Co^[2+] | ligand_7029 | Ethylenediamine | L | NCCN | 3 | 3 | 25 | 1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7224 | 1,4,7,10-Tetraazadecane (Tr… | L | NCCNCCNCCN | 2 | 1 | 25 | 0.1~1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7212 | 1,4,7-Triazaheptane (Diethy… | L | NCCNCCN | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7225 | 1,4,8,11-Tetraazaundecane (… | L | NCCNCCCNCCN | 2 | 1 | 25 | 0.1~1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7039 | 2,2-Dimethyltrimethylenedia… | L | CC(C)(CN)CN | 2 | 2 | 25 | 1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7372 | DL-2-(Aminomethyl)piperidine | L | NCC1CCCCN1 | 2 | 2 | 25 | 0 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7244 | 1,4,7,10,13-Pentaazatrideca… | L | NCCNCCNCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7213 | 1,4,8-Triazaoctane (2,3-tri) | L | NCCCNCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7226 | 1,4,9,12-Tetraazadodecane (… | L | NCCNCCCCNCCN | 1 | 1 | 25 | 1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7232 | 1,5,9,13-Tetraazatridecane … | L | NCCCNCCCNCCCN | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_7215 | 1,5,9-Triazanonane (3,3-tri) | L | NCCCNCCCN | 1 | 1 | 25 | 0.1 | *** | 0 |

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id IN (metal_33, metal_34) AND c.ligand_name_SRD LIKE '%amm%')",
  "order_by": "c.ligand_name_SRD ASC, c.metal_id ASC, s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability — 35 row(s)

### `Co^[2+]` + 2-[Bis(carboxymethyl)aminoethyl]trimethylammonium (perchlor… — 2 measurement(s)
metal_id: metal_33 | ligand_id: ligand_6255
ligand_HxL_def: H2L | ligand_SMILES: C[N+](C)(C)CCN(CC(=O)O)CC(=O)O

| equation | type | vlm_counts | ref_eq_map | value_range | T°C_range | I(M)_range | beta_defs | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|----------|------|------------|------------|-------------|-----------|------------|-----------|--------------------|--------------|-------------|
| `[M] + [L]^2 <=> [ML2]` | logK | 1 | ref_eq_map_4701 | 10.49 | 20 | 0.1 | beta_def_840 | *** | [L] | (5.45, L, +inf) |
| `[M] + [L] <=> [ML]` | logK | 1 | ref_eq_map_4701 | 5.51 | 20 | 0.1 | beta_def_812 | *** | [L] | (5.45, L, +inf) |

Summary stats
| type | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|------|------------|-------------|-----------|------------|--------------------|-------------------|
| logK | 2 | 2 | 20 | 0.1 | *** | 1 |

### `Co^[2+]` + Ammonia — 19 measurement(s)
metal_id: metal_33 | ligand_id: ligand_10103
ligand_HxL_def: L | ligand_SMILES: N

| equation | type | vlm_counts | ref_eq_map | value_range | T°C_range | I(M)_range | beta_defs | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|----------|------|------------|------------|-------------|-----------|------------|-----------|--------------------|--------------|-------------|
| `[M] + [L]^5 <=> [ML5]` | logK | 3 | ref_eq_map_28122; ref_eq_map_28123; ref_eq_map_28124 | 5.13~6.68 | 25~30 | 0~5 | beta_def_903 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^4 <=> [ML4]` | logK | 3 | ref_eq_map_28122; ref_eq_map_28123; ref_eq_map_28124 | 5.07~6.36 | 25~30 | 0~5 | beta_def_894 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^3 <=> [ML3]` | logK | 3 | ref_eq_map_28122; ref_eq_map_28123; ref_eq_map_28124 | 4.43~5.43 | 25~30 | 0~5 | beta_def_872 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L]^2 <=> [ML2]` | logK | 3 | ref_eq_map_28122; ref_eq_map_28123; ref_eq_map_28124 | 3.5~4.14 | 25~30 | 0~5 | beta_def_840 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L] <=> [ML]` | logK | 5 | 5 diff ref_eq_map | 2.03~2.31 | 25 | 0~5 | beta_def_812 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L] <=> [ML]` | ΔS | 1 | *** | -4.2 | 25 | 2 | beta_def_812 | *** | [L] | (9.26, L, +inf) |
| `[M] + [L] <=> [ML]` | ΔH | 1 | *** | -13.4 | 25 | 2 | beta_def_812 | *** | [L] | (9.26, L, +inf) |

Summary stats
| type | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|------|------------|-------------|-----------|------------|--------------------|-------------------|
| logK | 17 | 5 | 25~30 | 0~5 | *** | 5 |
| ΔS | 1 | 1 | 25 | 2 | *** | 0 |
| ΔH | 1 | 1 | 25 | 2 | *** | 0 |

### `Co^[3+]` + Ammonia — 14 measurement(s)
metal_id: metal_34 | ligand_id: ligand_10103
ligand_HxL_def: L | ligand_SMILES: N

| equation | type | vlm_counts | ref_eq_map | value_range | T°C_range | I(M)_range | beta_defs | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|----------|------|------------|------------|-------------|-----------|------------|-----------|--------------------|--------------|-------------|
| `[M] + [L]^6 <=> [ML6]` | logK | 2 | ref_eq_map_28143; ref_eq_map_28144 | 34.36~35.21 | 30 | 1~2 | beta_def_907 | *** | [L] | (9.26, L, +inf) |
| `[H] + [M(OH)2L4(cis)] <=> [M(OH)L4] + [H2O]` | logK | 1 | ref_eq_map_28140 | 7.99 | 20 | 0.1 | beta_def_993 | *** |  |  |
| `[H] + [M(OH)2L3(fac)] <=> [M(OH)L3] + [H2O]` | logK | 1 | ref_eq_map_28140 | 7.6 | 20 | 0.1 | beta_def_991 | *** |  |  |
| *** | logK | 1 | ref_eq_map_28140 | 6.33 | 25 | 0.1 | beta_def_906 | *** |  |  |
| `[H] + [M(OH)L4(cis)] <=> [ML4] + [H2O]` | logK | 1 | ref_eq_map_28140 | 5.69 | 20 | 0.1 | beta_def_895 | *** |  |  |
| `[H] + [M(OH)L3(fac)] <=> [ML3] + [H2O]` | logK | 1 | ref_eq_map_28140 | 5.33 | 20 | 0.1 | beta_def_882 | *** |  |  |
| `[ML4] + [L] <=> [ML5]` | logK | 1 | ref_eq_map_28141 | 5.07 | 25 | 2 | beta_def_905 | *** | [L] | (9.26, L, +inf) |
| `[ML5] + [L] <=> [ML6]` | logK | 2 | ref_eq_map_28141; ref_eq_map_28142 | 4.33~4.5 | 25 | 1~2 | beta_def_909 | *** | [L] | (9.26, L, +inf) |
| `[ML4] + [L] <=> [ML5]` | ΔH | 1 | *** | 0 | 25 | 0 | beta_def_905 | *** | [L] | (9.26, L, +inf) |
| `[ML5] + [L] <=> [ML6]` | ΔS | 1 | *** | 0 | 25 | 2 | beta_def_909 | *** | [L] | (9.26, L, +inf) |
| `[ML5] + [L] <=> [ML6]` | ΔH | 1 | *** | -28.9 | 25 | 0 | beta_def_909 | *** | [L] | (9.26, L, +inf) |
| `[ML4] + [L] <=> [ML5]` | ΔS | 1 | *** | -75.3 | 25 | 2 | beta_def_905 | *** | [L] | (9.26, L, +inf) |

Summary stats
| type | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|------|------------|-------------|-----------|------------|--------------------|-------------------|
| logK | 10 | 8 | 20~30 | 0.1~2 | *** | 5 |
| ΔH | 2 | 2 | 25 | 0 | *** | 0 |
| ΔS | 2 | 2 | 25 | 2 | *** | 0 |

---
