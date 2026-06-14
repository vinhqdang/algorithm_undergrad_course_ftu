"""
Problem 10 - Connected Components via DFS (SOLUTION)
========================================================
"""

from typing import List


def connected_components_dfs(adj: List[List[int]]) -> List[List[int]]:
    """Return the connected components of an undirected graph, each sorted, in
    order of their smallest vertex, using DFS."""
    n = len(adj)
    visited = [False] * n
    components: List[List[int]] = []

    for start in range(n):
        if visited[start]:
            continue
        component = []
        stack = [start]
        visited[start] = True
        while stack:
            u = stack.pop()
            component.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)
        components.append(sorted(component))

    return components


def same_component(adj: List[List[int]], u: int, v: int) -> bool:
    """Return True iff u and v are in the same connected component."""
    for component in connected_components_dfs(adj):
        comp_set = set(component)
        if u in comp_set and v in comp_set:
            return True
        if u in comp_set or v in comp_set:
            return False
    return False


def is_connected(adj: List[List[int]]) -> bool:
    """Return True iff the graph is a single connected component."""
    if len(adj) <= 1:
        return True
    return len(connected_components_dfs(adj)) == 1


if __name__ == "__main__":
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

    path = [[1], [0, 2], [1, 3], [2]]
    assert is_connected(path) is True
    assert same_component(path, 0, 3) is True

    assert is_connected([[]]) is True
    assert is_connected([]) is True

    print("All tests passed!")
