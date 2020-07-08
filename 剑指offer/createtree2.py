# -*- coding: utf-8 -*- 
"""
Creator: YJ
Create time: 2020-06-28
Introduction:
"""
"""从控制台输入创建二叉树"""


class Node():
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def create(root):
    a = input('enter a key')
    if a == '#':
        return None
    else:
        root = Node(data=root)
        root.left = create(root.left)
        root.right = create(root.right)
        return root
    return root


# root1 = None
# root2 = create(root1)
# print(root2)

"""用列表递归创建二叉树"""


class Node():
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def listCreateTree(root, L, i):
    if i < len(L):
        if L[i] == '#':
            return None
        else:
            root = Node(data=L[i])
            print(i)
            root.left = listCreateTree(root.left, L, 2 * i + 1)
            root.right = listCreateTree(root.right, L, 2 * i + 2)
            return root
        return root


root = Node()
L = ['1', '2', '3', '#', '4', '5']
root = listCreateTree(root, L, 0)
