# Q5.1.1 — Tool Results (batch 1)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "mercury(I)",
  "limit": 10
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

### Step 3: `search_metals`
**Args:**
```json
{
  "name": "mercury(II)",
  "limit": 10
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
  "where": "(c.metal_id = metal_71 AND c.ligand_name_SRD LIKE '%chloride%' AND s.temperature_c BETWEEN 24 AND 26)",
  "order_by": "s.temperature_c ASC, s.ionic_strength_mol_l ASC",
  "limit": 50
}
```

[summary]
## search_stability — 38 row(s)

### `Hg^[2+]` + Chloride ion — 38 measurement(s)
metal_id: metal_71 | ligand_id: ligand_10163
ligand_HxL_def: *** | ligand_SMILES: ***

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_177575 | ref_eq_map_29798 | beta_def_812 | logK | 7.3 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177583 | ref_eq_map_29798 | beta_def_840 | logK | 14 | 25 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_177592 | ref_eq_map_29798 | beta_def_872 | logK | 15 | 25 | 0 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_177601 | ref_eq_map_29798 | beta_def_894 | logK | 15.6 | 25 | 0 | `[M] + [L]^4 <=> [ML4]` | *** | [L] |  |
| vlm_177572 | ref_eq_map_29801 | beta_def_812 | logK | 6.74 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177576 | *** | beta_def_812 | ΔH | -23 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177578 | *** | beta_def_812 | ΔS | 51.9 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177580 | ref_eq_map_29801 | beta_def_840 | logK | 13.22 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_177584 | *** | beta_def_840 | ΔH | -52.7 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_177586 | *** | beta_def_840 | ΔS | 76.1 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_177588 | ref_eq_map_29801 | beta_def_872 | logK | 14.2 | 25 | 0.5 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_177593 | *** | beta_def_872 | ΔH | -54.4 | 25 | 0.5 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_177595 | *** | beta_def_872 | ΔS | 89.5 | 25 | 0.5 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_177597 | ref_eq_map_29801 | beta_def_894 | logK | 15.2 | 25 | 0.5 | `[M] + [L]^4 <=> [ML4]` | *** | [L] |  |
| vlm_177602 | *** | beta_def_894 | ΔH | -61.1 | 25 | 0.5 | `[M] + [L]^4 <=> [ML4]` | *** | [L] |  |
| vlm_177604 | *** | beta_def_894 | ΔS | 86.2 | 25 | 0.5 | `[M] + [L]^4 <=> [ML4]` | *** | [L] |  |
| vlm_177573 | ref_eq_map_29799 | beta_def_812 | logK | 6.72 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177581 | ref_eq_map_29799 | beta_def_840 | logK | 13.23 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_177589 | ref_eq_map_29799 | beta_def_872 | logK | 14.2 | 25 | 1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_177598 | ref_eq_map_29799 | beta_def_894 | logK | 15.3 | 25 | 1 | `[M] + [L]^4 <=> [ML4]` | *** | [L] |  |
| vlm_177606 | ref_eq_map_29799 | beta_def_966 | logK | 3.05 | 25 | 1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |
| vlm_177608 | *** | beta_def_966 | ΔH | -20.1 | 25 | 1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |
| vlm_177609 | *** | beta_def_966 | ΔS | -9.2 | 25 | 1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |
| vlm_177590 | ref_eq_map_29802 | beta_def_872 | logK | 14.7 | 25 | 2 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_177599 | ref_eq_map_29802 | beta_def_894 | logK | 15.7 | 25 | 2 | `[M] + [L]^4 <=> [ML4]` | *** | [L] |  |
| vlm_177574 | ref_eq_map_29800 | beta_def_812 | logK | 7.15 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177577 | *** | beta_def_812 | ΔH | -24.3 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177579 | *** | beta_def_812 | ΔS | 55.6 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_177582 | ref_eq_map_29800 | beta_def_840 | logK | 13.99 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_177585 | *** | beta_def_840 | ΔH | -51.5 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_177587 | *** | beta_def_840 | ΔS | 95 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_177591 | ref_eq_map_29800 | beta_def_872 | logK | 15.1 | 25 | 3 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_177594 | *** | beta_def_872 | ΔH | -55.6 | 25 | 3 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_177596 | *** | beta_def_872 | ΔS | 102.5 | 25 | 3 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_177600 | ref_eq_map_29800 | beta_def_894 | logK | 16.1 | 25 | 3 | `[M] + [L]^4 <=> [ML4]` | *** | [L] |  |
| vlm_177603 | *** | beta_def_894 | ΔH | -61.9 | 25 | 3 | `[M] + [L]^4 <=> [ML4]` | *** | [L] |  |
| vlm_177605 | *** | beta_def_894 | ΔS | 100.4 | 25 | 3 | `[M] + [L]^4 <=> [ML4]` | *** | [L] |  |
| vlm_177607 | ref_eq_map_29800 | beta_def_966 | logK | 3.05 | 25 | 3 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |

