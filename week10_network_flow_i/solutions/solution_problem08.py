"""
Problem 08 - Extract the Minimum Cut from a Max Flow (SOLUTION)
================================================================
"""

import os
import sys
from collections import deque
from typing import Hashable, Set, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solution_problem02 import cut_capacity
from solution_problem05 import edmonds_karp
from starter_code import FlowNetwork, generate_flow_network

Node = Hashable


def min_cut(network: FlowNetwork) -> Tuple[Set[Node], float]:
    """Compute a maximum flow, then extract a minimum cut from it.

    After a maximum flow is found, let S be the set of nodes reachable from the
    source in the *final residual graph* (along edges with positive residual
    capacity). Then (S, V\\S) is a minimum cut, and its capacity equals the
    max-flow value (Max-Flow Min-Cut theorem). Returns (S, max_flow_value).
    """
    flow_value = edmonds_karp(network)
    s = network.source

    # BFS from s in the residual graph.
    S = {s}
    queue = deque([s])
    while queue:
        u = queue.popleft()
        for e in network.adj[u]:
            if e.residual_capacity() > 1e-12 and e.v not in S:
                S.add(e.v)
                queue.append(e.v)

    return S, flow_value


def verify_max_flow_min_cut(num_trials: int = 50, n: int = 8, seed: int = 0) -> bool:
    """Return True iff, on every random network, the extracted cut's capacity
    equals the max-flow value (and the sink is on the far side of the cut)."""
    for trial in range(num_trials):
        g = generate_flow_network(n, seed=seed + trial)
        S, value = min_cut(g)
        # The sink must NOT be reachable in the final residual graph.
        if g.sink in S:
            return False
        if abs(cut_capacity(g, S) - value) > 1e-9:
            return False
    return True


if __name__ == "__main__":
    G = FlowNetwork(source="s", sink="t")
    G.add_edge("s", "a", 3)
    G.add_edge("s", "b", 2)
    G.add_edge("a", "b", 1)
    G.add_edge("a", "t", 2)
    G.add_edge("b", "t", 3)
    S, value = min_cut(G)
    assert value == 5.0
    assert "s" in S and "t" not in S
    assert cut_capacity(G, S) == 5.0

    # Bottleneck network: min cut is the single edge a->t with capacity 1.
    G2 = FlowNetwork(source="s", sink="t")
    G2.add_edge("s", "a", 100)
    G2.add_edge("a", "t", 1)
    S2, v2 = min_cut(G2)
    assert v2 == 1.0
    assert S2 == {"s", "a"}  # reachable until the saturated a->t
    assert cut_capacity(G2, S2) == 1.0

    assert verify_max_flow_min_cut(num_trials=50, n=8, seed=0) is True
    assert verify_max_flow_min_cut(num_trials=30, n=12, seed=500) is True

    print("All tests passed!")
