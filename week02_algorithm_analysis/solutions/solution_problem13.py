"""
Problem 13 - Indexed Priority Queue with decrease-key (SOLUTION)
====================================================================
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

    def _swap(self, i: int, j: int) -> None:
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.position[self.heap[i][1]] = i
        self.position[self.heap[j][1]] = j

    def _sift_up(self, i: int) -> None:
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i][0] < self.heap[parent][0]:
                self._swap(i, parent)
                i = parent
            else:
                break

    def _sift_down(self, i: int) -> None:
        n = len(self.heap)
        while True:
            left, right = 2 * i + 1, 2 * i + 2
            smallest = i
            if left < n and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left
            if right < n and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right
            if smallest == i:
                break
            self._swap(i, smallest)
            i = smallest

    def insert(self, key: object, priority: float) -> None:
        """Insert a new key with the given priority."""
        self.heap.append([priority, key])
        i = len(self.heap) - 1
        self.position[key] = i
        self._sift_up(i)

    def decrease_key(self, key: object, new_priority: float) -> None:
        """Lower the priority of an existing key, restoring the heap property."""
        i = self.position[key]
        self.heap[i][0] = new_priority
        self._sift_up(i)

    def extract_min(self) -> Tuple[object, float]:
        """Remove and return (key, priority) with the smallest priority."""
        if not self.heap:
            raise IndexError("extract_min from empty priority queue")

        min_priority, min_key = self.heap[0]
        last = self.heap.pop()
        del self.position[min_key]

        if self.heap:
            self.heap[0] = last
            self.position[last[1]] = 0
            self._sift_down(0)

        return min_key, min_priority


if __name__ == "__main__":
    pq = IndexedMinPQ()
    assert len(pq) == 0

    pq.insert("A", 10)
    pq.insert("B", 5)
    pq.insert("C", 20)
    pq.insert("D", 15)

    assert len(pq) == 4
    assert "B" in pq
    assert "Z" not in pq

    key, prio = pq.extract_min()
    assert (key, prio) == ("B", 5)
    assert "B" not in pq
    assert len(pq) == 3

    pq.decrease_key("D", 1)
    key, prio = pq.extract_min()
    assert (key, prio) == ("D", 1)

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
