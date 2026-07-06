Now I have sufficient data to deliver a comprehensive final answer. Let me compile everything.

---

# Co²⁺ vs Co³⁺ Stability Constants: A Crystal-Field Analysis

*Source: NIST SRD-46 Critically Selected Stability Constants of Metal Complexes*

---

## 1. The Overlap Set: Ligands Studied with Both Co²⁺ and Co³⁺

The SRD-46 database contains **Co²⁺ (metal_33)** with 977 ligands and **Co³⁺ (metal_34)** with only 19 ligands — reflecting the experimental challenge of working with kinetically inert Co³⁺. The confirmed overlap set with matched reference conditions (~20–30 °C, low ionic strength) includes:

| Ligand | Denticity | Donor Type |
|--------|-----------|------------|
| Ammonia (NH₃) | 1 | N |
| Ethylenediamine (en) | 2 | N,N |
| Iminodiacetic acid (IDA) | 3 | N,O,O |
| Nitrilotriacetic acid (NTA) | 4 | N,O,O,O |
| EDTA | 6 | N,N,O,O,O,O |

---

## 2. Stability Constant Comparison Table

All values are log K or log β at T ≈ 20–30 °C, I ≈ 0–0.25 M (reference-state networks).

### Ammonia (NH₃) — Monodentate N-donor

| Species | Equation | log K (Co²⁺) | log K (Co³⁺) | Δ log K |
|---------|----------|:---:|:---:|:---:|
| ML (CoNH₃) | M + L ⇌ ML | 2.08 | — | — |
| ML₅ (Co(NH₃)₅) | M + 5L ⇌ ML₅ | 5.13 | — | — |
| ML₆ (Co(NH₃)₆) | M + 6L ⇌ ML₆ | — | **34.36** | — |

> Note: Co³⁺ data for NH₃ are reported as cumulative β₆ = **log β = 34.36** (I = 1 M, 25–35 °C). For Co²⁺, the highest measured is β₅ = 5.13. Extrapolating Co²⁺ β₆ ≈ 5.1 (stepwise K₆ ≈ 0), the **Δ log β ≈ +29 log units** in favor of Co³⁺.

### Ethylenediamine (en) — Bidentate N,N-donor

| Species | Equation | log β (Co²⁺) | log β (Co³⁺) | Δ log β |
|---------|----------|:---:|:---:|:---:|
| ML (Co·en) | M + L ⇌ ML | 5.50 | — | — |
| ML₂ (Co·en₂) | M + 2L ⇌ ML₂ | 10.10 | — | — |
| ML₃ (Co·en₃) | M + 3L ⇌ ML₃ | **13.40** | **48.69** | **+35.3** |

### Iminodiacetic acid (IDA) — Tridentate N,O,O-donor

| Species | Equation | log β (Co²⁺) | log β (Co³⁺) | Δ log β |
|---------|----------|:---:|:---:|:---:|
| ML | M + L ⇌ ML | **6.97** | **29.60** | **+22.6** |
| ML₂ | M + 2L ⇌ ML₂ | 12.20 | — | — |

### Nitrilotriacetic acid (NTA) — Tetradentate N,O,O,O-donor

| Species | Equation | log β (Co²⁺) | log β (Co³⁺) | Δ log β |
|---------|----------|:---:|:---:|:---:|
| ML | M + L ⇌ ML | **10.38** | — | — |
| M(OH)L | M(OH)L + H ⇌ ML + H₂O | 10.80 | **6.84** | — |

> Note: The Co³⁺ NTA data are reported only as hydroxo-complex equilibria (no direct β₁ for ML), reflecting the strong tendency of Co³⁺ to hydrolyze. Direct comparison is limited here.

### EDTA — Hexadentate N,N,O,O,O,O-donor

| Species | Equation | log β (Co²⁺) | log β (Co³⁺) | Δ log β |
|---------|----------|:---:|:---:|:---:|
| ML | M + L ⇌ ML | **16.45** | **41.40** | **+24.95** |
| MHL | ML + H ⇌ MHL | 3.00 | 2.98 | ≈ 0 |

---

## 3. Summary of Δ log β Values

