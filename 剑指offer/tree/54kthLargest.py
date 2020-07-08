# -*- coding: utf-8 -*- 
"""
Creator: YJ
Create time: 2020-07-08
Introduction:二叉搜索树的第k大节点（1 ≤ k ≤ 二叉搜索树元素个数）
"""
"""二叉搜索树的中序遍历为递增序列,其倒序为递减序列,即按右-根-左顺序遍历二叉搜索树"""


# 为求第k个节点，需要实现以下三项工作 ：
# 递归遍历时计数，统计当前节点的序号；
# 递归到第 k个节点时，应记录结果 res；
# 记录结果后，后续的遍历即失去意义，应提前终止（即返回）


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left, self.right = None, None


class Solution:
    def kthLargest(self, root, k):
        self.k, self.res = k, None

        def dfs(node):
            if not root or not self.k: return
            dfs(node.right)
            # if self.k == 0: return
            self.k -= 1
            if self.k == 0:
                self.res = node.val
            if self.k > 0: dfs(node.left)

        dfs(root)
        return self.res


root = [5, 3, 6, 2, 4, None, None, 1]
k = 3
s = Solution().kthLargest(root, k)
print(s)
