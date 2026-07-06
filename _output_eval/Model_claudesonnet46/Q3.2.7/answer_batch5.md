I now have all the data I need. The overall β values (log β₁–β₄) at 25 °C, I ≈ 0 are: 4.02, 7.40, 10.20, 12.30. The stepwise log Kₙ values are derived as β_n − β_{n−1}.

---

## Cu²⁺–Ammonia Stepwise Formation Constants

*Source: NIST SRD-46, aqueous solution, 25 °C, I → 0*

### Overall β values (log β_n)

| n | Species | log β_n | β_def |
|---|---------|---------|-------|
| 1 | [Cu(NH₃)]²⁺ | 4.02 | beta_def_812 |
| 2 | [Cu(NH₃)₂]²⁺ | 7.40 | beta_def_840 |
| 3 | [Cu(NH₃)₃]²⁺ | 10.20 | beta_def_872 |
| 4 | [Cu(NH₃)₄]²⁺ | 12.30 | beta_def_894 |

### Derived Stepwise Constants (log Kₙ = log β_n − log β_{n−1})

| Step | Reaction | log Kₙ | Kₙ |
|------|----------|--------|-----|
| K₁ | Cu²⁺ + NH₃ → [Cu(NH₃)]²⁺ | **4.02** | ~10,500 |
| K₂ | [Cu(NH₃)]²⁺ + NH₃ → [Cu(NH₃)₂]²⁺ | **3.38** | ~2,400 |
| K₃ | [Cu(NH₃)₂]²⁺ + NH₃ → [Cu(NH₃)₃]²⁺ | **2.80** | ~630 |
| K₄ | [Cu(NH₃)₃]²⁺ + NH₃ → [Cu(NH₃)₄]²⁺ | **2.10** | ~126 |

---

### Do they decrease monotonically?

**Yes — K₁ > K₂ > K₃ > K₄, a clean monotonic decrease** (log K: 4.02 → 3.38 → 2.80 → 2.10).

The stepwise drop of ~0.6–0.7 log units per step is remarkably regular. This is broadly consistent with a **statistical effect**: as each NH₃ is added, there are fewer vacant sites for the next ligand and more steric/electrostatic repulsion among the coordinated amines.

---

### What does this tell us about coordination geometry?

Several important insights emerge:

1. **Square-planar preference (Jahn–Teller active Cu²⁺).** Cu²⁺ is a d⁹ ion subject to a strong **Jahn–Teller distortion**. The four equatorial positions are strongly bonding, while the two axial positions are elongated and much weaker. The series stops cleanly at **n = 4** in aqueous solution — a fifth and sixth NH₃ would have to occupy the axial sites, which are so weakly bound that water competes effectively. (Indeed, log K₅ and log K₆ for Cu²⁺–NH₃ are near zero or negative, a dramatic break from the smooth K₁–K₄ trend.)

2. **Thermodynamic confirmation.** The ΔH values retrieved (−20.1, −42.3, −62.3, −86.6 kJ/mol for β₁–β₄) show that each successive NH₃ binding is enthalpically favourable, but the ΔS values become increasingly negative (0, −14.2, −55.2 J/mol·K for β₂–β₄), reflecting the growing entropic cost of organising more ligands — consistent with a rigid, planar coordination shell.

3. **Contrast with octahedral metals.** For metals like Ni²⁺ or Co²⁺ (no Jahn–Teller distortion), the stepwise series extends smoothly to K₆. The **sharp cutoff at K₄** for Cu²⁺ is a hallmark of its distorted geometry and is one of the clearest experimental signatures of the Jahn–Teller effect in coordination chemistry.

> **In short:** The monotonic K₁ > K₂ > K₃ > K₄ trend reflects normal statistical/steric effects within the equatorial plane of a square-planar Cu²⁺ complex, while the absence of stable K₅/K₆ directly reveals the Jahn–Teller elongation of the axial bonds.

*Data source: NIST SRD-46 (vlm_173242–173283), 25 °C, I → 0 M.*

---