# Q3.1.4 — Tool Results (batch 2)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "Iron(II), Iron(III)",
  "limit": 10
}
```

[summary]
## search_metals

*(no results)*

---

### Step 4: `search_metals`
**Args:**
```json
{
  "name": "iron, ferric, ferrous",
  "symbol": "Fe",
  "limit": 20
}
```

[summary]
## search_metals

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
  "symbol": "Fe(II), Fe(III), Fe",
  "limit": 50
}
```

[summary]
## search_metals

*(no results)*

---

### Step 7: `search_metals`
**Args:**
```json
{
  "metal_id": 26,
  "limit": 10
}
```

[summary]
## search_metals — 1 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_26 | Cd^[2+] | Cd | 2 | ✓ | [Cd+2] | InChI=1S/Cd/q+2 | beta_totN_95 | ligand_totN_818 | vlm_totN_2828 |

---

### Step 8: `search_metals`
**Args:**
```json
{
  "name": "Fe^[2+], Fe^[3+], Fe",
  "symbol": "Fe",
  "limit": 20,
  "exclude": "Cd^[2+]"
}
```

[summary]
## search_metals

*(no results)*

---

### Step 9: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT metal_id, metal_name, symbol, charge FROM metal_card WHERE symbol = 'Fe' OR metal_name LIKE '%Fe%' OR metal_name LIKE '%iron%' OR metal_name LIKE '%ferric%' OR metal_name LIKE '%ferrous%' LIMIT 20;"
}
```

[PHASE ERROR] Tool 'execute_srd46_sql' is not available yet. You must call 0_plan_search_strategy first (PHASE 2) before using the execution tools.

---

### Step 10: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_26"
}
```

[summary]
[CATALOG]
## build_system_catalog — 20 pair(s), 83 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_107 | [M(H-1L)] + [H] <=> [ML] |  |
| beta_def_339 | [ML2(s,beta)] <=> [M] + [L]^2 | solid |
| beta_def_345 | [ML2(s,gamma)] <=> [M] + [L]^2 | solid |
| beta_def_374 | [M]^2 + [L]^2 <=> [M2(H-1L)2] + [H]^2 |  |
| beta_def_502 | [M]^2 + [L] <=> [M2L] |  |
| beta_def_519 | [M]^2 + [L]^2 <=> [M2L2] |  |
| beta_def_674 | [M]^4 + [L]^4 <=> [M4L4] |  |
| beta_def_732 | [M] + [H2L] <=> [MH2L] |  |
| beta_def_739 | [MHL] + [H] <=> [MH2L] |  |
| beta_def_779 | [M] + [HL] <=> [MHL] |  |
| beta_def_788 | [ML] + [H] <=> [MHL] |  |
| beta_def_812 | [M] + [L] <=> [ML] |  |
| beta_def_840 | [M] + [L]^2 <=> [ML2] |  |
| beta_def_872 | [M] + [L]^3 <=> [ML3] |  |
| beta_def_894 | [M] + [L]^4 <=> [ML4] |  |
| beta_def_966 | [M(OH)L] + [H] <=> [ML] + [H2O] |  |

*(all species aqueous unless noted)*

**1. Cd^[2+] + Hydrogen thiocyanate (Thiocyanic acid)** (metal_26 + ligand_10092) — ligand_def_HxL: HL | 51 ent, 4 sp, 51 vlms (vlm_172405…vlm_172455)
   - species: beta_def_812(15) beta_def_840(16) beta_def_872(13) beta_def_894(7)
   - eq:7 nets T:19~30°C I:-0.15~3.15M max 4n/6e
**2. Cd^[2+] + Bromide ion** (metal_26 + ligand_10168) — ligand_def_HxL: *** | 49 ent, 4 sp, 49 vlms (vlm_178102…vlm_178150)
   - species: beta_def_812(14) beta_def_840(14) beta_def_872(12) beta_def_894(9)
   - eq:8 nets T:19~30°C I:-0.05~4.15M max 4n/6e
**3. Cd^[2+] + Ammonia** (metal_26 + ligand_10103) — ligand_def_HxL: L | 49 ent, 4 sp, 49 vlms (vlm_173415…vlm_173463)
   - species: beta_def_812(13) beta_def_840(12) beta_def_872(12) beta_def_894(12)
   - eq:5 nets T:19~30°C I:-0.15~3.15M max 4n/6e
**4. Cd^[2+] + Hydrogen cyanide (Hydrocyanic acid)** (metal_26 + ligand_10090) — ligand_def_HxL: HL | 44 ent, 4 sp, 44 vlms (vlm_172010…vlm_172053)
   - species: beta_def_812(11) beta_def_840(11) beta_def_872(11) beta_def_894(11)
   - eq:5 nets T:5~45°C I:-0.15~3.15M max 4n/6e
**5. Cd^[2+] + Iodide ion** (metal_26 + ligand_10171) — ligand_def_HxL: *** | 40 ent, 4 sp, 40 vlms (vlm_178489…vlm_178528)
   - species: beta_def_812(12) beta_def_840(9) beta_def_872(9) beta_def_894(10)
   - eq:7 nets T:19~30°C I:-0.15~4.15M max 4n/6e
**6. Cd^[2+] + Ethanoic acid (Acetic acid)** (metal_26 + ligand_8465) — ligand_def_HxL: HL | 40 ent, 3 sp, 40 vlms (vlm_144851…vlm_144890)
   - species: beta_def_812(16) beta_def_840(13) beta_def_872(11)
   - eq:6 nets T:19~30°C I:-0.15~3.15M max 3n/3e
