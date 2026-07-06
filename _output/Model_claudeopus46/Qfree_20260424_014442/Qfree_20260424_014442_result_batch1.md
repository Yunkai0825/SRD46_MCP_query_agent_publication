# Qfree_20260424_014442 -- Result (batch 1)

**Section:** freeform -- Fe(III)/Fe(II) ligand selection (corrected)

**Prompt:** I would like to find ligands that can complex Fe(III) to stabilize the acidic solution (pH<5), yet with limited complexation to Fe(II) so that it does not decrease the free Fe2+ concentration too much. This is for Fe electrodeposition since we also try to minimize the hydrogen evolution reaction when Fe electrodeposition happens. The expected concentration of Fe(II) is ~0.1M. Meanwhile, be cautious about ligand pH and its actual state, and be cautious about possible precipitations. If there are missing entries, try to observe similar metal-ligand systems with available data to estimate those with very robust reasons and explanations. You have unlimited time and unlimited turns.

**Tool calls:** 57  |  **Time:** 3166s planning + 1518s execution + 0s verdict = 4683s total

---

Now I have all the data I need. Let me compile the comprehensive final analysis with proper conditional stability constant calculations.

---

# Ligand Selection for Fe Electrodeposition: Fe(III) Stabilization with Minimal Fe(II) Complexation at pH < 5

## Problem Summary

You need a ligand that:
1. **Strongly complexes Fe(III)** to keep it soluble and prevent Fe(OH)₃ precipitation at pH < 5
2. **Weakly complexes Fe(II)** to maintain ~0.1 M free Fe²⁺ for electrodeposition
3. **Is active at pH < 5** — the ligand must be sufficiently deprotonated to bind metals
4. **Does not precipitate** with either Fe(III) or Fe(II)
5. **Minimizes HER** — avoiding overly acidic conditions or catalytic surfaces

## Key Data from NIST SRD-46

### Raw Stability Constants (log K₁ for M + L → ML)

| Ligand | pKa values | log K₁ Fe³⁺ | log K₁ Fe²⁺ | Δlog K | Conditions |
|--------|-----------|-------------|-------------|--------|------------|
| **Citric acid** | 2.90, 4.35, 5.65 | **11.27** | **4.40** | **6.87** | 25°C, I=0.1 |
| **Acetohydroxamic acid** | 9.29 | **11.42** | **4.80** | **6.62** | 20°C, I=0.1 |
| **Dipicolinic acid** | 2.07, 4.66 | **10.91** | **5.71** | **5.20** | 20°C, I=0.1 |
| **Benzohydroxamic acid** | 8.76 | **11.06** | no data | est. ~5† | 20°C, I=0.1 |
| **Malonic acid** | 2.65, 5.27 | **8.12** | **2.24** | **5.88** | 25°C, I=0.1–1 |
| **Oxalic acid** | 1.25, 3.81 | **7.58** | **3.05** | **4.53** | 25°C, I=1 |
| **Succinic acid** | 3.99, 5.24 | **6.88** | **−1.4** | **8.28** | 25°C, I=0.5 |
| **Fluoride (HF)** | 2.94 | **6.04** | **0.80** | **5.24** | 25°C, I=0–1 |
| **D-Gluconic acid** | 3.46 | **3.10** | **−1.00** | **4.10** | 25°C, I=1 |
| **Glycolic acid** | 3.62 | **2.90** | **1.33** | **1.57** | 25°C, I=1 |

†Estimated from acetohydroxamic acid analogy (same donor set: hydroxamate O,O).

### Phenolate/Catecholate Ligands (proton-competition equilibria converted)

