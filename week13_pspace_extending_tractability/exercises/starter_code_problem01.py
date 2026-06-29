"""
Problem 01 - Evaluate a Fully-Quantified Boolean Formula (QBF)
==============================================================

Implement `eval_qbf(formula, env)` that recursively evaluates a quantified
boolean formula and returns True or False. The formula is built from the node
classes in starter_code.py: Const, Var, Not, And, Or, Quant.

A Quant('A', var, body) is "forall var. body"; Quant('E', var, body) is
"exists var. body". Evaluate by trying var = False and var = True, recursing
into body, and combining with all(...) for forall or any(...) for exists.
A fully-quantified formula (every variable bound) evaluates to a single bool.

This is the canonical PSPACE-complete problem (QSAT / TQBF) restricted to the
recursive evaluation step. See practical_exercises.pdf, Problem 1.
"""

import os
import sys
from typing import Dict

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from starter_code import And, Const, Not, Or, Quant, Var  # noqa: E402


def eval_qbf(formula, env: Dict[str, bool] | None = None) -> bool:
    """Recursively evaluate a (quantified) boolean formula to True/False."""
    # TODO: implement this function.
    raise NotImplementedError


if __name__ == "__main__":
    try:
        assert eval_qbf(Quant("E", "x", Var("x"))) is True
        assert eval_qbf(Quant("A", "x", Var("x"))) is False
        assert eval_qbf(Quant("A", "x", Or(Var("x"), Not(Var("x"))))) is True
        biconditional = Or(And(Var("x"), Var("y")), And(Not(Var("x")), Not(Var("y"))))
        assert eval_qbf(Quant("A", "x", Quant("E", "y", biconditional))) is True
        assert eval_qbf(Quant("E", "x", Quant("A", "y", biconditional))) is False
        assert eval_qbf(Quant("A", "x", Quant("E", "y", And(Var("x"), Var("y"))))) is False
        assert eval_qbf(Const(True)) is True
        assert eval_qbf(And()) is True
        assert eval_qbf(Or()) is False

        print("All tests passed!")
    except NotImplementedError:
        print("TODO: implement the functions above.")
