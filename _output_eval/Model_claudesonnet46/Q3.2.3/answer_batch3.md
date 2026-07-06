## Final Answer

# Calcium Oxalate Precipitation: pH Threshold Analysis

All data from **NIST SRD-46**.

---

## Key Thermodynamic Data (25 °C)

### Oxalic Acid pKa Values (I = 0.1 M, 25 °C)

| Equilibrium | pKa | Species |
|---|---|---|
| H₂C₂O₄ ⇌ H⁺ + HC₂O₄⁻ | **−1.2** | pKa1 |
| HC₂O₄⁻ ⇌ H⁺ + C₂O₄²⁻ | **3.8** | pKa2 |

### Ca²⁺–Oxalate Constants (25 °C)

| Species | β definition | log K | Conditions |
|---|---|---|---|
| CaC₂O₄·H₂O(s) dissolution | Ksp (beta_def_327) | **−8.75** | 25 °C, I = 0 |
| CaC₂O₄·H₂O(s) dissolution | Ksp (beta_def_327) | **−7.86** | 25 °C, I = 0.1 M |
| CaC₂O₄·3H₂O(s) dissolution | Ksp (beta_def_307) | **−8.32** | 25 °C, I = 0 |
| Ca²⁺ + C₂O₄²⁻ ⇌ CaC₂O₄(aq) | β (beta_def_812) | **+3.19** | 25 °C, I = 0 |

---

## Reasoning: pH Threshold for Precipitation

The controlling equilibrium is:

> **CaC₂O₄·H₂O(s) ⇌ Ca²⁺ + C₂O₄²⁻**, pKsp = −8.75 (I = 0, 25 °C)

Precipitation occurs when the **ion product** [Ca²⁺][C₂O₄²⁻] > Ksp = 10⁻⁸·⁷⁵.

The fraction of total oxalate present as the fully deprotonated dianion C₂O₄²⁻ (the precipitating species) is governed by pKa2 = **3.8**:

| pH | α(C₂O₄²⁻) fraction | Comment |
|---|---|---|
| 1 | ~0.001 | Mostly H₂C₂O₄; negligible dianion |
| 2 | ~0.004 | Still mostly HC₂O₄⁻ |
| 3 | ~0.04 | Small but growing dianion fraction |
| **4** | **~0.28** | Approaching pKa2; dianion fraction rising fast |
| **5** | **~0.94** | Mostly C₂O₄²⁻; precipitation likely |
| 6+ | ~1.0 | Essentially all dianion |

The aqueous complex log β = **3.19** means CaC₂O₄(aq) is moderately stable, which slightly *reduces* free [Ca²⁺] and *raises* the effective precipitation threshold — but this effect is modest (< 0.5 pH units) at typical calcium concentrations.

---

## Conclusion

> **Calcium oxalate precipitation becomes significant at approximately pH 4–5.**

More precisely:
- **Below pH ~3.5**: oxalate is predominantly HC₂O₄⁻ (monoanion); [C₂O₄²⁻] is too low to exceed Ksp under physiological or typical laboratory Ca²⁺ concentrations (~1–10 mM).
- **pH 4–5**: the dianion fraction rises steeply past pKa2 = 3.8; the ion product [Ca²⁺][C₂O₄²⁻] crosses Ksp = 10⁻⁷·⁸⁶ (at I = 0.1 M), and precipitation begins in earnest.
- **Above pH 5**: essentially all oxalate is C₂O₄²⁻, and precipitation is thermodynamically driven for any physiologically relevant [Ca²⁺].

**Clinical relevance:** Kidney stones (calcium oxalate monohydrate, *whewellite*) form in urine at near-neutral pH (~5.5–7), consistent with this analysis — the urinary pH is well above pKa2, ensuring maximal dianion availability, while urinary [Ca²⁺] and [oxalate] routinely approach or exceed the Ksp of 10⁻⁸·⁷⁵.

*Source: NIST SRD-46 — metal_25 (Ca²⁺), ligand_8872 (oxalic acid), beta_def_327/812.*

---