---

### Step 6: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.ligand_name_SRD LIKE '%bromide%' AND s.temperature_c BETWEEN 24 AND 26)",
  "order_by": "s.temperature_c ASC, s.ionic_strength_mol_l ASC",
  "limit": 50
}
```

[summary]
## search_stability — 28 row(s)

### `Hg^[2+]` + Bromide ion — 28 measurement(s)
metal_id: metal_71 | ligand_id: ligand_10168
ligand_HxL_def: *** | ligand_SMILES: ***

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_178151 | ref_eq_map_29988 | beta_def_812 | logK | 9.07 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_178153 | *** | beta_def_812 | ΔH | -42.3 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_178157 | *** | beta_def_812 | ΔS | 31.8 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_178159 | ref_eq_map_29988 | beta_def_840 | logK | 17.27 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_178161 | *** | beta_def_840 | ΔH | -87.4 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_178163 | *** | beta_def_840 | ΔS | 37.2 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_178165 | ref_eq_map_29988 | beta_def_872 | logK | 19.7 | 25 | 0.5 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_178167 | *** | beta_def_872 | ΔH | -99.2 | 25 | 0.5 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_178169 | *** | beta_def_872 | ΔS | 44.4 | 25 | 0.5 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_178171 | ref_eq_map_29988 | beta_def_894 | logK | 21.2 | 25 | 0.5 | `[M] + [L]^4 <=> [ML4]` | *** | [L] |  |
| vlm_178173 | *** | beta_def_894 | ΔH | -114.2 | 25 | 0.5 | `[M] + [L]^4 <=> [ML4]` | *** | [L] |  |
| vlm_178175 | *** | beta_def_894 | ΔS | 22.6 | 25 | 0.5 | `[M] + [L]^4 <=> [ML4]` | *** | [L] |  |
| vlm_178177 | ref_eq_map_29988 | beta_def_966 | logK | 3.37 | 25 | 0.5 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |
| vlm_178154 | *** | beta_def_812 | ΔH | -41.8 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_178155 | *** | beta_def_812 | ΔH | -41.4 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_178152 | ref_eq_map_29989 | beta_def_812 | logK | 9.4 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_178156 | *** | beta_def_812 | ΔH | -40.2 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_178158 | *** | beta_def_812 | ΔS | 45.2 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_178160 | ref_eq_map_29989 | beta_def_840 | logK | 17.98 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_178162 | *** | beta_def_840 | ΔH | -80.3 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_178164 | *** | beta_def_840 | ΔS | 74.5 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_178166 | ref_eq_map_29989 | beta_def_872 | logK | 20.7 | 25 | 3 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_178168 | *** | beta_def_872 | ΔH | -91.2 | 25 | 3 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_178170 | *** | beta_def_872 | ΔS | 90.4 | 25 | 3 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_178172 | ref_eq_map_29989 | beta_def_894 | logK | 22.2 | 25 | 3 | `[M] + [L]^4 <=> [ML4]` | *** | [L] |  |
| vlm_178174 | *** | beta_def_894 | ΔH | -109.6 | 25 | 3 | `[M] + [L]^4 <=> [ML4]` | *** | [L] |  |
| vlm_178176 | *** | beta_def_894 | ΔS | 56.9 | 25 | 3 | `[M] + [L]^4 <=> [ML4]` | *** | [L] |  |
| vlm_178178 | ref_eq_map_29989 | beta_def_966 | logK | 3.5 | 25 | 3 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |

---

### Step 7: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.ligand_name_SRD LIKE '%iodide%' AND s.temperature_c BETWEEN 24 AND 26)",
  "order_by": "s.temperature_c ASC, s.ionic_strength_mol_l ASC",
  "limit": 50
}
```

