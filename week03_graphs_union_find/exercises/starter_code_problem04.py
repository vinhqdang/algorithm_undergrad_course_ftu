"""
Problem 04 - BFS Distances and Layers
=======================================

Implement `bfs_distances(adj, source)`, which runs Breadth-First Search from
`source` on a graph given as an adjacency list `adj` (list of length n,
`adj[u]` is the list of neighbors of u; the graph may be directed or
undirected -- BFS does not care).

Return a list `dist` of length `len(adj)` where:
  - `dist[source] == 0`
  - `dist[v]` is the length (number of edges) of the SHORTEST path from
    `source` to `v`, for every `v` reachable from `source`.
  - `dist[v] == -1` for every `v` NOT reachable from `source`.

Also implement `bfs_layers(adj, source)`, which returns a list of "layers":
`layers[0] == [source]`, `layers[1]` is all vertices at distance 1, etc.
(within each layer, vertices should appear in the order they were first
discovered).

See practical_exercises.pdf, Problem 4.
"""

from collections import deque
from typing import List


def bfs_distances(adj: List[List[int]], source: int) -> List[int]:
    """Return shortest-path distances (in edges) from source, or -1 if unreachable."""
    # TODO: implement this function.
    raise NotImplementedError


def bfs_layers(adj: List[List[int]], source: int) -> List[List[int]]:
    """Return BFS layers: layers[d] is the list of vertices at distance d from source."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        # Path graph: 0 - 1 - 2 - 3 - 4
        adj = [[1], [0, 2], [1, 3], [2, 4], [3]]
        dist = bfs_distances(adj, 0)
        assert dist == [0, 1, 2, 3, 4]

        layers = bfs_layers(adj, 0)
        assert layers == [[0], [1], [2], [3], [4]]

        # Star graph: 0 connected to 1, 2, 3; 4 is isolated
        star = [[1, 2, 3], [0], [0], [0], []]
        dist_star = bfs_distances(star, 0)
        assert dist_star == [0, 1, 1, 1, -1]

        layers_star = bfs_layers(star, 0)
        assert layers_star == [[0], [1, 2, 3]]

        # Disconnected graph: two components {0,1} and {2,3}
        disconnected = [[1], [0], [3], [2]]
        dist_disc = bfs_distances(disconnected, 0)
        assert dist_disc == [0, 1, -1, -1]

        # BFS from an isolated vertex
        dist_isolated = bfs_distances(star, 4)
        assert dist_isolated == [-1, -1, -1, -1, 0]

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
