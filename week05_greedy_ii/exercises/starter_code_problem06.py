"""
Problem 06 - Counter-Example: Dijkstra Fails on a Negative Edge
===============================================================

Construct a small directed graph with a single negative edge (and no negative
cycle) on which Dijkstra (Problem 2) reports a wrong distance, while
Bellman-Ford (Problem 4) is correct. See practical_exercises.pdf, Problem 6.
"""

import os
import sys
from typing import Dict, Hashable, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from starter_code import Graph, add_edge  # noqa: F401,E402

from starter_code_problem02 import dijkstra  # noqa: E402
from starter_code_problem04 import bellman_ford  # noqa: E402


def negative_edge_graph() -> Graph:
    """Return a small directed graph with one negative edge and no negative cycle
    on which Dijkstra is incorrect."""
    # TODO: implement this function.
    raise NotImplementedError


def dijkstra_vs_bellman_ford() -> Tuple[Dict[Hashable, float], Dict[Hashable, float]]:
    """Return ``(dijkstra_dist, bellman_ford_dist)`` for the counter-example.

    The two distance dicts must differ at some vertex.
    """
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        d_dij, d_bf = dijkstra_vs_bellman_ford()
        # The two algorithms must disagree somewhere.
        assert any(d_dij[v] != d_bf[v] for v in d_bf)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
