"""
Problem 05 - Edmonds-Karp Maximum Flow
========================================

Implement the Edmonds-Karp maximum-flow algorithm: Ford-Fulkerson augmenting
paths, where each augmenting path is a SHORTEST residual path found by BFS.
This path-selection rule gives the O(V E^2) worst-case bound.

Repeatedly: BFS for a shortest s-t residual path; if none exists, stop. Else
find the bottleneck (minimum residual capacity along the path) and push that
much flow along it (updating forward and reverse residual edges). Mutate the
edge flows in place and return the max-flow value.

See practical_exercises.pdf, Problem 5, for the full statement and examples.
"""

import os
import sys
from typing import Hashable

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import FlowNetwork

Node = Hashable


def edmonds_karp(network: FlowNetwork) -> float:
    """Compute the maximum s-t flow using BFS augmenting paths."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        G = FlowNetwork(source="s", sink="t")
        G.add_edge("s", "a", 3)
        G.add_edge("s", "b", 2)
        G.add_edge("a", "b", 1)
        G.add_edge("a", "t", 2)
        G.add_edge("b", "t", 3)
        assert edmonds_karp(G) == 5.0

        G2 = FlowNetwork(source="s", sink="t")
        G2.add_edge("s", "a", 1)
        G2.add_edge("s", "b", 1)
        G2.add_edge("a", "b", 1)
        G2.add_edge("a", "t", 1)
        G2.add_edge("b", "t", 1)
        assert edmonds_karp(G2) == 2.0

        G3 = FlowNetwork(source="s", sink="t")
        G3.add_edge("s", "a", 100)
        G3.add_edge("a", "t", 1)
        assert edmonds_karp(G3) == 1.0

        G4 = FlowNetwork(source="s", sink="t")
        G4.add_edge("s", "a", 5)
        G4.add_node("t")
        assert edmonds_karp(G4) == 0.0

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
