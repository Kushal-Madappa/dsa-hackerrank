# HackerRank: Compare the Triplets
# https://www.hackerrank.com/challenges/compare-the-triplets/problem


def compareTriplets(a, b):
    alice, bob = 0, 0
    for x, y in zip(a, b):
        if x > y:
            alice += 1
        elif x < y:
            bob += 1
    return [alice, bob]


if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)
    print(*result)
