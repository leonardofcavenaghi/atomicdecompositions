with open("generate_catalog_fast.py", "r") as f:
    content = f.read()

# Replace ??? note "Quantum Matrix ($y=1$)"
content = content.replace(
    'md += f"    ??? note \\"Quantum Matrix ($y=1$)\\"\\n"',
    'md += f"    <details><summary>Quantum Matrix ($y=1$)</summary>\\n\\n"'
)
# And the closing of Quantum Matrix? Wait, it was just indented.
# We need to add the closing </details> after the matrix.
