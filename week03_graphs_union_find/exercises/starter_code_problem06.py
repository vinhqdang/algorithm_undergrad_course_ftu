"""
Problem 06 - Connected Components via BFS
============================================

Implement `connected_components_bfs(adj)`, which takes an adjacency list of
an UNDIRECTED graph with `n = len(adj)` vertices and returns a list of
components, where each component is a sorted list of vertices.

Components should be ordered by their smallest vertex (i.e. process vertices
0, 1, 2, ... in order, starting a new BFS whenever you encounter an unvisited
vertex). Use BFS as the underlying traversal (you may reuse the BFS idea from
Problem 4, reimplemented here).

Also implement `num_components(adj)`, returning just the count.

See practical_exercises.pdf, Problem 6.
"""

from collections import deque
from typing import List


def connected_components_bfs(adj: List[List[int]]) -> List[List[int]]:
    """Return the connected components of an undirected graph, each sorted, in
    order of their smallest vertex."""
    # TODO: implement this function.
    raise NotImplementedError


def num_components(adj: List[List[int]]) -> int:
    """Return the number of connected components."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        # Two triangles: {0,1,2} and {3,4,5}
        adj = [
            [1, 2],     # 0
            [0, 2],     # 1
            [0, 1],     # 2
            [4, 5],     # 3
            [3, 5],     # 4
            [3, 4],     # 5
        ]
        comps = connected_components_bfs(adj)
        assert comps == [[0, 1, 2], [3, 4, 5]]
        assert num_components(adj) == 2

        # Fully connected graph -> 1 component
        path = [[1], [0, 2], [1, 3], [2]]
        assert num_components(path) == 1
        assert connected_components_bfs(path) == [[0, 1, 2, 3]]

        # All isolated vertices -> n components
        isolated = [[], [], []]
        assert num_components(isolated) == 3
        assert connected_components_bfs(isolated) == [[0], [1], [2]]

        # Single vertex
        assert num_components([[]]) == 1

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
