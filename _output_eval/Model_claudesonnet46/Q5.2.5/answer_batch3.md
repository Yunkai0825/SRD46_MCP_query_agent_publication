## Cu²⁺/Cu⁰ Electrode Potential

The NIST SRD-46 database specializes in **aqueous metal–ligand stability constants** (log β values) and ligand pKa data — it does **not** contain standard electrode potentials (reduction potentials).

---

### Standard Electrode Potential (from established electrochemistry references)

| Half-Reaction | E° (V vs. SHE) | Conditions |
|---|---|---|
| Cu²⁺ + 2e⁻ → Cu⁰ | **+0.3419 V** | 25 °C, unit activity (standard state) |

> **Source:** NIST Chemistry WebBook / IUPAC recommendations (not SRD-46).

---

### A bit of chemistry context

- The **positive** E° (+0.342 V) means Cu²⁺ is a moderately good oxidizing agent and copper metal is **thermodynamically stable** in water (it does not dissolve in dilute non-oxidizing acids, unlike zinc or iron).
- This value is the basis for the classic **copper electrodeposition** reaction used in electroplating and the Daniell cell (Zn/Cu galvanic cell, E°_cell ≈ 1.10 V).
- Complexation of Cu²⁺ with ligands (e.g., ammonia, EDTA) **shifts the effective potential** to more negative values via the Nernst equation — that's where SRD-46 data becomes relevant!

---

> ⚠️ **SRD-46 scope note:** If you're interested in how ligand complexation affects the *apparent* Cu²⁺/Cu⁰ potential (e.g., in ammonia or cyanide solutions), I can query SRD-46 for Cu²⁺ stability constants and calculate the shift using the Nernst equation. Just ask!

---