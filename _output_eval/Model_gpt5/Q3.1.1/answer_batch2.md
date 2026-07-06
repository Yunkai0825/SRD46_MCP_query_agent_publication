Short answer and status
- I resolved Pb2+ in NIST SRD‑46 (metal_125), which links to 470 ligands and 1,585 Pb(II) stability measurements. However, my first‑pass queries were too strict (narrow temperature/ionic strength and a very specific β-definition), so no constants were returned within this time budget. I did not retrieve a ranked list yet.

What this means for “highest affinity”
- In SRD‑46, the ligands that typically give the largest overall stability for Pb2+ are polyaminocarboxylates and vicinal dithiols. Based on chemical class (to be verified with the proper query), likely high‑affinity candidates include:
  - Polyaminocarboxylates: EDTA (ethylenediaminetetraacetate), DTPA, CyDTA.
  - Vicinal dithiols: DMSA (meso‑2,3‑dimercaptosuccinic acid), DMPS (2,3‑dimercaptopropanesulfonate), BAL (2,3‑dimercaprol).
- I will rerun with broader β/stochiometry filters (include log β1, log β2 where PbL2 is dominant; allow wider ionic strength and common aqueous media such as NaCl, KNO3, ClO4−, and accept 20–30 °C or report exact T/I for each value), then sort by the largest directly comparable log β and present a ranked table with conditions.

Clinical use (outside SRD‑46 numeric extraction; for context only)
- In standard medical practice, CaNa2EDTA and DMSA (succimer) are established chelators for lead; BAL and penicillamine have been used but are not first‑line for routine Pb poisoning due to safety/efficacy considerations. I will confirm SRD‑46 coverage of these ligands and attach the strongest Pb(II) constants for each in the next pass.

Proposed next step (fast)
- I’ll broaden the SRD‑46 search to:
  - Include log β for PbL and PbL2 (exclude hydroxo/mixed‑ligand species).
  - Allow aqueous media with specified electrolytes; report exact T and ionic strength with each constant.
  - Target by ligand name to guarantee coverage: “EDTA,” “DTPA,” “DMSA,” “DMPS,” “dimercaprol,” “penicillamine,” plus the top N polyaminocarboxylates discovered in the Pb2+ set.
- Then I’ll return a ranked table of the top Pb(II) affinities with conditions, and clearly flag which ligands are clinically used.

If you’d like me to proceed with that broader pull now, I can deliver the ranked table in the next reply.

Source: NIST Standard Reference Database 46 (SRD‑46), Inorganic Complexes Stability Constants (Pb2+ entity metal_125; ligand/measurement counts as retrieved above).

Important medical note
- Chelation therapy should be selected and dosed by qualified clinicians using established guidelines (e.g., CDC/WHO/poison control recommendations). The SRD‑46 constants help compare affinity but do not replace clinical criteria (exposure level, symptoms, renal function, and safety profiles).

---