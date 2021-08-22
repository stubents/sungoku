import copy
import unittest
from unittest import TestCase

from Sudoku import Sudoku
from creator.UniquenessChecker import UniquenessChecker
from test.ExampleSudokus import ExampleSudokus


class TestUniquenessChecker(TestCase):
    def test_is_unique_when_unique(self):
        checker = UniquenessChecker(ExampleSudokus.HARD[0])
        res = checker.is_unique()
        self.assertTrue(res)

    def test_is_unique_when_not_unique(self):
        sudoku = Sudoku.deserialize('000000000012034567034506182001058206008600001020007050003705028080060700207083610')
        checker = UniquenessChecker(sudoku)
        res = checker.is_unique()
        self.assertFalse(res)

    def test_is_unique_all_variations_for_high_clue(self):
        sudoku_input = ExampleSudokus.HIGH_CLUE[0]
        self.all_variations(sudoku_input)

    def test_is_unique_all_variations_for_low_clue(self):
        sudoku_input = ExampleSudokus.LOW_CLUE[0]
        self.all_variations(sudoku_input)

    def test_is_unique_all_variations_for_medium(self):
        sudoku_input = ExampleSudokus.MEDIUM[0]
        self.all_variations(sudoku_input)

    def test_is_unique_all_variations_for_hard(self):
        sudoku_input = ExampleSudokus.HARD[0]
        self.all_variations(sudoku_input)

    def all_variations(self, sudoku_input):
        tested_original = False
        for i in range(80, -1, -1):
            sudoku = copy.copy(sudoku_input)
            num = sudoku.sudoku_nums[i]
            sudoku.sudoku_nums[i] = 0
            checker = UniquenessChecker(sudoku)
            if num == 0 and not tested_original:
                self.assertTrue(checker.is_unique())
                tested_original = True
            elif num != 0:
                self.assertFalse(checker.is_unique())
