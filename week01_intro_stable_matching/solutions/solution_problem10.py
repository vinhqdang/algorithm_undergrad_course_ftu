"""
Problem 10 - Stack: Balanced Brackets Checker (SOLUTION)
==========================================================
"""

from typing import Any


class Stack:
    def __init__(self):
        self._data = []

    def push(self, x: Any) -> None:
        self._data.append(x)

    def pop(self) -> Any:
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self) -> Any:
        if not self._data:
            raise IndexError("peek from empty stack")
        return self._data[-1]

    def is_empty(self) -> bool:
        return len(self._data) == 0


PAIRS = {")": "(", "]": "[", "}": "{"}


def is_balanced(expr: str) -> bool:
    """Return True iff brackets in `expr` are balanced and correctly nested."""
    stack = Stack()
    for ch in expr:
        if ch in "([{":
            stack.push(ch)
        elif ch in ")]}":
            if stack.is_empty() or stack.pop() != PAIRS[ch]:
                return False
    return stack.is_empty()


if __name__ == "__main__":
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
