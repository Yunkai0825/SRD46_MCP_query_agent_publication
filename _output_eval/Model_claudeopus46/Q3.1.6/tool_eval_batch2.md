# Q3.1.6 — Tool Results (batch 2)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "lanthanum"
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_79 | La^[3+] | La | 3 | ✓ | [La+3] | InChI=1S/La/q+3 | beta_totN_30 | ligand_totN_297 | vlm_totN_931 |

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "ligand_class": "carboxylic acid",
  "limit": 50
}
```

[summary]
## search_ligands — 50 result(s)

**stats:** 804 SQL matches · showing 50 · limit 50

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5950 | 1-Carboxymethyl-2-ketopiperazine | HL | Aza macrocycles with car… | 1 | `O=C(O)CN1CCNCC1=O` | (-inf, HL, 6.55, L, +inf) |
| ligand_5951 | 4-Carboxymethyl-2-ketopiperazine | HL | Aza macrocycles with car… | 1 | `O=C(O)CN1CCNC(=O)C1` | (-inf, HL, 5.51, L, +inf) |
| ligand_5952 | 1,4-Bis(carboxymethyl)-2-ketopiperazine | H2L | Aza macrocycles with car… | 2 | `O=C(O)CN1CCN(CC(=O)O)C(=O)C1` | (-inf, H2L, 2.95, HL, 5.87, L, +inf) |
| ligand_6058 | 1,4-Diazacyclohexa… (Piperazine-1,4-diacetic acid) | H2L | Aza macrocycles with car… | 17 | `O=C(O)CN1CCN(CC(=O)O)CC1` | (-inf, H3L, -1.8, H2L, 4.4, HL, 8.67, L, +inf) |
| ligand_6059 | 1,4-Diazacycloheptane-N,N'-diacetic acid | H2L | Aza macrocycles with car… | 18 | `O=C(O)CN1CCCN(CC(=O)O)CC1` | (-inf, H3L, 2.04, H2L, 5.92, HL, 9.53, L, +inf) |
| ligand_6060 | 1,4-Diazacycloheptane-N,N'-di(2-propanoic acid) | H2L | Aza macrocycles with car… | 3 | `CC(CN1CCCN(C(C)C(=O)O)CC1)C(=O)O` | (-inf, H2L, 6.11, HL, 10.2, L, +inf) |
| ligand_6061 | 1,4-Diazacycloheptane-N,N'-di(2-butanoic acid) | H2L | Aza macrocycles with car… | 3 | `CCC(C(=O)O)N1CCCN(C(CC)C(=O)O)CC1` | (-inf, H2L, 5.74, HL, 9.82, L, +inf) |
| ligand_6062 | 1,4-Diazacycloheptane-N,N'-di(2-pentanoic acid) | H2L | Aza macrocycles with car… | 3 | `CCCC(C(=O)O)N1CCCN(C(CCC)C(=O)O)CC1` | (-inf, H2L, 5.67, HL, 9.88, L, +inf) |
| ligand_6063 | 1,5-Diazacyclooctane-N,N'-diacetic acid | H2L | Aza macrocycles with car… | 31 | `O=C(O)CN1CCCN(CC(=O)O)CCC1` | (-inf, H3L, -1.9, H2L, 4.78, HL, 4.78, L, +inf) |
| ligand_6064 | 1-Oxa-4,7-diazacyclononane-N,N'-diacetic acid | H2L | Aza macrocycles with car… | 16 | `O=C(O)CN1CCOCCN(CC(=O)O)CC1` | (-inf, H3L, -1.8, H2L, 4.02, HL, 10.57, L, +inf) |
| ligand_6065 | 1-Thia-4,7-diazacyclononane-N,N'-diacetic acid | H2L | Aza macrocycles with car… | 25 | `O=C(O)CN1CCSCCN(CC(=O)O)CC1` | (-inf, H3L, -1.8, H2L, 4.05, HL, 4.05, L, +inf) |
| ligand_6066 | 1-Thia-4,8-diazacyclodecane-N,N'-diacetic acid | H2L | Aza macrocycles with car… | 14 | `O=C(O)CN1CCCN(CC(=O)O)CCSCC1` | (-inf, H3L, 2, H2L, 3.95, HL, 3.95, L, +inf) |
| ligand_6067 | 1,4-Dioxa-7,10-diazacyclododecane-N,N'-diacetic a… | H2L | Aza macrocycles with car… | 15 | `O=C(O)CN1CCOCCOCCN(CC(=O)O)CC1` | (-inf, H2L, 4.84, HL, 10.54, L, +inf) |
| ligand_6068 | 1,4-Dioxa-7,11-diazacyclotridecane-7,11-diacetic … | H2L | Aza macrocycles with car… | 27 | `O=C(O)CN1CCCN(CC(=O)O)CCOCCOCC1` | (-inf, H3L, 2.42, H2L, 6.95, HL, 9.91, L, +inf) |
| ligand_6069 | 1,7-Dioxa-4,10-diazacyclododecane-N,N'-diacetic a… | H2L | Aza macrocycles with car… | 16 | `O=C(O)CN1CCOCCN(CC(=O)O)CCOCC1` | (-inf, H3L, 2.11, H2L, 7.46, HL, 9.53, L, +inf) |
| ligand_6070 | 1,4,10-Trioxa-7,13-diazacyclopentadecane-N,N'-dia… | H2L | Aza macrocycles with car… | 74 | `O=C(O)CN1CCOCCOCCN(CC(=O)O)CCOCC1` | (-inf, H3L, 2, H2L, 8.45, HL, 8.63, L, +inf) |
| ligand_6071 | 1,4,10,13-Tetraoxa-7,16-diazacyclooctadecane-N,N'… | H2L | Aza macrocycles with car… | 74 | `O=C(O)CN1CCOCCOCCN(CC(=O)O)CCOCCOCC1` | (-inf, H3L, 2.2, H2L, 7.9, HL, 7.9, L, +inf) |
| ligand_6073 | 6,11-Dioxo-1,4,7,10-tetraazacyclododecane-1,4-dia… | H2L | Aza macrocycles with car… | 25 | `O=C(O)CN1CCN(CC(=O)O)CC(=O)NCCNC(=O)C1` | (-inf, H2L, 3.54, HL, 6.5, L, +inf) |
| ligand_6074 | 6,12-Dioxo-1,4,7,11-tetraazacyclotridecane-1,4-di… | H2L | Aza macrocycles with car… | 22 | `O=C(O)CN1CCN(CC(=O)O)CC(=O)NCCCNC(=O)C1` | (-inf, H2L, 3.4, HL, 6.41, L, +inf) |
| ligand_6075 | 1,4,7-Triazacyclononane-N-acetic acid (NOMA) | HL | Aza macrocycles with car… | 17 | `O=C(O)CN1CCNCCNCC1` | (-inf, H3L, 2.82, H2L, 7.45, HL, 7.45, L, +inf) |
| ligand_6076 | 1,4,7-Triazacyclononane-N,N',N''-triacetic… (NOTA) | H3L | Aza macrocycles with car… | 55 | `O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CC1` | (-inf, H4L, -1.7, H3L, 3.17, H2L, 5.7, HL, 5.7, L, +inf) |
| ligand_6077 | 1,4,7-Triazacyclodecane-N,N',N''-triacetic… (DETA) | H3L | Aza macrocycles with car… | 3 | `O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CC1` | (-inf, H4L, -2.3, H3L, 3.69, H2L, 6.12, HL, +inf) |
| ligand_6078 | 9-Methyl-1,4,7-triazacyclodecane-N,N',N''-triacet… | H3L | Aza macrocycles with car… | 2 | `CC1CN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)C1` | (-inf, H3L, 3.65, H2L, 6, HL, +inf) |
| ligand_6079 | 9,9-Methyl-1,4,7-triazacyclodecane-N,N',N''-triac… | H3L | Aza macrocycles with car… | 2 | `CC1(C)CN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)C1` | (-inf, H3L, 3.78, H2L, 6.28, HL, +inf) |
| ligand_6080 | 1,4,8-Triazacyclodecane-N,N',N''-triacetic… (UNTA) | H3L | Aza macrocycles with car… | 3 | `O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCC1` | (-inf, H4L, -1.7, H3L, 3.4, H2L, 7.2, HL, +inf) |
| ligand_6081 | 1,5,9-Triazacyclododecane-N,N',N''-triace… (DOTRA) | H3L | Aza macrocycles with car… | 9 | `O=C(O)CN1CCCN(CC(=O)O)CCCN(CC(=O)O)CCC1` | (-inf, H4L, 2.1, H3L, 3.65, H2L, 7.55, HL, 7.55, L, +inf) |
| ligand_6082 | 1-Oxa-4,7,10-triazacyclododecane-4,10-diacetic ac… | H2L | Aza macrocycles with car… | 26 | `O=C(O)CN1CCNCCN(CC(=O)O)CCOCC1` | (-inf, H4L, -1.4, H3L, 2.94, H2L, 6.02, HL, 6.02, L, +inf) |
| ligand_6083 | 1-Oxa-4,8,12-triazacyclotetradecane-4,12-diacetic… | H2L | Aza macrocycles with car… | 17 | `O=C(O)CN1CCCNCCCN(CC(=O)O)CCOCC1` | (-inf, H3L, 3.58, H2L, 6.97, HL, 6.97, L, +inf) |
| ligand_6084 | 1-Oxa-4,7,10-triazacyclododecane-4,7,10-triacetic… | H3L | Aza macrocycles with car… | 50 | `O=C(O)CN1CCOCCN(CC(=O)O)CCN(CC(=O)O)CC1` | (-inf, H4L, 2.7, H3L, 4.03, H2L, 7.73, HL, 7.73, L, +inf) |
| ligand_6085 | 1-Oxa-4,7,11-triazacyclotridecane-4,7,11-triaceti… | H3L | Aza macrocycles with car… | 24 | `O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCOCC1` | (-inf, H4L, 2.31, H3L, 4.17, H2L, 8.39, HL, 8.39, L, +inf) |
| ligand_6086 | 1-Oxa-4,8,12-triazacyclotetradecane-4,8,12-triace… | H3L | Aza macrocycles with car… | 16 | `O=C(O)CN1CCCN(CC(=O)O)CCOCCN(CC(=O)O)CCC1` | (-inf, H3L, 5.52, H2L, 8.33, HL, 10.25, L, +inf) |
| ligand_6087 | 1,7-Dioxa-4,10,13-triazacyclopentadecane-N,N',N''… | H3L | Aza macrocycles with car… | 50 | `O=C(O)CN1CCOCCN(CC(=O)O)CCN(CC(=O)O)CCOCC1` | (-inf, H4L, -1.6, H3L, 4.51, H2L, 8.92, HL, 9.55, L, +inf) |
| ligand_6088 | 1,7,13-Trioxa-4,10,16-triazacyclooctadecane-N,N',… | H3L | Aza macrocycles with car… | 46 | `O=C(O)CN1CCOCCN(CC(=O)O)CCOCCN(CC(=O)O)CCOCC1` | (-inf, H4L, -1.1, H3L, 7.67, H2L, 8.15, HL, 9.57, L, +inf) |
| ligand_6089 | 9,14-Dioxo-1,4,7,10,13-pentaazacyclopentadecane-1… | H3L | Aza macrocycles with car… | 41 | `O=C(O)CN1CCN(CC(=O)O)CC(=O)NCCNC(=O)CN(CC(=O)O)CC1` | (-inf, H4L, 2, H3L, 3.42, H2L, 4.2, HL, 9.49, L, +inf) |
| ligand_6090 | 9,15-Dioxo-1,4,7,10,14-pentaazacyclohexadecane-1,… | H3L | Aza macrocycles with car… | 24 | `O=C(O)CN1CCN(CC(=O)O)CC(=O)NCCCNC(=O)CN(CC(=O)O)CC1` | (-inf, H4L, -1.8, H3L, 3.58, H2L, 4.42, HL, 9.66, L, +inf) |
| ligand_6091 | 9,16-Dioxo-1,4,7,10,15-pentaazacycloheptadecane-1… | H3L | Aza macrocycles with car… | 25 | `O=C(O)CN1CCN(CC(=O)O)CC(=O)NCCCCNC(=O)CN(CC(=O)O)CC1` | (-inf, H4L, -1.8, H3L, 3.37, H2L, 4.45, HL, 9.05, L, +inf) |
| ligand_6092 | 9,16-Dioxo-1,4,7,10,15-pentaaza-cis-cycloheptadec… | *** | Aza macrocycles with car… | 6 | *** | (-inf, H4L, 2, H3L, 3.32, H2L, 4.67, HL, 9.68, L, +inf) |
| ligand_6093 | 9,17-Dioxo-1,4,7,10,16-pentaazacyclooctadecane-1,… | H3L | Aza macrocycles with car… | 6 | `O=C(O)CN1CCN(CC(=O)O)CC(=O)NCCCCCNC(=O)CN(CC(=O)O)CC1` | (-inf, H4L, -1.8, H3L, 3.13, H2L, 4.48, HL, 9.09, L, +inf) |
| ligand_6094 | 3,6,9-Tris(carboxymethyl)-4,14-dioxo-3,6,9,12,15-… | H3L | Aza macrocycles with car… | 6 | `O=C(O)CN1CCN(CC(=O)O)CC(=O)NCc2cccc(c2)CNC(=O)CN(CC(=O)O)CC1` | (-inf, H4L, -1.5, H3L, 3.31, H2L, 4.29, HL, 8.3, L, +inf) |
| ligand_6095 | 9,20-Dioxo-13,16-dioxa-1,4,7,10,19-pentaazacycloh… | H3L | Aza macrocycles with car… | 18 | `O=C(O)CN1CCN(CC(=O)O)CC(=O)NCCOCCOCCNC(=O)CN(CC(=O)O)CC1` | (-inf, H4L, -1.6, H3L, 3.49, H2L, 4.6, HL, 8.98, L, +inf) |
| ligand_6096 | 6,14-Dioxo-1,4,7,10,13-pentaazacyclopentadecane-1… | H3L | Aza macrocycles with car… | 18 | `O=C(O)CN1CCNC(=O)CN(CC(=O)O)CCN(CC(=O)O)CC(=O)NCC1` | (-inf, H4L, -1.4, H3L, 3.72, H2L, 7.22, HL, 7.42, L, +inf) |
| ligand_6097 | 1,4,7,10-Tetraazacyclododecane-N,N',N''-tr… (DO3A) | H3L | Aza macrocycles with car… | 25 | `O=C(O)CN1CCNCCN(CC(=O)O)CCN(CC(=O)O)CC1` | (-inf, H4L, 3.48, H3L, 4.43, H2L, 9.24, HL, 9.24, L, +inf) |
| ligand_6098 | 1,4,7,10-Tetraazacyclododecane-N,N',N''-tr… (DO3P) | H3L | Aza macrocycles with car… | 16 | `CC(C(=O)O)N1CCNCCN(C(C)C(=O)O)CCN(C(C)C(=O)O)CC1` | (-inf, H4L, 4.07, H3L, 5.3, H2L, 9.15, HL, 9.15, L, +inf) |
| ligand_6099 | N'''-2-Hydroxyethyl-1,4,7,10-tetraazacy… (HE-DO3A) | H3L | Aza macrocycles with car… | 6 | `O=C(O)CN1CCN(CCO)CCN(CC(=O)O)CCN(CC(=O)O)CC1` | (-inf, H4L, 3.67, H3L, 4.54, H2L, 9.28, HL, 9.28, L, +inf) |
| ligand_6100 | N'''-2-Hydroxypropyl-1,4,7,10-Tetraazac… (HP-DO3A) | H3L | Aza macrocycles with car… | 18 | `CC(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1` | (-inf, H4L, 3.26, H3L, 4.3, H2L, 9.43, HL, 9.43, L, +inf) |
| ligand_6101 | N'''-2-Hydroxy-1-methylethyl-1,4,7,10-… (HIP-DO3A) | H3L | Aza macrocycles with car… | 6 | `CC(CO)N1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1` | (-inf, H4L, 3.55, H3L, 4.51, H2L, 9.07, HL, 9.07, L, +inf) |
| ligand_6102 | 1,4,7,10-Tetraazacyclododecane-N,N',N'',N'… (DOTA) | H4L | Aza macrocycles with car… | 119 | `O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1` | (-inf, H4L, 4.23, H3L, 4.47, H2L, 9.69, HL, 9.69, L, +inf) |
| ligand_6103 | 2-Methyl-1,4,7,10-tetraazacyclododecane-N,N',N'',… | H4L | Aza macrocycles with car… | 1 | `CC1CN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CCN1CC(=O)O` | (-inf, H2L, 10.17, HL, +inf) |
| ligand_6104 | 1,4,7,10-Tetraazacyclotridecane-N,N',N'',… (TRITA) | H4L | Aza macrocycles with car… | 71 | `O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1` | (-inf, H4L, 3.27, H3L, 4.3, H2L, 9.8, HL, 9.8, L, +inf) |
| ligand_6105 | 12-Methyl-1,4,7,10-tetraazacyclotridecane-N,N',N'… | H4L | Aza macrocycles with car… | 4 | `CC1CN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)C1` | (-inf, H4L, 3.8, H3L, 4.55, H2L, 9.63, HL, 11.47, L, +inf) |

### Functional groups across all SQL matches (797 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 796 | 100% |
| aromatic_ring | 363 | 46% |
| tertiary_amine | 130 | 16% |
| hydroxyl | 120 | 15% |
| halide | 93 | 12% |
| thioether | 92 | 12% |
| amide | 56 | 7% |
| ether | 55 | 7% |
| pyridine | 39 | 5% |
| secondary_amine | 31 | 4% |
| thiol | 24 | 3% |
| primary_amine | 19 | 2% |
| ester | 16 | 2% |
| ketone | 14 | 2% |
| nitrile | 10 | 1% |
| sulfonate | 9 | 1% |
| phenol | 7 | 1% |
| phosphate | 7 | 1% |
| phosphonate | 5 | 1% |
| aldehyde | 3 | 0% |
| imine | 1 | 0% |

---

### Step 4: `search_ligands`
**Args:**
```json
{
  "name": "citric acid",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 8 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_9057 | DL-1-Hydroxypropane-1,2,3-tricar… (Isocitric acid) | H3L | Carboxylic acids polyaci… | 24 | `O=C(O)CC(C(=O)O)C(O)C(=O)O` | (-inf, H3L, 3.05, H2L, 4.3, HL, 5.73, L, +inf) |
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxyli… (Citric acid) | H3L | Carboxylic acids polyaci… | 384 | `O=C(O)CC(O)(CC(=O)O)C(=O)O` | (-inf, H3L, 2.9, H2L, 4.35, HL, 5.65, L, +inf) |
| ligand_10950 | DL-Methylcitric acid | *** | Ligands not selected | 0 | *** | *** |
| ligand_10951 | DL-Homocitric acid | *** | Ligands not selected | 0 | *** | *** |
| ligand_10952 | DL-threo-2-Methylisocitric acid | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (2 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 2 | 100% |
| hydroxyl | 2 | 100% |

---

### Step 5: `search_ligands`
**Args:**
```json
{
  "name": "oxalic acid",
  "limit": 5
}
```

[summary]
## search_ligands — 4 result(s)

**stats:** 4 SQL matches · showing 4 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8872 | Ethanedioic acid (Oxalic acid) | H2L | Carboxylic acids diacids | 394 | `O=C(O)C(=O)O` | (-inf, H2L, -1.2, HL, 3.8, L, +inf) |
| ligand_8960 | Oxopropanedioic acid (Ketomaloni… (Mesoxalic acid) | H2L | Carboxylic acids diacids… | 3 | `O=C(O)C(=O)C(=O)O` | (-inf, H2L, -1.82, HL, 3.52, L, +inf) |
| ligand_9763 | Dithiooxalic acid | H2L | miscellaneous mercaptans | 3 | `O=C(S)C(=O)S` | *** |
| ligand_11304 | Ethanedi(dithioic acid) (Tetrathiooxalic acid) | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (3 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 2 | 67% |
| ketone | 1 | 33% |
| thiol | 1 | 33% |

---

### Step 6: `search_ligands`
**Args:**
```json
{
  "name": "EDTA",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 5 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6118 | 6,11,18,23-Tetraoxo-1,4,7,10,13,16,19,… (24edtaen) | *** | Aza macrocycles with car… | 15 | *** | (-inf, H4L, 3.3, H3L, 4.18, H2L, 7.26, HL, 7.78, L, +inf) |
| ligand_6275 | N-(2-Hydroxyethyl)ethylenedinitrilotriace… (HEDTA) | H3L | EDTA and derivatives | 237 | `O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O` | (-inf, H3L, 2.62, H2L, 5.38, HL, 9.7, L, +inf) |
| ligand_6277 | Ethylenedinitrilotetraacetic acid (EDTA) | H4L | EDTA and derivatives | 596 | `O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O` | (-inf, H5L, -1.5, H4L, 2, H3L, 2.69, H2L, 6.13, HL, 9.52, L, +inf) |
| ligand_6335 | Oxybis(ethylenenitrilo)tetraacetic acid (EEDTA) | H4L | EDTA and derivatives | 124 | `O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O` | (-inf, H4L, -1.8, H3L, 2.76, H2L, 8.75, HL, 9.39, L, +inf) |
| ligand_6348 | Thiobis(ethylenenitrilo)tetraacetic acid (TEDTA) | H4L | EDTA and derivatives | 101 | `O=C(O)CN(CCSCCN(CC(=O)O)CC(=O)O)CC(=O)O` | (-inf, H4L, 2, H3L, 2.68, H2L, 8.37, HL, 9.31, L, +inf) |

### Functional groups across all SQL matches (4 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 4 | 100% |
| tertiary_amine | 4 | 100% |
| ether | 1 | 25% |
| hydroxyl | 1 | 25% |
| thioether | 1 | 25% |

---

### Step 7: `search_ligands`
**Args:**
```json
{
  "name": "DTPA",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 5 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6117 | 9,17-Dioxo-1,4,7,10,13,16-hexaazacycl… (DTPA-dien) | H3L | Aza macrocycles with car… | 6 | `O=C(O)CN1CCN(CC(=O)O)CC(=O)NCCNCCNC(=O)CN(CC(=O)O)CC1` | (-inf, H5L, -1.8, H4L, 2.62, H3L, 4.1, H2L, 8.87, HL, 10.02, L, +inf) |
| ligand_6356 | Diethylenetrinitrilopentaacetic acid (DTPA) | H5L | EDTA and derivatives | 322 | `O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O` | (-inf, H8L, -0.1, H7L, -0.1, H6L, -0.7, H5L, 2, H4L, 2.7, H3L, 4.28, H2L, 4.28, HL, -8.4, L, +inf) |
| ligand_6362 | Diethylenetrinitrilopentaacetic acid N… (DTPA-BMA) | *** | EDTA and derivatives | 43 | *** | (-inf, H4L, -1.4, H3L, 3.31, H2L, 4.38, HL, 9.37, L, +inf) |
| ligand_6363 | Diethylenetrinitrilopentaacetic acid N… (DTPA-BBA) | *** | EDTA and derivatives | 9 | *** | (-inf, H3L, 3.31, H2L, 4.44, HL, 9.36, L, +inf) |
| ligand_6364 | N,N"-Bis(2-pyridylmethyl)diethylenetrin… (DTPA-BP) | *** | EDTA and derivatives | 14 | *** | (-inf, H5L, 2.28, H4L, 3.41, H3L, 4.76, H2L, 6.46, HL, 9.5, L, +inf) |

### Functional groups across all SQL matches (2 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 2 | 100% |
| tertiary_amine | 2 | 100% |
| amide | 1 | 50% |
| secondary_amine | 1 | 50% |

---

### Step 8: `search_ligands`
**Args:**
```json
{
  "name": "NTA",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 298 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5763 | DL-2-Aminopentanoic acid (Norvaline) | HL | Amino Acids | 35 | `CCC[C@H](N)C(=O)O` | (-inf, H2L, 2.31, HL, 9.65, L, +inf) |
| ligand_5766 | L-2-Amino-4-methylpentanoic acid (Leucine) | HL | Amino Acids | 49 | `CC(C)C[C@H](N)C(=O)O` | (-inf, H2L, 2.32, HL, 9.58, L, +inf) |
| ligand_5767 | L-2-Amino-3-methylpentanoic acid (Isoleucine) | HL | Amino Acids | 51 | `CC[C@H](C)[C@H](N)C(=O)O` | (-inf, H2L, 2.26, HL, 9.6, L, +inf) |
| ligand_5768 | D-allo-2-Amino-3-methylpentan… (D-allo-Isoleucine) | HL | Amino Acids | 16 | `CC[C@H](C)[C@@H](N)C(=O)O` | (-inf, H2L, 2.2, HL, 9.62, L, +inf) |
| ligand_5773 | 1-Aminocyclopentanecarboxylic acid (Cycloleucine) | HL | Amino Acids | 11 | `NC1(C(=O)O)CCCC1` | (-inf, H2L, 2.4, HL, 10.31, L, +inf) |

### Functional groups across all SQL matches (223 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 88 | 39% |
| secondary_amine | 81 | 36% |
| tertiary_amine | 60 | 27% |
| amide | 46 | 21% |
| primary_amine | 45 | 20% |
| hydroxyl | 38 | 17% |
| ether | 37 | 17% |
| aromatic_ring | 31 | 14% |
| thioether | 13 | 6% |
| phosphonate | 10 | 4% |
| pyridine | 9 | 4% |
| imine | 7 | 3% |
| ketone | 7 | 3% |
| ester | 6 | 3% |
| halide | 6 | 3% |
| thiol | 5 | 2% |
| oxime | 3 | 1% |
| phenol | 2 | 1% |
| phosphate | 2 | 1% |
| sulfonate | 1 | 0% |

---

### Step 9: `search_ligands`
**Args:**
```json
{
  "name": "tartaric acid",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 9 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_8955 | D-2,3-Dihydroxybutanedioic acid (D-Tartaric acid) | H2L | Carboxylic acids diacids… | 214 | `O=C(O)C(O)C(O)C(=O)O` | (-inf, H2L, 2.82, HL, 3.97, L, +inf) |
| ligand_8956 | meso-2,3-Dihydroxybutanedioi… (meso-Tartaric acid) | H2L | Carboxylic acids diacids… | 43 | `O=C(O)[C@@H](O)[C@@H](O)C(=O)O` | (-inf, H2L, 2.97, HL, 4.49, L, +inf) |
| ligand_8996 | DL-2,3-Dimercaptobutaned… (DL-Dithiotartaric acid) | H4L | Carboxylic acids diacids… | 9 | `O=C(O)C(S)C(S)C(=O)O` | (-inf, H4L, 2.25, H3L, 3.96, H2L, 9.61, HL, +inf) |
| ligand_8997 | meso-2,3-Dimercaptobut… (meso-Dithiotartaric acid) | H4L | Carboxylic acids diacids… | 41 | `O=C(O)[C@@H](S)[C@@H](S)C(=O)O` | (-inf, H4L, 2.4, H3L, 3.46, H2L, 9.64, HL, 9.64, L, +inf) |
| ligand_10941 | erthro-2-Methyltartaric acid | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (4 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 4 | 100% |
| hydroxyl | 2 | 50% |
| thiol | 2 | 50% |

---

### Step 10: `search_ligands`
**Args:**
```json
{
  "name": "malonic acid",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 36 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5801 | Aminopropanedioic acid (Aminomalonic acid) | H2L | Amino Acids | 14 | `NC(C(=O)O)C(=O)O` | (-inf, H3L, -1.8, H2L, 2.94, HL, 9.22, L, +inf) |
| ligand_5808 | (3-Aminopropyl)malonic acid | H2L | Amino Acids | 18 | `NCCCC(C(=O)O)C(=O)O` | (-inf, H3L, 2.52, H2L, 4.86, HL, 10.45, L, +inf) |
| ligand_8873 | Propanedioic acid (Malonic acid) | H2L | Carboxylic acids diacids | 505 | `O=C(O)CC(=O)O` | (-inf, H2L, 2.65, HL, 5.27, L, +inf) |
| ligand_8874 | Ethane-1,1-dicarboxylic acid (Methylmalonic acid) | H2L | Carboxylic acids diacids | 71 | `CC(C(=O)O)C(=O)O` | (-inf, H2L, 2.87, HL, 5.38, L, +inf) |
| ligand_8875 | Propane-1,1-dicarboxylic acid (Ethylmalonic acid) | H2L | Carboxylic acids diacids | 61 | `CCC(C(=O)O)C(=O)O` | (-inf, H2L, 2.77, HL, 5.46, L, +inf) |

### Functional groups across all SQL matches (32 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 32 | 100% |
| aromatic_ring | 6 | 19% |
| primary_amine | 2 | 6% |
| hydroxyl | 1 | 3% |
| ketone | 1 | 3% |

---

### Step 11: `search_ligands`
**Args:**
```json
{
  "name": "nitrilotriacetic acid",
  "limit": 5
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 35 SQL matches · showing 5 · limit 5

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6047 | N,N''-Bis(3-hydroxy-6-methyl-2-pyridiny… (DTTA-HP) | H5L | Amino Acids | 24 | `Cc1ccc(O)c(CN(CCN(CCN(CC(=O)O)Cc2nc(C)ccc2O)CC(=O)O)CC(=O)O)n1` | (-inf, H8L, -1.5, H7L, 2.25, H6L, 3.49, H5L, 5.19, H4L, 6.21, H3L, 8.9, H2L, 10.95, HL, 10.95, L, +inf) |
| ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | NTA and derivatives | 534 | `O=C(O)CN(CC(=O)O)CC(=O)O` | (-inf, H4L, -1, H3L, -1, H2L, 2.52, HL, 9.46, L, +inf) |
| ligand_6166 | Nitrilotriacetic acid N-oxide | H3L | NTA and derivatives | 4 | `O=C(O)C[N+]([O-])(CC(=O)O)CC(=O)O` | (-inf, H2L, 2.57, HL, 7.89, L, +inf) |
| ligand_6172 | DL-2-Methylnitrilotriacetic acid | H3L | NTA and derivatives | 50 | `CC(C(=O)O)N(CC(=O)O)CC(=O)O` | (-inf, H3L, -1.5, H2L, -1.5, HL, -2.58, L, +inf) |
| ligand_6173 | DL-2-Ethylnitrilotriacetic acid | H3L | NTA and derivatives | 43 | `CCC(C(=O)O)N(CC(=O)O)CC(=O)O` | (-inf, H3L, -1.9, H2L, -1.9, HL, 9.81, L, +inf) |

### Functional groups across all SQL matches (34 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 34 | 100% |
| tertiary_amine | 33 | 97% |
| aromatic_ring | 12 | 35% |
| hydroxyl | 4 | 12% |
| amide | 2 | 6% |
| halide | 2 | 6% |
| phenol | 1 | 3% |
| pyridine | 1 | 3% |
| secondary_amine | 1 | 3% |
| sulfonate | 1 | 3% |
| thioether | 1 | 3% |

---

### Step 13: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_79"
}
```

[summary]
[CATALOG]
## build_system_catalog — 20 pair(s), 59 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_194 | [M] + [HL]^2 <=> [M(HL)2] |  |
| beta_def_352 | [ML3(s)] <=> [M] + [L]^3 | solid |
| beta_def_741 | [ML] + [H]^2 <=> [MH2L] |  |
| beta_def_779 | [M] + [HL] <=> [MHL] |  |
| beta_def_788 | [ML] + [H] <=> [MHL] |  |
| beta_def_792 | [ML2] + [H] <=> [MHL2] |  |
| beta_def_812 | [M] + [L] <=> [ML] |  |
| beta_def_840 | [M] + [L]^2 <=> [ML2] |  |
| beta_def_872 | [M] + [L]^3 <=> [ML3] |  |
| beta_def_894 | [M] + [L]^4 <=> [ML4] |  |
| beta_def_981 | [ML] + [OH] <=> [M(OH)L] |  |

*(all species aqueous unless noted)*

**1. La^[3+] + Propanedioic acid (Malonic acid)** (metal_79 + ligand_8873) — ligand_def_HxL: H2L | 20 ent, 4 sp, 20 vlms (vlm_152038…vlm_152057)
   - species: beta_def_779(4) beta_def_792(3) beta_def_812(8) beta_def_840(5)
   - eq:4 nets T:19~30°C I:-0.15~1.15M max 4n/4e
**2. La^[3+] + D-2,3-Dihydroxybutanedioic acid (D-Tartaric acid)** (metal_79 + ligand_8955) — ligand_def_HxL: H2L | 19 ent, 3 sp, 19 vlms (vlm_154960…vlm_154978)
   - species: beta_def_779(6) beta_def_812(7) beta_def_840(6)
   - eq:5 nets T:19~30°C I:-0.15~1.15M max 3n/3e
**3. La^[3+] + Hydroxyacetic acid (Glycolic acid)** (metal_79 + ligand_8640) — ligand_def_HxL: HL | 19 ent, 4 sp, 19 vlms (vlm_147101…vlm_147119)
   - species: beta_def_812(6) beta_def_840(5) beta_def_872(5) beta_def_894(3)
   - eq:4 nets T:19~30°C I:-0.05~2.15M max 4n/6e
**4. La^[3+] + 2-Hydroxy-2-methylpropanoic acid** (metal_79 + ligand_8647) — ligand_def_HxL: HL | 17 ent, 3 sp, 17 vlms (vlm_148045…vlm_148061)
   - species: beta_def_812(6) beta_def_840(6) beta_def_872(5)
   - eq:4 nets T:19~30°C I:-0.05~2.15M max 3n/3e
**5. La^[3+] + Ethanoic acid (Acetic acid)** (metal_79 + ligand_8465) — ligand_def_HxL: HL | 17 ent, 3 sp, 17 vlms (vlm_144473…vlm_144489)
   - species: beta_def_812(6) beta_def_840(6) beta_def_872(5)
   - eq:4 nets T:19~30°C I:-0.15~2.15M max 3n/3e
**6. La^[3+] + Pentane-2,4-dione (Acetylacetone)** (metal_79 + ligand_9526) — ligand_def_HxL: *** | 14 ent, 3 sp, 14 vlms (vlm_165187…vlm_165200)
   - species: beta_def_812(5) beta_def_840(5) beta_def_872(4)
   - eq:3 nets T:19~35°C I:-0.15~2.15M max 3n/3e
**7. La^[3+] + Hydrogen sulfate ion (Sulfuric acid)** (metal_79 + ligand_10148) — ligand_def_HxL: HL | 13 ent, 2 sp, 13 vlms (vlm_175723…vlm_175735)
   - species: beta_def_812(8) beta_def_840(5)
   - eq:4 nets T:19~30°C I:-0.05~2.15M max 2n/1e
**8. La^[3+] + D-2-Hydroxypropanoic acid (Lactic acid)** (metal_79 + ligand_8641) — ligand_def_HxL: HL | 13 ent, 3 sp, 13 vlms (vlm_147517…vlm_147529)
   - species: beta_def_812(5) beta_def_840(4) beta_def_872(4)
   - eq:3 nets T:15~30°C I:-0.05~2.15M max 3n/3e
**9. La^[3+] + Ethylenedinitrilo-N,N'-di(3-propanoic)-N,N'-diacetic acid** (metal_79 + ligand_6309) — ligand_def_HxL: H4L | 12 ent, 2 sp, 12 vlms (vlm_110121…vlm_110132)
   - species: beta_def_779(6) beta_def_812(6)
   - eq:2 nets T:19~30°C I:-0.05~0.65M max 2n/1e
**10. La^[3+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_79 + ligand_6277) — ligand_def_HxL: H4L | 12 ent, 2 sp, 12 vlms (vlm_108389…vlm_108400)
   - species: beta_def_788(3) beta_def_812(9)
   - eq:4 nets T:15~30°C I:-0.05~1.15M max 2n/1e
**11. La^[3+] + Oxydiacetic acid (Diglycolic acid)** (metal_79 + ligand_8974) — ligand_def_HxL: H2L | 11 ent, 3 sp, 11 vlms (vlm_155427…vlm_155437)
   - species: beta_def_812(4) beta_def_840(4) beta_def_872(3)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 3n/3e
**12. La^[3+] + Nitrilotriacetic acid (NTA)** (metal_79 + ligand_6165) — ligand_def_HxL: H3L | 11 ent, 3 sp, 11 vlms (vlm_105294…vlm_105304)
   - species: beta_def_812(6) beta_def_840(3) beta_def_981(2)
   - eq:3 nets T:15~30°C I:-0.05~0.65M max 3n/2e
**13. La^[3+] + Ethylenebis(oxyacetic acid)** (metal_79 + ligand_8986) — ligand_def_HxL: H2L | 10 ent, 4 sp, 10 vlms (vlm_155881…vlm_155890)
   - species: beta_def_792(3) beta_def_812(3) beta_def_840(3) beta_def_872(1)
   - eq:1 nets T:16.5~31.5°C I:0.775~1.225M max 4n/4e
**14. La^[3+] + Ethylenediiminodiacetic acid (EDDA)** (metal_79 + ligand_5975) — ligand_def_HxL: H2L | 10 ent, 4 sp, 10 vlms (vlm_100320…vlm_100329)
   - species: beta_def_741(1) beta_def_788(1) beta_def_812(4) beta_def_840(4)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 4n/4e
**15. La^[3+] + Pyridine-2,6-dicarboxylic acid (Dipicolinic acid)** (metal_79 + ligand_6774) — ligand_def_HxL: H2L | 9 ent, 3 sp, 9 vlms (vlm_119355…vlm_119363)
   - species: beta_def_812(3) beta_def_840(3) beta_def_872(3)
   - eq:1 nets T:16.5~31.5°C I:0.275~0.725M max 3n/3e
**16. La^[3+] + Pyridine-2-carboxylic acid (Picolinic acid)** (metal_79 + ligand_6762) — ligand_def_HxL: HL | 9 ent, 4 sp, 9 vlms (vlm_118694…vlm_118702)
   - species: beta_def_812(4) beta_def_840(2) beta_def_872(2) beta_def_894(1)
   - eq:2 nets T:19~30°C I:-0.05~0.65M max 4n/6e
**17. La^[3+] + Hydrogen fluoride (Hydrofluoric acid)** (metal_79 + ligand_10162) — ligand_def_HxL: HL | 8 ent, 2 sp, 8 vlms (vlm_176718…vlm_176725)
   - species: beta_def_352(2) beta_def_812(6)
   - eq:4 nets T:19~30°C I:-0.15~1.15M max 2n/1e
**18. La^[3+] + L-Hydroxybutanedioic acid (Hydroxysuccinic acid)(Malic acid)** (metal_79 + ligand_8953) — ligand_def_HxL: H2L | 8 ent, 3 sp, 8 vlms (vlm_154773…vlm_154780)
   - species: beta_def_779(2) beta_def_812(3) beta_def_840(3)
   - eq:3 nets T:19~30°C I:-0.05~1.15M max 3n/3e
**19. La^[3+] + Mercaptoacetic acid (Thioglycolic acid)** (metal_79 + ligand_8766) — ligand_def_HxL: H2L | 8 ent, 2 sp, 8 vlms (vlm_150501…vlm_150508)
   - species: beta_def_194(4) beta_def_779(4)
   - eq:2 nets T:19~30°C I:-0.05~2.15M max 2n/1e
**20. La^[3+] + 2-Methylpropanoic acid (Isobutyric acid)** (metal_79 + ligand_8473) — ligand_def_HxL: HL | 8 ent, 2 sp, 8 vlms (vlm_145441…vlm_145448)
   - species: beta_def_812(4) beta_def_840(4)
   - eq:2 nets T:16.5~31.5°C I:0.275~2.225M max 2n/1e

---

### Step 14: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_79 AND c.ligand_id = ligand_6277 AND c.beta_definition_id = beta_def_812",
  "order_by": "s.constant_value DESC",
  "limit": 5
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. You must call 0_plan_search_strategy first (PHASE 2) before using the execution tools.

---

### Step 15: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_79 AND c.ligand_id = ligand_6356 AND c.beta_definition_id = beta_def_812",
  "order_by": "s.constant_value DESC",
  "limit": 5
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. You must call 0_plan_search_strategy first (PHASE 2) before using the execution tools.

---

### Step 16: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_79 AND c.ligand_id = ligand_6165 AND c.beta_definition_id = beta_def_812",
  "order_by": "s.constant_value DESC",
  "limit": 5
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. You must call 0_plan_search_strategy first (PHASE 2) before using the execution tools.

---

### Step 17: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_79 AND c.ligand_id = ligand_9058 AND c.beta_definition_id = beta_def_812",
  "order_by": "s.constant_value DESC",
  "limit": 5
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. You must call 0_plan_search_strategy first (PHASE 2) before using the execution tools.

---

### Step 18: `search_stability`
**Args:**
```json
{
  "where": "c.metal_id = metal_79 AND c.ligand_id = ligand_8872 AND c.beta_definition_id = beta_def_812",
  "order_by": "s.constant_value DESC",
  "limit": 5
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. You must call 0_plan_search_strategy first (PHASE 2) before using the execution tools.

---
