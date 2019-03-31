'''
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
'''

'''

'''

# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        max = 0x7fffffff
        mask = 0xffffffff
        while num2 != 0:
            num1, num2 = (num1 ^ num2), ((num1 & num2) << 1)
            num1 = num1 & mask
            num2 = num2 & mask
        return num1 if num1 <= max else ~(num1 ^ mask)