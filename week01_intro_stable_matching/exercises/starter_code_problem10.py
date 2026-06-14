"""
Problem 10 - Stack: Balanced Brackets Checker
===============================================

Implement a simple `Stack` class with `push`, `pop`, `peek`, and `is_empty`,
backed by a Python list. Then implement `is_balanced(expr)` that returns True
iff every `(`, `[`, `{` in `expr` is closed by the matching `)`, `]`, `}` in
the correct order (other characters are ignored).

See practical_exercises.pdf, Problem 10.
"""

from typing import Any


class Stack:
    def __init__(self):
        self._data = []

    def push(self, x: Any) -> None:
        # TODO: implement.
        raise NotImplementedError

    def pop(self) -> Any:
        # TODO: implement. Raise IndexError if empty.
        raise NotImplementedError

    def peek(self) -> Any:
        # TODO: implement. Raise IndexError if empty.
        raise NotImplementedError

    def is_empty(self) -> bool:
        # TODO: implement.
        raise NotImplementedError


PAIRS = {")": "(", "]": "[", "}": "{"}


def is_balanced(expr: str) -> bool:
    """Return True iff brackets in `expr` are balanced and correctly nested."""
    # TODO: implement using Stack.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        s = Stack()
        assert s.is_empty() is True
        s.push(1)
        s.push(2)
        assert s.peek() == 2
        assert s.pop() == 2
        assert s.pop() == 1
        assert s.is_empty() is True

        assert is_balanced("") is True
        assert is_balanced("()") is True
        assert is_balanced("([{}])") is True
        assert is_balanced("(a + b) * [c - {d / e}]") is True
        assert is_balanced("(]") is False
        assert is_balanced("((a)") is False
        assert is_balanced("a)b(c") is False

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
