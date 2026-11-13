"""Catalogue repository sources, distributions and mathematical collections."""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'docs/data/repository-catalog.json'
IGNORED = {'.git', '__pycache__', '.pytest_cache', 'site', 'node_modules', 'build', 'dist'}
CATEGORIES = {
    'project_documents': 'Project overview, version notes and legal information',
    'contributor_guidance': 'Contributor instructions and repository maintenance',
    'project_configuration': 'Package, documentation and dependency configuration',
    'catalogue_inputs': 'Maintained Fanography input definitions',
    'flag_package': 'Repository-root flag localization package',
    'versioned_distributions': 'Independently installable versioned source snapshots',
    'primary_results': 'Exact localization input and result collections',
    'analysis_results': 'Geometric, connection and atomic analyses',
    'catalogue_metadata': 'Normalized geometric catalogue and search metadata',
    'repository_metadata': 'Generated repository file and collection catalogue',
    'derived_catalogue_pages': 'Catalogue pages derived from exact result metadata',
    'catalogue_pages': 'Geometric examples, dimension collections and invariant expositions',
    'mathematical_guides': 'Localization formulas and mathematical conventions',
    'software_guides': 'Installation, Python, terminal and interface documentation',
    'compatibility_pages': 'Documentation routes retained for existing links',
    'website_assets': 'Website styles, scripts, images and search-engine metadata',
    'distributed_artifacts': 'Versioned archives, checksums and computation notes',
    'maintained_tools': 'Supported generators, validators and browser regressions',
    'regression_tests': 'Maintained tests, mathematical references and fixtures',
    'workflows': 'Continuous integration and documentation publication',
    'historical_archive': 'Earlier utilities and raw catalogue source snapshots',
}
RESULTS = {
    'localization-results.json': ('examples', 'Exact flag localization results'),
    'toric-fourfolds.json': ('records', 'Exact toric fourfold results'),
    'toric-fivefolds.json': ('records', 'Exact toric fivefold results'),
    'flag-fourfolds.json': ('records', 'Additional homogeneous fourfold results'),
}
ANALYSES = {
    'geometric-presentations.json': 'Geometric identification from fans and divisor classes',
    'connection-exponents.json': 'Regularized exponent multisets at specified points',
    'atomic-invariants.json': 'Hodge data, cyclicity and certified atomic invariants',
}


def generated_path(path):
    parts = Path(path).parts
    return (any(part in IGNORED or part in {'venv', '.venv', 'workspace', 'interactive-combined-workspace'}
                or part.endswith(('_env', '_venv', '.egg-info', '.dist-info'))
                or part.startswith('gw-work') for part in parts)
            or path.endswith(('.pyc', '.pyo', '.log', '.out'))
            or re.search(r'(?:^|/)screenshot\d*\.png$', path) is not None)


def tracked_files():
    try:
        result = subprocess.run(['git', 'rev-parse', '--show-toplevel'], cwd=ROOT,
                                capture_output=True, text=True)
    except FileNotFoundError:
        result = None
    if result is not None and result.returncode == 0 and Path(result.stdout.strip()).resolve() == ROOT:
        files = subprocess.check_output(['git', 'ls-files', '-z'], cwd=ROOT).decode().split('\0')
        paths = {p for p in files if p}
    else:
        paths = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*')
                 if p.is_file() and not generated_path(p.relative_to(ROOT).as_posix())}
    paths.add(OUTPUT.relative_to(ROOT).as_posix())
    return sorted(paths)


