# HackerRank: Simple Array Sum
# https://www.hackerrank.com/challenges/simple-array-sum/problem


def simpleArraySum(ar):
    return sum(ar)


if __name__ == '__main__':
    _ = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    print(simpleArraySum(ar))
