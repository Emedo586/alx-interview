#!/usr/bin/python3
"""
Define UTF-8 Validation function:
method that determines if a given data set
represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    UTF-8 Validation
    """
    expected_bytes = 0
    s1 = 1 << 7
    s2 = 1 << 6

    for num in data:
        binary_str = 1 << 7
        if expected_bytes == 0:
            while binary_str & num:
                expected_bytes += 1
                binary_str = binary_str >> 1
            if expected_bytes == 0:
                continue
            if expected_bytes == 1 or expected_bytes > 4:
                return False
        else:
            if not (num & s1 and not (num & s2)):
                return False
        expected_bytes -= 1
    #return not expected_bytes
    return expected_bytes == 0
