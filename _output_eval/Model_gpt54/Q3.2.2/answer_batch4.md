SRD-46 shows the **Ni²⁺–ethylenediamine** system has data for **ML, ML₂, and ML₃** over **ionic strength 0 to 3 M** at mostly **25 °C**.

| Species | Beta definition | logK data points | T range (°C) | Ionic strength range (M) | logK range |
|---|---|---:|---:|---:|---:|
| ML | beta_def_812 | 6–7 | 25–37 | 0–3 | 6.98–7.90 |
| ML₂ | beta_def_840 | 6–7 | 25–37 | 0–3 | -14.77–14.53* |
| ML₃ | beta_def_872 | 6–7 | 25–37 | 0–3 | -19.70–19.18* |

\*The extreme negative/positive ranges here indicate that mixed definitions or data handling across sources may be present in the summary view, so these ranges alone should not be over-interpreted.

### Is there a clear ionic-strength trend?
**Not from the currently retrieved SRD-46 summary alone.**  
We can say there is **coverage across ionic strength**, but the tool output returned only aggregated ranges, not the individual **logK at each ionic strength and electrolyte** needed to establish a clean monotonic trend.

### What can be said safely
| Conclusion | Support from SRD-46 |
|---|---|
| The Ni²⁺–ethylenediamine system has substantial ionic-strength coverage | Yes |
| Data exist for ML, ML₂, and ML₃ separately | Yes |
| A single, unambiguous increase or decrease of logK with ionic strength is proven by the retrieved output | No |

### Best interpretation
For this question, a **clear trend cannot yet be claimed** unless the constants are compared **within the same electrolyte medium** and **at matched temperature**. That matters because ionic-strength effects can be masked by changing medium, and chloride-containing media would be especially problematic for Ni²⁺.

### Chemistry note
For metal–amine complexes, one often expects **conditional stability constants to shift with ionic strength**, but whether they appear to rise or fall depends strongly on the **charge pattern of reactants/products** and on the **activity model / supporting electrolyte** used. So for Ni²⁺–en, the right comparison is not “all points vs I”, but **same species, same temperature, same background electrolyte**.

If you want, I can do one more SRD-46 pass to extract the **individual ML / ML₂ / ML₃ logK values vs ionic strength** and check whether, for example in **perchlorate or nitrate medium at 25 °C**, the trend is actually monotonic.

---