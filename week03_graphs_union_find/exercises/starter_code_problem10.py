"""
Problem 10 - Connected Components via DFS
=============================================

Implement `connected_components_dfs(adj)`, the DFS analogue of Problem 6:
given an adjacency list of an UNDIRECTED graph, return a list of components
(each a sorted list of vertices), ordered by smallest vertex, using DFS
instead of BFS as the underlying traversal.

Then implement `same_component(adj, u, v)`, returning True iff `u` and `v`
are in the same connected component.

Finally, implement `is_connected(adj)`, returning True iff the WHOLE graph
is a single connected component (or has 0 or 1 vertices).

Note: for an undirected graph, the SET of vertices visited from a given
start does not depend on whether you use BFS or DFS -- only the discovery
ORDER differs. So `connected_components_dfs` should return the same
PARTITION of vertices as `connected_components_bfs` from Problem 6 (though
your code should not import Problem 6 -- implement DFS directly).

See practical_exercises.pdf, Problem 10.
"""

from typing import List


def connected_components_dfs(adj: List[List[int]]) -> List[List[int]]:
    """Return the connected components of an undirected graph, each sorted, in
    order of their smallest vertex, using DFS."""
    # TODO: implement this function.
    raise NotImplementedError


def same_component(adj: List[List[int]], u: int, v: int) -> bool:
    """Return True iff u and v are in the same connected component."""
    # TODO: implement this function.
    raise NotImplementedError


def is_connected(adj: List[List[int]]) -> bool:
    """Return True iff the graph is a single connected component."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        # Two triangles: {0,1,2} and {3,4,5}
        adj = [
            [1, 2],
            [0, 2],
            [0, 1],
            [4, 5],
            [3, 5],
            [3, 4],
        ]
        comps = connected_components_dfs(adj)
        assert comps == [[0, 1, 2], [3, 4, 5]]

        assert same_component(adj, 0, 2) is True
        assert same_component(adj, 0, 3) is False
        assert is_connected(adj) is False

        # Fully connected path
        path = [[1], [0, 2], [1, 3], [2]]
        assert is_connected(path) is True
        assert same_component(path, 0, 3) is True

        # Single vertex / empty-ish graphs
        assert is_connected([[]]) is True
        assert is_connected([]) is True

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
