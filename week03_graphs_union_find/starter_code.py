"""
Week 03 - Graphs & Union-Find
==============================

Shared utilities used by the practical exercise problems
(starter_code_problem01.py ... starter_code_problem24.py).

You do not need to modify this file. Import what you need, e.g.:

    from starter_code import (
        edges_to_adjacency_list,
        edges_to_adjacency_matrix,
        random_undirected_graph,
        random_dag,
        UnionFind,
    )

Conventions
-----------
- Vertices are labeled ``0, 1, ..., n-1`` (integers) unless a problem says
  otherwise.
- An **undirected graph** is given either as:
    * a list of edges ``[(u, v), ...]``, or
    * an adjacency list ``Dict[int, List[int]]`` / ``List[List[int]]`` where
      each edge ``(u, v)`` appears in *both* ``adj[u]`` and ``adj[v]``.
- A **directed graph** is given either as a list of directed edges
  ``[(u, v), ...]`` (meaning an arc ``u -> v``), or an adjacency list where
  ``adj[u]`` lists only the out-neighbors of ``u``.
- ``n`` is always the number of vertices, and vertices are ``range(n)``.
"""

from __future__ import annotations

import random
from typing import Dict, Hashable, Iterable, List, Tuple


def edges_to_adjacency_list(n: int, edges: Iterable[Tuple[int, int]], directed: bool = False) -> List[List[int]]:
    """Build an adjacency list of size `n` from a list of edges.

    For an undirected graph (`directed=False`), each edge (u, v) contributes
    v to adj[u] AND u to adj[v]. For a directed graph, edge (u, v) means an
    arc u -> v and only contributes v to adj[u].

    Self-loops and parallel (multi-)edges are preserved as given (i.e. this
    function does not deduplicate).
    """
    adj: List[List[int]] = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        if not directed and u != v:
            adj[v].append(u)
        elif not directed and u == v:
            # Self-loop in an undirected graph: conventionally counts twice
            # toward the degree, so we add it a second time here too.
            adj[v].append(u)
    return adj


def edges_to_adjacency_matrix(n: int, edges: Iterable[Tuple[int, int]], directed: bool = False) -> List[List[int]]:
    """Build an n x n adjacency matrix from a list of edges.

    matrix[u][v] counts the number of edges between u and v (so parallel
    edges/self-loops are reflected as values > 1, not just 0/1).
    """
    matrix = [[0] * n for _ in range(n)]
    for u, v in edges:
        matrix[u][v] += 1
        if not directed:
            matrix[v][u] += 1
    return matrix


def random_undirected_graph(n: int, m: int, seed: int | None = None, allow_self_loops: bool = False) -> List[Tuple[int, int]]:
    """Generate a random simple undirected graph with `n` vertices and `m`
    distinct edges (no parallel edges; self-loops only if `allow_self_loops`).

    Raises ValueError if `m` exceeds the number of possible distinct edges.
    """
    rng = random.Random(seed)
    possible = []
    for u in range(n):
        start = u if allow_self_loops else u + 1
        for v in range(start, n):
            possible.append((u, v))
    if m > len(possible):
        raise ValueError(f"Cannot create {m} distinct edges among {n} vertices "
                          f"(max is {len(possible)})")
    return rng.sample(possible, m)


def random_dag(n: int, m: int, seed: int | None = None) -> List[Tuple[int, int]]:
    """Generate a random Directed Acyclic Graph with `n` vertices and up to
    `m` edges.

    Every edge (u, v) satisfies u < v, which guarantees acyclicity (the
    natural order 0, 1, ..., n-1 is a valid topological order).
    """
    rng = random.Random(seed)
    possible = [(u, v) for u in range(n) for v in range(u + 1, n)]
    m = min(m, len(possible))
    return rng.sample(possible, m)


class UnionFind:
    """A general-purpose disjoint-set (Union-Find) data structure with
    union-by-rank and path compression, supporting arbitrary hashable
    elements (not just 0..n-1 integers).

    This is the "production-quality" version used as a building block by
    later problems (e.g. Problems 22-24). Problems 18-20 ask you to build
    simpler integer-indexed variants from scratch.
    """

    def __init__(self, elements: Iterable[Hashable] = ()) -> None:
        self._parent: Dict[Hashable, Hashable] = {}
        self._rank: Dict[Hashable, int] = {}
        for e in elements:
            self.make_set(e)

    def make_set(self, x: Hashable) -> None:
        if x not in self._parent:
            self._parent[x] = x
            self._rank[x] = 0

    def find(self, x: Hashable) -> Hashable:
        """Return the representative (root) of the set containing x, with
        path compression."""
        if x not in self._parent:
            self.make_set(x)
        root = x
        while self._parent[root] != root:
            root = self._parent[root]
        # Path compression: point every node on the path directly to root.
        while self._parent[x] != root:
            self._parent[x], x = root, self._parent[x]
        return root

    def union(self, x: Hashable, y: Hashable) -> bool:
        """Union the sets containing x and y. Returns True if they were in
        different sets (and are now merged), False if they were already in
        the same set."""
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self._rank[rx] < self._rank[ry]:
            rx, ry = ry, rx
        self._parent[ry] = rx
        if self._rank[rx] == self._rank[ry]:
            self._rank[rx] += 1
        return True

    def connected(self, x: Hashable, y: Hashable) -> bool:
        return self.find(x) == self.find(y)

    def num_sets(self) -> int:
        return len({self.find(x) for x in self._parent})
