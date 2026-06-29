"""
Problem 02 - Maximum Bipartite Matching via Augmenting Paths (Kuhn's) (SOLUTION)
================================================================================
"""

import os
import sys
from typing import Dict, Hashable, List, Optional, Set, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

Vertex = Hashable
Edge = Tuple[Vertex, Vertex]


def kuhn_matching(
    left: List[Vertex], right: List[Vertex], edges: List[Edge]
) -> Dict[Vertex, Vertex]:
    """Maximum bipartite matching by Kuhn's augmenting-path algorithm.

    Returns a dict mapping each MATCHED right vertex to its left partner. (We
    key by right vertices so that ``match_right[v]`` answers "who owns v".)
    For each left vertex we run a DFS that tries to find an augmenting path,
    repeatedly bumping already-matched right vertices to alternative partners.
    """
    adj: Dict[Vertex, List[Vertex]] = {u: [] for u in left}
    for u, v in edges:
        adj[u].append(v)

    match_right: Dict[Vertex, Vertex] = {}

    def try_augment(u: Vertex, visited: Set[Vertex]) -> bool:
        for v in adj[u]:
            if v in visited:
                continue
            visited.add(v)
            # v is free, or v's current partner can be rematched elsewhere.
            if v not in match_right or try_augment(match_right[v], visited):
                match_right[v] = u
                return True
        return False

    for u in left:
        try_augment(u, set())

    return match_right


def max_matching_size(
    left: List[Vertex], right: List[Vertex], edges: List[Edge]
) -> int:
    """Convenience wrapper returning the size of a maximum matching."""
    return len(kuhn_matching(left, right, edges))


if __name__ == "__main__":
    # Perfect matching on a 3x3 "identity" graph.
    left = [("L", i) for i in range(3)]
    right = [("R", j) for j in range(3)]
    edges = [(("L", i), ("R", i)) for i in range(3)]
    assert max_matching_size(left, right, edges) == 3

    # A path L0-R0-L1-R1 ... classic augmenting structure.
    left2 = [("L", 0), ("L", 1)]
    right2 = [("R", 0), ("R", 1)]
    edges2 = [(("L", 0), ("R", 0)), (("L", 0), ("R", 1)), (("L", 1), ("R", 0))]
    m = kuhn_matching(left2, right2, edges2)
    assert len(m) == 2  # both left vertices can be matched

    # Star: one left vertex connected to three right vertices -> matching size 1.
    left3 = [("L", 0)]
    right3 = [("R", 0), ("R", 1), ("R", 2)]
    edges3 = [(("L", 0), r) for r in right3]
    assert max_matching_size(left3, right3, edges3) == 1

    # No edges -> empty matching.
    assert max_matching_size([0, 1], [2, 3], []) == 0

    # The matching returned must be valid (distinct left partners).
    big_left = [("L", i) for i in range(5)]
    big_right = [("R", j) for j in range(5)]
    big_edges = [(("L", i), ("R", j)) for i in range(5) for j in range(5) if (i + j) % 2 == 0]
    matching = kuhn_matching(big_left, big_right, big_edges)
    assert len(set(matching.values())) == len(matching)  # left partners distinct

    print("All tests passed!")
