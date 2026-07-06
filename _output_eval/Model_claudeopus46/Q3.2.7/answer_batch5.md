I have all the data needed. Let me compute the stepwise constants and present the final answer.

From the reference-state network (ref_eq_net_28241, T ≈ 25 °C, I ≈ 0 M), the **cumulative** log β values are:

- log β₁ = 4.10
- log β₂ = 7.40
- log β₃ = 10.20
- log β₄ = 12.30

The **stepwise** constants K_n are derived as K_n = β_n / β_{n−1}, so log K_n = log β_n − log β_{n−1}:

| Step | Equilibrium | log K_n | K_n |
|------|-------------|---------|-----|
| K₁ | Cu²⁺ + NH₃ ⇌ Cu(NH₃)²⁺ | 4.10 | 1.26 × 10⁴ |
| K₂ | Cu(NH₃)²⁺ + NH₃ ⇌ Cu(NH₃)₂²⁺ | 3.30 | 2.00 × 10³ |
| K₃ | Cu(NH₃)₂²⁺ + NH₃ ⇌ Cu(NH₃)₃²⁺ | 2.80 | 6.31 × 10² |
| K₄ | Cu(NH₃)₃²⁺ + NH₃ ⇌ Cu(NH₃)₄²⁺ | 2.10 | 1.26 × 10² |

*(Source: NIST SRD-46, 25 °C, I ≈ 0 M)*

## Do they decrease monotonically?

**Yes.** The stepwise log K values decrease steadily: **4.10 → 3.30 → 2.80 → 2.10**. Each successive ammonia binds less strongly than the previous one.

The decreases between steps are:

| Transition | Δ(log K) |
|------------|----------|
| K₁ → K₂ | −0.80 |
| K₂ → K₃ | −0.50 |
| K₃ → K₄ | −0.70 |

The drops are fairly uniform (0.5–0.8 log units per step), consistent with a **statistical effect** combined with increasing electrostatic repulsion among coordinated NH₃ ligands.

## What does this tell us about coordination geometry?

1. **Four-coordinate preference.** The SRD-46 database contains β definitions only up to Cu(NH₃)₄²⁺ — no Cu(NH₃)₅²⁺ or Cu(NH₃)₆²⁺ entries appear. This is the hallmark of Cu²⁺'s strong preference for **square-planar** (or tetragonally distorted octahedral) coordination. The four equatorial sites bind NH₃ tightly, while the two axial positions are elongated by the **Jahn–Teller distortion** characteristic of the d⁹ Cu²⁺ ion, making fifth and sixth ligand binding far too weak to be reliably measured.

2. **Smooth monotonic decrease.** The absence of any anomalous jump or plateau in the K₁–K₄ series indicates that all four equatorial sites are essentially equivalent — there is no geometric changeover (e.g., tetrahedral → octahedral) mid-sequence. The decrease is driven primarily by statistical factors (fewer vacant sites) and cumulative steric/electronic repulsion.

3. **Sharp cutoff at n = 4.** In contrast to ions like Ni²⁺ or Co²⁺, which readily form hexaammine complexes, Cu²⁺ stops at four. This is direct experimental evidence of the Jahn–Teller elongation: the axial Cu–N bonds would be so long (~2.6 Å vs. ~2.0 Å equatorial) that NH₃ binding there contributes negligible stability.

---