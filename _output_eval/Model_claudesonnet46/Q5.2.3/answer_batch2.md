## Stability Constants at 200 °C and 50 bar — What SRD-46 Can Tell You

Based on my investigation of the NIST SRD-46 database, here is a clear and honest summary:

---

### 🌡️ Temperature Coverage in SRD-46

| Temperature (°C) | Number of Measurements |
|---|---|
| 75 | 9 |
| 55 | 2 |
| 50 | 14 |
| 45 | 33 |
| 40 | 189 |
| 37 | 1,691 |
| 35 | 314 |
| 30 | 799 |
| 25 | 49,950 |
| 20 | 6,399 |
| 10 | 201 |
| 0 | 18 |

**The maximum temperature recorded in SRD-46 is 75 °C.** There are **no stability constants at 200 °C** in the database.

---

### 🔬 Pressure Coverage in SRD-46

**Pressure is not a structured/indexed field** in SRD-46. A search of all citation text for keywords like "bar", "MPa", "pressure", "autoclave", and "hydrothermal" returned only false positives (author names like "Barksdale", "Barb", "Barnes", etc.) — **no citations explicitly reporting measurements at 50 bar** were found.

---

### Why This Gap Exists

This is not surprising from a chemistry standpoint:

- **Most stability constant measurements** (potentiometry, spectrophotometry, calorimetry) are performed at or near ambient conditions (25 °C, 1 atm) in aqueous solution.
- **At 200 °C and 50 bar**, water is still liquid (above its normal boiling point but below the critical point at 374 °C/221 bar), making this a **hydrothermal regime**. Measurements here require specialized autoclaves and are far less common.
- High-temperature hydrothermal stability data, when it exists, tends to appear in geochemical or nuclear waste literature and may not have been compiled into SRD-46.

---

### Recommendation

If you need stability constants at 200 °C / 50 bar, consider:

1. **SUPCRT92 / SUPCRTBL** — thermodynamic databases for hydrothermal aqueous species
2. **GEMS-Selektor** or **PHREEQC** with the **llnl.dat** or **pitzer.dat** databases
3. Literature from geochemical journals (e.g., *Geochimica et Cosmochimica Acta*) for specific metal–ligand systems

> **Source:** NIST SRD-46 (Critically Selected Stability Constants of Metal Complexes). No data at 200 °C or 50 bar is present in this database.

---