# Q2.2.3 — Tool Results (batch 1)

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
  "name": "DTPA, TTHA, DOTA, DTPMP, EDTMP, NTMP, Phytate, ATP, EDTA, EGTA",
  "limit": 50
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

### Step 6: `search_networks`
**Args:**
```json
{
  "where": "(c.metal_id = metal_68 AND n.node_count >= 8)",
  "order_by": "n.node_count DESC",
  "limit": 100
}
```

[summary]
## search_networks — 257 row(s)

> **Reference equilibrium networks (compact)** — each network is built around room-temperature (≈20–25 °C) and low ionic-strength (≈0 M) anchor conditions.

### Beta-definition legend
| beta_def | equation |
|----------|----------|
| beta_def_1016 | ``[H2L]^5 <=> [V5O15] + [H2O]^5`` |
| beta_def_79 | ``[L] + [H] <=> [HL]`` |
| beta_def_1013 | ``[HL]^2 <=> [V2O7] + [H2O]`` |
| beta_def_61 | ``[H2V10O28] + [H] <=> [H3V10O28]`` |
| beta_def_96 | ``[V2O7] + [H] <=> [HV2O7]`` |
| beta_def_51 | ``[HV10O28] + [H] <=> [H2V10O28]`` |
| beta_def_1014 | ``[H2L]^4 <=> [V4O12] + [H2O]^4`` |
| beta_def_32 | ``[HL] + [H] <=> [H2L]`` |
| beta_def_95 | ``[V10O28] + [H] <=> [HV10O28]`` |
| beta_def_1015 | ``[HV4O13] + [H] <=> [V4O12] + [H2O]`` |
| beta_def_1018 | ``[H2L] + [H]^2 <=> [VO2] + [H2O]^2`` |
| beta_def_97 | ``[V4O13] + [H] <=> [HV4O13]`` |
| beta_def_53 | ``[H2L] + [H] <=> [H3L]`` |
| beta_def_64 | ``[H3L] + [H] <=> [H4L]`` |
| beta_def_68 | ``[H4L] + [H] <=> [H5L]`` |
| beta_def_72 | ``[H5L] + [H] <=> [H6L]`` |
| beta_def_76 | ``[H6L] + [H] <=> [H7L]`` |
| beta_def_77 | ``[H7L] + [H] <=> [H8L]`` |
| beta_def_78 | ``[H8L] + [H] <=> [H9L]`` |
| beta_def_25 | ``[H9L] + [H] <=> [H10L]`` |
| beta_def_26 | ``[H10L] + [H] <=> [H11L]`` |
| beta_def_1008 | ``[H2L]^2 <=> [Si2O3(OH)4] + [H]^2 + [H2O]`` |
| beta_def_1007 | ``[Si2O3(OH)4] + [H] <=> [Si2O2(OH)5]`` |
| beta_def_1006 | ``[Si(OH)4]^2 <=> [Si2O(OH)6] + [H2O]`` |
| beta_def_1010 | ``[H2L]^3 <=> [Si3O6(OH)3(cyclo)] + [H]^3 + [H2O]^3`` |
| beta_def_1009 | ``[H2L]^3 <=> [Si3O5(OH)5(linear)] + [H]^3 + [H2O]^2`` |
| beta_def_1011 | ``[H2L]^4 <=> [Si4O7(OH)5(cyclo)] + [H]^3 + [H2O]^4`` |
| beta_def_1012 | ``[Si4O8(OH)4] + [H] <=> [Si4O7(OH)5(cyclo)]`` |

