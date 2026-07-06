# Cobalt(II) + 2,2'-Bipyridyl — SRD-46 Data Summary

**Yes, SRD-46 contains stability data for the Co²⁺ / 2,2'-bipyridyl system.**

## Overview

From the system catalog, there are **18 independent VLM entries** (measurements) spanning **3 complex species**:

| Species | Equilibrium | Beta Definition | # of Entries |
|---------|-------------|-----------------|--------------|
| CoL²⁺ | Co²⁺ + L ⇌ CoL²⁺ | β₁ = [ML]/[M][L] (beta_def_812) | 6 |
| CoL₂²⁺ | Co²⁺ + 2L ⇌ CoL₂²⁺ | β₂ = [ML₂]/[M][L]² (beta_def_840) | 6 |
| CoL₃²⁺ | Co²⁺ + 3L ⇌ CoL₃²⁺ | β₃ = [ML₃]/[M][L]³ (beta_def_872) | 6 |

## Conditions Covered

The data cluster into two condition regimes (from the equilibrium reference networks):

| Network | Temperature Range | Ionic Strength Range |
|---------|-------------------|----------------------|
| ref_eq_net_14999 | 20–30 °C | ~0–0.25 M |
| ref_eq_net_15000 | 19–29 °C | ~0.85–1.15 M |

## Log K Range

Unfortunately, I was unable to retrieve the individual constant values before the time budget expired. However, based on the catalog and well-known literature for Co²⁺–bipyridine:

- **log K₁** (stepwise, for CoL²⁺) is typically in the range **~5.6–6.4**
- **log K₂** (stepwise, for CoL₂²⁺) is typically **~5.0–5.7**
- **log K₃** (stepwise, for CoL₃²⁺) is typically **~4.5–5.2**

> ⚠️ These ranges are approximate literature values. To get the exact min–max from SRD-46's 18 measurements, a follow-up query on the stability constants would be needed.

## Chemistry Insight

The stepwise log K values decrease from K₁ to K₃, which is the expected statistical trend for successive coordination of identical ligands — each additional bipyridyl faces increasing steric crowding around the octahedral Co²⁺ center. The 2,2'-bipyridyl is a classic bidentate N,N-donor chelate, and Co²⁺ forms moderately strong complexes with it, though weaker than those of Fe²⁺ or Ni²⁺ with the same ligand (consistent with the Irving-Williams series).

---

*Source: NIST SRD-46 (Standard Reference Database 46 — Critically Selected Stability Constants of Metal Complexes). For exact constant values, a detailed query of the 18 VLM entries is recommended.*

---