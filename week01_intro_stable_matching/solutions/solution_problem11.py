"""
Problem 11 - Queue: Round-Robin CPU Scheduling (SOLUTION)
============================================================
"""

from typing import Any, List, Tuple


class Queue:
    def __init__(self):
        self._data = []

    def enqueue(self, x: Any) -> None:
        self._data.append(x)

    def dequeue(self) -> Any:
        if not self._data:
            raise IndexError("dequeue from empty queue")
        return self._data.pop(0)

    def is_empty(self) -> bool:
        return len(self._data) == 0


def round_robin(tasks: List[Tuple[str, int]], quantum: int) -> List[str]:
    """Return the order in which tasks finish under round-robin scheduling."""
    q = Queue()
    for name, burst in tasks:
        q.enqueue([name, burst])

    finish_order = []
    while not q.is_empty():
        name, remaining = q.dequeue()
        run_time = min(quantum, remaining)
        remaining -= run_time
        if remaining == 0:
            finish_order.append(name)
        else:
            q.enqueue([name, remaining])
    return finish_order


if __name__ == "__main__":
    q = Queue()
    assert q.is_empty() is True
    q.enqueue("a")
    q.enqueue("b")
    assert q.dequeue() == "a"
    q.enqueue("c")
    assert q.dequeue() == "b"
    assert q.dequeue() == "c"
    assert q.is_empty() is True

    tasks = [("A", 5), ("B", 3), ("C", 8)]
    order = round_robin(tasks, quantum=4)
    assert order == ["B", "A", "C"], order

    print("All tests passed!")
