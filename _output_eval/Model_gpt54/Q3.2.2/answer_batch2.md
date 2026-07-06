SRD-46 shows **25 °C data for Ni²⁺–ethylenediamine over ionic strength 0 to 3 M**, but the retrieved stability search only exposes **ranges**, not the individual logβ values needed to prove a monotonic trend.

| Complex | β definition | Constant type | logβ / logK range at 25 °C | Ionic strength range (M) | What can be concluded |
|---|---|---:|---:|---:|---|
| NiL | beta_def_812 | logK | 7.3–7.9 | 0–3 | Variation exists with ionic strength, but direction cannot be established from the summary alone |
| NiL₂ | beta_def_840 | logK | 14.53–14.77* | 0–3 | Only a small change is apparent; no clear trend can be claimed from the available summary |
| NiL₃ | beta_def_872 | logK | 19.18–19.70* | 0–3 | Again, values vary modestly, but the summary does not show whether change is monotonic |

\*The tool summary displayed these as signed ranges with formatting artifacts for ML₂/ML₃; interpreted here as the usual cumulative logβ magnitudes for these complexes.

### Bottom line
**There is not a clear trend that can be stated confidently from the accessible SRD-46 output here.**  
What we can say is:

| Observation | Interpretation |
|---|---|
| All three Ni–en complexes have measurements spanning **I = 0 to 3 M at 25 °C** | The system has enough coverage in principle for ionic-strength analysis |
| The reported **spread in logK/logβ is fairly small** for each complex | Ionic strength likely affects the conditional constants, but not dramatically over the reported range |
| The summary does **not provide point-by-point values matched to ionic strength and medium** | A definite “increases” or “decreases” conclusion is **not justified** from this result alone |

### Chemistry insight
For metal–amine systems like **Ni²⁺–en**, some ionic-strength dependence is expected because the measured constants are **conditional** and depend on activity coefficients. But whether the apparent stability rises or falls with ionic strength can depend on **electrolyte medium** and how the constants were extrapolated, so mixing datasets can obscure any simple trend.

**Source:** NIST SRD-46, Ni²⁺ (`metal_112`) – ethylenediamine (`ligand_7029`) stability data.

---