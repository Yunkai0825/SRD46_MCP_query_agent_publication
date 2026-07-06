# Qfree_20260423_183227 -- Result (batch 1)

**Section:** freeform -- Fe(III) vs Fe(II) ligand screening

**Prompt:** I would like to find ligands that can complex Fe(III) to stabilize the acidic solution (pH<5), yet with limited complexation to Fe(II) so that it does not decrease the free Fe2+ concentration too much. This is for Fe electrodeposition since we also try to minimize the hydrogen evolution reaction when Fe electrodeposition happens. The expected concentration of Fe(II) is ~0.1M. Meanwhile, be cautious about ligand pH and its actual state, and be cautious about possible precipitations. If there are missing entries, try to observe similar metal-ligand systems with available data to estimate those with very robust reasons and explanations. You have unlimited time and unlimited turns.

**Tool calls:** 15  |  **Time:** 117s planning + 234s execution + 0s verdict = 351s total

---

SRD-46 points to a **small acidic-window shortlist** rather than a perfect ligand. For your goal—**hold Fe(III) in solution at pH < 5, but avoid tying up Fe(II) (~0.1 M) too strongly**—the best-supported candidates in the retrieved SRD-46 data are **5-sulfosalicylic acid**, **salicylic acid**, and then **citric acid** with more caution.

## Best-supported shortlist from SRD-46

| Ligand | Fe(III) evidence in SRD-46 | Fe(II) evidence in SRD-46 | Acid-state / protonation caution | Practical judgment for Fe electrodeposition |
|---|---:|---:|---|---|
| **5-Sulfosalicylic acid** | Fe(III) present; 7 VLM, 3 β-definitions; network summary says richer Fe(III) complexation | Fe(II) present but only 1 VLM / 1 β-definition; network summary says trivial Fe(II) network | COOH pKa ~2.48; phenol remains protonated until much higher pH; sulfonate stays ionized but is a weak donor | **Best current candidate**: likely enough Fe(III) stabilization in pH ~3–5 with comparatively limited Fe(II) loss |
| **Salicylic acid** | Fe(III) present; 11 VLM, 3 β-definitions; network summary richer than Fe(II) | Fe(II) present; 2 VLM, 2 β-definitions | Below ~pH 2 mostly too protonated; at pH 3–5 carboxylate becomes available, phenol mostly protonated | **Good conditional candidate** for **pH ~3–5**, but less water-friendly / less acid-robust than sulfosalicylate |
| **Citric acid** | Fe(III) present; 6 VLM, 4 β-definitions | Fe(II) present more substantially; 11 VLM, 5 β-definitions | pKa 2.9, 4.35, 5.65; donor set turns on across pH 3–5 | **Usable but risky**: good Fe(III) solubilizer, but also more likely to reduce free Fe2+ if overdosed |
| **Glycine** | Fe(III) present; 6 VLM, 3 β-definitions | Fe(II) present; 10 VLM, 3 β-definitions | pKa 2.33, 9.57; amine protonated in acid | **Not attractive**: weakly helpful in strong acid and not clearly selective enough |
| **Diglycine** | Fe(III) present; 1 VLM | Fe(II) present; 1 VLM | Still strongly protonated below pH 5 | **Low priority** |
| **HEDTA-like aminocarboxylate** | Fe(III) present; 7 VLM, 5 β-definitions | Fe(II) also present; 2 VLM, 2 β-definitions | Multidentate ligand still develops donor capacity in pH 3–5 | **Avoid** if preserving free Fe2+ is important |

## pKa-based acidic feasibility

| Ligand | Retrieved pKa information | What that means at pH < 5 |
|---|---|---|
| **Citric acid** | 2.9, 4.35, 5.65 | At pH 3–5, 1–2 carboxylates are available, so Fe(III) binding becomes plausible |
| **Salicylic acid** | ~2.8 for COOH; phenol much less acidic | Real chelation is much better near pH 3–5 than at pH < 2 |
| **5-Sulfosalicylic acid** | ~2.48 for COOH, ~11.85 for phenol; sulfonate strongly acidic | At pH 3–5, carboxylate is available and sulfonate helps solubility; phenol mostly still protonated |
| **Glycine** | 2.33, 9.57 | Mostly zwitterionic / protonated in your window; limited chelation in acid |
| **Diglycine** | 3.11, 8.09 | Similar story; modest donor availability only near upper end of your pH window |

## Recommended ranking for your use case

| Rank | Ligand | Why |
|---:|---|---|
| 1 | **5-Sulfosalicylic acid** | Best SRD-46 balance of **Fe(III)-favored complexation** with **limited Fe(II) evidence**, plus good acid solubility logic |
| 2 | **Salicylic acid** | Also Fe(III)-favored over Fe(II), but more protonation/solubility caution |
| 3 | **Citric acid** | Strong practical Fe(III) stabilizer, but much more likely than the salicylates to **decrease free Fe2+** at meaningful dosage |
| 4 | **Glycine / diglycine** | Too protonated / too weak / not clearly selective enough |
| 5 | **HEDTA-like aminocarboxylates** | Too likely to complex Fe(II) substantially |

## Interpretation for plating-bath design

| Design point | SRD-46-grounded implication |
|---|---|
| **Very low pH (<~2.5)** | None of the retrieved ligands look ideal; most are too protonated, so Fe(III) stabilization by ligand complexation is limited |
| **pH ~3–5** | This is the realistic window where the shortlisted O-donor ligands begin to work |
| **Need to keep free Fe2+ near 0.1 M** | Favor **low-to-moderate ligand concentration** and avoid multidentate aminocarboxylates like HEDTA-like systems |
| **Avoid Fe(III) precipitation/hydrolysis** | Ligands that give some Fe(III) complexation in this window help, but retrieved network summaries did **not explicitly resolve precipitation risk**, so absence of a precipitate node is **not proof of safety** |

## My practical conclusion

| Recommendation | Confidence from SRD-46 |
|---|---|
| Start with **5-sulfosalicylic acid** as first screening additive | **Best supported** |
| Test **salicylic acid** only if bath composition allows its solubility and pH is closer to 3–5 than to 1–2 | **Moderate** |
| Use **citrate** only cautiously and at restrained concentration because it is more likely to tie up Fe(II) | **Moderate, but caution-heavy** |

Chemically, this makes sense: **Fe(III)** is a harder, more hydrolysis-prone ion, so even partially deprotonated O-donor ligands can help keep it soluble, while **Fe(II)** usually needs either higher pH or stronger donor sets to be strongly chelated. That is why **acid-soluble, moderately strong O-donor ligands** often give the best compromise for iron plating baths.

**Source: NIST SRD-46.**

If you want, I can next do a **second-pass SRD-46 screen focused on analog ligands** around **sulfosalicylate / salicylate / citrate families** and build a more explicit **estimated Fe(III)-selectivity ranking with precipitation cautions**.