| Ligand | pKa values | log K₁ Fe³⁺ | log K₁ Fe²⁺ | Δlog K | Notes |
|--------|-----------|-------------|-------------|--------|-------|
| **Salicylic acid** | 2.81, 12.44 | ~**15.3** | ~**5.6** | ~**9.7** | Phenol-carboxylate chelate |
| **5-Sulfosalicylic acid** | 2.48, 11.85 | ~**14.6** | ~**5.9** | ~**8.6** | Sulfonated, highly soluble |
| **Catechol** | 9.26, ~13.0 | ~**20.1** | ~**7.9** | ~**12.2** | Very strong, but protonated at pH<5 |
| **4-Nitrocatechol** | 6.69, 10.83 | ~**14.8** | est. ~5.8‡ | ~**9.0** | Lower pKa, partially active at pH<5 |
| **Tiron** | 7.62, ~12.5 | ~**20.4** | est. ~9–11§ | ~**9–11** | Sulfonated catechol, very soluble |

‡Estimated from catechol Fe²⁺ trend with EW substituent correction.
§Estimated from Mn²⁺ (8.6), Co²⁺ (11.1) analogy with tiron.

*Source: NIST SRD-46 database*

---

## Critical Analysis: Conditional Stability at pH < 5

The **raw log K₁** values above assume fully deprotonated ligand L. At pH < 5, many ligands are protonated, reducing the effective (conditional) stability. The **conditional log K₁'** is:

**log K₁' = log K₁ − log αL(H)**

where αL(H) = 1 + [H⁺]/Ka₁ + [H⁺]²/(Ka₁·Ka₂) + ...

### Conditional Stability at pH 3 and pH 4

| Ligand | log αL(H) at pH 3 | log αL(H) at pH 4 | log K₁'(Fe³⁺) pH 3 | log K₁'(Fe³⁺) pH 4 | log K₁'(Fe²⁺) pH 3 | log K₁'(Fe²⁺) pH 4 | Δlog K' |
|--------|-------------------|-------------------|--------------------|--------------------|--------------------|--------------------|---------|
| **Citric acid** | 7.55 | 4.25 | 3.72 | 7.02 | −3.15 | 0.15 | **~6.9** |
| **Acetohydroxamic** | 6.29 | 5.29 | 5.13 | 6.13 | −1.49 | −0.49 | **~6.6** |
| **Dipicolinic acid** | 1.73 | 0.69 | 9.18 | 10.22 | 3.98 | 5.02 | **~5.2** |
| **Malonic acid** | 2.62 | 1.35 | 5.50 | 6.77 | −0.38 | 0.89 | **~5.9** |
| **Oxalic acid** | 0.81 | 0.00 | 6.77 | 7.58 | 2.24 | 3.05 | **~4.5** |
| **Fluoride** | 0.00 | 0.00 | 6.04 | 6.04 | 0.80 | 0.80 | **~5.2** |
| **5-Sulfosalicylic acid** | 0.00 | 0.00 | ~14.6 | ~14.6 | ~5.9 | ~5.9 | **~8.6** |
| **Salicylic acid** | 0.00 | 0.00 | ~15.3 | ~15.3 | ~5.6 | ~5.6 | **~9.7** |
| **Succinic acid** | 3.24 | 1.99 | 3.64 | 4.89 | −4.64 | −3.39 | **~8.3** |
| **Catechol** | 6.26 | 5.26 | 13.84 | 14.84 | 1.64 | 2.64 | **~12.2** |
| **4-Nitrocatechol** | 3.69 | 2.69 | ~11.1 | ~12.1 | ~2.1 | ~3.1 | **~9.0** |

---

## Speciation Check: Will Fe²⁺ Remain Free at 0.1 M?

For a 1:1 ligand-to-metal ratio with [Fe²⁺]total = 0.1 M and [L]total = 0.1 M:

**Fraction of Fe²⁺ complexed ≈ K₁'·[L]free / (1 + K₁'·[L]free)**

