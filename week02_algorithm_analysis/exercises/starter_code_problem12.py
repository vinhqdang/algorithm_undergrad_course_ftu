"""
Problem 12 - Binary Min-Heap from Scratch
============================================

Implement an array-based binary `MinHeap` class with:

  - `push(x)`: insert x, then "sift up" to restore the heap property.
  - `pop()`: remove and return the minimum element, moving the last element
    to the root and "sifting down" to restore the heap property. Raise
    `IndexError` if empty.
  - `peek()`: return (without removing) the minimum element. Raise
    `IndexError` if empty.
  - `__len__`: number of elements.

The heap is stored in `self.data` (a Python list), where for index i, the
children are at indices 2*i+1 and 2*i+2, and the parent is at (i-1)//2.

Then implement `heapsort(arr)` that returns a new sorted list by pushing all
elements of `arr` onto a `MinHeap` and popping them off in order. This gives
an O(n log n) sort.

See practical_exercises.pdf, Problem 12.
"""

from typing import List


class MinHeap:
    def __init__(self) -> None:
        self.data: List[int] = []

    def __len__(self) -> int:
        return len(self.data)

    def push(self, x: int) -> None:
        """Insert x and restore the heap property by sifting up."""
        # TODO: implement this method.
        raise NotImplementedError

    def pop(self) -> int:
        """Remove and return the minimum element, restoring the heap property."""
        # TODO: implement this method.
        raise NotImplementedError

    def peek(self) -> int:
        """Return the minimum element without removing it."""
        # TODO: implement this method.
        raise NotImplementedError


def heapsort(arr: List[int]) -> List[int]:
    """Return a new sorted list by pushing all elements onto a MinHeap and popping them off."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        heap = MinHeap()
        assert len(heap) == 0

        for x in [5, 3, 8, 1, 9, 2, 7]:
            heap.push(x)

        assert len(heap) == 7
        assert heap.peek() == 1

        popped = []
        while len(heap) > 0:
            popped.append(heap.pop())

        assert popped == sorted([5, 3, 8, 1, 9, 2, 7])

        try:
            heap.pop()
            assert False, "expected IndexError"
        except IndexError:
            pass

        try:
            heap.peek()
            assert False, "expected IndexError"
        except IndexError:
            pass

        assert heapsort([4, 2, 7, 1, 3]) == [1, 2, 3, 4, 7]
        assert heapsort([]) == []
        assert heapsort([1]) == [1]
        assert heapsort([3, 3, 1, 1, 2]) == [1, 1, 2, 3, 3]

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
