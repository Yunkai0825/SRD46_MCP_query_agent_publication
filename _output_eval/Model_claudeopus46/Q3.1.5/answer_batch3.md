## Ligands That Bind Ca²⁺ Strongly but Have Relatively Weak Cu²⁺ Affinity

**Key finding:** No ligand in the NIST SRD-46 database binds Ca²⁺ *more* strongly than Cu²⁺ — this is expected from the **Irving-Williams series**, which places Cu²⁺ at the top of divalent first-row transition-metal stability. However, some ligands show a **much smaller selectivity gap**, making them practical Ca²⁺ masking agents that leave trace Cu²⁺ relatively unaffected.

### Matched-Condition Comparison (25 °C, I = 0–0.1 M, aqueous, 1:1 ML β₁)

| Ligand | log β₁(Ca²⁺) | log β₁(Cu²⁺) | Δ (Ca − Cu) | Comment |
|--------|:---:|:---:|:---:|---------|
| **Triphosphate** | 5.06 | 5.35 | **−0.29** | Near-equal affinity; best ratio |
| **Glucose-1-phosphate** | 1.50 | 2.36 | **−0.86** | Weak overall binding |
| **Maleic acid** | 1.58 | 3.64 | −2.06 | Weak Ca²⁺ binding |
| **Succinic acid** | 1.20 | 3.30 | −2.10 | Weak Ca²⁺ binding |
| **Etidronic acid (HEDP)** | 5.20 | 7.41 | **−2.21** | Good Ca²⁺ affinity; small gap |
| **ATP** | 3.93 | 6.34 | −2.41 | Biologically relevant but costly |
| **Pentane-1,1-dicarboxylic acid** | 1.55 | 4.00 | −2.45 | Weak Ca²⁺ binding |
| **Malonic acid** | 1.51 | 5.70 | −4.19 | Moderate gap |
| **N-(2-Hydroxyethyl)iminodiacetic acid** | 4.68 | 8.73 | −4.05 | Mixed N/O donor |
| **Tetramethylene-EDTA** | 7.23 | 13.10 | −5.87 | Longer backbone reduces Cu²⁺ preference |
| **Trimethylene-EDTA (TMDTA)** | 8.52 | 14.50 | −5.98 | Similar effect |
| **NTA** | 6.39 | 12.94 | −6.55 | Classic aminocarboxylate |
| **EGTA** | **10.86** | 17.57 | **−6.71** | Highest absolute Ca²⁺ affinity |
| **EDTA** | 10.61 | 18.70 | −8.09 | Strong but very Cu²⁺-selective |
| **DTPA** | 10.74 | 21.20 | −10.46 | Largest gap; worst for masking |

### Top Practical Recommendations

| Rank | Ligand | Rationale |
|:---:|--------|-----------|
| **1** | **Triphosphate (P₃O₁₀⁵⁻)** | Smallest Δ of only −0.29 with a useful Ca²⁺ log β of 5.1. Pure oxygen donor — no N atoms to boost Cu²⁺ binding. Commercially available as sodium tripolyphosphate. |
| **2** | **Etidronic acid (HEDP)** | Δ = −2.2 with moderate Ca²⁺ affinity (log β = 5.2). Widely used industrial scale inhibitor; stable, inexpensive, and well-characterized. |
| **3** | **EGTA** | Although Δ = −6.7, EGTA has the **highest absolute Ca²⁺ affinity** (log β = 10.9) in this set. It is the classic Ca²⁺-selective chelator in biochemistry. At trace Cu²⁺ levels with large Ca²⁺ excess, Ca²⁺ can kinetically and stoichiometrically dominate binding. |
| **4** | **TMDTA / Tetramethylene-EDTA** | These longer-backbone aminocarboxylates retain strong Ca²⁺ binding (log β ≈ 7–9) while showing a notably smaller Cu²⁺ preference (Δ ≈ −5.9 to −5.9) compared to EDTA (Δ = −8.1). |

### Chemistry Insight

The pattern is clear: **pure oxygen donors (phosphates, phosphonates, simple dicarboxylates) minimize the Ca²⁺/Cu²⁺ selectivity gap**, because Ca²⁺ is a hard Lewis acid that strongly prefers hard O-donors, while Cu²⁺ gains its extra stability primarily through nitrogen coordination (crystal-field stabilization). Every additional N-donor in the ligand widens the gap in Cu²⁺'s favor — compare IDA (Δ = −8.0, one N) → NTA (Δ = −6.6, one N but more carboxylates) → EDTA (Δ = −8.1, two N) → DTPA (Δ = −10.5, three N).

For practical trace-metal analysis, **sodium tripolyphosphate or etidronic acid** added in moderate excess will preferentially complex Ca²⁺ while leaving Cu²⁺ largely available for detection by a selective reagent (e.g., bathocuproine disulfonate or dithizone). If very strong Ca²⁺ sequestration is needed (e.g., in biological buffers), **EGTA** remains the gold standard despite its non-negligible Cu²⁺ affinity.

*Source: NIST Standard Reference Database 46 — Critically Selected Stability Constants of Metal Complexes*

---