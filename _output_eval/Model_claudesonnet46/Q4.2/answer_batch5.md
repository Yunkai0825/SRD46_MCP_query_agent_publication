I now have sufficient data to construct a comprehensive, well-supported answer. Let me compile the findings.

---

# Hg²⁺ Donor Preference: S >> N >> O — An HSAB Analysis

## Summary of log K₁ Values (25 °C, aqueous, β_def_812: M + L ⇌ ML)

### 🟡 Sulfur-Donor Ligands

| Ligand | Donor Atom | log K₁ | I (M) | T (°C) |
|---|---|---|---|---|
| Thiourea (SC(NH₂)₂) | S | **11.4** | 0.5 | 25 |
| Thiocyanate (SCN⁻) | S | **9.64** | 0 | 25 |
| Thiocyanate (SCN⁻) | S | **9.08** | 1 | 25 |

> Note: H₂S forms predominantly insoluble HgS precipitates (β_def_288/292 dominate), reflecting an *even stronger* affinity — the Ksp of HgS is among the smallest known (~10⁻⁵²).

---

### 🔵 Nitrogen-Donor Ligands

| Ligand | Donor Atom | log K₁ | I (M) | T (°C) |
|---|---|---|---|---|
| Ethylenediamine (en) | N,N (chelate) | **14.3** | 0.1–1 | 25 |
| Imidazole | N | **9.18** | 3 | 25 |
| Ammonia (NH₃) | N | **8.8** | 2 | ~22 |
| Pyridine | N | **5.2** | 0.5 | 25 |

> Ethylenediamine's exceptionally high log K₁ = 14.3 reflects the **chelate effect** (bidentate N,N donor forming a 5-membered ring), not purely N-donor affinity. Monodentate N-donors (NH₃, pyridine) are far weaker.

---

### 🔴 Oxygen-Donor Ligands

| Ligand | Donor Atom | log K₁ | I (M) | T (°C) |
|---|---|---|---|---|
| EDTA⁴⁻ | N,N,O,O,O,O (hexadentate) | **21.5** | 0.1 | 25 |
| Carbonate (CO₃²⁻) | O | **−11.0** | 0.5 | 25 |
| Carbonate (CO₃²⁻) | O | **−10.7** | 3 | 25 |

> EDTA's enormous log K₁ = 21.5 is driven by the **macrochelate effect** (6 donor atoms, 5 chelate rings) — not O-donor affinity. Pure O-donors like carbonate show *negative* log K values, meaning Hg²⁺ essentially does **not** form stable complexes with simple oxygen donors.

---

## Hypothesis: **S >> N (monodentate) >> O for Hg²⁺**

### Evidence-Based Ranking

| Donor Class | Representative log K₁ (monodentate) | Trend |
|---|---|---|
| **S-donors** | 9–11 (thiourea, thiocyanate) | ✅ Strongest |
| **N-donors** | 5–9 (pyridine → ammonia → imidazole) | ✅ Intermediate |
| **O-donors** | −11 (carbonate) | ❌ Negligible / unfavorable |

---

## Chemistry Insight

This hierarchy is a textbook illustration of **Pearson's Hard-Soft Acid-Base (HSAB) theory**:

1. **Hg²⁺ is the archetypal soft acid** — it has a large ionic radius, high polarizability, and low charge density. It strongly prefers **soft bases** (S-donors) that are themselves highly polarizable, forming highly covalent bonds.

2. **S-donors win decisively**: Thiourea (log K₁ = 11.4) and thiocyanate (log K₁ = 9.6) bind strongly because sulfur's large, diffuse electron cloud overlaps well with Hg²⁺'s d-orbitals. H₂S affinity is so extreme that HgS precipitates immediately (Ksp ≈ 10⁻⁵²).

3. **N-donors are intermediate**: Nitrogen is a borderline-to-soft base. Monodentate N-donors (NH₃: 8.8, imidazole: 9.2, pyridine: 5.2) bind moderately. The chelate effect with ethylenediamine (log K₁ = 14.3) dramatically boosts stability beyond what N-donor affinity alone would predict.

4. **O-donors are essentially non-binding**: Carbonate gives log K₁ ≈ −11, meaning the equilibrium strongly *disfavors* complex formation. Hard oxygen donors are simply incompatible with this soft metal center.

5. **Biological relevance**: This HSAB preference explains why Hg²⁺ is so toxic — it binds irreversibly to cysteine thiol groups (–SH) in enzymes and proteins, displacing essential metals and destroying protein function. Chelation therapy with DMSA (dimercaptosuccinic acid, a dithiol) exploits this same S-donor preference to sequester Hg²⁺ in vivo.

---

*Source: NIST SRD-46 (Critically Selected Stability Constants of Metal Complexes), metal_71 (Hg²⁺), β_def_812 (M + L ⇌ ML, log K₁).*

---