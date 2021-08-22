import copy
from unittest import TestCase

from creator.SudokuGenerator import SudokuGenerator, find_unnecessary_fields, find_random_unnecessary_field
from solver.CombinedSolver import CombinedSolver
from test.ExampleSudokus import ExampleSudokus


class TestSudokuGenerator(TestCase):

    def test_generate_grid(self):
        grid = SudokuGenerator.generate_grid()
        self.assertFalse(grid.has_contradictions())

    def test_find_unnecessary_fields_on_minial_sudoku_returns_nothing(self):
        result = find_unnecessary_fields(ExampleSudokus.LOW_CLUE[0])
        self.assertEqual(len(result), 0)

    def test_find_unnecessary_fields_on_non_minial_sudoku_returns_list(self):
        result = find_unnecessary_fields(ExampleSudokus.EASY[0])
        self.assertNotEqual(len(result), 0)

    def test_find_random_unnecessary_field_on_minial_sudoku_returns_no_valid_index(self):
        result = find_random_unnecessary_field(ExampleSudokus.LOW_CLUE[0])
        self.assertEqual(result, -1)

    def test_find_random_unnecessary_field_on_minial_sudoku_returns_index(self):
        result = find_random_unnecessary_field(ExampleSudokus.EASY[0])
        self.assertTrue(0 <= result <= 80)

    def test_remove_random_number_removes_hint(self):
        generator = SudokuGenerator()
        test_sudoku = copy.copy(ExampleSudokus.EASY[0])
        generator.grid = test_sudoku

        generator.remove_random_number([2, 3, 6])

        self.assertEqual(test_sudoku.number_of_hints(), ExampleSudokus.EASY[0].number_of_hints() - 1)

    def test_generate_sudoku(self):
        generator = SudokuGenerator()

        sudoku = generator.generate()

        self.assertTrue(17 <= sudoku.number_of_hints() <= 40, 'Hints: ' + str(sudoku.number_of_hints()) + '\n' + str(sudoku))
        self.assertTrue(CombinedSolver.from_sudoku(sudoku).solve())
        self.assertFalse(sudoku.has_contradictions())

    def test_minimum_hints(self):
        generator = SudokuGenerator(41)
        sudoku = generator.generate()
        self.assertEqual(sudoku.number_of_hints(), 41)
