# Q3.1.6 — Tool Results (batch 2)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "lanthanum",
  "limit": 5
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_79 | La^[3+] | La | 3 | ✓ | [La+3] | InChI=1S/La/q+3 | beta_totN_30 | ligand_totN_297 | vlm_totN_931 |

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "ligand_class": "carboxylic acid",
  "limit": 30
}
```

[summary]
## search_ligands — 30 result(s)

**stats:** 804 SQL matches · showing 30 · limit 30

| ligand_id | ligand_name | HxL_def | ligand_class | vlm_count | smiles | pka_brackets |
|-----------|-------------|---------|--------------|-----------|--------|--------------|
| ligand_5950 | 1-Carboxymethyl-2-ketopiperazine | HL | Aza macrocycles with car… | 1 | `O=C(O)CN1CCNCC1=O` | (-inf, HL, 6.55, L, +inf) |
| ligand_5951 | 4-Carboxymethyl-2-ketopiperazine | HL | Aza macrocycles with car… | 1 | `O=C(O)CN1CCNC(=O)C1` | (-inf, HL, 5.51, L, +inf) |
| ligand_5952 | 1,4-Bis(carboxymethyl)-2-ketopiperazine | H2L | Aza macrocycles with car… | 2 | `O=C(O)CN1CCN(CC(=O)O)C(=O)C1` | (-inf, H2L, 2.95, HL, 5.87, L, +inf) |
| ligand_6058 | 1,4-Diazacyclohexa… (Piperazine-1,4-diacetic acid) | H2L | Aza macrocycles with car… | 17 | `O=C(O)CN1CCN(CC(=O)O)CC1` | (-inf, H3L, -1.8, H2L, 4.4, HL, 8.67, L, +inf) |
| ligand_6059 | 1,4-Diazacycloheptane-N,N'-diacetic acid | H2L | Aza macrocycles with car… | 18 | `O=C(O)CN1CCCN(CC(=O)O)CC1` | (-inf, H3L, 2.04, H2L, 5.92, HL, 9.53, L, +inf) |
| ligand_6060 | 1,4-Diazacycloheptane-N,N'-di(2-propanoic acid) | H2L | Aza macrocycles with car… | 3 | `CC(CN1CCCN(C(C)C(=O)O)CC1)C(=O)O` | (-inf, H2L, 6.11, HL, 10.2, L, +inf) |
| ligand_6061 | 1,4-Diazacycloheptane-N,N'-di(2-butanoic acid) | H2L | Aza macrocycles with car… | 3 | `CCC(C(=O)O)N1CCCN(C(CC)C(=O)O)CC1` | (-inf, H2L, 5.74, HL, 9.82, L, +inf) |
| ligand_6062 | 1,4-Diazacycloheptane-N,N'-di(2-pentanoic acid) | H2L | Aza macrocycles with car… | 3 | `CCCC(C(=O)O)N1CCCN(C(CCC)C(=O)O)CC1` | (-inf, H2L, 5.67, HL, 9.88, L, +inf) |
| ligand_6063 | 1,5-Diazacyclooctane-N,N'-diacetic acid | H2L | Aza macrocycles with car… | 31 | `O=C(O)CN1CCCN(CC(=O)O)CCC1` | (-inf, H3L, -1.9, H2L, 4.78, HL, 4.78, L, +inf) |
| ligand_6064 | 1-Oxa-4,7-diazacyclononane-N,N'-diacetic acid | H2L | Aza macrocycles with car… | 16 | `O=C(O)CN1CCOCCN(CC(=O)O)CC1` | (-inf, H3L, -1.8, H2L, 4.02, HL, 10.57, L, +inf) |
| ligand_6065 | 1-Thia-4,7-diazacyclononane-N,N'-diacetic acid | H2L | Aza macrocycles with car… | 25 | `O=C(O)CN1CCSCCN(CC(=O)O)CC1` | (-inf, H3L, -1.8, H2L, 4.05, HL, 4.05, L, +inf) |
| ligand_6066 | 1-Thia-4,8-diazacyclodecane-N,N'-diacetic acid | H2L | Aza macrocycles with car… | 14 | `O=C(O)CN1CCCN(CC(=O)O)CCSCC1` | (-inf, H3L, 2, H2L, 3.95, HL, 3.95, L, +inf) |
| ligand_6067 | 1,4-Dioxa-7,10-diazacyclododecane-N,N'-diacetic a… | H2L | Aza macrocycles with car… | 15 | `O=C(O)CN1CCOCCOCCN(CC(=O)O)CC1` | (-inf, H2L, 4.84, HL, 10.54, L, +inf) |
| ligand_6068 | 1,4-Dioxa-7,11-diazacyclotridecane-7,11-diacetic … | H2L | Aza macrocycles with car… | 27 | `O=C(O)CN1CCCN(CC(=O)O)CCOCCOCC1` | (-inf, H3L, 2.42, H2L, 6.95, HL, 9.91, L, +inf) |
| ligand_6069 | 1,7-Dioxa-4,10-diazacyclododecane-N,N'-diacetic a… | H2L | Aza macrocycles with car… | 16 | `O=C(O)CN1CCOCCN(CC(=O)O)CCOCC1` | (-inf, H3L, 2.11, H2L, 7.46, HL, 9.53, L, +inf) |
| ligand_6070 | 1,4,10-Trioxa-7,13-diazacyclopentadecane-N,N'-dia… | H2L | Aza macrocycles with car… | 74 | `O=C(O)CN1CCOCCOCCN(CC(=O)O)CCOCC1` | (-inf, H3L, 2, H2L, 8.45, HL, 8.63, L, +inf) |
| ligand_6071 | 1,4,10,13-Tetraoxa-7,16-diazacyclooctadecane-N,N'… | H2L | Aza macrocycles with car… | 74 | `O=C(O)CN1CCOCCOCCN(CC(=O)O)CCOCCOCC1` | (-inf, H3L, 2.2, H2L, 7.9, HL, 7.9, L, +inf) |
| ligand_6073 | 6,11-Dioxo-1,4,7,10-tetraazacyclododecane-1,4-dia… | H2L | Aza macrocycles with car… | 25 | `O=C(O)CN1CCN(CC(=O)O)CC(=O)NCCNC(=O)C1` | (-inf, H2L, 3.54, HL, 6.5, L, +inf) |
| ligand_6074 | 6,12-Dioxo-1,4,7,11-tetraazacyclotridecane-1,4-di… | H2L | Aza macrocycles with car… | 22 | `O=C(O)CN1CCN(CC(=O)O)CC(=O)NCCCNC(=O)C1` | (-inf, H2L, 3.4, HL, 6.41, L, +inf) |
| ligand_6075 | 1,4,7-Triazacyclononane-N-acetic acid (NOMA) | HL | Aza macrocycles with car… | 17 | `O=C(O)CN1CCNCCNCC1` | (-inf, H3L, 2.82, H2L, 7.45, HL, 7.45, L, +inf) |
| ligand_6076 | 1,4,7-Triazacyclononane-N,N',N''-triacetic… (NOTA) | H3L | Aza macrocycles with car… | 55 | `O=C(O)CN1CCN(CC(=O)O)CCN(CC(=O)O)CC1` | (-inf, H4L, -1.7, H3L, 3.17, H2L, 5.7, HL, 5.7, L, +inf) |
| ligand_6077 | 1,4,7-Triazacyclodecane-N,N',N''-triacetic… (DETA) | H3L | Aza macrocycles with car… | 3 | `O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CC1` | (-inf, H4L, -2.3, H3L, 3.69, H2L, 6.12, HL, +inf) |
| ligand_6078 | 9-Methyl-1,4,7-triazacyclodecane-N,N',N''-triacet… | H3L | Aza macrocycles with car… | 2 | `CC1CN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)C1` | (-inf, H3L, 3.65, H2L, 6, HL, +inf) |
| ligand_6079 | 9,9-Methyl-1,4,7-triazacyclodecane-N,N',N''-triac… | H3L | Aza macrocycles with car… | 2 | `CC1(C)CN(CC(=O)O)CCN(CC(=O)O)CCN(CC(=O)O)C1` | (-inf, H3L, 3.78, H2L, 6.28, HL, +inf) |
| ligand_6080 | 1,4,8-Triazacyclodecane-N,N',N''-triacetic… (UNTA) | H3L | Aza macrocycles with car… | 3 | `O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCC1` | (-inf, H4L, -1.7, H3L, 3.4, H2L, 7.2, HL, +inf) |
| ligand_6081 | 1,5,9-Triazacyclododecane-N,N',N''-triace… (DOTRA) | H3L | Aza macrocycles with car… | 9 | `O=C(O)CN1CCCN(CC(=O)O)CCCN(CC(=O)O)CCC1` | (-inf, H4L, 2.1, H3L, 3.65, H2L, 7.55, HL, 7.55, L, +inf) |
| ligand_6082 | 1-Oxa-4,7,10-triazacyclododecane-4,10-diacetic ac… | H2L | Aza macrocycles with car… | 26 | `O=C(O)CN1CCNCCN(CC(=O)O)CCOCC1` | (-inf, H4L, -1.4, H3L, 2.94, H2L, 6.02, HL, 6.02, L, +inf) |
| ligand_6083 | 1-Oxa-4,8,12-triazacyclotetradecane-4,12-diacetic… | H2L | Aza macrocycles with car… | 17 | `O=C(O)CN1CCCNCCCN(CC(=O)O)CCOCC1` | (-inf, H3L, 3.58, H2L, 6.97, HL, 6.97, L, +inf) |
| ligand_6084 | 1-Oxa-4,7,10-triazacyclododecane-4,7,10-triacetic… | H3L | Aza macrocycles with car… | 50 | `O=C(O)CN1CCOCCN(CC(=O)O)CCN(CC(=O)O)CC1` | (-inf, H4L, 2.7, H3L, 4.03, H2L, 7.73, HL, 7.73, L, +inf) |
| ligand_6085 | 1-Oxa-4,7,11-triazacyclotridecane-4,7,11-triaceti… | H3L | Aza macrocycles with car… | 24 | `O=C(O)CN1CCCN(CC(=O)O)CCN(CC(=O)O)CCOCC1` | (-inf, H4L, 2.31, H3L, 4.17, H2L, 8.39, HL, 8.39, L, +inf) |

### Functional groups across all SQL matches (797 parseable SMILES)

| group | count | % |
|-------|-------|---|
| carboxyl | 796 | 100% |
| aromatic_ring | 363 | 46% |
| tertiary_amine | 130 | 16% |
| hydroxyl | 120 | 15% |
| halide | 93 | 12% |
| thioether | 92 | 12% |
| amide | 56 | 7% |
| ether | 55 | 7% |
| pyridine | 39 | 5% |
| secondary_amine | 31 | 4% |
| thiol | 24 | 3% |
| primary_amine | 19 | 2% |
| ester | 16 | 2% |
| ketone | 14 | 2% |
| nitrile | 10 | 1% |
| sulfonate | 9 | 1% |
| phenol | 7 | 1% |
| phosphate | 7 | 1% |
| phosphonate | 5 | 1% |
| aldehyde | 3 | 0% |
| imine | 1 | 0% |

---

### Step 5: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_79"
}
```

