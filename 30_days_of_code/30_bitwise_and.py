# HackerRank: Day 29: Bitwise AND
# https://www.hackerrank.com/challenges/30-bitwise-and/problem
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    best = 0
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            v = a & b
            if v < k and v > best:
                best = v
    print(best)
