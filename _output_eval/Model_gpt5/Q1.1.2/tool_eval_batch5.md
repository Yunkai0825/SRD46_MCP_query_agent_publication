# Q1.1.2 — Tool Results (batch 5)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "hydrogen",
  "limit": 5
}
```

[summary]
## search_metals — 5 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_20 | BuHg^[+] | B | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_23 | BuNH_[3]^[+] | B | 1 |  | *** | *** | beta_totN_1 | ligand_totN_2 | vlm_totN_2 |
| metal_24 | C(NH_[2])_[3]^[+] | C | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_45 | Et_[2]NH_[2]^[+] | E2NH2 | 1 |  | *** | *** | beta_totN_1 | ligand_totN_1 | vlm_totN_1 |
| metal_48 | Et_[3]NH^[+] | E3NH | 1 |  | *** | *** | beta_totN_1 | ligand_totN_1 | vlm_totN_1 |

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "citric acid",
  "limit": 25
}
```

[summary]
## search_ligands — 8 result(s)

**stats:** 8 SQL matches · showing 8 · limit 25

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_9057 | DL-1-Hydroxypropane-1,2,3-tricar… (Isocitric acid) | H3L | Carboxylic acids polyaci… | 24 | `O=C(O)CC(C(=O)O)C(O)C(=O)O` | (-inf, H3L, 3.05, H2L, 4.3, HL, 5.73, L, +inf) |
| ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxyli… (Citric acid) | H3L | Carboxylic acids polyaci… | 384 | `O=C(O)CC(O)(CC(=O)O)C(=O)O` | (-inf, H3L, 2.9, H2L, 4.35, HL, 5.65, L, +inf) |
| ligand_10950 | DL-Methylcitric acid | *** | Ligands not selected | 0 | *** | *** |
| ligand_10951 | DL-Homocitric acid | *** | Ligands not selected | 0 | *** | *** |
| ligand_10952 | DL-threo-2-Methylisocitric acid | *** | Ligands not selected | 0 | *** | *** |
| ligand_10953 | DL-erytho-2-Methylisocitric acid | *** | Ligands not selected | 0 | *** | *** |
| ligand_10954 | DL-threo-Homoisocitric acid | *** | Ligands not selected | 0 | *** | *** |
| ligand_10955 | DL-erythro-Fluorocitric acid | *** | Ligands not selected | 0 | *** | *** |

### Functional groups across all SQL matches (2 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 2 | 100% |
| hydroxyl | 2 | 100% |

---

### Step 5: `build_system_catalog`
**Args:**
```json
{
  "ligand_id": "ligand_9058"
}
```

