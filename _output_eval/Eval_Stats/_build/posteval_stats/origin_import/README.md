# Origin Import Bundle

- `all_csv/`: normalized copies of every CSV under `../csv/` with `nan` cells blanked for OriginPro import.
- `plot_ready/`: extra wide tables for heatmaps, verified-share and claim-type major-section facets, per-model major-section stacked bars, tool-usage grouped bars, and prompt-difficulty ranking.
- `convert_posteval_csvs_for_origin.py`: rerun the export after any CSV changes.

Typical usage:

```bash
python convert_posteval_csvs_for_origin.py
```