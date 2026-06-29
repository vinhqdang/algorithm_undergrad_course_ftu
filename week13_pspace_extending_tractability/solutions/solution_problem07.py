"""
Problem 07 - Maximum Independent Set on a Tree via DP (SOLUTION)
================================================================

On a tree, the maximum independent set is computable in linear time by a
post-order DP. For each vertex v, root the tree and define:

  incl[v] = 1 + sum over children c of excl[c]   (v in the set)
  excl[v] = sum over children c of max(incl[c], excl[c])  (v not in the set)

The answer is max(incl[root], excl[root]). We also reconstruct the set.
"""

import os
import sys
from typing import List, Set, Tuple

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import (  # noqa: E402
    brute_force_independent_set,
    edges_to_adj,
    generate_tree,
)

Edge = Tuple[int, int]


def max_independent_set_tree(n: int, edges: List[Edge]) -> Set[int]:
    """Return a maximum independent set of the tree (n, edges)."""
    if n == 0:
        return set()
    adj = edges_to_adj(n, edges)
    incl = [0] * n
    excl = [0] * n
    # Iterative post-order from root 0 to avoid recursion limits.
    root = 0
    parent = [-1] * n
    order: List[int] = []
    stack = [root]
    visited = [False] * n
    visited[root] = True
    while stack:
        v = stack.pop()
        order.append(v)
        for w in adj[v]:
            if not visited[w]:
                visited[w] = True
                parent[w] = v
                stack.append(w)

    # Process in reverse BFS/DFS order (children before parents).
    for v in reversed(order):
        incl[v] = 1
        excl[v] = 0
        for c in adj[v]:
            if c == parent[v]:
                continue
            incl[v] += excl[c]
            excl[v] += max(incl[c], excl[c])

    # Reconstruct: walk from root choosing include/exclude.
    chosen: Set[int] = set()
    # take[v] = True means we include v in the chosen set.
    decide = {root: incl[root] >= excl[root]}
    for v in order:
        take = decide[v]
        if take:
            chosen.add(v)
        for c in adj[v]:
            if c == parent[v]:
                continue
            if take:
                decide[c] = False  # parent included -> child excluded
            else:
                decide[c] = incl[c] >= excl[c]
    return chosen


def verify_tree_mis(num_trials: int, n: int, seed: int) -> bool:
    """Return True iff the DP size equals the brute-force optimum on random trees."""
    for trial in range(num_trials):
        nn, edges = generate_tree(n, seed=seed + trial)
        dp = max_independent_set_tree(nn, edges)
        bf = brute_force_independent_set(nn, edges)
        # Validate independence of the DP set, and matching size.
        for u, v in edges:
            if u in dp and v in dp:
                return False
        if len(dp) != len(bf):
            return False
    return True


if __name__ == "__main__":
    # Path 0-1-2-3-4: MIS size 3 (e.g. {0,2,4}).
    n, edges = 5, [(0, 1), (1, 2), (2, 3), (3, 4)]
    mis = max_independent_set_tree(n, edges)
    assert len(mis) == 3
    for u, v in edges:
        assert not (u in mis and v in mis)

    # Star with center 0: MIS is the 4 leaves.
    n, edges = 5, [(0, 1), (0, 2), (0, 3), (0, 4)]
    mis = max_independent_set_tree(n, edges)
    assert len(mis) == 4 and 0 not in mis

    # Single vertex.
    assert max_independent_set_tree(1, []) == {0}

    # Randomized verification against brute force.
    assert verify_tree_mis(num_trials=40, n=12, seed=7) is True
    assert verify_tree_mis(num_trials=20, n=16, seed=500) is True

    print("All tests passed!")
