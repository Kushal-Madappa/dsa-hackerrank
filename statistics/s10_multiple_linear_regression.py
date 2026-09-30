# HackerRank: Day 9: Multiple Linear Regression
# https://www.hackerrank.com/challenges/s10-multiple-linear-regression/problem
import numpy as np

m, n = map(int, input().split())
X, Y = [], []
for _ in range(n):
    row = list(map(float, input().split()))
    X.append([1.0] + row[:m])
    Y.append(row[m])
q = int(input())
Q = [[1.0] + list(map(float, input().split())) for _ in range(q)]

X = np.array(X); Y = np.array(Y); Q = np.array(Q)
beta = np.linalg.pinv(X.T @ X) @ X.T @ Y
for pred in Q @ beta:
    print(f"{pred:.2f}")
