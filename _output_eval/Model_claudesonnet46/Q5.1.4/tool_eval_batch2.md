# Q5.1.4 — Tool Results (batch 2)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "zinc",
  "limit": 20
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_208 | Zn^[2+] | Zn | 2 | ✓ | [Zn+2] | InChI=1S/Zn/q+2 | beta_totN_122 | ligand_totN_1169 | vlm_totN_4095 |

---

### Step 4: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_208"
}
```

[summary]
[CATALOG]
## build_system_catalog — 20 pair(s), 94 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_204 | [MHL2] + [H] <=> [M(HL)2] |  |
| beta_def_238 | [M(OH)2L] + [H] <=> [M(OH)L] + [H2O] |  |
| beta_def_334 | [ML2(s)] <=> [M] + [L]^2 | solid |
| beta_def_337 | [ML2(s,am)] <=> [M] + [L]^2 | solid |
| beta_def_340 | [ML2(s,beta1)] <=> [M] + [L]^2 | solid |
| beta_def_341 | [ML2(s,beta2)] <=> [M] + [L]^2 | solid |
| beta_def_343 | [ML2(s,delta)] <=> [M] + [L]^2 | solid |
| beta_def_344 | [ML2(s,epsilon)] <=> [M] + [L]^2 | solid |
| beta_def_345 | [ML2(s,gamma)] <=> [M] + [L]^2 | solid |
| beta_def_347 | [MO(s)] + [H2O] <=> [M] + [OH]^2 | solid |
| beta_def_374 | [M]^2 + [L]^2 <=> [M2(H-1L)2] + [H]^2 |  |
| beta_def_502 | [M]^2 + [L] <=> [M2L] |  |
| beta_def_636 | [M]^3 + [H] + [L]^4 <=> [M3HL4] |  |
| beta_def_637 | [M3L4] + [H] <=> [M3HL4] |  |
| beta_def_651 | [M3(OH)L4] + [H] <=> [M3L4] + [H2O] |  |
| beta_def_674 | [M]^4 + [L]^4 <=> [M4L4] |  |
| beta_def_739 | [MHL] + [H] <=> [MH2L] |  |
| beta_def_751 | [MH2L] + [H] <=> [MH3L] |  |
| beta_def_765 | [MH3L] + [H] <=> [MH4L] |  |
| beta_def_779 | [M] + [HL] <=> [MHL] |  |
| beta_def_788 | [ML] + [H] <=> [MHL] |  |
| beta_def_792 | [ML2] + [H] <=> [MHL2] |  |
| beta_def_812 | [M] + [L] <=> [ML] |  |
| beta_def_840 | [M] + [L]^2 <=> [ML2] |  |
| beta_def_872 | [M] + [L]^3 <=> [ML3] |  |
| beta_def_894 | [M] + [L]^4 <=> [ML4] |  |
| beta_def_966 | [M(OH)L] + [H] <=> [ML] + [H2O] |  |
| beta_def_984 | [M(OH)L2] + [H] <=> [ML2] + [H2O] |  |

*(all species aqueous unless noted)*

**1. Zn^[2+] + Aminoacetic acid (Glycine)** (metal_208 + ligand_5760) — ligand_def_HxL: HL | 37 ent, 4 sp, 37 vlms (vlm_93924…vlm_93960)
   - species: beta_def_812(12) beta_def_840(13) beta_def_872(11) beta_def_966(1)
   - eq:7 nets T:5~45°C I:-0.15~1.15M max 4n/4e
**2. Zn^[2+] + Ethylenediamine** (metal_208 + ligand_7029) — ligand_def_HxL: L | 36 ent, 3 sp, 36 vlms (vlm_122508…vlm_122543)
   - species: beta_def_812(12) beta_def_840(12) beta_def_872(12)
   - eq:8 nets T:19~41°C I:-0.15~3.15M max 3n/3e
**3. Zn^[2+] + Hydroxide ion** (metal_208 + ligand_10076) — ligand_def_HxL: *** | 33 ent, 13 sp, 33 vlms (vlm_170929…vlm_170961)
   - species: beta_def_337(4) beta_def_340(2) beta_def_341(2) beta_def_343(2) beta_def_344(2) beta_def_345(2) beta_def_347(4) beta_def_502(3) beta_def_674(1) beta_def_812(5) beta_def_840(2) beta_def_872(2) beta_def_894(2)
   - eq:4 nets T:19~30°C I:-0.15~3.15M max 11n/55e
**4. Zn^[2+] + Hydrogen cyanide (Hydrocyanic acid)** (metal_208 + ligand_10090) — ligand_def_HxL: HL | 30 ent, 5 sp, 30 vlms (vlm_171980…vlm_172009)
   - species: beta_def_334(1) beta_def_812(2) beta_def_840(9) beta_def_872(9) beta_def_894(9)
   - eq:5 nets T:5~45°C I:-0.15~3.15M max 5n/10e
**5. Zn^[2+] + 1,3-Diazole (Imidazole)** (metal_208 + ligand_7795) — ligand_def_HxL: L | 30 ent, 4 sp, 30 vlms (vlm_133954…vlm_133983)
   - species: beta_def_812(9) beta_def_840(7) beta_def_872(7) beta_def_894(7)
   - eq:7 nets T:19~41°C I:-0.05~3.15M max 4n/6e
**6. Zn^[2+] + L-2-Amino-3-(4-imidazolyl)propanoic acid (Histidine)** (metal_208 + ligand_5898) — ligand_def_HxL: HL | 29 ent, 6 sp, 29 vlms (vlm_98899…vlm_98927)
   - species: beta_def_204(1) beta_def_788(4) beta_def_792(3) beta_def_812(8) beta_def_840(12) beta_def_984(1)
   - eq:6 nets T:19~41°C I:-0.05~3.15M max 5n/6e
**7. Zn^[2+] + Hydrogen thiocyanate (Thiocyanic acid)** (metal_208 + ligand_10092) — ligand_def_HxL: HL | 24 ent, 4 sp, 24 vlms (vlm_172381…vlm_172404)
   - species: beta_def_812(8) beta_def_840(6) beta_def_872(5) beta_def_894(5)
   - eq:6 nets T:19~30°C I:-0.15~5.15M max 4n/6e
**8. Zn^[2+] + L-2-Amino-3-mercaptopropanoic acid (Cysteine)** (metal_208 + ligand_5856) — ligand_def_HxL: H2L | 23 ent, 8 sp, 23 vlms (vlm_97446…vlm_97468)
   - species: beta_def_204(4) beta_def_636(4) beta_def_637(3) beta_def_651(1) beta_def_779(2) beta_def_792(4) beta_def_812(1) beta_def_840(4)
   - eq:4 nets T:15~41°C I:-0.05~3.15M max 7n/14e
**9. Zn^[2+] + Ammonia** (metal_208 + ligand_10103) — ligand_def_HxL: L | 21 ent, 4 sp, 21 vlms (vlm_173394…vlm_173414)
   - species: beta_def_812(6) beta_def_840(5) beta_def_872(5) beta_def_894(5)
   - eq:4 nets T:19~30°C I:-0.15~2.15M max 4n/6e
**10. Zn^[2+] + Nitrilotris(methylenephosphonic acid) (NTP)** (metal_208 + ligand_8412) — ligand_def_HxL: H6L | 21 ent, 5 sp, 21 vlms (vlm_143422…vlm_143442)
   - species: beta_def_739(2) beta_def_751(2) beta_def_765(1) beta_def_788(7) beta_def_812(9)
   - eq:2 nets T:19~30°C I:-0.15~0.25M max 5n/7e
**11. Zn^[2+] + Iminodiacetic acid (IDA)** (metal_208 + ligand_6127) — ligand_def_HxL: H2L | 20 ent, 2 sp, 20 vlms (vlm_104424…vlm_104443)
   - species: beta_def_812(10) beta_def_840(10)
   - eq:3 nets T:19~41°C I:-0.05~1.15M max 2n/1e
**12. Zn^[2+] + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid)** (metal_208 + ligand_9058) — ligand_def_HxL: H3L | 19 ent, 4 sp, 19 vlms (vlm_157746…vlm_157764)
   - species: beta_def_374(3) beta_def_779(5) beta_def_812(6) beta_def_840(5)
   - eq:4 nets T:19~41°C I:-0.05~0.65M max 4n/6e
**13. Zn^[2+] + 1,10-Phenanthroline (Dipyridino[a,c]benzene)** (metal_208 + ligand_8191) — ligand_def_HxL: L | 19 ent, 3 sp, 19 vlms (vlm_139340…vlm_139358)
   - species: beta_def_812(7) beta_def_840(6) beta_def_872(6)
   - eq:3 nets T:19~30°C I:-0.15~1.15M max 3n/3e
**14. Zn^[2+] + L-2-Aminopropanoic acid (Alanine)** (metal_208 + ligand_5761) — ligand_def_HxL: HL | 19 ent, 4 sp, 19 vlms (vlm_94305…vlm_94323)
   - species: beta_def_812(7) beta_def_840(7) beta_def_872(3) beta_def_966(2)
   - eq:5 nets T:19~41°C I:-0.15~1.15M max 4n/4e
**15. Zn^[2+] + 2,2'-Bipyridyl** (metal_208 + ligand_8156) — ligand_def_HxL: L | 18 ent, 3 sp, 18 vlms (vlm_138658…vlm_138675)
   - species: beta_def_812(6) beta_def_840(6) beta_def_872(6)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 3n/3e
**16. Zn^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_208 + ligand_6277) — ligand_def_HxL: H4L | 18 ent, 4 sp, 18 vlms (vlm_108707…vlm_108724)
   - species: beta_def_739(1) beta_def_788(5) beta_def_812(6) beta_def_966(6)
   - eq:5 nets T:19~30°C I:-0.15~3.15M max 4n/5e
**17. Zn^[2+] + N-(2-Hydroxyethyl)iminodiacetic acid (HIDA)** (metal_208 + ligand_6204) — ligand_def_HxL: H2L | 18 ent, 4 sp, 18 vlms (vlm_106769…vlm_106786)
   - species: beta_def_238(1) beta_def_812(8) beta_def_840(8) beta_def_966(1)
   - eq:1 nets T:20~30°C I:-0.05~0.25M max 4n/3e
**18. Zn^[2+] + D-2-Amino-3-mercapto-3-methylbutanoic acid (Penicillamine)** (metal_208 + ligand_5857) — ligand_def_HxL: H2L | 18 ent, 8 sp, 18 vlms (vlm_97593…vlm_97610)
   - species: beta_def_204(4) beta_def_636(1) beta_def_637(1) beta_def_779(2) beta_def_792(4) beta_def_812(1) beta_def_840(4) beta_def_984(1)
   - eq:4 nets T:15~41°C I:-0.05~3.15M max 6n/13e
**19. Zn^[2+] + Ethanoic acid (Acetic acid)** (metal_208 + ligand_8465) — ligand_def_HxL: HL | 17 ent, 3 sp, 17 vlms (vlm_144834…vlm_144850)
   - species: beta_def_812(8) beta_def_840(6) beta_def_872(3)
   - eq:6 nets T:19~30°C I:-0.15~3.15M max 3n/3e
**20. Zn^[2+] + DL-Methylethylenediamine (1,2-Propylenediamine) (pn)** (metal_208 + ligand_7030) — ligand_def_HxL: L | 17 ent, 3 sp, 17 vlms (vlm_122671…vlm_122687)
   - species: beta_def_812(8) beta_def_840(8) beta_def_872(1)
   - eq:8 nets T:19~35°C I:-0.15~2.15M max 3n/3e

---

### Step 5: `db_ranked_pairs`
**Args:**
```json
{
  "rank_by": "vlm_count",
  "limit": 15,
  "where": "lc.metal_id = 208"
}
```

[summary]
**db_ranked_pairs:** Error - Unknown rank_by='vlm_count'. Choose from: ['ligands_per_metal', 'measurements_per_ligand', 'measurements_per_metal', 'metals_per_ligand', 'pka_per_ligand']

---

### Step 6: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208 AND s.temperature_c BETWEEN 24 AND 26 AND s.ionic_strength_mol_l BETWEEN 0.09 AND 0.11)",
  "order_by": "s.constant_value DESC",
  "limit": 20
}
```

