"""
Problem 11 - Cycle Detection in an Undirected Graph (DFS)
============================================================

Implement `has_cycle_undirected(adj)`, which returns True iff the UNDIRECTED
graph given by adjacency list `adj` contains at least one cycle (in any
connected component).

Use DFS: for each unvisited vertex, run a DFS keeping track of each vertex's
PARENT in the DFS tree. If DFS encounters an edge to an already-visited
vertex that is NOT the current vertex's parent, that is a "back edge" and
indicates a cycle.

Important: in an adjacency list built from `edges_to_adjacency_list`, each
undirected edge (u, v) appears as `v` in `adj[u]` AND `u` in `adj[v]` -- so
when you are at `u` and see neighbor `v == parent[u]`, that is just the edge
you came from, NOT a cycle. Only treat it as a cycle if you encounter a
visited, non-parent neighbor (or, more simply: a self-loop, or a vertex
visited via a different edge).

Also implement `find_a_cycle(adj)`, which returns a list of vertices forming
one cycle (in order, e.g. `[a, b, c, a]` meaning the cycle a-b-c-a), or `None`
if the graph is acyclic (a forest).

See practical_exercises.pdf, Problem 11.
"""

import os
import sys
from typing import List, Optional

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import edges_to_adjacency_list


def has_cycle_undirected(adj: List[List[int]]) -> bool:
    """Return True iff the undirected graph contains a cycle."""
    # TODO: implement this function.
    raise NotImplementedError


def find_a_cycle(adj: List[List[int]]) -> Optional[List[int]]:
    """Return a list of vertices forming a cycle (first == last), or None if acyclic."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        # Tree (acyclic): 0-1, 0-2, 1-3
        tree = edges_to_adjacency_list(4, [(0, 1), (0, 2), (1, 3)])
        assert has_cycle_undirected(tree) is False
        assert find_a_cycle(tree) is None

        # Triangle: 0-1, 1-2, 0-2 (cycle)
        triangle = edges_to_adjacency_list(3, [(0, 1), (1, 2), (0, 2)])
        assert has_cycle_undirected(triangle) is True
        cycle = find_a_cycle(triangle)
        assert cycle is not None
        assert cycle[0] == cycle[-1]
        assert len(set(cycle[:-1])) == 3  # all 3 vertices appear

        # Disconnected: one acyclic component + one cyclic component
        mixed = edges_to_adjacency_list(5, [(0, 1), (2, 3), (3, 4), (2, 4)])
        assert has_cycle_undirected(mixed) is True  # {2,3,4} is a triangle

        # Disconnected, all acyclic (forest)
        forest = edges_to_adjacency_list(4, [(0, 1), (2, 3)])
        assert has_cycle_undirected(forest) is False

        # Single edge -> no cycle
        single_edge = edges_to_adjacency_list(2, [(0, 1)])
        assert has_cycle_undirected(single_edge) is False

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
