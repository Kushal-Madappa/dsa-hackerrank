# HackerRank: Day 5: Poisson Distribution I
# https://www.hackerrank.com/challenges/s10-poisson-distribution-1/problem
from math import exp, factorial

lam = float(input())
k = int(input())
prob = (lam ** k) * exp(-lam) / factorial(k)
print(f"{prob:.3f}")