[summary]
[CATALOG]
## build_system_catalog — 20 pair(s), 59 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_194 | [M] + [HL]^2 <=> [M(HL)2] |  |
| beta_def_352 | [ML3(s)] <=> [M] + [L]^3 | solid |
| beta_def_741 | [ML] + [H]^2 <=> [MH2L] |  |
| beta_def_779 | [M] + [HL] <=> [MHL] |  |
| beta_def_788 | [ML] + [H] <=> [MHL] |  |
| beta_def_792 | [ML2] + [H] <=> [MHL2] |  |
| beta_def_812 | [M] + [L] <=> [ML] |  |
| beta_def_840 | [M] + [L]^2 <=> [ML2] |  |
| beta_def_872 | [M] + [L]^3 <=> [ML3] |  |
| beta_def_894 | [M] + [L]^4 <=> [ML4] |  |
| beta_def_981 | [ML] + [OH] <=> [M(OH)L] |  |

*(all species aqueous unless noted)*

**1. La^[3+] + Propanedioic acid (Malonic acid)** (metal_79 + ligand_8873) — ligand_def_HxL: H2L | 20 ent, 4 sp, 20 vlms (vlm_152038…vlm_152057)
   - species: beta_def_779(4) beta_def_792(3) beta_def_812(8) beta_def_840(5)
   - eq:4 nets T:19~30°C I:-0.15~1.15M max 4n/4e
