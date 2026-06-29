"""
Problem 01 - Flow Feasibility Checker (SOLUTION)
==================================================
"""

import os
import sys
from typing import Dict, Hashable, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import FlowNetwork

Node = Hashable
Edge = Tuple[Node, Node]


def verify_flow(network: FlowNetwork, flow: Dict[Edge, float], tol: float = 1e-9):
    """Verify a flow assignment and return (is_valid, value).

    `flow` maps each original edge (u, v) to the flow on it. The flow is valid
    iff (1) every edge satisfies 0 <= flow <= capacity, and (2) flow is
    conserved at every node other than the source and sink. Returns
    (True, value) when valid, (False, 0.0) otherwise.
    """
    s, t = network.source, network.sink

    # (1) Capacity constraints: 0 <= flow(e) <= capacity(e) for each edge.
    for edge, cap in network.capacity.items():
        f = flow.get(edge, 0.0)
        if f < -tol or f > cap + tol:
            return False, 0.0
    # Any edge in `flow` that is not an edge of the network is illegal.
    for edge in flow:
        if edge not in network.capacity:
            return False, 0.0

    # (2) Conservation at internal nodes: inflow == outflow.
    inflow: Dict[Node, float] = {u: 0.0 for u in network.nodes()}
    outflow: Dict[Node, float] = {u: 0.0 for u in network.nodes()}
    for (u, v), f in flow.items():
        outflow[u] += f
        inflow[v] += f
    for u in network.nodes():
        if u == s or u == t:
            continue
        if abs(inflow[u] - outflow[u]) > tol:
            return False, 0.0

    value = outflow[s] - inflow[s]
    return True, value


if __name__ == "__main__":
    G = FlowNetwork(source="s", sink="t")
    G.add_edge("s", "a", 3)
    G.add_edge("s", "b", 2)
    G.add_edge("a", "b", 1)
    G.add_edge("a", "t", 2)
    G.add_edge("b", "t", 3)

    # A valid flow of value 4.
    good = {("s", "a"): 2, ("s", "b"): 2, ("a", "t"): 2, ("b", "t"): 2}
    ok, val = verify_flow(G, good)
    assert ok is True and abs(val - 4.0) < 1e-9, (ok, val)

    # A valid flow of value 5 (the maximum).
    good_max = {("s", "a"): 3, ("s", "b"): 2, ("a", "b"): 1, ("a", "t"): 2, ("b", "t"): 3}
    ok, val = verify_flow(G, good_max)
    assert ok is True and abs(val - 5.0) < 1e-9, (ok, val)

    # Violates a capacity constraint.
    bad_cap = {("s", "a"): 4, ("a", "t"): 4}
    ok, _ = verify_flow(G, bad_cap)
    assert ok is False

    # Violates conservation at node 'a' (3 in, 2 out).
    bad_cons = {("s", "a"): 3, ("a", "t"): 2}
    ok, _ = verify_flow(G, bad_cons)
    assert ok is False

    # An edge that does not exist in the network.
    bad_edge = {("s", "t"): 1}
    ok, _ = verify_flow(G, bad_edge)
    assert ok is False

    # The zero flow is valid and has value 0.
    ok, val = verify_flow(G, {})
    assert ok is True and abs(val) < 1e-9

    print("All tests passed!")
