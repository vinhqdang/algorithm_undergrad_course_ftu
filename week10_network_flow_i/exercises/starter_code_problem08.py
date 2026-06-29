"""
Problem 08 - Extract the Minimum Cut from a Max Flow
======================================================

Implement ``min_cut(network)``: compute a maximum flow, then extract a minimum
cut. After the max flow is found, let S be the set of nodes reachable from the
source in the FINAL residual graph (BFS along edges with positive residual
capacity). Then (S, V\\S) is a minimum cut whose capacity equals the max-flow
value (Max-Flow Min-Cut theorem). Return ``(S, max_flow_value)``.

Also implement ``verify_max_flow_min_cut(num_trials, n, seed)`` returning True
iff, on every random network, the extracted cut's capacity equals the max-flow
value and the sink is NOT in S.

See practical_exercises.pdf, Problem 8, for the full statement and examples.
"""

import os
import sys
from typing import Hashable, Set, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import FlowNetwork, generate_flow_network

# from starter_code_problem02 import cut_capacity
# from starter_code_problem05 import edmonds_karp

Node = Hashable


def min_cut(network: FlowNetwork) -> Tuple[Set[Node], float]:
    """Compute a max flow, then extract a min cut (S, value)."""
    # TODO: implement this function.
    raise NotImplementedError


def verify_max_flow_min_cut(num_trials: int = 50, n: int = 8, seed: int = 0) -> bool:
    """Return True iff the extracted cut's capacity equals the max-flow value
    on every random network."""
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
        S, value = min_cut(G)
        assert value == 5.0
        assert "s" in S and "t" not in S

        G2 = FlowNetwork(source="s", sink="t")
        G2.add_edge("s", "a", 100)
        G2.add_edge("a", "t", 1)
        S2, v2 = min_cut(G2)
        assert v2 == 1.0
        assert S2 == {"s", "a"}

        assert verify_max_flow_min_cut(num_trials=50, n=8, seed=0) is True
        assert verify_max_flow_min_cut(num_trials=30, n=12, seed=500) is True

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
