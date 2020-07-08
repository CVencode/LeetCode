# -*- coding: utf-8 -*- 
"""
Creator: YJ
Create time: 2020-07-03
Introduction:从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，
每一层打印到一行。
"""


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class SolutionSelf:
    def levelOrder(self, root):
        if not root: return root
        queue, res = [root], []
        print(queue)
        while queue:
            re, tmp = [], []
            for node in queue:
                re.append(node.data)
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            queue = tmp
            res.append(re)
        return res
import collections


class Solution:
    def levelOrder(self, root):
        if not root: return []
        queue, res = collections.deque(), []
        queue.append(root)
        print(queue)
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.data)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(tmp)
        return res


root1 = Node('3', Node('9'), Node('20', Node('15'), Node('7')))
s = Solution()
print(s.levelOrder(root1))
