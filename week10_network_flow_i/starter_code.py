"""
Week 10 - Network Flow I (Maximum Flow and Minimum Cut)
=======================================================

Shared utilities used by the practical exercise problems
(starter_code_problem01.py ... starter_code_problem12.py).

You do not need to modify this file. Import what you need, e.g.:

    from starter_code import FlowNetwork, generate_flow_network

Conventions
-----------
- A "flow network" is a directed graph with a distinguished *source* ``s`` and
  *sink* ``t``. Every directed edge ``(u, v)`` carries a non-negative integer
  *capacity*. Nodes are arbitrary hashable labels (we use ints by default).
- A "flow" is a dict mapping each directed edge ``(u, v)`` (one that appears in
  the network) to a non-negative number ``f(u, v) <= capacity(u, v)``, subject
  to *conservation*: for every node other than ``s`` and ``t``, the total flow
  in equals the total flow out.
- The *value* of a flow is the net flow leaving the source ``s`` (equivalently,
  the net flow entering the sink ``t``).
- An "s-t cut" ``(S, T)`` is a partition of the nodes with ``s`` in ``S`` and
  ``t`` in ``T``. Its *capacity* is the sum of capacities of edges going from
  ``S`` to ``T``.
- The residual graph is represented with explicit edge objects that carry a
  ``capacity``, a current ``flow``, and a pointer to a paired *reverse* edge,
  so that pushing flow along an edge automatically updates residual capacity in
  both directions (the standard Ford-Fulkerson adjacency representation).
- Random instances are generated with Python's ``random.Random(seed)`` so that
  results are reproducible across runs.
"""

from __future__ import annotations

import random
from typing import Dict, Hashable, List, Optional, Set, Tuple

Node = Hashable
Edge = Tuple[Node, Node]


class FlowEdge:
    """A single directed edge in a residual-graph adjacency representation.

    Each "real" edge ``u -> v`` with capacity ``c`` is stored together with a
    paired *reverse* edge ``v -> u`` with capacity ``0``. Pushing ``d`` units of
    flow along this edge does ``flow += d`` here and ``flow -= d`` on the reverse
    edge, so the *residual capacity* (``capacity - flow``) of each direction is
    always kept consistent.
    """

    __slots__ = ("u", "v", "capacity", "flow", "reverse")

    def __init__(self, u: Node, v: Node, capacity: float) -> None:
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0.0
        self.reverse: "FlowEdge" = None  # set when the paired edge is created

    def residual_capacity(self) -> float:
        """Remaining capacity that can still be pushed along this edge."""
        return self.capacity - self.flow

    def push(self, amount: float) -> None:
        """Push `amount` units along this edge (and -amount on the reverse)."""
        self.flow += amount
        self.reverse.flow -= amount

    def __repr__(self) -> str:  # pragma: no cover - debugging aid only
        return f"FlowEdge({self.u!r}->{self.v!r}, cap={self.capacity}, flow={self.flow})"


class FlowNetwork:
    """A directed flow network with explicit residual-edge adjacency.

    Usage::

        G = FlowNetwork(source="s", sink="t")
        G.add_edge("s", "a", 3)
        G.add_edge("a", "t", 2)
        value = G.edmonds_karp()  # see Problem 5

    The adjacency list ``G.adj[u]`` is a list of ``FlowEdge`` objects leaving
    ``u`` (including the zero-capacity reverse edges that make the residual
    graph explicit).
    """

    def __init__(self, source: Node = "s", sink: Node = "t") -> None:
        self.source = source
        self.sink = sink
        self.adj: Dict[Node, List[FlowEdge]] = {}
        # Remember capacities of the *original* (forward) edges, keyed by (u, v),
        # so callers can ask "what was the capacity of this edge?" cheaply.
        self.capacity: Dict[Edge, float] = {}

    # -- graph construction ------------------------------------------------

    def add_node(self, u: Node) -> None:
        """Ensure node `u` exists in the adjacency structure."""
        if u not in self.adj:
            self.adj[u] = []

    def add_edge(self, u: Node, v: Node, capacity: float) -> FlowEdge:
        """Add a directed edge u -> v with the given capacity.

        Also creates the paired zero-capacity reverse edge v -> u used by the
        residual graph. Returns the forward FlowEdge.
        """
        self.add_node(u)
        self.add_node(v)
        forward = FlowEdge(u, v, capacity)
        backward = FlowEdge(v, u, 0.0)
        forward.reverse = backward
        backward.reverse = forward
        self.adj[u].append(forward)
        self.adj[v].append(backward)
        self.capacity[(u, v)] = self.capacity.get((u, v), 0.0) + capacity
        return forward

    # -- introspection -----------------------------------------------------

    def nodes(self) -> List[Node]:
        """Return a list of all nodes in the network."""
        return list(self.adj.keys())

    def forward_edges(self) -> List[FlowEdge]:
        """Return all *original* (positive-capacity) forward edges."""
        return [e for u in self.adj for e in self.adj[u] if e.capacity > 0]

    def reset_flow(self) -> None:
        """Set the flow on every edge back to zero."""
        for u in self.adj:
            for e in self.adj[u]:
                e.flow = 0.0

    def value(self) -> float:
        """Net flow leaving the source under the current edge flows."""
        return sum(e.flow for e in self.adj.get(self.source, []) if e.capacity > 0)

    def copy(self) -> "FlowNetwork":
        """Return a fresh FlowNetwork with the same nodes and edge capacities
        (and zero flow), built only from the original forward edges."""
        g = FlowNetwork(self.source, self.sink)
        for u in self.adj:
            g.add_node(u)
        for e in self.forward_edges():
            g.add_edge(e.u, e.v, e.capacity)
        return g

    # -- a reference max-flow implementation -------------------------------
    #
    # Provided so the *non-algorithm* problems (cuts, residual graphs,
    # matching reductions, ...) can obtain a correct max flow without each
    # re-implementing Edmonds-Karp. Problems 5 and 6 ask you to write your
    # own; this one is just a dependable utility.

    def edmonds_karp(self) -> float:
        """Compute the maximum s-t flow with the Edmonds-Karp (BFS) rule.

        Mutates the edge flows in place and returns the max-flow value.
        """
        from collections import deque

        self.reset_flow()
        s, t = self.source, self.sink
        if s == t:
            return 0.0
        max_flow = 0.0
        while True:
            # BFS for a shortest augmenting path in the residual graph.
            parent_edge: Dict[Node, FlowEdge] = {s: None}
            queue = deque([s])
            while queue:
                u = queue.popleft()
                if u == t:
                    break
                for e in self.adj[u]:
                    if e.residual_capacity() > 1e-12 and e.v not in parent_edge:
                        parent_edge[e.v] = e
                        queue.append(e.v)
            if t not in parent_edge:
                break  # no augmenting path: current flow is maximum
            # Find the bottleneck residual capacity along the path.
            bottleneck = float("inf")
            v = t
            while v != s:
                e = parent_edge[v]
                bottleneck = min(bottleneck, e.residual_capacity())
                v = e.u
            # Push the bottleneck along the path.
            v = t
            while v != s:
                e = parent_edge[v]
                e.push(bottleneck)
                v = e.u
            max_flow += bottleneck
        return max_flow


