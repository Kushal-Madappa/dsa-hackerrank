# HackerRank: Day 26: Nested Logic
# https://www.hackerrank.com/challenges/30-nested-logic/problem
rd, rm, ry = map(int, input().split())
ed, em, ey = map(int, input().split())

if (ry, rm, rd) <= (ey, em, ed):
    fine = 0
elif ry == ey and rm == em:
    fine = 15 * (rd - ed)
elif ry == ey:
    fine = 500 * (rm - em)
else:
    fine = 10000

print(fine)
