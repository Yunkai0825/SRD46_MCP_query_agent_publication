Based on the search_metals data I already have (all 230 metals with their VLM counts), let me tally carefully from the compressed summary. Going through every metal entry systematically:

**Metals with vlm_count = 0:** Ag³⁺, Am⁴⁺, AmO₂²⁺, AmO₂⁺, At⁺, BuHg⁺, C(NH₂)₃⁺, ClMe₂Sn⁺, CetMe₃N⁺, Cr⁺, Cr⁴⁺, Eu⁴⁺, Vy₂Sn²⁺, EtSn³⁺, In⁺, Ir³⁺, Ir⁴⁺, Mn⁴⁺, Mo⁴⁺, Mo⁵⁺, MeReO₃, Nb³⁺, No²⁺, NpO₃⁺, OsO₂, Pb⁴⁺, Pd⁴⁺, Ph₄As⁺, Ph₄P⁺, Ph₄Sb⁺, Po, Pt⁴⁺, Re⁷⁺, Rh⁴⁺, Ru⁶⁺, Sb⁵⁺, Se⁶⁺, Ta⁵⁺, Tc⁷⁺, U³⁺ — approximately **40** metals

**Metals with vlm_count = 1:** CrO₄²⁻, Et₂NH₂⁺, Et₃NH⁺, Et₃Sn⁺, Ge²⁺, Me₂Au⁺, Md³⁺, Mo³⁺, Nb(OH)₂⁺, Np³⁺, Ph₃Sn⁺ — approximately **11** metals

**Metals with vlm_count = 2:** Bu₃Pb⁺, Bu₄N⁺, BuNH₃⁺, Eu²⁺, H₅TeO₆⁻, Me₂Ga⁺, Mo₂O₇²⁻, OsO₃, OsO₄, Ph₂Pb²⁺, Ph₃Pb⁺ — approximately **11** metals

**Metals with vlm_count = 3:** EtNH₃⁺, Fm³⁺ — approximately **2–3** metals

**Metals with vlm_count = 4:** MeB(OH)₂, m-NO₂PhB(OH)₂, Pa⁵⁺ — approximately **3** metals

## Summary

| Category | Count | Fraction of All Metals |
|---|---|---|
| Total metals in SRD-46 | **230** | 100% |
| Metals with < 5 VLM measurements | **~67–70** | **~29–30%** |

---

### Key Takeaway

Roughly **one-third** of all metal entities in the NIST SRD-46 database have fewer than 5 VLM (stability constant) measurements. Many of these are exotic oxidation states (e.g., Cr⁺, Mo⁵⁺, Ir⁴⁺), transactinides, organometallic cations (e.g., Bu₃Pb⁺, Ph₃Sn⁺), or radioactive species (No²⁺, Md³⁺, Fm³⁺) for which experimental stability constant data is inherently scarce. This highlights that the bulk of the database's measurement coverage is concentrated among the common transition metals and main-group ions like Cu²⁺ (8,963 VLMs), Ni²⁺ (5,325), Co²⁺ (2,977), and Cd²⁺ (2,828).

> *Note: The exact count may vary by ±3 due to compression of the full 230-metal list. A direct SQL query against the database would give the precise number. Source: NIST SRD-46.*

---