[summary]
## search_stability — 20 row(s)

### ΔS — 19 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_208 | Zn^[2+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 2 | 2 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_8412 | Nitrilotris(methylenephosph… | H6L | O=P(O)(O)CN(CP(=O)(O)O)CP(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6109 | 1,4,8,11-Tetraazacyclotetra… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6112 | 1,4,8,12-Tetraazacyclopenta… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCCN(CC(=O)O)CCN(CC(=O)O)CCC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6311 | Trimethylenedinitrilotetraa… | H4L | O=C(O)CN(CCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_10117 | Hydrogen triphosphate (Trip… | H5L | O=P(O)(O)OP(=O)(O)OP(=O)(O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6278 | DL-(Methylethylene)dinitril… | H4L | CC(CN(CC(=O)O)CC(=O)O)N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6104 | 1,4,7,10-Tetraazacyclotride… | H4L | O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6313 | Tetramethylenedinitrilotetr… | H4L | O=C(O)CN(CCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6739 | N-(2,5-Dicarboxyphenyl)imin… | H4L | O=C(O)CN(CC(=O)O)c1cc(C(=O)O)ccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6070 | 1,4,10-Trioxa-7,13-diazacyc… | H2L | O=C(O)CN1CCOCCOCCN(CC(=O)O)CCOCC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6736 | N-(2-Carboxyphenyl)iminodia… | H3L | O=C(O)CN(CC(=O)O)c1ccccc1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6348 | Thiobis(ethylenenitrilo)tet… | H4L | O=C(O)CN(CCSCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6314 | Pentamethylenedinitrilotetr… | H4L | O=C(O)CN(CCCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6071 | 1,4,10,13-Tetraoxa-7,16-dia… | H2L | O=C(O)CN1CCOCCOCCN(CC(=O)O)CCOCCOCC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_208 | Zn^[2+] | ligand_6140 | N-Methyliminodiacetic acid … | H2L | CN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |

