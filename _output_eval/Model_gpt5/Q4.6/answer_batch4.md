I wasn’t able to retrieve the SRD‑46 stability data yet because Phase 1 discovery failed: none of the metal or ligand names resolved to SRD‑46 IDs, and without at least one metal_*, ligand_*, or beta_def_* to build a system catalog, the stability-search tools are gated.

If you can provide any prefixed IDs (e.g., metal_41 for Cu, ligand_5760 for EDTA) or allow me to proceed with a broad, name-pattern query (e.g., “copper(II)”, “EDTA”, “cyclam”, “cyanide”) to seed the catalog, I’ll run the comparison immediately. Alternatively, if you’d like me to use raw SQL name filters to find candidate systems, I can make that one critical call.

Plan (what I’ll do once the gate is opened)
- Pull ML formation constants (log β) for Mn2+, Fe2+, Co2+, Ni2+, Cu2+, and Zn2+ across ligands with ≥5 metals reported, matched conditions (~25 °C, aqueous, low ionic strength).
- Rank the metals per ligand and flag any deviations from Irving–Williams (Mn < Fe < Co < Ni < Cu > Zn).
- Verify each flagged case via inspect_card/inspect_literature to ensure true ML stoichiometry, divalent state (Cu2+, Fe2+), matched T/I, and consistent solvent/electrolyte.
- Report exceptions with a compact table of log β values and cite SRD‑46.

Hypotheses we’ll test against any exceptions (to be tied to the SRD‑46 records)
- Macrocyclic preorganization/cavity fit: rigid tetraaza macrocycles (cyclam/cyclen) often favor Ni2+ and can penalize Jahn–Teller-distorted Cu2+, leading to Ni2+ ≥ Cu2+.
- Ligand field/geometry: Ni2+ (d8) square‑planar stabilization with strong-field donors may elevate Ni2+ relative to Cu2+.
- HSAB/donor type: soft S/N donors (e.g., thiocyanate, thioethers) can enhance Cu2+ covalency; hard O‑donors (carboxylates) may let Zn2+ approach or surpass Ni2+ in some ML sets.
- Protonation/conditional constants: comparing MLH or mixed stoichiometries can appear to “violate” the series; we’ll control for this.
- Redox/handling: Fe2+ oxidation or Cu+/Cu2+ speciation can skew apparent stability.

Source: NIST SRD‑46 (Virtual Ligand‑Metal database). Please share any known SRD‑46 IDs or approve a broad name-pattern search so I can produce the exception list with citations and numeric tables.

---