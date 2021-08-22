from solver.BaseSolver import BaseSolver
from solver.LogicSolver import LogicSolver, ContradictionError


class UniquenessChecker:

    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.unique = True

    def unsolved_fields(self, possible):
        fields = []
        for x in range(9):
            for y in range(9):
                if len(possible[x][y]) > 1:
                    fields.append((x, y))
        return fields

    def first_unsolved(self, possible):
        for x in range(9):
            for y in range(9):
                if len(possible[x][y]) > 1:
                    return x, y

    def unsolved_field_with_smalles_choice(self, possible):
        smallest_choice = 10
        result = None
        for x in range(9):
            for y in range(9):
                len_xy = len(possible[x][y])
                if 1 < len_xy < smallest_choice:
                    smallest_choice = len_xy
                    result = (x, y)
        return result

    def backtracking(self, possible):
        if not self.unique:
            return False

        logic = LogicSolver(possible)
        if logic.solve():
            return True

        x, y = self.unsolved_field_with_smalles_choice(logic.possible)
        hits = 0
        for value in possible[x][y]:
            new_possible = logic.copy_replacing(x, y, value)
            try:
                if self.backtracking(new_possible):
                    hits += 1
            except ContradictionError:
                pass

        if hits > 1:
            self.unique = False
            return True
        elif hits == 1:
            return True
        else:
            return False

    def is_unique(self):
        possibles = BaseSolver.from_sudoku(self.sudoku).possible
        if not self.backtracking(possibles):
            raise ValueError("No valid solution")
        return self.unique

def check_uniqueness(sudoku):
    return UniquenessChecker(sudoku).is_unique()