[summary]
## search_stability — 16 row(s)

### `Hg^[2+]` + Iodide ion — 16 measurement(s)
metal_id: metal_71 | ligand_id: ligand_10171
ligand_HxL_def: *** | ligand_SMILES: ***

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_178530 | *** | beta_def_812 | ΔH | -71.5 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_178538 | *** | beta_def_894 | ΔH | -181.2 | 25 | 0 | `[M] + [L]^4 <=> [ML4]` | *** | [L] |  |
| vlm_178529 | ref_eq_map_30091 | beta_def_812 | logK | 12.87 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_178531 | *** | beta_def_812 | ΔH | -75.3 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_178532 | *** | beta_def_812 | ΔS | -6.3 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] |  |
| vlm_178533 | ref_eq_map_30091 | beta_def_840 | logK | 23.82 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_178534 | *** | beta_def_840 | ΔH | -143.1 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_178535 | *** | beta_def_840 | ΔS | -24.3 | 25 | 0.5 | `[M] + [L]^2 <=> [ML2]` | *** | [L] |  |
| vlm_178536 | ref_eq_map_30091 | beta_def_872 | logK | 27.6 | 25 | 0.5 | `[M] + [L]^3 <=> [ML3]` | *** | [L] |  |
| vlm_178537 | ref_eq_map_30091 | beta_def_894 | logK | 29.8 | 25 | 0.5 | `[M] + [L]^4 <=> [ML4]` | *** | [L] |  |
| vlm_178539 | *** | beta_def_894 | ΔH | -185.4 | 25 | 0.5 | `[M] + [L]^4 <=> [ML4]` | *** | [L] |  |
| vlm_178540 | *** | beta_def_894 | ΔS | -51.9 | 25 | 0.5 | `[M] + [L]^4 <=> [ML4]` | *** | [L] |  |
| vlm_178541 | ref_eq_map_30091 | beta_def_966 | logK | 4 | 25 | 0.5 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |
| vlm_178542 | ref_eq_map_30091 | beta_def_334 | logK | -27.95 | 25 | 0.5 | `[ML2(s)] <=> [M] + [L]^2` | solid | [L] |  |
| vlm_178543 | *** | beta_def_334 | ΔH | 172 | 25 | 0.5 | `[ML2(s)] <=> [M] + [L]^2` | solid | [L] |  |
| vlm_178544 | *** | beta_def_334 | ΔS | 42.3 | 25 | 0.5 | `[ML2(s)] <=> [M] + [L]^2` | solid | [L] |  |

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.ligand_name_SRD LIKE '%cyanide%' AND s.temperature_c BETWEEN 24 AND 26)",
  "order_by": "s.temperature_c ASC, s.ionic_strength_mol_l ASC",
  "limit": 50
}
```

[summary]
## search_stability — 13 row(s)

### `Hg^[2+]` + Hydrogen cyanide (Hydrocyanic acid) — 13 measurement(s)
metal_id: metal_71 | ligand_id: ligand_10090
ligand_HxL_def: HL | ligand_SMILES: C#N

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_172056 | ref_eq_map_27747 | beta_def_812 | logK | 17 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.04, L, +inf) |
| vlm_172059 | *** | beta_def_812 | ΔH | -97.1 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.04, L, +inf) |
| vlm_172061 | *** | beta_def_812 | ΔS | -0.4 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (9.04, L, +inf) |
| vlm_172066 | ref_eq_map_27747 | beta_def_840 | logK | 32.75 | 25 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.04, L, +inf) |
| vlm_172069 | *** | beta_def_840 | ΔH | -195 | 25 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.04, L, +inf) |
| vlm_172071 | *** | beta_def_840 | ΔS | -27.6 | 25 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.04, L, +inf) |
| vlm_172075 | ref_eq_map_27747 | beta_def_872 | logK | 36.31 | 25 | 0 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (9.04, L, +inf) |
| vlm_172078 | *** | beta_def_872 | ΔH | -223.4 | 25 | 0 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (9.04, L, +inf) |
| vlm_172080 | *** | beta_def_872 | ΔS | -54.8 | 25 | 0 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (9.04, L, +inf) |
| vlm_172084 | ref_eq_map_27747 | beta_def_894 | logK | 38.97 | 25 | 0 | `[M] + [L]^4 <=> [ML4]` | *** | [L] | (9.04, L, +inf) |
| vlm_172087 | *** | beta_def_894 | ΔH | -249.8 | 25 | 0 | `[M] + [L]^4 <=> [ML4]` | *** | [L] | (9.04, L, +inf) |
| vlm_172089 | *** | beta_def_894 | ΔS | -94.1 | 25 | 0 | `[M] + [L]^4 <=> [ML4]` | *** | [L] | (9.04, L, +inf) |
| vlm_172064 | ref_eq_map_27752 | beta_def_840 | logK | 34.01 | 25 | 2 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.04, L, +inf) |

---

### Step 9: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.ligand_name_SRD LIKE '%thiocyanate%' AND s.temperature_c BETWEEN 24 AND 26)",
  "order_by": "s.temperature_c ASC, s.ionic_strength_mol_l ASC",
  "limit": 50
}
```

