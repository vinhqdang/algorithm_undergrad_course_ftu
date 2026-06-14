"""
Problem 11 - Queue: Round-Robin CPU Scheduling
================================================

Implement a `Queue` class backed by a Python list with `enqueue`, `dequeue`,
and `is_empty` (FIFO order).

Then implement `round_robin(tasks, quantum)`, where `tasks` is a list of
(name, burst_time) pairs. Simulate round-robin scheduling: repeatedly dequeue
a task, run it for up to `quantum` time units, and if it still has remaining
time, enqueue it again at the back. Return the order in which tasks FINISH
(a list of names, in finishing order).

See practical_exercises.pdf, Problem 11.
"""

from typing import Any, List, Tuple


class Queue:
    def __init__(self):
        self._data = []

    def enqueue(self, x: Any) -> None:
        # TODO: implement.
        raise NotImplementedError

    def dequeue(self) -> Any:
        # TODO: implement. Raise IndexError if empty.
        raise NotImplementedError

    def is_empty(self) -> bool:
        # TODO: implement.
        raise NotImplementedError


def round_robin(tasks: List[Tuple[str, int]], quantum: int) -> List[str]:
    """Return the order in which tasks finish under round-robin scheduling."""
    # TODO: implement using Queue.
    raise NotImplementedError


if __name__ == "__main__":
    try:
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
        # B finishes first (3 <= 4), then A (5 = 4+1, finishes on its 2nd turn
        # before C's 2nd turn), then C (8 = 4+4).
        assert order == ["B", "A", "C"], order

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
