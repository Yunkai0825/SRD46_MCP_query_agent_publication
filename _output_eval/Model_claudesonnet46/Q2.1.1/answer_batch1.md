## Fe³⁺ Complex Stability: EDTA vs. NTA

Here are the 1:1 formation constants (log K, β₁) from NIST SRD-46, both at **25 °C, I = 0.1 M** (aqueous):

| Ligand | Formula | log K (I = 0.1 M) | log K (I = 1.0 M) | ΔH (kJ/mol) | ΔS (J/mol·K) |
|--------|---------|:-----------------:|:-----------------:|:-----------:|:------------:|
| **EDTA** (ligand_6277) | C₁₀H₁₂N₂O₈⁴⁻ | **25.1** | 23.8 | −11.3 | 442.7 |
| **NTA** (ligand_6165) | C₆H₆NO₆³⁻ | **15.9** | 14.78 | +13.4 | 349.8 |

> **Difference at I = 0.1 M: Δlog K ≈ 9.2 log units** — EDTA binds Fe³⁺ roughly **1.6 billion times** more strongly than NTA.

---

### 🏆 Winner: EDTA — by a wide margin

**EDTA** (log K = **25.1**) vastly outperforms **NTA** (log K = **15.9**) in forming stable complexes with Fe³⁺.

### Why such a large difference?

1. **Denticity:** EDTA is a **hexadentate** ligand (4 carboxylates + 2 amines), while NTA is **tetradentate** (3 carboxylates + 1 amine). More donor atoms → stronger chelate effect → higher stability.

2. **Thermodynamic signatures are revealing:**
   - EDTA complexation is **exothermic** (ΔH = −11.3 kJ/mol) and highly entropy-driven (ΔS = +442.7 J/mol·K) — the release of many water molecules from Fe³⁺'s coordination sphere drives the reaction.
   - NTA complexation is actually **endothermic** (ΔH = +13.4 kJ/mol) and is *entirely* entropy-driven (ΔS = +349.8 J/mol·K), meaning it is less favorable enthalpically.

3. **Real-world relevance:** The extraordinary stability of Fe³⁺–EDTA (log K = 25.1) is exploited in iron-fortified foods, plant nutrient solutions, and industrial water treatment. NTA, while a weaker chelator, is used as a biodegradable alternative to EDTA in some applications.

*Source: NIST SRD-46 (metal_61 = Fe³⁺, ligand_6277 = EDTA, ligand_6165 = NTA; beta_def_812 = [ML]/[M][L])*

---