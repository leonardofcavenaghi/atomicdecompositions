import re

with open('gwflags/gui.py', 'r') as f:
    content = f.read()

def repl_sqm(m):
    return """        elif kind == 'sqm':
            import sympy
            workers = int(params.get('workers') or 0)
            fano, betas = X.fano_index_and_betas(K or None)
            log(f'Fano index {fano}; {len(betas)} curve classes '
                f'(max degree {max(sum(b) for b in betas)})')
            M, Gr, idx = X.small_quantum_multiplication(
                K or None, betas, progress=log, workers=workers)
            
            eval_y = params.get('eval_y', '').strip()
            eval_dict = {}
            if eval_y:
                for pair in eval_y.split(','):
                    if '=' in pair:
                        k, v = pair.split('=')
                        eval_dict[sympy.Symbol(k.strip())] = sympy.sympify(v.strip())
            
            if eval_dict:
                log(f'matrix assembled in {time.time() - t0:.1f}s; evaluating at {eval_y} ...')
                M = [[sympy.sympify(val).subs(eval_dict) if hasattr(val, 'free_symbols') or isinstance(val, str) else val for val in row] for row in M]
            else:
                log(f'matrix assembled in {time.time() - t0:.1f}s; keeping symbolic variables ...')
            
            # Compute Characteristic Polynomial
            log('computing characteristic polynomial ...')
            lam = sympy.Symbol('lambda')
            sympy_M = sympy.Matrix(M)
            char_poly = sympy_M.charpoly(lam).as_expr()
            
            result['fano'] = fano
            result['n_betas'] = len(betas)
            result['basis_indices'] = idx
            result['matrix'] = [[str(v) for v in row] for row in M]
            result['grading'] = [str(Gr[a][a]) for a in range(len(Gr))]
            result['char_poly'] = str(char_poly)
            
            # Only compute eigenvalues if not evaluated custom (to avoid complex root finding hangups)
            try:
                ev = spectrum_at_one(M) if not eval_dict else []
            except Exception as e:
                log(f"could not compute eigenvalues: {e}")
                ev = []
            result['eigenvalues'] = [[z.real, z.imag] for z in ev] if ev else []"""

content = re.sub(r"        elif kind == 'sqm':.*?result\['eigenvalues'\] = \[\[z\.real, z\.imag\] for z in ev\]", repl_sqm, content, flags=re.DOTALL)

with open('gwflags/gui.py', 'w') as f:
    f.write(content)

print("Patched!")
