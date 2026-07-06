I have all the data needed. The SRD-46 database returns **overall β values** (M + nL ⇌ MLₙ), not stepwise K values directly — I need to derive the stepwise Kₙ from the cumulative log β values. Let me do that now using the I = 0 (infinite dilution) dataset, which is the cleanest reference point.

---

## Cu²⁺–Ammonia Stepwise Constants K₁–K₄

### Deriving Stepwise log Kₙ from Cumulative log βₙ (25 °C, I = 0)

The database reports **cumulative** log β values (M + nNH₃ ⇌ [Cu(NH₃)ₙ]²⁺):

| n | log βₙ (I = 0, 25 °C) | beta_def |
|---|----------------------|----------|
| 1 | 4.02 | beta_def_812 |
| 2 | 7.40 | beta_def_840 |
| 3 | 10.20 | beta_def_872 |
| 4 | 12.30 | beta_def_894 |

Stepwise log Kₙ = log βₙ − log βₙ₋₁ (with log β₀ = 0):

| Step | Reaction | log Kₙ | Kₙ |
|------|----------|--------|----|
| K₁ | Cu²⁺ + NH₃ ⇌ [Cu(NH₃)]²⁺ | **4.02** | ~10,500 |
| K₂ | [Cu(NH₃)]²⁺ + NH₃ ⇌ [Cu(NH₃)₂]²⁺ | **3.38** | ~2,400 |
| K₃ | [Cu(NH₃)₂]²⁺ + NH₃ ⇌ [Cu(NH₃)₃]²⁺ | **2.80** | ~630 |
| K₄ | [Cu(NH₃)₃]²⁺ + NH₃ ⇌ [Cu(NH₃)₄]²⁺ | **2.10** | ~126 |

> *Source: NIST SRD-46, metal_41 (Cu²⁺) + ligand_10103 (NH₃), vlm_173246/173258/173270/173282*

---

### Do They Decrease Monotonically?

**Yes — strictly and significantly.** Each successive log K drops by ~0.6–0.7 log units:

| Transition | Δ log K |
|------------|---------|
| K₁ → K₂ | −0.64 |
| K₂ → K₃ | −0.58 |
| K₃ → K₄ | −0.70 |

The decrease is remarkably regular, consistent with a **purely statistical effect** (fewer available coordination sites at each step) combined with increasing steric/electrostatic repulsion among bound NH₃ ligands.

---

### What Does This Tell Us About Coordination Geometry?

The smooth, monotonic decline through K₄ — with **no anomalous drop at K₅ or K₆** — is a classic fingerprint of the **Jahn–Teller distorted octahedral geometry** of Cu²⁺:

1. **Cu²⁺ is a d⁹ ion** subject to Jahn–Teller distortion. In an octahedral field, the two axial bonds are significantly elongated (~2.3 Å) compared to the four equatorial bonds (~2.0 Å).

2. **K₁–K₄ fill the four equatorial sites**, which bind NH₃ strongly and with similar affinity — hence the smooth, moderate decline.

3. **K₅ and K₆ are dramatically smaller** (log K₅ ≈ −0.5 in many studies, effectively negligible), because the axial positions are so weakly binding that [Cu(NH₃)₅]²⁺ and [Cu(NH₃)₆]²⁺ are essentially not formed in aqueous solution. Water outcompetes NH₃ for the axial sites.

4. The **effective coordination number of Cu²⁺ with NH₃ is 4**, giving a square-planar or tetragonally elongated octahedral geometry — a direct consequence of the Jahn–Teller effect.

> **In short:** The monotonic K₁ > K₂ > K₃ > K₄ sequence with a sharp cliff at K₅ is one of the most elegant experimental demonstrations of Jahn–Teller distortion in coordination chemistry, encoded directly in the thermodynamic stability constants.

---