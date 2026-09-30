# HackerRank: Day 23: BST Level-Order Traversal
# https://www.hackerrank.com/challenges/30-bst-level-order-traversal/problem
from collections import deque


class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def levelOrder(self, root):
        if root is None:
            return
        q = deque([root])
        out = []
        while q:
            node = q.popleft()
            out.append(str(node.data))
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        print(" ".join(out))


T = int(input())
myTree = Solution()
root = None
for _ in range(T):
    data = int(input())
    root = myTree.insert(root, data)
myTree.levelOrder(root)
