"""
Problem 02 - Cut Capacity
===========================

Given a flow network and an s-t cut described by a set ``S`` (which must contain
the source and not the sink), compute the capacity of the cut (S, T) where
T = V \\ S.

The cut capacity is the sum of capacities of edges going FROM a node in S TO a
node in T. Edges that go from T back into S do NOT contribute.

See practical_exercises.pdf, Problem 2, for the full statement and examples.
"""

import os
import sys
from typing import Hashable, Set

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import FlowNetwork

Node = Hashable


def cut_capacity(network: FlowNetwork, S: Set[Node]) -> float:
    """Return the capacity of the s-t cut (S, V\\S)."""
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

        assert cut_capacity(G, {"s"}) == 5.0
        assert cut_capacity(G, {"s", "a"}) == 5.0
        assert cut_capacity(G, {"s", "a", "b"}) == 5.0

        G2 = FlowNetwork(source="s", sink="t")
        G2.add_edge("s", "a", 10)
        G2.add_edge("a", "t", 1)
        assert cut_capacity(G2, {"s"}) == 10.0
        assert cut_capacity(G2, {"s", "a"}) == 1.0

        try:
            cut_capacity(G, {"a"})
            assert False
        except ValueError:
            pass
        try:
            cut_capacity(G, {"s", "t"})
            assert False
        except ValueError:
            pass

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
