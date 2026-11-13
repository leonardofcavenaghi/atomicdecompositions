import glob
import re
import json

for filename in glob.glob("docs/catalog/*.md"):
    with open(filename, "r") as f:
        text = f.read()

    text = text.replace(
        '    <details><summary>Quantum Matrix ($y=1$)</summary>',
        '    ??? note "Quantum Matrix ($y=1$)"'
    )
    text = text.replace(
        '    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>',
        '    ??? note "Hodge Diamond ($h^{p,q}$)"'
    )
    text = text.replace(
        '    <details><summary>Hodge Diamond</summary>',
        '    ??? note "Hodge Diamond"'
    )
    
    # We also need to remove the </details> tags
    text = text.replace('    </details>\n', '')
                
    with open(filename, "w") as f:
        f.write(text)

with open("catalog_cache.json", "r") as f:
    cache = json.load(f)

for case in cache["cases"]:
    text = case["text"]
    text = text.replace(
        '    <details><summary>Quantum Matrix ($y=1$)</summary>',
        '    ??? note "Quantum Matrix ($y=1$)"'
    )
    text = text.replace(
        '    <details><summary>Hodge Diamond ($h^{p,q}$)</summary>',
        '    ??? note "Hodge Diamond ($h^{p,q}$)"'
    )
    text = text.replace(
        '    <details><summary>Hodge Diamond</summary>',
        '    ??? note "Hodge Diamond"'
    )
    text = text.replace('    </details>\n', '')
    case["text"] = text

with open("catalog_cache.json", "w") as f:
    json.dump(cache, f, indent=2)

print("Fixed details!")
