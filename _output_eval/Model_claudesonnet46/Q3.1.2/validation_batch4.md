# Q3.1.2 - Validation (batch 4)

**32 of 96 claims unsupported**

| # | Para | Type | Unsupported Claim | Context |
|---|------|------|-------------------|---------|
| 1 | 0 | exact_value | I = 0.1 M | ...lity constants from NIST SRD-46, 25 °C, I = 0.1 M, aqueous.*... |
| 2 | 1 | exact_value | \| **Glycine** (ligand_5760) \| 8.57 \| 6.18 \| 15.54 \| 11.12 \| | ...(ML₂) Ni²⁺ \| \|--------\|:-:\|:-:\|:-:\|:-:\| \| **Glycine** (ligand_5760) \| 8.57 \| 6.18 \| 15.54 \| 11.12 \| \| **L-Histidine** (ligand_5898) \| 10.60... |
| 3 | 1 | exact_value | \| **L-Histidine** (ligand_5898) \| 10.60 \| 8.70 \| 19.60 \| 16.40 \| | ...d_5760) \| 8.57 \| 6.18 \| 15.54 \| 11.12 \| \| **L-Histidine** (ligand_5898) \| 10.60 \| 8.70 \| 19.60 \| 16.40 \| \| **L-Cysteine** (ligand_5856) \| 19.20 ... |
| 4 | 1 | exact_value | \| **L-Cysteine** (ligand_5856) \| 19.20 \| 9.90 \| — \| — \| | ..._5898) \| 10.60 \| 8.70 \| 19.60 \| 16.40 \| \| **L-Cysteine** (ligand_5856) \| 19.20 \| 9.90 \| — \| — \|... |
| 5 | 2 | exact_value | at 25 °C | ...### pKa Values at 25 °C, I = 0.1 M (from SRD-46)  \| Ligand \| pK... |
| 6 | 2 | exact_value | I = 0.1 M | ...### pKa Values at 25 °C, I = 0.1 M (from SRD-46)  \| Ligand \| pKa₁ (COOH) \|... |
| 7 | 2 | exact_value | \| L-Histidine \| 1.70 \| 6.05 (imidazole-H⁺) \| 9.10 (–NH₃⁺) \| | ...\| \| Glycine \| 2.33 \| 9.57 (–NH₃⁺) \| — \| \| L-Histidine \| 1.70 \| 6.05 (imidazole-H⁺) \| 9.10 (–NH₃⁺) \| \| L-Cysteine \| 1.90 \| 8.18 (–SH) \| 10.3... |
| 8 | 2 | exact_value | \| L-Cysteine \| 1.90 \| 8.18 (–SH) \| 10.30 (–NH₃⁺) \| | ... \| 6.05 (imidazole-H⁺) \| 9.10 (–NH₃⁺) \| \| L-Cysteine \| 1.90 \| 8.18 (–SH) \| 10.30 (–NH₃⁺) \|... |
| 9 | 3 | calculation | - log β′₁(Cu²⁺) = 8.57 − 2.57 = **6.00** | ...αL ≈ 9.57 − 7 = **2.57 log units lost** - log β′₁(Cu²⁺) = 8.57 − 2.57 = **6.00** - log β′₁(Ni²⁺) = 6.18 − 2.57 = **3.61*... |
| 10 | 3 | calculation | - log β′₁(Ni²⁺) = 6.18 − 2.57 = **3.61** | ... log β′₁(Cu²⁺) = 8.57 − 2.57 = **6.00** - log β′₁(Ni²⁺) = 6.18 − 2.57 = **3.61** - **Δlog β′ = 2.39**  **L-Histidine** —... |
| 11 | 3 | calculation | - **Δlog β′ = 2.39** | ... log β′₁(Ni²⁺) = 6.18 − 2.57 = **3.61** - **Δlog β′ = 2.39**  **L-Histidine** — imidazole pKa = 6.05... |
| 12 | 3 | calculation | - log β′₁(Cu²⁺) = 10.60 − 2.10 = **8.50** | ...e correction is only ~0.09, negligible) - log β′₁(Cu²⁺) = 10.60 − 2.10 = **8.50** - log β′₁(Ni²⁺) = 8.70 − 2.10 = **6.60*... |
| 13 | 3 | calculation | - log β′₁(Ni²⁺) = 8.70 − 2.10 = **6.60** | ...log β′₁(Cu²⁺) = 10.60 − 2.10 = **8.50** - log β′₁(Ni²⁺) = 8.70 − 2.10 = **6.60** - **Δlog β′ = 1.90**  For the bis-compl... |
| 14 | 3 | calculation | - **Δlog β′ = 1.90** | ... log β′₁(Ni²⁺) = 8.70 − 2.10 = **6.60** - **Δlog β′ = 1.90**  For the bis-complex (ML₂), both ligand... |
| 15 | 3 | calculation | - log β′₂(Cu²⁺) = 19.60 − 4.20 = **15.40** | ...eprotonated, so the correction doubles: - log β′₂(Cu²⁺) = 19.60 − 4.20 = **15.40** - log β′₂(Ni²⁺) = 16.40 − 4.20 = **12.2... |
| 16 | 3 | calculation | - log β′₂(Ni²⁺) = 16.40 − 4.20 = **12.20** | ...og β′₂(Cu²⁺) = 19.60 − 4.20 = **15.40** - log β′₂(Ni²⁺) = 16.40 − 4.20 = **12.20** - **Δlog β′₂ = 3.20** ← largest gap of ... |
| 17 | 3 | calculation | - **Δlog β′₂ = 3.20** | ...og β′₂(Ni²⁺) = 16.40 − 4.20 = **12.20** - **Δlog β′₂ = 3.20** ← largest gap of all  **L-Cysteine** — ... |
| 18 | 3 | comparison | largest gap of all | ....20 = **12.20** - **Δlog β′₂ = 3.20** ← largest gap of all  **L-Cysteine** — thiol pKa = 8.18; at ... |
| 19 | 3 | calculation | - log β′₁(Cu²⁺) = 19.20 − 3.30 = **15.90** | ...3.30 log units lost** (amine dominates) - log β′₁(Cu²⁺) = 19.20 − 3.30 = **15.90** - log β′₁(Ni²⁺) = 9.90 − 3.30 = **6.60*... |
| 20 | 3 | calculation | - log β′₁(Ni²⁺) = 9.90 − 3.30 = **6.60** | ...og β′₁(Cu²⁺) = 19.20 − 3.30 = **15.90** - log β′₁(Ni²⁺) = 9.90 − 3.30 = **6.60** - **Δlog β′ = 9.30** — enormous gap, bu... |
| 21 | 3 | calculation | - **Δlog β′ = 9.30** — enormous gap, but read the caveat below. | ... log β′₁(Ni²⁺) = 9.90 − 3.30 = **6.60** - **Δlog β′ = 9.30** — enormous gap, but read the caveat below.... |
| 22 | 5 | calculation | Δlog β′ ≈ 9.3 at pH 7 | ...ity: L-Cysteine** delivers a staggering Δlog β′ ≈ 9.3 at pH 7 (selectivity ratio ~2 × 10⁹). This is b... |
| 23 | 5 | calculation | selectivity ratio ~2 × 10⁹ | ...ers a staggering Δlog β′ ≈ 9.3 at pH 7 (selectivity ratio ~2 × 10⁹). This is because Cu²⁺ has an exception... |
| 24 | 5 | exact_value | log β₁ = 19.2 | ...y high affinity for soft sulfur donors (log β₁ = 19.2 vs Ni²⁺'s 9.9 — a raw gap of 9.3 log un... |
| 25 | 5 | exact_value | Ni²⁺'s 9.9 | ...or soft sulfur donors (log β₁ = 19.2 vs Ni²⁺'s 9.9 — a raw gap of 9.3 log units), and the ... |
| 26 | 5 | calculation | a raw gap of 9.3 log units | ...r donors (log β₁ = 19.2 vs Ni²⁺'s 9.9 — a raw gap of 9.3 log units), and the thiol is only partially proto... |
| 27 | 5 | listing | The ML₂ complex | ...u²⁺'s preferred square-planar geometry. The ML₂ complex gives Δlog β′₂ = 3.2 (~1600-fold select... |
| 28 | 5 | calculation | Δlog β′₂ = 3.2 | ...-planar geometry. The ML₂ complex gives Δlog β′₂ = 3.2 (~1600-fold selectivity) — robust and w... |
| 29 | 5 | calculation | ~1600-fold selectivity | .... The ML₂ complex gives Δlog β′₂ = 3.2 (~1600-fold selectivity) — robust and well-documented.  > **Pra... |
| 30 | 5 | exact_value | All constants at 25 °C | ...L-Histidine), ligand_5856 (L-Cysteine). All constants at 25 °C, I = 0.1 M, aqueous.*... |
| 31 | 5 | exact_value | I = 0.1 M | ...6 (L-Cysteine). All constants at 25 °C, I = 0.1 M, aqueous.*... |
| 32 | 5 | property_attribution | aqueous | ...ne). All constants at 25 °C, I = 0.1 M, aqueous.*... |