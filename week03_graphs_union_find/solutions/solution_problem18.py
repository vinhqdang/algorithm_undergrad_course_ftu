"""
Problem 18 - Quick-Find (Eager Union-Find) (SOLUTION)
========================================================
"""


class QuickFind:
    def __init__(self, n: int) -> None:
        self.id_ = list(range(n))
        self.find_calls = 0
        self.union_relabels = 0

    def find(self, p: int) -> int:
        """Return the component id of p. O(1)."""
        self.find_calls += 1
        return self.id_[p]

    def union(self, p: int, q: int) -> None:
        """Merge the components containing p and q. O(n)."""
        pid, qid = self.find(p), self.find(q)
        if pid == qid:
            return
        for i in range(len(self.id_)):
            if self.id_[i] == pid:
                self.id_[i] = qid
                self.union_relabels += 1

    def connected(self, p: int, q: int) -> bool:
        """Return True iff p and q are in the same component."""
        return self.find(p) == self.find(q)


if __name__ == "__main__":
    uf = QuickFind(10)

    for i in range(10):
        assert uf.find(i) == i

    uf.union(4, 3)
    uf.union(3, 8)
    uf.union(6, 5)
    uf.union(9, 4)
    uf.union(2, 1)

    assert uf.connected(4, 8) is True
    assert uf.connected(3, 9) is True
    assert uf.connected(4, 9) is True
    assert uf.connected(1, 2) is True
    assert uf.connected(0, 7) is False
    assert uf.connected(5, 6) is True

    uf.union(5, 0)
    uf.union(7, 2)
    uf.union(6, 1)

    assert uf.connected(0, 6) is True
    assert uf.connected(1, 5) is True
    assert uf.connected(9, 3) is True

    assert uf.find_calls > 0

    print("All tests passed!")
