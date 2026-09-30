# HackerRank: Day 18: Queues and Stacks
# https://www.hackerrank.com/challenges/30-queues-stacks/problem
class Solution:
    def __init__(self):
        self.stack = []
        self.queue = []

    def pushCharacter(self, ch):
        self.stack.append(ch)

    def enqueueCharacter(self, ch):
        self.queue.append(ch)

    def popCharacter(self):
        return self.stack.pop()

    def dequeueCharacter(self):
        return self.queue.pop(0)


s = input()
obj = Solution()
l = len(s)
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
result = True
for _ in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        result = False
        break
if result:
    print("The word,", s, ", is a palindrome.")
else:
    print("The word,", s, ", is not a palindrome.")
