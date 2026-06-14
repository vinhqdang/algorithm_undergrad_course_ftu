"""
Problem 16 - Efficient Gale-Shapley with Arrays and Queues
=============================================================

Week 1's Gale-Shapley implementation used Python dicts and `.index()` lookups,
which can hide costly linear scans. This problem re-implements the
men-proposing algorithm (Kleinberg & Tardos, Section 2.3 style) using only
arrays (lists) and a queue, to make the O(n^2) bound explicit and measurable.

Represent men and women as integers 0..n-1. You are given:
  - `men_pref[m]` = list of women in order of preference (best first).
  - `women_rank[w]` = list such that `women_rank[w][m]` = the rank woman w
    assigns to man m (lower = more preferred). Precomputing this rank table
    lets you compare two suitors in O(1) instead of calling `.index()`
    (which is O(n)).

Implement `build_women_rank(women_pref, n)` that, given `women_pref[w]` (list
of men in order of preference for woman w) and `n`, returns `women_rank`
where `women_rank[w][m]` is the 0-based rank of man m in woman w's list.

Then implement `efficient_gale_shapley(men_pref, women_pref, n)`:
  1. Build `women_rank` via `build_women_rank`.
  2. Use a queue (e.g. `collections.deque`) of free men, initially containing
     all of 0..n-1.
  3. Maintain `next_proposal[m]` = index into `men_pref[m]` of the next
     woman m will propose to (starts at 0, array of size n).
  4. Maintain `woman_partner[w]` = current partner of woman w, or -1 if free
     (array of size n).
  5. While the queue is non-empty: pop a free man m, let
     `w = men_pref[m][next_proposal[m]]`, increment `next_proposal[m]`. If w
     is free, engage (m, w). Else compare `women_rank[w][m]` against
     `women_rank[w][woman_partner[w]]`: if m is preferred, the old partner
     becomes free (pushed back onto the queue) and (m, w) become engaged;
     otherwise m remains free (pushed back onto the queue).
  6. Return `(matching, total_proposals)` where `matching` is a list with
     `matching[m] = woman_partner` for man m (i.e. `matching[m]` is the
     woman matched to man m), and `total_proposals` is the total number of
     proposals made.

Verify on a random instance that the result is a valid permutation (a
perfect matching) and that `total_proposals <= n*n`.

See practical_exercises.pdf, Problem 16.
"""

from collections import deque
from typing import List, Tuple


def build_women_rank(women_pref: List[List[int]], n: int) -> List[List[int]]:
    """Return women_rank where women_rank[w][m] = rank of man m in women_pref[w]."""
    # TODO: implement this function.
    raise NotImplementedError


def efficient_gale_shapley(men_pref: List[List[int]], women_pref: List[List[int]], n: int) -> Tuple[List[int], int]:
    """Run the array/queue-based men-proposing Gale-Shapley algorithm.

    Returns (matching, total_proposals) where matching[m] = woman matched to man m.
    """
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
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

        # matching must be a permutation of 0..n-1 (a perfect matching).
        assert sorted(matching) == list(range(n))
        assert 0 < total_proposals <= n * n

        # No man proposes to the same woman twice: each man proposes at
        # most n times, so total_proposals <= n*n.
        print(f"n={n}: total_proposals={total_proposals} (n^2={n*n})")

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
