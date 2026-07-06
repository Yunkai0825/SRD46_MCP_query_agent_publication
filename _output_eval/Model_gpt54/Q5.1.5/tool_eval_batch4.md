# Q5.1.5 — Tool Results (batch 4)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Fe(III), Fe(II), Cu(II), Zn(II), Ni(II), Co(II), Mn(II), Al(III), Ca(II), Mg(II), Pb(II), Cd(II)",
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

### Step 5: `build_system_catalog`
**Args:**
```json
{}
```

[summary]
[CATALOG]
## build_system_catalog

**Error:** Provide at least one of metal_id, ligand_id, or beta_definition_id.

---

### Step 6: `search_metals`
**Args:**
```json
{
  "symbol": "Fe, Cu, Zn, Ni, Co, Mn, Al, Ca, Mg, Pb, Cd",
  "limit": 20
}
```

[summary]
## search_metals

*(no results)*

---

### Step 7: `search_ligands`
**Args:**
```json
{
  "name": "%EDTA%",
  "formula": "C10H16N2O8",
  "limit": 20
}
```

[summary]
## search_ligands — 1 result(s)

**stats:** 1 SQL matches · showing 1 · limit 20

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_6277 | Ethylenedinitrilotetraacetic acid (EDTA) | H4L | EDTA and derivatives | 596 | `O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O` | (-inf, H5L, -1.5, H4L, 2, H3L, 2.69, H2L, 6.13, HL, 9.52, L, +inf) |

### Functional groups across all SQL matches (1 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 1 | 100% |
| tertiary_amine | 1 | 100% |

---

### Step 8: `search_metals`
**Args:**
```json
{
  "name": "iron, copper, zinc, nickel, cobalt, manganese, aluminum, calcium, magnesium, lead, cadmium",
  "limit": 20
}
```

[summary]
## search_metals

*(no results)*

---

### Step 9: `build_system_catalog`
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

### Step 11: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_6277 AND c.metal_id IN (metal_25, metal_92, metal_208, metal_41, metal_112, metal_33, metal_26, metal_61, metal_5) AND c.beta_definition_id = beta_def_812 AND s.solvent_name = 'water')",
  "order_by": "ABS(s.temperature_c - 25) ASC, ABS(s.ionic_strength_mol_l - 0.1) ASC, s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability

*(no results)*

---

### Step 12: `search_pka_values`
**Args:**
```json
{
  "where": "(lc.ligand_id = ligand_6277 AND p.solvent_name = 'water')",
  "order_by": "ABS(p.temperature_c - 25) ASC, ABS(p.ionic_strength_mol_l - 0.1) ASC, p.pKa ASC",
  "limit": 50
}
```

[summary]
## search_pka_values

*(no results)*

---

### Step 13: `search_stability`
**Args:**
```json
{
  "where": "(c.ligand_id = ligand_6277 AND c.metal_id IN (metal_25, metal_92, metal_208, metal_41, metal_112, metal_33, metal_26, metal_61, metal_5))",
  "order_by": "s.constant_value DESC",
  "limit": 100
}
```

[summary]
## search_stability — 100 row(s)

### ΔS — 9 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_26 | Cd^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 5 | 2 | 25 | 0~1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 4 | 4 | 20~25 | 0.1~1 | *** | 0 |
| metal_92 | Mg^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 4 | 1 | 25 | 0.1~1 | *** | 0 |
| metal_25 | Ca^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 4 | 1 | 25 | 0.1~1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 3 | 3 | 25 | 0.1 | *** | 0 |
| metal_5 | Al^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |

### ΔH — 7 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_92 | Mg^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 6 | 1 | 15~35 | 0~1 | *** | 0 |
| metal_61 | Fe^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 3 | 3 | 25 | 0.1~1 | *** | 0 |
| metal_5 | Al^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 0 |
| metal_112 | Ni^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 0 |
| metal_41 | Cu^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 20 | 0.1 | *** | 0 |
| metal_26 | Cd^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |

### logK — 9 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_208 | Zn^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 8 | 3 | 25 | 0~3 | *** | 5 |
| metal_26 | Cd^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 8 | 3 | 25 | 0~3 | *** | 5 |
| metal_92 | Mg^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 8 | 2 | 20~37 | 0.1~1 | *** | 6 |
| metal_25 | Ca^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 8 | 2 | 20~37 | 0.1~1 | *** | 6 |
| metal_5 | Al^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 7 | 4 | 25 | 0.1~1 | *** | 3 |
| metal_61 | Fe^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 6 | 4 | 25 | 0.1~1 | *** | 2 |
| metal_41 | Cu^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 5 | 3 | 25 | 0.1~1 | *** | 2 |
| metal_33 | Co^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 4 | 3 | 25 | 0.1~1 | *** | 2 |
| metal_112 | Ni^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 4 | 3 | 25 | 0.1~1 | *** | 2 |

---

### Step 14: `search_pka_ligands`
**Args:**
```json
{
  "where": "(lc.ligand_id = ligand_6277)",
  "order_by": "p.pKa ASC",
  "limit": 50
}
```

[summary]
## search_pka_ligands — 5 row(s)

| ligand_id | ligand_name | HxL_def | formula | smiles | pH_ladder | T°C_range | I(M)_range | similarity_score |
|-----------|-------------|---------|---------|--------|-----------|-----------|------------|------------------|
| ligand_6277 | Ethylenedinitrilotetraacetic acid (EDTA) | H4L | C10H16N2O8 | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | −∞; H5L (M_tot_1); (-1.5, vlm_108289); H4L (M_tot_2); (2, vlm_108282); H3L (M_tot_2); (2.69, vlm_108272); H2L (M_tot_1); (6.13, vlm_108254); HL (M_tot_7); (9.52, vlm_108224); L (M_tot_70); +∞ | 25 | 0.1 | *** |

---
