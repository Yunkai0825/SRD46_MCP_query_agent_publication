#!/usr/bin/env python3
"""
NIST SRD-46 Database Browser — Flask web application.

Usage:
    python app.py   # start server on http://localhost:5046
"""

import sys
import logging
from pathlib import Path
from flask import Flask, render_template

# ---------------------------------------------------------------------------
# Verbose logging by default — all enricher / classifier / grounder messages
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(name)s %(message)s",
)

# Ensure this package's directory is on sys.path when running as a script.
_BROWSER_DIR = str(Path(__file__).resolve().parent)
if __package__ in (None, "") and _BROWSER_DIR not in sys.path:
    sys.path.insert(0, _BROWSER_DIR)

if __package__:
    from . import db as dbmod
    from .request_dbs import close_dbs as close_request_dbs, get_cards, get_eq, get_fp, get_lit
    from .routes.metals import metals_bp
    from .routes.ligands import ligands_bp
    from .routes.stability import stability_bp
    from .routes.pka import pka_bp
    from .routes.equilibrium import eq_bp
    from .routes.literature import lit_bp
    from .routes.similarity import sim_bp
    from .routes.pourbaix import pourbaix_bp
    from .routes.agent import agent_bp
    from .routes.evaluation import eval_bp
else:
    import db as dbmod
    from request_dbs import close_dbs as close_request_dbs, get_cards, get_eq, get_fp, get_lit
    from routes.metals import metals_bp
    from routes.ligands import ligands_bp
    from routes.stability import stability_bp
    from routes.pka import pka_bp
    from routes.equilibrium import eq_bp
    from routes.literature import lit_bp
    from routes.similarity import sim_bp
    from routes.pourbaix import pourbaix_bp
    from routes.agent import agent_bp
    from routes.evaluation import eval_bp

PER_PAGE = 30

app = Flask(__name__)


@app.teardown_appcontext
def teardown_dbs(exc):
    close_request_dbs(exc)

app.register_blueprint(metals_bp)
app.register_blueprint(ligands_bp)
app.register_blueprint(stability_bp)
app.register_blueprint(pka_bp)
app.register_blueprint(eq_bp)
app.register_blueprint(lit_bp)
app.register_blueprint(sim_bp)
app.register_blueprint(pourbaix_bp)
app.register_blueprint(agent_bp)
app.register_blueprint(eval_bp)


# ---------------------------------------------------------------------------
# Dashboard
# ---------------------------------------------------------------------------

@app.route("/")
def index():
    db = get_cards()
    stats = {
        "metals": db.execute("SELECT COUNT(*) FROM metal_card").fetchone()[0],
        "ligands": db.execute("SELECT COUNT(*) FROM ligand_card").fetchone()[0],
        "measurements": db.execute(
            "SELECT COUNT(*) FROM ligandmetal_stability_measured"
        ).fetchone()[0],
        "pka": db.execute("SELECT COUNT(*) FROM ligand_pka_measured").fetchone()[0],
    }

    stats["citations"] = db.execute(
        "SELECT COUNT(*) FROM ref_literature_alt"
    ).fetchone()[0]

    stats["pourbaix"] = len(dbmod.get_pourbaix_data())

    # Top-10 metals by measurement count
    top_metals = dbmod.rows_to_dicts(
        db.execute(
            """SELECT m.metal_id, m.metal_name_SRD, m.symbol_pure, m.charge,
                      COUNT(*) AS cnt
               FROM ligandmetal_card c
               JOIN metal_card m ON c.metal_id = m.metal_id
               GROUP BY c.metal_id
               ORDER BY cnt DESC LIMIT 10"""
        )
    )

    # Top-10 ligand classes
    top_classes = dbmod.rows_to_dicts(
        db.execute(
            """SELECT ligand_class_name, COUNT(*) AS cnt
               FROM ligand_card
               WHERE ligand_class_name IS NOT NULL
               GROUP BY ligand_class_name
               ORDER BY cnt DESC LIMIT 10"""
        )
    )

    # Periodic table data: count of ligandmetal_card entries per metal symbol
    pt_data = dbmod.rows_to_dicts(
        db.execute(
            """SELECT m.symbol_pure AS symbol, COUNT(*) AS count
               FROM ligandmetal_card c
               JOIN metal_card m ON c.metal_id = m.metal_id
               GROUP BY m.symbol_pure"""
        )
    )

    return render_template(
        "index.html",
        stats=stats,
        top_metals=top_metals,
        top_classes=top_classes,
        pt_data=pt_data,
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import os
    status = dbmod.verify_all_paths()
    for name, ok in status.items():
        print(f"  {'✓' if ok else '✗'} {name}")
    # Debug/auto-reloader is OFF by default; the watchdog reloader will
    # restart the server mid-run and kill any in-flight agent thread.
    # Set FLASK_DEBUG=1 to enable it for template/route hot-reload work.
    debug = os.environ.get("FLASK_DEBUG", "0") not in ("", "0", "false", "False")
    app.run(host="127.0.0.1", port=5046, debug=debug, use_reloader=debug)
