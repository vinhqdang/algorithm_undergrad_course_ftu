"""
Problem 09 - Baseball Elimination via Max Flow (SOLUTION)
==========================================================
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
    """Decide whether team ``x`` is eliminated (cannot possibly finish first).

    Model (Kleinberg-Tardos Section 7.12): let W = wins[x] + remaining[x] be the
    most wins x can finish with. For every other team i, if wins[i] > W, x is
    trivially eliminated. Otherwise build a flow network:

      source -> (game node {i,j}) with capacity g_ij  (games left between i, j)
      game node {i,j} -> team node i, and -> team node j  (capacity inf)
      team node i -> sink with capacity W - wins[i]      (slack for team i)

    x can still finish first iff the max flow saturates all game-source edges
    (i.e. all remaining games among the other teams can be distributed without
    pushing any team's win total above W). Otherwise x is eliminated.

    ``games_between`` is keyed by unordered pairs given as sorted tuples.
    """
    W = wins[x] + remaining[x]
    others = [t for t in teams if t != x]

    # Trivial elimination: some team already has more wins than x can reach.
    for i in others:
        if wins[i] > W:
            return True

    mf = MaxFlow()
    s, t = "__source__", "__sink__"
    total_games = 0
    for i, j in combinations(others, 2):
        key = tuple(sorted((i, j), key=str))
        g = games_between.get(key, 0)
        if g == 0:
            continue
        total_games += g
        game_node = ("game", key)
        mf.add_edge(s, game_node, g)
        mf.add_edge(game_node, ("team", i), float("inf"))
        mf.add_edge(game_node, ("team", j), float("inf"))

    for i in others:
        mf.add_edge(("team", i), t, W - wins[i])

    flow_value = mf.max_flow(s, t)
    # Eliminated iff we cannot route all remaining games (some game edge unsaturated).
    return flow_value < total_games - 1e-9


if __name__ == "__main__":
    # Classic 4-team example (Detroit is eliminated in K&T's running example shape).
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
    # NY leads and has games in hand: not eliminated.
    assert is_eliminated(teams, wins, remaining, games, "NY") is False

    # A team that already trails by more than it can make up is eliminated.
    teams2 = ["A", "B", "C"]
    wins2 = {"A": 10, "B": 10, "C": 2}
    remaining2 = {"A": 0, "B": 0, "C": 5}
    games2 = {tuple(sorted(("A", "B"), key=str)): 0,
              tuple(sorted(("A", "C"), key=str)): 0,
              tuple(sorted(("B", "C"), key=str)): 5}
    # C can reach 7 < 10: trivially eliminated.
    assert is_eliminated(teams2, wins2, remaining2, games2, "C") is True

    # A team that can still tie/overtake everyone is not eliminated.
    teams3 = ["A", "B"]
    wins3 = {"A": 5, "B": 5}
    remaining3 = {"A": 3, "B": 3}
    games3 = {tuple(sorted(("A", "B"), key=str)): 3}
    assert is_eliminated(teams3, wins3, remaining3, games3, "A") is False

    # Leader who has clinched (everyone else maxes below) is not eliminated.
    teams4 = ["A", "B", "C"]
    wins4 = {"A": 100, "B": 1, "C": 1}
    remaining4 = {"A": 0, "B": 1, "C": 1}
    games4 = {tuple(sorted(("B", "C"), key=str)): 1}
    assert is_eliminated(teams4, wins4, remaining4, games4, "A") is False

    print("All tests passed!")