**2. La^[3+] + D-2,3-Dihydroxybutanedioic acid (D-Tartaric acid)** (metal_79 + ligand_8955) — ligand_def_HxL: H2L | 19 ent, 3 sp, 19 vlms (vlm_154960…vlm_154978)
   - species: beta_def_779(6) beta_def_812(7) beta_def_840(6)
   - eq:5 nets T:19~30°C I:-0.15~1.15M max 3n/3e
**3. La^[3+] + Hydroxyacetic acid (Glycolic acid)** (metal_79 + ligand_8640) — ligand_def_HxL: HL | 19 ent, 4 sp, 19 vlms (vlm_147101…vlm_147119)
   - species: beta_def_812(6) beta_def_840(5) beta_def_872(5) beta_def_894(3)
   - eq:4 nets T:19~30°C I:-0.05~2.15M max 4n/6e
**4. La^[3+] + 2-Hydroxy-2-methylpropanoic acid** (metal_79 + ligand_8647) — ligand_def_HxL: HL | 17 ent, 3 sp, 17 vlms (vlm_148045…vlm_148061)
   - species: beta_def_812(6) beta_def_840(6) beta_def_872(5)
   - eq:4 nets T:19~30°C I:-0.05~2.15M max 3n/3e
**5. La^[3+] + Ethanoic acid (Acetic acid)** (metal_79 + ligand_8465) — ligand_def_HxL: HL | 17 ent, 3 sp, 17 vlms (vlm_144473…vlm_144489)
   - species: beta_def_812(6) beta_def_840(6) beta_def_872(5)
   - eq:4 nets T:19~30°C I:-0.15~2.15M max 3n/3e
