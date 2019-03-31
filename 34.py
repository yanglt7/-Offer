'''
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,
并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
'''

'''

'''

# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        length = len(s)
        if length == 0:
            return -1
        item = {}
        for i in range(length):
            if s[i] not in item.keys():
                item[s[i]] = 1
            else:
                item[s[i]] += 1
        for i in range(length):
            if item[s[i]] == 1:
                return i
        return -1