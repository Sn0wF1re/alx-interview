#!/usr/bin/python3
"""
Prime game
"""


def is_prime(n):
    """
    Check if number is a prime number
    """
    primes = []
    prime_flags = [True] * (n + 1)
    prime_flags[0] = prime_flags[1] = False

    p = 2
    while p * p <= n:
        if prime_flags[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                prime_flags[i] = False
        p += 1
    for num in range(p, n + 1):
        if prime_flags[num] and num not in primes:
            primes.append(num)
    return primes


def isWinner(x, nums):
    """
    Find winner of prime game after x rounds
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n < 2:
            ben_wins += 1
        else:
            primes = is_prime(n)

            if len(primes) % 2 == 0:
                ben_wins += 1
            else:
                maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
