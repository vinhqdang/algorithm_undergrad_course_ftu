"""
Week 01 - Introduction & Stable Matching
=========================================

Shared utilities used by the practical exercise problems
(starter_code_problem01.py ... starter_code_problem22.py).

You do not need to modify this file. Import what you need, e.g.:

    from starter_code import generate_instance, is_perfect_matching, is_stable, rank

Conventions
-----------
- `men` and `women` are lists of names, e.g. ["M0", "M1", "M2"].
- `men_prefs[m]` is a list of women names, best choice first.
- `women_prefs[w]` is a list of men names, best choice first.
- A `matching` is a dict mapping man -> woman (and is assumed to be a bijection
  between `men` and `women` once it is "perfect").
"""

from __future__ import annotations

import random
from typing import Dict, List, Tuple


def generate_instance(n: int, seed: int | None = None) -> Tuple[List[str], List[str], Dict[str, List[str]], Dict[str, List[str]]]:
    """Generate a random instance of the Stable Matching problem with n men and n women.

    Returns (men, women, men_prefs, women_prefs) where men_prefs/women_prefs are
    complete, strictly-ordered preference lists (a uniformly random permutation
    of the opposite side for every participant).
    """
    rng = random.Random(seed)
    men = [f"M{i}" for i in range(n)]
    women = [f"W{i}" for i in range(n)]
    men_prefs = {m: rng.sample(women, len(women)) for m in men}
    women_prefs = {w: rng.sample(men, len(men)) for w in women}
    return men, women, men_prefs, women_prefs


def rank(prefs: Dict[str, List[str]], person: str, candidate: str) -> int:
    """Return the 0-based rank of `candidate` in `person`'s preference list.

    Lower rank = more preferred. Raises ValueError if candidate is not present
    (i.e. the list is incomplete and `candidate` is unacceptable to `person`).
    """
    return prefs[person].index(candidate)


def is_perfect_matching(matching: Dict[str, str], men: List[str], women: List[str]) -> bool:
    """Return True iff `matching` is a bijection between `men` and `women`."""
    if set(matching.keys()) != set(men):
        return False
    if sorted(matching.values()) != sorted(women):
        return False
    return True


def find_rogue_couples(matching: Dict[str, str], men_prefs: Dict[str, List[str]], women_prefs: Dict[str, List[str]]) -> List[Tuple[str, str]]:
    """Return a list of (man, woman) pairs that form a rogue (blocking) couple
    with respect to `matching`: both prefer each other to their current partner.
    """
    woman_to_man = {w: m for m, w in matching.items()}
    rogue = []
    for m, w_current in matching.items():
        for w in men_prefs[m]:
            if w == w_current:
                break  # m does not prefer anyone before w_current
            m_current = woman_to_man[w]
            if rank(women_prefs, w, m) < rank(women_prefs, w, m_current):
                rogue.append((m, w))
    return rogue


def is_stable(matching: Dict[str, str], men_prefs: Dict[str, List[str]], women_prefs: Dict[str, List[str]]) -> bool:
    """Return True iff `matching` admits no rogue couples."""
    return len(find_rogue_couples(matching, men_prefs, women_prefs)) == 0


def print_matching(matching: Dict[str, str]) -> None:
    """Pretty-print a matching, sorted by man's name."""
    for m in sorted(matching, key=lambda x: int(x[1:])):
        print(f"  {m} -- {matching[m]}")
