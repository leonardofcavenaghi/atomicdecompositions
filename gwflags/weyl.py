"""Weyl group machinery (WeylGroupWords / GenerateGroup / FindCosets /
ProjectionMap / ReflextionRoots of V3.nb).

Group elements are matrices acting on orthogonal coordinates, stored as
hashable tuples of tuples of Fractions.  Words are tuples of 1-based simple
reflection indices, obtained from the same breadth-first search the notebook
uses, so every stored word is reduced and coset representatives found first
are the minimal-length ones.
"""

from .rootsystem import matmul, matvec, identity


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

        self.words = weyl_group_words(rs)          # WeylGroupWords
        self.group = [m for _, m in self.words]    # WeylGroup[[All,2]]
        self.word_of = {m: w for w, m in self.words}

        if not self.removed_roots:
            wp = [self.group[0]]
        else:
            wp = generate_group(
                [rs.reflection_matrices[i - 1] for i in self.removed_roots],
                rs.dim_ort)
        self.wp = wp                               # W_P
        self.cosets = find_cosets(self.group, wp)  # CosetsWeyl
        self.reduced_group = [c[0] for c in self.cosets]  # ReducedWeylGroup
        self._proj = {}
        for c in self.cosets:
            for m in c:
                self._proj[m] = c[0]
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
        return len(self.word_of[m])
