import re

with open('docs/catalog.md', 'r') as f:
    content = f.read()

# We need to wipe all the old "-   __Case" entries from catalog.md
# They are all between `<div class="grid cards" markdown>` and `</div>`
# Wait, no, they are just appended. We will just wipe everything from the first '-   __Case' onwards up to `</div>`

idx = content.find('-   __Case #')
if idx != -1:
    end_idx = content.rfind('</div>')
    if end_idx != -1:
        new_content = content[:idx] + content[end_idx:]
        with open('docs/catalog.md', 'w') as f:
            f.write(new_content)
        print("Wiped old cards.")
