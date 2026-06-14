"""
Problem 15 - Dynamic Array with Doubling: Amortized Analysis
===============================================================

Implement `DynamicArray`, a simple dynamic array (manual resizing, no use of
Python's built-in list growth) with:

  - `__init__(self, initial_capacity=1)`: starts with `self.capacity =
    initial_capacity`, `self.size = 0`, and `self.data = [None] *
    self.capacity`. Also `self.copy_ops = 0` (total number of element copies
    performed across all resizes).

  - `append(x)`: if `self.size == self.capacity`, first *resize*: create a
    new array of capacity `2 * self.capacity`, copy all `self.size` existing
    elements into it (incrementing `self.copy_ops` by `self.size` for this
    resize), and replace `self.data`. Then store `x` at index `self.size`
    and increment `self.size`.

  - `__len__`: returns `self.size`.

  - `__getitem__(i)`: returns `self.data[i]` (no bounds re-check needed
    beyond what Python gives you, but `i` should be `< self.size`).

Then implement `total_copy_ops(n)` that creates a fresh `DynamicArray()`
(starting capacity 1), appends `n` items, and returns `self.copy_ops`.

**What you should observe.** Resizes happen when size passes 1, 2, 4, 8, ...
(powers of two), so the total number of copies is
`1 + 2 + 4 + ... + 2^(k-1)` where `2^k` is the smallest power of two `>= n`,
which is `< 2n`. Hence the *total* cost of `n` appends is `O(n)`, i.e. each
append costs `O(1)` *amortized*, even though individual appends that trigger
a resize cost `O(size)`.

See practical_exercises.pdf, Problem 15.
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
        # TODO: implement this method.
        raise NotImplementedError


def total_copy_ops(n: int) -> int:
    """Create a fresh DynamicArray(), append n items, return self.copy_ops."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        arr = DynamicArray()
        for i in range(10):
            arr.append(i)
        assert len(arr) == 10
        assert [arr[i] for i in range(10)] == list(range(10))

        # 10 appends starting from capacity 1: resizes at sizes 1,2,4,8
        # (i.e. when appending the 2nd, 3rd, 5th, 9th elements), copying
        # 1, 2, 4, 8 elements respectively -> total copy_ops = 1+2+4+8 = 15.
        assert arr.copy_ops == 15, arr.copy_ops

        for n in [1, 2, 5, 10, 100, 1000]:
            ops = total_copy_ops(n)
            assert ops < 2 * n, (n, ops)  # O(n) total, i.e. < 2n copies

        # copy_ops is monotonically non-decreasing in n.
        prev = -1
        for n in [1, 2, 4, 8, 16, 32]:
            ops = total_copy_ops(n)
            assert ops >= prev
            prev = ops

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
