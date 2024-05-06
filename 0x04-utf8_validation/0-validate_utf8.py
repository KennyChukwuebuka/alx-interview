#!/usr/bin/python3
"""
validate_utf8 module
"""


def validUTF8(data):
    """
    Checks if the given data is a valid UTF-8 encoding
    """
    if not data:
        return True
    if len(data) < 1 or len(data) > 4:
        return False
    if len(data) == 1:
        return data[0] < 128
    if len(data) == 2:
        return data[0] >= 192 and data[0] < 224
    if len(data) == 3:
        return data[0] >= 224 and data[0] < 240
    return data[0] >= 240


if __name__ == "__main__":
    data = [240, 162, 138, 147]
    print(validUTF8(data))
