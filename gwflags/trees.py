"""Tree combinatorics of the localization sum (AllTrees, DecoratedTrees,
TableOfTheTree, RemoveIsomorphicDuplicates, DecoratedAutomorphismGroupSize).

A decorated tree is the fixed-locus datum of the graph sum: vertices 1..n
carry a Weyl coset representative (a matrix) and a tuple of marked points;
edges carry (index of a positive root, degree).  Trees are rooted at
vertex 1 for bookkeeping, exactly like the notebook (parentEdge[g, 1, v]).
"""

from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations, product as iproduct
from math import factorial

from .rootsystem import matmul

_FACT = [factorial(i) for i in range(64)]


# ------------------------------------------------------------ integer lattice
def _snf_solve(vectors, target):
    """Integer solution x of  M x = target  with M's columns = vectors,
    or None.  (IntegerCombination of V3.nb, via Smith reduction.)"""
    if not vectors:
        return [] if all(v == 0 for v in target) else None
    nrows, ncols = len(vectors[0]), len(vectors)
    # rows of M
    M = [[vectors[j][i] for j in range(ncols)] for i in range(nrows)]
    t = list(target)
    # eliminate with integer row/column ops; track column ops in V
    V = [[1 if i == j else 0 for j in range(ncols)] for i in range(ncols)]
    r = 0
    for c in range(ncols):
        # find pivot: smallest nonzero |entry| in column c at row >= r
        while True:
            piv = None
            for i in range(r, nrows):
                if M[i][c] != 0 and (piv is None or abs(M[i][c]) < abs(M[piv][c])):
                    piv = i
            if piv is None:
                break
            M[r], M[piv] = M[piv], M[r]
            t[r], t[piv] = t[piv], t[r]
            done = True
            for i in range(r + 1, nrows):
                q = M[i][c] // M[r][c]
                if q:
                    M[i] = [a - q * b for a, b in zip(M[i], M[r])]
                    t[i] -= q * t[r]
                if M[i][c] != 0:
                    done = False
            if done:
                break
        if piv is not None:
            r += 1
    # back-substitute over the rationals, then check integrality of x = V z
    x = [Fraction(0)] * ncols
    for i in range(min(nrows, ncols) - 1, -1, -1):
        lead = next((j for j in range(ncols) if M[i][j] != 0), None)
        if lead is None:
            continue
        s = t[i] - sum(M[i][j] * x[j] for j in range(lead + 1, ncols))
        x[lead] = Fraction(s, M[i][lead])
    # verify (guards rank-deficient / inconsistent cases)
    for i in range(nrows):
        if sum(M[i][j] * x[j] for j in range(ncols)) != t[i]:
            return None
    if any(v.denominator != 1 for v in x):
        return None
    return [int(v) for v in x]


def congruent_mod_gens(v, beta, gens):
    """congruentModGensQ: is v - beta an integer combination of gens?"""
    diff = [a - b for a, b in zip(v, beta)]
    if not gens:
        return all(d == 0 for d in diff)
    # fast path: gens are unit vectors (the removed simple roots), so
    # congruence just means agreement on the other coordinates
    if all(sum(1 for x in g if x) == 1 and max(g) == 1 for g in gens):
        free = {g.index(1) for g in gens}
        return all(d == 0 for i, d in enumerate(diff) if i not in free)
    return _snf_solve(gens, diff) is not None


def nonneg_compositions(k, n):
    """Weak compositions of k into n parts."""
    if n == 1:
        return [[k]]
    out = []
    for i in range(k + 1):
        for rest in nonneg_compositions(k - i, n - 1):
            out.append([i] + rest)
    return out


