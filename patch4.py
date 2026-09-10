import re
with open("resume_catalog.py", "r") as f:
    code = f.read()

new_except = """
    except Exception as e:
        import traceback
        return idx, f"Error: {e}\n{traceback.format_exc()}"
"""
code = re.sub(r'    except Exception as e:\n        return idx, f"Error: \{e\}"', new_except, code)

with open("resume_catalog.py", "w") as f:
    f.write(code)
