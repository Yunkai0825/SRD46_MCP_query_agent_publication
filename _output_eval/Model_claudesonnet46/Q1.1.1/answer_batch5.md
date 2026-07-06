## Cu(II)–Glycine Stability Constants (SRD-46)

**System:** Cu²⁺ (metal_41) + Glycine / Aminoacetic acid (ligand_5760, SMILES: `NCC(=O)O`)  
**Species defined:** Cu²⁺ + nL⁻ ⇌ CuLₙ (cumulative β, fully deprotonated ligand L⁻)

---

### Cumulative log β — CuL (ML, beta_def_812): Cu²⁺ + Gly⁻ ⇌ CuGly⁺

| vlm_id | T (°C) | I (mol/L) | log β |
|-----------|--------|-----------|-------|
| vlm_93853 | 10 | 0 | **8.80** |
| vlm_93854 | 25 | 0 | **8.56** |
| vlm_93847 | 25 | 0.1 | 8.19 |
| vlm_93849 | 25 | 0.5 | 8.10 |
| vlm_93850 | 25 | 1.0 | 8.20 |
| vlm_93851 | 25 | 2.0 | 8.38 |
| vlm_93852 | 25 | 2.5 | 8.34 |
| vlm_93848 | 37 | 0.15 | 7.99 |
| vlm_93855 | 40 | 0 | 8.37 |

---

### Cumulative log β — CuL₂ (ML₂, beta_def_840): Cu²⁺ + 2 Gly⁻ ⇌ Cu(Gly)₂

| vlm_id | T (°C) | I (mol/L) | log β |
|-----------|--------|-----------|-------|
| vlm_93868 | 10 | 0 | **16.30** |
| vlm_93869 | 25 | 0 | **15.70** |
| vlm_93862 | 25 | 0.1 | 15.10 |
| vlm_93864 | 25 | 0.5 | 15.00 |
| vlm_93865 | 25 | 1.0 | 15.10 |
| vlm_93866 | 25 | 2.0 | 15.40 |
| vlm_93867 | 25 | 2.5 | 15.40 |
| vlm_93863 | 37 | 0.15 | 14.69 |
| vlm_93870 | 40 | 0 | 15.30 |

---

### Thermodynamic Data at 25 °C

| Species | I (mol/L) | ΔH (kJ/mol) | ΔS (J/mol·K) |
|---------|-----------|-------------|--------------|
| CuGly⁺ (ML) | 0 | −25.1 | +79.5 |
| CuGly⁺ (ML) | 0.1 | −25.1 | +72.4 |
| Cu(Gly)₂ (ML₂) | 0 | −54.4 | +118.0 |
| Cu(Gly)₂ (ML₂) | 0.1 | −54.4 | +106.7 |

---

### Key Observations

- **Canonical values (25 °C, I → 0):** log β₁ = **8.56**, log β₂ = **15.70**, giving a stepwise log K₂ = 15.70 − 8.56 = **7.14** — slightly lower than K₁, consistent with statistical and electrostatic factors for adding a second anionic ligand.
- **Temperature effect:** log β decreases from 10 °C → 25 °C → 40 °C (e.g., ML: 8.80 → 8.56 → 8.37), indicating the complexation is **exothermic** (confirmed by ΔH ≈ −25 kJ/mol for ML), with entropy making a significant favorable contribution (ΔS > 0).
- **Ionic strength effect:** Both β₁ and β₂ show a shallow minimum around I = 0.1–0.5 M and then rise slightly at higher ionic strengths — a classic Debye–Hückel / activity-coefficient effect for 2+/1− charge interactions.
- **Biological relevance:** The physiological-condition value (37 °C, I = 0.15 M) of log β₂ = **14.69** reflects the strong chelation of Cu²⁺ by glycine's amino-carboxylate bidentate coordination, relevant to copper transport and amino acid supplementation chemistry.

*Source: NIST SRD-46 (Standard Reference Database 46), 9 equilibrium networks (ref_eq_map_86–94).*

---