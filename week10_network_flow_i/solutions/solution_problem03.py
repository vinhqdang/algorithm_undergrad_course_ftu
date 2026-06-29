"""
Problem 03 - Build the Residual Graph for a Given Flow (SOLUTION)
==================================================================
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
    """Return the residual graph of `network` under the assignment `flow`.

    For each original edge (u, v) with capacity c and flow f:
      * a *forward* residual edge u -> v with residual capacity c - f exists
        whenever c - f > 0 (we can still push more);
      * a *backward* residual edge v -> u with residual capacity f exists
        whenever f > 0 (we can cancel/undo flow already pushed).

    The result is an adjacency dict mapping each node to a list of
    (neighbour, residual_capacity) pairs, omitting zero-capacity residual
    edges. Parallel residual edges between the same pair are summed.
    """
    residual: Dict[Node, Dict[Node, float]] = {u: {} for u in network.nodes()}

    for (u, v), cap in network.capacity.items():
        f = flow.get((u, v), 0.0)
        forward_res = cap - f
        backward_res = f
        if forward_res > 1e-12:
            residual[u][v] = residual[u].get(v, 0.0) + forward_res
        if backward_res > 1e-12:
            residual[v][u] = residual[v].get(u, 0.0) + backward_res

    return {u: sorted(nbrs.items()) for u, nbrs in residual.items()}


if __name__ == "__main__":
    G = FlowNetwork(source="s", sink="t")
    G.add_edge("s", "a", 3)
    G.add_edge("a", "t", 3)

    # No flow yet: residual graph equals the original (forward only).
    res0 = build_residual_graph(G, {})
    assert res0["s"] == [("a", 3.0)]
    assert res0["a"] == [("t", 3.0)]
    assert res0["t"] == []

    # Push 2 units along s->a->t.
    flow = {("s", "a"): 2, ("a", "t"): 2}
    res = build_residual_graph(G, flow)
    # s->a has 1 forward residual left; a->s has 2 backward residual.
    assert dict(res["s"]) == {"a": 1.0}
    assert dict(res["a"]) == {"s": 2.0, "t": 1.0}
    assert dict(res["t"]) == {"a": 2.0}

    # Saturate the edge: only backward residual remains.
    flow_full = {("s", "a"): 3, ("a", "t"): 3}
    res_full = build_residual_graph(G, flow_full)
    assert dict(res_full["s"]) == {}            # s->a saturated, no forward
    assert dict(res_full["a"]) == {"s": 3.0}    # only backward a->s
    assert dict(res_full["t"]) == {"a": 3.0}

    print("All tests passed!")
