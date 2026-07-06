# Co²⁺ vs Co³⁺ Stability Constants: A Crystal-Field Perspective

*Source: NIST SRD-46 | All data at 25 °C, aqueous solution*

---

## 1. Overlapping Ligand Systems in SRD-46

Five ligands appear in the database for **both** Co²⁺ (metal_33, 977 ligands) and Co³⁺ (metal_34, 19 ligands):

| Ligand | Denticity | Donor Type |
|--------|-----------|------------|
| Ammonia (NH₃) | 1 | N-monodentate |
| Ethylenediamine (en) | 2 | N,N-bidentate |
| IDA (iminodiacetate) | 3 | N,O,O-tridentate |
| NTA (nitrilotriacetate) | 4 | N,O,O,O-tetradentate |
| EDTA | 6 | N,N,O,O,O,O-hexadentate |

---

## 2. Head-to-Head Stability Constant Comparison

All values at 25 °C, aqueous, matched ionic strength where possible.

### Ammonia (monodentate, I = 2.0 M)

| Species | Co²⁺ log β | Co³⁺ log β | Δ log β (Co³⁺ − Co²⁺) |
|---------|:----------:|:----------:|:----------------------:|
| ML₁ | 2.11 | — | — |
| ML₂ | 3.74 | — | — |
| ML₃ | 4.79 | — | — |
| ML₄ | 5.55 | 30.76 | **+25.2** |
| ML₅ | 5.73 | 35.16 | **+29.4** |
| ML₆ | — | 35.16 | — |

### Ethylenediamine / en (bidentate, I = 0.5–1.0 M)

| Species | Co²⁺ log β | Co³⁺ log β | Δ log β |
|---------|:----------:|:----------:|:-------:|
| ML₁ (en) | 5.89 | — | — |
| ML₂ (en₂) | 10.72 | — | — |
| ML₃ (en₃) | **13.94** | **47.68** | **+33.7** |

### IDA — iminodiacetate (tridentate, I = 0.1 M)

| Species | Co²⁺ log β | Co³⁺ log β | Δ log β |
|---------|:----------:|:----------:|:-------:|
| ML₁ | **7.05** | **14.0** | **+6.95** |
| ML₂ | 11.09 | — | — |

### NTA — nitrilotriacetate (tetradentate, I = 0.1 M)

| Species | Co²⁺ log β | Co³⁺ log β | Δ log β |
|---------|:----------:|:----------:|:-------:|
| ML₁ | **10.38** | ~6.0 ⚠️ | — |
| ML₂ | 14.50 | — | — |

> ⚠️ The Co³⁺/NTA entry (log β = 6.0) is a **conditional constant** for the hydroxo species [Co(OH)(NTA)]⁻ (beta_def_966/238), not the simple [Co(NTA)] complex. This reflects the kinetic inertness of Co³⁺ — equilibrium measurements are extremely difficult and the tabulated value is not directly comparable to the Co²⁺ ML₁ constant.

### EDTA (hexadentate, I = 0.1 M)

| Species | Co²⁺ log β | Co³⁺ log β | Δ log β |
|---------|:----------:|:----------:|:-------:|
| ML₁ | **16.31** | **36.0** | **+19.7** |
| MHL₁ | 20.11 | 40.67 | +20.6 |

---

## 3. Summary of Δ log β by Ligand

| Ligand | Denticity | Co²⁺ log β (MLₙ) | Co³⁺ log β (MLₙ) | Δ log β |
|--------|:---------:|:-----------------:|:-----------------:|:-------:|
| NH₃ (ML₅) | 1×5 | 5.73 | 35.16 | **+29.4** |
| en (ML₃) | 2×3 | 13.94 | 47.68 | **+33.7** |
| IDA (ML₁) | 3×1 | 7.05 | 14.0 | **+7.0** |
| EDTA (ML₁) | 6×1 | 16.31 | 36.0 | **+19.7** |

The pattern is unambiguous: **Co³⁺ forms dramatically more stable complexes than Co²⁺ with every nitrogen-donor ligand**, with Δ log β ranging from ~7 to ~34 log units.

---

## 4. Crystal-Field Theory Interpretation

### Electronic configurations

| Ion | Config | Geometry | Spin state | CFSE |
|-----|--------|----------|------------|------|
| Co²⁺ | d⁷ | Octahedral | High-spin (weak N-donors) | −0.8 Δₒ |
| Co³⁺ | d⁶ | Octahedral | **Low-spin** (amine/NH₃) | **−2.4 Δₒ** |

### Why Co³⁺ wins so decisively

1. **Charge effect (+3 vs +2):** Higher charge increases electrostatic attraction to donor atoms, raising all log β values by a baseline amount.
2. **CFSE dominance:** Co³⁺ is a d⁶ low-spin ion with amine ligands. Its crystal-field stabilization energy (CFSE = −2.4 Δₒ) is **three times** that of high-spin Co²⁺ (d⁷, CFSE = −0.8 Δₒ). This extra thermodynamic stabilization is directly reflected in the enormous Δ log β values.
3. **Chelate amplification:** The chelate effect multiplies the CFSE advantage. Each additional chelate ring locks the geometry into the ideal octahedral arrangement that maximizes CFSE for low-spin d⁶. This explains why Δ log β grows from ~7 (IDA, one tridentate) to ~34 (en₃, three bidentate rings forming a perfect octahedron).
4. **Kinetic inertness:** Co³⁺ complexes are substitution-inert (t₂g⁶ configuration, no labile eg electrons), which is why the NTA data is complicated — equilibrium is hard to reach, and the database reflects only the hydroxo-intermediate species.

---

## 5. Prediction for a New Polydentate Amine Ligand

Based on the SRD-46 data and crystal-field theory, here is what to expect for a hypothetical new **polydentate amine** (e.g., a tetradentate or hexadentate polyamine like trien or cyclam):

| Property | With Co²⁺ | With Co³⁺ | Basis |
|----------|-----------|-----------|-------|
| log β (estimated) | ~15–20 | ~45–60 | Extrapolating from en₃ and EDTA trends |
| Δ log β vs Co²⁺ | baseline | **+25 to +40** | CFSE + charge + chelate effect |
| Kinetics | Labile (fast exchange) | **Inert** (very slow exchange) | t₂g⁶ low-spin d⁶ |
| Preferred geometry | Distorted octahedral | **Rigid octahedral** | CFSE maximized at Oh |
| Selectivity | Moderate | **Extreme** | Kinetic trap + thermodynamic sink |
| Redox behavior | Easily oxidized to Co³⁺ in complex | Stabilized in +3 state | Complex formation shifts E° |

**Key prediction:** A new hexadentate polyamine (e.g., a macrocyclic hexaamine) would form a **thermodynamic and kinetic trap** with Co³⁺ — log β likely exceeding 50, with dissociation half-lives of days to years at room temperature. With Co²⁺, the same ligand would form a moderately stable complex (log β ~15–25) that is **kinetically labile** and readily dissociates. This enormous difference (~25–35 log units) is the direct experimental signature of low-spin d⁶ CFSE, and it is precisely why Co³⁺ amine complexes like [Co(en)₃]³⁺ and [Co(NH₃)₆]³⁺ were the workhorses of classical coordination chemistry — they are stable enough to isolate, characterize, and study stereochemistry without decomposition.

---

*All stability constants from NIST SRD-46. Conditions: 25 °C, aqueous, I = 0.1–2.0 M as noted.*

---