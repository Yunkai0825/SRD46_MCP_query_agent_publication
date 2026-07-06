# Q2.2.3 — Tool Results (batch 2)

### Step 2: `search_metals`
**Args:**
```json
{
  "name": "H+",
  "limit": 10
}
```

[summary]
## search_metals — 10 result(s)

| metal_id | metal_name | symbol | charge | simple_ion | smiles | inchi | beta_def_count | ligand_count | vlm_count |
|----------|------------|--------|--------|------------|--------|-------|----------------|--------------|-----------|
| metal_20 | BuHg^[+] | B | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_23 | BuNH_[3]^[+] | B | 1 |  | *** | *** | beta_totN_1 | ligand_totN_2 | vlm_totN_2 |
| metal_24 | C(NH_[2])_[3]^[+] | C | 1 |  | *** | *** | beta_totN_0 | ligand_totN_0 | vlm_totN_0 |
| metal_45 | Et_[2]NH_[2]^[+] | E2NH2 | 1 |  | *** | *** | beta_totN_1 | ligand_totN_1 | vlm_totN_1 |
| metal_48 | Et_[3]NH^[+] | E3NH | 1 |  | *** | *** | beta_totN_1 | ligand_totN_1 | vlm_totN_1 |
| metal_53 | EtHg^[+] | EHg | 1 |  | *** | *** | beta_totN_4 | ligand_totN_3 | vlm_totN_6 |
| metal_54 | EtNH_[3]^[+] | ENH3 | 1 |  | *** | *** | beta_totN_1 | ligand_totN_3 | vlm_totN_3 |
| metal_68 | H^[+] | H | 1 | ✓ | [H+] | InChI=1S/p+1 | beta_totN_82 | ligand_totN_4081 | vlm_totN_20720 |
| metal_69 | H_[5]TeO_[6]^[-] | H | -1 |  | *** | *** | beta_totN_1 | ligand_totN_1 | vlm_totN_2 |
| metal_70 | Hf^[4+] | Hf | 4 | ✓ | [Hf+4] | InChI=1S/Hf/q+4 | beta_totN_10 | ligand_totN_14 | vlm_totN_49 |

---

### Step 3: `search_ligands`
**Args:**
```json
{
  "name": "DTPA, TTHA, DOTA, phytate, inositol hexakisphosphate, hexametaphosphate, tripolyphosphate",
  "limit": 20
}
```

[summary]
## search_ligands

*(no results)*

---

### Step 4: `build_system_catalog`
**Args:**
```json
{
  "metal_id": "metal_68"
}
```

[summary]
[CATALOG]
## build_system_catalog — 20 pair(s), 92 species *(ultra-compact)*

### Equation legend

| beta_def_id | equation | note |
|-------------|----------|------|
| beta_def_32 | [HL] + [H] <=> [H2L] |  |
| beta_def_33 | [CO2(g)] + [H2O] <=> [H2L] | gas |
| beta_def_50 | * |  |
| beta_def_51 | [HV10O28] + [H] <=> [H2V10O28] |  |
| beta_def_53 | [H2L] + [H] <=> [H3L] |  |
| beta_def_61 | [H2V10O28] + [H] <=> [H3V10O28] |  |
| beta_def_64 | [H3L] + [H] <=> [H4L] |  |
| beta_def_68 | [H4L] + [H] <=> [H5L] |  |
| beta_def_72 | [H5L] + [H] <=> [H6L] |  |
| beta_def_73 | [H4L] + [H]^2 <=> [H6L] |  |
| beta_def_76 | [H6L] + [H] <=> [H7L] |  |
| beta_def_77 | [H7L] + [H] <=> [H8L] |  |
| beta_def_79 | [L] + [H] <=> [HL] |  |
| beta_def_95 | [V10O28] + [H] <=> [HV10O28] |  |
| beta_def_96 | [V2O7] + [H] <=> [HV2O7] |  |
| beta_def_97 | [V4O13] + [H] <=> [HV4O13] |  |
| beta_def_1013 | [HL]^2 <=> [V2O7] + [H2O] |  |
| beta_def_1014 | [H2L]^4 <=> [V4O12] + [H2O]^4 |  |
| beta_def_1015 | [HV4O13] + [H] <=> [V4O12] + [H2O] |  |
| beta_def_1016 | [H2L]^5 <=> [V5O15] + [H2O]^5 |  |
| beta_def_1017 | * |  |
| beta_def_1018 | [H2L] + [H]^2 <=> [VO2] + [H2O]^2 |  |

