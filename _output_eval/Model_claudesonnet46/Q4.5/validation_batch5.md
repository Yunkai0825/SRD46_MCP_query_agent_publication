# Q4.5 - Validation (batch 5)

**29 of 108 claims unsupported**

| # | Para | Type | Unsupported Claim | Context |
|---|------|------|-------------------|---------|
| 1 | 0 | counting | 644 ligands | ... *Source: NIST SRD-46 — metal_25 (Ca²⁺, 644 ligands, 1761 VLMs)*  ---... |
| 2 | 0 | counting | 1761 VLMs | ...T SRD-46 — metal_25 (Ca²⁺, 644 ligands, 1761 VLMs)*  ---... |
| 3 | 1 | comparison | dominated by **citric acid | ... °C) returned the highest-ranked values dominated by **citric acid at log β₁ = 4.68** (water, I = 0.0, 25 ... |
| 4 | 1 | exact_value | log β₁ = 4.68 | ...ed values dominated by **citric acid at log β₁ = 4.68** (water, I = 0.0, 25 °C), confirmed ac... |
| 5 | 1 | listing | water | ...ed by **citric acid at log β₁ = 4.68** (water, I = 0.0, 25 °C), confirmed across mult... |
| 6 | 1 | exact_value | I = 0.0 | ...*citric acid at log β₁ = 4.68** (water, I = 0.0, 25 °C), confirmed across multiple inde... |
| 7 | 1 | counting | confirmed across multiple independent measurements. | ...og β₁ = 4.68** (water, I = 0.0, 25 °C), confirmed across multiple independent measurements.... |
| 8 | 2 | range | (20–30 °C) | ...### pKa Values Retrieved (20–30 °C)  From `search_pka_values` for the five ... |
| 9 | 2 | citation | From `search_pka_values` | ...### pKa Values Retrieved (20–30 °C)  From `search_pka_values` for the five key ligands:  \| Ligand \| S... |
| 10 | 2 | counting | the five key ligands | ...20–30 °C)  From `search_pka_values` for the five key ligands:  \| Ligand \| SRD-46 ID \| pKa₁ \| pKa₂ \| ... |
| 11 | 2 | exact_value | \| Citric acid \| ligand_9059 \| ~3.1 \| ~4.8 \| 6.40 \| **6.40** \| | ... \| 2.33 \| 9.57 \| — \| **9.57** (–NH₃⁺) \| \| Citric acid \| ligand_9059 \| ~3.1 \| ~4.8 \| 6.40 \| **6.40** \|... |
| 12 | 3 | exact_value | confirmed citric acid value (log K₁ = 4.68) | ...ombining SRD-46 retrieved data with the confirmed citric acid value (log K₁ = 4.68) and literature-consistent values for th... |
| 13 | 3 | comparison | literature-consistent values for the other ligands within the same database | ...d citric acid value (log K₁ = 4.68) and literature-consistent values for the other ligands within the same database:  \| Ligand \| Donor type \| Highest pKa \|... |
| 14 | 3 | exact_value | \| Oxalic acid \| –COO⁻ × 2 \| 3.80 \| ~3.0 \| bidentate \| | ...---\|----------------------\|-----------\| \| Oxalic acid \| –COO⁻ × 2 \| 3.80 \| ~3.0 \| bidentate \| \| Succinic acid \| –COO⁻ × 2 \| 5.24 \| ~1... |
| 15 | 3 | exact_value | \| Succinic acid \| –COO⁻ × 2 \| 5.24 \| ~1.8 \| flexible bidentate \| | ...\| –COO⁻ × 2 \| 3.80 \| ~3.0 \| bidentate \| \| Succinic acid \| –COO⁻ × 2 \| 5.24 \| ~1.8 \| flexible bidentate \| \| Malonic acid \| –COO⁻ × 2 \| 5.27 \| ~2.... |
| 16 | 3 | exact_value | \| Malonic acid \| –COO⁻ × 2 \| 5.27 \| ~2.4 \| bidentate \| | ... 2 \| 5.24 \| ~1.8 \| flexible bidentate \| \| Malonic acid \| –COO⁻ × 2 \| 5.27 \| ~2.4 \| bidentate \| \| Citric acid \| –COO⁻ × 3, –OH \| 6.40 \|... |
| 17 | 3 | exact_value | \| Citric acid \| –COO⁻ × 3, –OH \| 6.40 \| **4.68** ✓ SRD-46 \| tridentate \| | ...\| –COO⁻ × 2 \| 5.27 \| ~2.4 \| bidentate \| \| Citric acid \| –COO⁻ × 3, –OH \| 6.40 \| **4.68** ✓ SRD-46 \| tridentate \| \| Glycine \| –COO⁻, –NH₂ \| 9.57 \| ~1.4 \|... |
| 18 | 3 | exact_value | \| Glycine \| –COO⁻, –NH₂ \| 9.57 \| ~1.4 \| bidentate \| | ...6.40 \| **4.68** ✓ SRD-46 \| tridentate \| \| Glycine \| –COO⁻, –NH₂ \| 9.57 \| ~1.4 \| bidentate \|  > ✓ = directly confirmed from SRD-46 `... |
| 19 | 3 | citation | ✓ = directly confirmed from SRD-46 `search_stability` query | ...O⁻, –NH₂ \| 9.57 \| ~1.4 \| bidentate \|  > ✓ = directly confirmed from SRD-46 `search_stability` query... |
| 20 | 4 | trend | Within oxygen-donor carboxylates: moderate positive correlation | ...## Correlation Analysis  ### Within oxygen-donor carboxylates: moderate positive correlation  Plotting the carboxylate-only subset (... |
| 21 | 4 | listing | (oxalate, malonate, succinate, citrate) | ...n  Plotting the carboxylate-only subset (oxalate, malonate, succinate, citrate) against their highest pKa and log K₁:  ... |
| 22 | 4 | exact_value | \| Oxalic acid \| 3.80 \| ~3.0 \| | ... K₁ \| \|--------\|-------------\|--------\| \| Oxalic acid \| 3.80 \| ~3.0 \| \| Malonic acid \| 5.27 \| ~2.4 \| \| Succin... |
| 23 | 4 | exact_value | \| Malonic acid \| 5.27 \| ~2.4 \| | ...--------\| \| Oxalic acid \| 3.80 \| ~3.0 \| \| Malonic acid \| 5.27 \| ~2.4 \| \| Succinic acid \| 5.24 \| ~1.8 \| \| Citri... |
| 24 | 4 | exact_value | \| Succinic acid \| 5.24 \| ~1.8 \| | ...\| ~3.0 \| \| Malonic acid \| 5.27 \| ~2.4 \| \| Succinic acid \| 5.24 \| ~1.8 \| \| Citric acid \| 6.40 \| 4.68 \|  The tren... |
| 25 | 4 | exact_value | \| Citric acid \| 6.40 \| 4.68 \| | ... ~2.4 \| \| Succinic acid \| 5.24 \| ~1.8 \| \| Citric acid \| 6.40 \| 4.68 \|  The trend is **not strictly monotonic*... |
| 26 | 4 | trend | The trend is **not strictly monotonic** within diacids | ...\| ~1.8 \| \| Citric acid \| 6.40 \| 4.68 \|  The trend is **not strictly monotonic** within diacids (oxalate > malonate > succinate despite... |
| 27 | 4 | comparison | (oxalate > malonate > succinate despite lower pKa) | ...not strictly monotonic** within diacids (oxalate > malonate > succinate despite lower pKa), revealing that **chelate ring geometry... |
| 28 | 7 | exact_value | \| Citric acid log K₁ = 4.68 (SRD-46 confirmed) \| Tridentate O-donor + moderate pKa = strong Ca²⁺ binder \| | ...ation \| \|-------------\|---------------\| \| Citric acid log K₁ = 4.68 (SRD-46 confirmed) \| Tridentate O-donor + moderate pKa = strong Ca²⁺ binder \| \| Oxalate > malonate > succinate (despi... |
| 29 | 7 | comparison | \| Oxalate > malonate > succinate (despite similar pKa) \| Chelate ring geometry overrides basicity within diacids \| | ...r + moderate pKa = strong Ca²⁺ binder \| \| Oxalate > malonate > succinate (despite similar pKa) \| Chelate ring geometry overrides basicity within diacids \| \| Glycine (pKa 9.57) has low Ca²⁺ affin... |