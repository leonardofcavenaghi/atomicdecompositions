"""Weyl group machinery (WeylGroupWords / GenerateGroup / FindCosets /
ProjectionMap / ReflextionRoots of V3.nb).

Group elements are matrices acting on orthogonal coordinates, stored as
hashable tuples of tuples of Fractions.  Words are tuples of 1-based simple
reflection indices, obtained from the same breadth-first search the notebook
uses, so every stored word is reduced and coset representatives found first
are the minimal-length ones.
"""

from itertools import combinations, islice, permutations
from math import factorial

from .rootsystem import matmul, matvec, identity


class _PermutationGroupView:
    """Lazy view of the Weyl group of type A.

    The localization code only needs the identity from ``wd.group``.  Keeping
    the view iterable and indexable preserves that small public convenience
    while avoiding materializing ``S_n`` when a partial flag has only a small
    number of minimal coset representatives.
    """

    def __init__(self, n):
        self.n = n
        self._order = factorial(n)

    def __len__(self):
        return self._order

    def __iter__(self):
        return (_a_perm_matrix(p) for p in permutations(range(1, self.n + 1)))

    def __getitem__(self, index):
        if isinstance(index, slice):
            start, stop, step = index.indices(self._order)
            if step < 0:
                raise ValueError('negative slices are not supported')
            return list(islice(iter(self), start, stop, step))
        if index < 0:
            index += self._order
        if index < 0 or index >= self._order:
            raise IndexError('Weyl-group index out of range')
        return next(islice(iter(self), index, index + 1))


def _a_perm_matrix(p):
    """Permutation matrix for the one-line image tuple ``p``."""
    n = len(p)
    rows = [[0] * n for _ in range(n)]
    for col, image in enumerate(p):
        rows[image - 1][col] = 1
    return tuple(tuple(row) for row in rows)


def _a_matrix_perm(m):
    """Recover a type-A one-line image tuple from a permutation matrix."""
    n = len(m)
    out = []
    for col in range(n):
        nonzero = [i + 1 for i in range(n) if m[i][col] != 0]
        if len(nonzero) != 1 or m[nonzero[0] - 1][col] != 1:
            raise ValueError('matrix is not a type-A permutation matrix')
        out.append(nonzero[0])
    if set(out) != set(range(1, n + 1)):
        raise ValueError('matrix is not a type-A permutation matrix')
    return tuple(out)


def _a_reduced_word(p):
    """A reduced right-multiplication word for an A-type permutation."""
    work = list(p)
    swaps = []
    while True:
        changed = False
        for i in range(len(work) - 1):
            if work[i] > work[i + 1]:
                work[i], work[i + 1] = work[i + 1], work[i]
                swaps.append(i + 1)
                changed = True
        if not changed:
            break
    # The swaps sent p to the identity; reverse them to obtain p from 1.
    return tuple(reversed(swaps))


def _a_partial_representatives(n, block_sizes):
    """Minimal right-coset representatives for a type-A partial flag.

    A representative is a concatenation of increasing blocks.  Choosing the
    values in each block gives the usual multinomial number of Schubert
    classes without constructing the full symmetric group.
    """
    values = tuple(range(1, n + 1))
    out = []

    def choose(remaining, sizes, prefix):
        if not sizes:
            out.append(tuple(prefix))
            return
        size = sizes[0]
        for block in combinations(remaining, size):
            chosen = set(block)
            choose(tuple(v for v in remaining if v not in chosen),
                   sizes[1:], prefix + list(block))

    choose(values, tuple(block_sizes), [])
    return out


def _a_minimal_right_coset_rep(m, block_sizes):
    """Project a type-A Weyl element to its minimal right-coset rep."""
    p = _a_matrix_perm(m)
    out, start = [], 0
    for size in block_sizes:
        out.extend(sorted(p[start:start + size]))
        start += size
    return _a_perm_matrix(tuple(out))


def weyl_group_words(rs):
    """BFS over products of simple reflections.

    Returns a list of (word, matrix) pairs; entry 0 is the identity.
    Mirrors WeylGroupWords[] including its ordering.
    """
    gens = rs.reflection_matrices
    ident = identity(rs.dim_ort)
    seen = {ident: ()}
    order = [(ident, ())]
    frontier = [ident]
    while frontier:
        new = []
        for m in frontier:
            w = seen[m]
            for i, g in enumerate(gens):
                p = matmul(m, g)
                if p not in seen:
                    seen[p] = w + (i + 1,)
                    order.append((p, w + (i + 1,)))
                    new.append(p)
        frontier = new
    return [(word, m) for m, word in order]


def generate_group(gens, dim):
    """GenerateGroup: all products of the given reflection matrices."""
    ident = identity(dim)
    seen = {ident}
    order = [ident]
    frontier = [ident]
    while frontier:
        new = []
        for m in frontier:
            for g in gens:
                p = matmul(m, g)
                if p not in seen:
                    seen.add(p)
                    order.append(p)
                    new.append(p)
        frontier = new
    return order


def find_cosets(group, subgroup):
    """FindCosets: partition `group` (list of matrices, BFS order) into left
    cosets g.P; each coset is listed with its first-found (minimal) element
    first."""
    index = {m: i for i, m in enumerate(group)}
    used = [False] * len(group)
    cosets = []
    for i, g in enumerate(group):
        if used[i]:
            continue
        coset_idx = []
        for p in subgroup:
            j = index.get(matmul(g, p))
            if j is not None and j not in coset_idx:
                coset_idx.append(j)
        for j in coset_idx:
            used[j] = True
        cosets.append([group[j] for j in coset_idx])
    return cosets