*(all species aqueous unless noted)*

**1. H^[+] + Hydrogen vanadate (Vanadic acid)** (metal_68 + ligand_10077) — ligand_def_HxL: H3L | 92 ent, 14 sp, 92 vlms (vlm_171266…vlm_171357)
   - species: beta_def_32(12) beta_def_50(4) beta_def_51(10) beta_def_61(2) beta_def_79(13) beta_def_95(10) beta_def_96(5) beta_def_97(4) beta_def_1013(7) beta_def_1014(10) beta_def_1015(3) beta_def_1016(4) beta_def_1017(3) beta_def_1018(5)
   - eq:21 nets T:15~30°C I:-0.05~3.15M max 12n/50e
**2. H^[+] + Hydrogen phosphate (Phosphoric acid)** (metal_68 + ligand_10113) — ligand_def_HxL: H3L | 84 ent, 4 sp, 84 vlms (vlm_174186…vlm_174269)
   - species: beta_def_32(31) beta_def_53(24) beta_def_64(1) beta_def_79(28)
   - eq:21 nets T:5~45°C I:-0.15~5.15M max 4n/6e
**3. H^[+] + Ethylenedinitrilotetraacetic acid (EDTA)** (metal_68 + ligand_6277) — ligand_def_HxL: H4L | 75 ent, 6 sp, 75 vlms (vlm_108224…vlm_108298)
   - species: beta_def_32(18) beta_def_53(10) beta_def_64(7) beta_def_68(6) beta_def_72(4) beta_def_79(30)
   - eq:14 nets T:19~41°C I:-0.15~3.15M max 6n/15e
**4. H^[+] + 1,4,7,10,13,16-Hexaazahexadecane (Pentaethylenehexamine) (2,2,2,2,2-hex)** (metal_68 + ligand_7246) — ligand_def_HxL: L | 72 ent, 6 sp, 72 vlms (vlm_126593…vlm_126664)
   - species: beta_def_32(12) beta_def_53(12) beta_def_64(12) beta_def_68(12) beta_def_72(12) beta_def_79(12)
   - eq:4 nets T:19~30°C I:-0.15~1.15M max 6n/15e
**5. H^[+] + Nitrilotriacetic acid (NTA)** (metal_68 + ligand_6165) — ligand_def_HxL: H3L | 72 ent, 4 sp, 72 vlms (vlm_105158…vlm_105229)
   - species: beta_def_32(18) beta_def_53(19) beta_def_64(7) beta_def_79(28)
   - eq:15 nets T:15~41°C I:-0.15~3.15M max 4n/6e
**6. H^[+] + N-(Phosphonomethyl)glycine (Glyphosate)** (metal_68 + ligand_5937) — ligand_def_HxL: H3L | 70 ent, 4 sp, 70 vlms (vlm_99687…vlm_99756)
   - species: beta_def_32(22) beta_def_53(22) beta_def_64(1) beta_def_79(25)
   - eq:13 nets T:19~30°C I:-0.15~5.15M max 4n/6e
**7. H^[+] + 1,4,7,10,13-Pentaazatridecane (Tetraethylenepentamine)(tetren)(2,2,2,2-pent)** (metal_68 + ligand_7244) — ligand_def_HxL: L | 65 ent, 5 sp, 65 vlms (vlm_126479…vlm_126543)
   - species: beta_def_32(13) beta_def_53(13) beta_def_64(13) beta_def_68(13) beta_def_79(13)
   - eq:5 nets T:19~41°C I:-0.15~1.15M max 5n/10e
