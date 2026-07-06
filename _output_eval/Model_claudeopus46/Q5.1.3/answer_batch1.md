# Iron vs. Copper — A Comparison from NIST SRD-46

## 1. Data Richness Overview

| Ion | Oxidation State | Distinct Ligands | Distinct β-Definitions | Total Measurements (VLMs) |
|-----|----------------|-----------------|----------------------|--------------------------|
| **Cu²⁺** (metal_41) | +2 | 1,951 | 264 | 8,963 |
| **Cu⁺** (metal_42) | +1 | 117 | 32 | 285 |
| Cu³⁺ (metal_43) | +3 | 8 | 4 | 10 |
| **Fe³⁺** (metal_61) | +3 | 406 | 128 | 1,473 |
| **Fe²⁺** (metal_62) | +2 | 217 | 57 | 667 |

**Cu²⁺ is the second most-studied metal ion in SRD-46** (after H⁺), with nearly **6× more measurements** and **5× more ligand partners** than Fe³⁺. Fe³⁺ ranks ~10th overall, and Fe²⁺ falls further behind. Cu⁺ and Cu³⁺ are niche entries with very limited data.

## 2. Global Ranking Context

| Rank | Metal | Ligand Partners | Measurements |
|------|-------|----------------|-------------|
| 1 | H⁺ | 4,081 | 20,720 |
| **2** | **Cu²⁺** | **1,951** | **8,963** |
| 3 | Ni²⁺ | 1,369 | 5,325 |
| 4 | Zn²⁺ | 1,169 | 4,095 |
| … | … | … | … |
| **~10** | **Fe³⁺** | **406** | **1,473** |
| ~15+ | Fe²⁺ | 217 | 667 |

## 3. Shared Ligands — Top Partners

The two metals share many classic ligands. The most data-rich shared systems are:

| Ligand | Shared Metals | Total Measurements |
|--------|--------------|-------------------|
| Hydroxide (OH⁻) | Cu²⁺, Cu⁺, Fe³⁺, Fe²⁺ | 88 |
| Ammonia (NH₃) | Cu²⁺, Cu⁺, Fe²⁺ | 87 |
| Thiocyanate (SCN⁻) | Cu²⁺, Cu⁺, Fe³⁺, Fe²⁺ | 66 |
| Histidine | Cu²⁺, Cu⁺, Fe³⁺, Fe²⁺ | 60 |
| Acetic acid | Cu²⁺, Fe³⁺, Fe²⁺ | 54 |
| Glycine | Cu²⁺, Cu⁺, Fe³⁺, Fe²⁺ | 51 |
| Chloride (Cl⁻) | Cu²⁺, Cu⁺, Fe³⁺, Fe²⁺ | 48 |
| 2,2'-Bipyridyl | Cu²⁺, Cu⁺, Fe³⁺, Fe²⁺ | 46 |
| Ethylenediamine | Cu²⁺, Cu⁺, Fe²⁺ | 44 |
| EDTA | Cu²⁺, Fe³⁺, Fe²⁺ | 40 |
| 1,10-Phenanthroline | Cu²⁺, Cu⁺, Fe³⁺, Fe²⁺ | 39 |

## 4. Head-to-Head Stability Constants (25 °C, I ≈ 0.1 M)

| Ligand | Equilibrium | Cu²⁺ log K/β | Fe²⁺ log K/β | Fe³⁺ log K/β |
|--------|------------|--------------|--------------|--------------|
| **Ammonia** | ML (log K₁) | **4.27** | 1.4 | — |
| **Glycine** | ML (log K₁) | **8.62** | 4.31 | 10.0 |
| **Glycine** | ML₂ (log β₂) | **15.64** | 7.60 | 18.49 |
| **Glycine** | ML₃ (log β₃) | — | — | 24.33 |
| **2,2'-Bipyridyl** | ML (log K₁) | **8.0** | 4.34 | — |
| **2,2'-Bipyridyl** | ML₃ (log β₃) | — | **17.45** | 16.31 |
| **EDTA** | ML (log K) | 18.70 | 14.33 | **25.10** |

## 5. Key Chemical Insights

1. **Cu²⁺ dominates over Fe²⁺** for virtually every ligand, consistent with the **Irving–Williams series** (Mn²⁺ < Fe²⁺ < Co²⁺ < Ni²⁺ < **Cu²⁺** > Zn²⁺). Cu²⁺ log K₁ values are typically 3–4 units higher than Fe²⁺ for the same ligand — a reflection of the Jahn–Teller-distorted d⁹ configuration that provides extra ligand-field stabilization energy.

2. **Fe³⁺ can surpass Cu²⁺** thanks to its higher charge density. With EDTA, Fe³⁺ (log K = 25.1) far exceeds Cu²⁺ (18.7), reflecting the strong electrostatic advantage of a +3 ion with a hard, hexadentate O/N-donor chelate. Similarly, Fe³⁺–glycine complexes (log K₁ = 10.0) are stronger than Cu²⁺–glycine (log K₁ = 8.6), consistent with HSAB theory — Fe³⁺ is a hard acid that pairs well with hard oxygen/nitrogen donors.

3. **2,2'-Bipyridyl is a special case**: Fe²⁺ forms the iconic tris-complex [Fe(bipy)₃]²⁺ (log β₃ = 17.45) with a large cooperative stabilization from the low-spin d⁶ configuration, making it *more stable* than the Fe³⁺ analogue (log β₃ = 16.31) — a rare reversal that underpins the use of ferroin as a redox indicator.

4. **Data asymmetry matters**: Cu²⁺ has ~9,000 measurements across ~2,000 ligands, making it the best-characterized transition metal in the database. Iron data, while substantial, is roughly 5–6× sparser, so users should expect fewer condition-matched entries for Fe systems. Researchers needing iron stability data may find gaps, especially for Fe²⁺ with softer donor ligands.

*Source: NIST Standard Reference Database 46 (Critically Selected Stability Constants of Metal Complexes).*

---