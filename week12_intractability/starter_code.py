"""
Week 12 - Intractability: NP-Completeness and Reductions
=========================================================

Shared utilities used by the practical exercise problems
(starter_code_problem01.py ... starter_code_problem12.py).

You do not need to modify this file. Import what you need, e.g.:

    from starter_code import generate_graph, complement_graph, all_assignments

Conventions
-----------
- A CNF *formula* is a list of *clauses*; each clause is a list of *signed
  integers* (literals). A positive literal ``v`` (v >= 1) means "variable v is
  True"; a negative literal ``-v`` means "variable v is False". Variables are
  numbered 1, 2, ..., num_vars. For example the formula

      (x1 OR NOT x2) AND (x2 OR x3)

  is represented as ``[[1, -2], [2, 3]]`` with ``num_vars = 3``.
- An *assignment* is a list/tuple of booleans of length ``num_vars`` where
  ``assignment[v - 1]`` is the truth value of variable ``v``.
- A *graph* is represented as ``(n, edges)`` where ``n`` is the number of
  vertices (labelled ``0 .. n-1``) and ``edges`` is a set of frozensets
  ``frozenset({u, v})`` -- one per undirected edge.
- A *weighted graph* (for TSP) is an ``n x n`` distance matrix (list of lists)
  with ``dist[i][j]`` the cost of travelling from city ``i`` to city ``j``.
- Random instances are generated with Python's ``random.Random(seed)`` so that
  results are reproducible across runs.

These problems are all about *intractable* (NP-hard / NP-complete) problems, so
the "reference" algorithms here are deliberately exponential brute-force or
backtracking searches. They are correct but only practical for small inputs.
"""

from __future__ import annotations

import itertools
import random
from typing import Dict, FrozenSet, Iterable, List, Optional, Set, Tuple

Literal = int                      # signed integer; -v means "NOT x_v"
Clause = List[Literal]
Formula = List[Clause]
Assignment = Tuple[bool, ...]
Edge = FrozenSet[int]
Graph = Tuple[int, Set[Edge]]      # (num_vertices, set of edges)
Matrix = List[List[float]]


# ---------------------------------------------------------------------------
# CNF / SAT helpers
# ---------------------------------------------------------------------------

def num_variables(formula: Formula) -> int:
    """Return the largest variable index appearing in `formula` (0 if empty)."""
    m = 0
    for clause in formula:
        for lit in clause:
            m = max(m, abs(lit))
    return m


def all_assignments(num_vars: int) -> Iterable[Assignment]:
    """Yield every boolean assignment (tuple of length num_vars), 2**num_vars total."""
    for bits in itertools.product((False, True), repeat=num_vars):
        yield bits


def generate_3sat(num_vars: int, num_clauses: int, seed: int | None = None) -> Formula:
    """Generate a random 3-CNF formula with `num_clauses` clauses over `num_vars`
    variables. Each clause has exactly 3 distinct variables, each negated with
    probability 1/2. Variables are numbered 1 .. num_vars.
    """
    rng = random.Random(seed)
    formula: Formula = []
    for _ in range(num_clauses):
        vars_chosen = rng.sample(range(1, num_vars + 1), 3)
        clause = [v if rng.random() < 0.5 else -v for v in vars_chosen]
        formula.append(clause)
    return formula


# ---------------------------------------------------------------------------
# Graph helpers
# ---------------------------------------------------------------------------

def make_graph(n: int, edge_list: Iterable[Tuple[int, int]]) -> Graph:
    """Build a graph (n, edges) from an iterable of (u, v) pairs."""
    edges: Set[Edge] = set()
    for u, v in edge_list:
        if u != v:
            edges.add(frozenset({u, v}))
    return (n, edges)


def generate_graph(n: int, p: float = 0.5, seed: int | None = None) -> Graph:
    """Generate a random Erdos-Renyi graph G(n, p): n vertices, each possible
    edge present independently with probability p. Reproducible given `seed`.
    """
    rng = random.Random(seed)
    edges: Set[Edge] = set()
    for u in range(n):
        for v in range(u + 1, n):
            if rng.random() < p:
                edges.add(frozenset({u, v}))
    return (n, edges)


def neighbors(graph: Graph, v: int) -> Set[int]:
    """Return the set of vertices adjacent to `v`."""
    n, edges = graph
    result: Set[int] = set()
    for e in edges:
        if v in e:
            result.add(next(iter(e - {v})))
    return result


def complement_graph(graph: Graph) -> Graph:
    """Return the complement of `graph`: same vertices, edge (u,v) present iff
    it is ABSENT in the original. (No self-loops.)
    """
    n, edges = graph
    comp: Set[Edge] = set()
    for u in range(n):
        for v in range(u + 1, n):
            if frozenset({u, v}) not in edges:
                comp.add(frozenset({u, v}))
    return (n, comp)


def edge_tuple(e: Edge) -> Tuple[int, int]:
    """Return the (u, v) pair of an edge with u < v (for printing/ordering)."""
    a, b = sorted(e)
    return (a, b)


def is_clique(graph: Graph, vertices: Iterable[int]) -> bool:
    """Return True iff every pair of `vertices` is joined by an edge."""
    _, edges = graph
    vs = list(vertices)
    for i in range(len(vs)):
        for j in range(i + 1, len(vs)):
            if frozenset({vs[i], vs[j]}) not in edges:
                return False
    return True


# ---------------------------------------------------------------------------
# Subset-sum / misc helpers
# ---------------------------------------------------------------------------

def generate_subset_sum(n: int, max_val: int = 50, seed: int | None = None) -> List[int]:
    """Generate a list of `n` positive integers, each in [1, max_val]."""
    rng = random.Random(seed)
    return [rng.randint(1, max_val) for _ in range(n)]


def generate_distance_matrix(n: int, max_dist: int = 100, seed: int | None = None) -> Matrix:
    """Generate a symmetric n x n distance matrix with zero diagonal."""
    rng = random.Random(seed)
    dist: Matrix = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            d = float(rng.randint(1, max_dist))
            dist[i][j] = d
            dist[j][i] = d
    return dist
