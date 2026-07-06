Below is a rapid, data‑grounded snapshot from SRD‑46 followed by an interpretation. Because of time limits, I focused on ligands where both aqueous pKa and Ca2+ ML (beta_def_812, [M]+[L]⇌[ML]) entries at ~25 °C are present; most of these are O‑donor aminopolycarboxylates. The numeric Ca–L constants are present in SRD‑46, but I did not extract the exact logK values in this pass; pKa values shown are those retrieved at ~25 °C.

Evidence snapshot (SRD‑46; water; T ≈ 25 °C)
| Ligand (SRD‑46 ID) | Selected pKa at ~25 °C (assignment) | Ca2+ ML data at ~25 °C (I≈0–0.1 M) | Notes on donors |
|---|---|---|---|
| Hexamethylenedinitrilotetraacetic acid, HMDTA (ligand_6315) | 9.70 (HL→H2L), 10.64 (L→HL); also −2.4 (H3L→H4L) | Yes (beta_def_812; I=0.1 M) | Carboxylate O donors dominate Ca2+ binding; amine pKa (~10–11) not primary donor |
| Tetramethylenedinitrilotetraacetic acid, TMDTA (ligand_6313) | 2.68 (H2L→H3L), 8.98 (HL→H2L), 10.45 (L→HL), 10.66 (L→HL) | Yes (beta_def_812; I=0.1 M) | Similar pattern; carboxylate deprotonations in the 2–3 band |
| Octamethylenedinitrilotetraacetic acid, OMDTA (ligand_6316) | 2.00 (H3L→H4L), 9.86 (HL→H2L), 10.66 (L→HL) | Yes (beta_def_812; I=0.1 M) | Carboxylate pKa near 2–3; amine pKa ~10–11 |
| Decamethylenedinitrilotetraacetic acid, DMDTA (ligand_6317) | 2.03, 2.65 (carboxylates), 9.79, 10.65 (amine protonation) | Yes (beta_def_812; I≈1.0 M also reported) | Longer spacers, same donor set |
| Dodecamethylenedinitrilotetraacetic acid, DoMDTA (ligand_6318) | 2.6 (H2L→H3L), 9.96 (HL→H2L), −10.55 (L→HL, highly clustered) | Yes (Ca entries exist at ~25 °C) | As above |
| N‑Butyliminodiacetic acid, IDA derivative (ligand_6144) | −1.4 (H2L→H3L), 10.07 (L→HL) | Yes (beta_def_812; I≈0 M) | Monofunctional aminodiacetate; Ca data present |

What this says about correlation (from these SRD‑46 pulls)
- The carboxylate deprotonations that create the O− donor occur mostly in a narrow pKa band near 2–3 across aminopolycarboxylate families, while amine protonations cluster ~9–11. Ca2+ is a hard Lewis acid and binds primarily to O‑donors; protonation of tertiary/secondary amines (high pKa) does not create the donor that anchors Ca2+. Thus, the “pKa” that matters for Ca2+ binding is the acidity of the oxygen‑donor site(s), which varies only modestly in these families.
- Consistent Ca2+ ML constants are reported for all entries above at ~25 °C in water (beta_def_812). Because the relevant O‑donor pKa values are tightly clustered, denticity/chelation and geometry dominate the spread in Ca2+ logK1 across these ligands. In other words, within this dataset, pKa alone shows at best a weak positive relationship with ML strength; the chelate effect and ligand preorganization overshadow any simple pKa→logK1 trend.

Hypothesis (for alkaline‑earth metals)
- Within a fixed donor class and denticity (e.g., monodentate or fixed bidentate O‑donors), higher basicity of the O‑donor (i.e., higher pKa for the acid that generates the O− site) should correlate positively with stronger binding: logK1 increases modestly with donor pKa. However, once ligands differ in denticity or topology (polycarboxylates, chelators), chelation and size/geometry matching dominate and largely decouple simple pKa from logK1.
- Across the alkaline‑earth series, the sensitivity of logK1 to donor basicity is expected to increase with metal ionic size/hydration softness (Mg2+ < Ca2+ < Sr2+ < Ba2+): Mg2+ (strongly hydrated) shows weaker, less pKa‑sensitive binding; larger ions sacrifice less hydration penalty and benefit more from increased O‑donor basicity. Thus, within a fixed O‑donor class/denticity, both higher donor pKa and larger cation radius should enhance binding, but chelation and preorganization remain the primary predictors when denticity varies.

Limitations and next steps
- To cleanly quantify correlation, we should restrict to simple O‑donor series where donor pKa varies more appreciably (e.g., monocarboxylates: formate/acetate/propionate/benzoate; α‑hydroxycarboxylates: glycolate/lactate; dicarboxylates: oxalate/malonate/succinate) and extract matched‑condition Ca2+ logK1 (beta_def_812), water, 25 ± 1 °C, fixed ionic strength (e.g., 0.1 M). We began this but did not finish extracting numeric logK1 in this pass.
- With that filtered table (ligand_id, donor‑site pKa, Ca2+ logK1), we can compute Pearson/Spearman correlations overall and within denticity classes, and then repeat for Mg2+/Sr2+/Ba2+ to test the “metal‑size” slope change in the hypothesis.

Source: NIST Standard Reference Database 46 (SRD‑46) — tools used here: build_system_catalog (Ca2+), search_stability (beta_def_812; Ca–ligand ML at ~25 °C), and search_pka_values (aqueous pKa near 25 °C).

---