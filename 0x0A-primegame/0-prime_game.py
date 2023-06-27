#!/usr/bin/python3
"""
Prime game
"""


def is_prime(n):
    """
    Check if number is a prime number
    """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [i for i, val in enumerate(primes) if val]


def isWinner(x, nums):
    """
    Find winner of prime game after x rounds
    """
    wins = {'Ben': 0, 'Maria': 0}
    primes = is_prime(max(nums))

    for num in nums:
        if num == 1:
            wins['Ben'] += 1
        else:
            picks = sum(1 for prime in primes if prime <= num)
            # if picks is even, Ben wins directly
            if picks % 2 == 0:
                wins['Ben'] += 1

            # Maria wins if picks is odd
            else:
                wins['Maria'] += 1

    max_val = max(wins.values())
    winners = [player for player, score in wins.items() if score == max_val]

    if len(winners) == 1:
        return winners[0]
    else:
        return None
