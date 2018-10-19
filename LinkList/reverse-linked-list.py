#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-22 13:11:51
# File Name: reverse-linked-list.py
# Description: 翻转链表 
# LintCode: https://www.lintcode.com/problem/reverse-linked-list/
#########################################################################
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse(self, head):
        if not head or not head.next:
            return head

        p = None
        while head:
            temp = head.next
            head.next = p
            p = head
            head = temp

        return p 
