I have all the data needed. Let me compute the stepwise constants and present the final answer.

From the reference-state network (ref_eq_net_28241, T ≈ 25 °C, I ≈ 0 M), the **cumulative** log β values are:

- log β₁ = 4.1
- log β₂ = 7.4
- log β₃ = 10.2
- log β₄ = 12.3

The **stepwise** log K values are:

- log K₁ = log β₁ = 4.1
- log K₂ = log β₂ − log β₁ = 7.4 − 4.1 = 3.3
- log K₃ = log β₃ − log β₂ = 10.2 − 7.4 = 2.8
- log K₄ = log β₄ − log β₃ = 12.3 − 10.2 = 2.1

---

## Cu²⁺–Ammonia Stepwise Formation Constants (25 °C, I ≈ 0 M)

| Step | Equilibrium | log Kₙ | Kₙ | Δ(log K) from previous |
|------|-------------|--------|----|------------------------|
| K₁ | Cu²⁺ + NH₃ ⇌ Cu(NH₃)²⁺ | 4.1 | ~1.3 × 10⁴ | — |
| K₂ | Cu(NH₃)²⁺ + NH₃ ⇌ Cu(NH₃)₂²⁺ | 3.3 | ~2.0 × 10³ | −0.8 |
| K₃ | Cu(NH₃)₂²⁺ + NH₃ ⇌ Cu(NH₃)₃²⁺ | 2.8 | ~6.3 × 10² | −0.5 |
| K₄ | Cu(NH₃)₃²⁺ + NH₃ ⇌ Cu(NH₃)₄²⁺ | 2.1 | ~1.3 × 10² | −0.7 |

*Source: NIST SRD-46, reference equilibrium network ref_eq_net_28241.*

### Do they decrease monotonically?

**Yes.** The stepwise constants decrease smoothly: log K₁ > log K₂ > log K₃ > log K₄ (4.1 → 3.3 → 2.8 → 2.1). Each successive ammonia binds more weakly than the last.

### What does this tell us about coordination geometry?

1. **Jahn–Teller distortion governs the pattern.** Cu²⁺ is a d⁹ ion and undergoes a strong Jahn–Teller elongation of the octahedral geometry, producing four short equatorial bonds and two long axial bonds. The first four NH₃ molecules fill the four equatorial positions — all relatively strong — so all four stepwise constants remain substantial (log K > 2).

2. **No anomalous "step" between K₂ and K₃.** In a regular octahedron one might expect a statistical drop, but for Cu²⁺ the drop from K₁ to K₄ is gradual and monotonic. This is consistent with all four ligands entering equivalent (or near-equivalent) equatorial sites. The steady decline is largely statistical — each successive step has fewer available sites and increased ligand–ligand repulsion.

3. **Why only four?** SRD-46 lists no β₅ or β₆ for this system. The two axial positions are so elongated (Jahn–Teller) that fifth and sixth NH₃ molecules bind too weakly to be measured as discrete species in aqueous solution. This is the classic signature of **tetragonally distorted (4+2) coordination** effectively behaving as square-planar for strong-field ligands like ammonia.

4. **Thermodynamic confirmation.** The enthalpy data in SRD-46 show increasingly negative cumulative ΔH values but also increasingly negative ΔS, reflecting growing steric crowding and loss of translational freedom — consistent with packing four NH₃ into the equatorial plane before the energetic cost of axial binding becomes prohibitive.

In summary, the monotonic decrease of K₁ through K₄ — and the absence of K₅/K₆ — is a textbook fingerprint of Cu²⁺'s Jahn–Teller-distorted coordination: a strong preference for four equatorial ligands with effectively no binding at the elongated axial sites.

---