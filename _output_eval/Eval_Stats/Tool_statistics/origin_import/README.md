# Origin Import Bundle

- `all_csv/`: normalized copies of every CSV under `../csv/` with `nan` cells blanked for OriginPro import.
- `plot_ready/`: wide tables for the major-section run-timing grouped-bar plot, the mean successful step-header tool-duration chart, the mean deduced wall-time-per-call chart excluding the final pre-answer group, the mean Argo `_meta` timing chart, the compactor trigger/context/selection/retry charts, and the top second-order tool-chain chart.
- `convert_tool_stats_csvs_for_origin.py`: rerun the export after any CSV changes.

Typical usage:

```bash
python convert_tool_stats_csvs_for_origin.py
```