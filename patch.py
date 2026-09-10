import re
with open("resume_catalog.py", "r") as f:
    code = f.read()
code = code.replace("import multiprocessing as mp", "from concurrent.futures import ProcessPoolExecutor, as_completed\nimport multiprocessing as mp")
new_main = """
    with ProcessPoolExecutor(max_workers=mp.cpu_count()) as pool:
        futures = {pool.submit(run_worker, arg): arg for arg in args_list}
        for future in as_completed(futures):
            idx, result = future.result()
            if isinstance(result, dict):
                print(f"[{idx+1}] Success: {result['label']}")
                cache["cases"].append(result)
                with open("catalog_cache.json", "w") as f:
                    json.dump(cache, f, indent=2)
                subprocess.run(["python3", "restructure_catalog.py"], check=True)
                subprocess.run("git add docs/catalog/ catalog_cache.json && git commit -m 'chore: cache computed cases' && git push", shell=True)
            else:
                print(f"[{idx+1}] Failed: {result}")
"""
code = re.sub(r'    with mp.*?:.*?Failed: \{result\}["\']\)', new_main, code, flags=re.DOTALL)
with open("resume_catalog.py", "w") as f:
    f.write(code)
