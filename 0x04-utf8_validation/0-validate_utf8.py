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
    """Determines if a given data set represents
     a valid UTF-8 encoding or not
    """
    count = 0
    for d in data:
        if count == 0:
            if d & 128 == 0:
                count = 0
            elif d & 224 == 192:
                count = 1
            elif d & 240 == 224:
                count = 2
            elif d & 248 == 240:
                count = 3
            else:
                return False
        else:
            if d & 192 != 128:
                return False    
            count -= 1
    if count == 0:
        return True
    return False
