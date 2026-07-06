Here is what we could extract from SRD‑46 within the time budget for Pb²⁺ chelation. The only complete numeric stability constant we retrieved is for Pb²⁺–EDTA; the other ligands below are present in SRD‑46 with Pb²⁺ data but require one more query to pull their exact values for a proper “highest‑affinity” ranking.

Pb²⁺–EDTA stability (aqueous; near-physiological conditions)

| Ligand (SRD‑46 ID) | Stoichiometry | constant_type | log value | T (°C) | I (M) | Notes |
| EDTA (ligand_6277) | ML | overall β ([ML]/[M][L]) | 18.0 | 25.0 | 0.10 | beta_def_812; PbEDTA²⁻ dominates at pH ≥ 6

Additional Pb²⁺–EDTA protonation steps (same conditions; for speciation context)

| Species | Step constant_type | log value | Notes |
| MHL     | [MHL]/[ML][H]      | 2.1       | beta_def_788 |
| MH₂L    | [MH₂L]/[MHL][H]    | 2.3       | beta_def_739 |
| MH₃L    | [MH₃L]/[MH₂L][H]   | 2.6       | beta_def_751 |

Ligands with Pb²⁺ stability data in SRD‑46 (IDs resolved; numbers not pulled yet)

| Ligand (SRD‑46 ID) | Pb²⁺ data in SRD‑46 | Practice note (outside SRD‑46) |
| DTPA (ligand_6356) | Yes (complex data available) | Used mainly for actinides; not standard for lead |
| EGTA (ligand_6342) | Yes | Nonstandard for lead chelation |
| DOTA (ligand_6102) | Yes | Radiometal chelator; not used clinically for lead |
| DMSA / succimer (ligand_8997) | Present; the specific logβ not retrieved here | Standard clinical lead chelator |
| DMPS / unithiol (ligand_9758) | Yes (e.g., vlm_count ≈ 28) | Used in some regions; not universal first‑line |
| Dimercaprol / BAL (ligand_9759) | Present | Historical agent; limited modern use |
| Penicillamine (ligand_5857) | Present | Nonstandard/off‑label for lead; generally less preferred |
| NTA (ligand_6165) | Present | Nonclinical comparator |
| Cysteine (ligand_5856) | Present | Endogenous comparator; not a therapeutic chelator |
| Glutathione (ligand_6592) | Present | Endogenous comparator; not a therapeutic chelator |

Quick interpretation grounded in the retrieved EDTA data
- At 25 °C and I ≈ 0.10 M, PbEDTA²⁻ (ML, logβ ≈ 18) forms very strongly, and at physiological pH (≥6–7.4) this ML species dominates when EDTA is in excess. This is consistent with EDTA’s robust ability to hold Pb²⁺ in aqueous media.
- Protonated complex steps (MHL, MH₂L, MH₃L) become relevant only toward lower pH; under near‑physiological pH they have minimal impact on the dominant ML speciation.

Clinical‑use notes (outside SRD‑46 scope; summarized for context only)
- Used clinically for lead: CaNa₂‑EDTA (EDTA salt), DMSA (succimer). DMPS (unithiol) is used in some regions. BAL (dimercaprol) is an older agent now rarely used due to toxicity. Penicillamine is not preferred for lead.
- EGTA and DOTA are not used clinically for lead; DTPA is mainly for actinide decorporation rather than Pb²⁺.

What’s missing to definitively rank “highest affinity”
- SRD‑46 contains Pb²⁺ stability constants for DTPA, EGTA, DOTA, DMPS, DMSA, BAL, penicillamine, NTA, cysteine, and glutathione under various conditions. To rank them rigorously, we need to pull each ligand’s best‑matched aqueous logβ (or consistent stepwise constants), filtered to ~25 °C, I ≤ 0.1–0.5 M, and non‑chloride media, and then compare the dominant stoichiometry (ML vs ML₂/ML₃ for thiols).

If you’d like, I can run the ranking pull in a follow‑up to produce a complete table of Pb²⁺ affinities across all ligands and highlight the top performers under matched conditions.

Source: NIST SRD‑46 (Complexation Constants of Metal Ions).

---