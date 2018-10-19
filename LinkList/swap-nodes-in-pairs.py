#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-22 13:11:51
# File Name: swap-nodes-in-pairs.py
# Description: 两两交换链表中的节点
# LintCode: https://www.lintcode.com/problem/swap-nodes-in-pairs/
#########################################################################
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        # write your code here
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head

        p = dummy

        while p.next and p.next.next:
            tmp = p.next.next
            p.next.next = temp.next
            tmp.next = p.next
            p.next = tmp
            p = p.next.next

        return dummy.next
