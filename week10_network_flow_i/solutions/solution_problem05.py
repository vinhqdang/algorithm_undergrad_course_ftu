"""
Problem 05 - Edmonds-Karp Maximum Flow (SOLUTION)
===================================================
"""

import os
import sys
from collections import deque
from typing import Hashable

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import FlowNetwork

Node = Hashable


def edmonds_karp(network: FlowNetwork) -> float:
    """Compute the maximum s-t flow using the Edmonds-Karp rule.

    Edmonds-Karp = Ford-Fulkerson with the specific choice of always augmenting
    along a *shortest* (fewest-edges) residual path, found by BFS. This choice
    guarantees O(V E^2) running time. Mutates the edge flows in place and
    returns the max-flow value.
    """
    network.reset_flow()
    s, t = network.source, network.sink
    if s == t:
        return 0.0

    max_flow = 0.0
    while True:
        # BFS for a shortest augmenting path; record the edge used to reach
        # each node so we can recover (and update) the path.
        parent_edge = {s: None}
        queue = deque([s])
        while queue:
            u = queue.popleft()
            if u == t:
                break
            for e in network.adj[u]:
                if e.residual_capacity() > 1e-12 and e.v not in parent_edge:
                    parent_edge[e.v] = e
                    queue.append(e.v)
        if t not in parent_edge:
            break  # no augmenting path remains

        # Bottleneck = minimum residual capacity along the path.
        bottleneck = float("inf")
        v = t
        while v != s:
            e = parent_edge[v]
            bottleneck = min(bottleneck, e.residual_capacity())
            v = e.u

        # Push the bottleneck along the whole path.
        v = t
        while v != s:
            e = parent_edge[v]
            e.push(bottleneck)
            v = e.u

        max_flow += bottleneck

    return max_flow


if __name__ == "__main__":
    # Classic K&T-style example with max flow 5.
    G = FlowNetwork(source="s", sink="t")
    G.add_edge("s", "a", 3)
    G.add_edge("s", "b", 2)
    G.add_edge("a", "b", 1)
    G.add_edge("a", "t", 2)
    G.add_edge("b", "t", 3)
    assert edmonds_karp(G) == 5.0

    # A network requiring flow cancellation (the "diamond" that breaks naive
    # greedy DFS without residual back-edges). Max flow is 2.
    G2 = FlowNetwork(source="s", sink="t")
    G2.add_edge("s", "a", 1)
    G2.add_edge("s", "b", 1)
    G2.add_edge("a", "b", 1)
    G2.add_edge("a", "t", 1)
    G2.add_edge("b", "t", 1)
    assert edmonds_karp(G2) == 2.0

    # Single path bottleneck.
    G3 = FlowNetwork(source="s", sink="t")
    G3.add_edge("s", "a", 100)
    G3.add_edge("a", "t", 1)
    assert edmonds_karp(G3) == 1.0

    # No path from source to sink.
    G4 = FlowNetwork(source="s", sink="t")
    G4.add_edge("s", "a", 5)
    G4.add_node("t")
    assert edmonds_karp(G4) == 0.0

    print("All tests passed!")
