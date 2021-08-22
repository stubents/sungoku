from solver.BaseSolver import BaseSolver
from solver.BruteForceSolver import BruteForceSolver
from solver.LogicSolver import LogicSolver


class CombinedSolver(BaseSolver):

    def next_step(self, possibles):
        solver = LogicSolver(possibles)
        try:
            solver.solve()
        except ValueError:
            return False
        if not solver.is_solved():
            backtracking = BruteForceSolver(solver.copy_possibles(), True)
            return backtracking.progress(self.next_step)
        else:
            self.possible = solver.possible
            return True

    def solve(self):
        return self.next_step(self.possible)
