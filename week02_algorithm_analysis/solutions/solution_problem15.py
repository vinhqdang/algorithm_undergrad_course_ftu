"""
Problem 15 - Dynamic Array with Doubling: Amortized Analysis (SOLUTION)
==========================================================================
"""

from typing import List, Optional


class DynamicArray:
    def __init__(self, initial_capacity: int = 1) -> None:
        self.capacity = initial_capacity
        self.size = 0
        self.data: List[Optional[int]] = [None] * self.capacity
        self.copy_ops = 0

    def __len__(self) -> int:
        return self.size

    def __getitem__(self, i: int) -> int:
        return self.data[i]

    def append(self, x: int) -> None:
        """Append x, resizing (doubling capacity) if necessary."""
        if self.size == self.capacity:
            new_capacity = 2 * self.capacity
            new_data: List[Optional[int]] = [None] * new_capacity
            for i in range(self.size):
                new_data[i] = self.data[i]
                self.copy_ops += 1
            self.data = new_data
            self.capacity = new_capacity

        self.data[self.size] = x
        self.size += 1


def total_copy_ops(n: int) -> int:
    """Create a fresh DynamicArray(), append n items, return self.copy_ops."""
    arr = DynamicArray()
    for i in range(n):
        arr.append(i)
    return arr.copy_ops


if __name__ == "__main__":
    arr = DynamicArray()
    for i in range(10):
        arr.append(i)
    assert len(arr) == 10
    assert [arr[i] for i in range(10)] == list(range(10))

    assert arr.copy_ops == 15, arr.copy_ops

    for n in [1, 2, 5, 10, 100, 1000]:
        ops = total_copy_ops(n)
        assert ops < 2 * n, (n, ops)

    prev = -1
    for n in [1, 2, 4, 8, 16, 32]:
        ops = total_copy_ops(n)
        assert ops >= prev
        prev = ops

    print("All tests passed!")
