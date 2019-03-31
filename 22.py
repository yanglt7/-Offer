'''
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
'''

'''
要查找树A中是否存在和树B结构一样的子树，我们可以分为两步：
第一步在树A中找到和B的根结点的值一样的结点R，
第二步再判断树A中以R为根节点的子树是不是包含和树B一样的结构。

and:遇假则假，所以前面为假就不执行和判断后面，前面为真则继续判断执行后面的;
or:遇真则真，所以前面为真就不执行和判断后面，前面为假则继续判断执行后面的。
'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        return self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.is_subtree(pRoot1, pRoot2)
    def is_subtree(self, A, B):
        if not B:
            return True
        if not A or A.val != B.val:
            return False
        return self.is_subtree(A.left, B.left) and self.is_subtree(A.right, B.right)