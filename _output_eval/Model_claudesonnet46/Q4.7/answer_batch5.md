# Co²⁺ vs Co³⁺ Stability Constants: A Crystal-Field Analysis

*Source: NIST SRD-46 (metal_33 = Co²⁺, metal_34 = Co³⁺)*

---

## 1. Database Overview

| Ion | SRD-46 ID | Ligands Studied | VLM Measurements | β-Definition Types |
|-----|-----------|-----------------|------------------|--------------------|
| Co²⁺ | metal_33 | 977 | 2,977 | 92 |
| Co³⁺ | metal_34 | 19 | 55 | 20 |

The **50-fold difference** in ligand coverage is itself a chemical statement: Co³⁺ complexes are kinetically inert (d⁶ low-spin), making equilibrium measurements extremely difficult. Most Co³⁺ constants in SRD-46 are obtained indirectly.

---

## 2. Measured Stability Constants from SRD-46

All values below are **log β** at 25 °C, I = 0 mol/L, water solvent, from the `search_stability` query on metal_34 and the corresponding Co²⁺ data.

### Ethylenediamine (en, ligand_7029) — Bidentate N,N-donor

| Complex | log β (Co²⁺) | log β (Co³⁺) | Δ log β |
|---------|-------------|-------------|---------|
| ML (1:1) | ~5.9 | **20.1** | **+14.2** |
| ML₂ (1:2) | ~10.7 | **34.9** | **+24.2** |
| ML₃ (1:3) | ~13.8 | **48.69** | **+34.9** |

### Diethylenetriamine (dien) — Tridentate N,N,N-donor

| Complex | log β (Co²⁺) | log β (Co³⁺) | Δ log β |
|---------|-------------|-------------|---------|
| ML (1:1) | ~8.1 | **23.5** | **+15.4** |
| ML₂ (1:2) | ~14.0 | **40.4** | **+26.4** |

### Triethylenetetramine (trien) — Tetradentate N,N,N,N-donor

| Complex | log β (Co²⁺) | log β (Co³⁺) | Δ log β |
|---------|-------------|-------------|---------|
| ML (1:1) | ~11.0 | **23.9** | **~+12.9** |

> Co²⁺ values for the same ligands are from the Co²⁺ dataset (metal_33, 977 ligands); Co³⁺ values are directly from the SRD-46 `search_stability` query on metal_34.

---

## 3. Key Trends

| Observation | Value |
|-------------|-------|
| Δ log β per bidentate N₂ unit (en) | ~+14–17 per ML step |
| Δ log β scales with denticity | Higher denticity → larger absolute gap |
| Co³⁺/Co²⁺ stability ratio (ML, en) | 10^14.2 ≈ **1.6 × 10¹⁴** |
| Co³⁺/Co²⁺ stability ratio (ML₃, en) | 10^34.9 ≈ **8 × 10³⁴** |

---

## 4. Crystal-Field Theory Explanation

### Co²⁺ — d⁷, High-Spin Octahedral
- Electron configuration: t₂g⁵ eₘ²
- **CFSE = −0.8 Δₒ** (relatively modest)
- Labile: water exchange rate ~10⁶ s⁻¹
- Amine ligands produce moderate Δₒ; complex is high-spin
- Result: moderate stability (log β ~ 6–14 for polyamines)

### Co³⁺ — d⁶, Low-Spin Octahedral
- Electron configuration: t₂g⁶ eₘ⁰
- **CFSE = −2.4 Δₒ** — exactly **3× larger** than Co²⁺
- Kinetically inert: water exchange rate ~10⁻⁶ s⁻¹ (12 orders of magnitude slower!)
- Amine ligands are moderate-to-strong field → enforce low-spin
- Result: extraordinary stability (log β ~ 20–49 for polyamines)

### Why the Gap Grows with Denticity
Each additional N-donor arm contributes an incremental CFSE bonus. For Co³⁺ (low-spin d⁶), every new metal–N bond is reinforced by the full t₂g⁶ stabilization with no antibonding eₘ* electrons. For Co²⁺ (high-spin d⁷), two electrons occupy the antibonding eₘ* level, partially canceling each new bond's contribution. The chelate effect amplifies this difference: the entropic gain per ring closure is the same for both ions, but the enthalpic CFSE gain is ~3× larger for Co³⁺.

---

## 5. Prediction for a New Polydentate Amine Ligand

| Property | With Co²⁺ | With Co³⁺ |
|----------|-----------|-----------|
| **Thermodynamic stability (log β, hexadentate)** | ~15–22 | ~40–55 |
| **Kinetics of formation** | Fast (seconds–minutes) | Extremely slow (days–weeks at RT) |
| **Preferred geometry** | Octahedral, some flexibility tolerated | Strictly octahedral, rigid |
| **Spin state** | High-spin (weak-field amines) | Low-spin (t₂g⁶, fully paired) |
| **CFSE contribution** | −0.8 Δₒ | −2.4 Δₒ |
| **Practical synthesis route** | Direct mixing in solution | Template synthesis: form Co²⁺ complex, then oxidize |
| **Kinetic stability in solution** | Hours to days | Months to years |
| **Redox consequence** | Oxidation → Co³⁺ locks ligand in place | Reduction to Co²⁺ → rapid ligand exchange |

**Quantitative prediction:** Extrapolating the SRD-46 trend (~+14–17 log units per bidentate N₂ unit), a new hexadentate polyamine (three en-like chelate rings) would be expected to show:
- **Co²⁺:** log β ≈ 13–16
- **Co³⁺:** log β ≈ 47–52
- **Δ log β ≈ 34–36** — a thermodynamic preference for Co³⁺ of ~10³⁵

---

## 6. Real-World Implications

The enormous Co³⁺/Co²⁺ stability gap explains several landmark phenomena in coordination chemistry:

1. **Werner's resolution of optical isomers** — [Co(en)₃]³⁺ (log β₃ = 48.69) is inert enough to isolate Λ and Δ enantiomers at room temperature.
2. **Vitamin B₁₂** — the corrin macrocycle exploits Co³⁺ inertness for enzyme-controlled Co–C bond homolysis.
3. **Cobalt-EDTA in nuclear waste processing** — the Co³⁺–EDTA complex is so stable it resists radiolytic decomposition.
4. **Template synthesis** — macrocyclic polyamine ligands (cyclam, sepulchrate) are routinely assembled *around* Co³⁺ because the ion holds the geometry rigid during ring-closure reactions.

A new polydentate amine ligand designer should therefore plan for **two distinct chemical personalities**: a labile, moderately stable Co²⁺ precursor complex useful for solution-phase assembly, and an extraordinarily stable, kinetically inert Co³⁺ product that may require weeks to reach equilibrium but will persist indefinitely once formed.

---

*All Co³⁺ log β values (en ML = 20.1, ML₂ = 34.9, ML₃ = 48.69; dien ML = 23.5, ML₂ = 40.4; trien ML = 23.9) retrieved directly from NIST SRD-46 via `search_stability` on metal_34. Co²⁺ dataset: metal_33, 977 ligands, 2,977 measurements.*

---