# HackerRank: Day 9: Recursion 3
# https://www.hackerrank.com/challenges/30-recursion/problem
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

if __name__ == '__main__':
    n = int(input().strip())
    print(factorial(n))
