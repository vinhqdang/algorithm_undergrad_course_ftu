"""
Problem 05 - Konig's Theorem: Min Vertex Cover from Max Matching (SOLUTION)
============================================================================
"""

import os
import sys
from typing import Dict, Hashable, List, Set, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solution_problem02 import kuhn_matching
from starter_code import generate_bipartite_graph

Vertex = Hashable
Edge = Tuple[Vertex, Vertex]


def min_vertex_cover(
    left: List[Vertex], right: List[Vertex], edges: List[Edge]
) -> Set[Vertex]:
    """Construct a minimum vertex cover of a bipartite graph (Konig's theorem).

    Algorithm (the constructive proof of Konig's theorem):
      1. Find a maximum matching M.
      2. Let U = unmatched left vertices. Mark all vertices reachable from U via
         alternating paths (unmatched edge from left, matched edge from right).
      3. The cover is (left vertices NOT marked) UNION (right vertices marked).
    The resulting cover has size exactly |M|.
    """
    adj: Dict[Vertex, Set[Vertex]] = {u: set() for u in left}
    for u, v in edges:
        adj[u].add(v)

    match_right = kuhn_matching(left, right, edges)  # right -> left
    matched_left = set(match_right.values())

    # Alternating-path search from unmatched left vertices.
    marked_left: Set[Vertex] = set()
    marked_right: Set[Vertex] = set()
    stack = [u for u in left if u not in matched_left]
    marked_left.update(stack)
    while stack:
        u = stack.pop()
        for w in adj[u]:
            if w in marked_right:
                continue
            marked_right.add(w)
            if w in match_right:  # follow matching edge back to left
                partner = match_right[w]
                if partner not in marked_left:
                    marked_left.add(partner)
                    stack.append(partner)

    cover = {u for u in left if u not in marked_left} | {v for v in marked_right}
    return cover


def is_vertex_cover(edges: List[Edge], cover: Set[Vertex]) -> bool:
    """Return True iff every edge has at least one endpoint in ``cover``."""
    return all((u in cover) or (v in cover) for u, v in edges)


if __name__ == "__main__":
    for seed in range(60):
        left, right, edges = generate_bipartite_graph(5, 5, p=0.4, seed=seed)
        matching = kuhn_matching(left, right, edges)
        cover = min_vertex_cover(left, right, edges)
        # Konig: |min vertex cover| == |max matching| in bipartite graphs.
        assert len(cover) == len(matching), (seed, len(cover), len(matching))
        # The cover must actually cover every edge.
        assert is_vertex_cover(edges, cover), seed

    # Specific tiny example: a single edge -> cover of size 1, matching of size 1.
    L = [("L", 0)]
    R = [("R", 0)]
    E = [(("L", 0), ("R", 0))]
    assert len(min_vertex_cover(L, R, E)) == 1
    assert is_vertex_cover(E, min_vertex_cover(L, R, E))

    print("All tests passed!")
