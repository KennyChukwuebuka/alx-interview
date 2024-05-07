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
    num_bytes = 0

    for byte in data:
        if num_bytes == 0:
            if byte >> 5 == 0b110:
                num_bytes = 1
            elif byte >> 4 == 0b1110:
                num_bytes = 2
            elif byte >> 3 == 0b11110:
                num_bytes = 3
            elif byte >> 7 == 0b1:
                return False
        else:
            if byte >> 6 == 0b10:
                num_bytes -= 1
            else:
                return False

    return num_bytes == 0
