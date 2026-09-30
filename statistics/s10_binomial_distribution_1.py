# HackerRank: Day 4: Binomial Distribution I
# https://www.hackerrank.com/challenges/s10-binomial-distribution-1/problem
from math import comb

ratio = list(map(float, input().split()))
b, g = ratio
p = b / (b + g)
n = 6
prob = sum(comb(n, k) * (p ** k) * ((1 - p) ** (n - k)) for k in range(3, n + 1))
print(f"{prob:.3f}")
