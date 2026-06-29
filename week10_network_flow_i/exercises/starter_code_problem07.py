"""
Problem 07 - Verify Edmonds-Karp and Ford-Fulkerson Agree
===========================================================

Implement ``verify_algorithms_agree(num_trials, n, seed)``: for each of
``num_trials`` random networks (``generate_flow_network(n, seed=seed+trial)``),
compute the max flow with BOTH your Edmonds-Karp (Problem 5) and your DFS
Ford-Fulkerson (Problem 6) and check the values are equal. Return True iff they
agree on every trial.

Because the max-flow value is unique (Max-Flow Min-Cut theorem), any correct
augmenting-path method must produce the same value regardless of path choice.

Hint: use ``network.copy()`` so each algorithm runs on its own copy (the flow
mutations are in place).

See practical_exercises.pdf, Problem 7, for the full statement and examples.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starter_code import generate_flow_network

# When you have implemented Problems 5 and 6, you can import them here. The
# reference solutions live in the solutions/ directory.
# from starter_code_problem05 import edmonds_karp
# from starter_code_problem06 import ford_fulkerson


def verify_algorithms_agree(num_trials: int = 50, n: int = 8, seed: int = 0) -> bool:
    """Return True iff Edmonds-Karp and DFS Ford-Fulkerson agree on every
    random network."""
    # TODO: implement this function (using your Problem 5 and 6 solutions).
    raise NotImplementedError


if __name__ == "__main__":
    try:
        assert verify_algorithms_agree(num_trials=50, n=8, seed=0) is True
        assert verify_algorithms_agree(num_trials=30, n=12, seed=1000) is True
        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
