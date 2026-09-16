"""Regression checks for the local web GUI's documented input contract."""
import json
import threading
import time
from http.client import HTTPConnection
from http.server import ThreadingHTTPServer

import pytest

from gwflags import FlagVariety
from gwflags.gui import Handler, JOBS, JOBS_LOCK, parse_classes, parse_k, run_job


def execute(action, **params):
    job = {'state': 'running', 'log': [], 'result': None}
    run_job(job, action, params)
    return job


def test_gui_accepts_quotient_bundle_and_reports_input():
    job = execute('info', algebra='A4', keep='2', K='taut_quot(X, 2)',
                  beta='', classes='', eval_y='', workers='0')
    assert job['state'] == 'done', job.get('error')
    assert job['result']['input']['K'] == 'taut_quot(X, 2)'
    assert job['result']['dim'] == 3


@pytest.mark.parametrize('params, fragment', [
    ({'algebra': 'A3', 'keep': '1,', 'K': ''}, 'comma-separated integers'),
    ({'algebra': 'A3', 'keep': '9', 'K': ''}, 'within 1..3'),
])
def test_gui_describes_invalid_variety_inputs(params, fragment):
    job = execute('info', beta='', classes='', eval_y='', workers='0', **params)
    assert job['state'] == 'error'
    assert fragment in job['error']


def test_gui_accepts_kept_beta_and_rejects_malformed_ambient_beta():
    # A kept-root beta has one entry for each kept root.  The API
    # reports the canonical ambient vector after embedding it at that node.
    job = execute('gw', algebra='A2', keep='1', K='', beta='1',
                  classes='pt|pt', eval_y='', workers='0')
    assert job['state'] == 'done', job.get('error')
    assert job['result']['value'] == '1'
    assert job['result']['beta_input'] == [1]
    assert job['result']['beta'] == [1, 0]

    # A vector of the wrong length is rejected with the two accepted shapes.
    job = execute('gw', algebra='A2', keep='1', K='', beta='1,0,0',
                  classes='pt|pt', eval_y='', workers='0')
    assert job['state'] == 'error'
    assert 'either 1 entries' in job['error']


def test_cli_info_reports_zero_locus_dimension_for_bundle(capsys):
    from gwflags.cli import main as cli_main
    cli_main(['A4', '--keep', '2', '-K', 'quot(osum(S(2),Q(2)),S(2))', 'info'])
    output = capsys.readouterr().out
    assert 'dimension 3 (ambient dimension 6)' in output


def test_gui_accepts_compact_bundle_aliases_and_nested_operations():
    X = FlagVariety('A4', [2])  # Gr(2,5), so S(2), Q(2), and O(1) are valid.
    from gwflags.cli import parse_k as cli_parse_k
    for spec, rank in [('O(1)', 1), ('S(2)', 2), ('Q(2)', 3),
                       ('quot(osum(S(2),Q(2)),S(2))', 3),
                       ('Quot(osum(S(2),Q(2)),S(2))', 3)]:
        for parser in (parse_k, cli_parse_k):
            K = parser(spec, X)
            assert K.X is X
            assert K.rank == rank

    # Nested constructors remain available for ordinary bundle combinations.
    K_nested = parse_k('osum(wedge(2,Q(2)),dual(wedge(2,S(2))),O(1))', X)
    assert K_nested.X is X and K_nested.rank == 5
    with pytest.raises(ValueError, match='subbundle'):
        parse_k('quot(Q(2),S(2))', X)


def test_gui_and_cli_require_reduced_minimal_words():
    X = FlagVariety('A3', [2])
    with pytest.raises(ValueError, match='reduced and minimal'):
        parse_classes('1 2 3', X)
    with pytest.raises(ValueError, match='reduced and minimal'):
        parse_classes('1 1', X)

    from gwflags.cli import parse_classes as cli_parse_classes
    with pytest.raises(ValueError, match='reduced and minimal'):
        cli_parse_classes('1 2 3', X)
    with pytest.raises(ValueError, match='reduced and minimal'):
        cli_parse_classes('1 1', X)

    # A valid reduced representative remains accepted by both parsers.
    assert parse_classes('2 1 3 2|1 3 2|pt', X)[0]
    assert len(cli_parse_classes('2 1 3 2|1 3 2|pt', X)) == 3


def test_all_gui_presets_have_parseable_inputs():
    from gwflags.gui import PRESETS
    for label, algebra, keep, K, action, beta, classes, eval_y, expected in PRESETS:
        X = FlagVariety(algebra, [int(v) for v in keep.split(',')])
        parsed = parse_k(K, X)
        if classes:
            parse_classes(classes, X)
        if parsed and hasattr(parsed, 'X'):
            assert parsed.X is X


def test_gui_bundle_expression_rejects_attribute_access():
    X = FlagVariety('A3', [1])
    with pytest.raises(ValueError, match='attribute access'):
        parse_k('X.__class__', X)
    with pytest.raises(ValueError, match='attribute access'):
        parse_k('X.rs', X)
    from gwflags.cli import parse_k as cli_parse_k
    with pytest.raises(ValueError, match='attribute access'):
        cli_parse_k('X.__class__', X)


def test_gui_rejects_bad_reduced_word_and_nonconvex_bundle():
    X = FlagVariety('A3', [1])
    with pytest.raises(ValueError, match='valid reduced word'):
        parse_classes('not-a-word', X)

    job = execute('info', algebra='A3', keep='1', K='taut_sub(X, 1)',
                  beta='', classes='', eval_y='', workers='0')
    assert job['state'] == 'error'
    assert 'convexity' in job['error'] or 'globally generated' in job['error']


def test_gui_reports_malformed_novikov_assignment():
    job = execute('sqm', algebra='A2', keep='1', K='', beta='', classes='',
                  eval_y='y1=', workers='0')
    assert job['state'] == 'error'
    assert 'missing a value' in job['error']


def request(server, method, path, body=None):
    conn = HTTPConnection(*server.server_address)
    payload = None if body is None else json.dumps(body)
    conn.request(method, path, payload, {'Content-Type': 'application/json'} if payload else {})
    response = conn.getresponse()
    data = json.loads(response.read())
    conn.close()
    return response.status, data


def test_http_api_presets_and_info_job():
    server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        status, presets = request(server, 'GET', '/api/presets')
        assert status == 200
        assert any(p['K'] == 'taut_quot(X, 2)' for p in presets)

        status, started = request(server, 'POST', '/api/run', {
            'action': 'info', 'algebra': 'A2', 'keep': '1', 'K': '',
            'beta': '', 'classes': '', 'eval_y': '', 'workers': '0'})
        assert status == 200 and started['id']
        for _ in range(100):
            status, state = request(server, 'GET', '/api/status?id=' + started['id'])
            if state['state'] != 'running':
                break
            time.sleep(0.02)
        assert state['state'] == 'done', state
        assert state['result']['dim'] == 2
    finally:
        server.shutdown()
        server.server_close()
