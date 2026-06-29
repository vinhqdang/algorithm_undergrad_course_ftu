"""
Week 11 - Network Flow II/III: Bipartite Matching and Flow Applications
=======================================================================

Shared utilities used by the practical exercise problems
(starter_code_problem01.py ... starter_code_problem12.py).

You do not need to modify this file. Import what you need, e.g.:

    from starter_code import MaxFlow, generate_bipartite_graph, edges_to_adj

Conventions
-----------
- A directed flow network is built with the :class:`MaxFlow` helper, which runs
  the Edmonds-Karp algorithm (BFS-augmenting-path Ford-Fulkerson). Vertices are
  arbitrary hashable labels; you call ``add_edge(u, v, cap)`` and then
  ``max_flow(s, t)``.
- A "bipartite graph" is represented as ``(left, right, edges)`` where ``left``
  and ``right`` are lists of vertex labels for the two sides and ``edges`` is a
  list of ``(u, v)`` pairs with ``u in left`` and ``v in right``.
- An "adjacency list" is a ``dict`` mapping each vertex to a ``set`` of
  neighbours (undirected unless stated otherwise).
- Random instances are generated with Python's ``random.Random(seed)`` so that
  results are reproducible across runs.
"""

from __future__ import annotations

import random
from collections import defaultdict, deque
from typing import Dict, Hashable, List, Optional, Set, Tuple

Vertex = Hashable
Edge = Tuple[Vertex, Vertex]


class MaxFlow:
    """A small max-flow solver using the Edmonds-Karp algorithm.

    Edmonds-Karp is Ford-Fulkerson where each augmenting path is found by BFS
    (a shortest path in the residual graph, by number of edges). This runs in
    ``O(V * E^2)`` time, which is more than fast enough for the small networks
    that arise in this week's flow-application reductions.

    Usage
    -----
        mf = MaxFlow()
        mf.add_edge("s", "a", 3)
        mf.add_edge("a", "t", 2)
        value = mf.max_flow("s", "t")

    After ``max_flow`` returns, ``mf.flow(u, v)`` gives the flow pushed along
    the original edge ``(u, v)``, and ``mf.min_cut_reachable(s)`` returns the
    set of vertices on the source side of a minimum cut.
    """

    def __init__(self) -> None:
        # capacity[u][v] is the residual capacity of the edge u -> v.
        self.capacity: Dict[Vertex, Dict[Vertex, float]] = defaultdict(dict)
        # original_capacity remembers the capacities before any flow was pushed,
        # so we can recover the flow on each forward edge afterward.
        self.original_capacity: Dict[Vertex, Dict[Vertex, float]] = defaultdict(dict)
        self.vertices: Set[Vertex] = set()

    def add_edge(self, u: Vertex, v: Vertex, cap: float) -> None:
        """Add a directed edge u -> v with capacity ``cap``.

        A reverse residual edge v -> u with capacity 0 is created automatically
        (if one does not already exist) so that flow can be cancelled.
        """
        self.vertices.add(u)
        self.vertices.add(v)
        self.capacity[u][v] = self.capacity[u].get(v, 0.0) + cap
        self.original_capacity[u][v] = self.original_capacity[u].get(v, 0.0) + cap
        # Ensure a reverse residual edge exists.
        if u not in self.capacity[v]:
            self.capacity[v][u] = self.capacity[v].get(u, 0.0)

    def _bfs_augmenting_path(self, s: Vertex, t: Vertex) -> Optional[Dict[Vertex, Vertex]]:
        """Find a shortest augmenting path from s to t in the residual graph.

        Returns a parent map (child -> parent) describing the path, or None if
        t is unreachable.
        """
        parent: Dict[Vertex, Vertex] = {s: s}
        queue = deque([s])
        while queue:
            u = queue.popleft()
            if u == t:
                return parent
            for v, residual in self.capacity[u].items():
                if v not in parent and residual > 1e-12:
                    parent[v] = u
                    queue.append(v)
        return None

    def max_flow(self, s: Vertex, t: Vertex) -> float:
        """Compute and return the value of a maximum s-t flow."""
        self.vertices.add(s)
        self.vertices.add(t)
        total = 0.0
        while True:
            parent = self._bfs_augmenting_path(s, t)
            if parent is None:
                break
            # Find the bottleneck residual capacity along the path.
            bottleneck = float("inf")
            v = t
            while v != s:
                u = parent[v]
                bottleneck = min(bottleneck, self.capacity[u][v])
                v = u
            # Push `bottleneck` units of flow along the path.
            v = t
            while v != s:
                u = parent[v]
                self.capacity[u][v] -= bottleneck
                self.capacity[v][u] = self.capacity[v].get(u, 0.0) + bottleneck
                v = u
            total += bottleneck
        return total

    def flow(self, u: Vertex, v: Vertex) -> float:
        """Flow pushed on the original edge (u, v) after max_flow has run.

        Equals (original capacity) - (remaining residual capacity).
        """
        orig = self.original_capacity.get(u, {}).get(v, 0.0)
        remaining = self.capacity.get(u, {}).get(v, 0.0)
        return orig - remaining

    def min_cut_reachable(self, s: Vertex) -> Set[Vertex]:
        """Return the set of vertices reachable from s in the residual graph.

        Call this after :meth:`max_flow`. By the max-flow min-cut theorem, the
        edges from this set to its complement form a minimum cut.
        """
        reachable: Set[Vertex] = {s}
        queue = deque([s])
        while queue:
            u = queue.popleft()
            for v, residual in self.capacity[u].items():
                if v not in reachable and residual > 1e-12:
                    reachable.add(v)
                    queue.append(v)
        return reachable