**8. H^[+] + Iminobis(methylenephosphonic acid) (IDP)** (metal_68 + ligand_8380) — ligand_def_HxL: H4L | 64 ent, 5 sp, 64 vlms (vlm_142412…vlm_142475)
   - species: beta_def_32(17) beta_def_53(15) beta_def_64(15) beta_def_68(2) beta_def_79(15)
   - eq:4 nets T:19~30°C I:-0.15~1.15M max 5n/10e
**9. H^[+] + Butanedioic acid (Succinic acid)** (metal_68 + ligand_8907) — ligand_def_HxL: H2L | 60 ent, 2 sp, 60 vlms (vlm_153268…vlm_153327)
   - species: beta_def_32(28) beta_def_79(32)
   - eq:22 nets T:5~45°C I:-0.15~4.15M max 2n/1e
**10. H^[+] + Hydrogen diphosphate (Pyrophosphoric acid)** (metal_68 + ligand_10114) — ligand_def_HxL: H4L | 59 ent, 4 sp, 59 vlms (vlm_174571…vlm_174629)
   - species: beta_def_32(21) beta_def_53(9) beta_def_64(7) beta_def_79(22)
   - eq:16 nets T:19~30°C I:-0.15~3.15M max 4n/6e
**11. H^[+] + Propanedioic acid (Malonic acid)** (metal_68 + ligand_8873) — ligand_def_HxL: H2L | 59 ent, 2 sp, 59 vlms (vlm_151918…vlm_151976)
   - species: beta_def_32(28) beta_def_79(31)
   - eq:21 nets T:5~45°C I:-0.15~3.15M max 2n/1e
**12. H^[+] + Nitrilotris(methylenephosphonic acid) (NTP)** (metal_68 + ligand_8412) — ligand_def_HxL: H6L | 59 ent, 6 sp, 59 vlms (vlm_143208…vlm_143266)
   - species: beta_def_32(13) beta_def_53(12) beta_def_64(12) beta_def_68(3) beta_def_73(6) beta_def_79(13)
   - eq:3 nets T:19~30°C I:-0.15~1.15M max 6n/15e
**13. H^[+] + Diethylenetrinitrilopentaacetic acid (DTPA)** (metal_68 + ligand_6356) — ligand_def_HxL: H5L | 57 ent, 8 sp, 57 vlms (vlm_112470…vlm_112526)
   - species: beta_def_32(14) beta_def_53(8) beta_def_64(8) beta_def_68(8) beta_def_72(2) beta_def_76(2) beta_def_77(1) beta_def_79(14)
   - eq:10 nets T:15~41°C I:-0.05~1.15M max 8n/28e
**14. H^[+] + Ethanedioic acid (Oxalic acid)** (metal_68 + ligand_8872) — ligand_def_HxL: H2L | 56 ent, 2 sp, 56 vlms (vlm_151494…vlm_151549)
   - species: beta_def_32(18) beta_def_79(38)
   - eq:25 nets T:5~45°C I:-0.15~9.15M max 2n/1e
**15. H^[+] + 1-Hydroxyethane-1,1-diphosphonic acid (Etidronic acid)** (metal_68 + ligand_9142) — ligand_def_HxL: H4L | 54 ent, 4 sp, 54 vlms (vlm_159111…vlm_159164)
   - species: beta_def_32(17) beta_def_53(15) beta_def_64(13) beta_def_79(9)
   - eq:7 nets T:19~30°C I:-0.15~2.15M max 4n/6e
**16. H^[+] + L-2-Amino-3-(4-imidazolyl)propanoic acid (Histidine)** (metal_68 + ligand_5898) — ligand_def_HxL: HL | 51 ent, 3 sp, 51 vlms (vlm_98706…vlm_98756)
   - species: beta_def_32(17) beta_def_53(17) beta_def_79(17)
   - eq:6 nets T:19~41°C I:-0.15~3.15M max 3n/3e
**17. H^[+] + Hydrogen triphosphate (Triphosphoric acid)** (metal_68 + ligand_10117) — ligand_def_HxL: H5L | 50 ent, 5 sp, 50 vlms (vlm_174813…vlm_174862)
   - species: beta_def_32(16) beta_def_53(6) beta_def_64(6) beta_def_68(6) beta_def_79(16)
   - eq:10 nets T:19~30°C I:-0.15~1.15M max 5n/10e
