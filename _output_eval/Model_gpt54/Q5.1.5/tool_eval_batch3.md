# Q5.1.5 — Tool Results (batch 3)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "calcium, magnesium, copper(II), zinc(II), iron(II), iron(III), nickel(II), cobalt(II), manganese(II), aluminum(III), lead(II), cadmium(II)",
  "limit": 20
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
  "name": "EDTA, ethylenediaminetetraacetic acid",
  "limit": 10
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 4: `search_metals`
**Args:**
```json
{
  "symbol": "Ca, Mg, Cu, Zn, Fe, Ni, Co, Mn, Al, Pb, Cd",
  "limit": 20
}
```

[summary]
## search_metals

*(no results)*

---

### Step 5: `search_ligands`
**Args:**
```json
{
  "name": "edta",
  "limit": 20
}
```

[summary]
## search_ligands — 5 result(s)

**stats:** 5 SQL matches · showing 5 · limit 20

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

### Step 6: `build_system_catalog`
**Args:**
```json
{
  "ligand_id": "ligand_6277"
}
```

[summary]
[CATALOG]
## build_system_catalog — 20 pair(s), 66 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_32 | [HL] + [H] <=> [H2L] |  |
| beta_def_53 | [H2L] + [H] <=> [H3L] |  |
| beta_def_64 | [H3L] + [H] <=> [H4L] |  |
| beta_def_68 | [H4L] + [H] <=> [H5L] |  |
| beta_def_72 | [H5L] + [H] <=> [H6L] |  |
| beta_def_79 | [L] + [H] <=> [HL] |  |
| beta_def_238 | [M(OH)2L] + [H] <=> [M(OH)L] + [H2O] |  |
| beta_def_423 | [ML]^2 + [H2O]^2 <=> [M2(OH)2L2] + [H]^2 |  |
| beta_def_427 | [M(OH)L]^2 <=> [M2(OH)2L2] |  |
| beta_def_502 | [M]^2 + [L] <=> [M2L] |  |
| beta_def_536 | [M2L] + [L] <=> [M2L2] |  |
| beta_def_570 | [M2(OH)L] + [H] <=> [M2L] + [H2O] |  |
| beta_def_662 | [M]^4 + [L]^2 + [H2O]^4 <=> [M4(OH)4L2] + [H]^4 |  |
| beta_def_699 | [M]^6 + [L]^3 + [H2O]^4 <=> [M6(OH)4L3] + [H]^4 |  |
| beta_def_739 | [MHL] + [H] <=> [MH2L] |  |
| beta_def_751 | [MH2L] + [H] <=> [MH3L] |  |
| beta_def_779 | [M] + [HL] <=> [MHL] |  |
| beta_def_788 | [ML] + [H] <=> [MHL] |  |
| beta_def_812 | [M] + [L] <=> [ML] |  |
| beta_def_966 | [M(OH)L] + [H] <=> [ML] + [H2O] |  |

*(all species aqueous)*

**1. H^[+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_68 + ligand_6277) — ligand_def_HxL: H4L | 75 ent, 6 sp, 75 vlms (vlm_108224…vlm_108298)
   - species: beta_def_32(18) beta_def_53(10) beta_def_64(7) beta_def_68(6) beta_def_72(4) beta_def_79(30)
   - eq:14 nets T:19~41°C I:-0.15~3.15M max 6n/15e
**2. Cd^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_26 + ligand_6277) — ligand_def_HxL: H4L | 23 ent, 4 sp, 23 vlms (vlm_108725…vlm_108747)
   - species: beta_def_739(1) beta_def_788(5) beta_def_812(14) beta_def_966(3)
   - eq:5 nets T:19~30°C I:-0.15~3.15M max 4n/5e
**3. Cu^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_41 + ligand_6277) — ligand_def_HxL: H4L | 20 ent, 4 sp, 20 vlms (vlm_108604…vlm_108623)
   - species: beta_def_739(2) beta_def_788(4) beta_def_812(8) beta_def_966(6)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 4n/5e
**4. Ni^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_112 + ligand_6277) — ligand_def_HxL: H4L | 19 ent, 4 sp, 19 vlms (vlm_108585…vlm_108603)
   - species: beta_def_739(1) beta_def_788(4) beta_def_812(8) beta_def_966(6)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 3n/3e
**5. Zn^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_208 + ligand_6277) — ligand_def_HxL: H4L | 18 ent, 4 sp, 18 vlms (vlm_108707…vlm_108724)
   - species: beta_def_739(1) beta_def_788(5) beta_def_812(6) beta_def_966(6)
   - eq:5 nets T:19~30°C I:-0.15~3.15M max 4n/5e
