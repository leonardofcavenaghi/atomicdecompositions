"""Keep software regressions for software changes; validate docs on every push."""
from __future__ import annotations
import json, os, subprocess, sys
from urllib.request import Request, urlopen
from pathlib import Path

DOC_CHECKS = {
    'scripts/repository_catalog.py', 'scripts/validate_catalog.py', 'scripts/validate_catalog_tex.py',
    'scripts/validate_catalog_math.py', 'scripts/validate_delivery.py',
    'scripts/validate_flag_fourfolds.py', 'scripts/validate_atomic_invariants.py',
    'scripts/generate_catalog_index.py', 'scripts/catalog_results.py', 'scripts/search_keywords.py', 'scripts/render_static_math.js',
    '.github/workflows/deploy.yml',
    'scripts/validate_geometric_presentations.py', 'scripts/validate_exponent_multisets.py',
    'scripts/validate_localization_results.py', 'scripts/validate_toric_results.py',
    'scripts/validate_release_metadata.py', 'scripts/validate_search_metadata.py',
    'scripts/test_catalog_navigation.js', 'scripts/test_gui_controls.js',
    'scripts/classify_ci_changes.py', '.github/workflows/test.yml',
}

def requires_software_tests(paths: list[str]) -> bool:
    if not paths:
        return True
    def documentation(path: str) -> bool:
        return ((path.startswith('docs/') and not path.startswith('docs/downloads/'))
                or ('/' not in path and path.endswith('.md'))
                or path == 'mkdocs.yml' or path in DOC_CHECKS)
    return not all(documentation(path) for path in paths)

def self_test() -> None:
    for paths, expected in [
        (['docs/methodology.md', 'docs/javascripts/mathjax-loader.js'], False),
        (['docs/data/catalog-records.json', 'scripts/validate_toric_results.py'], False),
        (['README.md', 'mkdocs.yml'], False),
        (['docs/downloads/gw-combined-1.1.0.dev1.zip'], True),
        (['gwflags/quantum.py', 'docs/index.md'], True),
        (['software/combined-1.1.0.dev1/gwapp/worker.py'], True),
        (['requirements-docs.txt'], True), (['pyproject.toml'], True),
        (['.github/workflows/test.yml'], False), (['tests/test_quantum.py'], True),
        (['.github/workflows/test.yml', 'gwflags/quantum.py'], True),
        (['unknown-new-file'], True), ([], True),
    ]:
        assert requires_software_tests(paths) is expected, paths
    print('Change classification checks passed')

if __name__ == '__main__':
    self_test()
    if '--self-test' in sys.argv:
        raise SystemExit(0)
    try:
        event = json.loads(Path(os.environ['GITHUB_EVENT_PATH']).read_text())
        if os.environ.get('GITHUB_EVENT_NAME') != 'push':
            raise ValueError('Non-push event; run the complete suite')
        # Compare against a successful ancestor, not the preceding push: a docs
        # follow-up must never bypass a previous software change that failed CI.
        repo = os.environ['GITHUB_REPOSITORY']
        request = Request(
            f'https://api.github.com/repos/{repo}/actions/workflows/test.yml/runs'
            '?branch=main&status=success&event=push&per_page=30',
            headers={'Authorization': 'Bearer ' + os.environ['GITHUB_TOKEN'],
                     'Accept': 'application/vnd.github+json'})
        with urlopen(request, timeout=20) as response:
            runs = json.load(response)['workflow_runs']
        base = None
        for run in runs:
            sha = run['head_sha']
            if subprocess.run(['git', 'merge-base', '--is-ancestor', sha, 'HEAD'],
                              stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0:
                base = sha
                break
        if base is None:
            raise ValueError('No successful ancestor found; run the complete suite')
        changed = subprocess.check_output(
            ['git', 'diff', '--name-only', '--no-renames', '-z', base, 'HEAD'])
        paths = [p.decode('utf-8') for p in changed.split(b'\0') if p]
        full = requires_software_tests(paths)
    except (KeyError, ValueError, UnicodeError, OSError, subprocess.CalledProcessError) as exc:
        print(f'Using the complete suite: {exc}')
        full = True
    print(f'Software regression suite required: {full}')
    with open(os.environ['GITHUB_OUTPUT'], 'a') as out:
        out.write(f'full={str(full).lower()}\n')
