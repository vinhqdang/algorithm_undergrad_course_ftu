"""
Problem 09 - Baseball Elimination via Max Flow
===============================================

Implement `is_eliminated(teams, wins, remaining, games_between, x)`: decide
whether team `x` is eliminated (cannot possibly finish in first place).

Let W = wins[x] + remaining[x] be the most wins x can finish with. If any other
team already has wins[i] > W, x is trivially eliminated. Otherwise build a flow
network (Kleinberg-Tardos Section 7.12):

  source -> game node {i,j}      capacity = games left between i and j
  game node {i,j} -> team i, j   capacity = infinity
  team i -> sink                 capacity = W - wins[i]

x can still finish first iff the max flow saturates all game-source edges
(all remaining games among other teams can be distributed without any team
exceeding W). Otherwise x is eliminated.

`games_between` is keyed by unordered pairs given as `tuple(sorted((i, j), key=str))`.

Use the `MaxFlow` helper from starter_code.py.

See practical_exercises.pdf, Problem 9, for the full statement and examples.
"""

import os
import sys
from itertools import combinations
from typing import Dict, Hashable, List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import MaxFlow

Team = Hashable


def is_eliminated(
    teams: List[Team],
    wins: Dict[Team, int],
    remaining: Dict[Team, int],
    games_between: Dict[Tuple[Team, Team], int],
    x: Team,
) -> bool:
    """Decide whether team `x` is eliminated (cannot possibly finish first)."""
    # TODO: implement this function using MaxFlow.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        teams = ["NY", "Bal", "Bos", "Tor"]
        wins = {"NY": 90, "Bal": 88, "Bos": 87, "Tor": 86}
        remaining = {"NY": 11, "Bal": 13, "Bos": 12, "Tor": 13}
        games = {
            tuple(sorted(("NY", "Bal"), key=str)): 1,
            tuple(sorted(("NY", "Bos"), key=str)): 6,
            tuple(sorted(("NY", "Tor"), key=str)): 4,
            tuple(sorted(("Bal", "Bos"), key=str)): 1,
            tuple(sorted(("Bal", "Tor"), key=str)): 5,
            tuple(sorted(("Bos", "Tor"), key=str)): 1,
        }
        assert is_eliminated(teams, wins, remaining, games, "NY") is False

        teams2 = ["A", "B", "C"]
        wins2 = {"A": 10, "B": 10, "C": 2}
        remaining2 = {"A": 0, "B": 0, "C": 5}
        games2 = {tuple(sorted(("A", "B"), key=str)): 0,
                  tuple(sorted(("A", "C"), key=str)): 0,
                  tuple(sorted(("B", "C"), key=str)): 5}
        assert is_eliminated(teams2, wins2, remaining2, games2, "C") is True

        teams3 = ["A", "B"]
        wins3 = {"A": 5, "B": 5}
        remaining3 = {"A": 3, "B": 3}
        games3 = {tuple(sorted(("A", "B"), key=str)): 3}
        assert is_eliminated(teams3, wins3, remaining3, games3, "A") is False

        teams4 = ["A", "B", "C"]
        wins4 = {"A": 100, "B": 1, "C": 1}
        remaining4 = {"A": 0, "B": 1, "C": 1}
        games4 = {tuple(sorted(("B", "C"), key=str)): 1}
        assert is_eliminated(teams4, wins4, remaining4, games4, "A") is False

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
