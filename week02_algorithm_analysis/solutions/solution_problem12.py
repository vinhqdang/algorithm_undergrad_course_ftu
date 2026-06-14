"""
Problem 12 - Binary Min-Heap from Scratch (SOLUTION)
=======================================================
"""

from typing import List


class MinHeap:
    def __init__(self) -> None:
        self.data: List[int] = []

    def __len__(self) -> int:
        return len(self.data)

    def push(self, x: int) -> None:
        """Insert x and restore the heap property by sifting up."""
        self.data.append(x)
        i = len(self.data) - 1
        while i > 0:
            parent = (i - 1) // 2
            if self.data[i] < self.data[parent]:
                self.data[i], self.data[parent] = self.data[parent], self.data[i]
                i = parent
            else:
                break

    def pop(self) -> int:
        """Remove and return the minimum element, restoring the heap property."""
        if not self.data:
            raise IndexError("pop from empty heap")

        min_val = self.data[0]
        last = self.data.pop()
        if self.data:
            self.data[0] = last
            self._sift_down(0)
        return min_val

    def peek(self) -> int:
        """Return the minimum element without removing it."""
        if not self.data:
            raise IndexError("peek from empty heap")
        return self.data[0]

    def _sift_down(self, i: int) -> None:
        n = len(self.data)
        while True:
            left, right = 2 * i + 1, 2 * i + 2
            smallest = i
            if left < n and self.data[left] < self.data[smallest]:
                smallest = left
            if right < n and self.data[right] < self.data[smallest]:
                smallest = right
            if smallest == i:
                break
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            i = smallest


def heapsort(arr: List[int]) -> List[int]:
    """Return a new sorted list by pushing all elements onto a MinHeap and popping them off."""
    heap = MinHeap()
    for x in arr:
        heap.push(x)
    return [heap.pop() for _ in range(len(heap))]


if __name__ == "__main__":
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
