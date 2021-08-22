
import time
import random

from Sudoku import Sudoku
from solver.BaseSolver import BaseSolver


class BruteForceSolver(BaseSolver):

    def __init__(self, possibles, find_smallest_choice=False, random_guessing=False):
        super().__init__(possibles)
        self.find_smallest_choice = find_smallest_choice #todo: not needed
        self.random_guessing=random_guessing

    def next_field(self):
        lowest = 10
        lx = -1
        ly = -1
        for y in range(9):
            for x in range(9):
                nums = self.numbers_left_at(x, y)
                if 1 < nums and not self.find_smallest_choice:
                    return x, y
                if 1 < nums < lowest:
                    lx = x
                    ly = y
                    lowest = nums
        return lx, ly

    def keep_guessing(self, next_possibles):
        next_try = BruteForceSolver(next_possibles,
                                    find_smallest_choice=self.find_smallest_choice,
                                    random_guessing=self.random_guessing)
        if next_try.progress(next_try.keep_guessing):
            self.possible = next_try.possible
            return True
        return False

    def progress(self, next_step):
        if self.is_solved():
            return True
        lx, ly = self.next_field()
        possible_here = list(self.possible_at(lx, ly))
        if self.random_guessing:
            random.shuffle(possible_here)
        for guess in possible_here:
            if guess not in self.already_excluded(lx, ly):
                next_possibles = self.copy_replacing(lx, ly, guess)
                if next_step(next_possibles):
                    return True
        return False

    def solve(self):
        return self.progress(self.keep_guessing)
