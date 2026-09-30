# HackerRank: Day 14: Scope
# https://www.hackerrank.com/challenges/30-scope/problem
class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        self.maximumDifference = max(self.__elements) - min(self.__elements)


_ = int(input())
a = list(map(int, input().split()))
d = Difference(a)
d.computeDifference()
print(d.maximumDifference)
