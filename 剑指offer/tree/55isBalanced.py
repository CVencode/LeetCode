# -*- coding: utf-8 -*- 
"""
Creator: YJ
Create time: 2020-06-27
Introduction:平衡二叉树
"""
"""方法1：后序遍历 + 剪枝（从底至顶）
算法流程：
recur(root) 函数：
    返回值：
        当节点root左右子树的深度差≤1： 则返回当前子树的深度，即节点root的左右子树的深度最大值max(left, right) + 1；
        当节点root左右子树的深度差>1 ：则返回−1，代表此子树不是平衡树 。
    终止条件：
        当root为空：说明越过叶节点，因此返回高度0 ；
        当左右子树深度为−1 ：代表此树的左右子树不是平衡树，因此剪枝，直接返回−1 ；
isBalanced(root) 函数：
    返回值：若 recur(root) != -1 ，则说明此树平衡，返回true ；否则返回false。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def listCreatTree(root, llist, i):
    if i < len(llist):
        if llist[i] == '#':
            return None  ###这里的return很重要
        else:
            root = TreeNode(llist[i])
            # 往左递推
            root.left = listCreatTree(root.left, llist, 2 * i + 1)  # 从根开始一直到最左，直至为空，
            # 往右回溯
            root.right = listCreatTree(root.right, llist, 2 * i + 2)  # 再返回上一个根，回溯右，
            # 再返回根'
            return root  ###这里的return很重要
    return root


class Solution1:
    def isBalanced(self, root):
        def recur(root):
            if not root: return 0
            left = recur(root.left)
            if left == -1: return -1
            right = recur(root.right)
            if right == -1: return -1
            return max(left, right) + 1 if abs(left - right) <= 1 else -1

        return recur(root) != -1


class Solution2:
    def isBalanced(self, root):
        if not root: return True
        if abs(self.depth(root.left) - self.depth(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False

    def depth(self, root):
        if not root: return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1


l = [1, 2, 2, 3, 3, None, None, 4, 4]
# l=[3,9,20,None,None,15,7]
root = listCreatTree(None, l, 0)
print(root)
s = Solution2().isBalanced(root)
print(s)

