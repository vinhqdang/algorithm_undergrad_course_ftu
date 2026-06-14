"""
Problem 15 - Topological Sort via DFS
========================================

A TOPOLOGICAL ORDER of a directed graph is an ordering of its vertices such
that for every edge (u, v), `u` comes before `v` in the order. A directed
graph has a topological order IFF it is a DAG (no directed cycles).

Implement `topological_sort_dfs(adj)`:
  - If `adj` (a directed graph) contains a cycle, return `None`.
  - Otherwise, return a list of all vertices in a valid topological order.

Algorithm: run DFS from every unvisited vertex. When a vertex FINISHES
(all its descendants have been fully explored), prepend it to the result
list (or equivalently, append to a list and reverse at the end). This works
because a vertex finishes only after all vertices reachable from it have
finished, so it must come before them in topological order.

Implement `verify_topological_order(adj, order)`, returning True iff `order`
is a permutation of `range(len(adj))` such that for every edge (u, v) in
`adj`, `u` appears before `v` in `order`.

See practical_exercises.pdf, Problem 15.
"""

import os
import sys
from typing import List, Optional

_PARENT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, _PARENT)
sys.path.insert(0, os.path.join(_PARENT, "solutions"))

from solution_problem14 import has_cycle_directed
from starter_code import edges_to_adjacency_list


def topological_sort_dfs(adj: List[List[int]]) -> Optional[List[int]]:
    """Return a topological order of the DAG `adj`, or None if it has a cycle."""
    # TODO: implement this function.
    raise NotImplementedError


def verify_topological_order(adj: List[List[int]], order: List[int]) -> bool:
    """Return True iff `order` is a valid topological order of `adj`."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        # Classic example: 0 -> 1, 0 -> 2, 1 -> 3, 2 -> 3
        dag = edges_to_adjacency_list(4, [(0, 1), (0, 2), (1, 3), (2, 3)], directed=True)
        order = topological_sort_dfs(dag)
        assert order is not None
        assert sorted(order) == [0, 1, 2, 3]
        assert verify_topological_order(dag, order) is True

        # 0 must come before 1, 2, 3; 3 must come last.
        assert order.index(0) < order.index(1)
        assert order.index(0) < order.index(2)
        assert order.index(3) > order.index(1)
        assert order.index(3) > order.index(2)

        # Graph with a cycle: no topological order
        cyclic = edges_to_adjacency_list(3, [(0, 1), (1, 2), (2, 0)], directed=True)
        assert topological_sort_dfs(cyclic) is None
        assert has_cycle_directed(cyclic) is True

        # Single chain: 0 -> 1 -> 2 -> 3 (unique topological order)
        chain = edges_to_adjacency_list(4, [(0, 1), (1, 2), (2, 3)], directed=True)
        assert topological_sort_dfs(chain) == [0, 1, 2, 3]

        # Edges list with bad order should fail verification
        assert verify_topological_order(chain, [3, 2, 1, 0]) is False
        assert verify_topological_order(chain, [0, 1, 2, 3]) is True

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
