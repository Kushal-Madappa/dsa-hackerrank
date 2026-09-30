# HackerRank: Day 6: Let's Review
# https://www.hackerrank.com/challenges/30-review-loop/problem
t = int(input().strip())
for _ in range(t):
    s = input()
    print(s[::2], s[1::2])
