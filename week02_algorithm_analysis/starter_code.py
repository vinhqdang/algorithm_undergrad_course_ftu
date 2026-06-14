"""
Week 02 - Algorithm Analysis & Asymptotics
============================================

Shared utilities used by the practical exercise problems
(starter_code_problem01.py ... starter_code_problem24.py).

You do not need to modify this file. Import what you need, e.g.:

    from starter_code import random_array, is_sorted, GROWTH_FUNCTIONS

Conventions
-----------
- `random_array(n, seed=...)` generates a list of `n` random integers.
- `GROWTH_FUNCTIONS` is a dictionary mapping growth-rate names to callables
  of a single positive integer `n`, used throughout Section 1 (asymptotic
  analysis) of the practical exercises.
- Several problems re-use the Gale-Shapley preference-list generator from
  Week 1; a self-contained copy (`generate_instance`) is provided here so
  this week's exercises do not depend on week01's folder.
"""

from __future__ import annotations

import math
import random
from typing import Callable, Dict, List, Tuple


def random_array(n: int, seed: int | None = None, lo: int = 0, hi: int = 1_000_000) -> List[int]:
    """Return a list of n random integers in [lo, hi], using `seed` for reproducibility."""
    rng = random.Random(seed)
    return [rng.randint(lo, hi) for _ in range(n)]


def is_sorted(arr: List[int]) -> bool:
    """Return True iff arr is sorted in non-decreasing order."""
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


# A small library of named growth-rate functions, used by Problems 1 and 2
# (ordering functions by growth, and empirically checking O/Omega/Theta
# relationships). All functions are defined for positive integers n >= 1.
GROWTH_FUNCTIONS: Dict[str, Callable[[int], float]] = {
    "constant":     lambda n: 1.0,
    "logarithmic":  lambda n: math.log2(n) if n > 0 else 0.0,
    "sqrt":         lambda n: math.sqrt(n),
    "linear":       lambda n: float(n),
    "linearithmic": lambda n: n * math.log2(n) if n > 0 else 0.0,
    "quadratic":    lambda n: float(n ** 2),
    "cubic":        lambda n: float(n ** 3),
    "exponential":  lambda n: float(2 ** n),
}


def generate_instance(n: int, seed: int | None = None) -> Tuple[List[str], List[str], Dict[str, List[str]], Dict[str, List[str]]]:
    """Generate a random instance of the Stable Matching problem with n men and n women.

    Returns (men, women, men_prefs, women_prefs), exactly as in Week 1's
    starter_code.generate_instance. Re-included here so Week 2's
    "efficient Gale-Shapley" problem is self-contained.
    """
    rng = random.Random(seed)
    men = [f"M{i}" for i in range(n)]
    women = [f"W{i}" for i in range(n)]
    men_prefs = {m: rng.sample(women, len(women)) for m in men}
    women_prefs = {w: rng.sample(men, len(men)) for w in women}
    return men, women, men_prefs, women_prefs


def is_perfect_matching(matching: Dict[str, str], men: List[str], women: List[str]) -> bool:
    """Return True iff `matching` is a bijection between `men` and `women`."""
    if set(matching.keys()) != set(men):
        return False
    if sorted(matching.values()) != sorted(women):
        return False
    return True


def find_rogue_couples(matching: Dict[str, str], men_prefs: Dict[str, List[str]], women_prefs: Dict[str, List[str]]) -> List[Tuple[str, str]]:
    """Return a list of (man, woman) pairs that form a rogue (blocking) couple."""
    woman_to_man = {w: m for m, w in matching.items()}
    rogue = []
    for m, w_current in matching.items():
        for w in men_prefs[m]:
            if w == w_current:
                break
            m_current = woman_to_man[w]
            if women_prefs[w].index(m) < women_prefs[w].index(m_current):
                rogue.append((m, w))
    return rogue


def is_stable(matching: Dict[str, str], men_prefs: Dict[str, List[str]], women_prefs: Dict[str, List[str]]) -> bool:
    """Return True iff `matching` admits no rogue couples."""
    return len(find_rogue_couples(matching, men_prefs, women_prefs)) == 0
