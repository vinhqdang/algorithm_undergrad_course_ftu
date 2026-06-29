"""
Problem 05 - Konig's Theorem: Min Vertex Cover from Max Matching
================================================================

Implement `min_vertex_cover(left, right, edges)`: construct a MINIMUM vertex
cover of a bipartite graph using the constructive proof of Konig's theorem.

  1. Find a maximum matching M (e.g. via kuhn_matching from Problem 2).
  2. Let U = unmatched left vertices. Mark all vertices reachable from U via
     alternating paths (unmatched edge from left, matched edge from right).
  3. Cover = (unmarked left vertices) UNION (marked right vertices).

The resulting cover has size exactly |M| (Konig's theorem).

Also implement `is_vertex_cover(edges, cover)` returning True iff every edge has
at least one endpoint in `cover`.

See practical_exercises.pdf, Problem 5, for the full statement and examples.
"""

import os
import sys
from typing import Hashable, List, Set, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "solutions"))

from solution_problem02 import kuhn_matching
from starter_code import generate_bipartite_graph

Vertex = Hashable
Edge = Tuple[Vertex, Vertex]


def min_vertex_cover(
    left: List[Vertex], right: List[Vertex], edges: List[Edge]
) -> Set[Vertex]:
    """Construct a minimum vertex cover of a bipartite graph (Konig's theorem)."""
    # TODO: implement this function.
    raise NotImplementedError


def is_vertex_cover(edges: List[Edge], cover: Set[Vertex]) -> bool:
    """Return True iff every edge has at least one endpoint in `cover`."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        for seed in range(60):
            left, right, edges = generate_bipartite_graph(5, 5, p=0.4, seed=seed)
            matching = kuhn_matching(left, right, edges)
            cover = min_vertex_cover(left, right, edges)
            assert len(cover) == len(matching), (seed, len(cover), len(matching))
            assert is_vertex_cover(edges, cover), seed

        L = [("L", 0)]
        R = [("R", 0)]
        E = [(("L", 0), ("R", 0))]
        assert len(min_vertex_cover(L, R, E)) == 1
        assert is_vertex_cover(E, min_vertex_cover(L, R, E))

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
