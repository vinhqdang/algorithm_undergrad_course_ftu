"""
Problem 08 - Hamiltonian Cycle by Backtracking (SOLUTION)
==========================================================
"""

from typing import FrozenSet, Iterable, List, Optional, Set, Tuple

Edge = FrozenSet[int]
Graph = Tuple[int, Set[Edge]]


def make_graph(n: int, edge_list: Iterable[Tuple[int, int]]) -> Graph:
    edges: Set[Edge] = set()
    for u, v in edge_list:
        if u != v:
            edges.add(frozenset({u, v}))
    return (n, edges)


def verify_hamiltonian_cycle(graph: Graph, cycle: List[int]) -> bool:
    """Return True iff `cycle` (vertices, no repeated start at the end) visits
    every vertex exactly once and consecutive vertices -- including the wrap
    from last back to first -- are joined by edges."""
    n, edges = graph
    if len(cycle) != n:
        return False
    if set(cycle) != set(range(n)):
        return False
    if n == 0:
        return True
    if n == 1:
        # a single vertex: a Hamiltonian "cycle" requires a self-loop, which we
        # do not model; treat as non-Hamiltonian.
        return False
    for i in range(n):
        u = cycle[i]
        v = cycle[(i + 1) % n]
        if frozenset({u, v}) not in edges:
            return False
    return True


def find_hamiltonian_cycle(graph: Graph) -> Optional[List[int]]:
    """Backtracking search for a Hamiltonian cycle starting at vertex 0."""
    n, edges = graph
    if n == 0:
        return []
    if n == 1:
        return None

    def adjacent(u: int, v: int) -> bool:
        return frozenset({u, v}) in edges

    path = [0]
    visited = [False] * n
    visited[0] = True

    def backtrack() -> bool:
        if len(path) == n:
            return adjacent(path[-1], 0)  # close the cycle back to start
        last = path[-1]
        for nxt in range(n):
            if not visited[nxt] and adjacent(last, nxt):
                visited[nxt] = True
                path.append(nxt)
                if backtrack():
                    return True
                path.pop()
                visited[nxt] = False
        return False

    if backtrack():
        return list(path)
    return None


if __name__ == "__main__":
    # 4-cycle: has a Hamiltonian cycle
    c4 = make_graph(4, [(0, 1), (1, 2), (2, 3), (3, 0)])
    cyc = find_hamiltonian_cycle(c4)
    assert cyc is not None
    assert verify_hamiltonian_cycle(c4, cyc)

    # Path 0-1-2-3 (no edge 3-0): no Hamiltonian cycle
    path = make_graph(4, [(0, 1), (1, 2), (2, 3)])
    assert find_hamiltonian_cycle(path) is None

    # K4: has a Hamiltonian cycle
    k4 = make_graph(4, [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)])
    cyc = find_hamiltonian_cycle(k4)
    assert cyc is not None and verify_hamiltonian_cycle(k4, cyc)

    # Verifier rejects a non-cycle ordering
    assert verify_hamiltonian_cycle(c4, [0, 2, 1, 3]) is False  # 0-2 not an edge
    assert verify_hamiltonian_cycle(c4, [0, 1, 2]) is False     # wrong length

    # Two disconnected triangles: no Hamiltonian cycle
    two = make_graph(6, [(0, 1), (1, 2), (0, 2), (3, 4), (4, 5), (3, 5)])
    assert find_hamiltonian_cycle(two) is None

    print("All tests passed!")
