with open("generate_catalog_fast.py", "r") as f:
    code = f.read()

code = code.replace(
    '        $$\n"""\n        if label in SCRAPED_HODGE:',
    '        $$\n\n    </details>\n"""\n        if label in SCRAPED_HODGE:'
)

with open("generate_catalog_fast.py", "w") as f:
    f.write(code)
