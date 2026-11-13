"""gwtoric - genus-0 Gromov-Witten invariants of smooth projective toric
varieties by torus localization, built on the gwflags engine.

Quick start::

    from gwtoric import ToricVariety, projective_space, hirzebruch

    X = projective_space(2)
    X.gw([X.pt, X.pt], beta=(1, 1, 1))      # Fraction(1, 1): one line
    X.gw([X.pt] * 5, beta=(2, 2, 2))        # one conic through 5 points

    F2 = hirzebruch(2)
    print(F2.hodge_diamond_str()); F2.wall_curves

    X = ToricVariety([(1,0), (0,1), (-1,-1)], [(0,1), (1,2), (0,2)])
    M, Gr, names = X.small_quantum_multiplication()
    X.eigenvalues(M, at_one=True)

Curve classes are vectors (a_rho) with sum a_rho rho = 0 and
int_beta x_i = a_i, or coordinates in X.h2_basis.  Classes are polynomials
in the divisor classes X.x(i); X.pt, X.c1, X.classes (graded basis).
"""

from .fan import Fan
from .ring import CohClass, CohomologyRing
from .hodge import HodgeNotSupported
from .engine import ToricGKMEngine, gkm_graph_of_fan, Cancelled
from .variety import (ToricVariety, projective_space, hirzebruch,
                      product_of_projective_spaces,
                      projective_bundle_over_projective_space, del_pezzo_6)
from .quantum import (metric_matrix, betas_and_fano_index,
                      curve_class_report, nonpositive_curves,
                      default_max_degree, small_quantum_multiplication,
                      c1_grading, specialize_c1)
from .mori import (fano_ci_classes, MoriStuck, verify_mori,
                   suggest_inequalities, excluded_classes)
from .connection import (disk_connection, cyclic_determinant, exponents,
                         simple_exponent, characteristic_factors, chi_and_N,
                         hodge_invariant_status, exponential_type_status,
                         allowed_type, invariants, report, NotCyclic)
