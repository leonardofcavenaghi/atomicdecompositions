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


def test_gui_reports_beta_length_and_preserves_empty_insertion_contract():
    job = execute('gw', algebra='A2', keep='1', K='', beta='1', classes='pt', eval_y='', workers='0')
    assert job['state'] == 'error'
    assert 'beta needs exactly 2 entries' in job['error']

    # Empty insertions are valid for degree-zero-point counts (for example,
    # the documented cubic-surface and quintic-line examples).


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
