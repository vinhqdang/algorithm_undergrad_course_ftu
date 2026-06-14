"""
Problem 09 - Array vs Linked List: Counting Operations
========================================================

Implement two simple sequence data structures, each instrumented with an
`ops` counter that counts "basic steps" (element shifts for the array,
pointer hops for the linked list):

  - `ArraySeq.prepend(x)`: insert x at index 0. Every existing element must be
    shifted right by one slot -> costs `len(self.data)` ops.
  - `ArraySeq.get(i)`: direct indexing -> costs 1 op.

  - `LinkedSeq.prepend(x)`: create a new head node -> costs 1 op.
  - `LinkedSeq.get(i)`: walk i pointers from the head -> costs (i + 1) ops.

Then implement `total_prepend_ops(seq_class, n)` that creates a fresh
`seq_class()`, prepends `n` items (0, 1, ..., n-1 in that order), and returns
the final value of `seq.ops` (total cost of all prepends).

See practical_exercises.pdf, Problem 9.
"""


class ArraySeq:
    def __init__(self):
        self.data = []
        self.ops = 0

    def prepend(self, x):
        # TODO: shift all existing elements right by one, then place x at
        # index 0. Add len(self.data) to self.ops BEFORE inserting.
        raise NotImplementedError

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
        # TODO: create a new head node pointing at the old head. Add 1 to
        # self.ops.
        raise NotImplementedError

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
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        n = 50
        array_ops = total_prepend_ops(ArraySeq, n)
        linked_ops = total_prepend_ops(LinkedSeq, n)

        # Array prepends cost 0+1+...+(n-1) = n(n-1)/2 -> quadratic.
        assert array_ops == n * (n - 1) // 2, array_ops
        # Linked-list prepends cost 1 each -> linear.
        assert linked_ops == n, linked_ops
        assert array_ops > linked_ops

        # Sanity check the data ends up in the right (reversed) order.
        a = ArraySeq()
        for x in range(5):
            a.prepend(x)
        assert [a.get(i) for i in range(5)] == [4, 3, 2, 1, 0]

        print(f"n={n}: ArraySeq prepend ops = {array_ops}, LinkedSeq prepend ops = {linked_ops}")
        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
