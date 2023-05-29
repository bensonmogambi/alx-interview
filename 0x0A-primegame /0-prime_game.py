#!/usr/bin/python3
'''Prime Game'''


def isWinner(x, nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes(n):
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def can_win(primes, n):
        if n <= 2:
            return True
        for prime in primes:
            if prime > n:
                break
            if not can_win(primes, n - prime):
                return True
        return False

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = get_primes(n)
        if can_win(primes, n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
