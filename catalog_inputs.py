"""Single source of truth for executable Fanography catalog inputs.

The JSON file next to this module is intentionally readable and is consumed by
the catalog injector, verifier, matrix helper, and Markdown validator.
"""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

_DATA_PATH = Path(__file__).with_name("catalog_inputs.json")


@lru_cache(maxsize=1)
def _load_data() -> dict:
    with _DATA_PATH.open(encoding="utf-8") as stream:
        data = json.load(stream)
    if data.get("schema_version") != 1:
        raise ValueError(f"unsupported catalog input schema: {data.get('schema_version')!r}")
    if not isinstance(data.get("fanography"), dict):
        raise ValueError("catalog input data must contain a fanography mapping")
    return data


def fanography_specs() -> dict:
    """Return the checked-in Fanography input records in display order."""
    return _load_data()["fanography"]


def legacy_tuple(spec: dict) -> tuple[str, list[int], list[list[int]]]:
    """Convert a line-bundle record to the tuple used by legacy helpers."""
    if "bundle_rows" not in spec:
        raise ValueError("homogeneous-bundle records do not have legacy K rows")
    rows = [[int(value) for value in row] for row in spec["bundle_rows"]]
    return str(spec["algebra"]), [int(node) for node in spec["keep"]], rows


def compact_bundle(spec: dict) -> str:
    """Return the GUI/validator Bundle-K spelling for a catalog record."""
    if "bundle_expression" in spec:
        return str(spec["bundle_expression"])
    return ";".join(",".join(str(value) for value in row) for row in spec.get("bundle_rows", []))


def selected_legacy_specs(flag: str) -> dict[str, tuple[str, list[int], list[list[int]]]]:
    """Return line-bundle records selected by a helper-specific boolean flag."""
    return {
        identifier: legacy_tuple(spec)
        for identifier, spec in fanography_specs().items()
        if spec.get(flag, False) and "bundle_rows" in spec
    }