def edges_to_adj(vertices: List[Vertex], edges: List[Edge], directed: bool = False) -> Dict[Vertex, Set[Vertex]]:
    """Build an adjacency-list dict from a vertex list and an edge list."""
    adj: Dict[Vertex, Set[Vertex]] = {v: set() for v in vertices}
    for u, v in edges:
        adj.setdefault(u, set()).add(v)
        if not directed:
            adj.setdefault(v, set()).add(u)
    return adj


def generate_bipartite_graph(
    n_left: int,
    n_right: int,
    p: float = 0.4,
    seed: Optional[int] = None,
) -> Tuple[List[Vertex], List[Vertex], List[Edge]]:
    """Generate a random bipartite graph.

    Left vertices are labelled ``("L", 0), ("L", 1), ...`` and right vertices
    ``("R", 0), ("R", 1), ...``. Each possible left-right pair becomes an edge
    independently with probability ``p``.

    Returns ``(left, right, edges)``.
    """
    rng = random.Random(seed)
    left: List[Vertex] = [("L", i) for i in range(n_left)]
    right: List[Vertex] = [("R", j) for j in range(n_right)]
    edges: List[Edge] = []
    for u in left:
        for v in right:
            if rng.random() < p:
                edges.append((u, v))
    return left, right, edges


def generate_random_graph(
    n: int,
    p: float = 0.3,
    seed: Optional[int] = None,
) -> Tuple[List[Vertex], List[Edge]]:
    """Generate a random undirected simple graph on vertices ``0..n-1``.

    Each unordered pair is an edge independently with probability ``p``.
    Returns ``(vertices, edges)``.
    """
    rng = random.Random(seed)
    vertices = list(range(n))
    edges: List[Edge] = []
    for i in range(n):
        for j in range(i + 1, n):
            if rng.random() < p:
                edges.append((i, j))
    return vertices, edges


def matching_size(matching: Dict[Vertex, Vertex]) -> int:
    """Number of matched pairs in a matching given as a dict left -> right.

    Only counts entries whose value is not None.
    """
    return sum(1 for v in matching.values() if v is not None)


def is_valid_matching(edges: List[Edge], matching: List[Edge]) -> bool:
    """Return True iff ``matching`` is a subset of ``edges`` with no shared
    endpoints (i.e. a genuine matching of the graph)."""
    edge_set = {(u, v) for u, v in edges} | {(v, u) for u, v in edges}
    used: Set[Vertex] = set()
    for u, v in matching:
        if (u, v) not in edge_set:
            return False
        if u in used or v in used:
            return False
        used.add(u)
        used.add(v)
    return True
