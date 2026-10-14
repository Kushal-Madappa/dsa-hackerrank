# HackerRank: Diagonal Difference
# https://www.hackerrank.com/challenges/diagonal-difference/problem


def diagonalDifference(arr):
    n = len(arr)
    left = sum(arr[i][i] for i in range(n))
    right = sum(arr[i][n - 1 - i] for i in range(n))
    return abs(left - right)


if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    print(diagonalDifference(arr))
