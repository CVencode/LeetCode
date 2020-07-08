# -*- coding: utf-8 -*- 
"""
Creator: YJ
Create time: 2020-06-14
Introduction:创建二叉树
"""


class TreeNode1(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    # 这一步是在每次调用某个结点时，自动调用.data的方法
    # 当使用print输出对象的时候，只要自己定义了__str__(self)方法，
    # 那么就会打印从在这个方法中return的数据
    def __str__(self):  # 返回一个字符串，是对该对象的描写
        return str(self.data)


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""方法一"""
A, B, C, D, E, F, G, H, I = [TreeNode(x) for x in 'ABCDEFGHI']
A.left, A.right = B, C
B.right = D
C.left, C.right = E, F
E.left = G
F.left, F.right = H, I
print(C.right)

A, B, C, D, E, F, G, H, I = [TreeNode1(x) for x in 'ABCDEFGHI']
A.left, A.right = B, C
B.right = D
C.left, C.right = E, F
E.left = G
F.left, F.right = H, I
print(C.right)

"""方法二"""


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


root11 = Node('1', Node('2', Node('3')), Node('4', Node('5', '6')))
print('root11', root11)

a = Node('a', 'b', 'c')
b = Node('b', None, 'd')
c = Node('c', 'e', 'f')
e = Node('e', 'g', None)
f = Node('f', 'h', 'i')
print(e.left)