**6. La^[3+] + Pentane-2,4-dione (Acetylacetone)** (metal_79 + ligand_9526) — ligand_def_HxL: *** | 14 ent, 3 sp, 14 vlms (vlm_165187…vlm_165200)
   - species: beta_def_812(5) beta_def_840(5) beta_def_872(4)
   - eq:3 nets T:19~35°C I:-0.15~2.15M max 3n/3e
**7. La^[3+] + Hydrogen sulfate ion (Sulfuric acid)** (metal_79 + ligand_10148) — ligand_def_HxL: HL | 13 ent, 2 sp, 13 vlms (vlm_175723…vlm_175735)
   - species: beta_def_812(8) beta_def_840(5)
   - eq:4 nets T:19~30°C I:-0.05~2.15M max 2n/1e
**8. La^[3+] + D-2-Hydroxypropanoic acid (Lactic acid)** (metal_79 + ligand_8641) — ligand_def_HxL: HL | 13 ent, 3 sp, 13 vlms (vlm_147517…vlm_147529)
   - species: beta_def_812(5) beta_def_840(4) beta_def_872(4)
   - eq:3 nets T:15~30°C I:-0.05~2.15M max 3n/3e
**9. La^[3+] + Ethylenedinitrilo-N,N'-di(3-propanoic)-N,N'-diacetic acid** (metal_79 + ligand_6309) — ligand_def_HxL: H4L | 12 ent, 2 sp, 12 vlms (vlm_110121…vlm_110132)
   - species: beta_def_779(6) beta_def_812(6)
   - eq:2 nets T:19~30°C I:-0.05~0.65M max 2n/1e
**10. La^[3+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_79 + ligand_6277) — ligand_def_HxL: H4L | 12 ent, 2 sp, 12 vlms (vlm_108389…vlm_108400)
   - species: beta_def_788(3) beta_def_812(9)
   - eq:4 nets T:15~30°C I:-0.05~1.15M max 2n/1e
**11. La^[3+] + Oxydiacetic acid (Diglycolic acid)** (metal_79 + ligand_8974) — ligand_def_HxL: H2L | 11 ent, 3 sp, 11 vlms (vlm_155427…vlm_155437)
   - species: beta_def_812(4) beta_def_840(4) beta_def_872(3)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 3n/3e
**12. La^[3+] + Nitrilotriacetic acid (NTA)** (metal_79 + ligand_6165) — ligand_def_HxL: H3L | 11 ent, 3 sp, 11 vlms (vlm_105294…vlm_105304)
   - species: beta_def_812(6) beta_def_840(3) beta_def_981(2)
   - eq:3 nets T:15~30°C I:-0.05~0.65M max 3n/2e
**13. La^[3+] + Ethylenebis(oxyacetic acid)** (metal_79 + ligand_8986) — ligand_def_HxL: H2L | 10 ent, 4 sp, 10 vlms (vlm_155881…vlm_155890)
   - species: beta_def_792(3) beta_def_812(3) beta_def_840(3) beta_def_872(1)
   - eq:1 nets T:16.5~31.5°C I:0.775~1.225M max 4n/4e