class WeylData:
    """Bundles the Weyl-group objects of the notebook for a flag G/P.

    roots_that_stay: 1-based indices of the simple roots kept out of P
    (the notebook's ``m`` / RootsThatStay).
    """

    def __init__(self, rs, roots_that_stay):
        self.rs = rs
        self.roots_that_stay = list(roots_that_stay)
        self.removed_roots = [i for i in range(1, rs.rank + 1)
                              if i not in self.roots_that_stay]
        # RemovedSimpleRoots: unit vectors of the removed nodes
        self.removed_simple_roots = [
            tuple(1 if j == i - 1 else 0 for j in range(rs.rank))
            for i in self.removed_roots]

        # For the large type-A cases relevant to Peskine, enumerate the
        # minimal partial-flag representatives directly.  The old BFS first
        # built all of S_10 (3,628,800 matrices) even though F(1,4;10) has
        # only 840 Schubert classes.
        direct_a = (len(rs.factors) == 1 and rs.factors[0][0] == 'A'
                    and factorial(rs.factors[0][1] + 1) > 100_000)
        self._a_block_sizes = None
        if direct_a:
            n = rs.factors[0][1] + 1
            cuts = [0] + sorted(self.roots_that_stay) + [n]
            block_sizes = tuple(b - a for a, b in zip(cuts, cuts[1:]))
            rep_count = factorial(n)
            for size in block_sizes:
                rep_count //= factorial(size)
            if rep_count > 250_000:
                raise ValueError(
                    f'type-A partial flag has {rep_count} Schubert classes; '
                    'the direct backend is capped at 250000 classes')
            reps = _a_partial_representatives(n, block_sizes)
            self.words = [(_a_reduced_word(p), _a_perm_matrix(p))
                          for p in reps]
            self.group = _PermutationGroupView(n)
            self.group_order = len(self.group)
            self.word_of = {m: w for w, m in self.words}
            self.wp = None
            self.wp_order = 1
            for size in block_sizes:
                self.wp_order *= factorial(size)
            self.cosets = None
            self.reduced_group = [m for _, m in self.words]
            self._a_block_sizes = block_sizes
        else:
            self.words = weyl_group_words(rs)          # WeylGroupWords
            self.group = [m for _, m in self.words]    # WeylGroup[[All,2]]
            self.group_order = len(self.group)
            self.word_of = {m: w for w, m in self.words}

            if not self.removed_roots:
                wp = [self.group[0]]
            else:
                wp = generate_group(
                    [rs.reflection_matrices[i - 1]
                     for i in self.removed_roots], rs.dim_ort)
            self.wp = wp                               # W_P
            self.wp_order = len(wp)
            self.cosets = find_cosets(self.group, wp)  # CosetsWeyl
            self.reduced_group = [c[0] for c in self.cosets]
        self._proj = {}
        if self.cosets is not None:
            for c in self.cosets:
                for m in c:
                    self._proj[m] = c[0]
        else:
            for m in self.reduced_group:
                self._proj[m] = m
        # small-int id per coset representative (fast decorated-tree keys)
        self.rep_index = {m: i for i, m in enumerate(self.reduced_group)}
        # DecoratedTrees results, shared by every calculator on this flag
        self.decoration_cache = {}

        # ReducedRootSystem: positive roots not in the root system of P
        # (RootsComput[] of V3.nb)
        keep = []
        for q, r in enumerate(rs.positive_roots):
            if any(r[e - 1] != 0 for e in self.roots_that_stay):
                keep.append(q)
        self.reduced_root_indices = keep
        self.reduced_roots = [rs.positive_roots[q] for q in keep]
        self.reduced_roots_ort = [rs.positive_roots_ort[q] for q in keep]
        self.reduced_coroots = [rs.coroots[q] for q in keep]

        # ReflextionRoots: the reflection matrix s_beta for every positive
        # root beta (computed directly instead of by conjugation search)
        self.reflection_of_root = {
            r: rs.reflection_matrix_of(r_ort)
            for r, r_ort in zip(rs.positive_roots, rs.positive_roots_ort)}

    def project(self, m):
        """ProjectionMap: minimal representative of the coset m.W_P."""
        if self._a_block_sizes is not None:
            return _a_minimal_right_coset_rep(m, self._a_block_sizes)
        return self._proj[m]

    def step_table(self):
        """(rep index, positive-root index) -> rep index of
        proj(rep . s_root), precomputed for the reduced roots.  Turns the
        vertex computation of decorated trees into integer table lookups."""
        tab = getattr(self, '_step_table', None)
        if tab is None:
            tab = {}
            for i, w in enumerate(self.reduced_group):
                for q in self.reduced_root_indices:
                    root = self.rs.positive_roots[q]
                    tab[(i, q)] = self.rep_index[self.project(
                        matmul(w, self.reflection_of_root[root]))]
            self._step_table = tab
        return tab

    def length(self, m):
        """Coxeter length of a group element (its BFS word is reduced)."""
        if self._a_block_sizes is not None and m not in self.word_of:
            p = _a_matrix_perm(m)
            return sum(p[i] > p[j]
                       for i in range(len(p)) for j in range(i + 1, len(p)))
        return len(self.word_of[m])
