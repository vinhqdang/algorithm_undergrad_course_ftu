"""
Problem 03 - Greedy Set Cover
==============================

A Set Cover instance is a `universe` (a set of elements) and a list `subsets`
of sets whose union is the universe. Implement `greedy_set_cover(universe,
subsets)`: repeatedly pick the subset covering the MOST currently-uncovered
elements, until everything is covered. Return the list of chosen subset INDICES
in the order chosen.

See practical_exercises.pdf, Problem 3.
"""

from typing import List, Set


def greedy_set_cover(universe: Set, subsets: List[Set]) -> List[int]:
    """Greedily cover the most uncovered elements; return chosen subset indices."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        universe = {1, 2, 3, 4, 5}
        subsets = [{1, 2, 3}, {2, 4}, {3, 4}, {4, 5}]
        chosen = greedy_set_cover(universe, subsets)
        assert chosen == [0, 3]
        covered = set().union(*(subsets[i] for i in chosen))
        assert covered == universe

        assert greedy_set_cover({1, 2}, [{1, 2}]) == [0]

        U = set(range(1, 7))
        S = [{1, 2, 3, 4, 5, 6}, {1, 2, 3}, {4, 5, 6}]
        assert greedy_set_cover(U, S) == [0]

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
