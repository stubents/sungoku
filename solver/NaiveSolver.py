from solver.BaseSolver import BaseSolver
from solver.LogicSolver import ContradictionError


class NaiveSolver(BaseSolver):

    def solve(self):
        progress = True
        while progress:
            progress = False
            for x in range(9):
                for y in range(9):
                    if self.progress_at(x, y):
                        progress = True
        return self.is_solved()

    def progress_at(self, x, y):
        numbers_left = self.numbers_left_at(x, y)
        if numbers_left == 1:
            return False
        self.possible[x][y] = self.possible[x][y] - self.already_excluded(x, y)
        new_length = self.numbers_left_at(x, y)
        if new_length == 0:
            raise ContradictionError("Contradiction in possible states")
        assert 1 <= new_length
        assert new_length <= numbers_left
        if new_length < numbers_left:
            return True
        return False
