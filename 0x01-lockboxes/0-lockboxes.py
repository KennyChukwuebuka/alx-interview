#!/usr/bin/python3
"""You have n number of locked boxes in front of you.
Each box is numbered from 0 to n - 1 and each box
may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.
    Prototype: def canUnlockAll(boxes)
    boxes is a list of lists
    A key with the same number as a box opens that box
    You can assume all keys will be positive integers
    There can be keys that do not have boxes
    The first box boxes[0] is unlocked
    Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    n = len(boxes)
    visited = set()  # Set to keep track of visited boxes
    stack = [0]      # Stack for DFS, start with the first box
    visited.add(0)   # Mark the first box as visited

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            # Check if key is valid and not visited
            if key < n and key not in visited:
                # Add the key's box to the stack
                stack.append(key)
                # Mark the key's box as visited
                visited.add(key)
# All boxes have been visited if len(visited) == n
    return len(visited) == n
