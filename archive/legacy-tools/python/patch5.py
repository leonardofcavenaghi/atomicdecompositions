with open("resume_catalog.py", "r") as f:
    code = f.read()

code = code.replace("        return idx, f\"Error: {e}\n{traceback.format_exc()}\"", "        return idx, f\"Error: {e}\\n{traceback.format_exc()}\"")

with open("resume_catalog.py", "w") as f:
    f.write(code)
