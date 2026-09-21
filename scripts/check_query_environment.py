"""Check the locked SRD query environment locally without model requests."""
from __future__ import annotations

import argparse
import asyncio
import hashlib
import importlib.metadata as metadata
import io
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import tomllib
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


async def check_mcp():
    from agent_runtime import MCPManager
    manager = MCPManager()
    try:
        tools, _ = await manager.setup()
        names = {tool["name"] for tool in tools}
        required = {"search_metals", "search_ligands", "0_preplan_decision", "0_plan_search_strategy"}
        if not required <= names:
            raise RuntimeError(f"Missing MCP tools: {sorted(required - names)}")
        result = await manager.call_tool("search_metals", {"symbol": "Cu", "limit": 3})
        text = "\n".join(getattr(block, "text", "") for block in result.content)
        if getattr(result, "is_error", False) or "Cu" not in text:
            raise RuntimeError("MCP copper search failed or returned no copper result")
        return {"tool_count": len(tools), "copper_search": "passed"}
    finally:
        await manager.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, help="Write validation and installed package versions as JSON")
    args = parser.parse_args()
    os.chdir(ROOT)
    os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
    os.environ["PYTHONIOENCODING"] = "utf-8"
    os.environ["ARGO_API_USER"] = "offline-environment-check"
    sys.dont_write_bytecode = True
    expected_python = (ROOT / ".python-version").read_text().strip()
    if platform.python_version() != expected_python:
        raise RuntimeError(f"Use Python {expected_python}; found {platform.python_version()}")
    project = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    for requirement in project["project"]["dependencies"]:
        name, expected = requirement.split("==", 1)
        actual = metadata.version(name)
        if actual != expected:
            raise RuntimeError(f"{name}: expected {expected}, found {actual}; run uv sync --locked")
    from workspace_setup import ensure_packaged_files
    ensure_packaged_files()

    cards = ROOT / "SRD46_db" / "srd46_cards.db"
    with cards.open("rb") as stream:
        if stream.read(16) != b"SQLite format 3\x00":
            raise RuntimeError("The cards database is missing or is not a restored SQLite file")
        stream.seek(0)
        cards_sha256 = hashlib.file_digest(stream, "sha256").hexdigest()

    import argo_client
    import freeform_runner
    import query_agent
    from SRD46_tools.Search_tools.entity_search import search_metals
    from rdkit import Chem
    from rdkit.Chem import inchi
    molecule = Chem.MolFromSmiles("NCC(=O)O")
    if molecule is None or not inchi.MolToInchi(molecule).startswith("InChI="):
        raise RuntimeError("RDKit SMILES/InChI conversion failed")
    rows = search_metals(symbol="Cu", limit=3)
    if not rows or not all("Cu" in row["symbol"] for row in rows):
        raise RuntimeError("Direct copper search failed")

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    figure, axis = plt.subplots()
    axis.plot([0, 1], [0, 1])
    png = io.BytesIO()
    figure.savefig(png, format="png")
    plt.close(figure)
    if not png.getvalue().startswith(b"\x89PNG\r\n\x1a\n"):
        raise RuntimeError("Plot rendering failed")

    from NIST_SRD46_database_browser.app import app
    app.config["TESTING"] = True
    with app.test_client() as client:
        response = client.get("/metals", follow_redirects=True)
        if response.status_code != 200:
            raise RuntimeError(f"Browser metal page failed: HTTP {response.status_code}")
    mcp = asyncio.run(asyncio.wait_for(check_mcp(), timeout=180))
    cli = subprocess.run([sys.executable, "-B", "API_SRD46_Query_UI.py", "query", "--help"],
                         cwd=ROOT, capture_output=True, text=True, encoding="utf-8", timeout=120)
    if cli.returncode or "--model" not in cli.stdout:
        raise RuntimeError(f"Query CLI check failed: {cli.stderr}")
    packages = {dist.metadata["Name"]: dist.version for dist in metadata.distributions() if dist.metadata.get("Name")}
    report = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "provenance": "Current validated environment; not a recovered historical experiment environment",
        "python": platform.python_version(), "python_build": sys.version,
        "platform": platform.platform(), "sqlite": __import__("sqlite3").sqlite_version,
        "source_base_commit": "103b24eaf92610b3d90c2daa159238519d99b71a",
        "cards_database_sha256": cards_sha256,
        "checks": {"direct_dependency_versions": "passed", "imports": "passed", "rdkit_smiles_inchi": "passed",
                   "plot_png": "passed", "direct_copper_rows": len(rows), "browser_metals_http": 200,
                   "mcp": mcp, "query_cli_help": "passed"},
        "packages": dict(sorted(packages.items(), key=lambda item: item[0].lower())),
    }
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "passed", "python": report["python"], "packages": len(packages), "checks": report["checks"]}, indent=2))


if __name__ == "__main__":
    main()
