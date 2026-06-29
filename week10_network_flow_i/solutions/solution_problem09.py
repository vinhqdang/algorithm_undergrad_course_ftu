"""
Problem 09 - Bipartite Matching via Max Flow (SOLUTION)
========================================================
"""

import os
import sys
from typing import List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solution_problem05 import edmonds_karp
from starter_code import FlowNetwork, generate_bipartite_graph


def max_bipartite_matching(left: int, right: int, edges: List[Tuple[int, int]]) -> int:
    """Maximum-cardinality bipartite matching size, computed via max flow.

    Standard reduction: add a super-source s with a unit-capacity edge to every
    left vertex, a unit-capacity edge for each allowed pair (u on the left to v
    on the right), and a unit-capacity edge from every right vertex to a
    super-sink t. The max-flow value equals the maximum matching size, and (by
    integrality) an integral max flow selects a set of matching edges.
    """
    g = FlowNetwork(source="s", sink="t")
    # Label nodes so the two sides cannot collide.
    for u in range(left):
        g.add_edge("s", ("L", u), 1)
    for v in range(right):
        g.add_edge(("R", v), "t", 1)
    for (u, v) in edges:
        g.add_edge(("L", u), ("R", v), 1)
    return int(edmonds_karp(g))


def _brute_force_matching(left: int, right: int, edges: List[Tuple[int, int]]) -> int:
    """Reference matching size via DFS augmenting paths (Kuhn's algorithm)."""
    adj = {u: [] for u in range(left)}
    for (u, v) in edges:
        adj[u].append(v)
    match_r = [-1] * right

    def try_kuhn(u, seen):
        for v in adj[u]:
            if not seen[v]:
                seen[v] = True
                if match_r[v] == -1 or try_kuhn(match_r[v], seen):
                    match_r[v] = u
                    return True
        return False

    result = 0
    for u in range(left):
        if try_kuhn(u, [False] * right):
            result += 1
    return result


if __name__ == "__main__":
    # Simple perfect matching: 3 left, 3 right, identity edges.
    edges = [(0, 0), (1, 1), (2, 2)]
    assert max_bipartite_matching(3, 3, edges) == 3

    # A "star" where everyone wants vertex 0: matching size only 1.
    edges = [(0, 0), (1, 0), (2, 0)]
    assert max_bipartite_matching(3, 3, edges) == 1

    # Classic case needing an augmenting path to reach the optimum (size 2).
    edges = [(0, 0), (0, 1), (1, 0)]
    assert max_bipartite_matching(2, 2, edges) == 2

    # No edges: matching size 0.
    assert max_bipartite_matching(3, 3, []) == 0

    # Cross-check against Kuhn's algorithm on random bipartite graphs.
    for seed in range(40):
        L, R = 5, 6
        e = generate_bipartite_graph(L, R, seed=seed)
        assert max_bipartite_matching(L, R, e) == _brute_force_matching(L, R, e)

    print("All tests passed!")
