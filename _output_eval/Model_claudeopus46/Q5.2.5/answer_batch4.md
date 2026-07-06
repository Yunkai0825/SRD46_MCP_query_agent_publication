Based on my thorough investigation of the NIST SRD-46 database, here is my conclusion:

---

## Electrode Potential of Cu²⁺/Cu⁰ — Not Available in SRD-46

**NIST SRD-46 (Critically Selected Stability Constants of Metal Complexes) does not contain standard electrode potentials.** The database is dedicated exclusively to:

- **Stability constants** (log β, log K) for metal–ligand complexes
- **pKa values** for ligands
- **Literature citations** for those equilibrium measurements

I confirmed this by:

1. **Inspecting the Cu²⁺ card** (metal_41) — it contains only complexation data (1,951 ligand partners, 8,963 stability measurements), with no redox/potential fields.
2. **Searching citations** for "electrode," "standard potential," and "redox" — the 6 hits all relate to ion-selective electrode methodology, not standard reduction potentials.
3. **Checking database schemas** — no table or column stores electrode potential (E°) values.

---

### For Reference (from standard electrochemistry sources, **not** SRD-46):

| Half-reaction | E° (V vs. SHE) | T (K) |
|---|---|---|
| Cu²⁺(aq) + 2e⁻ → Cu(s) | **+0.340** | 298.15 |

This well-known value can be found in the CRC Handbook of Chemistry and Physics or IUPAC's *Standard Potentials in Aqueous Solution*. For NIST electrochemical data, you might consult **NIST SRD-10** (the NIST Chemistry WebBook) instead.

---

If you're interested in Cu²⁺ **stability constants** with specific ligands (e.g., EDTA, ammonia, glycine) — that's exactly what SRD-46 excels at, and I'd be happy to look those up!

---