import random

from model.Sudoku import Sudoku
from creator.UniquenessChecker import UniquenessChecker
from solver.BruteForceSolver import BruteForceSolver


class SudokuGenerator:

    def __init__(self, minimum_hints=0):
        self.minimum_hints = minimum_hints
        self.grid = self.generate_grid()
        self.fast_lane_initial_remove = 35

    @staticmethod
    def generate_grid():
        grid = Sudoku([0 for _ in range(81)])
        solver = BruteForceSolver.from_sudoku(grid)
        solver.random_guessing = True
        solver.solve()
        return solver.to_sudoku()

    def remove_fast_path(self):
        for i in range(self.fast_lane_initial_remove, -1, -1):
            nums = list(self.grid.sudoku_nums)
            to_remove_idx = random.sample([i for i in range(81)], i)
            left_over_nums = []
            for j in range(81):
                left_over_nums.append(0 if j in to_remove_idx else nums[j])
            new_sudoku = Sudoku(left_over_nums)
            if UniquenessChecker(new_sudoku).is_unique():
                self.grid = new_sudoku
                return

    def generate(self):
        self.remove_fast_path()
        unnecessary = find_random_unnecessary_field(self.grid)
        while not unnecessary == -1 and self.grid.number_of_hints() > self.minimum_hints:
            self.grid.sudoku_nums[unnecessary] = 0
            unnecessary = find_random_unnecessary_field(self.grid)
        return self.grid

    def remove_random_number(self, removable_indexes):
        remove = random.choice(removable_indexes)
        self.grid.sudoku_nums[remove] = 0


def find_unnecessary_fields(sudoku):
    unnecessary = []
    for i in range(81):
        num = sudoku.sudoku_nums[i]
        if num != 0:
            fields = list(sudoku.sudoku_nums)
            fields[i] = 0
            smaller_sudoku = Sudoku(fields)
            checker = UniquenessChecker(smaller_sudoku)
            if checker.is_unique():
                unnecessary.append(i)
    return unnecessary


def find_random_unnecessary_field(sudoku):
    shuffled_indexes = [i for i in range(81)]
    random.shuffle(shuffled_indexes)
    for i in shuffled_indexes:
        num = sudoku.sudoku_nums[i]
        if num != 0:
            fields = list(sudoku.sudoku_nums)
            fields[i] = 0
            smaller_sudoku = Sudoku(fields)
            checker = UniquenessChecker(smaller_sudoku)
            if checker.is_unique():
                return i
    return -1
