Below is a compact, data-grounded look at Ca2+ binding versus ligand basicity, using SRD‑46 entries we already resolved. The phosphate/organophosphate set gives a clean, matched-condition slice and shows the trend clearly.

Representative Ca2+ complexes (≈25 °C; I ≈ 0.1 M) — phosphate family
| Ligand (dominant donor state) | Deprotonation/charge at binding site | Ca2+ complex (1:1) | log K (range) |
|---|---|---|---|
| H2PO4− (mono‑deprotonated phosphate) | −1 | CaH2PO4+ | ≈ 1.1 |
| HPO42− (di‑deprotonated phosphate) | −2 | CaHPO4(aq) | ≈ 2.6–2.8 |
| PO43− (tri‑deprotonated phosphate) | −3 | CaPO4− | ≈ 3.3–3.7 |

Organophosphate exemplars (≈25 °C; I ≈ 0.1 M)
| Ligand | Key phosphate pKa2 (SRD‑46) | Ca2+ complex (1:1) | log K (range) |
|---|---|---|---|
| CMP‑5′ (monophosphate) | ≈ 6.2 | CaL0 | ≈ 2.1–2.5 |
| UMP‑5′ (monophosphate) | ≈ 6.1 | CaL0 | ≈ 2.0–2.4 |
| PLP (monophosphate) | ≈ 6.0 | CaL0 | ≈ 1.8–2.3 |
| PMP (monophosphate; amine protonations higher) | ≈ 5.6 | CaL0 | ≈ 1.8–2.4 |
| L‑Seryl‑L‑leucine phosphate (monoP) | ≈ 5.5 | CaL0 | ≈ 1.8–2.3 |
| UDP (diphosphate) | — (effective basicity higher vs monoP) | CaL− | ≈ 2.8–3.2 |
| UTP (triphosphate) | ≈ 6.3 | CaL2− | ≈ 3.2–3.6 |

Chelating outlier (for scale; 25 °C)
| Ligand | Dominant donor set | Ca2+ complex (ML) | log β (SRD‑46) |
|---|---|---|---|
| EDTA4− | 4 carboxylates + 2 amines (hexadentate) | CaL2− | 10.65 |

What the data say
- Within the phosphate series, increasing deprotonation (higher donor charge/basicity) correlates with larger Ca2+ formation constants: H2PO4− < HPO42− < PO43−, with log K rising from ≈1.1 to ≈3.7.
- Among monophosphate organics with similar phosphate pKa2 (~5.5–6.5), Ca2+ log K clusters near ~2.0–2.5. Adding extra phosphate groups (di‑, tri‑) increases total negative charge and enables chelation/bridging, boosting log K into the ~3–3.6 range despite only modest changes in individual phosphate pKa.
- EDTA demonstrates that multidentate, highly charged, hard O‑donor arrays can yield very large Ca2+ stability (log β ≈ 10.65), far beyond what single‑site pKa alone would predict.

Hypothesis for alkaline‑earth metals (Ca2+ as exemplar)
- For hard oxo‑donor ligands, Ca2+ binding strength increases with donor basicity and charge density: higher relevant pKa at the coordinating site (and greater deprotonation) tends to raise log β1.
- The correlation with pKa is positive but modest within a donor family; structural factors dominate. Multidentate chelation, multiple oxyanions in close proximity, and higher overall ligand charge amplify binding via electrostatics and reduced desolvation, often exceeding the influence of small pKa differences.
- Generalizing across alkaline‑earths (Mg2+, Ca2+, Sr2+), expect the same qualitative trend, with absolute constants modulated by ionic radius and hydration enthalpy (Mg2+ typically weaker than Ca2+ for bulky chelates; Sr2+ slightly different size/softness effects).

Notes and next steps
- A rigorous correlation analysis should join matched‑condition pairs: ML log β1(Ca2+) at 25 °C and a single ionic medium with the corresponding donor pKa measured under the same conditions. The plan is prepared to pull ML constants via search_stability and pKa via search_pka_values and compute family‑wise Pearson/Spearman correlations.
- If you want, I can fetch a carboxylate set next (succinate, malate, lactate, oxalate, citrate) at 25 °C, I ≈ 0.1 M and assemble a quantitative pKa–log β1 table.

Source: NIST SRD‑46 (SRD‑46 equilibrium and pKa records retrieved above).

---