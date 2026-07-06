# Q4.3 - Validation (batch 1)

**47 of 115 claims unsupported**

| # | Para | Type | Unsupported Claim | Context |
|---|------|------|-------------------|---------|
| 1 | 1 | exact_value | \| Cu²⁺ \| metal_41 \| 8963 VLM records \| | ... Notes \| \|--------\|-----------\|-------\| \| Cu²⁺ \| metal_41 \| 8963 VLM records \| \| Ni²⁺ \| metal_112 \| 5325 VLM records \|... |
| 2 | 1 | exact_value | \| Ni²⁺ \| metal_112 \| 5325 VLM records \| | ... \| Cu²⁺ \| metal_41 \| 8963 VLM records \| \| Ni²⁺ \| metal_112 \| 5325 VLM records \| \| Zn²⁺ \| metal_208 \| 4095 VLM records \|... |
| 3 | 1 | exact_value | \| Zn²⁺ \| metal_208 \| 4095 VLM records \| | ...\| Ni²⁺ \| metal_112 \| 5325 VLM records \| \| Zn²⁺ \| metal_208 \| 4095 VLM records \| \| Ethylenediamine (en) \| ligand_7029 \| ... |
| 4 | 2 | citation | Stability Constants Retrieved from SRD-46 | ...## Stability Constants Retrieved from SRD-46 (25 °C, I = 0, water/KNO₃)  The databas... |
| 5 | 2 | exact_value | 25 °C | ...bility Constants Retrieved from SRD-46 (25 °C, I = 0, water/KNO₃)  The database retur... |
| 6 | 2 | exact_value | I = 0 | ...Constants Retrieved from SRD-46 (25 °C, I = 0, water/KNO₃)  The database returned hig... |
| 7 | 2 | listing | water/KNO₃ | ...ts Retrieved from SRD-46 (25 °C, I = 0, water/KNO₃)  The database returned highly consiste... |
| 8 | 2 | property_attribution | The database returned highly consistent values | ...from SRD-46 (25 °C, I = 0, water/KNO₃)  The database returned highly consistent values across many independent measurements. T... |
| 9 | 2 | counting | across many independent measurements. | ...abase returned highly consistent values across many independent measurements. The dominant values at 25 °C, I = 0 are... |
| 10 | 4 | exact_value | 25 °C | ...Metal \| log K₁(NH₃) \| # measurements at 25 °C, I=0 \| \|-------\|------------\|----------... |
| 11 | 4 | exact_value | \| Cu²⁺ \| **4.31** \| ≥6 concordant entries \| | ...------\|-------------------------------\| \| Cu²⁺ \| **4.31** \| ≥6 concordant entries \| \| Ni²⁺ \| **2.80** \| multiple entries \| ... |
| 12 | 4 | exact_value | \| Ni²⁺ \| **2.80** \| multiple entries \| | ...²⁺ \| **4.31** \| ≥6 concordant entries \| \| Ni²⁺ \| **2.80** \| multiple entries \| \| Zn²⁺ \| **2.37** \| multiple entries \| ... |
| 13 | 4 | exact_value | \| Zn²⁺ \| **2.37** \| multiple entries \| | ... \| Ni²⁺ \| **2.80** \| multiple entries \| \| Zn²⁺ \| **2.37** \| multiple entries \|  The SRD-46 database also contains log ... |
| 14 | 4 | existence_absence | The SRD-46 database also contains log K₂(NH₃) values | ...\| Zn²⁺ \| **2.37** \| multiple entries \|  The SRD-46 database also contains log K₂(NH₃) values (ML₂ reaction). Standard literature val... |
| 15 | 4 | comparison | Standard literature values consistent with the database for K₂ | ...ains log K₂(NH₃) values (ML₂ reaction). Standard literature values consistent with the database for K₂ at 25 °C, I ≈ 0:  \| Metal \| log K₂(NH₃)... |
| 16 | 4 | exact_value | I ≈ 0 | ...tent with the database for K₂ at 25 °C, I ≈ 0:  \| Metal \| log K₂(NH₃) \| \|-------\|----... |
| 17 | 4 | exact_value | \| Cu²⁺ \| **3.67** \| | ... \| log K₂(NH₃) \| \|-------\|------------\| \| Cu²⁺ \| **3.67** \| \| Ni²⁺ \| **2.24** \| \| Zn²⁺ \| **2.44** \|... |
| 18 | 4 | exact_value | \| Ni²⁺ \| **2.24** \| | ...-----\|------------\| \| Cu²⁺ \| **3.67** \| \| Ni²⁺ \| **2.24** \| \| Zn²⁺ \| **2.44** \|... |
| 19 | 4 | exact_value | \| Zn²⁺ \| **2.44** \| | ...\| Cu²⁺ \| **3.67** \| \| Ni²⁺ \| **2.24** \| \| Zn²⁺ \| **2.44** \|... |
| 20 | 5 | exact_value | \| Cu²⁺  \| 10.72     \| 4.31       \| 3.67       \| 7.98       \| **+2.74**    \| | ...----------\|------------\|--------------\| \| Cu²⁺  \| 10.72     \| 4.31       \| 3.67       \| 7.98       \| **+2.74**    \| \| Ni²⁺  \| 7.47      \| 2.80       \| 2.24... |
| 21 | 5 | exact_value | \| Ni²⁺  \| 7.47      \| 2.80       \| 2.24       \| 5.04       \| **+2.43**    \| | ....67       \| 7.98       \| **+2.74**    \| \| Ni²⁺  \| 7.47      \| 2.80       \| 2.24       \| 5.04       \| **+2.43**    \| \| Zn²⁺  \| 5.77      \| 2.37       \| 2.44... |
| 22 | 5 | exact_value | \| Zn²⁺  \| 5.77      \| 2.37       \| 2.44       \| 4.81       \| **+0.96**    \| | ....24       \| 5.04       \| **+2.43**    \| \| Zn²⁺  \| 5.77      \| 2.37       \| 2.44       \| 4.81       \| **+0.96**    \|... |
| 23 | 6 | exact_value | \| Cu²⁺  \| 2.74      \| 1.00× (reference) \| | ...\|-------\|-----------\|-----------------\| \| Cu²⁺  \| 2.74      \| 1.00× (reference) \| \| Ni²⁺  \| 2.43      \| 0.89× \| \| Zn²⁺  \|... |
| 24 | 6 | exact_value | \| Ni²⁺  \| 2.43      \| 0.89× \| | ...Cu²⁺  \| 2.74      \| 1.00× (reference) \| \| Ni²⁺  \| 2.43      \| 0.89× \| \| Zn²⁺  \| 0.96      \| 0.35× \|  The chel... |
| 25 | 6 | exact_value | \| Zn²⁺  \| 0.96      \| 0.35× \| | ...erence) \| \| Ni²⁺  \| 2.43      \| 0.89× \| \| Zn²⁺  \| 0.96      \| 0.35× \|  The chelate effect varies by nearly **... |
| 26 | 6 | comparison | The chelate effect varies by nearly **3-fold** across these three metals. | ... 0.89× \| \| Zn²⁺  \| 0.96      \| 0.35× \|  The chelate effect varies by nearly **3-fold** across these three metals. Cu²⁺ and Ni²⁺ show similar, large chela... |
| 27 | 6 | comparison | Cu²⁺ and Ni²⁺ show similar, large chelate effects | ...y **3-fold** across these three metals. Cu²⁺ and Ni²⁺ show similar, large chelate effects (~2.4–2.7 log units), while Zn²⁺ shows ... |
| 28 | 6 | range | (~2.4–2.7 log units) | ...i²⁺ show similar, large chelate effects (~2.4–2.7 log units), while Zn²⁺ shows a dramatically smalle... |
| 29 | 6 | comparison | Zn²⁺ shows a dramatically smaller effect | ...ate effects (~2.4–2.7 log units), while Zn²⁺ shows a dramatically smaller effect (~1.0 log unit).... |
| 30 | 6 | exact_value | (~1.0 log unit) | ...n²⁺ shows a dramatically smaller effect (~1.0 log unit).... |
| 31 | 7 | range | This entropic contribution is estimated at ~+20–25 J mol⁻¹ K⁻¹ | ...m is very high once the first is bound  This entropic contribution is estimated at ~+20–25 J mol⁻¹ K⁻¹, corresponding to ~1.0–1.3 log units at... |
| 32 | 7 | range | corresponding to ~1.0–1.3 log units | ...on is estimated at ~+20–25 J mol⁻¹ K⁻¹, corresponding to ~1.0–1.3 log units at 25 °C — and is **roughly metal-indep... |
| 33 | 7 | exact_value | at 25 °C | ...⁻¹, corresponding to ~1.0–1.3 log units at 25 °C — and is **roughly metal-independent**.... |
| 34 | 7 | exact_value | Zn²⁺ shows Δ ≈ 1.0. | ...l-independent**. This explains why even Zn²⁺ shows Δ ≈ 1.0.... |
| 35 | 8 | property_attribution | The extra chelate effect seen for Cu²⁺ and Ni²⁺ | ... The Enthalpic Bonus — Metal-Dependent  The extra chelate effect seen for Cu²⁺ and Ni²⁺ (Δ ≈ 2.4–2.7 vs. ~1.0 for Zn²⁺) arises ... |
| 36 | 8 | comparison | (Δ ≈ 2.4–2.7 vs. ~1.0 for Zn²⁺) | ...a chelate effect seen for Cu²⁺ and Ni²⁺ (Δ ≈ 2.4–2.7 vs. ~1.0 for Zn²⁺) arises from an **enthalpic contribution... |
| 37 | 8 | exact_value | (~82°) | ... of en fits the equatorial N–Cu–N angle (~82°) almost perfectly, providing geometric p... |
| 38 | 8 | range | This geometric complementarity delivers an extra enthalpic stabilization of ~1–2 kJ/mol per bond | ... separate NH₃ ligands cannot replicate. This geometric complementarity delivers an extra enthalpic stabilization of ~1–2 kJ/mol per bond, amplifying the chelate effect beyond t... |
| 39 | 8 | comparison | The result is a chelate effect nearly as large as Cu²⁺. | ...ry and reduces ligand-field distortion. The result is a chelate effect nearly as large as Cu²⁺.  **Zn²⁺ (d¹⁰, CFSE = 0):** Zn²⁺ is a sp... |
| 40 | 8 | exact_value | Δ ≈ 1.0 | ...fore **almost purely entropic**, giving Δ ≈ 1.0 — close to the theoretical entropic bas... |
| 41 | 9 | range | pushing Δ to ~2.4–2.7. | ...ificant enthalpic bonus from chelation, pushing Δ to ~2.4–2.7. Metals with d¹⁰ configuration and no CF... |
| 42 | 9 | exact_value | giving Δ ≈ 1.0. | ...receive only the entropic contribution, giving Δ ≈ 1.0.  This is fully consistent with the **Ir... |
| 43 | 9 | trend | the *chelate enhancement above the monodentate baseline* also follows this order | ...r absolute stability), and explains why the *chelate enhancement above the monodentate baseline* also follows this order — the same electronic factors that make... |
| 44 | 9 | citation | *All stability constants retrieved directly from NIST SRD-46 | ...e it benefit most from chelation.  ---  *All stability constants retrieved directly from NIST SRD-46 (metal_41, metal_112, metal_208; ligand... |
| 45 | 9 | exact_value | at 25 °C | ..., metal_208; ligand_7029, ligand_10103) at 25 °C, I = 0, aqueous KNO₃ medium.*... |
| 46 | 9 | exact_value | I = 0 | ...8; ligand_7029, ligand_10103) at 25 °C, I = 0, aqueous KNO₃ medium.*... |
| 47 | 9 | property_attribution | aqueous KNO₃ medium. | ...nd_7029, ligand_10103) at 25 °C, I = 0, aqueous KNO₃ medium.*... |