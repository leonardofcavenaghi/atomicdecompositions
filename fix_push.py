with open("generate_catalog_fast.py", "r") as f:
    code = f.read()

code = code.replace('subprocess.run(["git", "commit", "-m", "Auto-update catalog with new case"])', '')
code = code.replace('subprocess.run(["git", "push", "origin", "main"])', '')

with open("generate_catalog_fast.py", "w") as f:
    f.write(code)
