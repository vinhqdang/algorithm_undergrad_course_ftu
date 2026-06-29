"""
Problem 03 - Alpha-Beta Pruning
================================

Implement `alphabeta(node, maximizing, alpha, beta)` returning
``(value, leaves_visited)``. It must compute the SAME value as plain minimax
(provided here as `minimax_count`) while visiting no more leaves -- and, on
the test trees overall, strictly fewer.

Alpha is the best value the maximizer can already guarantee; beta the best the
minimizer can guarantee. Prune (break out of the loop) when alpha >= beta.

See practical_exercises.pdf, Problem 3.
"""

import math


def minimax_count(node, maximizing: bool = True):
    """Plain minimax; returns (value, leaves_visited). Provided for comparison."""
    if not isinstance(node, list):
        return node, 1
    visited = 0
    if maximizing:
        best = -math.inf
        for child in node:
            v, c = minimax_count(child, False)
            visited += c
            best = max(best, v)
        return best, visited
    best = math.inf
    for child in node:
        v, c = minimax_count(child, True)
        visited += c
        best = min(best, v)
    return best, visited


def alphabeta(node, maximizing: bool = True, alpha=-math.inf, beta=math.inf):
    """Alpha-beta search; returns (value, leaves_visited)."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        trees = [
            [[3, 5], [2, 9]],
            [
                [[3, 12, 8], [2, 4, 6]],
                [[14, 5, 2], [3, 3]],
            ],
            [
                [[5, 6], [7, 4, 5]],
                [[3], [6, 6, 9], [7]],
                [[5], [9, 8], [6]],
            ],
        ]
        total_mm = 0
        total_ab = 0
        for t in trees:
            for maximizing in (True, False):
                mm_val, mm_visited = minimax_count(t, maximizing)
                ab_val, ab_visited = alphabeta(t, maximizing)
                assert ab_val == mm_val
                assert ab_visited <= mm_visited
                total_mm += mm_visited
                total_ab += ab_visited
        assert total_ab < total_mm

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
