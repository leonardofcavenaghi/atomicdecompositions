with open("generate_catalog_fast.py", "r") as f:
    code = f.read()

import re

# Fix the unterminated string literal
code = code.replace('new_content = content.replace("</div>\n\n***", card + "\n\n</div>\n\n***")', 'new_content = content.replace("</div>\\n\\n***", card + "\\n\\n</div>\\n\\n***")')

with open("generate_catalog_fast.py", "w") as f:
    f.write(code)