**18. H^[+] + Hydrogen carbonate (Carbonic acid)** (metal_68 + ligand_10096) — ligand_def_HxL: H2L | 48 ent, 3 sp, 48 vlms (vlm_172612…vlm_172659)
   - species: beta_def_32(18) beta_def_33(10) beta_def_79(20)
   - eq:16 nets T:5~45°C I:-0.15~5.15M max 3n/2e
**19. H^[+] + 2-Hydroxypropane-1,2,3-tricarboxylic acid (Citric acid)** (metal_68 + ligand_9058) — ligand_def_HxL: H3L | 48 ent, 3 sp, 48 vlms (vlm_157439…vlm_157486)
   - species: beta_def_32(14) beta_def_53(14) beta_def_79(20)
   - eq:14 nets T:13~41°C I:-0.15~3.15M max 3n/3e
**20. H^[+] + Aminoacetic acid (Glycine)** (metal_68 + ligand_5760) — ligand_def_HxL: HL | 48 ent, 2 sp, 48 vlms (vlm_93606…vlm_93653)
   - species: beta_def_32(27) beta_def_79(21)
   - eq:15 nets T:5~45°C I:-0.15~3.15M max 2n/1e

---

### Step 6: `get_table_schema`
**Args:**
```json
{
  "table_name": "ligand_pka_measured",
  "database": "cards"
}
```

[summary]
## get_table_schema - 16 column(s)

| cid | name | type | notnull | pk |
|-----|------|------|---------|----|
| 0 | pka_id | INTEGER | False | True |
| 1 | ligand_id | INTEGER | True | False |
| 2 | source | TEXT | False | False |
| 3 | bracket_from_state | TEXT | False | False |
| 4 | bracket_to_state | TEXT | False | False |
| 5 | pKa | REAL | False | False |
| 6 | pKa_type | TEXT | False | False |
| 7 | temperature_c | REAL | False | False |
| 8 | ionic_strength_mol_l | REAL | False | False |
| 9 | solvent_id | INTEGER | False | False |
| 10 | solvent_name | TEXT | False | False |
| 11 | electrolyte | TEXT | False | False |
| 12 | measurement_method | TEXT | False | False |
| 13 | quality | TEXT | False | False |
| 14 | notes | TEXT | False | False |
| 15 | vlm_ids_json | TEXT | False | False |

---

### Step 7: `get_table_schema`
**Args:**
```json
{
  "table_name": "ligand_card",
  "database": "cards"
}
```

[summary]
## get_table_schema - 13 column(s)

| cid | name | type | notnull | pk |
|-----|------|------|---------|----|
| 0 | ligand_id | INTEGER | False | True |
| 1 | ligand_name_SRD | TEXT | True | False |
| 2 | ligand_class_id | INTEGER | False | False |
| 3 | ligand_class_name | TEXT | False | False |
| 4 | ligand_SMILES | TEXT | False | False |
| 5 | ligand_InChi | TEXT | False | False |
| 6 | formula | TEXT | False | False |
| 7 | composition | TEXT | False | False |
| 8 | figure_definition | TEXT | False | False |
| 9 | definition_HxL | TEXT | False | False |
| 10 | synonym_iupac_name | TEXT | False | False |
| 11 | synonym_common_name | TEXT | False | False |
| 12 | created_at | TIMESTAMP | False | False |

---

### Step 8: `execute_srd46_sql`
**Args:**
```json
{
  "sql_query": "SELECT lc.ligand_id, lc.ligand_name_SRD, COUNT(DISTINCT CASE WHEN p.pKa_type IS NULL OR LOWER(p.pKa_type) NOT LIKE '%micro%' THEN COALESCE(p.bracket_from_state,'') || '->' || COALESCE(p.bracket_to_state,'') END) AS n_distinct_pka_steps FROM ligand_card lc JOIN ligand_pka_measured p ON lc.ligand_id = p.ligand_id GROUP BY lc.ligand_id, lc.ligand_name_SRD HAVING COUNT(DISTINCT CASE WHEN p.pKa_type IS NULL OR LOWER(p.pKa_type) NOT LIKE '%micro%' THEN COALESCE(p.bracket_from_state,'') || '->' || COALESCE(p.bracket_to_state,'') END) > 6 ORDER BY n_distinct_pka_steps DESC, lc.ligand_name_SRD ASC;"
}
```

