# Q5.1.1 — Tool Results (batch 2)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "mercury",
  "symbol": "Hg",
  "limit": 50
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

### Step 4: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND s.constant_value IS NOT NULL)",
  "order_by": "s.constant_value DESC",
  "limit": 25
}
```

[summary]
## search_stability — 25 row(s)

### ΔS — 20 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_71 | Hg^[2+] | ligand_10076 | Hydroxide ion | *** | *** | 2 | 1 | 25 | 1~3 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6335 | Oxybis(ethylenenitrilo)tetr… | H4L | O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6794 | N-(6-Methyl-2-pyridylmethyl… | H2L | Cc1cccc(CN(CC(=O)O)CC(=O)O)n1 | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6793 | N-(2-Pyridylmethyl)iminodia… | H2L | O=C(O)CN(CC(=O)O)Cc1ccccn1 | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
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
| metal_71 | Hg^[2+] | ligand_10163 | Chloride ion | *** | *** | 1 | 1 | 25 | 3 | *** | 0 |
| metal_71 | Hg^[2+] | ligand_7582 | 1,4,10,13-Tetraoxa-7,16-dia… | L | C1COCCOCCNCCOCCOCCN1 | 1 | 1 | 25 | 0.1 | *** | 0 |

### ΔH — 1 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_71 | Hg^[2+] | ligand_10171 | Iodide ion | *** | *** | 1 | 1 | 25 | 0.5 | solid | 0 |

---

### Step 5: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_72 AND s.constant_value IS NOT NULL)",
  "order_by": "s.constant_value DESC",
  "limit": 25
}
```

[summary]
## search_stability — 25 row(s)

### ΔS — 2 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_72 | Hg^[+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_72 | Hg^[+] | ligand_10106 | Hydrogen azide (Hydrazoic a… | HL | [N-]=[N+]=N | 1 | 1 | 25 | 0 | solid | 0 |

### ΔH — 2 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_72 | Hg^[+] | ligand_10106 | Hydrogen azide (Hydrazoic a… | HL | [N-]=[N+]=N | 1 | 1 | 25 | 0 | solid | 0 |
| metal_72 | Hg^[+] | ligand_9677 | cis-syn-cis-2,5,8,15,18,21-… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |

