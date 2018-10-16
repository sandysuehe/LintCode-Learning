#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-15 14:47:04
# File Name: linked-list-cycle.py
# Description: 
#########################################################################
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head):
        # write your code here
        if head is None:    		
            return False		
        p1 = head		
        p2 = head		
        while True:
            if p1.next is not None:
                p1=p1.next.next
                p2=p2.next
                if p1 is None or p2 is None:
                    return False
                elif p1 == p2:
                    return True
            else:
                return False
        return False
# vim: set noexpandtab ts=4 sts=4 sw=4 :
