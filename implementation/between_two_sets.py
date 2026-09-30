# HackerRank: Between Two Sets
# https://www.hackerrank.com/challenges/between-two-sets/problem
from math import gcd
from functools import reduce


def getTotalX(a, b):
    lcm_a = reduce(lambda x, y: x * y // gcd(x, y), a)
    gcd_b = reduce(gcd, b)
    count = 0
    x = lcm_a
    while x <= gcd_b:
        if gcd_b % x == 0:
            count += 1
        x += lcm_a
    return count


if __name__ == "__main__":
    n, m = map(int, input().rstrip().split())
    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))
    print(getTotalX(arr, brr))
