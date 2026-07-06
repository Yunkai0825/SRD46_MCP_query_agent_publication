Short answer
I haven’t retrieved the matched stability constants yet (time budget cut off before Phase 1 completion), so I cannot name confirmed Irving–Williams exceptions from SRD‑46 in this turn. I did resolve the six divalent ions and a focused ligand panel in SRD‑46 (IDs below) and outlined the exact filters I will use to pull comparable logβ (ML, 1:1) values at ~25 °C and low ionic strength. With those data, I’ll flag any ligand(s) where the observed ordering deviates from Mn2+ < Fe2+ < Co2+ < Ni2+ < Cu2+ > Zn2+ and provide the tables and citations.

What’s ready (targets resolved in SRD‑46)
- Metals (divalent series): Mn2+ (metal_94), Fe2+ (metal_62), Co2+ (metal_33), Ni2+ (metal_112), Cu2+ (metal_41), Zn2+ (metal_208).
- Ligand panel with good coverage across N- and O-donors (and varying rigidity/basicity): EDTA (ligand_6277), DTPA (ligand_6356), glycine (ligand_5760), histidine (ligand_5898), ammonia (ligand_10103), ethylenediamine (en, ligand_7029), diethylenetriamine (dien, ligand_7212), 1,10‑phenanthroline (phen, ligand_8191), 2,2′‑bipyridine (bipy, ligand_8156), cyclam ([14]aneN4, ligand_7439), cyclen ([12]aneN4, ligand_7425), imidazole (ligand_7795), hydrogen carbonate/carbonate (ligand_10096).

How I will identify exceptions (on the next run)
- Pull only thermodynamic ML (1:1) constants (logK1/logβ1) for the six ions above, filter to 20–30 °C and I ≤ 0.2 M (or matched I), exclude hydroxo/polynuclear/speciation mixtures and redox‑affected datasets, and compare within each ligand.
- A “violation” is any ligand where the rank order shows an inversion, e.g., Ni2+ ≥ Cu2+ or Zn2+ ≥ Ni2+/Co2+ under matched stoichiometry and conditions. I’ll confirm across multiple entries/sources in SRD‑46 and report conditions and citations.

What exceptions I expect to test (hypotheses to explain them)
- Macrocyclic, size‑matched N4 ligands (cyclam/cyclen): Rigid cavities can strongly favor Ni2+ (d8) via optimal size/geometry and enhanced ligand‑field stabilization (“macrocyclic effect”), while Cu2+ (d9) may be penalized if Jahn–Teller distortion is frustrated by the ring. This can narrow or even invert the usual Cu2+ > Ni2+ gap for 1:1 complexes in some macrocycles.
- Constrained geometries with strong σ donors (e.g., certain chelating polyamines): If the enforced geometry suits Ni2+ but not Cu2+, Cu2+ may lose its usual edge; I’ll check en/dien vs more rigid polyamines to see if any Ni2+ ≥ Cu2+ cases appear.
- Weak O‑donors and competing hydrolysis (carbonate/phosphate): Conditional constants can be depressed by M2+ hydrolysis and oligomer formation at certain pH/ionic strengths, sometimes causing Zn2+ to track closer to Ni2+ or even overtake Co2+/Fe2+ conditionally. Any “exception” here will be scrutinized for speciation bias.
- Aromatic diimines (phen, bipy): The classic series generally holds, but geometry and ionic‑strength effects can compress differences; I’ll check if any datasets show Ni2+ approaching or surpassing Cu2+ under tightly constrained stoichiometries or specific media.
- Redox/sampling artifacts (Fe2+): Apparent deviations that elevate Fe2+ (vs Mn2+) or depress it can arise if partial Fe2+ → Fe3+ oxidation occurred during measurement; I’ll filter out such cases where labeled.

What I need from you to finish
- If you’re happy with this ligand set, I’ll run the catalog and matched‑condition queries next and return compact tables of logβ1 values per ligand across Mn2+–Zn2+, highlighting any rank‑order inversions and attaching SRD‑46 citations. If you’d rather prioritize a smaller set (e.g., cyclam/cyclen; phen/bipy; en/dien; EDTA/DTPA), tell me which 2–4 to do first.

Source
- All entity IDs and data will be drawn from NIST SRD‑46 (Critical Stability Constants of Metal Complexes).

---