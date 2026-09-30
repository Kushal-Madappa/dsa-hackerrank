# HackerRank: Day 20: Sorting
# https://www.hackerrank.com/challenges/30-sorting/problem
n = int(input())
a = list(map(int, input().split()))
num_swaps = 0
for i in range(n):
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            num_swaps += 1
    if num_swaps == 0:
        break

print("Array is sorted in", num_swaps, "swaps.")
print("First Element:", a[0])
print("Last Element:", a[n - 1])
