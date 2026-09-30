# HackerRank: Day 1: Interquartile Range
# https://www.hackerrank.com/challenges/s10-interquartile-range/problem

def median(arr):
    n = len(arr)
    m = n // 2
    if n % 2:
        return float(arr[m])
    return (arr[m - 1] + arr[m]) / 2

n = int(input())
vals = list(map(int, input().split()))
freq = list(map(int, input().split()))

data = []
for v, f in zip(vals, freq):
    data.extend([v] * f)
data.sort()

L = len(data)
half = L // 2
if L % 2:
    lower = data[:half]
    upper = data[half + 1:]
else:
    lower = data[:half]
    upper = data[half:]

iqr = median(upper) - median(lower)
print(f"{iqr:.1f}")
