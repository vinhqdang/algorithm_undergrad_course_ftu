"""
Problem 06 - Ford-Fulkerson with DFS Augmenting Paths
=======================================================

Implement the Ford-Fulkerson maximum-flow method, choosing augmenting paths by
DEPTH-first search rather than BFS.

Repeatedly: DFS for ANY residual s-t path; if none exists, stop. Else push the
bottleneck along it. Any path choice yields a correct maximum flow with integer
capacities (the DFS rule does not give the O(V E^2) bound, but terminates on
the small integer instances here). Mutate the edge flows in place and return
the max-flow value.

See practical_exercises.pdf, Problem 6, for the full statement and examples.
"""

import os
import sys
from typing import Hashable

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import FlowEdge, FlowNetwork

Node = Hashable


def ford_fulkerson(network: FlowNetwork) -> float:
    """Compute the maximum s-t flow using DFS augmenting paths."""
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
        assert ford_fulkerson(G) == 5.0

        G2 = FlowNetwork(source="s", sink="t")
        G2.add_edge("s", "a", 1)
        G2.add_edge("s", "b", 1)
        G2.add_edge("a", "b", 1)
        G2.add_edge("a", "t", 1)
        G2.add_edge("b", "t", 1)
        assert ford_fulkerson(G2) == 2.0

        G3 = FlowNetwork(source="s", sink="t")
        G3.add_edge("s", "a", 100)
        G3.add_edge("a", "t", 1)
        assert ford_fulkerson(G3) == 1.0

        G4 = FlowNetwork(source="s", sink="t")
        G4.add_edge("s", "a", 5)
        G4.add_node("t")
        assert ford_fulkerson(G4) == 0.0

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