[summary]
[CATALOG]
## build_system_catalog — 20 pair(s), 95 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_32 | [HL] + [H] <=> [H2L] |  |
| beta_def_53 | [H2L] + [H] <=> [H3L] |  |
| beta_def_79 | [L] + [H] <=> [HL] |  |
| beta_def_107 | [M(H-1L)] + [H] <=> [ML] |  |
| beta_def_283 | [MHL(s)] <=> [M] + [H] + [L] | solid |
| beta_def_369 | [M]^2 + [L] <=> [M2(H-1L)] + [H] |  |
| beta_def_372 | [M2(H-1L)2] + [H] <=> [M2(H-1L)L] |  |
| beta_def_374 | [M]^2 + [L]^2 <=> [M2(H-1L)2] + [H]^2 |  |
| beta_def_382 | [M2(H-1L)L] + [H] <=> [M2L2] |  |
| beta_def_422 | [M2(OH)2L2] + [H] <=> [M2(OH)L2] + [H2O] |  |
| beta_def_424 | [M]^2 + [L]^2 + [H2O]^2 <=> [M2(OH)2L2] + [H]^2 |  |
| beta_def_432 | [M]^2 + [L]^2 + [H2O]^2 <=> [M2(OH)2L2] + [H]^2 |  |
| beta_def_433 | [M2(OH)L2] + [OH] <=> [M2(OH)2L2] |  |
| beta_def_519 | [M]^2 + [L]^2 <=> [M2L2] |  |
| beta_def_554 | * |  |
| beta_def_555 | [M2O4(OH)3(H-1L)] + [H] <=> [M2O4(OH)2(H-1L)] + [H2O] |  |
| beta_def_556 | [(MO2(OH)4)2] + [L] + [H]^4 <=> [M2O4(OH)3(H-1L)] + [H2O]^5 |  |
| beta_def_559 | * |  |
| beta_def_560 | [M2O5(H-1L)2] + [H] <=> [M2O5(H-1L)L] |  |
| beta_def_574 | [M2(OH)2L] + [H] <=> [M2(OH)L] + [H2O] |  |
| beta_def_578 | [M(OH)L] + [M] <=> [M2(OH)L] |  |
| beta_def_579 | [M2(OH)L2] + [H] <=> [M2L2] + [H2O] |  |
| beta_def_584 | [M2L2] + [OH] <=> [M2(OH)L2] |  |
| beta_def_608 | [M]^3 + [L]^3 + [H2O]^4 <=> [M3(OH)4(H-1L)3] + [H]^7 |  |
| beta_def_614 | [M]^3 + [L]^3 + [H2O]^4 <=> [M3(OH)4L3] + [H]^4 |  |
| beta_def_624 | [M3L2(s)] <=> [M]^3 + [L]^2 | solid |
| beta_def_659 | [M2(OH)2L2] + [M]^2 <=> [M4(OH)2L2] |  |
| beta_def_660 | [M4(OH)3L2] + [H] <=> [M4(OH)2L2] + [H2O] |  |
| beta_def_661 | [M4(OH)4L2] + [H] <=> [M4(OH)3L2] + [H2O] |  |
| beta_def_732 | [M] + [H2L] <=> [MH2L] |  |
| beta_def_779 | [M] + [HL] <=> [MHL] |  |
| beta_def_792 | [ML2] + [H] <=> [MHL2] |  |
| beta_def_800 | [MHL] + [L] <=> [MHL2] |  |
| beta_def_812 | [M] + [L] <=> [ML] |  |
| beta_def_840 | [M] + [L]^2 <=> [ML2] |  |
| beta_def_925 | [MO2(OH)(H-1L)] + [H] <=> [MO2(H-1L)] + [H2O] |  |
| beta_def_934 | [MO2(OH)2(H-1L)] + [H] <=> [MO2(OH)(H-1L)] + [H2O] |  |
| beta_def_936 | [MO2(OH)4] + [L] + [H] <=> [MO2(OH)2(H-1L)] + [H2O]^2 |  |
| beta_def_937 | [MO2(OH)4] + [L]^2 + [H]^4 <=> [MO2H2(H-1L)2] + [H2O]^4 |  |
| beta_def_938 | [MO2(H-1L)] + [H] <=> [MO2L] |  |
| beta_def_966 | [M(OH)L] + [H] <=> [ML] + [H2O] |  |

*(all species aqueous unless noted)*

**1. H^[+] + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid)** (metal_68 + ligand_9058) — ligand_def_HxL: H3L | 48 ent, 3 sp, 48 vlms (vlm_157439…vlm_157486)
   - species: beta_def_32(14) beta_def_53(14) beta_def_79(20)
   - eq:14 nets T:13~41°C I:-0.15~3.15M max 3n/3e
**2. Ni^[2+] + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid)** (metal_112 + ligand_9058) — ligand_def_HxL: H3L | 25 ent, 6 sp, 25 vlms (vlm_157638…vlm_157662)
   - species: beta_def_374(4) beta_def_732(2) beta_def_779(5) beta_def_800(4) beta_def_812(6) beta_def_840(4)
   - eq:4 nets T:19~30°C I:-0.05~1.15M max 6n/14e
**3. W^[6+] + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid)** (metal_204 + ligand_9058) — ligand_def_HxL: H3L | 24 ent, 8 sp, 24 vlms (vlm_157711…vlm_157734)
   - species: beta_def_554(3) beta_def_559(3) beta_def_560(3) beta_def_925(3) beta_def_934(3) beta_def_936(3) beta_def_937(3) beta_def_938(3)
   - eq:3 nets T:16.5~31.5°C I:0.775~1.225M max 6n/15e
