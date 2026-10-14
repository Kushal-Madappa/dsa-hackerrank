# HackerRank: Mini-Max Sum
# https://www.hackerrank.com/challenges/mini-max-sum/problem


def miniMaxSum(arr):
    total = sum(arr)
    print(total - max(arr), total - min(arr))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
