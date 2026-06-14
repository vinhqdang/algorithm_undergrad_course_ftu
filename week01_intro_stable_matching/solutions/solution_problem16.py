"""
Problem 16 - Binary Min-Heap and Heapsort (SOLUTION)
=======================================================
"""

from typing import List


class MinHeap:
    def __init__(self):
        self.data: List[int] = []

    def push(self, x: int) -> None:
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
        if not self.data:
            raise IndexError("pop from empty heap")
        top = self.data[0]
        last = self.data.pop()
        if self.data:
            self.data[0] = last
            i = 0
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
        return top

    def __len__(self) -> int:
        return len(self.data)


def heapsort(arr: List[int]) -> List[int]:
    """Return a new sorted list using MinHeap."""
    h = MinHeap()
    for x in arr:
        h.push(x)
    return [h.pop() for _ in range(len(h))]


if __name__ == "__main__":
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
