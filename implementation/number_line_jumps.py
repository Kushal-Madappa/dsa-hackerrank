# HackerRank: Number Line Jumps
# https://www.hackerrank.com/challenges/kangaroo/problem
def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        return "YES" if x1 == x2 else "NO"
    if (x2 - x1) % (v1 - v2) != 0:
        return "NO"
    t = (x2 - x1) // (v1 - v2)
    return "YES" if t >= 0 else "NO"


if __name__ == "__main__":
    x1, v1, x2, v2 = map(int, input().split())
    print(kangaroo(x1, v1, x2, v2))
