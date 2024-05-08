#!/usr/bin/python3

def validUTF8(data):
    # Initialize a variable to keep track of the number of remaining bytes
    remaining_bytes = 0
    
    # Iterate through each integer in the data
    for num in data:
        # Check if the most significant bit (MSB) is set (i.e., it's a multi-byte character)
        if remaining_bytes == 0:
            if num >> 7 == 0b0:
                # Single-byte character
                continue
            elif num >> 5 == 0b110:
                # Two-byte character
                remaining_bytes = 1
            elif num >> 4 == 0b1110:
                # Three-byte character
                remaining_bytes = 2
            elif num >> 3 == 0b11110:
                # Four-byte character
                remaining_bytes = 3
            else:
                # Invalid start byte
                return False
        else:
            # Check if the next byte is a continuation byte (i.e., starts with 0b10)
            if num >> 6 != 0b10:
                return False
            remaining_bytes -= 1
    
    # Make sure all bytes were consumed
    return remaining_bytes == 0
