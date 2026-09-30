# HackerRank: Day 21: Generics
# https://www.hackerrank.com/challenges/30-generics/problem
# Python has dynamic typing, so a single function accepts any iterable.
def printArray(arr):
    for x in arr:
        print(x)


int_arr = [1, 2, 3, 4, 5]
str_arr = ["Hello", "World"]
printArray(int_arr)
printArray(str_arr)
