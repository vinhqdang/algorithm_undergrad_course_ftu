"""
Problem 02 - Minimax Game-Tree Evaluation (SOLUTION)
=====================================================

A game tree is a nested structure: an internal node is a list of child
subtrees; a leaf is an int/float payoff (from the maximizing player's view).
The root and every even-depth node is a MAX node; odd-depth nodes are MIN.
"""


def minimax(node, maximizing: bool = True):
    """Return the minimax value of ``node`` for the player to move.

    ``maximizing`` is True if the player to move at ``node`` maximizes.
    Leaves are numbers; internal nodes are non-empty lists of children.
    """
    if not isinstance(node, list):
        return node  # leaf payoff
    if maximizing:
        return max(minimax(child, False) for child in node)
    return min(minimax(child, True) for child in node)


if __name__ == "__main__":
    # A single leaf.
    assert minimax(5) == 5

    # Classic 2-level tree (root MAX, children MIN over leaves).
    #        MAX
    #      /     \
    #    MIN      MIN
    #   / \      / \
    #  3   5    2   9
    # MIN children -> 3 and 2; MAX picks 3.
    tree = [[3, 5], [2, 9]]
    assert minimax(tree, maximizing=True) == 3

    # Same tree but root is MIN: MAX children -> 5 and 9; MIN picks 5.
    assert minimax(tree, maximizing=False) == 5

    # 3-level tree.
    tree3 = [
        [[3, 12, 8], [2, 4, 6]],   # MIN of (MAX 12, MAX 6) -> 6
        [[14, 5, 2], [3, 3]],      # MIN of (MAX 14, MAX 3)  -> 3
    ]
    # root MAX of (6, 3) -> 6
    assert minimax(tree3, maximizing=True) == 6

    # Negamax-style symmetry check: negating all leaves and flipping role.
    assert minimax([1, 2, 3], maximizing=True) == 3
    assert minimax([1, 2, 3], maximizing=False) == 1

    print("All tests passed!")
