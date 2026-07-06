## Irving–Williams Series: M²⁺ + NH₃ Log β₁ Rankings

Here is the complete picture from SRD-46 data for the aqueous reaction **M²⁺ + NH₃ ⇌ [M(NH₃)]²⁺** at **25 °C**, all in water.

---

### Log β₁ Values at 25 °C (Aqueous, [ML]/[M][L])

| Metal | log β₁ (I → 0) | log β₁ (I = 0.1 M) | log β₁ (I = 1.0 M) |
|-------|:--------------:|:-------------------:|:-------------------:|
| **Cu²⁺** | **4.31** | 4.25 | 4.04 |
| **Ni²⁺** | **2.80** | 2.72 | 2.67 |
| **Zn²⁺** | **2.37** | 2.31 | 2.21 |
| **Co²⁺** | **2.11** | 2.05 | 2.10 |
| **Mn²⁺** | **1.00** | 0.93 | — |
| **Fe²⁺** | *not found* | — | — |

> **Note on Fe²⁺:** No log β₁(NH₃) data for Fe²⁺ were returned by SRD-46. This is chemically understandable — Fe²⁺ is readily oxidised to Fe³⁺ in ammoniacal solutions, making reliable equilibrium measurements difficult, and such data may simply be absent from the critically selected database.

---

### Ranking (highest → lowest log β₁, thermodynamic I → 0)

| Rank | Metal | log β₁ (I → 0) |
|------|-------|:--------------:|
| 1 | Cu²⁺ | 4.31 |
| 2 | Ni²⁺ | 2.80 |
| 3 | Zn²⁺ | 2.37 |
| 4 | Co²⁺ | 2.11 |
| 5 | Mn²⁺ | 1.00 |
| — | Fe²⁺ | no data |

---

### Does It Follow the Irving–Williams Series?

**Yes — the observed data are fully consistent with the Irving–Williams series.**

The canonical Irving–Williams order is:
> **Mn²⁺ < Fe²⁺ < Co²⁺ < Ni²⁺ < Cu²⁺ > Zn²⁺**

Checking each position against the SRD-46 data:

| Criterion | Expected | Observed | Consistent? |
|-----------|----------|----------|:-----------:|
| Mn²⁺ is weakest | Mn²⁺ lowest | log β₁ = 1.00 (lowest) | ✅ |
| Co²⁺ > Mn²⁺ | Co²⁺ > Mn²⁺ | 2.11 > 1.00 | ✅ |
| Ni²⁺ > Co²⁺ | Ni²⁺ > Co²⁺ | 2.80 > 2.11 | ✅ |
| Cu²⁺ is the peak | Cu²⁺ highest | 4.31 (highest by far) | ✅ |
| Zn²⁺ < Cu²⁺ | Zn²⁺ drops off | 2.37 < 4.31 | ✅ |
| Zn²⁺ < Ni²⁺ | Zn²⁺ < Ni²⁺ | 2.37 < 2.80 | ✅ |
| Zn²⁺ > Co²⁺ | Zn²⁺ > Co²⁺ | 2.37 > 2.11 | ✅ |

Every testable relationship matches the Irving–Williams prediction perfectly.

---

### Chemistry Insight

1. **Cu²⁺ dominates by a wide margin** (log β₁ = 4.31, nearly 1.5 log units above Ni²⁺). This is the hallmark of the **Jahn–Teller effect**: the d⁹ configuration distorts the octahedral coordination sphere, lowering the energy of the equatorial bonds and providing extra stabilisation for nitrogen donors. Cu²⁺ is consistently the strongest Lewis acid toward N-donor ligands across the entire first-row series.

2. **Zn²⁺ sits between Co²⁺ and Ni²⁺**, not at the bottom as its filled d¹⁰ shell (zero crystal-field stabilisation energy) might naively suggest. Its relatively small ionic radius and high effective nuclear charge give it a modest but real advantage over Co²⁺ for the first ammine step, even without any CFSE contribution.

3. **Mn²⁺ is the weakest binder** (log β₁ = 1.00), consistent with its half-filled d⁵ high-spin configuration (zero CFSE), the largest ionic radius in the series, and the lowest effective nuclear charge — all conspiring to minimise electrostatic and covalent attraction toward NH₃.

*Source: NIST SRD-46 (Critically Selected Stability Constants of Metal Complexes), aqueous data at 25 °C.*

---