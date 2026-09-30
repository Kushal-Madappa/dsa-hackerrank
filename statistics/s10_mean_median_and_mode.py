# HackerRank: Day 0: Mean, Median, and Mode
# https://www.hackerrank.com/challenges/s10-mean-median-and-mode/problem
from collections import Counter

n = int(input())
a = sorted(map(int, input().split()))

mean = sum(a) / n
if n % 2:
    median = float(a[n // 2])
else:
    median = (a[n // 2 - 1] + a[n // 2]) / 2

cnt = Counter(a)
best = max(cnt.values())
mode = min(k for k, v in cnt.items() if v == best)

print(f"{mean:.1f}")
print(f"{median:.1f}")
print(mode)
