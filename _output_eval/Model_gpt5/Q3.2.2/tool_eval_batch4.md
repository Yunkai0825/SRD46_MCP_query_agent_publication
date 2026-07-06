# Q3.2.2 — Tool Results (batch 4)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Nickel",
  "symbol": "Ni",
  "limit": 10
}
```

[summary]
## search_metals — 2 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_112 | Ni^[2+] | Ni | 2 | ✓ | [Ni+2] | InChI=1S/Ni/q+2 | beta_totN_149 | ligand_totN_1369 | vlm_totN_5325 |
| metal_113 | Ni^[3+] | Ni | 3 | ✓ | [Ni+3] | InChI=1S/Ni/q+3 | beta_totN_5 | ligand_totN_4 | vlm_totN_7 |

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "ethylenediamine",
  "limit": 50
}
```

[summary]
## search_ligands — 50 result(s)

**stats:** 105 SQL matches · showing 50 · limit 50

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5948 | N-(2-Aminoethyl)glycine (Ethylenediamine m… (EDMA) | HL | Amino Acids | 30 | `NCCNCC(=O)O` | (-inf, H3L, -1.9, H2L, 6.67, HL, 9.84, L, +inf) |
| ligand_6253 | N-(2-Aminoeth… (Ethylenediamine-N,N-diacetic acid) | H2L | NTA and derivatives | 39 | `NCCN(CC(=O)O)CC(=O)O` | (-inf, H2L, 5.53, HL, 10.87, L, +inf) |
| ligand_7029 | Ethylenediamine | L | Aliphatic amines | 310 | `NCCN` | (-inf, H2L, 7.11, HL, 9.92, L, +inf) |
| ligand_7030 | DL-Methylethylenediamine (1,2-Propylenediami… (pn) | L | Aliphatic amines | 86 | `CC(N)CN` | (-inf, H2L, 6.85, HL, 9.81, L, +inf) |
| ligand_7031 | DL-Ethylethylenediamine (1,2-Butylenediamine) | L | Aliphatic amines | 19 | `CCC(N)CN` | (-inf, H2L, 6.65, HL, 9.66, L, +inf) |
| ligand_7032 | DL-(2-Methyl-2-propyl)et… (t-Butylethylenediamine) | L | Aliphatic amines | 2 | `CC(C)(C)C(N)CN` | (-inf, H2L, 6.26, HL, 9.78, L, +inf) |
| ligand_7033 | 1,1-Dimethylethylenediamine | L | Aliphatic amines | 37 | `CC(C)(N)CN` | (-inf, H2L, 6.46, HL, 9.75, L, +inf) |
| ligand_7034 | DL-1,2-Dimethylethylened… (DL-2,3-Butylenediamine) | L | Aliphatic amines | 46 | `CC(N)C(C)N` | (-inf, H2L, 6.6, HL, 9.7, L, +inf) |
| ligand_7035 | meso-1,2-Dimethylethyl… (meso-2,3-Butylenediamine) | L | Aliphatic amines | 53 | `C[C@H](N)[C@@H](C)N` | (-inf, H2L, 6.63, HL, 9.76, L, +inf) |
| ligand_7036 | 1,1,2,2-Tetramethylethylenediamine | L | Aliphatic amines | 15 | `CC(C)(N)C(C)(C)N` | (-inf, H2L, 6.35, HL, 9.93, L, +inf) |
| ligand_7037 | Trimethylenediamine (1,3-Propylenediamine) | L | Aliphatic amines | 112 | `NCCCN` | (-inf, H2L, 8.78, HL, 10.54, L, +inf) |
| ligand_7038 | DL-1-Methyltrimethylenediam… (1,3-Butylenediamine) | L | Aliphatic amines | 30 | `CC(N)CCN` | (-inf, H2L, 8.68, HL, 10.55, L, +inf) |
| ligand_7039 | 2,2-Dimethylt… (2,2-Dimethyl-1,3-propylenediamine) | L | Aliphatic amines | 31 | `CC(C)(CN)CN` | (-inf, H2L, 8.18, HL, 10.22, L, +inf) |
| ligand_7040 | 2-Methylenetri… (2-Methylene-1,3-propylenediamine) | L | Aliphatic amines | 15 | `C=C(CN)CN` | (-inf, H2L, 8.33, HL, 10.09, L, +inf) |
| ligand_7041 | Tetramethylenediamine (1,4-Butylened… (Putrescine) | L | Aliphatic amines | 42 | `NCCCCN` | (-inf, H2L, 9.46, HL, 10.72, L, +inf) |
| ligand_7042 | Pentamethylenediamine (Cadaverine) | L | Aliphatic amines | 24 | `NCCCCCN` | (-inf, H2L, 9.83, HL, 10.9, L, +inf) |
| ligand_7043 | Hexamethylenediamine | L | Aliphatic amines | 16 | `NCCCCCCN` | (-inf, H2L, 10.07, HL, 10.95, L, +inf) |
| ligand_7044 | Octamethylenediamine | L | Aliphatic amines | 8 | `NCCCCCCCCN` | (-inf, H2L, 10.17, HL, 10.99, L, +inf) |
| ligand_7045 | Decamethylenediamine | L | Aliphatic amines | 8 | `NCCCCCCCCCCN` | (-inf, H2L, 10.25, HL, 10.97, L, +inf) |
| ligand_7052 | DL-1-Phenylethylenediamine | L | Aliphatic amines | 12 | `NCC(N)c1ccccc1` | (-inf, H2L, 6.01, HL, 8.85, L, +inf) |
| ligand_7059 | 1,3-Diamino-2-prop… (2-Hydroxytrimethylenediamine) | L | Aliphatic amines | 54 | `NCC(O)CN` | (-inf, H2L, 8.02, HL, 9.56, L, +inf) |
| ligand_7066 | N,N'-Diglycylethylenediamine (DGEN) | L | Aliphatic amines | 30 | `NCC(=O)NCCNC(=O)CN` | (-inf, H2L, 7.48, HL, 8.22, L, +inf) |
| ligand_7069 | N,N'-Di-L-alanylethylenediamine (DAEN) | L | Aliphatic amines | 7 | `C[C@H](N)C(=O)NCCNC(=O)[C@H](C)N` | (-inf, H2L, 7.3, HL, 8.34, L, +inf) |
| ligand_7072 | N,N'-Diglycyltrimethylenediamine | L | Aliphatic amines | 9 | `NCC(=O)NCCCNC(=O)CN` | (-inf, H2L, 7.72, HL, 8.4, L, +inf) |
| ligand_7073 | N,N'-Diglycyltetramethylenediamine | L | Aliphatic amines | 6 | `NCC(=O)NCCCCNC(=O)CN` | (-inf, H2L, 7.78, HL, 8.41, L, +inf) |
| ligand_7074 | N,N'-Diglycylpentamethylenediamine | L | Aliphatic amines | 6 | `NCC(=O)NCCCCCNC(=O)CN` | (-inf, H2L, 7.73, HL, 8.36, L, +inf) |
| ligand_7075 | N,N'-Diglycylhexamethylenediamine | L | Aliphatic amines | 6 | `NCC(=O)NCCCCCCNC(=O)CN` | (-inf, H2L, 7.78, HL, 8.41, L, +inf) |
| ligand_7076 | N,N'-Diglycyloctamethylenediamine | L | Aliphatic amines | 4 | `NCC(=O)NCCCCCCCCNC(=O)CN` | (-inf, H2L, 7.75, HL, 8.41, L, +inf) |
| ligand_7161 | N-Methylethylenediamine | L | Aliphatic amines seconda… | 79 | `CNCCN` | (-inf, H2L, 7.04, HL, 10.11, L, +inf) |
| ligand_7162 | N-Ethylethylenediamine | L | Aliphatic amines seconda… | 31 | `CCNCCN` | (-inf, H2L, 7.1, HL, 10.16, L, +inf) |
| ligand_7163 | N-Propylethylenediamine | L | Aliphatic amines seconda… | 7 | `CCCNCCN` | (-inf, H2L, -7.39, HL, 10.19, L, +inf) |
| ligand_7164 | N-2-Propylethylenedi… (N-Isopropylethylenediamine) | L | Aliphatic amines seconda… | 10 | `CC(C)NCCN` | (-inf, H2L, 7.11, HL, 10.19, L, +inf) |
| ligand_7165 | N-Butylethylenediamine | L | Aliphatic amines seconda… | 7 | `CCCCNCCN` | (-inf, H2L, -7.38, HL, 10.15, L, +inf) |
| ligand_7166 | 2-(2-Pro… (N-2-Propyl-2,2-dimethylethylenediamine) | L | Aliphatic amines seconda… | 24 | `CC(C)NCC(C)(C)N` | (-inf, H2L, 6.6, HL, 10.07, L, +inf) |
| ligand_7167 | N-Methyltrimethylenediamine | L | Aliphatic amines seconda… | 10 | `CNCCCN` | (-inf, H2L, 8.74, HL, 10.62, L, +inf) |
| ligand_7168 | 2-(Cyc… (N-Cyclohexyl-2,2-dimethylethylenediamine) | L | Aliphatic amines seconda… | 6 | `CC(C)(N)CNC1CCCCC1` | (-inf, H2L, 6.77, HL, 10.18, L, +inf) |
| ligand_7169 | N-Benzylethylenediamine | L | Aliphatic amines seconda… | 4 | `NCCNCc1ccccc1` | (-inf, H2L, 6.48, HL, 9.41, L, +inf) |
| ligand_7170 | N-(4-Methylbenzyl)ethylenediamine | L | Aliphatic amines seconda… | 4 | `Cc1ccc(CNCCN)cc1` | (-inf, H2L, 6.51, HL, 9.41, L, +inf) |
| ligand_7171 | N-(2-Phenylethyl)ethylenediamine | L | Aliphatic amines seconda… | 4 | `NCCNCCc1ccccc1` | (-inf, H2L, 6.59, HL, 9.44, L, +inf) |
| ligand_7172 | N,N'-Dimethylethylenediamine | L | Aliphatic amines seconda… | 83 | `CNCCNC` | (-inf, H2L, 7.04, HL, 10.05, L, +inf) |
| ligand_7173 | N,N'-Diethylethylenediamine | L | Aliphatic amines seconda… | 45 | `CCNCCNCC` | (-inf, H2L, 7.28, HL, 10.16, L, +inf) |
| ligand_7174 | N,N'-Di-2-propylethylenediamine | L | Aliphatic amines seconda… | 2 | `CC(C)NCCNC(C)C` | (-inf, H2L, 7.44, HL, 10.25, L, +inf) |
| ligand_7175 | N,N'-Dipropylethylenediamine | L | Aliphatic amines seconda… | 6 | `CCCNCCNCCC` | (-inf, H2L, 7.38, HL, 10.12, L, +inf) |
| ligand_7176 | N,N'-Dibutylethylenediamine | L | Aliphatic amines seconda… | 5 | `CCCCNCCNCCCC` | (-inf, H2L, 7.31, HL, 10.04, L, +inf) |
| ligand_7177 | N,N'-Dimethyltrimethylenediamine | L | Aliphatic amines seconda… | 12 | `CNCCCNC` | (-inf, H2L, 8.81, HL, 10.64, L, +inf) |
| ligand_7178 | N,N'-Dimethyl-2-methylenetrimethylenediamine | L | Aliphatic amines seconda… | 2 | `C=C(CNC)CNC` | (-inf, H2L, 8.39, HL, 10.42, L, +inf) |
| ligand_7179 | N-(2-Hydroxybenzyl)ethylenediamine (HBEN) | HL | Aliphatic amines seconda… | 3 | `NCCNCc1ccccc1O` | (-inf, H3L, 6.89, H2L, 9.49, HL, 9.49, L, +inf) |
| ligand_7180 | Ethylenebis(iminomethylene-2-phenol) [N,N'-Bis(2-… | H2L | Aliphatic amines seconda… | 7 | `Oc1ccccc1CNCCNCc1ccccc1O` | (-inf, H4L, 6.17, H3L, 8.37, H2L, 9.8, HL, 10.5, L, +inf) |
| ligand_7181 | 2-(2-Aminoethylamino)ethanol [N-(2-Hydroxyethyl)e… | L | Aliphatic amines seconda… | 68 | `NCCNCCO` | (-inf, H2L, 6.55, HL, 9.56, L, +inf) |
| ligand_7182 | DL-1-(2-Aminoethylamino)-2-propanol [N-(2-Hydroxy… | L | Aliphatic amines seconda… | 6 | `CC(O)CNCCN` | (-inf, H2L, 6.78, HL, 9.62, L, +inf) |

### Functional groups across all SQL matches (85 parseable SMILES)

| group | count | % |
|-------|-------|---|
| primary_amine | 58 | 68% |
| secondary_amine | 43 | 51% |
| tertiary_amine | 23 | 27% |
| hydroxyl | 14 | 16% |
| aromatic_ring | 13 | 15% |
| amide | 7 | 8% |
| phosphonate | 4 | 5% |
| thioether | 4 | 5% |
| phenol | 3 | 4% |
| pyridine | 3 | 4% |
| carboxyl | 2 | 2% |
| sulfonate | 1 | 1% |
| thiol | 1 | 1% |

---

### Step 4: `search_ligands`
**Args:**
```json
{
  "name": "1,2-diaminoethane",
  "limit": 50
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 5 SQL matches · showing 5 · limit 50

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6343 | N,N'-Diglycyl-1,2-diaminoethane-N'',N'',… (DGENTA) | H4L | EDTA and derivatives | 24 | `O=C(O)CN(CC(=O)O)CC(=O)NCCNC(=O)CN(CC(=O)O)CC(=O)O` | (-inf, H5L, -1.2, H4L, -1.2, H3L, 2.65, H2L, 6.15, HL, 7.28, L, +inf) |
| ligand_6345 | N-(Glycylglycyl)-1,2-diaminoethane-N',N'… (GGENTA) | *** | EDTA and derivatives | 16 | *** | (-inf, H4L, 2.1, H3L, 2.9, H2L, 6.2, HL, 8.7, L, +inf) |
| ligand_8177 | Ethylenebis(aminomethylene-2-pyridine) (N,N'-Bis(… | L | Bipyridines | 40 | `c1ccc(CNCCNCc2ccccn2)nc1` | (-inf, H4L, -1.6, H3L, -1.6, H2L, 5.4, HL, 8.22, L, +inf) |
| ligand_8182 | Ethylenebis(aminoethylene-2-pyridine) (N,N'-Bis(2… | L | Bipyridines | 15 | `c1ccc(CCNCCNCCc2ccccn2)nc1` | (-inf, H3L, 3.69, H2L, 6.82, HL, 9.83, L, +inf) |
| ligand_8183 | Ethylenebis(aminoethylene-3-pyridine) (N,N'-Bis(3… | L | Bipyridines | 11 | `c1cncc(CCNCCNCCc2cccnc2)c1` | (-inf, H3L, 4.61, H2L, 6.76, HL, 9.78, L, +inf) |

### Functional groups across all SQL matches (4 parseable SMILES)

| group | count | % |
|-------|-------|---|
| aromatic_ring | 3 | 75% |
| pyridine | 3 | 75% |
| secondary_amine | 3 | 75% |
| amide | 1 | 25% |
| carboxyl | 1 | 25% |
| tertiary_amine | 1 | 25% |

---

### Step 5: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_112",
  "ligand_id": "ligand_7029"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 3 species

### Ni^[2+] + Ethylenediamine
**metal_id:** metal_112 | **ligand_id:** ligand_7029 | **ligand_def_HxL:** L  
**entries:** 45 | **species:** 3 | **vlm_count:** 45

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 15 |
| beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | [M] + [L]^2 <=> [ML2] | [ML2](aqueous), [M](aqueous), [L](aqueous) | 15 |
| beta_def_872 | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | [M] + [L]^3 <=> [ML3] | [ML3](aqueous), [M](aqueous), [L](aqueous) | 15 |

**vlm_ids:** vlm_122365, vlm_122366, vlm_122367, vlm_122368, vlm_122369, … vlm_122407, vlm_122408, vlm_122409 (45 listed)

**equilibrium_maps:** 7 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_9591 | 3 | 3 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_9592 | 3 | 3 | 31~41 °C | 0~0.3 M |
| ref_eq_net_9593 | 3 | 3 | 19~29 °C | 0.35~0.65 M |
| ref_eq_net_9594 | 3 | 3 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_9595 | 3 | 3 | 19~29 °C | 1.85~2.15 M |
| ref_eq_net_9596 | 3 | 3 | 19~29 °C | 2.85~3.15 M |
| ref_eq_net_9597 | 3 | 3 | 19~29 °C | -0.15~0.15 M |

---

### Step 7: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_112 AND c.ligand_id = ligand_7029 AND c.beta_definition_id IN (beta_def_812, beta_def_840) AND s.temperature_c BETWEEN 19 AND 29 AND s.ionic_strength_mol_l IS NOT NULL)",
  "order_by": "c.beta_definition_id, s.electrolyte_composition, s.ionic_strength_mol_l ASC",
  "limit": 200
}
```

[summary]
## search_stability — 28 row(s)

### `Ni^[2+]` + Ethylenediamine — 28 measurement(s)
metal_id: metal_112 | ligand_id: ligand_7029
ligand_HxL_def: L | ligand_SMILES: NCCN

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_122371 | ref_eq_map_9574 | beta_def_812 | logK | 7.32 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122365 | ref_eq_map_9568 | beta_def_812 | logK | 7.3 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122372 | *** | beta_def_812 | ΔH | 0 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122376 | *** | beta_def_812 | ΔS | 9.2 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122367 | ref_eq_map_9570 | beta_def_812 | logK | 7.45 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122373 | *** | beta_def_812 | ΔH | -37.7 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122377 | *** | beta_def_812 | ΔS | 16.3 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122368 | ref_eq_map_9571 | beta_def_812 | logK | 7.56 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122374 | *** | beta_def_812 | ΔH | -37.7 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122378 | *** | beta_def_812 | ΔS | 18.4 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122369 | ref_eq_map_9572 | beta_def_812 | logK | 7.9 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122370 | ref_eq_map_9573 | beta_def_812 | logK | 7.87 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122375 | *** | beta_def_812 | ΔH | 0 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122379 | *** | beta_def_812 | ΔS | 0 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (9.92, L, +inf) |
| vlm_122386 | ref_eq_map_9574 | beta_def_840 | logK | 13.5 | 25 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122380 | ref_eq_map_9568 | beta_def_840 | logK | 13.44 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122387 | *** | beta_def_840 | ΔH | -75.7 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122391 | *** | beta_def_840 | ΔS | 2.9 | 25 | 0.1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122382 | ref_eq_map_9570 | beta_def_840 | logK | 13.7 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122388 | *** | beta_def_840 | ΔH | -76.1 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122392 | *** | beta_def_840 | ΔS | 6.7 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122383 | ref_eq_map_9571 | beta_def_840 | logK | 13.95 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122389 | *** | beta_def_840 | ΔH | -76.6 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122393 | *** | beta_def_840 | ΔS | 10 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122384 | ref_eq_map_9572 | beta_def_840 | logK | -14.77 | 25 | 2 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122385 | ref_eq_map_9573 | beta_def_840 | logK | 14.53 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122390 | *** | beta_def_840 | ΔH | 0 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |
| vlm_122394 | *** | beta_def_840 | ΔS | 0 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.92, L, +inf) |

---
