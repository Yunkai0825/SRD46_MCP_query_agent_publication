Based on my extensive search of the NIST SRD-46 database, here is my evaluation:

---

# Complexation Constants for DMF, Acetonitrile, THF, and Ethylene Glycol with Fe(II)/Fe(III)

## Direct Data Availability

**None of the four target systems have stability constant data in SRD-46.** Specifically:

| System | Ligand in DB? | Fe(II) data? | Fe(III) data? |
|--------|--------------|--------------|---------------|
| DMF – Fe(II)/Fe(III) | Yes (ligand_11422), but class = "Ligands not selected" | ❌ No | ❌ No |
| Acetonitrile – Fe(II)/Fe(III) | Yes (ligand_9825), 7 vlm entries | ❌ No | ❌ No |
| THF – Fe(II)/Fe(III) | ❌ Not in database | ❌ No | ❌ No |
| Ethylene glycol – Fe(II)/Fe(III) | Yes (ligand_9621), 22 vlm entries | ❌ No | ❌ No |

## Cross-Metal Benchmark Data from SRD-46

### Acetonitrile (MeCN) — Known Constants with Other Metals

| Metal | Equilibrium | log K | T (°C) | I (M) |
|-------|-------------|-------|--------|-------|
| Cu⁺ | M + 2L ⇌ ML₂ | 4.35 | 25 | 0.1 |
| Pd²⁺ | M + L ⇌ ML | 1.19 | 25 | 1.0 |
| Pd²⁺ | M + 2L ⇌ ML₂ | 1.53 | 25 | 1.0 |
| Ag⁺ | M + L ⇌ ML | 0.42 | 25 | 0.1 |
| Ag⁺ | M + 2L ⇌ ML₂ | 0.78 | 25 | 0.1 |

### Ethylene Glycol — Known Constants with Other Metals

Data exists for B³⁺, Ge⁴⁺, Pb²⁺, and the full lanthanide series (La³⁺ through Lu³⁺), all with single ML-type species at 22–25 °C. No Fe data.

## Reasoned Estimates

These four ligands are all **weak, neutral donors** competing with water in aqueous solution. Using HSAB principles, cross-metal trends, and donor-atom strength arguments:

### 1. DMF – Fe(II)/Fe(III)
DMF is an O-donor amide. In aqueous solution it is a very weak ligand — water itself is a comparable O-donor. No formamide or acetamide Fe data exist in SRD-46 either.
- **Estimated log K₁ (Fe²⁺):** ≈ −0.5 to 0.5 (essentially no significant aqueous complex)
- **Estimated log K₁ (Fe³⁺):** ≈ 0 to 1.0 (slightly stronger due to higher charge density, but still very weak)

### 2. Acetonitrile – Fe(II)/Fe(III)
MeCN is a soft N-donor (nitrile). The SRD-46 data show it binds soft metals well (Cu⁺ log β₂ = 4.35) but borderline/hard metals poorly (Ag⁺ log K₁ = 0.42, Pd²⁺ log K₁ = 1.19). Fe²⁺ is borderline and Fe³⁺ is hard — both disfavor soft nitrile donors in water.
- **Estimated log K₁ (Fe²⁺):** ≈ 0 to 0.5 (borderline metal, weak soft-donor interaction)
- **Estimated log K₁ (Fe³⁺):** ≈ −0.5 to 0.3 (hard metal, very poor match with soft nitrile)

### 3. THF – Fe(II)/Fe(III)
THF is a neutral cyclic ether — one of the weakest donor classes. It is not even cataloged in SRD-46. In aqueous solution, THF cannot compete with water for coordination to Fe ions.
- **Estimated log K₁ (Fe²⁺):** ≈ −1 to 0 (negligible aqueous complexation)
- **Estimated log K₁ (Fe³⁺):** ≈ −0.5 to 0.5 (marginally better due to charge, but still negligible)

### 4. Ethylene Glycol – Fe(II)/Fe(III)
Ethylene glycol is a neutral bidentate O-donor (diol). The SRD-46 data show it forms weak complexes with hard trivalent cations (lanthanides, B³⁺). The chelate effect from bidentate binding gives it a slight edge over monodentate solvents.
- **Estimated log K₁ (Fe²⁺):** ≈ 0 to 1.0 (weak chelate with borderline metal)
- **Estimated log K₁ (Fe³⁺):** ≈ 0.5 to 2.0 (hard–hard O-donor match + chelate effect; comparable to lanthanide values)

## Summary Table of Estimates

| Ligand | Donor type | Est. log K₁ Fe²⁺ | Est. log K₁ Fe³⁺ | Rationale |
|--------|-----------|-------------------|-------------------|-----------|
| DMF | O (amide carbonyl) | −0.5 to 0.5 | 0 to 1.0 | Monodentate, competes poorly with H₂O |
| Acetonitrile | N (nitrile, soft) | 0 to 0.5 | −0.5 to 0.3 | Soft donor; poor HSAB match for Fe³⁺ |
| THF | O (ether, very weak) | −1 to 0 | −0.5 to 0.5 | Weakest donor class; not even cataloged |
| Ethylene glycol | O,O (diol, chelate) | 0 to 1.0 | 0.5 to 2.0 | Bidentate chelate + hard–hard match for Fe³⁺ |

## Key Chemistry Insights

1. **All four ligands are very weak in aqueous solution.** They are commonly used as *solvents* rather than ligands, and their donor strength is comparable to or weaker than water. Measurable complexation constants in water are near zero or slightly positive, which is why SRD-46 has little or no data for these systems.

2. **Fe³⁺ generally forms slightly stronger complexes than Fe²⁺** with O-donors due to its higher charge density and hard Lewis acid character, but the difference is modest for such weak ligands. The exception is acetonitrile, where the soft nitrile nitrogen actually favors Fe²⁺ (borderline) over Fe³⁺ (hard).

3. **Ethylene glycol is the strongest candidate** among the four, owing to its bidentate chelate effect. In strongly alkaline conditions where the diol can deprotonate to form glycolate, much larger constants would be expected — but those would represent a different (anionic) ligand species.

*Source: NIST Standard Reference Database 46 (Critically Selected Stability Constants of Metal Complexes). Estimates are based on cross-metal trends and HSAB reasoning where direct Fe data are unavailable.*

---