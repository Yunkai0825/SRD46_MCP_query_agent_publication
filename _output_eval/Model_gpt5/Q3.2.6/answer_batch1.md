| Quantity | Value | Conditions | Source (SRD-46) |
|---|---|---|---|
| pKa1 (H2L ⇌ HL− + H+) | 2.65 | 25°C, I = 0.10 M | ligand_8873 (vlm_151949) |
| pKa2 (HL− ⇌ L2− + H+) | 5.27 | 25°C, I = 0.10 M | ligand_8873 (vlm_151918) |
| log K(ML) for Cu²⁺ + L2− ⇌ ML | 5.04 | 25°C, I = 0.10 M | metal_41 + ligand_8873, beta_def_812 (ref_eq_map_20105) |
| log K(MHL) for Cu²⁺ + HL− ⇌ MHL | 2.08 | 25°C, I = 0.10 M | metal_41 + ligand_8873, beta_def_779 (vlm_152328) |

| Species | α at pH 4 | log K | log K′(pH 4) |
|---|---:|---:|---:|
| ML (binds L2−) | 0.0489 | 5.04 | 3.73 |
| MHL (binds HL−) | 0.910 | 2.08 | 2.04 |
| Apparent total (ML + MHL) | — | — | 3.74 |

How it was computed
- At pH 4, [H+] = 10⁻⁴. From pKa1 = 2.65 and pKa2 = 5.27, K1 = 10⁻²·⁶⁵ and K2 = 10⁻⁵·²⁷. The malonic-acid fraction terms are α(H2L) = [H+]²/D, α(HL−) = [H+]K1/D, α(L2−) = K1K2/D, where D = [H+]² + [H+]K1 + K1K2. This gives α(L2−) = 0.0489 and α(HL−) = 0.910 at 25°C, I = 0.10 M.
- The conditional stability constant for the ML species at pH 4 is K′(ML) = K(ML)·α(L2−); thus log K′(ML) = log K(ML) + log10 α(L2−) = 5.04 + log10(0.0489) ≈ 3.73.
- If the protonated complex MHL is considered, K′(MHL) = K(MHL)·α(HL−) → log K′(MHL) ≈ 2.08 + log10(0.910) ≈ 2.04. The apparent conditional constant against total unbound ligand is K′(total) ≈ K′(ML) + K′(MHL), giving log K′(total) ≈ 3.74.

Insight
At pH 4 the ligand is mostly HL−, so although MHL has a large α, its intrinsic log K is much smaller; ML still dominates the conditional stability because its intrinsic log K is high even after discounting by the modest fraction of L2−. Matching temperature and ionic strength (25°C, I = 0.10 M) between pKa and metal–ligand constants is essential for a consistent estimate.

Source: NIST Standard Reference Database 46 (SRD-46).

---