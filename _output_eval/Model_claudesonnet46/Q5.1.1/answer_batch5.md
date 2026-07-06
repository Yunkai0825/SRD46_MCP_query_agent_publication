# 🧪 Mercury Complexes in NIST SRD-46 — Complete Overview

## Mercury Species in the Database

SRD-46 contains data for **8 mercury-containing metal entities**. Three are data-rich and scientifically significant:

| Metal ID | Species | Ligands | VLM Measurements |
|---|---|---|---|
| metal_71 | **Hg²⁺** (mercuric ion) | 310 | 1,097 |
| metal_93 | **MeHg⁺** (methylmercury) | 79 | 148 |
| metal_72 | **Hg⁺** (mercurous ion) | 31 | 83 |
| metal_136 | PhHg⁺ (phenylmercury) | 8 | 8 |
| metal_53 | EtHg⁺ (ethylmercury) | 3 | 6 |

Hg²⁺ is by far the most studied, with over **1,000 measurements across 310 ligands** — placing it among the most extensively characterized metals in the entire database.

---

## Ligand Class Distribution for Hg²⁺

Based on all 1,097 VLM records for metal_71:

| Ligand Class | Count | % of Total |
|---|---|---|
| Inorganic ligands (halides, CN⁻, SCN⁻, OH⁻, S²⁻…) | 253 | 23.1% |
| EDTA and derivatives | 109 | 9.9% |
| Miscellaneous ureas, hydrazides, amidines | 79 | 7.2% |
| Amino acids | 76 | 6.9% |
| Aliphatic amines (primary N) | 74 | 6.8% |
| Miscellaneous sulfides | 40 | 3.7% |
| Carboxylic acids (polyacids) | 39 | 3.6% |
| Aza-macrocycles | 39 | 3.6% |
| Aliphatic amines (secondary N) | 36 | 3.3% |
| Pyridine carboxylic acids | 29 | 2.6% |
| Carboxylic acids (simple) | 29 | 2.6% |
| NTA and derivatives | 28 | 2.6% |
| Bipyridines | 28 | 2.6% |
| Aza-oxa-macrocycles | 23 | 2.1% |
| Carboxylic acids with S/Se/Te/P/As donors | 20 | 1.8% |
| Aza macrocycles with carboxylates | 19 | 1.7% |
| Pyridines / azines | 17 | 1.6% |
| Tripyridines | 14 | 1.3% |
| Pyrroles / azoles | 14 | 1.3% |
| Crown ethers | 12 | 1.1% |
| Amides | 12 | 1.1% |
| Iminodiacetic acid and derivatives | 11 | 1.0% |

---

## Halide Stability Constants for Hg²⁺ (Actual SRD-46 Data)

These cumulative log β values were retrieved directly from the SRD-46 equilibrium networks at **25°C, I = 0.5 M**:

| Ligand | log β₁ | log β₂ | log β₃ | log β₄ |
|---|---|---|---|---|
| **Chloride (Cl⁻)** | 6.74 | 13.22 | 14.07 | 15.07 |
| **Bromide (Br⁻)** | 9.05 | 17.33 | 19.74 | 21.00 |
| **Iodide (I⁻)** | 12.87 | — | — | — |

> β_n is the cumulative stability constant for [HgXₙ]^(2−n). The dramatic increase from Cl⁻ to Br⁻ to I⁻ is a hallmark of soft-acid behavior.

---

## Key Chemistry Insights

### 🟡 Hg²⁺ is the Archetypal Soft Lewis Acid
The halide trend Cl⁻ ≪ Br⁻ < I⁻ (log β₁: 6.74 → 9.05 → 12.87) is a textbook demonstration of **Hard-Soft Acid-Base (HSAB) theory**. Hard metals like Ca²⁺ or Mg²⁺ barely bind halides; Hg²⁺ forms extraordinarily stable complexes with the softest halide, I⁻. The stepwise constants also reveal that Hg²⁺ strongly favors 4-coordinate tetrahedral halide complexes (e.g., [HgI₄]²⁻), one of the most stable halide complexes of any metal.

### 🔵 Inorganic Ligands Dominate (23% of All Data)
The largest single ligand class is inorganic — halides, cyanide, thiocyanate, hydroxide, and sulfide. This reflects Hg²⁺'s central importance in **environmental geochemistry**: speciation among Cl⁻, Br⁻, and HS⁻ in natural waters controls mercury solubility, mobility, and bioavailability. The sulfide complexes (HgS, [Hg(HS)₂]) are particularly important in anoxic sediments.

### 🟢 Organomercury Species Are Toxicologically Critical
**Methylmercury (MeHg⁺, metal_93)** has 148 measurements across 79 ligands — a rich dataset driven by its extreme neurotoxicity. MeHg⁺ is produced by anaerobic bacteria (sulfate-reducing bacteria) in sediments via biomethylation of Hg²⁺, and it bioaccumulates up the food chain. Its strong preference for thiol groups (cysteine, glutathione) explains its ability to cross the blood-brain barrier and cause neurological damage. The SRD-46 data for MeHg⁺ spans amino acids, peptides, and sulfur-donor ligands — all relevant to its biological speciation.

### 🔴 EDTA and Macrocycles Are Well-Represented
EDTA and its derivatives account for nearly **10% of all Hg²⁺ measurements**, reflecting both analytical chemistry applications (complexometric titrations) and environmental remediation research. Aza-macrocycles (39 measurements) and aza-oxa-macrocycles (23 measurements) are also well-studied, as their preorganized cavities can be tuned to selectively capture Hg²⁺ over other metals — a strategy for mercury sensing and removal.

### 🟣 Mercurous Hg⁺ Is a Special Case
Hg⁺ (metal_72) exists in solution as the **dimeric Hg₂²⁺** species, not as a simple mononuclear ion. With 31 ligands and 83 measurements, it is far less studied than Hg²⁺, and its complexes are generally weaker due to the lower effective charge density and steric constraints of the dimer. Many ligands that bind Hg²⁺ strongly will actually oxidize or disproportionate Hg₂²⁺.

---

## Summary

Mercury's coordination chemistry in SRD-46 is vast and chemically diverse. The data spans **simple inorganic halides** through **macrocyclic chelators**, **amino acids**, **sulfur donors**, and **organomercury species** — reflecting decades of research driven by mercury's environmental toxicity, industrial uses, and fundamental interest as the softest common divalent metal. The halide stability constants retrieved here (log β₁ = 6.74 for Cl⁻, 9.05 for Br⁻, 12.87 for I⁻) quantitatively confirm the HSAB prediction and illustrate why iodide-functionalized sorbents are among the most effective materials for mercury capture.

---

> **Source:** NIST SRD-46 — Critically Selected Stability Constants of Metal Complexes Database

---