[summary]
## search_stability — 20 row(s)

### `Hg^[2+]` + Hydrogen thiocyanate (Thiocyanic acid) — 20 measurement(s)
metal_id: metal_71 | ligand_id: ligand_10092
ligand_HxL_def: HL | ligand_SMILES: N=C=S

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_172457 | ref_eq_map_27901 | beta_def_812 | logK | 9.64 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172458 | *** | beta_def_812 | ΔH | -49 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172460 | *** | beta_def_812 | ΔS | 20.1 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172463 | ref_eq_map_27901 | beta_def_840 | logK | 17.5 | 25 | 0 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172456 | ref_eq_map_27902 | beta_def_812 | logK | 9.08 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172459 | *** | beta_def_812 | ΔH | -50.2 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172461 | *** | beta_def_812 | ΔS | 5.4 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172462 | ref_eq_map_27902 | beta_def_840 | logK | 16.86 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172464 | *** | beta_def_840 | ΔH | -101.3 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172465 | *** | beta_def_840 | ΔS | -17.2 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172466 | ref_eq_map_27902 | beta_def_872 | logK | 19.7 | 25 | 1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172467 | *** | beta_def_872 | ΔH | -120.9 | 25 | 1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172468 | *** | beta_def_872 | ΔS | -28.9 | 25 | 1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172469 | ref_eq_map_27902 | beta_def_894 | logK | 21.7 | 25 | 1 | `[M] + [L]^4 <=> [ML4]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172470 | *** | beta_def_894 | ΔH | -141.8 | 25 | 1 | `[M] + [L]^4 <=> [ML4]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172471 | *** | beta_def_894 | ΔS | -60.7 | 25 | 1 | `[M] + [L]^4 <=> [ML4]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172472 | ref_eq_map_27902 | beta_def_966 | logK | 3.4 | 25 | 1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |
| vlm_172473 | *** | beta_def_966 | ΔH | -22.2 | 25 | 1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |
| vlm_172474 | *** | beta_def_966 | ΔS | -9.2 | 25 | 1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |
| vlm_172475 | ref_eq_map_27902 | beta_def_334 | logK | -19.56 | 25 | 1 | `[ML2(s)] <=> [M] + [L]^2` | solid | [L] | (-1.1, L, +inf) |

---

### Step 10: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND c.ligand_name_SRD LIKE '%thiosulfate%' AND s.temperature_c BETWEEN 24 AND 26)",
  "order_by": "s.temperature_c ASC, s.ionic_strength_mol_l ASC",
  "limit": 50
}
```