**6. Mg^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_92 + ligand_6277) — ligand_def_HxL: H4L | 18 ent, 2 sp, 18 vlms (vlm_108326…vlm_108343)
   - species: beta_def_788(2) beta_def_812(16)
   - eq:6 nets T:19~41°C I:-0.05~1.15M max 2n/1e
**7. Ca^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_25 + ligand_6277) — ligand_def_HxL: H4L | 18 ent, 2 sp, 18 vlms (vlm_108344…vlm_108361)
   - species: beta_def_788(2) beta_def_812(16)
   - eq:6 nets T:19~41°C I:-0.05~1.15M max 2n/1e
**8. Fe^[3+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_61 + ligand_6277) — ligand_def_HxL: H4L | 14 ent, 4 sp, 14 vlms (vlm_108639…vlm_108652)
   - species: beta_def_427(3) beta_def_788(3) beta_def_812(4) beta_def_966(4)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 3n/3e
**9. VO_[2]^[+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_202 + ligand_6277) — ligand_def_HxL: H4L | 13 ent, 4 sp, 13 vlms (vlm_108673…vlm_108685)
   - species: beta_def_739(5) beta_def_751(1) beta_def_788(5) beta_def_812(2)
   - eq:3 nets T:19~30°C I:-0.05~3.15M max 4n/4e
**10. Co^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_33 + ligand_6277) — ligand_def_HxL: H4L | 13 ent, 3 sp, 13 vlms (vlm_108572…vlm_108584)
   - species: beta_def_739(1) beta_def_788(4) beta_def_812(8)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 2n/1e
**11. Al^[3+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_5 + ligand_6277) — ligand_def_HxL: H4L | 13 ent, 4 sp, 13 vlms (vlm_108770…vlm_108782)
   - species: beta_def_238(2) beta_def_788(4) beta_def_812(3) beta_def_966(4)
   - eq:3 nets T:19~30°C I:-0.05~1.15M max 4n/5e
**12. La^[3+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_79 + ligand_6277) — ligand_def_HxL: H4L | 12 ent, 2 sp, 12 vlms (vlm_108389…vlm_108400)
   - species: beta_def_788(3) beta_def_812(9)
   - eq:4 nets T:15~30°C I:-0.05~1.15M max 2n/1e
**13. Nd^[3+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_110 + ligand_6277) — ligand_def_HxL: H4L | 11 ent, 2 sp, 11 vlms (vlm_108416…vlm_108426)
   - species: beta_def_788(2) beta_def_812(9)
   - eq:3 nets T:19~30°C I:-0.05~1.15M max 2n/1e
**14. Hg^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_71 + ligand_6277) — ligand_def_HxL: H4L | 11 ent, 4 sp, 11 vlms (vlm_108748…vlm_108758)
   - species: beta_def_739(1) beta_def_788(4) beta_def_812(5) beta_def_966(1)
   - eq:3 nets T:19~30°C I:-0.05~1.15M max 3n/3e
**15. Eu^[3+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_58 + ligand_6277) — ligand_def_HxL: H4L | 11 ent, 2 sp, 11 vlms (vlm_108438…vlm_108448)
   - species: beta_def_788(1) beta_def_812(10)
   - eq:3 nets T:19~30°C I:-0.05~1.15M max 1n/0e
**16. UO_[2]^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_195 + ligand_6277) — ligand_def_HxL: H4L | 10 ent, 6 sp, 10 vlms (vlm_108542…vlm_108551)
   - species: beta_def_502(2) beta_def_536(1) beta_def_570(1) beta_def_662(1) beta_def_699(1) beta_def_779(4)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 6n/13e
**17. Th^[4+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_185 + ligand_6277) — ligand_def_HxL: H4L | 10 ent, 4 sp, 10 vlms (vlm_108521…vlm_108530)
   - species: beta_def_423(2) beta_def_788(3) beta_def_812(4) beta_def_966(1)
   - eq:3 nets T:15~30°C I:-0.05~0.65M max 4n/6e
**18. Sm^[3+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_173 + ligand_6277) — ligand_def_HxL: H4L | 10 ent, 2 sp, 10 vlms (vlm_108428…vlm_108437)
   - species: beta_def_788(1) beta_def_812(9)
   - eq:3 nets T:19~30°C I:-0.05~1.15M max 1n/0e
**19. Sr^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_177 + ligand_6277) — ligand_def_HxL: H4L | 9 ent, 2 sp, 9 vlms (vlm_108362…vlm_108370)
   - species: beta_def_788(1) beta_def_812(8)
   - eq:2 nets T:20~41°C I:-0.05~0.3M max 2n/1e
**20. Na^[+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_106 + ligand_6277) — ligand_def_HxL: H4L | 9 ent, 1 sp, 9 vlms (vlm_108307…vlm_108315)
   - species: beta_def_812(9)
   - eq:3 nets T:19~30°C I:-0.05~1.15M max 1n/0e

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_6277 AND c.beta_definition_id = beta_def_812 AND s.solvent_name = 'water' AND s.temperature_c >= 24 AND s.temperature_c <= 26 AND s.ionic_strength_mol_l >= 0 AND s.ionic_strength_mol_l <= 0.15)",
  "order_by": "s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability

