# HackerRank: Day 10: Binary Numbers
# https://www.hackerrank.com/challenges/30-binary-numbers/problem
n = int(input().strip())
b = bin(n)[2:]
best = cur = 0
for ch in b:
    if ch == '1':
        cur += 1
        best = max(best, cur)
    else:
        cur = 0
print(best)