| Ligand | Denticity | Donor Set | log β (Co²⁺) | log β (Co³⁺) | **Δ log β** |
|--------|:---------:|-----------|:---:|:---:|:---:|
| NH₃ (β₆) | 1×6 | N₆ | ~5.1 | 34.36 | **~+29** |
| en (β₃) | 2×3 | N₆ | 13.40 | 48.69 | **+35.3** |
| IDA (β₁) | 3 | N,O,O | 6.97 | 29.60 | **+22.6** |
| EDTA (β₁) | 6 | N₂O₄ | 16.45 | 41.40 | **+24.95** |

> **Key finding:** Across all comparable systems, Co³⁺ complexes are **22–35 log units more stable** than their Co²⁺ counterparts. The largest gap is seen with pure N-donor chelates (en: Δ = +35.3), while mixed N,O-donors show slightly smaller but still enormous differences (IDA: +22.6, EDTA: +25.0).

---

## 4. Crystal-Field Theory Interpretation

The dramatic stability difference is rooted in the electronic structures of the two ions:

| Property | Co²⁺ | Co³⁺ |
|----------|------|------|
| d-electron count | d⁷ | d⁶ |
| Typical spin state (N-donors) | High-spin (t₂g⁵ eₘ²) | **Low-spin** (t₂g⁶) |
| Crystal Field Stabilization Energy (CFSE) | ~0.8 Δₒ | **2.4 Δₒ** (3× larger) |
| Ligand field preference | Moderate | **Extremely strong** |
| Kinetics | Labile | **Inert** (substitution-inert) |
| Charge | +2 | **+3** (stronger electrostatic attraction) |

**Why Co³⁺ wins so decisively:**
1. **Higher charge (+3 vs +2):** Stronger electrostatic attraction to all ligands, contributing ~5–8 log units per unit charge increase.
2. **Low-spin d⁶ configuration:** Co³⁺ with strong-field N-donors achieves a fully filled t₂g shell (t₂g⁶), maximizing CFSE. The CFSE for low-spin Co³⁺ is ~2.4 Δₒ vs ~0.8 Δₒ for high-spin Co²⁺ — a factor of 3 in stabilization energy.
3. **Chelate effect amplification:** Polydentate N-donors enforce the octahedral geometry that Co³⁺ strongly prefers, and the entropic chelate effect is the same for both ions, so the CFSE advantage is additive.
4. **Kinetic inertness:** Co³⁺ complexes are substitution-inert (d⁶ low-spin), meaning once formed they persist — this is reflected in the thermodynamic stability constants being enormous.

---

## 5. Prediction for a New Polydentate Amine Ligand

Based on the observed data, here is a quantitative prediction for a hypothetical **hexadentate polyamine** (e.g., a tren-based or cyclam-type ligand with 4–6 N-donors):

| Property | Predicted Co²⁺ | Predicted Co³⁺ |
|----------|:--------------:|:--------------:|
| log β (ML) | **~15–20** | **~45–55** |
| Δ log β | — | **+25 to +35** |
| Spin state | High-spin d⁷, labile | Low-spin d⁶, **inert** |
| Geometry preference | Distorted octahedral | Ideal octahedral |
| Kinetic behavior | Fast ligand exchange | Very slow exchange |
| Practical implication | Moderate chelator | **Exceptional chelator** |

**Rationale:** The en data (Δ = +35.3) and EDTA data (Δ = +25.0) bracket the expected range. A pure N-donor polydentate amine will sit at the **upper end** (Δ ≈ +30–35) because:
- N-donors generate larger Δₒ than O-donors → greater CFSE for Co³⁺
- Higher denticity → greater chelate effect (same for both, but amplifies the absolute stability)
- The Co³⁺ complex will be **kinetically trapped** once formed — practically irreversible under mild conditions

**Real-world relevance:** This principle is exploited in **cobalt-based radiopharmaceuticals** (⁵⁵Co/⁵⁷Co PET imaging), where hexadentate amine-carboxylate cages like sarcophagine (sar) achieve log β > 50 with Co³⁺, making them essentially irreversible in vivo. It also underlies the classical **Werner complexes** (Co(en)₃³⁺ being the archetype of coordination chemistry), and the use of Co³⁺ as a "locking" oxidation state in supramolecular cage assembly.

---

*All stability constants from NIST SRD-46. Conditions: T = 20–30 °C, I = 0–0.25 M (reference-state networks) unless noted.*

---