'''
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
'''

'''

'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        self.flag = True
        self.TreeDepth(pRoot)
        return self.flag

    def TreeDepth(self, pRoot):
        if not pRoot or self.flag == False:
            return 0
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        if abs(left - right) > 1:
            self.flag = False
        return left+1 if left>right else right+1