**4. Cd^[2+] + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid)** (metal_26 + ligand_9058) — ligand_def_HxL: H3L | 22 ent, 6 sp, 22 vlms (vlm_157765…vlm_157786)
   - species: beta_def_107(3) beta_def_374(1) beta_def_732(2) beta_def_779(5) beta_def_812(6) beta_def_840(5)
   - eq:4 nets T:19~30°C I:-0.05~2.15M max 5n/10e
**5. Zn^[2+] + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid)** (metal_208 + ligand_9058) — ligand_def_HxL: H3L | 19 ent, 4 sp, 19 vlms (vlm_157746…vlm_157764)
   - species: beta_def_374(3) beta_def_779(5) beta_def_812(6) beta_def_840(5)
   - eq:4 nets T:19~41°C I:-0.05~0.65M max 4n/6e
**6. Cu^[2+] + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid)** (metal_41 + ligand_9058) — ligand_def_HxL: H3L | 19 ent, 5 sp, 19 vlms (vlm_157663…vlm_157681)
   - species: beta_def_369(4) beta_def_372(4) beta_def_382(3) beta_def_519(4) beta_def_779(4)
   - eq:2 nets T:19~30°C I:-0.05~0.25M max 5n/7e
**7. Mo^[6+] + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid)** (metal_103 + ligand_9058) — ligand_def_HxL: H3L | 18 ent, 5 sp, 18 vlms (vlm_157693…vlm_157710)
   - species: beta_def_555(3) beta_def_556(3) beta_def_925(4) beta_def_934(4) beta_def_936(4)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 5n/10e
**8. Ca^[2+] + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid)** (metal_25 + ligand_9058) — ligand_def_HxL: H3L | 18 ent, 5 sp, 18 vlms (vlm_157530…vlm_157547)
   - species: beta_def_283(1) beta_def_624(1) beta_def_732(1) beta_def_779(5) beta_def_812(10)
   - eq:8 nets T:19~41°C I:-0.15~0.3M max 5n/10e
**9. Mg^[2+] + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid)** (metal_92 + ligand_9058) — ligand_def_HxL: H3L | 15 ent, 3 sp, 15 vlms (vlm_157515…vlm_157529)
   - species: beta_def_732(1) beta_def_779(5) beta_def_812(9)
   - eq:7 nets T:19~41°C I:-0.15~0.3M max 3n/3e
**10. Al^[3+] + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid)** (metal_5 + ligand_9058) — ligand_def_HxL: H3L | 15 ent, 7 sp, 15 vlms (vlm_157802…vlm_157816)
   - species: beta_def_107(2) beta_def_432(1) beta_def_608(1) beta_def_614(2) beta_def_779(3) beta_def_812(3) beta_def_840(3)
   - eq:3 nets T:19~41°C I:-0.05~0.65M max 6n/13e
**11. Pb^[2+] + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid)** (metal_125 + ligand_9058) — ligand_def_HxL: H3L | 12 ent, 8 sp, 12 vlms (vlm_157788…vlm_157799)
   - species: beta_def_433(1) beta_def_519(1) beta_def_584(1) beta_def_732(2) beta_def_779(2) beta_def_792(1) beta_def_812(2) beta_def_840(2)
   - eq:2 nets T:16.5~31.5°C I:0.775~2.225M max 8n/13e
**12. Fe^[2+] + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid)** (metal_62 + ligand_9058) — ligand_def_HxL: H3L | 11 ent, 5 sp, 11 vlms (vlm_157619…vlm_157629)
   - species: beta_def_374(1) beta_def_732(1) beta_def_779(4) beta_def_800(1) beta_def_812(4)
   - eq:5 nets T:15~41°C I:-0.05~3.15M max 5n/9e
