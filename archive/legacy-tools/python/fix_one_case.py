import json
import subprocess

from generated_fano_cases import CASES_100
from resume_catalog import process_case

print("Processing just ONE flag variety...")
args = (1000, "(a)  Fl(1,2,3)", "A2", [1,2], [], None)
idx, result = process_case(args)

if isinstance(result, dict):
    print("Success, adding to cache!")
    with open("catalog_cache.json", "r") as f:
        cache = json.load(f)
    cache["cases"].append(result)
    with open("catalog_cache.json", "w") as f:
        json.dump(cache, f, indent=2)
    
    import os
    os.system("python3 fix_categories.py")
    os.system("python3 restructure_catalog.py")
    os.system("./new_mkdocs_env/bin/mkdocs gh-deploy --force")
else:
    print("Failed to compute:", result)
