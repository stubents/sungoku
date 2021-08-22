from solver.BaseSolver import BaseSolver
from solver.BruteForceSolver import BruteForceSolver


class OptimizedBruteForceSolver(BaseSolver):

    def solve(self):
        for y in range(9):
            for x in range(9):
                self.possible[x][y] = self.possible[x][y] - self.already_excluded(x, y)
        bfs = BruteForceSolver(self.possible)
        solved = bfs.solve()
        self.possible = bfs.possible
        return solved
