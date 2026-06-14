"""
Problem 16 - Efficient Gale-Shapley with Arrays and Queues (SOLUTION)
=========================================================================
"""

from collections import deque
from typing import List, Tuple


def build_women_rank(women_pref: List[List[int]], n: int) -> List[List[int]]:
    """Return women_rank where women_rank[w][m] = rank of man m in women_pref[w]."""
    women_rank = [[0] * n for _ in range(n)]
    for w in range(n):
        for rank, m in enumerate(women_pref[w]):
            women_rank[w][m] = rank
    return women_rank


def efficient_gale_shapley(men_pref: List[List[int]], women_pref: List[List[int]], n: int) -> Tuple[List[int], int]:
    """Run the array/queue-based men-proposing Gale-Shapley algorithm.

    Returns (matching, total_proposals) where matching[m] = woman matched to man m.
    """
    women_rank = build_women_rank(women_pref, n)

    free_men = deque(range(n))
    next_proposal = [0] * n
    woman_partner = [-1] * n
    total_proposals = 0

    while free_men:
        m = free_men.popleft()
        w = men_pref[m][next_proposal[m]]
        next_proposal[m] += 1
        total_proposals += 1

        if woman_partner[w] == -1:
            woman_partner[w] = m
        else:
            m_current = woman_partner[w]
            if women_rank[w][m] < women_rank[w][m_current]:
                woman_partner[w] = m
                free_men.append(m_current)
            else:
                free_men.append(m)

    matching = [0] * n
    for w in range(n):
        matching[woman_partner[w]] = w

    return matching, total_proposals


if __name__ == "__main__":
    import random

    n = 6
    rng = random.Random(42)
    men_pref = [rng.sample(range(n), n) for _ in range(n)]
    women_pref = [rng.sample(range(n), n) for _ in range(n)]

    women_rank = build_women_rank(women_pref, n)
    for w in range(n):
        for m in range(n):
            assert women_rank[w][women_pref[w][m]] == m

    matching, total_proposals = efficient_gale_shapley(men_pref, women_pref, n)

    assert sorted(matching) == list(range(n))
    assert 0 < total_proposals <= n * n

    print(f"n={n}: total_proposals={total_proposals} (n^2={n*n})")

    print("All tests passed!")
