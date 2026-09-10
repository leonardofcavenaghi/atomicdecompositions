import os
import glob

def replace_in_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Simple replacements
    content = content.replace("Atomic Decomposition of Complete Intersections", "Quantum Cohomology of Complete Intersections")
    content = content.replace("atomic decomposition", "quantum cohomology")
    content = content.replace("Atomic decomposition", "Quantum cohomology")
    content = content.replace("Hodge Atoms", "Quantum Structures")
    content = content.replace("Hodge atoms", "quantum structures")
    content = content.replace("Hodge atom", "quantum structure")
    content = content.replace("Theory of Atoms", "Quantum Geometry")
    content = content.replace("theory of atoms", "quantum geometry")
    
    with open(filepath, 'w') as f:
        f.write(content)

for root, _, files in os.walk("docs"):
    for file in files:
        if file.endswith(".md"):
            replace_in_file(os.path.join(root, file))
            
replace_in_file("mkdocs.yml")
