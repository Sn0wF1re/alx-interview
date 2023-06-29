#!/usr/bin/python3
"""
Prime game
"""


def find_primes(nums):
    """
    Find primes in a range
    """
    n = max(nums)
    primes = [True] * (n + 1)
    primes[0] = False

    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    return primes


def isWinner(x, nums):
    """
    Find winner of prime game after x rounds
    """
    if x < 1 or not nums:
        return None
    maria_wins = 0
    ben_wins = 0
    primes = find_primes(nums)

    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        if primes_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins == ben_wins:
        return None
    return 'Maria' if maria_wins > ben_wins else 'Ben'
