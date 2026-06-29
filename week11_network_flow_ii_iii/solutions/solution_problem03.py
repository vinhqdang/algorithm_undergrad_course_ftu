"""
Problem 03 - Maximum Bipartite Matching via Max-Flow Reduction (SOLUTION)
=========================================================================
"""

import os
import sys
from typing import Dict, Hashable, List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import MaxFlow, generate_bipartite_graph
from solution_problem02 import kuhn_matching

Vertex = Hashable
Edge = Tuple[Vertex, Vertex]


def flow_matching(
    left: List[Vertex], right: List[Vertex], edges: List[Edge]
) -> List[Edge]:
    """Maximum bipartite matching via the standard max-flow reduction.

    Build a unit-capacity network: source s -> each left vertex (cap 1),
    each edge left -> right (cap 1), each right vertex -> sink t (cap 1).
    The value of the max s-t flow equals the size of a maximum matching, and
    the saturated left->right edges form the matching.
    """
    mf = MaxFlow()
    s, t = "__source__", "__sink__"
    for u in left:
        mf.add_edge(s, ("left", u), 1)
    for v in right:
        mf.add_edge(("right", v), t, 1)
    for u, v in edges:
        mf.add_edge(("left", u), ("right", v), 1)

    mf.max_flow(s, t)

    matching: List[Edge] = []
    for u, v in edges:
        if mf.flow(("left", u), ("right", v)) > 0.5:
            matching.append((u, v))
    return matching


def flow_matching_size(
    left: List[Vertex], right: List[Vertex], edges: List[Edge]
) -> int:
    """Size of a maximum matching computed via max flow."""
    return len(flow_matching(left, right, edges))


if __name__ == "__main__":
    # On many random bipartite graphs, the flow-based size must equal Kuhn's.
    for seed in range(40):
        left, right, edges = generate_bipartite_graph(5, 5, p=0.4, seed=seed)
        flow_size = flow_matching_size(left, right, edges)
        kuhn_size = len(kuhn_matching(left, right, edges))
        assert flow_size == kuhn_size, (seed, flow_size, kuhn_size)

    # The returned matching must be a genuine matching (no shared endpoints).
    left, right, edges = generate_bipartite_graph(6, 6, p=0.5, seed=7)
    matching = flow_matching(left, right, edges)
    seen_left = set()
    seen_right = set()
    for u, v in matching:
        assert u not in seen_left and v not in seen_right
        seen_left.add(u)
        seen_right.add(v)

    # Unbalanced sides.
    for seed in range(20):
        left, right, edges = generate_bipartite_graph(3, 7, p=0.5, seed=seed + 100)
        assert flow_matching_size(left, right, edges) == len(kuhn_matching(left, right, edges))

    print("All tests passed!")