### logK — 12 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_72 | Hg^[+] | ligand_10076 | Hydroxide ion | *** | *** | 4 | 3 | 25 | 0.5~3 | *** | 2 |
| metal_72 | Hg^[+] | ligand_10114 | Hydrogen diphosphate (Pyrop… | H4L | O=P(O)(O)OP(=O)(O)O | 2 | 2 | 27 | 0.7 | *** | 1 |
| metal_72 | Hg^[+] | ligand_10117 | Hydrogen triphosphate (Trip… | H5L | O=P(O)(O)OP(=O)(O)OP(=O)(O)O | 2 | 2 | 27 | 0.7 | *** | 1 |
| metal_72 | Hg^[+] | ligand_8887 | Propane-2,2-dicarboxylic ac… | H2L | CC(C)(C(=O)O)C(=O)O | 2 | 2 | 27 | 0.7 | *** | 1 |
| metal_72 | Hg^[+] | ligand_8907 | Butanedioic acid (Succinic … | H2L | O=C(O)CCC(=O)O | 2 | 2 | 27 | 2.5 | *** | 1 |
| metal_72 | Hg^[+] | ligand_8872 | Ethanedioic acid (Oxalic ac… | H2L | O=C(O)C(=O)O | 2 | 2 | 27 | 2.5 | *** | 1 |
| metal_72 | Hg^[+] | ligand_8467 | Propanoic acid (Propionic a… | HL | CCC(=O)O | 1 | 1 | 25 | 3 | *** | 1 |
| metal_72 | Hg^[+] | ligand_8465 | Ethanoic acid (Acetic acid) | HL | CC(=O)O | 1 | 1 | 25 | 3 | *** | 1 |
| metal_72 | Hg^[+] | ligand_8724 | 3-Methoxypropanoic acid | HL | COCCC(=O)O | 1 | 1 | 25 | 3 | *** | 1 |
| metal_72 | Hg^[+] | ligand_8640 | Hydroxyacetic acid (Glycoli… | HL | O=C(O)CO | 1 | 1 | 25 | 3 | *** | 1 |
| metal_72 | Hg^[+] | ligand_8464 | Methanoic acid (Formic acid) | HL | O=CO | 1 | 1 | 25 | 3 | *** | 1 |
| metal_72 | Hg^[+] | ligand_8721 | Methoxyacetic acid | HL | COCC(=O)O | 1 | 1 | 25 | 3 | *** | 1 |

---

### Step 6: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_93 AND s.constant_value IS NOT NULL)",
  "order_by": "s.constant_value DESC",
  "limit": 25
}
```

[summary]
## search_stability — 25 row(s)

### ΔS — 4 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_93 | MeHg^[+] | ligand_10076 | Hydroxide ion | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_93 | MeHg^[+] | ligand_10149 | Hydrogen thiosulfate (Thios… | H2L | O=S(O)(O)=S | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_93 | MeHg^[+] | ligand_9747 | 2-Mercaptoethanol | HL | OCCS | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_93 | MeHg^[+] | ligand_10163 | Chloride ion | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |

### logK — 14 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_93 | MeHg^[+] | ligand_5856 | L-2-Amino-3-mercaptopropano… | H2L | N[C@@H](CS)C(=O)O | 4 | 2 | 25 | 0.1~1 | *** | 2 |
| metal_93 | MeHg^[+] | ligand_9759 | 2,3-Dimercaptopropanol (BAL) | H2L | OCC(S)CS | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_93 | MeHg^[+] | ligand_9747 | 2-Mercaptoethanol | HL | OCCS | 2 | 2 | 20~25 | 0.1 | *** | 1 |
| metal_93 | MeHg^[+] | ligand_5857 | D-2-Amino-3-mercapto-3-meth… | H2L | CC(C)(S)[C@H](N)C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_93 | MeHg^[+] | ligand_6592 | L-5-Glutamyl-L-cysteinylgly… | H3L | N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 2 |
| metal_93 | MeHg^[+] | ligand_8995 | DL-Mercaptobutanedioic acid… | H3L | O=C(O)CC(S)C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_93 | MeHg^[+] | ligand_9761 | erythro-1,4-Dimercaptobutan… | H2L | OC(CS)C(O)CS | 1 | 1 | 25 | 0.5 | *** | 1 |
| metal_93 | MeHg^[+] | ligand_8766 | Mercaptoacetic acid (Thiogl… | H2L | O=C(O)CS | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_93 | MeHg^[+] | ligand_8773 | N-Acetyl-D-penicillamine | H2L | CC(=O)N[C@@H](C(=O)O)C(C)(C)S | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_93 | MeHg^[+] | ligand_10144 | Hydrogen sulfide (Hydrosulf… | H2L | S | 1 | 1 | 20 | 0.1 | *** | 1 |
| metal_93 | MeHg^[+] | ligand_7374 | 4-Mercapto-N-methylpiperidi… | HL | CN1CCC(S)CC1 | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_93 | MeHg^[+] | ligand_9750 | Mercaptoacetic acid methyl … | HL | COC(=O)CS | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_93 | MeHg^[+] | ligand_9724 | 2-Mercaptoethyltrimethylamm… | HL | C[N+](C)(C)CCS | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_93 | MeHg^[+] | ligand_9867 | 2-Hydroxyethyldiethylphosph… | L | CCP(CC)CCO | 1 | 1 | 20 | 1 | *** | 1 |

---

### Step 7: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_53 AND s.constant_value IS NOT NULL)",
  "order_by": "s.constant_value DESC",
  "limit": 25
}
```

[summary]
## search_stability — 6 row(s)

### `EtHg^[+]` + Chloride ion — 1 measurement(s)
metal_id: metal_53 | ligand_id: ligand_10163
ligand_HxL_def: *** | ligand_SMILES: ***

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_177475 | ref_eq_map_29766 | beta_def_812 | logK | 5.32 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] |  |

### `EtHg^[+]` + Iodide ion — 3 measurement(s)
metal_id: metal_53 | ligand_id: ligand_10171
ligand_HxL_def: *** | ligand_SMILES: ***

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_178460 | ref_eq_map_30072 | beta_def_888 | logK | 0.75 | 25 | 1 | `[ML2] + [L] <=> [ML3]` | *** | [L] |  |
| vlm_178459 | ref_eq_map_30072 | beta_def_868 | logK | -0.67 | 25 | 1 | `[ML] + [L] <=> [ML2]` | *** | [L] |  |
| vlm_178461 | ref_eq_map_30072 | beta_def_311 | logK | -4.11 | 25 | 1 | `[ML(s)] <=> [M] + [L]` | solid | [L] |  |

### `EtHg^[+]` + Hydrogen thiocyanate (Thiocyanic acid) — 2 measurement(s)
metal_id: metal_53 | ligand_id: ligand_10092
ligand_HxL_def: HL | ligand_SMILES: N=C=S

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_172363 | ref_eq_map_27875 | beta_def_888 | logK | 0.2 | 25 | 1 | `[ML2] + [L] <=> [ML3]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172362 | ref_eq_map_27875 | beta_def_868 | logK | -0.1 | 25 | 1 | `[ML] + [L] <=> [ML2]` | *** | [L] | (-1.1, L, +inf) |

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND (c.ligand_id = ligand_10163 OR c.ligand_id = ligand_10171) AND s.constant_value IS NOT NULL)",
  "order_by": "s.constant_value DESC",
  "limit": 50
}
```

[summary]
## search_stability — 50 row(s)

### `Hg^[2+]` + Iodide ion — 12 measurement(s)
metal_id: metal_71 | ligand_id: ligand_10171
ligand_HxL_def: *** | ligand_SMILES: ***

| equation | type | vlm_counts | ref_eq_map | value_range | T°C_range | I(M)_range | beta_defs | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|----------|------|------------|------------|-------------|-----------|------------|-----------|--------------------|--------------|-------------|
| `[ML2(s)] <=> [M] + [L]^2` | ΔH | 1 | *** | 172 | 25 | 0.5 | beta_def_334 | solid | [L] |  |
| `[ML2(s)] <=> [M] + [L]^2` | ΔS | 1 | *** | 42.3 | 25 | 0.5 | beta_def_334 | solid | [L] |  |
| `[M] + [L]^4 <=> [ML4]` | logK | 1 | ref_eq_map_30091 | 29.8 | 25 | 0.5 | beta_def_894 | *** | [L] |  |
| `[M] + [L]^3 <=> [ML3]` | logK | 1 | ref_eq_map_30091 | 27.6 | 25 | 0.5 | beta_def_872 | *** | [L] |  |
| `[M] + [L]^2 <=> [ML2]` | logK | 1 | ref_eq_map_30091 | 23.82 | 25 | 0.5 | beta_def_840 | *** | [L] |  |
| `[M] + [L] <=> [ML]` | logK | 1 | ref_eq_map_30091 | 12.87 | 25 | 0.5 | beta_def_812 | *** | [L] |  |
| `[M(OH)L] + [H] <=> [ML] + [H2O]` | logK | 1 | ref_eq_map_30091 | 4 | 25 | 0.5 | beta_def_966 | *** |  |  |
| `[M] + [L] <=> [ML]` | ΔS | 1 | *** | -6.3 | 25 | 0.5 | beta_def_812 | *** | [L] |  |
| `[M] + [L]^2 <=> [ML2]` | ΔS | 1 | *** | -24.3 | 25 | 0.5 | beta_def_840 | *** | [L] |  |
| `[ML2(s)] <=> [M] + [L]^2` | logK | 1 | ref_eq_map_30091 | -27.95 | 25 | 0.5 | beta_def_334 | solid | [L] |  |
| `[M] + [L]^4 <=> [ML4]` | ΔS | 1 | *** | -51.9 | 25 | 0.5 | beta_def_894 | *** | [L] |  |
| `[M] + [L] <=> [ML]` | ΔH | 1 | *** | -71.5 | 25 | 0 | beta_def_812 | *** | [L] |  |

Summary stats
| type | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|------|------------|-------------|-----------|------------|--------------------|-------------------|
| ΔH | 2 | 2 | 25 | 0~0.5 | solid | 0 |
| ΔS | 4 | 4 | 25 | 0.5 | solid | 0 |
| logK | 6 | 6 | 25 | 0.5 | solid | 1 |

### `Hg^[2+]` + Chloride ion — 38 measurement(s)
metal_id: metal_71 | ligand_id: ligand_10163
ligand_HxL_def: *** | ligand_SMILES: ***

| equation | type | vlm_counts | ref_eq_map | value_range | T°C_range | I(M)_range | beta_defs | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|----------|------|------------|------------|-------------|-----------|------------|-----------|--------------------|--------------|-------------|
| `[M] + [L]^3 <=> [ML3]` | ΔS | 2 | *** | 89.5~102.5 | 25 | 0.5~3 | beta_def_872 | *** | [L] |  |
| `[M] + [L]^4 <=> [ML4]` | ΔS | 2 | *** | 86.2~100.4 | 25 | 0.5~3 | beta_def_894 | *** | [L] |  |
| `[M] + [L]^2 <=> [ML2]` | ΔS | 2 | *** | 76.1~95 | 25 | 0.5~3 | beta_def_840 | *** | [L] |  |
| `[M] + [L] <=> [ML]` | ΔS | 2 | *** | 51.9~55.6 | 25 | 0.5~3 | beta_def_812 | *** | [L] |  |
| `[M] + [L]^4 <=> [ML4]` | logK | 5 | 5 diff ref_eq_map | 15.2~16.1 | 25 | 0~3 | beta_def_894 | *** | [L] |  |
| `[M] + [L]^3 <=> [ML3]` | logK | 5 | 5 diff ref_eq_map | 14.2~15.1 | 25 | 0~3 | beta_def_872 | *** | [L] |  |
| `[M] + [L]^2 <=> [ML2]` | logK | 4 | 4 diff ref_eq_map | 13.22~14 | 25 | 0~3 | beta_def_840 | *** | [L] |  |
| `[M] + [L] <=> [ML]` | logK | 4 | 4 diff ref_eq_map | 6.72~7.3 | 25 | 0~3 | beta_def_812 | *** | [L] |  |
| `[M(OH)L] + [H] <=> [ML] + [H2O]` | logK | 2 | ref_eq_map_29799; ref_eq_map_29800 | 3.05 | 25 | 1~3 | beta_def_966 | *** |  |  |
| `[M(OH)L] + [H] <=> [ML] + [H2O]` | ΔS | 1 | *** | -9.2 | 25 | 1 | beta_def_966 | *** |  |  |
| `[M(OH)L] + [H] <=> [ML] + [H2O]` | ΔH | 1 | *** | -20.1 | 25 | 1 | beta_def_966 | *** |  |  |
| `[M] + [L] <=> [ML]` | ΔH | 2 | *** | -24.3~-23 | 25 | 0.5~3 | beta_def_812 | *** | [L] |  |
| `[M] + [L]^2 <=> [ML2]` | ΔH | 2 | *** | -52.7~-51.5 | 25 | 0.5~3 | beta_def_840 | *** | [L] |  |
| `[M] + [L]^3 <=> [ML3]` | ΔH | 2 | *** | -55.6~-54.4 | 25 | 0.5~3 | beta_def_872 | *** | [L] |  |
| `[M] + [L]^4 <=> [ML4]` | ΔH | 2 | *** | -61.9~-61.1 | 25 | 0.5~3 | beta_def_894 | *** | [L] |  |

Summary stats
| type | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|------|------------|-------------|-----------|------------|--------------------|-------------------|
| ΔS | 9 | 5 | 25 | 0.5~3 | *** | 0 |
| logK | 20 | 5 | 25 | 0~3 | *** | 5 |
| ΔH | 9 | 5 | 25 | 0.5~3 | *** | 0 |

---
