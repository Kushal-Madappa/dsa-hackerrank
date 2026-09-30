# HackerRank: Day 8: Dictionaries and Maps
# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem
import sys

n = int(input().strip())
book = {}
for _ in range(n):
    name, phone = input().split()
    book[name] = phone

for line in sys.stdin:
    query = line.strip()
    if not query:
        continue
    if query in book:
        print(f"{query}={book[query]}")
    else:
        print("Not found")
