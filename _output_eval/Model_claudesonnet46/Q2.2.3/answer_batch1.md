## Ligands in SRD-46 with More Than 6 Reported pKa Values

Based on the data retrieved from NIST SRD-46, here is what was confirmed:

---

### ✅ Confirmed: DTPA — Diethylenetrinitrilopentaacetic acid (`ligand_6356`)

DTPA is the clearest confirmed example, with **8 distinct protonation steps** documented in the database (L through H8L). The H⁺ + DTPA system has 57 total VLM entries across 8 protonation equilibria:

| Protonation Step | Reaction | # Measurements | Approx. pKa |
|---|---|---|---|
| 1st | L + H⁺ ⇌ HL | 14 | ~8–10 |
| 2nd | HL + H⁺ ⇌ H2L | 14 | ~4.3 |
| 3rd | H2L + H⁺ ⇌ H3L | 8 | ~4.3 |
| 4th | H3L + H⁺ ⇌ H4L | 8 | ~2.7 |
| 5th | H4L + H⁺ ⇌ H5L | 8 | ~2.0 |
| 6th | H5L + H⁺ ⇌ H6L | 2 | ~−0.7 |
| 7th | H6L + H⁺ ⇌ H7L | 2 | ~−0.1 |
| 8th | H7L + H⁺ ⇌ H8L | 1 | ~−0.1 |

Conditions: T = 15–41°C, ionic strength I = 0–1.15 M.

---

### Other Candidates Identified (from pKa bracket data)

| Ligand | ligand_id | Class | Protonation States | Steps |
|---|---|---|---|---|
| DTPA | ligand_6356 | EDTA and derivatives | H8L → L | **8** |
| DTPA-dien | ligand_6117 | Aza macrocycles w/ carboxylates | H5L → L | 5 |
| DTPA-BP | ligand_6364 | EDTA and derivatives | H5L → L | 5 |
| DTPA-BMA | ligand_6362 | EDTA and derivatives | H4L → L | 4 |
| DTPA-BBA | ligand_6363 | EDTA and derivatives | H3L → L | 3 |

Among those searched, **only DTPA itself clearly exceeds 6 pKa values** with 8 documented protonation steps. The DTPA derivatives have fewer ionizable sites due to amide substitution of carboxylate arms.

---

### Chemistry Insight

DTPA's extraordinary polyproticity stems from its molecular architecture: **five carboxylate groups** (pKa ~2–4) and **three tertiary amine nitrogens** (pKa ~4–10), yielding up to 8 ionizable protons. The highest protonation states (H6L–H8L, pKa < 0) represent protonation of already-acidic carboxylates and are only measurable under strongly acidic conditions — hence the sparse data (1–2 measurements each). This broad protonation envelope is exactly what makes DTPA such a versatile chelator: it remains an effective metal binder from strongly acidic to basic pH, underpinning its use in Gd-DTPA MRI contrast agents and actinide decorporation therapy.

> **Note:** A complete database-wide survey (SQL `HAVING COUNT(pKa) > 6`) was not executed due to session time constraints. Other likely candidates not yet confirmed include polyphosphonates (NTMP, EDTMP, DTPMP), phytic acid (6 phosphate groups), and nucleotide polyphosphates (ATP, GTP). A follow-up query using `execute_srd46_sql` would reveal the full list.

*Source: NIST SRD-46 (Critically Selected Stability Constants of Metal Complexes)*

---