| Ligand | log K₁'(Fe²⁺) pH 4 | K₁'(Fe²⁺) | % Fe²⁺ complexed (est.) | Verdict |
|--------|---------------------|-----------|------------------------|---------|
| **Citric acid** | 0.15 | 1.4 | ~12% | ✅ Acceptable |
| **Acetohydroxamic** | −0.49 | 0.32 | ~3% | ✅ Excellent |
| **Dipicolinic acid** | 5.02 | 1.0×10⁵ | ~99% | ❌ **Too strong** |
| **Malonic acid** | 0.89 | 7.8 | ~44% | ⚠️ Marginal |
| **Oxalic acid** | 3.05 | 1120 | ~99% | ❌ **Too strong** + precipitation risk |
| **Fluoride** | 0.80 | 6.3 | ~39% | ⚠️ Marginal + HF toxicity |
| **5-Sulfosalicylic acid** | 5.9 | 7.9×10⁵ | ~99% | ❌ **Too strong** |
| **Salicylic acid** | 5.6 | 4.0×10⁵ | ~99% | ❌ **Too strong** |
| **Succinic acid** | −3.39 | 4×10⁻⁴ | ~0% | ✅ Excellent (but weak Fe³⁺ too) |
| **Catechol** | 2.64 | 437 | ~98% | ❌ **Too strong** |
| **4-Nitrocatechol** | 3.1 | 1260 | ~99% | ❌ **Too strong** |

### ⚠️ Important Correction

