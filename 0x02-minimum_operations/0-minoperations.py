#!/usr/bin/python3
"""
Calculates the fewest num of ops needed to result in n H characters in a file.
"""

def minOperations(n):
    """
    Calculates the fewest number of operations needed.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The fewest number of operations needed.
              Returns 0 if n is impossible to achieve.
    """
    if n <= 1:
        return 0

    for op in range(2, n + 1):
        if n % op == 0:
            return minOperations(int(n/op)) + op