*(no results)*

---

### Step 9: `search_pka_values`
**Args:**
```json
{
  "where": "(lc.ligand_id = ligand_6277)",
  "order_by": "p.pKa ASC",
  "limit": 20
}
```

[summary]
## search_pka_values — 5 row(s)

### pKa -1.5–-1.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_108289 | ligand_6277 | Ethylenedinitrilotetraacetic acid … | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | -1.5 | 25 | 0.1 | H4L→H5L | M_tot_1 | M_tot_2 |

### pKa 2.0–2.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_108282 | ligand_6277 | Ethylenedinitrilotetraacetic acid … | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 25 | 0.1 | H3L→H4L | M_tot_2 | M_tot_2 |

### pKa 2.5–3.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_108272 | ligand_6277 | Ethylenedinitrilotetraacetic acid … | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2.69 | 25 | 0.1 | H2L→H3L | M_tot_2 | M_tot_1 |

### pKa 6.0–6.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_108254 | ligand_6277 | Ethylenedinitrilotetraacetic acid … | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 6.13 | 25 | 0.1 | HL→H2L | M_tot_1 | M_tot_7 |

### pKa 9.5–10.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_108224 | ligand_6277 | Ethylenedinitrilotetraacetic acid … | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 9.52 | 25 | 0.1 | L→HL | M_tot_7 | M_tot_70 |

---

### Step 10: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_6277 AND c.beta_definition_name = 'ML' AND s.solvent_name = 'water' AND s.temperature_c >= 24 AND s.temperature_c <= 26 AND s.ionic_strength_mol_l >= 0 AND s.ionic_strength_mol_l <= 0.15)",
  "order_by": "s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability

*(no results)*

---

### Step 11: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_6277 AND c.beta_definition_name = 'ML')",
  "order_by": "s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability

*(no results)*

---

### Step 12: `inspect_card`
**Args:**
```json
{
  "prefix_id": "ligand_6277"
}
```

[summary]
## inspect_card — Ligand | ligand_6277

**Name:** Ethylenedinitrilotetraacetic acid (EDTA)  
**Formula:** C10H16N2O8 | **Class:** EDTA and derivatives  
**SMILES:** `O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O`  
**InChI:** `InChI=1S/C10H16N2O8/c13-7(14)3-11(4-8(15)16)1-2-12(5-9(17)18)6-10(19)20/h1-6H2,(H,13,14)(H,15,16)(H,17,18)(H,19,20)`  
**HxL definition:** H4L  

**pKa values:** 5

| source_vlm | pKa | T (°C) | I (M) | From → To | Solvent | Method | Quality |
|------------|-----|--------|-------|-----------|---------|--------|---------|
| vlm_108289 | -1.50 | 25.0 | 0.1 | H4L → H5L | *** | *** | *** |
| vlm_108282 | 2.00 | 25.0 | 0.1 | H3L → H4L | *** | *** | *** |
| vlm_108272 | 2.69 | 25.0 | 0.1 | H2L → H3L | *** | *** | *** |
| vlm_108254 | 6.13 | 25.0 | 0.1 | HL → H2L | *** | *** | *** |
| vlm_108224 | 9.52 | 25.0 | 0.1 | L → HL | *** | *** | *** |

**Partners:** 75 metal(s), 596 measurement(s) total

| metal_id | Metal | # meas |
|----------|-------|--------|
| metal_68 | H^[+] | 75 |
| metal_26 | Cd^[2+] | 23 |
| metal_41 | Cu^[2+] | 20 |
| metal_112 | Ni^[2+] | 19 |
| metal_208 | Zn^[2+] | 18 |
| … | *(showing top 5 of 75)* | |

---

