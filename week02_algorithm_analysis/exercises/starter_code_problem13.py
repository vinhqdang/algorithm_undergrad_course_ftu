"""
Problem 13 - Indexed Priority Queue with decrease-key
=======================================================

In algorithms like Dijkstra's shortest path (covered in a later week), we
need a priority queue where items can have their priority *decreased* after
insertion, and we need to look up an item's current position efficiently.

Implement `IndexedMinPQ`, a binary min-heap of (key, priority) pairs that
supports:

  - `insert(key, priority)`: insert a new key with the given priority.
    Assumes `key` is not already present.
  - `decrease_key(key, new_priority)`: lower the priority of an existing
    `key` to `new_priority` (assumes `new_priority <= current priority`),
    then restore the heap property by sifting up.
  - `extract_min()`: remove and return `(key, priority)` with the smallest
    priority, restoring the heap property by sifting down. Raise
    `IndexError` if empty.
  - `__len__`: number of elements.
  - `__contains__(key)`: True iff `key` is currently in the priority queue.

Implementation hints:
  - Maintain `self.heap`: a list of `[priority, key]` pairs (heap-ordered by
    priority).
  - Maintain `self.position`: a dict mapping `key -> index in self.heap`,
    updated on every swap, so `decrease_key` can find the key in O(1) and
    then sift up in O(log n).

See practical_exercises.pdf, Problem 13.
"""

from typing import Dict, List, Tuple


class IndexedMinPQ:
    def __init__(self) -> None:
        self.heap: List[List] = []  # list of [priority, key]
        self.position: Dict[object, int] = {}  # key -> index in self.heap

    def __len__(self) -> int:
        return len(self.heap)

    def __contains__(self, key: object) -> bool:
        return key in self.position

    def insert(self, key: object, priority: float) -> None:
        """Insert a new key with the given priority."""
        # TODO: implement this method.
        raise NotImplementedError

    def decrease_key(self, key: object, new_priority: float) -> None:
        """Lower the priority of an existing key, restoring the heap property."""
        # TODO: implement this method.
        raise NotImplementedError

    def extract_min(self) -> Tuple[object, float]:
        """Remove and return (key, priority) with the smallest priority."""
        # TODO: implement this method.
        raise NotImplementedError


if __name__ == "__main__":
    try:
        pq = IndexedMinPQ()
        assert len(pq) == 0

        pq.insert("A", 10)
        pq.insert("B", 5)
        pq.insert("C", 20)
        pq.insert("D", 15)

        assert len(pq) == 4
        assert "B" in pq
        assert "Z" not in pq

        # B has the smallest priority (5).
        key, prio = pq.extract_min()
        assert (key, prio) == ("B", 5)
        assert "B" not in pq
        assert len(pq) == 3

        # Decrease D's priority below A's and C's.
        pq.decrease_key("D", 1)
        key, prio = pq.extract_min()
        assert (key, prio) == ("D", 1)

        # Remaining: A (10), C (20).
        key, prio = pq.extract_min()
        assert (key, prio) == ("A", 10)
        key, prio = pq.extract_min()
        assert (key, prio) == ("C", 20)

        assert len(pq) == 0

        try:
            pq.extract_min()
            assert False, "expected IndexError"
        except IndexError:
            pass

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
