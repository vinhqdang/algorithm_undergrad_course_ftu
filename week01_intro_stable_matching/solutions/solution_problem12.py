"""
Problem 12 - Singly Linked List (SOLUTION)
=============================================
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
        new_node = _Node(x)
        if self.head is None:
            self.head = new_node
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = new_node

    def prepend(self, x: Any) -> None:
        self.head = _Node(x, self.head)

    def delete(self, x: Any) -> None:
        if self.head is None:
            return
        if self.head.val == x:
            self.head = self.head.next
            return
        node = self.head
        while node.next is not None:
            if node.next.val == x:
                node.next = node.next.next
                return
            node = node.next

    def find(self, x: Any) -> bool:
        node = self.head
        while node is not None:
            if node.val == x:
                return True
            node = node.next
        return False

    def to_list(self) -> List[Any]:
        result = []
        node = self.head
        while node is not None:
            result.append(node.val)
            node = node.next
        return result

    def reverse(self) -> None:
        prev = None
        node = self.head
        while node is not None:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt
        self.head = prev


if __name__ == "__main__":
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

    ll.delete(42)
    assert ll.to_list() == [3, 1, 0]

    print("All tests passed!")