---

### Step 7: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id = metal_208)",
  "limit": 10
}
```

[summary]
## search_networks — 36 row(s)

> **Reference equilibrium networks (compact)** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### Beta-definition legend
| beta_def | equation |
|----------|----------|
| beta_def_840 | ``[M] + [L]^2 <=> [ML2]`` |
| beta_def_812 | ``[M] + [L] <=> [ML]`` |
| beta_def_872 | ``[M] + [L]^3 <=> [ML3]`` |
| beta_def_966 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` |
| beta_def_839 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` |
| beta_def_975 | ``[M(OH)2L] + [H] <=> [M(OH)L] + [H2O]`` |
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` |
| beta_def_516 | ``[ML] + [M] <=> [M2L]`` |
| beta_def_515 | ``[M2(OH)L] + [H] <=> [M2L] + [H2O]`` |
| beta_def_739 | ``[MHL] + [H] <=> [MH2L]`` |

### Metal-ligand pair summary
| metal | metal_id | ligand | ligand_id | HxL | T_range | I_range | net_count | max_nodes | ligand_SMILES |
|-------|----------|--------|-----------|-----|---------|---------|-----------|----------|---------------|
| `Zn^[2+]` | metal_208 | Aminoacetic acid (Glycine) | ligand_5760 | HL | 5~45 | -0.15~1.15 | 7 | 4 | NCC(=O)O |
| `Zn^[2+]` | metal_208 | 6,16-Dioxa-3,9,13,19-tetraaza-1,11(2,6)… | ligand_7653 | L | 20~30 | -0.05~0.25 | 1 | 6 | c1cc2nc(c1)CNCCOCCNCc1cccc(n1)CNCCOCCNC2 |
| `Zn^[2+]` | metal_208 | 6,9,19,22-Tetraoxa-3,12,16,25-tetraaza-… | ligand_7654 | L | 20~30 | -0.05~0.25 | 1 | 6 | c1cc2nc(c1)CNCCOCCOCCNCc1cccc(n1)CNCCOCCOCCNC2 |
| `Zn^[2+]` | metal_208 | 13,16,21,24-Tetramethyl-4,7-dioxa-1,10,… | ligand_7655 | L | 20~30 | -0.05~0.25 | 1 | 2 | CN1CCN(C)CCN2CCOCCOCCN(CC1)CCN(C)CCN(C)CC2 |

