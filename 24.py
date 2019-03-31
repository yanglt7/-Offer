'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
'''

'''
以{5,7,6,9,11,10,8}为例，后序遍历结果的最后一个数字8就是根结点的值。
在这个数组中，前3个数字5、7和6都比8小，是值为8的结点的左子树结点；后3个数字9、11和10都比8大，是值为8的结点的右子树结点。
我们接下来用同样的方法确定与数组每一部分对应的子树的结构。这其实就是一个递归的过程。
对于序列5、7、6，最后一个数字6是左子树的根结点的值。数字5比6小，是值为6的结点的左子结点，而7则是它的右子结点。
同样，在序列9、11、10中，最后一个数字10是右子树的根结点，数字9比10小，是值为10的结点的左子结点，而11则是它的右子结点。
我们使用递归的方法，先判断数组的左子树和右子树的位置，然后再判断左子树、右子树是不是二叉搜索树。
'''

# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 0:
            return False
        if len(sequence) == 1:
            return True
        length = len(sequence)
        root = sequence[-1]
        i = 0
        while sequence[i] < root:
            i += 1
        k = i
        for j in range(i, length-1):
            if sequence[j] < root:
                return False
        left_s = sequence[:k]
        right_s = sequence[k:length-1]
        left, right = True, True
        if len(left_s) > 0:
            left = self.VerifySquenceOfBST(left_s)
        if len(right_s) > 0:
            left = self.VerifySquenceOfBST(right_s)
        return left and right