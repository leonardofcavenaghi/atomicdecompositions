"""Isolated tree processes: cancelling one tree never breaks its siblings."""
import ctypes
import json
import multiprocessing
import os
from pathlib import Path
import time
import traceback
from . import tree_parallel as original


def memory_usage():
    class Memory(ctypes.Structure):
        _fields_ = [('length', ctypes.c_ulong), ('load', ctypes.c_ulong)] + [
            (n, ctypes.c_ulonglong) for n in ('total_phys', 'avail_phys', 'total_page',
                                            'avail_page', 'total_virtual', 'avail_virtual', 'extended')]
    m = Memory(); m.length = ctypes.sizeof(m)
    if not ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m)):
        raise ctypes.WinError()
    ram = 100 * (1 - m.avail_phys / m.total_phys)
    commit = 100 * (1 - m.avail_page / m.total_page)
    return dict(ram_percent=ram, commit_percent=commit, pressure=max(ram, commit))


def pressure_paused(previous, pressure):
    return pressure >= 80 if previous else pressure >= 85


def run_tree(context, job, result_path):
    result_path = Path(result_path)
    original.initialize_worker(*context)
    try:
        values = original.evaluate_tree(job)
        original.atomic_json(result_path, dict(values=[str(v) for v in values]))
    except BaseException:
        original.atomic_json(result_path, dict(error=traceback.format_exc()))


class TreeTask:
    def __init__(self, context, job, directory):
        self.job = job
        self.result_path = Path(directory) / f'result-{os.getpid()}-{time.time_ns()}.json'
        self.process = multiprocessing.get_context('spawn').Process(
            target=run_tree, args=(context, job, str(self.result_path)))
        self.process.start()
        self.cancel_path = Path(directory) / f'cancel-{self.process.pid}.json'

    def cancel(self):
        if self.process.is_alive():
            self.process.terminate()
        self.process.join()

    def close(self):
        self.cancel()
        self.process.close()
        self.result_path.unlink(missing_ok=True)
        self.cancel_path.unlink(missing_ok=True)

from fractions import Fraction
import copy
from .tree_parallel import manifest, digest, Checkpoints, tree_counts, tree_jobs, now, worker_allocation

def atomic_json(path, data):
    return original.atomic_json(path, data)

def parallel_sum(eng, insertion_sets, beta, twist, config):
    """Same result as engine.gw_multi; no approximate or partial class cache."""
    from .engine import Cancelled
    if eng.bk.name != 'numeric':
        raise ValueError('Tree checkpointing requires the exact numeric backend')
    sizes = {len(t) for t in insertion_sets}
    if len(sizes) != 1 or not insertion_sets or not any(beta):
        raise ValueError('Expected nonzero class and equally sized insertion tuples')
    total_deg = eng.fan.wall_degree(eng.ample, beta)
    if total_deg <= 0:
        return [Fraction(0)] * len(insertion_sets)
    max_edges = total_deg // eng.min_deg
    trees_total = sum(tree_counts(max_edges+1))
    spec = manifest(eng, insertion_sets, beta, twist, max_edges)
    identity = digest(spec)
    base = Path(config['checkpoint_directory'])
    base.mkdir(parents=True, exist_ok=True)
    atomic_json(base / f'{identity}.json', spec)
    store = Checkpoints(base / f'{identity}.sqlite', identity, len(insertion_sets))
    completed, total = store.load()
    metadata = dict(beta=list(beta), max_edges=max_edges, trees_total=trees_total,
                    attempt=spec['attempt'], evaluation=spec['evaluation'], checkpoint=identity)
    status_path = base / 'status.json'
    atomic_json(status_path, dict(metadata, stage='running', trees_completed=len(completed), updated=now()))
    # Send the already chosen numerical weights to every process. Never reroll
    # weights per tree; callbacks and the parent reporter are not serializable.
    worker_eng = copy.copy(eng)
    worker_eng.cancel = None
    worker_eng.progress = None
    # Cached twists refer back to the original engine and its local callback.
    # The selected twist is copied and rebound below; no other twist is needed.
    worker_eng._twists = {}
    worker_twist = copy.copy(twist) if twist else None
    if worker_twist:
        worker_twist.eng = worker_eng
    retry_jobs = []
    context = (worker_eng, insertion_sets, tuple(beta), total_deg, worker_twist, str(base), metadata)
    pending = {}
    validated = set()
    jobs = iter(tree_jobs(max_edges))
    exhausted = False
    try:
        while not exhausted or pending or retry_jobs:
            if eng.cancel is not None and eng.cancel():
                raise Cancelled()
            limit, generation = worker_allocation(config)
            while (not exhausted or retry_jobs) and (len(pending) < limit or len(completed) == trees_total):
                try:
                    job = retry_jobs.pop(0) if retry_jobs else next(jobs)
                except StopIteration:
                    exhausted = True
                    break
                index, edges, vertices = job
                shape = digest((edges, vertices))
                if index in completed:
                    if completed[index] != shape:
                        raise ValueError('Tree enumeration differs from checkpoint')
                    validated.add(index)
                    continue
                task = TreeTask(context, job, base)
                pending[task] = index, shape
            atomic_json(status_path, dict(metadata, stage='running', driver_pid=os.getpid(),
                trees_completed=len(completed), pending_trees=len(pending),
                unsubmitted_trees=trees_total-len(completed)-len(pending),
                allocation_generation=generation, allocated_workers=limit, updated=now()))
            if not pending:
                time.sleep(.2)
            if pending:
                time.sleep(.25)
                for task in list(pending):
                    # A fully published result wins a race with cancellation.
                    if task.result_path.exists() and not task.process.is_alive():
                        index, shape = pending.pop(task)
                        result = json.loads(task.result_path.read_text())
                        task.close()
                        if 'error' in result:
                            raise RuntimeError(result['error'])
                        values = [Fraction(v) for v in result['values']]
                        store.put(index, shape, values)
                        total = [a+b for a,b in zip(total, values)]
                        completed[index] = shape
                        validated.add(index)
                    elif task.cancel_path.exists():
                        pending.pop(task)
                        retry_jobs.append(task.job)
                        task.close()
                    elif not task.process.is_alive():
                        raise RuntimeError(f'Tree worker exited unexpectedly: {task.process.exitcode}')
        if len(completed) != trees_total or validated != set(completed):
            raise ValueError('Incomplete tree coverage')
        atomic_json(status_path, dict(metadata, stage='complete', driver_pid=os.getpid(),
            trees_completed=len(completed), pending_trees=0, unsubmitted_trees=0,
            allocation_generation=generation, allocated_workers=limit, updated=now()))
        return total
    finally:
        for task in pending:
            task.close()
        store.close()
