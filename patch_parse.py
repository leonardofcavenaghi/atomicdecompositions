import re

for filename in ['gwflags/cli.py', 'gwflags/gui.py']:
    with open(filename, 'r') as f:
        content = f.read()
        
    old_parse1 = """def parse_k(spec):
    if not spec:
        return []
    return [[int(v) for v in row.split(',')] for row in spec.split(';')]"""
    
    old_parse2 = """def parse_k(spec):
    spec = spec.strip()
    if not spec:
        return []
    return [[int(v) for v in row.split(',')] for row in spec.split(';')]"""
    
    new_parse = """def parse_k(spec, X=None):
    spec = spec.strip()
    if not spec:
        return []
    if any(c.isalpha() for c in spec):
        from gwflags.bundles import O, taut_sub, taut_quot, dual, osum, tensor, sym, wedge
        try:
            return eval(spec, {"X": X, "O": O, "taut_sub": taut_sub, "taut_quot": taut_quot, "dual": dual, "osum": osum, "tensor": tensor, "sym": sym, "wedge": wedge})
        except Exception as e:
            raise ValueError(f"Invalid bundle expression: {e}")
    return [[int(v) for v in row.split(',')] for row in spec.split(';')]"""
    
    content = content.replace(old_parse1, new_parse)
    content = content.replace(old_parse2, new_parse)
    
    with open(filename, 'w') as f:
        f.write(content)

print("Patched parse_k in cli.py and gui.py!")
