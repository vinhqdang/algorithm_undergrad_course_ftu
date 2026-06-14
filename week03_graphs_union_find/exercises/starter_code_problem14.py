"""
Problem 14 - Cycle Detection in a Directed Graph (DFS with Colors)
=====================================================================

Implement `has_cycle_directed(adj)`, which returns True iff the DIRECTED
graph given by adjacency list `adj` (adj[u] = out-neighbors of u) contains a
directed cycle.

Use the classic 3-color DFS:
  - WHITE (0): not yet visited.
  - GRAY (1): currently on the DFS recursion stack (an ancestor of the
    current vertex).
  - BLACK (2): fully finished (popped off the stack).

A directed graph has a cycle IFF DFS ever encounters an edge to a GRAY
vertex (a "back edge" to an ancestor). Edges to BLACK vertices ("forward" or
"cross" edges) do NOT indicate a cycle.

Also implement `find_a_directed_cycle(adj)`, returning a list of vertices
`[v0, v1, ..., vk, v0]` forming a directed cycle (each consecutive pair, and
the last->first pair, must be an edge in `adj`), or `None` if the graph is
acyclic (a DAG).

See practical_exercises.pdf, Problem 14.
"""

import os
import sys
from typing import List, Optional

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import edges_to_adjacency_list


def has_cycle_directed(adj: List[List[int]]) -> bool:
    """Return True iff the directed graph contains a directed cycle."""
    # TODO: implement this function.
    raise NotImplementedError


def find_a_directed_cycle(adj: List[List[int]]) -> Optional[List[int]]:
    """Return a directed cycle (list of vertices, first == last), or None if acyclic."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        # DAG: 0 -> 1 -> 2, 0 -> 2
        dag = edges_to_adjacency_list(3, [(0, 1), (1, 2), (0, 2)], directed=True)
        assert has_cycle_directed(dag) is False
        assert find_a_directed_cycle(dag) is None

        # Directed cycle: 0 -> 1 -> 2 -> 0
        cycle_graph = edges_to_adjacency_list(3, [(0, 1), (1, 2), (2, 0)], directed=True)
        assert has_cycle_directed(cycle_graph) is True
        cyc = find_a_directed_cycle(cycle_graph)
        assert cyc is not None
        assert cyc[0] == cyc[-1]
        for a, b in zip(cyc, cyc[1:]):
            assert b in cycle_graph[a]

        # Self-loop is a cycle of length 1
        self_loop = edges_to_adjacency_list(2, [(0, 0), (0, 1)], directed=True)
        assert has_cycle_directed(self_loop) is True

        # "Diamond" DAG: 0 -> 1, 0 -> 2, 1 -> 3, 2 -> 3 (no cycle, even though
        # vertex 3 is reached via two different paths -- this is a cross/
        # forward edge situation, not a cycle).
        diamond = edges_to_adjacency_list(4, [(0, 1), (0, 2), (1, 3), (2, 3)], directed=True)
        assert has_cycle_directed(diamond) is False

        # Disconnected: acyclic component + cyclic component
        mixed = [[1], [], [3], [2]]  # 0->1 (acyclic), 2->3->2 (cycle)
        assert has_cycle_directed(mixed) is True

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
