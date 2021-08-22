from unittest import TestCase

from solver.NaiveSolver import NaiveSolver
from test.ExampleSudokus import ExampleSudokus


class TestNaiveSolver(TestCase):
    def test_solve_solves_easy_quiz(self):
        solver = NaiveSolver.from_sudoku(ExampleSudokus.EASY[0])
        solver.solve()
        self.assertEqual(solver.to_sudoku(), ExampleSudokus.EASY[1])

    def test_solve_gives_up_on_hard_quiz(self):
        solver = NaiveSolver.from_sudoku(ExampleSudokus.HARD[0])
        self.assertFalse(solver.solve())
