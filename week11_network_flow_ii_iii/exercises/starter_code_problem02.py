"""
Problem 02 - Maximum Bipartite Matching via Augmenting Paths (Kuhn's)
=====================================================================

Implement `kuhn_matching(left, right, edges)`: maximum bipartite matching by
Kuhn's augmenting-path algorithm. Return a dict mapping each MATCHED right
vertex to its left partner. For each left vertex, run a DFS that searches for an
augmenting path, bumping already-matched right vertices to alternative partners.

Also implement `max_matching_size(left, right, edges)` returning the size of a
maximum matching.

See practical_exercises.pdf, Problem 2, for the full statement and examples.
"""

import os
import sys
from typing import Dict, Hashable, List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

Vertex = Hashable
Edge = Tuple[Vertex, Vertex]


def kuhn_matching(
    left: List[Vertex], right: List[Vertex], edges: List[Edge]
) -> Dict[Vertex, Vertex]:
    """Maximum bipartite matching by Kuhn's algorithm (returns right -> left)."""
    # TODO: implement this function.
    raise NotImplementedError


def max_matching_size(
    left: List[Vertex], right: List[Vertex], edges: List[Edge]
) -> int:
    """Convenience wrapper returning the size of a maximum matching."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        left = [("L", i) for i in range(3)]
        right = [("R", j) for j in range(3)]
        edges = [(("L", i), ("R", i)) for i in range(3)]
        assert max_matching_size(left, right, edges) == 3

        left2 = [("L", 0), ("L", 1)]
        right2 = [("R", 0), ("R", 1)]
        edges2 = [(("L", 0), ("R", 0)), (("L", 0), ("R", 1)), (("L", 1), ("R", 0))]
        m = kuhn_matching(left2, right2, edges2)
        assert len(m) == 2

        left3 = [("L", 0)]
        right3 = [("R", 0), ("R", 1), ("R", 2)]
        edges3 = [(("L", 0), r) for r in right3]
        assert max_matching_size(left3, right3, edges3) == 1

        assert max_matching_size([0, 1], [2, 3], []) == 0

        big_left = [("L", i) for i in range(5)]
        big_right = [("R", j) for j in range(5)]
        big_edges = [(("L", i), ("R", j)) for i in range(5) for j in range(5) if (i + j) % 2 == 0]
        matching = kuhn_matching(big_left, big_right, big_edges)
        assert len(set(matching.values())) == len(matching)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
