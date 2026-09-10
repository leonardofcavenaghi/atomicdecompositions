import json
from restructure_catalog import parse_catalog

cases, fanography_text = parse_catalog()

with open("catalog_cache.json", "w") as f:
    json.dump({"cases": cases, "fanography_text": fanography_text}, f, indent=2)
print(f"Seeded {len(cases)} cases into cache.")
