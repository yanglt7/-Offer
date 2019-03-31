'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''

#双向队列
# -*- coding:utf-8 -*-
from collections import deque
class Solution:
    def reOrderArray(self, array):
        # write code here
        odd = deque()
        l = len(array)
        for i in range(l):
            if array[l-i-1] % 2 != 0:
                odd.appendleft(array[l-i-1])
            if array[i] % 2 == 0:
                odd.append(array[i])
        return list(odd)

#列表
# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        res = []
        l = len(array)
        for i in range(l):
            if array[l-i-1] % 2 != 0:
                res.insert(0, array[l-i-1])
            if array[i] % 2 == 0:
                res.append(array[i])
        return res