## Zn²⁺–EDTA Stability Constants vs. Ionic Strength

### Data from SRD-46 (25 °C, β₁ for [ML]/[M][L])

| vlm_id | log K | I (mol/L) | √I |
|--------|-------|-----------|----|
| vlm_108710 | 18.0 | 0.00 | 0.000 |
| vlm_108707 | 16.5 | 0.10 | 0.316 |
| vlm_108708 | 15.7 | 0.50 | 0.707 |
| vlm_108709 | 15.7 | 1.00 | 1.000 |

*(vlm_108711 and vlm_108712 are ΔH and ΔS entries at I = 0.1 M, not log K values — excluded from the fit.)*

---

### Linear Extrapolation to I = 0

Using the three non-zero ionic strength points (I = 0.1, 0.5, 1.0 M) and fitting log K vs. √I:

| Point | √I | log K |
|-------|----|-------|
| I = 0.10 | 0.316 | 16.5 |
| I = 0.50 | 0.707 | 15.7 |
| I = 1.00 | 1.000 | 15.7 |

A simple linear regression of log K on √I gives:

- **Slope ≈ −1.15** (log K decreases as ionic strength rises)
- **Intercept (extrapolated log K° at I = 0) ≈ 16.9**

> Extrapolated log K° ≈ **16.9** at I = 0, 25 °C

---

### Comparison with the Database I = 0 Value

| Source | log K | I (mol/L) | T (°C) |
|--------|-------|-----------|--------|
| Database (vlm_108710) | **18.0** | 0.00 | 25 |
| Linear extrapolation from I = 0.1–1.0 M | **~16.9** | 0 (extrap.) | 25 |
| Discrepancy | **~1.1 log units** | — | — |

---

### Chemistry Insight

The **~1.1 log unit gap** between the extrapolated value (~16.9) and the directly measured I = 0 value (18.0) is chemically significant and expected. EDTA⁴⁻ carries a high charge (−4), so the Zn²⁺–EDTA complex formation involves a large charge neutralization: Zn²⁺ + EDTA⁴⁻ → [ZnEDTA]²⁻. The Debye–Hückel / Davies equation predicts a **strong ionic-strength dependence** for such highly charged reactants — the activity coefficients of Zn²⁺ and EDTA⁴⁻ are suppressed at higher I, artificially lowering the apparent log K. A simple linear fit in √I underestimates the curvature at low I, which explains why the extrapolation falls short of the true thermodynamic value.

The database value of **log K° = 18.0** at I = 0 is the thermodynamic stability constant and is the most reliable reference for Zn²⁺–EDTA. This value is consistent with the well-known exceptional stability of EDTA complexes with divalent transition metals, driven by the hexadentate chelate effect (four carboxylate + two amine donors).

---

*Source: NIST SRD-46 (metal_208 = Zn²⁺, ligand_6277 = EDTA, beta_def_812 = [ML]/[M][L])*

---