**7. Cd^[2+] + 1,3-Diazole (Imidazole)** (metal_26 + ligand_7795) — ligand_def_HxL: L | 33 ent, 5 sp, 33 vlms (vlm_133984…vlm_134016)
   - species: beta_def_812(9) beta_def_840(9) beta_def_872(8) beta_def_894(6) beta_def_966(1)
   - eq:7 nets T:19~41°C I:-0.15~3.15M max 5n/7e
**8. Cd^[2+] + Thiocarbamide (Thiourea)** (metal_26 + ligand_10004) — ligand_def_HxL: L | 32 ent, 4 sp, 32 vlms (vlm_169498…vlm_169529)
   - species: beta_def_812(9) beta_def_840(9) beta_def_872(7) beta_def_894(7)
   - eq:5 nets T:19~30°C I:-0.05~3.15M max 4n/6e
**9. Cd^[2+] + Aminoacetic acid (Glycine)** (metal_26 + ligand_5760) — ligand_def_HxL: HL | 32 ent, 3 sp, 32 vlms (vlm_93961…vlm_93992)
   - species: beta_def_812(11) beta_def_840(11) beta_def_872(10)
   - eq:7 nets T:5~45°C I:-0.15~1.15M max 3n/3e
**10. Cd^[2+] + Chloride ion** (metal_26 + ligand_10163) — ligand_def_HxL: *** | 30 ent, 3 sp, 30 vlms (vlm_177542…vlm_177571)
   - species: beta_def_812(11) beta_def_840(10) beta_def_872(9)
   - eq:7 nets T:19~30°C I:-0.15~4.15M max 3n/3e
**11. Cd^[2+] + Ethylenediamine** (metal_26 + ligand_7029) — ligand_def_HxL: L | 29 ent, 3 sp, 29 vlms (vlm_122544…vlm_122572)
   - species: beta_def_812(10) beta_def_840(10) beta_def_872(9)
   - eq:6 nets T:19~30°C I:-0.15~3.15M max 3n/3e
**12. Cd^[2+] + Hydroxide ion** (metal_26 + ligand_10076) — ligand_def_HxL: *** | 23 ent, 8 sp, 23 vlms (vlm_170962…vlm_170984)
   - species: beta_def_339(4) beta_def_345(1) beta_def_502(4) beta_def_674(4) beta_def_812(5) beta_def_840(2) beta_def_872(1) beta_def_894(2)
   - eq:3 nets T:19~30°C I:-0.05~3.15M max 8n/28e
**13. Cd^[2+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_26 + ligand_6277) — ligand_def_HxL: H4L | 23 ent, 4 sp, 23 vlms (vlm_108725…vlm_108747)
   - species: beta_def_739(1) beta_def_788(5) beta_def_812(14) beta_def_966(3)
   - eq:5 nets T:19~30°C I:-0.15~3.15M max 4n/5e
**14. Cd^[2+] + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid)** (metal_26 + ligand_9058) — ligand_def_HxL: H3L | 22 ent, 6 sp, 22 vlms (vlm_157765…vlm_157786)
   - species: beta_def_107(3) beta_def_374(1) beta_def_732(2) beta_def_779(5) beta_def_812(6) beta_def_840(5)
   - eq:4 nets T:19~30°C I:-0.05~2.15M max 5n/10e
**15. Cd^[2+] + Thiosemicarbazide** (metal_26 + ligand_10025) — ligand_def_HxL: L | 18 ent, 3 sp, 18 vlms (vlm_169870…vlm_169887)
   - species: beta_def_812(7) beta_def_840(7) beta_def_872(4)
   - eq:3 nets T:19~30°C I:-0.05~1.15M max 3n/3e
**16. Cd^[2+] + Hydrogen thiosulfate (Thiosulfuric acid)** (metal_26 + ligand_10149) — ligand_def_HxL: H2L | 17 ent, 5 sp, 17 vlms (vlm_176296…vlm_176312)
   - species: beta_def_519(1) beta_def_812(8) beta_def_840(5) beta_def_872(2) beta_def_894(1)
   - eq:4 nets T:19~35°C I:-0.05~3.15M max 5n/10e
**17. Cd^[2+] + 4-(2-Aminoethyl)imidazole (Histamine)** (metal_26 + ligand_7849) — ligand_def_HxL: L | 17 ent, 5 sp, 17 vlms (vlm_134701…vlm_134717)
   - species: beta_def_788(3) beta_def_812(5) beta_def_840(5) beta_def_872(3) beta_def_966(1)
   - eq:3 nets T:19~41°C I:-0.15~0.3M max 4n/4e
**18. Cd^[2+] + Hydrogen azide (Hydrazoic acid)** (metal_26 + ligand_10106) — ligand_def_HxL: HL | 16 ent, 4 sp, 16 vlms (vlm_173681…vlm_173696)
   - species: beta_def_812(4) beta_def_840(4) beta_def_872(4) beta_def_894(4)
   - eq:2 nets T:16.5~31.5°C I:1.775~3.225M max 4n/6e
**19. Cd^[2+] + Selenocyanate ion** (metal_26 + ligand_10093) — ligand_def_HxL: L | 15 ent, 4 sp, 15 vlms (vlm_172583…vlm_172597)
   - species: beta_def_812(6) beta_def_840(3) beta_def_872(3) beta_def_894(3)
   - eq:2 nets T:19~30°C I:-0.05~1.15M max 4n/6e
**20. Cd^[2+] + 2-(Methylaminomethyl)pyridine** (metal_26 + ligand_8112) — ligand_def_HxL: L | 15 ent, 3 sp, 15 vlms (vlm_137742…vlm_137756)
   - species: beta_def_812(7) beta_def_840(7) beta_def_872(1)
   - eq:3 nets T:19~30°C I:-0.15~0.65M max 3n/3e

---