**13. Be^[2+] + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid)** (metal_19 + ligand_9058) — ligand_def_HxL: H3L | 11 ent, 9 sp, 11 vlms (vlm_157504…vlm_157514)
   - species: beta_def_422(1) beta_def_519(1) beta_def_579(1) beta_def_659(1) beta_def_660(1) beta_def_661(1) beta_def_732(1) beta_def_779(2) beta_def_812(2)
   - eq:2 nets T:16.5~43.5°C I:-0.125~1.225M max 8n/15e
**14. Mn^[2+] + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid)** (metal_94 + ligand_9058) — ligand_def_HxL: H3L | 10 ent, 4 sp, 10 vlms (vlm_157609…vlm_157618)
   - species: beta_def_374(2) beta_def_732(1) beta_def_779(2) beta_def_812(5)
   - eq:5 nets T:19~41°C I:-0.05~0.3M max 4n/6e
**15. NpO_[2]^[+] + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid)** (metal_118 + ligand_9058) — ligand_def_HxL: H3L | 8 ent, 1 sp, 8 vlms (vlm_157597…vlm_157604)
   - species: beta_def_812(8)
   - eq:8 nets T:16.5~31.5°C I:0.275~9.225M max 1n/0e
**16. Fe^[3+] + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid)** (metal_61 + ligand_9058) — ligand_def_HxL: H3L | 8 ent, 4 sp, 8 vlms (vlm_157682…vlm_157689)
   - species: beta_def_424(1) beta_def_779(1) beta_def_812(5) beta_def_966(1)
   - eq:3 nets T:19~30°C I:-0.05~1.15M max 4n/5e
**17. Co^[2+] + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid)** (metal_33 + ligand_9058) — ligand_def_HxL: H3L | 8 ent, 3 sp, 8 vlms (vlm_157630…vlm_157637)
   - species: beta_def_732(2) beta_def_779(3) beta_def_812(3)
   - eq:3 nets T:15~30°C I:-0.05~1.15M max 3n/3e
**18. K^[+] + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid)** (metal_78 + ligand_9058) — ligand_def_HxL: H3L | 6 ent, 1 sp, 6 vlms (vlm_157493…vlm_157498)
   - species: beta_def_812(6)
   - eq:3 nets T:19~41°C I:-0.15~0.3M max 1n/0e
**19. Sr^[2+] + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid)** (metal_177 + ligand_9058) — ligand_def_HxL: H3L | 5 ent, 3 sp, 5 vlms (vlm_157548…vlm_157552)
   - species: beta_def_732(1) beta_def_779(1) beta_def_812(3)
   - eq:3 nets T:19~30°C I:-0.05~0.25M max 3n/3e
**20. Me_[2]Sn^[2+] + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid)** (metal_85 + ligand_9058) — ligand_def_HxL: H3L | 5 ent, 5 sp, 5 vlms (vlm_157738…vlm_157742)
   - species: beta_def_574(1) beta_def_578(1) beta_def_779(1) beta_def_812(1) beta_def_966(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 5n/7e

---

### Step 7: `search_pka_values`
**Args:**
```json
{
  "where": "(lc.ligand_id = ligand_9058)",
  "order_by": "p.pKa ASC, p.pKa_type ASC, p.temperature_c ASC, p.ionic_strength_mol_l ASC",
  "limit": 500
}
```

[summary]
## search_pka_values — 3 row(s)

### pKa 2.5–3.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_157473 | ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxyl… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 2.9 | 25 | 0.1 | H2L→H3L | M_tot_1 | M_tot_12 |

### pKa 4.0–4.5 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_157459 | ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxyl… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 4.35 | 25 | 0.1 | HL→H2L | M_tot_12 | M_tot_18 |

### pKa 5.5–6.0 (1 entries)

| vlm_id | ligand_id | ligand_name | HxL_def | smiles | pKa | T°C | I(M) | bracket_from→to | M_bind_totN_below | M_bind_totN_above |
|--------|-----------|-------------|---------|--------|-----|-----|------|-----------------|-------------------|-------------------|
| vlm_157439 | ligand_9058 | 2-Hydroxypropane-1,2,3-tricarboxyl… | H3L | O=C(O)CC(O)(CC(=O)O)C(=O)O | 5.65 | 25 | 0.1 | L→HL | M_tot_18 | M_tot_57 |

---
