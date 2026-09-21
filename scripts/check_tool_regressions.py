"""Check SRD-46 retrieval and evidence regressions without model calls.

Run from any directory with the repository environment::

    python scripts/check_tool_regressions.py

The checks exercise synthetic ranking/error cases and real packaged databases.
Network connections are blocked and all real SQLite connections use query_only.
Missing packaged databases are restored by normal startup. Reports are written
only under __tmp__/tool_regression_checks; benchmark answers are never rerun.
"""
from __future__ import annotations
import ast
from contextlib import contextmanager
import copy
import importlib
import json
from pathlib import Path
import socket
import sqlite3
import sys
import time
import traceback
from unittest.mock import patch, MagicMock
sys.dont_write_bytecode = True
sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / '__tmp__' / 'tool_regression_checks'
HERE.mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(ROOT))
RESULTS = []
ATTEMPTS = []

def audit(event, args):
    if event == 'socket.connect':
        ATTEMPTS.append(str(args))
        raise RuntimeError('No network/model requests allowed')
sys.addaudithook(audit)
CONNECT = sqlite3.connect
DBS = set()

def readonly(database, *args, **kwargs):
    conn = CONNECT(database, *args, **kwargs)
    if str(database) != ':memory:':
        conn.execute('PRAGMA query_only=ON')
        assert conn.execute('PRAGMA query_only').fetchone()[0] == 1
        DBS.add(str(database))
    return conn
sqlite3.connect = readonly

def check(name, fn):
    print('CHECK', name, flush=True)
    start = time.monotonic()
    try:
        detail = fn()
        RESULTS.append({'name': name, 'passed': True, 'seconds': round(time.monotonic() - start, 3), 'detail': detail})
        print('PASS', name, flush=True)
    except Exception as exc:
        RESULTS.append({'name': name, 'passed': False, 'seconds': round(time.monotonic() - start, 3), 'error': repr(exc), 'traceback': traceback.format_exc()})
        print('FAIL', name, repr(exc), flush=True)
    (HERE / 'tool_regression_validation.json').write_text(json.dumps({'checks': RESULTS, 'network_attempts': ATTEMPTS, 'real_sqlite_query_only': True, 'database_connections': sorted(DBS)}, indent=2), encoding='utf-8')
import SRD46_tools.Search_tools as tools
from SRD46_tools.Search_tools import similarity_search as sim, _db_connection as db, stability_search as stability
from SRD46_tools.Search_tools._tools_results_compactors import similar_ligand_compactor as sc, inspect_card_compactor as ic, stability_compactor as stc, network_compactor as nc
from SRD46_tools import compactor
VALUES = {}

def import_check():
    import server
    VALUES['server'] = server
    assert server.NT is tools
    assert db.CARDS_DB.parent == ROOT / 'SRD46_db'
    assert '_verify(FINGERPRINT_DB)' in (ROOT / 'SRD46_tools/Search_tools/similarity_search.py').read_text()
    paths = ['SRD46_tools/Search_tools/similarity_search.py', 'SRD46_tools/Search_tools/card_inspect.py', 'SRD46_tools/Search_tools/stability_search.py', 'SRD46_tools/Search_tools/_tools_results_compactors/similar_ligand_compactor.py', 'SRD46_tools/Search_tools/_tools_results_compactors/inspect_card_compactor.py', 'SRD46_tools/Search_tools/_tools_results_compactors/stability_compactor.py', 'SRD46_tools/Search_tools/_tools_results_compactors/network_compactor.py', 'SRD46_tools/compactor.py', 'server.py']
    for path in paths:
        ast.parse((ROOT / path).read_text(encoding='utf-8-sig'))
    assert 'speciation_hint' not in (ROOT / 'SRD46_tools/Search_tools/_tools_results_compactors/stability_compactor.py').read_text()
    return {'changed_python_files': len(paths), 'mcp_tools': len(server.mcp._tool_manager._tools)}
check('standalone_imports_and_restore_hook', import_check)

