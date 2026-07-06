I have the data from the L0 search_metals call which returned all 230 metals with their VLM counts. The compressed summary explicitly identified **88 metals** with fewer than 5 VLM measurements. Let me compute the final answer from that.

## Result

| Metric | Value |
|--------|-------|
| Metals with < 5 VLM measurements | **88** |
| Total metals in database | **230** |
| Fraction | **88 / 230 ≈ 38.3%** |

More than a third of all metal entries in the NIST SRD-46 database have fewer than 5 VLM (stability constant) measurements. This group is dominated by metals with **zero** VLM records — including noble gases (He, Ne, Ar, Kr, Xe, Rn), superheavy elements (Rf, Db, Sg, Bh, Hs, Mt, Lr), non-metals used as placeholders (O, F, S, Cl, Br, I), and exotic or redox-unstable oxidation states (Ir³⁺/⁴⁺, Pt⁴⁺, Pb⁴⁺, V⁴⁺, etc.). The bulk of the thermodynamic data is concentrated on the remaining ~142 metals that have ≥ 5 measurements, reflecting the practical focus of coordination chemistry on common transition metals, lanthanides, and actinides in stable oxidation states.

*Source: NIST Standard Reference Database 46 (Critically Selected Stability Constants of Metal Complexes).*

---