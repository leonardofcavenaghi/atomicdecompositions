"""Throttled observational counters; never used to decide mathematical work."""
from contextvars import ContextVar
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import time

ACTIVE_PROGRESS = ContextVar('toric_localization_progress', default=None)


class ClassProgress:
    def __init__(self, beta, callback=None, directory=None, interval=30):
        self.callback = callback
        self.directory = Path(directory) if directory else None
        self.interval = interval
        self.started = time.monotonic()
        self.cpu_started = time.process_time()
        self.last_emit = float('-inf')
        self.assignment_nodes = 0
        self.matching_assignments = 0
        self.marked_configurations = 0
        self.fixed_loci = 0
        self.tree_size_started = None
        self.tree_size_cpu_started = None
        self.data = dict(beta=list(beta), pid=os.getpid(), stage='starting',
                         result_checkpoint=False,
                         note='Work counters are not a time percentage or ETA; counters reset for each evaluation pass.')

    @classmethod
    def create(cls, beta, callback=None):
        directory = os.environ.get('GWTORIC_PROGRESS_DIR')
        if directory and (Path(__file__).resolve().parents[1] / 'examples/fourfolds/batch_results/REPORTING_ON_REQUEST').exists():
            return None
        return cls(beta, callback, directory) if directory or callback else None

    def emit(self, force=False, **updates):
        current = time.monotonic()
        vertices = updates.get('tree_vertices')
        if vertices is not None and vertices != self.data.get('tree_vertices'):
            self.tree_size_started = current
            self.tree_size_cpu_started = time.process_time()
            updates['tree_size_started_at'] = datetime.now(timezone.utc).isoformat()
            force = True
        self.data.update(updates)
        if not force and current - self.last_emit < self.interval:
            return
        self.last_emit = current
        if self.tree_size_started is not None:
            self.data.update(tree_size_wall_seconds=round(current - self.tree_size_started, 3),
                tree_size_cpu_seconds=round(time.process_time() - self.tree_size_cpu_started, 3))
        self.data.update(updated=datetime.now(timezone.utc).isoformat(),
            wall_seconds=round(current - self.started, 3),
            cpu_seconds=round(time.process_time() - self.cpu_started, 3),
            assignment_nodes=self.assignment_nodes,
            matching_assignments=self.matching_assignments,
            marked_configurations=self.marked_configurations, fixed_loci=self.fixed_loci)
        value = json.dumps(self.data)
        # Reporting failures must never abort or change a localization sum.
        if self.directory:
            try:
                self.directory.mkdir(parents=True, exist_ok=True)
                path = self.directory / f'progress-{os.getpid()}.json'
                tmp = path.with_suffix('.tmp')
                tmp.write_text(value + '\n', encoding='utf-8')
                os.replace(tmp, path)
            except OSError:
                pass
        if self.callback:
            try:
                self.callback('class_progress ' + value)
            except Exception:
                pass

    def begin_pass(self, attempt, evaluation, max_edges):
        self.tree_size_started = self.tree_size_cpu_started = None
        self.assignment_nodes = self.matching_assignments = 0
        self.marked_configurations = self.fixed_loci = 0
        for key in ('tree_vertices', 'root_fixed_point', 'root_fixed_points_total',
                    'generation_vertices', 'rooted_shapes_examined', 'unique_shapes_generated',
                    'tree_size_started_at', 'tree_size_wall_seconds', 'tree_size_cpu_seconds'):
            self.data.pop(key, None)
        self.emit(force=True, stage='generating_tree_shapes', evaluation_attempt=attempt,
                  evaluation_pass=evaluation, evaluations_per_attempt=2, max_edges=max_edges,
                  trees_completed=0, trees_total=None, tree_index=None)

    def visit_assignment(self):
        self.assignment_nodes += 1
        # Avoid reading the clock or touching the filesystem on every node.
        if self.assignment_nodes % 4096 == 0:
            self.emit()
