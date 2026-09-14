import markdown
md = markdown.Markdown(extensions=['pymdownx.arithmatex', 'pymdownx.superfences', 'pymdownx.details'])
text = """
??? example "Ex"
    ??? note "Note"
        $$
            \\left[\\begin{array}{c}0\\\\0\\end{array}\\right]
        $$
"""
print(md.convert(text))
