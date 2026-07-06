# Q2.2.3 — Tool Results (batch 4)

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
  "name": "DTPA, TTHA, DOTA, EDTMP, DTPMP, phytic acid, EDTA",
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

### Step 6: `search_pka_ligands`
**Args:**
```json
{
  "where": "(1=1)",
  "order_by": "lc.ligand_id ASC",
  "limit": 5000
}
```

[summary]
## search_pka_ligands — 200 row(s)

| ligand_id | ligand_name | HxL_def | formula | smiles | pH_ladder | T°C_range | I(M)_range | similarity_score |
|-----------|-------------|---------|---------|--------|-----------|-----------|------------|------------------|
| ligand_5760 | Aminoacetic acid (Glycine) | HL | C2H5N1O2 | NCC(=O)O | −∞; H2L (M_tot_1); (2.33, vlm_93627); HL (M_tot_20); (9.57, vlm_93606); L (M_tot_43); +∞ | 25 | 0.1 | *** |
| ligand_5761 | L-2-Aminopropanoic acid (Alanine) | HL | C3H7N1O2 | C[C@H](N)C(=O)O | −∞; H2L (M_tot_1); (2.33, vlm_94078); HL (M_tot_6); (9.71, vlm_94058); L (M_tot_19); +∞ | 25 | 0.1 | *** |
| ligand_5762 | DL-2-Aminobutanoic acid | HL | C4H9N1O2 | CCC(N)C(=O)O | −∞; H2L (M_tot_1); (2.3, vlm_94386); HL (M_tot_3); (9.63, vlm_94377); L (M_tot_8); +∞ | 25 | 0.1 | *** |
| ligand_5763 | DL-2-Aminopentanoic acid (Norvaline) | HL | C5H11N1O2 | CCC[C@H](N)C(=O)O | −∞; H2L (M_tot_1); (2.31, vlm_94456); HL (M_tot_1); (9.65, vlm_94449); L (M_tot_7); +∞ | 25 | 0.1 | *** |
| ligand_5764 | DL-2-Aminohexanoic acid (Norleucine) | HL | C6H13N1O2 | CCCC[C@H](N)C(=O)O | −∞; H2L (M_tot_1); (2.31, vlm_94501); HL (M_tot_1); (9.68, vlm_94495); L (M_tot_7); +∞ | 25 | 0.1 | *** |
| ligand_5765 | L-2-Amino-3-methylbutanoic acid (Valine) | HL | C5H11N1O2 | CC(C)[C@H](N)C(=O)O | −∞; H2L (M_tot_1); (2.27, vlm_94563); HL (M_tot_3); (9.52, vlm_94551); L (M_tot_11); +∞ | 25 | 0.1 | *** |
| ligand_5766 | L-2-Amino-4-methylpentanoic acid (Leucine) | HL | C6H13N1O2 | CC(C)C[C@H](N)C(=O)O | −∞; H2L (M_tot_1); (2.32, vlm_94676); HL (M_tot_3); (9.58, vlm_94665); L (M_tot_7); +∞ | 25 | 0.1 | *** |
| ligand_5767 | L-2-Amino-3-methylpentanoic acid (Isoleucine) | HL | C6H13N1O2 | CC[C@H](C)[C@H](N)C(=O)O | −∞; H2L (M_tot_1); (2.26, vlm_94759); HL (M_tot_2); (9.6, vlm_94748); L (M_tot_7); +∞ | 25 | 0.1 | *** |
| ligand_5768 | D-allo-2-Amino-3-methylpentanoic acid (D-allo-Isoleucine) | HL | C6H13N1O2 | CC[C@H](C)[C@@H](N)C(=O)O | −∞; H2L (M_tot_1); (2.2, vlm_94822); HL (M_tot_1); (9.62, vlm_94819); L (M_tot_3); +∞ | 25 | 0.1 | *** |
| ligand_5769 | 2-Amino-2-methylpropanoic acid (2-Aminoisobutyric acid) | HL | C4H9N1O2 | CC(C)(N)C(=O)O | −∞; H2L (M_tot_1); (2.34, vlm_94845); HL (M_tot_2); (10.1, vlm_94835); L (M_tot_7); +∞ | 25 | 0.1 | *** |
| ligand_5770 | DL-2-Amino-4-pentenoic acid | HL | C5H9N1O2 | C=CCC(N)C(=O)O | −∞; H2L (M_tot_1); (2.13, vlm_94882); HL (M_tot_2); (9.28, vlm_94881); L (M_tot_9); +∞ | 25 | 0.1 | *** |
| ligand_5771 | DL-2-Amino-5-hexenoic acid | HL | C6H11N1O2 | C=CCCC(N)C(=O)O | −∞; H2L (M_tot_1); (2.25, vlm_94900); HL (M_tot_2); (9.43, vlm_94899); L (M_tot_7); +∞ | 25 | 0.1 | *** |
| ligand_5772 | DL-2-Amino-6-heptenoic acid | HL | C7H13N1O2 | C=CCCCC(N)C(=O)O | −∞; H2L (M_tot_1); (2.34, vlm_94915); HL (M_tot_2); (9.52, vlm_94914); L (M_tot_7); +∞ | 25 | 0.1 | *** |
| ligand_5773 | 1-Aminocyclopentanecarboxylic acid (Cycloleucine) | HL | C6H11N1O2 | NC1(C(=O)O)CCCC1 | −∞; H2L (M_tot_1); (2.4, vlm_94930); HL (M_tot_2); (10.31, vlm_94929); L (M_tot_5); +∞ | 20 | 0.1 | *** |
| ligand_5774 | 1-Aminocyclohexanecarboxylic acid | HL | C7H13N1O2 | NC1(C(=O)O)CCCCC1 | −∞; H2L (M_tot_1); (2.41, vlm_94941); HL (M_tot_1); (10.13, vlm_94940); L (M_tot_6); +∞ | 20 | 0.1 | *** |
| ligand_5775 | 1-Aminocycloheptanecarboxylic acid | HL | C8H15N1O2 | NC1(C(=O)O)CCCCCC1 | −∞; H2L (M_tot_1); (2.59, vlm_94952); HL (M_tot_2); (10.46, vlm_94951); L (M_tot_5); +∞ | 20 | 0.1 | *** |
| ligand_5776 | DL-Aminophenylacetic acid (Phenylglycine) | HL | C8H9N1O2 | NC(C(=O)O)c1ccccc1 | −∞; H2L (M_tot_1); (-1.9, vlm_94963); HL (M_tot_1); (8.92, vlm_94962); L (M_tot_6); +∞ | 25 | 0.1 | *** |
| ligand_5777 | L-2-Amino-3-phenylpropanoic acid (Phenylalanine) | HL | C9H11N1O2 | N[C@@H](Cc1ccccc1)C(=O)O | −∞; H2L (M_tot_1); (2.18, vlm_94993); HL (M_tot_1); (9.09, vlm_94975); L (M_tot_11); +∞ | 25 | 0.1 | *** |
| ligand_5778 | DL-2-Amino-3-chloropropanoic acid (3-Chloroalanine) | HL | C3H6Cl1N1O2 | N[C@@H](CCl)C(=O)O | −∞; H2L (M_tot_1); (2, vlm_95146); HL (M_tot_1); (8.18, vlm_95145); L (M_tot_4); +∞ | 25 | 0.1 | *** |
| ligand_5779 | DL-2-Amino-3-chlorobutanoic acid | HL | C4H8Cl1N1O2 | CC(Cl)C(N)C(=O)O | −∞; H2L (M_tot_1); (-1.5, vlm_95156); HL (M_tot_1); (8.07, vlm_95155); L (M_tot_4); +∞ | 25 | 0.1 | *** |
| ligand_5780 | DL-2-Amino-3-(2-fluorophenyl)propanoic acid (DL-3-(2-Fluoro… | HL | C9H10F1N1O2 | N[C@@H](Cc1ccccc1F)C(=O)O | −∞; H2L (M_tot_1); (2.12, vlm_95166); HL (M_tot_1); (9.01, vlm_95163); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5781 | DL-2-Amino-3-(3-fluorophenyl)propanoic acid (DL-3-(3-Fluoro… | HL | C9H10F1N1O2 | N[C@@H](Cc1cccc(F)c1)C(=O)O | −∞; H2L (M_tot_1); (2.1, vlm_95172); HL (M_tot_1); (8.98, vlm_95169); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5782 | DL-2-Amino-3-(4-fluorophenyl)propanoic acid (DL-3-(4-Fluoro… | HL | C9H10F1N1O2 | N[C@@H](Cc1ccc(F)cc1)C(=O)O | −∞; H2L (M_tot_1); (2.13, vlm_95178); HL (M_tot_1); (9.05, vlm_95175); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5783 | DL-2-Amino-3-(2-chlorophenyl)propanoic acid (DL-3-(2-Chloro… | HL | C9H10Cl1N1O2 | N[C@@H](Cc1ccccc1Cl)C(=O)O | −∞; H2L (M_tot_1); (2.23, vlm_95183); HL (M_tot_1); (8.94, vlm_95182); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5784 | DL-2-Amino-3-(3-chlorophenyl)propanoic acid (DL-3-(3-Chloro… | HL | C9H10Cl1N1O2 | N[C@@H](Cc1cccc(Cl)c1)C(=O)O | −∞; H2L (M_tot_1); (2.17, vlm_95185); HL (M_tot_1); (8.91, vlm_95184); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5785 | DL-2-Amino-3-(4-chlorophenyl)propanoic acid (DL-3-(4-Chloro… | HL | C9H10Cl1N1O2 | N[C@@H](Cc1ccc(Cl)cc1)C(=O)O | −∞; H2L (M_tot_1); (2.08, vlm_95187); HL (M_tot_1); (8.96, vlm_95186); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5786 | DL-Amino-4-sulfophenylacetic acid (4-Sulfophenylglycine) | H2L | C8H9N1O5S1 | NC(C(=O)O)c1ccc(S(=O)(=O)O)cc1 | −∞; H2L (M_tot_1); (-1.8, vlm_95189); HL (M_tot_1); (8.66, vlm_95188); L (M_tot_6); +∞ | 25 | 0.1 | *** |
| ligand_5787 | DL-2-Amino-4-sulfobutanoic acid (Homocysteic acid) | H2L | C4H9N1O5S1 | N[C@@H](CCS(=O)(=O)O)C(=O)O | −∞; H2L (M_tot_1); (2.11, vlm_95201); HL (M_tot_1); (8.93, vlm_95200); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_5788 | 3-Aminopropanoic acid (beta-Alanine) | HL | C3H7N1O2 | NCCC(=O)O | −∞; H2L (M_tot_1); (3.51, vlm_95222); HL (M_tot_3); (10.08, vlm_95204); L (M_tot_11); +∞ | 25 | 0.1 | *** |
| ligand_5789 | DL-3-Aminobutanoic acid | HL | C4H9N1O2 | CC(N)CC(=O)O | −∞; H2L (M_tot_1); (3.43, vlm_95342); HL (M_tot_1); (10.05, vlm_95337); L (M_tot_4); +∞ | 25 | 0.1 | *** |
| ligand_5790 | cis-2-Aminocyclopentane-1-carboxylic acid | HL | C6H11N1O2 | N[C@H]1CCC[C@H]1C(=O)O | −∞; H2L (M_tot_1); (3.54, vlm_95371); HL (M_tot_1); (10.1, vlm_95370); L (M_tot_5); +∞ | 25 | 0.5 | *** |
| ligand_5791 | trans-2-Aminocyclopentane-1-carboxylic acid | HL | C6H11N1O2 | N[C@@H]1CCC[C@H]1C(=O)O | −∞; H2L (M_tot_1); (3.75, vlm_95377); HL (M_tot_1); (9.91, vlm_95376); L (M_tot_2); +∞ | 25 | 0.5 | *** |
| ligand_5792 | cis-2-Aminocyclohexane-1-carboxylic acid | HL | C7H13N1O2 | N[C@H]1CCCC[C@H]1C(=O)O | −∞; H2L (M_tot_1); (3.49, vlm_95380); HL (M_tot_1); (10.54, vlm_95379); L (M_tot_5); +∞ | 25 | 0.5 | *** |
| ligand_5793 | trans-2-Aminocyclohexane-1-carboxylic acid | HL | C7H13N1O2 | N[C@@H]1CCCC[C@H]1C(=O)O | −∞; H2L (M_tot_1); (3.47, vlm_95386); HL (M_tot_1); (10.01, vlm_95385); L (M_tot_5); +∞ | 25 | 0.5 | *** |
| ligand_5794 | cis-2-Amino-4-cyclohexene-1-carboxylic acid | HL | C7H11N1O2 | N[C@H]1CC=CC[C@H]1C(=O)O | −∞; H2L (M_tot_1); (3.29, vlm_95392); HL (M_tot_1); (10.2, vlm_95391); L (M_tot_5); +∞ | 25 | 0.5 | *** |
| ligand_5795 | trans-2-Amino-4-cyclohexene-1-carboxylic acid | HL | C7H11N1O2 | N[C@@H]1CC=CC[C@H]1C(=O)O | −∞; H2L (M_tot_1); (3.33, vlm_95398); HL (M_tot_1); (10.29, vlm_95397); L (M_tot_4); +∞ | 25 | 0.5 | *** |
| ligand_5796 | DL-3-Amino-3-phenylpropanoic acid (Phenyl-beta-Alanine) | HL | C9H11N1O2 | NC(CC(=O)O)c1ccccc1 | −∞; H2L (M_tot_1); (3.4, vlm_95403); HL (M_tot_1); (9, vlm_95402); L (M_tot_1); +∞ | 25 | 0.5 | *** |
| ligand_5797 | 4-Aminobutanoic acid | HL | C4H9N1O2 | NCCCC(=O)O | −∞; H2L (M_tot_1); (4.02, vlm_95418); HL (M_tot_5); (10.35, vlm_95408); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_5798 | 5-Aminopentanoic acid | HL | C5H11N1O2 | NCCCCC(=O)O | −∞; H2L (M_tot_1); (4.27, vlm_95469); HL (M_tot_1); (10.766, vlm_95464); L (M_tot_3); +∞ | 25 | 0 | *** |
| ligand_5799 | 6-Aminohexanoic acid | HL | C6H13N1O2 | NCCCCCC(=O)O | −∞; H2L (M_tot_1); (4.373, vlm_95495); HL (M_tot_2); (10.804, vlm_95486); L (M_tot_4); +∞ | 25 | 0 | *** |
| ligand_5800 | 7-Aminoheptanoic acid | HL | C7H15N1O2 | NCCCCCCC(=O)O | −∞; H2L (M_tot_1); (4.502, vlm_95520); HL (M_tot_1); +∞ | 25 | 0 | *** |
| ligand_5801 | Aminopropanedioic acid (Aminomalonic acid) | H2L | C3H5N1O4 | NC(C(=O)O)C(=O)O | −∞; H3L (M_tot_1); (-1.8, vlm_95531); H2L (M_tot_1); (2.94, vlm_95527); HL (M_tot_1); (9.22, vlm_95523); L (M_tot_4); +∞ | 25 | 0.1 | *** |
| ligand_5802 | L-Aminobutanedioic acid (Aspartic acid) | H2L | C4H7N1O4 | N[C@@H](CC(=O)O)C(=O)O | −∞; H3L (M_tot_1); (1.95, vlm_95563); H2L (M_tot_1); (3.71, vlm_95550); HL (M_tot_9); (9.66, vlm_95537); L (M_tot_36); +∞ | 25 | 0.1 | *** |
| ligand_5803 | DL-2-Amino-3-methylbutanedioic acid (3-Methylaspartic acid) | H2L | C5H9N1O4 | CC(C(=O)O)[C@H](N)C(=O)O | −∞; H3L (M_tot_1); (1.99, vlm_95735); H2L (M_tot_1); (3.59, vlm_95734); HL (M_tot_2); (9.48, vlm_95733); L (M_tot_2); +∞ | 25 | 0.5 | *** |
| ligand_5804 | L-2-Aminopentanedioic acid (Glutamic acid) | H2L | C5H9N1O4 | N[C@@H](CCC(=O)O)C(=O)O | −∞; H3L (M_tot_1); (2.16, vlm_95761); H2L (M_tot_2); (4.15, vlm_95750); HL (M_tot_8); (9.58, vlm_95739); L (M_tot_17); +∞ | 25 | 0.1 | *** |
| ligand_5805 | DL-2-Amino-2-methylpentanedioic acid (2-Methylglutamic acid) | H2L | C6H11N1O4 | C[C@](N)(CCC(=O)O)C(=O)O | −∞; H2L (M_tot_1); (4.05, vlm_95867); HL (M_tot_1); (9.72, vlm_95866); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_5806 | DL-2-Aminohexanedioic acid | H2L | C6H11N1O4 | NC(CCCC(=O)O)C(=O)O | −∞; HL (M_tot_1); (9.73, vlm_95870); L (M_tot_1); +∞ | 20 | 0.1 | *** |
| ligand_5807 | DL-2-Amino-3-hydroxypentanedioic acid (3-Hydroxyglutamic ac… | H2L | C5H9N1O5 | N[C@H](C(=O)O)C(O)CC(=O)O | −∞; H3L (M_tot_1); (2.09, vlm_95876); H2L (M_tot_1); (4.08, vlm_95875); HL (M_tot_1); (9.06, vlm_95874); L (M_tot_4); +∞ | 25 | 0.1 | *** |
| ligand_5808 | (3-Aminopropyl)malonic acid | H2L | C6H11N1O4 | NCCCC(C(=O)O)C(=O)O | −∞; H3L (M_tot_1); (2.52, vlm_95888); H2L (M_tot_1); (4.86, vlm_95885); HL (M_tot_2); (10.45, vlm_95882); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_5809 | L-2-Amino-3-phosphopropanoic acid (Phosphoserine) | H3L | C3H8N1O6P1 | N[C@@H](COP(=O)(O)O)C(=O)O | −∞; H4L (M_tot_1); (-0.7, vlm_95914); H3L (M_tot_1); (2.14, vlm_95911); H2L (M_tot_1); (5.7, vlm_95904); HL (M_tot_1); (9.8, vlm_95900); L (M_tot_11); +∞ | 25 | 0.1 | *** |
| ligand_5810 | L-2-Amino-2-methyl-3-phosphopropanoic acid | H4L | C4H10N1O6P1 | CC(N)(COP(=O)(O)O)C(=O)O | −∞; H3L (M_tot_1); (2.07, vlm_95954); H2L (M_tot_1); (5.68, vlm_95953); HL (M_tot_1); (10.07, vlm_95952); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5811 | L-2-Amino-3-phosphobutanoic acid (Phosphothreonine) | H4L | C4H10N1O6P1 | C[C@@H](OP(=O)(O)O)[C@H](N)C(=O)O | −∞; H3L (M_tot_1); (2.25, vlm_95964); H2L (M_tot_1); (5.83, vlm_95963); HL (M_tot_1); (9.67, vlm_95962); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5812 | DL-2-Amino-3-(phenylphospho)propanoic acid | H3L | C9H12N1O6P1 | NC(COP(=O)(O)Oc1ccccc1)C(=O)O | −∞; H2L (M_tot_1); (2.13, vlm_95973); HL (M_tot_1); (8.79, vlm_95972); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5813 | DL-2-Amino-3-phosphonopropanoic acid | H4L | C3H8N1O5P1 | NC(CP(=O)(O)O)C(=O)O | −∞; H3L (M_tot_1); (2.37, vlm_95978); H2L (M_tot_1); (6.06, vlm_95976); HL (M_tot_4); (10.74, vlm_95974); L (M_tot_7); +∞ | 25 | 0.1 | *** |
| ligand_5814 | DL-2-Amino-4-phosphonobutanoic acid | H4L | C4H10N1O5P1 | NC(CCP(=O)(O)O)C(=O)O | −∞; H3L (M_tot_1); (2.51, vlm_96010); H2L (M_tot_1); (6.9, vlm_96009); HL (M_tot_3); (10.21, vlm_96008); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_5815 | DL-3-Amino-2-phosphonopropanoic acid | H4L | C3H8N1O5P1 | NCC(C(=O)O)P(=O)(O)O | −∞; H3L (M_tot_1); (3.44, vlm_96026); H2L (M_tot_5); (5.52, vlm_96025); HL (M_tot_5); (10.07, vlm_96024); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_5816 | D-3-Amino-3-carboxypropanohydroxamic acid (Asparagine hydro… | H2L | C4H8N2O4 | NC(CC(=O)NO)C(=O)O | −∞; H3L (M_tot_1); (2.18, vlm_96046); H2L (M_tot_1); (8.15, vlm_96045); HL (M_tot_1); (9.37, vlm_96044); L (M_tot_4); +∞ | 25 | 0.5 | *** |
| ligand_5817 | DL-2-Amino-3-(2-hydroxyphenyl)propanoic acid (o-Tyrosine) | H2L | C9H11N1O3 | NC(Cc1ccccc1O)C(=O)O | −∞; H3L (M_tot_1); (2.41, vlm_96078); H2L (M_tot_1); (8.67, vlm_96074); HL (M_tot_6); (11.01, vlm_96070); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_5818 | DL-2-Amino-3-(3-hydroxyphenyl)propanoic acid (m-Tyrosine) | H2L | C9H11N1O3 | N[C@@H](Cc1cccc(O)c1)C(=O)O | −∞; H3L (M_tot_1); (2.22, vlm_96149); H2L (M_tot_1); (8.95, vlm_96145); HL (M_tot_6); (10.04, vlm_96141); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5819 | L-2-Amino-3-(4-hydroxyphenyl)propanoic acid (Tyrosine) | H2L | C9H11N1O3 | N[C@@H](Cc1ccc(O)cc1)C(=O)O | −∞; H3L (M_tot_1); (2.24, vlm_96241); H2L (M_tot_1); (9.04, vlm_96234); HL (M_tot_10); (10.1, vlm_96227); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5820 | L-2-Amino-2-methyl-3-(4-hydroxyphenyl)propanoic acid (L-Met… | H2L | C10H13N1O3 | CC(N)(Cc1ccc(O)cc1)C(=O)O | −∞; H3L (M_tot_1); (2.16, vlm_96354); H2L (M_tot_1); (9.14, vlm_96353); HL (M_tot_2); (10.24, vlm_96352); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5821 | L-2-Amino-3-(4-hydroxy-3,5-diiodophenyl)propanoic acid (L-3… | H2L | C9H9I2N1O3 | N[C@@H](Cc1cc(I)c(O)c(I)c1)C(=O)O | −∞; H2L (M_tot_1); (6.16, vlm_96360); HL (M_tot_2); (9.1, vlm_96359); L (M_tot_1); +∞ | 25 | 0.5 | *** |
| ligand_5822 | DL-2-Amino-3-(3-hydroxy-4-methoxyphenyl)propanoic acid | H2L | C10H13N1O4 | COc1ccc(CC(N)C(=O)O)cc1O | −∞; H3L (M_tot_1); (2.23, vlm_96366); H2L (M_tot_1); (8.84, vlm_96365); HL (M_tot_1); (10.12, vlm_96364); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5823 | DL-2-Amino-3-(4-hydroxy-3-methoxyphenyl)propanoic acid | H2L | C10H13N1O4 | COc1cc(CC(N)C(=O)O)ccc1O | −∞; H3L (M_tot_1); (2.13, vlm_96369); H2L (M_tot_1); (8.78, vlm_96368); HL (M_tot_1); (10.14, vlm_96367); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5824 | L-2-Amino-3-(3-amino-4-hydroxyphenyl)propanoic acid (m-Amin… | H2L | C9H12N2O3 | Nc1cc(C[C@H](N)C(=O)O)ccc1O | −∞; H4L (M_tot_1); (2, vlm_96373); H3L (M_tot_1); (4.48, vlm_96372); H2L (M_tot_2); (9.09, vlm_96371); HL (M_tot_2); (10.19, vlm_96370); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_5825 | DL-2-Amino-2-(3,4-dihydroxyphenyl)acetic acid (DOPG) | H3L | C8H9N1O4 | NC(C(=O)O)c1ccc(O)c(O)c1 | −∞; HL (M_tot_1); (-13.6, vlm_96379); L (M_tot_1); (2, vlm_96382); H3L (M_tot_1); (8.56, vlm_96381); H2L (M_tot_2); (9.75, vlm_96380); HL (M_tot_1); +∞ | 25 | 1 | *** |
| ligand_5826 | L-2-Amino-3-(3,4-dihydroxyphenyl)propanoic acid (DOPA) | H3L | C9H11N1O4 | NC(Cc1ccc(O)c(O)c1)C(=O)O | −∞; HL (M_tot_6); (-13.4, vlm_96385); L (M_tot_1); (2.2, vlm_96401); H3L (M_tot_1); (8.75, vlm_96395); H2L (M_tot_9); (9.81, vlm_96389); HL (M_tot_6); +∞ | 25 | 0.1 | *** |
| ligand_5827 | L-2-Amino-2-methyl-3-(3,4-dihydroxyphenyl)propanoic acid (L… | H3L | C10H13N1O4 | CC(N)(Cc1ccc(O)c(O)c1)C(=O)O | −∞; H4L (M_tot_1); (2.24, vlm_96485); H3L (M_tot_1); (8.88, vlm_96484); H2L (M_tot_2); (9.99, vlm_96483); HL (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5828 | L-2-Amino-3-hydroxypropanoic acid (Serine) | HL | C3H7N1O3 | N[C@@H](CO)C(=O)O | −∞; H2L (M_tot_1); (2.16, vlm_96511); HL (M_tot_3); (9.05, vlm_96498); L (M_tot_16); +∞ | 25 | 0.1 | *** |
| ligand_5829 | L-2-Amino-3-hydroxybutanoic acid (Threonine) | HL | C4H9N1O3 | C[C@@H](O)[C@H](N)C(=O)O | −∞; H2L (M_tot_1); (2.2, vlm_96687); HL (M_tot_2); (8.94, vlm_96674); L (M_tot_11); +∞ | 25 | 0.1 | *** |
| ligand_5830 | allo-L-2-Amino-3-hydroxybutanoic acid (L-allo-Threonine) | HL | C4H9N1O3 | C[C@H](O)[C@H](N)C(=O)O | −∞; H2L (M_tot_1); (2.11, vlm_96824); HL (M_tot_1); (8.92, vlm_96819); L (M_tot_4); +∞ | 25 | 0.1 | *** |
| ligand_5831 | erythro-2-Amino-3-hydroxy-3-phenylpropanoic acid (erythro-P… | HL | C9H11N1O3 | NC(C(=O)O)C(O)c1ccccc1 | −∞; H2L (M_tot_1); (-1.9, vlm_96854); HL (M_tot_1); (8.7, vlm_96851); L (M_tot_7); +∞ | 25 | 0.1 | *** |
| ligand_5832 | threo-2-Amino-3-hydroxy-3-phenylpropanoic acid (threo-Pheny… | HL | C9H11N1O3 | NC(C(=O)O)C(O)c1ccccc1 | −∞; H2L (M_tot_1); (-1.9, vlm_96877); HL (M_tot_1); (8.87, vlm_96876); L (M_tot_4); +∞ | 25 | 0.1 | *** |
| ligand_5833 | L-2-Amino-4-hydroxybutanoic acid (Homoserine) | HL | C4H9N1O3 | N[C@@H](CCO)C(=O)O | −∞; H2L (M_tot_1); (2.24, vlm_96895); HL (M_tot_1); (9.28, vlm_96890); L (M_tot_7); +∞ | 25 | 0.1 | *** |
| ligand_5834 | DL-3-Amino-2-hydroxypropanoic acid (Isoserine) | HL | C3H7N1O3 | NCC(O)C(=O)O | −∞; H2L (M_tot_1); (2.66, vlm_96924); HL (M_tot_5); (9.13, vlm_96921); L (M_tot_6); +∞ | 25 | 0.1 | *** |
| ligand_5835 | DL-4-Amino-3-hydroxybutanoic acid | HL | C4H9N1O3 | NCC(O)CC(=O)O | −∞; H2L (M_tot_1); (3.9, vlm_96961); HL (M_tot_1); (9.46, vlm_96957); L (M_tot_3); +∞ | 25 | 0.1 | *** |
| ligand_5836 | L-trans-2-Amino-3-hydroxy-2,3-dihydrobenzoic acid | HL | C7H9N1O3 | N[C@H]1C(C(=O)O)=CC=C[C@@H]1O | −∞; H2L (M_tot_1); (3.36, vlm_96980); HL (M_tot_1); (8.56, vlm_96979); L (M_tot_2); +∞ | 25 | 0.1 | *** |
| ligand_5837 | D-gluco-2-Amino-3,4,5,6-tetrahydroxyhexanoic acid (D-Glucos… | HL | C6H13N1O6 | N[C@@H](C(=O)O)[C@@H](O)[C@H](O)[C@H](O)CO | −∞; H2L (M_tot_1); (2.2, vlm_96988); HL (M_tot_1); (9.08, vlm_96985); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_5838 | DL-Amino-4-Methoxyphenylacetic acid (4-Methoxyphenylglycine) | HL | C9H11N1O3 | COc1ccc(C(N)C(=O)O)cc1 | −∞; H2L (M_tot_1); (2, vlm_97021); HL (M_tot_1); (9.07, vlm_97020); L (M_tot_6); +∞ | 25 | 0.1 | *** |
| ligand_5839 | L-2-Aminobutanedioic acid 4-methyl ester (4-Methyl aspartat… | HL | C5H9N1O4 | COC(=O)CC(N)C(=O)O | −∞; HL (M_tot_1); (8.5, vlm_97032); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5840 | DL-2-Aminopentanedioic acid 5-ethyl ester (5-Ethyl glutamat… | HL | C7H13N1O4 | CCOC(=O)CC[C@H](N)C(=O)O | −∞; H2L (M_tot_1); (2.15, vlm_97034); HL (M_tot_1); (9.19, vlm_97033); L (M_tot_1); +∞ | 25 | 0 | *** |
| ligand_5841 | L-2-Aminopentanedioic acid 5-benzyl ester (5-Benzyl glutama… | HL | C12H15N1O4 | N[C@@H](CCC(=O)OCc1ccccc1)C(=O)O | −∞; H2L (M_tot_1); (2.06, vlm_97036); HL (M_tot_1); (8.89, vlm_97035); L (M_tot_1); +∞ | 25 | 0.1 | *** |
| ligand_5842 | DL-2-Aminopentanedioic acid 1-ethyl ester (1-Ethyl glutamat… | HL | C7H13N1O4 | CCOC(=O)[C@@H](N)CCC(=O)O | −∞; H2L (M_tot_1); (3.85, vlm_97038); HL (M_tot_1); (7.84, vlm_97037); L (M_tot_1); +∞ | 25 | 0 | *** |
| ligand_5843 | L-2-Aminobutanedioic acid 4-amide (Asparagine) | HL | C4H8N2O3 | NC(=O)C[C@H](N)C(=O)O | −∞; H2L (M_tot_1); (2.16, vlm_97048); HL (M_tot_2); (8.73, vlm_97039); L (M_tot_14); +∞ | 25 | 0.1 | *** |
| ligand_5844 | L-2-Aminopentanedioic acid 5-amide (Glutamine) | HL | C5H10N2O3 | NC(=O)CC[C@H](N)C(=O)O | −∞; H2L (M_tot_1); (2.19, vlm_97179); HL (M_tot_1); (9, vlm_97170); L (M_tot_10); +∞ | 25 | 0.1 | *** |
| ligand_5845 | L-2-Amino-6-(2-methylpropamido)hexanoic acid (N(6)-Isobutyr… | HL | C10H20N2O3 | CC(C)C(=O)NCCCCC(N)C(=O)O | −∞; H2L (M_tot_1); (2.4, vlm_97270); HL (M_tot_1); (9.42, vlm_97267); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_5847 | L-2-Amino-6-acetamidohexanoic acid (N(6)-Acetyl-L-lysine) | HL | C8H16N2O3 | CC(=O)NCCCCC(N)C(=O)O | −∞; H2L (M_tot_1); (2.13, vlm_97299); HL (M_tot_1); (9.52, vlm_97298); L (M_tot_5); +∞ | 25 | 0.1 | *** |
| ligand_5848 | L-2-Amino-3-(oxalylamido)propanoic acid | HL | C5H8N2O5 | NC(CNC(=O)C(=O)O)C(=O)O | −∞; H2L (M_tot_1); (2.44, vlm_97306); HL (M_tot_1); (8.95, vlm_97305); L (M_tot_3); +∞ | 25 | 0.1 | *** |

---

### Step 7: `get_table_schema`
**Args:**
```json
{
  "table_name": "ligand_pka_measured",
  "database": "equilibrium"
}
```

[summary]
**get_table_schema:** Error - Table 'ligand_pka_measured' not found.
Available tables: eq_collection_unassigned, eq_edge, eq_edge_species, eq_export_metadata, eq_map, eq_map_collection, eq_map_stray, eq_network, eq_network_species, eq_node, eq_node_species, sqlite_sequence

---
