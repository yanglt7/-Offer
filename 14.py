'''
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''

# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        cnt = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            cnt += 1
            n = n & (n-1)
        return cnt