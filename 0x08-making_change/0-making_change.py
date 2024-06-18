#!/usr/bin/python3
"""
Ddetermine the fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    if total <= 0:
        return 0
    
    # Initialize the dp array with infinity for all amounts > 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    # Compute the fewest coins required for each amount from 1 to total
    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    # If dp[total] is still infinity, it means it's not possible to form the total with the given coins
    return dp[total] if dp[total] != float('inf') else -1

# Testing the function
if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))  # Output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