[summary]
## search_stability — 6 row(s)

### `Hg^[2+]` + Hydrogen thiosulfate (Thiosulfuric acid) — 6 measurement(s)
metal_id: metal_71 | ligand_id: ligand_10149
ligand_HxL_def: H2L | ligand_SMILES: O=S(O)(O)=S

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_176313 | ref_eq_map_29292 | beta_def_840 | logK | -29.93 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (-1.3, L, +inf) |
| vlm_176315 | ref_eq_map_29292 | beta_def_872 | logK | -33.26 | 25 | 1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (-1.3, L, +inf) |
| vlm_176317 | *** | beta_def_872 | ΔH | -161.1 | 25 | 1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (-1.3, L, +inf) |
| vlm_176318 | *** | beta_def_872 | ΔS | -96.2 | 25 | 1 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (-1.3, L, +inf) |
| vlm_176314 | ref_eq_map_29293 | beta_def_840 | logK | 29.23 | 25 | 3 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (-1.3, L, +inf) |
| vlm_176316 | ref_eq_map_29293 | beta_def_872 | logK | 30.6 | 25 | 3 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (-1.3, L, +inf) |

---

### Step 11: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND (c.ligand_name_SRD LIKE '%ammonia%' OR c.ligand_name_SRD LIKE '%ammine%') AND s.temperature_c BETWEEN 24 AND 26)",
  "order_by": "s.temperature_c ASC, s.ionic_strength_mol_l ASC",
  "limit": 50
}
```

[summary]
## search_stability — 8 row(s)

### `Hg^[2+]` + Ammonia — 8 measurement(s)
metal_id: metal_71 | ligand_id: ligand_10103
ligand_HxL_def: L | ligand_SMILES: N

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_173472 | ref_eq_map_28181 | beta_def_894 | logK | -19.3 | 25 | 0.1 | `[M] + [L]^4 <=> [ML4]` | *** | [L] | (9.26, L, +inf) |
| vlm_173465 | ref_eq_map_28183 | beta_def_840 | logK | -17.8 | 25 | 1 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.26, L, +inf) |
| vlm_173466 | ref_eq_map_28182 | beta_def_840 | logK | 17.3 | 25 | 2 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.26, L, +inf) |
| vlm_173468 | *** | beta_def_840 | ΔS | -15.9 | 25 | 2 | `[M] + [L]^2 <=> [ML2]` | *** | [L] | (9.26, L, +inf) |
| vlm_173469 | ref_eq_map_28182 | beta_def_872 | logK | 18.3 | 25 | 2 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (9.26, L, +inf) |
| vlm_173471 | *** | beta_def_872 | ΔS | -43.1 | 25 | 2 | `[M] + [L]^3 <=> [ML3]` | *** | [L] | (9.26, L, +inf) |
| vlm_173473 | ref_eq_map_28182 | beta_def_894 | logK | 19 | 25 | 2 | `[M] + [L]^4 <=> [ML4]` | *** | [L] | (9.26, L, +inf) |
| vlm_173475 | *** | beta_def_894 | ΔS | -80.3 | 25 | 2 | `[M] + [L]^4 <=> [ML4]` | *** | [L] | (9.26, L, +inf) |

---

### Step 12: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_71 AND (c.ligand_name_SRD LIKE '%EDTA%' OR c.ligand_name_SRD LIKE '%ethylenediaminetetraac%') AND s.temperature_c BETWEEN 24 AND 26)",
  "order_by": "s.temperature_c ASC, s.ionic_strength_mol_l ASC",
  "limit": 50
}
```

[summary]
## search_stability — 19 row(s)

