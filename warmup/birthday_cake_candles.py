# HackerRank: Birthday Cake Candles
# https://www.hackerrank.com/challenges/birthday-cake-candles/problem
def birthdayCakeCandles(candles):
    m = max(candles)
    return candles.count(m)

_ = int(input())
candles = list(map(int, input().split()))
print(birthdayCakeCandles(candles))
