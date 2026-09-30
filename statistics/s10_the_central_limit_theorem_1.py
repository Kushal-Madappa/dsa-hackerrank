# HackerRank: Day 7: The Central Limit Theorem I
# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-1/problem
from math import erf, sqrt

x = float(input())
n = int(input())
mu = float(input())
sigma = float(input())

mean_sum = n * mu
std_sum = sqrt(n) * sigma
z = (x - mean_sum) / std_sum
prob = 0.5 * (1 + erf(z / sqrt(2)))
print(f"{prob:.4f}")
