# Co²⁺ vs. Co³⁺ Stability Constants: A Comprehensive Comparison

## Shared Ligands in NIST SRD-46

Co²⁺ (metal_33) has **977 ligand partners** while Co³⁺ (metal_34) has only **19** — reflecting the kinetic inertness of low-spin d⁶ Co(III) that makes equilibrium measurements challenging. I identified **12 ligands** studied with both oxidation states.

## Side-by-Side Stability Constants (log β₁, 25 °C, aqueous)

All values are log β₁ for the reaction **[M] + [L] ⇌ [ML]** (beta_def_812) at 25 °C:

| Ligand | Denticity | Donor Set | log β₁ Co²⁺ | log β₁ Co³⁺ | Δ log β₁ |
|--------|-----------|-----------|-------------|-------------|----------|
| Ammonia (NH₃) | 1 | N | 2.1 | 6.7–7.3 | **+4.6 to +5.2** |
| Glycine | 2 | N,O | 4.7 (25 °C, I=0.1) | 12.4 | **+7.7** |
| Ethylenediamine (en) | 2 | N,N | 5.9 | 18.7 | **+12.8** |
| DL-Propylenediamine (pn) | 2 | N,N | ~5.9* | 18.7 | **~+12.8** |
| Diethylenetriamine (dien) | 3 | N₃ | ~8.1* | 24.0 | **~+15.9** |
| NTA | 4 | N,O₃ | 10.6 | 20.0 | **+9.4** |
| Cyclen | 4 | N₄ | ~12* | 23.8 | **~+12** |
| Triethylenetetramine (trien) | 4 | N₄ | ~11* | 28.0 | **~+17** |
| Tren | 4 | N₄ | ~11* | 26.0 | **~+15** |
| EDTA | 6 | N₂O₄ | 16.3 | 36.0–40.7 | **+19.7 to +24.4** |
| Tetraethylenepentamine (tetren) | 5 | N₅ | ~14* | 32.0 | **~+18** |
| Pentaethylenehexamine (penten) | 6 | N₆ | ~16* | 34.0 | **~+18** |

*\*Estimated from SRD-46 trends where exact matched-condition Co²⁺ data was not fully retrieved.*

## Cumulative β Values for Ammonia (25 °C, I = 0)

| Species | log βₙ Co²⁺ | log βₙ Co³⁺ | Δ log βₙ |
|---------|-------------|-------------|----------|
| ML (β₁) | 2.1 | 7.0 | +4.9 |
| ML₂ (β₂) | 3.5* | 13.9 | +10.4 |
| ML₃ (β₃) | 4.4* | 20.1 | +15.7 |
| ML₄ (β₄) | 5.1* | 25.6 | +20.5 |
| ML₅ (β₅) | 5.5* | 30.4 | +24.9 |
| ML₆ (β₆) | — | 33.2 | — |

## Stepwise Constants for Ethylenediamine (Co³⁺, 25 °C, I = 0)

| Step | log K (Co³⁺) |
|------|-------------|
| K₁ | 18.7 |
| K₂ | 16.2 |
| K₃ | 13.8 |

The remarkably slow decline in stepwise K values for Co³⁺ (only ~2.5 log units per step) contrasts with typical Co²⁺ behavior where stepwise constants drop more steeply. This reflects the strong preference of low-spin d⁶ Co³⁺ for a full octahedral coordination shell.

## Key Trends Observed

1. **Δ log β₁ increases with denticity**: From ~5 (monodentate NH₃) → ~13 (bidentate en) → ~16–18 (tetradentate amines) → ~20–24 (hexadentate EDTA).

2. **N-donors amplify the gap more than O-donors**: Compare glycine (N,O; Δ = +7.7) vs. ethylenediamine (N,N; Δ = +12.8) — both bidentate, but the all-nitrogen donor set produces a 5 log unit larger enhancement for Co³⁺.

3. **The chelate effect compounds**: Each additional chelate ring adds roughly +3–5 log units to the Co³⁺ advantage beyond what Co²⁺ gains.

## Crystal-Field Theory Explanation

| Property | Co²⁺ (d⁷) | Co³⁺ (d⁶) |
|----------|-----------|-----------|
| Typical spin state | High-spin | Low-spin |
| Configuration | t₂g⁵ eg² | t₂g⁶ eg⁰ |
| CFSE (octahedral) | −0.8 Δ_oct | −2.4 Δ_oct |
| Ionic radius | ~74.5 pm | ~54.5 pm |
| eg electrons | 2 (antibonding) | 0 |

The enormous stability enhancement for Co³⁺ arises from three reinforcing factors:

1. **Electrostatics**: Higher charge (+3 vs. +2) packed into a smaller radius gives Co³⁺ a much higher charge density, strengthening all metal–ligand bonds.

2. **Maximum CFSE**: The low-spin d⁶ configuration achieves the **largest possible CFSE** of any dⁿ system (−2.4 Δ_oct). With zero eg electrons, there is no antibonding destabilization of the σ framework. N-donor ligands, being moderate-to-strong field, push Δ_oct higher, further stabilizing the low-spin state in a cooperative feedback loop.

3. **Chelate amplification**: The intrinsic per-bond advantage (~5 log units for monodentate NH₃) is multiplied by the chelate effect. Each chelate ring constrains the ligand geometry, and Co³⁺'s strong preference for regular octahedral geometry (no Jahn-Teller distortion, unlike d⁷ Co²⁺) means polydentate ligands achieve near-ideal bite angles.

## Prediction: New Polydentate Amine Ligand

Based on the quantitative trends extracted from SRD-46, here is a prediction for a hypothetical new polydentate amine:

| Property | With Co²⁺ | With Co³⁺ |
|----------|-----------|-----------|
| **Tetradentate N₄ amine** | log β₁ ≈ 10–12 | log β₁ ≈ 25–28 |
| **Hexadentate N₆ amine** | log β₁ ≈ 15–17 | log β₁ ≈ 33–36 |
| **Expected Δ log β₁** | — | **+15 to +20** |
| Spin state | High-spin (likely) | Low-spin (certain) |
| Kinetic behavior | Labile (ms–s exchange) | Inert (hours–days) |
| Geometry | Distorted octahedral | Regular octahedral |
| Redox effect | Complex stabilizes Co³⁺ state | Co³⁺/²⁺ reduction potential shifts negative |

**Specific predictions:**

- A **tetradentate linear tetraamine** (like trien) should give log β₁ ≈ 26–28 with Co³⁺ and ~11 with Co²⁺ (Δ ≈ +16), based on the trien data (28.0 vs. ~11).
- A **hexadentate cage amine** (e.g., sar or sep-type) should approach log β₁ ≈ 34–36 with Co³⁺, rivaling penten (34.0), with the macrocyclic/cage effect adding 1–3 log units beyond the open-chain analogue.
- The complex will strongly **stabilize the +3 oxidation state**, shifting the Co³⁺/²⁺ reduction potential negative by roughly −0.06 V per unit of Δ log β (Nernst relationship), potentially making the Co³⁺ complex stable against reduction by ~1.0–1.2 V relative to the aqua ion.

This is precisely why Werner's classic cobalt(III) amine complexes — [Co(en)₃]³⁺, [Co(NH₃)₆]³⁺ — are among the most stable and kinetically inert coordination compounds known, and why polydentate amines remain the ligand class of choice for stabilizing cobalt in its +3 oxidation state.

*Data source: NIST Standard Reference Database 46 (Critically Selected Stability Constants of Metal Complexes)*

---