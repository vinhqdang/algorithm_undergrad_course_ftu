"""
Problem 06 - Reduction 3-SAT -> Independent Set
================================================

Implement the gadget reduction:
  - reduce_3sat_to_independent_set(formula) -> (graph, k):
      one vertex per (clause, literal-position); triangle edges within each
      clause; conflict edges between complementary literals in DIFFERENT
      clauses; k = number of clauses.
  - verify_reduction(formula) -> bool:
      True iff (formula satisfiable) == (gadget graph has an independent set of
      size >= k). This checks both directions of the reduction's correctness.

Small self-contained helpers (brute_force_sat, is_independent_set,
max_independent_set) are provided below.

See practical_exercises.pdf, Problem 6.
"""

import itertools
from typing import FrozenSet, Iterable, List, Optional, Set, Tuple

Clause = List[int]
Formula = List[Clause]
Edge = FrozenSet[int]
Graph = Tuple[int, Set[Edge]]


def _num_variables(formula: Formula) -> int:
    m = 0
    for clause in formula:
        for lit in clause:
            m = max(m, abs(lit))
    return m


def brute_force_sat(formula: Formula) -> Optional[Tuple[bool, ...]]:
    n = _num_variables(formula)
    for bits in itertools.product((False, True), repeat=n):
        ok = True
        for clause in formula:
            if not any(
                (lit > 0 and bits[abs(lit) - 1]) or (lit < 0 and not bits[abs(lit) - 1])
                for lit in clause
            ):
                ok = False
                break
        if ok:
            return bits
    return None


def is_independent_set(graph: Graph, subset: Iterable[int]) -> bool:
    _, edges = graph
    vs = list(subset)
    for i in range(len(vs)):
        for j in range(i + 1, len(vs)):
            if frozenset({vs[i], vs[j]}) in edges:
                return False
    return True


def max_independent_set(graph: Graph) -> FrozenSet[int]:
    n, _ = graph
    for size in range(n, -1, -1):
        for combo in itertools.combinations(range(n), size):
            if is_independent_set(graph, combo):
                return frozenset(combo)
    return frozenset()


def reduce_3sat_to_independent_set(formula: Formula) -> Tuple[Graph, int]:
    """Build the gadget graph and target k. Returns (graph, k)."""
    # TODO: implement this function.
    raise NotImplementedError


def verify_reduction(formula: Formula) -> bool:
    """True iff (formula satisfiable) == (gadget has IS of size >= k)."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        f_sat = [[1, 2, 3], [-1, -2, -3], [1, -2, 3]]
        g, k = reduce_3sat_to_independent_set(f_sat)
        assert k == 3
        assert verify_reduction(f_sat)

        f_unsat = [[1], [-1]]
        assert verify_reduction(f_unsat)

        f_all = [[a, b, c] for a in (1, -1) for b in (2, -2) for c in (3, -3)]
        assert brute_force_sat(f_all) is None
        assert verify_reduction(f_all)

        import random
        rng = random.Random(12)
        for _ in range(20):
            nv = rng.randint(2, 4)
            nc = rng.randint(1, 5)
            formula = []
            for _ in range(nc):
                vs = rng.sample(range(1, nv + 1), min(3, nv))
                formula.append([v if rng.random() < 0.5 else -v for v in vs])
            assert verify_reduction(formula)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
