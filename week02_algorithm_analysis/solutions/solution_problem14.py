"""
Problem 14 - Heap-Based PQ vs. Naive Sorted-List PQ (SOLUTION)
==================================================================
"""

import bisect
import os
import sys
from typing import List, Tuple

_PARENT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, _PARENT)

from solution_problem12 import MinHeap  # noqa: E402
from starter_code import random_array  # noqa: E402


class CountingMinHeap(MinHeap):
    """A MinHeap that also counts the total number of element swaps performed."""

    def __init__(self) -> None:
        super().__init__()
        self.swaps = 0

    def push(self, x: int) -> None:
        self.data.append(x)
        i = len(self.data) - 1
        while i > 0:
            parent = (i - 1) // 2
            if self.data[i] < self.data[parent]:
                self.data[i], self.data[parent] = self.data[parent], self.data[i]
                self.swaps += 1
                i = parent
            else:
                break

    def pop(self) -> int:
        if not self.data:
            raise IndexError("pop from empty heap")
        min_val = self.data[0]
        last = self.data.pop()
        if self.data:
            self.data[0] = last
            self._sift_down_counting(0)
        return min_val

    def _sift_down_counting(self, i: int) -> None:
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
            self.swaps += 1
            i = smallest


class SortedListPQ:
    def __init__(self) -> None:
        self.data: List[int] = []
        self.ops = 0

    def __len__(self) -> int:
        return len(self.data)

    def push(self, x: int) -> None:
        """Insert x, keeping self.data sorted; count len(self.data) shift ops."""
        self.ops += len(self.data)
        bisect.insort(self.data, x)

    def pop(self) -> int:
        """Remove and return the smallest element; count len(self.data)-1 shift ops."""
        self.ops += max(len(self.data) - 1, 0)
        return self.data.pop(0)

    def peek(self) -> int:
        """Return the smallest element without removing it."""
        return self.data[0]


def compare_pq_costs(n: int, seed: int = 0) -> Tuple[int, int]:
    """Return (heap_ops, sorted_list_ops) for pushing then popping n random values."""
    values = random_array(n, seed=seed)

    heap = CountingMinHeap()
    sorted_pq = SortedListPQ()

    for x in values:
        heap.push(x)
        sorted_pq.push(x)

    for _ in range(n):
        heap.pop()
        sorted_pq.pop()

    return heap.swaps, sorted_pq.ops


if __name__ == "__main__":
    pq = SortedListPQ()
    for x in [5, 1, 3, 2, 4]:
        pq.push(x)
    assert pq.peek() == 1
    popped = [pq.pop() for _ in range(5)]
    assert popped == [1, 2, 3, 4, 5]
    assert len(pq) == 0

    for n in [16, 64, 256]:
        heap_ops, sorted_ops = compare_pq_costs(n, seed=0)
        assert heap_ops > 0
        assert sorted_ops > 0
        assert sorted_ops > heap_ops, (n, heap_ops, sorted_ops)
        print(f"n={n}: heap_ops={heap_ops}, sorted_list_ops={sorted_ops}")

    print("All tests passed!")