def validation():
    bad = [{'top_k': True}, {'top_k': 1.5}, {'top_k': 0}, {'top_k': 101}, {'metric': 'typo'}, {'min_similarity': True}, {'min_similarity': float('nan')}, {'min_similarity': float('inf')}, {'min_similarity': -0.1}, {'min_similarity': 1.1}, {'metal_ids': [True]}, {'metal_ids': 'metal_1'}]
    for changes in bad:
        kwargs = {'top_k': 10, 'metric': 'tanimoto_morgan', 'min_similarity': 0.0, 'metal_ids': None}
        kwargs.update(changes)
        try:
            sim._validate_search_options(**kwargs)
        except ValueError:
            pass
        else:
            raise AssertionError(changes)
    for value in [True, 1.5, 'ligand_1x', 'metal_1', '0', 2 ** 63]:
        try:
            sim._positive_entity_id(value, 'ligand')
        except ValueError:
            pass
        else:
            raise AssertionError(value)
    assert sim._positive_entity_id('ligand_5760', 'ligand') == 5760
    return {'invalid_option_cases': len(bad), 'invalid_id_cases': 6, 'canonical_id_passed': True}
check('strict_ids_options_and_thresholds', validation)

def fingerprint_open_errors():
    uri = sim._fingerprint_readonly_uri(db.FINGERPRINT_DB)
    assert uri.endswith('?mode=ro&immutable=1')
    if str(db.FINGERPRINT_DB.absolute()).startswith('\\\\'):
        assert uri.startswith('file:////')
    connection = MagicMock()
    with patch.object(sim.sqlite3, 'connect', side_effect=[sqlite3.OperationalError('unable to open database file'), connection]) as connect, patch.object(sim.time, 'sleep') as sleep:
        assert sim._get_fp_db() is connection
        assert connect.call_count == 2 and sleep.call_count == 1
    with patch.object(sim.sqlite3, 'connect', side_effect=sqlite3.OperationalError('database disk image is malformed')) as connect, patch.object(sim.time, 'sleep') as sleep:
        try:
            sim._get_fp_db()
        except sqlite3.OperationalError:
            pass
        else:
            raise AssertionError('Permanent database error was suppressed')
        assert connect.call_count == 1 and sleep.call_count == 0
    return 'Canonical readonly URI; transient opens retried, permanent errors raised immediately.'
check('fingerprint_uri_and_bounded_open_retry', fingerprint_open_errors)

def name_resolution():
    with patch.object(sim, 'search_ligands', return_value={'results': [{'ligand_id': 'ligand_10', 'ligand_name': 'alpha derivative'}, {'ligand_id': 'ligand_20', 'ligand_name': 'beta derivative'}]}):
        try:
            sim._resolve_ligand_id(ligand_name='derivative')
        except ValueError as exc:
            assert 'Ambiguous' in str(exc)
        else:
            raise AssertionError('Ambiguity silently selected')
    with patch.object(sim, 'search_ligands', return_value={'results': [{'ligand_id': 'ligand_10', 'ligand_name': 'Methyl citric acid'}, {'ligand_id': 'ligand_20', 'ligand_name': 'Citric acid'}]}) as search:
        assert sim._resolve_ligand_id(ligand_name='citrate') == 20
        assert search.call_args.kwargs['name'] == 'citric acid'
    return 'Ambiguous names rejected; citrate resolves exact citric-acid hit.'
check('ligand_name_resolution', name_resolution)

def fp_fixture():
    conn = CONNECT(':memory:')
    conn.row_factory = sqlite3.Row
    conn.execute('CREATE TABLE ligand_similarity(ligand_id_1,ligand_id_2,tanimoto_maccs,tanimoto_morgan,tversky_morgan_1to2,tversky_morgan_2to1)')
    conn.executemany('INSERT INTO ligand_similarity VALUES (?,?,?,?,?,?)', [(10, 20, 0.2, 0.9, 0.8, 0.4), (10, 30, 0.95, 0.3, 0.2, 0.9), (5, 10, 0.4, 0.5, 0.7, 0.6), (10, 40, 0.8, None, 0.6, None)])
    conn.execute('CREATE TABLE ligand_fingerprint(ligand_id,fp_status)')
    conn.execute("INSERT INTO ligand_fingerprint VALUES(10,'ok')")
    return conn

def metric_ranking():
    with fp_fixture() as conn:
        expected = {'tanimoto_morgan': [20, 5, 30], 'tanimoto_maccs': [30, 40, 5], 'tversky_query_in_target': [20, 5, 40], 'tversky_target_in_query': [30, 5, 20]}
        for metric, ids in expected.items():
            rows = sim._fetch_top_similar(conn, 10, 3, metric, 0)
            assert [r['similar_id'] for r in rows] == ids, (metric, rows)
        assert [r['similar_id'] for r in sim._fetch_top_similar(conn, 10, 3, 'tanimoto_maccs', 0.8)] == [30, 40]
    return 'All four metrics rank correctly; reverse Tversky, NULL scores, inclusive threshold, deterministic tie order verified.'
