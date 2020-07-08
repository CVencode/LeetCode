# -*- coding: utf-8 -*- 
"""
Creator: YJ
Create time: 2020-07-03
Introduction:
"""


class Node:
    def __init__(self, data, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right


class SolutionSelf:
    def levelOrder(self, root):
        if not root: return []
        queue, res = [root], []
        while queue:
            for node in queue:
                tmp = []
                res.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            queue = tmp
        return res


import collections


class Solution:
    def levelOrder(self, root):
        if not root: return []
        queue, res = collections.deque(), []
        queue.append(root)
        while queue:
            # tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                # tmp.append(node.val)
                res.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            # res.append(tmp)
        return res


root1 = Node('3', Node('9'), Node('20', Node('15'), Node('7')))
s = SolutionSelf()
print(s.levelOrder(root1))
