#!/usr/bin/python3
"""
Prime game
"""


def isWinner(x, nums):
    """
    Find winner of prime game after x rounds
    """
    wins = {"Maria": 0, "Ben": 0}

    for n in nums:
        if n == 1:
            wins["Ben"] += 1
        else:
            prime_count = sum(1 for num in range(2, n + 1)
                              if all(num % i != 0
                              for i in range(2, int(num ** 0.5) + 1)))
            if prime_count % 2 == 0:
                wins["Ben"] += 1
            else:
                wins["Maria"] += 1

    max_wins = max(wins.values())

    if wins["Maria"] == wins["Ben"]:
        return None
    elif wins["Maria"] == max_wins:
        return "Maria"
    else:
        return "Ben"
