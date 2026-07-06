SRD-46 does **not appear to contain the needed Cu²⁺/Ni²⁺/Zn²⁺ + ethylenediamine systems** in the accessible records I could resolve, and for these metals it also did **not return the corresponding ammonia pairs** needed for a clean cross-metal comparison. So I can’t compute a reliable SRD-46-based table of

| metal | log K(M–en) | log β₂(M–(NH₃)₂) | Δ = log K_en − 2·log K_NH₃ |
|---|---:|---:|---:|

without inventing values, which I won’t do.

What SRD-46 did show is:

| finding | SRD-46 result |
|---|---|
| Ammonia ligand resolved | `ligand_10103` = Ammonia |
| Cu²⁺ resolved | `metal_41` = Cu²⁺ |
| Ni²⁺ resolved | `metal_112` = Ni²⁺ |
| Zn²⁺ resolved | `metal_208` = Zn²⁺ |
| Cu²⁺/Ni²⁺/Zn²⁺ + ammonia/en pair coverage | not recovered as a usable matched set |
| Ethylenediamine ligand by name-pattern search | not recovered in returned records |

## Conclusion from SRD-46
Based on the retrieved dataset alone, **the comparison is inconclusive** because the required en and NH₃ constants for all three metals were not available in a matched, extractable form.

## Chemistry hypothesis
If you’re asking conceptually whether the chelate effect should be constant across Cu²⁺, Ni²⁺, and Zn²⁺, the answer is **probably not exactly**. A reasonable hypothesis is:

| metal | expected chelate-effect tendency | rationale |
|---|---|---|
| Cu²⁺ | often larger / less “ideal” | Jahn–Teller distortion and strong preference for N-donor coordination can make preorganized bidentate binding especially favorable |
| Ni²⁺ | substantial and often very regular | octahedral d⁸ ion gains from strong, well-matched N-donor chelation and ligand-field stabilization |
| Zn²⁺ | still positive, but often more entropy-dominated | d¹⁰ ion lacks LFSE, so differences may reflect mainly ring closure/preorganization and solvation rather than crystal-field effects |

So the **chelate effect should remain positive for all three**, but its **magnitude can vary with metal-ion size, preferred geometry, ligand-field stabilization, Jahn–Teller effects, and desolvation**.

If you want, I can do one of these next:
| option | what I’ll do |
|---|---|
| Broaden the SRD-46 search | try raw schema/SQL workflow to hunt the exact ethylenediamine naming used in the database |
| Use only ammonia within SRD-46 | extract Cu²⁺/Ni²⁺/Zn²⁺ ammonia stepwise/cumulative constants and summarize available trends |
| Help compare with literature outside SRD-46 | if you allow non-SRD sources, I can build the full chelate-effect table |

---