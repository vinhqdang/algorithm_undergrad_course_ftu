"""
Problem 14 - Heap-Based PQ vs. Naive Sorted-List PQ
=====================================================

A priority queue can be implemented in (at least) two ways:

  1. **Heap-based** (Problem 12's `MinHeap`): `push` and `pop` are both
     O(log n).

  2. **Naive sorted list**: maintain a Python list that is kept sorted at
     all times.
       - `push(x)`: find the insertion point with `bisect.insort` (O(n) due
         to the shift, though the search itself is O(log n)) -- count this
         as `len(self.data)` "shift operations" (worst case, inserting at
         the front).
       - `pop()`: remove and return `self.data.pop(0)` -- also O(n) due to
         the shift, count as `len(self.data) - 1` "shift operations" (the
         number of remaining elements that must shift left).

Implement `SortedListPQ` with `push`, `pop`, `peek`, `__len__`, and an
`self.ops` counter that accumulates the "shift operations" described above
(for `push`, count `len(self.data)` *before* insertion; for `pop`, count
`len(self.data) - 1` *before* removal).

Then implement `compare_pq_costs(n, seed)`:
  1. Generate `n` random integers (use `random_array(n, seed=seed)` from
     starter_code).
  2. Push all `n` values onto a `MinHeap` (Problem 12) and a `SortedListPQ`,
     in the same order.
  3. Pop all `n` values from each (in increasing order).
  4. Return `(heap_ops, sorted_list_ops)`, where `heap_ops` is the total
     number of "element moves" performed by the heap (count 1 per swap
     during sift-up/sift-down -- to keep this simple, instrument `MinHeap`'s
     `push`/`pop` from Problem 12's *solution* by re-implementing a small
     counting wrapper here -- see the provided `CountingMinHeap` below), and
     `sorted_list_ops` is `SortedListPQ.ops` after all operations.

A `CountingMinHeap` (subclass of `MinHeap` that also counts swaps) is
provided in this file's solution; in the starter file you only need to
implement `SortedListPQ` and `compare_pq_costs`.

**What you should observe.** For large n, `heap_ops` grows roughly like
`n log n`, while `sorted_list_ops` grows roughly like `n^2 / 4` (on random
data, the average insertion/removal point is near the middle).

See practical_exercises.pdf, Problem 14.
"""

import os
import sys
from typing import List, Tuple

_PARENT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, _PARENT)
sys.path.insert(0, os.path.join(_PARENT, "solutions"))

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
        # TODO: implement this method.
        raise NotImplementedError

    def pop(self) -> int:
        """Remove and return the smallest element; count len(self.data)-1 shift ops."""
        # TODO: implement this method.
        raise NotImplementedError

    def peek(self) -> int:
        """Return the smallest element without removing it."""
        # TODO: implement this method.
        raise NotImplementedError


def compare_pq_costs(n: int, seed: int = 0) -> Tuple[int, int]:
    """Return (heap_ops, sorted_list_ops) for pushing then popping n random values."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
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
            # For n >= 16, the sorted-list approach should do more "work"
            # than the heap-based approach.
            assert sorted_ops > heap_ops, (n, heap_ops, sorted_ops)

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
