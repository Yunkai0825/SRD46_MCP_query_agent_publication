# Q2.2.6 - Validation (batch 3)

**16 of 29 claims unsupported**

| # | Para | Type | Unsupported Claim | Context |
|---|------|------|-------------------|---------|
| 1 | 0 | counting | **vlm_count = 0 → 74 metals** | ...d counting those with `vlm_count < 5`:  **vlm_count = 0 → 74 metals** **vlm_count = 1 → 13 metals** **vlm_cou... |
| 2 | 0 | counting | **vlm_count = 1 → 13 metals** | ...nt < 5`:  **vlm_count = 0 → 74 metals** **vlm_count = 1 → 13 metals** **vlm_count = 2 → 16 metals** **vlm_cou... |
| 3 | 0 | counting | **vlm_count = 2 → 16 metals** | ... metals** **vlm_count = 1 → 13 metals** **vlm_count = 2 → 16 metals** **vlm_count = 3 → 3 metals** **vlm_coun... |
| 4 | 0 | counting | **vlm_count = 3 → 3 metals** | ... metals** **vlm_count = 2 → 16 metals** **vlm_count = 3 → 3 metals** **vlm_count = 4 → 3 metals**  **Total w... |
| 5 | 0 | counting | **vlm_count = 4 → 3 metals** | ...6 metals** **vlm_count = 3 → 3 metals** **vlm_count = 4 → 3 metals**  **Total with < 5 VLM measurements: 109... |
| 6 | 0 | counting | **Total with < 5 VLM measurements: 109** | ... metals** **vlm_count = 4 → 3 metals**  **Total with < 5 VLM measurements: 109**  ---   \| Metric \| Value \| \|---\|---\| \| T... |
| 7 | 0 | exact_value | \| Metals with < 5 VLM measurements \| **109** \| | ...-\| \| Total metals in SRD-46 \| **230** \| \| Metals with < 5 VLM measurements \| **109** \| \| Fraction of all metals \| **109 / 230 ... |
| 8 | 0 | exact_value | \| Fraction of all metals \| **109 / 230 ≈ 47.4%** \| | ...s with < 5 VLM measurements \| **109** \| \| Fraction of all metals \| **109 / 230 ≈ 47.4%** \|... |
| 9 | 1 | exact_value | \| 0 \| 74 \| | ...LM count \| Number of metals \| \|---\|---\| \| 0 \| 74 \| \| 1 \| 13 \| \| 2 \| 16 \| \| 3 \| 3 \| \| 4 \| 3... |
| 10 | 1 | exact_value | \| 1 \| 13 \| | ...Number of metals \| \|---\|---\| \| 0 \| 74 \| \| 1 \| 13 \| \| 2 \| 16 \| \| 3 \| 3 \| \| 4 \| 3 \| \| **Tota... |
| 11 | 1 | exact_value | \| 2 \| 16 \| | ...etals \| \|---\|---\| \| 0 \| 74 \| \| 1 \| 13 \| \| 2 \| 16 \| \| 3 \| 3 \| \| 4 \| 3 \| \| **Total < 5** \| *... |
| 12 | 1 | exact_value | \| 3 \| 3 \| | ...-\|---\| \| 0 \| 74 \| \| 1 \| 13 \| \| 2 \| 16 \| \| 3 \| 3 \| \| 4 \| 3 \| \| **Total < 5** \| **109** \|  ... |
| 13 | 1 | exact_value | \| 4 \| 3 \| | ... \| 74 \| \| 1 \| 13 \| \| 2 \| 16 \| \| 3 \| 3 \| \| 4 \| 3 \| \| **Total < 5** \| **109** \|  Nearly hal... |
| 14 | 1 | exact_value | \| **Total < 5** \| **109** \| | ...1 \| 13 \| \| 2 \| 16 \| \| 3 \| 3 \| \| 4 \| 3 \| \| **Total < 5** \| **109** \|  Nearly half of all metal entries in NI... |
| 15 | 1 | comparison | Nearly half of all metal entries in NIST SRD-46 have fewer than 5 VLM measurements. | ... \| 4 \| 3 \| \| **Total < 5** \| **109** \|  Nearly half of all metal entries in NIST SRD-46 have fewer than 5 VLM measurements. The vast majority of these (74 out of 1... |
| 16 | 1 | counting | The vast majority of these (74 out of 109) have **zero** measurements | ...-46 have fewer than 5 VLM measurements. The vast majority of these (74 out of 109) have **zero** measurements — including noble gases (He, Ne, Ar, Kr... |