#!/usr/bin/python3
"""
Prime game
"""


def is_prime(num):
    """
    Check if number is a prime number
    """
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """
    Find winner of prime game after x rounds
    """
    wins = {'Ben': 0, 'Maria': 0}
    for n in nums:
        picks = 0
        for i in range(2, n + 1):
            if is_prime(i):
                picks += 1
        if picks % 2 == 0:
            wins['Ben'] += 1
        else:
            wins['Maria'] += 1

    max_val = max(wins.values())
    winners = [player for player, score in wins.items() if score == max_val]

    if len(winners) == 1:
        return winners[0]
    else:
        return None
