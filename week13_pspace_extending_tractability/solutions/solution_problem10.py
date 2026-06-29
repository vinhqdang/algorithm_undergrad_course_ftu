"""
Problem 10 - 2-SAT in Polynomial Time (SOLUTION)
=================================================

2-SAT is solvable in linear time via the implication graph: each clause
(a OR b) becomes two implications (NOT a -> b) and (NOT b -> a). The formula
is satisfiable iff no variable x and its negation NOT x lie in the same
strongly connected component. We use Kosaraju's algorithm for SCCs and read
off an assignment by SCC order.
"""

import os
import sys
from typing import Dict, List, Optional

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import cnf_is_satisfied, generate_2sat  # noqa: E402


def _node(lit: int, num_vars: int) -> int:
    """Map literal +v -> index, -v -> index for NOT v. Vars are 1..num_vars.

    Node 2*(v-1) represents 'v is True'; node 2*(v-1)+1 represents 'v is False'.
    """
    v = abs(lit)
    base = 2 * (v - 1)
    return base if lit > 0 else base + 1


def two_sat(num_vars: int, clauses: List[List[int]]) -> Optional[Dict[int, bool]]:
    """Return a satisfying assignment {var: bool}, or None if unsatisfiable."""
    N = 2 * num_vars
    graph: List[List[int]] = [[] for _ in range(N)]
    rgraph: List[List[int]] = [[] for _ in range(N)]

    def add_impl(a: int, b: int):
        graph[a].append(b)
        rgraph[b].append(a)

    for clause in clauses:
        a, b = clause
        # (a OR b): (NOT a -> b) and (NOT b -> a)
        na = _node(-a, num_vars)
        nb = _node(-b, num_vars)
        pa = _node(a, num_vars)
        pb = _node(b, num_vars)
        add_impl(na, pb)
        add_impl(nb, pa)

    # Kosaraju: first pass to get finish order.
    visited = [False] * N
    order: List[int] = []

    def dfs1(start):
        stack = [(start, iter(graph[start]))]
        visited[start] = True
        while stack:
            node, it = stack[-1]
            advanced = False
            for nb in it:
                if not visited[nb]:
                    visited[nb] = True
                    stack.append((nb, iter(graph[nb])))
                    advanced = True
                    break
            if not advanced:
                order.append(node)
                stack.pop()

    for i in range(N):
        if not visited[i]:
            dfs1(i)

    # Second pass on reverse graph in reverse finish order.
    comp = [-1] * N
    c = 0
    for node in reversed(order):
        if comp[node] == -1:
            stack = [node]
            comp[node] = c
            while stack:
                u = stack.pop()
                for w in rgraph[u]:
                    if comp[w] == -1:
                        comp[w] = c
                        stack.append(w)
            c += 1

    assignment: Dict[int, bool] = {}
    for v in range(1, num_vars + 1):
        true_node = 2 * (v - 1)
        false_node = true_node + 1
        if comp[true_node] == comp[false_node]:
            return None  # x and NOT x in same SCC -> unsatisfiable
        # In Kosaraju the component numbered later is topologically earlier;
        # choose the literal whose component index is larger.
        assignment[v] = comp[true_node] > comp[false_node]
    return assignment


if __name__ == "__main__":
    # Satisfiable: (x1 OR x2) AND (NOT x1 OR x2) AND (NOT x2 OR x3)
    clauses = [[1, 2], [-1, 2], [-2, 3]]
    asg = two_sat(3, clauses)
    assert asg is not None and cnf_is_satisfied(clauses, asg)

    # Unsatisfiable: forces x1 true and false.
    # (x1) AND (NOT x1): encode each as a clause with both literals equal.
    unsat = [[1, 1], [-1, -1]]
    assert two_sat(1, unsat) is None

    # Classic UNSAT 2-SAT chain.
    unsat2 = [[1, 2], [1, -2], [-1, 2], [-1, -2]]
    assert two_sat(2, unsat2) is None

    # Randomized cross-check against brute force over all 2^n assignments.
    import itertools

    def brute_force_sat(num_vars, clauses):
        for bits in itertools.product([False, True], repeat=num_vars):
            asg = {i + 1: bits[i] for i in range(num_vars)}
            if cnf_is_satisfied(clauses, asg):
                return True
        return False

    for seed in range(300):
        nv = 6
        cl = generate_2sat(num_vars=nv, num_clauses=8, seed=seed)
        res = two_sat(nv, cl)
        bf_sat = brute_force_sat(nv, cl)
        # Satisfiability decision must match brute force.
        assert (res is not None) == bf_sat, (seed, cl)
        if res is not None:
            assert cnf_is_satisfied(cl, res), (seed, cl, res)

    print("All tests passed!")
