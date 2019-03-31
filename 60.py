'''
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
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
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        resultList = []
        curLayerNodes = [pRoot]
        while curLayerNodes:
            curList = []
            nextLayerNodes = []
            for node in curLayerNodes:
                curList.append(node.val)
                if node.left:
                    nextLayerNodes.append(node.left)
                if node.right:
                    nextLayerNodes.append(node.right)
            resultList.append(curList)
            curLayerNodes = nextLayerNodes
        return resultList