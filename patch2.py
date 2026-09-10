with open("resume_catalog.py", "r") as f:
    code = f.read()
code = code.replace("X.dim", "X.dimension()")
code = code.replace("X.index", "X.fano_index()")
with open("resume_catalog.py", "w") as f:
    f.write(code)
