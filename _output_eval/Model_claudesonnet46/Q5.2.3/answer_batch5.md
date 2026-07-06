## Stability Constants at 200 °C and 50 bar — Not Available in SRD-46

Unfortunately, **SRD-46 does not contain stability constant data at 200 °C or 50 bar pressure**. Here's a summary of what the database actually covers:

| Parameter | SRD-46 Coverage |
|---|---|
| **Temperature range (eq_node)** | 0 °C to **75 °C** |
| **Temperature range (eq_map)** | −7.5 °C to **81 °C** |
| **Pressure field** | ❌ Not stored in the database |
| **Total stability constant nodes** | 60,540 measurements |

### Key Findings

1. **Temperature ceiling is ~81 °C** — The highest temperature recorded in any SRD-46 equilibrium map is 81 °C, far below the requested 200 °C. No data exists in the 150–250 °C range.

2. **No pressure field** — SRD-46 does not store pressure as a structured column. Hydrothermal/autoclave conditions (e.g., 50 bar) are not captured in the database schema.

3. **Scope of SRD-46** — This database focuses on aqueous solution equilibria under near-ambient conditions (primarily 15–45 °C, ionic strengths 0–5 mol/L), which is the regime where most potentiometric, spectrophotometric, and calorimetric titration experiments are conducted.

### Where to Look Instead

For stability constants at **hydrothermal conditions** (200 °C, 50 bar), you would need specialized sources such as:
- **SUPCRT92 / SUPCRTBL** — thermodynamic database for minerals and aqueous species at high T/P
- **Shock et al. (1997)** and related HKF (Helgeson-Kirkham-Flowers) equation-of-state literature
- **Hydrothermal experimental literature** (e.g., journals like *Geochimica et Cosmochimica Acta*)

> **Source:** NIST SRD-46 (Critically Selected Stability Constants of Metal Complexes)

---