### `Hg^[2+]` + N-(2-Hydroxyethyl)ethylenedinitrilotriacetic acid (HEDTA) — 5 measurement(s)
metal_id: metal_71 | ligand_id: ligand_6275
ligand_HxL_def: H3L | ligand_SMILES: O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_108158 | ref_eq_map_4878 | beta_def_812 | logK | 20.1 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.7, L, +inf) |
| vlm_108160 | *** | beta_def_812 | ΔH | -83.7 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.7, L, +inf) |
| vlm_108161 | *** | beta_def_812 | ΔS | 104.2 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.7, L, +inf) |
| vlm_108162 | ref_eq_map_4878 | beta_def_966 | logK | 8.4 | 25 | 0.1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |
| vlm_108159 | ref_eq_map_4879 | beta_def_812 | logK | 19.4 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.7, L, +inf) |

### `Hg^[2+]` + Ethylenedinitrilotetraacetic acid (EDTA) — 9 measurement(s)
metal_id: metal_71 | ligand_id: ligand_6277
ligand_HxL_def: H4L | ligand_SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_108748 | ref_eq_map_5060 | beta_def_812 | logK | 21.5 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108752 | *** | beta_def_812 | ΔS | 146.4 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108753 | ref_eq_map_5060 | beta_def_788 | logK | 3.2 | 25 | 0.1 | `[ML] + [H] <=> [MHL]` | *** |  |  |
| vlm_108755 | *** | beta_def_788 | ΔH | -2.9 | 25 | 0.1 | `[ML] + [H] <=> [MHL]` | *** |  |  |
| vlm_108756 | *** | beta_def_788 | ΔS | -51.5 | 25 | 0.1 | `[ML] + [H] <=> [MHL]` | *** |  |  |
| vlm_108758 | ref_eq_map_5060 | beta_def_966 | logK | 8.9 | 25 | 0.1 | `[M(OH)L] + [H] <=> [ML] + [H2O]` | *** |  |  |
| vlm_108749 | ref_eq_map_5062 | beta_def_812 | logK | 20.8 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108754 | ref_eq_map_5061 | beta_def_788 | logK | 3.1 | 25 | 1 | `[ML] + [H] <=> [MHL]` | *** |  |  |
| vlm_108757 | ref_eq_map_5061 | beta_def_739 | logK | 2.1 | 25 | 1 | `[MHL] + [H] <=> [MH2L]` | *** |  |  |

### `Hg^[2+]` + Oxybis(ethylenenitrilo)tetraacetic acid (EEDTA) — 3 measurement(s)
metal_id: metal_71 | ligand_id: ligand_6335
ligand_HxL_def: H4L | ligand_SMILES: O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_111817 | ref_eq_map_6375 | beta_def_812 | logK | 22.8 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.39, L, +inf) |
| vlm_111818 | *** | beta_def_812 | ΔH | -81.6 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.39, L, +inf) |
| vlm_111820 | *** | beta_def_812 | ΔS | 162.8 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.39, L, +inf) |

### `Hg^[2+]` + Thiobis(ethylenenitrilo)tetraacetic acid (TEDTA) — 2 measurement(s)
metal_id: metal_71 | ligand_id: ligand_6348
ligand_HxL_def: H4L | ligand_SMILES: O=C(O)CN(CCSCCN(CC(=O)O)CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_112310 | ref_eq_map_6557 | beta_def_812 | logK | 23.6 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.31, L, +inf) |
| vlm_112312 | *** | beta_def_812 | ΔS | 131.8 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.31, L, +inf) |

---

