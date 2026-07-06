# Q2.1.2 - Validation (batch 3)

**24 of 46 claims unsupported**

| # | Para | Type | Unsupported Claim | Context |
|---|------|------|-------------------|---------|
| 1 | 0 | exact_value | \| Mn²⁺ \| **1.00** \| vlm_173099 \| | ... \| vlm_id \| \|-------\|--------\|--------\| \| Mn²⁺ \| **1.00** \| vlm_173099 \| \| Co²⁺ \| **2.11** \| vlm_173133 \| \| Zn²⁺... |
| 2 | 0 | exact_value | \| Co²⁺ \| **2.11** \| vlm_173133 \| | ...-----\| \| Mn²⁺ \| **1.00** \| vlm_173099 \| \| Co²⁺ \| **2.11** \| vlm_173133 \| \| Zn²⁺ \| **2.37** \| vlm_173205 \| \| Ni²⁺... |
| 3 | 0 | exact_value | \| Zn²⁺ \| **2.37** \| vlm_173205 \| | ...3099 \| \| Co²⁺ \| **2.11** \| vlm_173133 \| \| Zn²⁺ \| **2.37** \| vlm_173205 \| \| Ni²⁺ \| **2.80** \| vlm_173181 \| \| Cu²⁺... |
| 4 | 0 | exact_value | \| Ni²⁺ \| **2.80** \| vlm_173181 \| | ...3133 \| \| Zn²⁺ \| **2.37** \| vlm_173205 \| \| Ni²⁺ \| **2.80** \| vlm_173181 \| \| Cu²⁺ \| **4.31** \| vlm_173157 \|  > **F... |
| 5 | 0 | exact_value | \| Cu²⁺ \| **4.31** \| vlm_173157 \| | ...3205 \| \| Ni²⁺ \| **2.80** \| vlm_173181 \| \| Cu²⁺ \| **4.31** \| vlm_173157 \|  > **Fe²⁺** — No log β₁ entry was found... |
| 6 | 0 | existence_absence | > **Fe²⁺** — No log β₁ entry was found at I ≤ 0.5 M in the database. | ...181 \| \| Cu²⁺ \| **4.31** \| vlm_173157 \|  > **Fe²⁺** — No log β₁ entry was found at I ≤ 0.5 M in the database. This is unsurprising: Fe²⁺–NH₃ complexe... |
| 7 | 0 | existence_absence | reliable measurements are scarce | ...n a persistent experimental problem, so reliable measurements are scarce.... |
| 8 | 1 | exact_value | Mn²⁺ (1.00) | ...### Observed ordering  **Mn²⁺ (1.00) < Co²⁺ (2.11) < Zn²⁺ (2.37) < Ni²⁺ (2.8... |
| 9 | 1 | exact_value | Co²⁺ (2.11) | ...### Observed ordering  **Mn²⁺ (1.00) < Co²⁺ (2.11) < Zn²⁺ (2.37) < Ni²⁺ (2.80) < Cu²⁺ (4.3... |
| 10 | 1 | exact_value | Zn²⁺ (2.37) | ...ordering  **Mn²⁺ (1.00) < Co²⁺ (2.11) < Zn²⁺ (2.37) < Ni²⁺ (2.80) < Cu²⁺ (4.31)**... |
| 11 | 1 | exact_value | Ni²⁺ (2.80) | ...²⁺ (1.00) < Co²⁺ (2.11) < Zn²⁺ (2.37) < Ni²⁺ (2.80) < Cu²⁺ (4.31)**... |
| 12 | 1 | exact_value | Cu²⁺ (4.31) | ...²⁺ (2.11) < Zn²⁺ (2.37) < Ni²⁺ (2.80) < Cu²⁺ (4.31)**... |
| 13 | 2 | exact_value | \| Mn²⁺ weakest \| Lowest of the series \| log β₁ = 1.00 (lowest) \| ✅ \| | ...---------------\|-------------\|--------\| \| Mn²⁺ weakest \| Lowest of the series \| log β₁ = 1.00 (lowest) \| ✅ \| \| Co²⁺ < Ni²⁺ \| Monotonic increase \| 2.... |
| 14 | 2 | exact_value | \| Co²⁺ < Ni²⁺ \| Monotonic increase \| 2.11 < 2.80 \| ✅ \| | ...e series \| log β₁ = 1.00 (lowest) \| ✅ \| \| Co²⁺ < Ni²⁺ \| Monotonic increase \| 2.11 < 2.80 \| ✅ \| \| Cu²⁺ is the maximum \| Strongest compl... |
| 15 | 2 | exact_value | \| Cu²⁺ is the maximum \| Strongest complex \| 4.31 (highest) \| ✅ \| | ... Monotonic increase \| 2.11 < 2.80 \| ✅ \| \| Cu²⁺ is the maximum \| Strongest complex \| 4.31 (highest) \| ✅ \| \| Cu²⁺ > Zn²⁺ \| Drop after Cu \| 4.31 > ... |
| 16 | 2 | exact_value | \| Cu²⁺ > Zn²⁺ \| Drop after Cu \| 4.31 > 2.37 \| ✅ \| | ...trongest complex \| 4.31 (highest) \| ✅ \| \| Cu²⁺ > Zn²⁺ \| Drop after Cu \| 4.31 > 2.37 \| ✅ \| \| Zn²⁺ < Ni²⁺ \| Zn falls back below Ni ... |
| 17 | 2 | exact_value | \| Zn²⁺ < Ni²⁺ \| Zn falls back below Ni \| 2.37 < 2.80 \| ✅ \| | ...n²⁺ \| Drop after Cu \| 4.31 > 2.37 \| ✅ \| \| Zn²⁺ < Ni²⁺ \| Zn falls back below Ni \| 2.37 < 2.80 \| ✅ \|  **Yes — the ammonia log β₁ values foll... |
| 18 | 2 | trend | the ammonia log β₁ values follow the Irving–Williams series. | ...k below Ni \| 2.37 < 2.80 \| ✅ \|  **Yes — the ammonia log β₁ values follow the Irving–Williams series.** Every testable prediction of the seri... |
| 19 | 2 | comparison | Every testable prediction of the series is confirmed by the SRD-46 data. | ...es follow the Irving–Williams series.** Every testable prediction of the series is confirmed by the SRD-46 data. The characteristic "hump" at Cu²⁺ is st... |
| 20 | 2 | trend | The characteristic "hump" at Cu²⁺ is striking | ...series is confirmed by the SRD-46 data. The characteristic "hump" at Cu²⁺ is striking: its log β₁ is nearly **1.5 log units**... |
| 21 | 2 | calculation | its log β₁ is nearly **1.5 log units** above the next strongest binder (Ni²⁺) | ...racteristic "hump" at Cu²⁺ is striking: its log β₁ is nearly **1.5 log units** above the next strongest binder (Ni²⁺) and more than **3 log units** above Mn²... |
| 22 | 2 | calculation | more than **3 log units** above Mn²⁺. | ...ve the next strongest binder (Ni²⁺) and more than **3 log units** above Mn²⁺. This reflects the Jahn–Teller-enhanced ... |
| 23 | 2 | existence_absence | The absence of Fe²⁺ data | ...tions without any crystal-field bonus.  The absence of Fe²⁺ data is itself consistent with the series: F... |
| 24 | 2 | comparison | (log β₁ somewhere between Mn²⁺ and Co²⁺) | ...Fe²⁺–NH₃ binding is expected to be weak (log β₁ somewhere between Mn²⁺ and Co²⁺), and the experimental difficulty of wor... |