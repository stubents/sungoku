from model.Sudoku import Sudoku


class BaseSolver:
    NUM_RANGE = {i for i in range(1, 10)}

    def __init__(self, possibles):
        self.possible = possibles

    @classmethod
    def from_sudoku(cls, sudoku):
        poss = [[BaseSolver.NUM_RANGE for j in range(9)] for i in range(9)]
        for y in range(9):
            for x in range(9):
                if sudoku.get(x, y) != 0:
                    poss[x][y] = {sudoku.get(x, y)}
        return cls(poss)

    def __repr__(self):
        res = ''
        for y in range(9):
            for x in range(9):
                res += str(len(self.possible[x][y]))
                res += ' '
                if x == 8:
                    res += '\n'
                elif x % 3 == 2:
                    res += '| '
            if y % 3 == 2 and y != 8:
                res += '- - - + - - - + - - -\n'
        return res.replace('1', ' ')

    def copy_possibles(self):
        return [[set(self.possible[x][y]) for y in range(9)] for x in range(9)]

    def copy_replacing(self, x, y, value):
        next_possibles = self.copy_possibles()
        next_possibles[x][y] = {value}
        return next_possibles

    def possible_in_section(self, x, y):
        res = []
        ulx = x - (x % 3)
        uly = y - (y % 3)
        for i in range(ulx, ulx + 3):
            for j in range(uly, uly + 3):
                if i != x or j != y:
                    res.append(self.possible_at(i, j))
        return res

    def possible_in_column(self, x, y):
        return [self.possible_at(x, i) for i in range(9) if y != i]

    def possible_in_row(self, x, y):
        return [self.possible_at(i, y) for i in range(9) if x != i]

    def already_excluded(self, x, y):
        excluded = set()
        combined = self.possible_in_section(x, y) + \
                   self.possible_in_row(x, y) + \
                   self.possible_in_column(x, y)
        for field in combined:
            if len(field) == 1:
                excluded.add(list(field)[0])
        return excluded

    def numbers_left_at(self, x, y):
        return len(self.possible[x][y])

    def possible_at(self, x, y):
        return self.possible[x][y]

    def is_solved(self):
        for y in range(9):
            for x in range(9):
                if self.numbers_left_at(x, y) > 1:
                    return False
        return True

    def to_sudoku(self):
        sudoku = Sudoku([0 for i in range(0, 81)])
        for y in range(9):
            for x in range(9):
                p = self.possible_at(x, y)
                if len(p) == 1:
                    sudoku.set_at(x, y, list(p)[0])
        return sudoku
