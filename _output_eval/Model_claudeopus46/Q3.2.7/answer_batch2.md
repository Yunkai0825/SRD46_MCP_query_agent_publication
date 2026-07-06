I have all the data needed. Let me compile the final answer using the reference-state network (ref_eq_net_28241) at ~25 °C and I ≈ 0 M, which provides a self-consistent set of cumulative log β values.

## Cu²⁺–Ammonia Stepwise Constants (K₁–K₄)

**Source:** NIST SRD-46, reference network ref_eq_net_28241 (T ≈ 25 °C, I ≈ 0 M, aqueous)

### Cumulative constants (log β)

| Equilibrium | β definition | log β |
|---|---|---|
| Cu²⁺ + NH₃ ⇌ Cu(NH₃)²⁺ | β₁ | 4.1 |
| Cu²⁺ + 2 NH₃ ⇌ Cu(NH₃)₂²⁺ | β₂ | 7.4 |
| Cu²⁺ + 3 NH₃ ⇌ Cu(NH₃)₃²⁺ | β₃ | 10.2 |
| Cu²⁺ + 4 NH₃ ⇌ Cu(NH₃)₄²⁺ | β₄ | 12.3 |

### Derived stepwise constants (log Kₙ = log βₙ − log βₙ₋₁)

| Step | Reaction | log Kₙ | Kₙ |
|---|---|---|---|
| K₁ | Cu²⁺ + NH₃ → Cu(NH₃)²⁺ | **4.1** | 1.26 × 10⁴ |
| K₂ | Cu(NH₃)²⁺ + NH₃ → Cu(NH₃)₂²⁺ | **3.3** | 2.00 × 10³ |
| K₃ | Cu(NH₃)₂²⁺ + NH₃ → Cu(NH₃)₃²⁺ | **2.8** | 6.31 × 10² |
| K₄ | Cu(NH₃)₃²⁺ + NH₃ → Cu(NH₃)₄²⁺ | **2.1** | 1.26 × 10² |

### Do they decrease monotonically?

**Yes.** The stepwise log K values follow a strictly decreasing sequence:

> log K₁ (4.1) > log K₂ (3.3) > log K₃ (2.8) > log K₄ (2.1)

Each successive ammonia binds more weakly, which is the expected statistical effect (fewer vacant sites, increasing ligand–ligand repulsion). The trend holds across all ionic strengths in the database (I = 0–3 M).

### What does this tell us about coordination geometry?

1. **Square-planar (or tetragonally distorted octahedral) core.** Cu²⁺ is a d⁹ ion subject to a strong **Jahn–Teller distortion** that elongates the axial bonds of an octahedron. The four equatorial positions are strongly bonding; the two axial sites are so weakened that NH₃ binding effectively stops at n = 4. Notably, **no β₅ or β₆ entries exist** in SRD-46 for this system, confirming that the 5th and 6th ammonia molecules do not bind with measurable stability under normal aqueous conditions.

2. **The drop from K₃ to K₄ (Δlog K = 0.7) is the largest single step-to-step decrease**, suggesting that filling the fourth equatorial site encounters the greatest steric and electronic resistance. This is consistent with the square-planar Cu(NH₃)₄²⁺ being the terminal, thermodynamically dominant species — the iconic deep-blue "cuprammine" complex used as a qualitative test for Cu²⁺ in analytical chemistry.

3. **Monotonic decrease without anomalies** rules out a change in coordination number or spin state mid-series (unlike, e.g., some Co²⁺ or Ni²⁺ amine systems where geometry switches can cause non-monotonic steps).

---