# HackerRank: Day 15: Linked List
# https://www.hackerrank.com/challenges/30-linked-list/problem
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        node = Node(data)
        if head is None:
            return node
        cur = head
        while cur.next is not None:
            cur = cur.next
        cur.next = node
        return head


mylist = Solution()
T = int(input())
head = None
for _ in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head)
