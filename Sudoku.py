class Sudoku:
    def __init__(self, sudoku_nums):
        assert len(sudoku_nums) == 81
        self.sudoku_nums = sudoku_nums

    def __repr__(self):
        res = ''
        for y in range(9):
            for x in range(9):
                res += str(self.get(x, y))
                res += ' '
                if x == 8:
                    res += '\n'
                elif x % 3 == 2:
                    res += '| '
            if y % 3 == 2 and y != 8:
                res += '- - - + - - - + - - -\n'
        return res.replace('0', ' ')

    def __eq__(self, other):
        if isinstance(other, Sudoku):
            return self.sudoku_nums == other.sudoku_nums
        return False

    def __copy__(self):
        return Sudoku(list(self.sudoku_nums))

    def serialize(self):
        res = ''
        for num in self.sudoku_nums:
            res += str(num)
        return res

    @classmethod
    def deserialize(cls, sudoku_str):
        assert len(sudoku_str) == 81
        nums = []
        for char in sudoku_str:
            nums.append(int(char))
        return Sudoku(nums)

    def get(self, x, y):
        return self.sudoku_nums[y * 9 + x]

    def set_at(self, x, y, value):
        self.sudoku_nums[y * 9 + x] = value

    def number_of_hints(self):
        return sum(map(lambda el: 1 if el > 0 else 0, self.sudoku_nums))

    def hints_in_block(self, x, y):
        res = set()
        ulx = x - (x % 3)
        uly = y - (y % 3)
        for i in range(ulx, ulx + 3):
            for j in range(uly, uly + 3):
                if i != x or j != y:
                    res.add(self.get(i, j))
        return res

    def hints_in_column(self, x, y):
        return {self.get(x, i) for i in range(9) if y != i}

    def hints_in_row(self, x, y):
        return {self.get(i, y) for i in range(9) if x != i}

    def has_contradictions(self):
        for x in range(9):
            for y in range(9):
                num = self.get(x, y)
                if num != 0 and num in self.hints_in_row(x, y) |\
                        self.hints_in_column(x, y) |\
                        self.hints_in_block(x, y):
                    return True
        return False

