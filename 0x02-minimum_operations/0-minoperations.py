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
        return n

    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = i
        for j in range(i - 1, 1, -1):
            if i % j == 0:
                dp[i] = dp[j] + i // j
                break

    return dp[n]
