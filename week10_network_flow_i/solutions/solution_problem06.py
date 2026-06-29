"""
Problem 06 - Ford-Fulkerson with DFS Augmenting Paths (SOLUTION)
=================================================================
"""

import os
import sys
from typing import Hashable, List, Optional

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import FlowEdge, FlowNetwork

Node = Hashable


def _dfs_find_path(network: FlowNetwork, u: Node, t: Node, visited: set):
    """Return a list of FlowEdge forming a residual path u -> ... -> t, or None."""
    if u == t:
        return []
    visited.add(u)
    for e in network.adj[u]:
        if e.residual_capacity() > 1e-12 and e.v not in visited:
            sub = _dfs_find_path(network, e.v, t, visited)
            if sub is not None:
                return [e] + sub
    return None


def ford_fulkerson(network: FlowNetwork) -> float:
    """Compute the maximum s-t flow with Ford-Fulkerson, choosing augmenting
    paths by DFS (depth-first search) rather than BFS.

    Any choice of augmenting path yields a correct maximum flow with integer
    capacities; using DFS (instead of Edmonds-Karp's BFS) does not give the
    O(V E^2) bound, but on the small integer-capacity instances here it
    terminates and returns the same max-flow value. Mutates the edge flows in
    place and returns the value.
    """
    network.reset_flow()
    s, t = network.source, network.sink
    if s == t:
        return 0.0

    max_flow = 0.0
    while True:
        path = _dfs_find_path(network, s, t, set())
        if path is None:
            break
        bottleneck = min(e.residual_capacity() for e in path)
        for e in path:
            e.push(bottleneck)
        max_flow += bottleneck

    return max_flow


if __name__ == "__main__":
    G = FlowNetwork(source="s", sink="t")
    G.add_edge("s", "a", 3)
    G.add_edge("s", "b", 2)
    G.add_edge("a", "b", 1)
    G.add_edge("a", "t", 2)
    G.add_edge("b", "t", 3)
    assert ford_fulkerson(G) == 5.0

    # The diamond requiring flow cancellation: DFS may pick s-a-b-t first, then
    # the residual back-edge lets it still reach value 2.
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
