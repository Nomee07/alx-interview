#!/usr/bin/python3
# This is the prime game implementation


def isWinner(x, nums):
    if not nums or x < 1:
        return None

    # Find the maximum number in nums to limit sieve size
    max_num = max(nums)

    # Sieve of Eratosthenes to find all prime numbers up to max_num
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for i in range(2, int(max_num**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_num + 1, i):
                sieve[j] = False

    # Prepare prime counts up to each number
    prime_counts = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if sieve[i] else 0)

    # Initialize win counters for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    # Determine winner for each round
    for n in nums:
        if prime_counts[n] % 2 == 0:  # Ben wins if prime count is even
            ben_wins += 1
        else:  # Maria wins if prime count is odd
            maria_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
