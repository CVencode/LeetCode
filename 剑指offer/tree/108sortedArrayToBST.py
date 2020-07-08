# -*- coding: utf-8 -*- 
"""
Creator: YJ
Create time: 2020-07-03
Introduction:将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点的左右两个子树的高度差的绝对值不超过 1。
"""


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right


class Solution1:
    def sortedArrayToBST(self, nums):  # List[int] -> TreeNode
        if not nums: return None
        mid = (len(nums)) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root

from random import randint
class Solution2:
    def sortedArrayToBST(self, nums):
        def helper(left, right):
            if left > right: return None
            # 总是选择中间位置左边的数字作为根节点 mid = (left + right) // 2
            # 总是选择中间位置右边的数字作为根节点mid = (left + right+1) // 2
            # 选择任意一个中间位置的数字作为根节点mid = (left + right + randint(0, 1)) // 2
            mid = (left + right + randint(0, 1)) // 2
            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, len(nums) - 1)


# root1 = Node('3', Node('9'), Node('20', Node('15'), Node('7')))
nums = [-10, -3, 0, 5, 9]
s = Solution2()
print(s.sortedArrayToBST(nums))
