import json

with open("catalog_cache.json", "r") as f:
    cache = json.load(f)

for c in cache["cases"]:
    if c['label'].startswith("P"):
        c['category'] = 'projective'
    elif c['label'].startswith("Gr"):
        c['category'] = 'grassmannians'
    else:
        c['category'] = 'flag_varieties'

with open("catalog_cache.json", "w") as f:
    json.dump(cache, f, indent=2)
