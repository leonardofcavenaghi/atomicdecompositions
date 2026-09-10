import json
import os

def get_dimension_name(dim_str):
    if not dim_str.isdigit():
        return f"Dimension {dim_str}"
    d = int(dim_str)
    if d == 1: return "Curves (1-folds)"
    if d == 2: return "Surfaces (2-folds)"
    if d == 3: return "3-folds"
    if d == 4: return "4-folds"
    return f"{d}-folds"

def write_category_page(title, filename, cases):
    cases.sort(key=lambda x: (int(x['dim']) if x['dim'].isdigit() else 0, int(x['fano']) if x['fano'].isdigit() else 0), reverse=True)
    
    grouped = {}
    for c in cases:
        d = c['dim']
        if d not in grouped:
            grouped[d] = []
        grouped[d].append(c)
        
    with open(f"docs/catalog/{filename}", "w") as f:
        f.write(f"# {title}\n\n")
        f.write("This section contains complete intersections inside this geometric family, systematically organized by dimension and Fano index.\n\n")
        
        for dim, dim_cases in grouped.items():
            dim_title = get_dimension_name(dim)
            f.write(f"## {dim_title}\n\n")
            
            f.write("| Geometry | Fano Index | Basis Rank |\n")
            f.write("|---|---|---|\n")
            for c in dim_cases:
                clean_label = "".join([char for char in c['label'].lower() if char.isalnum() or char == '-'])
                anchor = f"{clean_label}"
                f.write(f"| [{c['label']}](#{anchor}) | {c['fano']} | {c['rank']} |\n")
            f.write("\n---\n\n")
            
            for c in dim_cases:
                clean_label = "".join([char for char in c['label'].lower() if char.isalnum() or char == '-'])
                anchor = f"{clean_label}"
                f.write(f"<span id=\"{anchor}\"></span>\n")
                f.write(c['text'] + "\n\n---\n\n")

def main():
    os.makedirs("docs/catalog", exist_ok=True)
    with open("catalog_cache.json", "r") as f:
        data = json.load(f)
        
    cases = data["cases"]
    fanography_text = data["fanography_text"]
    
    proj_cases = [c for c in cases if c['category'] == 'projective']
    grass_cases = [c for c in cases if c['category'] == 'grassmannians']
    flag_cases = [c for c in cases if c['category'] == 'flag_varieties']
    
    write_category_page("Projective Spaces", "projective.md", proj_cases)
    write_category_page("Grassmannians", "grassmannians.md", grass_cases)
    if flag_cases:
        write_category_page("Flag Varieties", "flag_varieties.md", flag_cases)
    
    with open("docs/catalog/fanography.md", "w") as f:
        f.write("# Fanography 3-Folds\n\n")
        f.write("This section contains the 3-dimensional Fano varieties rigorously mapped and computed from fanography.info.\n\n")
        cleaned_fano = fanography_text.replace("### Fanography ID:", "### Fano 3-fold:")
        f.write(cleaned_fano)
        
if __name__ == "__main__":
    main()