**14. La^[3+] + Ethylenediiminodiacetic acid (EDDA)** (metal_79 + ligand_5975) — ligand_def_HxL: H2L | 10 ent, 4 sp, 10 vlms (vlm_100320…vlm_100329)
   - species: beta_def_741(1) beta_def_788(1) beta_def_812(4) beta_def_840(4)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 4n/4e
**15. La^[3+] + Pyridine-2,6-dicarboxylic acid (Dipicolinic acid)** (metal_79 + ligand_6774) — ligand_def_HxL: H2L | 9 ent, 3 sp, 9 vlms (vlm_119355…vlm_119363)
   - species: beta_def_812(3) beta_def_840(3) beta_def_872(3)
   - eq:1 nets T:16.5~31.5°C I:0.275~0.725M max 3n/3e
**16. La^[3+] + Pyridine-2-carboxylic acid (Picolinic acid)** (metal_79 + ligand_6762) — ligand_def_HxL: HL | 9 ent, 4 sp, 9 vlms (vlm_118694…vlm_118702)
   - species: beta_def_812(4) beta_def_840(2) beta_def_872(2) beta_def_894(1)
   - eq:2 nets T:19~30°C I:-0.05~0.65M max 4n/6e
**17. La^[3+] + Hydrogen fluoride (Hydrofluoric acid)** (metal_79 + ligand_10162) — ligand_def_HxL: HL | 8 ent, 2 sp, 8 vlms (vlm_176718…vlm_176725)
   - species: beta_def_352(2) beta_def_812(6)
   - eq:4 nets T:19~30°C I:-0.15~1.15M max 2n/1e
**18. La^[3+] + L-Hydroxybutanedioic acid (Hydroxysuccinic acid)(Malic acid)** (metal_79 + ligand_8953) — ligand_def_HxL: H2L | 8 ent, 3 sp, 8 vlms (vlm_154773…vlm_154780)
   - species: beta_def_779(2) beta_def_812(3) beta_def_840(3)
   - eq:3 nets T:19~30°C I:-0.05~1.15M max 3n/3e
**19. La^[3+] + Mercaptoacetic acid (Thioglycolic acid)** (metal_79 + ligand_8766) — ligand_def_HxL: H2L | 8 ent, 2 sp, 8 vlms (vlm_150501…vlm_150508)
   - species: beta_def_194(4) beta_def_779(4)
   - eq:2 nets T:19~30°C I:-0.05~2.15M max 2n/1e
**20. La^[3+] + 2-Methylpropanoic acid (Isobutyric acid)** (metal_79 + ligand_8473) — ligand_def_HxL: HL | 8 ent, 2 sp, 8 vlms (vlm_145441…vlm_145448)
   - species: beta_def_812(4) beta_def_840(4)
   - eq:2 nets T:16.5~31.5°C I:0.275~2.225M max 2n/1e

---