### Max-node network per pair
| metal | metal_id | ligand | ligand_id | max_net_id | max_nodes | max_edge_counts | max_T_range | max_I_range | max_vlm_counts | max_beta_def_ids | max_type | max_values |
|-------|----------|--------|----------|------------|-----------|------------------|-------------|-------------|----------------|------------------|----------|------------|
| `Zn^[2+]` | metal_208 | Aminoacetic acid (Glycine) | ligand_5760 | ref_eq_net_113 | 4 | 4 | 31~41 | 0~0.3 | 4 | 4 diff beta_def | logK | 4.87~11.3 |
| `Zn^[2+]` | metal_208 | 6,16-Dioxa-3,9,13,19-tetraaza-1,11(2,6)… | ligand_7653 | ref_eq_net_171 | 6 | 12 | 20~30 | -0.05~0.25 | 6 | 6 diff beta_def | logK | 3.8~11 |
| `Zn^[2+]` | metal_208 | 6,9,19,22-Tetraoxa-3,12,16,25-tetraaza-… | ligand_7654 | ref_eq_net_176 | 6 | 12 | 20~30 | -0.05~0.25 | 6 | 6 diff beta_def | logK | 3.9~9.7 |
| `Zn^[2+]` | metal_208 | 13,16,21,24-Tetramethyl-4,7-dioxa-1,10,… | ligand_7655 | ref_eq_net_187 | 2 | 1 | 20~30 | -0.05~0.25 | 2 | beta_def_788; beta_def_812 | logK | 6.6~6.8 |

### Global max-node network: `Zn^[2+]` + 6,16-Dioxa-3,9,13,19-tetraaza-1,11(2,6)-dipyridinacycloeico…
network_id: ref_eq_net_171 | metal_id: metal_208 | ligand_id: ligand_7653 | ligand_def_HxL: L | nodes: 6

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_516 | ``[ML] + [M] <=> [M2L]`` | logK | 3.8 |
| beta_def_515 | ``[M2(OH)L] + [H] <=> [M2L] + [H2O]`` | logK | 7.07 |
| beta_def_788 | ``[ML] + [H] <=> [MHL]`` | logK | 7.45 |
| beta_def_812 | ``[M] + [L] <=> [ML]`` | logK | 8.89 |
| beta_def_839 | ``[M(OH)L] + [H] <=> [ML] + [H2O]`` | logK | 9.52 |
| beta_def_975 | ``[M(OH)2L] + [H] <=> [M(OH)L] + [H2O]`` | logK | 11 |

---
