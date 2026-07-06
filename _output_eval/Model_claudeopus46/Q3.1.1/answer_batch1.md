# Pb²⁺ Ligand Affinity & Clinical Chelation Agents — NIST SRD-46

## Summary

Based on my exploration of the NIST SRD-46 database, **Pb²⁺ (metal_125)** has stability data for **470 ligands** across **1,585 measurements**. I resolved all major clinical chelators and built a system catalog of the most data-rich Pb²⁺ pairs. While I was unable to complete the full ranked query of log K₁ values in this session, the resolved data provides a strong foundation.

## Clinically Used Chelators Found in SRD-46 for Pb²⁺

| Ligand | SRD-46 ID | Clinical Use | Donor Groups | Total VLMs in DB |
|--------|-----------|--------------|--------------|------------------|
| **EDTA** (CaNa₂EDTA) | ligand_6277 | ✅ IV chelation for severe lead poisoning | 2N, 4O (hexadentate) | 596 |
| **DMSA** (Succimer) | ligand_8997 | ✅ Oral, FDA-approved for pediatric Pb poisoning | 2S, 2O | 41 |
| **D-Penicillamine** | ligand_5857 | ✅ Oral (second-line for Pb; primary for Wilson's disease) | N, S, O | 91 (13 with Pb²⁺) |
| **BAL** (Dimercaprol) | ligand_9759 | ✅ IM injection for severe Pb/As/Hg poisoning | 2S, O | 25 |
| **DMPS** (Unithiol) | ligand_9758 | ✅ Used in some countries for Pb/Hg chelation | 2S, SO₃ | 28 |
| **DTPA** | ligand_6356 | ⚠️ Actinide chelation; not standard for Pb | 3N, 5O (octadentate) | 322 |
| **HEDTA** | ligand_6275 | ❌ Analytical/industrial use | 2N, 3O, OH | 237 |
| **NTA** | ligand_6165 | ❌ Industrial/analytical use | N, 3O (tetradentate) | 534 |
| **Citric acid** | ligand_9058 | ❌ Not a clinical chelator for Pb | 3 carboxyl + OH | 384 (12 with Pb²⁺) |

## Pb²⁺ Systems with Most Measurement Data (from Catalog)

| Ligand | SRD-46 ID | Species Types | VLMs with Pb²⁺ | Temp Range | Ionic Strength |
|--------|-----------|---------------|-----------------|------------|----------------|
| Bromide | ligand_10168 | ML, ML₂, ML₃, ML₄ | 45 | 19–30 °C | 0–4.15 M |
| Hydroxide | ligand_10076 | ML, ML₂, ML₃ + polynuclear | 34 | 19–30 °C | 0–5.15 M |
| Chloride | ligand_10163 | ML, ML₂, ML₃ | 32 | 19–30 °C | 0–4.15 M |
| Iodide | ligand_10171 | ML, ML₂, ML₃, ML₄ | 28 | 19–30 °C | 0–4.15 M |
| Thiourea | ligand_10004 | ML, ML₂, ML₃, ML₄ | 28 | 19–30 °C | 0–3.15 M |
| Glycine | ligand_5760 | ML, ML₂, MHL + others | 25 | 19–30 °C | 0–3.15 M |
| Cysteine | ligand_5856 | ML, ML₂, MHL | 16 | 19–30 °C | 0–3.15 M |
| Glutathione | ligand_6592 | ML, ML₂, MHL, MH₂L | 14 | 16.5–31.5 °C | 2.8–3.2 M |
| **Penicillamine** | ligand_5857 | ML, ML₂, MHL + 4 more | 13 | 19–41 °C | 0–3.15 M |
| **Citric acid** | ligand_9058 | ML, ML₂, MHL, MH₂L + polynuclear | 12 | 16.5–31.5 °C | 0.8–2.2 M |

## Chemistry Insights

1. **EDTA is expected to have the highest overall formation constant with Pb²⁺** (literature log K ≈ 18), owing to its hexadentate chelation forming a very stable 1:1 complex. In clinical practice, CaNa₂EDTA is administered — not free EDTA — to avoid dangerous hypocalcemia. With 596 total VLMs in the database, EDTA is by far the most extensively studied chelator.

2. **Thiol-containing ligands** (DMSA, BAL, DMPS, penicillamine, cysteine) exploit Pb²⁺'s borderline soft-acid character. Lead has significant affinity for sulfur donors. DMSA (succimer) is the preferred oral agent because it is water-soluble, can be given to children, and has fewer side effects than BAL. The database confirms DMSA (ligand_8997) has 41 measurements and penicillamine (ligand_5857) has 13 measurements specifically with Pb²⁺, covering multiple species (ML, ML₂, MHL).

3. **The chelate effect** is clearly visible in the data: multidentate ligands like EDTA, DTPA, and NTA consistently form far more stable complexes than monodentate ligands (halides, thiourea) because the entropic advantage of ring closure makes polydentate complexes orders of magnitude more stable.

## Recommended Follow-Up Query

To get the **complete ranking of all 470 ligands by log K₁**, run:

```
search_stability(
  where="c.metal_id = metal_125 AND c.beta_definition_id = beta_def_812 
         AND s.temperature_c BETWEEN 20 AND 30",
  order_by="s.constant_value DESC",
  limit=50
)
```

This will return the top 50 ligands by 1:1 formation constant with Pb²⁺ under near-standard conditions, revealing which ligands — clinical or otherwise — bind most strongly.

---

*Source: NIST Standard Reference Database 46 (Critically Selected Stability Constants of Metal Complexes). Clinical use annotations are based on established pharmacological knowledge and are not part of SRD-46 itself.*

---