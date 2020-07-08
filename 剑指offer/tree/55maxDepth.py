# -*- coding: utf-8 -*- 
"""
Creator: YJ
Create time: 2020-06-27
Introduction:offer55--二叉树的深度
"""
"""DFS:后序遍历(递归)"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def maxDepth(self, root):
        if not root: return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        res = max(left, right) + 1
        return res


"""BFS:层次遍历(利用队列)"""


class Solution2:
    def maxDepth(self, root):
        if not root: return 0
        queue, res = [root], 0
        while queue:
            tmp = []
            for node in queue:
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            queue = tmp
            res = res + 1
        return res
