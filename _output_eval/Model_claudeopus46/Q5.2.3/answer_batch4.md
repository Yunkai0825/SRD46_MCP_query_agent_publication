Thank you for your question. Unfortunately, **the NIST SRD-46 database does not contain stability constant data at 200 °C and 50 bar pressure**. Here's why:

### Temperature Limitation

The database overwhelmingly covers near-ambient temperatures. Here is the temperature distribution of all ~79,000 stability constant measurements:

| Temperature (°C) | Measurements | % of Total |
|-------------------|-------------|------------|
| 25 | 67,237 | 85.0% |
| 20 | 6,845 | 8.7% |
| 37 | 1,699 | 2.2% |
| 30 | 919 | 1.2% |
| Other (0–50) | ~2,300 | 2.9% |
| **75 (maximum)** | **21** | **0.03%** |

The **highest temperature** recorded in SRD-46 is **75 °C** (for protonation and Mg²⁺ complexation of ADP). There are **zero measurements** at or above 100 °C, let alone 200 °C.

### Pressure Limitation

The database schema **does not include a pressure field** at all. SRD-46 records temperature, ionic strength, solvent, and electrolyte composition — but not pressure. This is typical for aqueous-phase stability constant compilations, which assume standard atmospheric pressure (~1 bar).

### What You Can Do

If you need stability constants at extreme conditions (200 °C, 50 bar), consider:

1. **Hydrothermal geochemistry databases** — e.g., SUPCRT92/SUPCRTBL, which use the Helgeson–Kirkham–Flowers (HKF) equation of state to extrapolate equilibrium constants to high *T* and *P*.
2. **IUPAC/NIST Solubility Data Series** — some volumes cover high-temperature aqueous systems.
3. **Primary literature** — researchers like Sverjensky, Shock, and Helgeson have published high-*T*/*P* complexation data for geochemically relevant metal–ligand systems.

If you'd like, I can help you find what stability constants are available in SRD-46 for a **specific metal–ligand system** at the highest temperatures recorded (up to 75 °C). Just let me know the metal and ligand of interest!

*Source: NIST Standard Reference Database 46 (Critically Selected Stability Constants of Metal Complexes)*

---