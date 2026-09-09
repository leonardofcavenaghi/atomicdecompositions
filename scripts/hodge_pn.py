import sympy

def hodge_numbers_pn(n, degrees):
    x, y = sympy.symbols('x y')
    k = len(degrees)
    dimX = n - k
    
    prod = sympy.S(1)
    for d in degrees:
        num = (1+x)**d - (1+y)**d
        den = -(1+x)**d * y + (1+y)**d * x
        
        # We need to divide out (x-y) from both numerator and denominator to avoid singularity
        # num = ((1+x)-(1+y)) * P = (x-y)*P
        # den = -(1+x)^d y + (1+y)^d x 
        # For d=1: - (1+x)y + (1+y)x = -y - xy + x + xy = x-y.
        # So den is divisible by (x-y). We can just use sympy.cancel!
        factor = sympy.cancel(num / den)
        prod = prod * factor
        
    gen_func = sympy.cancel((prod - 1) / ((1+x)*(1+y)))
    
    t = sympy.symbols('t')
    gf_t = gen_func.subs({x: t*x, y: t*y})
    
    series_exp = sympy.series(gf_t, t, 0, dimX + 1).removeO()
    term_dimX = series_exp.coeff(t, dimX)
    
    # Expand and simplify the term to make it a polynomial
    poly_expr = sympy.expand(term_dimX)
    poly = sympy.Poly(poly_expr, x, y)
    
    hodge = {}
    for p in range(dimX + 1):
        for q in range(dimX + 1):
            if p + q == dimX:
                coeff = poly.coeff_monomial(x**p * y**q)
                h_prim = int(coeff * ((-1)**q))
                base_h = 1 if p == q else 0
                hodge[(p,q)] = base_h + h_prim
            else:
                base_h = 1 if p == q else 0
                hodge[(p,q)] = base_h
                
    return hodge, dimX

def print_diamond(h, dim):
    for p in range(dim+1):
        row = []
        for q in range(dim+1):
            row.append(str(h.get((p,q), 0)))
        print("  " + "  ".join(row))

print("Control Test: P^4 / O(2) (Quadric 3-fold)")
h, dim = hodge_numbers_pn(4, [2])
print_diamond(h, dim)

print("\nControl Test: P^4 / O(3) (Cubic 3-fold)")
h, dim = hodge_numbers_pn(4, [3])
print_diamond(h, dim)

print("\nControl Test: P^5 / O(3) (Cubic 4-fold)")
h, dim = hodge_numbers_pn(5, [3])
print_diamond(h, dim)
