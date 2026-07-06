# Q4.3 — Tool Results (batch 2)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Cu(II), Ni(II), Zn(II)",
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
  "name": "ethylenediamine, ammonia",
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
  "symbol": "Cu, Ni, Zn",
  "limit": 10
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
  "name": "en, ethane-1,2-diamine, 1,2-diaminoethane, ammine, ammonia, azane",
  "limit": 20
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 7: `build_system_catalog`
**Args:**
```json
{}
```

[summary]
[CATALOG]
## build_system_catalog

**Error:** Provide at least one of metal_id, ligand_id, or beta_definition_id.

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_name_SRD LIKE '%copper%' OR c.metal_name_SRD LIKE '%nickel%' OR c.metal_name_SRD LIKE '%zinc%') AND (c.ligand_name_SRD LIKE '%ethylenediamine%' OR c.ligand_name_SRD LIKE '%ammonia%' OR c.ligand_name_SRD LIKE '%ammine%')",
  "order_by": "c.metal_name_SRD, c.ligand_name_SRD, s.temperature_c",
  "limit": 200
}
```

[PHASE ERROR] Tool 'search_stability' is not available yet. You must call 0_plan_search_strategy first (PHASE 2) before using the execution tools.

---

### Step 9: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_29"
}
```

[summary]
[CATALOG]
## build_system_catalog — 20 pair(s), 30 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_788 | [ML] + [H] <=> [MHL] |  |
| beta_def_812 | [M] + [L] <=> [ML] |  |
| beta_def_840 | [M] + [L]^2 <=> [ML2] |  |
| beta_def_872 | [M] + [L]^3 <=> [ML3] |  |

*(all species aqueous)*

**1. Cf^[3+] + Hydrogen sulfate ion (Sulfuric acid)** (metal_29 + ligand_10148) — ligand_def_HxL: HL | 6 ent, 2 sp, 6 vlms (vlm_175930…vlm_175935)
   - species: beta_def_812(4) beta_def_840(2)
   - eq:2 nets T:19~30°C I:-0.05~2.15M max 2n/1e
**2. Cf^[3+] + Hydrogen fluoride (Hydrofluoric acid)** (metal_29 + ligand_10162) — ligand_def_HxL: HL | 3 ent, 1 sp, 3 vlms (vlm_176844, vlm_176845, vlm_176846)
   - species: beta_def_812(3)
   - eq:1 nets T:16.5~31.5°C I:0.775~1.225M max 1n/0e
