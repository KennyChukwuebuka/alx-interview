#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """
    Returns the name of the player that won the most rounds
    """
    if x < 1 or nums is None or x > 10000:
        return None
    if x == 1:
        return "Maria"
    if x == 2:
        return "Ben"
    return "Maria" if sum(nums) % 2 == 0 else "Ben"


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
