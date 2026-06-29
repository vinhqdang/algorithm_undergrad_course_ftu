"""
Problem 06 - Reduction 3-SAT -> Independent Set (SOLUTION)
===========================================================
"""

import itertools
from typing import FrozenSet, Iterable, List, Optional, Set, Tuple

Clause = List[int]
Formula = List[Clause]
Edge = FrozenSet[int]
Graph = Tuple[int, Set[Edge]]


# --- small self-contained helpers (SAT + independent set) ---

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


# --- the reduction ---

def reduce_3sat_to_independent_set(formula: Formula) -> Tuple[Graph, int]:
    """Build the gadget graph and target k for the 3-SAT -> Independent Set
    reduction. One vertex per (clause, literal-position); triangle edges within
    a clause; conflict edges between complementary literals in different clauses.
    Returns (graph, k) with k = number of clauses.
    """
    # Vertices: index them 0, 1, 2, ... in order of (clause, position).
    # Record the literal each vertex represents and which clause it belongs to.
    vertex_literal: List[int] = []
    vertex_clause: List[int] = []
    clause_vertices: List[List[int]] = []

    vid = 0
    for ci, clause in enumerate(formula):
        vs: List[int] = []
        for lit in clause:
            vertex_literal.append(lit)
            vertex_clause.append(ci)
            vs.append(vid)
            vid += 1
        clause_vertices.append(vs)

    n = vid
    edges: Set[Edge] = set()

    # Triangle edges: connect all literal-vertices within the same clause.
    for vs in clause_vertices:
        for i in range(len(vs)):
            for j in range(i + 1, len(vs)):
                edges.add(frozenset({vs[i], vs[j]}))

    # Conflict edges: complementary literals in DIFFERENT clauses.
    for a in range(n):
        for b in range(a + 1, n):
            if vertex_clause[a] != vertex_clause[b] and vertex_literal[a] == -vertex_literal[b]:
                edges.add(frozenset({a, b}))

    k = len(formula)
    return (n, edges), k


def verify_reduction(formula: Formula) -> bool:
    """True iff (formula is satisfiable) == (gadget graph has an IS of size >= k)."""
    graph, k = reduce_3sat_to_independent_set(formula)
    sat = brute_force_sat(formula) is not None
    mis = max_independent_set(graph)
    has_is = len(mis) >= k
    return sat == has_is


if __name__ == "__main__":
    # Satisfiable formula
    f_sat = [[1, 2, 3], [-1, -2, -3], [1, -2, 3]]
    g, k = reduce_3sat_to_independent_set(f_sat)
    assert k == 3
    assert verify_reduction(f_sat)

    # Unsatisfiable formula over 1 variable: (x1) AND (NOT x1) -- treat as 1-literal clauses
    f_unsat = [[1], [-1]]
    assert verify_reduction(f_unsat)

    # All 8 clauses over 3 vars -> unsatisfiable
    f_all = [[a, b, c] for a in (1, -1) for b in (2, -2) for c in (3, -3)]
    assert brute_force_sat(f_all) is None
    assert verify_reduction(f_all)

    # A handful of random small formulas
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