### Step 13: `search_networks`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_6277)",
  "order_by": "n.network_db_id ASC",
  "limit": 20
}
```

[summary]
## search_networks — 40 row(s)

> **Reference equilibrium networks** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### `H^[+]` + Ethylenedinitrilotetraacetic acid (EDTA) — 14 network(s)
metal_id: metal_68 | ligand_id: ligand_6277 | ligand_def_HxL: H4L | ligand_SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O

| beta_def | equation |
|----------|----------|
| beta_def_79 | ``[L] + [H] <=> [HL]`` |
| beta_def_68 | ``[H4L] + [H] <=> [H5L]`` |
| beta_def_53 | ``[H2L] + [H] <=> [H3L]`` |
| beta_def_64 | ``[H3L] + [H] <=> [H4L]`` |
| beta_def_32 | ``[HL] + [H] <=> [H2L]`` |
| beta_def_72 | ``[H5L] + [H] <=> [H6L]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_4906 | 5 | 10 | 20~30 | -0.05~0.25 | 5 | 5 diff beta_def | logK | -1.5~9.52 |
| ref_eq_net_4907 | 6 | 15 | 19~29 | 0.85~1.15 | 6 | 6 diff beta_def | logK | -1.4~8.73 |
| ref_eq_net_4908 | 5 | 10 | 31~41 | 0~0.3 | 5 | 5 diff beta_def | logK | -1.6~9.38 |
| ref_eq_net_4909 | 6 | 15 | 19~29 | 2.85~3.15 | 6 | 6 diff beta_def | logK | -1.7~9.05 |
| ref_eq_net_4910 | 2 | 1 | 19~29 | 0.35~0.65 | 2 | beta_def_32; beta_def_79 | logK | 6.1~8.86 |
| ref_eq_net_4911 | 2 | 1 | 19~29 | -0.05~0.25 | 2 | beta_def_32; beta_def_79 | logK | 6.273~10.19 |
| ref_eq_net_4912 | 1 | 0 | 31~41 | 0~0.3 | 1 | beta_def_79 | logK | 10.02 |
| ref_eq_net_4913 | 1 | 0 | 19~29 | 0.35~0.65 | 1 | beta_def_79 | logK | 9.62 |
| ref_eq_net_4914 | 1 | 0 | 19~29 | 0.85~1.15 | 1 | beta_def_79 | logK | 9.86 |
| ref_eq_net_4915 | 1 | 0 | 19~29 | -0.05~0.25 | 1 | beta_def_79 | logK | 10.37 |
| ref_eq_net_4916 | 1 | 0 | 31~41 | 0~0.3 | 1 | beta_def_79 | logK | 10.21 |
| ref_eq_net_4917 | 1 | 0 | 19~29 | 0.35~0.65 | 1 | beta_def_79 | logK | 10.23 |
| ref_eq_net_4918 | 1 | 0 | 19~29 | 0.85~1.15 | 1 | beta_def_79 | logK | 10.2 |
| ref_eq_net_4919 | 1 | 0 | 19~29 | -0.15~0.15 | 1 | beta_def_79 | logK | 10.948 |

#### Reference-state network: ref_eq_net_4906 (5 nodes)
> First network — reference conditions (T 20~30 °C, I -0.05~0.25 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_68 | ``[H4L] + [H] <=> [H5L]`` | logK | -1.5 |
| beta_def_64 | ``[H3L] + [H] <=> [H4L]`` | logK | 2 |
| beta_def_53 | ``[H2L] + [H] <=> [H3L]`` | logK | 2.69 |
| beta_def_32 | ``[HL] + [H] <=> [H2L]`` | logK | 6.13 |
| beta_def_79 | ``[L] + [H] <=> [HL]`` | logK | 9.52 |

### `Li^[+]` + Ethylenedinitrilotetraacetic acid (EDTA) — 3 network(s)
metal_id: metal_80 | ligand_id: ligand_6277 | ligand_def_HxL: H4L | ligand_SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O

| beta_def | equation |
|----------|----------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_4920 | 1 | 0 | 20~30 | -0.05~0.25 | 1 | beta_def_812 | logK | 2.95 |
| ref_eq_net_4921 | 1 | 0 | 19~29 | 0.35~0.65 | 1 | beta_def_812 | logK | 2.8 |
| ref_eq_net_4922 | 1 | 0 | 19~29 | 0.85~1.15 | 1 | beta_def_812 | logK | 2.76 |

#### Reference-state network: ref_eq_net_4920 (1 nodes)
> First network — reference conditions (T 20~30 °C, I -0.05~0.25 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 2.95 |

### `Na^[+]` + Ethylenedinitrilotetraacetic acid (EDTA) — 3 network(s)
metal_id: metal_106 | ligand_id: ligand_6277 | ligand_def_HxL: H4L | ligand_SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O

| beta_def | equation |
|----------|----------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` |

| network_id | node_counts | edge_counts | T_range | I_range | vlm_counts | beta_def_ids | type | values |
|------------|-------------|-------------|---------|---------|------------|--------------|------|--------|
| ref_eq_net_4923 | 1 | 0 | 20~30 | -0.05~0.25 | 1 | beta_def_812 | logK | 1.86 |
| ref_eq_net_4924 | 1 | 0 | 19~29 | 0.35~0.65 | 1 | beta_def_812 | logK | 1.77 |
| ref_eq_net_4925 | 1 | 0 | 19~29 | 0.85~1.15 | 1 | beta_def_812 | logK | 1.76 |

#### Reference-state network: ref_eq_net_4923 (1 nodes)
> First network — reference conditions (T 20~30 °C, I -0.05~0.25 M).

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 1.86 |

---