def category(path):
    parts = Path(path).parts
    assert not generated_path(path), ('Tracked generated artifact', path)
    assert not any(p.endswith(('_env', '_venv')) or p in {'.venv', 'venv', 'pyvenv.cfg'} for p in parts), ('Tracked local environment', path)
    assert not path.endswith(('.log', '.out', '.pyc', '.pyo')), ('Tracked execution output', path)
    assert not re.search(r'(?:^|/)screenshot\d*\.png$', path), ('Tracked exploratory screenshot', path)
    assert path not in {'tests/os', 'tests/sys', 'extracted_api.txt', 'archive/catalogue/extracted_api.txt'}, ('Unclassified local artifact', path)
    if path in {'README.md', 'LAUNCH.md', 'CHANGELOG.md', 'cli.md', 'LICENSE'}:
        return 'project_documents'
    if path in {'AGENTS.md', 'GEMINI.md', 'INSTRUCTION.md', 'CONTRIBUTING.md'} or path.startswith('docs/development/'):
        return 'contributor_guidance'
    if path in {'.gitignore', 'pyproject.toml', 'mkdocs.yml', 'requirements-docs.txt', 'requirements-test.txt'}:
        return 'project_configuration'
    if path in {'catalog_inputs.py', 'catalog_inputs.json'}:
        return 'catalogue_inputs'
    for prefix, label in [('gwflags/', 'flag_package'), ('software/', 'versioned_distributions'),
                          ('archive/', 'historical_archive'), ('tests/', 'regression_tests'),
                          ('.github/workflows/', 'workflows'), ('scripts/', 'maintained_tools')]:
        if path.startswith(prefix):
            return label
    if path.startswith('docs/data/'):
        name = Path(path).name
        if name in RESULTS:
            return 'primary_results'
        if name in ANALYSES:
            return 'analysis_results'
        if name == 'catalog-records.json':
            return 'catalogue_metadata'
        if name == OUTPUT.name:
            return 'repository_metadata'
        raise AssertionError(('Unregistered mathematical collection', path))
    if path in {'docs/catalog/additional.md', 'docs/catalog/computed.md', 'docs/catalog/index.md'}:
        return 'derived_catalogue_pages'
    if path.startswith('docs/catalog/'):
        return 'catalogue_pages'
    if path in {'docs/methodology.md', 'docs/toric/mathematics.md', 'docs/lie-algebras.md'}:
        return 'mathematical_guides'
    if path.startswith(('docs/archive/', 'docs/audits/')) or path in {'docs/change-log.md', 'docs/discrepancy.md'}:
        return 'compatibility_pages'
    if path.startswith('docs/software/') or path in {'docs/installation.md', 'docs/how-to-use.md', 'docs/api-reference.md'}:
        return 'software_guides'
    if path.startswith('docs/downloads/'):
        return 'distributed_artifacts'
    if path.startswith(('docs/assets/', 'docs/javascripts/', 'docs/stylesheets/')) or path in {'docs/robots.txt', 'docs/googlebd6161581795df59.html'}:
        return 'website_assets'
    if path in {'docs/index.md', 'docs/about.md', 'docs/releases.md'}:
        return 'project_documents'
    raise AssertionError(('Unclassified repository path', path))


def package_metadata(directory):
    text = (ROOT / directory / 'pyproject.toml').read_text()
    version = re.search(r'^version\s*=\s*"([^"]+)"', text, re.M).group(1)
    python = re.search(r'^requires-python\s*=\s*"([^"]+)"', text, re.M).group(1)
    scripts = text.split('[project.scripts]')[1].split('\n[')[0]
    entrypoints = dict(re.findall(r'^([\w-]+)\s*=\s*"([\w.]+:\w+)"', scripts, re.M))
    for entry in entrypoints.values():
        module = entry.split(':')[0].replace('.', '/') + '.py'
        assert (ROOT / directory / module).is_file(), (directory, 'Missing entry point', module)
    return version, python, entrypoints


