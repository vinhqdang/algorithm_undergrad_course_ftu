"""
Problem 03 - Greedy Set Cover (SOLUTION)
=========================================
"""

from typing import List, Set


def greedy_set_cover(universe: Set, subsets: List[Set]) -> List[int]:
    """Repeatedly pick the subset covering the most uncovered elements.

    Returns the list of chosen subset indices, in the order chosen.
    """
    uncovered = set(universe)
    chosen: List[int] = []
    while uncovered:
        best_idx = -1
        best_gain = -1
        for i, s in enumerate(subsets):
            gain = len(s & uncovered)
            if gain > best_gain:
                best_gain = gain
                best_idx = i
        if best_gain <= 0:
            # No subset can cover any remaining element; universe is not coverable.
            raise ValueError("subsets do not cover the universe")
        chosen.append(best_idx)
        uncovered -= subsets[best_idx]
    return chosen


if __name__ == "__main__":
    universe = {1, 2, 3, 4, 5}
    subsets = [{1, 2, 3}, {2, 4}, {3, 4}, {4, 5}]
    chosen = greedy_set_cover(universe, subsets)
    # First picks index 0 (covers 3 elements), then index 3 (covers {4,5}).
    assert chosen == [0, 3]
    covered = set().union(*(subsets[i] for i in chosen))
    assert covered == universe

    # Single set covering everything.
    assert greedy_set_cover({1, 2}, [{1, 2}]) == [0]

    # Classic tie-broken example: greedy may use more sets than optimal.
    U = set(range(1, 7))
    S = [{1, 2, 3, 4, 5, 6}, {1, 2, 3}, {4, 5, 6}]
    chosen = greedy_set_cover(U, S)
    assert chosen == [0]  # the big set wins immediately

    print("All tests passed!")
