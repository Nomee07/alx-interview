#!/usr/bin/python3
"""
This module contains the validUTF8 function to validate UTF-8 encoding.
"""



def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    
    Args:
        data (list of int): A list of integers representing bytes of data.
        
    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the most significant bits
    mask1 = 1 << 7
    mask2 = 1 << 6

    # Iterate over each integer in the data
    for num in data:
        # Get the least significant 8 bits of the integer
        byte = num & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            # If num_bytes is 0, it is a 1-byte character
            if num_bytes == 0:
                continue

            # UTF-8 character should be 1 to 4 bytes long
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check that the byte is a valid continuation byte
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrement the number of bytes remaining in the current UTF-8 character
        num_bytes -= 1

    # If num_bytes is not 0, it means we have an incomplete multi-byte character
    return num_bytes == 0
