#!/usr/bin/python3
""" A function that returns the name
    of the player with the most rounds
"""

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    p = 2
    while p**2 <= n:
        if primes[p]:
            for i in range(p**2, n + 1, p):
                primes[i] = False
        p += 1
    return primes

def play_game(n):
    primes = sieve_of_eratosthenes(n)
    numbers = list(range(1, n + 1))
    player = 0
    while True:
        if player == 0:
            for p in range(2, n + 1):
                if primes[p] and p in numbers:
                    numbers = [x for x in numbers if x % p!= 0]
                    break
            else:
                return 1
        else:
            for p in range(2, n + 1):
                if primes[p] and p in numbers:
                    numbers = [x for x in numbers if x % p!= 0]
                    break
            else:
                return 0
        player = 1 - player

def isWinner(x, nums):
    maria_wins = 0
    for n in nums:
        if play_game(n) == 0:
            maria_wins += 1
    if maria_wins > x / 2:
        return "Maria"
    elif maria_wins < x / 2:
        return "Ben"
    else:
        return None
