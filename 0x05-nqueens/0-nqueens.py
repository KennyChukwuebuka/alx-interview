#!/usr/bin/python3
"""
    NQueens
"""

import sys


def nqueens(n):
    """
    nqueens
    """
    def solve(queens, xy_dif, xy_sum):
        p = len(queens)
        if p == n:
            result.append(queens)
            return None
        for q in range(n):
            if q not in queens and p - q not in xy_dif and p + q not in xy_sum:
                solve(queens + [q], xy_dif + [p - q], xy_sum + [p + q])
    result = []
    solve([], [], [])
    return result


if len(sys.argv) != 2:
    print("Usage: nqueens N", file=sys.stderr)
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number", file=sys.stderr)
    sys.exit(1)

if n < 4:
    print("N must be at least 4", file=sys.stderr)
    sys.exit(1)

for solution in nqueens(n):
    print('[' + ', '.join(['[' + str(i) + ', '
                           + str(solution.index(i))
                           + ']' for i in range(n)]) + ']')