### Step 7: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_79 AND c.beta_definition_id = beta_def_812)",
  "order_by": "s.constant_value DESC",
  "limit": 30
}
```

[summary]
## search_stability — 30 row(s)

### ΔS — 24 metal-ligand pair(s)
| metal_id | metal_name | ligand_id | ligand_name | ligand_HxL_def | ligand_SMILES | vlm_counts | beta_counts | T°C_range | I(M)_range | non_aqueous_phases | ref_eq_map_counts |
|----------|------------|-----------|-------------|----------------|---------------|------------|-------------|-----------|------------|--------------------|-------------------|
| metal_79 | La^[3+] | ligand_6301 | trans-1,2-Cyclohexylenedini… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCCC[C@H]1N(CC(=O)O)CC(=O)O | 2 | 1 | 20~25 | 0.1~0.5 | *** | 0 |
| metal_79 | La^[3+] | ligand_6277 | Ethylenedinitrilotetraaceti… | H4L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_79 | La^[3+] | ligand_6165 | Nitrilotriacetic acid (NTA) | H3L | O=C(O)CN(CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_79 | La^[3+] | ligand_6267 | N-Methylethylenedinitrilotr… | H3L | CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_79 | La^[3+] | ligand_6275 | N-(2-Hydroxyethyl)ethylened… | H3L | O=C(O)CN(CCO)CCN(CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_79 | La^[3+] | ligand_6309 | Ethylenedinitrilo-N,N'-di(3… | H4L | O=C(O)CCN(CCN(CCC(=O)O)CC(=O)O)CC(=O)O | 2 | 1 | 25 | 0.1~0.5 | *** | 0 |
| metal_79 | La^[3+] | ligand_6356 | Diethylenetrinitrilopentaac… | H5L | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6298 | trans-1,2-Cyclopentylenedin… | H4L | O=C(O)CN(CC(=O)O)[C@@H]1CCC[C@H]1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6311 | Trimethylenedinitrilotetraa… | H4L | O=C(O)CN(CCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6335 | Oxybis(ethylenenitrilo)tetr… | H4L | O=C(O)CN(CCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6751 | 1,2-Phenylenedinitrilotetra… | H4L | O=C(O)CN(CC(=O)O)c1ccccc1N(CC(=O)O)CC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6348 | Thiobis(ethylenenitrilo)tet… | H4L | O=C(O)CN(CCSCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6342 | Ethylenebis(oxyethylenenitr… | H4L | O=C(O)CN(CCOCCOCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6362 | Diethylenetrinitrilopentaac… | *** | *** | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6313 | Tetramethylenedinitrilotetr… | H4L | O=C(O)CN(CCCCN(CC(=O)O)CC(=O)O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_9054 | Benzene-1,2,3-tricarboxylic… | H3L | O=C(O)c1cccc(C(=O)O)c1C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_10148 | Hydrogen sulfate ion (Sulfu… | HL | O=S(=O)([O-])O | 1 | 1 | 25 | 0 | *** | 0 |
| metal_79 | La^[3+] | ligand_8985 | Benzene-1,2-bis(oxyacetic a… | H2L | O=C(O)COc1ccccc1OCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8937 | trans-Cyclohexane-1,4-dicar… | H2L | O=C(O)[C@H]1CC[C@H](C(=O)O)CC1 | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8873 | Propanedioic acid (Malonic … | H2L | O=C(O)CC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_5975 | Ethylenediiminodiacetic aci… | H2L | O=C(O)CNCCNCC(=O)O | 1 | 1 | 25 | 1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6127 | Iminodiacetic acid (IDA) | H2L | O=C(O)CNCC(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_8915 | cis-Butenedioic acid (Malei… | H2L | O=C(O)/C=C\C(=O)O | 1 | 1 | 25 | 0.1 | *** | 0 |
| metal_79 | La^[3+] | ligand_6774 | Pyridine-2,6-dicarboxylic a… | H2L | O=C(O)c1cccc(C(=O)O)n1 | 1 | 1 | 25 | 0.5 | *** | 0 |

---

### Step 8: `search_stability`
**Args:**
```json
{
  "where": "(c.metal_id = metal_79 AND c.ligand_id = ligand_6277)",
  "order_by": "s.constant_value DESC",
  "limit": 10
}
```

[summary]
## search_stability — 10 row(s)

### `La^[3+]` + Ethylenedinitrilotetraacetic acid (EDTA) — 10 measurement(s)
metal_id: metal_79 | ligand_id: ligand_6277
ligand_HxL_def: H4L | ligand_SMILES: O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CC(=O)O

| vlm_id | ref_eq_map | beta_def | type | value | T°C | I(M) | equation | non_aqueous_phases | HxL_involved | pKa_bracket_involved |
|--------|------------|----------|------|-------|-----|------|----------|--------------------|--------------|-------------|
| vlm_108396 | *** | beta_def_812 | ΔS | 253.6 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108397 | *** | beta_def_812 | ΔS | 222.6 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108389 | ref_eq_map_4946 | beta_def_812 | logK | 15.36 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108390 | ref_eq_map_4947 | beta_def_812 | logK | 14.48 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108398 | ref_eq_map_4946 | beta_def_788 | logK | 2.24 | 25 | 0.1 | `[ML] + [H] <=> [MHL]` | *** |  |  |
| vlm_108399 | ref_eq_map_4948 | beta_def_788 | logK | 2 | 20 | 0.1 | `[ML] + [H] <=> [MHL]` | *** |  |  |
| vlm_108400 | ref_eq_map_4949 | beta_def_788 | logK | 2 | 25 | 1 | `[ML] + [H] <=> [MHL]` | *** |  |  |
| vlm_108391 | *** | beta_def_812 | ΔH | -12.1 | 25 | 0.1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108392 | *** | beta_def_812 | ΔH | -16.3 | 25 | 0.5 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |
| vlm_108395 | *** | beta_def_812 | ΔH | -18.8 | 40 | 1 | `[M] + [L] <=> [ML]` | *** | [L] | (9.52, L, +inf) |

---
