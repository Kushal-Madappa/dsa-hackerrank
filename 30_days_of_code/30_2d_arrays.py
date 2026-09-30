# HackerRank: Day 11: 2D Arrays
# https://www.hackerrank.com/challenges/30-2d-arrays/problem
arr = [list(map(int, input().split())) for _ in range(6)]
best = -float('inf')
for i in range(4):
    for j in range(4):
        s = (arr[i][j] + arr[i][j+1] + arr[i][j+2]
             + arr[i+1][j+1]
             + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
        if s > best:
            best = s
print(best)
