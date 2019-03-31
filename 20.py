'''
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
'''

'''
首先第一步 复制原来的链表，顺次连接形成新链表
第二步，利用原节点的random指向，来用复制的相应节点的random
最后一步，将复制好的链表拆分出来，或者说将 偶数位的节点重新拆分合成新的链表，得到的就是复制的链表
'''

# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return pHead
        cloNode = pHead
        while cloNode:
            node = RandomListNode(cloNode.label)
            node.next = cloNode.next
            cloNode.next = node
            cloNode = node.next
        cloNode = pHead
        while cloNode:
            node = cloNode.next
            if cloNode.random:
                node.random = cloNode.random.next
                cloNode = node.next
        cloNode = pHead
        pHead = pHead.next
        while cloNode.next:
            node = cloNode.next
            cloNode.next = node.next
            cloNode = node