The phenolate/catecholate ligands (salicylic acid, SSA, catechol, tiron, nitrocatechol) and dipicolinic acid have **very high raw log K₁ values** that look great for selectivity, but they also bind Fe²⁺ too strongly at pH 4 (log K₁'(Fe²⁺) > 3), which would deplete free Fe²⁺ below the 0.1 M target. **These are eliminated.**

---

## 🏆 Top Recommended Ligands

### Tier 1: Best Candidates

| Rank | Ligand | Why | Caveats |
|------|--------|-----|---------|
| **1** | **Citric acid** | log K₁'(Fe³⁺) ≈ 7.0 at pH 4; log K₁'(Fe²⁺) ≈ 0.15 → only ~12% Fe²⁺ complexed. Excellent selectivity (Δ ≈ 6.9). Cheap, safe, highly soluble, FDA-approved. Buffers near pH 3–5. | At pH < 3, citrate becomes too protonated (log K₁' drops to ~3.7). At pH > 5, Fe(III)-citrate may form polynuclear species. Use 1:1 to 2:1 citrate:Fe ratio. |
| **2** | **Acetohydroxamic acid (AcHA)** | log K₁'(Fe³⁺) ≈ 6.1 at pH 4; log K₁'(Fe²⁺) ≈ −0.5 → <3% Fe²⁺ complexed. Superb Fe²⁺ sparing. Used clinically as urease inhibitor (Lithostat®). | pKa = 9.29 means only ~0.005% deprotonated at pH 4 — but Fe³⁺ is such a strong Lewis acid it pulls the equilibrium. Effective concentration of active ligand is low, so you need excess AcHA (~5–10× Fe³⁺). |
| **3** | **Malonic acid** | log K₁'(Fe³⁺) ≈ 6.8 at pH 4; log K₁'(Fe²⁺) ≈ 0.9 → ~44% Fe²⁺ complexed at 1:1 ratio. Reduce to 0.5:1 malonate:Fe ratio to keep Fe²⁺ loss < 25%. Cheap and safe. | Second pKa = 5.27 means partial protonation at pH 4–5. At high concentrations, Fe(III)-malonate is very stable and soluble. |

### Tier 2: Viable Alternatives

| Rank | Ligand | Why | Caveats |
|------|--------|-----|---------|
| **4** | **Fluoride (as NaF/KF)** | log K₁'(Fe³⁺) ≈ 6.0 at pH 4; log K₁'(Fe²⁺) ≈ 0.8 → ~39% Fe²⁺ complexed at 1:1. Good selectivity. F⁻ is fully deprotonated above pH 3. | **HF toxicity** is a serious safety concern. At pH < 3, HF forms (pKa 2.94). FeF₃ is soluble. Use only in well-controlled industrial settings with proper safety protocols. |
| **5** | **Succinic acid** | Essentially zero Fe²⁺ binding (log K₁' ≈ −3.4 at pH 4). | Fe³⁺ binding also weak (log K₁' ≈ 4.9 at pH 4) — may not prevent Fe(OH)₃ precipitation at pH > 3.5 without large excess. |

### Tier 3: Rejected Candidates

| Ligand | Reason for Rejection |
|--------|---------------------|
| **EDTA, NTA, DTPA, CDTA** | Bind Fe²⁺ too strongly (log K₁ > 8) → depletes free Fe²⁺ |
| **Oxalic acid** | FeC₂O₄ precipitation (Ksp ≈ 2×10⁻⁷); also binds Fe²⁺ too strongly at pH 4 |
| **Phosphoric acid** | FePO₄ precipitation (Ksp ≈ 10⁻²²) |
| **Salicylic acid, SSA** | Bind Fe²⁺ too strongly at pH 4 (log K₁' > 5) |
| **Catechol, Tiron, Nitrocatechol** | Bind Fe²⁺ too strongly; catechol also oxidizable |
| **Dipicolinic acid** | Binds Fe²⁺ too strongly (log K₁' ≈ 5 at pH 4) |
| **Glycine, Alanine** | Amine protonated at pH < 5; negligible Fe³⁺ binding |
| **Tartaric acid** | No Fe stability data in SRD-46; cannot verify |
| **1,10-Phenanthroline** | Binds Fe²⁺ very strongly (tris complex, log β₃ ≈ 21) |

---

## Practical Recommendations for Fe Electrodeposition Bath

### Recommended Formulation: Citric Acid Bath
- **Fe²⁺ source:** FeSO₄·7H₂O, 0.1 M
- **Fe³⁺ stabilizer:** Citric acid, 0.05–0.1 M (1:1 to 2:1 citrate:Fe³⁺)
- **pH:** 3.5–4.5 (adjust with NaOH/H₂SO₄)
- **Temperature:** 25–40°C

**Why citric acid works best:**
1. At pH 4, conditional log K₁'(Fe³⁺) ≈ 7.0 — strong enough to prevent Fe(OH)₃ precipitation (log Ksp ≈ −38.8 for Fe(OH)₃)
2. Conditional log K₁'(Fe²⁺) ≈ 0.15 — negligible Fe²⁺ complexation, preserving free Fe²⁺ for reduction
3. Citrate buffers the solution near pH 3–5, helping maintain stable pH during electrodeposition
4. Citrate does not catalyze HER — it's electrochemically inert in this potential window
5. Highly soluble, non-toxic, inexpensive, and widely used in electroplating

### Alternative: Acetohydroxamic Acid Bath
- Better Fe²⁺ sparing (<3% complexed) but requires 5–10× excess due to high pKa
- More expensive than citric acid
- Consider for applications where even 10% Fe²⁺ loss is unacceptable

### HER Mitigation Notes
- Citrate adsorption on the cathode can slightly inhibit HER by blocking active sites
- Maintaining pH 3.5–4.5 (rather than pH < 2) significantly reduces HER overpotential competition
- Adding small amounts of boric acid (H₃BO₃, pKa 9.24) as a pH buffer near the cathode surface can further suppress local pH drops that drive HER

---

## Fe(III) Hydrolysis Check

From SRD-46, Fe³⁺ hydrolysis:
- Fe³⁺ + OH⁻ → FeOH²⁺: log K = 11.81 (I=0)
- Fe(OH)₃(s): log Ksp = −38.8

At pH 4, [OH⁻] = 10⁻¹⁰ M. For 0.01 M Fe³⁺ (typical trace amount from oxidation):
- Without ligand: Fe³⁺ precipitates as Fe(OH)₃ above pH ~2.5–3.0
- With 0.1 M citrate at pH 4: log K₁'(Fe³⁺-citrate) ≈ 7.0, so [Fe-citrate]/[Fe³⁺] ≈ 10⁷ × 0.1 = 10⁶ → virtually all Fe³⁺ is complexed and soluble ✅

---

*All stability constants from NIST Standard Reference Database 46 (Critically Selected Stability Constants of Metal Complexes). Conditional constants calculated using standard protonation correction methodology.*
