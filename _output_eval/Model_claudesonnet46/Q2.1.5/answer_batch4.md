## Results

I have all the data needed for a clean comparison. Here is the full picture from SRD-46:

---

### Ni²⁺ + NH₃ vs. Ni²⁺ + Ethylenediamine (en) — 1:1 log K₁ at 25 °C

| Ligand | log K₁ | I (M) | T (°C) | vlm_id |
|--------|--------|-------|--------|--------|
| Ammonia (NH₃) | **2.72** | 0 (extrapolated) | 25 | vlm_173185 |
| Ammonia (NH₃) | **2.73** | 0.1 | 25 | vlm_173182 |
| Ethylenediamine (en) | **7.32** | 0 (extrapolated) | 25 | vlm_122371 |
| Ethylenediamine (en) | **7.30** | 0.1 | 25 | vlm_122365 |

### Δ log K (best-matched pair at I = 0.1 M, 25 °C)

| Comparison | Δ log K |
|---|---|
| log K(en) − log K(NH₃) | **7.30 − 2.73 = +4.57** |
| At I → 0 | **7.32 − 2.72 = +4.60** |

---

### 🏆 Ethylenediamine wins — by ~4.6 log units

**Ethylenediamine binds Ni²⁺ roughly 40,000× more strongly** than ammonia (10^4.6 ≈ 40,000) on a per-ligand-molecule basis.

---

### Chemistry Insight: The Chelate Effect

This dramatic difference is the textbook **chelate effect**. Both NH₃ and en donate nitrogen lone pairs to Ni²⁺, but en forms a **five-membered chelate ring** upon binding, gaining an enormous entropic advantage. The thermodynamic data confirm this beautifully:

| Ligand | ΔH (kJ/mol, I=0) | ΔS (J/mol·K, I=0) |
|--------|------|------|
| NH₃ | −15.1 | +1.7 |
| en | ~−37.7 (at I=0.5) | +9.2 (at I=0.1) |

Ethylenediamine is both **more exothermic** (stronger N→Ni bonds from the two coordinating amines acting cooperatively) and **entropically favored** (ring closure releases fewer solvent molecules per coordinating N). The chelate effect is one of the most important organizing principles in coordination chemistry, underpinning applications from EDTA-based chelation therapy to metal extraction processes.

---

*Source: NIST SRD-46 (Critically Selected Stability Constants of Metal Complexes), metal_112 (Ni²⁺), ligand_10103 (NH₃), ligand_7029 (en).*

---