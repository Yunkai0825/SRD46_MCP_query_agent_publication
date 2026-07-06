Based on my thorough investigation of the NIST SRD-46 database, here is the conclusion:

---

## Electrode Potential of Cu²⁺/Cu⁰ — SRD-46 Scope Limitation

**NIST SRD-46 (Critically Selected Stability Constants of Metal Complexes) does not contain electrode potential data.** The database is dedicated exclusively to **equilibrium stability constants** (log β, log K) for metal–ligand complexation reactions in solution.

My search confirmed this:

- No citations in SRD-46 reference "electrode potential," "standard potential," or "redox potential."
- No redox-type reaction entries exist for Cu²⁺ in the stability data.
- The database schema tracks `constant_type` values related to complexation equilibria, not electrochemical half-reactions.

### Standard Value from Electrochemical References

The well-known standard reduction potential is:

| Half-Reaction | E° (V vs. SHE) | Conditions |
|---|---|---|
| Cu²⁺(aq) + 2e⁻ → Cu(s) | **+0.340 V** | 25 °C, unit activity |

This value is available from authoritative electrochemical sources such as the **IUPAC Standard Electrode Potentials** or the **CRC Handbook of Chemistry and Physics**, not from SRD-46.

### What SRD-46 *can* offer for Cu²⁺

SRD-46 has an extensive collection of **stability constants** for Cu²⁺ complexes — covering **1,951 ligand partners** with **8,963 measurements**. If you're interested in how Cu²⁺ binds to specific ligands (e.g., EDTA, ammonia, glycine), I'd be happy to look those up!

---