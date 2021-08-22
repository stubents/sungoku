#!/usr/bin/env python3

import argparse
import sys
import csv

from Sudoku import Sudoku
from creator.SudokuGenerator import SudokuGenerator
from solver.CombinedSolver import CombinedSolver

csv_writer = None


def solve(sudoku):
    solver = CombinedSolver.from_sudoku(sudoku)
    solver.solve()
    return solver.to_sudoku()


def merge_string_lists(first, second):
    max_length = max([len(first), len(second)])
    result = []
    for i in range(max_length):
        if i < len(first) and i < len(second):
            result.append(first[i] + '       ' + second[i])
        elif i < len(first):
            result.append(first[i])
        else:
            result.append(second[i])
    return result


def write_pretty(unsolved, solved):
    unsolved_lines = str(unsolved).splitlines() if unsolved is not None else []
    solved_lines = str(solved).splitlines() if solved is not None else []
    for line in merge_string_lists(unsolved_lines, solved_lines):
        print(line)
    if unsolved is not None:
        print('\nNumber of hints: ' + str(unsolved.number_of_hints()))
    print('\n')


def get_csv_writer(unsolved, solved):
    global csv_writer
    if csv_writer is None:
        columns = []
        if unsolved is not None:
            columns.extend(['quiz', 'num_hints'])
        if solved is not None:
            columns.append('answer')
        csv_writer = csv.DictWriter(sys.stdout, fieldnames=columns, extrasaction='ignore')
        csv_writer.writeheader()
    return csv_writer


def write_as_csv(unsolved, solved):
    writer = get_csv_writer(unsolved, solved)
    writer.writerow({'quiz': unsolved.serialize() if unsolved is not None else '',
                     'num_hints': unsolved.number_of_hints() if unsolved is not None else '',
                     'answer': solved.serialize() if solved is not None else ''})


def create(arguments):
    for _ in range(arguments.number):
        generated = SudokuGenerator().generate()

        if arguments.pretty:
            write_pretty(generated, None)
        else:
            write_as_csv(generated, None)


def solve_input(arguments):
    reader = csv.DictReader(sys.stdin)
    for row in reader:
        unsolved = Sudoku.deserialize(row['quiz'])
        solved = solve(unsolved)
        if arguments.pretty:
            write_pretty(unsolved if arguments.include_quiz else None, solved)
        else:
            write_as_csv(unsolved if arguments.include_quiz else None, solved)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help='hello')
    create_parser = subparsers.add_parser('create')
    create_parser.add_argument('-n', '--number', type=int, default=1, help='specifies the number of sudokus to be created')
    create_parser.add_argument('-p', '--pretty', action='store_true', help='prints a formatted field instead of csv')
    create_parser.set_defaults(func=create)

    solve_parser = subparsers.add_parser('solve')
    solve_parser.add_argument('-p', '--pretty', action='store_true', help='prints a formatted field instead of csv')
    solve_parser.add_argument('-i', '--include-quiz', action='store_true', help='Includes the unsolved sudoku in the output')
    solve_parser.set_defaults(func=solve_input)

    args = parser.parse_args()
    args.func(args)
