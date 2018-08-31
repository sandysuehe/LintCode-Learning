#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (hexue@4paradigm.com)
#########################################################################
# Created Time: 2018-08-28 15:25:59
# File Name: plusOneLink.py
# Description: 
#########################################################################
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def plusOne(self, head):
        cur = head
        stack = []
        while cur:
            stack.append(cur)
            cur = cur.next

        flag = 1
        while len(stack) > 0 and flag == 1:
            node = stack.pop()
            val = node.val + flag
            node.val = val % 10
            flag = val / 10

        if flag == 1:
            new_node = ListNode(1)
            new_node.next = head
            head = new_node
        return head

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3
obj = Solution()
print obj.plusOne(node1)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