**3. Cf^[3+] + 5,7-Dichloro-8-hydroxyquinoline** (metal_29 + ligand_8129) — ligand_def_HxL: HL | 3 ent, 3 sp, 3 vlms (vlm_138072, vlm_138073, vlm_138074)
   - species: beta_def_812(1) beta_def_840(1) beta_def_872(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 3n/3e
**4. Cf^[3+] + N-(2-Carboxyethyl)iminodiacetic acid** (metal_29 + ligand_6167) — ligand_def_HxL: H3L | 3 ent, 3 sp, 3 vlms (vlm_105744, vlm_105745, vlm_105746)
   - species: beta_def_788(1) beta_def_812(1) beta_def_840(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 3n/2e
**5. Cf^[3+] + Nitrilotriacetic acid (NTA)** (metal_29 + ligand_6165) — ligand_def_HxL: H3L | 3 ent, 2 sp, 3 vlms (vlm_105467, vlm_105468, vlm_105469)
   - species: beta_def_812(2) beta_def_840(1)
   - eq:2 nets T:19~30°C I:-0.05~0.65M max 2n/1e
**6. Cf^[3+] + Dihydroxycyclobutenedione (Squaric acid)** (metal_29 + ligand_9564) — ligand_def_HxL: H2L | 2 ent, 2 sp, 2 vlms (vlm_165827, vlm_165828)
   - species: beta_def_812(1) beta_def_840(1)
   - eq:1 nets T:16.5~31.5°C I:0.775~1.225M max 2n/1e
**7. Cf^[3+] + Ethanedioic acid (Oxalic acid)** (metal_29 + ligand_8872) — ligand_def_HxL: H2L | 2 ent, 2 sp, 2 vlms (vlm_151702, vlm_151703)
   - species: beta_def_812(1) beta_def_840(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 2n/1e
**8. Cf^[3+] + Hydroxyacetic acid (Glycolic acid)** (metal_29 + ligand_8640) — ligand_def_HxL: HL | 2 ent, 2 sp, 2 vlms (vlm_147344, vlm_147345)
   - species: beta_def_812(1) beta_def_840(1)
   - eq:1 nets T:48.5~63.5°C I:1.775~2.225M max 2n/1e
**9. Cf^[3+] + Diethylenetrinitrilopentaacetic acid (DTPA)** (metal_29 + ligand_6356) — ligand_def_HxL: H5L | 2 ent, 1 sp, 2 vlms (vlm_112653, vlm_112654)
   - species: beta_def_812(2)
   - eq:2 nets T:15~30°C I:-0.05~0.25M max 1n/0e
**10. Cf^[3+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_29 + ligand_6277) — ligand_def_HxL: H4L | 2 ent, 1 sp, 2 vlms (vlm_108519, vlm_108520)
   - species: beta_def_812(2)
   - eq:2 nets T:19~30°C I:-0.05~0.25M max 1n/0e
**11. Cf^[3+] + N-(2-Hydroxyethyl)ethylenedinitrilotriacetic acid (HEDTA)** (metal_29 + ligand_6275) — ligand_def_HxL: H3L | 2 ent, 2 sp, 2 vlms (vlm_108094, vlm_108095)
   - species: beta_def_812(1) beta_def_840(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 2n/1e
**12. Cf^[3+] + Bromide ion** (metal_29 + ligand_10168) — ligand_def_HxL: *** | 1 ent, 1 sp, 1 vlms (vlm_177967)
   - species: beta_def_812(1)
   - eq:1 nets T:12.5~27.5°C I:2.775~3.225M max 1n/0e
**13. Cf^[3+] + Chloride ion** (metal_29 + ligand_10163) — ligand_def_HxL: *** | 1 ent, 1 sp, 1 vlms (vlm_177310)
   - species: beta_def_812(1)
   - eq:1 nets T:12.5~27.5°C I:2.775~3.225M max 1n/0e
**14. Cf^[3+] + Nitrate ion** (metal_29 + ligand_10109) — ligand_def_HxL: *** | 1 ent, 1 sp, 1 vlms (vlm_173917)
   - species: beta_def_812(1)
   - eq:1 nets T:16.5~31.5°C I:0.775~1.225M max 1n/0e
**15. Cf^[3+] + Hydrogen azide (Hydrazoic acid)** (metal_29 + ligand_10106) — ligand_def_HxL: HL | 1 ent, 1 sp, 1 vlms (vlm_173569)
   - species: beta_def_812(1)
   - eq:1 nets T:16.5~31.5°C I:0.275~0.725M max 1n/0e
**16. Cf^[3+] + Hydrogen thiocyanate (Thiocyanic acid)** (metal_29 + ligand_10092) — ligand_def_HxL: HL | 1 ent, 1 sp, 1 vlms (vlm_172170)
   - species: beta_def_812(1)
   - eq:1 nets T:16.5~31.5°C I:0.775~1.225M max 1n/0e
**17. Cf^[3+] + Hydroxide ion** (metal_29 + ligand_10076) — ligand_def_HxL: *** | 1 ent, 1 sp, 1 vlms (vlm_170520)
   - species: beta_def_812(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**18. Cf^[3+] + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid)** (metal_29 + ligand_9058) — ligand_def_HxL: H3L | 1 ent, 1 sp, 1 vlms (vlm_157593)
   - species: beta_def_812(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 1n/0e
**19. Cf^[3+] + D-2-Hydroxypropanoic acid (Lactic acid)** (metal_29 + ligand_8641) — ligand_def_HxL: HL | 1 ent, 1 sp, 1 vlms (vlm_147681)
   - species: beta_def_872(1)
   - eq:1 nets T:16.5~31.5°C I:0.275~0.725M max 1n/0e
**20. Cf^[3+] + Ethanoic acid (Acetic acid)** (metal_29 + ligand_8465) — ligand_def_HxL: HL | 1 ent, 1 sp, 1 vlms (vlm_144647)
   - species: beta_def_812(1)
   - eq:1 nets T:16.5~31.5°C I:1.775~2.225M max 1n/0e

---

### Step 11: `search_stability`
**Args:**
```json
{
  "where": "((c.metal_name_SRD LIKE '%Copper%' OR c.metal_name_SRD LIKE '%Nickel%' OR c.metal_name_SRD LIKE '%Zinc%') AND (c.ligand_name_SRD LIKE '%ammonia%' OR c.ligand_name_SRD LIKE '%ammine%' OR c.ligand_name_SRD LIKE '%ethylenediamine%' OR c.ligand_name_SRD LIKE '%ethane-1,2-diamine%' OR c.ligand_name_SRD LIKE '%1,2-diaminoethane%'))",
  "order_by": "c.metal_name_SRD, c.ligand_name_SRD, s.temperature_c, s.ionic_strength_mol_l",
  "limit": 200
}
```

[summary]
## search_stability — 200 row(s)

### logK — 26 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_2 | Ag^[+] | ligand_10103 | Ammonia | L | N | 29 | 2 | 25 | 0~5 | *** | 16 |
| metal_26 | Cd^[2+] | ligand_10103 | Ammonia | L | N | 17 | 4 | 25 | 0~3 | *** | 5 |
| metal_33 | Co^[2+] | ligand_10103 | Ammonia | L | N | 17 | 5 | 25~30 | 0~5 | *** | 5 |
| metal_37 | Cr^[3+] | ligand_10103 | Ammonia | L | N | 12 | 12 | 20~25 | 0.5~4.5 | *** | 3 |
| metal_34 | Co^[3+] | ligand_10103 | Ammonia | L | N | 10 | 8 | 20~30 | 0.1~2 | *** | 5 |
| metal_25 | Ca^[2+] | ligand_10103 | Ammonia | L | N | 8 | 2 | 25 | 0~2 | *** | 4 |
| metal_42 | Cu^[+] | ligand_10103 | Ammonia | L | N | 6 | 2 | 18~25 | 0.1~2 | *** | 6 |
| metal_18 | Ba^[2+] | ligand_10103 | Ammonia | L | N | 4 | 1 | 25 | 0~2 | *** | 4 |
| metal_33 | Co^[2+] | ligand_6727 | 2,5-Bis[N-(carboxymethyl)-N… | H4L | O=C(O)CN(CCO)c1cc(C(=O)O)c(N(CCO)CC(=O)O)cc1C(=O)O | 4 | 4 | 22 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_6749 | N-[2,5-Dicarboxy-4-(carboxy… | H5L | O=C(O)CNc1cc(C(=O)O)c(N(CC(=O)O)CC(=O)O)cc1C(=O)O | 4 | 4 | 25 | 0.1 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_9072 | Butane-1,2,3,4-tetracarboxy… | H4L | O=C(O)CC(C(=O)O)C(CC(=O)O)C(=O)O | 3 | 2 | 25 | 0~0.1 | solid | 2 |
| metal_26 | Cd^[2+] | ligand_6749 | N-[2,5-Dicarboxy-4-(carboxy… | H5L | O=C(O)CNc1cc(C(=O)O)c(N(CC(=O)O)CC(=O)O)cc1C(=O)O | 3 | 3 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_10104 | Hydrazine | L | NN | 3 | 3 | 25 | 1 | *** | 1 |
| metal_2 | Ag^[+] | ligand_8023 | Pyridine-3-carboxylic acid … | L | CNC(=O)c1cccnc1 | 2 | 2 | 25 | 0.5 | *** | 1 |
| metal_14 | Au^[3+] | ligand_10103 | Ammonia | L | N | 2 | 2 | 25 | 1 | *** | 1 |
| metal_26 | Cd^[2+] | ligand_6740 | N-(4-Hydroxy-2,5-dicarboxyp… | H5L | O=C(O)CN(CC(=O)O)c1cc(C(=O)O)c(O)cc1C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_6740 | N-(4-Hydroxy-2,5-dicarboxyp… | H5L | O=C(O)CN(CC(=O)O)c1cc(C(=O)O)c(O)cc1C(=O)O | 2 | 2 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_8023 | Pyridine-3-carboxylic acid … | L | CNC(=O)c1cccnc1 | 2 | 2 | 25 | 0.5 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_6719 | 2,5-Bis[bis(2-hydroxyethyl)… | H2L | O=C(O)c1cc(N(CCO)CCO)c(C(=O)O)cc1N(CCO)CCO | 2 | 2 | 22 | 0.1 | *** | 1 |
| metal_41 | Cu^[2+] | ligand_6718 | 2-Bis(2-hydroxyethyl)amino-… | H2L | O=C(O)c1cc(N(CCO)CCO)c(C(=O)O)cc1NCCO | 2 | 2 | 22 | 0.1 | *** | 1 |
| metal_2 | Ag^[+] | ligand_10105 | Hydroxylamine | L | NO | 1 | 1 | 20 | 0.5 | *** | 1 |
| metal_18 | Ba^[2+] | ligand_6740 | N-(4-Hydroxy-2,5-dicarboxyp… | H5L | O=C(O)CN(CC(=O)O)c1cc(C(=O)O)c(O)cc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_18 | Ba^[2+] | ligand_6749 | N-[2,5-Dicarboxy-4-(carboxy… | H5L | O=C(O)CNc1cc(C(=O)O)c(N(CC(=O)O)CC(=O)O)cc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_6740 | N-(4-Hydroxy-2,5-dicarboxyp… | H5L | O=C(O)CN(CC(=O)O)c1cc(C(=O)O)c(O)cc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_25 | Ca^[2+] | ligand_6749 | N-[2,5-Dicarboxy-4-(carboxy… | H5L | O=C(O)CNc1cc(C(=O)O)c(N(CC(=O)O)CC(=O)O)cc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 1 |
| metal_33 | Co^[2+] | ligand_10105 | Hydroxylamine | L | NO | 1 | 1 | 20 | 0.5 | *** | 1 |

### ΔH — 6 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_26 | Cd^[2+] | ligand_10103 | Ammonia | L | N | 16 | 4 | 25 | 0~3 | *** | 0 |
| metal_2 | Ag^[+] | ligand_10103 | Ammonia | L | N | 10 | 2 | 25 | 0~3 | *** | 0 |
| metal_34 | Co^[3+] | ligand_10103 | Ammonia | L | N | 2 | 2 | 25 | 0 | *** | 0 |
| metal_14 | Au^[3+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 2 | *** | 0 |
| metal_37 | Cr^[3+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 0.5 | *** | 0 |

### ΔS — 6 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_26 | Cd^[2+] | ligand_10103 | Ammonia | L | N | 16 | 4 | 25 | 0~3 | *** | 0 |
| metal_2 | Ag^[+] | ligand_10103 | Ammonia | L | N | 8 | 2 | 25 | 0~3 | *** | 0 |
| metal_34 | Co^[3+] | ligand_10103 | Ammonia | L | N | 2 | 2 | 25 | 2 | *** | 0 |
| metal_14 | Au^[3+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 1 | *** | 0 |
| metal_33 | Co^[2+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 2 | *** | 0 |
| metal_37 | Cr^[3+] | ligand_10103 | Ammonia | L | N | 1 | 1 | 25 | 0.5 | *** | 0 |

---

### Step 12: `search_networks`
**Args:**
```json
{
  "where": "((c.metal_name LIKE '%Copper%' OR c.metal_name LIKE '%Nickel%' OR c.metal_name LIKE '%Zinc%') AND (c.ligand_name LIKE '%ammonia%' OR c.ligand_name LIKE '%ammine%' OR c.ligand_name LIKE '%ethylenediamine%' OR c.ligand_name LIKE '%ethane-1,2-diamine%' OR c.ligand_name LIKE '%1,2-diaminoethane%'))",
  "order_by": "c.metal_name, c.ligand_name",
  "limit": 100
}
```

[summary]
## search_networks — 199 row(s)

> **Reference equilibrium networks (compact)** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### Beta-definition legend
| beta_def | equation |
|----------|----------|
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |
| beta_def_779 | ``[M] + [HL] <=> [MHL]`` |
| beta_def_457 | ``[M2L(s)] <=> [M]^2 + [L]`` |
| beta_def_739 | ``[MHL] + [H] <=> [MH2L]`` |
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` |
| beta_def_502 | ``[M]^2 + [L] <=> [M2L]`` |
| beta_def_872 | ``[M] + [L]^3 <=> [ML3]`` |
| beta_def_79 | ``[L] + [H] <=> [HL]`` |
| beta_def_32 | ``[HL] + [H] <=> [H2L]`` |
| beta_def_53 | ``[H2L] + [H] <=> [H3L]`` |
| beta_def_64 | ``[H3L] + [H] <=> [H4L]`` |
| beta_def_68 | ``[H4L] + [H] <=> [H5L]`` |
| beta_def_966 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` |
| beta_def_732 | ``[M] + [H2L] <=> [MH2L]`` |
| beta_def_751 | ``[MH2L] + [H] <=> [MH3L]`` |
| beta_def_894 | ``[M] + [L]^4 <=> [ML4]`` |
| beta_def_516 | ``[ML] + [M] <=> [M2L]`` |

### Metal-ligand pair summary
| metal | metal_id | ligand | ligand_id | HxL | T_range | I_range | net_count | max_nodes | max_net_id | ligand_SMILES |
|-------|----------|--------|-----------|-----|---------|---------|-----------|----------|------------|---------------|
| `Ag^[+]` | metal_2 | Pyridine-3-carboxylic acid methylamide | ligand_8023 | L | 16.5~31.5 | 0.275~0.725 | 1 | 2 | ref_eq_net_14364 | CNC(=O)c1cccnc1 |
| `Ba^[2+]` | metal_18 | Ammonia | ligand_10103 | L | 19~30 | -0.05~2.15 | 4 | 1 | ref_eq_net_28215 | N |
| `Ba^[2+]` | metal_18 | N-(4-Hydroxy-2,5-dicarboxyphenyl)iminod… | ligand_6740 | H5L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_8124 | O=C(O)CN(CC(=O)O)c1cc(C(=O)O)c(O)cc1C(=O)O |
| `Ba^[2+]` | metal_18 | N-[2,5-Dicarboxy-4-(carboxymethylamino)… | ligand_6749 | H5L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_8158 | O=C(O)CNc1cc(C(=O)O)c(N(CC(=O)O)CC(=O)O)cc1C(=O)O |
| `Ca^[2+]` | metal_25 | Ammonia | ligand_10103 | L | 19~30 | -0.05~2.15 | 4 | 2 | ref_eq_net_28207 | N |
| `Ca^[2+]` | metal_25 | Butane-1,2,3,4-tetracarboxylic acid | ligand_9072 | H4L | 19~30 | -0.15~0.25 | 2 | 2 | ref_eq_net_22285 | O=C(O)CC(C(=O)O)C(CC(=O)O)C(=O)O |
| `Ca^[2+]` | metal_25 | N-(4-Hydroxy-2,5-dicarboxyphenyl)iminod… | ligand_6740 | H5L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_8122 | O=C(O)CN(CC(=O)O)c1cc(C(=O)O)c(O)cc1C(=O)O |
| `Ca^[2+]` | metal_25 | N-[2,5-Dicarboxy-4-(carboxymethylamino)… | ligand_6749 | H5L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_8156 | O=C(O)CNc1cc(C(=O)O)c(N(CC(=O)O)CC(=O)O)cc1C(=O)O |
| `Cd^[2+]` | metal_26 | N-(4-Hydroxy-2,5-dicarboxyphenyl)iminod… | ligand_6740 | H5L | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_8130 | O=C(O)CN(CC(=O)O)c1cc(C(=O)O)c(O)cc1C(=O)O |
| `Cd^[2+]` | metal_26 | N-[2,5-Dicarboxy-4-(carboxymethylamino)… | ligand_6749 | H5L | 20~30 | -0.05~0.25 | 1 | 3 | ref_eq_net_8162 | O=C(O)CNc1cc(C(=O)O)c(N(CC(=O)O)CC(=O)O)cc1C(=O)O |
| `Co^[2+]` | metal_33 | 2,5-Bis[N-(carboxymethyl)-N-(2-hydroxye… | ligand_6727 | H4L | 20~30 | -0.05~0.25 | 1 | 4 | ref_eq_net_8035 | O=C(O)CN(CCO)c1cc(C(=O)O)c(N(CCO)CC(=O)O)cc1C(=O)O |
| `Co^[2+]` | metal_33 | N-(4-Hydroxy-2,5-dicarboxyphenyl)iminod… | ligand_6740 | H5L | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_8126 | O=C(O)CN(CC(=O)O)c1cc(C(=O)O)c(O)cc1C(=O)O |
| `Co^[2+]` | metal_33 | N-[2,5-Dicarboxy-4-(carboxymethylamino)… | ligand_6749 | H5L | 20~30 | -0.05~0.25 | 1 | 4 | ref_eq_net_8159 | O=C(O)CNc1cc(C(=O)O)c(N(CC(=O)O)CC(=O)O)cc1C(=O)O |
| `Co^[2+]` | metal_33 | Pyridine-3-carboxylic acid methylamide | ligand_8023 | L | 16.5~31.5 | 0.275~0.725 | 1 | 2 | ref_eq_net_14361 | CNC(=O)c1cccnc1 |
| `Cu^[2+]` | metal_41 | 2,5-Bis[bis(2-hydroxyethyl)amino]benzen… | ligand_6719 | H2L | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_8009 | O=C(O)c1cc(N(CCO)CCO)c(C(=O)O)cc1N(CCO)CCO |
| `Cu^[2+]` | metal_41 | 2-Bis(2-hydroxyethyl)amino-5-(2-hydroxy… | ligand_6718 | H2L | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_8006 | O=C(O)c1cc(N(CCO)CCO)c(C(=O)O)cc1NCCO |
| `Cu^[2+]` | metal_41 | DL-2-(1-Phenyl-1-hydroxyethyl)-1,4,5,6-… | ligand_8254 | L | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_15682 | CC(O)(C1=NCCCN1)c1ccccc1 |
| `Cu^[2+]` | metal_41 | N-(4-Hydroxy-2,5-dicarboxyphenyl)iminod… | ligand_6740 | H5L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_8128 | O=C(O)CN(CC(=O)O)c1cc(C(=O)O)c(O)cc1C(=O)O |
| `Cu^[2+]` | metal_41 | N-[2,5-Dicarboxy-4-(carboxymethylamino)… | ligand_6749 | H5L | 20~30 | -0.05~0.25 | 1 | 4 | ref_eq_net_8161 | O=C(O)CNc1cc(C(=O)O)c(N(CC(=O)O)CC(=O)O)cc1C(=O)O |
| `Cu^[2+]` | metal_41 | Pyridine-3-carboxylic acid methylamide | ligand_8023 | L | 16.5~31.5 | 0.275~0.725 | 1 | 3 | ref_eq_net_14363 | CNC(=O)c1cccnc1 |
| `H^[+]` | metal_68 | 2,5-Bis[N-(carboxymethyl)-N-(2-hydroxye… | ligand_6727 | H4L | 20~30 | -0.05~0.25 | 1 | 4 | ref_eq_net_8034 | O=C(O)CN(CCO)c1cc(C(=O)O)c(N(CCO)CC(=O)O)cc1C(=O)O |
| `H^[+]` | metal_68 | 2,5-Bis[bis(2-hydroxyethyl)amino]benzen… | ligand_6719 | H2L | 20~30 | -0.05~0.25 | 1 | 3 | ref_eq_net_8007 | O=C(O)c1cc(N(CCO)CCO)c(C(=O)O)cc1N(CCO)CCO |
| `H^[+]` | metal_68 | 2-Bis(2-hydroxyethyl)amino-5-(2-hydroxy… | ligand_6718 | H2L | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_8004 | O=C(O)c1cc(N(CCO)CCO)c(C(=O)O)cc1NCCO |
| `H^[+]` | metal_68 | Ammonia | ligand_10103 | L | 5~45 | -0.15~10.15 | 20 | 1 | ref_eq_net_28179 | N |
| `H^[+]` | metal_68 | Butane-1,2,3,4-tetracarboxylic acid | ligand_9072 | H4L | 19~30 | -0.15~3.15 | 9 | 4 | ref_eq_net_22270 | O=C(O)CC(C(=O)O)C(CC(=O)O)C(=O)O |
| `H^[+]` | metal_68 | DL-2-(1-Phenyl-1-hydroxyethyl)-1,4,5,6-… | ligand_8254 | L | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_15681 | CC(O)(C1=NCCCN1)c1ccccc1 |
| `H^[+]` | metal_68 | N-(4-Hydroxy-2,5-dicarboxyphenyl)iminod… | ligand_6740 | H5L | 20~30 | -0.05~0.25 | 1 | 4 | ref_eq_net_8120 | O=C(O)CN(CC(=O)O)c1cc(C(=O)O)c(O)cc1C(=O)O |
| `H^[+]` | metal_68 | N-[2,5-Dicarboxy-4-(carboxymethylamino)… | ligand_6749 | H5L | 20~30 | -0.05~0.25 | 1 | 5 | ref_eq_net_8154 | O=C(O)CNc1cc(C(=O)O)c(N(CC(=O)O)CC(=O)O)cc1C(=O)O |
| `H^[+]` | metal_68 | Pyridine-3-carboxylic acid methylamide | ligand_8023 | L | 16.5~31.5 | 0.275~0.725 | 1 | 1 | ref_eq_net_14360 | CNC(=O)c1cccnc1 |
| `K^[+]` | metal_78 | Butane-1,2,3,4-tetracarboxylic acid | ligand_9072 | H4L | 19~30 | -0.15~0.25 | 2 | 1 | ref_eq_net_22281 | O=C(O)CC(C(=O)O)C(CC(=O)O)C(=O)O |
| `Li^[+]` | metal_80 | Ammonia | ligand_10103 | L | 19~30 | -0.05~5.15 | 6 | 1 | ref_eq_net_28199 | N |
| `Me_[2]Sn^[2+]` | metal_85 | Butane-1,2,3,4-tetracarboxylic acid | ligand_9072 | H4L | 20~30 | -0.05~0.25 | 1 | 5 | ref_eq_net_22287 | O=C(O)CC(C(=O)O)C(CC(=O)O)C(=O)O |
| `Mg^[2+]` | metal_92 | Ammonia | ligand_10103 | L | 19~30 | -0.05~2.15 | 2 | 3 | ref_eq_net_28206 | N |
| `Mg^[2+]` | metal_92 | Butane-1,2,3,4-tetracarboxylic acid | ligand_9072 | H4L | 19~30 | -0.15~0.25 | 2 | 1 | ref_eq_net_22283 | O=C(O)CC(C(=O)O)C(CC(=O)O)C(=O)O |
| `Mg^[2+]` | metal_92 | N-(4-Hydroxy-2,5-dicarboxyphenyl)iminod… | ligand_6740 | H5L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_8121 | O=C(O)CN(CC(=O)O)c1cc(C(=O)O)c(O)cc1C(=O)O |
| `Mg^[2+]` | metal_92 | N-[2,5-Dicarboxy-4-(carboxymethylamino)… | ligand_6749 | H5L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_8155 | O=C(O)CNc1cc(C(=O)O)c(N(CC(=O)O)CC(=O)O)cc1C(=O)O |
| `Mn^[2+]` | metal_94 | Ammonia | ligand_10103 | L | 19~30 | -0.05~5.15 | 6 | 4 | ref_eq_net_28219 | N |
| `Mn^[2+]` | metal_94 | N-(4-Hydroxy-2,5-dicarboxyphenyl)iminod… | ligand_6740 | H5L | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_8125 | O=C(O)CN(CC(=O)O)c1cc(C(=O)O)c(O)cc1C(=O)O |
| `Na^[+]` | metal_106 | Butane-1,2,3,4-tetracarboxylic acid | ligand_9072 | H4L | 19~30 | -0.15~0.25 | 2 | 1 | ref_eq_net_22279 | O=C(O)CC(C(=O)O)C(CC(=O)O)C(=O)O |
| `Ni^[2+]` | metal_112 | 2,5-Bis[N-(carboxymethyl)-N-(2-hydroxye… | ligand_6727 | H4L | 20~30 | -0.05~0.25 | 1 | 4 | ref_eq_net_8036 | O=C(O)CN(CCO)c1cc(C(=O)O)c(N(CCO)CC(=O)O)cc1C(=O)O |
| `Ni^[2+]` | metal_112 | 2,5-Bis[bis(2-hydroxyethyl)amino]benzen… | ligand_6719 | H2L | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_8008 | O=C(O)c1cc(N(CCO)CCO)c(C(=O)O)cc1N(CCO)CCO |
| `Ni^[2+]` | metal_112 | 2-Bis(2-hydroxyethyl)amino-5-(2-hydroxy… | ligand_6718 | H2L | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_8005 | O=C(O)c1cc(N(CCO)CCO)c(C(=O)O)cc1NCCO |
| `Ni^[2+]` | metal_112 | N-(4-Hydroxy-2,5-dicarboxyphenyl)iminod… | ligand_6740 | H5L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_8127 | O=C(O)CN(CC(=O)O)c1cc(C(=O)O)c(O)cc1C(=O)O |
| `Ni^[2+]` | metal_112 | N-[2,5-Dicarboxy-4-(carboxymethylamino)… | ligand_6749 | H5L | 20~30 | -0.05~0.25 | 1 | 3 | ref_eq_net_8160 | O=C(O)CNc1cc(C(=O)O)c(N(CC(=O)O)CC(=O)O)cc1C(=O)O |
| `Ni^[2+]` | metal_112 | Pyridine-3-carboxylic acid methylamide | ligand_8023 | L | 16.5~31.5 | 0.275~0.725 | 1 | 3 | ref_eq_net_14362 | CNC(=O)c1cccnc1 |
| `Sr^[2+]` | metal_177 | Ammonia | ligand_10103 | L | 19~30 | -0.05~2.15 | 4 | 1 | ref_eq_net_28211 | N |
| `Sr^[2+]` | metal_177 | N-(4-Hydroxy-2,5-dicarboxyphenyl)iminod… | ligand_6740 | H5L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_8123 | O=C(O)CN(CC(=O)O)c1cc(C(=O)O)c(O)cc1C(=O)O |
| `Sr^[2+]` | metal_177 | N-[2,5-Dicarboxy-4-(carboxymethylamino)… | ligand_6749 | H5L | 20~30 | -0.05~0.25 | 1 | 1 | ref_eq_net_8157 | O=C(O)CNc1cc(C(=O)O)c(N(CC(=O)O)CC(=O)O)cc1C(=O)O |
| `Zn^[2+]` | metal_208 | N-(4-Hydroxy-2,5-dicarboxyphenyl)iminod… | ligand_6740 | H5L | 20~30 | -0.05~0.25 | 1 | 2 | ref_eq_net_8129 | O=C(O)CN(CC(=O)O)c1cc(C(=O)O)c(O)cc1C(=O)O |

### Global max-node network: `H^[+]` + N-[2,5-Dicarboxy-4-(carboxymethylamino)phenyl]iminodiacetic…
network_id: ref_eq_net_8154 | metal_id: metal_68 | ligand_id: ligand_6749 | ligand_def_HxL: H5L | nodes: 5

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_68 | ``[H4L] + [H] <=> [H5L]`` | logK | -1.8 |
| beta_def_64 | ``[H3L] + [H] <=> [H4L]`` | logK | 2.67 |
| beta_def_53 | ``[H2L] + [H] <=> [H3L]`` | logK | 3.57 |
| beta_def_32 | ``[HL] + [H] <=> [H2L]`` | logK | 4.48 |
| beta_def_79 | ``[L] + [H] <=> [HL]`` | logK | 9.4 |

---
