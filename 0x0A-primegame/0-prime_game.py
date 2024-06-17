#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    def isPrime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def playRound(n):
        primes = [i for i in range(2, n + 1) if isPrime(i)]
        player = 'Maria'
        while primes:
            if player == 'Maria':
                player = 'Ben'
            else:
                player = 'Maria'
            for prime in primes:
                if prime in range(1, n + 1):
                    primes.remove(prime)
                    for multiple in range(prime * 2, n + 1, prime):
                        if multiple in primes:
                            primes.remove(multiple)
                    break
        return player

    wins = {'Maria': 0, 'Ben': 0}
    for n in nums:
        winner = playRound(n)
        wins[winner] += 1

    if wins['Maria'] > wins['Ben']:
        return 'Maria'
    elif wins['Ben'] > wins['Maria']:
        return 'Ben'
    else:
        return None
