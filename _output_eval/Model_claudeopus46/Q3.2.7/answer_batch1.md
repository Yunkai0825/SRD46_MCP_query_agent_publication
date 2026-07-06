## Stepwise Formation Constants for Cu²⁺–Ammonia

Using a consistent dataset from **NIST SRD-46** at **25 °C, I ≈ 0 M** (ref_eq_net_28241), the cumulative (overall) formation constants are:

| Species | Equilibrium | log β |
|---------|-------------|-------|
| Cu(NH₃)²⁺ | M + L ⇌ ML | 4.1 |
| Cu(NH₃)₂²⁺ | M + 2L ⇌ ML₂ | 7.4 |
| Cu(NH₃)₃²⁺ | M + 3L ⇌ ML₃ | 10.2 |
| Cu(NH₃)₄²⁺ | M + 4L ⇌ ML₄ | 12.3 |

### Deriving Stepwise Constants (log Kₙ = log βₙ − log βₙ₋₁)

| Step | Reaction | log Kₙ | Kₙ |
|------|----------|--------|----|
| K₁ | Cu²⁺ + NH₃ ⇌ Cu(NH₃)²⁺ | **4.1** | 1.26 × 10⁴ |
| K₂ | Cu(NH₃)²⁺ + NH₃ ⇌ Cu(NH₃)₂²⁺ | **3.3** | 2.00 × 10³ |
| K₃ | Cu(NH₃)₂²⁺ + NH₃ ⇌ Cu(NH₃)₃²⁺ | **2.8** | 6.31 × 10² |
| K₄ | Cu(NH₃)₃²⁺ + NH₃ ⇌ Cu(NH₃)₄²⁺ | **2.1** | 1.26 × 10² |

### Do They Decrease Monotonically?

**Yes** — in this dataset the stepwise log K values decrease smoothly: **4.1 → 3.3 → 2.8 → 2.1**. Each successive ammonia binds more weakly than the previous one.

However, the pattern of the *differences* is noteworthy:

| Interval | Δ(log K) |
|----------|----------|
| K₁ → K₂ | −0.8 |
| K₂ → K₃ | −0.5 |
| K₃ → K₄ | −0.7 |

The drop from K₃ to K₄ (−0.7) is **larger** than the drop from K₂ to K₃ (−0.5). For a purely statistical effect on an octahedral ion, one would expect a more uniform decline. The relatively large drop at K₄ and the **absence of measurable K₅ and K₆** in the database are the key signatures.

### What This Tells Us About Coordination Geometry

Cu²⁺ is a d⁹ ion subject to a strong **Jahn–Teller distortion**, which elongates the two axial bonds of the octahedron while strengthening the four equatorial bonds. This means:

1. **The first four NH₃ molecules fill the equatorial plane** — these are the thermodynamically favorable positions, and all four stepwise constants are substantial (log K ≥ 2).
2. **The 5th and 6th coordination sites are axially elongated** — binding at these positions is so weak that K₅ and K₆ are essentially undetectable in aqueous solution (water competes effectively for these sites).
3. The result is an effective **square-planar-like coordination** of four ammonia ligands, even though Cu²⁺ nominally sits in a distorted octahedral environment with two loosely held axial water molecules.

This is a textbook illustration of how the Jahn–Teller effect in Cu(II) truncates the ammine series at four, giving the classic deep-blue **[Cu(NH₃)₄(H₂O)₂]²⁺** (tetraamminediaquacopper(II)) ion rather than a hexaammine complex.

*Source: NIST Standard Reference Database 46 (Critically Selected Stability Constants of Metal Complexes).*

---