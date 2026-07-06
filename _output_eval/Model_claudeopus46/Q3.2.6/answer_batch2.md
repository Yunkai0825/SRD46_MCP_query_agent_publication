# Conditional Stability Constant for Cu²⁺–Malonate at pH 4

## Data from NIST SRD-46

I'll use values measured at **25 °C, I = 0.1 M** for consistency:

| Parameter | Value | Source (vlm_id) | Conditions |
|-----------|-------|-----------------|------------|
| pKₐ₁ (H₂L ⇌ HL⁻ + H⁺) | **2.65** | vlm_151949 | 25 °C, I = 0.1 M |
| pKₐ₂ (HL⁻ ⇌ L²⁻ + H⁺) | **5.27** | vlm_151918 | 25 °C, I = 0.1 M |
| log K₁ (Cu²⁺ + L²⁻ ⇌ CuL) | **5.04** | vlm_152316 | 25 °C, I = 0.1 M |
| log K (Cu²⁺ + HL⁻ ⇌ CuHL⁺) | **2.08** | vlm_152328 | 25 °C, I = 0.1 M |

Here **L²⁻** is the fully deprotonated malonate dianion and **HL⁻** is the hydrogen malonate monoanion.

---

## Step-by-step Calculation

### 1. Acid dissociation constants

$$K_{a1} = 10^{-2.65} = 2.239 \times 10^{-3}, \qquad K_{a2} = 10^{-5.27} = 5.370 \times 10^{-6}$$

### 2. Speciation fractions at pH 4

At pH 4: $[\text{H}^+] = 10^{-4}$ M.

The denominator for the distribution of free ligand species is:

$$D = [\text{H}^+]^2 + [\text{H}^+]\,K_{a1} + K_{a1}\,K_{a2}$$

$$D = (10^{-4})^2 + (10^{-4})(2.239 \times 10^{-3}) + (2.239 \times 10^{-3})(5.370 \times 10^{-6})$$

$$D = 1.000 \times 10^{-8} + 2.239 \times 10^{-7} + 1.202 \times 10^{-8}$$

$$D = 2.459 \times 10^{-7}$$

Now the mole fractions:

| Species | Formula | Value |
|---------|---------|-------|
| α(L²⁻) | $K_{a1} K_{a2} / D$ | $1.202 \times 10^{-8} / 2.459 \times 10^{-7} = 0.04889$ |
| α(HL⁻) | $[\text{H}^+] K_{a1} / D$ | $2.239 \times 10^{-7} / 2.459 \times 10^{-7} = 0.9106$ |
| α(H₂L) | $[\text{H}^+]^2 / D$ | $1.000 \times 10^{-8} / 2.459 \times 10^{-7} = 0.04067$ |

At pH 4, **~91% of free malonate exists as HL⁻**, with only **~4.9% as L²⁻** and **~4.1% as H₂L**.

### 3. Conditional stability constant

The **conditional (effective) formation constant** $K'$ relates the metal to the *total* free ligand concentration $C_L = [\text{L}^{2-}] + [\text{HL}^-] + [\text{H}_2\text{L}]$, rather than just $[\text{L}^{2-}]$.

#### (a) CuL pathway only

$$\log K'_{\text{CuL}} = \log K_1 + \log_{10}\,\alpha(\text{L}^{2-})$$

$$\log K'_{\text{CuL}} = 5.04 + \log_{10}(0.04889) = 5.04 + (-1.311) = \boxed{3.73}$$

#### (b) Including the protonated complex CuHL⁺

The CuHL⁺ species also forms at pH 4. Its conditional contribution is:

$$\log K'_{\text{CuHL}} = \log K_{\text{MHL}} + \log_{10}\,\alpha(\text{HL}^-) = 2.08 + \log_{10}(0.9106) = 2.08 + (-0.041) = 2.04$$

The **total conditional constant** combines both pathways:

$$K'_{\text{total}} = K'_{\text{CuL}} + K'_{\text{CuHL}} = 10^{3.73} + 10^{2.04} = 5370 + 110 = 5480$$

$$\log K'_{\text{total}} = \log_{10}(5480) = \boxed{3.74}$$

---

## Summary

| Quantity | log K' at pH 4 |
|----------|---------------|
| CuL pathway only | **3.73** |
| CuL + CuHL combined | **3.74** |

### Physical interpretation

The "thermodynamic" log K₁ of 5.04 for Cu²⁺–malonate drops by about **1.3 log units** at pH 4 because only ~5% of the free ligand is in the fully deprotonated L²⁻ form needed for the dominant binding equilibrium. The protonated complex CuHL⁺ (log K = 2.08) contributes only modestly (~2% of the total conditional constant) because, although HL⁻ is the dominant free-ligand species, its Cu²⁺ affinity is much weaker than that of L²⁻.

At pH 4, Cu²⁺–malonate complexation is still significant (K' ≈ 5500), meaning malonate is an effective chelator of copper even under mildly acidic conditions — relevant in soil chemistry and biological buffering.

*Source: NIST Standard Reference Database 46 (Critically Selected Stability Constants of Metal Complexes).*

---