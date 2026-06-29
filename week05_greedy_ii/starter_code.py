"""
Week 05 - Greedy Algorithms II
==============================

Shared utilities used by the practical exercise problems
(starter_code_problem01.py ... starter_code_problem12.py).

You do not need to modify this file. Import what you need, e.g.:

    from starter_code import generate_weighted_graph, UnionFind, edge_list

Conventions
-----------
- A "weighted graph" is represented as an *adjacency dict*: a mapping from each
  vertex ``u`` to a dict ``{v: weight}`` of its neighbours and the weight of the
  edge ``(u, v)``. For undirected graphs the edge appears in both ``graph[u]``
  and ``graph[v]`` with the same weight.
- Vertices are typically the integers ``0, 1, ..., n-1`` but any hashable label
  works.
- An "edge" is a tuple ``(u, v, w)`` of two endpoints and a weight ``w``.
- Random instances are generated with Python's ``random.Random(seed)`` so that
  results are reproducible across runs.
"""

from __future__ import annotations

import random
from typing import Dict, Hashable, List, Tuple

Vertex = Hashable
Weight = float
Graph = Dict[Vertex, Dict[Vertex, Weight]]
Edge = Tuple[Vertex, Vertex, Weight]


def empty_graph(vertices: List[Vertex]) -> Graph:
    """Return an adjacency-dict graph with the given vertices and no edges."""
    return {v: {} for v in vertices}


def add_edge(graph: Graph, u: Vertex, v: Vertex, w: Weight, directed: bool = False) -> None:
    """Add an edge ``(u, v)`` of weight ``w`` to ``graph`` (in place).

    Vertices are created if missing. For undirected graphs (the default) the
    edge is stored in both directions.
    """
    graph.setdefault(u, {})
    graph.setdefault(v, {})
    graph[u][v] = w
    if not directed:
        graph[v][u] = w


def edge_list(graph: Graph, directed: bool = False) -> List[Edge]:
    """Return the edges of ``graph`` as a list of ``(u, v, w)`` tuples.

    For an undirected graph each edge is listed once (with ``u <= v`` by the
    natural ordering of the vertex labels, when comparable; otherwise in the
    order encountered).
    """
    edges: List[Edge] = []
    seen = set()
    for u in graph:
        for v, w in graph[u].items():
            if directed:
                edges.append((u, v, w))
            else:
                key = frozenset((u, v))
                if key in seen:
                    continue
                seen.add(key)
                edges.append((u, v, w))
    return edges


def generate_weighted_graph(
    n: int,
    seed: int | None = None,
    edge_prob: float = 0.5,
    max_weight: int = 20,
    directed: bool = False,
    connected: bool = True,
) -> Graph:
    """Generate a random weighted graph on vertices ``0, ..., n-1``.

    Each possible edge is included independently with probability ``edge_prob``;
    weights are integers uniform in ``[1, max_weight]``. If ``connected`` is
    True a random spanning tree is added first so the (undirected) graph is
    guaranteed connected.
    """
    rng = random.Random(seed)
    graph = empty_graph(list(range(n)))

    if connected and n > 1:
        # Random spanning tree: attach each new vertex to a random earlier one.
        perm = list(range(n))
        rng.shuffle(perm)
        for i in range(1, n):
            u = perm[i]
            v = perm[rng.randrange(i)]
            w = rng.randint(1, max_weight)
            add_edge(graph, u, v, w, directed=directed)

    for u in range(n):
        for v in range(n):
            if u == v:
                continue
            if not directed and u > v:
                continue
            if v in graph[u]:
                continue
            if rng.random() < edge_prob:
                w = rng.randint(1, max_weight)
                add_edge(graph, u, v, w, directed=directed)

    return graph


def vertices(graph: Graph) -> List[Vertex]:
    """Return a sorted list of the vertices of ``graph`` (best effort)."""
    try:
        return sorted(graph.keys())
    except TypeError:
        return list(graph.keys())


class UnionFind:
    """Disjoint-set (union-find) with path compression and union by rank.

    Supports ``find`` (with path compression) and ``union`` (by rank) in
    near-constant amortized time. Used by Kruskal's algorithm and single-link
    clustering.
    """

    def __init__(self, elements: List[Hashable] | None = None) -> None:
        self.parent: Dict[Hashable, Hashable] = {}
        self.rank: Dict[Hashable, int] = {}
        self.num_sets = 0
        if elements is not None:
            for e in elements:
                self.add(e)

    def add(self, x: Hashable) -> None:
        """Add ``x`` as a new singleton set if not already present."""
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
            self.num_sets += 1

    def find(self, x: Hashable) -> Hashable:
        """Return the representative of ``x``'s set, with path compression."""
        if x not in self.parent:
            self.add(x)
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        # Path compression: point every node on the path directly at the root.
        while self.parent[x] != root:
            self.parent[x], x = root, self.parent[x]
        return root

    def union(self, x: Hashable, y: Hashable) -> bool:
        """Merge the sets containing ``x`` and ``y``.

        Returns True if a merge happened, False if they were already together.
        """
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self.num_sets -= 1
        return True

    def connected(self, x: Hashable, y: Hashable) -> bool:
        """Return True iff ``x`` and ``y`` are in the same set."""
        return self.find(x) == self.find(y)
