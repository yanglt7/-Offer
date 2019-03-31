'''
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
'''

'''
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead == None
            return None
        meetingnode = self.MeetingNode(pHead)
        if meetingnode == None:
            return None
        nodeslop = 1
        node1 = meetingnode
        while node1.next != meetingnode:
            node1 = node1.next
            nodeslop += 1
        node1 = pHead
        for _ in range(nodeslop):
            node1 = node1.next
        node2 = pHead
        while node1 != node2:
            node1 = node1.next
            node2 = node2.next
        return node1
    def MeetingNode(self, pHead):
        slow = pHead.next
        if slow == None:
            return None
        fast = slow.next
        while fast != None and slow != None:
            if slow == fast:
                return fast
            slow = slow.next
            fast = fast.next
            if fast != None:
                fast = fast.next
        return None