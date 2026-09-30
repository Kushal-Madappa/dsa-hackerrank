# HackerRank: Day 6: Normal Distribution I
# https://www.hackerrank.com/challenges/s10-normal-distribution-1/problem
from math import erf, sqrt

mu, sigma = map(float, input().split())
x1 = float(input())
lo, hi = map(float, input().split())

def cdf(x):
    return 0.5 * (1 + erf((x - mu) / (sigma * sqrt(2))))

print(f"{cdf(x1):.3f}")
print(f"{cdf(hi) - cdf(lo):.3f}")
