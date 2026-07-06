# Q2.1.5 — Tool Results (batch 3)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Nickel(II)",
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
  "name": "ammonia",
  "limit": 10
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 10

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_10103 | Ammonia | L | Inorganic ligands | 447 | `N` | (-inf, HL, 9.26, L, +inf) |

---

### Step 4: `search_ligands`
**Args:**
```json
{
  "name": "ethylenediamine",
  "limit": 10
}
```

[summary]
## search_ligands — 10 result(s)

**stats:** 105 SQL matches · showing 10 · limit 10

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

### Step 5: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_112",
  "ligand_id": "ligand_10103"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 6 species

### Ni^[2+] + Ammonia
**metal_id:** metal_112 | **ligand_id:** ligand_10103 | **ligand_def_HxL:** L  
**entries:** 60 | **species:** 6 | **vlm_count:** 60

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 11 |
| beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | [M] + [L]^2 <=> [ML2] | [ML2](aqueous), [M](aqueous), [L](aqueous) | 13 |
| beta_def_872 | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | [M] + [L]^3 <=> [ML3] | [ML3](aqueous), [M](aqueous), [L](aqueous) | 10 |
| beta_def_894 | [ML<sub>4</sub>]/[M][L]<sup>4</sup> | [M] + [L]^4 <=> [ML4] | [ML4](aqueous), [M](aqueous), [L](aqueous) | 10 |
| beta_def_903 | [ML<sub>5</sub>]/[M][L]<sup>5</sup> | [M] + [L]^5 <=> [ML5] | [ML5](aqueous), [M](aqueous), [L](aqueous) | 8 |
| beta_def_907 | [ML<sub>6</sub>]/[M][L]<sup>6</sup> | [M] + [L]^6 <=> [ML6] | [ML6](aqueous), [M](aqueous), [L](aqueous) | 8 |

**vlm_ids:** vlm_173182, vlm_173183, vlm_173184, vlm_173185, vlm_173186, … vlm_173239, vlm_173240, vlm_173241 (60 listed)

**equilibrium_maps:** 5 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_28236 | 6 | 15 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_28237 | 6 | 15 | 19~29 °C | 1.85~2.15 M |
| ref_eq_net_28238 | 4 | 6 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_28239 | 2 | 1 | 19~29 °C | -0.15~0.15 M |
| ref_eq_net_28240 | 1 | 0 | 19~29 °C | 2.85~3.15 M |

---

### Step 7: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_112 AND c.ligand_id = ligand_10103 AND c.beta_definition_id = beta_def_812)",
  "order_by": "s.temperature_c ASC, s.ionic_strength_mol_l ASC, s.constant_value DESC",
  "limit": 50
}
```

[summary]
## search_stability — 11 row(s)

### `Ni^[2+]` + Ammonia — 11 measurement(s)
metal_id: metal_112 | ligand_id: ligand_10103
ligand_HxL_def: L | ligand_SMILES: N

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_173185 | ref_eq_map_28130 | beta_def_812 | logK | 2.72 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173190 | *** | beta_def_812 | ΔS | 1.7 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173186 | *** | beta_def_812 | ΔH | -15.1 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173182 | ref_eq_map_28127 | beta_def_812 | logK | 2.73 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173183 | ref_eq_map_28129 | beta_def_812 | logK | 2.8 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173191 | *** | beta_def_812 | ΔS | 1.7 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173187 | *** | beta_def_812 | ΔH | -15.5 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173184 | ref_eq_map_28128 | beta_def_812 | logK | 2.85 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173192 | *** | beta_def_812 | ΔS | 1.3 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173188 | *** | beta_def_812 | ΔH | -15.9 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |
| vlm_173189 | *** | beta_def_812 | ΔH | -16.3 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (9.26, L, +inf) |

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_112 AND c.ligand_id = ligand_7029)",
  "order_by": "s.temperature_c ASC, s.ionic_strength_mol_l ASC, s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability — 45 row(s)

### `Ni^[2+]` + Ethylenediamine — 45 measurement(s)
metal_id: metal_112 | ligand_id: ligand_7029
ligand_HxL_def: L | ligand_SMILES: NCCN

| equation | type | vlm_counts | ref_eq_map | value_range | T°C_range | I(M)_range | beta_defs | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|----------|------|------------|------------|-------------|-----------|------------|-----------|--------------------|--------------|-------------|
| `[M] + [L]^3 <=> [ML3]` | logK | 7 | 7 diff ref_eq_map | -19.7~19.18 | 25~37 | 0~3 | beta_def_872 | *** | [L] | (9.92, L, +inf) |
| `[M] + [L]^2 <=> [ML2]` | logK | 7 | 7 diff ref_eq_map | -14.77~14.53 | 25~37 | 0~3 | beta_def_840 | *** | [L] | (9.92, L, +inf) |
| `[M] + [L] <=> [ML]` | logK | 7 | 7 diff ref_eq_map | 6.98~7.9 | 25~37 | 0~3 | beta_def_812 | *** | [L] | (9.92, L, +inf) |
| `[M] + [L] <=> [ML]` | ΔS | 4 | *** | 0~18.4 | 25 | 0.1~3 | beta_def_812 | *** | [L] | (9.92, L, +inf) |
| `[M] + [L]^2 <=> [ML2]` | ΔS | 4 | *** | 0~10 | 25 | 0.1~3 | beta_def_840 | *** | [L] | (9.92, L, +inf) |
| `[M] + [L] <=> [ML]` | ΔH | 4 | *** | -37.7~0 | 25 | 0.1~3 | beta_def_812 | *** | [L] | (9.92, L, +inf) |
| `[M] + [L]^3 <=> [ML3]` | ΔS | 4 | *** | -58.2~0 | 25 | 0.1~3 | beta_def_872 | *** | [L] | (9.92, L, +inf) |
| `[M] + [L]^2 <=> [ML2]` | ΔH | 4 | *** | -76.6~0 | 25 | 0.1~3 | beta_def_840 | *** | [L] | (9.92, L, +inf) |
| `[M] + [L]^3 <=> [ML3]` | ΔH | 4 | *** | -117.6~0 | 25 | 0.1~3 | beta_def_872 | *** | [L] | (9.92, L, +inf) |

Summary stats
| type | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|------|------------|-------------|-----------|------------|--------------------|-------------------|
| logK | 21 | 3 | 25~37 | 0~3 | *** | 7 |
| ΔS | 12 | 3 | 25 | 0.1~3 | *** | 0 |
| ΔH | 12 | 3 | 25 | 0.1~3 | *** | 0 |

---