# -- random instance generation -------------------------------------------


def generate_flow_network(
    n: int,
    seed: int | None = None,
    max_capacity: int = 10,
    edge_prob: float = 0.45,
) -> FlowNetwork:
    """Generate a random *acyclic* integer-capacity flow network on `n` nodes.

    Node ``0`` is the source and node ``n-1`` is the sink. Edges only go from a
    lower-numbered node to a higher-numbered node (guaranteeing acyclicity and
    that the sink is reachable-in-principle), each present with probability
    ``edge_prob`` and given an integer capacity in ``[1, max_capacity]``.

    To avoid degenerate instances, the source always has at least one outgoing
    edge and the sink always has at least one incoming edge.
    """
    rng = random.Random(seed)
    s, t = 0, n - 1
    g = FlowNetwork(source=s, sink=t)
    for i in range(n):
        g.add_node(i)
    for u in range(n):
        for v in range(u + 1, n):
            if rng.random() < edge_prob:
                g.add_edge(u, v, rng.randint(1, max_capacity))
    # Guarantee the source has an out-edge and the sink has an in-edge.
    if not any(e.capacity > 0 for e in g.adj[s]):
        v = rng.randint(1, n - 1)
        g.add_edge(s, v, rng.randint(1, max_capacity))
    if not any(e.capacity > 0 for u in g.adj for e in g.adj[u] if e.v == t):
        u = rng.randint(0, n - 2)
        g.add_edge(u, t, rng.randint(1, max_capacity))
    return g


def generate_bipartite_graph(
    left: int,
    right: int,
    seed: int | None = None,
    edge_prob: float = 0.4,
) -> List[Tuple[int, int]]:
    """Generate random bipartite edges between `left` and `right` vertices.

    Returns a list of ``(u, v)`` pairs with ``0 <= u < left`` and
    ``0 <= v < right``; each possible pair is present with probability
    ``edge_prob``.
    """
    rng = random.Random(seed)
    edges = []
    for u in range(left):
        for v in range(right):
            if rng.random() < edge_prob:
                edges.append((u, v))
    return edges


# -- small flow utilities -------------------------------------------------


def edges_of(network: FlowNetwork) -> Dict[Edge, float]:
    """Return a dict mapping each original edge (u, v) to its capacity."""
    return dict(network.capacity)


def flow_value_from_assignment(
    flow: Dict[Edge, float], source: Node, network: FlowNetwork
) -> float:
    """Net flow leaving `source` for an externally supplied flow assignment."""
    out_flow = sum(f for (u, _), f in flow.items() if u == source)
    in_flow = sum(f for (_, v), f in flow.items() if v == source)
    return out_flow - in_flow


def neighbors_with_residual(network: FlowNetwork, u: Node) -> List[Node]:
    """Nodes reachable from `u` along an edge with positive residual capacity."""
    return [e.v for e in network.adj[u] if e.residual_capacity() > 1e-12]


if __name__ == "__main__":
    # A tiny smoke test of the shared utilities.
    G = FlowNetwork(source="s", sink="t")
    G.add_edge("s", "a", 3)
    G.add_edge("s", "b", 2)
    G.add_edge("a", "b", 1)
    G.add_edge("a", "t", 2)
    G.add_edge("b", "t", 3)
    assert G.edmonds_karp() == 5.0
    rng_net = generate_flow_network(8, seed=1)
    assert rng_net.source == 0 and rng_net.sink == 7
    assert rng_net.edmonds_karp() >= 0
    print("starter_code self-test passed!")
