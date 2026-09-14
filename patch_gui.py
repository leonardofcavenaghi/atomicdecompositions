import re

with open('gwflags/gui.py', 'r') as f:
    content = f.read()

# Replace the part in run_job where SQM is handled
old_sqm = """        elif kind == 'sqm':
            fano, betas = X.fano_index_and_betas(K or None)
            log(f'fano index {fano}, {len(betas)} curve classes')
            M, Gr, idx = X.small_quantum_multiplication(
                K or None, betas, progress=log, workers=workers)
            log(f'matrix assembled in {time.time() - t0:.1f}s; '
                'extracting spectrum at y=1 ...')
            ev = spectrum_at_one(M)
            result['fano'] = fano
            result['n_betas'] = len(betas)
            result['basis_indices'] = idx
            result['matrix'] = [[str(v) for v in row] for row in M]
            result['grading'] = [str(Gr[a][a]) for a in range(len(Gr))]
            result['eigenvalues'] = [[z.real, z.imag] for z in ev]"""

new_sqm = """        elif kind == 'sqm':
            import sympy
            fano, betas = X.fano_index_and_betas(K or None)
            log(f'fano index {fano}, {len(betas)} curve classes')
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
            
            # Optionally attempt to compute numerical eigenvalues if requested, else skip
            try:
                ev = spectrum_at_one(M) if not eval_dict else [] # Skip if evaluated
            except:
                ev = []
            result['eigenvalues'] = [[z.real, z.imag] for z in ev] if ev else []"""

content = content.replace(old_sqm, new_sqm)

# Update rendering logic
old_render = """    h+='<h2>Grading</h2><div>diag('+res.grading.join(', ')+')</div>';
    h+='<h2>Eigenvalues at y = 1</h2><table><tr>';
    res.eigenvalues.forEach(([re,im],i)=>{
      const fmt=x=>{ let t=x.toFixed(4).replace(/\.?0+$/,'');
        return (t===''||t==='-0')?'0':t; };
      const s=fmt(re)+(Math.abs(im)>1e-6?((im>0?' + ':' − ')+
        fmt(Math.abs(im))+'i'):'');
      h+='<td class="'+(i===0?'dom':'')+'">'+s+'</td>'; });
    h+='</tr></table><div style="color:var(--dim);font-size:12px">'+
       'first entry = spectral radius (Conjecture O: real &amp; simple).'+
       '</div>';"""

new_render = """    h+='<h2>Grading</h2><div>diag('+res.grading.join(', ')+')</div>';
    if (res.char_poly) {
        h+='<h2>Characteristic Polynomial</h2><div style="padding: 10px; background: var(--panel); border: 1px solid var(--edge); font:13px ui-monospace,Menlo,monospace;">'+pretty(res.char_poly)+'</div>';
    }
    if (res.eigenvalues && res.eigenvalues.length > 0) {
        h+='<h2>Eigenvalues</h2><table><tr>';
        res.eigenvalues.forEach(([re,im],i)=>{
          const fmt=x=>{ let t=x.toFixed(4).replace(/\.?0+$/,'');
            return (t===''||t==='-0')?'0':t; };
          const s=fmt(re)+(Math.abs(im)>1e-6?((im>0?' + ':' − ')+
            fmt(Math.abs(im))+'i'):'');
          h+='<td class="'+(i===0?'dom':'')+'">'+s+'</td>'; });
        h+='</tr></table><div style="color:var(--dim);font-size:12px">'+
           'first entry = spectral radius (Conjecture O: real &amp; simple).'+
           '</div>';
    }"""
    
content = content.replace(old_render, new_render)

with open('gwflags/gui.py', 'w') as f:
    f.write(content)

print("Patched!")
