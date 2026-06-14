"""
Problem 06 - Connected Components via BFS (SOLUTION)
=======================================================
"""

from collections import deque
from typing import List


def connected_components_bfs(adj: List[List[int]]) -> List[List[int]]:
    """Return the connected components of an undirected graph, each sorted, in
    order of their smallest vertex."""
    n = len(adj)
    visited = [False] * n
    components: List[List[int]] = []

    for start in range(n):
        if visited[start]:
            continue
        component = []
        visited[start] = True
        queue = deque([start])
        while queue:
            u = queue.popleft()
            component.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
        components.append(sorted(component))

    return components


def num_components(adj: List[List[int]]) -> int:
    """Return the number of connected components."""
    return len(connected_components_bfs(adj))


if __name__ == "__main__":
    adj = [
        [1, 2],
        [0, 2],
        [0, 1],
        [4, 5],
        [3, 5],
        [3, 4],
    ]
    comps = connected_components_bfs(adj)
    assert comps == [[0, 1, 2], [3, 4, 5]]
    assert num_components(adj) == 2

    path = [[1], [0, 2], [1, 3], [2]]
    assert num_components(path) == 1
    assert connected_components_bfs(path) == [[0, 1, 2, 3]]

    isolated = [[], [], []]
    assert num_components(isolated) == 3
    assert connected_components_bfs(isolated) == [[0], [1], [2]]

    assert num_components([[]]) == 1

    print("All tests passed!")
