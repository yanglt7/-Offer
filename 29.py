'''
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
'''

'''
我们可以先创建一个大小为k的数据容器来存储最小的k个数字，
接下来我们每次从输入的n个整数中的n个整数中读入一个数。
如果容器中已有的数字少于k个，则直接把这次读入的整数放入容器之中；
如果容器已经有k个数字了，也就是容器满了，此时我们不能再插入新的数字而只能替换已有的数字。
找出这已有的k个数中的最大值，然后拿这次待插入的整数和最大值进行比较。
如果待插入的值比当前已有的最大值小，则用这个数替换当前已有的最大值；
如果待插入的值比当前已有的最大值还要大，那么这个数不可能是最小的k个整数之一，于是我们可以抛弃这个整数。

因此当容器满了之后，我们要做3件事情：
一是在k个整数中找到最大数；
二是有可能在这个容器中删除最大数；
三是有可能要插入一个新的数字。
如果用一个二叉树来实现这个数据容器，那么我们在O(logk)时间内实现这三步操作。
因此对于n个输入数字而言，总的时间效率就是O(nlogk)。
'''

# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if len(tinput) < k:
            return []
        tmp = sorted(tinput[:k])
        for each in tinput[k:]:
            index = k - 1
            flag = False
            while index >= 0 and tmp[index] > each:
                index -= 1
                flag = True
            if flag == True:
                tmp.insert(index+1, each)
                tmp.pop()
        return tmp

