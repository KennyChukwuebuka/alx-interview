#!/usr/bin/python3
"""
validate_utf8 module
    Requirement:
        Prototype: def validUTF8(data)
        Return: True if data is a valid UTF-8 encoding, else return False
        A character in UTF-8 can be 1 to 4 bytes long
        The data set can contain multiple characters
        The data will be represented by a list of integers
        Each integer represents 1 byte of data, therefore you only
        need to handle the 8 least significant bits of each integeer
"""


def validUTF8(data):
    """
    Determines if a given data set is a valid UTF-8 encoding

    Args:
        data (list): A list of integers

    Returns:
        If a valid UTF-8 encoding is detected
        return True, otherwise return False
    """
    return all(num >> 7 == 0 for num in data)


if __name__ == "__main__":
    import doctest
