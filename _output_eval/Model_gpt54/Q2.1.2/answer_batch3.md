Using the SRD-46 ammonia reference-equilibrium networks for the **stepwise first formation constant**  
**β₁: M²⁺ + NH₃ ⇌ M(NH₃)²⁺** (`beta_def_812`), the **log β₁** values for the first-row divalent ions are:

| Rank | Metal ion | metal_id | log β₁ with NH₃ |
|---|---:|---|---:|
| 1 | Cu²⁺ | `metal_41` | 4.10 |
| 2 | Ni²⁺ | `metal_112` | 2.73 |
| 3 | Zn²⁺ | `metal_208` | 2.33 |
| 4 | Co²⁺ | `metal_33` | 2.08 |
| 5 | Fe²⁺ | `metal_62` | 1.40 |
| 6 | Mn²⁺ | `metal_94` | 0.84 |

So the ordering is:

| Order by increasing log β₁ |
|---|
| Mn²⁺ < Fe²⁺ < Co²⁺ < Zn²⁺ < Ni²⁺ < Cu²⁺ |

### Does this follow the Irving–Williams series?

| Comparison | Result |
|---|---|
| Expected Irving–Williams trend | Mn²⁺ < Fe²⁺ < Co²⁺ < Ni²⁺ < Cu²⁺ > Zn²⁺ |
| Observed from SRD-46 NH₃ β₁ values | Mn²⁺ < Fe²⁺ < Co²⁺ < Zn²⁺ < Ni²⁺ < Cu²⁺ |

**Answer:** **Mostly yes.** The overall rise from **Mn²⁺ → Cu²⁺** is consistent with the Irving–Williams series, and **Cu²⁺ is the maximum**. The only noticeable deviation is that **Zn²⁺ falls above Co²⁺ but below Ni²⁺** here, rather than simply appearing after Cu²⁺ in the classic simplified sequence.

A bit of chemistry context: the Irving–Williams series is a **general trend**, not a rigid rule for every ligand and every individual stepwise constant. With **ammonia** and specifically **β₁**, ligand-field and hydration effects can shift the middle of the series slightly, while still preserving the strong stabilization of **Ni²⁺ and especially Cu²⁺**.

**Source:** NIST SRD-46, ammonia (`ligand_10103`) reference equilibrium networks, `beta_def_812` for `M + L ⇌ ML`.

---