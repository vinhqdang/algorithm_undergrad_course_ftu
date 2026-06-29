"""
Week 13 - PSPACE and Extending Tractability (FPT, Branch and Bound)
===================================================================

Shared utilities used by the practical exercise problems
(starter_code_problem01.py ... starter_code_problem12.py).

You do not need to modify this file. Import what you need, e.g.:

    from starter_code import generate_graph, edges_to_adj, brute_force_vertex_cover

Conventions
-----------
- A "graph" is represented as ``(n, edges)`` where ``n`` is the number of
  vertices (labelled ``0 .. n-1``) and ``edges`` is a list of undirected
  ``(u, v)`` tuples with ``u < v`` and no duplicates / self-loops.
- An adjacency representation ``adj`` is a ``dict`` mapping each vertex to a
  ``set`` of its neighbours.
- A "QBF" (quantified boolean formula) is represented as a small tree of
  ``Quant``/``And``/``Or``/``Not``/``Var``/``Const`` node objects (see below).
- A "CNF" formula is a list of clauses; each clause is a list of *literals*;
  a literal is a signed integer ``+i`` (variable ``i`` true) or ``-i``
  (variable ``i`` false), with variables numbered ``1, 2, ...``.
- Random instances are generated with Python's ``random.Random(seed)`` so
  that results are reproducible across runs.
"""

from __future__ import annotations

import itertools
import random
from typing import Dict, List, Optional, Set, Tuple

Graph = Tuple[int, List[Tuple[int, int]]]
Edge = Tuple[int, int]


# ---------------------------------------------------------------------------
# Graph generators and utilities
# ---------------------------------------------------------------------------

def generate_graph(n: int, p: float = 0.3, seed: Optional[int] = None) -> Graph:
    """Generate a random undirected graph G(n, p) on vertices 0..n-1.

    Each possible edge (u, v) with u < v is included independently with
    probability ``p``. Returns ``(n, edges)`` with ``edges`` sorted.
    """
    rng = random.Random(seed)
    edges: List[Edge] = []
    for u in range(n):
        for v in range(u + 1, n):
            if rng.random() < p:
                edges.append((u, v))
    return n, edges


def generate_tree(n: int, seed: Optional[int] = None) -> Graph:
    """Generate a random (uniformly attached) tree on vertices 0..n-1.

    Vertex 0 is the root; each new vertex i attaches to a uniformly random
    earlier vertex. Returns ``(n, edges)`` with ``edges`` sorted (u < v).
    """
    rng = random.Random(seed)
    edges: List[Edge] = []
    for i in range(1, n):
        parent = rng.randrange(i)
        u, v = (parent, i) if parent < i else (i, parent)
        edges.append((u, v))
    edges.sort()
    return n, edges


def edges_to_adj(n: int, edges: List[Edge]) -> Dict[int, Set[int]]:
    """Build an adjacency dict {vertex: set(neighbours)} for an undirected graph."""
    adj: Dict[int, Set[int]] = {v: set() for v in range(n)}
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    return adj


def is_vertex_cover(edges: List[Edge], cover: Set[int]) -> bool:
    """Return True iff ``cover`` touches at least one endpoint of every edge."""
    return all(u in cover or v in cover for u, v in edges)


def is_independent_set(edges: List[Edge], subset: Set[int]) -> bool:
    """Return True iff no edge has both endpoints in ``subset``."""
    return all(not (u in subset and v in subset) for u, v in edges)


def brute_force_vertex_cover(n: int, edges: List[Edge]) -> Set[int]:
    """Return a MINIMUM vertex cover by checking all subsets (exponential).

    Intended only for small ``n`` (n <= ~18). Tries subsets in increasing
    size order and returns the first that covers every edge.
    """
    vertices = list(range(n))
    for size in range(n + 1):
        for combo in itertools.combinations(vertices, size):
            cover = set(combo)
            if is_vertex_cover(edges, cover):
                return cover
    return set(range(n))  # unreachable for finite graphs


