#!/usr/bin/env python3
"""Keep current development metadata, README, and release notes synchronized."""
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
text = (ROOT/'pyproject.toml').read_text()
version = re.search(r'^version = "([^"]+)"',text,re.M).group(1)
readme = (ROOT/'README.md').read_text()
releases = (ROOT/'docs/releases.md').read_text()
assert f'`{version}`' in readme, 'README does not identify package version'
if '.dev' in version:
    assert f'## Current development version: {version}' in releases
tags = subprocess.check_output(['git','tag','--list','v*','--sort=-version:refname'],
                               cwd=ROOT,text=True).splitlines()
if tags:
    stable=tags[0]
    if '.dev' not in version:
        assert stable == f'v{version}', 'Stable tag and package version differ'
    assert stable in readme and f'## {stable} ' in releases
    assert f'/archive/refs/tags/{stable}.zip' in releases
    for name in ('index.md', 'installation.md', 'releases.md'):
        page = (ROOT / 'docs' / name).read_text()
        downloads = re.findall(r'/archive/refs/tags/(v[^/]+)\.zip', page)
        assert downloads and set(downloads) == {stable}, (name, 'stale stable download', downloads)
    assert f'The stable ZIP matches version `{stable[1:]}`' in releases
print(f'Release metadata validation passed: package {version}, stable {tags[0] if tags else "no tags fetched"}')
