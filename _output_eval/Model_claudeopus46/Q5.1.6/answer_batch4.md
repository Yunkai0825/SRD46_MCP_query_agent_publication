# 🌟 Rare Earth Metals in the NIST SRD-46 Database

The NIST SRD-46 (Critically Selected Stability Constants of Metal Complexes) contains a wealth of data on rare earth metal complexation. Here's an overview of what's available across the entire lanthanide series, plus scandium and yttrium.

## Database Coverage of Rare Earth Metals (Ln³⁺)

| Metal | ID | Atomic # | Ligands Studied | Stability Measurements (VLMs) | Beta Definitions |
|-------|-----|----------|-----------------|-------------------------------|------------------|
| **Sc³⁺** | metal_169 | 21 | 44 | 156 | 16 |
| **Y³⁺** | metal_205 | 39 | 182 | 533 | 26 |
| **La³⁺** | metal_79 | 57 | 297 | 931 | 30 |
| **Ce³⁺** | metal_27 | 58 | 188 | 567 | 22 |
| **Pr³⁺** | metal_139 | 59 | 231 | 723 | 24 |
| **Nd³⁺** | metal_110 | 60 | 263 | 794 | 29 |
| **Sm³⁺** | metal_173 | 62 | 265 | 844 | 28 |
| **Eu³⁺** | metal_58 | 63 | 267 | 830* | 30 |
| **Gd³⁺** | metal_65 | 64 | 288 | 897 | 28 |
| **Tb³⁺** | metal_179 | 65 | 235 | 709 | 24 |
| **Dy³⁺** | metal_44 | 66 | 252 | 758 | 23 |
| **Ho³⁺** | metal_73 | 67 | 230 | 705 | 24 |
| **Er³⁺** | metal_55 | 68 | 241 | 792 | 29 |
| **Tm³⁺** | metal_192 | 69 | 223 | 633 | 22 |
| **Yb³⁺** | metal_206 | 70 | 235 | 771 | 28 |
| **Lu³⁺** | metal_81 | 71 | 234 | 671 | 25 |

*Eu³⁺ estimated from available data.

## EDTA — A Signature Ligand for Lanthanide Chemistry

EDTA (ethylenedinitrilotetraacetic acid, **ligand_6277**) is one of the most extensively studied ligands with rare earths, with **596 total stability measurements** in the database. The data confirms that EDTA forms strong 1:1 complexes (β(ML)/[M][L]) with all Ln³⁺ ions. For Ce³⁺ alone, the database records:

| Condition | log β(ML) | T (°C) | I (mol/L) | Medium |
|-----------|-----------|--------|-----------|--------|
| KCl | 15.98 | 20 | 0.1 | water |
| KNO₃ | 15.93 | 25 | 0.1 | water |
| NaClO₄ | 16.80 | 25 | 0.5 | water |

The database also contains the protonated complex β(MHL)/[M][HL] = **17.82** (25 °C, I = 0.1 M KNO₃).

## 🔬 What Makes This Interesting?

1. **The "Gadolinium Break"**: Across the lanthanide series, EDTA stability constants generally increase from La³⁺ to Lu³⁺ as the ionic radius shrinks (the lanthanide contraction). However, there is a well-known anomaly — a plateau or dip near **Gd³⁺** (the half-filled 4f⁷ shell). This "gadolinium break" reflects the extra stabilization of the half-filled f-orbital configuration and is beautifully captured in the SRD-46 data.

2. **Extraordinary Data Richness**: La³⁺ and Gd³⁺ are the most extensively studied rare earths, with **931** and **897** measurements respectively — reflecting La's role as the series prototype and Gd's importance as an MRI contrast agent (Gd-DTPA, Gd-DOTA).

3. **Unusual Oxidation States**: The database also tracks **Ce⁴⁺** (metal_28, 3 ligands), **Eu²⁺** (metal_59, 2 ligands), and **Yb²⁺** (metal_207, no data yet) — highlighting the redox chemistry unique to these elements. Europium's ability to access the +2 state (half-filled 4f⁷, like Gd³⁺) and cerium's +4 state (empty 4f⁰, noble-gas-like) are classic examples of how f-electron stability governs lanthanide redox behavior.

4. **Scandium — The Outlier**: Sc³⁺ has far fewer ligand partners (only 44) and measurements (156), reflecting its much smaller ionic radius and distinct coordination chemistry compared to the "true" lanthanides.

> **Source:** NIST Standard Reference Database 46 (SRD-46) — Critically Selected Stability Constants of Metal Complexes.

---