def brute_force_independent_set(n: int, edges: List[Edge]) -> Set[int]:
    """Return a MAXIMUM independent set by checking all subsets (exponential).

    Intended only for small ``n`` (n <= ~18).
    """
    vertices = list(range(n))
    for size in range(n, -1, -1):
        for combo in itertools.combinations(vertices, size):
            subset = set(combo)
            if is_independent_set(edges, subset):
                return subset
    return set()


# ---------------------------------------------------------------------------
# QBF / quantified boolean formula representation
# ---------------------------------------------------------------------------
#
# A quantified boolean formula is built from the node classes below.  Each
# node has a ``.eval(env)`` method, where ``env`` maps variable names (str) to
# bool.  ``Quant`` nodes bind a variable with a quantifier ('A' = forall,
# 'E' = exists) over a sub-formula.

class Const:
    """A constant boolean leaf: Const(True) or Const(False)."""

    def __init__(self, value: bool):
        self.value = bool(value)

    def eval(self, env: Dict[str, bool]) -> bool:
        return self.value


class Var:
    """A boolean variable leaf, identified by a name string."""

    def __init__(self, name: str):
        self.name = name

    def eval(self, env: Dict[str, bool]) -> bool:
        return env[self.name]


class Not:
    """Logical negation of one sub-formula."""

    def __init__(self, child):
        self.child = child

    def eval(self, env: Dict[str, bool]) -> bool:
        return not self.child.eval(env)


class And:
    """Logical conjunction of zero or more sub-formulas (empty And == True)."""

    def __init__(self, *children):
        self.children = list(children)

    def eval(self, env: Dict[str, bool]) -> bool:
        return all(c.eval(env) for c in self.children)


class Or:
    """Logical disjunction of zero or more sub-formulas (empty Or == False)."""

    def __init__(self, *children):
        self.children = list(children)

    def eval(self, env: Dict[str, bool]) -> bool:
        return any(c.eval(env) for c in self.children)


class Quant:
    """A quantifier node: kind in {'A', 'E'}, binding ``var`` over ``body``.

    'A' means "forall var"; 'E' means "exists var".
    """

    def __init__(self, kind: str, var: str, body):
        assert kind in ("A", "E")
        self.kind = kind
        self.var = var
        self.body = body

    def eval(self, env: Dict[str, bool]) -> bool:
        # Provided for convenience; Problem 1 asks you to implement this
        # evaluation yourself in a stand-alone function.
        results = []
        for value in (False, True):
            env2 = dict(env)
            env2[self.var] = value
            results.append(self.body.eval(env2))
        return all(results) if self.kind == "A" else any(results)


# ---------------------------------------------------------------------------
# CNF utilities (used by the 2-SAT problem)
# ---------------------------------------------------------------------------

def cnf_is_satisfied(clauses: List[List[int]], assignment: Dict[int, bool]) -> bool:
    """Return True iff ``assignment`` (var -> bool) satisfies every clause.

    A literal ``+i`` is satisfied iff assignment[i] is True; ``-i`` iff
    assignment[i] is False. A clause is satisfied iff at least one literal is.
    """
    for clause in clauses:
        ok = False
        for lit in clause:
            var = abs(lit)
            want = lit > 0
            if assignment.get(var) is want:
                ok = True
                break
        if not ok:
            return False
    return True


def generate_2sat(num_vars: int, num_clauses: int, seed: Optional[int] = None) -> List[List[int]]:
    """Generate a random 2-CNF formula over variables 1..num_vars.

    Each clause has two literals over distinct variables, with random signs.
    """
    rng = random.Random(seed)
    clauses: List[List[int]] = []
    for _ in range(num_clauses):
        a, b = rng.sample(range(1, num_vars + 1), 2)
        lit_a = a if rng.random() < 0.5 else -a
        lit_b = b if rng.random() < 0.5 else -b
        clauses.append([lit_a, lit_b])
    return clauses
