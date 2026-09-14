import json

with open("catalog_cache.json", "r") as f:
    cache = json.load(f)

for case in cache["cases"]:
    text = case["text"]
    # Change ### {label} to ??? example "{label}"
    label = case["label"]
    if f"### {label}" in text:
        text = text.replace(f"### {label}\n", f'??? example "{label}"\n')
        # Indent every line after the first by 4 spaces
        lines = text.split("\n")
        new_lines = [lines[0]]
        for line in lines[1:]:
            new_lines.append("    " + line if line else "")
        # But wait! We already indented the matrix by 4 spaces (so it had 4 spaces).
        # When we add 4 spaces, it will have 8 spaces! That's correct for a nested note!
        case["text"] = "\n".join(new_lines)

with open("catalog_cache.json", "w") as f:
    json.dump(cache, f, indent=2)

