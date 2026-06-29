"""
Problem 04 - BFS for an Augmenting Path in the Residual Graph (SOLUTION)
=========================================================================
"""

import os
import sys
from collections import deque
from typing import Hashable, List, Optional

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import FlowNetwork

Node = Hashable


def bfs_augmenting_path(network: FlowNetwork) -> Optional[List[Node]]:
    """Find a shortest (fewest-edges) augmenting path in the residual graph.

    Uses the *current edge flows* stored in `network` to determine residual
    capacities (an edge is usable iff its residual capacity is positive).
    Returns the path as a list of nodes [s, ..., t], or None if the sink is
    unreachable in the residual graph (i.e. the current flow is maximum).
    """
    s, t = network.source, network.sink
    if s == t:
        return [s]
    parent: dict = {s: None}
    queue = deque([s])
    while queue:
        u = queue.popleft()
        if u == t:
            break
        for e in network.adj[u]:
            if e.residual_capacity() > 1e-12 and e.v not in parent:
                parent[e.v] = u
                queue.append(e.v)
    if t not in parent:
        return None
    # Reconstruct the path from t back to s.
    path = []
    v = t
    while v is not None:
        path.append(v)
        v = parent[v]
    path.reverse()
    return path


if __name__ == "__main__":
    G = FlowNetwork(source="s", sink="t")
    G.add_edge("s", "a", 3)
    G.add_edge("a", "t", 3)

    # On the zero flow there is a path s -> a -> t.
    path = bfs_augmenting_path(G)
    assert path == ["s", "a", "t"], path

    # BFS finds a SHORTEST path. Add a longer alternative; the direct 2-hop
    # path should still be returned.
    G2 = FlowNetwork(source="s", sink="t")
    G2.add_edge("s", "a", 1)
    G2.add_edge("a", "t", 1)      # 2-hop path s-a-t
    G2.add_edge("s", "b", 1)
    G2.add_edge("b", "c", 1)
    G2.add_edge("c", "t", 1)      # 3-hop path s-b-c-t
    p2 = bfs_augmenting_path(G2)
    assert p2 == ["s", "a", "t"], p2  # shortest

    # Saturate s->a->t so no residual forward path remains there. Locate the
    # forward edges by their endpoints (adj lists also contain reverse edges).
    edge_sa = next(e for e in G.adj["s"] if e.v == "a" and e.capacity > 0)
    edge_at = next(e for e in G.adj["a"] if e.v == "t" and e.capacity > 0)
    edge_sa.push(3)
    edge_at.push(3)
    assert bfs_augmenting_path(G) is None  # sink unreachable now

    # Trivial network where source == sink.
    G3 = FlowNetwork(source="x", sink="x")
    G3.add_node("x")
    assert bfs_augmenting_path(G3) == ["x"]

    print("All tests passed!")
