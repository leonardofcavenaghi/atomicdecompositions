#!/usr/bin/env python3
"""Compile every display-math block in the public catalog with LaTeX.

The website renders these blocks with MathJax, while this check catches source
mistakes (unbalanced delimiters, malformed matrix rows, or missing LaTeX
packages) before a catalog page is published.  It writes only to a temporary
working directory.
"""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "docs" / "catalog"
DISPLAY_RE = re.compile(r"(?ms)^\s*\$\$\s*\n(.*?)^\s*\$\$\s*$")


def blocks() -> list[tuple[Path, str]]:
    found: list[tuple[Path, str]] = []
    for path in sorted(CATALOG.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        found.extend((path, match.group(1).strip()) for match in DISPLAY_RE.finditer(text))
    return found


def main() -> int:
    compiler = shutil.which("pdflatex")
    if compiler is None:
        print("pdflatex is required for catalog TeX validation", file=sys.stderr)
        return 2
    source_blocks = blocks()
    if not source_blocks:
        print("No catalog display-math blocks found", file=sys.stderr)
        return 1

    document = [
        r"\documentclass{article}",
        r"\usepackage{amsmath}",
        r"\usepackage[margin=1in]{geometry}",
        r"\setcounter{MaxMatrixCols}{50}",
        r"\allowdisplaybreaks",
        r"\begin{document}",
    ]
    for path, block in source_blocks:
        document.append("% " + path.relative_to(ROOT).as_posix())
        document.extend((r"\[", block, r"\]"))
    document.append(r"\end{document}")
    tex = "\n".join(document) + "\n"

    with tempfile.TemporaryDirectory(prefix="gwflags-catalog-tex-") as work:
        tex_path = Path(work) / "catalog.tex"
        tex_path.write_text(tex, encoding="utf-8")
        result = subprocess.run(
            [compiler, "-interaction=nonstopmode", "-halt-on-error", tex_path.name],
            cwd=work,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        if result.returncode:
            print(result.stdout[-12000:], file=sys.stderr)
            return result.returncode
    print(f"Catalog TeX validation passed: {len(source_blocks)} display blocks compiled")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
