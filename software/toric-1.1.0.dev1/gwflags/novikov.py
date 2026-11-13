"""Names of quantum parameters, independent of the ambient curve lattice.

The papers retain ambient node labels for type A examples and use consecutive
parameters for the other root-system families. Explicit conventions make old
results and alternative presentations reproducible without changing beta.
"""

CONVENTIONS = ('paper', 'ambient', 'compact')


def variable_labels(rs, kept, convention='paper'):
    if convention not in CONVENTIONS:
        raise ValueError('novikov_convention must be paper, ambient or compact')
    ambient = convention == 'ambient' or (
        convention == 'paper' and all(family == 'A' for family, _ in rs.factors))
    return tuple(kept) if ambient else tuple(range(1, len(kept) + 1))


def metadata(rs, kept, convention):
    labels = variable_labels(rs, kept, convention)
    return dict(convention=convention,
                variables=[dict(node=node, name=f'y{label}')
                           for node, label in zip(kept, labels)],
                beta_coordinates='kept-root order or zero-padded ambient roots')
