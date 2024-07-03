#!/usr/bin/python3
"""
A set of consecutive integers starting from 1 up to and including n.
"""


def is_prime(num):
    """ Returns True if num is a prime number, otherwise False """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def sieve_of_eratosthenes(max_num):
    """ Returns a list of primes up to max_num using Sieve of Eratosthenes """
    is_prime = [True] * (max_num + 1)
    p = 2
    while p * p <= max_num:
        if is_prime[p]:
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    prime_numbers = []
    for p in range(2, max_num + 1):
        if is_prime[p]:
            prime_numbers.append(p)
    return prime_numbers


def isWinner(x, nums):
    max_num = max(nums)  # Determine the maximum n we need to consider
    prime_numbers = sieve_of_eratosthenes(max_num)
    prime_set = set(prime_numbers)  # Convert to set for O(1) lookup

    # Counting wins
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = sum(1 for num in range(1, n + 1) if num in prime_set)

        # Maria always starts first
        if prime_count % 2 == 0:
            # If the number of primes is even, Ben wins
            ben_wins += 1
        else:
            # If the number of primes is odd, Maria wins because she starts
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None  # If it's a tie
