# HackerRank: Day 8: Least Square Regression Line
# https://www.hackerrank.com/challenges/s10-least-square-regression-line/problem
import sys

xs, ys = [], []
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    a, b = map(float, line.split())
    xs.append(a); ys.append(b)

n = len(xs)
mx = sum(xs) / n
my = sum(ys) / n
num = sum((xs[i] - mx) * (ys[i] - my) for i in range(n))
den = sum((xs[i] - mx) ** 2 for i in range(n))
b1 = num / den
b0 = my - b1 * mx
print(f"{b0 + b1 * 80:.3f}")
