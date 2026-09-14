import glob

for filepath in glob.glob("docs/catalog/*.md"):
    with open(filepath, "r") as f:
        lines = f.readlines()
        
    new_lines = []
    in_math_block = False
    
    for line in lines:
        if line.strip() == "$$":
            in_math_block = not in_math_block
            new_lines.append(line)
            continue
            
        if in_math_block:
            # The math block should be exactly at 8 spaces.
            # If a line starts with 12 spaces, strip 4 spaces so it has 8 spaces.
            if line.startswith("            "):
                new_lines.append(line[4:])
            # If it starts with 16 spaces, strip 8 spaces? No, just strip down to 8 spaces max.
            # Actually, to be perfectly uniform, all math content should be indented by 8 spaces.
            elif line.startswith("        "):
                new_lines.append(line)
            else:
                # If it's something else, strip it and add 8 spaces
                new_lines.append("        " + line.lstrip())
        else:
            new_lines.append(line)
            
    with open(filepath, "w") as f:
        f.writelines(new_lines)

print("Fixed indentation in all catalog markdown files.")
