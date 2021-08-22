from unittest import TestCase

from solver.CombinedSolver import CombinedSolver
from test.ExampleSudokus import ExampleSudokus


class TestCombinedSolver(TestCase):
    def test_solve_solves_easy_quiz(self):
        solver = CombinedSolver.from_sudoku(ExampleSudokus.EASY[0])
        solver.solve()
        self.assertEqual(solver.to_sudoku(), ExampleSudokus.EASY[1])

    def test_solve_solves_medium_quiz(self):
        solver = CombinedSolver.from_sudoku(ExampleSudokus.MEDIUM[0])
        solver.solve()
        self.assertEqual(solver.to_sudoku(), ExampleSudokus.MEDIUM[1])

    def test_solve_solves_hard_quiz(self):
        solver = CombinedSolver.from_sudoku(ExampleSudokus.HARD[0])
        solver.solve()
        self.assertEqual(solver.to_sudoku(), ExampleSudokus.HARD[1])

    def test_solve_solves_very_hard_quiz(self):
        solver = CombinedSolver.from_sudoku(ExampleSudokus.VERY_HARD[0])
        solver.solve()
        self.assertEqual(solver.to_sudoku(), ExampleSudokus.VERY_HARD[1])

    def test_solve_solves_low_clue_quiz(self):
        solver = CombinedSolver.from_sudoku(ExampleSudokus.LOW_CLUE[0])
        solver.solve()
        self.assertEqual(solver.to_sudoku(), ExampleSudokus.LOW_CLUE[1])

    def test_solve_solves_high_clue_quiz(self):
        solver = CombinedSolver.from_sudoku(ExampleSudokus.HIGH_CLUE[0])
        solver.solve()
        self.assertEqual(solver.to_sudoku(), ExampleSudokus.HIGH_CLUE[1])

    def test_solve_solves_any_quiz(self):
        solver = CombinedSolver.from_sudoku(ExampleSudokus.MISC_1[0])
        solver.solve()
        self.assertEqual(solver.to_sudoku(), ExampleSudokus.MISC_1[1])

    def test_solve_solves_all_the_quizzes(self):
        solver = CombinedSolver.from_sudoku(ExampleSudokus.MISC_2[0])
        solver.solve()
        self.assertEqual(solver.to_sudoku(), ExampleSudokus.MISC_2[1])
