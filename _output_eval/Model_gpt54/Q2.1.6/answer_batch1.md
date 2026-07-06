I’m missing valid SRD-46 hits for the requested three metals, so I can’t give a database-backed numeric ranking for **Cd²⁺, Pb²⁺, and Hg²⁺** from the results obtained so far.

What happened is that the attempted targeted lookup landed on the wrong metal IDs:

| Requested metal | Intended symbol | Retrieved ID used | Actual metal from SRD-46 |
|---|---:|---:|---|
| Cd²⁺ | Cd | metal_41 | Cu²⁺ |
| Pb²⁺ | Pb | metal_62 | Fe²⁺ |
| Hg²⁺ | Hg | metal_80 | not validated |

So the numeric values returned are for **Cu²⁺** and **Fe²⁺** with hydrogen thiocyanate, not Cd/Pb/Hg.

Based on chemistry alone, the expected soft-metal affinity trend with thiocyanate is:

| Metal | Qualitative affinity to SCN⁻ |
|---|---|
| Hg²⁺ | highest |
| Cd²⁺ | intermediate |
| Pb²⁺ | lower/intermediate |

So the **most likely highest-affinity soft metal is Hg²⁺**.

But to be precise: **this qualitative ranking is not yet confirmed by SRD-46 numeric log K values in the retrieved data**. If you want, I can continue and do a stricter SRD-46 search to resolve the correct Cd, Pb, and Hg entries and extract matched-condition log K values.

---