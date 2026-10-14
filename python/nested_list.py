# HackerRank: Nested Lists
# https://www.hackerrank.com/challenges/nested-list/problem
if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    second = sorted({s[1] for s in students})[1]
    for name in sorted(n for n, s in students if s == second):
        print(name)
