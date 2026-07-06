SRD-46 gives matched **Cu²⁺–glycine** values for:

- **K₁** as the **[ML]/[M][L]** constant (`beta_def_812`)
- **β₂** as the **[ML₂]/[M][L]²** constant (`beta_def_840`)

A true stepwise **K₂ = [ML₂]/[ML][L]** is not directly listed in the retrieved Cu–glycine records, so use:

\[
\log \beta_2 = \log K_1 + \log K_2
\]

and therefore, from the matched SRD-46 values,

\[
\log K_2 = \log \beta_2 - \log K_1
\]

For the representative **25 °C, I = 0.10 M** aqueous case:

| Condition | log K₁ | direct log β₂ | derived log K₂ | estimated log β₂ = log K₁ + log K₂ |
|---|---:|---:|---:|---:|
| 25 °C, 0.10 M | 8.19 | 15.10 | 6.91 | 15.10 |

So the estimated overall constant is:

| Quantity | Value |
|---|---:|
| **log β₂ (estimated)** | **15.10** |
| **β₂ (estimated)** | **10^15.10 ≈ 1.26 × 10^15** |
| **log β₂ (directly reported in SRD-46)** | **15.10** |

They agree exactly for the matched dataset, as expected.

Across the other matched Cu²⁺–glycine conditions in SRD-46, the same identity holds: the directly reported **log β₂** values range from **14.69 to 16.3**, and each is consistent with **log β₂ = log K₁ + log K₂** when conditions are matched. Chemically, this is a nice illustration that the bis-glycinato copper(II) complex is very stable, with the second binding step weaker than the first but still strongly favorable.

**Source:** NIST SRD-46, Cu²⁺ (`metal_41`) + glycine (`ligand_5760`) stability data, `beta_def_812` and `beta_def_840`.

---