### Metal-ligand pair summary
| metal | metal_id | ligand | ligand_id | HxL | T_range | I_range | net_count | max_nodes | max_net_id | ligand_SMILES |
|-------|----------|--------|-----------|-----|---------|---------|-----------|----------|------------|---------------|
| `H^[+]` | metal_68 | Hydrogen vanadate (Vanadic acid) | ligand_10077 | H3L | 19~30 | -0.05~3.15 | 5 | 12 | ref_eq_net_27594 | [O]=[V]([OH])([OH])[OH] |
| `H^[+]` | metal_68 | 1,4,7,10,13,16,19,22,25,28,31-Undecaaza… | ligand_7540 | L | 20~30 | -0.05~0.25 | 1 | 11 | ref_eq_net_12007 | C1CNCCNCCNCCNCCNCCNCCNCCNCCNCCNCCN1 |
| `H^[+]` | metal_68 | 1,4,7,10,13,16,19,22,25,28,31,34-Dodeca… | ligand_7541 | L | 20~30 | -0.05~0.25 | 1 | 11 | ref_eq_net_12014 | C1CNCCNCCNCCNCCNCCNCCNCCNCCNCCNCCNCCN1 |
| `H^[+]` | metal_68 | Pentaethylenehexanitrilooctaacetic acid… | ligand_6368 | H8L | 20~30 | -0.05~0.25 | 1 | 10 | ref_eq_net_6898 | O=C(O)CN(CCN(CCN(CCN(CC(=O)O)CC(=O)O)CC(=O)O)CC(=O)O)CCN(CCN(CC(=O)O)CC(=O)O)CC(=O)O |
| `H^[+]` | metal_68 | 2,5,8,11,14,17,20,23,26,29-Decaazatriac… | ligand_7253 | L | 20~30 | -0.05~0.25 | 1 | 10 | ref_eq_net_10797 | CNCCNCCNCCNCCNCCNCCNCCNCCNCCNC |
| `H^[+]` | metal_68 | 1,4,7,10,13,16,19,22,25,28-Decaazacyclo… | ligand_7539 | L | 20~30 | -0.05~0.25 | 1 | 10 | ref_eq_net_12000 | C1CNCCNCCNCCNCCNCCNCCNCCNCCNCCN1 |
| `H^[+]` | metal_68 | Tetraethylenepentanitriloheptaacetic ac… | ligand_6367 | H7L | 20~30 | -0.05~0.25 | 1 | 9 | ref_eq_net_6889 | O=C(O)CN(CCN(CCN(CC(=O)O)CC(=O)O)CC(=O)O)CCN(CCN(CC(=O)O)CC(=O)O)CC(=O)O |
| `H^[+]` | metal_68 | 2,5,8,11,14,17,20,23,26-Nonaazaheptacos… | ligand_7252 | L | 20~30 | -0.05~0.25 | 1 | 9 | ref_eq_net_10792 | CNCCNCCNCCNCCNCCNCCNCCNCCNC |
| `H^[+]` | metal_68 | 1,4,7,10,13,16,19,22,25-Nonaazacyclohep… | ligand_7538 | L | 20~30 | -0.05~0.25 | 1 | 9 | ref_eq_net_11993 | C1CNCCNCCNCCNCCNCCNCCNCCNCCN1 |
| `H^[+]` | metal_68 | Hydrogen silicate (Silicic acid) | ligand_10101 | H2L | 19~29 | 0.35~0.65 | 1 | 9 | ref_eq_net_28156 | O[Si](O)(O)O |
| `H^[+]` | metal_68 | N,N'-Bis(3-hydroxy-5-phosphomethyl-2-me… | ligand_6041 | H6L | 20~30 | -0.05~0.25 | 1 | 8 | ref_eq_net_2456 | Cc1ncc(COP(=O)(O)O)c(CN(CCN(CC(=O)O)Cc2c(COP(=O)(O)O)cnc(C)c2O)CC(=O)O)c1O |
| `H^[+]` | metal_68 | N,N''-Bis(3-hydroxy-6-methyl-2-pyridiny… | ligand_6047 | H5L | 20~30 | -0.05~0.25 | 1 | 8 | ref_eq_net_2485 | Cc1ccc(O)c(CN(CCN(CCN(CC(=O)O)Cc2nc(C)ccc2O)CC(=O)O)CC(=O)O)n1 |
| `H^[+]` | metal_68 | Diethylenetrinitrilopentaacetic acid (D… | ligand_6356 | H5L | 20~30 | -0.05~0.25 | 1 | 8 | ref_eq_net_6647 | O=C(O)CN(CCN(CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O |
| `H^[+]` | metal_68 | Triethylenetetranitrilohexaacetic acid … | ligand_6366 | H6L | 20~30 | -0.05~0.25 | 1 | 8 | ref_eq_net_6835 | O=C(O)CN(CCN(CCN(CC(=O)O)CC(=O)O)CC(=O)O)CCN(CC(=O)O)CC(=O)O |
| `H^[+]` | metal_68 | 2,5,8,11,14,17,20,23-Octaazatetracosane… | ligand_7251 | L | 20~30 | -0.05~0.25 | 1 | 8 | ref_eq_net_10787 | CNCCNCCNCCNCCNCCNCCNCCNC |
| `H^[+]` | metal_68 | 1,3-Bis(2,5,8,11-tetraazaundecyl)benzen… | ligand_7254 | L | 20~30 | -0.05~0.25 | 1 | 8 | ref_eq_net_10801 | NCCNCCNCCNCc1cccc(CNCCNCCNCCN)c1 |
| `H^[+]` | metal_68 | 1,4,7,10,13,16,19,22-Octaazacyclotetrac… | ligand_7534 | L | 19~30 | -0.05~0.65 | 2 | 8 | ref_eq_net_11977 | C1CNCCNCCNCCNCCNCCNCCNCCN1 |
| `H^[+]` | metal_68 | 1,5,9,13,17,21,25,32-Octaazacyclodotria… | ligand_7535 | L | 20~30 | -0.05~0.25 | 1 | 8 | ref_eq_net_11987 | C1CNCCCNCCCNCCCNCCCNCCCNCCCNCCCNC1 |
| `H^[+]` | metal_68 | 1,5,9,13,17,21,28,32-Octaazabicyclo[11.… | ligand_7543 | L | 20~30 | -0.05~0.25 | 1 | 8 | ref_eq_net_12024 | C1CNCCCN2CCCNCCCNCCCN(CCCNC1)CCCNCCCNCCC2 |
| `H^[+]` | metal_68 | Oxybis[ethylenenitrilobis(methylenephos… | ligand_8431 | H4L | 20~30 | -0.05~0.25 | 1 | 8 | ref_eq_net_16804 | O=P(O)(O)CN(CCOCCN(CP(=O)(O)O)CP(=O)(O)O)CP(=O)(O)O |
| `H^[+]` | metal_68 | Diethylenetrinitrilopentakis(methylenep… | ligand_8433 | H10L | 20~30 | -0.05~0.25 | 1 | 8 | ref_eq_net_16814 | O=P(O)(O)CN(CCN(CP(=O)(O)O)CP(=O)(O)O)CCN(CP(=O)(O)O)CP(=O)(O)O |
| `H^[+]` | metal_68 | myo-Inositol-hexa(dihydrogenphosphate) … | ligand_9171 | H12L | 19~30 | -0.05~3.15 | 3 | 8 | ref_eq_net_22907 | O=P(O)(O)O[C@H]1[C@H](OP(=O)(O)O)[C@@H](OP(=O)(O)O)[C@H](OP(=O)(O)O)[C@@H](OP(=O)(O)O)[C@H]1OP(=O)(O)O |

### Global max-node network: `H^[+]` + Hydrogen vanadate (Vanadic acid)
network_id: ref_eq_net_27594 | metal_id: metal_68 | ligand_id: ligand_10077 | ligand_def_HxL: H3L | nodes: 12

| beta_def | equation | type | value |
|----------|----------|------|-------|
| beta_def_79 | ``[L] + [H] <=> [HL]`` | logK | -13.3 |
| beta_def_1013 | ``[HL]^2 <=> [V2O7] + [H2O]`` | logK | 0.67 |
| beta_def_61 | ``[H2V10O28] + [H] <=> [H3V10O28]`` | logK | 1.6 |
| beta_def_51 | ``[HV10O28] + [H] <=> [H2V10O28]`` | logK | 3.74 |
| beta_def_95 | ``[V10O28] + [H] <=> [HV10O28]`` | logK | 6 |
| beta_def_1018 | ``[H2L] + [H]^2 <=> [VO2] + [H2O]^2`` | logK | 6.97 |
| beta_def_32 | ``[HL] + [H] <=> [H2L]`` | logK | 7.89 |
| beta_def_97 | ``[V4O13] + [H] <=> [HV4O13]`` | logK | 9 |
| beta_def_1015 | ``[HV4O13] + [H] <=> [V4O12] + [H2O]`` | logK | 9.8 |
| beta_def_96 | ``[V2O7] + [H] <=> [HV2O7]`` | logK | 9.96 |
| beta_def_1014 | ``[H2L]^4 <=> [V4O12] + [H2O]^4`` | logK | 10 |
| beta_def_1016 | ``[H2L]^5 <=> [V5O15] + [H2O]^5`` | logK | 12.53 |

---
