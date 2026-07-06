# Q2.1.6 — Tool Results (batch 1)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "cadmium, lead, mercury",
  "symbol": "Cd, Pb, Hg",
  "limit": 10
}
```

[summary]
## search_metals

*(no results)*

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "thiocyan",
  "limit": 50
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 50

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_10092 | Hydrogen thiocyanate (Thiocyanic acid) | HL | Inorganic ligands | 434 | `N=C=S` | (-inf, HL, -1.1, L, +inf) |

---

### Step 4: `search_metals`
**Args:**
```json
{
  "name": "Cadmium(II)",
  "limit": 10
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_26 | Cd^[2+] | Cd | 2 | ✓ | [Cd+2] | InChI=1S/Cd/q+2 | beta_totN_95 | ligand_totN_818 | vlm_totN_2828 |

---

### Step 5: `search_metals`
**Args:**
```json
{
  "name": "Lead(II)",
  "limit": 10
}
```

[summary]
## search_metals — 10 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_16 | Bu_[3]Pb^[+] | B | 1 |  | *** | *** | beta_totN_2 | ligand_totN_1 | vlm_totN_2 |
| metal_46 | Et_[2]Pb^[2+] | E2Pb | 2 |  | *** | *** | beta_totN_2 | ligand_totN_3 | vlm_totN_5 |
| metal_49 | Et_[3]Pb^[+] | E3Pb | 1 |  | *** | *** | beta_totN_2 | ligand_totN_3 | vlm_totN_5 |
| metal_84 | Me_[2]Pb^[2+] | M2Pb | 2 |  | *** | *** | beta_totN_5 | ligand_totN_4 | vlm_totN_9 |
| metal_87 | Me_[3]Pb^[+] | M3Pb | 1 |  | *** | *** | beta_totN_7 | ligand_totN_23 | vlm_totN_33 |
| metal_125 | Pb^[2+] | Pb | 2 | ✓ | [Pb+2] | InChI=1S/Pb/q+2 | beta_totN_80 | ligand_totN_470 | vlm_totN_1585 |
| metal_126 | Pb^[4+] | Pb | 4 | ✓ | [Pb+4] | InChI=1S/Pb/q+4 | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_129 | Ph_[2]Pb^[2+] | Ph2Pb | 2 |  | *** | *** | beta_totN_2 | ligand_totN_1 | vlm_totN_2 |
| metal_130 | Ph_[3]Pb^[+] | Ph3Pb | 1 |  | *** | *** | beta_totN_1 | ligand_totN_2 | vlm_totN_2 |
| metal_140 | Pr_[2]Pb^[2+] | Pr | 2 |  | *** | *** | beta_totN_2 | ligand_totN_3 | vlm_totN_5 |

---

### Step 6: `search_metals`
**Args:**
```json
{
  "name": "Mercury(II)",
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

### Step 8: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_26",
  "ligand_id": "ligand_10092"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 4 species

### Cd^[2+] + Hydrogen thiocyanate (Thiocyanic acid)
**metal_id:** metal_26 | **ligand_id:** ligand_10092 | **ligand_def_HxL:** HL  
**entries:** 51 | **species:** 4 | **vlm_count:** 51

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 15 |
| beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | [M] + [L]^2 <=> [ML2] | [ML2](aqueous), [M](aqueous), [L](aqueous) | 16 |
| beta_def_872 | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | [M] + [L]^3 <=> [ML3] | [ML3](aqueous), [M](aqueous), [L](aqueous) | 13 |
| beta_def_894 | [ML<sub>4</sub>]/[M][L]<sup>4</sup> | [M] + [L]^4 <=> [ML4] | [ML4](aqueous), [M](aqueous), [L](aqueous) | 7 |

**vlm_ids:** vlm_172405, vlm_172406, vlm_172407, vlm_172408, vlm_172409, … vlm_172453, vlm_172454, vlm_172455 (51 listed)

**equilibrium_maps:** 7 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_27996 | 4 | 6 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_27997 | 4 | 6 | 19~29 °C | 1.85~2.15 M |
| ref_eq_net_27998 | 4 | 6 | 19~29 °C | 0.35~0.65 M |
| ref_eq_net_27999 | 4 | 6 | 19~29 °C | 0.85~1.15 M |
| ref_eq_net_28000 | 4 | 6 | 19~29 °C | 2.85~3.15 M |
| ref_eq_net_28001 | 2 | 1 | 19~29 °C | -0.15~0.15 M |
| ref_eq_net_28002 | 1 | 0 | 19~29 °C | 1.85~2.15 M |

---

### Step 9: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_125",
  "ligand_id": "ligand_10092"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 3 species

### Pb^[2+] + Hydrogen thiocyanate (Thiocyanic acid)
**metal_id:** metal_125 | **ligand_id:** ligand_10092 | **ligand_def_HxL:** HL  
**entries:** 10 | **species:** 3 | **vlm_count:** 10

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 6 |
| beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | [M] + [L]^2 <=> [ML2] | [ML2](aqueous), [M](aqueous), [L](aqueous) | 3 |
| beta_def_872 | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | [M] + [L]^3 <=> [ML3] | [ML3](aqueous), [M](aqueous), [L](aqueous) | 1 |

**vlm_ids:** vlm_172483, vlm_172484, vlm_172485, vlm_172486, vlm_172487, vlm_172488, vlm_172489, vlm_172490, vlm_172491, vlm_172492

**equilibrium_maps:** 4 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_28008 | 3 | 3 | 16.5~31.5 °C | 2.775~3.225 M |
| ref_eq_net_28009 | 2 | 1 | 16.5~31.5 °C | 1.775~2.225 M |
| ref_eq_net_28010 | 2 | 1 | 16.5~31.5 °C | 3.775~4.225 M |
| ref_eq_net_28011 | 1 | 0 | 16.5~31.5 °C | 0.775~1.225 M |

---

### Step 10: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_71",
  "ligand_id": "ligand_10092"
}
```

[summary]
[CATALOG]
## build_system_catalog — 1 pair(s), 6 species

### Hg^[2+] + Hydrogen thiocyanate (Thiocyanic acid)
**metal_id:** metal_71 | **ligand_id:** ligand_10092 | **ligand_def_HxL:** HL  
**entries:** 20 | **species:** 6 | **vlm_count:** 20

| beta_definition_id | beta_definition_name | equation_str | phases | n_entries |
|--------------------|----------------------|--------------|--------|----------|
| beta_def_334 | [M][L]<sup>2</sup>/[ML<sub>2</sub>(s)] | [ML2(s)] <=> [M] + [L]^2 | [M](aqueous), [L](aqueous), [ML2(s)](solid) | 1 |
| beta_def_812 | [ML]/[M][L] | [M] + [L] <=> [ML] | [ML](aqueous), [M](aqueous), [L](aqueous) | 6 |
| beta_def_840 | [ML<sub>2</sub>]/[M][L]<sup>2</sup> | [M] + [L]^2 <=> [ML2] | [ML2](aqueous), [M](aqueous), [L](aqueous) | 4 |
| beta_def_872 | [ML<sub>3</sub>]/[M][L]<sup>3</sup> | [M] + [L]^3 <=> [ML3] | [ML3](aqueous), [M](aqueous), [L](aqueous) | 3 |
| beta_def_894 | [ML<sub>4</sub>]/[M][L]<sup>4</sup> | [M] + [L]^4 <=> [ML4] | [ML4](aqueous), [M](aqueous), [L](aqueous) | 3 |
| beta_def_966 | [ML]/[M(OH)L][H] | [M(OH)L] + [H] <=> [ML] + [H2O] | [ML](aqueous), [H2O](aqueous), [M(OH)L](aqueous), [H](aqueous) | 3 |

**vlm_ids:** vlm_172456, vlm_172457, vlm_172458, vlm_172459, vlm_172460, … vlm_172473, vlm_172474, vlm_172475 (20 listed)

**equilibrium_maps:** 2 preset reference network(s) *(clustered around room temperature & low ionic strength)*

| network_id | nodes | edges | T range | I range |
|------------|-------|-------|---------|---------|
| ref_eq_net_28003 | 2 | 1 | 20~30 °C | -0.05~0.25 M |
| ref_eq_net_28004 | 6 | 11 | 19~29 °C | 0.85~1.15 M |

---

### Step 12: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_10092 AND c.metal_id IN (metal_26, metal_125, metal_71) AND c.beta_definition_id = beta_def_812 AND s.temperature_c BETWEEN 20 AND 30)",
  "order_by": "s.ionic_strength_mol_l ASC, s.temperature_c ASC",
  "limit": 200
}
```

[summary]
## search_stability — 27 row(s)

### `Cd^[2+]` + Hydrogen thiocyanate (Thiocyanic acid) — 15 measurement(s)
metal_id: metal_26 | ligand_id: ligand_10092
ligand_HxL_def: HL | ligand_SMILES: N=C=S

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_172411 | ref_eq_map_27899 | beta_def_812 | logK | 1.93 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172412 | *** | beta_def_812 | ΔH | -13 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172416 | *** | beta_def_812 | ΔS | -6.7 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172405 | ref_eq_map_27894 | beta_def_812 | logK | 1.68 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172406 | ref_eq_map_27896 | beta_def_812 | logK | 1.35 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172413 | *** | beta_def_812 | ΔH | -9.2 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172417 | *** | beta_def_812 | ΔS | -5 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172407 | ref_eq_map_27897 | beta_def_812 | logK | 1.31 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172414 | *** | beta_def_812 | ΔH | -9.6 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172418 | *** | beta_def_812 | ΔS | -7.1 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172408 | ref_eq_map_27895 | beta_def_812 | logK | 1.09 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172409 | ref_eq_map_27900 | beta_def_812 | logK | 1.33 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172410 | ref_eq_map_27898 | beta_def_812 | logK | 1.39 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172415 | *** | beta_def_812 | ΔH | -10 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172419 | *** | beta_def_812 | ΔS | -7.1 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |

### `Hg^[2+]` + Hydrogen thiocyanate (Thiocyanic acid) — 6 measurement(s)
metal_id: metal_71 | ligand_id: ligand_10092
ligand_HxL_def: HL | ligand_SMILES: N=C=S

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_172457 | ref_eq_map_27901 | beta_def_812 | logK | 9.64 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172458 | *** | beta_def_812 | ΔH | -49 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172460 | *** | beta_def_812 | ΔS | 20.1 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172456 | ref_eq_map_27902 | beta_def_812 | logK | 9.08 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172459 | *** | beta_def_812 | ΔH | -50.2 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172461 | *** | beta_def_812 | ΔS | 5.4 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |

### `Pb^[2+]` + Hydrogen thiocyanate (Thiocyanic acid) — 6 measurement(s)
metal_id: metal_125 | ligand_id: ligand_10092
ligand_HxL_def: HL | ligand_SMILES: N=C=S

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_172487 | *** | beta_def_812 | ΔH | -1.3 | 25 | 0 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172483 | ref_eq_map_27909 | beta_def_812 | logK | 0.49 | 25 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172484 | ref_eq_map_27907 | beta_def_812 | logK | 0.54 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172488 | *** | beta_def_812 | ΔS | -25.1 | 25 | 2 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172485 | ref_eq_map_27906 | beta_def_812 | logK | 0.78 | 25 | 3 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |
| vlm_172486 | ref_eq_map_27908 | beta_def_812 | logK | 1.08 | 25 | 4 | `[M] + [L] <=> [ML]` | *** | [L] | (-1.1, L, +inf) |

---

### Step 13: `inspect_literature`
**Args:**
```json
{
  "prefix_id": "vlm_172407"
}
```

[summary]
## inspect_literature — vlm_172407 — 52 citation(s)

| lit_id | shortcut | citation |
|--------|----------|----------|
| lit_581 | 41L | I. Leden, Z. Phys. Chem., 1941, A188, 160 |
| lit_1002 | 51HDC | D. N. Hume, D. D. DeFord, and G. C. B. Cave, J. Amer. Chem. Soc., 1951, 73, 5323 |
| lit_1015 | 51KM | I. A. Korshunov, N. I. Malyugina, and O. M. Balabanova, J. Gen. Chem. USSR, 195… |
| lit_2407 | 57GB | A. M. Golub and O. G. Bilyk, J. Inorg. Chem. USSR, 1957, No.12, 58 (2723) |
| lit_2437 | 57JH | H. Q. Jiang and K. H. Hsu, Hua Hsueh Hsueh Pao (Acta Chim. Sinica), 1957, 23, 1… |
| lit_2552 | 57TS | Ya. I. Turyan and G. F. Serova, J. Inorg. Chem. USSR, 1957, 2, No. 2, 165 (336) |
| lit_3034 | 59TB | Ya. I. Turyan and N. I. Bondarenko, Russ. J. Inorg. Chem., 1959, 4, 486 (1070) |
| lit_3547 | 61SN | P. Senise and E. A. Neves, J. Amer. Chem. Soc., 1961, 83, 4146 |
| lit_3742 | 62KH | M. Kodama and K. Hanawa, Ibaraki Daigaku Bunrigakubu Kiyo, Shizen Kagaku, 1962,… |
| lit_4274 | 63TC | S. Tribalat and J. M. Caldero, J. Electroanal. Chem., 1963, 5, 176; Compt. Rend… |
| lit_4290 | 63VM | V. P. Vasilev and P. S. Mukhina, Russ. J. Inorg. Chem., 1963, 8, 986 (1895) |
| lit_4454 | 64KS | V. N. Kumok and V. V. Serebrennikov, Russ. J. Inorg. Chem., 1964, 9, 1160 (2148) |
| lit_4624 | 64TCa | S. Tribalat and J. M. Caldero, Compt. Rend. Acad. Sci. Paris, Sec. C, 1964, 258… |
| lit_4811 | 65HS | H. E. Hellwege and G. K. Schweitzer, J. Inorg. Nucl. Chem., 1965, 27, 99 |
| lit_5056 | 66AC | G. Alexandrides and C. Cummiskey, J. Inorg. Nucl. Chem., 1966, 28, 2025 |
| lit_5163 | 66Gb | P. Gerding, Acta Chem. Scand., 1966, 20, 2771 |
| lit_5582 | 67HB | A. A. Humffray, A. M. Bond, and J. S. Forrest, J. Electroanal. Chem., 1967, 15,… |
| lit_5716 | 67MSO | K. Momoki, H. Sato, and H. Ogawa, Anal. Chem., 1967, 39, 1072 |
| lit_5744 | 67NT | G. H. Nancollas and K. Torrance, Inorg. Chem., 1967, 6, 1567 |
| lit_6084 | 68GJa | P. Gerding and I. Jonsson, Acta Chem. Scand., 1968, 22, 2255 |
| lit_6066 | 68Gd | P. Gerding, Acta Chem. Scand., 1968, 22, 1283 |
| lit_6274 | 68Pc | B. Prasad, J. Indian Chem. Soc., 1968, 45, 1037 |
| lit_6651 | 69MO | K. Momoki, H. Ogawa, and H. Sato, Anal. Chem., 1969, 41, 1826 |
| lit_7402 | 71DDS | R. C. Das, A. C. Dash, D. Satyanarayan, and U. N. Dash, Thermochim. Acta, 1971,… |
| lit_7698 | 71PBb | M. Polasek and M. Bartusek, Scr. Fac. Sci. Nat. Univ. Purk. Brun., 1971, 1, 109 |
| lit_8591 | 73HH | M. H. Hutchinson and W. C. E. Higginson, J. Chem. Soc. Dalton, 1973, 1247 |
| lit_8812 | 73RS | C. Ruzycki, Yu. B. Solovev, and V. E. Mironov, Russ. J. Inorg. Chem., 1973, 18,… |
| lit_9203 | 74MM | M. H. Mihailov, V. Ts. Mihailova, and V. A. Khalkin, J. Inorg. Nucl. Chem., 197… |
| lit_9298 | 74RB | Ts. Ruzhitski, V. V. Blokhin, and V. E. Mironov, Russ. J. Phys. Chem., 1974, 48… |
| lit_9671 | 75Ma | L. Meites, Talanta, 1975, 22, 733 |
| lit_10039 | 76JBD | P. D. Jadhav, R. G. Bidkar, D. G. Dhuley, and R. A. Bhobe, J. Indian Chem. Soc.… |
| lit_10105 | 76LPa | S. C. Lal and B. Prasad, J. Indian Chem. Soc., 1976, 53, 136 |
| lit_10337 | 77ARM | A. Arevalo, J. C. Rodriguez Placeres, T. Moreno, and J. Segura, An. Real. Soc. … |
| lit_10722 | 78FN | D. W. Franco, E. A. Neves, and M. A. C. Dellatorre, Cienc. Cult. (Sao Paulo), 1… |
| lit_11183 | 79JBa | P. D. Jadhav and R. A. Bhobe, Indian J. Chem., 1979, 17A, 311 |
| lit_1624 | 80L | D. J. Leggett, Talanta, 1980, 27, 787 |
| lit_11848 | 81DDa | D. G. Dhuley and V. G. Dongre, Indian J. Chem., 1981, 20A, 426 |
| lit_11964 | 81KVS | Krishna, A. Varshney, and M. Singh, J. Inorg. Nucl. Chem., 1981, 43, 2075 |
| lit_12561 | 82TCN | V. A. Tsiplyakova, T. T. P. Chan, and T. B. Nguyen, Russ. J. Inorg. Chem., 1982… |
| lit_12568 | 82TP | V. A. Tsiplyakova, C. T. T. Phuong, and N. T. Bat, Russ. J. Inorg. Chem., 1982,… |
| lit_12691 | 83D | V. G. Dongre, Inorg. Chim. Acta, 1983, 73, 281 |
| lit_13055 | 83ZY | S. Zhang and J. Yang, Fenxi Huaxue, 1983, 11, 561 |
| lit_13252 | 84KKa | Krishna, R. Kulshrestha, M. Shivhare, and M. Singh, J. Electrochem. Soc. India,… |
| lit_13834 | 85SBA | J. A. Santaballa, C. Blanco, F. Arce, and J. Casado, Talanta, 1985, 32, 931 |
| lit_13914 | 85VN | N. C. F. Velloso, E. A. Neves, and I. G. R. Gutz, Polyhedron, 1985, 4, 2043 |
| lit_13986 | 86CA | E. Casassas and C. Arino, J. Electroanal. Chem., 1986, 213, 235 |
| lit_14082 | 86IY | S. Ishiguro, K. Yamamoto, and H. Ohtaki, Bull. Chem. Soc. Japan, 1986, 59, 1009 |
| lit_14311 | 86WM | G. S. Wang, J. Y. Miao, and X. H. Li, Hua Hsueh Hsueh Pao (Acta Chim. Sinica), … |
| lit_14986 | 88SMb | V. M. Samoilenko and O. G. Movchan, Soviet Progr. Chem. (Ukr. Khim. Zh.), 1988,… |
| lit_16495 | 93Ja | P. Janos, J. Chronatogr. A, 1993, 657, 435 |
| lit_18276 | 97BP | A. Bahta, G. A. Parker, and D. G. Tuck, Pure Appl. Chem., 1997, 69, 1489 |
| lit_17601 | 97USI | Y. Umebayashi, M. Shin, and S. Ishiguro, J. Coll. Int. Sci., 1997, 191, 391 |

---

### Step 14: `inspect_literature`
**Args:**
```json
{
  "prefix_id": "vlm_172483"
}
```

[summary]
## inspect_literature — vlm_172483 — 19 citation(s)

| lit_id | shortcut | citation |
|--------|----------|----------|
| lit_2253 | 56LS | G. W. Leonard, M. E. Smith, and D. N. Hume, J. Phys. Chem., 1956, 60, 1493 |
| lit_2413 | 57GS | A. M. Golub and V. M. Samoilenko, Ukr. Khim. Zh., 1957, 23, 17 |
| lit_2428 | 57I | A. Iwase, Nippon Kagaku Zasshi, 1957, 78, 1659 |
| lit_2734 | 58PD | F. Pantani and P. Desideri, Gazz. Chim. Ital., 1958, 88, 1183 |
| lit_2889 | 59GRS | A. M. Golub, L. I. Romanenko, and V. M. Samoilenko, Ukr. Khim. Zh., 1959, 25, 50 |
| lit_2902 | 59JH | H. Q. Jiang and K. H. Hsu, Kexue Tongbao, 1959, 331; Chem. Abstr., 1959, 53, 21… |
| lit_3042 | 59TS | Ya. I. Turyan and R. Ya. Shtipelman, Russ. J. Inorg. Chem., 1959, 4, 366 (808) |
| lit_3164 | 60GR | A. M. Golub and L. I. Romanenko, Ukr. Khim. Zh., 1960, 26, 418 |
| lit_3395 | 61GR | A. M. Golub and L. I. Romanenko, Ukr. Khim. Zh., 1961, 27, 11 |
| lit_4142 | 63MKT | V. E. Mironov, F. Ya. Kulba, and O. I. Trifonov, Russ. J. Inorg. Chem., 1963, 8… |
| lit_5744 | 67NT | G. H. Nancollas and K. Torrance, Inorg. Chem., 1967, 6, 1567 |
| lit_6485 | 69FS | V. A. Fedorov, N. P. Samsonova, and V. E. Mironov, Russ. J. Inorg. Chem., 1969,… |
| lit_7036 | 70FS | V. A. Fedorov, N. P. Samsonova, and V. E. Mironov, Russ. J. Inorg. Chem., 1970,… |
| lit_9203 | 74MM | M. H. Mihailov, V. Ts. Mihailova, and V. A. Khalkin, J. Inorg. Nucl. Chem., 197… |
| lit_11641 | 80RCM | J. C. Rodriquez Placeres, A. Cabrera Gonzalez, T. Moreno, and A. Arevalo, An. Q… |
| lit_11961 | 81KSa | S. Kusakabe and T. Sekine, Bull. Chem. Soc. Japan, 1981, 54, 2533 |
| lit_13252 | 84KKa | Krishna, R. Kulshrestha, M. Shivhare, and M. Singh, J. Electrochem. Soc. India,… |
| lit_13821 | 85RRS | J. C. Rodriguez Placeres, G. Ruiz Cabrera, J. A. Sanchez, and A. Arevalo, J. El… |
| lit_18276 | 97BP | A. Bahta, G. A. Parker, and D. G. Tuck, Pure Appl. Chem., 1997, 69, 1489 |

---

### Step 15: `inspect_literature`
**Args:**
```json
{
  "prefix_id": "vlm_172456"
}
```

[summary]
## inspect_literature — vlm_172456 — 19 citation(s)

| lit_id | shortcut | citation |
|--------|----------|----------|
| lit_47 | 05G | H. Grossmann, Z. Anorg. Allg. Chem., 1905, 43, 356 |
| lit_51 | 05SS | M. S. Sherrill and S. Skowronski, J. Amer. Chem. Soc., 1905, 27, 30 |
| lit_844 | 49KSa | I. A. Korshunov and M. K. Shchennikova, J. Gen. Chem. USSR, 1949, 19, 1820 (182… |
| lit_2313 | 56T | V. F. Toropova, J. Inorg. Chem. USSR, 1956, 1, No. 2, 56 (243) |
| lit_2338 | 56YT | K. B. Yatsimirskii and B. D. Tukhlov, J. Gen. Chem. USSR, 1956, 26, 377 (356) |
| lit_2414 | 57GT | A. M. Golub and T. I. Tsitsurina, Naukovi Zapiski Kiev Derzhav Univ., 1957, 16,… |
| lit_3242 | 60NA | C. J. Nyman and G. S. Alberts, Anal. Chem., 1960, 32, 207 |
| lit_3882 | 62TE | N. Tanaka, K. Ebata and T. Murayama, Bull. Chem. Soc. Japan, 1962, 35, 124 |
| lit_4600 | 64SK | T. D. Seth and R. C. Kapoor, J. Polarogr. Soc., 1964, 10, 17 |
| lit_6958 | 70CG | L. Ciavatta and M. Grimaldi, Inorg. Chim. Acta, 1970, 4, 312 |
| lit_7222 | 70SI | T. Sekine and T. Ishii, Bull. Chem. Soc. Japan, 1970, 43, 2422 |
| lit_7311 | 71AKb | S. Ahrland and L. Kullberg, Acta Chem. Scand., 1971, 25, 3692 |
| lit_9131 | 74KIH | H. Khalifa, F. M. Issa, and A. T. Haj-Hussein, Egypt. J. Chem., 1974, 17, 19 |
| lit_9113 | 74Kb | L. Kullberg, Acta Chem. Scand., 1974, A28, 979 |
| lit_9471 | 75CGP | L. Ciavatta, M. Grimaldi, and R. Palombari, J. Inorg. Nucl. Chem., 1975, 37, 16… |
| lit_9927 | 76CGP | L. Ciavatta, M. Grimaldi, and R. Palombari, J. Inorg. Nucl. Chem., 1976, 38, 823 |
| lit_13476 | 84VK | V. P. Vasilev, E. V. Kozlovskii, and A. A. Mokeev, Russ. J. Inorg. Chem., 1984,… |
| lit_14026 | 86EC | M. Esteban, E. Casassas, and L. Fernandez, Talanta, 1986, 33, 843 |
| lit_18276 | 97BP | A. Bahta, G. A. Parker, and D. G. Tuck, Pure Appl. Chem., 1997, 69, 1489 |

---
