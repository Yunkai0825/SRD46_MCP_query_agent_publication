# Q3.1.2 - Validation (batch 2)

**26 of 78 claims unsupported**

| # | Para | Type | Unsupported Claim | Context |
|---|------|------|-------------------|---------|
| 1 | 1 | exact_value | 25 °C | ... NIST SRD-46  Under matched conditions (25 °C, I = 0.1 M KNO₃, aqueous, 1:1 ML specie... |
| 2 | 1 | exact_value | I = 0.1 M KNO₃ | ...RD-46  Under matched conditions (25 °C, I = 0.1 M KNO₃, aqueous, 1:1 ML species), the database... |
| 3 | 1 | exact_value | \| **L-Histidine** \| **10.19** \| **8.70** \| **+1.49** \| **~31×** \| | ...lectivity ratio \| \|---\|---\|---\|---\|---\| \| **L-Histidine** \| **10.19** \| **8.70** \| **+1.49** \| **~31×** \| \| Glycine \| 8.22 \| 5.77 \| +2.45 \| ~280×... |
| 4 | 1 | exact_value | \| Glycine \| 8.22 \| 5.77 \| +2.45 \| ~280× \| | ...9** \| **8.70** \| **+1.49** \| **~31×** \| \| Glycine \| 8.22 \| 5.77 \| +2.45 \| ~280× \|  > *Species: [ML]/[M][L]. Source: NIST ... |
| 5 | 2 | property_attribution | However, glycine's absolute conditional constants at pH 7 become very small | ...Δlog K′(pH 7) ≈ Δlog β** in both cases. However, glycine's absolute conditional constants at pH 7 become very small (log K′Cu ≈ 5.8, log K′Ni ≈ 3.3 after c... |
| 6 | 2 | exact_value | log K′Cu ≈ 5.8 | ...al constants at pH 7 become very small (log K′Cu ≈ 5.8, log K′Ni ≈ 3.3 after correction), mean... |
| 7 | 2 | exact_value | log K′Ni ≈ 3.3 | ...pH 7 become very small (log K′Cu ≈ 5.8, log K′Ni ≈ 3.3 after correction), meaning neither meta... |
| 8 | 2 | domain_reasoning | meaning neither metal is well-complexed. | ... 5.8, log K′Ni ≈ 3.3 after correction), meaning neither metal is well-complexed. Histidine retains strong absolute bindi... |
| 9 | 2 | property_attribution | Histidine retains strong absolute binding for Cu²⁺ even after correction. | ...eaning neither metal is well-complexed. Histidine retains strong absolute binding for Cu²⁺ even after correction.... |
| 10 | 3 | comparison | is the best amino acid ligand for selective Cu²⁺ complexation in the presence of Ni²⁺ at pH 7 | ...tidine**  **L-Histidine (ligand_5898)** is the best amino acid ligand for selective Cu²⁺ complexation in the presence of Ni²⁺ at pH 7, for three converging reasons:  1. **St... |
| 11 | 3 | property_attribution | **Strong absolute Cu²⁺ binding at pH 7** | ...pH 7, for three converging reasons:  1. **Strong absolute Cu²⁺ binding at pH 7**: With log β = 10.19 and the imidazole ~... |
| 12 | 3 | exact_value | With log β = 10.19 | ...Strong absolute Cu²⁺ binding at pH 7**: With log β = 10.19 and the imidazole ~91% available, Cu²⁺ ... |
| 13 | 3 | domain_reasoning | Cu²⁺ is robustly complexed even at micromolar concentrations. | ...10.19 and the imidazole ~91% available, Cu²⁺ is robustly complexed even at micromolar concentrations. 2. **Meaningful selectivity gap**: Δlog... |
| 14 | 3 | exact_value | Δlog β = +1.49 | ...ons. 2. **Meaningful selectivity gap**: Δlog β = +1.49 corresponds to a ~31-fold thermodynamic... |
| 15 | 3 | calculation | corresponds to a ~31-fold thermodynamic preference for Cu²⁺ over Ni²⁺ under identical conditions. | ...ngful selectivity gap**: Δlog β = +1.49 corresponds to a ~31-fold thermodynamic preference for Cu²⁺ over Ni²⁺ under identical conditions. 3. **Donor atom match**: Histidine's tr... |
| 16 | 3 | comparison | Glycine's larger raw Δlog β | ...vely less from this donor arrangement.  Glycine's larger raw Δlog β (+2.45) is misleading at pH 7: its amin... |
| 17 | 3 | exact_value | (+2.45) | ...rangement.  Glycine's larger raw Δlog β (+2.45) is misleading at pH 7: its amine group ... |
| 18 | 3 | exact_value | its amine group is only ~3% deprotonated | ...w Δlog β (+2.45) is misleading at pH 7: its amine group is only ~3% deprotonated, so the effective ligand concentration ... |
| 19 | 3 | domain_reasoning | neither metal is well-complexed in practice. | ... ligand concentration is negligible and neither metal is well-complexed in practice.... |
| 20 | 4 | exact_value | log β(Cu²⁺) = 10.19 | ...se **L-histidine** at pH 7. It delivers log β(Cu²⁺) = 10.19 vs log β(Ni²⁺) = 8.70 (Δ = +1.49, ~31× ... |
| 21 | 4 | exact_value | log β(Ni²⁺) = 8.70 | ...H 7. It delivers log β(Cu²⁺) = 10.19 vs log β(Ni²⁺) = 8.70 (Δ = +1.49, ~31× selectivity) under mat... |
| 22 | 4 | calculation | Δ = +1.49 | ... β(Cu²⁺) = 10.19 vs log β(Ni²⁺) = 8.70 (Δ = +1.49, ~31× selectivity) under matched condit... |
| 23 | 4 | calculation | ~31× selectivity | ...10.19 vs log β(Ni²⁺) = 8.70 (Δ = +1.49, ~31× selectivity) under matched conditions, with the imi... |
| 24 | 4 | property_attribution | under matched conditions | ...⁺) = 8.70 (Δ = +1.49, ~31× selectivity) under matched conditions, with the imidazole group fully active ... |
| 25 | 4 | exact_value | 25 °C | ..., metal_112, ligand_5898, ligand_5760), 25 °C, I = 0.1 M KNO₃, aqueous.*... |
| 26 | 4 | exact_value | I = 0.1 M KNO₃ | ..._112, ligand_5898, ligand_5760), 25 °C, I = 0.1 M KNO₃, aqueous.*... |