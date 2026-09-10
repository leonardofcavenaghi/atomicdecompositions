with open("restructure_catalog.py", "r") as f:
    code = f.read()

code = code.replace("grass_cases = [c for c in cases if c['category'] == 'grassmannians']", "grass_cases = [c for c in cases if c['category'] == 'grassmannians']\n    flag_cases = [c for c in cases if c['category'] == 'flag_varieties']")
code = code.replace("write_category_page(\"Grassmannians\", \"grassmannians.md\", grass_cases)", "write_category_page(\"Grassmannians\", \"grassmannians.md\", grass_cases)\n    if flag_cases:\n        write_category_page(\"Flag Varieties\", \"flag_varieties.md\", flag_cases)")

with open("restructure_catalog.py", "w") as f:
    f.write(code)
