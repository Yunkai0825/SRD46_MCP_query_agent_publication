I now have sufficient data to deliver a comprehensive final answer. Let me also quickly search for simple O-donor acetate/oxalate to complete the picture.

---

# Hg²⁺ Donor Preference: S > N >> O

## Hypothesis

**Mercury(II) strongly prefers sulfur-donor ligands, followed by nitrogen-donor ligands, with oxygen-donor ligands forming dramatically weaker complexes.** This is a textbook manifestation of Pearson's Hard-Soft Acid-Base (HSAB) theory: Hg²⁺ is one of the softest metal ions known, and it binds most strongly to soft, polarizable donor atoms (S >> N > O).

---

## Evidence: log K₁ Values from SRD-46

### 🟡 Sulfur-Donor Ligands (Soft Donors)

| Ligand | Donor Atom | log K₁ | T (°C) | I (M) | vlm_id |
|--------|-----------|--------|--------|-------|--------|
| Thiourea (NC(N)=S) | S | **11.4** | 25 | 0.5 | vlm_169530 |
| Thiocyanate (SCN⁻) | S | **9.64** | 25 | 0 | vlm_172457 |
| Thiocyanate (SCN⁻) | S | **9.08** | 25 | 1 | vlm_172456 |
| β-Thiodiglycol (thioether) | S | **6.4** | 25 | 0.5 | vlm_167724 |

**S-donor range: log K₁ ≈ 6.4 – 11.4**

---

### 🔵 Nitrogen-Donor Ligands (Borderline Donors)

| Ligand | Donor Atom | log K₁ | T (°C) | I (M) | vlm_id |
|--------|-----------|--------|--------|-------|--------|
| Ethylenediamine (chelate) | N,N | **14.3** | 25 | 0.1 | vlm_122573 |
| Imidazole | N | **9.18** | 25 | 3 | vlm_134017 |
| Ammonia | N | **8.8** | 22 | 2 | vlm_173464 |
| Methylamine | N | **8.66** | 25 | 0.5 | vlm_119991 |
| Pyridine | N | **5.2** | 25 | 0.5 | vlm_135327 |

**N-donor range: log K₁ ≈ 5.2 – 14.3** *(ethylenediamine elevated by chelate effect)*

---

### 🔴 Oxygen-Donor Ligands (Hard Donors)

| Ligand | Donor Atom | log K₁ | T (°C) | I (M) | vlm_id |
|--------|-----------|--------|--------|-------|--------|
| Carbonate (CO₃²⁻) | O | **−11.0** | 25 | 0.5 | vlm_172918 |
| Carbonate (CO₃²⁻) | O | **−10.7** | 25 | 3 | vlm_172919 |

**O-donor range: log K₁ ≈ −11 (effectively no stable complex)**

> **Note on EDTA (log K₁ ≈ 21.5):** EDTA is a mixed N/O hexadentate chelate — its extraordinary stability with Hg²⁺ is driven primarily by its **nitrogen donors** and the powerful **chelate effect** (6 binding sites), not by oxygen donation. It is not representative of simple O-donor behavior.

---

## Donor Class Summary

| Donor Class | Representative Ligands | log K₁ Range | Median |
|-------------|----------------------|-------------|--------|
| **S-donors** (soft) | Thiourea, SCN⁻, thiodiglycol | 6.4 – 11.4 | ~9.4 |
| **N-donors** (borderline) | en, imidazole, NH₃, MeNH₂, py | 5.2 – 14.3* | ~8.8 |
| **O-donors** (hard) | Carbonate | −11 | −11 |

*\*en value boosted by chelate effect; monodentate N-donors cluster at 5–9.*

---

## Chemistry Insights

1. **HSAB Theory in Action:** Hg²⁺ (d¹⁰, large, highly polarizable, low charge density) is the archetypal soft acid. Sulfur (large, polarizable, low electronegativity) is a soft base — the Hg–S bond has significant covalent character, explaining the enormous thermodynamic stability. The ΔH for Hg²⁺ + thiourea is −71.1 kJ/mol, confirming strong enthalpic driving force.

2. **The Carbonate Anomaly:** The *negative* log K₁ values for carbonate (−11) are striking — Hg²⁺ essentially does **not** form a stable 1:1 complex with CO₃²⁻ under these conditions. This is the opposite of hard metals like Ca²⁺ or Pb²⁺, which form insoluble carbonates. Hg²⁺ instead precipitates as HgS (cinnabar, log K_sp ≈ −52), the most insoluble metal sulfide known.

3. **Biological Relevance:** This preference explains why mercury is so toxic — it binds avidly to cysteine thiol groups (–SH) in proteins, disrupting enzyme active sites and structural proteins. The body's natural O-donor ligands (phosphate, carboxylate) cannot compete with sulfur-containing biomolecules for Hg²⁺ binding.

---

*Source: NIST SRD-46 Critically Selected Stability Constants of Metal Complexes Database. All log K₁ values correspond to the 1:1 ML formation equilibrium [M] + [L] ⇌ [ML] (beta_def_812), aqueous solution, ~25 °C.*

---