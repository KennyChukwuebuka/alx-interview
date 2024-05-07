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
            # Check if the byte represents the start of a character
            if (byte >> 7) == 0:  # 1-byte character
                num_bytes = 0
            elif (byte >> 5) == 0b110:  # 2-byte character
                num_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character
                num_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character
                num_bytes = 3
            else:
                return False  # Invalid start of a character
        else:
            # Check if the byte is a continuation byte
            if (byte >> 6) != 0b10:
                return False  # Invalid continuation byte
            num_bytes -= 1

    # If there are remaining bytes required, return False
    return num_bytes == 0
