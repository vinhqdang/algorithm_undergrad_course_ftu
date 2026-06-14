"""
Problem 04 - BFS Distances and Layers (SOLUTION)
==================================================
"""

from collections import deque
from typing import List


def bfs_distances(adj: List[List[int]], source: int) -> List[int]:
    """Return shortest-path distances (in edges) from source, or -1 if unreachable."""
    n = len(adj)
    dist = [-1] * n
    dist[source] = 0
    queue = deque([source])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.append(v)
    return dist


def bfs_layers(adj: List[List[int]], source: int) -> List[List[int]]:
    """Return BFS layers: layers[d] is the list of vertices at distance d from source."""
    n = len(adj)
    dist = [-1] * n
    dist[source] = 0
    queue = deque([source])
    layers: List[List[int]] = [[source]]
    while queue:
        current_layer = []
        for _ in range(len(queue)):
            u = queue.popleft()
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    current_layer.append(v)
                    queue.append(v)
        if current_layer:
            layers.append(current_layer)
    return layers


if __name__ == "__main__":
    adj = [[1], [0, 2], [1, 3], [2, 4], [3]]
    dist = bfs_distances(adj, 0)
    assert dist == [0, 1, 2, 3, 4]

    layers = bfs_layers(adj, 0)
    assert layers == [[0], [1], [2], [3], [4]]

    star = [[1, 2, 3], [0], [0], [0], []]
    dist_star = bfs_distances(star, 0)
    assert dist_star == [0, 1, 1, 1, -1]

    layers_star = bfs_layers(star, 0)
    assert layers_star == [[0], [1, 2, 3]]

    disconnected = [[1], [0], [3], [2]]
    dist_disc = bfs_distances(disconnected, 0)
    assert dist_disc == [0, 1, -1, -1]

    dist_isolated = bfs_distances(star, 4)
    assert dist_isolated == [-1, -1, -1, -1, 0]

    print("All tests passed!")
