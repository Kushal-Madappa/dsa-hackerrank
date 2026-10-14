# HackerRank: A Very Big Sum
# https://www.hackerrank.com/challenges/a-very-big-sum/problem
def aVeryBigSum(ar):
    return sum(ar)

_ = int(input())
ar = list(map(int, input().split()))
print(aVeryBigSum(ar))
