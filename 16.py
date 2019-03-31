'''
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
'''

# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        flag = 0
        result = 1
        if base == 0:
            return False
        if exponent < 1:
            flag = 1
        for i in range(abs(exponent)):
            result *= base
        if flag:
            result = 1 / result
        return result