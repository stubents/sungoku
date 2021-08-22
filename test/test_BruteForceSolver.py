from unittest import TestCase

from solver.BruteForceSolver import BruteForceSolver
from test.ExampleSudokus import ExampleSudokus


class TestBruteForceSolver(TestCase):
    def test_solve_solves_easy_quiz(self):
        solver = BruteForceSolver.from_sudoku(ExampleSudokus.EASY[0])
        solver.solve()
        self.assertEqual(solver.to_sudoku(), ExampleSudokus.EASY[1])

    def test_solve_solves_medium_quiz(self):
        solver = BruteForceSolver.from_sudoku(ExampleSudokus.MEDIUM[0])
        solver.solve()
        self.assertEqual(solver.to_sudoku(), ExampleSudokus.MEDIUM[1])

    def test_solve_solves_hard_quiz(self):
        solver = BruteForceSolver.from_sudoku(ExampleSudokus.HARD[0])
        solver.solve()
        self.assertEqual(solver.to_sudoku(), ExampleSudokus.HARD[1])
