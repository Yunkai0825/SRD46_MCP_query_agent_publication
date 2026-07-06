# Qfree_20260423_200125 - Validation (batch 1)

**85 of 249 claims unsupported**

| # | Para | Type | Unsupported Claim | Context |
|---|------|------|-------------------|---------|
| 1 | 0 | range | logK₁ = 11.38-11.42 (20-25°C, I=0.1M) | ...HA (L⁻ = deprotonated hydroxamate):** - logK₁ = 11.38-11.42 (20-25°C, I=0.1M) - logβ₂ = 21.1 (20°C, I=0.1M) - logβ₃ =... |
| 2 | 0 | exact_value | logβ₂ = 21.1 (20°C, I=0.1M) | ...logK₁ = 11.38-11.42 (20-25°C, I=0.1M) - logβ₂ = 21.1 (20°C, I=0.1M) - logβ₃ = 28.3 (20°C, I=0.1M)  **Fe²⁺-A... |
| 3 | 0 | exact_value | logβ₃ = 28.3 (20°C, I=0.1M) | ...I=0.1M) - logβ₂ = 21.1 (20°C, I=0.1M) - logβ₃ = 28.3 (20°C, I=0.1M)  **Fe²⁺-AHA:** - logK₁ = 4.8 (20°C, I=0... |
| 4 | 0 | exact_value | logβ₂ = 8.5 (20°C, I=0.1M) | ...⁺-AHA:** - logK₁ = 4.8 (20°C, I=0.1M) - logβ₂ = 8.5 (20°C, I=0.1M)  **ΔlogK₁ = 6.6** — excellent selectivi... |
| 5 | 0 | calculation | ΔlogK₁ = 6.6 | ...I=0.1M) - logβ₂ = 8.5 (20°C, I=0.1M)  **ΔlogK₁ = 6.6** — excellent selectivity!  But AHA pKa... |
| 6 | 0 | calculation | Fe³⁺: logK₁_cond = 11.42 - 9.29 + pH = 11.42 - 9.29 + 3 = 5.13 | ...onditional constant at pH 3 would be: - Fe³⁺: logK₁_cond = 11.42 - 9.29 + pH = 11.42 - 9.29 + 3 = 5.13 → still significant! - Fe²⁺: logK₁_cond... |
| 7 | 0 | calculation | Fe³⁺: logK₁_cond = 11.42 - 6.29 = **5.13** | ...29) = 10^(-6.29), so log(αL) ≈ -6.29  - Fe³⁺: logK₁_cond = 11.42 - 6.29 = **5.13** → K_cond = 1.3×10⁵ — significant! - Fe²... |
| 8 | 0 | calculation | K_cond = 1.3×10⁵ | ... logK₁_cond = 11.42 - 6.29 = **5.13** → K_cond = 1.3×10⁵ — significant! - Fe²⁺: logK₁_cond = 4.8... |
| 9 | 0 | calculation | Fe³⁺: logK₁_cond = 11.42 - 5.29 = **6.13** | ...gible!  At pH 4: αL = 10^(-5.29), so: - Fe³⁺: logK₁_cond = 11.42 - 5.29 = **6.13** → K_cond = 1.3×10⁶ — strong! - Fe²⁺: lo... |
| 10 | 0 | calculation | K_cond = 1.3×10⁶ | ... logK₁_cond = 11.42 - 5.29 = **6.13** → K_cond = 1.3×10⁶ — strong! - Fe²⁺: logK₁_cond = 4.8 - 5.... |
| 11 | 0 | domain_reasoning | This is **outstanding** selectivity at pH < 5! | ...** → K_cond = 0.32 — still negligible!  This is **outstanding** selectivity at pH < 5! The protonation of AHA actually HELPS t... |
| 12 | 1 | range | pH < 5 | ...electrodeposition from acidic solution (pH < 5, ~0.1 M Fe²⁺): 1. **Stabilize Fe³⁺** — ... |
| 13 | 1 | exact_value | ~0.1 M Fe²⁺ | ...eposition from acidic solution (pH < 5, ~0.1 M Fe²⁺): 1. **Stabilize Fe³⁺** — prevent Fe(OH... |
| 14 | 1 | exact_value | Ksp ≈ 10⁻³⁹ | ...Fe³⁺** — prevent Fe(OH)₃ precipitation (Ksp ≈ 10⁻³⁹; precipitates at [Fe³⁺] > 10⁻⁶ M at pH ... |
| 15 | 3 | exact_value | \| **Acetohydroxamic acid (AHA)** \| 9.29 \| 11.42 \| 4.8 \| **6.6** \| **5.1** \| **6.1** \| −1.5 \| −0.5 \| Low \| ⭐ **Top pick** \| | ...--\|---\|---\|---\|---\|---\|---\|---\|---\|---\| \| **Acetohydroxamic acid (AHA)** \| 9.29 \| 11.42 \| 4.8 \| **6.6** \| **5.1** \| **6.1** \| −1.5 \| −0.5 \| Low \| ⭐ **Top pick** \| \| **Oxalic acid** \| 1.04, 3.82 \| 7.58 \|... |
| 16 | 3 | exact_value | \| **Citric acid** \| 3.13, 4.76, 6.40 \| 11.2 \| 3.2–4.4 \| **6.8–8.0** \| **4.0** \| **6.2** \| −4.0 \| −1.6 \| Low \| ⭐ **Excellent** \| | ... \| ⚠️ FeC₂O₄·2H₂O \| Good but ppt risk \| \| **Citric acid** \| 3.13, 4.76, 6.40 \| 11.2 \| 3.2–4.4 \| **6.8–8.0** \| **4.0** \| **6.2** \| −4.0 \| −1.6 \| Low \| ⭐ **Excellent** \| \| **Malonic acid** \| 2.65, 5.28 \| 8.12 ... |
| 17 | 3 | exact_value | \| **Malonic acid** \| 2.65, 5.28 \| 8.12 \| 2.24 \| **5.9** \| **4.5** \| **6.1** \| −1.4 \| 0.2 \| Low \| ⭐ **Very good** \| | ...\| −4.0 \| −1.6 \| Low \| ⭐ **Excellent** \| \| **Malonic acid** \| 2.65, 5.28 \| 8.12 \| 2.24 \| **5.9** \| **4.5** \| **6.1** \| −1.4 \| 0.2 \| Low \| ⭐ **Very good** \| \| **Tartaric acid** \| 2.82, 3.95 \| 6.49... |
| 18 | 3 | exact_value | \| **Sulfosalicylic acid (SSA)** \| 2.48, 11.85 \| ~10 (vs L²⁻) \| 5.40 (vs HL⁻) \| **~3.3** (vs HL) \| **~2.7** \| **~3.7** \| ~0.4 \| ~1.4 \| Low \| Moderate \| | ...** \| **5.9** \| 0.2 \| 1.5 \| Low \| Good \| \| **Sulfosalicylic acid (SSA)** \| 2.48, 11.85 \| ~10 (vs L²⁻) \| 5.40 (vs HL⁻) \| **~3.3** (vs HL) \| **~2.7** \| **~3.7** \| ~0.4 \| ~1.4 \| Low \| Moderate \| \| **Fluoride** \| 2.94 (HF) \| 5.17 \| 0.8... |
| 19 | 3 | exact_value | \| **Sulfate** \| 1.54 \| 2.80 \| ~2.3 \| **~0.5** \| **2.8** \| **2.8** \| ~2.3 \| ~2.3 \| Low \| Poor selectivity \| | ...** \| 0.8 \| 0.8 \| Low \| Good but toxic \| \| **Sulfate** \| 1.54 \| 2.80 \| ~2.3 \| **~0.5** \| **2.8** \| **2.8** \| ~2.3 \| ~2.3 \| Low \| Poor selectivity \| \| **Phosphate** \| 2.15, 7.09 \| 3.47 (H₂... |
| 20 | 3 | exact_value | \| **Phosphate** \| 2.15, 7.09 \| 3.47 (H₂PO₄⁻) \| 0.55 (H₂PO₄⁻) \| **2.9** \| **3.5** \| **3.5** \| 0.6 \| 0.6 \| ⚠️ FePO₄ \| Moderate, ppt risk \| | ... ~2.3 \| ~2.3 \| Low \| Poor selectivity \| \| **Phosphate** \| 2.15, 7.09 \| 3.47 (H₂PO₄⁻) \| 0.55 (H₂PO₄⁻) \| **2.9** \| **3.5** \| **3.5** \| 0.6 \| 0.6 \| ⚠️ FePO₄ \| Moderate, ppt risk \| \| **Gluconic acid** \| 3.46 \| 3.1 \| −1.0... |
| 21 | 3 | exact_value | \| **Gluconic acid** \| 3.46 \| 3.1 \| −1.0 to 1.5 \| **1.6–4.1** \| **2.6** \| **3.1** \| <0 \| <0 \| Low \| Too weak \| | ...\| 0.6 \| ⚠️ FePO₄ \| Moderate, ppt risk \| \| **Gluconic acid** \| 3.46 \| 3.1 \| −1.0 to 1.5 \| **1.6–4.1** \| **2.6** \| **3.1** \| <0 \| <0 \| Low \| Too weak \| \| **EDTA** \| 2.0, 2.7, 6.2, 10.3 \| 25.1... |
| 22 | 3 | exact_value | \| **1,10-Phenanthroline** \| 4.92 \| 6.5 \| 5.85 (logβ₃=21) \| **−14.6** (β₃) \| — \| — \| — \| — \| Low \| ❌ Binds Fe²⁺ more! \| | ... ~3 \| ~5 \| ~−4 \| ~−2 \| Low \| Marginal \| \| **1,10-Phenanthroline** \| 4.92 \| 6.5 \| 5.85 (logβ₃=21) \| **−14.6** (β₃) \| — \| — \| — \| — \| Low \| ❌ Binds Fe²⁺ more! \| \| **Catechol** \| 9.26, 13.3 \| 20.4 (vs ... |
| 23 | 3 | exact_value | \| **Catechol** \| 9.26, 13.3 \| 20.4 (vs L²⁻) \| 8.3 (vs L²⁻) \| **12.1** \| ~−2.2 (vs H₂L) \| ~0.8 \| ~−14 \| ~−12 \| Low \| Too weak at pH<5 \| | ... — \| — \| — \| Low \| ❌ Binds Fe²⁺ more! \| \| **Catechol** \| 9.26, 13.3 \| 20.4 (vs L²⁻) \| 8.3 (vs L²⁻) \| **12.1** \| ~−2.2 (vs H₂L) \| ~0.8 \| ~−14 \| ~−12 \| Low \| Too weak at pH<5 \|  *Conditional logK values are approxima... |
| 24 | 4 | exact_value | \| Fe³⁺ logK₁ (M+L⁻⇌ML) \| 11.42 (20°C, I=0.1M) \| vlm_168448 \| | ...₃C(O)NHOH \| — \| \| pKa \| 9.29 \| SRD-46 \| \| Fe³⁺ logK₁ (M+L⁻⇌ML) \| 11.42 (20°C, I=0.1M) \| vlm_168448 \| \| Fe³⁺ logβ₂ \| 21.1 (20°C, I=0.1M) \| vl... |
| 25 | 4 | exact_value | \| Fe³⁺ logβ₂ \| 21.1 (20°C, I=0.1M) \| vlm_168453 \| | ...) \| 11.42 (20°C, I=0.1M) \| vlm_168448 \| \| Fe³⁺ logβ₂ \| 21.1 (20°C, I=0.1M) \| vlm_168453 \| \| Fe³⁺ logβ₃ \| 28.3 (20°C, I=0.1M) \| vl... |
| 26 | 4 | exact_value | \| Fe³⁺ logβ₃ \| 28.3 (20°C, I=0.1M) \| vlm_168455 \| | ...β₂ \| 21.1 (20°C, I=0.1M) \| vlm_168453 \| \| Fe³⁺ logβ₃ \| 28.3 (20°C, I=0.1M) \| vlm_168455 \| \| Fe²⁺ logK₁ (M+L⁻⇌ML) \| 4.8 (20°C, I=0... |
| 27 | 4 | exact_value | \| Fe²⁺ logβ₂ \| 8.5 (20°C, I=0.1M) \| vlm_168433 \| | ...ML) \| 4.8 (20°C, I=0.1M) \| vlm_168432 \| \| Fe²⁺ logβ₂ \| 8.5 (20°C, I=0.1M) \| vlm_168433 \| \| ΔlogK₁ \| **6.6** \| — \|  **Why AHA is ... |
| 28 | 4 | exact_value | \| ΔlogK₁ \| **6.6** \| — \| | ...gβ₂ \| 8.5 (20°C, I=0.1M) \| vlm_168433 \| \| ΔlogK₁ \| **6.6** \| — \|  **Why AHA is ideal:** - **Protonation ... |
| 29 | 4 | calculation | (conditional logK₁ ≈ 5.1) | ...1.5) while Fe³⁺ still binds effectively (conditional logK₁ ≈ 5.1) because Fe³⁺ is a much harder Lewis aci... |
| 30 | 4 | property_attribution | **No precipitation risk**: | ...the proton from the hydroxamic group. - **No precipitation risk**: Fe(III)-hydroxamate complexes are highl... |
| 31 | 4 | calculation | K_cond = 10⁵·¹ = 1.3×10⁵ | ... → **>99% Fe²⁺ remains free** ✓ - Fe³⁺: K_cond = 10⁵·¹ = 1.3×10⁵ → with 0.1 M AHA, virtually all Fe³⁺ is... |
| 32 | 4 | calculation | with 0.1 M AHA, virtually all Fe³⁺ is complexed ✓ | ...** ✓ - Fe³⁺: K_cond = 10⁵·¹ = 1.3×10⁵ → with 0.1 M AHA, virtually all Fe³⁺ is complexed ✓  **At pH 4:** - Fe²⁺: K_cond = 10⁻⁰·⁵ =... |
| 33 | 4 | calculation | K_cond = 10⁶·¹ | ...0.1M AHA → **~97% Fe²⁺ free** ✓ - Fe³⁺: K_cond = 10⁶·¹ → all Fe³⁺ complexed ✓... |
| 34 | 4 | calculation | all Fe³⁺ complexed ✓ | ... Fe²⁺ free** ✓ - Fe³⁺: K_cond = 10⁶·¹ → all Fe³⁺ complexed ✓... |
| 35 | 5 | exact_value | \| pKa₁, pKa₂, pKa₃ \| 3.13, 4.76, 6.40 \| SRD-46 \| | ...---\|---\| \| Formula \| C₆H₈O₇ (H₃L) \| — \| \| pKa₁, pKa₂, pKa₃ \| 3.13, 4.76, 6.40 \| SRD-46 \| \| Fe³⁺ logK₁ (M+L³⁻⇌ML) \| 11.2 (25°C, I... |
| 36 | 5 | range | \| Fe²⁺ logK₁ (M+L³⁻⇌ML) \| 3.2–4.4 (20-25°C, I=0.1M) \| SRD-46 \| | ...³⁻⇌ML) \| 11.2 (25°C, I=0.1M) \| SRD-46 \| \| Fe²⁺ logK₁ (M+L³⁻⇌ML) \| 3.2–4.4 (20-25°C, I=0.1M) \| SRD-46 \| \| Fe²⁺ logK (M+HL⇌MHL) \| 2.6–2.9 \| SRD-... |
| 37 | 5 | calculation | \| ΔlogK₁ \| **6.8–8.0** \| — \| | ...²⁺ logK (M+HL⇌MHL) \| 2.6–2.9 \| SRD-46 \| \| ΔlogK₁ \| **6.8–8.0** \| — \|  **Why citric acid works well:** - At p... |
| 38 | 5 | range | (~logK_cond ≈ 4–6) | ...ional Fe³⁺ binding is still significant (~logK_cond ≈ 4–6) because Fe³⁺ can chelate through the ca... |
| 39 | 5 | existence_absence | No precipitation risk | ...logK < 0) — free Fe²⁺ is preserved. - **No precipitation risk** — Fe(III)-citrate complexes are highl... |
| 40 | 5 | property_attribution | Cheap | ...trate complexes are highly soluble. - **Cheap, food-grade, non-toxic, widely used in ... |
| 41 | 5 | property_attribution | food-grade | ...omplexes are highly soluble. - **Cheap, food-grade, non-toxic, widely used in electroplati... |
| 42 | 5 | property_attribution | non-toxic | ... highly soluble. - **Cheap, food-grade, non-toxic, widely used in electroplating**. - Cau... |
| 43 | 5 | property_attribution | widely used in electroplating | ...uble. - **Cheap, food-grade, non-toxic, widely used in electroplating**. - Caution: dinuclear Fe₂(OH)₂(cit)₂ ... |
| 44 | 6 | exact_value | \| pKa₁, pKa₂ \| 2.65, 5.28 \| SRD-46 \| | ...---\| \| Formula \| CH₂(COOH)₂ (H₂L) \| — \| \| pKa₁, pKa₂ \| 2.65, 5.28 \| SRD-46 \| \| Fe³⁺ logK₁ (M+L²⁻⇌ML) \| 8.12 (25°C, I... |
| 45 | 6 | exact_value | \| Fe³⁺ logK₁ (M+L²⁻⇌ML) \| 8.12 (25°C, I=0.1M) \| SRD-46 \| | ... \| \| pKa₁, pKa₂ \| 2.65, 5.28 \| SRD-46 \| \| Fe³⁺ logK₁ (M+L²⁻⇌ML) \| 8.12 (25°C, I=0.1M) \| SRD-46 \| \| Fe³⁺ logβ₂ \| 14.00 (25°C, I=0.1M) \| S... |
| 46 | 6 | exact_value | \| Fe³⁺ logβ₂ \| 14.00 (25°C, I=0.1M) \| SRD-46 \| | ...²⁻⇌ML) \| 8.12 (25°C, I=0.1M) \| SRD-46 \| \| Fe³⁺ logβ₂ \| 14.00 (25°C, I=0.1M) \| SRD-46 \| \| Fe²⁺ logK₁ (M+L²⁻⇌ML) \| 2.24 (25°C, I... |
| 47 | 6 | exact_value | \| ΔlogK₁ \| **5.9** \| — \| | ...+L²⁻⇌ML) \| 2.24 (25°C, I=1M) \| SRD-46 \| \| ΔlogK₁ \| **5.9** \| — \|  **Why malonic acid is good:** - At pH ... |
| 48 | 6 | exact_value | Conditional Fe³⁺ logK at pH 3 ≈ 4.5 | ...d availability for Fe³⁺ complexation. - Conditional Fe³⁺ logK at pH 3 ≈ 4.5 — adequate for Fe³⁺ stabilization. - Fe... |
| 49 | 6 | range | (conditional logK < 0 at pH 3) | ...bilization. - Fe²⁺ binding is very weak (conditional logK < 0 at pH 3) — free Fe²⁺ preserved. - **No precipita... |
| 50 | 6 | property_attribution | **No precipitation risk** | ...K < 0 at pH 3) — free Fe²⁺ preserved. - **No precipitation risk** — Fe(III)-malonate complexes are solubl... |
| 51 | 6 | property_attribution | Fe(III)-malonate complexes are soluble. | ...reserved. - **No precipitation risk** — Fe(III)-malonate complexes are soluble. - Simple bidentate chelate ring (6-memb... |
| 52 | 6 | property_attribution | Simple bidentate chelate ring (6-membered) | ...(III)-malonate complexes are soluble. - Simple bidentate chelate ring (6-membered) — kinetically labile, good for dynamic ... |
| 53 | 6 | property_attribution | kinetically labile | ...e bidentate chelate ring (6-membered) — kinetically labile, good for dynamic equilibrium.... |
| 54 | 7 | exact_value | \| pKa₁, pKa₂ \| 1.04, 3.82 \| SRD-46 \| | ...operty \| Value \| Source \| \|---\|---\|---\| \| pKa₁, pKa₂ \| 1.04, 3.82 \| SRD-46 \| \| Fe³⁺ logK₁ \| 7.58 (25°C, I=1M) \| SRD-... |
| 55 | 7 | exact_value | \| Fe³⁺ logβ₃ \| 18.6 (25°C, I=1M) \| SRD-46 \| | ...³⁺ logK₁ \| 7.58 (25°C, I=1M) \| SRD-46 \| \| Fe³⁺ logβ₃ \| 18.6 (25°C, I=1M) \| SRD-46 \| \| Fe²⁺ logK₁ \| 3.05 (25°C, I=1M) \| SRD-... |
| 56 | 7 | calculation | At 0.1 M Fe²⁺, precipitation occurs when [C₂O₄²⁻] > 2×10⁻⁶ M. | ...drate (humboldtine) has Ksp ≈ 2×10⁻⁷. - At 0.1 M Fe²⁺, precipitation occurs when [C₂O₄²⁻] > 2×10⁻⁶ M. - At pH 3 with 0.1 M total oxalate: [C₂... |
| 57 | 7 | range | very low concentrations (<10⁻⁴ M) | ...cid is NOT recommended** unless used at very low concentrations (<10⁻⁴ M), which limits its Fe³⁺ stabilization ca... |
| 58 | 8 | exact_value | \| pKa₁, pKa₂ \| 2.82, 3.95 \| SRD-46 \| | ...operty \| Value \| Source \| \|---\|---\|---\| \| pKa₁, pKa₂ \| 2.82, 3.95 \| SRD-46 \| \| Fe³⁺ logK₁ \| 6.49–6.66 (20-25°C, I=0.... |
| 59 | 8 | existence_absence | No precipitation risk. | ...at pH 3–5 — good ligand availability. - No precipitation risk. Widely used in electroplating. - Slight... |
| 60 | 8 | property_attribution | Widely used in electroplating. | ... availability. - No precipitation risk. Widely used in electroplating. - Slightly weaker Fe³⁺ binding than cit... |
| 61 | 9 | exact_value | \| **1,10-Phenanthroline** \| Fe²⁺ logβ₃ = 21 > Fe³⁺ logβ₃ = 14 — preferentially sequesters Fe²⁺! \| | ...too strongly, would deplete free Fe²⁺ \| \| **1,10-Phenanthroline** \| Fe²⁺ logβ₃ = 21 > Fe³⁺ logβ₃ = 14 — preferentially sequesters Fe²⁺! \| \| **NTA** \| Fe²⁺ logK₁ = 8.9 — signific... |
| 62 | 9 | exact_value | \| **Oxalic acid** \| FeC₂O₄·2H₂O precipitation at 0.1 M Fe²⁺ \| | ...— significant Fe²⁺ depletion at 0.1 M \| \| **Oxalic acid** \| FeC₂O₄·2H₂O precipitation at 0.1 M Fe²⁺ \| \| **Ascorbic acid** \| Reduces Fe³⁺ → Fe... |
| 63 | 9 | exact_value | \| **Phosphate** \| FePO₄ precipitation risk (Ksp ≈ 10⁻²²) \| | ...(redox-active), defeating the purpose \| \| **Phosphate** \| FePO₄ precipitation risk (Ksp ≈ 10⁻²²) \| \| **Catechol** \| pKa₁ = 9.26 → fully pr... |
| 64 | 9 | exact_value | \| **Catechol** \| pKa₁ = 9.26 → fully protonated at pH < 5, negligible binding \| | ...ePO₄ precipitation risk (Ksp ≈ 10⁻²²) \| \| **Catechol** \| pKa₁ = 9.26 → fully protonated at pH < 5, negligible binding \| \| **Glycine** \| Too weak Fe³⁺ binding a... |
| 65 | 9 | exact_value | \| **Glycine** \| Too weak Fe³⁺ binding at pH < 5 (conditional logK ≈ 2) \| | ...tonated at pH < 5, negligible binding \| \| **Glycine** \| Too weak Fe³⁺ binding at pH < 5 (conditional logK ≈ 2) \|... |
| 66 | 10 | exact_value | Fe³⁺ logK₁ = 11.4 | ...timate based on:  1. **AHA benchmark**: Fe³⁺ logK₁ = 11.4, Fe²⁺ logK₁ = 4.8, ΔlogK = 6.6 2. **HSA... |
| 67 | 10 | exact_value | ΔlogK = 6.6 | ...*: Fe³⁺ logK₁ = 11.4, Fe²⁺ logK₁ = 4.8, ΔlogK = 6.6 2. **HSAB principle**: Hydroxamic acids... |
| 68 | 10 | exact_value | Fe³⁺ logK₁ = 19.4 | ...trilotriacetohydroxamic acid (NTAHA)**, Fe³⁺ logK₁ = 19.4: - Estimated Fe²⁺ logK₁ ≈ 19.4 − 6.6 ≈ ... |
| 69 | 10 | calculation | Estimated Fe²⁺ logK₁ ≈ 19.4 − 6.6 ≈ **12.8** (using AHA ΔlogK) | ...ic acid (NTAHA)**, Fe³⁺ logK₁ = 19.4: - Estimated Fe²⁺ logK₁ ≈ 19.4 − 6.6 ≈ **12.8** (using AHA ΔlogK) - This would be too strong for Fe²⁺ — w... |
| 70 | 10 | listing | NTAHA pKa values (5.92, 6.81, 8.84) | ...²⁺ — would deplete free Fe²⁺ - However, NTAHA pKa values (5.92, 6.81, 8.84) mean at pH < 5, the ligand is fully pro... |
| 71 | 10 | domain_reasoning | at pH < 5, the ligand is fully protonated | ...TAHA pKa values (5.92, 6.81, 8.84) mean at pH < 5, the ligand is fully protonated → conditional Fe²⁺ binding negligible  ... |
| 72 | 10 | domain_reasoning | conditional Fe²⁺ binding negligible | ...H < 5, the ligand is fully protonated → conditional Fe²⁺ binding negligible  For **4-nitrocatechol** (Fe³⁺ + H₂L ⇌ ... |
| 73 | 10 | exact_value | logK = −2.0 | ...itrocatechol** (Fe³⁺ + H₂L ⇌ FeL + 2H⁺, logK = −2.0): - Using catechol ΔlogK ≈ 12: Fe²⁺ + H... |
| 74 | 10 | calculation | Using catechol ΔlogK ≈ 12: Fe²⁺ + H₂L ⇌ FeL + 2H⁺, logK ≈ −14 | ...Fe³⁺ + H₂L ⇌ FeL + 2H⁺, logK = −2.0): - Using catechol ΔlogK ≈ 12: Fe²⁺ + H₂L ⇌ FeL + 2H⁺, logK ≈ −14 - At pH 3: conditional Fe³⁺ logK ≈ −2 +... |
| 75 | 10 | calculation | At pH 3: conditional Fe³⁺ logK ≈ −2 + 2×3 = 4 | ...2: Fe²⁺ + H₂L ⇌ FeL + 2H⁺, logK ≈ −14 - At pH 3: conditional Fe³⁺ logK ≈ −2 + 2×3 = 4; Fe²⁺ logK ≈ −14 + 6 = −8 - Excellent s... |
| 76 | 10 | calculation | Fe²⁺ logK ≈ −14 + 6 = −8 | ...: conditional Fe³⁺ logK ≈ −2 + 2×3 = 4; Fe²⁺ logK ≈ −14 + 6 = −8 - Excellent selectivity but moderate Fe... |
| 77 | 11 | exact_value | ΔlogK = 6.6 | ...)** - Best balance of Fe³⁺ selectivity (ΔlogK = 6.6), adequate conditional binding at pH 3–... |
| 78 | 11 | property_attribution | adequate conditional binding at pH 3–5 | ...ance of Fe³⁺ selectivity (ΔlogK = 6.6), adequate conditional binding at pH 3–5, no precipitation, redox stability, and... |
| 79 | 11 | existence_absence | no precipitation | ...adequate conditional binding at pH 3–5, no precipitation, redox stability, and commercial availa... |
| 80 | 11 | existence_absence | commercial availability | ... no precipitation, redox stability, and commercial availability. - Suggested concentration: 0.05–0.2 M ... |
| 81 | 11 | range | 0.05–0.2 M | ...vailability. - Suggested concentration: 0.05–0.2 M (adjust based on expected Fe³⁺ concentr... |
| 82 | 11 | range | At pH 3–4 | ...based on expected Fe³⁺ concentration) - At pH 3–4 with 0.1 M AHA: >99% Fe²⁺ remains free,... |
| 83 | 11 | exact_value | 0.1 M AHA | ...ed Fe³⁺ concentration) - At pH 3–4 with 0.1 M AHA: >99% Fe²⁺ remains free, virtually all ... |
| 84 | 11 | range | >99% Fe²⁺ remains free | ...centration) - At pH 3–4 with 0.1 M AHA: >99% Fe²⁺ remains free, virtually all Fe³⁺ complexed... |
| 85 | 11 | property_attribution | virtually all Fe³⁺ complexed | ...with 0.1 M AHA: >99% Fe²⁺ remains free, virtually all Fe³⁺ complexed... |