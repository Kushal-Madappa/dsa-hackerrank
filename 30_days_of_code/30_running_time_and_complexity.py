# HackerRank: Day 25: Running Time and Complexity
# https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem
def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


t = int(input())
for _ in range(t):
    n = int(input())
    print("Prime" if is_prime(n) else "Not prime")
