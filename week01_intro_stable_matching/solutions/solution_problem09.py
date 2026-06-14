"""
Problem 09 - Array vs Linked List: Counting Operations (SOLUTION)
====================================================================
"""


class ArraySeq:
    def __init__(self):
        self.data = []
        self.ops = 0

    def prepend(self, x):
        self.ops += len(self.data)
        self.data.insert(0, x)

    def get(self, i):
        self.ops += 1
        return self.data[i]


class LinkedSeq:
    class _Node:
        __slots__ = ("val", "next")

        def __init__(self, val, nxt=None):
            self.val = val
            self.next = nxt

    def __init__(self):
        self.head = None
        self.ops = 0

    def prepend(self, x):
        self.head = LinkedSeq._Node(x, self.head)
        self.ops += 1

    def get(self, i):
        node = self.head
        cost = 1
        for _ in range(i):
            node = node.next
            cost += 1
        self.ops += cost
        return node.val


def total_prepend_ops(seq_class, n: int) -> int:
    """Create a fresh seq_class(), prepend 0..n-1, return total ops used."""
    seq = seq_class()
    for x in range(n):
        seq.prepend(x)
    return seq.ops


if __name__ == "__main__":
    n = 50
    array_ops = total_prepend_ops(ArraySeq, n)
    linked_ops = total_prepend_ops(LinkedSeq, n)

    assert array_ops == n * (n - 1) // 2, array_ops
    assert linked_ops == n, linked_ops
    assert array_ops > linked_ops

    a = ArraySeq()
    for x in range(5):
        a.prepend(x)
    assert [a.get(i) for i in range(5)] == [4, 3, 2, 1, 0]

    print(f"n={n}: ArraySeq prepend ops = {array_ops}, LinkedSeq prepend ops = {linked_ops}")
    print("All tests passed!")
