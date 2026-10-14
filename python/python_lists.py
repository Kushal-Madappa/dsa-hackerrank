# HackerRank: Lists
# https://www.hackerrank.com/challenges/python-lists/problem
if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(N):
        cmd = input().split()
        op = cmd[0]
        args = list(map(int, cmd[1:]))
        if op == 'insert':
            arr.insert(args[0], args[1])
        elif op == 'print':
            print(arr)
        elif op == 'remove':
            arr.remove(args[0])
        elif op == 'append':
            arr.append(args[0])
        elif op == 'sort':
            arr.sort()
        elif op == 'pop':
            arr.pop()
        elif op == 'reverse':
            arr.reverse()