def distributions():
    manifest = json.loads((ROOT / 'docs/downloads/manifest.json').read_text())
    choices = [
        ('Flag', '.', 'gwflags-1.0.6.dev0.zip', 'docs/software/flags-1.0.6.md', 'development'),
        ('Flag', 'software/flag-1.1.0.dev1', 'gw-flag-1.1.0.dev1.zip', 'docs/software/flags-1.1.0.md', 'development'),
        ('Toric', 'software/toric-1.1.0.dev1', 'gw-toric-1.1.0.dev1.zip', 'docs/software/toric-1.1.0.md', 'development'),
        ('Combined', 'software/combined-1.1.0.dev1', 'gw-combined-1.1.0.dev1.zip', 'docs/software/combined.md', 'development'),
        ('Preserved flag', 'software/flag-1.0.5', 'gwflags-1.0.5-preserved.zip', 'docs/software/flags-legacy.md', 'stable'),
    ]
    out = []
    for name, source, archive, guide, status in choices:
        version, python, entrypoints = package_metadata(source)
        item = next(r for r in manifest if r['file'] == archive)
        assert version == item['version'], (source, 'Version differs from download manifest')
        assert (ROOT / guide).is_file() and (ROOT / 'docs/downloads' / archive).is_file()
        out.append(dict(name=name, version=version, status=status, source=source,
                        archive='docs/downloads/' + archive, guide=guide,
                        requires_python=python, entrypoints=entrypoints))
    assert len(out) == len(manifest)
    return out


def collections():
    data = ROOT / 'docs/data'
    out, primary_ids, toric_ids = [], set(), set()
    for name, (key, label) in RESULTS.items():
        rows = json.loads((data / name).read_text())[key]
        ids = {r['id'] for r in rows}
        assert len(ids) == len(rows) and not primary_ids.intersection(ids), name
        primary_ids.update(ids)
        if name.startswith('toric-'):
            toric_ids.update(ids)
        out.append(dict(path='docs/data/' + name, role=label, records=len(rows), collection_key=key))
    for name, label in {**ANALYSES, 'catalog-records.json': 'Normalized geometric catalogue and search index'}.items():
        rows = json.loads((data / name).read_text())['records']
        ids = {r['id'] for r in rows}
        assert len(ids) == len(rows), name
        assert ids == (toric_ids if name in {'geometric-presentations.json', 'connection-exponents.json'} else primary_ids), (name, 'Cross-reference coverage')
        out.append(dict(path='docs/data/' + name, role=label, records=len(rows), collection_key='records'))
    return out


def documentation_tooling():
    package = json.loads((ROOT / 'scripts/package.json').read_text())
    lock = json.loads((ROOT / 'scripts/package-lock.json').read_text())
    assert package.get('private') is True, 'Documentation tools are not a public npm distribution'
    assert lock['name'] == package['name'] == lock['packages']['']['name']
    assert lock['version'] == package['version'] == lock['packages']['']['version']
    assert package['license'] == lock['packages']['']['license'] == 'MIT'
    assert package['dependencies'] == lock['packages']['']['dependencies']
    for command in package['scripts'].values():
        for file in re.findall(r'\bnode\s+([\w./-]+\.js)', command):
            assert (ROOT / 'scripts' / file).is_file(), ('Missing tooling command', file)
    if 'main' in package:
        assert (ROOT / 'scripts' / package['main']).is_file()
    return dict(manifest='scripts/package.json', lockfile='scripts/package-lock.json',
                name=package['name'], private=package['private'], commands=package['scripts'])


def build():
    grouped = {key: [] for key in CATEGORIES}
    for path in tracked_files():
        assert path == OUTPUT.relative_to(ROOT).as_posix() or (ROOT / path).is_file(), ('Tracked file missing', path)
        grouped[category(path)].append(path)
    return dict(schema_version=1, categories=[dict(key=key, description=label, files=grouped[key]) for key, label in CATEGORIES.items()],
                distributions=distributions(), datasets=collections(), documentation_tooling=documentation_tooling())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    result = build()
    rendered = json.dumps(result, ensure_ascii=False, indent=2) + '\n'
    if args.check:
        assert OUTPUT.read_text() == rendered, 'Repository catalogue is stale; regenerate after staging changed paths'
    else:
        OUTPUT.write_text(rendered)
    counts = Counter({r['key']: len(r['files']) for r in result['categories']})
    print(json.dumps(dict(files=sum(counts.values()), categories=len(counts), distributions=len(result['distributions']), datasets=len(result['datasets']), passed=True)))


if __name__ == '__main__':
    main()
