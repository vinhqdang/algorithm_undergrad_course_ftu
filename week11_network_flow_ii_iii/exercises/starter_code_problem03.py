"""
Problem 03 - Maximum Bipartite Matching via Max-Flow Reduction
===============================================================

Implement `flow_matching(left, right, edges)` using the standard max-flow
reduction: source -> each left vertex (cap 1), each edge left -> right (cap 1),
each right vertex -> sink (cap 1). The saturated left->right edges form a
maximum matching. Return that list of matched (left, right) edges.

Also implement `flow_matching_size(...)`. The whole point of this exercise is to
confirm the flow-based result agrees with Kuhn's algorithm (Problem 2).

Use the `MaxFlow` helper from starter_code.py.

See practical_exercises.pdf, Problem 3, for the full statement and examples.
"""

import os
import sys
from typing import Hashable, List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "solutions"))

from starter_code import MaxFlow, generate_bipartite_graph
from solution_problem02 import kuhn_matching  # reference, for cross-checking

Vertex = Hashable
Edge = Tuple[Vertex, Vertex]


def flow_matching(
    left: List[Vertex], right: List[Vertex], edges: List[Edge]
) -> List[Edge]:
    """Maximum bipartite matching via the max-flow reduction (returns edges)."""
    # TODO: implement this function using MaxFlow.
    raise NotImplementedError


def flow_matching_size(
    left: List[Vertex], right: List[Vertex], edges: List[Edge]
) -> int:
    """Size of a maximum matching computed via max flow."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        for seed in range(40):
            left, right, edges = generate_bipartite_graph(5, 5, p=0.4, seed=seed)
            assert flow_matching_size(left, right, edges) == len(kuhn_matching(left, right, edges))

        left, right, edges = generate_bipartite_graph(6, 6, p=0.5, seed=7)
        matching = flow_matching(left, right, edges)
        seen_left, seen_right = set(), set()
        for u, v in matching:
            assert u not in seen_left and v not in seen_right
            seen_left.add(u)
            seen_right.add(v)

        for seed in range(20):
            left, right, edges = generate_bipartite_graph(3, 7, p=0.5, seed=seed + 100)
            assert flow_matching_size(left, right, edges) == len(kuhn_matching(left, right, edges))

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
