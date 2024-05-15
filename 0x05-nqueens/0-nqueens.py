#!/usr/bin/python3
"""
    NQueens
"""

import sys


def is_safe(board, row, col):
    """
        is safe methos
    """
    for i in range(row):
        if board[i] == col:
            return False

        # Check diagonals
        if abs(i - row) == abs(board[i] - col):
            return False
    return True


def solve_n_queens(n):
    """
        solving the nqueen
    """
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solutions = []

    def backtrack(row):
        if row == n:
            solutions.append([[i, board[i]] for i in range(n)])
        else:
            for col in range(n):
                if is_safe(board, row, col):
                    board[row] = col
                    backtrack(row + 1)
                    board[row] = -1

    backtrack(0)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_n_queens(N)
