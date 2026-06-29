"""
Problem 02 - Cut Capacity (SOLUTION)
======================================
"""

import os
import sys
from typing import Hashable, Set

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import FlowNetwork

Node = Hashable


def cut_capacity(network: FlowNetwork, S: Set[Node]) -> float:
    """Return the capacity of the s-t cut (S, T), where T = V \\ S.

    `S` must contain the source and not the sink. The cut capacity is the sum
    of capacities of edges going FROM a node in S TO a node in T (edges from T
    to S do not count).
    """
    if network.source not in S:
        raise ValueError("the source must be in S")
    if network.sink in S:
        raise ValueError("the sink must not be in S")

    total = 0.0
    for (u, v), cap in network.capacity.items():
        if u in S and v not in S:
            total += cap
    return total


if __name__ == "__main__":
    G = FlowNetwork(source="s", sink="t")
    G.add_edge("s", "a", 3)
    G.add_edge("s", "b", 2)
    G.add_edge("a", "b", 1)
    G.add_edge("a", "t", 2)
    G.add_edge("b", "t", 3)

    # Cut S = {s}: edges s->a (3) and s->b (2) cross, total 5.
    assert cut_capacity(G, {"s"}) == 5.0

    # Cut S = {s, a}: crossing edges are a->b (1), a->t (2), s->b (2); a->? and
    # note s->a is internal to S so it does NOT cross. Total = 1 + 2 + 2 = 5.
    assert cut_capacity(G, {"s", "a"}) == 5.0

    # Cut S = {s, a, b}: crossing edges are a->t (2) and b->t (3). Total 5.
    assert cut_capacity(G, {"s", "a", "b"}) == 5.0

    # The minimum cut here has capacity 5 (= max flow); all the above happen to
    # equal 5 in this small symmetric example. A larger cut:
    G2 = FlowNetwork(source="s", sink="t")
    G2.add_edge("s", "a", 10)
    G2.add_edge("a", "t", 1)
    assert cut_capacity(G2, {"s"}) == 10.0       # s->a
    assert cut_capacity(G2, {"s", "a"}) == 1.0    # a->t (the min cut)

    # Errors for malformed cuts.
    try:
        cut_capacity(G, {"a"})  # source not in S
        assert False
    except ValueError:
        pass
    try:
        cut_capacity(G, {"s", "t"})  # sink in S
        assert False
    except ValueError:
        pass

    print("All tests passed!")
