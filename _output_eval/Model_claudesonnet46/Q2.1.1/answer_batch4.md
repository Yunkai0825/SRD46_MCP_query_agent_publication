## Fe³⁺ Complex Stability: EDTA vs. NTA

Here are the log K values for the 1:1 ML formation reaction `Fe³⁺ + L ⇌ [FeL]` from the NIST SRD-46 database:

### Side-by-Side Comparison

| Ligand | Formula | log K (I = 0.1 M, 25 °C) | log K (I = 1.0 M, 25 °C) | Equation |
|--------|---------|--------------------------|--------------------------|----------|
| **EDTA** (H₄L) | C₁₀H₁₆N₂O₈ | **25.1** | 23.8 | Fe³⁺ + L⁴⁻ ⇌ [FeL]⁻ |
| **NTA** (H₃L) | C₆H₉NO₆ | **15.9** | 14.78 | Fe³⁺ + L³⁻ ⇌ [FeL] |

> **β-definition:** `beta_def_812` — overall 1:1 ML formation constant, both at 25 °C.  
> *Source: NIST SRD-46*

---

### Verdict

**EDTA wins decisively.** At I = 0.1 M and 25 °C, EDTA forms a **~9.2 log-unit more stable** complex with Fe³⁺ than NTA (log K = 25.1 vs. 15.9). This corresponds to a difference of ~**10⁹·²** in the equilibrium constant — an enormous thermodynamic advantage.

### Chemistry Insight

- **Why EDTA is so much stronger:** EDTA is a hexadentate ligand (4 carboxylate + 2 amine donors), while NTA is tetradentate (3 carboxylate + 1 amine). The extra binding arms of EDTA create a more complete octahedral cage around Fe³⁺, maximizing both enthalpic (more Fe–O/N bonds) and entropic (chelate effect) contributions. The ΔS values confirm this: EDTA gives ΔS = +442.7 J/mol·K vs. NTA's +349.8 J/mol·K.
- **Real-world relevance:** The extraordinary stability of [Fe(EDTA)]⁻ (log K = 25.1) makes EDTA the ligand of choice in iron-chelation therapies, analytical chemistry (complexometric titrations), and industrial processes where Fe³⁺ must be sequestered. NTA, while weaker, is used as a more biodegradable alternative in detergents and environmental remediation.
- **Ionic strength effect:** Both ligands show a ~1.1–1.2 log-unit drop in log K when ionic strength rises from 0.1 M to 1.0 M, consistent with the high charge product of the reaction (Fe³⁺ + L³⁻/L⁴⁻).

---