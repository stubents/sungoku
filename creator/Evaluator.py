from solver.CombinedSolver import CombinedSolver
from solver.LogicSolver import LogicSolver
from solver.NaiveSolver import NaiveSolver


def evaluate_difficultly(sudoku):
    if NaiveSolver.from_sudoku(sudoku).solve():
        return 'EASY'
    elif LogicSolver.from_sudoku(sudoku).solve():
        return 'MEDIUM'
    elif CombinedSolver.from_sudoku(sudoku).solve():
        return 'HARD'
    return 'UNKNOWN'
