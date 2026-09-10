def hodge_matrix_str(h, dim):
    out = "\\begin{matrix}\n"
    for k in range(2*dim + 1): 
        cols = []
        for i in range(2*dim + 1):
            if (k + i - dim) % 2 == 0:
                p = (k + i - dim) // 2
                q = (k - i + dim) // 2
                if 0 <= p <= dim and 0 <= q <= dim:
                    cols.append(str(h.get((p,q), 0)))
                else:
                    cols.append("")
            else:
                cols.append("")
        out += "        " + " & ".join(cols) + " \\\\\n"
    out += "        \\end{matrix}"
    return out

# test P2, dim=2. h00=1, h11=1, h22=1, rest 0
h = {(0,0): 1, (1,1): 1, (2,2): 1}
print(hodge_matrix_str(h, 2))
