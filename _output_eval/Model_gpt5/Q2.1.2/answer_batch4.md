Short answer
- Expected ranking (log β1 for M2+ + NH3 ⇌ M(NH3)2+, aqueous): Mn2+ < Fe2+ < Co2+ < Ni2+ < Cu2+ > Zn2+.
- Does it follow the Irving–Williams series? Yes—ammine complexes are a textbook case where the Irving–Williams order is observed: stability increases from Mn2+ to a maximum at Cu2+, then drops slightly at Zn2+.

What I confirmed in SRD‑46 and what’s pending
- SRD‑46 contains ammonia as ligand_10103 and has β1 entries (definition beta_def_812: [M] + [L] ⇌ [ML]) for each target metal pair:
  - Mn2+ (metal_94) + NH3
  - Fe2+ (metal_62) + NH3
  - Co2+ (metal_33) + NH3
  - Ni2+ (metal_112) + NH3
  - Cu2+ (metal_41) + NH3
  - Zn2+ (metal_208) + NH3
- Due to time limits I couldn’t pull a single matched-condition set (e.g., 25 °C, fixed ionic strength) of numerical log β1 values. With one more query, I can extract a 25 °C table using beta_def_812 for all six metals at matched ionic strength and provide exact numbers.

Chemistry note
- The Irving–Williams pattern reflects decreasing ionic radius and increasing ligand field stabilization moving from Mn2+ to Cu2+, with a pronounced maximum at Jahn–Teller-active Cu2+ and a drop for d10 Zn2+ (no LFSE). Ammonia is a moderate field, neutral σ‑donor ligand, so it typically exhibits the canonical trend.

Source
- NIST SRD‑46 (IUPAC Stability Constants Database). Systems verified present: ligand_10103 with metal_94 (Mn2+), metal_62 (Fe2+), metal_33 (Co2+), metal_112 (Ni2+), metal_41 (Cu2+), metal_208 (Zn2+); β1 defined by beta_def_812.

---