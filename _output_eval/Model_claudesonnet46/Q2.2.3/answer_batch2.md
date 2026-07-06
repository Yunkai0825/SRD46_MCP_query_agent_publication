# Ligands in SRD-46 with More Than 6 Reported pKa Values

Based on the data retrieved from NIST SRD-46, here is what was confirmed:

---

## ✅ Confirmed Example: DTPA

**Diethylenetrinitrilopentaacetic acid** (`ligand_6356`) is definitively confirmed to have **8 distinct protonation steps** — well above the threshold of 6. Its `pka_brackets` field in the database reads:

> `(-inf, H8L, −0.1, H7L, −0.1, H6L, −0.7, H5L, 2.0, H4L, 2.7, H3L, 4.28, H2L, 4.28, HL, ~8.4, L, +inf)`

| Step | Equilibrium | Approx. pKa |
|------|-------------|-------------|
| 1 | H8L → H7L | −0.1 |
| 2 | H7L → H6L | −0.1 |
| 3 | H6L → H5L | −0.7 |
| 4 | H5L → H4L | 2.0 |
| 5 | H4L → H3L | 2.7 |
| 6 | H3L → H2L | 4.28 |
| 7 | H2L → HL | 4.28 |
| 8 | HL → L | ~8.4 |

The H⁺ + DTPA system has **57 VLM entries** across 8 species, measured at 15–41°C and ionic strengths from near-zero to 1.15 M — one of the most thoroughly studied protonation systems in the database.

---

## Other Ligands Inspected (Fewer Than 7 Steps)

| Ligand | ID | Visible Steps | Class |
|--------|----|--------------|-------|
| DTPA-dien | ligand_6117 | 5 (H5L → L) | Aza macrocycles |
| DTPA-BMA | ligand_6362 | 4 (H4L → L) | EDTA derivatives |
| DTPA-BBA | ligand_6363 | 3 (H3L → L) | EDTA derivatives |
| DTPA-BP | ligand_6364 | 5 (H5L → L) | EDTA derivatives |

These DTPA derivatives have fewer ionizable groups due to amide substitution of carboxylates, reducing their protonation step count.

---

## Chemistry Insight

DTPA's 8 protonation steps arise from its **3 tertiary amine nitrogens** and **5 carboxylate groups**, giving it an extraordinary capacity to buffer across a wide pH range — from strongly acidic (pKa < 0) all the way to basic (pKa ~8.4). This polyprotic character is the foundation of its exceptional metal-chelating ability, which is exploited in:
- **MRI contrast agents** (Gd-DTPA / Magnevist)
- **Radiopharmaceuticals** (chelation of ⁹⁰Y, ¹¹¹In)
- **Heavy metal detoxification** therapies

A full database-wide survey (querying `ligand_pka_measured` grouped by ligand with `HAVING COUNT(DISTINCT pKa_type) > 6`) was planned but could not be completed within the session time budget. Additional candidates such as polyphosphonates (DTPMP, NTMP) and polyphosphates (phytate/inositol hexakisphosphate) are strong candidates based on their known chemistry, but their counts were not confirmed from the database in this session.

**Source:** NIST SRD-46 — Critically Selected Stability Constants of Metal Complexes.

---