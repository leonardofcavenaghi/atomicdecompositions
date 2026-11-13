"""Isolated flag jobs. Inputs and progress survive the browser connection."""
from pathlib import Path
import json
import sys
import time
import traceback


def atomic(path, value):
    temp = path.with_suffix('.tmp')
    temp.write_text(json.dumps(value,default=str),encoding='utf-8')
    temp.replace(path)


def run(params, log, directory):
    import sympy as sp
    from gwflags import FlagVariety
    from gwflags.gui import parse_k, parse_classes
    from gwflags.execution import configure, gw
    from gwtoric.gui_spectrum import exact_number
    kind = params.get('action','info')
    algebra = params['algebra'].strip()
    keep = [int(v) for v in params['keep'].split(',')]
    if kind == 'hodge':
        from gwflags.hodge import hodge_report
        return dict(hodge=hodge_report(algebra,keep,params.get('K',''),progress=log))
    if kind == 'info':
        from gwflags.gui import run_job
        class Log(list):
            def append(self,message):
                log(message)
        job = {'log':Log()}
        run_job(job,kind,params)
        if job['state']=='error':
            raise ValueError(job['error'])
        return job['result']
    evaluations = int(params.get('evaluations',2))
    cache = Path(directory)/'checkpoints'
    X = configure(FlagVariety(algebra,keep,novikov_convention=params.get('novikov_convention','paper')),cache,evaluations)
    if params.get('_log_path'):
        X._execution['log_path'] = params['_log_path']
    K = X._check_K(parse_k(params.get('K',''),X))
    if kind == 'gw':
        beta = X._check_beta(tuple(int(v) for v in params['beta'].split(',')))
        classes,names = parse_classes(params.get('classes',''),X)
        value = gw(X,classes,beta,K,log)
        return dict(value=str(value),insertions=names,beta=list(beta),evaluations=evaluations,
                    novikov=X.novikov_metadata)
    if kind not in ('sqm','analysis'):
        raise ValueError('Unknown action')
    # Full symbolic matrix is retained independently of the requested specialization.
    import hashlib
    identity = json.dumps([algebra,keep,repr(K.key() if hasattr(K,'key') else K),evaluations,X.novikov_metadata,'staged-v2'])
    cachefile = Path(directory)/('matrix-'+hashlib.sha256(identity.encode()).hexdigest()+'.json')
    if cachefile.exists():
        data = json.loads(cachefile.read_text())
        M, G, idx, fano, betas = sp.Matrix(data['M']),sp.Matrix(data['G']),data['idx'],data['fano'],data['betas']
        log('Reusing completed exact quantum matrix')
    else:
        if kind=='analysis':
            raise ValueError('Compute the quantum matrix for these inputs first')
        fano,betas = X.fano_index_and_betas(K)
        log(f'{len(betas)} supported curve classes; {evaluations} exact evaluation(s) per class')
        M,G,idx = X.small_quantum_multiplication(K,betas,log,int(params.get('workers') or 1))
        M,G = sp.Matrix(M),sp.Matrix(G)
        atomic(cachefile,dict(M=[[str(v) for v in row] for row in M.tolist()],
                             G=[[str(v) for v in row] for row in G.tolist()],idx=idx,fano=fano,betas=betas))
    values = {v:sp.Integer(1) for v in M.free_symbols}
    for pair in params.get('eval_y','').split(','):
        if not pair.strip():
            continue
        if pair.count('=')!=1:
            raise ValueError('Use assignments such as y1=2,y3=3')
        key,value = pair.split('='); symbol=sp.Symbol(key.strip())
        if symbol not in M.free_symbols:
            raise ValueError(f'Unknown Novikov variable {symbol}')
        values[symbol] = exact_number(value)
    from gwflags.gui_analysis import matrix_analysis
    from gwflags.connection_spectra import connection_report
    log('Computing exact unit cyclic determinant and spectrum at the selected Novikov values')
    analysis = matrix_analysis(M,unit_index=idx.index(0),specialization=values,symbolic_cyclicity=False)
    # Distinguish the multiplication determinant from the connection convention.
    if 'cyclic_determinant' in analysis:
        sign = (-1)**(M.rows*(M.rows-1)//2)
        analysis['connection_cyclic_determinant'] = str(sign*sp.sympify(analysis['cyclic_determinant']))
    log('Computing exact regularized exponent multisets')
    try:
        connection = connection_report(M,G,values,log)
    except ValueError as exc:
        connection = dict(status='unresolved',reason=str(exc),sectors=[])
    return dict(matrix=[[str(v) for v in row] for row in M.tolist()],
                grading=[str(G[i,i]) for i in range(G.rows)],basis_indices=idx,
                fano=fano,n_betas=len(betas),evaluations=evaluations,novikov=X.novikov_metadata,
                char_poly=str(M.charpoly().as_expr()),eigenvalues=[],
                analysis=analysis,connection=connection,
                scope='Ambient quantum cohomology for complete intersections')


def main():
    path = Path(sys.argv[1]); request=json.loads(path.read_text(encoding='utf-8'))
    logpath=path.with_suffix('.log'); resultpath=path.with_suffix('.result.json')
    def log(message):
        with logpath.open('a',encoding='utf-8') as stream:
            stream.write(str(message)+'\n')
    start=time.monotonic()
    try:
        request['_log_path']=str(logpath)
        result=run(request,log,path.parent.parent)
        request.pop('_log_path',None)
        result.update(seconds=round(time.monotonic()-start,2),input=request)
        atomic(resultpath,dict(state='done',result=result))
    except Exception as exc:
        log(traceback.format_exc())
        atomic(resultpath,dict(state='error',error=f'{type(exc).__name__}: {exc}'))


if __name__=='__main__':
    main()

