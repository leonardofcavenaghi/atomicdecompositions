import re

with open('docs/how-to-use.md', 'r') as f:
    content = f.read()

# Replace Mode with Card references
replacements = [
    (r'- \*\*Mode:\*\* Single GW Invariant\n- \*\*Algebra:\*\*', r'- **Card 1 (Space Definition)** -> **Algebra:**'),
    (r'- \*\*Mode:\*\* Quantum Multiplication\n- \*\*Algebra:\*\*', r'- **Card 1 (Space Definition)** -> **Algebra:**'),
    (r'- \*\*Keep Nodes:\*\*', r'- **Card 1** -> **Keep Simple Roots:**'),
    (r'- \*\*Twisting Bundle K:\*\*', r'- **Card 1** -> **Twisting Bundle K:**'),
    (r'- \*\*Curve Class \(Beta\):\*\*', r'- **Card 3 (GW Invariants)** -> **Curve Class &beta;:**'),
    (r'- \*\*Insertions:\*\*', r'- **Card 3** -> **Insertions:**'),
    (r'- \*\*Click:\*\* Compute GW Invariant', r'- **Card 3** -> **Click:** Compute Invariant'),
    (r'- \*\*Click:\*\* Compute SQM', r'- **Card 2 (Execution Options)** -> **Click:** Compute c₁(TX)⋆ Matrix')
]

for old, new in replacements:
    content = re.sub(old, new, content)

with open('docs/how-to-use.md', 'w') as f:
    f.write(content)
