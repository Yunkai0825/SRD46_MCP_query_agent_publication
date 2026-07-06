Here’s what SRD-46 currently shows for Zn(II):

Overall coverage (entity summary)
| Metal | Prefixed ID | Charge | Ligands with data | Distinct β-definitions | Measured values |
|---|---|---|---:|---:|---:|
| Zn2+ | metal_208 | +2 | 1169 | 122 | 4095 |

Representative equilibria under near-ambient conditions
- Zn2+ + Glycine (ligand_id: ligand_5760; “Aminoacetic acid”)
  - Network ref_eq_net_113 (T 31–41 °C; I 0–0.3 M)
  | Reaction (β-def) | Equilibrium expression | logK |
  |---|---|---:|
  | beta_def_812 | [M] + [L] ⇌ [ML] | 4.87 |
  | beta_def_966 | [M(OH)L] + [H] ⇌ [ML] + H2O | 8.90 |
  | beta_def_840 | [M] + [L]2 ⇌ [ML2] | 8.97 |
  | beta_def_872 | [M] + [L]3 ⇌ [ML3] | 11.30 |

- Zn2+ + 6,16-Dioxa-3,9,13,19-tetraaza-1,11(2,6)-dipyridinacycloeicosane (ligand_id: ligand_7653; macrocyclic polyamine)
  - Network ref_eq_net_171 (T 20–30 °C; I −0.05–0.25 M)
  | Reaction (β-def) | Equilibrium expression | logK |
  |---|---|---:|
  | beta_def_812 | [M] + [L] ⇌ [ML] | 8.89 |
  | beta_def_788 | [ML] + [H] ⇌ [MHL] | 7.45 |
  | beta_def_516 | [ML] + [M] ⇌ [M2L] | 3.80 |
  | beta_def_839 | [M(OH)L] + [H] ⇌ [ML] + H2O | 9.52 |
  | beta_def_975 | [M(OH)2L] + [H] ⇌ [M(OH)L] + H2O | 11.00 |
  | beta_def_515 | [M2(OH)L] + [H] ⇌ [M2L] + H2O | 7.07 |

Notes and quick takeaways
- Breadth: Zn2+ has very broad coverage in SRD‑46 (1169 ligands; 4095 measured values). The database includes simple amino acids, polyamines/macrocycles, and hydrolysis-coupled reactions.
- Strength trends: As expected, multidentate macrocycles bind Zn2+ more strongly than simple amino acids (e.g., ML logK ≈ 8.9 for the macrocycle vs ≈ 4.9 for glycine at comparable low-ionic-strength, near-room-temperature conditions). For glycine, higher stoichiometry (ML2, ML3) increases overall cumulative stability (logβ) as shown.
- Media sensitivity: Constants vary with temperature and ionic strength; the values above are anchored near room temperature and low to moderate ionic strength as indicated.

If you have a specific ligand, medium (e.g., NaCl vs. KNO3), or temperature/ionic-strength window in mind, I can pull a focused set of Zn(II) constants and pKa data for the relevant ligand(s).

Source: NIST Standard Reference Database 46 (SRD‑46).

---