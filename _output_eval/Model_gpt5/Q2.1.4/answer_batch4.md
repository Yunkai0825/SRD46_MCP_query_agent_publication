Status summary (from NIST SRD‑46, resolved IDs)

| System | Metal (ID) | Ligand (ID) | Stepwise definition | Species | Entries present |
|---|---|---|---|---|---|
| Cu2+ + Cl− | Cu2+ (metal_41) | Chloride (ligand_10163) | beta_def_812: [ML]/[M][L] | CuCl+ (aqueous) | 15 entries (CuCl+) within 19 total for the pair |
| Cu2+ + Br− | Cu2+ (metal_41) | Bromide (ligand_10168) | beta_def_812: [ML]/[M][L] | CuBr+ (aqueous) | 7 entries (CuBr+) within 9 total for the pair |

What’s missing
- I attempted to pull the actual log K (or β) values for beta_def_812 under matched conditions, but the query with a “water” solvent filter returned no rows (likely a solvent/medium string mismatch), and a broader follow‑up query could not complete within the time budget. As a result, I don’t yet have the numeric constants needed to state which halide forms the stronger Cu(II) complex.

How I will complete the comparison (fast follow‑up)
- Pull stepwise ML formation constants for both systems using the resolved IDs and a consistent β-definition:
  - WHERE: c.metal_id = metal_41 AND c.ligand_id IN (ligand_10163, ligand_10168) AND c.beta_definition_id = beta_def_812
  - Then align conditions: ~25 °C and the same ionic strength and medium (avoid cases where the halide is the background electrolyte unless used identically for both).
- Report matched-condition log K1 (ML) for CuCl+ vs CuBr+ and conclude which is larger (the stronger complex).

If you’d like, I can run that broader query (without an over‑strict solvent string) and return the matched 25 °C data immediately.

Source: NIST SRD‑46 (IUPAC Stability Constants Database) — Cu2+ with chloride (ligand_10163) and bromide (ligand_10168), stepwise ML β-definition beta_def_812.

---