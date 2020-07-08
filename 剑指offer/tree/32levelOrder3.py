# -*- coding: utf-8 -*- 
"""
Creator: YJ
Create time: 2020-07-03
Introduction:按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右到左的顺序打印，
第三行再按照从左到右的顺序打印，其他行以此类推。
"""
import collections


class Node:
    def __init__(self, data, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root):
        if not root: return []
        deque, res = collections.deque([root]), []
        print(deque)
        while deque:
            tmp = collections.deque()  # 用于临时存储当前层打印结果
            for _ in range(len(deque)):
                node = deque.popleft()
                print(node.val)
                if len(res) % 2:
                    tmp.appendleft(node.val)
                else:
                    tmp.append(node.val)
                if node.left: deque.append(node.left)
                if node.right: deque.append(node.right)
            res.append(list(tmp))
        return res


root1 = Node('3', Node('9'), Node('20', Node('15'), Node('7')))
s = Solution()
print(s.levelOrder(root1))
