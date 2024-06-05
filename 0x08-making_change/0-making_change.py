#!/usr/bin/python3
"""
Coin Change Algorithm
"""


def makeChange(coins, total):
    """Calculate the fewest number needed to meet,
    needed to meet a given total amount.
    Args:
        coins ([list]): A list of coin values available.
        total ([number]): The target amount
    Return: The fewest number of coins needed to reach the total,
    or -1 if not possible.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    i, no_coins = (0, 0)
    
    total_cpy = total
    len_coins = len(coins)

    while(i < len_coins and total_cpy > 0):
        if (total_cpy - coins[i]) >= 0:
            total_cpy -= coins[i]
            no_coins += 1
        else:
            i += 1

    check = total_cpy > 0 and no_coins > 0
    return -1 if check or no_coins == 0 else no_coins
