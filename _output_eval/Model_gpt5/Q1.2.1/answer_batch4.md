I couldn’t finish the provenance lookup within the time budget, so I don’t yet have the authors and year for the highest Cu²⁺–EDTA log K. Here’s what I verified in SRD‑46 and the exact next step needed to complete it:

What’s confirmed from SRD‑46
- Metal: Cu²⁺ = metal_41
- Ligand: EDTA (Ethylenedinitrilotetraacetic acid) = ligand_6277 (H4L; synonym “EDTA”)
- Cu²⁺–EDTA system coverage: 20 VLM records across 4 species; the 1:1 overall formation constant is beta_def_812 ([ML]/[M][L]) with 8 entries.

Next step to retrieve the authors/year (1 quick query + citation readout)
- Query the 1:1 overall constants and sort by value descending:
  • search_stability where: c.metal_id = metal_41 AND c.ligand_id = ligand_6277 AND c.beta_definition_id = beta_def_812; order_by s.constant_value DESC; limit 1.
- Open the top vlm_* returned and read its linked citation(s) to report the primary article’s authors and publication year (inspect_literature).

If you’d like, I can run that single lookup now and return the authors and publication year immediately.

Source: NIST SRD‑46 (BindingDB/Thermodynamics of Metal–Ligand Complexes) system catalog for Cu²⁺–EDTA.

---