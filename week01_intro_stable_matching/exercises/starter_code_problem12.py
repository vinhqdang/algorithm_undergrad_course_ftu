"""
Problem 12 - Singly Linked List
=================================

Implement a `LinkedList` class with:
  - `append(x)`: add x at the end -- O(n) without a tail pointer.
  - `prepend(x)`: add x at the front -- O(1).
  - `delete(x)`: remove the first node with value x (no-op if not found).
  - `find(x)`: return True iff x is in the list.
  - `to_list()`: return a Python list of the values, in order.
  - `reverse()`: reverse the list IN PLACE (re-link nodes, do not just
    reverse `to_list()`).

See practical_exercises.pdf, Problem 12.
"""

from typing import Any, List


class _Node:
    __slots__ = ("val", "next")

    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, x: Any) -> None:
        # TODO: implement.
        raise NotImplementedError

    def prepend(self, x: Any) -> None:
        # TODO: implement.
        raise NotImplementedError

    def delete(self, x: Any) -> None:
        # TODO: implement.
        raise NotImplementedError

    def find(self, x: Any) -> bool:
        # TODO: implement.
        raise NotImplementedError

    def to_list(self) -> List[Any]:
        # TODO: implement.
        raise NotImplementedError

    def reverse(self) -> None:
        # TODO: implement (in place, by re-linking nodes).
        raise NotImplementedError


if __name__ == "__main__":
    try:
        ll = LinkedList()
        for x in [1, 2, 3]:
            ll.append(x)
        assert ll.to_list() == [1, 2, 3]

        ll.prepend(0)
        assert ll.to_list() == [0, 1, 2, 3]

        assert ll.find(2) is True
        assert ll.find(99) is False

        ll.delete(2)
        assert ll.to_list() == [0, 1, 3]

        ll.reverse()
        assert ll.to_list() == [3, 1, 0]

        # Deleting a non-existent value is a no-op.
        ll.delete(42)
        assert ll.to_list() == [3, 1, 0]

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
