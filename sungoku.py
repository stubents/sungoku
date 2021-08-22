#!/usr/bin/env python3

import argparse
import csv
import sys

from Sudoku import Sudoku
from creator.Evaluator import evaluate_difficultly
from creator.SudokuGenerator import SudokuGenerator, find_random_unnecessary_field
from creator.UniquenessChecker import check_uniqueness
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


def is_unique(sudoku):
    return 'yes' if check_uniqueness(sudoku) else 'no'


def is_minimal(sudoku):
    return 'yes' if find_random_unnecessary_field(sudoku) == -1 else 'no'


def write_pretty(unsolved, solved, analyse=False):
    unsolved_lines = str(unsolved).splitlines() if unsolved is not None else []
    solved_lines = str(solved).splitlines() if solved is not None else []
    for line in merge_string_lists(unsolved_lines, solved_lines):
        print(line)
    if unsolved is not None:
        print('\nNumber of hints: ' + str(unsolved.number_of_hints()))
        print('Difficulty: ' + str(evaluate_difficultly(unsolved)))
    if analyse:
        print('Unique: ' + is_unique(unsolved))
        print('Minimal: ' + is_minimal(unsolved))
    print('\n')


def get_csv_writer(unsolved, solved, analyse=False):
    global csv_writer
    if csv_writer is None:
        columns = []
        if unsolved is not None:
            columns.extend(['quiz', 'num_hints', 'difficulty'])
        if analyse:
            columns.extend(['unique', 'minimal'])
        if solved is not None:
            columns.append('answer')
        csv_writer = csv.DictWriter(sys.stdout, fieldnames=columns, extrasaction='ignore')
        csv_writer.writeheader()
    return csv_writer


def write_as_csv(unsolved, solved, analyse=False):
    writer = get_csv_writer(unsolved, solved, analyse)
    writer.writerow({'quiz': unsolved.serialize() if unsolved is not None else '',
                     'num_hints': unsolved.number_of_hints() if unsolved is not None else '',
                     'difficulty': evaluate_difficultly(unsolved) if unsolved is not None else '',
                     'unique': is_unique(unsolved) if analyse and unsolved is not None else '',
                     'minimal': is_minimal(unsolved) if analyse and unsolved is not None else '',
                     'answer': solved.serialize() if solved is not None else ''})


def create(arguments):
    for _ in range(arguments.number):
        generated = SudokuGenerator(arguments.min_hints).generate()

        if arguments.pretty:
            write_pretty(generated, None)
        else:
            write_as_csv(generated, None)


def solve_input(arguments):
    reader = csv.DictReader(sys.stdin)
    include = arguments.include_quiz or arguments.analyse
    for row in reader:
        unsolved = Sudoku.deserialize(row['quiz'])
        solved = solve(unsolved)
        if arguments.pretty:
            write_pretty(unsolved if include else None, solved, arguments.analyse)
        else:
            write_as_csv(unsolved if include else None, solved, arguments.analyse)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help='hello')
    create_parser = subparsers.add_parser('create')
    create_parser.add_argument('-n', '--number', type=int, default=1, help='specifies the number of sudokus to be created')
    create_parser.add_argument('-m', '--min-hints', type=int, default=0, help='generate sudokus that have at least the specified number of hints')
    create_parser.add_argument('-p', '--pretty', action='store_true', help='prints a formatted field instead of csv')
    create_parser.set_defaults(func=create)

    solve_parser = subparsers.add_parser('solve')
    solve_parser.add_argument('-p', '--pretty', action='store_true', help='prints a formatted field instead of csv')
    solve_parser.add_argument('-i', '--include-quiz', action='store_true', help='Includes the unsolved sudoku in the output')
    solve_parser.add_argument('-a', '--analyse', action='store_true', help='Same as --include-quiz but with additional information about the sudoku')
    solve_parser.set_defaults(func=solve_input)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        print(parser.format_help())
