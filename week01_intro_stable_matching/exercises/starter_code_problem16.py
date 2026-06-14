"""
Problem 16 - Binary Min-Heap and Heapsort
============================================

Implement an array-based binary `MinHeap` with:
  - `push(x)`: insert x, then "sift up" to restore the heap property.
  - `pop()`: remove and return the minimum element, moving the last element
    to the root and "sifting down" to restore the heap property. Raise
    IndexError if empty.
  - `__len__`: number of elements.

Then implement `heapsort(arr)` that returns a new sorted list by pushing all
elements onto a `MinHeap` and popping them off in order.

See practical_exercises.pdf, Problem 16.
"""

from typing import List


class MinHeap:
    def __init__(self):
        self.data: List[int] = []

    def push(self, x: int) -> None:
        # TODO: append x, then sift up.
        raise NotImplementedError

    def pop(self) -> int:
        # TODO: remove and return the min, then sift down.
        raise NotImplementedError

    def __len__(self) -> int:
        return len(self.data)


def heapsort(arr: List[int]) -> List[int]:
    """Return a new sorted list using MinHeap."""
    # TODO: implement.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        h = MinHeap()
        for x in [5, 3, 8, 1, 9, 2, 7]:
            h.push(x)

        assert len(h) == 7
        popped = [h.pop() for _ in range(7)]
        assert popped == sorted([5, 3, 8, 1, 9, 2, 7])

        try:
            h.pop()
            assert False, "expected IndexError on empty heap"
        except IndexError:
            pass

        import random
        rng = random.Random(1)
        for _ in range(10):
            arr = [rng.randint(0, 100) for _ in range(20)]
            assert heapsort(arr) == sorted(arr)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
