import re

with open('docs/catalog/grassmannians.md', 'r') as f:
    content = f.read()

# Replace ??? note "..." with <details><summary>...</summary>
content = re.sub(
    r'\?\?\? note "(.*?)"\n\s*\$\$(.*?)\$\$',
    r'<details><summary>\1</summary>\n\n$$\2$$\n\n</details>',
    content,
    flags=re.DOTALL
)

with open('docs/catalog/grassmannians.md', 'w') as f:
    f.write(content)
