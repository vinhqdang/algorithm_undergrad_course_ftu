"""
Problem 17 - Counting Topological Orderings & Uniqueness
============================================================

A DAG can have MANY valid topological orderings. This problem asks you to
count them (for small DAGs) and relate uniqueness to the graph's structure.

Implement `count_topological_orders(adj)`, which returns the TOTAL number of
distinct topological orderings of the DAG `adj`, using backtracking:
  - At each step, the "available" vertices are those not yet placed whose
    in-degree (counting only edges from not-yet-placed vertices) is 0.
  - Try placing each available vertex next, recurse, then undo.
  - Base case: all vertices placed -> count 1 ordering.

(For graphs where `adj` has a cycle, return 0 -- there are no topological
orderings.)

Then implement `has_unique_topological_order(adj)`, returning True iff
`count_topological_orders(adj) == 1`.

Theorem connection: a DAG has a UNIQUE topological order iff it contains a
Hamiltonian path (a path visiting every vertex exactly once) that is
consistent with the edges -- equivalently, iff for every pair of
"adjacent-in-the-order" vertices there is a direct edge between them. A
"total order" DAG (0->1->2->...->(n-1) plus possibly extra edges, but no
"gaps") has a unique topological order; if any two vertices are
INCOMPARABLE (no path between them in either direction), there are multiple
valid orderings.

See practical_exercises.pdf, Problem 17.
"""

import os
import sys
from typing import List

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import edges_to_adjacency_list


def count_topological_orders(adj: List[List[int]]) -> int:
    """Return the total number of distinct topological orderings of `adj`."""
    # TODO: implement this function.
    raise NotImplementedError


def has_unique_topological_order(adj: List[List[int]]) -> bool:
    """Return True iff `adj` has exactly one topological ordering."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        # Total order: 0 -> 1 -> 2 -> 3 (unique ordering)
        chain = edges_to_adjacency_list(4, [(0, 1), (1, 2), (2, 3)], directed=True)
        assert count_topological_orders(chain) == 1
        assert has_unique_topological_order(chain) is True

        # No edges at all on 3 vertices: any permutation works -> 3! = 6
        empty = [[], [], []]
        assert count_topological_orders(empty) == 6
        assert has_unique_topological_order(empty) is False

        # "Diamond": 0 -> 1, 0 -> 2, 1 -> 3, 2 -> 3.
        # Valid orders: 0,1,2,3 and 0,2,1,3 -> count = 2
        diamond = edges_to_adjacency_list(4, [(0, 1), (0, 2), (1, 3), (2, 3)], directed=True)
        assert count_topological_orders(diamond) == 2
        assert has_unique_topological_order(diamond) is False

        # Two independent chains: 0->1 and 2->3.
        # Orderings: interleavings of {0,1} (in order) and {2,3} (in order)
        # = C(4,2) = 6
        independent = edges_to_adjacency_list(4, [(0, 1), (2, 3)], directed=True)
        assert count_topological_orders(independent) == 6

        # Cycle: no valid topological order
        cyclic = edges_to_adjacency_list(3, [(0, 1), (1, 2), (2, 0)], directed=True)
        assert count_topological_orders(cyclic) == 0
        assert has_unique_topological_order(cyclic) is False

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
