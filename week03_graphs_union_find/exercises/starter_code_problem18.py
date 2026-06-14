"""
Problem 18 - Quick-Find (Eager Union-Find)
=============================================

Implement `QuickFind`, a disjoint-set data structure over elements
`0, 1, ..., n-1` using the QUICK-FIND strategy:

  - Maintain an array `id_` of length n, where `id_[i]` is the "component
    id" (representative) of element `i`. Initially `id_[i] == i` for all i.
  - `find(p)`: return `id_[p]` -- O(1).
  - `union(p, q)`: if `find(p) != find(q)`, relabel EVERY element whose id
    equals `id_[p]` to have id `id_[q]` instead -- O(n) per union.
  - `connected(p, q)`: return `find(p) == find(q)` -- O(1).

Also track `self.find_calls` and `self.union_relabels` (total number of
elements relabeled across all `union` calls), so Problem 21 can compare
QuickFind against other strategies empirically.

See practical_exercises.pdf, Problem 18.
"""


class QuickFind:
    def __init__(self, n: int) -> None:
        self.id_ = list(range(n))
        self.find_calls = 0
        self.union_relabels = 0

    def find(self, p: int) -> int:
        """Return the component id of p. O(1)."""
        # TODO: implement this method.
        raise NotImplementedError

    def union(self, p: int, q: int) -> None:
        """Merge the components containing p and q. O(n)."""
        # TODO: implement this method.
        raise NotImplementedError

    def connected(self, p: int, q: int) -> bool:
        """Return True iff p and q are in the same component."""
        return self.find(p) == self.find(q)


if __name__ == "__main__":
    try:
        uf = QuickFind(10)

        # Initially, every element is its own component.
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

        # Now {4,3,8,9,5,6,0,1,2,7} should mostly be connected via unions.
        assert uf.connected(0, 6) is True
        assert uf.connected(1, 5) is True  # 1-2-7 ... 6-5, and 6 unioned with 1
        assert uf.connected(9, 3) is True  # 9-4-3-8 were unioned earlier

        # find_calls should reflect the number of find() calls made above
        assert uf.find_calls > 0

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
