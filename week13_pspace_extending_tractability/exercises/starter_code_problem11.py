"""
Problem 11 - Iterative-Deepening DFS on a State Space
======================================================

Implement `iddfs(start, goal, side, max_depth)` returning a SHORTEST solution
path (a list of states from ``start`` to ``goal`` inclusive) for a sliding
puzzle, or None if no solution within ``max_depth`` moves.

A state is a flattened tuple of a ``side`` x ``side`` board; 0 is the blank.
`neighbors(state, side)` (provided) returns the states reachable by one slide.

IDDFS runs depth-limited DFS with limit = 1, 2, 3, ... until the goal is found;
the first limit that succeeds yields a shortest path. Track visited states on
the current path to avoid cycles.

See practical_exercises.pdf, Problem 11.
"""

from typing import List, Optional, Tuple

State = Tuple[int, ...]


def neighbors(state: State, side: int) -> List[State]:
    """Return states reachable by sliding one tile into the blank (0); provided."""
    z = state.index(0)
    r, c = divmod(z, side)
    result = []
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < side and 0 <= nc < side:
            nz = nr * side + nc
            lst = list(state)
            lst[z], lst[nz] = lst[nz], lst[z]
            result.append(tuple(lst))
    return result


def iddfs(start: State, goal: State, side: int, max_depth: int = 40) -> Optional[List[State]]:
    """Return a shortest solution path from start to goal, or None."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        goal = (1, 2, 3, 0)
        assert iddfs(goal, goal, side=2) == [goal]

        start = (1, 2, 0, 3)
        path = iddfs(start, goal, side=2)
        assert path is not None
        assert path[0] == start and path[-1] == goal
        assert len(path) == 2

        start = (2, 0, 1, 3)
        path = iddfs(start, goal, side=2)
        assert path is not None and path[0] == start and path[-1] == goal
        for a, b in zip(path, path[1:]):
            assert b in neighbors(a, 2)

        goal3 = (1, 2, 3, 4, 5, 6, 7, 8, 0)
        start3 = (1, 2, 3, 4, 5, 6, 7, 0, 8)
        path = iddfs(start3, goal3, side=3, max_depth=20)
        assert path is not None and path[-1] == goal3 and len(path) == 2

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
