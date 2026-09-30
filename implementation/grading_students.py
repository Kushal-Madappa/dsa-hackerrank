# HackerRank: Grading Students
# https://www.hackerrank.com/challenges/grading/problem

def gradingStudents(grades):
    out = []
    for g in grades:
        if g < 38:
            out.append(g)
        else:
            nxt = ((g // 5) + 1) * 5
            if nxt - g < 3:
                out.append(nxt)
            else:
                out.append(g)
    return out

if __name__ == '__main__':
    n = int(input().strip())
    grades = [int(input().strip()) for _ in range(n)]
    result = gradingStudents(grades)
    print('\n'.join(map(str, result)))
