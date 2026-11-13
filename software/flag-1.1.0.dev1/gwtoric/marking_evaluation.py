"""Exact marking sums with the unmarked contribution evaluated only once.

For nonzero vertex sums S_v = sum_{flags at v} d/weight, adding a mark
at v multiplies the unmarked base by S_v. The marked automorphism factor
is still computed separately for every orbit. All caches die with this
one unmarked decoration; no collection of previous decorations is kept.
"""
from fractions import Fraction
import json

from gwflags.trees import ahu_canon, all_possible_marks


def evaluate_key(eng, sets, twist, key):
    canonical = json.loads(key)
    images, edges, labels = {}, [], {}

    def node(encoded):
        v = len(images) + 1
        images[v] = encoded[0]
        for label, child_image, children in encoded[1]:
            w = node([child_image, children])
            edge = (v, w)
            edges.append(edge)
            labels[edge] = tuple(label)
        return v

    if canonical[0] == 'v':
        node(canonical[1])
    else:
        a, b = node(canonical[2]), node(canonical[3])
        edges.append((a, b))
        labels[(a, b)] = tuple(canonical[1])
    k = len(images)
    adj = {v: [] for v in images}
    eimg = {}
    for edge in edges:
        a, b = edge
        adj[a].append((b, edge))
        adj[b].append((a, edge))
        eid, degree = labels[edge]
        pv = images[a]
        fi = next(i for i, flag in enumerate(eng.g.flags[pv]) if flag['edge'] == eid)
        assert sum(eng.g.edges[eid]) - pv == images[b]
        eimg[edge] = (eid, degree, pv, fi)

    vertex_sums = {}
    for v in images:
        value = 0
        for _, edge in adj[v]:
            _, degree, pv, fi = eimg[edge]
            weight = eng.g.flags[pv][fi]['weight']
            if pv != images[v]:
                weight = -weight
            value += degree / weight
        vertex_sums[v] = value

    # Factoring out S_v**(valence-3) could introduce an artificial pole
    # when S_v=0. Keep the original evaluation in that exceptional case,
    # including its handling of actual poles and zero powers.
    shared = all(not eng.bk.is_zero(s) for s in vertex_sums.values())
    if shared:
        unmarked_base, _ = eng._base(
            edges, k, adj, images, eimg, ((),) * k, 1, twist)
    seen = set()
    total = [Fraction(0)] * len(sets)
    nmarks = len(sets[0])
    for marks in all_possible_marks(nmarks, k):
        marked, aut = ahu_canon(k, adj, labels, lambda v: (images[v], marks[v-1]))
        if marked in seen:
            continue
        seen.add(marked)
        if shared:
            base = unmarked_base / aut
            carriers = {}
            for v, at_vertex in enumerate(marks, 1):
                for mark in at_vertex:
                    base *= vertex_sums[v]
                    carriers[mark-1] = images[v]
        else:
            base, carriers = eng._base(edges, k, adj, images, eimg, marks, aut, twist)
        for s, insertions in enumerate(sets):
            value = base
            for mark in range(nmarks):
                value *= insertions[mark][carriers[mark]]
            total[s] += value
    return total
