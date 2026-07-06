Here’s a quick, data‑grounded orientation to mercury complexes in SRD‑46, focusing on what’s well covered and the key aqueous ligands you can use to explore further.

Coverage in SRD‑46 (entities and counts)
| metal_id | species (SRD name) | charge | beta_def_count | ligand_count | vlm_count |
|---|---|---|---:|---:|---:|
| metal_71 | Hg2+ (Hg^[2+]) | +2 | 68 | 310 | 1097 |
| metal_72 | Hg+ (Hg^[+]) | +1 | 12 | 31 | 83 |
| metal_93 | MeHg+ (methylmercury, MHg^[+]) | +1 | 18 | 79 | 148 |
| metal_53 | EtHg+ (ethylmercury, EHg^[+]) | +1 | 4 | 3 | 6 |

Key aqueous ligands (IDs you can query; selected pKa data where available)
| ligand_id | ligand | class | charge/state near neutral pH | pKa notes (water, from SRD‑46) |
|---|---|---|---|---|
| ligand_10163 | chloride (Cl−) | Inorganic ligands | −1 | — |
| ligand_10168 | bromide (Br−) | Inorganic ligands | −1 | — |
| ligand_10171 | iodide (I−) | Inorganic ligands | −1 | — |
| ligand_10076 | hydroxide (OH−) | Inorganic ligands | −1 | pKa(H2O) ≈ 13.78 band shown |
| ligand_10144 | hydrogen sulfide (H2S/HS−) | Inorganic ligands | HL/H2L; HS− at basic pH | H2S ⇌ HS− pKa ≈ 6.82 |
| ligand_10090 | hydrogen cyanide (HCN/CN−) | Inorganic ligands | HL at pH < 9; CN− > pH ~9 | pKa ≈ 9.04 |
| ligand_10103 | ammonia (NH3/NH4+) | Inorganic ligands | L; becomes NH4+ below ~pH 9.3 | pKa(NH4+) ≈ 9.26 |
| ligand_7029 | ethylenediamine (en) | Aliphatic amines | HL at pH ~7–10 | pKa1 ≈ 7.11; pKa2 ≈ 9.92 |
| ligand_5856 | L‑cysteine | Amino acids (thiol) | thiolate emerges ≥HL | pKa(SH) ≈ 8.18 (S); other sites: −1.9, 10.3 |
| ligand_6592 | glutathione (GSH/GS−) | Peptides (thiol) | GS− above pH ~9 | pKa steps: … 8.64 → 9.51 (thiol/amine band) |

Speciation network example (Hg2+–chloride)
| metal_id | ligand_id | network_id | condition summary |
|---|---|---|---|
| metal_71 | ligand_10163 (Cl−) | ref_eq_net_29920 | 19–29 °C, near room temp; low ionic strength (~0 M) |

Notes and chemistry insight
- SRD‑46 has deep coverage for Hg2+ complexes across many ligand families, and smaller but meaningful coverage for Hg+ and MeHg+. Halides (Cl−, Br−, I−), soft sulfur donors (HS−/thiolates like cysteine, glutathione), cyanide, and amines are canonical aqueous partners.
- pKa context matters: thiolate formation (e.g., GS−, Cys−) increases above pH ~8–9, aligning with strong Hg–S binding expected for a soft Lewis acid like Hg2+; CN− availability rises above pH ~9; NH3 is mostly unprotonated near neutral-to-basic pH.
- We attempted to pull matched-condition (25 °C, low ionic strength) stability constants for these systems; within those strict filters, no values surfaced in this pass. A broader filter (e.g., include common background electrolytes such as NaCl or higher ionic strengths, and allow temperatures outside 23–27 °C) typically reveals the familiar Hg–Clx and Hg–SR speciation constants in SRD‑46.

If you’d like, I can re-run stability pulls with relaxed conditions (e.g., include 20–30 °C and ionic strength up to ~1–3 M, and allow chloride media) and assemble a compact table of representative β or stepwise constants for Hg2+, Hg+, and MeHg+ with the ligands above.

Source: NIST SRD‑46 (Critical Stability Constants of Metal Complexes).

---