### Step 13: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_72 AND c.ligand_name_SRD LIKE '%chloride%' AND s.temperature_c BETWEEN 24 AND 26)",
  "order_by": "s.temperature_c ASC, s.ionic_strength_mol_l ASC",
  "limit": 50
}
```

[summary]
## search_stability — 4 row(s)

### `Hg^[+]` + Chloride ion — 4 measurement(s)
metal_id: metal_72 | ligand_id: ligand_10163
ligand_HxL_def: *** | ligand_SMILES: ***

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_177467 | ref_eq_map_29761 | beta_def_458 | logK | -17.91 | 25 | 0 | `[M2L2(s)] <=> [M]^2 + [L]^2` | solid | [L] |  |
| vlm_177468 | *** | beta_def_458 | ΔH | -92 | 25 | 0 | `[M2L2(s)] <=> [M]^2 + [L]^2` | solid | [L] |  |
| vlm_177469 | *** | beta_def_458 | ΔS | 0 | 25 | 0 | `[M2L2(s)] <=> [M]^2 + [L]^2` | solid | [L] |  |
| vlm_177466 | ref_eq_map_29762 | beta_def_458 | logK | -16.88 | 25 | 0.5 | `[M2L2(s)] <=> [M]^2 + [L]^2` | solid | [L] |  |

---

### Step 14: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_72 AND c.ligand_name_SRD LIKE '%bromide%' AND s.temperature_c BETWEEN 24 AND 26)",
  "order_by": "s.temperature_c ASC, s.ionic_strength_mol_l ASC",
  "limit": 50
}
```

[summary]
## search_stability — 4 row(s)

### `Hg^[+]` + Bromide ion — 4 measurement(s)
metal_id: metal_72 | ligand_id: ligand_10168
ligand_HxL_def: *** | ligand_SMILES: ***

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_178042 | ref_eq_map_29956 | beta_def_458 | logK | -22.25 | 25 | 0 | `[M2L2(s)] <=> [M]^2 + [L]^2` | solid | [L] |  |
| vlm_178041 | ref_eq_map_29957 | beta_def_458 | logK | -21.29 | 25 | 0.5 | `[M2L2(s)] <=> [M]^2 + [L]^2` | solid | [L] |  |
| vlm_178043 | *** | beta_def_458 | ΔH | -133.9 | 25 | 0.5 | `[M2L2(s)] <=> [M]^2 + [L]^2` | solid | [L] |  |
| vlm_178044 | *** | beta_def_458 | ΔS | -41.8 | 25 | 0.5 | `[M2L2(s)] <=> [M]^2 + [L]^2` | solid | [L] |  |

---

### Step 15: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_72 AND c.ligand_name_SRD LIKE '%iodide%' AND s.temperature_c BETWEEN 24 AND 26)",
  "order_by": "s.temperature_c ASC, s.ionic_strength_mol_l ASC",
  "limit": 50
}
```

[summary]
## search_stability — 4 row(s)

### `Hg^[+]` + Iodide ion — 4 measurement(s)
metal_id: metal_72 | ligand_id: ligand_10171
ligand_HxL_def: *** | ligand_SMILES: ***

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_178452 | ref_eq_map_30068 | beta_def_458 | logK | -28.34 | 25 | 0 | `[M2L2(s)] <=> [M]^2 + [L]^2` | solid | [L] |  |
| vlm_178451 | ref_eq_map_30069 | beta_def_458 | logK | -27.47 | 25 | 0.5 | `[M2L2(s)] <=> [M]^2 + [L]^2` | solid | [L] |  |
| vlm_178453 | *** | beta_def_458 | ΔH | -163.2 | 25 | 0.5 | `[M2L2(s)] <=> [M]^2 + [L]^2` | solid | [L] |  |
| vlm_178454 | *** | beta_def_458 | ΔS | -20.9 | 25 | 0.5 | `[M2L2(s)] <=> [M]^2 + [L]^2` | solid | [L] |  |

---

### Step 16: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_72 AND c.ligand_name_SRD LIKE '%cyanide%' AND s.temperature_c BETWEEN 24 AND 26)",
  "order_by": "s.temperature_c ASC, s.ionic_strength_mol_l ASC",
  "limit": 50
}
```

[summary]
## search_stability — 1 row(s)

### `Hg^[+]` + Hydrogen cyanide (Hydrocyanic acid) — 1 measurement(s)
metal_id: metal_72 | ligand_id: ligand_10090
ligand_HxL_def: HL | ligand_SMILES: C#N

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_171967 | ref_eq_map_27732 | beta_def_458 | logK | -39.3 | 25 | 0 | `[M2L2(s)] <=> [M]^2 + [L]^2` | solid | [L] | (9.04, L, +inf) |

---
