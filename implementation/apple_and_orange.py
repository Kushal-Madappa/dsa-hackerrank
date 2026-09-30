# HackerRank: Apple and Orange
# https://www.hackerrank.com/challenges/apple-and-orange/problem


def countApplesAndOranges(s, t, a, b, apples, oranges):
    ac = sum(1 for d in apples if s <= a + d <= t)
    oc = sum(1 for d in oranges if s <= b + d <= t)
    print(ac)
    print(oc)


if __name__ == '__main__':
    s, t = map(int, input().split())
    a, b = map(int, input().split())
    m, n = map(int, input().split())
    apples = list(map(int, input().split()))
    oranges = list(map(int, input().split()))
    countApplesAndOranges(s, t, a, b, apples, oranges)