# ------------------------------------------------------------------ raw trees
@lru_cache(maxsize=None)
def all_trees_n(n):
    """All trees on vertices 1..n up to isomorphism, first (lexicographic)
    representative kept — same enumeration order as AllTreesN."""
    if n == 1:
        return [((), 1)]
    pairs = list(combinations(range(1, n + 1), 2))
    reps, seen_canon = [], set()
    for edges in combinations(pairs, n - 1):
        adj = {v: [] for v in range(1, n + 1)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        # connectivity (n-1 edges + connected => tree)
        stack, seen = [1], {1}
        while stack:
            for w in adj[stack.pop()]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
        if len(seen) != n:
            continue
        canon = min(
            tuple(sorted(tuple(sorted((p[u], p[v]))) for u, v in edges))
            for p in ({v: i + 1 for i, v in enumerate(perm)}
                      for perm in permutations(range(1, n + 1))))
        if canon not in seen_canon:
            seen_canon.add(canon)
            reps.append((edges, n))
    return reps


def all_trees(n):
    """All trees with at most n vertices (AllTrees)."""
    out = []
    for i in range(1, n + 1):
        out.extend(all_trees_n(i))
    return out


# ---------------------------------------------------------------- AHU hashing
def tree_center(n, adj):
    if n <= 2:
        return list(range(1, n + 1))
    deg = {v: len(adj[v]) for v in adj}
    leaves = [v for v, d in deg.items() if d == 1]
    remaining = n
    while remaining > 2:
        new = []
        for v in leaves:
            deg[v] = 0
            for w, _ in adj[v]:
                if deg[w] > 1:
                    deg[w] -= 1
                    if deg[w] == 1:
                        new.append(w)
        remaining -= len(leaves)
        leaves = new
    return leaves


def ahu_canon(n, adj, edeg, vlabel):
    """Canonical key + automorphism group size of a labeled tree, by AHU
    hashing from the center.  Vertex labels compared in full, edge labels
    are the (degree-only) values in edeg — see the note on DecoratedTree."""
    aut = [1]

    def encode(v, parent):
        enc = []
        for w, e in adj[v]:
            if w != parent:
                enc.append((edeg[e],) + encode(w, v))
        enc.sort()
        i = 0
        while i < len(enc):
            j = i
            while j < len(enc) and enc[j] == enc[i]:
                j += 1
            aut[0] *= _FACT[j - i]
            i = j
        return (vlabel(v), tuple(enc))

    center = tree_center(n, adj)
    if len(center) == 1:
        key = encode(center[0], None)
        return ('v', key), aut[0]
    u, v = center
    eu = encode(u, v)
    ev = encode(v, u)
    edge_deg = edeg[(u, v) if (u, v) in edeg else (v, u)]
    return (('e', edge_deg, min(eu, ev), max(eu, ev)),
            aut[0] * (2 if eu == ev else 1))


# ------------------------------------------------------------ decorated trees
class DecoratedTree:
    """edges: tuple of (u,v); elabel: edge -> (root_index, degree);
    vw: vertex -> Weyl matrix; vmarks: vertex -> tuple of mark ids;
    vid: vertex -> small int identifying vw[v] (for fast label keys)."""

    def __init__(self, n, edges, elabel, vw, vmarks, vid=None):
        self.n = n
        self.edges = tuple(edges)
        self.elabel = dict(elabel)
        self.vw = dict(vw)
        self.vmarks = dict(vmarks)
        if vid:
            self.vid = dict(vid)
        else:
            # intern by value (a raw hash() could collide and silently
            # merge distinct vertex labels)
            interned = {}
            self.vid = {v: interned.setdefault(vw[v], len(interned))
                        for v in vw}
        # parent structure, rooted at vertex 1
        adj = {v: [] for v in range(1, n + 1)}
        for e in self.edges:
            u, v = e
            adj[u].append((v, e))
            adj[v].append((u, e))
        self.parent = {1: None}          # vertex -> (parent_vertex, edge)
        order, seen = [1], {1}
        for v in order:
            for w, e in adj[v]:
                if w not in seen:
                    seen.add(w)
                    self.parent[w] = (v, e)
                    order.append(w)
        self.adj = adj

    def children_edges(self, v):
        pe = self.parent[v][1] if self.parent[v] else None
        return [e for _, e in self.adj[v] if e != pe]

    def table(self):
        """TableOfTheTree: per vertex (w, parent_label|None, children labels,
        marks tuple)."""
        lines = []
        for v in range(1, self.n + 1):
            pl = self.elabel[self.parent[v][1]] if self.parent[v] else None
            cl = [self.elabel[e] for e in self.children_edges(v)]
            lines.append((self.vw[v], pl, cl, self.vmarks[v]))
        return lines

    def parent_w(self, v):
        return self.vw[self.parent[v][0]]

    # -------------------------------------------------------- isomorphism
    # Vertex labels (Weyl element, marks) are compared in full; edge labels
    # only by their *degree*.  This mirrors the notebook exactly: its
    # EffectiveEdgeLabel[{_, lbl_}] := lbl keeps only the second entry of an
    # edge label {root, degree}, so RemoveIsomorphicDuplicates and the
    # automorphism count never see the root part.  That is load-bearing: it
    # identifies the two directed representations of one fixed curve, whose
    # root labels differ when seen from either end in a partial flag.
    #
    # Both the canonical form and the automorphism count use AHU tree
    # hashing from the tree's center (O(n^2), no permutation sweep):
    # aut = product over vertices of prod(multiplicity of identical child
    # encodings)!, times 2 when the center is an edge with equal halves.
    def _canon(self):
        """(canonical key, automorphism group size), computed together."""
        edeg = {e: lab[1] for e, lab in self.elabel.items()}
        return ahu_canon(self.n, self.adj, edeg,
                         lambda v: (self.vid[v], self.vmarks[v]))

    def canonical_key(self):
        """Canonical form under labeled isomorphism
        (RemoveIsomorphicDuplicates equivalence)."""
        cached = getattr(self, '_canon_cache', None)
        if cached is None:
            cached = self._canon_cache = self._canon()
        return cached[0]

    def automorphism_group_size(self):
        """DecoratedAutomorphismGroupSize (degree-only edge labels)."""
        cached = getattr(self, '_canon_cache', None)
        if cached is None:
            cached = self._canon_cache = self._canon()
        return cached[1]


@lru_cache(maxsize=None)
def all_possible_marks(k, n):
    """AllPossibleMarks: for every function {1..k} -> {1..n}, the tuple of
    per-vertex mark sets."""
    out = []
    for f in iproduct(range(1, n + 1), repeat=k):
        out.append(tuple(tuple(m + 1 for m in range(k) if f[m] == v)
                         for v in range(1, n + 1)))
    return out


def find_expanded_associations(num_edges, labels, beta, gens):
    """FindExpandedAssociations.

    labels: list of (root_index, coroot_vector) available on edges;
    returns a list of assignments, each a tuple over edges of
    (root_index, degree).

    When the congruence generators are unit vectors (removed simple roots —
    always the case in this pipeline) the assignments are generated by a
    per-edge DFS with componentwise pruning on the kept coordinates, where
    every coroot contribution is nonnegative.  Output is identical to the
    notebook's compositions-then-permutations enumeration."""
    k = num_edges
    cmax = max(1, sum(abs(b) for b in beta)
               + (sum(abs(x) for g in gens for x in g) if gens else 0))
    expanded = [(ri, c, tuple(c * x for x in co))
                for (ri, co) in labels for c in range(1, cmax + 1)]
    if not expanded:
        return []

    unit_gens = all(sum(1 for x in g if x) == 1 and max(g) == 1 for g in gens)
    if unit_gens:
        free = {g.index(1) for g in gens} if gens else set()
        kept = [i for i in range(len(beta)) if i not in free]
        target = [beta[i] for i in kept]
        if any(t < 0 for t in target):
            return []
        vecs = [(ri, c, [vec[i] for i in kept])
                for (ri, c, vec) in expanded]
        out = []
        assign = [None] * k
        def dfs(e, remaining):
            if e == k:
                if all(r == 0 for r in remaining):
                    out.append(tuple(assign))
                return
            for ri, c, v in vecs:
                ok = True
                for i, x in enumerate(v):
                    if x > remaining[i]:
                        ok = False
                        break
                if ok:
                    assign[e] = (ri, c)
                    dfs(e + 1, [r - x for r, x in zip(remaining, v)])
            assign[e] = None
        dfs(0, target)
        return out

    valid = []
    for count in nonneg_compositions(k, len(expanded)):
        total = [0] * len(beta)
        for cnt, (_, _, vec) in zip(count, expanded):
            for i, x in enumerate(vec):
                total[i] += cnt * x
        if congruent_mod_gens(total, beta, gens):
            multiset = []
            for cnt, (ri, c, _) in zip(count, expanded):
                multiset.extend([(ri, c)] * cnt)
            valid.extend(set(permutations(multiset)))
    return valid


def _tree_adjacency(edges, n):
    adj = {v: [] for v in range(1, n + 1)}
    for e in edges:
        adj[e[0]].append((e[1], e))
        adj[e[1]].append((e[0], e))
    return adj


def decoration_representatives(tree, beta, wd):
    """Pass 1 of the decoration enumeration: representatives
    (assoc, vfix, edeg) of the UNMARKED decoration classes of `tree` in
    class beta.  Cached on `wd` — these tuples are two orders of magnitude
    smaller than the marked DecoratedTree lists (no objects are built)."""
    edges, n = tree
    cache_key = (edges, n, tuple(beta), 'unmarked-reps')
    hit = wd.decoration_cache.get(cache_key)
    if hit is not None:
        return hit
    labels = [(qi, wd.rs.coroots[qi]) for qi in wd.reduced_root_indices]
    assocs = find_expanded_associations(len(edges), labels, list(beta),
                                        [list(g) for g in wd.removed_simple_roots])
    adj = _tree_adjacency(edges, n)
    eidx = {e: i for i, e in enumerate(edges)}
    bfs_seq, visited = [], {1}
    order = [1]
    for v in order:
        for w, e in adj[v]:
            if w not in visited:
                visited.add(w)
                bfs_seq.append((w, v, eidx[e]))
                order.append(w)
    step = wd.step_table()
    reps = wd.reduced_group
    # dedup UNMARKED decorated trees.  Marked isomorphism implies unmarked
    # isomorphism, so the marked classes are exactly the marked variants of
    # unmarked class representatives — no need to canonicalize every
    # (start, assoc, marks) triple.
    unmarked_seen = set()
    representatives = []
    vidx = [0] * (n + 1)
    for start_i in range(len(reps)):
        for assoc in assocs:
            # VertexComputation as integer table lookups
            vidx[1] = start_i
            for (w, v, ei) in bfs_seq:
                vidx[w] = step[(vidx[v], assoc[ei][0])]
            edeg = {e: assoc[i][1] for i, e in enumerate(edges)}
            ukey, _ = ahu_canon(n, adj, edeg, vidx.__getitem__)
            if ukey in unmarked_seen:
                continue
            unmarked_seen.add(ukey)
            representatives.append((tuple(assoc), tuple(vidx), edeg))
    wd.decoration_cache[cache_key] = representatives
    return representatives


def iter_decorated_trees(tree, beta, num_marks, wd):
    """Lazy variant of decorated_trees: yields the same marked decoration
    classes in the same order WITHOUT materializing or caching the marked
    list (only the small unmarked pass-1 representatives are cached).  The
    dedup set is scoped per representative — a marked isomorphism restricts
    to an unmarked one, so marked classes of distinct representatives can
    never collide.  Yielded objects are transient: callers must not retain
    them or key caches by id()."""
    edges, n = tree
    representatives = decoration_representatives(tree, beta, wd)
    adj = _tree_adjacency(edges, n)
    marks_options = all_possible_marks(num_marks, n)
    reps = wd.reduced_group
    for assoc, vfix, edeg in representatives:
        seen = set()
        for marks in marks_options:
            key, aut = ahu_canon(
                n, adj, edeg, lambda v: (vfix[v], marks[v - 1]))
            if key in seen:
                continue
            seen.add(key)
            dt = DecoratedTree(
                n, edges, dict(zip(edges, assoc)),
                {v: reps[vfix[v]] for v in range(1, n + 1)},
                {v: marks[v - 1] for v in range(1, n + 1)},
                {v: vfix[v] for v in range(1, n + 1)})
            dt._canon_cache = (key, aut)
            yield dt


def decorated_trees(tree, beta, num_marks, wd):
    """DecoratedTrees: all inequivalent decorations of `tree` in class beta
    with num_marks marked points.  `wd` is a WeylData instance.  Results are
    cached on `wd` (they are reused heavily by paths that revisit the same
    decorations, e.g. single invariants; the quantum-multiplication block
    uses the streaming iter_decorated_trees instead)."""
    edges, n = tree
    cache_key = (edges, n, tuple(beta), num_marks)
    hit = wd.decoration_cache.get(cache_key)
    if hit is not None:
        return hit

    representatives = decoration_representatives(tree, beta, wd)
    adj = _tree_adjacency(edges, n)
    marks_options = all_possible_marks(num_marks, n)
    reps = wd.reduced_group
    # Pass 2: attach marks to the representatives only
    seen, out = set(), []
    for assoc, vfix, edeg in representatives:
        for marks in marks_options:
            key, aut = ahu_canon(
                n, adj, edeg, lambda v: (vfix[v], marks[v - 1]))
            if key in seen:
                continue
            seen.add(key)
            dt = DecoratedTree(
                n, edges, dict(zip(edges, assoc)),
                {v: reps[vfix[v]] for v in range(1, n + 1)},
                {v: marks[v - 1] for v in range(1, n + 1)},
                {v: vfix[v] for v in range(1, n + 1)})
            dt._canon_cache = (key, aut)
            out.append(dt)
    wd.decoration_cache[cache_key] = out
    return out
