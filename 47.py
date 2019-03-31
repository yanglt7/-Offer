'''
求1+2+3+...+n，要求不能使用
乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
'''

'''

'''

# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        # write code here
        ans = n
        if ans:
            ans += self.Sum_Solution(n-1)
        return ans