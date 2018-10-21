#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-15 10:27:32
# File Name: addTwoNumbers.py
# Description: 链表求和 
# LintCode: https://www.lintcode.com/problem/add-two-numbers/
#########################################################################
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        
        dummy = ListNode(-1)
        p = dummy
        flag = 0

        while l1 and l2:
            val = (l1.val + l2.val + flag) % 10
            flag = (l1.val + l2.val + flag) / 10
            p.next = ListNode(val)
            l1 = l1.next
            l2 = l2.next
            p = p.next
        if l2:
            while l2:
                val = (l2.val + flag) % 10
                flag = (l2.val + flag) / 10
                p.next = ListNode(val)
                l2 = l2.next
                p = p.next
        if l1:
            while l1:
                val = (l1.val + flag) % 10
                flag = (l1.val + flag) / 10
                p.next = ListNode(val)
                l1 = l1.next
                p = p.next
        if flag == 1:
            p.next = ListNode(1)
        return dummy.next

# vim: set noexpandtab ts=4 sts=4 sw=4 :
