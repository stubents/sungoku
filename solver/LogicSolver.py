from solver.BaseSolver import BaseSolver


class LogicSolver(BaseSolver):

    @staticmethod
    def find_excluded(possible_list):
        excluded = set()
        possible_for_others = set()
        for possible in possible_list:
            if len(possible) == 1:
                excluded = excluded | possible
            possible_for_others = possible_for_others | possible
        return excluded if len(possible_for_others) == 9 else excluded | possible_for_others

    @staticmethod
    def find_excluded2(possible_list):
        excluded = [False for _ in range(9)]
        possible_for_others = [False for _ in range(9)]
        for possible in possible_list:
            for p in possible:
                if len(possible) == 1:
                    excluded[p - 1] = True
                possible_for_others[p - 1] = True

        num_possible_for_others = 0
        for i in range(9):
            if possible_for_others[i]:
                num_possible_for_others += 1
        if num_possible_for_others == 9:
            res = set()
            for i in range(9):
                if excluded[i]:
                    res.add(i + 1)
            return res

        res = set()
        for i in range(9):
            if excluded[i] or possible_for_others[i]:
                res.add(i + 1)
        return res


    def progress_at(self, x, y):
        numbers_left = self.numbers_left_at(x, y)
        if numbers_left == 1:
            return False

        excluded = self.find_excluded(self.possible_in_column(x, y)) | \
                   self.find_excluded(self.possible_in_row(x, y)) | \
                   self.find_excluded(self.possible_in_section(x, y))

        new_possible = self.NUM_RANGE - excluded
        if len(new_possible) == 0:
            raise ContradictionError("Contradiction in possible states")
        assert 1 <= len(new_possible)
        assert len(new_possible) <= numbers_left

        if len(new_possible) < numbers_left:
            self.possible[x][y] = new_possible
            if len(new_possible) == 1:
                pass
                #print(self.to_sudoku())
                #time.sleep(0.1)
            return True
        else:
            return False

    def next_round(self):
        progress = False
        for y in range(9):
            for x in range(9):
                if self.progress_at(x, y):
                    progress = True
        return progress

    def solve(self):
        progress = True
        while progress:
            progress = self.next_round()
        return self.is_solved()


class ContradictionError(ValueError):
    pass