check('sql_metric_ranking_and_direction', metric_ranking)

@contextmanager
def dummy_connection():
    yield None

def mock_search(metric='tanimoto_morgan', threshold=0.0):
    with patch.object(sim, '_get_fp_db', side_effect=fp_fixture), patch.object(sim, 'get_cards_db', dummy_connection), patch.object(sim, 'get_equilibrium_db', dummy_connection), patch.object(sim, '_fetch_ligand_info', side_effect=lambda _, ids: {i: {'ligand_id': i, 'ligand_name': f'L{i}', 'smiles': 'N', 'HxL_canonical': 'L'} for i in ids}), patch.object(sim, '_fetch_eq_richness', return_value={'n_metals': 0, 'n_beta_defs': 0, 'metals_covered': [], 'top_maps': []}):
        return sim.search_similar_ligands(ligand_id='ligand_10', top_k=4, metric=metric, min_similarity=threshold)

def nohit_null():
    empty = mock_search(threshold=1.0)
    assert empty['similar_ligands'] == [] and 'error' not in empty and ('No other ligands' in empty['message'])
    out = mock_search(metric='tanimoto_maccs')
    row = next((r for r in out['similar_ligands'] if r['ligand_id'] == 'ligand_40'))
    assert row['similarity_score'] is None and row['ranking_score'] == 0.8
    VALUES['mock_similarity'] = out
    return 'Valid zero-hit query stays successful; NULL unselected Morgan score is preserved without rounding error.'
check('valid_nohit_and_null_secondary_scores', nohit_null)

def compactor_scope():
    payload = VALUES['mock_similarity']
    with patch.object(sqlite3, 'connect', side_effect=AssertionError('Compactor must not open database')):
        rendered = sc.compact_search_similar_ligands(payload)
        failed = sc.compact_search_similar_ligands({'query_ligand': {'ligand_id': 'ligand_999'}, 'similar_ligands': [], 'error': 'No usable fingerprint'})
    assert 'MACCS Tanimoto' in rendered and 'returned ligand' in rendered
    assert 'ERROR' in failed and 'No usable fingerprint' in failed
    assert 'ligand_999' in failed
    return 'Compaction makes no DB query; selected metric/returned scope and failures retained.'
check('similarity_compactor_scope_and_errors', compactor_scope)

def missing_fp():

    def connection():
        c = fp_fixture()
        c.execute("UPDATE ligand_fingerprint SET fp_status='invalid_smiles'")
        return c
    with patch.object(sim, '_get_fp_db', side_effect=connection):
        result = sim.search_similar_ligands(ligand_id=10)
    assert result['error_code'] == 'no_fingerprint_data' and result['similar_ligands'] == []
    with patch.object(sim, '_get_fp_db', side_effect=fp_fixture):
        result = sim.search_similar_ligands(ligand_id=99)
    assert result['error_code'] == 'ligand_not_found'
    return 'Missing ligand and invalid fingerprint produce distinct explicit errors.'
check('fingerprint_failure_distinction', missing_fp)

def real_similarity():
    payload = tools.search_similar_ligands(ligand_id='ligand_5760', top_k=3, metric='tanimoto_maccs', min_similarity=0.1, metal_ids=['metal_41'])
    assert len(payload['similar_ligands']) == 3 and payload['metric'] == 'tanimoto_maccs'
    scores = [r['ranking_score'] for r in payload['similar_ligands']]
    assert scores == sorted(scores, reverse=True)
    with db.get_equilibrium_db() as conn:
        expected = conn.execute('SELECT COUNT(DISTINCT nd.beta_definition_id) FROM eq_node nd JOIN eq_network nw ON nw.network_db_id=nd.network_db_id JOIN eq_map m ON m.map_id=nw.map_id JOIN eq_map_collection c ON c.collection_id=m.collection_id WHERE c.ligand_id=? AND c.metal_id=?', (5760, 41)).fetchone()[0]
    assert payload['query_eq_richness']['n_beta_defs'] == expected
    VALUES['real_similarity'] = payload
    return {'ligands': [r['ligand_id'] for r in payload['similar_ligands']], 'scores': scores, 'filtered_beta_count': expected}
check('real_similarity_and_metal_filtered_coverage', real_similarity)

