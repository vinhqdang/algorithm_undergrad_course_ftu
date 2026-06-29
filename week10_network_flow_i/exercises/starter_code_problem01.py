"""
Problem 01 - Flow Feasibility Checker
=======================================

Given a flow network and a candidate flow assignment, verify that the
assignment is a valid flow, and return its value.

`flow` maps each original edge (u, v) to the amount of flow on it. The flow is
*valid* iff:
  (1) every edge satisfies 0 <= flow(u, v) <= capacity(u, v) (capacity
      constraints), and
  (2) at every node other than the source and sink, total flow IN equals total
      flow OUT (flow conservation).

Return ``(True, value)`` when the flow is valid, where `value` is the net flow
leaving the source; return ``(False, 0.0)`` otherwise.

See practical_exercises.pdf, Problem 1, for the full statement and examples.
"""

import os
import sys
from typing import Dict, Hashable, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import FlowNetwork

Node = Hashable
Edge = Tuple[Node, Node]


def verify_flow(network: FlowNetwork, flow: Dict[Edge, float], tol: float = 1e-9):
    """Verify a flow assignment and return (is_valid, value)."""
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

        good = {("s", "a"): 2, ("s", "b"): 2, ("a", "t"): 2, ("b", "t"): 2}
        ok, val = verify_flow(G, good)
        assert ok is True and abs(val - 4.0) < 1e-9, (ok, val)

        good_max = {("s", "a"): 3, ("s", "b"): 2, ("a", "b"): 1, ("a", "t"): 2, ("b", "t"): 3}
        ok, val = verify_flow(G, good_max)
        assert ok is True and abs(val - 5.0) < 1e-9, (ok, val)

        bad_cap = {("s", "a"): 4, ("a", "t"): 4}
        assert verify_flow(G, bad_cap)[0] is False

        bad_cons = {("s", "a"): 3, ("a", "t"): 2}
        assert verify_flow(G, bad_cons)[0] is False

        bad_edge = {("s", "t"): 1}
        assert verify_flow(G, bad_edge)[0] is False

        ok, val = verify_flow(G, {})
        assert ok is True and abs(val) < 1e-9

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
