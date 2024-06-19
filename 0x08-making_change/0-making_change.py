#!/usr/bin/python3
"""
Ddetermine the fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet the total.
    If total is 0 or less, return 0.
    If total cannot be met by any number of coins you have, return -1.
    """
    if not coins:
        return -1
    if total <= 0:
        return 0
    
    coins.sort(reverse=True)
    change = 0
    
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if total == 0:
            return change
    
    return -1
