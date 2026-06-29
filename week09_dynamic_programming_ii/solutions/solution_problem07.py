"""
Problem 07 - Bellman-Ford Negative-Cycle Detection (SOLUTION)
==============================================================
"""

from typing import List, Optional, Tuple

Edge = Tuple[int, int, float]


def find_negative_cycle(n: int, edges: List[Edge]) -> Optional[List[int]]:
    """Return a negative cycle [c0, ..., c0] if one exists, else None.

    Initialise all distances to 0 so every vertex acts as a potential source;
    after n-1 relaxation passes, one more pass that still relaxes an edge means
    a negative cycle is reachable.
    """
    dist = [0.0] * n
    parent: List[Optional[int]] = [None] * n

    x = -1
    for _ in range(n):
        x = -1
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                x = v
    if x == -1:
        return None  # no relaxation in the n-th pass => no negative cycle

    # Walk n parent steps to guarantee landing on the cycle.
    y = x
    for _ in range(n):
        y = parent[y]  # type: ignore[assignment]

    # Collect the cycle starting and ending at y.
    cycle = [y]
    cur = parent[y]
    while cur != y:
        cycle.append(cur)
        cur = parent[cur]  # type: ignore[assignment]
    cycle.append(y)
    cycle.reverse()
    return cycle


def _cycle_weight(edges: List[Edge], cycle: List[int]) -> float:
    weight = {}
    for u, v, w in edges:
        if (u, v) not in weight or w < weight[(u, v)]:
            weight[(u, v)] = w
    total = 0.0
    for a, b in zip(cycle, cycle[1:]):
        total += weight[(a, b)]
    return total


if __name__ == "__main__":
    # Simple 2-cycle with total weight -2
    cyc = find_negative_cycle(2, [(0, 1, 1), (1, 0, -3)])
    assert cyc is not None
    assert cyc[0] == cyc[-1]
    assert _cycle_weight([(0, 1, 1), (1, 0, -3)], cyc) < 0

    # No negative cycle
    assert find_negative_cycle(3, [(0, 1, 4), (0, 2, 5), (1, 2, -3)]) is None

    # 3-cycle with negative total
    edges = [(0, 1, 1), (1, 2, -3), (2, 0, 1)]
    cyc = find_negative_cycle(3, edges)
    assert cyc is not None and cyc[0] == cyc[-1]
    assert _cycle_weight(edges, cyc) < 0
    # All consecutive pairs are real edges
    edge_set = {(u, v) for u, v, _ in edges}
    assert all((a, b) in edge_set for a, b in zip(cyc, cyc[1:]))

    # Positive cycle: not negative -> None
    assert find_negative_cycle(3, [(0, 1, 1), (1, 2, 1), (2, 0, 1)]) is None

    print("All tests passed!")
