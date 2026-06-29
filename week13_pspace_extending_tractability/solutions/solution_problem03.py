"""
Problem 03 - Alpha-Beta Pruning (SOLUTION)
===========================================

Alpha-beta pruning computes the SAME value as plain minimax (Problem 2) while
visiting fewer leaves. We return both the value and a leaf-visit count so the
test can confirm equality of values and a reduction in visited leaves.
"""

import math


def minimax_count(node, maximizing: bool = True):
    """Plain minimax; returns (value, leaves_visited)."""
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
    if not isinstance(node, list):
        return node, 1
    visited = 0
    if maximizing:
        value = -math.inf
        for child in node:
            v, c = alphabeta(child, False, alpha, beta)
            visited += c
            value = max(value, v)
            alpha = max(alpha, value)
            if alpha >= beta:
                break  # beta cut-off
        return value, visited
    value = math.inf
    for child in node:
        v, c = alphabeta(child, True, alpha, beta)
        visited += c
        value = min(value, v)
        beta = min(beta, value)
        if beta <= alpha:
            break  # alpha cut-off
    return value, visited


if __name__ == "__main__":
    trees = [
        [[3, 5], [2, 9]],
        [
            [[3, 12, 8], [2, 4, 6]],
            [[14, 5, 2], [3, 3]],
        ],
        # Classic textbook tree where pruning is dramatic.
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
            # Same value as plain minimax.
            assert ab_val == mm_val, (ab_val, mm_val)
            # Never visits MORE leaves than plain minimax.
            assert ab_visited <= mm_visited
            total_mm += mm_visited
            total_ab += ab_visited

    # Overall, alpha-beta should visit strictly fewer leaves.
    assert total_ab < total_mm, (total_ab, total_mm)

    print("All tests passed!")
