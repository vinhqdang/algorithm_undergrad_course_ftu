"""
Problem 16 - Topological Sort via Kahn's Algorithm (BFS + In-Degree Queue)
=============================================================================

Implement `topological_sort_kahn(adj)`, an alternative topological-sort
algorithm using a queue (continuity with BFS / Problem 4):

  1. Compute the in-degree of every vertex (number of incoming edges).
  2. Initialize a queue with all vertices of in-degree 0.
  3. Repeatedly dequeue a vertex `u`, append it to the result, and for each
     out-neighbor `v` of `u`, decrement `v`'s in-degree; if it becomes 0,
     enqueue `v`.
  4. If the result contains all `n` vertices, return it. Otherwise (some
     vertices never reached in-degree 0, because they're in a cycle), return
     `None`.

To make the result DETERMINISTIC (for testing), use a `collections.deque`
and, whenever multiple vertices simultaneously become available, enqueue them
in increasing order of vertex index; initialize the queue with in-degree-0
vertices in increasing order too.

Also implement `in_degrees(adj)`, returning a list `indeg` of length
`len(adj)` where `indeg[v]` is the number of edges (u, v) for any u.

See practical_exercises.pdf, Problem 16.
"""

import os
import sys
from collections import deque
from typing import List, Optional

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import edges_to_adjacency_list


def in_degrees(adj: List[List[int]]) -> List[int]:
    """Return the in-degree of every vertex."""
    # TODO: implement this function.
    raise NotImplementedError


def topological_sort_kahn(adj: List[List[int]]) -> Optional[List[int]]:
    """Return a topological order via Kahn's algorithm, or None if `adj` has a cycle."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        # 0 -> 1, 0 -> 2, 1 -> 3, 2 -> 3
        dag = edges_to_adjacency_list(4, [(0, 1), (0, 2), (1, 3), (2, 3)], directed=True)
        assert in_degrees(dag) == [0, 1, 1, 2]

        order = topological_sort_kahn(dag)
        assert order is not None
        # Deterministic: 0 first (only in-degree-0 vertex), then 1 and 2 (in
        # index order), then 3.
        assert order == [0, 1, 2, 3]

        # Cycle: 0 -> 1 -> 2 -> 0
        cyclic = edges_to_adjacency_list(3, [(0, 1), (1, 2), (2, 0)], directed=True)
        assert topological_sort_kahn(cyclic) is None
        assert in_degrees(cyclic) == [1, 1, 1]

        # Chain: 0 -> 1 -> 2 -> 3 (unique order)
        chain = edges_to_adjacency_list(4, [(0, 1), (1, 2), (2, 3)], directed=True)
        assert topological_sort_kahn(chain) == [0, 1, 2, 3]

        # Multiple independent chains: 0->1 and 2->3 (vertex order breaks ties)
        independent = edges_to_adjacency_list(4, [(0, 1), (2, 3)], directed=True)
        assert topological_sort_kahn(independent) == [0, 2, 1, 3]

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
