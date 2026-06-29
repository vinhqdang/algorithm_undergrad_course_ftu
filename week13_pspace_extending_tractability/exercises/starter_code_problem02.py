"""
Problem 02 - Minimax Game-Tree Evaluation
==========================================

Implement `minimax(node, maximizing)` returning the minimax value of a game
tree for the player to move. A game tree is a nested structure: an internal
node is a NON-EMPTY list of child subtrees; a leaf is a number (the payoff,
from the maximizing player's point of view).

If ``maximizing`` is True, the player to move maximizes (take the max over
children, each evaluated with maximizing=False); otherwise the player
minimizes (take the min, children evaluated with maximizing=True).

See practical_exercises.pdf, Problem 2.
"""


def minimax(node, maximizing: bool = True):
    """Return the minimax value of ``node`` for the player to move."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        assert minimax(5) == 5
        tree = [[3, 5], [2, 9]]
        assert minimax(tree, maximizing=True) == 3
        assert minimax(tree, maximizing=False) == 5
        tree3 = [
            [[3, 12, 8], [2, 4, 6]],
            [[14, 5, 2], [3, 3]],
        ]
        assert minimax(tree3, maximizing=True) == 6
        assert minimax([1, 2, 3], maximizing=True) == 3
        assert minimax([1, 2, 3], maximizing=False) == 1

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
