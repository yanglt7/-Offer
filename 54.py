'''
请实现一个函数用来找出字符流中第一个只出现一次的字符。
例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
'''

'''
'''

# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.s = ''
        self.count = {}

    def FirstAppearingOnce(self):
        # write code here
        length = len(self.s)
        for i in range(length):
            if self.count[self.s[i]] == 1:
                return self.s[i]
        return '#'
    def Insert(self, char):
        # write code here
        self.s += char
        if char not in self.count:
            self.count[char] = 1
        else:
            self.count[char] += 1