import json

with open("catalog_cache.json", "r") as f:
    cache = json.load(f)

table_rows = []
seen = set()
for case in cache["cases"]:
    text = case["text"]
    label = case["label"]
    category = case["category"]
    
    # Extract Dimension, Fano Index, Basis Rank
    dim = ""
    fano = ""
    rank = ""
    ambient = ""
    
    for line in text.split('\n'):
        if "**Dimension:**" in line:
            dim = line.split("**Dimension:**")[-1].strip().replace('$', '')
        elif "**Fano Index:**" in line:
            fano = line.split("**Fano Index:**")[-1].strip().replace('$', '')
        elif "**Basis Rank:**" in line:
            rank = line.split("**Basis Rank:**")[-1].strip().replace('$', '')
        elif "**Ambient Space:**" in line:
            ambient = line.split("**Ambient Space:**")[-1].strip().replace('$', '').replace('`', '')
            
    anchor = "".join([char for char in label.lower() if char.isalnum() or char == '-'])
    link = f"{category}.md#{anchor}"
    if (category, anchor) in seen:
        continue
    seen.add((category, anchor))
        
    table_rows.append(f"| [{label}]({link}) | {ambient} | {dim} | {fano} | {rank} |")

md = """# Catalog Master Search

Welcome to the **Master Search Database**. Use the search bar in the top right of this table to instantly filter through all computed geometric spaces, or sort by dimension, Fano index, and rank. You can type freely (e.g., "Gr", "Fano Index 2", "15") to find exactly what you are looking for.

<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.13.6/css/jquery.dataTables.css">
<script type="text/javascript" charset="utf8" src="https://code.jquery.com/jquery-3.7.0.min.js"></script>
<script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.13.6/js/jquery.dataTables.js"></script>
<script>
$(document).ready( function () {
    $('table').DataTable({
        "pageLength": 25,
        "order": [[ 2, "desc" ]]
    });
} );
</script>

| Geometry | Ambient Space | Dimension | Fano Index | Basis Rank |
|---|---|---|---|---|
"""
md += "\n".join(table_rows)

with open("docs/catalog/index.md", "w") as f:
    f.write(md)

print("Generated DataTables master index!")
