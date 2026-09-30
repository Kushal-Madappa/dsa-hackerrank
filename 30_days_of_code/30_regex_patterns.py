# HackerRank: Day 28: RegEx, Patterns, and Intro to Databases
# https://www.hackerrank.com/challenges/30-regex-patterns/problem
import re

n = int(input())
names = []
pattern = re.compile(r'.+@gmail\.com$')
for _ in range(n):
    first_name, email_id = input().split()
    if pattern.match(email_id):
        names.append(first_name)

for name in sorted(names):
    print(name)
