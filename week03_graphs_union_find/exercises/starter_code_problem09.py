"""
Problem 09 - Iterative DFS with an Explicit Stack
====================================================

Implement `dfs_iterative(adj, source)`, an ITERATIVE version of DFS using an
explicit stack (a Python list used with `append`/`pop`) instead of recursion.
Return the list of vertices in the order they are first visited (discovered),
exactly like `dfs_recursive` from Problem 8.

To match the recursive version's order (which visits `adj[u][0]` before
`adj[u][1]`, etc.), when you push multiple neighbors of `u` onto the stack at
once, push them in REVERSE order, so that the first neighbor is popped first.

Also implement `max_stack_size(adj, source)`, returning the maximum size the
explicit stack reaches during the traversal -- this gives a sense of the
O(V) auxiliary space DFS can use in the worst case (e.g. a path graph).

See practical_exercises.pdf, Problem 9.
"""

import os
import sys
from typing import List

_PARENT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, _PARENT)
sys.path.insert(0, os.path.join(_PARENT, "solutions"))

from solution_problem08 import dfs_recursive
from starter_code import edges_to_adjacency_list


def dfs_iterative(adj: List[List[int]], source: int) -> List[int]:
    """Return the DFS preorder (discovery order), computed iteratively."""
    # TODO: implement this function.
    raise NotImplementedError


def max_stack_size(adj: List[List[int]], source: int) -> int:
    """Return the maximum size reached by the explicit stack during dfs_iterative."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        # Path graph: 0 - 1 - 2 - 3
        path = edges_to_adjacency_list(4, [(0, 1), (1, 2), (2, 3)])
        assert dfs_iterative(path, 0) == dfs_recursive(path, 0) == [0, 1, 2, 3]

        # Tree: 0 -> [1, 2], 1 -> [3], 2 -> [], 3 -> []  (directed)
        tree = [[1, 2], [3], [], []]
        assert dfs_iterative(tree, 0) == dfs_recursive(tree, 0) == [0, 1, 3, 2]

        # Star graph: order should match the recursive version too
        star = [[1, 2, 3], [0], [0], [0]]
        assert dfs_iterative(star, 0) == dfs_recursive(star, 0)

        # On a path graph of length n, the stack never holds more than ~2
        # vertices at a time (each vertex has at most 1 unvisited neighbor
        # pushed at once, except the source).
        long_path = edges_to_adjacency_list(6, [(i, i + 1) for i in range(5)])
        assert max_stack_size(long_path, 0) <= 3

        # Disconnected graph: should only visit reachable component
        disconnected = edges_to_adjacency_list(4, [(0, 1), (2, 3)])
        assert set(dfs_iterative(disconnected, 0)) == {0, 1}

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
