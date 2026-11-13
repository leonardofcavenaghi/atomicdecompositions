with open("resume_catalog.py", "r") as f:
    code = f.read()
code = code.replace("X.dimension()()", "X.dimension()")
code = code.replace("X.fano_index()", "X.fano_index_and_betas()[0]")
with open("resume_catalog.py", "w") as f:
    f.write(code)
