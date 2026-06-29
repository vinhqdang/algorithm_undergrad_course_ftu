"""
Problem 11 - Iterative-Deepening DFS on a State Space (SOLUTION)
================================================================

IDDFS performs a series of depth-limited DFS searches with increasing limits,
combining DFS's low memory use with BFS's optimality (shortest solution in
number of moves). We apply it to a small sliding puzzle (the 8-puzzle on a
3x3 board, or smaller) and return a solution path of states.
"""

from typing import List, Optional, Tuple

State = Tuple[int, ...]  # flattened board; 0 is the blank


def neighbors(state: State, side: int) -> List[State]:
    """Return the states reachable by sliding one tile into the blank (0)."""
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
    """Return a shortest solution path (list of states from start to goal),
    or None if no solution within ``max_depth`` moves."""
    if start == goal:
        return [start]

    def dls(state, goal, depth, path, visited):
        if state == goal:
            return list(path)
        if depth == 0:
            return None
        for nxt in neighbors(state, side):
            if nxt in visited:
                continue
            visited.add(nxt)
            path.append(nxt)
            res = dls(nxt, goal, depth - 1, path, visited)
            if res is not None:
                return res
            path.pop()
            visited.discard(nxt)
        return None

    for limit in range(1, max_depth + 1):
        visited = {start}
        res = dls(start, goal, limit, [start], visited)
        if res is not None:
            return res
    return None


if __name__ == "__main__":
    # 2x2 puzzle (3 tiles + blank). Goal is (1,2,3,0).
    goal = (1, 2, 3, 0)

    # Already solved.
    assert iddfs(goal, goal, side=2) == [goal]

    # One move away: blank and tile 3 swapped.
    start = (1, 2, 0, 3)
    path = iddfs(start, goal, side=2)
    assert path is not None
    assert path[0] == start and path[-1] == goal
    assert len(path) == 2  # start + goal -> one move

    # A scrambled 2x2: rotate. Solution should be the shortest path.
    start = (2, 0, 1, 3)
    path = iddfs(start, goal, side=2)
    assert path is not None and path[0] == start and path[-1] == goal
    # Each consecutive pair differs by a legal slide.
    for a, b in zip(path, path[1:]):
        assert b in neighbors(a, 2)

    # 3x3 puzzle, a few moves from solved.
    goal3 = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    start3 = (1, 2, 3, 4, 5, 6, 7, 0, 8)  # one move
    path = iddfs(start3, goal3, side=3, max_depth=20)
    assert path is not None and path[-1] == goal3 and len(path) == 2

    print("All tests passed!")
