import json
import os

with open("catalog_cache.json", "r") as f:
    cache = json.load(f)

markdown_by_category = {}

for case in cache["cases"]:
    cat = case["category"]
    if cat not in markdown_by_category:
        markdown_by_category[cat] = []
    markdown_by_category[cat].append((int(case.get("dim", 0)), case["text"]))

# Sort by dimension
for cat in markdown_by_category:
    markdown_by_category[cat].sort(key=lambda x: x[0], reverse=True)

for cat, cards in markdown_by_category.items():
    filename = f"docs/catalog/{cat}.md"
    with open(filename, "r") as f:
        content = f.read()
    
    # Strip everything after ---
    header = content.split('---')[0] + "---\n\n"
    
    with open(filename, "w") as f:
        f.write(header)
        for _, text in cards:
            f.write(text + "\n\n")
