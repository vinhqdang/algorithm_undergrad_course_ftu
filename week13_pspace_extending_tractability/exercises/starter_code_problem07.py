"""
Problem 07 - Maximum Independent Set on a Tree via DP
======================================================

Implement `max_independent_set_tree(n, edges)` returning a MAXIMUM independent
set of a tree in linear time, via a post-order DP rooted at vertex 0:

  incl[v] = 1 + sum over children c of excl[c]            (v in the set)
  excl[v] = sum over children c of max(incl[c], excl[c])  (v not in the set)

The optimum size is max(incl[root], excl[root]); reconstruct the actual set by
walking down from the root (if a vertex is included, all children are excluded).

Also implement `verify_tree_mis(num_trials, n, seed)` confirming the DP size
matches ``brute_force_independent_set`` on random trees (``generate_tree``).

See practical_exercises.pdf, Problem 7.
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
    # TODO: implement this function.
    raise NotImplementedError


def verify_tree_mis(num_trials: int, n: int, seed: int) -> bool:
    """Return True iff the DP size equals brute force on random trees."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        n, edges = 5, [(0, 1), (1, 2), (2, 3), (3, 4)]
        mis = max_independent_set_tree(n, edges)
        assert len(mis) == 3
        for u, v in edges:
            assert not (u in mis and v in mis)

        n, edges = 5, [(0, 1), (0, 2), (0, 3), (0, 4)]
        mis = max_independent_set_tree(n, edges)
        assert len(mis) == 4 and 0 not in mis

        assert max_independent_set_tree(1, []) == {0}

        assert verify_tree_mis(num_trials=40, n=12, seed=7) is True
        assert verify_tree_mis(num_trials=20, n=16, seed=500) is True

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
