# Reproducible SRD-46 query environment

This specification targets the standalone [SRD46_MCP_query_agent_publication](https://github.com/Yunkai0825/SRD46_MCP_query_agent_publication) code at commit `103b24eaf92610b3d90c2daa159238519d99b71a`. It covers the MCP server/client, query agent, chemical identifier handling, browser, query-evaluation plotting, and developer checks. It does not specify the separate SRD-46 research/Analysis framework.

The software release is **v1.0.0(R)**. Its Python environment metadata uses the PEP 440-compatible version `1.0.0.post1`; the GitHub tag and Zenodo version retain the requested release name.

## What is recorded

- `.python-version`: Python **3.13.13**, the interpreter patch version used for validation.
- `pyproject.toml`: exact direct dependency versions and a separate pytest development group. The locked environment is restricted to Python 3.13; the original source advertised Python 3.11+, which is not a claim that this lock was tested on those older interpreters.
- `uv.lock`: exact resolved direct and transitive dependencies, source URLs, distribution hashes, and platform conditions. Generated with **uv 0.8.15**.
- Root `requirements.txt`: hash-pinned pip export of the same lock, including the development group. This is the only requirements file; browser dependencies are included here.
- `environment-validation.json`: validation platform, interpreter/build, SQLite version, database checksum, check outcomes, and every installed package version.
- `environment-versions.txt`: installed-version snapshot from the clean Windows validation environment (`uv pip freeze`); use the platform-aware lock or root requirements for installation.

## Install and run

Install Python **3.13.13** first and make it discoverable on PATH. The validated interpreter was the Windows x86-64 Conda-forge build. Install uv if needed; version 0.8.15 was used for this verification:

```sh
python -m pip install uv==0.8.15
uv sync --locked
uv run --locked python -B scripts/check_query_environment.py
uv run --locked python API_SRD46_Query_UI.py query --help
```

Run these commands from the repository root. `uv sync` creates a local `.venv`; it does not need to modify an existing shared Python installation. `--locked` rejects dependency metadata that would require changing the committed lock. Other platforms have not been executed in this verification, even where dependency wheels are present in the lock.

The query check automatically restores missing packaged databases from this checkout before opening `SRD46_db/srd46_cards.db`. [PACKAGED_DATA.md](./PACKAGED_DATA.md) lists the current database packages and provides an independent byte-for-byte verification command. The validation report records the actual cards database checksum; it does not establish that this database revision was used for the historical benchmark results. The check validates imports, RDKit SMILES/InChI conversion, PNG plotting, a direct copper search, the browser metal page, an actual local MCP stdio connection and copper search, and query CLI help. It makes no Argo/model or PubChem requests and overrides the API identity in its own process with an offline-check value. It does not run the full benchmark or validate the other three database assets.

For a live query, set your own `ARGO_API_USER` and the appropriate API endpoint/model configuration, as described in INSTALLATION_GUIDE.md. API access, server-side model versions, and database/artifact revisions remain separate requirements; a Python dependency lock does not freeze a hosted model service.

### Pip alternative

Using Python 3.13.13, create and activate a fresh virtual environment, then install the hash-pinned export:

```sh
python -m venv .venv
# Windows PowerShell: .\.venv\Scripts\Activate.ps1
# POSIX shell: source .venv/bin/activate
python -m pip install --require-hashes -r requirements.txt
python -B scripts/check_query_environment.py
```

## Historical provenance

The original GitHub history contains two commits: initial release `d57484ef74211ffffa8b3dad1a4e08d4e32e0b94` (6 July 2026) and the citation-only update `103b24eaf92610b3d90c2daa159238519d99b71a` (7 July 2026). Both used unpinned dependency names except `sqlglot>=23.0`, and neither included a lock, installed-version snapshot, or exact Python patch version. See the [original requirements](https://github.com/Yunkai0825/SRD46_MCP_query_agent_publication/blob/d57484ef74211ffffa8b3dad1a4e08d4e32e0b94/requirements.txt).

This is a **newly validated reproducible environment**, prepared on 21 September 2026. Direct dependency pins were taken from the available working Python installation; transitive dependencies were resolved into a fresh, isolated environment. The included version snapshot records that fresh environment. These files do **not** establish that identical versions were used for the manuscript's original experiments, and no benchmark results were regenerated. Recovering that provenance would require a contemporaneous environment snapshot or equivalent execution records.

LangChain is not installed: the published query path uses direct Argo calls and already treats its older LangChain wrapper as optional. Omitting it matches the original standalone requirements. Chemistry dependencies are included even where the source permits fallbacks, because missing RDKit or PubChemPy can change query behavior.

## Check or update the specification

```sh
uv lock --check
uv pip check --python .venv
uv run --locked python -B scripts/check_query_environment.py --report environment-validation.json
uv pip freeze --python .venv > environment-versions.txt
```

Focused offline regression checks for the maintenance fixes are also included:

```sh
uv run --locked python -B scripts/check_runtime_regressions.py
uv run --locked python -B scripts/check_evaluation_regressions.py
uv run --locked python -B scripts/check_tool_regressions.py
```

These checks exercise API retry/error handling with mocks, evaluation-cache isolation and database selection, and similarity/evidence preservation. They make no model requests and keep temporary fixtures under ignored `__tmp__/`.

The JSON report records all installed versions and the actual database checksum. After intentionally editing dependency pins, regenerate and review both install specifications:

```sh
uv lock
uv export --locked --format requirements.txt --no-emit-project --no-header --output-file requirements.txt
uv sync --locked
```

Then rerun validation and refresh its records. Keep package updates separate from claims about historical experiment versions.
