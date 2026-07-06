# Cu²⁺ vs Ni²⁺ Selectivity with Amino-Acid Ligands at pH 7

*Source: NIST SRD-46 — Cu²⁺ = metal_41, Ni²⁺ = metal_112, 25 °C, I = 0.1 M*

---

## Raw Stability Constants (ML, 1:1 complex, log β)

| Ligand | log β₁ Cu²⁺ | log β₁ Ni²⁺ | **Δlog β** | Selectivity ratio |
|--------|-------------|-------------|------------|-------------------|
| β-Alanine | 7.10 | 4.80 | 2.30 | ~200× |
| Glycine | 8.57 | 6.18 | 2.39 | ~245× |
| Glutamic acid | 8.83 | 6.71 | 2.12 | ~130× |
| Aspartic acid | 8.90 | 6.84 | 2.06 | ~115× |
| Tyrosine | 8.70 | 6.60 | 2.10 | ~125× |
| Alanine | 8.54 | 6.00 | 2.54 | ~350× |
| Phenylalanine | 8.55 | 5.90 | 2.65 | ~450× |
| **Histidine** | **10.20** | **8.74** | **1.46** | **~29×** |
| **Cysteine** | **12.00** | **9.00** | **3.00** | **~1000×** |

---

## pH 7 Conditional Stability (log β′ = log β − log α_L)

At pH 7, the dominant protonation correction is **log α_L ≈ pKa(amine) − 7** for the amine group. Because α_L is the same for both metals, the **selectivity gap Δlog β is pH-independent** — but the absolute conditional stability determines whether the complex actually forms.

| Ligand | Key pKa values | log α_L (pH 7) | log β′₁ Cu²⁺ | log β′₁ Ni²⁺ | **Δlog β′** |
|--------|---------------|----------------|--------------|--------------|-------------|
| β-Alanine | 3.51, 10.08 | 3.08 | 4.02 | 1.72 | 2.30 |
| Glycine | 2.33, 9.57 | 2.57 | 6.00 | 3.61 | 2.39 |
| Alanine | 2.33, 9.71 | 2.71 | 5.83 | 3.29 | 2.54 |
| Phenylalanine | 2.18, 9.09 | 2.09 | 6.46 | 3.81 | 2.65 |
| Glutamic acid | 2.16, 4.15, 9.58 | 2.73 | 6.10 | 3.98 | 2.12 |
| Aspartic acid | 1.95, 3.71, 9.66 | 3.37 | 5.53 | 3.47 | 2.06 |
| Tyrosine | 2.24, 9.04, 10.10 | 2.04 | 6.66 | 4.56 | 2.10 |
| **Histidine** | **1.70, 6.05, 9.10** | **2.15** | **8.05** | **6.59** | **1.46** |
| **Cysteine** | **1.90, 8.18, 10.30** | **4.48** | **7.52** | **4.52** | **3.00** |

> *Histidine's low log α_L (2.15) benefits from the imidazole pKa = 6.05 — at pH 7 the imidazole is ~90% deprotonated and available for coordination, keeping the conditional stability high. Cysteine's thiol pKa = 8.18 means only ~6% is deprotonated at pH 7, but the raw Δlog β is so large (3.00) that the selectivity gap is fully preserved.*

---

## 🏆 Recommendation

### For maximum Cu²⁺/Ni²⁺ selectivity ratio → **Cysteine**
- **Δlog β = 3.00** → **~1000:1 selectivity** (the largest gap of all amino acids tested)
- Conditional log β′(Cu²⁺) = **7.52** at pH 7 — still strong enough for effective complexation
- The thiol–amino–carboxylate tridentate set exploits Cu²⁺'s borderline-soft character far more than Ni²⁺'s harder preference
- **Caveat:** cysteine is air-oxidisable; use under inert atmosphere or with a reducing agent

### For best absolute complexation at pH 7 with reliable selectivity → **Histidine**
- **log β′(Cu²⁺) = 8.05** at pH 7 — the highest conditional stability of all amino acids tested
- **Δlog β = 1.46** → ~29:1 selectivity — lower ratio than cysteine, but the complex is far more stable and the ligand is air-stable
- The imidazole N (pKa 6.05) + α-amino N + carboxylate O form a stable tridentate chelate that is uniquely suited to pH 7 operation
- Histidine is the dominant Cu²⁺-binding residue in biology (copper chaperones, ceruloplasmin) for exactly this reason

### Summary table

| Priority | Best ligand | Δlog β | log β′(Cu²⁺) at pH 7 | Selectivity |
|----------|-------------|--------|----------------------|-------------|
| Maximum selectivity ratio | **Cysteine** | 3.00 | 7.52 | ~1000× |
| Best stability + good selectivity | **Histidine** | 1.46 | 8.05 | ~29× |
| Simple, air-stable, moderate selectivity | **Phenylalanine** | 2.65 | 6.46 | ~450× |

---

**Chemistry insight:** The Irving-Williams series (Mn < Fe < Co < Ni < **Cu** > Zn) guarantees Cu²⁺ > Ni²⁺ for all O/N/S donors, but the *magnitude* of the gap depends on donor softness. Cysteine's thiol is the softest donor among common amino-acid side chains, and Cu²⁺ is significantly softer than Ni²⁺, which maximises the Δlog β to 3.00 log units. Histidine's imidazole, while not as soft, provides the highest absolute affinity at pH 7 because it remains deprotonated and coordinating at physiological pH — making it the ligand of choice when you need both selectivity and robust complexation under biological conditions.

---