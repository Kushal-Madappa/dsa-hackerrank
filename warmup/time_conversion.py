# HackerRank: Time Conversion
# https://www.hackerrank.com/challenges/time-conversion/problem

def timeConversion(s):
    hh = int(s[:2])
    period = s[-2:]
    if period == 'AM':
        hh = 0 if hh == 12 else hh
    else:
        hh = 12 if hh == 12 else hh + 12
    return f"{hh:02d}{s[2:-2]}"

if __name__ == '__main__':
    s = input().strip()
    print(timeConversion(s))
