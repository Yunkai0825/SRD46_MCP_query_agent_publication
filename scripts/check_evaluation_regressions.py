"""Offline regression checks for evaluation database selection and cache roots."""
from __future__ import annotations
from pathlib import Path
import sqlite3
import sys
import tempfile
import threading
from contextlib import closing
from concurrent.futures import ThreadPoolExecutor
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.dont_write_bytecode = True
from SRD46_query_output_eval_pipeline.db_support_helpers import db_reference
from SRD46_query_output_eval_pipeline.regex_enricher import enricher

class EvaluationRegressionChecks(unittest.TestCase):
    def setUp(self):
        scratch = ROOT / '__tmp__'
        scratch.mkdir(exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix='evaluation_regression_', dir=scratch)
        self.root = Path(self.temp.name)
        self.addCleanup(self.temp.cleanup)

    def test_default_database_checks_packages_before_use(self):
        with patch.object(db_reference, 'ensure_packaged_files') as restore:
            selected = db_reference._database_directory(None)
        restore.assert_called_once_with()
        self.assertEqual(selected, db_reference.REPO_ROOT / 'SRD46_db')

    def test_external_databases_are_independent(self):
        for name in db_reference.DB_NAMES.values():
            with closing(sqlite3.connect(self.root / name)) as db:
                db.execute('CREATE TABLE sample(value INTEGER)')
                db.execute('INSERT INTO sample VALUES (46)')
                db.commit()
        with patch.object(db_reference, 'ensure_packaged_files') as restore:
            conn = db_reference.open_reference_connection(self.root)
            try:
                for alias in db_reference.DB_NAMES:
                    self.assertEqual(conn.execute(f'SELECT value FROM {alias}.sample').fetchone()[0], 46)
            finally:
                conn.close()
            self.assertEqual(set(db_reference.db_fingerprints(self.root)), set(db_reference.DB_NAMES))
        restore.assert_not_called()

    def test_custom_cache_uses_requested_root_and_resets_after_return(self):
        expected = self.root / 'Model_fixture' / 'Qfixture'
        sentinel = object()
        def cached(*args, **kwargs):
            self.assertEqual(enricher._claims_cache_dir('fixture', 'Qfixture'), expected)
            return sentinel
        with patch.object(enricher, '_load_claims_cache', side_effect=cached):
            result = enricher.enrich_run_claims('fixture', 'Qfixture', 1, eval_root=self.root)
        self.assertIs(result, sentinel)
        self.assertIsNone(enricher._claims_eval_root.get())
        self.assertTrue(expected.is_dir())

    def test_cache_root_resets_after_failure(self):
        with patch.object(enricher, '_load_claims_cache', side_effect=RuntimeError('fixture error')):
            with self.assertRaisesRegex(RuntimeError, 'fixture error'):
                enricher.enrich_run_claims('fixture', 'Qfixture', 1, eval_root=self.root)
        self.assertIsNone(enricher._claims_eval_root.get())

    def test_concurrent_runs_do_not_share_cache_roots(self):
        barrier = threading.Barrier(2)
        def cached(model, question_id, *args, **kwargs):
            barrier.wait(timeout=10)
            self.assertEqual(enricher._claims_cache_dir(model, question_id),
                             self.root / model / f'Model_{model}' / question_id)
            return object()
        def run(model):
            enricher.enrich_run_claims(model, 'Qfixture', 1, eval_root=self.root / model)
            self.assertIsNone(enricher._claims_eval_root.get())
        with patch.object(enricher, '_load_claims_cache', side_effect=cached):
            with ThreadPoolExecutor(max_workers=2) as pool:
                list(pool.map(run, ['first', 'second']))

if __name__ == '__main__':
    unittest.main()
