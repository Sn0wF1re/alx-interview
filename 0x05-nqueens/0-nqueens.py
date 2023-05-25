#!/usr/bin/python3
"""
Write a program that solves the N queens problem
"""
import sys


def solve_nqueens(N):
    board = [[-1 for _ in range(N)] for _ in range(N)]
    solns = []
    solve_nqueens_util(board, 0, solns)
    return solns


def solve_nqueens_util(board, row, solns):
    if row == len(board):
        solns.append(board.copy())
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens_util(board, row + 1, solns)
            board[row] = -1


def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or \
                board[i] + i == col + row:
            return False
    return True


def print_solns(solns):
    for soln in solns:
        print([[row, soln[row]] for row in range(len(soln))])


def main():
    length = len(sys.argv)

    if length != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    if N < 4:
        print('N must be at least 4')
        sys.exit(1)

    solns = solve_nqueens(N)
    print_solns(solns)


if __name__ == "__main__":
    main()
