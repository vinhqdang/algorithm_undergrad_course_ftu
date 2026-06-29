"""
Problem 03 - Build the Residual Graph for a Given Flow
========================================================

Given a flow network and a flow assignment, build the residual graph.

For each original edge (u, v) with capacity c and flow f:
  * a FORWARD residual edge u -> v with residual capacity c - f exists whenever
    c - f > 0 (we can still push more), and
  * a BACKWARD residual edge v -> u with residual capacity f exists whenever
    f > 0 (we can cancel flow already pushed).

Return an adjacency dict mapping each node to a SORTED list of
(neighbour, residual_capacity) pairs, omitting zero-capacity residual edges.

See practical_exercises.pdf, Problem 3, for the full statement and examples.
"""

import os
import sys
from typing import Dict, Hashable, List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import FlowNetwork

Node = Hashable
Edge = Tuple[Node, Node]


def build_residual_graph(
    network: FlowNetwork, flow: Dict[Edge, float]
) -> Dict[Node, List[Tuple[Node, float]]]:
    """Return the residual graph of `network` under the assignment `flow`."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        G = FlowNetwork(source="s", sink="t")
        G.add_edge("s", "a", 3)
        G.add_edge("a", "t", 3)

        res0 = build_residual_graph(G, {})
        assert res0["s"] == [("a", 3.0)]
        assert res0["a"] == [("t", 3.0)]
        assert res0["t"] == []

        flow = {("s", "a"): 2, ("a", "t"): 2}
        res = build_residual_graph(G, flow)
        assert dict(res["s"]) == {"a": 1.0}
        assert dict(res["a"]) == {"s": 2.0, "t": 1.0}
        assert dict(res["t"]) == {"a": 2.0}

        flow_full = {("s", "a"): 3, ("a", "t"): 3}
        res_full = build_residual_graph(G, flow_full)
        assert dict(res_full["s"]) == {}
        assert dict(res_full["a"]) == {"s": 3.0}
        assert dict(res_full["t"]) == {"a": 3.0}

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
