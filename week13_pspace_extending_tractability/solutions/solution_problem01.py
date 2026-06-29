"""
Problem 01 - Evaluate a Fully-Quantified Boolean Formula (QBF) (SOLUTION)
=========================================================================
"""

import os
import sys
from typing import Dict

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import And, Const, Not, Or, Quant, Var  # noqa: E402


def eval_qbf(formula, env: Dict[str, bool] | None = None) -> bool:
    """Recursively evaluate a (quantified) boolean formula to True/False."""
    if env is None:
        env = {}
    if isinstance(formula, Const):
        return formula.value
    if isinstance(formula, Var):
        return env[formula.name]
    if isinstance(formula, Not):
        return not eval_qbf(formula.child, env)
    if isinstance(formula, And):
        return all(eval_qbf(c, env) for c in formula.children)
    if isinstance(formula, Or):
        return any(eval_qbf(c, env) for c in formula.children)
    if isinstance(formula, Quant):
        outcomes = []
        for value in (False, True):
            env[formula.var] = value
            outcomes.append(eval_qbf(formula.body, env))
        del env[formula.var]
        return all(outcomes) if formula.kind == "A" else any(outcomes)
    raise TypeError(f"unknown node type: {type(formula)}")


if __name__ == "__main__":
    # exists x. x  -> True
    assert eval_qbf(Quant("E", "x", Var("x"))) is True
    # forall x. x  -> False
    assert eval_qbf(Quant("A", "x", Var("x"))) is False
    # forall x. (x or not x) -> True (tautology)
    assert eval_qbf(Quant("A", "x", Or(Var("x"), Not(Var("x"))))) is True
    # forall x. exists y. (x == y), i.e. x<->y: True
    biconditional = Or(And(Var("x"), Var("y")), And(Not(Var("x")), Not(Var("y"))))
    assert eval_qbf(Quant("A", "x", Quant("E", "y", biconditional))) is True
    # exists x. forall y. (x == y): False
    assert eval_qbf(Quant("E", "x", Quant("A", "y", biconditional))) is False
    # forall x. exists y. (x and y): False (need x and y true, but x ranges over False)
    assert eval_qbf(Quant("A", "x", Quant("E", "y", And(Var("x"), Var("y"))))) is False
    # constants
    assert eval_qbf(Const(True)) is True
    assert eval_qbf(And()) is True   # empty And
    assert eval_qbf(Or()) is False   # empty Or

    print("All tests passed!")