[summary]
## execute_srd46_sql - 33 row(s)

| ligand_id | ligand_name_SRD | n_distinct_pka_steps |
|-----------|-----------------|----------------------|
| ligand_7541 | 1,4,7,10,13,16,19,22,25,28,31,34-Dodecaazacyclohexatriacontane ([36]aneN12) | 11 |
| ligand_7540 | 1,4,7,10,13,16,19,22,25,28,31-Undecaazacyclotritriacontane ([33]aneN11) | 11 |
| ligand_7539 | 1,4,7,10,13,16,19,22,25,28-Decaazacyclotriacontane ([30]aneN10) | 10 |
| ligand_7253 | 2,5,8,11,14,17,20,23,26,29-Decaazatriacontane (Me2nonaen) | 10 |
| ligand_6368 | Pentaethylenehexanitrilooctaacetic acid (PHOA) | 10 |
| ligand_7538 | 1,4,7,10,13,16,19,22,25-Nonaazacycloheptacosane ([27]aneN9) | 9 |
| ligand_7252 | 2,5,8,11,14,17,20,23,26-Nonaazaheptacosane (Me2octaen) | 9 |
| ligand_6367 | Tetraethylenepentanitriloheptaacetic acid (TPHA) | 9 |
| ligand_7254 | 1,3-Bis(2,5,8,11-tetraazaundecyl)benzene (MXTRIEN) | 8 |
| ligand_7534 | 1,4,7,10,13,16,19,22-Octaazacyclotetracosane ([24]aneN8) | 8 |
| ligand_7535 | 1,5,9,13,17,21,25,32-Octaazacyclodotriacontane ([32]aneN8) | 8 |
| ligand_7543 | 1,5,9,13,17,21,28,32-Octaazabicyclo[11.11.11]pentatriacontane | 8 |
| ligand_7251 | 2,5,8,11,14,17,20,23-Octaazatetracosane (Me2heptaen) | 8 |
| ligand_6356 | Diethylenetrinitrilopentaacetic acid (DTPA) | 8 |
| ligand_8433 | Diethylenetrinitrilopentakis(methylenephosphonic acid) (DTPP) | 8 |
| ligand_6047 | N,N''-Bis(3-hydroxy-6-methyl-2-pyridinylmethyl)diethylenetrinitrilotriacetic ac... | 8 |
| ligand_6041 | N,N'-Bis(3-hydroxy-5-phosphomethyl-2-methyl-4-pyridylmethyl)ethylenedinitrilodi... | 8 |
| ligand_8431 | Oxybis[ethylenenitrilobis(methylenephosphonic acid)] | 8 |
| ligand_6366 | Triethylenetetranitrilohexaacetic acid (TTHA) | 8 |
| ligand_9171 | myo-Inositol-hexa(dihydrogenphosphate) (Phytic acid) | 8 |
| ligand_8432 | (2-Hydroxytrimethylene)dinitrilotetrakis(methylenephosphonic acid) | 7 |
| ligand_7649 | 1,4,16,19-Tetraoxa-7,10,13,22,25,28,31-heptaazacyclotritriacotane ([33]aneN7O4) | 7 |
| ligand_7530 | 1,4,7,10,13,16,19-Heptaazacycloheneicosane ([21]aneN7) | 7 |
| ligand_8403 | 1,4,7,10-Tetraazacyclododecane-1,4,7,10-tetrakis(methylenephosphonic acid) (DOT... | 7 |
| ligand_7422 | 1,4,7-Tris(3-hydroxy-6-methyl-2-pyridylmethyl)-1,4,7-triazacyclononane | 7 |

... 8 more row(s) omitted

---
