Using a direct SRD-46 SQL count derived from `metal_card` LEFT JOIN `eq_node` on `metal_id`:

| metric | value |
|---|---:|
| Total metals | 230 |
| Metals with fewer than 5 total VLM measurements | 114 |
| Fraction of all metals | 0.4956521739 |
| Percentage | 49.6% |

So, **114 metals** in the database have **fewer than 5 VLM measurements total**, which is **114/230 = 0.4957**, or **about 49.6%** of all metals.

This was computed by counting **distinct `vlm_id` values per metal** from the equilibrium data, using a **LEFT JOIN** so metals with zero measurements were included.

**Source:** NIST SRD-46 (`metal_card` and `eq_node` via `execute_srd46_sql`).

---