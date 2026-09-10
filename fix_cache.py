import json

with open("catalog_cache.json", "r") as f:
    cache = json.load(f)

for c in cache["cases"]:
    if not c["text"].startswith("### "):
        c["text"] = f"### {c['label']}\n{c['text']}"

with open("catalog_cache.json", "w") as f:
    json.dump(cache, f, indent=2)