def mcp_contract():
    server = VALUES['server']
    tool = server.mcp._tool_manager.get_tool('search_similar_ligands')
    model = tool.fn_metadata.arg_model
    assert tool.parameters['additionalProperties'] is False
    invalid = [{'top_k': True}, {'top_k': 1.5}, {'top_k': 0}, {'min_similarity': True}, {'min_similarity': float('nan')}, {'metric': 'bad'}, {'min_similarty': 0.5}, {'ligand_id': True}, {'metal_ids': [1.5]}]
    for kwargs in invalid:
        try:
            model.model_validate(kwargs)
        except ValueError:
            pass
        else:
            raise AssertionError(kwargs)
    with patch.object(server.NT, 'search_similar_ligands', return_value={'similar_ligands': []}) as fn:
        server.search_similar_ligands(ligand_id='ligand_5760', metal_ids='metal_41,metal_2', metric='tanimoto_maccs', min_similarity=0.8)
    assert fn.call_args.kwargs['metal_ids'] == ['metal_41', 'metal_2']
    assert fn.call_args.kwargs['metric'] == 'tanimoto_maccs' and fn.call_args.kwargs['min_similarity'] == 0.8
    return {'invalid_schema_cases': len(invalid), 'ranking_and_filter_forwarding': True}
check('mcp_schema_and_argument_forwarding', mcp_contract)

def citations():
    with db.attach_all_dbs() as conn:
        r = conn.execute('SELECT vlm_id,COUNT(*) n FROM litdb.vlm_literature_sic GROUP BY vlm_id HAVING COUNT(*)>5 ORDER BY n DESC LIMIT 1').fetchone()
    identifier = 'vlm_' + str(r['vlm_id'])
    card = tools.inspect_card(identifier)
    lit = tools.inspect_literature(identifier)
    assert card['citations'] == lit['citations'] and card['total_citations'] == lit['total_citations'] > 5
    rendered = ic.compact_inspect_card(card)
    assert all((c['literature_alt_id'] in rendered for c in card['citations']))
    return {'measurement': identifier, 'citations_preserved': card['total_citations']}
check('all_card_citations_retained', citations)

def stability_evidence():
    rows = tools.search_stability(sql_where_query='c.ligand_id=5760 LIMIT 6', ligand_similarity=True)
    assert rows and all(('similarity_score' in r for r in rows))
    rendered = stc.compact_search_stability(rows)
    assert 'Similarity-ranked ligands' in rendered
    groups = stc._group_rows(rows)
    for lines in (stc._render_merged(groups), stc._render_global_stats(groups)):
        text = '\n'.join(lines)
        assert all((r['vlm_id'] in text for r in rows))
    VALUES['stability'] = rows
    return {'rows': len(rows), 'evidence_ids_preserved': [r['vlm_id'] for r in rows]}
check('stability_similarity_and_summary_ids', stability_evidence)

def network_evidence():
    rows = tools.search_networks(sql_where_query='1=1 LIMIT 3')
    assert rows
    for lines in (nc._network_full(rows), nc._network_summary(rows)):
        text = '\n'.join(lines)
        assert any((str(r['vlm_id']) in text for r in rows if r.get('vlm_id')))
    return {'rows': len(rows), 'preserved_vlm_ids': True}
check('network_summary_evidence_ids', network_evidence)

def no_recompression():
    body = '[summary]\n' + 'vlm_123 logK=15.2 ' * 1000
    memory = [{'role': 'user', 'content': 'Find constants'}, {'role': 'assistant', 'content': 'search_stability'}, {'role': 'user', 'content': '<tool_result>\n' + body + '\n</tool_result>'}]
    before = copy.deepcopy(memory)

    def forbidden(*args, **kwargs):
        raise AssertionError('Unexpected learned recompression')
    coro = compactor.compact_memory(memory, forbidden)
    try:
        coro.send(None)
    except StopIteration:
        pass
    else:
        raise AssertionError('Unexpected asynchronous work')
    assert memory == before
    return 'Existing bounded tool summary is byte-preserved without a model call.'
check('already_compacted_evidence_not_recompressed', no_recompression)
print(json.dumps({'passed': sum((r['passed'] for r in RESULTS)), 'total': len(RESULTS), 'network_attempts': len(ATTEMPTS)}, indent=2))
raise SystemExit(0 if all((r['passed'] for r in RESULTS)) else 1)
