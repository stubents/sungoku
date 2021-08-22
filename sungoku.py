#!/usr/bin/env python3

import argparse
import sys
import csv

from creator.SudokuGenerator import SudokuGenerator
from solver.CombinedSolver import CombinedSolver


def solve(sudoku):
    solver = CombinedSolver.from_sudoku(sudoku)
    solver.solve()
    return solver.to_sudoku()


def write_pretty(sudokus):
    for sudoku in sudokus:
        unsolved = str(sudoku).split('\n')
        solved = str(solve(sudoku)).split('\n')
        for i in range(len(unsolved)):
            print(unsolved[i] + '    ' + solved[i])
        print('Number of hints: ' + str(sudoku.number_of_hints()) + '\n\n')


def write_as_csv(sudokus):
    writer = csv.DictWriter(sys.stdout, fieldnames=['quiz', 'answer', 'num_hints'])
    writer.writeheader()
    for sudoku in sudokus:
        writer.writerow({'quiz': sudoku.serialize(),
                         'answer': solve(sudoku).serialize(),
                         'num_hints': sudoku.number_of_hints()})


def create(arguments):
    generated = []
    for _ in range(arguments.number):
        sudoku = SudokuGenerator().generate()
        generated.append(sudoku)

    if arguments.pretty:
        write_pretty(generated)
    else:
        write_as_csv(generated)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help='hello')
    create_parser = subparsers.add_parser('create')
    create_parser.add_argument('-n', '--number', type=int, default=1, help='specifies the number of sudokus to be created')
    create_parser.add_argument('-p', '--pretty', action='store_true', help='prints a formatted field instead of csv')
    create_parser.set_defaults(func=create)
    args = parser.parse_args()
    args.func(args)
