# HackerRank: Day 7: Arrays
# https://www.hackerrank.com/challenges/30-arrays/problem
n = int(input().strip())
arr = list(map(int, input().split()))
print(*arr[::-1])
