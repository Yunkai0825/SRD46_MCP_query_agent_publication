Based on my investigation of the SRD-46 database schema, I can now give you a clear and honest answer.

---

## Stability Constants at 200 °C and 50 bar — What SRD-46 Can (and Cannot) Tell You

### Key Finding: No Pressure Field in SRD-46

After inspecting the database schema, **SRD-46 does not store pressure as a recorded field** in any of its equilibrium tables (`eq_node`, `eq_map`, etc.). The available condition fields are:

| Field | Description |
|---|---|
| `temperature` / `condition_temperature` | Temperature in Kelvin |
| `ionic_strength` / `condition_ionic_strength` | Ionic strength in mol/L |

There is **no `pressure` column** anywhere in the equilibrium database. This means it is impossible to filter or verify stability constants at exactly 50 bar from the database alone.

---

### Why This Matters Chemically

- **50 bar at 200 °C** is a hydrothermal condition. At 200 °C, water's vapor pressure is ~15.5 bar, so 50 bar would keep water liquid — a common setup in geochemical and nuclear waste studies.
- High-temperature/pressure stability data in the literature is sparse and often reported at **autogenous pressure** (the vapor pressure of the solution at that temperature), not a fixed external pressure like 50 bar.
- SRD-46 may contain entries measured near 200 °C (≈473 K), but **pressure is not recorded**, so the 50 bar condition cannot be verified or enforced.

---

### What You Can Do

To find stability constants near **200 °C**, I can search SRD-46 for entries with `temperature ≈ 473 K` — but I **cannot guarantee** they correspond to 50 bar. If you'd like:

1. **Specify a metal–ligand system** (e.g., Fe³⁺–chloride, Cu²⁺–ammonia, UO₂²⁺–carbonate) — I can search for high-temperature data for that system.
2. **Relax the pressure requirement** — I can find all entries near 200 °C and note that pressure is unspecified in the database.
3. **Check primary literature** — For explicit 50 bar data, you would need to consult hydrothermal chemistry references (e.g., Shock & Helgeson, Sverjensky et al.) directly.

> **Source:** NIST SRD-46 (Critically Selected Stability Constants of Metal Complexes). No pressure field exists in the database schema; temperature and ionic strength are the only stored conditions.

---