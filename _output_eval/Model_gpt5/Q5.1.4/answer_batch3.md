Here’s a compact, data‑driven snapshot of zinc(II) in NIST SRD‑46.

Overall coverage (metal_208 = Zn2+)
| Metric | Count / Note |
|---|---|
| Distinct equilibria (β definitions) | ~122 |
| Distinct ligand partners | ~1169 |
| Individual measurements (VLM) | ~4095 |

Most-studied Zn2+ systems in SRD‑46 (sampled top 10 by entry count from catalog)
| Rank | Ligand (SRD name) | Entries | Species count | VLMs | T range (°C) | Ionic strength range (M) | Noted species (examples) |
|---|---|---:|---:|---:|---|---|---|
| 1 | Aminoacetic acid (Glycine) | 37 | 4 | 37 | 5–45 | ~0–1.15 | ML, ML2, ML3, M(OH)L |
| 2 | Ethylenediamine | 36 | 3 | 36 | 19–41 | ~0–3.15 | ML, ML2, ML3 |
| 3 | Hydroxide | 33 | 13 | 33 | 19–30 | ~0–3.15 | ML–ML4, M4L4; solids (ZnL2, ZnO) |
| 4 | Hydrogen cyanide (Hydrocyanic acid) | 30 | 5 | 30 | 5–45 | ~0–3.15 | ML–ML4; 1 solid step |
| 5 | 1,3‑Diazole (Imidazole) | 30 | 4 | 30 | 19–41 | ~0–3.15 | ML–ML4 |
| 6 | L‑Histidine | 29 | 6 | 29 | 19–41 | ~0–3.15 | ML, ML2; protonation/hydrolysis steps |
| 7 | Hydrogen thiocyanate (Thiocyanic acid) | 24 | 4 | 24 | 19–30 | ~0–5.15 | ML–ML4 |
| 8 | L‑Cysteine | 23 | 8 | 23 | 15–41 | ~0–3.15 | protonated, M2L, ML, ML2; hydrolysis |
| 9 | Ammonia | 21 | 4 | 21 | 19–30 | ~0–2.15 | ML–ML4 |
| 10 | Nitrilotris(methylenephosphonic acid) (NTP) | 21 | 5 | 21 | 19–30 | ~0–0.25 | protonation series, ML |

Representative zinc networks (glycine system)
| Network ID | T range (°C) | Ionic strength range (M) | Notes |
|---|---|---|---|
| ref_eq_net_112 | 20–30 | ~0–0.25 | ML, ML2, ML3 |
| ref_eq_net_113 | 31–41 | 0–0.3 | Adds M(OH)L step |
| ref_eq_net_114 | 19–29 | 0.35–0.65 | ML, ML2, ML3 |

Selected stability data (25 °C unless noted)

Zn2+–ammine complexes (aqueous, 25 °C; cumulative formation of Zn(NH3)4²+)
| Complex (reaction basis) | logβ | Ionic strength (M) | Notes |
|---|---:|---:|---|
| Zn2+ + 4 NH3 ⇌ Zn(NH3)4²+ | 8.89 | 0 | ref_eq_map 28172 |
| Zn2+ + 4 NH3 ⇌ Zn(NH3)4²+ | 9.34 | 1 | ref_eq_map 28173 |
| Zn2+ + 4 NH3 ⇌ Zn(NH3)4²+ | 9.73 | 2 | ref_eq_map 28174 |

Zn2+–phosphate ester complexes (25 °C, I = 0.1 M)
| Ligand | Reaction definition (β_def) | Type | Value | vlm_id |
|---|---|---|---:|---|
| Phosphoric acid methyl ester (Methyl phosphate) | [M(OH)L] + [H] ⇌ [ML] + H2O (beta_def_966) | logK | 7.29 | vlm_159408 |
| Phosphoric acid 1‑naphthyl ester (α‑Naphthyl phosphate) | [M(OH)L] + [H] ⇌ [ML] + H2O (beta_def_966) | logK | 6.74 | vlm_159468 |
| Diphosphoric acid butyl ester (Butyl diphosphate) | [M] + [L] ⇌ [ML] (beta_def_812) | logK | 4.40 | vlm_159624 |
| Diphosphoric acid phenyl ester (Phenyl diphosphate) | [M] + [L] ⇌ [ML] (beta_def_812) | logK | 4.06 | vlm_159636 |
| Phosphoric acid butyl ester (Butyl phosphate) | [M] + [L] ⇌ [ML] (beta_def_812) | logK | 2.30 | vlm_159421 |

Zn2+–hydroxo species (25 °C; L = OH−)
| Reaction definition (β_def) | Type | Value | I (M) | vlm_id | Notes |
|---|---|---:|---:|---|---|
| [M] + [L]^4 ⇌ [ML4] (beta_def_894) | logK | 15.5 | 0 | vlm_170939 | Mononuclear Zn(OH)4 species (cumulative) |
| [M] + [L]^4 ⇌ [ML4] (beta_def_894) | logK | 15.4 | 3 | vlm_170938 |  |
| [M]^4 + [L]^4 ⇌ [M4L4] (beta_def_674) | logK | 27.9 | 3 | vlm_170943 | Polynuclear hydroxo cluster |
| [ML2(s,am)] ⇌ [M] + [L]^2 (beta_def_337) | ΔH | 31.4 | 2 | vlm_170946 | Solid dissolution (amorphous Zn(OH)2) |
| [MO(s)] + H2O ⇌ [M] + [OH]^2 (beta_def_347) | ΔH | 22.6 | 2 | vlm_170960 | Solid oxide hydration |

Zn2+–EDTA family (thermodynamics; ΔS reported for M + L ⇌ ML definition)
| Ligand (protonation/variant) | ΔS | T (°C) | I (M) | vlm_id | Notes |
|---|---:|---:|---:|---|---|
| EDTA (H4L) | 250.2 | 25 | 0.1 | vlm_108712 | ΔS only; no β listed in this subset |
| EEDTA (H4L) | 207.5 | 20 | 0.1 | vlm_111809 |  |
| EEDTA (H4L) | 184.5 | 25 | 0.1 | vlm_111808 |  |
| TEDTA (H4L) | 204.6 | 25 | 0.1 | vlm_112304 |  |
| HEDTA (H3L) | 161.5 | 25 | 0.1 | vlm_108152 |  |

Notes and cautions
- Ionic strength and medium sensitivity: Reported Zn2+ formation constants vary markedly with I (e.g., Zn(NH3)4²+ logβ rises from 8.89 at I=0 to 9.73 at I=2 M at 25 °C). Always compare values at matched conditions.
- Speciation breadth: SRD‑46 covers amino acids, amines, N‑ and O‑donor chelators, sulfur donors (cysteine/penicillamine), inorganic anions (OH−, CN−, SCN−), and organophosphates, including mononuclear and polynuclear hydroxo species and some solid–solution equilibria.
- Practical trend: Zn2+ binds strongly to multidentate N/O ligands and forms stable tetraammine and hydroxo complexes under alkaline conditions; organophosphate ester binding is moderate under the surveyed 0.1 M conditions.

Source: NIST Standard Reference Database 46 (SRD‑46), as retrieved in this session (entity IDs: metal_208; selected vlm_ids and beta_def_ids shown).

---