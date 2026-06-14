"""
Problem 13 - Finding an Odd Cycle (Certificate of Non-Bipartiteness)
=======================================================================

Theorem (Kleinberg & Tardos): a graph is bipartite IFF it contains no odd
cycle. Problem 12 only tells you WHETHER a graph is bipartite; this problem
asks you to produce a CERTIFICATE when it is not -- an explicit odd cycle.

Implement `find_odd_cycle(adj)`:
  - If the graph is bipartite, return `None`.
  - Otherwise, return a list of vertices `[v0, v1, ..., vk, v0]` (first ==
    last) forming a cycle of ODD length `k+1` (i.e. `k+1` is odd, so there
    are an odd number of EDGES in the cycle).

Hint: run BFS 2-coloring (as in Problem 12) from each connected component's
start vertex, tracking each vertex's BFS-tree parent and distance from the
root. When you find an edge (u, v) where `color[u] == color[v]` (a
"same-color edge"), the path root->u, the edge u-v, and the path v->root
together form a cycle. Its length is `dist[u] + dist[v] + 1`. This is odd
exactly when `dist[u]` and `dist[v]` have the SAME parity (which they must,
since u and v have the same color, i.e. the same BFS-layer parity).

You can reconstruct the cycle by walking parent pointers from `u` back to the
root, and separately from `v` back to the root, then splicing the two paths
together at the root with the edge `(u, v)`.

See practical_exercises.pdf, Problem 13.
"""

import os
import sys
from collections import deque
from typing import List, Optional

_PARENT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, _PARENT)
sys.path.insert(0, os.path.join(_PARENT, "solutions"))

from solution_problem12 import is_bipartite
from starter_code import edges_to_adjacency_list


def find_odd_cycle(adj: List[List[int]]) -> Optional[List[int]]:
    """Return an odd-length cycle (list of vertices, first == last) if the
    graph is not bipartite, else None."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        # Triangle (3-cycle, odd): not bipartite
        c3 = edges_to_adjacency_list(3, [(0, 1), (1, 2), (0, 2)])
        cycle = find_odd_cycle(c3)
        assert cycle is not None
        assert cycle[0] == cycle[-1]
        assert (len(cycle) - 1) % 2 == 1
        for a, b in zip(cycle, cycle[1:]):
            assert b in c3[a]

        # 4-cycle (even): bipartite, no odd cycle
        c4 = edges_to_adjacency_list(4, [(0, 1), (1, 2), (2, 3), (0, 3)])
        assert find_odd_cycle(c4) is None
        assert is_bipartite(c4) is True

        # 5-cycle (odd): not bipartite
        c5 = edges_to_adjacency_list(5, [(i, (i + 1) % 5) for i in range(5)])
        cycle5 = find_odd_cycle(c5)
        assert cycle5 is not None
        assert (len(cycle5) - 1) % 2 == 1
        assert (len(cycle5) - 1) == 5  # the whole 5-cycle is the only cycle

        # Tree: no cycle at all
        tree = edges_to_adjacency_list(4, [(0, 1), (0, 2), (1, 3)])
        assert find_odd_cycle(tree) is None

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
