## Zn²⁺–EDTA Stability Constant: Ionic-Strength Trend & Extrapolation to I = 0

### Data from NIST SRD-46

All measurements are at **25 °C** for the reaction **[M] + [L] ⇌ [ML]** (beta_def_812):

| vlm_id | Type | log K | I (mol/L) |
|--------|------|------:|----------:|
| vlm_108710 | log K | **18.0** | **0** |
| vlm_108707 | log K | 16.5 | 0.1 |
| vlm_108708 | log K | 15.7 | 0.5 |
| vlm_108709 | log K | 15.7 | 1.0 |

### Extrapolation to I = 0

Using the three finite-ionic-strength points and a simple Debye–Hückel-type linear fit of log K vs. √I:

| I (M) | √I | log K |
|------:|-----:|------:|
| 0.1 | 0.316 | 16.5 |
| 0.5 | 0.707 | 15.7 |
| 1.0 | 1.000 | 15.7 |

A least-squares line **log K = a − b·√I** through these three points gives:

- Slope (b) ≈ 1.03
- Intercept (a) ≈ **16.9**

So the **extrapolated log K at I = 0 ≈ 16.9**.

### Comparison with the Database I = 0 Value

The SRD-46 database contains a direct entry at I = 0:

| Source | log K | I (M) |
|--------|------:|------:|
| Database (vlm_108710) | **18.0** | 0 |
| Linear extrapolation | **~16.9** | 0 |
| **Difference** | **~1.1 log units** | — |

### Chemistry Insight

The discrepancy of ~1.1 log units is expected and instructive. A simple linear fit in √I is a crude approximation — the Debye–Hückel limiting law applies rigorously only at very low ionic strengths (I < 0.01 M), and the Zn²⁺–EDTA⁴⁻ system involves highly charged species (charge product z₊z₋ = −8), making activity-coefficient corrections very large and strongly nonlinear. The database I = 0 value of **log K = 18.0** likely represents a more rigorous extrapolation (e.g., using SIT or extended Debye–Hückel with ion-specific parameters) or a critically evaluated thermodynamic value. The steep drop from 18.0 → 16.5 between I = 0 and I = 0.1 M — a 1.5 log-unit decrease — is characteristic of such high-charge-product equilibria, where even modest ionic strengths dramatically screen electrostatic attraction and lower the apparent stability constant.

**Bottom line:** The database's I = 0 value of **log K = 18.0** is consistent with the observed trend but cannot be accurately recovered from a naive linear extrapolation of finite-I data. Proper thermodynamic extrapolation methods are essential for systems with large charge products.

*Source: NIST Standard Reference Database 46 (Critically Selected Stability Constants of Metal Complexes)*

---