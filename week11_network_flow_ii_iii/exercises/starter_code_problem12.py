"""
Problem 12 - Matching <= Vertex Cover, with Equality in Bipartite Graphs
========================================================================

Implement three functions and then a verifier:

  - `brute_force_max_matching(vertices, edges)`: largest set of edges with no
    shared endpoint (works for ANY graph), by brute force.
  - `brute_force_min_vertex_cover(vertices, edges)`: smallest vertex set covering
    every edge (ANY graph), by brute force.
  - `verify_matching_cover_relationship(num_trials, seed)`: on random graphs,
    check (1) max matching <= min vertex cover always (weak duality), and (2) in
    bipartite graphs max matching == min vertex cover (Konig), confirming the
    constructive cover from Problem 5 attains the bound.

See practical_exercises.pdf, Problem 12, for the full statement and examples.
"""

import os
import sys
from itertools import combinations
from typing import Hashable, List, Set, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "solutions"))

from solution_problem02 import kuhn_matching
from solution_problem05 import min_vertex_cover, is_vertex_cover
from starter_code import generate_bipartite_graph, generate_random_graph

Vertex = Hashable
Edge = Tuple[Vertex, Vertex]


def brute_force_max_matching(vertices: List[Vertex], edges: List[Edge]) -> int:
    """Largest set of edges with no shared endpoint (any graph), by brute force."""
    # TODO: implement this function.
    raise NotImplementedError


def brute_force_min_vertex_cover(vertices: List[Vertex], edges: List[Edge]) -> int:
    """Smallest vertex set covering every edge (any graph), by brute force."""
    # TODO: implement this function.
    raise NotImplementedError


def verify_matching_cover_relationship(num_trials: int = 40, seed: int = 0) -> bool:
    """Check matching <= cover (any graph) and matching == cover (bipartite)."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        assert verify_matching_cover_relationship(num_trials=40, seed=0) is True
        assert verify_matching_cover_relationship(num_trials=25, seed=500) is True

        tri_v = [0, 1, 2]
        tri_e = [(0, 1), (1, 2), (2, 0)]
        assert brute_force_max_matching(tri_v, tri_e) == 1
        assert brute_force_min_vertex_cover(tri_v, tri_e) == 2

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
