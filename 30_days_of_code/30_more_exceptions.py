# HackerRank: Day 17: More Exceptions
# https://www.hackerrank.com/challenges/30-more-exceptions/problem
class Calculator:
    def power(self, n, p):
        if n < 0 or p < 0:
            raise Exception("n and p should be non-negative")
        return n ** p


myCalculator = Calculator()
T = int(input())
for _ in range(T):
    n, p = map(int, input().split())
    try:
        print(myCalculator.power(n, p))
    except Exception as e:
        print(e)
