"""Execution controls shared by the flag API and combined application."""
import os


def worker_limit(requested):
    requested = int(requested)
    if requested < 0:
        raise ValueError('Worker count must be nonnegative')
    limit = min(requested or max(1,(os.cpu_count() or 2)//2),12)
    if os.name == 'nt':
        from gwtoric.memory_workers import memory_usage
        usage = memory_usage()
        if usage['pressure'] >= 85:
            raise MemoryError('Memory pressure is above 85%; retry after memory is available')
        if usage['pressure'] >= 75:
            limit = 1
    return limit


def configure(X, checkpoint_directory=None, evaluations=2):
    if type(evaluations) is not int or evaluations not in (1,2):
        raise ValueError('Choose one or two exact evaluations')
    X._execution = dict(checkpoint_directory=str(checkpoint_directory) if checkpoint_directory else None,
                        evaluations=evaluations)
    return X


def gw(X, classes, beta, K=None, progress=None):
    from fractions import Fraction
    from .staged import staged_sum
    K, beta = X._check_K(K or []), X._check_beta(beta)
    if sum(X.wd.length(c) for c in classes) != X.expected_degree(beta,len(classes),K):
        return Fraction(0)
    if not any(beta):
        return X.gw(classes,beta,K,progress)
    config = X._execution
    for attempt in range(3):
        try:
            results = [staged_sum(c,beta,[classes],K,config['checkpoint_directory'],progress)[0]
                       for c in X._numeric_pair(fresh=attempt>0)[:config['evaluations']]]
            if len(results)==1 or results[0]==results[1]:
                return results[0]
        except ZeroDivisionError:
            pass
    raise ArithmeticError('Exact evaluations disagree')
